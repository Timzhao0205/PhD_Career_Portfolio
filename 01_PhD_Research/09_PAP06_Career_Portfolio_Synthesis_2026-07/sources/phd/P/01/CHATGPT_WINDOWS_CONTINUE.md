# Continue immediately in the ChatGPT desktop app for Windows

Use this path after you stop PowerShell manually, Claude exits, or a second
Fable-assigned attempt finishes without a verifiable Fable 5 final result.

1. Leave the extracted folder unchanged.
2. Open the ChatGPT desktop app for Windows.
3. Select **Add new project** or press **Ctrl+O**.
4. Choose this extracted `01` folder and make it the **primary**
   folder.
5. Open
   `06\state\CHATGPT_HANDOFF.md`.
6. Select the recommended GPT-5.6 Sol reasoning effort shown there:
   - Claude Sonnet/High stage → GPT-5.6 Sol/High
   - Claude Sonnet/Extra High stage → GPT-5.6 Sol/Extra High
   - Claude Fable/Extra High stage → GPT-5.6 Sol/Max
   - if Max is unavailable → GPT-5.6 Sol/Extra High
7. Start a new ChatGPT Work chat and paste the full contents of
   `CHATGPT_WINDOWS_START_PROMPT.md`.

No PowerShell recovery command is required first. If PowerShell was closed
while Claude was still running, `workflow_status` may remain
`CLAUDE_IN_PROGRESS`; treat that as an interrupted attempt and recover from the
listed stream, generated prompt, event log, and partial files.

The `_history\r0` tree contains the pre-restart audit record only. Do not count
its markers or outputs as active progress.

The project-level `AGENTS.md` is discovered from the primary folder. The nested
mission `AGENTS.md` contains the exact logging and completion contract.

Official references:

- https://developers.openai.com/codex/windows/windows-app
- https://developers.openai.com/codex/projects
- https://developers.openai.com/codex/agent-configuration/agents-md
- https://developers.openai.com/codex/models
