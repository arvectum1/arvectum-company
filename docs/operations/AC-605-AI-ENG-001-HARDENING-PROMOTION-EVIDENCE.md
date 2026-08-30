# AC-605 — AI-ENG-001 hardening promotion evidence

Status: `PROMOTED / post-promotion Mac mini verification pending`
Date: `2026-08-30`
Repository: `arvectum1/arvectum-company`

## 1. Trigger

The first real AC-605 Tender Agent / ARV-001 execution (`20260830T111956Z-AC605-ARV001-AUTOREWORK-001`) exposed an AI-ENG-001 runtime/observability failure before Product work began. The OpenCode executor became inactive for approximately 39 minutes while the supervisor had no streaming logs, heartbeat, idle timeout, live status or bounded process-group recovery. The Owner manually terminated the foreground run. The Product worktree remained unchanged and the ARV-001 attempt root was empty.

Canonical failure evidence:

`docs/operations/AC-605-AI-ENG-001-HANG-FAILURE-EVIDENCE.md`

Required hardening contract:

`docs/operations/AC-605-AI-ENG-001-RUNTIME-HARDENING.md`

## 2. Implementation candidate

Branch:

`work/ac-605-ai-eng-observability`

Base main:

`1515606d99158321e752ecbdeb42f667c1268480`

Implementation commit:

`ea092fa817ae750970242630b1e8339439f195b4`

Compared with base:

- ahead by 1 commit;
- behind by 0;
- 6 changed files;
- no Tender Agent files.

Implemented runtime changes include:

- incremental executor stdout/stderr persistence;
- atomic `runtime-status.json` heartbeat and phases;
- configurable `executor_idle_timeout_seconds`, default 600 seconds;
- distinct idle and hard timeout classifications;
- executor-only process-group termination and child cleanup;
- explicit `executor_idle_timeout`, `executor_hard_timeout`, `executor_nonzero_exit`, and `supervisor_interrupted` evidence;
- post-executor test short-circuit after timeout/non-zero executor result;
- in-progress run visibility through `status`;
- doctor validation of idle-timeout configuration;
- synthetic normal/hang regression coverage.

## 3. Local Mac mini evidence reported before promotion

The implementation branch reported:

- Python compile: PASS;
- unittest: 9/9 PASS;
- pytest: 9/9 PASS;
- shell syntax: PASS;
- normal synthetic smoke: PASS;
- synthetic hang smoke: PASS;
- idle timeout: 2 seconds in synthetic hang proof;
- executor terminated: YES;
- spawned child terminated: YES;
- post-executor test marker absent: YES;
- `runtime-status.json` preserved: YES;
- source repository unchanged: YES;
- in-progress `EXECUTOR_RUNNING` visible: YES;
- terminal transition to `BLOCKED`: YES.

The underlying reason why OpenCode/model became inactive in the original ARV-001 attempt remains unknown; this hardening addresses supervision, observability and bounded recovery rather than claiming to fix the executor/provider itself.

## 4. Independent GitHub review evidence

GitHub compare confirmed the implementation branch was a clean one-commit fast-forward candidate relative to its base with exactly the six expected Company runtime/docs/test files changed.

Pull request:

`#2 — AC-605 — harden AI-ENG executor observability and hang recovery`

Exact PR head:

`ea092fa817ae750970242630b1e8339439f195b4`

PR-triggered `AI-ENG-001 CI`:

- workflow run: `33311787999`;
- job: `runner-mechanics`;
- conclusion: `success`;
- compile: PASS;
- unit/integration tests: PASS;
- shell syntax: PASS.

PR was mergeable and non-draft.

## 5. Promotion

PR #2 was merged to canonical `main` with explicit expected-head binding.

Merge commit:

`8207f5da0e4b3ed03a2ceed178a122fec199ab66`

The merge commit is GitHub-verified.

Promotion changes only the Company-specific AI workforce runtime, tests and runtime documentation. It does not change Company authority semantics and does not modify Tender Agent Product code.

## 6. Authority boundary

This promotion does not activate AM-3 or AM-4 and does not grant autonomous authority to commit, push, merge, release, deploy, change Product Owner decisions, authorize independent review, retry governed provider acceptance, perform EIS/provider/RAG calls, mutate accepted/frozen evidence, mutate production DB or create customer external effects.

`READY_FOR_OWNER` remains a human review gate.

## 7. Remaining gate before ARV-001 retry

Promotion alone does not close the runtime remediation gate.

Before another real ARV-001 execution through AI-ENG-001, the Owner-controlled Mac mini must:

1. fast-forward the canonical Company checkout to the promoted `main`;
2. run `doctor` and confirm the new runtime is active;
3. run the promoted synthetic hang smoke and prove bounded idle termination, child cleanup, preserved runtime status and no post-executor tests;
4. run the normal synthetic smoke;
5. only then submit a new immutable ARV-001 real-task execution.

AC-605 remains open until a real supervised Product task reaches its next governed human gate or fails closed with new evidence.
