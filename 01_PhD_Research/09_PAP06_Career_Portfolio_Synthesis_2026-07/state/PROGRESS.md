# Durable progress

Package state: RUNNING

- Accepted pilots: 12 / 15
- Accepted full stages: 11 / 15
- Independent full-stage PASS reports: 11 / 15
- Operation A gate: COMPLETE (state/OP_A_COMPLETE.md, 2026-07-28)
- Final release: PENDING
- Next action: RESUME per state/SHUTDOWN_CHECKPOINT.md — retry
  B50_execution FULL as a fresh `outputs/B50_execution/attempt-2/`
  (Fable 5/xhigh worker); attempt-1 preserved, INCOMPLETE, NOT accepted
  (Fable 5 usage-credit exhaustion mid-run, 2026-07-29; not a model
  downgrade, not a quality failure). Then fresh independent Fable 5/xhigh
  verification before B50 can be accepted. Do not repeat any already-
  ACCEPTED stage.

## Shutdown checkpoints

- 2026-07-29 — FABLE 5 USAGE-CREDIT EXHAUSTION during B50_execution FULL
  attempt-1 (see `state/ERROR_LOG.md`). Durable checkpoint written to
  `state/SHUTDOWN_CHECKPOINT.md`. attempt-1 holds 2/6 files, preserved
  unmodified, NOT accepted; no verification report exists for B50. This
  checkpoint-writing turn ran administratively under Sonnet 5 (user
  `/model` switch after credit exhaustion) — bookkeeping only, no research
  content produced or modified; B50's requested route model remains
  Fable 5/xhigh. All 12 accepted pilots and 11 accepted full stages (with
  their PASS reports) confirmed unaffected. Not a package budget stop (none
  exists) and not a research-quality failure.

- 2026-07-28 — User-requested shutdown. Durable checkpoint written to
  `state/SHUTDOWN_CHECKPOINT.md` (since superseded/updated by the 2026-07-29
  entry above). B00 FULL attempt-1 FAILED verification and is preserved;
  attempt-2 repair finished naturally during checkpointing, retained
  COMPLETE BUT UNVERIFIED and unaccepted (no new agents launched per
  shutdown instruction). No partial or unverified work marked accepted.
  No background work running. Not a budget or provider stop. This episode
  was fully resolved on resume the same day (see Accepted items below).

## Accepted items

- 2026-07-29 — B50_execution PILOT ACCEPTED. Candidate:
  `pilot/B50_execution/attempt-1/`. Three-lane 90-day slice (PhD critical
  path prioritized incl. C04 day-0 block and C45 catch-up; BR-A verdict +
  bench start; BR-B cleared pre-flight with written-supervision and
  certificated-reference gates); MW-1..MW-9 human-only actions; IP items as
  professional questions; honest post-window scoping. All labeled.
  Environment date rolled 2026-07-28→29 mid-run, disclosed; anchor kept.

- 2026-07-28 — B40_portfolio FULL ACCEPTED. Candidate:
  `outputs/B40_portfolio/attempt-1/`. Independent verification:
  `verification/B40_portfolio/FULL_attempt-1.md` ends `VERDICT: PASS`
  (3 minor defects — selection-rule-iv wording, boundary-margin range, one
  source attribution — carry to B60/B70). Canonical 24: D-02 #1 through
  D-10 #24; dispositions 5 bridge / 12 watch / 7 stop / 0 keep; overlaps
  NEW24 20, BLIND24 19-20, OLD24 16; top-10 audits for all 24; 15 reasoned
  rejections; all scores/overlaps/sensitivity independently reproduced.

- 2026-07-28 — B40_portfolio PILOT ACCEPTED. Candidate:
  `pilot/B40_portfolio/attempt-1/`. Six-idea spectrum ranking (D-02 3.0
  bridge → D-10 0.7 stop) with declared weights, per-criterion uncertainty
  bands, and honest non-separation disclosure for ranks 1-3; zero `keep`
  dispositions (bridge-shaped top — every strong mechanism is C04/FT-02
  gated); sensitivity check provably stable with disclosed sample artifact;
  1 live open (Siemens SENTRON 3QD2), ABB timeout disclosed. All labeled.

