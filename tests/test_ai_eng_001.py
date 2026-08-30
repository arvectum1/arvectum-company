from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from ai_workforce.ai_eng_001.core import Config, Task, execute_task, path_allowed


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


class TestExecution(unittest.TestCase):
    def _git(self, cwd: Path, *args: str):
        subprocess.run(["git", *args], cwd=cwd, check=True, text=True, capture_output=True)

    def test_execute_with_fake_executor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = root / "repo"
            repo.mkdir()
            self._git(repo, "init")
            self._git(repo, "config", "user.email", "test@example.com")
            self._git(repo, "config", "user.name", "Test")
            (repo / "file.txt").write_text("old\n")
            self._git(repo, "add", "file.txt")
            self._git(repo, "commit", "-m", "init")
            fake = root / "fake-executor.sh"
            fake.write_text("#!/bin/sh\nprintf 'new\\n' > file.txt\n", encoding="utf-8")
            fake.chmod(0o755)
            task = root / "task.json"
            task.write_text(json.dumps({
                "id": "T-2", "repository": str(repo), "objective": "change file",
                "acceptance": ["file is new"], "allowed_paths": ["file.txt"],
                "test_commands": ["grep -q new file.txt"],
            }))
            cfg = Config(state_dir=root / "state", executor_cmd=[str(fake)])
            result = execute_task(task, cfg)
            self.assertEqual(result["state"], "READY_FOR_OWNER")
            self.assertIn("file.txt", result["changed_paths"])
            self.assertEqual((repo / "file.txt").read_text(), "old\n")

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
