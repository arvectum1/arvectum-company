# AC-605 — AI-ENG-001 external-directory and supervisor-signal hardening

Status: implementation candidate
Date: 2026-08-30

## Triggering evidence

Two distinct runtime gaps were observed during AC-605 verification before any Product mutation:

1. a foreground normal smoke was externally terminated by its bootstrap wrapper; the AI-ENG foreground supervisor disappeared while its OpenCode executor process group survived as an orphan;
2. the first clean queued ARV-001 execution-only run reached OpenCode successfully but OpenCode rejected access to the explicitly required candidate root under `/private/tmp` through its `external_directory` permission boundary.

The ARV-001 Product candidate remained unchanged and the Product Owner state was not advanced.

## Remediation scope

This change adds a supervised execution adapter around the existing AI-ENG core without expanding organizational authority.

### Supervisor signal handling

The CLI now translates `SIGINT` and `SIGTERM` into `KeyboardInterrupt` while an AI-ENG run is active. The existing core already treats `KeyboardInterrupt` as `supervisor_interrupted` and terminates only the executor process group. This allows externally stopped foreground runs and launchd watch shutdowns to preserve bounded cleanup rather than orphaning the executor.

The watch path is routed through the same supervised adapter. If a shutdown signal arrives while a queued task is executing, the task is allowed to finish fail-closed cleanup/report generation, is archived with its terminal state, and the watch then exits.

### Explicit external-directory capability

A task may declare:

```json
"external_directories": [
  "/private/tmp/example-candidate"
]
```

The field is opt-in and does not change the existing default. The supervisor:

- requires an absolute path;
- canonicalizes the path;
- rejects broad roots such as `/`, `/tmp`, `/private/tmp`, the user home directory, Desktop root, and Documents root;
- permits only the exact declared directory boundaries;
- injects the permission only for the executor process through `OPENCODE_CONFIG_CONTENT`;
- refuses to override a pre-existing inline OpenCode config implicitly;
- records the declared external directories in durable run evidence;
- augments the executor objective with the exact filesystem boundary.

For OpenCode 1.x the supervisor emits the legacy `permission.external_directory` form. For OpenCode 2.x it emits the `permissions` rule-array form. No blanket `--auto` permission mode is introduced.

This permission is a local filesystem execution capability only. It does not grant customer effect, deployment, release, merge, push, spend, secret, Product Owner approval, independent review, freeze, or scope-change authority.

## Fail-closed properties

- Tasks without `external_directories` behave as before.
- Broad external roots are rejected before executor launch.
- External-directory tasks require an OpenCode executor whose version can be determined.
- A pre-existing `OPENCODE_CONFIG_CONTENT` conflicts fail closed rather than being silently replaced.
- Git path/change gates remain unchanged.
- `requires_changes=false` continues to require a clean Git worktree and cannot be promoted by `approve_run()`.
- Signal cleanup targets only the executor process group created by AI-ENG.

## Required verification

Repository CI must prove:

- existing AI-ENG regression suite remains green;
- OpenCode 1.x and 2.x external-directory config shapes are generated deterministically;
- broad temp-root authorization is rejected;
- a narrowly declared external directory is injected into the executor environment without changing the source repository;
- SIGTERM delivered to the supervisor produces a bounded `supervisor_interrupted` result and terminates the executor child process group;
- Python compilation and shell syntax checks remain green.

Mac mini post-promotion verification remains required before relying on the new capability for a real autonomous Product task.
