# DECISION-2026-08-30 — AI Workforce Repository Structure Extension

Status: `Approved`
Decision date: `2026-08-30`
Decision authority: `Owner of Arvectum Company`
Scope: narrow extension of AC-003 for real Company-specific AI workforce implementation

## Decision

Approve one new top-level repository implementation directory:

`ai_workforce/`

as the canonical home for Company-specific, non-product, non-Arvectum-OS AI workforce runtime/reference implementation that directly realizes approved Company Positions/Assignments.

The first admitted implementation is:

`ai_workforce/ai_eng_001/`

for the bounded `AI-ENG-001` / `POS-004 — Engineering & Release Lead` M6 pilot.

## Rationale

AC-003 intentionally prohibited speculative enterprise filesystem expansion but allowed repository structure to evolve when a real artifact class provides operating value. The AI-ENG-001 runtime is now a real Company-owned implementation with durable organizational semantics and is not product implementation, an Arvectum OS platform capability, or merely a generic repository helper.

Keeping the runtime under `ai_workforce/` preserves the Company/OS/Product boundary and avoids misclassifying the persistent Position runtime as a generic `tools/` script.

Runtime-local templates, example task/config files and Mac deployment helpers are colocated under the specific workforce implementation directory rather than creating separate top-level `config/` or `deploy/` trees.

## Preserved boundaries

This extension does not authorize product implementation to move into the Company repository; does not create a generic agent platform; does not transfer Arvectum OS capability ownership; does not make runtime logs/high-volume operational records canonical Git artifacts; and does not authorize secrets/customer-confidential data in the repository.

The existing AC-003 rules remain controlling except for this narrow approved top-level extension.
