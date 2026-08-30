# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.49.0`
Создано: `2026-08-19`
Обновлено: `2026-08-30`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — Supervised AI Position pilot — Tender Agent ARV-001 selected / execution pending`

## 1. Модель публикации

Эта редакция `0.49.0` сохраняет полное содержание дорожной карты `0.48.0` по immutable git blob и публикует только Owner re-prioritization первой реальной задачи AI-ENG-001.

Предыдущая редакция:

- версия: `0.48.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `d3bf2a312e1604af14fd25447c7ab779e6d14b48`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-604 state, Mac mini deployment PASS, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. AC-605 first real task — reselected by Owner priority

Предыдущий pilot candidate:

`DP-CUST-019 — release provenance integrity regression coverage`

снимается именно с роли первой AC-605 задачи. Он остаётся валидной Discount Parser maintenance-задачей, но не нужен для текущего пилота: соответствующая implementation уже присутствует в текущем product state.

Новой первой реальной supervised engineering задачей для `AI-ENG-001` выбрана текущая работа:

**`Tender Agent / ARV-001 — decision-useful document analysis / human-facing report rework`.**

Canonical Product repository:

`arvectum1/tender-agent`

Current PR:

`#18 — ARV-001: decision-useful document analysis`

Current branch:

`arv001/decision-usefulness`

Observed PR head at selection:

`a78a55376ed1c5e42fc3d4f9515ac9f7453162b6`

Observed exact-head CI:

`CI #234 — success`.

Company selection artifact:

`docs/operations/AC-605-FIRST-REAL-TASK-RESELECTION-ARV-001.md`.

## 3. Current ARV-001 evidence state

The current human-facing report remains:

**`Product Owner REJECTED`.**

The active corrective scope is analytical depth / decision usefulness rather than presentation-only repair. PR #18 adds source-bound concrete technical standards/characteristics, payment mechanics, security, acceptance, liability/penalty/interest, termination and application requirements, deterministic locators, explicit Decision / Evidence / Uncertainty / Caveats / Next-action structure and fail-closed quality/render validation.

The latest real-source local run reached:

- decision-usefulness gate `PASS`;
- explicit unresolved source placeholder for the blank performance-security amount;
- safe literal rendering;
- human decision finalization without regex failure;

and then failed closed because rendered validation unconditionally required an exact standard where the semantic gate correctly allowed either an exact standard or a concrete technical characteristic.

The branch subsequently aligned the rendered validator with the semantic gate and added regression coverage. Exact-head CI now passes. The next required evidence is a **new immutable real-source local candidate run**.

Current governance remains:

- Product Owner: `REJECTED`;
- independent review: `NOT_AUTHORIZED`;
- freeze: `NOT_ALLOWED`;
- ARV-001: `OPEN`;
- P8.05: separate `BLOCKED_EXTERNAL_SOURCE`, not the cause of this rejection.

## 4. Why ARV-001 is the preferred real AI Position proof

This task directly tests the intended engineering delegation loop:

`Owner rejection -> AI-ENG-001 -> OpenCode executor -> bounded diagnosis/rework -> tests -> real candidate -> READY_FOR_OWNER -> explicit Owner review`.

The first real proof therefore measures whether POS-004 can absorb repeated technical coordination and corrective work, rather than merely execute a small isolated test-writing task.

The repository-owned local ARV-001 corrective path is explicitly designed for zero provider/EIS/RAG/acceptance/production mutation while producing a human-facing Product Owner candidate from already frozen source evidence.

## 5. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / bounded early admission`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Current / ARV-001 selected — execution pending` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned / blocked on real AC-605 task evidence` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / blocked on AC-605/606 evidence` |

## 6. AC-605 exact next step

Run a bounded ARV-001 continuation through the deployed Mac mini `AI-ENG-001`, based on the exact current `arv001/decision-usefulness` PR head after fetch.

The AI Position should:

1. verify the current PR head and successful CI;
2. execute the repository-owned zero-provider local candidate path against the frozen real corpus;
3. if the local candidate fails because of a concrete defect inside the already-approved decision-usefulness/report-rework scope, diagnose and repair it in the isolated AI-ENG worktree;
4. add/adjust focused regression coverage for any real defect repaired;
5. rerun the relevant local candidate and deterministic tests inside the bounded task window;
6. preserve sanitized evidence and a reviewable diff;
7. stop at `READY_FOR_OWNER` with a new candidate, or fail closed with the exact blocker.

Because AI-ENG-001 currently requires reviewable git changes for `READY_FOR_OWNER`, a successful validation-only run with no code defect should also create a sanitized candidate-evidence record under the admitted ARV-001 evidence/docs boundary; it must not claim Product Owner approval.

## 7. Authority boundary remains unchanged

AI-ENG-001 may not autonomously:

- merge PR #18;
- change Product Owner `REJECTED` to approved;
- authorize independent review;
- freeze ARV-001;
- retry governed provider quality acceptance;
- perform EIS/provider/RAG calls;
- create/consume acceptance acknowledgements;
- mutate accepted evidence or frozen source bytes;
- mutate production DB state;
- deploy or create customer external effects;
- activate AM-3/AM-4.

`READY_FOR_OWNER` remains a human review gate, not approval.

## 8. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with the existing customer evidence gates preserved from the previous roadmap chain.

M5 and M6 may continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