- 2026-07-28 — B30_skills FULL ACCEPTED. Candidate: `outputs/B30_skills/attempt-1/`.
  Independent verification: `verification/B30_skills/FULL_attempt-1.md` ends
  `VERDICT: PASS` (3 minor defects; skill-inflation audit CLEAN on all five
  current_demonstrated rows). 20 skills (5/7/3/5 levels, six founder-fit
  corrections bound); unified 9-entry bridge ladder BR-A..BR-I with complete
  BT-1..8 + PB-1..7 lineage; 14-gate 30/90/180/365 prep plan integrated
  with the PhD critical path.

- 2026-07-28 — B30_skills PILOT ACCEPTED. Candidate: `pilot/B30_skills/attempt-1/`.
  5 skills exercising all four levels (2 sensing, 2 power, 1 shared) with
  honest bounds carried per B10 claim; BR-A (estimator-honesty-gated
  reverse-direction ladder) and BR-B (traceable Hall-vs-TMR under WBG EMI)
  ranked with full lineage to BT/PB ladders; 7 stop/continue gates on the
  30/90/180/365 skeleton. All artifacts labeled.

- 2026-07-28 — B25_power FULL ACCEPTED. Candidate: `outputs/B25_power/attempt-1/`.
  Independent verification: `verification/B25_power/FULL_attempt-1.md` ends
  `VERDICT: PASS` (2 minor defects — PB-6 controls element; FIA 48% tie
  omission — carry to B60/B70). 31 rows (23 universe + 8 startup-corpus,
  roles 12/10/6/3); wedges W1 (DC-asset measurement/qualification authority
  around F-06/G-03/C-05/D-09) and W2 (magnet-power measurement-chain and
  protection-detection authority); ranked bridge ladder PB-1..PB-7; §3.6
  founder-fit correction vs startup corpus adjudicated justified.

- 2026-07-28 — B25_power PILOT ACCEPTED. Candidate: `pilot/B25_power/attempt-1/`.
  4 architectures spanning all four roles (C-01 end product, C-13 subsystem,
  F-06 measurement tool = preliminary preferred wedge, E-10 reference
  design); PB-1 bridge experiment (Hall-vs-TMR under WBG switching with
  traceable zero-flux chain) in full form; converter-stack missing
  capabilities named honestly; 3 live opens (NVIDIA 800VDC/Kyber 2027,
  Danisense zero-flux grade, IEC 62477-1 scope). All artifacts labeled.

- 2026-07-28 — B20_align FULL ACCEPTED. Candidate: `outputs/B20_align/attempt-1/`.
  Independent verification: `verification/B20_align/FULL_attempt-1.md` ends
  `VERDICT: PASS` (3 minor defects — G5 namespace collision, C23
  inferred-vs-proposed labels, F-06 dependency cell — carry to B60/B70).
  39 rows reconcile exactly to the 41-idea A30 union via SEM-01/SEM-02
  consolidations; classes 1 strong (D-02) / 7 medium / 30 weak / 1 adverse
  (D-10); all 5 founder-fit corrections adjudicated justified; Opt2 touches
  ~8/39 ideas. Key downstream facts: D-02 is the only direct-leverage case;
  A-10, D-09, F-06 are sleeper mediums from killed/cut strata.

- 2026-07-28 — B20_align PILOT ACCEPTED. Candidate: `pilot/B20_align/attempt-1/`.
  Six ideas spanning strong (D-02) / medium (D-01, A-14) / weak (C-13, C-07)
  / adverse (D-10); both causal directions with mechanism-based evidence
  chains to B10 claim IDs and B15 evidence rows; 3 counterfactuals; 4
  systematic asymmetries (PhD→startup stronger than reverse; synergy rides
  on proposed-not-demonstrated Opt2 elements); 2 new06 founder-fit
  overstatements corrected. All artifacts labeled.

- 2026-07-28 — B15_lit_synth FULL ACCEPTED. Candidate:
  `outputs/B15_lit_synth/attempt-1/`. Independent verification:
  `verification/B15_lit_synth/FULL_attempt-1.md` ends `VERDICT: PASS`
  (3 minor defects documented: P0048-vs-P0050 figure attribution in one
  row; EV11 CVD-on-SiC platform label doubtful; one heading slip — carry
  these to B60/B70 for cleanup). 35 evidence rows, 62/62 papers used
  (13/14/17/18), audit recount 43 recent confirmed, P0017/P0050 typing
  corrections adjudicated correct. Key verified findings for downstream:
  coil→Hall reverse calibration unsupported in corpus; GaN/AlGaN radiation
  dataset absent; 6 ranked bridge tests (BT-1..BT-6) feed B25/B30.

