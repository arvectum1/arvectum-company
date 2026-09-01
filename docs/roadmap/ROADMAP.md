# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.55.0`
Создано: `2026-08-19`
Обновлено: `2026-09-01`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее M6-действие: `AC-606 — Human/software fallback and executor-replacement proof — next Company execution step`

## 1. Модель публикации

Эта редакция `0.55.0` сохраняет полное содержание дорожной карты `0.54.0` по immutable git blob и фиксирует закрытие Product TLS/source blocker и успешный реальный Tender Agent E2E на Mac mini.

Предыдущая редакция:

- версия: `0.54.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `dac57ba7fd2bd2f189546b9a6093fd62f7bdd993`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-605 state, runtime-observability promotion, execution-only promotion, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. Tender Agent Product E2E — real Mac mini PASS

Issue:

`arvectum1/tender-agent#19`

Canonical integration PR:

`#21 — E2E: Mac mini autonomous procurement discovery to report`

Superseded draft PR:

`#20`

Accepted source head:

`155f97e563206993f2a315b4e47c9d1391538781`

Merge commit on Tender Agent `main`:

`b07d4eff59c5657dfd6f261437330bfb42b49828`

Runtime acceptance evidence:

`docs/operations/MACMINI_AUTONOMOUS_PROCUREMENT_E2E_ACCEPTANCE.md`

Observed real flow:

`public EIS search → deterministic relevance selection → public documentation intake → completeness gate → local LLM analysis → HTML report`

Acceptance facts:

- focused final regression suite: `54 passed, 9 warnings`;
- repository secret scan: `clean`;
- Product transport: `PRODUCT_TRANSPORT_PASS`;
- TLS: `CERT_REQUIRED`, hostname verification enabled, TLS >= 1.2;
- source-controlled direct route: `true`;
- selected real procurement: `0373100107026000032`;
- relevance threshold `20`: passed;
- run ID: `toa-run-20260901074713-d6bae8`;
- documentation: `5 files downloaded`;
- analysis mode: `llm_tender_operator_provider`;
- local LLM invoked: `true`;
- deterministic fallback: `false`;
- LLM evidence event: `llm_analysis_completed`;
- final marker: `MACMINI_AUTONOMOUS_PROCUREMENT_E2E_REPORT_READY`;
- HTML report SHA256: `6ca3f39b51ee90adb0f5cce626dae504f7b08c87d6398a100bf1daff1a8ec9bf`;
- CI run `#278`: `SUCCESS` on exact accepted head before merge.

## 3. Previous Product blocker is resolved

Roadmap `0.54.0` correctly recorded the then-current blocker:

`EIS public search → TLS verification failed`.

That blocker is now **resolved** for the accepted Mac mini Product contour.

The repository now proves verified public EIS transport, source-controlled direct routing, real procurement selection, public-document intake, local LLM execution and report generation without weakening TLS or introducing cloud dependence.

The earlier blocked run remains valid historical negative evidence and must not be rewritten; this revision records the later successful correction and acceptance.

## 4. What the PASS proves — and what it does not

The accepted Product contour proves an autonomous **read-only intelligence loop** on the Mac mini.

It proves:

- real external public-source reachability;
- deterministic procurement selection;
- real public-document retrieval and completeness progression;
- controlled local LLM invocation without fallback;
- human-facing HTML report generation;
- fail-closed safety and source/TLS controls retained.

It does **not** authorize or prove:

- procurement application submission;
- ETP login;
- captcha bypass;
- digital signature use;
- supplier/customer external messaging;
- legally final autonomous decisions;
- autonomous financial commitments;
- AM-3 or AM-4 authority.

ARV-001 remains separately `CLOSED / FROZEN`; the E2E track did not mutate its accepted evidence baseline.

## 5. M6 status after Product E2E PASS

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / execution mechanics and substantive Product-value evidence proven; continuity/economic proof remains`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Complete / PASS — real Product task, READY_FOR_OWNER, zero Owner interventions` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Available / NEXT Company M6 execution step` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / now has substantive Product E2E evidence; execute after AC-606` |

## 6. Exact next steps

Company sequencing is now:

1. **Execute `AC-606`** — prove bounded human/software fallback and executor replacement without breaking the governed Position contract.
2. **Execute `AC-607`** using the accumulated AC-605 and Tender Agent E2E evidence: Owner workload, execution quality, cost, replacement/continuity, module reuse and whether AI-ENG materially reduces work rather than merely shifting it into supervision.
3. Keep `M5 / AC-505` open in parallel until real external/customer evidence becomes available; do not fabricate it from Product runtime evidence.
4. Treat the merged Tender Agent Mac mini read-only E2E as a Product baseline for subsequent product-value/source expansion, without automatically widening Company autonomy or external-effect authority.

## 7. Owner workload and economic interpretation

The new Product E2E adds materially stronger evidence than the earlier TLS-blocked run: the full intelligence loop reached a real human-facing report with a local LLM and no deterministic fallback.

However, M6 is not yet an economic PASS. AC-607 must count bootstrap/setup effort, debugging time, supervision cost and replacement/fallback behavior alongside the successful zero-intervention execution evidence already recorded under AC-605.

## 8. Authority boundary remains unchanged

Neither the successful Tender Agent E2E nor AC-605 activates AM-3/AM-4 or grants authority to commit/push/merge/release/deploy autonomously, change Product Owner decisions, mutate accepted evidence, perform procurement submission, contact suppliers/customers, log into ETP, use digital signatures, bypass captcha, create external business effects, expand scope or spend money without the existing governed authority path.

## 9. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait`.

M5 and M6 continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
