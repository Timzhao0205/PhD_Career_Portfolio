# START HERE — Round 3: C12 + C10 Strategy, Competitors & IP Whitespace

One command. Claude Code (Fable, **session effort = MAX**) takes your two locked winners —
**C12** (NI/MI-HTS winding cells + inline QC + recipe software) and **C10** (fast-dynamics
precision magnet power converters) — and produces four things Rounds 1–2 never attempted:

1. **Competitor deep map** (8 segments, EN + 中文): who they are, what they ship, and a
   register of 20–40 *specific unsolved problems* with evidence.
2. **Patent landscape US + CN** (10 technology clusters, ≥150 verified patents, ≥50 Chinese):
   every number fetched and read, never recalled from memory.
3. **Whitespace → invention disclosures**: 15–25 scored whitespace slots → 10–14 drafted
   invention disclosures, each red-teamed against prior art, ending in a
   **FILE-CANDIDATE / REWORK / DROP** verdict (target ≥6 FILE-CANDIDATE).
4. **Strategy pack**: C12 + C10 playbooks, the C12×C10 cluster play, and an
   **IP roadmap 2026→2029** sequenced around your publication plans so a paper never kills
   a filing.

## Three decisions I locked (override = one line each)

1. **Scope = C12-cluster + C10 only.** C33 (coil QC) is treated as a C12 module and C11
   (quench protection) as a C10 module — matching the Round-2 final showdown's cluster
   verdict. No new idea generation. *Override:* edit the scope line in
   `01_MISSION/MISSION_BRIEF_V3.md`.
2. **Patent work = landscape + whitespace, not legal opinions.** The run maps who owns what
   and drafts disclosure documents an attorney can work from. It never renders
   freedom-to-operate or patentability opinions — every 40/50/60 file carries a mandatory
   disclaimer, and the audit fails the mission if one is missing. *Override:* none offered;
   this one protects you.
3. **The Stanford/UIUC wall + file-before-publish are enforced, not advisory.** Every
   invention disclosure must pass a written 4-prong independence test (outside funded scope;
   personal time/funds/equipment; no Stanford confidential info; no SNF/lab/compute) or it's
   marked BLOCKED-PENDING-COUNSEL. And because **China has no general grace period**, the IP
   roadmap sequences provisionals *before* your planned SUST/IEEE-TAS benchmark papers.
   *Override:* delete prongs in `01_MISSION/IP_GROUND_RULES.md` — not recommended.

## Setup & run

1. Install/log in once (skip if done): `irm https://claude.ai/install.ps1 | iex`, then
   `claude` → browser login → `/exit`.
2. Extract this zip into `PhD_Career_Portfolio\02_Startup\` so it sits **next to**
   `02_Novel_Lanes_Research_2026-07\` (the launcher auto-syncs the Round-2 finals and the
   four deep dives from there into `00_PRIOR_CORPUS\`; if the sibling is missing it falls
   back to the shipped copies — the package is self-contained either way).
3. Run:
   ```powershell
   cd <path>\PhD_Career_Portfolio\02_Startup\03_C12_C10_Strategy_IP_2026-07
   .\RUN_STRATEGY.ps1
   ```
   That's the whole interaction. Blocked script? `powershell -ExecutionPolicy Bypass -File .\RUN_STRATEGY.ps1`
   Stopped mid-run (weekly limit, sleep, crash)? `.\RUN_STRATEGY.ps1 -Resume` — state is
   checkpointed after every phase and wave. Disable Windows sleep for the run.

Manual fallback: in this folder, `$env:CLAUDE_CODE_EFFORT_LEVEL='max'` then
`claude --dangerously-skip-permissions --model claude-fable-5` and paste `KICKOFF_PROMPT.txt`.

## Effort policy

- The launcher sets `CLAUDE_CODE_EFFORT_LEVEL=max` → orchestrator and every inheriting
  subagent (competitor analysts, invention designers, IP red teams, strategy synthesis) run
  at **max**.
- The two search-reach-bound agents — `patent-scout` and `source-auditor` — are pinned to
  `effort: high` in their frontmatter (fetch-and-read work; max there only burns tokens
  re-pondering the same claim text). Verify in-session anytime with `/effort`.

## Budget honesty

~45 subagent runs total (8 competitor + 10 patent-scout + ~14 designers + ~14 red teams +
audit), comparable to Round 2's burn. The patent-scout passes are the heavy part — each
fetches and reads 15–25 patents across five search passes including a mandatory
Chinese-language pass. On a Max plan the realistic risk is the **weekly limit mid-run**; the
design assumes it: `-Resume` continues losslessly after reset (`/usage` shows timing). Fable
draws usage much faster than Opus, so start early in your weekly window.

## What you'll read when it's done

| You want… | Open |
|---|---|
| **The 5-minute answer** (what to build, what to file, what to ask at ASC) | `60_STRATEGY/00_EXEC_BRIEF.md` |
| C12 startup strategy (beachhead, moat, kill gates) | `60_STRATEGY/STRATEGY_C12.md` |
| C10 startup strategy | `60_STRATEGY/STRATEGY_C10.md` |
| How the two combine (and what to do at ASC 2026) | `60_STRATEGY/CLUSTER_PLAYBOOK.md` |
| **When to file what, vs. when you publish** | `60_STRATEGY/IP_ROADMAP_2026_2029.md` |
| The scored whitespace map (all 15–25 slots + verdicts) | `40_WHITESPACE/WHITESPACE_REGISTER.md` |
| The invention disclosures + red-team verdicts | `50_INVENTIONS/` |
| What competitors haven't solved (U-### register) | `20_UNSOLVED/UNSOLVED_REGISTER.md` |
| Every patent cited, one table (US + CN) | `90_BIBLIOGRAPHY/PATENT_INDEX.md` |
| Self-audit incl. patent re-verification + Stanford-wall table | `99_AUDIT/FINAL_AUDIT.md` |

## Design notes

- **The PATENT TRUTH RULE is the spine:** no patent number appears in any output unless the
  agent fetched that exact document and recorded title + assignee at time of use. The
  Phase-6 audit re-fetches a random 15 and fails the mission on any mismatch. Hallucinated
  patent numbers are the classic failure mode of LLM patent work; this design treats one as
  mission-fatal.
- **Whitespace claims are bounded, never absolute:** the register says "no results in the
  searches run" (with the queries listed), never "no patent exists" — that distinction is
  what makes the output usable by a real attorney later.
- **China is searched in Chinese:** competitor segments CS-B/CS-G and every patent cluster
  run mandatory 中文 passes (无绝缘 / 干式绕线 / 实用新型 utility models included) —
  consistent with your China-as-supply-chain-and-radar posture from Round 2.
- Same operator cautions as before: full-auto disables permission checks (folder confinement
  is by instruction; `-Mode guarded` for enforced rails).

## Honest framing before you spend the tokens

This run produces **research and drafting aids, not legal work product**. A FILE-CANDIDATE
verdict means "survived an adversarial prior-art search and is worth attorney time" — a
registered patent attorney (and, for anything borderline, a Stanford OTL/SU-18 conversation)
still stands between these documents and a filing. What the run *does* buy you: you walk
into ASC 2026 knowing exactly which unsolved problems to probe, which claims are already
fenced off in both jurisdictions, and which 6+ inventions you could file as provisionals
before your own papers become prior art against you. The interviews remain the decisive
experiment — this arms them.
