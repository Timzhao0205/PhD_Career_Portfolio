# Independent verification — B40_portfolio FULL attempt-1

- Verifier: `pap06-verifier` (fresh, independent; did not produce the candidate)
- Requested verifier model/effort: Fable 5 / xhigh. Observed: system context
  exposes model ID `claude-fable-5`; runtime effort `NOT_EXPOSED` (recorded as
  missing observation, not a mismatch and not proof).
- Candidate: `outputs/B40_portfolio/attempt-1/` (read-only; not edited)
- Worker named agent per task card: `pap06-fable-xhigh`, requested
  Fable 5 / xhigh. Candidate RUN_META records the same request, observed model
  `claude-fable-5` (system-context ID), observed effort/clock `NOT_EXPOSED` —
  requested and observed evidence kept separate per MODEL_POLICY. No mismatch.
- Inputs read: `state/CURRENT_VERIFY.md`; `workflow/stages/B40_portfolio.md`;
  `.claude/skills/pap06-native/references/ACCEPTANCE.md`; `MODEL_POLICY.md`;
  `SOURCE_POLICY.md`; all six candidate files; ground truth
  `outputs/A30_verify/attempt-1/COMPARE.json` + `VERDICT.md`;
  `outputs/B20_align/attempt-1/ALIGNMENT.csv` + `ALIGNMENT.md`;
  `outputs/B25_power/attempt-1/POWER_MAP.csv` + `POWER.md`;
  `outputs/B30_skills/attempt-1/BRIDGES.json` + `PREP_PLAN.md` (gate table);
  `outputs/B15_lit_synth/attempt-1/EVIDENCE_MAP.csv` + `GAPS.md` (cited rows);
  `outputs/A20_prov/attempt-1/PROVENANCE.json` + `PROVENANCE.md`;
  `pilot/B40_portfolio/attempt-1/RANKING.csv` + `DECISION.json`. Two live web
  re-opens (risk-stratified sample, below).

## Check 1 — Files, schemas, JSON validity: PASS

All six required files present and non-empty. RANKING.csv header is exactly
the 12-column schema
`idea_id,name,origin,disposition,score,uncertainty,phd_leverage,power_relevance,first_proof,capital_band,main_risk,falsifier`;
24 data rows, each with 12 fields (quoted cells inspected row by row); a
leading `#` comment row carries the row-order-is-rank convention — same
accepted convention as the pilot. SOURCES.csv header is exactly the 10-column
schema `claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`;
30 rows B40-01..B40-30. DECISION.json read in full; structure well-formed and
internally complete (ranking array, top_10, buckets, dependencies, sensitivity
cases, 15 rejected_alternatives, limitations).

## Check 2 — Exact counts and universe reconciliation: PASS (recounted)

I rebuilt the 41-ID union myself from A30 COMPARE.json membership arrays:
BLIND24 (24 IDs) + 12 OLD-only additions (C-01, S01, CN-01, B-01, CN-03,
F-12, G-01, G-03, D-12, F-23, F-06, F-03) + 5 NEW-only additions (A-22, D-19,
F-16, F-19, D-16) = 41, matching A30's own inclusion-exclusion check.
Applying the two documented consolidations (SEM-01: E-01→C-01; SEM-02:
B-01→C-04) gives 39 distinct concepts. Candidate ranks exactly 24 unique IDs
(no duplicates, no rank gaps; DECISION.json ranks 1-24 in identical order to
CSV row order) and rejects exactly 15. Ranked ∪ rejected = 39 with empty
intersection; the two absent union IDs are exactly E-01 and B-01 (origin-only,
per the consolidations). Reconciliation is exact: 24 + 15 = 39 = 41 − 2.
No semantic duplicate appears twice among the 24: E-01/B-01 appear only inside
C-01/C-04 origin cells; SEM-03/SEM-04 counterparts (A-13, A-21) were never
universe members; C-14 and A-22 (NON-MATCH-C14) are both rejected.

