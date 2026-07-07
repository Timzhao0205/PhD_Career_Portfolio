# START HERE — Market Learning Lab

A reading-first lab for learning how markets, company analysis, and semiconductor supply
chains work — using the Huawei 计算 (computing) business and its Ascend supplier ecosystem
as the live case study.

## Ground rules (binding)

1. **PAPER ONLY.** No real transactions, no brokerage accounts, no order execution, ever,
   inside this folder. "Positions" exist only as rows in `30_FINDINGS/PAPER_PORTFOLIO.csv`.
2. **Not financial advice.** Nothing here (including AI-generated content) is a
   recommendation. Verdicts are limited to WATCH / RESEARCH-MORE / DROP.
3. **Number truth rule.** A price or financial figure may be written into any file only if
   it traces to a source in `90_SOURCES/sources.json`. AI memory is not a source.
4. If real investing ever becomes relevant later: that decision lives outside this folder,
   after checking personal visa/tax specifics with the international student office and a
   tax professional — not with an AI.

## Map

| Folder | Contents |
|---|---|
| `01_CURRICULUM/` | Staged learning roadmap, resource list, AI usage playbook |
| `05_STATE/` | Progress log + parked open questions |
| `10_RESEARCH/` | Research briefs (RB_##) and company one-pagers; seeded with the Huawei case |
| `20_JOURNAL/` | Dated entries + weekly reviews (the real product of this lab) |
| `30_FINDINGS/` | Watchlist, paper portfolio, predictions log (CSV, machine-readable) |
| `90_SOURCES/` | Source standards + citation ledger `sources.json` |

## The weekly loop (~3–5 h)

1. **Read** — current stage of `01_CURRICULUM/LEARNING_ROADMAP.md` (60–90 min).
2. **Research** — advance one brief or one-pager in `10_RESEARCH/`; verify one tier-C
   watchlist claim against a primary filing (60–90 min).
3. **Predict** — open or resolve one row in `30_FINDINGS/PREDICTIONS_LOG.csv` (10 min).
4. **Journal** — Sunday weekly review from the template (20 min).

## What is pre-seeded (2026-07-05)

- `10_RESEARCH/RB_01` — what 计算 actually is, what Huawei officially discloses, and where
  the "70B this year / 200B next year" rumor plausibly comes from, with source tiers.
- `10_RESEARCH/RB_02` — Ascend supply-chain map by layer, 13 listed names, each tagged
  with an evidence tier and a verification path.
- `30_FINDINGS/WATCHLIST.csv` — same names, ready for the verification exercise.
- `90_SOURCES/sources.json` — S001–S016.

## Future Claude Code work

Deliberately deferred to keep local processing light. Mission backlog and operating rules
are pre-written in `CLAUDE.md`; when ready, open Claude Code in THIS folder and say
"run mission M1". Docs: https://docs.claude.com/en/docs/claude-code/overview
