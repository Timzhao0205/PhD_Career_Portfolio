# PORTFOLIO — B40_portfolio (FULL)

Stage `B40_portfolio` | Mode `FULL` | Attempt 1 | Worker `pap06-fable-xhigh`
(requested Fable 5 / xhigh) | 2026-07-28

The combined portfolio decision: EXACTLY 24 ranked directions from the
41-idea A30 universe, with the 41→24 cut itself decided and documented.
RANKING.csv row order is the ranking; DECISION.json holds the audit-grade
numbers, buckets, dependencies, sensitivity cases, and all 15 rejections.

## 1. Scope and inputs

Inputs: the accepted pilot (method, weights, disposition vocabulary, six
scored rows — carried; refinements in §3), B20 ALIGNMENT.csv (all 39 concept
rows over the 41-ID universe), B25 POWER_MAP.csv + POWER.md (31 power rows,
wedges W1/W2, non-wedge rule), B30 BRIDGES.json + PREP_PLAN.md (bridge
ladder BR-A..BR-I, gates, calendar), B15 LIT_REVIEW.md + GAPS.md (evidence
boundaries, EV/P/G/M/BT IDs), A30 COMPARE.json + VERDICT.md (membership, SEM
ledger, four verified disagreements, rerun priorities, provenance limits),
B10 OPT2.md (founder constraints, critical path, kill criteria). Three live
web actions this run, all decision-critical and logged in SOURCES.csv: the
ABB SSCB fetch failed a third time (B40-01, disclosed); a SAES US-capacity
search found no kill-trigger event at discovery level (B40-02); an OCP
conformance search corroborated methodology white papers but no conformance
program with reference hardware (B40-03).

## 2. The 41→24 cut (a decision, not an inheritance)

The A30 union is 41 IDs; SEM-01 (E-01→C-01) and SEM-02 (B-01→C-04) reduce it
to 39 distinct concepts. 24 are ranked; 15 are rejected with concrete
reasons in DECISION.json; 24 + 15 = 39 = 41 − 2. The selection rule
(DECISION.json `selection_rule_41_to_24`): ≥2-final concept membership
(20 ideas), OR B20 mechanism MEDIUM+ (adds F-06), OR an A30-verified
exemplar carried from the pilot (adds C-07), OR positive signals from ≥2 of
three processes short of final membership (adds D-19, A-02 — ranked and
closed rather than rejected unexamined). No prior final-24 was copied: the
result overlaps NEW24 at 20/24, BLIND24 at 19/24 exact (20 semantic), OLD24
at 16/24 (§6). All 11 exact triple-intersection ideas plus the SEM-01
concept are ranked — the cut discards no idea that any two processes agreed
belongs in a final list, except where A30-verified facts or documented
duplicate ledgers say otherwise (none do: every ≥2-final concept is in).

## 3. Method (carried; refinements disclosed)

Exactly the pilot's method: eleven criteria scored 0–4 coarse ordinal with
per-criterion half-width bands (0.5 well-evidenced / 1.0 record-level or
proposed-only / 1.5 pool-record-only), fixed declared weights (commercial
0.60 / founder 0.30 / downside 0.10; PhD leverage 0.12 structurally cannot
override commercial evidence), conservative linear-combined aggregate
uncertainty, dispositions keep/bridge/watch/stop with bridge always citing
named BR-x gates. The six pilot rows are carried with scores, uncertainties,
and criterion vectors UNCHANGED (D-02 3.00, D-01 2.78, C-05 2.55, C-01 1.57,
C-07 1.07, D-10 0.65); their cells were refreshed only to point at this
run's source IDs and gate names. Refinements, disclosed: (a) two base-score
ties (C-05/D-09, C-01/C-04) required stated tie-break judgments — the pilot
sample had none; (b) the 1.5 band went unused because every pool-record-only
concept was rejected at the cut; (c) no idea-specific live recheck was
repeated where the pilot's opened primary suffices (reuse noted per row in
SOURCES.csv). Weights, scale, definitions, and vocabulary are untouched.

## 4. The ranking

