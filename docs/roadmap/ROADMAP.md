# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.44.0`
Создано: `2026-08-19`
Обновлено: `2026-08-22`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`
Текущее каноническое действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Параллельное экономическое направление: `AC-507 — Complete / PASS — CONTINUE WITH CHANGE / bounded evidence phase`
Завершено параллельно: `AC-506 — Complete / PASS`

## 1. Модель публикации

Эта редакция `0.44.0` сохраняет полное содержание дорожной карты `0.43.0` по immutable git blob и меняет только то, что подтверждено новым attributable Owner decision по AC-507.

Предыдущая редакция:

- версия: `0.43.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `0af2ca1f9eaeff7cd7bb1b7fd66749b4f5248ae2`.

Полный master-index M0–M9, Company priority hierarchy, available execution paths, Company/Product/Arvectum OS boundaries, AC-108 bounded discovery loop, AC-501…AC-506 evidence и AC-901 сохраняются по этой immutable reference, если прямо не изменены ниже.

Chat может использоваться как основной рабочий/control thread, но durable planning/decision state остаётся в repository artifacts.

## 2. AC-507 — Owner decision recorded

Owner explicitly approved at `2026-08-22T11:10:00+03:00`:

**`AC-507: CONTINUE WITH CHANGE — bounded evidence phase — утверждаю`**.

Decision artifact:

`docs/governance/decisions/DECISION-2026-08-22-AC-507-APPROVAL.md`.

Approved publication:

`docs/business/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW-v1.0.0.md`.

Reviewed proposal:

- `docs/business/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW.md`;
- `Proposed 0.9.0`;
- blob `fa25d369a604b3f8a0989e2250ff742f347690ed`.

Cross-review:

- `docs/reviews/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW-CROSS-REVIEW.md`;
- `10 of 10`;
- `PASS for Owner decision gate`;
- blob `425b7147c5fca2f63d995cbf0c5269b91083d01e`.

`AC-507` is now:

**`Complete / PASS — approved bounded economic direction`.**

## 3. Approved direction

The Company continues `WF-M5-001` in a **bounded evidence phase**.

Binding direction:

1. preserve CL-3/W11 fail-closed behavior;
2. preserve current POS-002/POS-004 authority, data, customer and access boundaries;
3. keep AM-3/AM-4 inactive;
4. linked-successor recovery is used only on genuinely new attributable evidence;
5. on the next qualifying real case, capture lightweight Owner intervention count/minutes where practical;
6. capture coarse engineering effort avoided/incurred where practical;
7. capture cycle/rework and tool/runtime cost only where actual evidence exists;
8. test whether W1/W2 evidence-handling ceremony can be simplified without losing control;
9. prefer stronger real work evidence over building more governance/software infrastructure;
10. defer CRM/workflow-service/database/platformization, cross-product generalization and new OS capability work until stronger evidence exists.

The direction is reversible.

## 4. What AC-507 did not establish

AC-507 approval does **not** prove:

- profitability;
- revenue or margin uplift;
- reduced total delivery cost;
- improved customer satisfaction;
- quantified engineering savings;
- cross-product transferability worth platformization;
- justification for AM-4 or autonomous customer effects.

Unknown cost/value remains unknown rather than zero.

No material budget is created. Any later material spend remains subject to applicable ROD-02 controls.

## 5. AC-505 remains open

`AC-505 — Supervised real-operation proof` remains:

`Current / external evidence wait`.

Real case:

`WF-M5-001-20260821-AC505001`.

Current factual state:

`CL-3 — Evidence insufficient / not reproduced`
→
`W11 — unknown / customer-evidence follow-up required`.

No POS-004 correction is admitted and no customer acceptance is inferred.

Current valid evidence that can move the existing customer contour includes one or more of:

- exact affected build/version;
- exact source/settings/environment sufficient for reproduction;
- current reproduction result;
- explicit new customer validation/rework evidence.

A different real customer feedback item may be selected if it can progress further through WF-M5-001 without expanding scope/authority/data boundaries.

## 6. AC-506 remains complete

`AC-506 — Incident, uncertain-outcome, recovery and fallback drill` remains `Complete / PASS`.

Its bounded evidence remains:

