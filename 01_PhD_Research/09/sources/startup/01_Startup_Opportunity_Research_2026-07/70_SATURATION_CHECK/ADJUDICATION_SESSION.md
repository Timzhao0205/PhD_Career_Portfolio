# ADJUDICATION SESSION — the one Claude Code job worth running (max effort, bounded)

## Why this session and not a regeneration run
Generation coverage is settled (see SATURATION_REPORT.md). This session does the only remaining
compute-buyable work: formally adjudicating 7 rows into your evidence-adjusted ranking with the
same discipline your pipeline used. It is judgment-dense, small-context, and correctness-critical
— exactly the profile where max effort pays.

## Budget guardrails (moderate = roughly one evening of a Max week)
- ONE session. NO subagents (Task calls multiply tokens 4–7×; forbidden here).
- ≤ 6 web fetches per row, ≤ 45 total. Fetch only to (a) verify annex sources before any number
  becomes load-bearing, (b) close a named uncertainty (e.g., "has a vendor occupied slot X since
  2025"). No open-ended browsing.
- Read only: 01_MISSION/SCORING_RUBRIC.md, SOURCE_STANDARDS.md, 02_FULL_RANKING.md,
  03_MAX_EFFORT_DELTA.md, the relevant DD/policy files on demand, the two prior-generation files
  (june25, frontier/china), and 70_SATURATION_CHECK/*.
- Write only: 70_SATURATION_CHECK/ADJUDICATION_VERDICT.md, an appended marked section in
  02_FULL_RANKING.md, ledger entries, and (only if C02 survives) a DD_C02 file.
- Do NOT re-derive any existing candidate's score except C02. Do NOT touch the roadmap.

## Launch (PowerShell, from the research folder)
```powershell
cd <path>\02_Startup\01_Startup_Opportunity_Research_2026-07
claude --model claude-fable-5 --dangerously-skip-permissions
```
Then, as your FIRST input, type exactly:  `/effort max`
(Setting effort inside the session removes the flag ambiguity that likely made your earlier
"max" run execute at high. Confirm the status bar/`/effort` shows max before pasting the prompt.
Note: max applies to this session only — that's fine, this is one session.)

Then paste everything below the line as your second input, and walk away.

---------------------------------------------------------------------------------------------
Read CLAUDE.md, 01_MISSION/SCORING_RUBRIC.md, 01_MISSION/SOURCE_STANDARDS.md,
60_PHASE6_SYNTHESIS/02_FULL_RANKING.md, 60_PHASE6_SYNTHESIS/03_MAX_EFFORT_DELTA.md, and
70_SATURATION_CHECK/SATURATION_REPORT.md + ADJUDICATION_ANNEX.md. Two prior-generation reference
files are in 70_SATURATION_CHECK/REFERENCE/ (june25_research.md, frontier_rank_red_team.md,
china_feasibility_deep_dive.md); their citations are stale until re-verified.

Task: formally adjudicate the 7 annex rows (C02, N04, N05, N06, N08, R1, R2) into the ranking.
For each row, in order: (1) verify or refute the annex's premise — its sources are
snippet-verified only; fetch before relying (≤6 fetches/row, ≤45 total, no subagents);
(2) run a compressed red-team (strongest kill, hidden competitors incl. Chinese, founder-fit
doubts); (3) score all 11 rubric criteria + gates, then apply the mission's adjustment
discipline — since these get a compressed rather than full pipeline, report BOTH the adjusted
score and a conservative expected score using the mission's observed statistics (mean full
−11.4 from raw; −8.9 DD-stage for premise-level kills); (4) classify vs. the existing 40:
duplicate / variant-of-Cxx / novel; (5) verdict: standalone company, cluster product line,
tripwire-gated option, or kill — with explicit kill criteria and, for N06, a separate assessment
as a C12-cluster expansion line. C02 gets the fullest treatment (it is the ranking's own open
condition; re-derive its China leg under the current policy brief, not Gen-2's posture).

Then: (a) write 70_SATURATION_CHECK/ADJUDICATION_VERDICT.md — per-row verdicts, a final
saturation statement (does ANY row displace any top-12 member; is the top-7 stable), and the
N07 one-liner; (b) append a clearly-marked "Saturation adjudication (date)" section to
02_FULL_RANKING.md inserting the 7 rows at their expected-score ranks WITHOUT renumbering or
altering existing rows; (c) log every source you actually fetched into 90_BIBLIOGRAPHY/
sources.json per schema (continue S-numbering; mark lang/tier); (d) append one line each to
03_MAX_EFFORT_DELTA.md and 05_STATE/PROGRESS_LOG.md. Honesty rules: annex preliminary scores are
estimates to be overturned freely; if evidence contradicts the annex or the mission corpus, say
so plainly; no invented sources; quotes ≤25 words. Do not ask me questions; note assumptions in
the verdict file. Finish by printing the 7 verdicts and whether the top-7 changed.
---------------------------------------------------------------------------------------------

## After it finishes
Read ADJUDICATION_VERDICT.md. Expected outcome per the report: top-7 unchanged, N06 recorded as
a cluster line, most rows killed-with-reasons. If ANY row lands in the top 12, that is a real
signal — commission a full red-team + deep dive for that one row before believing it.
