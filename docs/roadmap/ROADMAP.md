# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.56.0`
Создано: `2026-08-19`
Обновлено: `2026-09-01`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее M6-действие: `AC-607 — Value, Owner-workload, module-reuse and risk review — NEXT`

## 1. Модель публикации

Эта редакция `0.56.0` сохраняет полное содержание дорожной карты `0.55.0` по immutable git blob и фиксирует завершение `AC-606`.

Предыдущая редакция:

- версия: `0.55.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `81f83269f333ca490daaa056df80f50d300dc39e`.

Все не изменённые ниже решения, границы, master-index M0–M9, M5/AC-505 state, Tender Agent E2E acceptance, AC-601…AC-605 evidence, Company/Product/Arvectum OS boundaries и authority semantics сохраняются по этой immutable reference.

## 2. AC-606 — Complete / PASS

Work item:

`AC-606 — Human/software fallback and executor-replacement proof`

Canonical PR:

`arvectum1/arvectum-company#5`

Accepted final PR head:

`facfa9bd93ae5674f1c23cbd95acdb876c744f92`

Canonical merge commit:

`fe8fca259794eef9af640e4b1baa66f8be3946f7`

Durable evidence:

`docs/operations/AC-606-AI-ENG-001-CONTINUITY-FALLBACK-EXECUTOR-REPLACEMENT.md`

Repository-owned implementation:

- `ai_workforce/ai_eng_001/continuity_probe.py`;
- `tests/test_ai_eng_001_continuity.py`;
- explicit AC-606 step in `.github/workflows/ai-eng-001-ci.yml`.

## 3. Continuity proof result

Accepted recovery sequence:

`primary executor failure → BLOCKED → explicit Owner/human recovery decision → replacement executor → attributable bounded-task resubmission → READY_FOR_OWNER`

The proof deliberately does not implement automatic failover.

Accepted CI/probe evidence:

- implementation/probe head: `6846fe682adbfc50c4e405e44091ff3ac0c8e7f0`;
- `AI-ENG-001 CI` run `#13`: `SUCCESS`;
- compile: PASS;
- unit/integration suite: `17 tests / PASS`;
- explicit continuity marker: `AC606_CONTINUITY_PROBE_PASS`;
- shell syntax checks: PASS.

Observed continuity invariants:

- Principal remains `AI-ENG-001`;
- Position remains `POS-004`;
- primary executor fails closed as `BLOCKED / executor_nonzero_exit`;
- primary produces no promotable changes;
- replacement executor reaches `READY_FOR_OWNER` only after explicit recovery/resubmission boundary;
- task contract is preserved except for the new attributable task ID;
- replacement changes only the declared allowed path;
- baseline SHA is preserved;
- source HEAD and source cleanliness are preserved across both attempts;
- replacement worktree remains uncommitted;
- `automatic_failover=false`;
- `authority_expanded=false`;
- no automatic approval, commit, push, merge, release or deploy occurs.

## 4. What AC-606 proves — and what it does not

AC-606 proves that the governed Position/Principal contract survives a coding-executor failure and explicit software replacement without silently transferring or enlarging authority.

The human fallback is an explicit decision boundary. After a failed executor, the Owner may select a replacement executor, defer the task, or perform it outside the AI Position process under normal human authority. No automatic repair/retry is treated as Owner approval.

AC-606 does **not** prove:

- equal engineering quality across every model/vendor/tool;
- unattended automatic failover;
- autonomous commit/push/merge/release/deploy;
- AM-3 or AM-4 authority;
- customer/business acceptance;
- economic success of M6 by itself.

## 5. M6 current status

`M6 — First real AI-held Position proven economically and operationally` is now:

**`Current / execution, substantive Product value, and continuity mechanics proven; final value/economic review remains`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Complete / PASS — real Product task, zero Owner execution interventions after enqueue` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Complete / PASS — continuity mechanics proven` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `NEXT — evidence set now sufficient for final M6 review` |

## 6. Exact next step — AC-607

Execute `AC-607` now using the accumulated evidence set rather than adding another runtime proof merely for volume.

The review must evaluate at minimum:

1. Owner workload actually removed versus work shifted into setup/supervision/recovery;
2. execution quality and fail-closed behavior across positive and negative runs;
3. known/unknown cost evidence — missing provider cost must remain `unknown`, never be rewritten as zero;
4. continuity and executor-replacement evidence from AC-606;
5. reuse value of the AI-ENG runtime across Product modules rather than one Tender Agent case;
6. operational and authority risks that remain;
7. whether M6 can be closed as PASS, requires another bounded evidence item, or should remain open with explicit conditions.

AC-607 must count bootstrap/setup effort and repeated debugging honestly. The successful Tender Agent Mac mini E2E and zero-intervention execution evidence are positive inputs, not permission to omit costs or supervision burden.

## 7. Parallel M5 state

`M5 — First real governed Company operating contour proven` remains `Current`.

`AC-505` remains `Current / external evidence wait` until actual external/customer evidence exists. M5 evidence must not be fabricated from M6/Product runtime evidence.

## 8. Authority boundary remains unchanged

AC-606 does not activate AM-3/AM-4 and does not grant autonomous authority to commit, push, merge, release, deploy, change Product Owner decisions, mutate accepted evidence, submit procurement applications, contact suppliers/customers, log into ETP, use digital signatures, bypass captcha, create external business effects, expand scope or spend money outside the existing governed authority path.

`READY_FOR_OWNER` remains the terminal autonomous promotion state for this pilot contour.
