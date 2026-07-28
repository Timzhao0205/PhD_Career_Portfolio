# No package-defined budget shutdown

The active launcher uses interactive Claude Code and does not pass:

- `--max-budget-usd`;
- `--max-turns`;
- print mode (`-p`);
- `--no-session-persistence`;
- a time limit or token limit.

No route field, hook, pilot, validator, or checkpoint defines a monetary
ceiling. Cost values are retained only as performance telemetry.

This cannot remove external account, plan, rate, weekly usage, provider,
authentication, or network limits. If one occurs, durable files remain and the
same `START.ps1` command resumes the named session.

