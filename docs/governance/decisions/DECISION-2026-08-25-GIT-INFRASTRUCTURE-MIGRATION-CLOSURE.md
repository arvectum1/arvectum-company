# DECISION-2026-08-25 — Git infrastructure migration closure

Status: `Approved`
Decision date: `2026-08-25`
Decision authority: `Owner of ООО «Арвектум»`
Scope: Company-wide Git repository hosting, mirroring and workstation recovery baseline
Related operational baseline: `docs/operations/GIT-INFRASTRUCTURE-BASELINE-v1.0.0.md`

## Decision

The Git infrastructure recovery and migration episode caused by loss of access to the previous GitHub account is closed.

Approved operating state:

- GitHub `arvectum1/*` is the canonical PRIMARY repository hosting contour;
- GitVerse `arvectum/*` is the canonical MIRROR contour;
- canonical default branch is `main`;
- all 9 canonical repositories are reconciled and mirrored successfully;
- Windows, Mac mini and MacBook committed histories have been reconciled;
- recovery/archive evidence remains preserved and is not canonical development state;
- normal development continues from GitHub `main`.

Canonical repositories:

1. `arvectum-os`
2. `arvectum-company`
3. `arvectum-landing`
4. `tender-agent`
5. `data-platform`
6. `proxy-launcher`
7. `discount-parser`
8. `doors_parser`
9. `creative-test-agent`

## Verified closure state

At closure:

- GitHub and GitVerse `main` SHA values match for all 9 repositories;
- branch refs match for all 9 repositories;
- tag refs match for all 9 repositories;
- GitHub default branch is `main` for all 9 repositories;
- GitVerse default branch is `main` for all 9 repositories;
- no canonical remote `master` branch remains;
- canonical `Mirror to GitVerse` workflow is present and successful for all 9 repositories;
- `GITVERSE_TOKEN` is configured for all 9 GitHub repositories;
- `GITVERSE_REPO` matches the target repository name for all 9 repositories.

## Credential risk disposition

A prior local embedded GitVerse credential reference was removed from the identified local recovery configurations and shell history. No remaining literal GitVerse credential was found in the scanned repository files and standard local credential/history locations.

The Owner explicitly chooses **not to rotate the currently configured GitVerse token at this time**.

This is an accepted bounded operational risk, not a claim that compromise has been cryptographically disproven. Token rotation is deferred and does not block normal development or closure of the migration episode.

## Reopen trigger

This incident/recovery topic should remain closed unless one of the following occurs:

- the current GitHub account or canonical repositories become unavailable or blocked;
- GitHub → GitVerse mirroring materially fails;
- repository authority or branch history diverges;
- a credential event requires rotation or recovery;
- an explicit Owner decision reopens the infrastructure baseline.

If a future GitHub account migration is required, repository authority must be reconciled before changing the PRIMARY contour.

## Result

`GIT INFRASTRUCTURE MIGRATION COMPLETE — 9/9.`

No further work is authorized by this decision merely for cleanup or additional infrastructure completeness.
