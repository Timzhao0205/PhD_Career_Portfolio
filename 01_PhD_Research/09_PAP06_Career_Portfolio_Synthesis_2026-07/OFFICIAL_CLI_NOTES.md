# Claude Code features used

Verified against the official Claude Code documentation on 2026-07-28.

- Project skills live at `.claude/skills/<name>/SKILL.md` and can be invoked
  with `/name`.
  - https://code.claude.com/docs/en/skills
- Project subagents live at `.claude/agents/*.md`; their frontmatter supports
  `model`, `effort`, `permissionMode`, `background`, and `initialPrompt`.
  - https://code.claude.com/docs/en/sub-agents
- Interactive CLI flags include `--agent`, `--model`, `--effort`,
  `--permission-mode`, `--name`, `--debug-file`, `--no-chrome`, and
  `--strict-mcp-config`.
  - https://code.claude.com/docs/en/cli-reference
- `bypassPermissions` skips permission prompts but remains subject to product
  and organization safeguards.
  - https://code.claude.com/docs/en/settings
- `Ctrl+T` toggles the task checklist, and task items persist through context
  compaction.
  - https://code.claude.com/docs/en/interactive-mode

The package deliberately does not use hooks, dynamic workflows, MCP servers,
Chrome integration, command shells, or non-interactive `claude -p`.
