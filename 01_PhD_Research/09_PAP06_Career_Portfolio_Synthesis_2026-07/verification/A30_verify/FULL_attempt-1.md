# Independent verification report — A30_verify FULL attempt-1

- Verifier: `pap06-verifier` (independent; did not produce the candidate).
  Requested verifier model/effort per `state/CURRENT_VERIFY.md`: Fable 5 /
  xhigh. Runtime self-identification: Fable 5 (`claude-fable-5`); runtime
  effort NOT_EXPOSED (recorded as missing observation, not evidence).
- Date: 2026-07-28.
- Candidate (read-only, unmodified): `outputs/A30_verify/attempt-1/`
  (COMPARE.json, COMPARE.md, VERDICT.md, SOURCES.csv, RUN_META.md,
  SELF_CHECK.md).
- Inputs read for ground truth: `state/CURRENT_VERIFY.md`;
  `workflow/stages/A30_verify.md`; `workflow/ROUTE.json`;
  `.claude/skills/pap06-native/references/ACCEPTANCE.md`; SOURCE_POLICY.md,
  MODEL_POLICY.md, LIT_POLICY.md; `outputs/A10_blind/attempt-1/`
  (SELECTION.json, TOP10.json, METHOD.md); `outputs/A20_prov/attempt-1/
  PROVENANCE.md`; `sources/old06/60_FINAL_PORTFOLIO/02_COMPARISON_MATRIX.csv`;
  `sources/old06/30_SCREENING/P5_SELECTION.json`; `sources/old06/30_SCREENING/
  SCORECARDS/P4_SCORES_ALL.md`; `sources/old06/30_SCREENING/REDTEAM/*`;
  `sources/old06/20_OPPORTUNITY_POOL/P3R2_ELEGANCE_ADJUDICATION.json`;
  `sources/new06/outputs/70_audit/FINAL/SELECTION.json`;
  `sources/new06/outputs/20_p4/P4_REPORT.md`;
  `sources/new06/outputs/40_select/SELECTION.md`;
  `pilot/A30_verify/attempt-1/SOURCES.csv`. Web re-opening of 4 cited URLs
  (listed under check 6).

## Check 1 — required files, SOURCES.csv structure: PASS

All six required files exist and are non-empty. ROUTE.json requires
COMPARE.json, COMPARE.md, VERDICT.md, SOURCES.csv for A30; RUN_META.md and
SELF_CHECK.md required by acceptance rules — all present, all only inside the
target directory. SOURCES.csv header is exactly
`claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`;
15 data rows; every comma-bearing field (all limitations) is double-quoted;
each row parses to exactly 10 fields.

## Check 2 — membership-set fidelity: PASS (fully re-derived)

- BLIND24 re-derived from `outputs/A10_blind/attempt-1/SELECTION.json` ranks
  1-24: E-01, C-05, D-01, C-09, D-02, A-14, E-14, C-08, A-10, C-07, C-04,
  E-10, C-14, D-10, C-22, F-02, A-05, C-15, A-02, F-01, E-04, C-12, D-09,
  C-13. Identical element-by-element and in order to the candidate's
  `BLIND24_ranked`. TOP10.json = ranks 1-10, same IDs/order = candidate's
  BLIND10.
- OLD24 re-derived from `02_COMPARISON_MATRIX.csv` ranks 1-24: D-02, C-22,
  D-01, F-01, C-01, P5-USSCI2-S01, E-14, P5R2-CN-01, A-14, C-13, C-08, B-01,
  E-04, P5R2-CN-03, F-02, C-04, F-12, G-01, A-10, G-03, D-12, F-23, F-06,
  F-03. Identical to candidate. I cross-checked ALL 24 idea_id/rank pairs
  against `P5_SELECTION.json` final_24 (exceeds the 8-rank minimum): all
  match. `top_10_deep_dives` (lines 1419-1430) = matrix ranks 1-10 in order =
  candidate's OLD10.
- NEW24 re-derived from `outputs/70_audit/FINAL/SELECTION.json` final_24 (read
  in full): D-02, C-01, C-05, D-10, E-14, A-14, D-01, A-10, C-13, F-01, A-05,
  C-09, C-22, C-08, G-03, E-04, D-09, A-22, C-04, D-19, F-16, F-19, F-23,
  D-16. Identical to candidate. NEW10_RANKS = ranks 1-10 — matches.
  NEW10_DEEP = `top_10_deep_dives` = ranks 1-8 plus C-09 (rank 12) and C-22
  (rank 13) — matches; the C-13/F-01 pass-over rationale confirmed in
  `40_select/SELECTION.md` "Deep-dive choices (10)".

