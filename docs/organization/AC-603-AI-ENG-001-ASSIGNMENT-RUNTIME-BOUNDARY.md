# AC-603 — AI-ENG-001 Principal, Assignment, Runtime, Tools and Data Boundary

Status: `Approved / pilot Assignment`
Version: `1.0.0`
Date: `2026-08-30`
Owner: `ООО «Арвектум»`
Position: `POS-004 — Engineering & Release Lead`
Principal: `AI-ENG-001`

## Principal

Create persistent Company Principal identifier `AI-ENG-001` for the first POS-004 pilot. The identifier is not a model, vendor, OpenCode session or machine.

## Assignment

`AI-ENG-001` is assigned only to bounded engineering execution during M6 pilot evidence collection. Permitted work stays inside existing `AM-0 / AM-1 / AM-2` semantics. `AM-3` and `AM-4` remain inactive.

The Assignment may prepare an engineering plan from supplied task evidence; create isolated local worktrees/branches; execute bounded edits and declared tests through the configured coding executor; make bounded technical choices needed for a pre-decided task when they do not alter scope, commitments, material dependencies, data/security boundaries or reserved decisions; classify a run from observable evidence; and prepare durable run evidence.

It may not autonomously commit, push, merge, release, deploy, contact customers or create external commitments. Commit/push are separate explicit Owner commands in the pilot runtime.

## Runtime

Initial target: Owner-controlled Mac mini. Runtime package: `ai_workforce.ai_eng_001` in the Company repository. Local state: `~/.local/share/arvectum/ai-eng-001`. Service mode: user `launchd` agent. Coding executor: OpenCode CLI through `opencode run`. Separate manager LLM: optional OpenAI-compatible endpoint, disabled by default.

Canonical product implementation truth remains in each target product repository rather than runtime state.

## Task admission

Every task is an attributable JSON record with objective, acceptance criteria, target repository and explicit protected-boundary flags. Any true protected flag causes fail-closed `NEEDS_OWNER` before coding execution: `requires_owner_decision`, `external_customer_effect`, `material_spend`, `requires_raw_secret`, `changes_company_product_os_boundary`, or `changes_scope_or_commitment`.

After Owner resolution, a corrected/re-scoped new task record is required.

## Access and secrets

The runtime is designed for repository/worktree/build/test access only. No standing right is created to bank/signing systems, Owner general mailbox, customer production systems, organization-wide administration or reusable secret values.

An optional manager LLM key is read from an environment variable and removed from the environment passed to the coding executor. Repository files and task prompts must not contain reusable secrets.

## Promotion boundary

Normal autonomous execution stops at `READY_FOR_OWNER`. The Owner may explicitly run `approve RUN_ID` to stage and commit the candidate locally. Remote branch push additionally requires an explicit `--push` flag. No automatic merge/release/deploy path exists in the pilot.

## Continuity

Position and Principal identity remain stable when OpenCode/model/runtime changes. Run evidence is file-based and reconstructable outside one LLM session. Runtime replacement does not transfer or broaden authority.

## Result

`AC-603 — Complete / PASS for bounded pilot implementation`.

Operational proof requires deployment and real tasks under AC-605.
