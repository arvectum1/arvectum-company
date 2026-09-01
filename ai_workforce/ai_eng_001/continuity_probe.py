from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .core import Config, execute_task

PRINCIPAL_ID = "AI-ENG-001"
POSITION_ID = "POS-004"
PASS_MARKER = "AC606_CONTINUITY_PROBE_PASS"


def _run_git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        text=True,
        capture_output=True,
    )
    return completed.stdout.strip()


def _make_repository(root: Path) -> Path:
    repo = root / "target-repo"
    repo.mkdir()
    _run_git(repo, "init")
    _run_git(repo, "config", "user.email", "continuity-probe@example.invalid")
    _run_git(repo, "config", "user.name", "AC-606 Continuity Probe")
    (repo / "baseline.txt").write_text("stable-baseline\n", encoding="utf-8")
    _run_git(repo, "add", "baseline.txt")
    _run_git(repo, "commit", "-m", "continuity baseline")
    return repo


def _make_task(root: Path, repo: Path) -> Path:
    task = root / "task.json"
    task.write_text(
        json.dumps(
            {
                "id": "AC606-CONTINUITY-PROBE",
                "repository": str(repo),
                "objective": "Create continuity.txt containing exactly 'replacement-executor'.",
                "acceptance": ["continuity.txt contains the replacement-executor marker"],
                "test_commands": ["grep -q '^replacement-executor$' continuity.txt"],
                "allowed_paths": ["continuity.txt"],
                "forbidden_paths": [],
                "requires_owner_decision": False,
                "external_customer_effect": False,
                "material_spend": False,
                "requires_raw_secret": False,
                "changes_company_product_os_boundary": False,
                "changes_scope_or_commitment": False,
                "requires_changes": True,
                "timeout_seconds": 60,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return task


def _write_executor(path: Path, body: str) -> Path:
    path.write_text("#!/bin/sh\nset -eu\n" + body, encoding="utf-8")
    path.chmod(0o755)
    return path


def run_continuity_probe(root: Path | None = None) -> dict[str, Any]:
    """Prove fail-closed handoff and explicit executor replacement.

    The first executor fails without producing a promotable result. A human/owner
    decision is then represented by explicitly selecting a different executor
    configuration and resubmitting the exact same bounded task. There is no
    automatic failover and no authority expansion.
    """

    owned_tmp: tempfile.TemporaryDirectory[str] | None = None
    if root is None:
        owned_tmp = tempfile.TemporaryDirectory(prefix="ac606-continuity-")
        root = Path(owned_tmp.name)
    else:
        root.mkdir(parents=True, exist_ok=True)

    try:
        repo = _make_repository(root)
        task = _make_task(root, repo)
        primary = _write_executor(root / "primary-executor.sh", "exit 17\n")
        replacement = _write_executor(
            root / "replacement-executor.sh",
            "printf 'replacement-executor\\n' > continuity.txt\n",
        )

        baseline = _run_git(repo, "rev-parse", "HEAD")

        primary_result = execute_task(
            task,
            Config(state_dir=root / "state-primary", executor_cmd=[str(primary)]),
        )
        after_primary_head = _run_git(repo, "rev-parse", "HEAD")
        after_primary_status = _run_git(repo, "status", "--porcelain")

        replacement_result = execute_task(
            task,
            Config(state_dir=root / "state-replacement", executor_cmd=[str(replacement)]),
        )
        after_replacement_head = _run_git(repo, "rev-parse", "HEAD")
        after_replacement_status = _run_git(repo, "status", "--porcelain")

        replacement_worktree = Path(str(replacement_result.get("worktree", "")))
        replacement_worktree_head = _run_git(replacement_worktree, "rev-parse", "HEAD")
        replacement_run_dir = root / "state-replacement" / "runs" / str(replacement_result["run_id"])
        approval_record_exists = (replacement_run_dir / "approval.json").exists()

        invariants = {
            "primary_failed_closed": primary_result.get("state") == "BLOCKED",
            "primary_nonzero_classified": primary_result.get("executor_termination_reason")
            == "executor_nonzero_exit",
            "source_head_unchanged_after_primary": after_primary_head == baseline,
            "source_clean_after_primary": after_primary_status == "",
            "replacement_ready_for_owner": replacement_result.get("state") == "READY_FOR_OWNER",
            "replacement_changed_only_allowed_path": replacement_result.get("changed_paths")
            == ["continuity.txt"],
            "replacement_baseline_preserved": replacement_result.get("baseline_sha") == baseline,
            "replacement_worktree_uncommitted": replacement_worktree_head == baseline,
            "source_head_unchanged_after_replacement": after_replacement_head == baseline,
            "source_clean_after_replacement": after_replacement_status == "",
            "no_automatic_approval_or_commit": not approval_record_exists,
        }
        passed = all(invariants.values())

        result: dict[str, Any] = {
            "marker": PASS_MARKER if passed else "AC606_CONTINUITY_PROBE_FAIL",
            "status": "PASS" if passed else "FAIL",
            "principal": PRINCIPAL_ID,
            "position": POSITION_ID,
            "task_id": "AC606-CONTINUITY-PROBE",
            "baseline_sha": baseline,
            "automatic_failover": False,
            "owner_recovery_boundary": "explicit executor replacement after failed-closed primary run",
            "authority_expanded": False,
            "primary": {
                "state": primary_result.get("state"),
                "termination_reason": primary_result.get("executor_termination_reason"),
                "changed_paths": primary_result.get("changed_paths"),
            },
            "replacement": {
                "state": replacement_result.get("state"),
                "termination_reason": replacement_result.get("executor_termination_reason"),
                "changed_paths": replacement_result.get("changed_paths"),
                "checks": replacement_result.get("checks"),
            },
            "invariants": invariants,
        }
        return result
    finally:
        if owned_tmp is not None:
            owned_tmp.cleanup()


def main() -> int:
    result = run_continuity_probe()
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
