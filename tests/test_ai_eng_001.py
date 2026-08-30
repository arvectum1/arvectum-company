from __future__ import annotations

import json
import os
import subprocess
import tempfile
import time
import unittest
from pathlib import Path

from ai_workforce.ai_eng_001.core import AgentError, Config, Task, approve_run, doctor, execute_task, list_runs, path_allowed, run_streaming_executor


class TestTask(unittest.TestCase):
    def test_escalation_boundaries(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "task.json"
            p.write_text(json.dumps({
                "id": "T-1", "repository": td, "objective": "x", "acceptance": ["y"],
                "material_spend": True, "requires_raw_secret": True,
            }))
            task = Task.from_json(p)
            self.assertEqual(task.escalation_reasons(), ["material_spend", "requires_raw_secret"])

    def test_path_policy(self):
        task = Task(task_id="T-1", repository=Path("/tmp/x"), objective="x", acceptance=["y"],
                    allowed_paths=["src"], forbidden_paths=["src/secrets"])
        self.assertTrue(path_allowed("src/a.py", task)[0])
        self.assertFalse(path_allowed("docs/a.md", task)[0])
        self.assertFalse(path_allowed("src/secrets/a.txt", task)[0])

    def test_doctor_rejects_invalid_idle_timeout(self):
        result = doctor(Config(state_dir=Path("/tmp/state"), executor_cmd=["true"], executor_idle_timeout_seconds=0))
        self.assertFalse(result["ok"])
        self.assertFalse(result["checks"]["executor_idle_timeout"]["ok"])


class TestExecution(unittest.TestCase):
    def _git(self, cwd: Path, *args: str):
        subprocess.run(["git", *args], cwd=cwd, check=True, text=True, capture_output=True)

    def _repo(self, root: Path) -> Path:
        repo = root / "repo"
        repo.mkdir()
        self._git(repo, "init")
        self._git(repo, "config", "user.email", "test@example.com")
        self._git(repo, "config", "user.name", "Test")
        (repo / "file.txt").write_text("old\n")
        self._git(repo, "add", "file.txt")
        self._git(repo, "commit", "-m", "init")
        return repo

    def _task(self, root: Path, repo: Path, test_commands: list[str] | None = None, requires_changes: bool | None = None) -> Path:
        payload = {
            "id": "T-2", "repository": str(repo), "objective": "change file",
            "acceptance": ["file is new"], "allowed_paths": ["file.txt"],
            "test_commands": test_commands or [], "timeout_seconds": 60,
        }
        if requires_changes is not None:
            payload["requires_changes"] = requires_changes
        task = root / "task.json"
        task.write_text(json.dumps(payload))
        return task

    def _run_dir(self, state: Path) -> Path:
        return next((state / "runs").iterdir())

    def test_execute_with_fake_executor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self._repo(root)
            fake = root / "fake-executor.sh"
            fake.write_text("#!/bin/sh\nprintf 'stdout\\n'\nprintf 'stderr\\n' >&2\nprintf 'new\\n' > file.txt\n", encoding="utf-8")
            fake.chmod(0o755)
            task = self._task(root, repo, ["grep -q new file.txt"])
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake)])
            result = execute_task(task, cfg)
            self.assertEqual(result["state"], "READY_FOR_OWNER")
            self.assertIn("file.txt", result["changed_paths"])
            self.assertTrue(result["requires_changes"])
            self.assertEqual((repo / "file.txt").read_text(), "old\n")
            run_dir = self._run_dir(cfg.state_dir)
            self.assertIn("stdout", (run_dir / "executor.stdout.txt").read_text())
            self.assertIn("stderr", (run_dir / "executor.stderr.txt").read_text())
            status = json.loads((run_dir / "runtime-status.json").read_text())
            self.assertEqual(status["phase"], "READY_FOR_OWNER")
            self.assertTrue({
                "run_id", "task_id", "phase", "executor_pid", "started_at", "phase_started_at", "updated_at",
                "last_activity_at", "elapsed_seconds", "hard_timeout_seconds", "idle_timeout_seconds", "termination_reason",
            }.issubset(status))

    def test_idle_hang_cleans_group_and_skips_tests(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self._repo(root)
            fake = root / "silent.sh"
            child_pid = root / "child.pid"
            fake.write_text(
                f"#!/usr/bin/env python3\nimport subprocess, time\nfrom pathlib import Path\n"
                f"child = subprocess.Popen(['sleep', '30'])\nPath({str(child_pid)!r}).write_text(str(child.pid))\ntime.sleep(30)\n"
            )
            fake.chmod(0o755)
            marker = root / "SHOULD_NOT_EXIST"
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake)], executor_idle_timeout_seconds=1)
            started = time.monotonic()
            result = execute_task(self._task(root, repo, [f"touch {marker}"]), cfg)
            self.assertLess(time.monotonic() - started, 10)
            self.assertEqual(result["state"], "BLOCKED")
            self.assertEqual(result["executor_termination_reason"], "executor_idle_timeout")
            self.assertFalse(marker.exists())
            run_dir = self._run_dir(cfg.state_dir)
            self.assertTrue((run_dir / "executor.stdout.txt").exists())
            self.assertTrue((run_dir / "executor.stderr.txt").exists())
            self.assertEqual(json.loads((run_dir / "runtime-status.json").read_text())["termination_reason"], "executor_idle_timeout")
            pid = int(child_pid.read_text())
            with self.assertRaises(ProcessLookupError):
                os.kill(pid, 0)

    def test_nonzero_executor_skips_tests(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self._repo(root)
            fake = root / "nonzero.sh"
            fake.write_text("#!/bin/sh\nexit 7\n")
            fake.chmod(0o755)
            marker = root / "SHOULD_NOT_EXIST"
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake)])
            result = execute_task(self._task(root, repo, [f"touch {marker}"], requires_changes=False), cfg)
            self.assertEqual(result["state"], "BLOCKED")
            self.assertIn("executor_nonzero_exit", result["reasons"])
            self.assertEqual(result["executor_termination_reason"], "executor_nonzero_exit")
            self.assertFalse(marker.exists())

    def test_execution_only_clean_worktree_is_ready_without_changes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self._repo(root)
            fake = root / "execution-only.sh"
            fake.write_text("#!/bin/sh\nexit 0\n")
            fake.chmod(0o755)
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake)])
            result = execute_task(self._task(root, repo, ["test -f file.txt"], requires_changes=False), cfg)
            self.assertEqual(result["state"], "READY_FOR_OWNER")
            self.assertEqual(result["changed_paths"], [])
            self.assertIn({"name": "execution_only_worktree_clean", "ok": True, "count": 0}, result["checks"])
            self.assertFalse(result["requires_changes"])

    def test_execution_only_mutation_is_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self._repo(root)
            fake = root / "mutation.sh"
            fake.write_text("#!/bin/sh\nprintf 'new\\n' > file.txt\n")
            fake.chmod(0o755)
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake)])
            result = execute_task(self._task(root, repo, requires_changes=False), cfg)
            self.assertEqual(result["state"], "BLOCKED")
            self.assertIn("unexpected_changes_in_execution_only_task", result["reasons"])
            self.assertIn({"name": "execution_only_worktree_clean", "ok": False, "count": 1}, result["checks"])

    def test_execution_only_run_cannot_be_approved(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self._repo(root)
            fake = root / "execution-only.sh"
            fake.write_text("#!/bin/sh\nexit 0\n")
            fake.chmod(0o755)
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake)])
            result = execute_task(self._task(root, repo, ["true"], requires_changes=False), cfg)
            self.assertEqual(result["state"], "READY_FOR_OWNER")
            with self.assertRaisesRegex(AgentError, "execution-only run has no git changes to approve"):
                approve_run(result["run_id"], cfg)

    def test_hard_timeout_is_distinct(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fake = root / "active.sh"
            fake.write_text("#!/bin/sh\nwhile true; do printf x; sleep 0.1; done\n")
            fake.chmod(0o755)
            result = run_streaming_executor([str(fake)], root, 1, 30, root, lambda *_: None, os.environ.copy())
            self.assertEqual(result.termination_reason, "executor_hard_timeout")

    def test_list_runs_includes_in_progress_status(self):
        with tempfile.TemporaryDirectory() as td:
            state = Path(td) / "state"
            run = state / "runs" / "z-running"
            run.mkdir(parents=True)
            (run / "runtime-status.json").write_text(json.dumps({
                "run_id": "z-running", "task_id": "T-4", "phase": "EXECUTOR_RUNNING", "executor_pid": 1,
                "elapsed_seconds": 2, "last_activity_at": "now", "termination_reason": None,
            }))
            runs = list_runs(Config(state_dir=state, executor_cmd=["true"]))["runs"]
            self.assertEqual(runs[0]["state"], "EXECUTOR_RUNNING")

    def test_protected_task_fails_before_repo_access(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            task = root / "task.json"
            task.write_text(json.dumps({
                "id": "T-3", "repository": str(root / "missing"), "objective": "send to customer",
                "acceptance": ["sent"], "external_customer_effect": True,
            }))
            cfg = Config(state_dir=root / "state", executor_cmd=["missing"])
            result = execute_task(task, cfg)
            self.assertEqual(result["state"], "NEEDS_OWNER")


if __name__ == "__main__":
    unittest.main()
