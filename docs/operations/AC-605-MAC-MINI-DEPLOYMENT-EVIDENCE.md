# AC-605 — Mac mini Deployment Evidence

Status: `Deployment proof complete / real supervised product-task proof pending`
Date: `2026-08-30`
Position: `POS-004 — Engineering & Release Lead`
Principal: `AI-ENG-001`
Roadmap item: `AC-605 — Supervised AI Position pilot`

## 1. Scope

This record captures the first Owner-controlled Mac mini deployment evidence for `AI-ENG-001` and the portability fix discovered during that deployment.

It does **not** close AC-605. A synthetic smoke task proves deployment/runtime mechanics, not a real supervised Position outcome on product work.

## 2. Owner-controlled Mac mini evidence

The deployment report supplied from the Mac mini recorded:

- AI-ENG-001 deployment complete;
- AI-ENG-001 running on the Mac mini;
- `py_compile`: PASS;
- targeted AI-ENG-001 tests: `4/4 PASS`;
- synthetic smoke final state: `READY_FOR_OWNER`;
- synthetic smoke checks: `5/5 PASS`;
- canonical `main` left unchanged during local diagnosis;
- deployment branch working tree clean;
- no real product task executed;
- no merge, release or customer effect performed by AI-ENG-001.

These Mac mini execution facts are recorded from the Owner-controlled local deployment report. They are not reconstructed from GitHub CI.

## 3. Deployment defect found

Root cause discovered during real Mac mini execution:

`opencode run` was invoked without an explicit `--dir` argument. The coding LLM could therefore resolve repository-relative paths against the canonical Company checkout rather than the task's isolated git worktree.

Local bounded fix:

```python
cmd += ["--dir", str(worktree)]
```

The fix was committed on:

`work/ac-605-mac-mini-deploy`

Commit:

`f08b2a7f4101cf73ea0896ca353eb72c332f7a1b`

## 4. Independent GitHub verification

Remote review verified that the branch was exactly one commit ahead of `main`, zero commits behind, and changed exactly one file with one insertion:

`ai_workforce/ai_eng_001/core.py`

The actual diff added only the OpenCode `--dir <worktree>` argument before prompt injection.

Pull request:

`#1 — AC-605 — fix OpenCode worktree directory invocation`

PR CI:

- `AI-ENG-001 CI` run `33301128677`;
- compile: PASS;
- unit/integration tests: PASS;
- shell syntax: PASS;
- overall runner-mechanics job: `success`.

The PR was mergeable and was promoted to canonical `main` after review.

Merge commit:

`6e8df32168bc665b8aac288a5b828379122918d3`

Current canonical `core.py` on `main` includes the `--dir` worktree binding.

## 5. Authority-boundary evidence

The synthetic result `READY_FOR_OWNER` remains a review gate only.

The deployment proof does not activate AM-3 or AM-4 and does not authorize autonomous:

- commit promotion;
- remote push;
- merge;
- release;
- deploy;
- customer acceptance;
- customer-system changes;
- product-scope changes;
- Reserved Owner Decisions.

No separate manager LLM was required for this proof.

## 6. Result

Deployment result:

**PASS — AI-ENG-001 deployed on the Owner-controlled Mac mini and synthetic smoke validated.**

Implementation portability result:

**PASS — the discovered OpenCode worktree-directory defect was minimally fixed, independently CI-validated and promoted to `main`.**

AC-605 result:

**OPEN — first real low-risk supervised product-task evidence is still required.**

## 7. Next evidence

The next AC-605 step is to select exactly one real, low-risk product engineering task with:

- clear product ownership;
- bounded scope;
- explicit acceptance criteria;
- no customer external effect;
- no material spend;
- no raw-secret requirement;
- no Company/Product/OS boundary change;
- reversible git-based output;
- meaningful tests or equivalent objective validation.

AI-ENG-001 should execute that task through the deployed Mac mini runtime, stop at `READY_FOR_OWNER`, and preserve run evidence including Owner interventions/rework.
