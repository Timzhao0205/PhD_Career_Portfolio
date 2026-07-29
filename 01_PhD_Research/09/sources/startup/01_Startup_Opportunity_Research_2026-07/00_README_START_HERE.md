# START HERE — Autonomous Startup Opportunity Research

Everything is pre-wired. You type **one command**, and Claude Code (Fable) runs a 7-phase,
multi-agent, source-verified research mission to completion inside this folder.

## What you'll get

- 10 domain landscape briefs → **≥36 candidate startup ideas** → scored matrix → red-team reviews
  → **12 investment-grade deep dives** → US/China policy brief → **Top-7 executive summary +
  2026→2030 roadmap** → **≥200-source bibliography** → self-audit report.
- Diversity rules are enforced: majority standalone products (not diagnostics), majority outside
  your thesis lane, every idea assessed for China-first AND US entry, all timed for a 2029/2030
  launch. Full spec: `01_MISSION/MISSION_BRIEF.md`.

## One-time setup (≈5 min)

1. **Install Claude Code** (PowerShell):
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```
   Installing [Git for Windows](https://git-scm.com/downloads/win) is recommended so Claude Code
   gets a proper Bash tool (it falls back to PowerShell without it — still works).
2. **Log in once** with your Max account: run `claude` in any folder, complete the browser login,
   then `/exit`.
3. Place this folder at `PhD_Career_Portfolio\02_Startup\01_Startup_Opportunity_Research_2026-07\`
   (it ships as exactly that — just extract the zip into `02_Startup\`).

## Run it

```powershell
cd <path>\PhD_Career_Portfolio\02_Startup\01_Startup_Opportunity_Research_2026-07
.\RUN_RESEARCH.ps1
```

That's the entire human interaction. If PowerShell blocks the script:
`powershell -ExecutionPolicy Bypass -File .\RUN_RESEARCH.ps1`

Manual fallback (identical effect, no script): start
`claude --dangerously-skip-permissions --model claude-fable-5` in this folder and paste the
contents of `KICKOFF_PROMPT.txt` as your only message.

### Modes

- **Default (`full`)** — zero prompts, uses `--dangerously-skip-permissions`. This is what you
  asked for (least human interaction). Honest caveat: that flag disables *all* permission checks
  for the session; the mission's CLAUDE.md confines Claude to this folder by instruction, not by
  OS enforcement. Anthropic recommends this flag mainly for isolated environments.
- **`.\RUN_RESEARCH.ps1 -Mode guarded`** — enforced guardrails (`acceptEdits` + the allow-list in
  `.claude/settings.json`). Expect a handful of one-time approvals early on (press `a` for
  "always allow"), then it runs hands-free. Recommended if you'll leave the machine unattended
  and want defense-in-depth.

### If it stops (rate limit, sleep, closed window, crash)

State is written to disk after every phase and wave, so nothing is lost:

```powershell
.\RUN_RESEARCH.ps1 -Resume
```

It re-reads `05_STATE/MASTER_STATE.json` and continues from the first incomplete phase.
Disable Windows sleep for the run (Settings → Power → Never), and keep the terminal open.

### Monitoring (optional)

Watch `05_STATE/PROGRESS_LOG.md` and the phase folders fill up. Inside the session, `/usage`
shows plan-limit consumption. Done = `99_AUDIT/FINAL_AUDIT.md` exists and the terminal prints the
completion summary with the Top 7.

## Budget & runtime expectations

- Expect a long session: **several hours** wall-clock; parallel subagent waves are the main
  accelerator. Total token volume is large (multi-agent runs typically consume several times a
  normal session).
- Model policy (set per-agent in `.claude/agents/*.md`): **Fable** for orchestration, deep
  dives, red-team, policy, and synthesis — the judgment-heavy work; **Sonnet** for the 10
  landscape scouts and the auditor — high-volume search/verification where Sonnet is fast,
  cheap, and excellent. This is the best accuracy-per-dollar split for a $150 ceiling.
  - Want literally everything on Fable? Change `model: sonnet` → `model: inherit` in
    `domain-scout.md` and `source-auditor.md`. Expect roughly 2–4× the usage burn in Phase 1/7
    and a higher chance of hitting your weekly Max limit mid-run.
- On a Max subscription, usage draws from your plan's session/weekly limits rather than
  pay-per-token; if you hit a limit, the run pauses — just `-Resume` after the reset shown in
  `/usage`. If you instead run on API credits, $150 should cover the hybrid configuration
  comfortably; an all-Fable run may not.

## Where the answers land

| You want… | Open |
|---|---|
| The bottom line | `60_PHASE6_SYNTHESIS/00_EXECUTIVE_SUMMARY.md` |
| What to do 2026→2030 | `60_PHASE6_SYNTHESIS/01_ROADMAP_2026_2030.md` |
| Full 12 deep dives | `40_PHASE4_DEEPDIVES/` |
| Every idea + scores | `30_PHASE3_SCORING/SCORING_MATRIX.md`, `60_PHASE6_SYNTHESIS/02_FULL_RANKING.md` |
| Bear cases | `30_PHASE3_SCORING/REDTEAM_*.md` |
| US/China rules | `50_PHASE5_POLICY/POLICY_BRIEF.md` |
| All 200+ sources | `90_BIBLIOGRAPHY/BIBLIOGRAPHY.md` |
| Did it check itself? | `99_AUDIT/FINAL_AUDIT.md` |

## Design notes (why it's built this way)

- **Fresh & unbiased:** CLAUDE.md forbids reading anything outside this folder and requires every
  claim to trace to a source gathered in this run — your "no prior memory" requirement, enforced.
- **Your PhD = skillset:** hard quota that ≥50% of ideas sit outside the GaN-sensor/fusion-
  diagnostics lane; the IEEE paper in `01_MISSION/REFERENCE/` is used only as capability evidence.
- **Standalone-product bias** and the diagnostics cap are hard constraints, audited in Phase 7.
- **Source rigor:** tiered standards (IEEE/peer-reviewed/policy prioritized; arXiv is
  discovery-only), fetch-verified load-bearing numbers, and a 20-link re-verification audit.
- **Crash-proof:** every phase/wave checkpoints to `05_STATE/`, so interruption costs minutes,
  not hours.

Two operator cautions: (1) full-auto mode's tradeoff is stated above — it's your call;
(2) the policy brief is research, not legal advice — before any 2029 China/US structuring
decision, have counsel review it.
