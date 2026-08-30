#!/bin/bash
set -euo pipefail
PLIST_PATH="$HOME/Library/LaunchAgents/com.arvectum.ai-eng-001.plist"
launchctl bootout "gui/$(id -u)" "$PLIST_PATH" >/dev/null 2>&1 || true
rm -f "$PLIST_PATH"
echo "AI-ENG-001 launch agent removed. State/config preserved."
