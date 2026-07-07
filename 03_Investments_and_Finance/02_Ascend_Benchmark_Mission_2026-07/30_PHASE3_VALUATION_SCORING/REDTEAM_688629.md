Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_688629 — 华丰科技 Sichuan Huafeng Technology (SSE-STAR 688629)

Red-team brief: attack, do not balance. Scored row under attack (initial, rank 1 of 14, the ONLY
name clearing the 3.0 portfolio bar): W1=4, W2=5, W3=3, W4=1, W5=5, W6=1, total 3.30. Inputs:
V_688629.md, F_688629.md, VAL_688629.md, SCORES.csv, SCORING_NOTES.md, 01_MISSION/SCORING_RUBRIC.md.
New sources this session: [S700]–[S702], ledgered in 90_BIBLIOGRAPHY/frags/rt_688629.json (all zh-language
fetches, accessed 2026-07-07). Headline: **six of six cells are disputed; a single two-notch concession on
W2 alone (5→3) takes the total to 2.90 and leaves ZERO names above the 3.0 bar — the whole answer key's
shape rests on the most contestable cell in the matrix.**

---

## 1. Strongest bear case (5 bullets)

- **B1 — The FY2025 "turnaround" is an income-statement event; cash went the other way.** Net profit
  attributable CNY 358.57M, but operating cash flow was **-CNY 2.49M — the second consecutive negative
  year** (FY2024: -3.09M) [S266; F_688629]. Where the profit went: receivables ended FY2025 at **CNY 1,141M,
  +104.09% YoY, = 45.13% of revenue**, and inventory at CNY 529M, +64.41% [S700 — same underlying jiemian
  article as ledgered S278, Sina mirror re-fetched this session for the balance-sheet detail P1/P2 did not
  extract]. Cash fell to CNY 280M (-27.41%) against CNY ~400M of short-term borrowings + notes due within
  one year [S700]; net cash +565.92M (FY2023) → net debt -108.32M (FY2025); FY2025 FCF ≈ -2.49 - 395.70
  capex = **-CNY 398M** [F_688629]. The counter-datum (Q1-2026 OCF +427.80M) is a single quarter whose
  driver F_688629 explicitly could not decompose — evidence gap, not evidence.
- **B2 — 60.52% single-customer concentration, accelerating INTO a risk that has already fired twice in the
  filing record.** Top-1 (corroborated Huawei) 25.36% → 37.11% → 60.52% of revenue FY2023→FY2025 [S266;
  S268; S276]; supplier top-5 concentration simultaneously 24.91% → 61.41% [S268] — both sides of the
  business concentrate. Episode 1: Huawei procurement of high-speed backplane connectors fell from H2-2020;
  2021 comms-connector sales volume **-42.24%**, capacity utilization **84.04% → 51.61%** [S272]. Episode 2:
  FY2024, a **loss year inside the current 3-FY scoring window** (headline -17.75M; **-78.26M
  ex-non-recurring**, i.e. 3.4x deeper; GM 18.47%) [S266; F_688629] — and it occurred while Huawei's revenue
  share was RISING, i.e. concentration growth and fundamental deterioration have already co-occurred at this
  company. Huawei is simultaneously customer (60.52%), indirect shareholder (Hubble, 3.47% at subscription
  [S273]), and co-/sole-owner of the jointly developed 56G+ connector IP with a non-compete barring sales to
  its domestic telecom rivals [S273] — the diversification path is contractually capped.
- **B3 — The Ascend attribution is a market construct, not a company one (prime tier-C dependency).** Zero
  昇腾/超节点 characters in the FY2025 annual report [S266], the Q1-2026 report [S270], the entire captured
  互动易 reply history into 2026 [S267], and the 2025-12-02 placement-inquiry response [S277] — confirmed by
  a fresh zh-search pass this session. The best locatable carrier of the "dominance" narrative is a
  self-media piece (BT财经, 腾讯新闻 rain, 2026-04-28): "被多方来源列为昇腾950PR/Atlas 350**唯一国产量产的
  224G**高速背板连接器供应商，**据报道**...市占率超过70%" — no named analyst, no filing, no citation
  ("据报道" only) [S702]; and its "唯一国产量产224G" claim **directly contradicts the company's own disclosed
  224G status** ("已与华为等主要客户开展项目合作、交流" — cooperation/sample stage, not mass production)
  [S267]. The one quantified Ascend figure in circulation (40万套/CNY 6bn) is labeled "Market Rumor
  (Unverified)" by the only source addressing it and is arithmetically impossible (>2x total FY2025 revenue)
  [S278]. The Ascend-specific revenue share is NOT-ESTIMABLE per the mission's own audit [V_688629].
