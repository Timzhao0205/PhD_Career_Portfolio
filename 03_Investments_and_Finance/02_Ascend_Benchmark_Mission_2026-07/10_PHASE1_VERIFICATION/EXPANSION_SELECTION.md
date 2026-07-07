Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# EXPANSION_SELECTION — accuracy-patch PP1: +5 names (selection rationale)

Date: 2026-07-07. Selector: orchestrator (session model), per PATCH_BRIEF PP1.
Criteria (binding, from the brief): (1) lead strength — tier-B-or-better evidence
plausibly available from filings/named media; (2) layer diversity vs the existing
14-name universe. Candidate pool = **documented leads only** — no new discovery searching
was done for this selection; every candidate below cites where v1 or the prior corpus
recorded it. This file ranks nothing and implies nothing about any existing name's score.

## Layer coverage of the existing 14 (from 05_STATE/UNIVERSE.csv)

server distribution (000034); server integrator (000628, 002261, 600839); advanced
packaging OSAT (002156); optical modules (002281, 300308); fab equipment (002371);
PCB/substrate (002916); liquid cooling (301018); ISV/all-in-one (301236); server+optical
(600498); high-speed connectors (688629); foundry (688981).
**Absent layers with documented leads:** power (PSU/power ICs), packaging materials,
switching silicon, upstream CCL. **Thin:** PCB/substrate (one name, tier C).

## Candidate pool (all documented leads)

| Candidate | Layer | Documented lead | Pool tier |
|---|---|---|---|
| 华虹半导体 688347 | foundry | v1 DISCOVERY in V_688981 (S285: TrendForce 2026-02-25 names Hua Hong alongside SMIC in the Ascend-950-driven 7/5nm-class buildout); logged noted-not-added in A10 | **B** (already on file) |
| 意华股份 002897 | connectors | S204 西部证券 weekly bare-list; RB_02 [S009] | C (bare-list) |
| 航天电器 002025 | connectors | S204 西部证券 weekly bare-list only | C (bare-list) |
| 科大讯飞 002230 | AI applications | A10: rejected — chain role is Ascend compute BUYER, not supplier | n/a (fit fails) |
| 泰嘉股份 002843 | power (PSU, via 深圳雅达) | RB_02 power row [S009] | C |
| 杰华特 688141 | power (DrMOS/DC-DC ICs) | RB_02 power row [S009] | C |
| 英维克 002837 | liquid cooling | RB_02 [S008;S009]; A10: did NOT clear tier ≤B for Ascend during v1 wave-3 verification | <B (documented negative) |
| 兴森科技 002436 | PCB / IC substrate | RB_02 PCB/CCL/substrate row, tier B–C [S009;S010] | B–C |
| 南亚新材 688519 | CCL | RB_02 same row [S009;S010]; also named in the S009 Ascend-chain roll | B–C |
| 华海诚科 688535 | packaging materials (EMC) | RB_02: "Molding compound for Ascend" [S009] | C |
| 盛科通信 (STAR; ticker not recorded in RB_02) | switching silicon | RB_02 switching row [S008] | C |

## Selected 5

1. **华虹半导体 688347 — foundry.** The single strongest documented lead in the pool:
   the only candidate already substantiated at tier B this mission (V_688981 DISCOVERY,
   S285), and the brief's priority class (a). Adds a second foundry data point; per A20
   it shares the foundry cap-group with 688981, so the value is evidence depth on the
   chain's bottleneck layer, not layer count. Auditor hypotheses to test: does any
   filing/IR reply tie 华虹 capacity to Huawei/Ascend-linked demand; mature-node
   (power/driver IC) share vs advanced-logic claims; A-share (688347) vs H-share
   (1347.HK) disclosure differences.
2. **杰华特 688141 — power management ICs (absent layer).** RB_02 documents the
   DrMOS/DC-DC server-power lead. STAR-board listing means a prospectus + 问询函 trail
   with named customers/shareholders is likely retrievable — a realistic tier-A/B path.
   Auditor hypotheses: any Huawei-affiliated shareholder in the prospectus top-10 list;
   any 互动易/上证e互动 reply on 华为/昇腾/服务器电源; design-win disclosures for
   AI-server power stages.
3. **兴森科技 002436 — PCB / IC substrate (thin layer, tier-C incumbent).** RB_02
   carries it at B–C for ABF/FCBGA substrate — the package-substrate chokepoint that
   advanced-packaging of AI silicon depends on. The layer's current evidence base is
   weak (incumbent 002916 verified at tier C / NOT-ESTIMABLE in v1), so a second,
   possibly better-disclosed name raises the layer's answer-key quality either way.
   Auditor hypotheses: FCBGA substrate capacity/qualification disclosures (珠海 lines);
   any named domestic AI-chip or HiSilicon-linked substrate business in filings/IR.
4. **华海诚科 688535 — packaging materials, EMC (absent layer).** RB_02's lead is
   Ascend-specific on its face ("molding compound for Ascend"). Small STAR-board
   specialty-materials name; recent-IPO prospectus + 问询函 give a plausible tier-A/B
   documentation path (named OSAT customers; advanced-packaging EMC qualification).
   Auditor hypotheses: which OSATs it supplies (通富/长电/华天), whether any disclosure
   ties EMC grades to AI/advanced packaging, revenue scale of that grade.
5. **南亚新材 688519 — CCL, upstream laminate (absent sub-layer).** Named in both
   prior-corpus sources for the layer [S009;S010]. CCL for AI-server boards is the
   materials input one step above 002916/002436; historic Huawei-qualified-supplier
   status is a commonly repeated claim the auditor must confirm or kill from filings/IR.
   Per A20 it caps with the boards/substrate group. Auditor hypotheses: any named
   Huawei/server-customer disclosure; high-speed (M6/M7-grade) laminate revenue share;
   AI-server-linked volume statements with dates.

## Not selected (documented reasons; no ranking implied)

- **意华股份 002897 / 航天电器 002025** — lead is a bare-list mention in one 西部证券
  weekly (S204, confirmed bare by two independent reads in v1); the connector layer is
  already covered at tier A/B by 688629. Both A10 rejection reasons stand unchanged.
- **科大讯飞 002230** — buyer of Ascend compute, not a supply-chain member; fit fails
  (A10 reasoning stands).
- **英维克 002837** — v1 wave-3 already searched and found the Ascend link does not
  clear tier ≤B (A10); no new documented lead has appeared since. Re-selecting it would
  spend a slot re-running a documented negative.
- **泰嘉股份 002843** — legitimate power-layer lead (via 深圳雅达), but one power name
  covers the absent layer and 杰华特's STAR-board disclosure trail offers the stronger
  tier-A/B path; taking both would double one layer while packaging materials or CCL
  went uncovered.
- **盛科通信** — weakest documented lead in the pool (single tier-4-sourced row, no
  ticker recorded in the corpus) plus a structural reason for doubt: Huawei designs its
  own switching silicon, so a Huawei-chain supplier role is likelier to verify UNVERIFIED
  than B-or-better. With five slots, expected evidence strength loses to the picks above.

## Mechanics

Universe: 14 → 19 (within no cap — v1's ≤18 cap governed v1 Phase 1; the patch brief
fixes the addition count at exactly +5). S-ID blocks per A17: 688347 S900–S919, 688141
S920–S939, 002436 S940–S959, 688535 S960–S979, 688519 S980–S999 (PP2/PP3 blocks in
A17). Full v1 treatment: filing-auditor → fundamentals-analyst → valuation-analyst,
same schemas and gates as v1; transport per A18. No existing name's row, tier, or file
is modified by this selection.
