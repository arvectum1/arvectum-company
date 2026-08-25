# Git Infrastructure Baseline

## Status

Approved operational baseline  
Version: 1.0.0  
Date: 2026-08-25  
Owner: ООО «Арвектум»

## Canonical topology

```text
Developer workstation
        ↓
GitHub arvectum1/<repo>
        PRIMARY
        ↓
GitHub Actions
Mirror to GitVerse
        ↓
GitVerse arvectum/<repo>
        MIRROR
```

## Canonical branch

`main`

## Canonical repositories

- `arvectum-os`
- `arvectum-company`
- `arvectum-landing`
- `tender-agent`
- `data-platform`
- `proxy-launcher`
- `discount-parser`
- `doors_parser`
- `creative-test-agent`

## Mirror contract

- Secret: `GITVERSE_TOKEN`
- Variable: `GITVERSE_REPO`
- Workflow: `.github/workflows/mirror-to-gitverse.yml`

## Rules

1. GitHub is the primary remote.
2. Normal development is pushed to GitHub.
3. GitVerse is the disaster-recovery and sovereignty mirror.
4. Manual pushes to GitVerse are not the normal workflow.
5. `main` is the canonical default branch.
6. The GitVerse mirror reflects GitHub branches and tags.
7. `--force --prune` is permitted only for the controlled GitHub-to-GitVerse mirror.
8. Recovery and archive branches are not canonical development branches.
9. Local copies, chat, and model memory do not replace GitHub canonical history.
10. A Git hosting change requires separate reconciliation before authority changes.

## Recovery history

- 2026-08-23..25: GitHub account migration and recovery.
- Mac mini, MacBook, and Windows histories reconciled.
- `discount-parser` recovered from the `discount-parser-github-mirror` superset.
- GitVerse `main.lock` and `HEAD.lock` cleared by GitVerse support.
- No unique committed history lost.
