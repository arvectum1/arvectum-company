# AC-605 — AI-ENG-001 first real-task executor hang evidence

Status: `Observed / fail-closed recovery completed`
Date: `2026-08-30`
Pilot: `AC-605 — Supervised AI Position pilot`
Position: `POS-004 — Engineering & Release Lead`
Principal: `AI-ENG-001`
Product task: `Tender Agent / ARV-001 — decision-useful document analysis`

## Summary

The first real AC-605 ARV-001 execution did not reach the repository-owned real-source candidate runner. The AI-ENG-001 parent process launched OpenCode successfully, but the OpenCode executor remained sleeping for approximately 39 minutes without a child process, network connection, worktree change or candidate output. The run was manually terminated fail-closed.

This is operational evidence about the AI-ENG-001 runtime, not evidence that ARV-001 itself failed.

## Run identity

- AI-ENG run ID: `20260830T111956Z-AC605-ARV001-AUTOREWORK-001`
- worktree: `~/.local/share/arvectum/ai-eng-001/worktrees/20260830T111956Z-AC605-ARV001-AUTOREWORK-001`
- run evidence directory: `~/.local/share/arvectum/ai-eng-001/runs/20260830T111956Z-AC605-ARV001-AUTOREWORK-001`
- attempted product output root: `/private/tmp/ac605-ai-eng-arv001-20260830T112033Z-attempt-0`
- executor model observed: `opencode/mimo-v2.5-free`

## Observed state before intervention

Parent AI-ENG process:

- command: `python3 -m ai_workforce.ai_eng_001.cli ... run /tmp/ac605-arv001-autorework.json`
- elapsed at diagnostic snapshot: approximately 33 minutes.

Child executor:

- command: `opencode run --model opencode/mimo-v2.5-free --dir <isolated-worktree> <bounded prompt>`
- elapsed at final diagnostic snapshot: approximately 39 minutes;
- process state: sleeping;
- CPU: approximately `0.2%` at final snapshot;
- no child processes;
- no network connections visible for the executor PID.

Run evidence directory contained only:

- `task.json`;
- `executor-prompt.txt`.

No `executor.stdout.txt`, `executor.stderr.txt`, `report.json` or `report.md` had yet been emitted because the current runner writes executor output only after subprocess completion.

## Product-side evidence

The isolated worktree remained unchanged:

- `git status --short`: empty.

The attempted ARV-001 output root existed but remained empty:

`/private/tmp/ac605-ai-eng-arv001-20260830T112033Z-attempt-0`

Expected candidate artifacts were absent:

- `upload-ready-report-decision-useful.html` — absent;
- `decision-useful-analysis.json` — absent;
- `human-decision-contract.json` — absent.

Therefore there is no evidence that `scripts/arv001/run_decision_useful_candidate_local.py` completed or that ARV-001 candidate generation itself was reached.

## Recovery

The Owner explicitly terminated only the hung foreground AI-ENG run and its OpenCode child with `SIGTERM`.

Post-termination checks showed:

- parent process absent;
- OpenCode child absent;
- no surviving child process;
- isolated worktree still unchanged;
- failed attempt root preserved and empty.

Unrelated persistent OpenCode service and AI-ENG watch process were not terminated.

## Root cause class

Exact root cause inside OpenCode/model execution is not proven by the available evidence.

The runtime defect that is proven is observability/control-related:

1. executor stdout/stderr are captured in memory and only persisted after subprocess completion;
2. there is no durable executor heartbeat/phase record while the subprocess is running;
3. task timeout is a single hard timeout and does not distinguish total duration from inactivity;
4. the runner cannot classify a long inactive executor before the hard timeout;
5. the current post-executor path proceeds to declared tests after a non-zero executor exit instead of short-circuiting when no reviewable engineering output exists.

## Owner workload evidence

- manual recovery intervention count: `1`;
- intervention duration: `unknown / not measured`;
- intervention reason: diagnose and terminate a non-progressing executor while preserving fail-closed state.

This is direct evidence against the desired low-intervention operating model and must be addressed before repeating the ARV-001 pilot.

## Required remediation before retry

AI-ENG-001 must gain bounded executor observability and inactivity control before ARV-001 is retried:

- streaming executor stdout/stderr to durable run files during execution;
- durable runtime-status heartbeat with phase, PID, timestamps and activity state;
- configurable idle timeout separate from total hard timeout;
- process-group termination on timeout/interruption with preserved evidence;
- explicit executor termination classification;
- skip post-executor tests when executor did not complete successfully and produced no reviewable changes;
- regression coverage for streaming, idle timeout, process cleanup and test short-circuit behavior.

No AM-3/AM-4 authority change is implied by this remediation.