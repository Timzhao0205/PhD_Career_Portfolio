# Ascend Supply Chain Research — START HERE

Pipeline order: 01_MISSION (rules) -> 05_STATE (progress) -> 10_CHAIN_MAP (Phase 1,
pre-seeded) -> 20_COMPANY_DOSSIERS -> 30_SCORING -> 40_REDTEAM -> 50_THESES ->
99_AUDIT. Cross-project outputs land in ../../20_FINDINGS/.

Human setup before kickoff:
1. Review 01_MISSION/* and edit anything you disagree with.
2. Copy .claude/settings.json from a 02_Startup project into .claude/ here (kept out
   of this scaffold so your known-working config stays canonical). Optionally adapt
   your RUN_RESEARCH.ps1 as RUN_RESEARCH.ps1 here.
3. Open Claude Code in this folder, paste KICKOFF_PROMPT.txt.

Two human gates are built in (after Phase 1 and Phase 4) — the run is intentionally
NOT fire-and-forget, because this pipeline feeds real-money decisions.
