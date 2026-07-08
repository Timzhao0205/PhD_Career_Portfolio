#!/usr/bin/env python3
"""Claude Code activity logger (hook target).

Wired in .claude/settings.json for: SessionStart, UserPromptSubmit,
PostToolUse, PostToolUseFailure, SubagentStop, Stop, SessionEnd.
Reads the hook event JSON from stdin and appends ONE compact JSON line
to 98_CLAUDE_METRICS/logs/activity_YYYY-MM.jsonl.

Design rules:
- FAIL-SAFE: always exit 0, never print to stdout/stderr. A logging
  bug must never block a tool call or pollute session context
  (SessionStart stdout would be injected into the conversation).
- PRIVACY-LIGHT: prompt/tool content is never stored verbatim beyond a
  short tool-input summary (file path, first 120 chars of a command,
  or a search query). Prompt text -> length only.
- Records what performance analysis needs: session id, event, model
  (recorded when the event provides it, else the configured default
  from settings.json), effort, permission mode, tool name + duration,
  success/failure, subagent type, transcript path.

Analyze with 98_CLAUDE_METRICS/analyze_activity.py or /metrics.
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def project_root() -> Path:
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    if env:
        return Path(env)
    # script lives at <root>/.claude/hooks/log_activity.py
    return Path(__file__).resolve().parents[2]


def configured_defaults(root: Path) -> dict:
    out = {}
    try:
        cfg = json.loads((root / ".claude" / "settings.json").read_text(encoding="utf-8"))
        if isinstance(cfg.get("model"), str):
            out["model_configured"] = cfg["model"]
        if isinstance(cfg.get("effortLevel"), str):
            out["effort_configured"] = cfg["effortLevel"]
    except Exception:
        pass
    # personal overrides win if present
    try:
        loc = json.loads((root / ".claude" / "settings.local.json").read_text(encoding="utf-8"))
        if isinstance(loc.get("model"), str):
            out["model_configured"] = loc["model"]
        if isinstance(loc.get("effortLevel"), str):
            out["effort_configured"] = loc["effortLevel"]
    except Exception:
        pass
    return out


def summarize_tool_input(tool_name: str, tool_input) -> str:
    if not isinstance(tool_input, dict):
        return ""
    for key in ("file_path", "path", "notebook_path"):
        if isinstance(tool_input.get(key), str):
            return tool_input[key][:200]
    for key in ("command", "query", "url", "pattern", "description", "prompt"):
        if isinstance(tool_input.get(key), str):
            return tool_input[key][:120]
    return ""


def build_record(evt: dict, root: Path) -> dict:
    name = evt.get("hook_event_name", "Unknown")
    rec = {
        "ts": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "event": name,
        "session_id": evt.get("session_id"),
    }
    for k in ("permission_mode", "effort", "agent_id", "agent_type"):
        if evt.get(k) is not None:
            rec[k] = evt[k]

    if name == "SessionStart":
        rec["source"] = evt.get("source")
        if evt.get("model"):  # present on SessionStart only, not guaranteed
            rec["model"] = evt.get("model")
        rec.update(configured_defaults(root))
        if evt.get("transcript_path"):
            rec["transcript_path"] = str(evt["transcript_path"])
    elif name == "UserPromptSubmit":
        p = evt.get("prompt")
        rec["prompt_chars"] = len(p) if isinstance(p, str) else None
    elif name in ("PostToolUse", "PostToolUseFailure"):
        rec["tool"] = evt.get("tool_name")
        rec["ok"] = name == "PostToolUse"
        if evt.get("duration_ms") is not None:
            rec["duration_ms"] = evt.get("duration_ms")
        rec["input_summary"] = summarize_tool_input(evt.get("tool_name", ""), evt.get("tool_input"))
    elif name == "SubagentStop":
        pass  # agent_type already captured above when provided
    elif name == "SessionEnd":
        if evt.get("reason"):
            rec["reason"] = evt.get("reason")
    return rec


def main() -> None:
    try:
        evt = json.load(sys.stdin)
    except Exception:
        return
    try:
        root = project_root()
        logdir = root / "98_CLAUDE_METRICS" / "logs"
        logdir.mkdir(parents=True, exist_ok=True)
        rec = build_record(evt, root)
        fname = logdir / f"activity_{datetime.now():%Y-%m}.jsonl"
        with open(fname, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception:
        return


if __name__ == "__main__":
    main()
    sys.exit(0)
