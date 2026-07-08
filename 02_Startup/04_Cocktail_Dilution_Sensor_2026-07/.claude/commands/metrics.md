---
description: Summarize Claude Code activity logs for this project
argument-hint: optional flags, e.g. "--days 7 --transcripts"
---
Run the activity analyzer and report the results compactly:

1. Execute: `python 98_CLAUDE_METRICS/logs/../analyze_activity.py $ARGUMENTS`
   (i.e. `python 98_CLAUDE_METRICS/analyze_activity.py $ARGUMENTS`).
2. Present: sessions table as-is, then 3-5 bullets of interpretation
   (heaviest sessions, failure hotspots, model/effort mix, whether
   /specs is being used for cheap lookups or expensive turns are
   being burned on trivia).
3. If the log directory is empty, say so and confirm hooks are wired
   by pointing at .claude/settings.json -- do not fabricate data.
