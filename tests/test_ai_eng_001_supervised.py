from __future__ import annotations

import json
import os
import signal
import subprocess
import tempfile
import threading
import time
import unittest
from pathlib import Path

from ai_workforce.ai_eng_001.core import AgentError, Config
from ai_workforce.ai_eng_001.supervised_execution import (
    execute_task_supervised,
    external_directories_from_task,
    opencode_external_directory_config,
)


class TestSupervisedExecution(unittest.TestCase):
    def _git(self, cwd: Path, *args: str) -> None:
        subprocess.run(["git", *args], cwd=cwd, check=True, text=True, capture_output=True)

    def _repo(self, root: Path) -> Path:
        repo = root / "repo"
        repo.mkdir()
        self._git(repo, "init")
        self._git(repo, "config", "user.email", "test@example.com")
        self._git(repo, "config", "user.name", "Test")
        (repo / "file.txt").write_text("old\n", encoding="utf-8")
        self._git(repo, "add", "file.txt")
        self._git(repo, "commit", "-m", "init")
        return repo

    def _task(self, root: Path, repo: Path, **extra: object) -> Path:
        payload: dict[str, object] = {
            "id": "SUPERVISED-1",
            "repository": str(repo),
            "objective": "Perform a bounded execution-only check.",
            "acceptance": ["executor exits successfully"],
            "requires_changes": False,
            "timeout_seconds": 60,
        }
        payload.update(extra)
        task = root / "task.json"
        task.write_text(json.dumps(payload), encoding="utf-8")
        return task

    def test_external_directory_config_supports_v1_and_v2(self) -> None:
        path = Path("/private/tmp/example")
        self.assertEqual(
            opencode_external_directory_config([path], 1),
            {"permission": {"external_directory": {"/private/tmp/example/**": "allow"}}},
        )
        self.assertEqual(
            opencode_external_directory_config([path], 2),
            {
                "permissions": [
                    {"action": "external_directory", "resource": "/private/tmp/example/*", "effect": "allow"}
                ]
            },
        )

    def test_external_directory_rejects_broad_temp_root(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            task = root / "task.json"
            task.write_text(json.dumps({
                "id": "T",
                "repository": td,
                "objective": "x",
                "acceptance": ["y"],
                "external_directories": ["/private/tmp"],
            }), encoding="utf-8")
            with self.assertRaisesRegex(AgentError, "too broad"):
                external_directories_from_task(task)

    def test_declared_external_directory_is_injected_into_opencode_only(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self._repo(root)
            external = root / "external" / "candidate"
            external.mkdir(parents=True)
            capture = root / "captured-config.json"
            fake = root / "opencode"
            fake.write_text(
                "#!/usr/bin/env python3\n"
                "import os, sys\n"
                "from pathlib import Path\n"
                "if '--version' in sys.argv:\n"
                "    print('1.9.0')\n"
                "    raise SystemExit(0)\n"
                f"Path({str(capture)!r}).write_text(os.environ.get('OPENCODE_CONFIG_CONTENT', ''), encoding='utf-8')\n",
                encoding="utf-8",
            )
            fake.chmod(0o755)
            task = self._task(root, repo, external_directories=[str(external)])
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake), "run"])

            result = execute_task_supervised(task, cfg)

            self.assertEqual(result["state"], "READY_FOR_OWNER")
            self.assertEqual(result["external_directories"], [str(external.resolve())])
            policy = json.loads(capture.read_text(encoding="utf-8"))
            self.assertEqual(
                policy["permission"]["external_directory"],
                {f"{external.resolve()}/**": "allow"},
            )
            self.assertEqual(subprocess.run(["git", "status", "--porcelain"], cwd=repo, text=True, capture_output=True).stdout, "")

    def test_sigterm_is_translated_to_bounded_executor_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self._repo(root)
            child_pid_file = root / "child.pid"
            fake = root / "sleeping-executor"
            fake.write_text(
                "#!/usr/bin/env python3\n"
                "import subprocess, time\n"
                "from pathlib import Path\n"
                "child = subprocess.Popen(['sleep', '30'])\n"
                f"Path({str(child_pid_file)!r}).write_text(str(child.pid), encoding='utf-8')\n"
                "time.sleep(30)\n",
                encoding="utf-8",
            )
            fake.chmod(0o755)
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake)], executor_idle_timeout_seconds=30)
            task = self._task(root, repo)
            timer = threading.Timer(1.0, lambda: os.kill(os.getpid(), signal.SIGTERM))
            timer.start()
            try:
                started = time.monotonic()
                result = execute_task_supervised(task, cfg)
            finally:
                timer.cancel()

            self.assertLess(time.monotonic() - started, 10)
            self.assertEqual(result["state"], "BLOCKED")
            self.assertEqual(result["executor_termination_reason"], "supervisor_interrupted")
            self.assertEqual(result["supervisor_signal"], signal.SIGTERM)
            self.assertTrue(child_pid_file.exists())
            child_pid = int(child_pid_file.read_text(encoding="utf-8"))
            time.sleep(0.1)
            with self.assertRaises(ProcessLookupError):
                os.kill(child_pid, 0)


if __name__ == "__main__":
    unittest.main()
