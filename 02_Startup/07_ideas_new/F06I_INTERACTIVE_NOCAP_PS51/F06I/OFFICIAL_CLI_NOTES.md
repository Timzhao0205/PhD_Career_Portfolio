# Official Claude Code behavior used by this package

Verified against current official documentation on 2026-07-27:

- `claude` starts an interactive session; `--resume` continues a saved session.
- `--model` pins the session model.
- `--effort xhigh` sets session effort when the model supports it.
- `--permission-mode bypassPermissions` removes permission prompts.
- Interactive sessions persist unless persistence is explicitly disabled.
- SessionStart hooks receive the actual model identifier and session ID.
- Status-line commands receive current model, effort, token, context, duration,
  cost, version, and rate-limit telemetry when available.
- Project subagents may declare their own model and effort in frontmatter.

References:

- https://code.claude.com/docs/en/cli-usage
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/statusline
- https://code.claude.com/docs/en/sub-agents

`bypassPermissions` is powerful and is officially recommended only in an
isolated environment. This package confines its project instructions to a
dedicated short-path folder, but the permission mode itself is not a sandbox.