- 2026-07-28 — B15_lit_synth PILOT ACCEPTED. Candidate:
  `pilot/B15_lit_synth/attempt-1/`. 8/8 B12 pilot papers independently
  re-opened and confirmed (0 corrections needed; 6 substantive quality
  additions incl. 36-real-quench-record base, synthetic-only Kalman
  validation, paywalled P0007 full text, 12-day review-cycle caveat); 10
  evidence rows across all four streams; 3 contradictions/gaps incl. the
  key finding that the coil→Hall reverse-calibration assumption is
  unsupported and JET's own coils were never bench-calibrated. All 7
  artifacts labeled.

- 2026-07-28 — B12_lit_search FULL ACCEPTED. Candidate:
  `outputs/B12_lit_search/attempt-1/`. Independent verification:
  `verification/B12_lit_search/FULL_attempt-1.md` ends `VERDICT: PASS`
  (4 minor non-blocking defects; notable: true 2020-2026 recency count is
  43, one better than the claimed 42 — carry the corrected figure forward).
  62 unique publications P0001-P0062, all accepted_core (streams 13/14/17/
  18), zero supplements, P0001-P0008 stable; verifier opened 20 rows live —
  all matched publisher records, zero fabrication; P0012 correction notice
  verified verbatim. B15 must use this ledger as its evidence base and may
  independently correct B12 classifications.

- 2026-07-28 — B12_lit_search PILOT ACCEPTED. Candidate:
  `pilot/B12_lit_search/attempt-1/`. 8 retained papers P0001-P0008, all
  accepted_core, exactly 2 per stream; 6 verified via directly opened
  publisher landing pages, 2 via disclosed PMC mirrors (MDPI 403); schema,
  controlled vocabulary, and DOI normalization exact; 10 logged queries, 11
  exclusions; correction/retraction status recorded per row. Full-run
  convention note: keep publisher_url a single clean URL per row.

- 2026-07-28 — B10_phd FULL ACCEPTED. Candidate: `outputs/B10_phd/attempt-1/`.
  Independent verification: `verification/B10_phd/FULL_attempt-1.md` ends
  `VERDICT: PASS` (4 minor non-blocking defects documented). 50 claims
  (24 demonstrated / 17 proposed / 4 inferred / 5 unknown), C01-C10 stable
  vs pilot; verifier spot-checked ~35 claims incl. opening the decision-
  letter PDF and raw HSX files; folder-08 pre-redteam caveat verified on
  every dependent claim. Note for later stages: folder-08 has a redteam log
  stream but no redteam OUTPUT files — recheck if that changes.

- 2026-07-28 — B10_phd PILOT ACCEPTED. Candidate: `pilot/B10_phd/attempt-1/`.
  10 claims spanning current work (C01-C05) and all three Opt2 elements
  (C06-C10); statuses demonstrated/proposed/inferred/unknown correctly
  disciplined; absolute calibration, mutual consistency, bandwidth fusion,
  and radiation compensation kept as distinct claims; all cited phd paths
  verified; folder-08 pre-redteam caveat applied consistently; no web
  needed; all six artifacts labeled.

- 2026-07-28 — B00_inventory FULL ACCEPTED at attempt-2 (post-shutdown
  resume; attempt-1 failed verification and is preserved). Candidate:
  `outputs/B00_inventory/attempt-2/`. Independent verification:
  `verification/B00_inventory/FULL_attempt-2.md` ends `VERDICT: PASS`
  (fresh verifier; 1 minor non-blocking defect). All 5 attempt-1 defects
  cured with fresh recounts (phd-08 outputs 25; disclosures 6 with ID_05
  gap; 7 surveys; 7 records/21 verdicts). The disputed 05_CryoFree tree
  count was independently adjudicated at 80 — the candidate was right and
  the attempt-1 FAIL report's own 83 was wrong (recorded for B80).

- 2026-07-28 — B00_inventory PILOT ACCEPTED at attempt-2 (attempt-1 rejected
  for a missing pilot banner on RUN_META.md; see ERROR_LOG). Candidate:
  `pilot/B00_inventory/attempt-2/`. Four roots + four canonical artifacts +
  old06 dedup relationship (manifest-attributed + absence spot checks); six
  conflicts recorded unresolved incl. old/new P3R2-D-02 score split (65.6 vs
  81.9) and startup 689-vs-690 source count; all six artifacts labeled.

