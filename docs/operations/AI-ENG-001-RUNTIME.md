# AI-ENG-001 Runtime Reference

Status: `Pilot-ready implementation`
Date: `2026-08-30`
Position: `POS-004 — Engineering & Release Lead`
Principal: `AI-ENG-001`

## Purpose

`AI-ENG-001` is a bounded pilot runtime for `POS-004`. It reduces manual relay between the Owner/planning layer and coding executor while preserving explicit human promotion and protected decision gates.

## Main flow

```text
Task JSON
  -> admission / protected-boundary check
  -> clean repository check
  -> isolated worktree + ai-eng branch
  -> optional manager-LLM plan
  -> OpenCode non-interactive execution
  -> changed-path + diff + declared-test checks
  -> READY_FOR_OWNER | NEEDS_OWNER | BLOCKED
  -> explicit Owner approve
  -> optional explicit Owner --push
```

No runtime state implies customer acceptance, production readiness or business approval.

## Task contract

Required fields: `id`, `repository`, `objective`, and a non-empty `acceptance` list.

Operational fields: `base_ref`, `test_commands`, `allowed_paths`, `forbidden_paths`, and `timeout_seconds`.

Protected flags, all of which must be false for the autonomous pilot path:

- `requires_owner_decision`;
- `external_customer_effect`;
- `material_spend`;
- `requires_raw_secret`;
- `changes_company_product_os_boundary`;
- `changes_scope_or_commitment`.

If a protected flag is true, the runner returns `NEEDS_OWNER` before engineering execution. It must not silently reinterpret the task as safe.

## Commands

```bash
python3 -m ai_workforce.ai_eng_001.cli --config PATH doctor
python3 -m ai_workforce.ai_eng_001.cli --config PATH run TASK.json
python3 -m ai_workforce.ai_eng_001.cli --config PATH enqueue TASK.json
python3 -m ai_workforce.ai_eng_001.cli --config PATH status
python3 -m ai_workforce.ai_eng_001.cli --config PATH approve RUN_ID
python3 -m ai_workforce.ai_eng_001.cli --config PATH approve RUN_ID --push
python3 -m ai_workforce.ai_eng_001.cli --config PATH watch
```

`--push` is intentionally a separate explicit Owner command. The pilot never merges, releases or deploys automatically.

## OpenCode integration

Default executor command is `opencode run`. The runtime appends the bounded engineering prompt. Optional `executor_model` and `executor_agent` config values are passed as OpenCode `--model` and `--agent` flags.

OpenCode owns the coding-provider/model configuration.

## Manager LLM

Default: disabled. A separate manager LLM is not required for the first proof because OpenCode already provides coding intelligence; the Python runtime supplies persistent admission, isolation, evidence and escalation mechanics.

If enabled, `llm_mode=openai_compatible` sends a planning request to `${llm_base_url}/chat/completions`. This is compatible with a local OpenAI-compatible server such as a llama.cpp server or a compatible remote provider. A key, when needed, is read from the environment named by `llm_api_key_env` and is removed from the environment passed to the coding executor.

## State

Default state root: `~/.local/share/arvectum/ai-eng-001`.

Subdirectories:

- `inbox/` — queued tasks;
- `processing/` — claimed tasks;
- `archive/` — completed queue records;
- `runs/<run-id>/` — evidence;
- `worktrees/<run-id>/` — isolated engineering worktrees.

Runtime state is operational evidence, not canonical product implementation truth.

## First pilot constraint

Use one product repository and one bounded technical task at a time. Do not include customer-production, signing, banking or broad organization-admin access.
