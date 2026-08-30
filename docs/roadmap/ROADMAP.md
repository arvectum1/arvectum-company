# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.48.0`
Создано: `2026-08-19`
Обновлено: `2026-08-30`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — Supervised AI Position pilot — first real task selected / execution pending`

## 1. Модель публикации

Эта редакция `0.48.0` сохраняет полное содержание дорожной карты `0.47.0` по immutable git blob и публикует только выбор первой реальной задачи для AI-ENG-001.

Предыдущая редакция:

- версия: `0.47.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `70c52aa2a3b60176aae00d16d92d712c4fd552ff`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-604 state, Mac mini deployment PASS, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. AC-605 first real task — selected

Первой реальной supervised product engineering задачей для `AI-ENG-001` выбрана:

**`DP-CUST-019 — release provenance integrity regression coverage`**

Product owner / canonical repository:

`arvectum1/discount-parser`

Canonical product task contract:

`docs/tasks/DP-CUST-019.md`

Company selection evidence:

`docs/operations/AC-605-FIRST-REAL-TASK-SELECTION.md`

Discount Parser execution baseline after admission of the task contract:

`e6b3bf81909e60d6d7ddae98dab0225bba3b8190`

The task adds deterministic regression coverage around the existing Discount Parser release-provenance generator/verifier. It is maintenance/release-safety work with objective tests and no intended parser/runtime/customer behavior change.

## 3. Why this task is admitted

The task satisfies the bounded AC-605 pilot criteria:

- real Product-owned engineering work;
- clear canonical repository and task contract;
- narrow expected path boundary (`tests/test_release_provenance.py`, with `scripts/release_provenance.py` only if a concrete defect is exposed);
- reversible isolated git worktree output;
- objective targeted/full tests;
- no network requirement;
- no raw secrets/customer data;
- no material spend;
- no version bump/release/deploy/customer delivery;
- no Company/Product/OS authority-boundary change;
- explicit human review gate at `READY_FOR_OWNER`.

## 4. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / bounded early admission`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Current / DP-CUST-019 selected — execution pending` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned / blocked on real AC-605 task evidence` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / blocked on AC-605/606 evidence` |

## 5. AC-605 exact next step

Run `DP-CUST-019` through the deployed Mac mini `AI-ENG-001` runtime from the current canonical Discount Parser `main` state.

The run must preserve:

1. actual execution baseline SHA;
2. product task contract;
3. isolated worktree and branch identity;
4. generated executor prompt and executor output;
5. changed paths/diff;
6. targeted and, if practical, full test results;
7. attempts/rework and failures/escalations;
8. final state;
9. Owner intervention count/time where observable.

If the result reaches `READY_FOR_OWNER`, AI-ENG-001 MUST stop. Commit/push/merge/release/deploy/customer delivery remain separate explicit human/promotion decisions.

## 6. Authority boundary remains unchanged

Task selection does not activate AM-3 or AM-4 and does not grant autonomous promotion authority. A need for material scope expansion, new dependency, raw secret, material spend, unrelated cleanup, customer external effect or Company/Product/OS boundary change must escalate/fail closed.

Technical PASS of DP-CUST-019 will be evidence for AC-605 but will not by itself prove M6 completion, customer readiness, profitability or positive unit economics.

## 7. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with the existing customer evidence gates preserved from the previous roadmap chain.

M5 and M6 may continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
