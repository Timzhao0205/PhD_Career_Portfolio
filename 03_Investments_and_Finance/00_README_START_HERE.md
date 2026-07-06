# 03_Investments_and_Finance — START HERE

**Created:** 2026-07-05 · **Owner:** Tim · **Status:** Scaffold (no positions, no compute run yet)

This folder is a complete personal-investing operating system in the same style as the
02_Startup research pipelines. Everything here is plain text: nothing executes, nothing
trades, nothing needs compute until you deliberately launch Claude Code.

---

## The map

| Folder | Role | Analogy to 02_Startup |
|---|---|---|
| `01_FOUNDATION/` | Constitution: IPS, compliance gate, education plan | MISSION docs, but for your money |
| `10_RESEARCH/` | One pipeline per project. `01_Ascend_Supply_Chain_2026-07/` is ready | Your research project folders |
| `20_FINDINGS/` | Durable conclusions + WATCHLIST across all projects | SYNTHESIS / FULL_RANKING |
| `30_JOURNAL/` | Append-only decision log (write BEFORE acting) | PROGRESS_LOG, but for decisions |
| `90_SOURCES/` | Shared library; drop PDFs in `inbox/` | BIBLIOGRAPHY (shared layer) |
| `99_ARCHIVE/` | Finished projects | 99_Archive |

## Reading order (human, ~1–2 hours, no computer work)

1. `01_FOUNDATION/IPS_DRAFT.md` — fill in the `[FILL]` fields. This is the constitution;
   every research run and every trade must comply with it.
2. `01_FOUNDATION/COMPLIANCE_GATE.md` — read fully. One item (OFAC NS-CMIC) is a hard
   legal gate for anyone physically in the US; resolve your personal status before any
   real-money action.
3. `01_FOUNDATION/EDUCATION_PLAN.md` — the staged reading list.
4. `10_RESEARCH/01_Ascend_Supply_Chain_2026-07/10_CHAIN_MAP/SEED_CHAIN_MAP.md` — the
   pre-loaded first-pass research from the 2026-07-05 session, with confidence tags.
5. `20_FINDINGS/WATCHLIST.md` and `FINDINGS_LEDGER.md` — current state of knowledge.

## When ready for the deep run (later, on your machine)

1. Review/edit `10_RESEARCH/01_Ascend_Supply_Chain_2026-07/01_MISSION/*` — especially
   SOURCE_STANDARDS.md and SCORING_RUBRIC.md.
2. Copy `.claude/settings.json` from one of your 02_Startup projects into the project's
   `.claude/` folder if you want the same auto-permissions (not included here so your
   existing, known-working config stays canonical). Same for a RUN_*.ps1 launcher —
   adapt your existing RUN_RESEARCH.ps1 pattern.
3. Open Claude Code in the project folder and paste `KICKOFF_PROMPT.txt`.
4. Human gates: the pipeline is designed to STOP for your review after Phase 1
   (chain map re-verification) and after Phase 4 (red team), per MASTER_STATE.json.

## Non-negotiables (also encoded in CLAUDE.md)

- Research output is never a buy/sell instruction. You are the portfolio manager.
- Every number must trace to a Tier-1/Tier-2 source (see project SOURCE_STANDARDS.md).
- Rumors are quarantined with a RUMOR tag, never silently blended into conclusions.
- The journal is append-only. Compliance gate precedes any actionable status.
