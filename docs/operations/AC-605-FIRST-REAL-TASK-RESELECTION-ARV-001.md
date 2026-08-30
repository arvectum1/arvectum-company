# AC-605 — First Real Task Reselection: Tender Agent / ARV-001

Status: `Selected`
Date: `2026-08-30`
Owner instruction: prefer automatic continuation of Tender Agent `ARV-001` over the previously selected Discount Parser maintenance task.

## Superseded pilot selection

The earlier AC-605 candidate `DP-CUST-019 — release provenance integrity regression coverage` remains a valid Discount Parser maintenance task but is no longer the selected first real AI-ENG-001 pilot task. It was not needed as the pilot because its implementation already exists in the current Discount Parser state.

No negative product decision is made about DP-CUST-019; only the Company-level AC-605 pilot selection changes.

## Selected real workload

Product: `Tender Agent`
Canonical repository: `arvectum1/tender-agent`
Current work item: `ARV-001 — decision-useful document analysis / human-facing report rework`
Current PR: `#18 — ARV-001: decision-useful document analysis`
Current PR branch: `arv001/decision-usefulness`
Observed PR head at selection: `a78a55376ed1c5e42fc3d4f9515ac9f7453162b6`
Observed CI: `CI #234 — success` on the exact PR head.

## Current ARV-001 state

The human-facing candidate is still Product Owner `REJECTED`. The blocker is report decision-usefulness, not merely HTML presentation. The corrective branch adds concrete source-bound technical, payment, security, acceptance, liability, termination and application-requirement extraction plus explicit Decision / Evidence / Uncertainty / Caveats / Next-action structure and fail-closed quality/render checks.

The latest real-source run reached decision-usefulness PASS but failed a stricter rendered-material validation because the renderer validator required an exact standard even when the semantic gate correctly accepted a concrete technical characteristic instead. The branch subsequently aligned the rendered validator with the semantic gate and added regression coverage. CI now passes; a new immutable real-source local candidate run is required.

Independent review remains `NOT_AUTHORIZED`; freeze remains `NOT_ALLOWED`; ARV-001 remains open. P8.05 remains a separate external-source blocker and is not the cause of the Product Owner rejection.

## Why this is the preferred AC-605 pilot

This work tests the intended organizational loop rather than a synthetic coding exercise:

`Owner quality rejection -> AI-ENG-001 -> OpenCode executor -> bounded diagnosis/rework -> deterministic tests -> real local candidate -> READY_FOR_OWNER -> explicit Product Owner review`.

It is real Product-owned engineering work, already important to current Tender Agent progress, and has a strong fail-closed evidence boundary. The corrective local candidate path is designed to perform no EIS call, provider call, RAG rerun, quality-acceptance rerun, accepted-evidence mutation, source-byte mutation or production DB mutation.

## Pilot authority boundary

AI-ENG-001 may continue the existing bounded ARV-001 corrective branch in an isolated child worktree/branch, run repository-owned local candidate tooling, inspect sanitized failure codes, modify only the existing decision-usefulness/report-rework implementation and its regressions when a concrete defect is found, and produce a new sanitized candidate/evidence record.

AI-ENG-001 must stop at `READY_FOR_OWNER`. It may not autonomously merge PR #18, approve Product Owner acceptance, authorize independent review, freeze ARV-001, retry governed provider acceptance, perform EIS/provider/RAG calls, create/consume acknowledgements, deploy, or create customer external effects.

## Economic/organizational evidence sought

The pilot should measure whether AI-ENG-001 can absorb the repeated engineering coordination loop that previously required the Owner to relay every blocker and repair step manually. Evidence should include attempts, failures, rework, changed paths, tests, candidate generation result, Owner intervention count/time where observable, and final human decision.
