#!/bin/bash
set -euo pipefail

REPO_PATH="${1:-$(pwd)}"
REPO_PATH="$(cd "$REPO_PATH" && pwd)"
RUNTIME_DIR="$REPO_PATH/ai_workforce/ai_eng_001"
CONFIG_DIR="$HOME/.config/arvectum/ai-eng-001"
CONFIG_PATH="$CONFIG_DIR/config.json"
STATE_DIR="$HOME/.local/share/arvectum/ai-eng-001"
LOG_DIR="$HOME/Library/Logs/Arvectum/AI-ENG-001"
PLIST_PATH="$HOME/Library/LaunchAgents/com.arvectum.ai-eng-001.plist"
TEMPLATE="$RUNTIME_DIR/com.arvectum.ai-eng-001.plist.template"

for cmd in python3 git opencode; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "ERROR: $cmd not found" >&2; exit 2; }
done

mkdir -p "$CONFIG_DIR" "$STATE_DIR/inbox" "$STATE_DIR/processing" "$STATE_DIR/archive" "$STATE_DIR/runs" "$STATE_DIR/worktrees" "$LOG_DIR" "$HOME/Library/LaunchAgents"

if [[ ! -f "$CONFIG_PATH" ]]; then
  python3 - "$RUNTIME_DIR/config.example.json" "$CONFIG_PATH" <<'PY'
import json, pathlib, sys
src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
data = json.loads(src.read_text())
data["state_dir"] = str(pathlib.Path.home() / ".local/share/arvectum/ai-eng-001")
dst.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
PY
fi

PYTHON_BIN="$(command -v python3)"; OPENCODE_BIN="$(command -v opencode)"
PATH_VALUE="$(dirname "$PYTHON_BIN"):$(dirname "$OPENCODE_BIN"):/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
python3 - "$TEMPLATE" "$PLIST_PATH" "$REPO_PATH" "$CONFIG_PATH" "$LOG_DIR" "$PATH_VALUE" <<'PY'
import pathlib, sys
src, dst, repo, config, log_dir, path_value = sys.argv[1:]
text = pathlib.Path(src).read_text()
for key, value in {"__COMPANY_REPO_PATH__": repo, "__CONFIG_PATH__": config, "__LOG_DIR__": log_dir, "__PATH__": path_value}.items():
    text = text.replace(key, value)
pathlib.Path(dst).write_text(text)
PY

plutil -lint "$PLIST_PATH"
launchctl bootout "gui/$(id -u)" "$PLIST_PATH" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$(id -u)" "$PLIST_PATH"
launchctl enable "gui/$(id -u)/com.arvectum.ai-eng-001"
cd "$REPO_PATH"
python3 -m ai_workforce.ai_eng_001.cli --config "$CONFIG_PATH" doctor || true

echo "AI-ENG-001 installed"
echo "Config: $CONFIG_PATH"
echo "State:  $STATE_DIR"
echo "Logs:   $LOG_DIR"
