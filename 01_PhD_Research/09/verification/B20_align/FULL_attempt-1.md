# Independent verification — B20_align FULL attempt-1

- Verifier: `pap06-verifier` (fresh, independent; did not produce the candidate)
- Requested verifier model/effort: Fable 5 / xhigh. Observed: the runtime
  system prompt self-identifies as Fable 5 (`claude-fable-5`); effort
  NOT_EXPOSED. Recorded as self-declaration, kept separate from the request.
- Date: 2026-07-28
- Candidate: `outputs/B20_align/attempt-1/` (read-only; nothing edited)
- Report target (this file): `verification/B20_align/FULL_attempt-1.md`

## Scope and inputs

Read in full or at targeted depth: `state/CURRENT_VERIFY.md`;
`workflow/stages/B20_align.md`; `.claude/skills/pap06-native/references/ACCEPTANCE.md`;
`SOURCE_POLICY.md`; `MODEL_POLICY.md`; all six candidate files
(`ALIGNMENT.csv`, `ALIGNMENT.md`, `IMPACT_MAP.md`, `SOURCES.csv`,
`RUN_META.md`, `SELF_CHECK.md`); ground truth
`outputs/A30_verify/attempt-1/COMPARE.json` (full),
`outputs/B10_phd/attempt-1/PHD_FACTS.json` (full, C01–C50),
`outputs/B15_lit_synth/attempt-1/EVIDENCE_MAP.csv` (full, EV01–EV35) and
`GAPS.md` (full); accepted pilot `pilot/B20_align/attempt-1/` (ALIGNMENT.csv,
SOURCES.csv); corpus records: `sources/new06/outputs/70_audit/FINAL/DEEP/`
D01–D04, D08 (§14 and founder-stack passages), `FINAL/SELECTION.json` entries
for F-19, D-19, G-03, `sources/old06/30_SCREENING/EVIDENCE/P3R2-D-09.md`,
`sources/old06/40_DEEP_DIVES/DD_P3R2_A_14.md`; directory existence checks
(Glob) of `30_SCREENING/EVIDENCE/` and `FINAL/DEEP/`. Live web: re-opened
S-B20-03 (Impedans Semion) myself.

## Check 1 — Required files and schemas: PASS

All six files present and non-empty. `ALIGNMENT.csv` header is exactly the
13-column stage-spec schema
(`idea_id,...,falsifier,action`); all 39 data rows carry 13 fields with
comma-containing fields quoted (visual field-walk of every row; unquoted
fields — idea_id, evidence, some confidence values — contain no commas).
`SOURCES.csv` header is exactly the 10-column schema. One legend comment line
precedes each header, matching the accepted pilot precedent. RUN_META and
SELF_CHECK are substantive. Named agent `pap06-fable-xhigh` and requested
Fable 5 / xhigh match the verification card and MODEL_POLICY (critical
worker); observed model recorded as an explicitly-labeled self-declaration and
observed effort NOT_EXPOSED — correct evidence discipline (treated as missing
observation, not mismatch, not proof).

## Check 2 — Universe completeness: PASS (own reconstruction)

I rebuilt the union from COMPARE.json membership arrays myself:

- BLIND24 (24 unique): E-01, C-05, D-01, C-09, D-02, A-14, E-14, C-08, A-10,
  C-07, C-04, E-10, C-14, D-10, C-22, F-02, A-05, C-15, A-02, F-01, E-04,
  C-12, D-09, C-13.
- OLD24 adds 12 new: C-01, P5-USSCI2-S01, P5R2-CN-01, B-01, P5R2-CN-03,
  F-12, G-01, G-03, D-12, F-23, F-06, F-03 → 36.
- NEW24 adds 5 new: A-22, D-19, F-16, F-19, D-16 → **41**, matching
  COMPARE.json's inclusion-exclusion check (72 − 12 − 16 − 14 + 11 = 41).

