# Environment setup manifest

## Required for the PowerShell route

- Windows PowerShell 5.1 or newer
- Claude Code 2.1.214 or newer on `PATH`
- authenticated Claude Code session
- access to the configured `sonnet` and `fable` version-5 aliases
- internet access for literature research

The folder contains no active alternate-provider CLI dependency and no MCP
server configuration. User-scoped MCP tools are explicitly denied in each
Claude invocation.

## Optional recovery surface

- ChatGPT desktop app for Windows
- local-project access to the extracted `01_PhD_Research` folder
- GPT-5.6 Sol with High, Extra High, or Max reasoning as recorded in the
  handoff state

The ChatGPT app is not launched from PowerShell. The user opens it manually
after an interruption or second model-integrity failure.
