# AC-605 — First Real AI-ENG-001 Task Selection

Status: `Selected / execution pending`
Date: `2026-08-30`
Position: `POS-004 — Engineering & Release Lead`
Principal: `AI-ENG-001`
Product: `Discount Parser`
Product repository: `arvectum1/discount-parser`
Product task: `DP-CUST-019 — release provenance integrity regression coverage`

## Selection

Select Discount Parser task `DP-CUST-019` as the first real supervised product engineering task for AC-605.

The product task contract is canonical in:

`arvectum1/discount-parser/docs/tasks/DP-CUST-019.md`

The task was admitted after Discount Parser `0.1.16` customer-delivery preparation and is intentionally maintenance/release-safety work rather than customer-facing runtime behavior.

## Why this task

The task has direct operating value because the existing Discount Parser release process already generates/verifies artifact provenance, while regression coverage for tamper/missing/extra-artifact failure behavior is not currently evidenced in the inspected test baseline.

It is appropriate for first supervised execution because it is bounded, reversible, testable, requires no secret/customer data/network/material spend, does not require a version bump or release, and can stop cleanly at `READY_FOR_OWNER`.

## Authority boundary

AI-ENG-001 may implement the bounded product task in an isolated worktree and run declared tests/evidence collection under its existing AM0/AM1/AM2 pilot boundary.

This selection does not authorize AI-ENG-001 to commit/push/merge/release/deploy/customer-deliver autonomously, activate AM3/AM4, change product scope, alter Company/Product/OS boundaries, incur material spend, or access raw secrets/customer systems.

Any need to change paths outside the task's stated boundary, introduce dependencies, alter release semantics materially, or handle unrelated failures must escalate.

## AC-605 evidence objective

The purpose is to test the real organizational contour, not merely coding quality:

`Owner-selected goal → AI-ENG-001 → OpenCode executor → isolated changes/tests/evidence → READY_FOR_OWNER → human review/promotion decision`.

Evidence must capture baseline SHA, changed paths, tests, executor output, attempts/rework, final state and Owner intervention count/time where observable.

Successful technical completion remains only supervised task evidence; it does not complete M6 or prove positive economics by itself.
