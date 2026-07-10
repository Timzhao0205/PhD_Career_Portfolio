---
description: Summarize model/effort/tool activity from the logs.
---
Run `python 98_CLAUDE_METRICS/analyze_activity.py $ARGUMENTS` and summarize:
per-model tool calls and time, effort levels used, failure rate, subagents invoked,
and (if --transcripts) indicative tokens per model. Flag any stage where the served
model may differ from the intended routing, and recommend which stages are worth a
rerun on a stronger model given the budget.