## Check 3 — pairwise overlaps recomputed: PASS (all figures reproduce)

Computed by me from the re-derived arrays, element by element:

- At 24: BLIND∩OLD = 12 (D-01, D-02, A-14, E-14, C-08, A-10, C-04, C-22,
  F-02, F-01, E-04, C-13 — candidate's shared/only lists identical);
  BLIND∩NEW = 16 (candidate's lists identical); OLD∩NEW = 14 (candidate's
  lists identical). Claimed 12/16/14 confirmed.
- Triple intersection = 11 (the BLIND∩OLD twelve minus F-02) — candidate's ID
  list identical. Union = 41 by inclusion-exclusion (72−12−16−14+11) and by
  direct enumeration (24 BLIND + 12 old-only + 5 new-only-vs-both: A-22,
  D-19, F-16, F-19, D-16).
- At 10: BLIND10∩OLD10 = 4 (D-01, D-02, A-14, E-14); BLIND10∩NEW10-RANKS = 6;
  BLIND10∩NEW10-DEEP = 7 (adds C-09); OLD10∩NEW10-RANKS = 7;
  OLD10∩NEW10-DEEP = 6. All claimed counts and member lists confirmed.
- Semantic-augmented figures (13, 17, 14; 5, 7, 8, 7, 6) differ from exact by
  exactly +1 in precisely those pairings where E-01 sits unmatched on the
  blind side and C-01 unmatched on the other side, and by 0 where C-01 is
  exact in both — the documented counting rule, applied correctly, nowhere
  else.

## Check 4 — semantic ledger: PASS

- SEM-01 (E-01↔C-01): corpus-internal documentation verified at
  `P3R2_ELEGANCE_ADJUDICATION.json` line 95 (E-01 verdict REJECT,
  `duplicate_of: "P3R2-C-01"`) and line 111 (cluster "800VDC rack-inlet
  protection", canonical C-01, members include E-01). A10-side reverse choice
  verified verbatim: SELECTION.json rank-1 decision "Chosen over
  near-duplicates A-01/B-03/C-01"; METHOD.md "E-01 over C-01 (same concept,
  lower capital and cleaner export posture)"; C-01 disposition DUP-UNSEL.
  This is cluster/merge documentation, not name similarity.
- SEM-02 (B-01↔C-04): new06 canonical SELECTION.json near-miss text verified
  verbatim ("the same two-phase-loop thesis as C-04 (its own merge notes say
  so)... one slot, C-04 took it"); A10 rank-11 decision verified verbatim
  ("the merged variant absorbs B-01's negative-pressure leak-safe mechanism").
  Correctly NOT counted (C-04 already exact in every pairing; counting would
  double-map one blind idea).
- SEM-03 (E-10↔A-13) verified at adjudication lines 104/131; SEM-04
  (C-15↔A-21) at lines 67/128. Both canonicals absent from all three finals,
  so correctly zero overlap effect. A-13 old P4 rank 25 at 57.2 and A-21 rank
  29 at 51.0 with P5 kills (92%, 84%) verified.
- NON-MATCH-C14 verified: line 66 has `duplicate_of: null` with "A-22 is the
  better vehicle" as preference prose; A10 rank-13 decision explicitly prefers
  C-14 over A-22 as different products. Correctly excluded.
- No other semantic match was silently counted (established arithmetically in
  check 3).

## Check 5 — decision-change and rank-delta tables: PASS (approx. 30 entries spot-checked, well above the 6 minimum)

All verified against ground-truth files:

- Old G7 kills with scores and reasons (`P4_SCORES_ALL.md` lines 47-78):
  D-10 73.4 (2026-2028 decision concentration), C-05 67.4 (no primary
  2028-2035 trigger; OCP/vendor-lab standardization path), C-09 64.4 (EtO
  wrong direction; Entity-List adjacency), C-07 60.0 (2027
  construction-start pull-forward; Ingeteam/Sungrow AFE occupancy), D-09
  58.2 G1+G7, F-16 57.4 G7, C-12 44.4 G1+G7, F-19 36.6 G1+G4+G7
  (Ecolab/CoolIT). All match the candidate's quotes/paraphrases.
- P5 revival re-kill: C-09 at 52.2, G7 FAIL, stale CEPC schedule
  (`P5_RT_REVIVALS.md` lines 10, 132) — matches.
- P5 kills/hold: A-05 82%/suggested 39.8/G1+G7 (P5_RT_G06 line 18), A-22
  90%/G2+G4+G7 (line 19), D-16 88%/G4 (P5_RT_G03 line 18), D-19 HOLD
  (P5_RT_G02 line 122), plus A-13 92%, D-13 80%, A-21 84%, E-02 84%, A-02
  82% supporting COMPARE.md's "killed 8, held 1" decomposition (30 P4
  survivors − 21 P3R2 finalists = 9: exactly those eight kills plus D-19).
- Old P4 survivor scores: A-05 63.2, A-22 61.0, D-19 60.4, D-16 56.2, A-02
  55.2, D-02 P4 total 76.6 vs matrix P5-adjusted 65.6 (the candidate's
  score_total disclosure is accurate).
- New06 figures (canonical SELECTION.json + P4_REPORT.md): all 24 ranks and
  every quoted score (C-05 78.3, D-10 78.7, C-09 72.0, A-05 72.1, D-09 67.4,
  A-22 66.9, D-19 64.9, F-16 64.8, F-19 64.6, D-16 63.0); cut at 62.7 with
  C-07 first excluded at 61.6 gates-clean and electrowinning fallback
  preserved; score-cuts F-02 59.4, F-12 56.0, F-06 59.5, F-03 58.3, A-13
  59.5, A-21 58.7, C-12 54.9 gates-clean; G-01 fresh G1 kill on the CEPC
  15th-FYP exclusion; B-01/D-12/A-02 near-miss texts. All match.
- BLIND disposition codes in the notes (A-22 CONTINGENT preferring C-14, D-12
  PHYSICS-OPT, D-16 PROGRAM, F-19 WEAK-EV near-miss, G-01 ACCESS+PROGRAM
  citing CEPC lumpiness, G-03 CONTINGENT near-miss) verified against A10
  METHOD.md's disposition table.
- Rank-delta arithmetic (e.g., C-22 +11, A-10 −11, C-01 −3, F-01 +6)
  recomputed from the verified rank arrays: correct throughout.

## Check 6 — disagreement verification quality and web spot-checks: PASS

Four disagreements (deepened DIS-C05 plus DIS-D10, DIS-C09, DIS-C07), each
with at least 2 sources marked OPENED that are primary/official (D10 and C09
have 3 opened each). I independently re-opened four load-bearing cited URLs:

1. Google Cloud Deschutes blog (C05-DIS-01): confirmed published 2025-10-13;
   Deschutes contributed to OCP; spec
   `ocp-specification-deschutes-final-2025-09-05` plus design collateral zip
   linked; exactly seven suppliers named (Boyd, CoolerMaster, Delta,
   Envicool, Nidec, nVent, Vertiv) demoing at OCP Global Summit and SC25.
   Exact match to the candidate's claims, including the seven-vs-eight vendor
   distinction the candidate flagged.
2. 26 USC 45V at uscode.house.gov (C07-DIS-01): confirmed (c)(3)(A)
   "construction of which begins before January 1, 2028" and the PL 119-21
   §70511 amendment note substituting 2028 for 2033 (enacted 2025-07-04).
   Exact match.
3. nLIGHT JLWS release (D10-DIS-02): confirmed 2026-07-09; $44M initial /
   $627M ceiling; ~150 kW prototypes scaling to 300-500 kW; demonstrations
   "as early as 2028"; "proprietary coherent beam combination and atmospheric
   correction technology, and vertically integrated manufacturing approach".
   Exact match, including the internalization-risk evidence the candidate's
   adjudication leans on.
4. EPA EtO release (C09-DIS-02): confirmed 2026-03-13; proposes removing the
   2024 rule's risk-based standards, CEMS flexibility, and references the
   January 2025 Presidential exemption process. Matches the candidate's use;
   the July-2025 proclamation/22-facility detail is correctly labeled
   search-level corroboration in COMPARE.json, not attributed to this page.

No fetch failed for me; no discrepancy found between any opened page and the
candidate's characterization of it. The six opened URLs I did not re-open
(Nidec, Lockheed, Military Times, ScandiNova, Rapiscan, Ingeteam) carry
claims consistent with the corpus and with the candidate's disclosed
anomalies (Lockheed URL-slug/date conflict, Nidec date ambiguity — both
honestly recorded rather than smoothed over).

## Check 7 — opened vs not-opened honesty: PASS

The five NOT OPENED rows (C05-DIS-03/04/05 all HTTP 403; C09-DIS-04 timeout;
C07-DIS-03 never attempted, search-level) are marked with failure mode and
downgraded confidence (existence-only/discovery-only). In COMPARE/VERDICT
they are used only at existence/discovery level: the OCP spec stays
"existence-only via the opened Google post's hyperlink"; the OCP-vacuum
negative claim stays "partially verified, discovery-level"; the OSI $19M
order and Ingeteam >600 MW figures are explicitly search-level corroboration
with an opened primary carrying the claim. Confidence labels match usage.

## Check 8 — VERDICT.md calibration: PASS

Conditioning matches accepted A20 PROVENANCE.md exactly: old06 decision layer
(P4 authoritative scoring, G7 kills, P5 red teams, final 24/10, deep dives)
CONTRADICTED (ChatGPT continuation, model/effort unknown); records/longlist
PARTIAL_PROVENANCE (Fable-5 model verified, effort request-only); new06
unaudited. VERDICT explicitly forbids Fable-vs-Fable readings, refuses
runtime-effort conclusions anywhere, and frames the 16/24 BLIND-NEW
convergence as agreement evidence given shared input lineage — never
authorship or correctness proof. The rerun list is concrete (8 prioritized
items with reasons and open evidence gaps).

## Check 9 — pilot labels, fabrication, cross-artifact consistency: PASS

No candidate file labels this run as a pilot; COMPARE.md's reference to
incorporating the accepted pilot after re-checking, and SELF_CHECK's
quotation of the label string in compliance discussion, are permitted. Every
URL/title/publisher/date/quote/rank/count I spot-checked traced correctly;
uncertain dates are marked uncertain rather than asserted. Overlap figures
are identical across COMPARE.json, COMPARE.md, and VERDICT.md (12/16/14;
13/17/14; 4/6/7/7/6; 5/7/8). Disagreement IDs, rank/kill facts, and
confidence labels agree across all four artifacts.

## Check 10 — RUN_META/SELF_CHECK honesty per MODEL_POLICY: PASS

Named agent `pap06-fable-xhigh` and requested Fable 5 / xhigh match the route
and the verification card. Observed model is recorded as runtime
self-identification and labeled as such (not external telemetry); observed
effort recorded NOT_EXPOSED — treated here as missing observation, not
mismatch and not proof. Web log (10 fetch successes, 5 failures, 9 searches)
is internally consistent and reconciles exactly with SOURCES.csv: 10 rows
marked OPENED, 4 failure-marked rows plus the BusinessWire mirror failure
disclosed inside C09-DIS-04's limitation; C07-DIS-03 (never attempted)
correctly absent from the failure list. No budget/turn/time stop claimed.

## Defects

1. (minor) `COMPARE.json` set_definitions.NEW.top_10_defined_by says C-13
   (9), F-01 (10), A-05 (11) were passed over "for lane-coverage reasons
   recorded in sources/new06/outputs/40_select/SELECTION.md"; SELECTION.md's
   "Deep-dive choices (10)" explicitly names only C-13 and F-01 — A-05's
   pass-over is implicit from the arrays (deep dives jump rank 8 → 12), not
   stated in that section. No numeric or membership effect; affected file:
   `outputs/A30_verify/attempt-1/COMPARE.json`. Does not fail any acceptance
   test.
2. (minor) The C-09 old-kill gloss names "CGN" as the Entity-List-adjacent
   counterparty; the P4 kill line itself says only "the largest named China
   counterparty". CGN is corpus-consistent (named in the C-09 idea record and
   A10's rank-4 reasoning), so this is an attributable gloss, not
   fabrication; affected files: `COMPARE.json`/`COMPARE.md`.

No critical or major defects found.

## Limitations of this verification

- I re-opened 4 of the 10 opened web sources (risk-stratified toward the most
  load-bearing claims); the other six were checked for internal consistency
  and disclosed anomalies only.
- new06 `SURVIVORS.json` C-04 p5_focus (SEM-02's third documentation leg) was
  not independently re-read; the two legs I verified are sufficient.
- Old06 red-team prose was verified at the rank/score/gate/verdict level, not
  read exhaustively.
- The worker's and this verifier's actual runtime model/effort are not
  externally observable; requested-configuration evidence proves intent only,
  per MODEL_POLICY.

VERDICT: PASS
