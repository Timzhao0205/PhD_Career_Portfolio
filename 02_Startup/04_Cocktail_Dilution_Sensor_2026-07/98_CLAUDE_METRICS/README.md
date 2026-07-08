# Claude Code activity metrics

What: every Claude Code session in this folder appends event records
to `logs/activity_YYYY-MM.jsonl` via hooks wired in
`.claude/settings.json` -> `.claude/hooks/log_activity.py`.

Recorded per event: timestamp, session_id, event type, configured
model + effortLevel (SessionStart; plus per-tool `effort` when the
event supplies it), tool name, duration_ms, success/failure, a short
tool-input summary (path / first 120 chars of a command / query),
subagent type, turn boundaries, transcript path. Prompt CONTENT is
never stored -- lengths only.

Analyze:
    python 98_CLAUDE_METRICS/analyze_activity.py            # all time
    python 98_CLAUDE_METRICS/analyze_activity.py --days 7
    python 98_CLAUDE_METRICS/analyze_activity.py --transcripts   # + token usage per model (best-effort)
    python 98_CLAUDE_METRICS/analyze_activity.py --csv sessions.csv
or `/metrics [flags]` inside a session.

Notes:
- Logger is fail-safe: always exit 0, silent -- a logging bug can
  never block a tool call or leak into context.
- `--transcripts` parses Claude Code's own session transcript JSONL
  (path captured at SessionStart) for per-model token counts. That
  format is an internal implementation detail and may change between
  Claude Code versions; treat as indicative and use `/cost` in-session
  for billing truth.
- To pause recording: delete the `hooks` block from
  `.claude/settings.json` (nothing else depends on it). `/hooks`
  in-session shows what is currently wired.
- What to look for over time: expensive-turn hotspots (long Bash/
  WebFetch tails), failure-rate spikes per tool, whether cheap /specs
  lookups are actually displacing full-model turns, and model/effort
  mix vs. task type -- feed conclusions back into the CLAUDE.md
  escalation ladder.