- 2026-07-28 — A30_verify FULL ACCEPTED. Candidate: `outputs/A30_verify/attempt-1/`.
  Independent verification: `verification/A30_verify/FULL_attempt-1.md` ends
  `VERDICT: PASS` (2 minor defects documented, none blocking). Verifier
  re-derived all membership sets, recomputed all overlaps (12/16/14 at 24;
  4/6/7/7/6 at 10; triple 11; union 41), verified the semantic ledger, checked
  ~30 decision/rank entries, and opened 4 cited URLs — all supported.
  OPERATION A COMPLETE — gate file `state/OP_A_COMPLETE.md` written.

- 2026-07-28 — A30_verify PILOT ACCEPTED. Candidate: `pilot/A30_verify/attempt-1/`.
  Six deterministic IDs (A10 full ranks 1-6) compared against old06/new06;
  exact-ID overlap 3/6 old and 5/6 new (4/6, 6/6 with one documented semantic
  match E-01<->C-01); one material disagreement (DIS-C05-OCP-DESCHUTES)
  verified with two opened primary sources; OCP/DCD 403 blocks disclosed and
  downgraded honestly. Labels, ledger separation, and A20 provenance
  conditioning all compliant.

- 2026-07-28 — A20_prov FULL ACCEPTED. Candidate: `outputs/A20_prov/attempt-1/`.
  Independent verification: `verification/A20_prov/FULL_attempt-1.md` ends
  `VERDICT: PASS` (pap06-verifier, requested Fable 5/xhigh; 4 minor
  non-blocking nits documented in the report). Findings of record: 165 task
  rows; core idea generation PARTIAL_PROVENANCE (runtime model fable verified
  15/15, runtime effort never recorded anywhere); adjudication/screening
  PARTIAL_PROVENANCE with a 27-task CONTRADICTED continuation subset; all
  later Folder 06 artifacts CONTRADICTED (ChatGPT continuation, actual model
  unknown). Zero CONFIRMED rows because no historical runtime effort field
  exists — an honest, evidence-limited result.

- 2026-07-28 — A20_prov PILOT ACCEPTED. Candidate: `pilot/A20_prov/attempt-1/`.
  4-item deterministic sample (P3R2-A, P3R2-ELEGANCE-JUDGE: PARTIAL_PROVENANCE
  with runtime-logged fable model but request-only effort; two ChatGPT-
  continuation deep dives: CONTRADICTED). Controller spot-checked routing-log
  lines 173/309/311/313, _about.md contradiction, and the 1829-count fable
  model-field grep — all verbatim matches. Labels, separation of requested vs
  observed, and limitations all compliant.

- 2026-07-28 — A10_blind FULL ACCEPTED. Candidate: `outputs/A10_blind/attempt-1/`.
  Independent verification: `verification/A10_blind/FULL_attempt-1.md` ends
  `VERDICT: PASS` (pap06-verifier, requested Fable 5/xhigh). Verifier recounted
  126/126 coverage from shard ground truth, spot-checked 10/24 selected objects
  and 9/102 dispositions, confirmed 24 unique ranks, TOP10 = ranks 1-10, no
  pilot labels, blind/no-web documentation consistent. One minor non-blocking
  nit: three figures sourced from explicitly-merged cluster-member records
  rather than headline records (verbatim pool-supported, disclosed).
  Limitations: worker tool invocations not post-hoc observable; observed
  model/effort rest on runtime self-identification / NOT_EXPOSED.

- 2026-07-28 — A10_blind PILOT ACCEPTED. Candidate: `pilot/A10_blind/attempt-1/`
  (SELECTION.json, TOP10.json, METHOD.md, RUN_META.md, SELF_CHECK.md).
  Controller-verified: deterministic 6-ID sample matches shard order
  (independently spot-checked), 3-of-6 TOP10 consistent, pilot labels present,
  schema exercises all nine rubric components, blind/no-web compliance stated.
  Limitations: shard hashes not recomputed (no code execution under native
  contract); observed effort/times NOT_EXPOSED; observed model is worker-side
  runtime declaration only.

This file is updated after every accepted item. Reconcile it with
`STAGE_LEDGER.json` and actual files at every session start.
