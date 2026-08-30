# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.47.0`
Создано: `2026-08-19`
Обновлено: `2026-08-30`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — Supervised AI Position pilot — deployment PASS / first real task pending`

## 1. Модель публикации

Эта редакция `0.47.0` сохраняет полное содержание дорожной карты `0.46.0` по immutable git blob и публикует только новое состояние Mac mini deployment/promotion внутри AC-605.

Предыдущая редакция:

- версия: `0.46.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `3bf8a32019db9b1a02bbcad403c61bf16dc73484`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-604 state, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. AC-605 deployment gate — PASS

Owner-controlled Mac mini deployment теперь имеет статус:

**`PASS — AI-ENG-001 deployed and synthetic smoke validated`.**

Canonical evidence:

`docs/operations/AC-605-MAC-MINI-DEPLOYMENT-EVIDENCE.md`.

Observed deployment evidence:

- AI-ENG-001 running on Mac mini;
- Python compile PASS;
- targeted runner tests `4/4 PASS`;
- synthetic smoke `READY_FOR_OWNER`;
- smoke checks `5/5 PASS`;
- no real product task executed;
- no autonomous merge/release/deploy/customer effect.

The deployment found one real portability defect in OpenCode worktree targeting. The bounded fix adds explicit:

`--dir <worktree>`

to the OpenCode executor invocation.

Remote review established that branch `work/ac-605-mac-mini-deploy` was one commit ahead, zero behind and changed exactly one file with one insertion. PR `#1` passed `AI-ENG-001 CI` and was promoted to canonical `main`.

Fix commit:

`f08b2a7f4101cf73ea0896ca353eb72c332f7a1b`

Merge commit:

`6e8df32168bc665b8aac288a5b828379122918d3`

## 3. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / bounded early admission`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Current / deployment PASS — first real task pending` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned / blocked on real AC-605 task evidence` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / blocked on AC-605/606 evidence` |

## 4. AC-605 exact next step

The installation/synthetic phase is complete. The next evidence MUST come from one real low-risk product engineering task executed through the deployed AI-ENG-001 runtime.

The task must have:

1. clear product ownership and canonical repository;
2. bounded engineering scope;
3. explicit acceptance criteria;
4. reversible git-based output;
5. objective tests/checks or equivalent evidence;
6. no material spend;
7. no raw-secret requirement;
8. no customer consequential external effect;
9. no Company/Product/OS authority-boundary change;
10. a human review gate at `READY_FOR_OWNER` before promotion.

The pilot must capture baseline SHA, task contract, changed paths, executor evidence, declared tests, rework/attempts, Owner intervention count/minutes where observable and final human decision.

A synthetic task is sufficient for deployment proof but not for AC-605 completion.

## 5. Authority boundary remains unchanged

Mac mini deployment PASS and promotion of the portability fix do not activate AM-3 or AM-4 and do not grant AI-ENG-001 autonomous authority to merge, release, deploy, make customer commitments, accept customer work, incur material spend or exercise Reserved Owner Decisions.

`READY_FOR_OWNER` remains evidence that the runtime reached a review gate, not evidence of Owner approval.

## 6. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with the existing customer evidence gates preserved from the previous roadmap chain.

M5 and M6 may continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
