# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.53.0`
Создано: `2026-08-19`
Обновлено: `2026-08-30`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — Supervised AI Position pilot — external/signal hardening promoted / Mac mini deployment verification pending`

## 1. Модель публикации

Эта редакция `0.53.0` сохраняет полное содержание дорожной карты `0.52.0` по immutable git blob и фиксирует фактический результат первого чистого queued execution-only run, а также последующее generic hardening AI-ENG-001.

Предыдущая редакция:

- версия: `0.52.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `cda45ef3375b35e5877127239c422ccdd58f0756`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-604 state, first AC-605 hang evidence, runtime-observability promotion, execution-only promotion, Owner intervention evidence, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. First clean queued execution-only run — BLOCKED before Product mutation

Run:

`20260830T135816Z-AC605-ARV001-COMPRESSION-EXEC-003`

Product baseline:

`arvectum1/tender-agent@7f63a38227c8cc009c722da820caf3cd05493bd9`

Observed terminal state:

`BLOCKED`

Evidence:

- executor exited `0`;
- AI-ENG observability and post-executor phases worked;
- Git worktree remained clean;
- `requires_changes=false` semantics worked;
- zero Owner execution interventions occurred;
- candidate pre-hashes matched the expected immutable values;
- compression itself was **not run**;
- OpenCode rejected the exact required candidate root through its `external_directory` permission boundary;
- all candidate hashes remained unchanged;
- no Product code, accepted evidence, Product Owner state, independent-review state or freeze state changed.

This result is a runtime capability blocker, not an ARV-001 Product failure.

## 3. Foreground supervisor orphan evidence

During post-promotion verification an accidentally real foreground normal-smoke run was externally terminated by its bootstrap wrapper.

The foreground AI-ENG supervisor disappeared while its separately-sessioned OpenCode executor survived as an orphan (`PPID=1`). The persistent launchd watch was not the parent and could not recover that executor.

Bounded cleanup affected only the orphan executor process group and preserved prior run evidence.

This established a second generic runtime gap: SIGTERM to a foreground supervisor had to enter the same bounded executor cleanup path as KeyboardInterrupt/idle/hard-timeout handling.

## 4. External-directory and supervisor-signal hardening — promoted

Remediation contract:

`docs/operations/AC-605-AI-ENG-001-EXTERNAL-AND-SIGNAL-HARDENING.md`

Implementation branch:

`work/ai-eng-external-supervisor-hardening`

Implementation head:

`aad352935feb2bb6eb21dcf094974c7fb87fb961`

Pull request:

`#4 — AC-605 — harden external-directory access and supervisor shutdown`

Exact-head GitHub CI:

- workflow: `AI-ENG-001 CI`;
- run: `33316389557`;
- compile PASS;
- existing and new unit/integration regressions PASS;
- shell syntax PASS.

PR #4 merged to canonical main.

Merge commit:

`f24e1787c5c00a2464910fa178f90a135c40162d`

Promotion evidence:

`docs/operations/AC-605-AI-ENG-001-EXTERNAL-AND-SIGNAL-PROMOTION-EVIDENCE.md`

Promoted capability now includes:

- CLI `run` and `watch` supervised SIGINT/SIGTERM handling;
- bounded cleanup of only the AI-ENG-created executor process group;
- opt-in task field `external_directories`;
- rejection of broad roots (`/`, `/tmp`, `/private/tmp`, home, Desktop root, Documents root);
- exact narrow OpenCode external-directory permission injected only into the executor process;
- OpenCode 1.x / 2.x permission syntax selection by detected version;
- no blanket `--auto` mode;
- fail-closed conflict with pre-existing inline OpenCode config;
- durable external-directory/signal evidence in run reports.

## 5. Product priority correction

ARV-001 Product work is no longer blocked on AC-605 infrastructure iteration. The Owner may continue the current ARV-001 compression/review loop manually while AI-ENG hardening is verified separately.

Do not create additional runtime work merely to automate a short one-off Product command. The next real autonomous pilot should preferably be a repository-contained engineering task where the automation is expected to reduce Owner workload materially.

The completed BLOCKED ARV-001 queued run remains valid AC-605 evidence and must not be rewritten as a Product failure.

## 6. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / bounded early admission`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Current / external+signal hardening promoted — Mac mini verification pending` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned / blocked on successful real AC-605 Product-task evidence` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / negative and zero-intervention evidence accumulating; blocked on AC-605/606 completion` |

## 7. AC-605 exact next step

After the current manual Product work reaches a convenient pause:

1. fast-forward the Owner-controlled Mac mini `arvectum-company` checkout to current canonical `main`;
2. restart the AI-ENG launchd watch so it loads the promoted supervised adapter;
3. run `doctor`;
4. run synthetic hang smoke;
5. run synthetic normal smoke with `AI_ENG_SMOKE_FAKE_EXECUTOR=1`;
6. run one narrow external-directory synthetic smoke against a disposable temp child directory and verify no interactive OpenCode permission request;
7. only after those gates pass, assign the next real repository-contained engineering task to AI-ENG-001.

A new autonomous run must again measure Owner execution interventions and duration. Technical `READY_FOR_OWNER` remains a human review gate, not Product/customer/business approval.

## 8. Authority boundary remains unchanged

The runtime changes do not activate AM-3 or AM-4 and do not grant autonomous authority to commit, push, merge, release, deploy, change Product Owner decisions, authorize independent review, retry governed provider acceptance, perform EIS/provider/RAG calls, mutate accepted/frozen evidence, mutate production DB, create customer external effects, expand scope, or spend money.

Explicit narrow local filesystem permission is an execution capability, not Organizational Authority.

## 9. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with the existing customer evidence gates preserved from the previous roadmap chain.

M5 and M6 may continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