Candidate rows: 39, all verbatim members of the 41. Union minus rows =
exactly {P3R2-E-01, P3R2-B-01}, i.e. the two claimed consolidations.
E-01→C-01 corresponds to A30 ledger SEM-01 (elegance-adjudication duplicate
cluster, counted in augmented overlap) and B-01→C-04 to SEM-02 (new06's own
merge note + A10 absorption) — both documented semantic-ledger entries, both
carried inside the consolidated rows' name/source_version cells with the SEM
ID cited. C-14 (row, line 40) and A-22 (row, line 34) are separate rows,
matching A30's NON-MATCH-C14. E-10 and C-15 correctly remain their own rows
(SEM-03/SEM-04 canonicals A-13/A-21 are outside every final set). No
invented, dropped, renamed, or double-counted ID. All per-row A30 rank
citations spot-checked against COMPARE.json's rank_delta_table across all 39
rows: no discrepancy found.

## Check 3 — Class vocabulary and distribution recount: PASS

Both direction fields in all 39 rows use only the four controlled classes
(direct leverage / adjacent leverage / speculative transfer / negative
interference), each with a parenthetical mechanism summary. My own recount
from the rows' direction pairs: direct 1 (D-02 fwd); adjacent 8 (D-02 rev +
forwards of D-01, A-14, A-10, C-05, D-09, E-04, F-06); negative interference
4 (D-10 both; C-07 rev; CN-03 rev); speculative fills the remainder. Overall
classes implied by the pairs and by ALIGNMENT.md §3's rubric: STRONG 1
(D-02), MEDIUM 7 (D-01, A-14, A-10, C-05, D-09, E-04, F-06), WEAK 30 (the §4
member list — I counted all 30 names against the rows), ADVERSE 1 (D-10).
1+7+30+1 = 39. Matches the claimed 1/7/30/1 exactly; IMPACT_MAP's "~79%
untouched" = 31/39 checks out. ADVERSE is reserved for idea-specific
interference per the rubric; C-07/CN-03 correctly stay WEAK with
opportunity-cost-only negative reverse cells.

## Check 4 — Evidence-chain spot-checks (11 rows): PASS

Rows checked: D-02 (STRONG), D-10 (ADVERSE), A-10, D-09, C-05, F-06, E-04
(MEDIUMs), C-01, C-13, E-10, C-08/F-19 (WEAKs). Every cited Cxx exists in
PHD_FACTS.json with the status the row relies on; every EVxx/Pxxxx/G/M/BT ID
exists in EVIDENCE_MAP.csv or GAPS.md and supports the stated point:

- **D-02**: C01/C03/C13/C46 all `demonstrated` in B10; the calibration
  credential correctly labeled proposed-only (C06 `proposed`, gated by C04
  `demonstrated` anomaly — the dependency cell says so). EV01 (single
  traceable-budget exemplar, P0008 template), EV35/G3/M3 (tesla-scale +
  traceable + harsh combination absent) support "under-published niche"
  exactly. Dependency cell honestly lists array instrumentation, LN2
  practice, and lock-in thermography as NOT in B10's demonstrated ledger. The
  direct-leverage call rests on demonstrated assets (readout chain,
  packaging) mapping onto the core sensing head, with the proposed leg
  bounded — defensible and falsifiable as stated.
- **D-10**: C33/C34/C49 all `demonstrated`; A30:D10-DIS-01..03 match
  COMPARE.json's verified register verbatim (JLWS awards 2026-07-09; nLIGHT
  proprietary vertically-integrated CBC; Navy JBCS from Q4-2026). The row
  explicitly rejects the "control/estimation" thematic chain and discloses
  B15's lack of photonic coverage as corpus distance, not field evidence.
  ADVERSE is mechanism-based (classification vs open-publication gates;
  A30-verified window collision), not theme-based.
- **A-10**: C46/C01/C03/C13 `demonstrated` and genuinely on-point (in-plasma
  packaging with graphite shield; EMI-disciplined readout); the closed-loop
  engine correctly attributed to proposed C23/C31 with pre-redteam C40, and
  new06 D08 §14's contrary claim corrected (see Check 5). S-B20-03 supports
  the measurement-only-incumbent point (my own re-open confirms). Mechanism
  is concrete (survivability + signal integrity), not "both do plasma" — the
  row itself says removing the plasma theme leaves the mechanism standing.
- **D-09**: C06 `proposed` mapped to a core element and accordingly classed
  adjacent-forward/MEDIUM-boundary per the rubric — no proposed-as-
  demonstrated inflation. I opened old06's P3R2-D-09 evidence record: NCI
  SBIR Contract Topic 461 with mandatory NIST traceability and 5% tolerance,
  instance expired (2023, disclosed in the row), and the two independent 2025
  Medical Physics BCT charge-buildup papers all appear in the record as the
  row states; "market is small and instrument-vendor-shaped" is the record's
  own wording, carried honestly.