| # | Idea | Score | Disp | One-line basis |
|---|------|-------|------|----------------|
| 1 | D-02 tape QC metrology | 3.0 ±0.8 | bridge | only STRONG; venture proof = thesis credential; C04-gated |
| 2 | D-01 quench detection | 2.8 ±0.8 | bridge | triple winner; $0 honesty gate starts its lane |
| 3 | C-05 cooling conformance | 2.6 ±0.9 | watch | A30-verified demand; methodology-not-domain |
| 4 | D-09 beam-current metrology | 2.6 ±1.0 | bridge | strongest sleeper mechanism; small unverified market |
| 5 | G-03 DC acceptance dossiers | 2.4 ±1.0 | bridge | both baselines selected; BR-B makes its product |
| 6 | F-06 precision DC sensing | 2.3 ±0.9 | bridge | discipline-nearest W1; weak commercial record disclosed |
| 7 | A-10 IEDF metrology | 2.2 ±0.9 | watch | demonstrated-asset mechanism; no founder gate exists |
| 8 | A-14 300C instrumentation | 1.9 ±0.8 | watch | strong consensus; $850k capital misfit |
| 9 | E-04 cryo readout loader | 1.8 ±0.8 | watch | nearest-readout venture; deemed-export defers it |
| 10 | F-02 magnet BoP skids | 1.7 ±0.8 | watch | verified buyer overlap; W2 observation post |
| 11 | F-01 RF match engines | 1.7 ±0.7 | watch | OLD-4 class; sliver is not the socket |
| 12 | A-05 NEG coating | 1.6 ±0.8 | watch | unverified 82%-kill reversal; trigger = verification |
| 13 | C-01 800VDC protection | 1.6 ±0.7 | watch | strongest consensus; consensus ≠ fit; BR-G sliver |
| 14 | C-04 two-phase cooling | 1.6 ±0.7 | stop | triple-final but zero founder lane in any record |
| 15 | C-22 electrolyzer benches | 1.6 ±0.7 | watch | OLD-2 venture quality; loses the W1 retest |
| 16 | E-14 MTDC relay + HIL | 1.5 ±0.7 | watch | 7/7/5 consensus; MTDC demand its own kill |
| 17 | C-13 GaN pump drivers | 1.4 ±0.7 | watch | vocabulary trap; $72k socket gate unpassed |
| 18 | C-08 PCHE recuperators | 1.4 ±0.7 | stop | no mechanism, no sliver found, capital misfit |
| 19 | C-09 pulsed-power platform | 1.4 ±0.6 | watch | verified non-EtO mid-pack; acceptance-metrology trigger |
| 20 | F-23 electrolyzer controllers | 1.3 ±0.7 | stop | both baselines' bottom tail; C-22 monitors the family |
| 21 | D-19 flywheel buffers | 1.2 ±0.7 | stop | unverified revival; no sliver worth naming |
| 22 | A-02 MVDC breaker | 1.1 ±0.7 | stop | shipping incumbents; $1.5M misfit; P5 KILL 82% |
| 23 | C-07 AFE rectification | 1.1 ±0.6 | stop | A30-verified kill (statute + incumbent) |
| 24 | D-10 beam combining | 0.7 ±0.7 | stop | only ADVERSE; verified proprietary internalization |

Tier structure (more robust than within-tier order): **1–2** clean bridge
top; **3–7** the wedge band (order weight-fragile, membership stable in all
six sensitivity variants); **8–13** monitored consensus/context band;
**14–20** weak-mechanism tail (mixed watch/stop by trigger logic);
**21–24** closed. No idea earns keep — confirmed at full scale: every
non-WEAK mechanism runs through proposed-only capabilities gated by C04 and
FT-02 (B30), so the top is bridge-shaped by construction.

## 5. Reasoning highlights

**Why the top is what it is.** D-02 is the unique case where the venture's
decisive risk IS the PhD's own planned credential (WP-C traceable
calibration), with rank-1 support in both baselines — and it still cannot be
keep while C04 is open. D-01 is the triple-intersection idea whose honest
founder lane (estimator-honesty false-trigger statistics) begins with a $0
desk gate that the corpus itself says gates every dollar after it. The 3–7
band is the two-wedge band: C-05 (W1 generalization proof, verified demand,
watch for lack of a domain gate), D-09 (W1 sleeper with the best
mechanism-per-dollar after D-02, capped by its small record-vintage market),
G-03 (nearest-term W1 play whose product artifact BR-B literally produces),
F-06 (discipline-nearest W1 embodiment ranked ABOVE its weak commercial
record on founder-axis grounds — the mirror image of C-01's demotion, and
disclosed as such), and A-10 (the one MEDIUM standing on demonstrated rather
than proposed assets).

