# DECISION-2026-08-30 — AC-601 Approval

Status: `Approved`
Decision date: `2026-08-30`
Decision authority: `Owner of Arvectum Company`
Subject: `AC-601 — AI delegation candidate selection from real workload`
Reviewed proposal: `docs/organization/AI-DELEGATION-CANDIDATE-SELECTION.md`
Proposal version: `0.9.0`
Proposal blob: `b1b37d87a963c717a589c34c74616f5c7e78f585`
Cross-review: `docs/reviews/AC-601-AI-DELEGATION-CANDIDATE-SELECTION-CROSS-REVIEW.md`
Cross-review blob: `c9c81ec5a086d796b1b8b0d31c3c7e19d7fdbf98`

## Decision

Approve AC-601 and select:

**`POS-004 — Engineering & Release Lead`**

as the first Arvectum Company Position to be taken through the M6 AI-held Position proof.

The selection is approved because the reviewed evidence shows a real current workload, an already-approved AI-led executor pattern, a bounded AM-0/AM-1/AM-2 execution surface, strong repository/test/CI evidence, least-privilege feasibility and practical runtime replacement/fallback characteristics relative to the other current Positions.

## Owner instruction evidence

The Owner explicitly instructed:

> `Сделай эту задачу, а потом распиши, как этого агента встроить в мои процессы`

This instruction followed the explicit proposal to execute `AC-601`, compare the candidate Positions and canonically select `POS-004` if the analysis confirmed the hypothesis.

The completed proposal and seven-iteration cross-review confirmed that hypothesis within the bounded scope. This decision promotes that result into durable Company state.

## Sequencing decision

AC-601 is admitted and completed while M5 remains open.

This is an explicit bounded sequencing change, not an M5 closure and not a claim that the missing AC-505 customer evidence has appeared.

Reason:

- POS-004 workload is independently evidenced by AC-104/AC-205 and current engineering work;
- AC-601 is internal, reversible and non-provisioning;
- it creates no customer effect, spend, credential, Principal or new authority;
- waiting for unrelated external customer evidence is not required merely to identify the first AI delegation candidate.

M5 remains `Current` and its evidence gates remain unchanged.

## Preserved boundaries

This approval does not:

- create a concrete AI Principal such as `AI-ENG-001`;
- create or broaden a POS-004 Assignment;
- provision repository, CI, production, customer-system or secret access;
- activate AM-3 or AM-4;
- delegate ROD-01…ROD-09 final decisions;
- authorize material spend, signing, payment, customer commitments or autonomous external effects;
- make any model, agent framework or runtime the Position itself;
- approve AC-602…AC-607 automatically;
- prove M6 economically or operationally complete.

## Next M6 handoff

The next M6 work item is:

`AC-602 — Position business case and unit-economics/workload evidence`.

AC-602 must establish the bounded business/workload measurement baseline before AC-603 creates the concrete persistent Principal, Assignment, runtime, tools and data boundary.

## Decision result

`AC-601 — Complete / PASS — POS-004 selected`.