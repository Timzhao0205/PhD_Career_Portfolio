Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_RESPONSES — orchestrator adjudication of all red-team challenges (Gate G3)

Date: 2026-07-07. Every challenge in REDTEAM_{688629,300308,002261,301236,600498,002371}.md
is answered below: **ACCEPT** (cell rescored) or **REBUT** (cell held, reason given). The
post-rescore SCORES.csv supersedes the initial one; SCORING_NOTES.md carries a supersede
notice. Arithmetic: weights W1 .20, W2 .20, W3 .15, W4 .20, W5 .15, W6 .10.

## R0 — Cross-cutting rulings (apply to all 14 names)

**R0.1 The W2 standard (answers the "one standard; pick it" demand in REDTEAM_688629 §W2,
REDTEAM_300308 §W2, REDTEAM_600498 §W2).** The rubric's anchor text says "Huawei-linked
share", not "Ascend-specific share" — the literal text governs, consistently:
- A filing-grade POINT estimate (or range within one band) of Huawei-linked revenue scores
  its band (5 if >30% AND growing; 3 if 10–30%; 1 if <10%).
- A verified-attributed component sum establishes a PROVEN MINIMUM and scores the band of
  that minimum (a floor made of named, quantified Huawei-linked wins is a fact, not a guess).
- Bounds that span multiple bands (unattributed floors, wide bundled ranges) select no band
  → NOT-ESTIMABLE → 0. Ceilings that confine the entire feasible set below 10% score 1
  ("<10%" is then literally known). Verified-zero scores 0 (zero materiality).
- CONSEQUENCE ACCEPTED: this rule was NOT uniformly applied initially. Corrections below:
  688629 W2=5 stands (rule-compliant); 600498 W2 1→0 (invalid floor); 301236 W2 3→1
  (proven minimum ~1.3%); 300308 W2=1 stands (ceiling confines to <10%); and — the
  symmetric correction the 688629 critic's own consistency test forces — **600839 W2 0→3**
  (verified ~37.35%-of-revenue Huawei-ICT distribution segment [V_600839, S257;S258;S261]
  is a filing-grade Huawei-linked point in the >30% band; growth unestablished, so 3 not 5).
  600839 was not red-teamed; this is an orchestrator consistency rescore forced by the
  adjudicated standard, documented here per the rubric's written-response rule.
**R0.2 The W4 standard (answers REDTEAM_688629 §W4, REDTEAM_300308 §W4, REDTEAM_600498
§W4).** W4's 0-vs-1 boundary keys on the P1 evidence TIER LETTER of the Huawei/Ascend link
(A/B → 1 when PRICED-FOR-PERFECTION; C/UNVERIFIED → 0). The critics are right that for
several names the PRICED NARRATIVE is more aggressive than the verified link; that gap is
acknowledged as the mission's central finding, and it is priced through W1/W2/W6 — not
double-priced in W4. Ruling applied uniformly; all W4 challenges on this ground are
REBUTTED (688629 W4=1, 300308 W4=1, 600498 W4=1, 002371 W4=1 all stand).
**R0.3 The W6 0-anchor (answers REDTEAM_688629 §W6 and REDTEAM_300308 §W6).** ACCEPT the
critics' reading: the parenthetical "(cf. in-house HBM)" defines the internalization
precedent as Huawei's DEMONSTRATED APPETITE, not a layer-specific prior event — requiring
layer-specific precedent would make the anchor unreachable ex ante. Applied below.
**R0.4 Citation-discipline defects.** All conceded and corrected in the final
SCORING_NOTES rescore section: (a) 688629 W3 "receivables build" — [S700] adopted as the
supporting source; (b) 002371 "quasi-oligopoly" and "contract liabilities signal backlog"
— struck (the latter was factually wrong: contract liabilities declined QoQ [S176]);
(c) 600498 "tier-1 segment floor" — mislabel struck (segment figures are tier-3-carried).
**R0.5 Non-re-red-teamed risers.** The brief assigns the red team to the INITIAL top 6.
Post-rescore, 600839 (risen via R0.1), 000034, and 688981 sit in the top half without
having been red-teamed. This residual asymmetry is disclosed here and in the answer key's
uncertainty section rather than papered over.

## R1 — 688629 华丰科技 (REDTEAM_688629: 7 challenges)

1. **W1 4→3 — ACCEPT.** V_688629's own tier for the claim-as-worded (Ascend-specific) is
   B; the rubric maps B→3, and interpolating above the verifying file's own tier was
   inconsistent with how 002261's verbatim-昇腾 filing earned its 5. W1=3.