**Dispositions are not rank-monotone, deliberately.** C-04 (rank 14) is a
stop above several watches because no record read contains any founder lane
or trigger for it; C-09 (rank 19) is a watch below stops because A30
verified its non-EtO demand legs and B20 named a concrete thin-link trigger.
Rank records integrated evidence quality; disposition records the founder
decision; the two must not be conflated (the pilot's C-01 lesson applied
symmetrically).

**Power ideas, neither forced up nor down.** The strongest-consensus power
products (C-01, E-14) sit at 13 and 16 because founder evidence, not theme,
is the integrating axis; the power measurement/qualification plays (D-09,
G-03, F-06) sit at 4–6 on the same rules; the B25 non-wedge rule (no
founder-led converter/breaker/relay/PSU/PPU/PMAD) is enforced everywhere,
and the surviving founder objects inside the power families are exactly the
slivers two corpora independently converged on (protection intelligence →
BR-G; measurement chain → BR-B/BR-E).

## 6. Comparison vs OLD24, NEW24, BLIND24

Counts (concept level, SEM ledger applied; A30 membership lists are the
reference):

| Pairing | Exact overlap | Semantic | This-24 only | Other only |
|---|---|---|---|---|
| vs NEW24 | 20/24 | 20/24 | F-06, F-02, A-02, C-07 | A-22, F-16, F-19, D-16 |
| vs BLIND24 | 19/24 | 20/24 (E-01↔C-01) | G-03, F-06, C-01*, F-23, D-19 | E-10, C-14, C-15, C-12, E-01* |
| vs OLD24 | 16/24 | 16/24 | C-05, D-09, A-05, C-09, D-19, A-02, C-07, D-10 | S01, CN-01, B-01†, CN-03, F-12, G-01, D-12, F-03 |

(*C-01/E-01 are the same concept — the exact-ID asymmetry is SEM-01;
†B-01 is inside C-04 per SEM-02 and adds no semantic overlap per A30's
counting rule.)

Top-10 overlaps: 5/10 vs BLIND10; 3/10 vs OLD10; 5/10 vs NEW10 (either
variant). For calibration: the three prior runs agreed with each other at
4–7/10, so this portfolio sits inside the existing band of top-10
disagreement while agreeing with the strongest pairing (BLIND↔NEW, 16/24)
at 19–20/24 on membership.

**Named changes and why:**

