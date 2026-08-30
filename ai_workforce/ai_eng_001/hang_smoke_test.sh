#!/bin/bash
set -euo pipefail

REPO_PATH="${1:-$(pwd)}"
TMP="$(mktemp -d /tmp/ai-eng-001-hang.XXXXXX)"
trap 'rm -rf "$TMP"' EXIT
SOURCE="$TMP/source"
STATE="$TMP/state"
MARKER="$TMP/SHOULD_NOT_EXIST"

mkdir -p "$SOURCE"
git -C "$SOURCE" init -q
git -C "$SOURCE" config user.email "ai-eng-001-smoke@local"
git -C "$SOURCE" config user.name "AI-ENG-001 Smoke"
printf 'original\n' > "$SOURCE/file.txt"
git -C "$SOURCE" add file.txt
git -C "$SOURCE" commit -qm init

cat > "$TMP/executor.sh" <<EOF
#!/usr/bin/env python3
import subprocess
import time
from pathlib import Path
child = subprocess.Popen(["sleep", "30"])
Path("$TMP/child.pid").write_text(str(child.pid))
time.sleep(30)
EOF
chmod +x "$TMP/executor.sh"
cat > "$TMP/config.json" <<EOF
{"state_dir":"$STATE","executor_cmd":["$TMP/executor.sh"],"llm_mode":"none","executor_idle_timeout_seconds":2}
EOF
cat > "$TMP/task.json" <<EOF
{"id":"HANG-SMOKE","repository":"$SOURCE","objective":"synthetic hang","acceptance":["must block"],"test_commands":["touch $MARKER"],"allowed_paths":["file.txt"],"timeout_seconds":60}
EOF

(cd "$REPO_PATH" && python3 -m ai_workforce.ai_eng_001.cli --config "$TMP/config.json" run "$TMP/task.json") > "$TMP/run.json" &
runner_pid=$!
sleep 1
(cd "$REPO_PATH" && python3 -m ai_workforce.ai_eng_001.cli --config "$TMP/config.json" status) > "$TMP/running-status.json"
python3 -c 'import json,sys; assert any(r.get("phase") == "EXECUTOR_RUNNING" and r.get("executor_pid") for r in json.load(open(sys.argv[1]))["runs"])' "$TMP/running-status.json"
set +e
wait "$runner_pid"
code=$?
set -e
test "$code" -eq 3
RUN="$(printf '%s\n' "$STATE"/runs/*)"
test -f "$RUN/runtime-status.json"
test -f "$RUN/executor.stdout.txt"
test -f "$RUN/executor.stderr.txt"
test ! -e "$MARKER"
test "$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["executor_termination_reason"])' "$RUN/report.json")" = "executor_idle_timeout"
test "$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["termination_reason"])' "$RUN/runtime-status.json")" = "executor_idle_timeout"
CHILD="$(cat "$TMP/child.pid")"
if kill -0 "$CHILD" 2>/dev/null; then
  echo "child process still alive: $CHILD" >&2
  exit 1
fi
test "$(git -C "$SOURCE" status --short)" = ""
test "$(cat "$SOURCE/file.txt")" = "original"
TERMINAL_STATUS="$(cd "$REPO_PATH" && python3 -m ai_workforce.ai_eng_001.cli --config "$TMP/config.json" status)"
test "$(python3 -c 'import json,sys; print(json.load(sys.stdin)["runs"][0]["state"])' <<< "$TERMINAL_STATUS")" = "BLOCKED"
echo "AI-ENG-001 hang smoke PASS"
