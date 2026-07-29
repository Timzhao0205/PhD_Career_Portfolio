# Official setup references

## Claude Code

- CLI reference: https://code.claude.com/docs/en/cli-reference

The launcher uses non-interactive stream JSON, an explicit model and effort,
project settings, and a deny rule for all MCP tools. It does not load an MCP
configuration or call an MCP server.

## ChatGPT desktop app for Windows

- Windows app: https://developers.openai.com/codex/windows/windows-app
- Local projects: https://developers.openai.com/codex/projects
- `AGENTS.md`: https://developers.openai.com/codex/agent-configuration/agents-md
- Model and effort selection: https://developers.openai.com/codex/models

The handoff instructions open the extracted folder as the primary local
project so its root `AGENTS.md` is automatically discovered. The model/effort
mapping is recorded in both the root routing table and the live handoff JSON.
