# LEARNING_ROADMAP — markets from zero, semis as the lane

Design principle: your circle of competence is already semiconductors/hardware (EE PhD,
computer-engineering undergrad). The fastest route to real analytical skill is generic
finance mechanics (Stages 0–2) applied immediately to the sector you can actually judge
(Stage 3+). Timebox: 3–5 h/week. Each stage has a shippable deliverable — no deliverable,
no advancing.

## Stage 0 — Market mechanics + the boring baseline (weeks 1–2)

Learn: what a share is, how prices form (order books, bid/ask), market vs limit orders,
indices, ETFs, why low-cost index funds beat most active investors over decades
(this is the null hypothesis every stock pick must beat).
Read: Bogleheads wiki "Getting started"; Investopedia on order types; Bogle,
*The Little Book of Common Sense Investing* (short).
Deliverable: `20_JOURNAL/` entry — one page, own words: "how a stock price forms, and why
beating an index is hard." Initialize paper portfolio with a fictional 100,000 CNY +
10,000 USD ledger note at top of PAPER_PORTFOLIO.csv.

## Stage 1 — Reading financial statements (weeks 3–5)

Learn: income statement, balance sheet, cash-flow statement and how they interlock
(think: three coupled state equations — earnings are an accrual estimate, cash is the
measurement). Key ratios: gross/net margin, ROE, debt/equity, FCF. Where filings live:
SEC EDGAR (US 10-K), HKEXnews (HK), cninfo 巨潮资讯 (A-shares).
Read: Ittelson, *Financial Statements*; one real 10-K (suggest: a fabless or equipment
company you already know); one A-share annual report in Chinese (suggest: a WATCHLIST.csv
tier-B name).
Deliverable: two company one-pagers from `10_RESEARCH/_TEMPLATE_company_onepager.md`,
financial-snapshot sections filled from the filings themselves with [S###] cites.

## Stage 2 — Valuation + semiconductor economics (weeks 6–9)

Learn: multiples (P/E, EV/EBITDA, P/S) and what they implicitly assume; a simple DCF and
why its output is hypersensitive to growth/discount inputs (garbage-in amplifier);
sector specifics — fab capex cycles, utilization → margin leverage, memory cycles,
advanced packaging, why "design win" ≠ revenue.
Read: Damodaran's free NYU valuation materials (session notes + spreadsheets);
Miller, *Chip War* (context, fast read); TrendForce/SemiAnalysis pieces on the China AI
compute buildout.
Deliverable: valuation snapshot added to both Stage-1 one-pagers, each ending with one
sentence: "at today's price the market implies ___; I believe that is
optimistic/pessimistic because ___."

## Stage 3 — Thesis, paper trades, calibration (weeks 10+, ongoing)

Learn by doing: write a falsifiable thesis before any paper trade; pre-commit exit
criteria; log a probability with every prediction and score it (brier). Expect to be
wrong often — the goal is a calibrated error bar, not a hit rate.
Rules: max 5 open paper positions; every position links to a one-pager; every close gets
a `lesson` cell filled in.
Deliverable: weekly review, every Sunday, no exceptions. After 12 weeks: a
`10_RESEARCH/RB_##_what_i_got_wrong.md` retrospective.

## Standing case study (all stages)

RB_01 (Huawei 计算) and RB_02 (Ascend chain) are the running example: Stage 1 filings
practice uses its suppliers, Stage 2 valuation uses two of them, Stage 3 predictions test
the rumor pipeline (e.g., P001). Rumor → primary source → filing → valuation → prediction
is the full skill chain this lab exists to train.
