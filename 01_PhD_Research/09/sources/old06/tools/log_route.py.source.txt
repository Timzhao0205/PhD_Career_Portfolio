#!/usr/bin/env python3
"""Orchestrator-only appender for 98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl."""
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG = ROOT / "98_RUN_LOGS" / "MODEL_ROUTING_LOG.jsonl"


def main(argv):
    if len(argv) != 8:
        print("usage: log_route.py phase task requested_model actual_model effort reason downgrade status")
        return 1
    phase, task, req, act, effort, reason, downgrade, status = argv
    entry = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "phase": phase,
        "task": task,
        "requested_model": req,
        "actual_model": act,
        "effort": effort,
        "reason": reason,
        "downgrade": downgrade.strip().lower() == "true",
        "status": status,
        "source": "orchestrator",
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"logged {phase} {task} {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
