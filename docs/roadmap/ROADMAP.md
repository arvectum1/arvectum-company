# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.50.0`
Создано: `2026-08-19`
Обновлено: `2026-08-30`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum1/arvectum-company`

Текущее M5-действие: `AC-505 — Supervised real-operation proof — external evidence wait`
Текущее параллельное M6-действие: `AC-605 — Supervised AI Position pilot — first real execution exposed runtime hang / hardening required before retry`

## 1. Модель публикации

Эта редакция `0.50.0` сохраняет полное содержание дорожной карты `0.49.0` по immutable git blob и публикует фактический результат первой попытки real-task execution и обязательный remediation gate.

Предыдущая редакция:

- версия: `0.49.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `4ae536ff856f3e42b296bf1bff4999fc1ced6588`.

Полный master-index M0–M9, M5/AC-505 evidence state, AC-507 bounded economic direction, AC-601…AC-604 state, Mac mini deployment PASS, ARV-001 task selection, Company priority hierarchy, AC-108 path и Company/Product/Arvectum OS boundaries сохраняются по этой immutable reference, если прямо не изменены ниже.

## 2. AC-605 first real execution — runtime BLOCKED before Product work

Первая реальная попытка через `AI-ENG-001` была запущена на:

**`Tender Agent / ARV-001 — decision-useful document analysis / human-facing report rework`.**

Run ID:

`20260830T111956Z-AC605-ARV001-AUTOREWORK-001`

AI-ENG-001 создал изолированный worktree и запустил OpenCode executor на exact selected ARV-001 branch state. Однако executor не дошёл до repository-owned ARV-001 real-source candidate runner.

Observed before manual recovery:

- OpenCode executor elapsed approximately 39 minutes;
- process sleeping with negligible CPU at final snapshot;
- no child processes;
- no network connection visible for executor PID;
- no worktree changes;
- attempted ARV-001 output root created but empty;
- expected candidate artifacts absent;
- run directory contained only `task.json` and `executor-prompt.txt` because current runtime buffers executor output until process completion.

The Owner terminated the hung foreground AI-ENG run and its executor fail-closed. Post-termination checks proved no surviving child process and no Product worktree mutation.

Canonical evidence:

`docs/operations/AC-605-AI-ENG-001-HANG-FAILURE-EVIDENCE.md`.

This event is classified as **AI-ENG-001 runtime/observability failure**, not as ARV-001 Product failure.

## 3. Required remediation gate

ARV-001 must not be retried through AI-ENG-001 until the runtime satisfies:

`docs/operations/AC-605-AI-ENG-001-RUNTIME-HARDENING.md`.

Required remediation includes:

- streaming executor stdout/stderr to durable run files;
- durable `runtime-status.json` heartbeat/phase state;
- configurable executor idle timeout separate from hard timeout;
- bounded process-group cleanup on idle/hard timeout;
- explicit termination classification;
- no post-executor tests after failed/hung executor with no reviewable changes;
- deterministic regression coverage for hang/streaming/process cleanup behavior.

Default pilot executor idle timeout target: `600` seconds.

After code promotion and Mac mini deployment, a synthetic hanging-executor smoke is required before the real ARV-001 retry.

## 4. Owner workload evidence

The first real task already produced useful economic/operational evidence:

- manual recovery intervention count: `1`;
- intervention duration: `unknown / not measured`;
- intervention reason: diagnose and terminate a non-progressing executor while preserving fail-closed state.

This is negative evidence against the desired low-intervention loop and must remain part of AC-607 value/Owner-workload review rather than being discarded as a test artifact.

## 5. M6 current status

`M6 — First real AI-held Position proven economically and operationally` remains:

**`Current / bounded early admission`.**

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Complete / PASS — POS-004 selected` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Complete / PASS — pilot baseline` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Complete / PASS — AI-ENG-001 pilot implemented` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Complete / PASS — pilot gates` |
| `AC-605` | Supervised AI Position pilot | `Current / runtime BLOCKED — executor observability/hang hardening required` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned / blocked on real AC-605 task evidence` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned / already accumulating intervention evidence; blocked on AC-605/606 completion` |

## 6. AC-605 exact next step

Implement and verify the AI-ENG-001 runtime hardening in `arvectum1/arvectum-company` without changing authority boundaries or Tender Agent Product behavior.

Promotion gate:

1. focused Python/unit tests PASS;
2. synthetic idle-hang regression proves fail-closed termination and evidence preservation;
3. existing AI-ENG synthetic smoke PASS;
4. Mac mini runtime updated and doctor PASS;
5. only then repeat the ARV-001 real-task run from the exact current Product branch state.

The repeated ARV-001 run must remain a new immutable execution; failed attempt evidence is preserved and must not be overwritten.

## 7. Authority boundary remains unchanged

The runtime remediation does not activate AM-3 or AM-4 and does not grant autonomous authority to commit, push, merge, release, deploy, change Product Owner decisions, authorize independent review, retry governed provider acceptance, perform EIS/provider/RAG calls, mutate accepted/frozen evidence, mutate production DB or create customer external effects.

`READY_FOR_OWNER` remains a human review gate, not approval.

## 8. M5 remains open

`M5 — First real governed Company operating contour proven` remains `Current` and `AC-505` remains `Current / external evidence wait` with the existing customer evidence gates preserved from the previous roadmap chain.

M5 and M6 may continue to produce independent evidence in parallel and MUST NOT borrow or fabricate evidence from one another.
