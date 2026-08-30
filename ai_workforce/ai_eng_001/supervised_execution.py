from __future__ import annotations

import json
import os
import re
import signal
import subprocess
import tempfile
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from .core import AgentError, Config, execute_task


_INLINE_CONFIG_ENV = "OPENCODE_CONFIG_CONTENT"
_VERSION_RE = re.compile(r"(?<!\d)(\d+)(?:\.\d+)+")


class SupervisorSignalGuard:
    """Translate SIGINT/SIGTERM into KeyboardInterrupt so core can clean its executor group."""

    def __init__(self) -> None:
        self.signum: int | None = None
        self._previous: dict[int, object] = {}

    def _handle(self, signum: int, _frame: object) -> None:
        self.signum = signum
        raise KeyboardInterrupt

    def __enter__(self) -> "SupervisorSignalGuard":
        for sig in (signal.SIGINT, signal.SIGTERM):
            self._previous[sig] = signal.getsignal(sig)
            signal.signal(sig, self._handle)
        return self

    def __exit__(self, _exc_type: object, _exc: object, _tb: object) -> None:
        for sig, handler in self._previous.items():
            signal.signal(sig, handler)


def _broad_external_roots() -> set[Path]:
    home = Path.home().resolve()
    roots = {Path("/").resolve(), home}
    for candidate in (Path("/tmp"), Path("/private/tmp"), home / "Desktop", home / "Documents"):
        roots.add(candidate.resolve(strict=False))
    return roots


def external_directories_from_task(task_path: Path) -> list[Path]:
    raw = json.loads(task_path.read_text(encoding="utf-8"))
    value = raw.get("external_directories", [])
    if value is None:
        value = []
    if not isinstance(value, list):
        raise AgentError("external_directories must be a JSON list")

    denied = _broad_external_roots()
    resolved: list[Path] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise AgentError("external_directories entries must be non-empty strings")
        expanded = Path(os.path.expandvars(item.strip())).expanduser()
        if not expanded.is_absolute():
            raise AgentError(f"external directory must be absolute: {item}")
        path = expanded.resolve(strict=False)
        if path in denied or len(path.parts) < 3:
            raise AgentError(f"external directory is too broad: {path}")
        if path not in resolved:
            resolved.append(path)
    return resolved


def opencode_external_directory_config(paths: list[Path], major_version: int) -> dict[str, object]:
    if major_version >= 2:
        return {
            "permissions": [
                {"action": "external_directory", "resource": f"{path}/*", "effect": "allow"}
                for path in paths
            ]
        }
    return {
        "permission": {
            "external_directory": {f"{path}/**": "allow" for path in paths}
        }
    }


def detect_opencode_major(config: Config) -> int:
    if not config.executor_cmd:
        raise AgentError("executor_cmd is empty")
    executable = config.executor_cmd[0]
    if Path(executable).name != "opencode":
        raise AgentError("external_directories are supported only with the OpenCode executor")
    try:
        result = subprocess.run(
            [executable, "--version"],
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise AgentError(f"cannot determine OpenCode version: {exc}") from exc
    text = (result.stdout + "\n" + result.stderr).strip()
    match = _VERSION_RE.search(text)
    if result.returncode != 0 or not match:
        raise AgentError(f"cannot determine OpenCode version from: {text or '<empty>'}")
    return int(match.group(1))


@contextmanager
def opencode_external_environment(task_path: Path, config: Config) -> Iterator[list[Path]]:
    paths = external_directories_from_task(task_path)
    previous = os.environ.get(_INLINE_CONFIG_ENV)
    if not paths:
        yield []
        return
    if previous:
        raise AgentError(
            "external_directories cannot be combined with a pre-existing OPENCODE_CONFIG_CONTENT; "
            "merge the policy explicitly instead of overriding it implicitly"
        )

    major = detect_opencode_major(config)
    os.environ[_INLINE_CONFIG_ENV] = json.dumps(
        opencode_external_directory_config(paths, major), ensure_ascii=False, separators=(",", ":")
    )
    try:
        yield paths
    finally:
        if previous is None:
            os.environ.pop(_INLINE_CONFIG_ENV, None)
        else:
            os.environ[_INLINE_CONFIG_ENV] = previous


@contextmanager
def prepared_task(task_path: Path, config: Config, paths: list[Path]) -> Iterator[Path]:
    if not paths:
        yield task_path
        return

    raw = json.loads(task_path.read_text(encoding="utf-8"))
    original_objective = str(raw.get("objective", "")).rstrip()
    boundary = "\n".join(f"- {path}" for path in paths)
    raw["objective"] = (
        original_objective
        + "\n\nSUPERVISOR FILESYSTEM BOUNDARY:\n"
        + "External filesystem access is authorized only inside these exact declared directories:\n"
        + boundary
        + "\nDo not access any other external directory. This permission does not expand business, customer, Git, "
        + "secret, deployment, release, or approval authority."
    )
    raw["external_directories"] = [str(path) for path in paths]

    prepared_dir = config.state_dir / "prepared"
    prepared_dir.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=f"-{raw.get('id', 'task')}.json",
        prefix="ai-eng-001-",
        dir=prepared_dir,
        delete=False,
    )
    prepared = Path(handle.name)
    try:
        with handle:
            json.dump(raw, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        yield prepared
    finally:
        prepared.unlink(missing_ok=True)


def _annotate_report(config: Config, result: dict[str, object], paths: list[Path], signum: int | None) -> None:
    result["external_directories"] = [str(path) for path in paths]
    result["supervisor_signal"] = signum
    run_id = result.get("run_id")
    if not isinstance(run_id, str):
        return
    run_dir = config.state_dir / "runs" / run_id
    report_path = run_dir / "report.json"
    if report_path.exists():
        report = json.loads(report_path.read_text(encoding="utf-8"))
        report["external_directories"] = [str(path) for path in paths]
        report["supervisor_signal"] = signum
        report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown = run_dir / "report.md"
    if markdown.exists():
        with markdown.open("a", encoding="utf-8") as fh:
            fh.write("\n## Supervised filesystem boundary\n")
            if paths:
                for path in paths:
                    fh.write(f"- external directory: `{path}`\n")
            else:
                fh.write("- no external directories authorized\n")
            if signum is not None:
                fh.write(f"- supervisor signal handled: `{signum}`\n")


def _execute_with_guard(task_path: Path, config: Config, guard: SupervisorSignalGuard) -> dict[str, object]:
    with opencode_external_environment(task_path, config) as paths:
        with prepared_task(task_path, config, paths) as prepared:
            result = execute_task(prepared, config)
    _annotate_report(config, result, paths, guard.signum)
    return result


def execute_task_supervised(task_path: Path, config: Config) -> dict[str, object]:
    with SupervisorSignalGuard() as guard:
        result = _execute_with_guard(task_path, config, guard)
    return result


def watch_supervised(config: Config) -> None:
    inbox = config.state_dir / "inbox"
    processing = config.state_dir / "processing"
    archive = config.state_dir / "archive"
    for path in (inbox, processing, archive):
        path.mkdir(parents=True, exist_ok=True)

    with SupervisorSignalGuard() as guard:
        while True:
            for task_file in sorted(inbox.glob("*.json")):
                claimed = processing / task_file.name
                try:
                    task_file.replace(claimed)
                except FileNotFoundError:
                    continue
                result = _execute_with_guard(claimed, config, guard)
                state = str(result.get("state", "blocked")).lower()
                claimed.replace(archive / f"{claimed.stem}.{state}.json")
                if guard.signum is not None:
                    return
            try:
                time.sleep(config.watch_interval_seconds)
            except KeyboardInterrupt:
                return
