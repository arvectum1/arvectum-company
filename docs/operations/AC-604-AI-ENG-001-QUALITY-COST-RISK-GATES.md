# AC-604 — AI-ENG-001 Quality, Evaluation, Cost and Risk Gates

Status: `Approved / pilot gates`
Version: `1.0.0`
Date: `2026-08-30`
Owner: `ООО «Арвектум»`

## Admission gates

A task is executable only when the source repository is a valid clean git worktree, the task has an explicit objective and at least one acceptance criterion, protected authority/risk flags are all false, the target base ref resolves, and the executor runtime is available.

Otherwise the runner returns `NEEDS_OWNER` or `BLOCKED` and performs no promotable action.

## Execution quality gates

A run may reach `READY_FOR_OWNER` only if all required checks pass:

- coding executor exits successfully;
- at least one file change exists;
- every changed path satisfies `allowed_paths` / `forbidden_paths` policy;
- `git diff --check` passes;
- every declared test command returns zero.

The report states exactly which checks/tests actually ran. Technical PASS is not customer/business acceptance.

## Promotion gate

`READY_FOR_OWNER` is not approval. Commit requires explicit `approve RUN_ID`. Remote push additionally requires `--push`. Merge, release and deploy remain outside the pilot runtime.

## Evidence gate

Each run preserves the submitted task, run ID, baseline SHA, worktree/branch, exact executor prompt, manager plan when used, executor stdout/stderr, changed paths, check results, test stdout/stderr, final state/escalation reasons, and an approval record when promoted.

## Risk gates

The runner fails closed on protected task flags, dirty source repository, path-policy violations, failed tests, failed diff check, executor timeout/error, missing runtime, or missing worktree at promotion.

The pilot does not claim OS-level sandbox isolation. It must not run with bank/signing credentials, customer-production credentials or unrelated reusable secrets in the process environment.

## Cost evidence

Cost is recorded only when the selected executor/provider exposes it. Missing cost data means `unknown`, not zero. Initial evidence should come from a small number of real tasks rather than synthetic benchmark volume.

## Implementation test evidence

Before publication, the runtime mechanics were exercised in a deterministic local implementation environment with tests for protected-boundary escalation, isolated git worktree execution, path policy, declared test execution, preservation of the source repository, and successful `READY_FOR_OWNER` classification.

Result: `4 tests / 4 PASS`. Python modules also passed `py_compile`; macOS shell deployment scripts passed `bash -n` syntax validation.

This does not prove actual OpenCode/model quality or Mac mini readiness.

## Result

`AC-604 — Complete / PASS for pilot quality/risk gates`.

`AC-605 — Supervised AI Position pilot` is the next operational step after Mac mini deployment.
