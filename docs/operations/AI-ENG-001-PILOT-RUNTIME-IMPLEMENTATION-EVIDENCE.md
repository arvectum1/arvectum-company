# AI-ENG-001 Pilot Runtime Implementation Evidence

Status: `Implementation complete / Mac mini deployment PASS / real task pending`
Date: `2026-08-30`

Implemented artifacts:

- `ai_workforce/ai_eng_001/core.py` — task admission, protected-boundary checks, worktree isolation, OpenCode invocation, optional manager LLM, validation, reporting, approval and watch queue;
- `ai_workforce/ai_eng_001/cli.py` — `doctor`, `run`, `enqueue`, `status`, `approve`, `watch`;
- `ai_workforce/ai_eng_001/config.example.json` — runtime config;
- `ai_workforce/ai_eng_001/task.example.json` — bounded task contract;
- `ai_workforce/ai_eng_001/com.arvectum.ai-eng-001.plist.template` — launchd service template;
- `ai_workforce/ai_eng_001/install_macos.sh`, `uninstall_macos.sh`, `smoke_test.sh` — Mac mini deployment helpers;
- `tests/test_ai_eng_001.py` — runner mechanics regression tests;
- `.github/workflows/ai-eng-001-ci.yml` — independent CI validation;
- `docs/operations/AI-ENG-001-RUNTIME.md` — operator/runtime reference.

Initial implementation validation:

```text
PYTHONPATH=. python3 -m unittest discover -s tests -v
Ran 4 tests
OK
```

Additional initial validation:

- Python modules compiled with `py_compile`;
- macOS deployment scripts passed `bash -n` syntax validation;
- GitHub Actions run `33299430866`: `completed / success`.

## Mac mini deployment evidence

The Owner-controlled Mac mini deployment has now been completed and recorded in:

`docs/operations/AC-605-MAC-MINI-DEPLOYMENT-EVIDENCE.md`.

Observed local deployment evidence reported from that environment:

- AI-ENG-001 running on the Mac mini;
- `py_compile`: PASS;
- targeted tests: `4/4 PASS`;
- synthetic smoke: `READY_FOR_OWNER`;
- smoke checks: `5/5 PASS`;
- no real product task executed;
- no autonomous merge/release/deploy/customer effect.

The deployment uncovered one portability defect: OpenCode execution lacked an explicit worktree directory. The minimal fix added:

```python
cmd += ["--dir", str(worktree)]
```

Remote review verified a one-file/one-line diff. Pull request `#1` passed `AI-ENG-001 CI` run `33301128677` and was promoted to canonical `main` in merge commit:

`6e8df32168bc665b8aac288a5b828379122918d3`.

The test suite and synthetic smoke prove runtime mechanics only. They do not prove model engineering quality on real product work, customer acceptance or positive economics.

Not yet evidenced:

- one real low-risk product task through the end-to-end supervised pilot;
- runtime/model replacement;
- measured Owner-time reduction;
- actual provider/tool cost under real workload;
- sustained value/rework/escalation behavior across real tasks.

Those belong to the remaining AC-605 evidence and AC-606/AC-607. They must not be inferred from deployment PASS.