- **In, against some or all prior runs:** G-03 at 5 (OLD 20/NEW 15 — the
  only idea whose product BR-B's dossier phase directly produces); F-06 at 6
  (OLD 23/NEW cut — founder-axis bet on the W1 wedge, weak commercial record
  explicitly carried, mechanical demote path scheduled); D-09 at 4 (BLIND
  23/OLD kill/NEW 17 — B20's sleeper elevation, capped by market honesty).
- **Demoted against consensus:** C-01 to 13 (top-5 in all three runs;
  consensus and founder fit are independent axes — B10's ledger has no
  power/certification capability; the BR-G-testable sliver is what survives);
  E-14 to 16 and C-22 to 15 (same independence-of-axes adjudication); C-09
  to 19 (BLIND 4 leaned on the EtO leg EPA's own proposal reversed —
  A30-verified); D-10 to 24/stop (NEW 4 overreached the opened primaries —
  awardee holds the technology proprietary; ADVERSE stands).
- **Excluded against one run each:** the four NEW-only revivals (A-22,
  F-16, F-19, D-16 — unverified reversals, one at 90% prior kill
  probability, zero mechanism); the three OLD-only supplementals (S01,
  CN-01, CN-03 — CONTRADICTED decision-layer provenance, A30 item 8
  requires independent regeneration first); the BLIND-only out-of-longlist
  picks (E-10, C-14, C-15 — documented duplicates of both-baseline-killed
  canonicals or pre-longlist rejects) plus C-12; and OLD's tail (F-12, G-01,
  D-12, F-03 — each with a NEW kill/cut and a BLIND decline).
- **Verified adjudications adopted exactly:** C-07 stop (statute +
  incumbent, B40-05/06), C-05 revival on merits (B40-07/08), C-09 mid-pack
  non-EtO (B40-20/21), D-10 split verdict (B40-09/10).

## 7. Sensitivity (honest summary)

Full numbers in DECISION.json. Across six variants (PhD-leverage ×½/×2,
capital ×½/×2, time-horizon ×½/×2): ranks 1–2, top-6 membership, top-10
membership, and rank 24 are stable in every case. Real flips, reported:
D-09↔C-05 flips on BOTH the PhD axis (doubled) and the time axis (halved) —
the portfolio's genuinely unstable adjacent pair; F-06↔G-03 flips when PhD
weight doubles; the 8–16 and 18–23 bands reshuffle under doubled capital
weight (E-04/A-14, C-04/C-22 over A-05/C-01, F-23 over C-08/C-09, C-07 over
A-02); C-07↔A-02 also flips when time weight halves; several movements are
0.01-margin near-ties and are flagged as non-separations, not flips. The
pilot's provable-stability property does NOT hold on the full set — as the
pilot itself predicted. No disposition changes under any case: dispositions
rest on gates and triggers, not score decimals.

## 8. Dependencies and next decisions

The portfolio's spine is unchanged from B30: **C04** (blocks BR-D, D-02's
decisive leg, D-09's credential, and every tesla-denominated claim),
**FT-02/BR-A Phase 0** ($0, gates D-01's lane and all estimator claims),
**G5** (~month 12: accepted paper + real-die calibration; binds ALL
venture-preparation time; failure re-bases preparation on surviving skills
per OPT3), and **C33/C34/FT-01** (disclosure and novelty gates on every
public artifact). Wedge gates G-365/W1 and G-365/W2 convert BR-B/BR-A/BR-C/
BR-G outcomes into mechanical promote/demote decisions for ranks 2, 4, 5, 6,
13, 17.

**Next decisions, in order:**

1. Execute the day-0-30 PREP_PLAN block as scheduled (BR-A Phase 0, C04
   root-cause, C45 module search, BR-F desk audits, M13 prep) — it is the
   first gate set for ranks 1–6 and costs ~$0.
2. On C04 review (G-30/G-90): closed → BR-D starts and D-02's bridge is
   live; no-path → D-02 demotes per its falsifier, W1/W2 credential prep
   pauses, BR-B becomes the evidence spine.
3. On BR-B pre-flight (supervision + certificated reference): secured →
   the benchmark+dossier campaign decides F-06's modality premise, G-03's
   product premise, and D-09's methodology rehearsal in one spend.
4. Monitored-option reviews on named triggers only: OCP/NVIDIA embed check
   end-2027 (C-01), OCP conformance-program status (C-05), A-05
   revival-fact verification (A30 item 5), MTDC FID (E-14), acceptance-layer
   pricing events (C-22/C-09/C-13/F-01/F-02).
5. Operation-B rerun list: adopt A30's priorities — OCP primaries via an
   account/mirror, the ABB Infinitus primary (three fetch timeouts now),
   the eight unverified OLD→NEW reversals, and independent regeneration of
   the three supplementals before they can re-enter any future universe.

## 9. Honesty notes

- Scores are coarse ordinal aggregates; two-decimal values exist only for
  ordering audit; overlapping bands are non-separation and are labeled.
- Both base-score ties and every 0.01-margin sensitivity movement are
  disclosed rather than smoothed; dispositions are the robust layer.
- No new market size, competitor, customer, or measurement fact was
  invented; every current-market claim traces to SOURCES.csv (opened
  primaries, reused opens with original claim IDs, three logged web actions
  this run including one failed fetch, or internal evidence rows);
  corpus-dated facts are labeled record-vintage.
- Provenance discipline carried: the old06 decision layer is CONTRADICTED
  provenance (A20); overlap with OLD confers nothing; BLIND↔NEW convergence
  is agreement evidence, never proof of correctness.
- This stage is research planning and strategic screening, not legal,
  safety, export, or certification advice (SOURCE_POLICY).
