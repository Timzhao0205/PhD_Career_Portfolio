Continue the PhD/HSX research mission from the durable files in this local
project. Do not start a new plan from memory.

First read, in order:

1. `AGENTS.md`
2. `06/AGENTS.md`
3. the mission `MISSION.md`, `SOURCE_POLICY.md`, `CHECKPOINT_PROTOCOL.md`, and
   `EXECUTION_PLAN.md`
4. `state/CHATGPT_HANDOFF_STATE.json` and `state/CHATGPT_HANDOFF.md`
5. all completion markers and the current stage attempt JSON
6. `state/OPERATION_LOG.csv`, `state/MODEL_EFFORT_LOG.csv`,
   `state/SESSION_INDEX.csv`, and the tail of `state/CLAUDE_EVENT_LOG.jsonl`
7. the raw stream and generated effective prompt listed by the handoff state
8. current-stage partial outputs and relevant supplied evidence

Then:

- identify the earliest incomplete stage;
- treat `_history/r0` as audit-only; do not count its markers, sessions, or
  outputs as current progress;
- verify which work is already valid and continue without duplicating it;
- use the GPT-5.6 Sol model/effort selected in the app and record the actual
  selection; if Max was unavailable, record the Extra High substitution;
- do not invoke Claude Code, another agent CLI, or an MCP server;
- after every meaningful read, research batch, decision, edit, validation, or
  checkpoint, append a compact row to `state/OPERATION_LOG.csv` containing
  timestamp, stage, operation, progress, route=`chatgpt_windows`, attempt,
  status, model, effort, downgrade/usage/inactivity flags, files/checkpoint,
  next action, and notes;
- update `state/CHATGPT_HANDOFF_STATE.json` and
  `state/CHATGPT_HANDOFF.md` before and after material edits;
- satisfy the current stage prompt and validate every required output;
- only after validation, write the completion marker using the schema in the
  nested `AGENTS.md`, then advance to the next stage;
- preserve all open evidence gaps and never invent citations, measurements,
  reviewer positions, venue rules, or legal conclusions.

Begin by reporting the recovered stage, durable evidence inspected, selected
model/effort, and the exact next operation. Then continue the work.