2. **W2 5→3/0 — REBUT.** Under R0.1 the 60.52% top-customer figure is a filing-anchored
   point of Huawei-LINKED revenue (identity corroborated three independent ways
   [V_688629]), >30% and growing in absolute terms (+131.5% revenue on the same customer
   base [F_688629]). The rubric's own W2 note ("Concentration downside is priced in W6,
   not here") sanctions high-W2/low-W6 coexistence. The 600839 consistency demand is
   answered by rescoring 600839 UP (R0.1), not 688629 down. W2=5 stands.
3. **W3 3→2 — ACCEPT.** Two consecutive negative-OCF years + receivables +104.09% to
   45.13% of revenue [S700] + FY2024 core loss inside the window: the anchor-1 "persistent
   cash burn" element is genuinely present alongside rising margins → interpolation 2.
   [S700] adopted as the cell's source (R0.4a). W3=2.
4. **W4 1→0 — REBUT** per R0.2: link tier is B (Ascend-specific)/A (generic), not C. The
   critic's asymmetry observation (priced story diverges furthest from verified fact on
   this name) is recorded as an answer-key uncertainty. W4=1 stands.
5. **W5 5→4 — ACCEPT.** The 002281 within-layer-position precedent applies: connector-line
   GM 17.19% and falling, 组件-line attribution unconfirmed, 56G+ IP co-owned by the
   customer with a non-compete [S273]. W5=4.
6. **W6 1→0 — ACCEPT** per R0.3: highest single-customer concentration in the universe
   (60.52%, rising), supplier-side 61.41%, customer-as-shareholder (Hubble), customer
   co-owns the key IP, named second sources auditioning [S204;S701], demonstrated 2021
   demand whipsaw [S272]. This is the anchor's central case. W6=0.
7. **Citation defect — ACCEPT** (R0.4a).
**New row: 3,5,2,1,4,0 → total 2.70.** The critic's headline stands: NO name clears 3.0,
and Phase 4's rubric-mandated construction is the cash-heavy "no strong answer".

## R2 — 300308 中际旭创 (REDTEAM_300308: 6 challenges)

1. **W1 3→1 — PARTIAL ACCEPT at 2.** The tier letter is B and stands in V_300308, but the
   critic is right that the substance is one bare stock-code clause the verifier himself
   impeached; the documented-interpolation convention caps a substance-thin B at 2 (the
   688981 comparison — named dies, multiple outlets — shows what a full 3 looks like). W1=2.
2. **W2 1→0 — REBUT** under R0.1: the 9.42% domestic ceiling (falling) confines the entire
   feasible Ascend-linked set below 10%, so band 1's text is literally satisfied; "possibly
   zero" is not "verified zero" (000628's case). W2=1 stands.
3. **W3 5→4 — ACCEPT.** New working-capital evidence [S709]: inventory +79.8% YoY to 28.0%
   of assets (DIO ~131→~162 days), still building +23.6% QoQ into the CPO transition, plus
   falling R&D intensity — a real quality deduction the P2 grid was structurally blind to.
   The critic's own honest negatives (receivables slower than revenue; OCF/NP 1.01x) keep
   this at 4, not 3. W3=4.
4. **W4 conditional 0 — REBUT** per R0.2: tier letter remains B; conditionality not
   triggered by the W1=2 interpolation. W4=1 stands.
5. **W5 5→4 — ACCEPT.** RB_02 read #2's content-per-system argument is Ascend-supernode-
   specific; Innolight's demonstrated content growth is in the overseas chain, its domestic
   mix skews to legacy speeds [S209;S210], and the layer's largest customer is co-packaging
   the layer away (CPO in production [S715]). Within-layer-position discounting per the
   002281 precedent. W5=4.
6. **W6 1→0 — ACCEPT** per R0.3: 75.98% one-decision customer block under a LIVE 1260H
   listing [S213;S710], with in-layer internalization documented on BOTH demand pools
   (Huawei 星联/HiSilicon optics [S711;S708]; Nvidia CPO + funded second sources
   [S715;S712]). W6=0.
Process defects (F_300308 working-capital blind spot; global-note-2 review): ACCEPTED —
the blind spot is recorded in the rescore notes; global note 2 is superseded by R0.1.
**New row: 2,1,4,1,4,0 → total 2.00.** The critic's headline is adopted into the answer
key: the initial rank-2 was substantially an artifact of scoring the overseas business
inside an Ascend rubric; what survives is a fundamentals-strong name whose Ascend sleeve
is a rounding error and which functions as the universe's anti-correlated hedge.

## R3 — 002261 拓维信息 (REDTEAM_002261: C1–C6)

1. **C1 W1 5→4 — ACCEPT.** The link's existence at tier A is untouched, but evidence
   STRENGTH is impaired by a regulator-stamped false-records finding covering the same
   periodic reports (chairman among the warned; abstaining director declined to vouch for
   the two documents the score rests on) [S153;S718]. W1=4.
