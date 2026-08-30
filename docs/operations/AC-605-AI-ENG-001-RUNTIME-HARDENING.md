# AC-605 — AI-ENG-001 executor observability and hang hardening

Status: `Required before ARV-001 retry`
Date: `2026-08-30`
Owner: `POS-004 / AI-ENG-001 pilot`
Trigger evidence: `docs/operations/AC-605-AI-ENG-001-HANG-FAILURE-EVIDENCE.md`

## Objective

Make long-running AI-ENG-001 engineering execution observable, bounded and fail-closed without weakening the existing authority, path or promotion gates.

The remediation is runtime infrastructure work in `arvectum1/arvectum-company`; it does not change Tender Agent product semantics and does not itself complete AC-605.

## Required behavior

### Streaming executor evidence

During executor execution, AI-ENG-001 must persist stdout and stderr incrementally to:

- `executor.stdout.txt`;
- `executor.stderr.txt`.

Files must exist once the executor starts and grow as output is received. The implementation must not wait for executor completion before writing captured output.

### Runtime status / heartbeat

Each running task must maintain a durable `runtime-status.json` in its run directory with at least:

- `run_id`;
- `task_id`;
- `phase`;
- `executor_pid` when applicable;
- `started_at`;
- `phase_started_at`;
- `last_activity_at`;
- `elapsed_seconds` or equivalent observable timing;
- `hard_timeout_seconds`;
- `idle_timeout_seconds`;
- terminal `termination_reason` when applicable.

Required phases should distinguish at minimum:

- `ADMISSION`;
- `WORKTREE_READY`;
- `EXECUTOR_RUNNING`;
- `POST_EXECUTOR_CHECKS`;
- `TESTING`;
- terminal state.

The status file is operational evidence, not Organizational Authority or approval.

### Idle timeout

Add a configurable executor inactivity timeout separate from the existing task hard timeout.

Default pilot value: `600` seconds.

Activity may be established conservatively from executor stdout/stderr progress and/or other explicit runner-observed executor activity. The implementation must not treat mere wall-clock process existence as progress.

When the idle timeout is exceeded, the runner must terminate the executor process group, preserve accumulated evidence and return `BLOCKED` with an explicit safe reason such as `executor_idle_timeout`.

The existing total task/executor hard timeout remains independently enforced.

### Process lifecycle

The executor must run in a process group/session that the supervisor can terminate as a unit on:

- idle timeout;
- hard timeout;
- runner interruption/controlled shutdown where practicable.

Termination must first use a graceful signal and then bounded forced termination if necessary. No unrelated OpenCode service/process may be killed.

### Post-executor short circuit

If the executor does not complete successfully and there are no reviewable changes, AI-ENG-001 must not run declared post-executor tests. The report must classify the executor failure/timeout directly.

If a non-zero executor exits after producing reviewable changes, the conservative pilot behavior should remain fail-closed; tests may be skipped unless there is a clearly documented reason to run them for diagnostics. No non-zero executor result may become `READY_FOR_OWNER`.

### Evidence/reporting

Terminal report/checks must distinguish at least:

- successful executor exit;
- non-zero executor exit;
- hard timeout;
- idle timeout;
- supervisor interruption where detectable.

Accumulated stdout/stderr, runtime status, worktree identity and changed paths must remain available after failure.

## Configuration

Extend `Config` and `config.example.json` with a bounded idle-timeout setting, preferably:

`executor_idle_timeout_seconds: 600`

Validation should reject unsafe/non-sensical values. Keep the existing task `timeout_seconds` as the per-task hard ceiling.

## Test requirements

Add deterministic tests using local fake executors only; no OpenCode/provider/network dependency.

Minimum regression cases:

1. stdout/stderr files are created and populated during/after normal executor execution;
2. normal executor output + valid change still reaches `READY_FOR_OWNER`;
3. silent sleeping executor is terminated by a short configured idle timeout and returns `BLOCKED` with `executor_idle_timeout`;
4. child process spawned by a fake executor is terminated with the executor process group;
5. hard timeout remains distinguishable from idle timeout;
6. post-executor test command is not executed after executor idle-timeout/non-zero failure with no reviewable changes;
7. `runtime-status.json` contains required phase/PID/timestamp/termination fields;
8. existing protected-boundary and isolated-worktree behavior remains intact.

Tests must be fast; test-specific idle/hard timeout values may be small while production/default values remain bounded.

## Acceptance

Remediation is acceptable only when:

- Python compile passes;
- full `tests/test_ai_eng_001.py` passes with new regressions;
- existing `ai_workforce/ai_eng_001/smoke_test.sh` passes;
- `git diff --check` passes;
- no Tender Agent repository change is included;
- no authority/promotion boundary is relaxed;
- no autonomous commit/push/merge/release/deploy behavior is added.

After promotion and Mac mini deployment, repeat a synthetic hanging-executor smoke before retrying the real ARV-001 pilot.