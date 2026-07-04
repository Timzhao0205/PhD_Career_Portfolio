# START HERE — Round 2: Novel Lanes & Final Showdown

One command. Claude Code (Fable, **session effort = MAX**) searches only the lanes no prior
generation covered, generates **≥12 genuinely new candidates** under a hard exclusion of all
~100 previously proposed concepts, stress-tests them with the identical Round-1 rubric, and
runs a **final merged showdown** against your incumbent best-of-best — ending in the
Best-of-the-Best Top 5 for your 2029/2030 decision.

## Two decisions I locked (override = one line each)

1. **Exclusion scope = everything prior.** All C01–C40, all Gen-1 RIDs, all Gen-2 CLs, all
   frontier-worker candidates, all saturation N/R rows are banned as generation targets
   (`01_MISSION/EXCLUSION_LIST.md`). Only the top finalists re-enter, score-frozen, at the
   final comparison. *Override:* delete entries from EXCLUSION_LIST.md.
2. **The single HTS slot is pre-seeded by C12.** Your "max 1 HTS idea" rule + "avoid ideas
   already proposed" together mean new HTS generation is banned (the corpus already explored
   15+ HTS concepts; anything new would be a variant). C12-cluster represents HTS in the
   showdown. *Override:* remove gate G6-HTS from SCORING_RUBRIC.md and the category ban from
   EXCLUSION_LIST.md — but then expect near-duplicates.

## Setup & run

1. Install/log in once (skip if done): `irm https://claude.ai/install.ps1 | iex`, then
   `claude` → browser login → `/exit`.
2. Extract this zip into `PhD_Career_Portfolio\02_Startup\` so it sits **next to**
   `01_Startup_Opportunity_Research_2026-07\` (the launcher auto-syncs Round-1 finals from
   there into `00_PRIOR_CORPUS\GEN3\`; if the sibling is missing it falls back to the shipped
   copies).
3. Run:
   ```powershell
   cd <path>\PhD_Career_Portfolio\02_Startup\02_Novel_Lanes_Research_2026-07
   .\RUN_RESEARCH.ps1
   ```
   That's the whole interaction. Blocked script? `powershell -ExecutionPolicy Bypass -File .\RUN_RESEARCH.ps1`
   Stopped mid-run (weekly limit, sleep, crash)? `.\RUN_RESEARCH.ps1 -Resume` — state is
   checkpointed after every phase and wave. Disable Windows sleep for the run.

Manual fallback: in this folder, `$env:CLAUDE_CODE_EFFORT_LEVEL='max'` then
`claude --dangerously-skip-permissions --model claude-fable-5` and paste `KICKOFF_PROMPT.txt`.

## Effort policy (your spec: max everywhere except source gathering)

- The launcher sets `CLAUDE_CODE_EFFORT_LEVEL=max` → the orchestrator session and every
  inheriting subagent (candidate generation, red teams, deep dives, policy delta, showdown
  synthesis) run at **max**.
- The two source-gathering agents — `domain-scout` and `source-auditor` — are pinned to
  `effort: high` in their frontmatter (search-reach-bound work; max there only burns tokens
  re-pondering the same pages). Verify in-session anytime with `/effort`.

## Budget honesty

Max-everywhere costs roughly 1.5–2.5× a high-effort run per token of reasoning, but this
mission is about half Round 1's size (8 lanes vs 10, ~14 candidates vs 40, 5 deep dives vs 12,
policy delta vs full brief, and ~half the bibliography reused). Net: comparable to Round 1's
burn. On a Max plan the realistic risk is hitting the **weekly limit mid-run** — the design
assumes it: `-Resume` continues losslessly after reset (`/usage` shows timing). Fable draws
usage much faster than Opus, so start the run early in your weekly window.

## What you'll read when it's done

| You want… | Open |
|---|---|
| **The final answer** (merged ranking + Best-of-the-Best Top 5 + does anything displace C12) | `60_FINAL_SYNTHESIS/00_FINAL_SHOWDOWN.md` |
| What changes in your prep plan | `60_FINAL_SYNTHESIS/01_ROADMAP_IMPLICATIONS.md` |
| Every concept ever considered, all generations, one table | `60_FINAL_SYNTHESIS/02_MERGED_FULL_RANKING.md` |
| The 5 new deep dives | `40_DEEPDIVES/` |
| All new ideas + novelty declarations | `20_CANDIDATES/CANDIDATES.md` |
| Bear cases on every new idea | `30_SCORING/REDTEAM_*.md` |
| Policy changes since Round 1 | `50_POLICY_DELTA/POLICY_DELTA.md` |
| Merged 200+ source bibliography | `90_BIBLIOGRAPHY/BIBLIOGRAPHY.md` |
| Self-audit incl. zero-duplicate proof | `99_AUDIT/FINAL_AUDIT.md` |

## Design notes

- **Comparability is sacred:** identical rubric, weights, gates, and score-adjustment
  statistics as Round 1; incumbent scores are frozen, never re-derived — so the showdown table
  is apples-to-apples (expected-score `e` convention marks evidence-class differences).
- **Novelty is audited, not assumed:** every candidate carries a written novelty declaration;
  red teams independently verify it; the Phase-7 audit re-checks all of them against the
  machine-readable exclusion ledger and fails the mission on any duplicate.
- **Profile updates are in:** battery magnetic camera (as a capability), "plasma" as a named
  sector (lane G02), ≤2 PhD-lane candidates, Magnefy wall, no Stanford IP.
- Same operator cautions as Round 1: full-auto disables permission checks (folder confinement
  is by instruction; `-Mode guarded` for enforced rails), and the policy delta is research,
  not legal advice.

## Honest framing before you spend the tokens

Round 1 + the saturation check already found the primary bet, and these eight lanes were
chosen precisely because they're the *unsearched remainder* — structurally, most of what comes
back should land below C12's 83.6 (that's what saturation means). The run's real value is
(a) closing the last coverage gaps with full rigor under your new constraints, (b) the merged
all-generations ranking as your permanent decision record, and (c) a fair shot for the
plasma/battery-adjacent lanes your updated profile emphasizes. If a V-candidate does crack the
top 5, the showdown file will say exactly why — and that would be worth knowing before 2029.
