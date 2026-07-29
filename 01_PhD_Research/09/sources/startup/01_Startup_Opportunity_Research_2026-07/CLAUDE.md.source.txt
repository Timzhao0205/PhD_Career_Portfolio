# CLAUDE.md — Operating Rules (binding for orchestrator and all subagents)

This folder is a self-contained autonomous research mission. The playbook is
`01_MISSION/MISSION_BRIEF.md`; state lives in `05_STATE/MASTER_STATE.json`. On any session start
or after any context compaction: re-read this file, the brief, and the state file, then continue
from the first incomplete phase. **Files are ground truth; your memory is not.**

## Hard rules

1. **Stay inside this folder.** Never read or write anything outside the project root — no `..`,
   no sibling folders, no home directory, no other parts of the portfolio. This preserves the
   requested from-scratch independence (and safety). The only external access is WebSearch/WebFetch.
2. **Zero user interaction.** Never ask the user questions or wait for approval. Make the
   reasonable assumption, log it in `05_STATE/ASSUMPTIONS.md`, continue. Do not stop until
   `MASTER_STATE.json` says `"mission": "COMPLETE"`.
3. **Fresh, unbiased research.** Use no prior conclusions about this founder's startup options.
   Every claim traces to a source gathered in this mission per `01_MISSION/SOURCE_STANDARDS.md`.
4. **PhD ≠ direction.** The founder's thesis topics are capability evidence only. Enforce the
   diversity quotas in the brief.
5. **Source discipline.** ≥200 unique sources; no preprints as support; load-bearing numbers only
   from fetched pages; log every source into `90_BIBLIOGRAPHY/sources.json` at time of use.
6. **State discipline.** After every phase and every subagent wave: update `MASTER_STATE.json`,
   merge/dedupe sources.json, append one line to `05_STATE/PROGRESS_LOG.md`
   (`[ISO-timestamp] phase=… wave=… files=… sources_total=…`).
7. **Parallel by default.** Use the custom subagents in `.claude/agents/` exactly as the brief
   assigns them; launch waves as parallel Task calls (5 scouts / 4 analysts / 5 critics at a time).
8. **Token discipline.** Subagents write findings to their assigned files and return only short
   summaries. Never dump full webpage text into the conversation.
9. **Windows host.** Use forward-slash relative paths in tool calls; UTF-8 for all files; avoid
   characters illegal in Windows filenames (`: * ? " < > |`).
10. **Style.** Direct, quantitative, no filler. The reader is a technically fluent PhD engineer.

## File map (write only to these)

- `10_PHASE1_LANDSCAPE/` scouts · `20_PHASE2_CANDIDATES/` candidates ·
  `30_PHASE3_SCORING/` matrix+red-team · `40_PHASE4_DEEPDIVES/` deep dives ·
  `50_PHASE5_POLICY/` policy · `60_PHASE6_SYNTHESIS/` summary+roadmap ·
  `90_BIBLIOGRAPHY/` sources · `99_AUDIT/` audit · `05_STATE/` state.

If a subagent fails or returns thin results, rerun that one agent before advancing the phase.