- **C-05**: C06 `proposed` → adjacent-forward, correct; EV01/EV35 support
  scarcity; A30:C05-DIS-01/02 match the verified register; the OCP negative
  claim correctly kept at discovery level per A30's unresolved issue.
- **F-06/E-04/C-01/C-13/E-10/C-08/F-19**: statuses correct throughout
  (C14 `proposed` labeled proposed in E-04; C42/C46 `demonstrated`; C29
  `unknown` used as Unknown; C27's persistent-mode veto used as documented).
  E-10 is an explicit vocabulary-trap test-and-reject with the one genuine
  (reverse, unplanned) channel tied to BT-5/M1 — exactly the anti-thematic
  discipline the stage demands. F-19/D-19/G-03 rows match their canonical
  SELECTION.json entries verbatim (I opened all three entries).

No fabricated citation, count, or status misuse found. No row claims
causation from thematic similarity; six rows explicitly test and reject such
chains.

## Check 5 — Founder-fit corrections (5): ALL JUSTIFIED

I opened each cited new06 passage and adjudicated against B10's ledger:

1. **D01 §14 (D-02)** — new06: "Hall-array magnetic sensing, lock-in thermal
   imaging, line-speed data acquisition, and calibrated reporting are the
   founder's core... skills." B10 demonstrates a single-channel readout chain
   (C03/C13) and one packaging execution (C46); no array instrumentation, no
   thermography, no line-speed DAQ; calibration proposed-only (C06/C15).
   Correction justified.
2. **D02 §14 (C-01)** — new06: "instrumentation and power-electronics
   engineering, the founder's core stack." No power-electronics hardware
   anywhere in B10's demonstrated ledger. Justified.
3. **D03 line 93 (C-05)** — new06: kW-class TTV calorimetric energy balance is
   "a controls-and-DAQ problem squarely in the founder's stack." Bench DAQ is
   demonstrated (C03/C13); multi-kW calorimetric/thermal metrology and
   controls are not (controls proposed, C23/C31). Justified.
4. **D04 line 89 + §14 (D-10)** — new06: "the founder's home ground";
   "deterministic FPGA control loops, electro-optic drive electronics,
   interferometric metrology... the founder's core stack." None of these
   appear in B10's demonstrated ledger. Justified (pilot-carried).
5. **D08 §14 (A-10)** — new06: "system identification and deterministic
   closed-loop control are the founder's core." Both are proposed Opt2
   elements (C23/C31), pre-redteam (C40), not demonstrated. Justified.

## Check 6 — IMPACT_MAP counterfactuals and the ~8-of-39 claim: PASS

Counterfactuals present for the STRONG idea (§3, with/without Opt2, class
consequence stated), the ADVERSE idea (§5, zero-delta control), a MEDIUM
representative (§4), both mechanism clusters covering all seven MEDIUMs
(§6 traceability: C-05/D-09/F-06/G-03/C-22; §7 demonstrated-asset:
A-10/A-14/E-04), and the portfolio (§8, both branches with a stated
distribution shift). "~8 of 39" = the 1 STRONG + 7 MEDIUM significant-
coupling set — consistent with the rows; the Opt2-sensitive subset (D-02,
C-05, D-09, D-01, F-06) matches the rows' dependency/direction cells (see
minor defect 3 on F-06's cell placement). §8's without-Opt2 distribution
(~0/~5/~33/1) is hedged and arithmetically coherent with the stated slips.

## Check 7 — SOURCES.csv honesty: PASS

Exact 10 columns. S-B20-01/02 disclosed as pilot-carried (same run date
2026-07-28) with claims reused verbatim — confirmed against the pilot's
SOURCES.csv, including the pilot's disclosed failed opens (password-protected
TAPESTAR datasheet, two 404s), which the full run repeats rather than hides.
**S-B20-03 re-opened by me this run (2026-07-28): OPENED OK.** The Impedans
Semion page measures ion flux and IED at substrate level in real time, is
positioned exclusively as a measurement/analysis instrument with no
closed-loop or bias-waveform control capability mentioned, self-describes as
"the industry standard for substrate level measurement of the ion energy
distribution," and claims 100+ publications — matching the candidate's row
verbatim, including its own caveat that a vendor page cannot prove a
market-wide negative. Limitation fields honestly scope what each source does
NOT verify.

