# AI-ENG-001 Pilot Runtime Implementation Evidence

Status: `Implementation complete / deployment pending`
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

Local implementation validation:

```text
PYTHONPATH=. python3 -m unittest discover -s tests -v
Ran 4 tests
OK
```

Additional local validation:

- Python modules compiled with `py_compile`;
- macOS deployment scripts passed `bash -n` syntax validation.

Independent GitHub Actions validation:

- workflow: `AI-ENG-001 CI`;
- run: `33299430866`;
- head: `d77e0f32d19e417b1cb556aad185845a8a1e72c3`;
- result: `completed / success`.

The test suite uses a deterministic fake coding executor to prove runner mechanics without pretending that a model's engineering quality was tested.

Not yet evidenced:

- execution against the Owner's actual OpenCode installation;
- launchd operation on the Mac mini;
- a real product task through the end-to-end pilot;
- runtime/model replacement;
- measured Owner-time reduction;
- actual provider/tool cost;
- branch push/PR behavior in the Owner environment.

Those belong to AC-605, AC-606 and AC-607 and must not be inferred from implementation PASS.
