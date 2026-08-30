# AI-ENG-001 Pilot Runtime Implementation Evidence

Status: `Implementation complete / deployment pending`
Date: `2026-08-30`

Implemented artifacts:

- `ai_workforce/ai_eng_001/core.py` — task admission, protected-boundary checks, worktree isolation, OpenCode invocation, optional manager LLM, validation, reporting, approval and watch queue;
- `ai_workforce/ai_eng_001/cli.py` — `doctor`, `run`, `enqueue`, `status`, `approve`, `watch`;
- `ai_workforce/ai_eng_001/config.example.json` — runtime config;
- `ai_workforce/ai_eng_001/task.example.json` — bounded task contract;
- `ai_workforce/ai_eng_001/com.arvectum.ai-eng-001.plist.template` — launchd service template;
- `ai_workforce/ai_eng_001/install_macos.sh` and `ai_workforce/ai_eng_001/uninstall_macos.sh` — Mac mini deployment helpers;
- `tests/test_ai_eng_001.py` — runner mechanics regression tests;
- `docs/operations/AI-ENG-001-RUNTIME.md` — operator/runtime reference.

Validation in the implementation environment:

```text
PYTHONPATH=. python3 -m unittest discover -s tests -v
Ran 4 tests
OK
```

Additional validation:

- Python modules compiled with `py_compile`;
- macOS deployment scripts passed `bash -n` syntax validation.

The test suite used a deterministic fake coding executor to prove runner mechanics without pretending that a model's engineering quality was tested.

Not yet evidenced:

- execution against the Owner's actual OpenCode installation;
- launchd operation on the Mac mini;
- a real product task through the end-to-end pilot;
- runtime/model replacement;
- measured Owner-time reduction;
- actual provider/tool cost;
- branch push/PR behavior in the Owner environment.

Those belong to AC-605, AC-606 and AC-607 and must not be inferred from implementation PASS.