2. **C2 W2 3→1 — PARTIAL ACCEPT at 2.** New FY2025 point 27.0% [S716] sits in the 10–30
   band (→3), but the anchor set prices trajectory ("or flat" in the 1-anchor), and a
   -58.7% collapse of the thesis segment in the chain's boom year is materially worse than
   flat; interpolation → 2. (Not 1: the point estimate is in-band and arithmetically
   checked against the tier-1 revenue total.) W2=2.
3. **C3 W3 2→1 — ACCEPT.** Core (扣非) losses in two consecutive years with the headline
   kept positive by a receivables-impairment reversal [S145;S146], and Q1-2026 OCF
   reversal — anchor-1's burn element is met at the core-earnings level. W3=1.
4. **C4 W6 1→0 — ACCEPT.** Dual-sided concentration (suppliers 81.01% with Huawei entities
   61.29–73.5%; customers 72.75%) + last-of-seven tender position [S717] + live regulator
   action + the 超聚变 re-tiering precedent [S721]. W6=0.
5. **C5 W4 aggravators — ACCEPTED AND LOGGED** (W4=1 stands per R0.2; the 606x-on-core-loss
   structure is recorded in the rescore notes and the answer key).
6. **C6 tiebreak re-run — ACCEPT**: resolved mechanically in the final ranking.
**New row: 4,2,1,1,1,0 → total 1.70.**

## R4 — 301236 软通动力 (REDTEAM_301236: C1–C6)

1. **C1 W1 5→4 — ACCEPT.** Relay-only evidence (zero directly-parsed tier-1 documents)
   cannot outscore 688629's directly-fetched-but-brand-word-absent record; consistency
   caps it at 4. W1=4.
2. **C2 W2 3→1 — ACCEPT.** The 19% "floor" is a pre-acquisition-mix extrapolation (V's own
   text: bounding exercise), the 45.05% ceiling bundles non-Huawei ODM; under R0.1 the
   only band-selecting fact is the PROVEN minimum of named Huawei-silicon wins ≈1.3% of
   revenue [S729;S300] → band "<10%" → 1. W2=1.
3. **C3 W3 aggravators — ACCEPTED AND LOGGED** (W3=1 already at the anchor floor above
   distress; Q1-2026 OCF −34.42亿, first inventory writedowns, goodwill 3.85x the ttm
   residual [S724;S726;S727] are recorded).
4. **C4 W4 aggravators — ACCEPTED AND LOGGED** (W4=1 stands per R0.2; bull-consensus
   forward P/E ≈125x recorded [S731]).
5. **C5 W5 2→1 — ACCEPT.** Both legs sit in anchor-1 economics with compressing margins
   (services GM 21.97→16.5%; hardware 4.82% and falling; R&D down three years) — the ISV
   overlay is not a defensible-layer franchise on current evidence. W5=1.
6. **C6 W6 hold at 1 with aggravators — ACCEPTED AS PROPOSED** (quasi-single-ecosystem
   dependence + placement-flow facts logged; not 0 because customer concentration 25.42%
   is far from single-customer and no in-layer internalization fact was produced). W6=1.
**New row: 4,1,1,1,1,1 → total 1.60.**

## R5 — 600498 烽火通信 (REDTEAM_600498: 8 challenges)

1. **W1 5→4 — ACCEPT.** Mirrors-only evidence both halves; the 70.71218% stake is a
   拟-stage 2023 figure with completion unconfirmed at tier ≤B (the chairman's 2026
   statement confirms control, not the number); filings themselves silent. The 301236
   parallel is affirmed: relay/mirror-grade A-substance scores 4. Stake-currency caveat
   adopted into the rescore notes. W1=4.
2. **W2 1→0 — ACCEPT.** The 5.70% segment "floor" fails attribution (长江计算 产值 ¥75亿
   [S737] cannot fit inside a ¥11.44亿 segment — containment arithmetically impossible),
   and an unattributed floor selects no band under R0.1. The "tier-1 floor" mislabel is
   struck (R0.4c). W2=0.
3. **W3 2→1 — ACCEPT.** Anchor-1's margin prong is literally met (NM 2.46→1.75%, Q1-2026
   0.85%), with receivables ≈59% of revenue, an ¥804M inventory write-down as the FY2025
   key audit matter, and net debt widening three straight years; OCF alone cannot hold the
   cell at 2. W3=1.
4. **W4 1→0 — REBUT** per R0.2 (link tier A; PFP → 1). The critic's point that the PRICED
   narrative (AI ramp size) has no tier ≤B carrier is recorded as an aggravator. W4=1.
5. **W5 2→1 — ACCEPT.** The +1 credited a shrinking carrier-optics franchise that is not
   the chain layer under test (the group's chain-relevant optics sit in sibling 002281);
   长江计算's own economics print as allocation-taker/possible cost center (negative NCI
   [F_600498], 产值-KPI sponsorship [S737]). W5=1.
