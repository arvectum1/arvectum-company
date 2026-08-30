# DECISION-2026-08-30 — AC-602…AC-604 AI-ENG-001 Bounded Pilot

Status: `Approved`
Decision date: `2026-08-30`
Decision authority: `Owner of Arvectum Company`

## Owner instruction

The Owner explicitly instructed after AC-601 selected POS-004:

> `давай попробуем сделать и посмотрим, что получится. сделай все сам, потом скажи, как мне это развернуть на мак мини и как подключить llm, если она нужна`

Within the already-selected POS-004 M6 contour, this instruction authorizes preparation and implementation of the smallest reversible AI-ENG-001 pilot needed for a real deployment attempt, while preserving existing reserved authority, access, security and customer boundaries.

## Approved bounded actions

Approve:

1. `AC-602` pilot business/workload measurement baseline;
2. creation of persistent pilot Principal identifier `AI-ENG-001` for POS-004;
3. `AC-603` bounded pilot Assignment and local Mac mini runtime implementation;
4. OpenCode as initial replaceable coding executor;
5. optional OpenAI-compatible manager LLM integration, disabled by default;
6. local worktree/edit/test/evidence execution inside admitted tasks;
7. `AC-604` quality/risk gates and implementation regression tests;
8. preparation of Mac mini launchd deployment helpers.

## Preserved boundaries

This decision does not activate AM-3 or AM-4; does not authorize autonomous customer communication/acceptance, commit, push, merge, release or deploy; does not authorize bank/signing access, customer-production access, organization-wide administration or raw reusable-secret exposure; does not change Company↔Product↔Arvectum OS boundaries; and does not prove operational/economic success.

The pilot stops autonomous execution at `READY_FOR_OWNER`. Local commit requires explicit Owner `approve RUN_ID`; remote push additionally requires explicit `--push`.

## Evidence status

Cross-review: `docs/reviews/AC-602-604-AI-ENG-001-PILOT-CROSS-REVIEW.md` — `7/7 PASS`.

Implementation mechanics tests: `4/4 PASS` in the implementation environment; Python compile and shell syntax validation also passed.

Mac mini deployment and real product execution remain unproven and belong to `AC-605`.

## Decision result

- `AC-602 — Complete / PASS for pilot baseline`;
- `AC-603 — Complete / PASS for bounded pilot implementation`;
- `AC-604 — Complete / PASS for pilot gates`;
- next operational step: `AC-605 — Supervised AI Position pilot`.
