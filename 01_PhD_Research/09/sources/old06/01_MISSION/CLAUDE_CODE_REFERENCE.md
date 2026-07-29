# Verified Claude Code/model design basis — checked 2026-07-12

- Fable 5 model ID and positioning: <https://platform.claude.com/docs/en/about-claude/models/overview>
- Fable 5 migration and effort guidance: <https://platform.claude.com/docs/en/about-claude/models/migration-guide>
- Fable-specific long-run prompting: <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5>
- Claude Code CLI flags (`-p`, `--model`, `--effort`, `--permission-mode`, JSONL output,
  `--max-budget-usd`): <https://code.claude.com/docs/en/cli-reference>
- Project settings and permission/sandbox behavior: <https://code.claude.com/docs/en/settings>
- Custom subagent frontmatter, including model and effort: <https://code.claude.com/docs/en/sub-agents>

At verification time, Anthropic describes Fable 5 as its highest-capability widely released model,
with always-on adaptive thinking, and recommends `high` for most work and `xhigh` for the most
capability-sensitive work. Claude Code accepts `low`, `medium`, `high`, `xhigh`, `max`, and model-
dependent higher modes; this package deliberately uses documented `xhigh` for critical work.

Current platform list pricing at verification time: Fable 5 $10/MTok input and $50/MTok output;
Sonnet 5 introductory $2/$10 through 2026-08-31, then $3/$15. Subscription Claude Code runs draw
from plan limits rather than exposing a reliable per-mission dollar counter, so the launcher logs
routing and supports resumable checkpoints; `-MaxBudgetUSD` is provided for API-billed print mode.

This file is a setup reference, not evidence for any startup conclusion. The research run must
search current technical, commercial, and policy sources independently.

