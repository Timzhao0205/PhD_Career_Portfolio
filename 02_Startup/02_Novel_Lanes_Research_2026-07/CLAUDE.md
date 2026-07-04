# CLAUDE.md - Operating Rules (binding; Round 2: Novel Lanes & Final Showdown)

Playbook: 01_MISSION/MISSION_BRIEF_V2.md. State: 05_STATE/MASTER_STATE.json. On session start
or after compaction: re-read this file, the brief, and the state, then continue from the first
incomplete phase. Files are ground truth.

## Hard rules
1. Stay inside this folder. The ONLY prior-work access is the local copy in 00_PRIOR_CORPUS/
   (the launcher populates GEN3/ from the sibling Round-1 folder). Never read or write ../
   or anything outside the project root. Web via WebSearch/WebFetch only.
2. Zero user interaction. Never ask questions or wait; assume, log to 05_STATE/ASSUMPTIONS.md,
   continue until "mission":"COMPLETE".
3. NOVELTY FIRST. No candidate may duplicate or lightly re-parameterize anything in
   01_MISSION/EXCLUSION_LIST.md or 05_STATE/exclusion_ledger.json. Zero HTS candidates
   (incumbent C12 holds the single allowed HTS slot). Magnefy wall absolute. <=2 PhD-lane
   candidates (GaN sensing / fusion diagnostics / battery magnetic imaging).
4. Comparability. Use the identical rubric and adjustment conventions so V-scores compare
   directly with the frozen incumbent scores; never re-derive incumbent scores.
5. Source discipline per 01_MISSION/SOURCE_STANDARDS.md: merged >=200 unique, >=100 fresh; no
   preprints as support; load-bearing numbers only from pages fetched THIS mission (incl.
   re-fetch of reused sources); log at time of use.
6. State discipline: after every phase and wave update MASTER_STATE.json, merge/dedupe
   90_BIBLIOGRAPHY/sources.json, append one line to PROGRESS_LOG.md
   ([ISO ts] phase= wave= files= sources_total= fresh=).
7. Parallel by default via .claude/agents/ exactly as the brief assigns (4 scouts/wave, 5
   red-teams/wave, 3+2 deep dives). Subagents return one-line summaries; findings go to files.
8. Effort policy: session runs at max (set by launcher env); domain-scout and source-auditor
   are pinned to high in their frontmatter for source-gathering efficiency. Do not override.
9. Windows host: forward-slash relative paths; UTF-8; no characters illegal on Windows.
10. Style: terse, quantitative, engineer-voice. Reader is a technically fluent PhD founder.

## Write map
10_GAP_LANDSCAPE scouts · 20_CANDIDATES · 30_SCORING · 40_DEEPDIVES · 50_POLICY_DELTA ·
60_FINAL_SYNTHESIS · 90_BIBLIOGRAPHY · 99_AUDIT · 05_STATE. Read-only: 00_PRIOR_CORPUS,
01_MISSION. If a subagent fails or returns thin results, rerun that one agent before advancing.
