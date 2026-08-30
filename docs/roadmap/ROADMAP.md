# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.46.0`
Создано: `2026-08-19`
Обновлено: `2026-08-30`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — Supervised AI Position pilot — Mac mini deployment / real-task evidence pending`

## 1. Модель публикации

Эта редакция `0.46.0` сохраняет полное содержание дорожной карты `0.45.0` по immutable git blob и публикует только новое состояние AC-602…AC-604 и handoff в AC-605.

Предыдущая редакция:

- версия: `0.45.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `89ba3b2bb361d7101adbb3ec63d1b8ebbacde312`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601 selection, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. AC-602 — complete

`AC-602 — Position business case and unit-economics/workload evidence` получает статус:

**`Complete / PASS for bounded pilot baseline`.**

Canonical artifact:

`docs/business/AC-602-POS-004-BUSINESS-CASE.md`.

AC-602 не заявляет исторические часы, экономию, прибыльность или положительный ROI. Pilot должен измерять real Owner interventions, attempts/rework, tests/checks и observable runtime/tool cost на реальных задачах.

## 3. AC-603 — complete

`AC-603 — Assignment, authority, runtime, tools and data boundary` получает статус:

**`Complete / PASS for bounded pilot implementation`.**

Создан persistent pilot Principal:

**`AI-ENG-001`**

для:

**`POS-004 — Engineering & Release Lead`.**

Canonical Assignment/runtime artifact:

`docs/organization/AC-603-AI-ENG-001-ASSIGNMENT-RUNTIME-BOUNDARY.md`.

Initial replaceable runtime:

- Owner-controlled Mac mini target;
- Python standard-library supervisor in `ai_workforce/ai_eng_001/**`;
- OpenCode CLI as coding executor;
- optional OpenAI-compatible manager LLM, disabled by default;
- local git worktree isolation;
- launchd user-service deployment helper;
- file-based run evidence and queue.

Autonomous pilot authority stops at `READY_FOR_OWNER`. `AM-3` and `AM-4` remain inactive. Commit requires explicit Owner `approve`; remote push additionally requires explicit `--push`. No automatic merge/release/deploy/customer effect exists.

## 4. AC-604 — complete

`AC-604 — Quality/evaluation, cost and risk gates` получает статус:

**`Complete / PASS for pilot gates`.**

Canonical gate artifact:

`docs/operations/AC-604-AI-ENG-001-QUALITY-COST-RISK-GATES.md`.

Implementation evidence:

`docs/operations/AI-ENG-001-PILOT-RUNTIME-IMPLEMENTATION-EVIDENCE.md`.

Cross-review:

`docs/reviews/AC-602-604-AI-ENG-001-PILOT-CROSS-REVIEW.md` — `7/7 PASS`.

Owner decision:

`docs/governance/decisions/DECISION-2026-08-30-AC-602-604-AI-ENG-001-PILOT.md`.

Implementation-environment validation:

- `4 tests / 4 PASS`;
- Python `py_compile` PASS;
- deployment shell syntax `bash -n` PASS.

These are runner-mechanics evidence only. They do not prove OpenCode/model quality, Mac mini deployment, customer readiness or positive economics.

## 5. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / bounded early admission`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Current / deployment + real-task evidence pending` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned / blocked on AC-605 evidence` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / blocked on AC-605/606 evidence` |

## 6. AC-605 exact next evidence

AC-605 may advance only from real Owner-controlled runtime evidence. Minimum next evidence:

1. clone/update `arvectum-company` on the Mac mini;
2. run the supplied macOS installer and `doctor`;
3. confirm the installed OpenCode CLI is available to the launchd runtime;
4. submit one low-risk bounded real product task through AI-ENG-001;
5. capture run state, baseline SHA, changed paths, declared test results, executor logs and Owner intervention count;
6. if `READY_FOR_OWNER`, perform human review; promotion remains explicit;
7. record any rework, runtime/model cost where observable and failures/escalations honestly.

A synthetic task can validate installation but cannot by itself complete the supervised real-position pilot.

## 7. M5 remains open

AC-602…AC-604 do not close or bypass M5.

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with its existing customer evidence gates preserved from roadmap 0.45.0/0.44.0.

## 8. Authority and readiness boundary

The existence of AI-ENG-001 code does not itself create production readiness, profitability, customer acceptance, new budget, new credentials, legal/corporate authority, AM-3/AM-4, autonomous consequential external effects or Arvectum OS lifecycle changes.

The pilot is intentionally reversible. OpenCode, the manager LLM and the Mac mini runtime are replaceable execution means rather than sources of Organizational Authority.
