# HSX ChatGPT Windows app package — start here

This package is designed for the ChatGPT Windows desktop app. It contains no PowerShell runner and
requires no terminal command.

## Start in the app

1. Extract this ZIP to a new writable folder. Do not merge it with the PowerShell or older package.
2. Open the ChatGPT desktop app and sign in.
3. Choose **ChatGPT Work** from the mode dropdown, then choose **Open folder** and select the
   extracted `05_HSX_ChatGPT_Windows_App` folder.
4. Set the model to **GPT-5.6 Sol** and reasoning to **Extra High**.
5. Set folder permissions to allow reading/writing this folder. Allow live web access when the app
   requests it for research.
6. Open `PASTE_THIS_PROMPT.txt`, copy its single paragraph into the composer, and send it once.

The `/goal` kickoff tells ChatGPT to work through every stage autonomously and to save frequent
checkpoints. You do not need to run PowerShell or Codex CLI.

## If the app or computer restarts

Open the same folder and send:

```text
Resume this mission from the durable files. Read AGENTS.md, EXECUTION_PLAN.md,
CHECKPOINT_PROTOCOL.md, state/PROJECT_STATE.md, and the latest entry in
state/CHECKPOINT_INDEX.md. Validate existing stage markers, resume the earliest incomplete stage,
and continue autonomously to the stopping condition.
```

Do not start a blank replacement folder. All useful progress is stored under `outputs/` and
`state/`, with optional local Git commits when Git is available.

## Where progress is saved

- `state/PROJECT_STATE.md`: authoritative current/next status.
- `state/checkpoints/`: self-contained recovery snapshots.
- `state/CHECKPOINT_INDEX.md`: checkpoint catalogue and optional commit hashes.
- `state/WORKLOG.md`: chronological work record.
- `state/DECISION_LOG.md`: reversible design rationale.
- `state/MODEL_EFFORT_LOG.md`: actual model/effort and downgrade disclosure.
- `outputs/`: engineering reports, drawings, CAD, tables, evidence ledger, and final deliverables.

The final starting point is `outputs/FINAL_RECOMMENDATION_250C_UHV.md`.

