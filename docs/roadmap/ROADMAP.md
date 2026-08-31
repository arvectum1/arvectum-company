# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.54.0`
Создано: `2026-08-19`
Обновлено: `2026-08-31`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — PASS for supervised autonomous Position pilot mechanics; Product TLS/source blocker now owns immediate engineering attention`

## 1. Модель публикации

Эта редакция `0.54.0` сохраняет полное содержание дорожной карты `0.53.0` по immutable git blob и фиксирует первый substantive real Product task, завершённый persistent AI-ENG-001 без Owner execution intervention после enqueue.

Предыдущая редакция:

- версия: `0.53.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `5cb8a68e28a2d3ca4bb5d783f02787f322522cd2`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-604 state, runtime-observability promotion, execution-only promotion, external/signal hardening, prior negative runs, Owner intervention evidence, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. First substantive autonomous Product execution — AI-ENG PASS / Product BLOCKED

Task:

`AC605-MACMINI-PROCUREMENT-E2E-003`

Run:

`20260831T075310Z-AC605-MACMINI-PROCUREMENT-E2E-003`

Product baseline:

`arvectum1/tender-agent@ddf8d2ea4ce785467d683136a1a995ce876a20d8`

AI-ENG terminal state:

`READY_FOR_OWNER`

Runtime evidence:

- duration `79.576s`;
- executor return code `0`;
- termination reason none;
- `changed_paths=[]`;
- `execution_only_worktree_clean` PASS;
- Owner execution interventions after enqueue `0`.

The persistent watch claimed and supervised the queued real Product task, preserved the exact Product baseline and Git cleanliness, collected deterministic evidence and returned the human review gate without execution correction from the Owner.

Canonical evidence:

`docs/operations/AC-605-AI-ENG-001-FIRST-AUTONOMOUS-E2E-EVIDENCE.md`

## 3. Product outcome is not business/E2E success

The Product runner exited `20` with:

`MACMINI_AUTONOMOUS_PROCUREMENT_E2E_BLOCKED`

Code:

`search_not_actionable`

Observed boundary:

- public EIS search outcome `source_unavailable`;
- parser status `blocked`;
- error `TLS verification failed`;
- no procurement selection;
- no documentation/analysis run;
- no local LLM runtime evidence;
- no HTML report.

This is a real Product/source-runtime blocker and MUST NOT be rewritten as AI-ENG failure or as successful Tender Agent business completion.

## 4. AC-605 decision

`AC-605 — Supervised AI Position pilot` is now:

**`Complete / PASS — supervised autonomous Position execution mechanics proven on a real Product task`.**

The proof is bounded:

- real Product workload reached a real external-source boundary;
- zero Owner execution interventions occurred after enqueue;
- fail-closed Product behavior was preserved;
- no automatic repair/retry/scope expansion occurred;
- no Git or external business-effect mutation occurred.

AC-605 does **not** prove:

- Tender Agent end-to-end report generation;
- LLM business usefulness;
- procurement/customer readiness;
- profitability;
- legal/compliance readiness;
- autonomous external-effect authority.

## 5. Business-first priority correction

Do not continue adding AI-ENG preflight gates merely to repeat the same runtime proof.

The immediate engineering blocker belongs to Tender Agent/Product runtime:

`EIS public search → TLS verification failed`.

Company priority therefore returns to Product value: diagnose/fix the Tender Agent source TLS path through the Product repository and then continue the Product E2E workflow.

The AI-ENG `external_directories` capability remains separate technical debt with status:

`NOT VERIFIED`.

It was not needed for the successful repository-contained AC-605 proof and should not block Product delivery.

## 6. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / execution mechanics proven; continuity/economic proof remains`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Complete / PASS — real Product task, READY_FOR_OWNER, zero Owner interventions` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Available / not yet executed; business-first priority may defer behind Product TLS blocker` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / positive zero-intervention evidence now available; final review blocked on AC-606 and additional Product-value evidence` |

## 7. Exact next steps

Company/Product sequencing now is:

1. **Tender Agent owns the immediate engineering next step:** diagnose and correct the Mac mini EIS TLS verification path without weakening TLS verification, bypassing source controls or introducing cloud dependence.
2. After the Product source path is corrected, re-run the same one-command Product E2E through AI-ENG when that re-run is expected to produce new Product evidence rather than merely repeat runtime mechanics.
3. Execute `AC-606` when it no longer competes with higher-value Product delivery work.
4. Use the accumulated AC-605 evidence in `AC-607` to evaluate Owner workload, execution quality, cost, replacement/continuity and whether AI-ENG materially reduces work rather than merely shifting it into supervision.

## 8. Owner workload evidence

Relevant AC-605 evidence now includes both negative and positive cases:

- first non-progressing executor required one manual recovery intervention; duration was not measured;
- subsequent fail-closed blocked runs preserved state and exposed runtime/environment defects;
- first substantive real Product run reached `READY_FOR_OWNER` with `0` Owner execution interventions after enqueue and completed in `79.576s`.

This is positive operational evidence but is not yet sufficient to claim economic success. Bootstrap/setup effort and repeated infrastructure debugging must be included honestly in AC-607 rather than omitted from the cost calculation.

## 9. Authority boundary remains unchanged

The successful AC-605 run does not activate AM-3 or AM-4 and does not grant autonomous authority to commit, push, merge, release, deploy, change Product Owner decisions, authorize independent review, mutate accepted/frozen evidence, perform procurement submission, contact suppliers, log into ETP, use a digital signature, bypass captcha, create customer external effects, expand scope or spend money.

`READY_FOR_OWNER` remains a human review gate, not approval.

## 10. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with the existing customer evidence gates preserved from the previous roadmap chain.

M5 and M6 may continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
