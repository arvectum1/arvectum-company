# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.51.0`
Создано: `2026-08-19`
Обновлено: `2026-08-30`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — Supervised AI Position pilot — runtime hardening promoted / Mac mini post-promotion verification pending`

## 1. Модель публикации

Эта редакция `0.51.0` сохраняет полное содержание дорожной карты `0.50.0` по immutable git blob и публикует завершение repository-level remediation/promotion после первого real-task runtime hang.

Предыдущая редакция:

- версия: `0.50.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `cb1dbf3491fd567228b2b86e2beff2fb5890db4e`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-604 state, ARV-001 selection, first failed run evidence, Owner intervention evidence, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. AC-605 runtime hardening — promoted to canonical main

Первый реальный run:

`20260830T111956Z-AC605-ARV001-AUTOREWORK-001`

остался классифицирован как **AI-ENG-001 runtime/observability failure before Product work**, а не как ARV-001 Product failure.

После него был реализован remediation contract:

`docs/operations/AC-605-AI-ENG-001-RUNTIME-HARDENING.md`.

Implementation branch:

`work/ac-605-ai-eng-observability`

Implementation commit:

`ea092fa817ae750970242630b1e8339439f195b4`

Repository review confirmed:

- exactly one commit ahead of the selected base;
- zero commits behind;
- 6 expected Company runtime/docs/test files changed;
- no Tender Agent Product files changed.

Pull request:

`#2 — AC-605 — harden AI-ENG executor observability and hang recovery`

Exact-head GitHub CI:

- workflow: `AI-ENG-001 CI`;
- run: `33311787999`;
- job: `runner-mechanics`;
- conclusion: `success`;
- compile PASS;
- unit/integration tests PASS;
- shell syntax PASS.

PR #2 was merged to canonical `main`.

Merge commit:

`8207f5da0e4b3ed03a2ceed178a122fec199ab66`

Canonical promotion evidence:

`docs/operations/AC-605-AI-ENG-001-HARDENING-PROMOTION-EVIDENCE.md`.

## 3. Promoted runtime capability

The promoted AI-ENG-001 runtime now includes:

- incremental executor stdout/stderr persistence;
- atomic `runtime-status.json` heartbeat and phase state;
- configurable executor idle timeout, default `600` seconds;
- distinct idle and hard timeout classifications;
- executor-only process-group termination and child cleanup;
- explicit `executor_idle_timeout`, `executor_hard_timeout`, `executor_nonzero_exit`, and `supervisor_interrupted` evidence;
- no declared post-executor tests after timeout/non-zero executor result;
- in-progress run visibility through `status`;
- doctor validation of idle-timeout configuration;
- normal and hanging synthetic regression/smoke coverage.

This hardening does **not** claim to identify or fix the underlying reason why OpenCode/model became inactive during the first ARV-001 attempt. It makes the AI Position observable and recoverable when an executor becomes inactive.

## 4. Remaining post-promotion gate

Repository promotion is complete, but the real-task retry remains blocked until the Owner-controlled Mac mini proves the promoted runtime in place.

Required order:

1. fast-forward canonical `arvectum-company` checkout to current `main`;
2. `doctor` PASS with valid executor idle timeout;
3. promoted synthetic hang smoke PASS, including bounded idle termination, child cleanup, preserved runtime status and skipped post-executor tests;
4. promoted normal synthetic smoke PASS;
5. only then start a **new immutable** ARV-001 execution from the exact current Product branch state.

The prior failed run and empty ARV-001 attempt root remain historical evidence and must not be overwritten or reclassified as Product execution.

## 5. Owner workload evidence

The first real-task attempt retains:

- manual recovery intervention count: `1`;
- intervention duration: `unknown / not measured`;
- reason: diagnose and terminate a non-progressing executor while preserving fail-closed state.

The subsequent hardening/promotion does not erase this negative workload evidence. It remains input to AC-607.

## 6. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / bounded early admission`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Current / runtime hardening promoted — Mac mini post-promotion verification pending` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned / blocked on real AC-605 Product-task evidence` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / intervention evidence accumulating; blocked on AC-605/606 completion` |

## 7. AC-605 exact next step

Deploy the promoted `main` runtime on the Owner-controlled Mac mini and execute the synthetic post-promotion verification gate.

If that gate passes, immediately repeat the Tender Agent / ARV-001 real-task pilot as a new run with the same authority restrictions and current exact Product branch state.

The repeated run must now expose live runtime status and durable executor logs. If executor activity ceases for the configured idle window, AI-ENG-001 must fail closed automatically rather than requiring manual process diagnosis.

## 8. Authority boundary remains unchanged

The runtime hardening and promotion do not activate AM-3 or AM-4 and do not grant autonomous authority to commit, push, merge, release, deploy, change Product Owner decisions, authorize independent review, retry governed provider acceptance, perform EIS/provider/RAG calls, mutate accepted/frozen evidence, mutate production DB or create customer external effects.

`READY_FOR_OWNER` remains a human review gate, not approval.

## 9. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with the existing customer evidence gates preserved from the previous roadmap chain.

M5 and M6 may continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
