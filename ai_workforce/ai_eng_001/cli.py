from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import AgentError, Config, approve_run, doctor, enqueue_task, execute_task, list_runs, watch


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ai-eng-001", description="Bounded runtime for POS-004 Engineering & Release Lead")
    p.add_argument("--config", type=Path, default=None, help="Path to JSON config")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor")
    enqueue = sub.add_parser("enqueue")
    enqueue.add_argument("task", type=Path)
    status = sub.add_parser("status")
    status.add_argument("--limit", type=int, default=20)
    run = sub.add_parser("run")
    run.add_argument("task", type=Path)
    approve = sub.add_parser("approve")
    approve.add_argument("run_id")
    approve.add_argument("--push", action="store_true", help="Explicit owner external-effect command: push approved branch")
    sub.add_parser("watch")
    return p


def main() -> int:
    args = parser().parse_args()
    config = Config.load(args.config)
    try:
        if args.command == "doctor":
            result = doctor(config)
        elif args.command == "enqueue":
            result = enqueue_task(args.task, config)
        elif args.command == "status":
            result = list_runs(config, args.limit)
        elif args.command == "run":
            result = execute_task(args.task, config)
        elif args.command == "approve":
            result = approve_run(args.run_id, config, push=args.push)
        elif args.command == "watch":
            watch(config)
            return 0
        else:
            raise AssertionError(args.command)
    except AgentError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if isinstance(result, dict) and result.get("state") in {"BLOCKED", "NEEDS_OWNER"}:
        return 3
    if isinstance(result, dict) and result.get("ok") is False:
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
