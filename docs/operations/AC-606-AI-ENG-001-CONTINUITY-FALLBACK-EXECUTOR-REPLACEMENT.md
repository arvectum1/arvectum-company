# AC-606 — AI-ENG-001 continuity, fallback and executor-replacement proof

Status: `Complete / PASS — bounded continuity mechanics proven`
Version: `1.0.1`
Date: `2026-09-01`
Owner: `ООО «Арвектум»`
Position: `POS-004 — Engineering & Release Lead`
Principal: `AI-ENG-001`
Canonical PR: `#5`
Canonical merge: `fe8fca259794eef9af640e4b1baa66f8be3946f7`

## 1. Purpose

AC-606 proves that the Company Position/Principal contract is not tied to one coding executor session or executable. A failed executor must stop fail-closed, after which the Owner can explicitly select a replacement executor and resubmit an attributable task without changing the Position, Principal, task scope, protected authority flags or promotion boundary.

This is a continuity/runtime-mechanics proof. It does not claim that every alternative model, vendor or coding tool has equivalent engineering quality.

## 2. Continuity model

The accepted recovery sequence is:

`primary executor failure → BLOCKED → Owner/human recovery decision → explicit replacement executor → attributable task resubmission → READY_FOR_OWNER`

There is deliberately **no automatic failover**. Executor failure cannot silently broaden scope, switch providers, commit, push, merge, deploy or create external effects.

The replacement attempt uses a new task identifier for attribution while preserving the same bounded task contract: repository, objective, acceptance criteria, test command, allowed path, protected-boundary flags, `requires_changes` and timeout.

## 3. Repository-owned proof

Implementation:

`ai_workforce/ai_eng_001/continuity_probe.py`

Regression:

`tests/test_ai_eng_001_continuity.py`

CI workflow executes both the full AI-ENG unit/integration suite and an explicit standalone continuity probe.

Accepted implementation/probe CI head:

`6846fe682adbfc50c4e405e44091ff3ac0c8e7f0`

Final accepted PR head:

`facfa9bd93ae5674f1c23cbd95acdb876c744f92`

Canonical merge on `main`:

`fe8fca259794eef9af640e4b1baa66f8be3946f7`

GitHub Actions:

- workflow: `AI-ENG-001 CI`;
- run: `#13`;
- job: `runner-mechanics`;
- result: `SUCCESS`;
- compile: PASS;
- unit/integration tests: `17 tests / PASS`;
- explicit `AC-606 continuity probe`: PASS;
- shell syntax checks: PASS.

The final PR-head delta after the accepted code/CI head is evidence/documentation only and does not alter continuity mechanics.

## 4. Explicit continuity evidence

The standalone probe emitted:

`AC606_CONTINUITY_PROBE_PASS`

Observed invariants:

- Principal remained `AI-ENG-001`;
- Position remained `POS-004`;
- `automatic_failover=false`;
- `authority_expanded=false`;
- primary executor returned non-zero and was classified `BLOCKED / executor_nonzero_exit`;
- primary executor produced no changed paths;
- source HEAD remained unchanged after primary failure;
- source repository remained clean after primary failure;
- replacement task contract matched the primary contract except for its attributable task ID;
- replacement executor reached `READY_FOR_OWNER`;
- replacement changed only the declared `continuity.txt` path;
- replacement baseline SHA matched the original baseline;
- replacement worktree remained uncommitted;
- source HEAD remained unchanged after replacement execution;
- source repository remained clean after replacement execution;
- no automatic approval or commit record was created.

The replacement run also passed its executor-exit, path-policy, changed-file, `git diff --check` and declared acceptance-test gates.

## 5. Human/software fallback interpretation

The human fallback is the explicit recovery boundary, not manual editing hidden inside the agent run. After a failed executor, the system preserves a non-promotable result and requires the Owner to choose what happens next. The Owner may choose a replacement software executor, defer the task, or perform the work outside the AI Position process under normal human authority.

The repository-owned proof exercises the software-replacement path after that human decision boundary. No automatic repair or retry is treated as human approval.

## 6. Authority and safety boundary

AC-606 does not change AC-603 authority:

- AM-3 and AM-4 remain inactive;
- `READY_FOR_OWNER` remains the terminal autonomous promotion state;
- no automatic commit, push, merge, release or deploy exists;
- no customer/supplier contact or procurement-platform effect is authorized;
- no reusable secrets are introduced;
- executor replacement does not transfer or enlarge authority;
- Position and Principal identity remain stable across executor replacement.

## 7. Result

`AC-606 — Complete / PASS`.

The required bounded continuity mechanics are now proven and merged to canonical `main`: fail-closed primary failure, explicit human recovery boundary, attributable resubmission, replacement executor success, unchanged baseline/source state, unchanged authority, and no automatic promotion.

The next M6 step is `AC-607 — Value, Owner-workload, module-reuse and risk review` using AC-605 real Product evidence, the successful Tender Agent Mac mini E2E evidence, and this AC-606 continuity proof.
