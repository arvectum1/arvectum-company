#!/bin/bash
set -euo pipefail
REPO_PATH="${1:-$(pwd)}"
CONFIG_PATH="${2:-$HOME/.config/arvectum/ai-eng-001/config.json}"
TMP="$(mktemp -d /tmp/ai-eng-001-smoke.XXXXXX)"
if [[ "${AI_ENG_SMOKE_FAKE_EXECUTOR:-0}" = "1" ]]; then
  cat > "$TMP/fake-executor.sh" <<'SH'
#!/bin/sh
printf 'AI-ENG-001 OK\n' > smoke.txt
SH
  chmod +x "$TMP/fake-executor.sh"
  cat > "$TMP/config.json" <<JSON
{"state_dir":"$TMP/state","executor_cmd":["$TMP/fake-executor.sh"],"llm_mode":"none","executor_idle_timeout_seconds":10}
JSON
  CONFIG_PATH="$TMP/config.json"
fi
SMOKE_REPO="$TMP/repo"
mkdir -p "$SMOKE_REPO"
git -C "$SMOKE_REPO" init -q
git -C "$SMOKE_REPO" config user.email "ai-eng-001-smoke@local"
git -C "$SMOKE_REPO" config user.name "AI-ENG-001 Smoke"
printf 'old\n' > "$SMOKE_REPO/smoke.txt"
git -C "$SMOKE_REPO" add smoke.txt
git -C "$SMOKE_REPO" commit -q -m init
cat > "$TMP/task.json" <<JSON
{
  "id": "SMOKE-001",
  "repository": "$SMOKE_REPO",
  "objective": "Change only smoke.txt so its complete content is exactly: AI-ENG-001 OK followed by a newline.",
  "acceptance": ["smoke.txt contains exactly AI-ENG-001 OK and a newline"],
  "test_commands": ["grep -qx 'AI-ENG-001 OK' smoke.txt"],
  "allowed_paths": ["smoke.txt"],
  "forbidden_paths": [".git", ".env"],
  "requires_owner_decision": false,
  "external_customer_effect": false,
  "material_spend": false,
  "requires_raw_secret": false,
  "changes_company_product_os_boundary": false,
  "changes_scope_or_commitment": false,
  "timeout_seconds": 900
}
JSON
cd "$REPO_PATH"
python3 -m ai_workforce.ai_eng_001.cli --config "$CONFIG_PATH" run "$TMP/task.json"
echo "Smoke source repo: $SMOKE_REPO"
echo "The source repo should remain unchanged; inspect the AI-ENG run worktree/report for the candidate."
