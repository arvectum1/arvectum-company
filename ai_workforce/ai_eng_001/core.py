from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import selectors
import signal
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import error, request

SAFE_ID = re.compile(r"^[A-Za-z0-9._-]+$")


class AgentError(RuntimeError):
    pass


@dataclass(frozen=True)
class Task:
    task_id: str
    repository: Path
    objective: str
    acceptance: list[str]
    test_commands: list[str] = field(default_factory=list)
    base_ref: str = "HEAD"
    allowed_paths: list[str] = field(default_factory=list)
    forbidden_paths: list[str] = field(default_factory=list)
    requires_owner_decision: bool = False
    external_customer_effect: bool = False
    material_spend: bool = False
    requires_raw_secret: bool = False
    changes_company_product_os_boundary: bool = False
    changes_scope_or_commitment: bool = False
    timeout_seconds: int = 3600

    @classmethod
    def from_json(cls, path: Path) -> "Task":
        raw = json.loads(path.read_text(encoding="utf-8"))
        task_id = str(raw.get("id", "")).strip()
        if not task_id or not SAFE_ID.fullmatch(task_id):
            raise AgentError("task.id must contain only letters, digits, dot, underscore or dash")
        repo = Path(str(raw.get("repository", ""))).expanduser().resolve()
        objective = str(raw.get("objective", "")).strip()
        acceptance = [str(x).strip() for x in raw.get("acceptance", []) if str(x).strip()]
        if not objective:
            raise AgentError("task.objective is required")
        if not acceptance:
            raise AgentError("task.acceptance must contain at least one criterion")
        timeout = int(raw.get("timeout_seconds", 3600))
        if timeout < 60 or timeout > 14400:
            raise AgentError("timeout_seconds must be between 60 and 14400")
        return cls(
            task_id=task_id,
            repository=repo,
            objective=objective,
            acceptance=acceptance,
            test_commands=[str(x) for x in raw.get("test_commands", [])],
            base_ref=str(raw.get("base_ref", "HEAD")),
            allowed_paths=[str(x).strip("/") for x in raw.get("allowed_paths", [])],
            forbidden_paths=[str(x).strip("/") for x in raw.get("forbidden_paths", [])],
            requires_owner_decision=bool(raw.get("requires_owner_decision", False)),
            external_customer_effect=bool(raw.get("external_customer_effect", False)),
            material_spend=bool(raw.get("material_spend", False)),
            requires_raw_secret=bool(raw.get("requires_raw_secret", False)),
            changes_company_product_os_boundary=bool(raw.get("changes_company_product_os_boundary", False)),
            changes_scope_or_commitment=bool(raw.get("changes_scope_or_commitment", False)),
            timeout_seconds=timeout,
        )

    def escalation_reasons(self) -> list[str]:
        mapping = {
            "requires_owner_decision": self.requires_owner_decision,
            "external_customer_effect": self.external_customer_effect,
            "material_spend": self.material_spend,
            "requires_raw_secret": self.requires_raw_secret,
            "changes_company_product_os_boundary": self.changes_company_product_os_boundary,
            "changes_scope_or_commitment": self.changes_scope_or_commitment,
        }
        return [name for name, active in mapping.items() if active]


@dataclass
class Config:
    state_dir: Path
    executor_cmd: list[str]
    executor_model: str | None = None
    executor_agent: str | None = None
    llm_mode: str = "none"
    llm_base_url: str | None = None
    llm_model: str | None = None
    llm_api_key_env: str = "AI_ENG_LLM_API_KEY"
    watch_interval_seconds: int = 30
    executor_idle_timeout_seconds: int = 600

    @classmethod
    def load(cls, path: Path | None) -> "Config":
        raw: dict[str, Any] = {}
        if path:
            raw = json.loads(path.expanduser().read_text(encoding="utf-8"))
        state_dir = Path(os.path.expandvars(str(raw.get("state_dir", "~/.local/share/arvectum/ai-eng-001")))).expanduser()
        executor = raw.get("executor_cmd", ["opencode", "run"])
        if isinstance(executor, str):
            executor = shlex.split(executor)
        return cls(
            state_dir=state_dir,
            executor_cmd=[str(x) for x in executor],
            executor_model=raw.get("executor_model"),
            executor_agent=raw.get("executor_agent"),
            llm_mode=str(raw.get("llm_mode", "none")),
            llm_base_url=raw.get("llm_base_url"),
            llm_model=raw.get("llm_model"),
            llm_api_key_env=str(raw.get("llm_api_key_env", "AI_ENG_LLM_API_KEY")),
            watch_interval_seconds=int(raw.get("watch_interval_seconds", 30)),
            executor_idle_timeout_seconds=int(raw.get("executor_idle_timeout_seconds", 600)),
        )


