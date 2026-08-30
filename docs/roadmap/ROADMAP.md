# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.52.0`
Создано: `2026-08-19`
Обновлено: `2026-08-30`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — Supervised AI Position pilot — execution-only mode promoted / Mac mini verification then exact ARV-001 retry`

## 1. Модель публикации

Эта редакция `0.52.0` сохраняет полное содержание дорожной карты `0.51.0` по immutable git blob и публикует promotion generic execution-only task semantics, необходимых для чистого ARV-001 presentation-compression retry без искусственного Git change.

Предыдущая редакция:

- версия: `0.51.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `bb76baf04326b8eab5879cfb2b478e1260481192`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-604 state, first AC-605 hang evidence, runtime hardening promotion, Owner intervention evidence, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. Execution-only task mode — promoted

После runtime observability/hang hardening обнаружен следующий generic contract gap: AI-ENG-001 требовал хотя бы один Git change для `READY_FOR_OWNER`, хотя реальная ARV-001 compression retry является execution-only задачей и по контракту не должна менять код.

Реализован backward-compatible task field:

`requires_changes`

Semantics:

- default/omitted `true` — существующая engineering semantics сохраняется, reviewable Git change обязателен;
- `false` — execution-only mode, успешный run обязан оставить Git worktree clean;
- любое Git изменение при `requires_changes=false` fail closed как `unexpected_changes_in_execution_only_task`;
- execution-only READY_FOR_OWNER не имеет Git candidate и не может быть promoted через `approve_run()`.

Implementation branch:

`work/ai-eng-execution-only-mode`

Implementation commit:

`1cb2ebef6f2cef1b504a85fa9ef51aa59a74b250`

Repository review:

- ahead 1 / behind 0 against base main `2f6e20190152647da0fe5683c0623122b9756e5e`;
- 4 expected Company runtime/docs/test files changed;
- no Tender Agent Product files changed.

Pull request:

`#3 — AI-ENG-001 — support fail-closed execution-only tasks`

Exact-head GitHub CI:

- workflow: `AI-ENG-001 CI`;
- run: `33314133950`;
- job: `runner-mechanics`;
- conclusion: `success`;
- compile PASS;
- unit/integration tests PASS;
- shell syntax PASS.

PR #3 merged to canonical main.

Merge commit:

`d81e08596cee82e433df4ef64d224f1fe03abb3d`

Canonical evidence:

`docs/operations/AC-605-AI-ENG-001-EXECUTION-ONLY-PROMOTION-EVIDENCE.md`.

## 3. Current ARV-001 exact handoff point

Tender Agent PR #18 remains open/draft and Product Owner remains `REJECTED`.

Exact current selected Product head:

`7f63a38227c8cc009c722da820caf3cd05493bd9`

Hosted PR CI:

`#246 — success`.

The current task is execution-only:

`ARV-001 — RETRY HUMAN REPORT COMPRESSION AFTER VALIDATOR-CONTRACT FIX`.

Existing candidate root:

`/private/tmp/arv001-human-decision-20260830112058`

The run must verify exact pre-compression hashes, execute only `scripts.arv001.compress_human_report`, preserve analysis and human-contract hashes, verify post-compression PASS markers and smoke-level presentation contract, copy the resulting review artifacts to the Owner desktop, and stop at `READY_FOR_OWNER`.

No code changes, commit, push, source/EIS run, provider/LLM call, RAG rerun, quality acceptance rerun, source recovery, accepted evidence mutation, merge, Product Owner approval, independent review or freeze are authorized.

## 4. Remaining Mac mini gate

Repository promotion is complete. Before the new real run, the Owner-controlled Mac mini must:

1. fast-forward `arvectum-company` to current canonical `main`;
2. restart the AI-ENG launchd watch process so it loads promoted Python code;
3. pass `doctor`;
4. pass promoted `hang_smoke_test.sh`;
5. pass promoted `smoke_test.sh`;
6. enqueue the exact ARV-001 execution-only task with `requires_changes=false`.

If the executor becomes inactive for the configured idle window, AI-ENG-001 must terminate only that executor process group and return `BLOCKED` evidence automatically.

## 5. Owner workload evidence

AC-605 retains the first-run manual recovery evidence:

- manual recovery intervention count: `1`;
- intervention duration: `unknown / not measured`;
- reason: diagnose and terminate a non-progressing executor while preserving fail-closed state.

The new execution-only run should record additional Owner intervention count and time separately. Passive review after `READY_FOR_OWNER` is a governance gate, not an execution correction.

## 6. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / bounded early admission`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Current / execution-only runtime promoted — exact ARV-001 retry next` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned / blocked on real AC-605 Product-task evidence` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / intervention evidence accumulating; blocked on AC-605/606 completion` |

## 7. AC-605 exact next step

Run Mac mini post-promotion verification and then enqueue the exact ARV-001 compression retry as a new AI-ENG-001 execution-only task based on `7f63a38227c8cc009c722da820caf3cd05493bd9`.

Expected successful terminal state:

`READY_FOR_OWNER`

with zero Git changes, exact hash evidence, compression marker `ARV001_HUMAN_REPORT_COMPRESSED_READY`, Product Owner still `REJECTED`, and review artifacts copied for human inspection.

## 8. Authority boundary remains unchanged

The runtime changes do not activate AM-3 or AM-4 and do not grant autonomous authority to commit, push, merge, release, deploy, change Product Owner decisions, authorize independent review, retry governed provider acceptance, perform EIS/provider/RAG calls, mutate accepted/frozen evidence, mutate production DB or create customer external effects.

`READY_FOR_OWNER` remains a human review gate, not approval.

## 9. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with the existing customer evidence gates preserved from the previous roadmap chain.

M5 and M6 may continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
