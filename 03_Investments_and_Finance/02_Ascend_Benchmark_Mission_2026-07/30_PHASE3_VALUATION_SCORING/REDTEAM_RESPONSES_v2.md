Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_RESPONSES_v2 — accuracy-patch re-red-team adjudications (orchestrator, 2026-07-07)

Scope: written responses to REDTEAM_600839_v2, REDTEAM_002156_v2, REDTEAM_688519_v2,
REDTEAM_688347_v2 (this file, §R5.1–R5.4) and REDTEAM_688141_v2 (§R5.5, appended after its
run). Every score change below is reflected in SCORES_v2.csv; v1 artifacts are not modified.
Cross-cutting rulings R0.5–R0.8 extend v1's R0 series and are mirrored in SCORING_NOTES_v2 §2.

## R0.5 — W4 evidence-tier: chain-nexus refinement of R0.2 (codified)

R0.2 (v1, unchanged for every G3 name) keyed W4's 0/1 boundary to the P1 tier letter of the
Huawei/Ascend link. The patch reviews surfaced a case R0.2 never faced: names whose PRICE is
carried by a tier-1-evidenced growth story that is not the Ascend link (002916: own-AR
AI-server/data-center demand; 002156: AMD export engine). Ruling: **the tier that governs W4
is the tier of the CHAIN-RELEVANT growth narrative the price embeds.** (a) If the priced
narrative is the Huawei/Ascend thesis or its direct domestic demand pool (e.g., AI-server
board demand named in the company's own filing), its evidence tier applies — 002916's W4=1
stands (tier-1 chain-relevant narrative; brand-unattributed but inside the chain's demand
pool). (b) If the chain-relevant content of the priced story is tier-C/UNVERIFIED, W4 maps
to 0 even where a non-chain business is tier-1 strong — the non-chain strength is priced in
W3, never in W4 (an Ascend answer key may not award its valuation cell to an AMD thesis).
(c) R0.2's outcomes for all v1 names are unchanged by this refinement; where letter and
narrative diverge, this ruling controls. This answers REDTEAM_002156_v2's codification
challenge on the merits: the rule now exists on disk, and its correct application REVERSES
the FR_002156 upgrade (§R5.2).

## R0.6 — W2 bound conventions (restatement of record)

Consolidated from R0.1 + patch practice, for the reader: a filing-grade POINT or PROVEN
MINIMUM inside a band maps to that band (002261: 27.0% FY2025 segment point → band 3, minus
a documented-interpolation notch for the disclosed segment collapse; 301236: ~1.3% proven
minimum → 1). A bound that SPANS band boundaries with no point inside maps to NOT-ESTIMABLE
→ 0 (688519: 0–17.70%; 600839: 0–~13.7%; 300308's 0–9.42% ceiling sits entirely inside one
band → 1). No change to any v1 cell.

## R0.7 — Regulator-action axis in W3 (new)

A live exchange inquiry letter or 监管警示 that targets P&L-quality dimensions (profit/cash
divergence, receivables, inventory, related-party flows) is a W3 aggravator of the same
class as the R1.3 precedent stack. It cannot alone force anchor-1, but it breaks ties toward
the lower interpolation. Applied: 688519 (§R5.3). Not applied retroactively to v1 names (no
equivalent facts on file).

## R0.8 — Entity-scope discipline for W1 (new)

Where the Ascend-linked substance attaches to an affiliated but UNOWNED entity, W1 scores
the listco's own evidence. If the claimed mechanism connecting the listco to that substance
is verified absent (not merely unverified), the listco-specific link is treated as C-grade
residue regardless of the source tier that covers the affiliate. Applied: 688347 (§R5.4;
deal perimeter verified to exclude the Ascend-linked fab). Consistent with v1's 600839
华鲲振宇 debunk handling and rule A8.

---

## R5.1 — Response to REDTEAM_600839_v2 (row 1.65 → 1.35)

- **W1 1→2 — ACCEPT.** The critic's own fetches supersede the FR justification: 长虹佳华's
  official brand page (tier 2, company voice) names distributed Huawei lines including
  AI服务器/AI加速卡 [S1251], and the subsidiary's tier-1 trail [S1250;S1252] confirms the
  distribution business at filing grade. FR_002436's precedent (official generic-Huawei
  statement above the C floor → 2, documented interpolation) transfers exactly. Not 3: no
  昇腾/Atlas naming, undated marketing page, subsidiary voice. The answer key will also
  correct the stale "8016.HK" to 3991 [S1252].