- **B4 — 216x trailing earnings for a connector house whose NAMED connector segment earns 17.19% gross
  margin and falling.** P/E ttm 216.20x, static 260.39x, P/S ttm 33.89x [VAL_688629] — 2.6x the multiple of
  the next-most-expensive verified-link name. The margin story rides entirely on the 组件 (components) line
  (61.53% of FY2025 revenue at 39.75% GM), whose equivalence to the AI cable-module business is an
  **unconfirmed inference** (F_688629's own flag); the 连接器 line — the layer the thesis names — earned
  17.19% GM in the boom year, down from 27.12% in FY2023 [S553; F_688629]. Meanwhile R&D intensity nearly
  halved (10.45% → 6.36%) [S266] in the year the moat narrative got priced. VAL_688629's own conclusion: the
  price embeds "an unverified competitive-dominance premium" on top of years of assumed uninterrupted
  hypergrowth.
- **B5 — Second-sourcing is live, not hypothetical.** The company's own standing language is "核心供应商
  **之一**" — one of several — for 2+ years [S267; S269]. 西部证券 (tier B) lists 意华股份/航天电器 beside
  华丰科技 in the identical backplane-connector category [S204]. 意华股份's official investor-platform reply
  (2025-09-25, via mirror): "我们的高速连接器，可应用于超节点算力场景！" — the alternate supplier is
  publicly auditioning for the same socket, with commentary putting its own Huawei revenue share at ~34%
  [S701, tier 4, signal only]. On the other side of the ledger, 华丰's diversification beyond Huawei was
  still at sample/small-batch, zero mass orders, at IPO review [S274], and **no fetched source quantifies
  any non-Huawei share of current revenue** (evidence gap) — the ByteDance/Alibaba names in the placement
  reply [S277] are target customers of future capacity, not booked revenue.

---

## 2. Score audit — every cell, supported or corrected

Weights: W1 .20, W2 .20, W3 .15, W4 .20, W5 .15, W6 .10. Current total 3.30 (arithmetic verified).

| Cell | Current | Supported by cited file? | Red-team proposal | Delta |
|---|---|---|---|---|
| W1 | 4 | **NO** — contradicts V_688629's own tier assignment | **3** | -0.20 |
| W2 | 5 | **NO** — inconsistent with the mission's own scoring practice; thesis-relevant share NOT-ESTIMABLE | **3** (strict reading: 0) | -0.40 |
| W3 | 3 | **WEAK** — anchor text fits 1-2 better; cited justification contains an unsupported claim | **2** | -0.15 |
| W4 | 1 | **CONTESTED** — tier classification of what is being priced | **0** | -0.20 |
| W5 | 5 | **NO** — inconsistent with the 002281 precedent in the same notes | **4** | -0.15 |
| W6 | 1 | **NO** — misreads the rubric's own 0-anchor | **0** | -0.10 |

Corrected row: W1=3, W2=3, W3=2, W4=0, W5=4, W6=0 → **total 2.10** (falls from rank 1 to ~rank 7, behind
300308 2.60, 002261/301236 2.35, 600498 2.30, 002371 2.15).

**Sensitivity (single concessions):** W2 5→3 alone → **2.90 (bar fails)**. W1 alone → 3.10; W3 alone → 3.15;
W4 alone → 3.10; W5 alone → 3.15; W6 alone → 3.20. Most two-cell combinations without W2 also breach or
touch the bar (W1+W3 = 2.95; W1+W4 = 2.90; W1+W5 = 2.95; W4+W5 = 2.95; W3+W5 = 3.00). **If any single
substantive challenge below is conceded at W2, or any two elsewhere, no name in the universe clears 3.0 and
Phase 4's rubric-mandated answer becomes the cash-heavy "no strong answer."** The orchestrator must respond
to each cell in writing before G3.

### W1 = 4 → propose 3

Rubric: 5 = tier A (own filing/IR names the business); 3 = tier B. V_688629's own conclusion for the claim
as worded ("...into Huawei **Ascend** systems"): "**This audit assigns Tier B to Claim 1 as literally
worded**." Rubric maps tier B → 3, full stop. The 4 is an interpolation ABOVE the file's own tier — it
re-credits the same own-statement fragments ("华为高速背板连接器核心供应商之一", data-center scoping,
AI-server growth language) that the P1 auditor already weighed when concluding Tier B rather than A. Scoring
consistency check: 002261 earned its 5 with 昇腾 verbatim in its own annual report; 688629 has zero 昇腾
anywhere in any company statement, ever, and the FY2025 AR does not even contain 华为 in the fetched
rendering [S266]. Compressing the gap between "names the chain in its own filing" and "has never said the
word" to a single point is not defensible. The tier-A sub-claim (generic Huawei backplane supplier) is a
different claim from the one under score — the watchlist claim is Ascend-specific, and its dominance half is
UNVERIFIED leaning tier C [V_688629]. W1=3.

### W2 = 5 → propose 3 (strict consistency reading: 0) — THE KEYSTONE CELL

The 60.52% is real, filing-anchored, and growing — as a **Huawei-all-products ceiling including legacy
telecom** (a relationship that predates Ascend: 21.40%/35.87%/20.75% of revenue 2019-2021 [S272; S273]).
V_688629 is explicit: "**Ascend/AI-server-specific sub-share NOT-ESTIMABLE** with any defensible arithmetic
from sources fetched this session." Four attacks:

1. **The scoring practice elsewhere in SCORING_NOTES gates W2 on thesis-specificity, and 688629 was
   exempted.** 600839's generic-Huawei ICT distribution — filing-verified at ~37% of revenue — scored
   **W2=0** ("Ascend-specific NOT-ESTIMABLE"). 002371's 93.34% exposed-base: "NOT Huawei-specific and is
   not credited" → 0. 688981's China-region 85.6%: "context, not Huawei-specific" → 0. Applying the 600839
   standard to 688629 — whose Ascend-specific share the mission's own V file declares NOT-ESTIMABLE — gives
   **W2=0**, not 5. If instead the literal anchor text ("Huawei-linked share") governs, then 600839's W2=0
   is wrong and must be rescored upward, and the orchestrator must explain in writing why an Ascend
   benchmark's exposure dimension rewards legacy base-station connector revenue. One standard; pick it;
   apply it to all 14.
2. **The composition of the 60.52% is unknown, and the known history says the non-AI part is large.** No
   source decomposes Huawei revenue into Ascend/AI-server vs. legacy telecom [V_688629 exposure section].
   The >95%-to-Huawei figure sometimes waved at this question is 2019-2021, sub-56G, pre-AI-buildout, and
   V_688629 explicitly rules it non-carry-forward.
3. **"Growing" is doing unearned work in the anchor.** Huawei-linked share also grew in FY2024
   (25.36→37.11%) — the loss year with GM 18.47% [S266; S268; S276]. In this company's own record,
   "Huawei share >30% and growing" has coincided with deteriorating fundamentals; the anchor's implicit
   premise (growing share = growing thesis value) fails locally.
4. **Even the trend line is tier-3 for 2/3 of its points.** Only FY2025's 60.52% is filing-anchored; FY2024
   is 37.11% [S268/S276] vs. ~35%/CNY 382M [S278/S700] — an unresolved ~2pt source conflict logged per
   SOURCE_STANDARDS.

Middle-ground correction, mirroring how bounded-but-bundled ranges were scored elsewhere (301236: 19-45%
bundled ceiling → 3; 002261: 21.7-50.4% → 3): treat the Ascend-linked share as a bounded 0-60.52% range
with own-filing qualitative support that the AI slice is "real and rising" [S270] → **W2=3**. Retaining 5
requires a written justification that survives the 600839 comparison; the red team's position is that no
such justification exists.

### W3 = 3 → propose 2

Anchor 1 reads "deteriorating margins OR persistent cash burn." OCF was negative in **two consecutive
fiscal years** while headline profit swung +376M — and the scoring window also contains a loss year whose
ex-non-recurring loss was 3.4x the headline (-78.26M), with positive non-recurring props to headline profit
in **all three years** (+45.98M/+60.51M/+28.05M) [F_688629]. Cash fell every year (777→386→280M); every debt
line rose; net cash flipped to net debt; FY2025 FCF ≈ -398M. New this session: receivables +104.09% to 45.13%
of revenue, inventory +64.41%, and CNY 280M cash vs ~400M short-term obligations [S700]. On the fiscal-year
grid the scores rest on, that is persistent cash burn (anchor 1) offset by genuinely rising FY2025 margins
(anchor-5 element) → the defensible interpolation is **2**, not 3. Peer consistency: 301236 took W3=1 for
ONE year of negative OCF plus a net-cash swing (its margins were falling — hence 688629 sits one notch above
it, at 2, not two notches at 3). Also a citation-discipline defect the orchestrator must correct in writing:
SCORING_NOTES' W3 cell asserts "profit not converting to cash; **receivables build**" — at scoring time NO
mission file contained receivables data (F_688629: "receivables/inventory/payables detail was not fetched...
NOT independently decomposed"). The claim happens to be true — [S700], fetched by the red team — but as
written the cell cited a fact not in evidence. Adopt [S700] as the cell's source or strike the phrase.

### W4 = 1 → propose 0

Rubric: 1 = PRICED-FOR-PERFECTION; 0 = PFP **on tier-C evidence**. The question is what evidence supports
the thing being priced. VAL_688629's own words: the multiple "prices in ... **an unverified
competitive-dominance premium**," and V_688629 grades the dominance claim "UNVERIFIED, leaning Tier C." A
216x ttm / 260x static P/E is not the price of "supplies Huawei backplane connectors" (tier A) plus one
strong year; the increment above every peer multiple is carried by the sole-supplier/70%-share narrative,
whose best locatable carrier is an unattributed self-media article [S702] that contradicts the company's own
224G maturity disclosure [S267]. Names where the priced narrative was tier C took 0 (002281, 002916, 002156,
301018). If the orchestrator holds W4=1 on the grounds that the supply LINK is tier ≤B, the written response
must state that reading explicitly and confirm it was applied uniformly — noting the asymmetry that for
688629 the tier-A fact and the priced story diverge more widely than for any other name in the universe.

### W5 = 5 → propose 4

Connectors are the rubric's named layer — but SCORING_NOTES itself established that company position within
the named layer adjusts the score: 002281 took **4** because it is "mid-pack globally with a large
telecom-legacy mix." Every element of that discount applies here, plus three more: (a) the named 连接器 line
earned 17.19% GM in FY2025, down from 27.12% FY2023 — margin compression in the boom year, monopsony
pricing in action [S553; F_688629]; (b) the high-margin 组件 line's identity as the AI cable-module business
is an unconfirmed inference [F_688629]; (c) the "moat" is partially owned by the customer — 56G+ IP jointly
or Huawei-solely held, with a non-compete capping the addressable market [S273] — and the company is
domestic-only (98.45% of revenue) with self-declared "之一" status in a three-vendor domestic field [S204;
S267]. A layer-5 with company-position discounts identical to (or worse than) 002281's is a 4. W5=4.

### W6 = 1 → propose 0

Rubric 0-anchor: "single-customer + internalization precedent **(cf. in-house HBM)**." The anchor's own
parenthetical DEFINES the precedent as Huawei's in-house-HBM behavior — a cross-layer demonstration of
appetite. SCORING_NOTES' defense of 1 ("connector internalization by Huawei has no direct precedent")
rewrites the anchor to require a layer-specific precedent, under which reading no company could ever score
0 until after its thesis had already died — the anchor becomes unreachable and the cell unfalsifiable.
688629 is the anchor's central case: highest verified single-customer concentration in the universe (60.52%,
rising; cf. 002156's 52.29% which took W6=2), supplier-side concentration 61.41%, customer-as-shareholder
(Hubble), and — the internalization-adjacent fact the current score ignores — **Huawei already co-owns or
solely owns the jointly developed 56G+ connector IP** [S273]: the technology layer is partially inside
Huawei today, contractually. Add a named two-vendor domestic alternate list [S204] and an alternate publicly
claiming supernode applicability [S701], and the demonstrated 2021 demand whipsaw [S272]. W6=0.

---

## 3. Verticalization test

If Huawei internalizes or even just dual-sources high-speed backplane connectors, the thesis does not
degrade — it breaks, because every enabling condition is already in place. Precedent: Huawei's in-house HBM
shows it will backward-integrate supply-constrained AI-system layers, and connectors are a lower barrier
than HBM — precision stamping/molding/plating and signal-integrity design, not DRAM stacking; more to the
point, Huawei already **owns the hard part**: the 56G+ connector IP from joint development is jointly or
Huawei-solely held, with a non-compete that binds 华丰 but not Huawei [S273], and Hubble's equity stake gives
inside visibility into 华丰's costs and capacity [S273]. The cheap first move is not a Huawei connector fab
but dual-sourcing, and that auditioning is already public: 西部证券 names 意华股份/航天电器 in the same
backplane-connector slot [S204], and 意华's official platform reply claims supernode applicability outright
[S701] — note the asymmetry that the alternate says "超节点" while 华丰 never has. Mechanically, 60.52% of
revenue (~CNY 1.53bn) faces a single procurement decision; the connector line's GM already compressed to
17.19% in the boom year [S553], so Huawei's price lever is demonstrably active even before any share shift;
and the company is adding 32 production lines aimed at this same customer from a base of 111.89% utilization
[S277] — operating leverage that runs in reverse exactly as it did in 2021 (utilization 84.04%→51.61%,
volume -42.24% [S272]), except now from a levered balance sheet (net debt, receivables at 45% of revenue
[S546; S700]) instead of IPO cash. At 216x trailing earnings, even a 10-20pt share shift to a second source,
or one Huawei-imposed price-down cycle, removes both the E and the multiple simultaneously; the FY2024 loss
year shows how little margin cushion exists beneath the narrative.

## 4. Common-mode test

688629's tailwind is a single factor: Huawei AI-compute capex under a domestic-substitution policy regime —
the company's own stated growth driver is "AI服务器、数据中心等终端产品**国产化替代**" [S270]. Shocks on
that factor (large-scale re-admission of NVIDIA to China making Ascend build-out less urgent; a state
AI-capex pause/digestion phase; any US action that interrupts Huawei's own production cadence, as 2020-21
already demonstrated at this exact company [S272]) hit, in the same direction and season: **002261** (拓维,
Ascend hardware 21.7-50.4% of revenue), **301236** (软通, Huawei-coupled three ways), **600498** (长江计算
consolidation), **000034** (神州鲲泰), and second-order **688981** (Huawei-attributed fab demand) and
**002371** (fab-capex derivative) — i.e., ranks 1, 3, 4, 5, 7 of the current answer key are one trade. The
portfolio's only above-bar name is the single most concentrated expression (60.52% single-customer) of the
factor the rest of the top cohort shares; a Phase-4 book built on this row has no second factor. The only
genuine diversifier in the universe is 300308 (rank 2), whose driver is the global/NVIDIA chain (domestic
revenue ≤9.42% and falling [V_300308 per SCORING_NOTES]) — a policy reversal that wounds 688629 plausibly
*helps* it — with 002281/002916's overseas mixes as weaker analogues. Red-team position for G3/Phase 4: any
allocation that pairs 688629 with 002261/301236/600498/000034 should be treated as one position with
layered tickers, and the 3.30 total that admits 688629 to the portfolio is itself the common-mode bet.

## 5. Five falsifiable checks

| # | Observable event | Window | Bear if | Bull if |
|---|---|---|---|---|
| C1 | H1-2026 半年报: OCF sign + receivables | by 2026-08-31 (statutory) | H1 OCF ≤ 0 (cash burn persists through the "best" demand year) or receivables/revenue ≥ 50% | H1 OCF strongly positive AND receivables growth < revenue growth — Q1's +427.80M [S555] was durable collection, not a one-off prepayment |
| C2 | H1-2026 半年报: top-1 customer % | by 2026-08-31 | ≥65% (deeper dependence), or top-1 % falls WITH sharp revenue deceleration (demand shock, 2021 pattern) | revenue ≥ +40% YoY with top-1 ≤ 55% — diversification without demand loss |
| C3 | Any company-sourced 昇腾/超节点 naming, or 224G 量产 (mass-production) statement, in a filing/互动易/IR record — spans the media-reported Atlas 950 Q4-2026 launch window (snippet-grade calendar) | now → 2026-12-31 | word still absent through the H1 report AND the 950 launch quarter — company cannot or will not claim the status the price assumes; [S702]-grade rumor stays the only carrier | verbatim 昇腾/超节点 or 224G-量产 confirmation appears — closes the brand-word gap, upgrades W1 toward 5 and would force this red team to concede B3 |
| C4 | Second-source hard evidence: 意华股份(002897) or 航天电器(002025) filing/互动易 confirming MASS orders (not applicability) for Huawei AI-server/supernode backplane connectors, or any Huawei dual-source/in-house connector signal | now → 2027-06-30 | confirmed — dominance premium erodes on observable fact; W6=0 vindicated | instead, 华丰 announces a mass NON-Huawei AI order (ByteDance/Alibaba per [S277] target list) — real second leg |
| C5 | Growth cadence + funding: 2026 三季报 revenue YoY and 9M OCF; fate of the ≤CNY 1bn placement | 三季报 by 2026-10-31; placement H2-2026 | revenue YoY < +30% (vs +56.15% Q1 — hypergrowth pricing falsified), or 9M OCF negative, or placement shelved/downsized (capex then rides on more debt from a 280M cash base [S700]) | revenue YoY ≥ +50%, 9M OCF positive, placement completed near current price — external capital validates the multiple |

---

## New sources fetched this session (zh-language, logged in frags/rt_688629.json)

- **[S700]** 新浪财经 mirror of 界面新闻 "单季获上市以来最好业绩，华丰科技高增长能持续吗？", 2026-04-18,
  tier 3, fetched — receivables CNY 1,141M +104.09% = 45.13% of revenue; inventory CNY 529M +64.41%; cash
  CNY 280M -27.41% vs ~CNY 400M ST obligations; OCF two consecutive negative years (matches [S266] exactly).
  Same underlying article as ledgered [S278]; re-fetched for balance-sheet detail P1/P2 did not extract.
- **[S701]** 东方财富财富号 (self-media) on 意华股份, 2025-09-25, tier 4, fetched — 意华 official platform
  reply "我们的高速连接器，可应用于超节点算力场景！"; author commentary: Huawei ≈34% of 意华 revenue.
  Signal + falsification target only; no figure load-bearing.
- **[S702]** 腾讯新闻 rain self-media "BT财经", 2026-04-28, tier 4, fetched — locates the ">70% Ascend-chain
  share / 唯一国产量产224G supplier" narrative: attribution is "据报道" with zero named sources, and the
  mass-production claim contradicts the company's own 224G sample/cooperation-stage disclosure [S267]. Used
  solely to grade the dominance narrative's provenance; supports no figure.

## Bottom line for the orchestrator (written response required per rubric before G3)

Seven challenges: six cell disputes (W1 4→3, W2 5→3 [keystone; strict reading 0], W3 3→2, W4 1→0, W5 5→4,
W6 1→0; corrected total 2.10) plus one citation-discipline defect (W3's "receivables build" cited no file;
adopt [S700] or strike). Minimum bar for keeping 688629 above 3.0: defend W2=5 against the 600839
consistency test in writing, AND concede at most one of {W1, W3, W4, W5} while conceding nothing else. If
W2 falls to 3, no name clears 3.0 and the rubric's own construction rule makes cash-heavy "no strong answer"
the mission's model answer.
