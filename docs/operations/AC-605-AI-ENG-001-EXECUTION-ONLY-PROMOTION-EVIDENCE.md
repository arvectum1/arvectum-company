# AC-605 — AI-ENG-001 execution-only promotion evidence

Status: `PASS / PROMOTED`
Date: `2026-08-30`
Repository: `arvectum1/arvectum-company`

## Scope

Promote backward-compatible support for bounded execution-only AI-ENG-001 tasks whose success requires zero Git mutation and review of runtime/external artifacts rather than a promotable code diff.

## Implementation

Branch: `work/ai-eng-execution-only-mode`

Implementation commit: `1cb2ebef6f2cef1b504a85fa9ef51aa59a74b250`

Base main: `2f6e20190152647da0fe5683c0623122b9756e5e`

Repository compare at review:
- ahead: 1;
- behind: 0;
- changed files: 4;
- no Tender Agent Product files changed.

Changed paths:
- `ai_workforce/ai_eng_001/core.py`;
- `ai_workforce/ai_eng_001/task.example.json`;
- `tests/test_ai_eng_001.py`;
- `docs/operations/AI-ENG-001-RUNTIME.md`.

## Contract

New task field: `requires_changes`.

- omitted/default `true`: existing engineering semantics preserved; at least one valid changed path is required;
- `false`: execution-only semantics; zero Git changes are required for success;
- any Git mutation in execution-only mode fails closed with `unexpected_changes_in_execution_only_task`;
- execution-only READY_FOR_OWNER has no Git candidate and `approve_run()` rejects promotion with `execution-only run has no git changes to approve`.

This does not expand authority and does not add autonomous commit, push, merge, release or deploy capability.

## Evidence

Mac mini implementation report:
- py_compile PASS;
- pytest 12/12 PASS;
- unittest 12/12 PASS;
- normal smoke PASS;
- hang smoke PASS;
- git diff --check PASS;
- worktree clean;
- no ARV-001 execution during implementation.

GitHub PR: `#3 — AI-ENG-001 — support fail-closed execution-only tasks`.

Exact-head GitHub CI:
- workflow: `AI-ENG-001 CI`;
- run: `33314133950`;
- job: `runner-mechanics`;
- conclusion: `success`;
- compile PASS;
- unit/integration tests PASS;
- shell syntax PASS.

PR #3 merge commit: `d81e08596cee82e433df4ef64d224f1fe03abb3d`.

## AC-605 consequence

The execution-only gate that previously blocked a clean ARV-001 presentation-compression retry is removed at repository level.

The next real AC-605 run may use `requires_changes=false` against exact Tender Agent head `7f63a38227c8cc009c722da820caf3cd05493bd9`, provided the Owner-controlled Mac mini first fast-forwards Company main, restarts the AI-ENG watch process, and passes doctor + normal/hang synthetic smoke on the promoted runtime.

Product Owner authority remains unchanged. `READY_FOR_OWNER` is review readiness only, not Product approval.