- W11 successor recovery mechanics → `CE-3`;
- case-state/manual fallback reconstruction → `CE-3`;
- helper/process portability → `CE-3`;
- real insufficient-evidence fail-closed behavior → `CE-2`.

This still does not prove actual POS-004 AI model/runtime swap, Company-wide DR, Owner-independent commercial/legal continuity, credential/signing/provider recovery or customer-system recovery.

## 7. M5 status

`M5 — First real governed Company operating contour proven` remains:

**`Current`**.

M5 is not closed by AC-507 approval.

Current Phase 5 status:

| ID | Work item | Status |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Complete / PASS` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Complete / PASS` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Complete / PASS` |
| `AC-504` | Bounded workflow implementation | `Complete / PASS` |
| `AC-505` | Supervised real-operation proof | `Current / external evidence wait` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Complete / PASS` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Complete / PASS — CONTINUE WITH CHANGE` |

M5 can close only when combined evidence is sufficient, including real operation/customer outcome evidence, uncertainty/recovery evidence, Owner burden, technical/AI quality-cost-reliability evidence where applicable, and the now-authorized AC-507 economic direction.

## 8. Master milestone status

- `M0 — Company canonically founded` — `Complete / PASS`;
- `M1 — Business/economic reality and first market-validation plan captured` — `Complete / PASS`;
- `M2 — Reference operating model and authority established` — `Complete / PASS`;
- `M3 — Product/module-candidate portfolio governed as investments` — `Complete / PASS`;
- `M4 — Owner control and reference-implementation observability established` — `Complete / PASS`;
- `M5 — First real governed Company operating contour proven` — `Current`;
- `M6 — First real AI-held Position proven economically and operationally` — `Planned`;
- `M7 — First external AI-company design-partner deployment proven` — `Future`;
- `M8 — Repeatable multi-customer AI-company product proven and scalable` — `Future`;
- `M9 — Final human-readable Russian reconciliation` — `Future`.

Detailed M0–M9 work-item index remains preserved from roadmap `0.43.0` by immutable blob reference above.

## 9. Available implementation paths now

### A. Canonical empirical M5 path

Resume AC-505 on the first valid new/recovered authoritative evidence or select another qualifying real customer feedback case.

On the next qualifying case, apply the approved AC-507 bounded evidence measurements rather than expanding infrastructure.

### B. Parallel business-evidence work

The already-approved AC-108 design-partner discovery loop may run when suitable candidate access exists. This is market evidence, not automatic pilot/customer commitment.

Current real product/client work may continue in its own repositories where it produces revenue, customer value, obligation closure or material evidence.

Portfolio review/cadence may execute under existing M3/M4 governance when new evidence materially changes priorities.

### C. Independent Arvectum OS work

Arvectum OS roadmap work may continue independently. Company must not create hidden cross-repository commitments.

AC-503 remains:

`NO-ADDITIONAL-OS-RELIANCE` for the first M5 proof.

### D. M6 boundary

`AC-601 — AI delegation candidate selection from real workload` remains the first planned M6 step, but **M6 is not admitted merely by AC-507 approval**.

M6 should begin only when M5 evidence is sufficient to identify a real delegation candidate with credible workload/economic/control evidence rather than invented demand.

Earlier possible AC-508 remains inactive and must be explicitly re-admitted/re-scoped before execution.

## 10. Stop/reconsider criteria for the bounded evidence phase

Reconsider the approved direction when evidence shows one or more of:

- governance handling cost materially exceeds avoided rework/control value;
- customer evidence collection becomes the dominant bottleneck;
- routine low-risk steps repeatedly require Owner interpretation without measurable benefit;
- a materially simpler process achieves equal control;
- real economics do not justify continued workflow support;
- further progress requires material spend, new external commitment, AM-3/AM-4 or unadmitted OS reliance.

## 11. Authority and boundary rule

Roadmap does not create Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant, production approval or OS lifecycle transition.

The AC-507 Owner decision authorizes only the reviewed `CONTINUE WITH CHANGE — bounded evidence phase` direction.

Customer acceptance still requires explicit authoritative customer evidence. Runtime/process recovery does not transfer authority. Synthetic drill evidence may not be represented as real customer evidence.