Selection-rule audit: rule (i) admits exactly the 20 claimed concepts
(11 exact triple-intersection per A30 + C-01 via SEM-01 + 8 two-final members,
each membership verified against A30 arrays); rule (ii) F-06 is B20
MEDIUM-boundary (verified); rule (iii) C-07 is the A30-verified pilot
exemplar; rule (iv) D-19 and A-02 have the claimed two-process positive
signals (verified in A30's rank-delta/decision-change tables). One rule-letter
inconsistency found (defect 1, minor): P3R2-D-12 (OLD final rank 21 + NEW P4
survivor 64.9/selection near-miss per A30) also satisfies rule (iv) as
written, yet is rejected; its rejection is separately and concretely reasoned,
so no concept is unexamined and the 24+15 partition holds, but the stated rule
does not uniquely generate the claimed 24.

## Check 3 — top_10, buckets, bridge gate citations: PASS

top_10 in DECISION.json = CSV rows 1-10 exactly (D-02, D-01, C-05, D-09,
G-03, F-06, A-10, A-14, E-04, F-02). Disposition recount from the CSV:
bridge 5 (rows 1, 2, 4, 5, 6), watch 12 (rows 3, 7-13, 15-17, 19), stop 7
(rows 14, 18, 20-24), keep 0; sums to 24 and matches the claimed
5/12/7/0 and the bucket membership lists ID-for-ID. Every bridge row cites
gates that exist in B30 BRIDGES.json / PREP_PLAN.md: G-BR-A-0, G-BR-B-pre/
mid/exit, G-BR-C, G-BR-D-pre/exit, G-BR-G, G-BR-I, G-30/G-90, G-365/W1,
G-365/W2 all verified present; PB-1/PB-2/PB-5 lineage (BR-B/BR-A) verified;
BR-B protocol step 9 does state "written acceptance dossier in the G-03
artifact format", supporting G-03's bridge premise verbatim. No invented
experiment or gate found.

## Check 4 — Pilot continuity: PASS (both files opened)

The six pilot ideas are carried with scores, uncertainties, criterion vectors,
and dispositions unchanged: D-02 3.00/0.80 bridge, D-01 2.78/0.84 bridge,
C-05 2.55/0.90 watch, C-01 1.57/0.65 watch, C-07 1.07/0.58 stop, D-10
0.65/0.65 stop — cell-by-cell identical between
`pilot/B40_portfolio/attempt-1/DECISION.json` and the full DECISION.json;
one-decimal CSV values match. Weights, scale, criteria definitions, and
disposition vocabulary carried verbatim; refinements (tie-break judgments,
unused 1.5 band) disclosed as claimed.

## Check 5 — Evidence-fidelity spot-checks: PASS (all 24 origin cells + 12 deep rows)

I verified all 24 origin cells against A30 membership arrays and rank-delta
notes (BLIND/OLD/NEW ranks, kill scores, P5 verdicts, near-miss labels) —
every cell faithful, including the fine print (e.g., D-09 "mapped but not
web-verified by A30", A-05 82% kill reversal unverified, C-09 double-kill
figures 64.4/52.2, D-10 73.4 highest-scored old kill, A-02 64.8 NEW near-miss).
Deep checks on ranks 1, 2, 3, 4, 5, 6, 7, 13, 14, 19, 23, 24:
- B20 classes faithful: 1 STRONG (D-02), 7 MEDIUM (D-01, A-14, A-10, C-05,
  D-09, E-04, F-06 — boundaries labeled), 30 WEAK, 1 ADVERSE (D-10), per
  ALIGNMENT.md §3; G-03's "WEAK at the boundary" and the D-09/F-06 "sleeper"
  characterization match B20's own text.
- B25 faithful: POWER_MAP has 31 rows; D-02, A-10, A-14, E-04, C-04, C-08,
  A-05 absent from it as claimed; C-05 "W1 family, not the founder's first
  wedge", D-01 "W2 family anchor (frontier side)", D-09 "W1 family (sleeper)"
  with PB-2 and beam-current measurand in its row, G-03 "W1 nearest-term",
  F-06 "W1 embodiment", C-22 "loses W1 retest", E-14 "HIL leg in W1
  comparison", D-10/D-19 retired — all verified in POWER.md §9 table and CSV.
- B15 citations faithful: EV01/EV06/EV23/EV26/EV27/EV30/EV31/EV34/EV35 rows
  exist; EV30/EV31 are the loose-analogy negative adjudication as claimed;
  EV06 contains the ≤9 mV vs >100 mV EMI content; EV27 the quantified WBG
  current-metrology need; G3/M3/M6/M7 present in GAPS.md as characterized.
- Score-direction: the three consequential divergences from prior-run
  standings (F-06 promoted to 6 against a weak commercial record; D-09
  promoted to 4; C-01 demoted to 13 against top-5 consensus) each carry
  explicit stated reasons in RANKING.csv, DECISION.json reasons/
  rejected_ranking_alternatives, and PORTFOLIO §6, grounded in B20/B25/B10
  adjudications; F-06's technical_proof 1 at a 0.5 band honestly carries the
  weak commercial evidence rather than smoothing it. No unexplained
  promotion or demotion found.
- The three old06 P5 supplementals (P5-USSCI2-S01, P5R2-CN-01, P5R2-CN-03)
  are rejected with the CONTRADICTED-provenance reason; A20 PROVENANCE.md
  confirms the P5 supplemental generation (including the finally selected
  S01 and CN-01) sits in the CONTRADICTED continuation layer
  (route_substitution_vs_policy), and A30 VERDICT.md rerun item 8 says
  exactly what the candidate cites (independent regeneration required).
  Cross-references to A30 rerun items 4, 5, 6 also verified accurate.

## Check 6 — Overlap recomputation: PASS (all recomputed from A30 arrays)

From the candidate's 24 and A30's membership arrays I recomputed:
- vs NEW24: exact 20 (this-24-only F-06, F-02, A-02, C-07; NEW-only A-22,
  F-16, F-19, D-16); semantic 20 (C-01 exact in both, SEM-01 adds nothing).
  Matches claimed 20/24.
- vs BLIND24: exact 19; semantic 20 via SEM-01 (E-01↔C-01, both sides
  otherwise unmatched — A30 counting rule satisfied); this-24-only G-03,
  F-06, C-01, F-23, D-19; BLIND-only E-10, C-14, C-15, C-12, E-01. Matches
  claimed 19 exact / 20 semantic.
- vs OLD24: exact 16; semantic 16 (B-01 adds nothing per SEM-02's
  counted_in_augmented_overlap=false); 8/8 only-lists match the PORTFOLIO §6
  table. Matches claimed 16/24.
- Top-10: vs BLIND10 = 5 (D-02, D-01, C-05, A-14, A-10); vs OLD10 = 3
  (D-02, D-01, A-14); vs NEW10_RANKS = 5 and vs NEW10_DEEP = 5 (same five).
  Matches claimed 5/3/5 "either variant". The calibration claims (prior runs
  agree 4-7/10 at top-10; BLIND↔NEW 16/24 strongest pairing) match A30.

## Check 7 — Sensitivity reproduction: PASS (fully recomputed)

I first re-derived all 24 base scores and aggregate uncertainties from the
published per-criterion vectors and weights (sum of weights = 1.00 verified):
every base score and uncertainty matches (including the two exact ties
C-05/D-09 at 2.55 and C-01/C-04 at 1.57, and row order = descending score
with stated tie-breaks). Then, using proportional renormalization as stated,
I recomputed ALL SIX variants (PhD ×½/×2, capital ×½/×2, time ×½/×2) for all
24 ideas. Every published two-decimal score array reproduces exactly
(96+ values checked; no discrepancies). Specifically:
- PhD doubled: D-09 2.61 > C-05 2.48 (claimed flip reproduces); F-06 2.42 >
  G-03 2.35 (claimed flip reproduces); G-03 vs A-10 0.01 near-tie confirmed;
  C-01/C-04 lockstep at 1.49 confirmed; ranks 1-2 (3.14/2.81) and rank 24
  (D-10 0.56) stable as claimed.
- PhD halved: no flips, order preserved (verified monotone).
- Capital and time variants: all claimed flips (C-08/C-13; the cap-doubled
  mid-band reshuffle; C-07/A-02 both directions; D-09/C-05 on time-halved)
  and all claimed 0.01 near-ties reproduce numerically.
- Cross-case stability: ranks 1-2 order, top-6 membership, top-10 membership,
  and D-10 last verified stable in every variant. No disposition boundary is
  crossed anywhere (dispositions rest on gates, and no variant is claimed or
  found to change one).
One numeric flaw: the cross_case_stability note states F-02 vs F-01 boundary
"margins of 0.05-0.13"; my recomputation gives 0.05-0.07 across the six
variants (exact values 0.052-0.064). The 0.13 upper figure is not
reproducible (defect 2, minor; the stability conclusion itself holds — the
true margins are tighter than stated, so the note mildly overstates the
cushion, not the membership result).

## Check 8 — Rejected list: PASS

Exactly 15 rejected IDs, each with a concrete, evidence-cited reason. Seven
reasons spot-checked in depth against the evidence base (E-10, C-14, F-19,
P5-USSCI2-S01, G-01, A-22, D-16): all faithful to A30's SEM ledger,
rank-delta notes, decision-change tables, kill probabilities (90%, 88%,
+28.0 swing), and A20's provenance verdicts. No misstated fact found.

## Check 9 — Honesty, labels, cross-artifact consistency: PASS

- ABB SACE Infinitus: third fetch timeout disclosed consistently in B40-01,
  RUN_META, PORTFOLIO §1/§6/§8, and the C-01 row; scoring treats it as
  window-pressure only — not load-bearing.
- B40-02/03 searches labeled discovery-only, no page opened, absence not
  treated as proof; A-05's and C-05's affected cells carry 1.0 bands and
  dispositions do not rest on the search outcomes.
- No pilot labels anywhere in the candidate directory (grep for "PILOT
  SAMPLE"/"NOT FINAL": zero hits); "pilot" appears only as method lineage.
- SELF_CHECK recounts all reproduce under my independent recomputation
  (IDs, buckets, aggregates, uncertainties, one-decimal rounding note).
- PORTFOLIO.md comparison numbers match my recomputations and DECISION.json;
  bucket/rank cross-references consistent across all three artifacts.
- Provenance discipline (old06 decision layer CONTRADICTED; overlap confers
  nothing; folder-08 pre-redteam C40) carried correctly.
- Live re-open sample (risk-stratified — the candidate opened no new pages
  itself, so I sampled the two most decision-critical reused primaries):
  (1) nLIGHT JLWS release: $44M initial / $627M ceiling, dated 2026-07-09,
  "proprietary coherent beam combination ... vertically integrated
  manufacturing" — verifies B40-09 and D-10's rank-24 stop basis exactly.
  (2) 26 USC 45V at uscode.house.gov: construction-start before
  January 1, 2028, substituted by PL 119-21 — verifies B40-05 and C-07's
  stop basis exactly. Both faithful.

## Defects

1. MINOR — DECISION.json `selection_rule_41_to_24`: rule (iv)'s letter
   ("final selection + P4-survivor/P5-HOLD/near-miss from >=2 processes")
   also matches rejected P3R2-D-12 (OLD final rank 21 + NEW P4 survivor
   64.9/selection near-miss per A30), so the stated four rules generate 25,
   not 24; the result paragraph's claim that rule (iv) admits only D-19 and
   A-02 is therefore imprecise. The D-12 exclusion itself is concretely
   reasoned in rejected_alternatives (mechanism absent per B20; its own
   record's EHD research-maturity verdict; BLIND PHYSICS-OPT), the 24+15
   reconciliation is exact, and D-12's disposition consequence would be a
   closed-tail stop either way — no membership or decision substance is
   affected. Repair (for any future revision, not a re-run requirement):
   tighten the rule wording or state the D-12 judgment exception explicitly.
   Acceptance test: mechanical application of the stated rule set reproduces
   exactly the 24 ranked IDs.
2. MINOR — DECISION.json `cross_case_stability`: the F-02-vs-F-01 top-10
   boundary "margins of 0.05-0.13" is not reproducible; recomputed margins
   are 0.05-0.07 across the six variants. The membership-stability claim
   itself is correct. Acceptance test: stated margin range matches
   recomputation from the published arrays.
3. MINOR — RANKING.csv P3R2-F-06 main_risk attributes both the "Danisense
   1 ppm class" and "Danfysik 10 ppm catalog" figures to B40-16, but B40-16
   (Danfysik System 9700 page) covers only the Danfysik figure; the Danisense
   1 ppm-class figure traces to B25's opened S-B25-02 (Danisense DQ500ID, in
   the accepted POWER_MAP F-06 row) and has no B40 SOURCES row. The fact is
   evidence-backed in the accepted base; only the claim-to-row mapping is
   imprecise. Acceptance test: every named incumbent figure maps to a
   SOURCES.csv row that actually contains it.

No critical or major defects.

## Limitations

- DECISION.json validity was verified by full structural read, not a machine
  parser (none is executed under the native contract); no imbalance or
  malformation was observed across the complete file.
- Live re-opening was sampled (2 of the 17 reused-open external sources);
  the remainder were opened and recorded by the accepted A30/B20/B25/pilot
  stages, whose ledgers I checked for transcription fidelity at the claim
  level rather than re-fetching.
- Verifier runtime effort is `NOT_EXPOSED` in this session; requested
  configuration (Fable 5 / xhigh) is intent evidence only, per MODEL_POLICY.

VERDICT: PASS