## Check 8 — Honesty, labels, consistency: PASS

- Record-depth stratification disclosed and true: the 7 canonical-entry-only
  NEW24 far-domain ideas' old06 evidence files all exist (Glob-confirmed) and
  their rows say "exists, not read"; the three entries I opened (F-19, D-19,
  G-03) match their rows' names/mechanisms exactly; G-03's row names its own
  upgrade path; CN-03's thinnest-record disclosure is accurate (screening
  JSON only).
- No pilot labels anywhere in the six output files (all Mode: FULL); pilot
  references are provenance-only. The pilot itself carries the required
  PILOT SAMPLE label — continuity confirmed; the six pilot analyses are
  carried substantively unchanged with changes disclosed in ALIGNMENT.md §9
  (A-14's closed read-gap confirmed: old06 DD line 37 reads verbatim
  "Packaging is the gating technical asset").
- NOT_EXPOSED discipline correct in RUN_META; requested vs observed kept
  separate.
- SELF_CHECK's recounts are reproducible: I independently confirmed the row
  count, the 41-ID reconciliation, the 1/7/30/1 distribution, the
  direction-class usage, and cross-file agreement among CSV, ALIGNMENT.md,
  and IMPACT_MAP. Corpus-dated market facts are labeled in-cell; F-19's
  A30-flagged unverified reversal is carried with the flag.
- No ranking performed; kill rules quoted, not adopted.

## Defects

1. **Minor** — ID-namespace collision on "G5". The CSV legend defines
   G1–G6 as B15 GAPS items, but the D-10 row's mechanism cell and
   ALIGNMENT.md §7 use "G5 (accepted paper needed; C49 records zero)" to mean
   B10's roadmap gate G5 (C38), not B15's G5 (Hall-vs-TMR tension). The
   underlying claim is accurate and the parenthetical makes the referent
   recoverable, so no factual error — but a downstream consumer resolving IDs
   strictly by the legend would mis-resolve it. Affected files:
   `ALIGNMENT.csv` (D-10 row), `ALIGNMENT.md` §7. Acceptance test: label the
   gate as C38-G5 (or "B10 roadmap gate G5") or cite C38 directly.
2. **Minor** — loose status shorthand. The C-01 and E-14 rows describe
   "estimator methodology C23/C31" as "proposed-only"; B10 lists C23 as
   `inferred` (C31 is `proposed`). The direction of the caveat is
   conservative (nothing not-demonstrated is upgraded), so no overstatement —
   but the shorthand blurs B10's status vocabulary. Affected file:
   `ALIGNMENT.csv` (C-01, E-14 rows). Acceptance test: statuses quoted per
   claim ID match PHD_FACTS.json vocabulary.
3. **Minor** — F-06's Opt2 sensitivity is stated in its direction/mechanism
   cells and in IMPACT_MAP §6, but its `dependency` cell says "No PhD-side
   gate," so the Opt2-sensitive cluster is not fully recoverable from
   dependency cells alone. Document-level consistency is preserved. Affected
   files: `ALIGNMENT.csv` (F-06 row), `IMPACT_MAP.md` §6. Acceptance test:
   dependency cell mentions the C06/WP-C condition its forward class rides on.

No critical or major defects found.

## Limitations of this verification

- I re-opened one of the three web sources (S-B20-03) live; S-B20-01/02 were
  accepted on the pilot ledger's same-date record rather than re-fetched —
  their claims are incumbent-class/buyer-class facts of low volatility, and
  the A30-verified registers I relied on were re-checked against COMPARE.json
  text, not re-fetched from the web.
- Field counts for all 39 CSV rows were verified by careful visual walk, not
  by executing a parser (native execution contract prohibits code).
- Spot-check depth: 11 rows fully chain-verified, all 39 verified for ID
  membership, rank citations, direction vocabulary, and class assignment;
  corpus record reads verified by sample (D-09 record, A-14 deep dive, five
  new06 founder-fit passages, three SELECTION.json entries, two Glob
  existence sweeps), not by re-reading every cited record end-to-end.
- Observed model/effort for the worker and for me rest on self-declaration
  and NOT_EXPOSED respectively; neither is treated as proof.

VERDICT: PASS