6. **W6 3→1 — ACCEPT.** Both anchor-1 conditions present (structural carrier concentration;
   verticalization exposure to Huawei's own machines and 战略级-certified rivals
   [S734;S735]); "state-parent stability" was an extra-rubric offset and is withdrawn.
   W6=1.
7-8. **Citation defects — ACCEPT** (R0.4c; the NCI-attribution caveat is carried verbatim
   into the rescore notes).
**New row: 4,0,1,1,1,1 → total 1.40.**

## R6 — 002371 北方华创 (REDTEAM_002371: 7 challenges)

1. **W1 3→2 — ACCEPT.** The rubric dimension measures the Huawei/Ascend LINK; V's tier B
   attaches to the capex-flow claim, and the link the score needs is a three-hop chain
   whose middle hop is company-non-confirmed [S178 Q24]. One-hop tier-B (688981) and
   three-hop derivative cannot both score 3. Documented interpolation → 2 (component hops
   are B-or-better; the company's own IR names the AI算力芯片 demand category [S177]).
2. **W2 0 hold — AGREED** (no challenge).
3. **W3 3→2 — ACCEPT.** Deteriorating margins are literally present (GM −2.75pp, NM
   −4.81pp, ex-NR profit −4.22%), FCF negative two years, net cash −62% with debt +152%,
   and ~33% of attributable profit rests on capitalized R&D [F_002371;S176]; the struck
   "backlog" phrase (R0.4b) removes the cell's main positive. W3=2.
4. **W4 1 hold — AGREED** per R0.2 (tier B claim; conditionality not triggered at W1=2).
5. **W5 4→3 — ACCEPT.** "Quasi-oligopoly" struck (R0.4b); FY2025 peer prints show
   competitive squeeze (拓荆 +34.67%, 中微 +30.69%, 盛美 +21.05% profit growth vs NAURA
   −1.77% [S741;S742;S743]), and fab tools sit outside the rubric's named component
   layers. Defensible-but-competitive → 3.
6. **W6 3→2 — ACCEPT.** The mission-flagged Entity-List open item is closed against the
   company: NAURA + 10 subsidiaries listed 2024-12-02 [S740], with the Affiliates Rule
   extension [S746]; substitution-by-competitor is the live analog channel. W6=2.
7. **Reverse-direction W1 check — ANSWERED** (the critic's own zh-search found no
   filing-grade upgrade path; no upward rescore available).
**New row: 2,0,2,1,3,2 → total 1.55.**

## Final post-rescore board (supersedes the initial SCORES.csv table)

| rank | ticker | W1 | W2 | W3 | W4 | W5 | W6 | total |
|---|---|---|---|---|---|---|---|---|
| 1 | 688629 | 3 | 5 | 2 | 1 | 4 | 0 | 2.70 |
| 2 | 600839 | 1 | 3 | 3 | 3 | 1 | 4 | 2.40 |
| 3 | 000034 | 5 | 1 | 1 | 1 | 1 | 3 | 2.00 |
| 4 | 300308 | 2 | 1 | 4 | 1 | 4 | 0 | 2.00 |
| 5 | 688981 | 3 | 0 | 2 | 1 | 4 | 2 | 1.90 |
| 6 | 002281 | 1 | 0 | 4 | 0 | 4 | 4 | 1.80 |
| 7 | 002916 | 1 | 0 | 4 | 0 | 4 | 4 | 1.80 |
| 8 | 002261 | 4 | 2 | 1 | 1 | 1 | 0 | 1.70 |
| 9 | 301236 | 4 | 1 | 1 | 1 | 1 | 1 | 1.60 |
| 10 | 002156 | 1 | 0 | 4 | 0 | 4 | 2 | 1.60 |
| 11 | 002371 | 2 | 0 | 2 | 1 | 3 | 2 | 1.55 |
| 12 | 301018 | 1 | 0 | 3 | 0 | 4 | 3 | 1.55 |
| 13 | 600498 | 4 | 0 | 1 | 1 | 1 | 1 | 1.40 |
| 14 | 000628 | 0 | 0 | 2 | 0 | 1 | 3 | 0.75 |

Tiebreaks (rubric W1→W4, then A12 extension W2→W3→ticker): 000034 over 300308 on W1 5>2;
002281/002916 identical vectors — ticker order, midrank 6.5 for Spearman; 301236 over
002156 on W1 4>1; 002371 over 301018 on W1 2>1. **Zero names clear the 3.0 portfolio bar**
→ per SCORING_RUBRIC's construction rule, the Phase-4 benchmark is cash-heavy by design;
"no strong answer" is the model answer of record. Gate G3: all 40 challenges answered
above; SCORES.csv rewritten post-rescore; PASS.