@dataclass
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


@dataclass
class ExecutorResult(CommandResult):
    termination_reason: str | None = None


def run_command(args: list[str] | str, cwd: Path, timeout: int, shell: bool = False, env: dict[str, str] | None = None) -> CommandResult:
    cp = subprocess.run(args, cwd=str(cwd), text=True, capture_output=True, timeout=timeout, shell=shell, env=env)
    return CommandResult(cp.returncode, cp.stdout, cp.stderr)


def git(repo: Path, *args: str, timeout: int = 120) -> CommandResult:
    return run_command(["git", *args], repo, timeout)


def require_clean_repo(repo: Path) -> None:
    if not repo.is_dir():
        raise AgentError(f"not a directory: {repo}")
    inside = git(repo, "rev-parse", "--is-inside-work-tree")
    if inside.returncode != 0 or inside.stdout.strip() != "true":
        raise AgentError(f"not a git repository: {repo}")
    status = git(repo, "status", "--porcelain")
    if status.returncode != 0:
        raise AgentError(status.stderr.strip() or "git status failed")
    if status.stdout.strip():
        raise AgentError("repository is dirty; AI-ENG-001 fails closed to avoid mixing owner and agent changes")


def utcstamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_runtime_status(run_dir: Path, **status: Any) -> None:
    target = run_dir / "runtime-status.json"
    temporary = run_dir / ".runtime-status.json.tmp"
    temporary.write_text(json.dumps(status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(target)


def runtime_status(
    run_id: str,
    task: Task,
    phase: str,
    started_at: str,
    phase_started_at: str,
    started: float,
    last_activity_at: str,
    idle_timeout_seconds: int,
    executor_pid: int | None = None,
    termination_reason: str | None = None,
    executor_returncode: int | None = None,
    branch: str | None = None,
    baseline_sha: str | None = None,
    worktree: Path | None = None,
) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "task_id": task.task_id,
        "phase": phase,
        "executor_pid": executor_pid,
        "started_at": started_at,
        "phase_started_at": phase_started_at,
        "updated_at": iso_now(),
        "last_activity_at": last_activity_at,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "hard_timeout_seconds": task.timeout_seconds,
        "idle_timeout_seconds": idle_timeout_seconds,
        "termination_reason": termination_reason,
        "executor_returncode": executor_returncode,
        "branch": branch,
        "baseline_sha": baseline_sha,
        "worktree": str(worktree) if worktree else None,
    }


def policy_header() -> str:
    return """You are executing bounded engineering work for Arvectum Company as a tool of POS-004 Engineering & Release Lead.\n\nBOUNDARIES:\n- Work only on the requested objective and acceptance criteria.\n- Do not contact customers, publish releases, deploy to production, merge branches, push remotes, create external commitments, spend money, or change company/product/Arvectum OS authority boundaries.\n- Do not request, print, read or persist reusable secrets, tokens, private keys, signing material or bank credentials.\n- Do not modify git remotes or credential configuration.\n- Do not commit. The supervising runner owns promotion after human review.\n- If the task requires scope expansion, a material dependency, a secret, customer acceptance, irreversible action, or ambiguous authority, stop and explain the blocker instead of guessing.\n- Technical PASS is not customer/business acceptance.\n- Prefer minimal, reversible changes.\n- Run relevant tests and leave the worktree in a reviewable state.\n"""


def llm_plan(config: Config, task: Task) -> dict[str, Any] | None:
    if config.llm_mode == "none":
        return None
    if config.llm_mode != "openai_compatible":
        raise AgentError(f"unsupported llm_mode: {config.llm_mode}")
    if not config.llm_base_url or not config.llm_model:
        raise AgentError("llm_base_url and llm_model are required for openai_compatible mode")
    payload = {
        "model": config.llm_model,
        "temperature": 0.1,
        "messages": [
            {"role": "system", "content": policy_header() + "\nReturn a concise engineering plan. Do not invent missing facts."},
            {"role": "user", "content": json.dumps({"objective": task.objective, "acceptance": task.acceptance}, ensure_ascii=False)},
        ],
    }
    url = config.llm_base_url.rstrip("/") + "/chat/completions"
    headers = {"Content-Type": "application/json"}
    key = os.environ.get(config.llm_api_key_env)
    if key:
        headers["Authorization"] = f"Bearer {key}"
    req = request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with request.urlopen(req, timeout=90) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except (error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise AgentError(f"manager LLM request failed: {exc}") from exc
    text = data["choices"][0]["message"]["content"]
    return {"text": text, "model": config.llm_model, "base_url": config.llm_base_url}


def build_executor_prompt(task: Task, plan: dict[str, Any] | None) -> str:
    parts = [policy_header(), "\nTASK:\n", task.objective, "\n\nACCEPTANCE CRITERIA:\n"]
    parts.extend(f"- {x}\n" for x in task.acceptance)
    if task.allowed_paths:
        parts.append("\nALLOWED PATH PREFIXES:\n" + "\n".join(f"- {x}" for x in task.allowed_paths))
    if task.forbidden_paths:
        parts.append("\nFORBIDDEN PATH PREFIXES:\n" + "\n".join(f"- {x}" for x in task.forbidden_paths))
    if plan:
        parts.append("\n\nSUPERVISOR PLAN:\n" + plan["text"])
    parts.append("\n\nExecute the task now. At the end, summarize files changed, tests run, unresolved risks, and anything requiring owner decision.")
    return "".join(parts)


def changed_paths(worktree: Path) -> list[str]:
    res = git(worktree, "status", "--porcelain")
    if res.returncode != 0:
        raise AgentError(res.stderr.strip() or "git status failed")
    paths: list[str] = []
    for line in res.stdout.splitlines():
        if not line:
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path)
    return sorted(set(paths))


def path_allowed(path: str, task: Task) -> tuple[bool, str | None]:
    normalized = path.lstrip("/")
    for prefix in task.forbidden_paths:
        if normalized == prefix or normalized.startswith(prefix.rstrip("/") + "/"):
            return False, f"forbidden path changed: {path}"
    if task.allowed_paths and not any(normalized == p or normalized.startswith(p.rstrip("/") + "/") for p in task.allowed_paths):
        return False, f"change outside allowed_paths: {path}"
    return True, None


def write_report(run_dir: Path, report: dict[str, Any]) -> None:
    (run_dir / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    lines = [
        f"# AI-ENG-001 run — {report['task_id']}", "", f"State: `{report['state']}`", f"Run: `{report['run_id']}`",
        f"Repository: `{report['repository']}`", f"Worktree: `{report.get('worktree', '')}`", f"Branch: `{report.get('branch', '')}`",
        "", "## Summary", report.get("summary", ""), "", "## Changed paths",
    ]
    lines.extend(f"- `{p}`" for p in report.get("changed_paths", []))
    lines += ["", "## Checks"]
    for check in report.get("checks", []):
        lines.append(f"- `{check['name']}`: {'PASS' if check['ok'] else 'FAIL'}")
    if report.get("reasons"):
        lines += ["", "## Reasons / escalation"] + [f"- {x}" for x in report["reasons"]]
    lines += ["", "## Owner next action", report.get("owner_next_action", "Review report and worktree.")]
    (run_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def terminate_executor_group(process: subprocess.Popen[bytes], grace_seconds: float = 3.0) -> None:
    """Stop only the session created for this executor, never unrelated OpenCode processes."""
    if process.poll() is not None:
        return
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    deadline = time.monotonic() + grace_seconds
    while process.poll() is None and time.monotonic() < deadline:
        time.sleep(0.05)
    if process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass


def run_streaming_executor(
    args: list[str],
    cwd: Path,
    hard_timeout_seconds: int,
    idle_timeout_seconds: int,
    run_dir: Path,
    status_writer: Any,
    env: dict[str, str],
) -> ExecutorResult:
    if idle_timeout_seconds <= 0:
        raise AgentError("executor_idle_timeout_seconds must be greater than zero")

    stdout_path = run_dir / "executor.stdout.txt"
    stderr_path = run_dir / "executor.stderr.txt"
    started = time.monotonic()
    last_activity = started
    termination_reason: str | None = None
    stdout_chunks: list[bytes] = []
    stderr_chunks: list[bytes] = []

    with stdout_path.open("wb") as stdout_file, stderr_path.open("wb") as stderr_file:
        process = subprocess.Popen(
            args,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            start_new_session=True,
            env=env,
        )
        assert process.stdout is not None and process.stderr is not None
        selector = selectors.DefaultSelector()
        for stream, file, chunks in ((process.stdout, stdout_file, stdout_chunks), (process.stderr, stderr_file, stderr_chunks)):
            os.set_blocking(stream.fileno(), False)
            selector.register(stream, selectors.EVENT_READ, (file, chunks))
        last_heartbeat = 0.0
        try:
            while selector.get_map() or process.poll() is None:
                now = time.monotonic()
                if now - started >= hard_timeout_seconds:
                    termination_reason = "executor_hard_timeout"
                    terminate_executor_group(process)
                elif now - last_activity >= idle_timeout_seconds:
                    termination_reason = "executor_idle_timeout"
                    terminate_executor_group(process)

                # Poll frequently enough that a newly spawned executor can initialize before a short test timeout.
                events = selector.select(timeout=0.2)
                for key, _ in events:
                    stream = key.fileobj
                    file, chunks = key.data
                    try:
                        data = os.read(stream.fileno(), 65536)
                    except BlockingIOError:
                        continue
                    if data:
                        file.write(data)
                        file.flush()
                        chunks.append(data)
                        last_activity = time.monotonic()
                        status_writer(process.pid, True, termination_reason)
                    else:
                        selector.unregister(stream)
                        stream.close()

                now = time.monotonic()
                if now - last_heartbeat >= 2.0:
                    status_writer(process.pid, False, termination_reason)
                    last_heartbeat = now
                if termination_reason and process.poll() is not None and not selector.get_map():
                    break
        except KeyboardInterrupt:
            termination_reason = "supervisor_interrupted"
            terminate_executor_group(process)
        finally:
            if process.poll() is None:
                process.wait(timeout=5)
            for key in list(selector.get_map().values()):
                stream = key.fileobj
                file, chunks = key.data
                while True:
                    try:
                        data = os.read(stream.fileno(), 65536)
                    except BlockingIOError:
                        break
                    if not data:
                        break
                    file.write(data)
                    chunks.append(data)
                file.flush()
                selector.unregister(stream)
                stream.close()
            selector.close()

    return ExecutorResult(
        returncode=process.returncode if process.returncode is not None else -1,
        stdout=b"".join(stdout_chunks).decode("utf-8", errors="replace"),
        stderr=b"".join(stderr_chunks).decode("utf-8", errors="replace"),
        termination_reason=termination_reason,
    )


def execute_task(task_path: Path, config: Config) -> dict[str, Any]:
    task = Task.from_json(task_path)
    run_id = f"{utcstamp()}-{task.task_id}"
    run_dir = config.state_dir / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    (run_dir / "task.json").write_text(task_path.read_text(encoding="utf-8"), encoding="utf-8")
    started = time.monotonic()
    started_at = iso_now()
    phase_started_at = started_at
    last_activity_at = started_at

    def status(phase: str, *, pid: int | None = None, reason: str | None = None, returncode: int | None = None,
               branch: str | None = None, baseline_sha: str | None = None, worktree: Path | None = None) -> None:
        nonlocal phase_started_at
        phase_started_at = iso_now()
        write_runtime_status(run_dir, **runtime_status(
            run_id, task, phase, started_at, phase_started_at, started, last_activity_at,
            config.executor_idle_timeout_seconds, pid, reason, returncode, branch, baseline_sha, worktree,
        ))

    status("ADMISSION")

    escalation = task.escalation_reasons()
    if escalation:
        report = {
            "run_id": run_id, "task_id": task.task_id, "repository": str(task.repository), "state": "NEEDS_OWNER",
            "summary": "Task crosses a protected authority/risk boundary and was not executed.", "reasons": escalation,
            "changed_paths": [], "checks": [],
            "owner_next_action": "Resolve or explicitly re-scope the flagged boundary, then submit a new task record.",
        }
        status("NEEDS_OWNER")
        write_report(run_dir, report)
        return report

    try:
        if config.executor_idle_timeout_seconds <= 0:
            raise AgentError("executor_idle_timeout_seconds must be greater than zero")
        require_clean_repo(task.repository)
        head = git(task.repository, "rev-parse", task.base_ref)
        if head.returncode != 0:
            raise AgentError(head.stderr.strip() or f"cannot resolve base_ref {task.base_ref}")
        baseline_sha = head.stdout.strip()
        branch = f"ai-eng/{task.task_id.lower()}-{utcstamp().lower()}"
        worktree = config.state_dir / "worktrees" / run_id
        worktree.parent.mkdir(parents=True, exist_ok=True)
        add = git(task.repository, "worktree", "add", "-b", branch, str(worktree), baseline_sha, timeout=180)
        if add.returncode != 0:
            raise AgentError(add.stderr.strip() or "git worktree add failed")
        status("WORKTREE_READY", branch=branch, baseline_sha=baseline_sha, worktree=worktree)

        plan = llm_plan(config, task)
        if plan:
            (run_dir / "manager-plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
        prompt = build_executor_prompt(task, plan)
        (run_dir / "executor-prompt.txt").write_text(prompt, encoding="utf-8")

        cmd = list(config.executor_cmd)
        if config.executor_model:
            cmd += ["--model", config.executor_model]
        if config.executor_agent:
            cmd += ["--agent", config.executor_agent]
        cmd += ["--dir", str(worktree)]
        cmd += [prompt]
        env = os.environ.copy()
        env.pop(config.llm_api_key_env, None)

        def executor_status(pid: int, active: bool, reason: str | None) -> None:
            nonlocal last_activity_at
            if active:
                last_activity_at = iso_now()
            write_runtime_status(run_dir, **runtime_status(
                run_id, task, "EXECUTOR_RUNNING", started_at, phase_started_at, started, last_activity_at,
                config.executor_idle_timeout_seconds, pid, reason, None, branch, baseline_sha, worktree,
            ))

        phase_started_at = iso_now()
        last_activity_at = phase_started_at
        executor = run_streaming_executor(
            cmd, worktree, task.timeout_seconds, config.executor_idle_timeout_seconds, run_dir, executor_status, env,
        )
        duration = round(time.monotonic() - started, 3)

        paths = changed_paths(worktree)
        checks: list[dict[str, Any]] = []
        reasons: list[str] = []
        checks.append({"name": "executor_exit", "ok": executor.returncode == 0, "returncode": executor.returncode})
        for p in paths:
            ok, reason = path_allowed(p, task)
            checks.append({"name": f"path:{p}", "ok": ok})
            if reason:
                reasons.append(reason)
        if executor.termination_reason:
            reasons.append(executor.termination_reason)
        elif executor.returncode != 0:
            reasons.append("executor_nonzero_exit")
        else:
            status("POST_EXECUTOR_CHECKS", branch=branch, baseline_sha=baseline_sha, worktree=worktree)
            checks.append({"name": "changed_files_present", "ok": bool(paths), "count": len(paths)})
            if not paths:
                reasons.append("executor produced no file changes")
            diffcheck = git(worktree, "diff", "--check")
            checks.append({"name": "git_diff_check", "ok": diffcheck.returncode == 0})
            if diffcheck.returncode != 0:
                reasons.append(diffcheck.stdout.strip() or diffcheck.stderr.strip() or "git diff --check failed")
            status("TESTING", branch=branch, baseline_sha=baseline_sha, worktree=worktree)
            for index, test_cmd in enumerate(task.test_commands, 1):
                tr = run_command(test_cmd, worktree, min(task.timeout_seconds, 1800), shell=True)
                (run_dir / f"test-{index}.stdout.txt").write_text(tr.stdout, encoding="utf-8")
                (run_dir / f"test-{index}.stderr.txt").write_text(tr.stderr, encoding="utf-8")
                checks.append({"name": f"test:{test_cmd}", "ok": tr.returncode == 0, "returncode": tr.returncode})
                if tr.returncode != 0:
                    reasons.append(f"test failed: {test_cmd}")

        executor_reason = executor.termination_reason or (
            "executor_nonzero_exit" if executor.returncode != 0 else None
        )
        state = "READY_FOR_OWNER" if not executor_reason and executor.returncode == 0 and all(c["ok"] for c in checks) else "BLOCKED"
        report = {
            "run_id": run_id, "task_id": task.task_id, "repository": str(task.repository), "worktree": str(worktree),
            "branch": branch, "baseline_sha": baseline_sha, "state": state,
            "summary": "Bounded engineering execution completed and is ready for human review." if state == "READY_FOR_OWNER" else "Execution completed but one or more required checks failed.",
            "reasons": reasons, "changed_paths": paths, "checks": checks, "duration_seconds": duration,
            "executor_returncode": executor.returncode, "executor_termination_reason": executor_reason,
            "owner_next_action": (
                f"Review `{worktree}` and `{run_dir / 'report.md'}`. If acceptable, run `python3 -m ai_workforce.ai_eng_001.cli approve {shlex.quote(run_id)}` from the arvectum-company checkout."
                if state == "READY_FOR_OWNER" else "Inspect the report/logs. Correct the task or environment; do not promote this worktree."
            ),
        }
        status(state, reason=executor_reason, returncode=executor.returncode,
               branch=branch, baseline_sha=baseline_sha, worktree=worktree)
        write_report(run_dir, report)
        return report
    except (AgentError, subprocess.TimeoutExpired) as exc:
        report = {
            "run_id": run_id, "task_id": task.task_id, "repository": str(task.repository), "state": "BLOCKED",
            "summary": "Runner failed closed before a promotable result was produced.", "reasons": [str(exc)],
            "changed_paths": [], "checks": [],
            "owner_next_action": "Inspect the task/environment and submit a corrected task. Do not infer success.",
        }
        status("BLOCKED")
        write_report(run_dir, report)
        return report


def approve_run(run_id: str, config: Config, push: bool = False) -> dict[str, Any]:
    run_dir = config.state_dir / "runs" / run_id
    report_path = run_dir / "report.json"
    if not report_path.exists():
        raise AgentError(f"unknown run: {run_id}")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("state") != "READY_FOR_OWNER":
        raise AgentError(f"run is not READY_FOR_OWNER: {report.get('state')}")
    worktree = Path(report["worktree"])
    if not worktree.exists():
        raise AgentError("worktree no longer exists")
    add = git(worktree, "add", "-A")
    if add.returncode != 0:
        raise AgentError(add.stderr.strip() or "git add failed")
    msg = f"{report['task_id']} — AI-ENG-001 validated candidate"
    commit = git(worktree, "commit", "-m", msg, timeout=180)
    if commit.returncode != 0:
        raise AgentError(commit.stderr.strip() or commit.stdout.strip() or "git commit failed")
    sha = git(worktree, "rev-parse", "HEAD").stdout.strip()
    result = {"state": "APPROVED_LOCAL", "run_id": run_id, "commit_sha": sha, "branch": report["branch"], "pushed": False}
    if push:
        pushed = git(worktree, "push", "-u", "origin", report["branch"], timeout=300)
        if pushed.returncode != 0:
            raise AgentError(pushed.stderr.strip() or "git push failed")
        result["state"] = "APPROVED_PUSHED"
        result["pushed"] = True
    (run_dir / "approval.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def doctor(config: Config) -> dict[str, Any]:
    checks = {
        "python": {"ok": sys.version_info >= (3, 11), "value": sys.version.split()[0]},
        "git": {"ok": shutil.which("git") is not None, "value": shutil.which("git")},
        "executor": {"ok": shutil.which(config.executor_cmd[0]) is not None, "value": shutil.which(config.executor_cmd[0])},
        "executor_idle_timeout": {
            "ok": config.executor_idle_timeout_seconds > 0,
            "value": config.executor_idle_timeout_seconds,
        },
    }
    if config.llm_mode == "openai_compatible":
        checks["manager_llm_config"] = {
            "ok": bool(config.llm_base_url and config.llm_model),
            "value": {"base_url": config.llm_base_url, "model": config.llm_model},
        }
    return {"ok": all(c["ok"] for c in checks.values()), "checks": checks}


def enqueue_task(task_path: Path, config: Config) -> dict[str, Any]:
    task = Task.from_json(task_path)
    inbox = config.state_dir / "inbox"
    inbox.mkdir(parents=True, exist_ok=True)
    target = inbox / f"{utcstamp()}-{task.task_id}.json"
    target.write_text(task_path.read_text(encoding="utf-8"), encoding="utf-8")
    return {"state": "QUEUED", "task_id": task.task_id, "path": str(target)}


def list_runs(config: Config, limit: int = 20) -> dict[str, Any]:
    runs_dir = config.state_dir / "runs"
    items: list[dict[str, Any]] = []
    if runs_dir.exists():
        for run_dir in sorted((p for p in runs_dir.iterdir() if p.is_dir()), reverse=True)[:limit]:
            report_path = run_dir / "report.json"
            status_path = run_dir / "runtime-status.json"
            try:
                if report_path.exists():
                    report = json.loads(report_path.read_text(encoding="utf-8"))
                    items.append({
                        "run_id": report.get("run_id"), "task_id": report.get("task_id"), "state": report.get("state"),
                        "branch": report.get("branch"), "report": str(report_path),
                    })
                elif status_path.exists():
                    status = json.loads(status_path.read_text(encoding="utf-8"))
                    items.append({
                        "run_id": status.get("run_id"), "task_id": status.get("task_id"),
                        "state": status.get("phase"), "phase": status.get("phase"),
                        "executor_pid": status.get("executor_pid"), "elapsed_seconds": status.get("elapsed_seconds"),
                        "last_activity_at": status.get("last_activity_at"),
                        "termination_reason": status.get("termination_reason"), "report": None,
                    })
            except (OSError, json.JSONDecodeError):
                continue
    return {"runs": items}


def watch(config: Config) -> None:
    inbox = config.state_dir / "inbox"
    processing = config.state_dir / "processing"
    archive = config.state_dir / "archive"
    for p in (inbox, processing, archive):
        p.mkdir(parents=True, exist_ok=True)
    while True:
        for task_file in sorted(inbox.glob("*.json")):
            claimed = processing / task_file.name
            try:
                task_file.replace(claimed)
            except FileNotFoundError:
                continue
            report = execute_task(claimed, config)
            claimed.replace(archive / f"{claimed.stem}.{report['state'].lower()}.json")
        time.sleep(config.watch_interval_seconds)