- **W2 0 — CONFIRM; basis replaced as demanded.** The direction-A attack failed on the
  critic's own arithmetic: the segment ≈ CJH 1:1 (implied 0.9274 CNY/HKD), and CJH's own
  FY2025 split (consumer 42.94% / enterprise 36.75% / other 20.31% [S1250]) caps the
  enterprise sleeve at ~13.7% of group revenue — the R0.1-era ">30% band" premise is
  arithmetically dead, and any true Huawei share spans the 10% boundary → 0 per R0.6.
  SCORES_v2 W2 cell now cites [S1250] and marks the R0.1 rescore SUPERSEDED. The
  W2-resurrection path (filing-grade ≥26.8%-of-CJH Huawei share via the 募集说明书 supplier
  table) is recorded as the critic's falsifiable check #1.
- **W3 2 — CONFIRM** (critic itself declined the challenge; net cash + positive OCF offsets
  per R1.3 convention).
- **W4 3→1 — ACCEPT.** The NEUTRAL flag was denominator-fragile: 90.83% of FY2025 headline
  attributable NP is non-recurring (扣非 90.64M vs 988.89M headline, F §2.0), the two most
  recent prints show 扣非 −78%, and the vendors' own run-rate field prints 76.52x with core-
  basis ~333x — inside the band the mission itself flagged PFP elsewhere (177x/231x). The
  market cap embeds either indefinite non-recurring gains or a sharp core recovery; that is
  a priced expectation, not NEUTRAL. Tier per R0.2/R0.5: the debunked 华鲲振宇 story is
  unpriced (VAL's finding), the priced narrative is the generic-Huawei distribution recovery
  at tier A/B (own-voice) → 1, not 0 (000628's PFP-on-debunked-narrative → 0 does not
  transfer). The FY2025-headline-basis NEUTRAL derivation remains documented in VAL_600839
  (a v1 artifact, unmodified); this response supersedes its flag for v2 scoring purposes.
- **W5 1 — CONFIRM** (strengthened by CJH's own 1.49–2.63% sleeve margins [S1250]).
- **W6 4→3 — ACCEPT.** Symmetry: W2 scores the Huawei share as unknowable; W6 may not score
  the same unknown as ~nil. The anchor's "diversified customers" clause is unsupported
  (top-5 MISSING ×3 FYs); the sleeve is ≈22.6% of attributable NP ≈ 2.5x group core 扣非;
  the CJH privatization concentrates the exposure further; comp 000034 sits at 3. One
  material concentration/verticalization exposure = 3.
- **Net: 2,0,2,1,1,3 = 1.35.** The re-red-team's both-directions mandate worked as designed:
  the FR demotion survived its strongest filing-grade challenge and the row still came down.

## R5.2 — Response to REDTEAM_002156_v2 (row 1.80 → 1.20; exits the top tier)

- **W1 1, W2 0 — CONFIRM** (unchallenged).
- **W3 4→3 — ACCEPT.** The 5-anchor is conjunctive and the misses are large, not marginal:
  net debt −13,357M (≈11x FY25 attributable NP, +40% in two years), GM FELL in the boom year
  (14.84→14.59%), cumulative 3-year FCF −754M, growth debt-funded. "Mixed" (3) is the honest
  anchor; FR's prong-counting hid magnitude.
- **W4 1→0 — ACCEPT (the load-bearing challenge), per R0.5.** The critic is right on all
  three grounds: (a) R0.2 was the written standard of record and the narrative refinement was
  uncodified at the time of the FR upgrade — that gap is now closed by R0.5, and closed
  AGAINST the upgrade; (b) the AMD narrative has zero chain nexus — in an Ascend benchmark,
  W4=1-via-AMD converts the valuation cell into a reward for owning a good non-Ascend
  business (the exact scoring-the-wrong-chain artifact G3's R2.5 corrected); (c) the forward
  path the 71.55x prices (~42%/yr NP CAGR ×3y) has no tier-≤B carrier. PFP with tier-C
  chain-relevant content → 0.
- **W5 4→3 — ACCEPT.** R2.5 is the controlling precedent and was unapplied: demonstrated
  advanced-packaging content growth sits in the overseas/AMD chain; the Ascend-relevant
  premium claims are tier C; chiplet HPC is 研发进行中; HBM is ceded; 14.59% GM / 4.36% NM
  are service-layer economics. "Defensible but competitive" (3), with the premium anchor
  reserved for chain-relevant demonstrated content.
- **W6 2→1 — ACCEPT.** Both anchor-1 prongs are present: six-year structural single-customer
  concentration (52.29/50.35/59.38%; AMD-attributed ≥49% since 2019; ">80% of AMD's relevant
  products" bilateral lock) AND live displacement/verticalization-equivalent exposure (the
  premium 2.5D/3D step of the flagship AI line captured upstream at the foundry; cooperation
  agreement's last disclosed horizon 2026 [S1260]; Penang migration channel validated at 3nm;
  the $800M MI308 license event demonstrating the policy trigger at scale [S1258]). Not 0:
  the 2016 divestment points away from customer re-internalization proper, and 52.29% is not
  the 0-anchor's near-total block.
- **Net: 1,0,3,0,3,1 = 1.20.** The FR corrected one cell in isolation and the red team is
  right that three others were simultaneously over-scored relative to the G3 record. The
  top-8 entry that triggered this pass is unwound by its own adjudication — the process,
  not the orchestrator's preference, decides.

## R5.3 — Response to REDTEAM_688519_v2 (row 2.20 → 1.60)

- **W1 4→3 — ACCEPT.** The critic's grammar analysis is decisive: the tier-1-parsed
  sentence's delivery subject is the CUSTOMERS' chip series (昇腾 bundled with non-Huawei
  海光 in scene-setting prose); Nanya's own clauses are counterparty-unnamed design-in and
  grade-level delivery claims; the 华为 word is absent from the 13pp abstract; the NOUYA8U
  华为认证 leg is relay-B; the company's own customer table names zero Huawei entity. The
  FR upgrade repaired only 1 of V_688519's four stated reasons for tier B and then paid a
  filing-language premium to marketing grammar. R1.1 (no interpolating above the verifying
  file's own tier) + the ladder test (688629: direct 60.52% corroborated relationship at 3;
  prose-without-relationship may not outrank it) → B maps to 3.
- **W2 0 — CONFIRM**, with the critic's audit note adopted: the 17.70% ceiling's numerator
  (9.25亿) is itself only relay-verified; any future W2 upgrade must first tier-1-verify it.
- **W3 3→2 — ACCEPT, applying R0.7.** The R1.3 stack is met or exceeded (OCF negative in the
  two most recent reported periods; FCF negative 2 of 3 FYs; receivables 61% of revenue —
  worse than 688629's 45.13%; an in-window headline loss year) PLUS two regulator actions the
  FR never weighed: the SSE inquiry naming 利润/现金流背离、应收激增、存货暴涨、关联交易、
  海外毛利率异常 [S983] and the 2025-09-10 监管警示 [S989]. Rising GM is real but was equally
  real in the R1.3 precedent.
- **W4 1 — REBUT the conditional 0; ACCEPT the mandatory aggravator log.** Under R0.5 the
  chain-relevant narrative here does carry tier ≤B: the own-filing (tier-1-parsed) 昇腾-
  adjacent delivery language plus relay-B 华为认证 — unlike 002156's AMD story, this
  narrative IS the domestic-chain story. The 0 therefore does not trigger on tier. The
  aggravator is logged as demanded and carried to the answer key: **75.8% of FY2025 revenue
  growth was ordinary-grade CCL riding an industry price-hike wave the company itself joined
  (调价函, cost-push copper/resin/glass [S1267]); a 215.30x ttm / 330.76x static structure on
  a majority-commodity growth base is PFP squared.** W2's 0 already prices the bundle's
  unattributability; W4 keeps the flag with the aggravator on the record.
- **W5 3→2 — ACCEPT (documented interpolation).** Load-bearing legs are the company's own
  by-grade mix (82% of product revenue at anchor-1 economics; trough GM 4.16%; SSE-flagged
  8.11% overseas GM) and the on-file grade-ladder fact set (生益科技's M6–M10 + sole mainland
  Nvidia-M9; three concurrent high-grade capacity placements). The tier-4 channel note
  [S1266] is a probe only and carries no weight in this ruling; the mix arithmetic alone
  moves the cell. Supplier-side 55.34% concentration squeezes the same P&L from the left.
- **W6 3→2 — ACCEPT (documented interpolation).** Single-ecosystem concentration (all top-5
  are PCB fabs pressing the same domestic AI/server boards; 34.96%, max 14.17%) + the
  receivables amplifier (61% of revenue; top-5 debtors 51.93%) + AVL substitution at zero
  switching cost (Huawei qualifies laminate makers directly while invoices flow through
  fabs; the FY2023 impulse response −21.05% revenue / 4.16% GM is on file). More than "one
  material concentration"; not the 0/1 anchor's near-total block.
- **Citation defect — ACCEPT, fixed in SCORES_v2:** the W1 cell now cites S1167 (the parse
  artifact), and the false "华为认证 language tier-1-verified" claim is removed (that leg is
  relay-B per FR_688519's own finding).
- **Net: 3,0,2,1,2,2 = 1.60.**

## R5.4 — Response to REDTEAM_688347_v2 (row 1.85 → 0.85)

Verification gate C6(a) — RESOLVED AGAINST THE ROW. Orchestrator fetches this session
(ledgered S1350–S1351): 36氪's deal analysis (2026-06-03, tier 3, fetched [S1350]) states
the perimeter plainly — the 82.68亿 buys 华虹五厂/Fab 5 (38k wpm, 12-inch, 55/40nm低功耗 +
65/55nm射频) and "华虹六厂（Fab6）则不在此次收购范围", with Fab 6 described as the more
advanced 28/22nm line retained by the group for independent financing/strategic investors/
possible separate listing; this corroborates the 问询回复 relay [S1277] ("新增3.8万片/月的
65/55nm、40nm产能") and the red team's partial parse of the 草案摘要 [S1274]. A second fetch
(观察者网 心智观察所 2026-06-04) returned an empty render — failure documented, title-level
only, non-load-bearing [S1351]. Ruling: the Ascend-linked substance (reported 7nm/SiCarrier
work at Fab 6 [S908;S909]) attaches to an entity/fab OUTSIDE both the listco and the deal
perimeter; the "merger closes the gap" mechanism is verified absent. R0.8 applies.

- **C1 / W1 3→1 — ACCEPT (conditional triggered).** With the mechanism verified absent, the
  listco-specific Ascend link is C-grade residue: entity-ambiguous, future-tense wire
  reporting ("planning to shift… other sources said") plus a group-conflated advanced-
  production mention. Not 0: nothing is verified FALSE about the reported Huawei–Hua Hong
  (group) engagement itself; A12's verified-false → 0 rule does not trigger. Ladder check:
  600839 rescued a 2 via its own tier-2 company-voice distribution business; 688347 has no
  listco-voice Huawei anything → 1.
- **C2 / W3 2→1 — ACCEPT.** Both anchor-1 elements are literally present across the window
  (attributable NM 11.93→2.65→2.18 with GM down ~8–9pp on both bases; FCF negative all three
  years, cumulative ≈ −25.3bn) and the consolidated TOTAL result is a loss three periods
  running — attributable profit exists only via −1,183.75M of minority loss absorption, a
  fact absent from the prior cell basis. Positive OCF and residual net cash are real but are
  anchor-5 fragments against a disjunctive anchor-1 test met twice over.
- **C3 / W5 3→2 — ACCEPT (documented interpolation).** The up-cycle-peak revelation stands:
  at >99% utilization and guided +10–15% ASP, the asset base produces 11.8–16% USD GM with
  total-basis losses; capacity is being added into the same nodes by the deal itself (+38k
  wpm) and FAB9A (+83k), and the scarcity notch the layer premium rewards belongs to the
  7nm holder, not the specialty-mature base. Specialty differentiation keeps it off 1.
- **C4 / W6 3→2 — ACCEPT (documented interpolation).** Live arms beyond "one": materialized,
  company-named BIS tool-shipment action (April 2026) aimed at the expansion program the
  price requires; the related-party issuance stack (+10.98% share count at 43.34 vs 324.00
  market — a dated post-lock overhang — plus a ≤75.56亿 companion raise); the open CSRC
  registration gate; concentration rising 25.66→34.18%. The 业绩承诺 absence in both fetched
  deal relays is recorded as an unresolved disclosure gap (not asserted as fact) and carried
  to the changelog's open items.
- **C5 / W4 1→0 — ACCEPT (conditional triggered via R0.5 + R0.8).** The 1141.08x multiple
  prices the advanced-node/Ascend scarcity story; with the listco mechanism verified absent,
  the chain-relevant content of that priced narrative is C-grade residue → 0. The three
  aggravators are logged as demanded: mission-extreme multiple on the mission's only
  verified-0% current exposure; the deal's market cost to holders is 61.81bn ≈ 10.98% of
  mktcap (7.48x the consideration framing — see corrections below); the in-group regulated
  appraisal prices the same asset class at 11.0–16.2x earnings, ~70x below the acquirer's
  market multiple.
- **C6 — ACCEPT in full.** (a) Perimeter verified (above); V_688347's corporate-structure
  section carries an entity conflation (Fab 6 assigned to 华力微) — V_688347 is a patch
  artifact and receives an appended correction note rather than an edit, preserving the
  audit trail. (b) The "deal ≈1.5% of mktcap" framing in VAL_688347/FR_688347 is restated by
  appended correction notes in both files: consideration 82.68亿 ≈ 1.5% of mktcap, but the
  share consideration at market (190,768,392 × 324.00 = 61.81bn) ≈ 10.98% of the pre-deal
  cap, 7.48x larger. (c) The SCORES_v2 W2 cell drops the "merger pendency is W4 catalyst"
  clause (the catalyst premise failed verification); W2=0 itself is unchanged (and, per the
  critic's own §W2 note, survives consolidation arithmetic in any case).
- **Net: 1,0,1,0,2,2 = 0.85.** The patch's own addition is demolished by the patch's own
  adversarial step — the answer key will present this as the patch's clearest lesson in
  entity-scope discipline (the ticker carried the group's story; the listco owns neither the
  fab nor, post-deal, the mechanism).

---

## R5.5 — Response to REDTEAM_688141_v2 (row 1.70 → 1.25)

- **W1 3→2 — ACCEPT (documented interpolation; letter B unchanged).** The R2.1 map is
  exact: a substance-thin B (one outlet's section placement, no counterparty asserted, no
  Huawei-side artifact) capped at 2. Decisive new evidence: the tier-1-parsed HK-roadshow
  record [S1282] — chairman presenting to ~60 global funds pre-H-share-IPO, zero
  华为/昇腾/Atlas mentions, no customer named — where an Ascend story would pay maximum
  dividends if speakable; and the second named house's deep-dive on the identical product
  line frames it as MPS-substitution with no Ascend placement [S1284] — the single Ascend
  placement is not even sell-side consensus. Ladder consistency with R5.3 (prose vs
  relationship) and R2.1 preserved.
- **W2 0 — CONFIRM** (attacked both directions; "计算" bundles PC/server/storage, no band
  selectable; A8 holds). Audit note adopted: re-run W2 if an HK PHIP prints a customer or
  segment table.
- **W3 1 — CONFIRM; both demands adjudicated.** (a) Audit-opinion verification: attempted
  three ways this session (audit-committee report parsed via the dfcfw local-PDF fallback
  [S1352] — states 天健 retained and committee affirmation, but no opinion type; the S920
  AR text page does not carry the audit-report section; the 摘要 PDF class is
  password-protected) → opinion type UNVERIFIABLE this session, documented; no
  going-concern or 强调事项 language exists in ANY fetched artifact, financing access is
  demonstrably open (FY2025 financing CF +713.85M), so anchor-0 "distress signs" remains
  unevidenced → 1 stands. Listed as a PP4 spot-check candidate. (b) Aggravators logged for
  the answer key: 0.42x coverage of <12-month maturities (1,128.35M due vs 474.17M liquid)
  at ~324M/yr OCF burn; and a NEW tier-1 fact from [S1352]: the 2025-04-18 audit-committee
  agenda includes 关于未弥补亏损达到实收股本总额三分之一的议案 — the statutory
  one-third-of-paid-in-capital accumulated-loss trigger was already reached on the FY2024
  book, and FY2025 added a further −717.12M (扣非 −794.53M). The critic's W3/W4
  double-count observation is accepted as drafting guidance: the HK-IPO event appears in
  W3 as funding contingency and in W4 as dilution overhang — one event, two distinct risk
  surfaces, each logged once.
- **W4 1 — HOLD per R0.2/R0.5 + mandatory aggravator log (conditional 0 not triggered).**
  The letter stays B (the W1=2 is an interpolation, not a letter change — R2.4 precedent),
  and under R0.5 the chain-relevant narrative carrier is the same tier-B placement; thin,
  but not C. Aggravators logged verbatim: (a) 27.63x/25.37x sales with P/E n/a — the only
  PFP structure on the board with no earnings floor of any size; (b) HK-IPO dilution
  overhang, terms unquantified, application lapsed once, resubmission approaching its
  validity window with no hearing record as of 2026-07-07; (c) the W3/W4 one-event-two-
  surfaces note above; (d) Q1-2026 margin break plus two consecutive quarters of
  sequential loss-widening (Q4-2025 revenue −5.63% QoQ; 归母 −257.22M → −276.00M) — the
  price underwrites an inflection the two most recent prints move away from.
- **W5 3→2 — ACCEPT (documented interpolation).** Within-layer-position method (R1.5/R2.5):
  incumbency sits with MPS/Infineon/Renesas/AOS; 国信 places 杰华特 at 客户导入和批量销售
  初期 [S1284]; GM fell four consecutive reported periods to 25.32% against a >45%-GM
  recovering domestic cohort [S1283]; the layer's pricing is regulator-documented war
  damage with the current repair coupled to a tradeable policy shield. R&D intensity and
  real multiphase barriers keep it at 2, not 1.
- **W6 3→2 — ACCEPT (documented interpolation); fork ELECTED: Fork B discipline.** The row
  adopts the A8 reading everywhere: the anonymous #1 (~30% for three years) is NOT equated
  with Huawei in any cell — W1's 2 rests solely on the S924 placement, not on a
  #1-is-Huawei imagination, so the critic's both-halves inconsistency is cured by
  election, not by scoring the bull half twice. What remains: material single-customer
  concentration + the IPO-era related-party anonymization precedent [S926] as a governance
  aggravator + the policy/funding common-modes → 2. Conditional 1 does not trigger (no
  Huawei-linked reading is adopted anywhere in this row's narrative).
- **Record correction — ACCEPT.** [S1282] verifies FR flag (b) at tier 1 (the 2025-11-10 IR
  record is Huawei-silent in full text, not merely by inference); the answer key cites
  S1282; the pdf.dfcfw.com host is logged as a working fallback for QQ/cninfo-blocked
  公告 PDFs (it also delivered S1352 this session).
- **Net: 2,0,1,1,2,2 = 1.25.**

## Status and PG2 closure notes

- R5.1–R5.5 adjudicated; all cell changes applied in SCORES_v2.csv (post-RT2 rewrite).
- **Top-8 coverage ruling (documented judgment):** after the R5.x rescores, 301236 moves
  into the top 8 solely because names above it fell — its own row is unchanged (1.60,
  FR-confirmed) and it already carries full adversarial coverage from v1
  (REDTEAM_301236.md + written responses R4) re-verified by FR_301236 this patch. The
  re-red-team trigger's purpose (adversarial vetting of top-tier rows) is satisfied; a
  fresh pass would re-attack an unchanged, twice-vetted row with no new facts and is not
  run. Every current top-8 member now holds either a v1 red-team memo (688629, 300308,
  002261, 301236), a patch re-red-team memo answered above (none remaining in top 8), or
  an FR review with all-cells-earned plus no trigger under the brief (000034, 002916,
  688981, 002281 — of which 002916/002281 also carry patch cell changes adjudicated in
  their FR files).
- Every re-red-team challenge across R5.1–R5.5 (4+4+6+6+6 = 26 numbered challenges plus 3
  record/citation-defect demands) is answered above with ACCEPT or REBUT and a reason;
  concessions are reflected cell-by-cell in SCORES_v2.csv. Gate PG2 CLOSES with this file.
