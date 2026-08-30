# AC-601 — AI Delegation Candidate Selection Cross-Review

Status: `Complete`
Version: `1.0.0`
Created: `2026-08-30`
Completed: `2026-08-30`
Owner: `ООО «Арвектум»`
Reviewed proposal: `docs/organization/AI-DELEGATION-CANDIDATE-SELECTION.md`
Proposal status/version: `Proposed 0.9.0`
Proposal immutable blob SHA: `b1b37d87a963c717a589c34c74616f5c7e78f585`
Roadmap item: `AC-601`
Iterations: `7 of maximum 7`
Result: `PASS for Owner approval / publication`

## 1. Review objective

Test whether selecting `POS-004 — Engineering & Release Lead` as the first M6 AI-held Position is justified by real workload and current Company governance without inventing demand, authority, economics, access or M5 closure.

The review deliberately tests the proposal from different functional perspectives rather than treating technical AI suitability as sufficient.

## 2. Iteration 1 — Business value and workload reality

Questions:

- Does real workload exist independently of the AI-employee initiative?
- Is there an actual Owner burden that delegation can reduce?
- Is the expected value mechanism plausible without fabricated economics?

Findings:

- AC-104 explicitly records current Owner execution/coordination burden in implementation, task sequencing, repository orchestration, QA exception review, local execution and state reconstruction.
- AC-205 already classifies POS-004 as AI-led, confirming that AI engineering execution is an existing operating pattern rather than a speculative staffing idea.
- The proposal correctly avoids invented hours, savings or profitability and moves quantitative testing to AC-602/AC-605.

Result: `PASS`.

## 3. Iteration 2 — Authority and corporate/legal boundary

Questions:

- Does the selection silently delegate ROD-* authority?
- Does it confuse technical capability with Organizational Authority?
- Does selecting a Position create a Principal, Assignment or legal power?

Findings:

- Proposal preserves AC-202 and AC-203 as hard authority boundaries.
- It explicitly keeps AM-3/AM-4 inactive and does not create a new Principal or Assignment.
- Engineering execution remains separable from customer acceptance, commercial commitment, material risk acceptance, portfolio decisions and Company↔Product↔OS boundary decisions.

Result: `PASS`.

## 4. Iteration 3 — Security, access and sovereignty

Questions:

- Can the first pilot be useful without broad privileged access or raw reusable secrets?
- Does the selection create ambient production/customer-system access?
- Is runtime/vendor choice being mistaken for Position identity?

Findings:

- AC-206 already provides a narrow POS-004 access ceiling suitable for repository/worktree/build/test execution while excluding default organization-wide admin, raw reusable secret, bank/signing and ambient production/customer access.
- The proposal creates no provisioning action.
- Model/runtime neutrality is explicit; technology remains replaceable.

Result: `PASS`.

## 5. Iteration 4 — Operational evidence and quality testability

Questions:

- Can performance be evaluated objectively enough for a first AI-held Position?
- Can failures and rework be detected without relying on the agent's self-report?

Findings:

- Git state, diffs, tests, CI/build/package artifacts, review findings, defect/rework history and escalation behavior provide independent evidence.
- This makes POS-004 materially easier to evaluate than customer persuasion, portfolio judgment, finance or security/risk acceptance.
- Proposal correctly treats technical PASS as insufficient for customer/business acceptance.

Result: `PASS`.

## 6. Iteration 5 — Continuity and replacement

Questions:

- Does the selection create dependence on one model/vendor/session?
- Is a fallback path conceptually available?

Findings:

- AC-207 already states that a POS-004 model/agent/runtime is replaceable and that runtime replacement is not authority transfer.
- Actual runtime-swap evidence remains unproven, which is correctly left as downstream M6 proof rather than assumed solved.
- Repository/evidence-based work is reconstructable more readily than chat/session-only execution.

Result: `PASS`.

## 7. Iteration 6 — Alternative-candidate challenge

Challenge: `POS-002 — Commercial & Customer Lead` may have greater direct revenue leverage and may therefore deserve first place.

Assessment:

- POS-002 is indeed a strong later candidate because customer context, intake, support triage and drafting are real bottlenecks.
- However its useful scope is closer to external effects, customer commitments, ambiguous acceptance and relationship context.
- Choosing POS-004 first does not reject POS-002; it reduces first-pilot consequence while providing cleaner objective evidence and an easier runtime-replacement test.

Challenge: `POS-003 — Portfolio & Product Lead` could reduce the Owner's cross-project scheduling bottleneck more directly.

Assessment:

- POS-003 has substantial value but its highest-value actions frequently approach ROD-04/ROD-09 and strategic prioritization.
- AI synthesis can continue in the existing hybrid Assignment without making it the first fully proven AI-held Position.

Result: `PASS — POS-004 remains preferred first candidate`.

## 8. Iteration 7 — M5 sequencing and final reconciliation

Questions:

- Does starting AC-601 while M5 remains open violate the roadmap's evidence-first logic?
- Does the Owner instruction justify bounded early admission?

Findings:

- Roadmap 0.44.0 prohibited entering M6 merely to keep the roadmap moving or to invent workload.
- Here the relevant workload is independently evidenced by AC-104/AC-205 and active engineering work.
- AC-601 itself is reversible, internal and non-provisioning.
- The Owner explicitly instructed execution of AC-601 after the proposed POS-004 hypothesis was presented.
- M5 remains open; missing customer evidence is not bypassed, and AC-602+ are not automatically authorized merely by this review.

Result: `PASS with bounded sequencing reconciliation`.

## 9. Final review result

Cross-review result:

**`PASS for Owner approval / publication`**.

The reviewed proposal may be approved with `POS-004 — Engineering & Release Lead` as the first M6 AI delegation candidate, subject to these preserved conditions:

1. no new Principal/Assignment/access is created by AC-601 itself;
2. no AM-3/AM-4 activation;
3. no ROD-* delegation;
4. no material spend or new external commitment;
5. M5 remains open;
6. AC-602 must establish the measurable business/workload baseline before AC-603 provisions the actual AI employee runtime/Assignment;
7. POS-002 remains the strongest identified follow-on AI-held candidate, not a rejected function.