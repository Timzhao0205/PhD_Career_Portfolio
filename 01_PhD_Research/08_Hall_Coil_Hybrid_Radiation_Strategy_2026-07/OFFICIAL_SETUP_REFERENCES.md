# Official Claude Code references

The package design is based on the current official Claude Code documentation.
Recheck these pages if the CLI has changed:

- CLI reference:
  https://code.claude.com/docs/en/cli-reference
- Model configuration, Fable alias, effort, safe mode, and category fallback:
  https://code.claude.com/docs/en/model-config
- Permission modes:
  https://code.claude.com/docs/en/permissions
- Settings:
  https://code.claude.com/docs/en/settings

The runner uses:

- `-p`
- `--model sonnet` or `--model fable`
- `--effort high` or `--effort xhigh`
- `--max-turns`
- `--output-format stream-json`
- `--verbose`
- `--resume` for an interrupted session
- `--permission-mode bypassPermissions` in default full mode
- `--permission-mode acceptEdits` in guarded mode
- `--safe-mode` only for the one clarified Fable retry
- `--no-chrome`
- `--disallowedTools mcp__*`

Minimum Claude Code version: 2.1.219.

The working directory is this isolated mission folder. Full permission does
not grant permission to write into sibling folders; the agent contract makes
those read-only context.
