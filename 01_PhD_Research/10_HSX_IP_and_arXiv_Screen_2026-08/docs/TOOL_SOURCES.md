# Native Claude Code configuration sources

These official pages support the launcher and model policy. Recheck if Claude
Code changes materially.

- Native Windows install and requirements:
  https://code.claude.com/docs/en/installation
- CLI flags for interactive prompt, resume/name, model, effort, debug file, and
  `--dangerously-skip-permissions`:
  https://code.claude.com/docs/en/cli-usage
- Fable 5, Sonnet 5, effort levels, model status, and classifier fallback:
  https://code.claude.com/docs/en/model-config
- Project subagent model, effort, max-turn, and permission frontmatter:
  https://code.claude.com/docs/en/sub-agents
- `switchModelsOnFlag` and `permissions.defaultMode` settings:
  https://code.claude.com/docs/en/settings
- Permission-mode behavior and cautions:
  https://code.claude.com/docs/en/permission-modes

The package requires Claude Code 2.1.219 or newer because that version supports
the current category-specific Fable fallback behavior, while the project sets
`switchModelsOnFlag` to false so a flag pauses rather than silently switches.
