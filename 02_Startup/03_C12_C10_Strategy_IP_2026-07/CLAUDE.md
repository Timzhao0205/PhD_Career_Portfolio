# CLAUDE.md - Operating Rules (binding; Round 3: C12+C10 Strategy, Competitors & Patent Whitespace)

Playbook: 01_MISSION/MISSION_BRIEF_V3.md. State: 05_STATE/MASTER_STATE.json. On session start
or after compaction: re-read this file, the brief, and the state, then continue from the first
incomplete phase. Files are ground truth.

## Hard rules
1. Stay inside this folder. The ONLY prior-work access is 00_PRIOR_CORPUS/ (launcher syncs it
   from the sibling Round-2 folder; shipped copies are the fallback). Never read or write ../
   or anything outside the project root. Web via WebSearch/WebFetch only.
2. Zero user interaction. Never ask questions or wait; assume, log to 05_STATE/ASSUMPTIONS.md,
   continue until "mission":"COMPLETE".
3. PATENT TRUTH RULE (absolute). Never cite a patent number that was not fetched THIS mission
   at its full-text page (Google Patents primary). Every cited patent gets a ledger record at
   time of use (number, title, assignee, priority date, URL, accessed, verified:"fetched").
   A number seen only in a secondary mention is resolved by fetching or dropped. Inventing,
   guessing, or pattern-completing a patent number is a mission-failing defect.
4. NOT LEGAL ADVICE. Every file written to 40_WHITESPACE/, 50_INVENTIONS/, and 60_STRATEGY/
   opens with the verbatim disclaimer block in 01_MISSION/IP_GROUND_RULES.md. No definitive
   patentability / freedom-to-operate / ownership conclusions anywhere - verdicts are
   FILE-CANDIDATE / REWORK / DROP plus flagged counsel questions.
5. STANFORD + UIUC/HINETICS WALL. Every invention disclosure carries an independence
   assessment per IP_GROUND_RULES.md. A concept that cannot plausibly be conceived and reduced
   to practice on personal time/resources, outside sponsored-research scope, is marked
   BLOCKED-PENDING-COUNSEL and excluded from the filing roadmap. Nothing may copy the
   UIUC/Hinetics v0 machine design; only independently conceived advances.
6. FILE-BEFORE-PUBLISH. China has no general novelty grace period (narrow exceptions do not
   cover ordinary journal/IEEE publication); EP effectively none; US 1-year inventor grace
   only. Every disclosure and the IP roadmap must sequence filings ahead of the founder's
   planned 2026-2028 publications (SUST/IEEE TAS benchmark papers from the Round-1 validation
   experiments).
7. Budget bands. Research tooling: free/public sources only (no paid patent databases).
   Every invention must include a reduction-to-practice path <= $25K parts+services; a $25-60K
   path is allowed only if flagged STRETCH with justification. No cleanroom dependence.
8. Magnefy wall absolute: nothing touching transformer condition monitoring, even as an
   invention embodiment or claim example.
9. Source discipline per 01_MISSION/SOURCE_STANDARDS.md: patents in 30_PATENTS/
   patent_ledger.json (>=150 fetched records, >=50 CN-family); non-patent sources in
   90_BIBLIOGRAPHY/sources.json (>=120 fresh); Chinese-language searching REQUIRED for all
   China competitor/patent/policy questions.
10. State discipline: after every phase and wave update MASTER_STATE.json, merge/dedupe the
    two ledgers, append one line to PROGRESS_LOG.md
    ([ISO ts] phase= wave= files= patents_total= cn_patents= sources_fresh=).
11. Parallel by default via .claude/agents/ exactly as the brief assigns (4 competitor
    analysts/wave, 5 patent scouts/wave, 4 invention designers/wave, 5 IP red-teams/wave).
    Subagents return one-line summaries; findings go to files. If a subagent fails or returns
    thin results, rerun that one agent before advancing.
12. Windows host: forward-slash relative paths; UTF-8; no characters illegal on Windows.
13. Style: terse, quantitative, engineer-voice; every file readable standalone. Reader is a
    technically fluent PhD founder preparing 2026-2028 actions for a 2029/2030 launch.

## Write map
10_COMPETITORS · 20_UNSOLVED · 30_PATENTS · 40_WHITESPACE · 50_INVENTIONS · 60_STRATEGY ·
90_BIBLIOGRAPHY · 99_AUDIT · 05_STATE. Read-only: 00_PRIOR_CORPUS, 01_MISSION.
