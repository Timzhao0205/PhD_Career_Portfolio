# Official product documentation basis

Package design was checked on 2026-07-12 against current OpenAI documentation:

- ChatGPT desktop quickstart: the Windows/macOS desktop app can open a selected folder and read or
  modify files there; ChatGPT Work is the documented mode for research, analysis, and deliverables.
  <https://developers.openai.com/codex/quickstart>
- Windows Codex app announcement: the app supports long-running project threads, local changes,
  sandboxed folder access, and coordinated agents; Windows availability was announced March 4,
  2026. <https://openai.com/index/introducing-the-codex-app/>
- `AGENTS.md` guidance: Codex reads project `AGENTS.md` instructions before work and closer project
  guidance has precedence. <https://developers.openai.com/codex/guides/agents-md>
- Goal workflow: define a stopping condition, work in checkpoints, maintain a progress log, and use
  durable artifacts to prove progress. <https://developers.openai.com/codex/use-cases/follow-goals/>
- Model guidance: Sol is intended for complex/high-value work; Terra and Luna are cost-oriented
  alternatives for narrower work, while higher reasoning is appropriate for difficult multi-step
  tasks. <https://developers.openai.com/codex/models>

The package therefore uses an app-native `/goal` kickoff, folder-local durable instructions,
explicit acceptance markers, frequent file checkpoints, optional local Git redundancy, and a
Sol/xhigh parent task. It intentionally contains no terminal runner or project configuration.

