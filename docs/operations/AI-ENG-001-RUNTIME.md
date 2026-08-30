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

## Executor Evidence And Time Limits

The coding executor runs in its own process session. Its stdout and stderr are appended incrementally to `executor.stdout.txt` and `executor.stderr.txt` in the run directory, so evidence is available before the executor exits.

Every run also has an atomically written `runtime-status.json`. It records the current phase, executor PID, heartbeat time, last observed stdout/stderr activity, elapsed time, hard and idle limits, and terminal termination classification. Phases include `ADMISSION`, `WORKTREE_READY`, `EXECUTOR_RUNNING`, `POST_EXECUTOR_CHECKS`, `TESTING`, `READY_FOR_OWNER`, `BLOCKED`, and `NEEDS_OWNER`.

`timeout_seconds` remains the task hard limit. `executor_idle_timeout_seconds` is a separate configuration limit (default `600`) for no stdout/stderr activity. A silent executor is terminated as its own process group with `SIGTERM`, then `SIGKILL` after a bounded grace period if needed. Classifications are `executor_idle_timeout`, `executor_hard_timeout`, `executor_nonzero_exit`, and `supervisor_interrupted` where applicable.

`status` includes runs that have `runtime-status.json` but no terminal report, allowing an Owner to observe a running task. Declared post-executor test commands run only after a zero executor exit; timeout and non-zero exits remain fail-closed.

## Task contract

Required fields: `id`, `repository`, `objective`, and a non-empty `acceptance` list.

Operational fields: `base_ref`, `test_commands`, `allowed_paths`, `forbidden_paths`, and `timeout_seconds`.

`requires_changes` defaults to `true` for engineering tasks and preserves the existing requirement for at least one changed path. Set it to `false` only for execution-only tasks whose output is contractually outside the Git repository. An execution-only task succeeds only with a clean worktree; any Git mutation fails closed. Execution-only runs have no Git candidate, so they cannot be approved or promoted through `approve`.

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
