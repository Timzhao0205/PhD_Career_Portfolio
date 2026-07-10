#!/usr/bin/env python3
"""Summarize Claude Code activity logs written by .claude/hooks/log_activity.py.

Usage (from the project root):
    python 98_CLAUDE_METRICS/analyze_activity.py
    python 98_CLAUDE_METRICS/analyze_activity.py --days 14
    python 98_CLAUDE_METRICS/analyze_activity.py --transcripts
    python 98_CLAUDE_METRICS/analyze_activity.py --csv sessions.csv

Outputs:
  1. Per-session table: start time, model/effort, turns, tool calls,
     failures, total tool time, top tools, subagents used.
  2. Aggregates: per-day activity, tool distribution, failure rate.
  3. --transcripts: best-effort token usage per model, parsed from the
     Claude Code session transcripts referenced in SessionStart records.
     The transcript format is an internal implementation detail and may
     change between Claude Code versions -- treat these numbers as
     indicative, and prefer /cost inside a session for billing truth.
"""
import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGDIR = HERE / "logs"


def load_records(days=None):
    recs = []
    cutoff = None
    if days:
        cutoff = datetime.now().astimezone() - timedelta(days=days)
    for f in sorted(LOGDIR.glob("activity_*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            try:
                r["_ts"] = datetime.fromisoformat(r["ts"])
            except Exception:
                continue
            if cutoff and r["_ts"] < cutoff:
                continue
            recs.append(r)
    return recs


def summarize_sessions(recs):
    sessions = defaultdict(lambda: {
        "start": None, "end": None, "source": None, "model": None,
        "effort": None, "turns": 0, "tools": Counter(), "tool_ms": 0,
        "failures": 0, "subagents": Counter(), "transcript": None,
        "prompt_chars": 0,
    })
    for r in recs:
        sid = r.get("session_id") or "unknown"
        s = sessions[sid]
        ts = r["_ts"]
        s["start"] = ts if s["start"] is None or ts < s["start"] else s["start"]
        s["end"] = ts if s["end"] is None or ts > s["end"] else s["end"]
        ev = r.get("event")
        if ev == "SessionStart":
            s["source"] = r.get("source") or s["source"]
            s["model"] = r.get("model") or r.get("model_configured") or s["model"]
            s["effort"] = r.get("effort_configured") or s["effort"]
            s["transcript"] = r.get("transcript_path") or s["transcript"]
        elif ev == "UserPromptSubmit":
            s["turns"] += 1
            s["prompt_chars"] += r.get("prompt_chars") or 0
        elif ev in ("PostToolUse", "PostToolUseFailure"):
            s["tools"][r.get("tool") or "?"] += 1
            s["tool_ms"] += r.get("duration_ms") or 0
            if ev == "PostToolUseFailure":
                s["failures"] += 1
            if r.get("effort"):
                s["effort"] = r["effort"]
        elif ev == "SubagentStop":
            s["subagents"][r.get("agent_type") or "?"] += 1
    return sessions


def fmt_dur(seconds):
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    m, s = divmod(seconds, 60)
    if m < 60:
        return f"{m}m{s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h{m:02d}m"


def print_sessions(sessions):
    print(f"\n=== Sessions ({len(sessions)}) ===")
    header = f"{'start':<17} {'sid':<9} {'model':<10} {'effort':<7} {'turns':>5} {'tools':>5} {'fail':>4} {'tool_time':>9} {'wall':>7}  top tools / agents"
    print(header)
    print("-" * len(header))
    for sid, s in sorted(sessions.items(), key=lambda kv: kv[1]["start"] or datetime.min):
        wall = (s["end"] - s["start"]).total_seconds() if s["start"] and s["end"] else 0
        top = ", ".join(f"{t}x{n}" for t, n in s["tools"].most_common(3))
        if s["subagents"]:
            top += " | agents: " + ", ".join(f"{a}x{n}" for a, n in s["subagents"].most_common())
        print(f"{s['start']:%Y-%m-%d %H:%M}  {sid[:8]:<9} {str(s['model'])[:10]:<10} {str(s['effort'])[:7]:<7} "
              f"{s['turns']:>5} {sum(s['tools'].values()):>5} {s['failures']:>4} "
              f"{fmt_dur(s['tool_ms']/1000):>9} {fmt_dur(wall):>7}  {top}")


def print_aggregates(recs, sessions):
    tool_calls = [r for r in recs if r.get("event") in ("PostToolUse", "PostToolUseFailure")]
    tools = Counter(r.get("tool") or "?" for r in tool_calls)
    fails = sum(1 for r in tool_calls if r.get("event") == "PostToolUseFailure")
    per_day = Counter(r["_ts"].strftime("%Y-%m-%d") for r in tool_calls)
    models = Counter(str(s["model"]) for s in sessions.values())

    print("\n=== Aggregates ===")
    print(f"tool calls: {len(tool_calls)}  failures: {fails} "
          f"({100.0*fails/len(tool_calls):.1f}%)" if tool_calls else "tool calls: 0")
    print("models (per session): " + ", ".join(f"{m}x{n}" for m, n in models.most_common()))
    print("tool distribution: " + ", ".join(f"{t}:{n}" for t, n in tools.most_common(12)))
    print("per day: " + ", ".join(f"{d}:{n}" for d, n in sorted(per_day.items())))


def parse_transcripts(sessions):
    """Best-effort token accounting from Claude Code session transcripts.

    Transcript files are JSONL; assistant entries carry message.model and
    message.usage.{input_tokens,output_tokens,cache_read_input_tokens,
    cache_creation_input_tokens}. Internal format -- parse defensively.
    """
    usage = defaultdict(lambda: Counter())
    seen, missing = 0, 0
    for s in sessions.values():
        tp = s.get("transcript")
        if not tp:
            continue
        p = Path(tp)
        if not p.exists():
            missing += 1
            continue
        seen += 1
        try:
            for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                msg = obj.get("message") if isinstance(obj, dict) else None
                if not isinstance(msg, dict):
                    continue
                model = msg.get("model")
                u = msg.get("usage")
                if not model or not isinstance(u, dict):
                    continue
                c = usage[model]
                for k in ("input_tokens", "output_tokens",
                          "cache_read_input_tokens", "cache_creation_input_tokens"):
                    v = u.get(k)
                    if isinstance(v, (int, float)):
                        c[k] += int(v)
                c["messages"] += 1
        except Exception:
            continue
    print(f"\n=== Token usage (best-effort, {seen} transcripts read, {missing} missing) ===")
    if not usage:
        print("no usable transcript data found -- use /cost in-session for billing truth")
        return
    for model, c in sorted(usage.items()):
        print(f"{model}: msgs={c['messages']} in={c['input_tokens']:,} out={c['output_tokens']:,} "
              f"cache_read={c['cache_read_input_tokens']:,} cache_write={c['cache_creation_input_tokens']:,}")


def write_csv(sessions, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["session_id", "start", "end", "model", "effort", "turns",
                    "tool_calls", "failures", "tool_time_s", "prompt_chars", "top_tools"])
        for sid, s in sorted(sessions.items(), key=lambda kv: kv[1]["start"] or datetime.min):
            w.writerow([sid, s["start"], s["end"], s["model"], s["effort"], s["turns"],
                        sum(s["tools"].values()), s["failures"], round(s["tool_ms"]/1000, 1),
                        s["prompt_chars"],
                        ";".join(f"{t}x{n}" for t, n in s["tools"].most_common(5))])
    print(f"wrote {path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=None, help="only include the last N days")
    ap.add_argument("--transcripts", action="store_true", help="parse transcripts for token usage")
    ap.add_argument("--csv", metavar="FILE", help="also write per-session CSV")
    args = ap.parse_args()

    recs = load_records(args.days)
    if not recs:
        print(f"No records found in {LOGDIR} -- run a Claude Code session in this folder first.")
        sys.exit(0)
    sessions = summarize_sessions(recs)
    print_sessions(sessions)
    print_aggregates(recs, sessions)
    if args.transcripts:
        parse_transcripts(sessions)
    if args.csv:
        write_csv(sessions, args.csv)


if __name__ == "__main__":
    main()
