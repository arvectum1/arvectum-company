# AC-605 — AI-ENG-001 external-directory and supervisor-signal promotion evidence

Status: PROMOTED / Mac mini deployment verification pending
Date: 2026-08-30

## Triggering evidence

AC-605 produced two runtime findings before Product mutation:

1. an externally terminated foreground smoke lost its foreground AI-ENG supervisor while its separately-sessioned OpenCode executor survived as an orphan;
2. queued run `20260830T135816Z-AC605-ARV001-COMPRESSION-EXEC-003` reached the executor with clean Product/Git state but OpenCode rejected access to the explicitly required external candidate directory under `/private/tmp`.

The ARV-001 candidate hashes remained unchanged, no Product code changed, and no Product Owner/independent-review/freeze state advanced.

## Remediation

Implementation branch:

`work/ai-eng-external-supervisor-hardening`

Selected base:

`18c5a318f2f4b995cbe6074000074d70b2726234`

Implementation head:

`aad352935feb2bb6eb21dcf094974c7fb87fb961`

Repository comparison before merge:

- ahead: 6;
- behind: 0;
- changed files: 6;
- no Product repository changes.

Pull request:

`#4 — AC-605 — harden external-directory access and supervisor shutdown`

Exact-head CI:

- workflow: `AI-ENG-001 CI`;
- run: `33316389557`;
- job: `runner-mechanics`;
- compile: PASS;
- unit/integration suite including supervised regressions: PASS;
- shell syntax: PASS.

PR #4 merged to canonical `main`.

Merge commit:

`f24e1787c5c00a2464910fa178f90a135c40162d`

## Promoted capability

The canonical runtime now:

- routes CLI `run` and `watch` through a supervised execution adapter;
- converts SIGINT/SIGTERM into the existing bounded `supervisor_interrupted` cleanup path while an executor is active;
- terminates only the AI-ENG-created executor process group;
- supports opt-in, explicit `external_directories` task declarations;
- rejects broad local roots such as `/`, `/tmp`, `/private/tmp`, home, Desktop root and Documents root;
- injects narrow OpenCode external-directory permission only into the executor process through `OPENCODE_CONFIG_CONTENT`;
- selects OpenCode 1.x or 2.x permission syntax by detected version;
- does not enable blanket OpenCode `--auto` permission mode;
- refuses to silently overwrite pre-existing inline OpenCode configuration;
- persists external-directory and handled-signal evidence in the run report;
- leaves Git/authority/execution-only/promotion gates unchanged.

## Authority

No AM-3/AM-4 authority was activated. This change does not grant autonomous commit, push, merge, release, deploy, spend, secret access, customer effect, Product Owner approval, independent review, freeze, or scope expansion.

## Remaining gate

Repository promotion is complete. Before the capability is relied on for another real autonomous Product task, the Owner-controlled Mac mini must fast-forward `arvectum-company` to this canonical main (or a later fast-forward), restart the AI-ENG watch, and pass doctor + synthetic hang + synthetic normal smoke. A narrow external-directory smoke should also confirm that the locally installed OpenCode version accepts the generated permission form without interactive approval.
