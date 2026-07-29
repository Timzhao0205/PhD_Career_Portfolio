# Independent verification report — B15_lit_synth FULL attempt-1

- Verifier: `pap06-verifier` (fresh, independent; did not produce the candidate)
- Requested verifier model/effort: Fable 5 / xhigh. Observed runtime identity:
  the session self-identifies as Fable 5 (model id `claude-fable-5`); no
  independent effort string was exposed. Requested and observed evidence kept
  separate; self-identification is not treated as independent proof.
- Date of verification and of all live web checks: 2026-07-28
- Candidate verified (read-only): `outputs/B15_lit_synth/attempt-1/`
  (`EVIDENCE_MAP.csv`, `LIT_REVIEW.md`, `GAPS.md`, `SOURCE_AUDIT.json`,
  `SOURCES.csv`, `RUN_META.md`, `SELF_CHECK.md`)
- Inputs read: `state/CURRENT_VERIFY.md`, `workflow/stages/B15_lit_synth.md`,
  `.claude/skills/pap06-native/references/ACCEPTANCE.md`, `LIT_POLICY.md`,
  `SOURCE_POLICY.md`, `MODEL_POLICY.md`,
  `outputs/B12_lit_search/attempt-1/PAPER_LEDGER.csv` (full read, all 62 rows),
  `verification/B12_lit_search/FULL_attempt-1.md`,
  `pilot/B15_lit_synth/attempt-1/EVIDENCE_MAP.csv` and `SOURCES.csv`,
  `outputs/B10_phd/attempt-1/PHD_FACTS.json` (claim IDs plus content reads of
  every load-bearing cited claim), `.claude/agents/pap06-fable-xhigh.md`.
- All counts below are my own recounts; all live-source results are pages I
  opened myself via WebFetch during this verification (16 fetches, 15 distinct
  paper records). I edited nothing; this report is the only file I wrote.

## 1. Files, structure, schemas (gate 1)

- All seven required files present and non-empty in the target directory.
- `EVIDENCE_MAP.csv`: header is the exact 15-column spec schema in spec order
  (evidence_id...falsifier). 35 data rows, EV01-EV35, sequential, gap-free, no
  repeats; quoting well-formed on full read; paper_ids semicolon-separated
  everywhere. PASS.
- `SOURCE_AUDIT.json`: valid JSON on full read; all 13 spec-required fields
  present; one extra disclosed top-level key (`scope`), same convention as the
  accepted pilot. `duplicate_dois` is an empty array rather than numeric 0 — a
  disclosed format choice conveying the same fact. PASS.
- `SOURCES.csv`: header exactly
  claim_id,url,title,publisher,published_date,accessed_date,source_type,
  stage_file,confidence,limitation; 14 rows S01-S14. PASS.

## 2. Evidence-map recounts (gate 2)

- Total rows: **35** (EV01-EV35) >= 30. PASS.
- Rows per stream (my tally): hall_metrology **9** (EV01, EV02, EV09,
  EV11-EV15, EV35); hybrid_diagnostics **10** (EV03, EV04, EV10, EV16-EV20,
  EV32, EV33); hts_quench_current **8** (EV05, EV06, EV21-EV26);
  power_conversion **8** (EV07, EV08, EV27-EV31, EV34). 9+10+8+8 = 35.
  Matches claimed 9/10/8/8. PASS.
- Distinct paper IDs cited across all paper_ids fields (my own parse of every
  semicolon list in all 35 rows): **62 distinct IDs, P0001-P0062, every ledger
  paper cited at least once** >= 48. Grouped by B12 ledger topic_stream:
  hall **13**, hybrid **14**, hts **17**, power **18** — matches claimed
  13/14/17/18; every stream >= 8. I also spot-verified SELF_CHECK §3's
  per-paper row attributions (e.g. P0008 in EV01/09/13/14/35, P0050 in
  EV27/28/32/34, P0031 in EV04/18/32/34) — all correct. PASS.

## 3. Referential integrity (gate 3)

- Every paper_id in EVIDENCE_MAP.csv and every P-ID citation in LIT_REVIEW.md
  and GAPS.md is in P0001-P0062 and resolves to a real ledger row (checked
  against my full ledger read). No out-of-range or phantom ID. PASS.
- Every EVxx citation in LIT_REVIEW/GAPS resolves to EV01-EV35. PASS.
- B10 cross-references: PHD_FACTS.json contains exactly C01-C50; every cited
  Cxx (C01, C03, C04, C06-C10, C20, C23, C26-C31, C43, C44, C46, C47, C49,
  C50) exists. I content-read C01, C03, C04, C05, C06, C07, C08, C09, C10,
  C23, C24, C25, C26, C27, C28, C29, C30, C31, C43, C44, C45, C46, C47, C49,
  C50: the candidate's characterizations are faithful (e.g. C06 WP-C
  u(k)/k <= 2% target; C23 Theorem-1 two-parameter non-identifiability; C26
  gaps (a)-(d) incl. the single non-fusion reverse-direction precedent; C27
  FOCS/Rogowski total-current counterexample and persistent-mode SC-magnet
  veto; C29 GaN radiation Unknown with the ~14x cross-species failure; C43
  TMR as sharpest single-channel competitor; C44 forbidden
  "first fusion Hall diagnostic" claim; C47 stellarator-reconstruction
  fallback). FT-xx references resolve to B10's FT-01..FT-12 ladder (C25).
  The §4 citation of C50 as "skill separation" is a loose but defensible
  mapping (C50 separates AI-produced work products from the researcher's own
  demonstrated skills); noted as an observation, not a defect. PASS.

## 4. SOURCE_AUDIT.json vs my own B12 ledger recount (gate 4)

My independent recount of all 62 ledger rows:

- ledger_rows 62 = my count (P0001-P0062, sequential, gap-free). PASS.
- accepted_core_count 62 = my count (every row `accepted_core`). PASS.
- peer_review_verified_count 62 = my count (every row `verified`); the
  candidate's limitations honestly scope its independent re-confirmation to
  the 39 opened rows. PASS.
- journal_count 62 = my count (52 journal_article + 10 review_article —
  P0005, P0006, P0010, P0015, P0017, P0046, P0052, P0053, P0054, P0057 —
  all journal-published). PASS.
- recent_2020_2026_count **43** = my own year-column recount: hall 7 (P0004,
  P0008, P0010, P0011, P0012, P0015, P0018), hybrid 10 (P0001, P0003, P0021,
  P0022, P0024, P0025, P0028, P0029, P0030, P0031), hts 11 (P0002, P0032,
  P0033, P0034, P0036, P0037, P0038, P0039, P0040, P0043, P0046), power 15
  (P0005, P0006, P0047-P0055, P0058-P0061). 7+10+11+15 = 43, confirming the
  B12 verifier's corrected figure (incl. P0043, 2022) over B12's stated 42.
  Candidate's per-stream split matches mine exactly. PASS.
- topic_counts 13/14/17/18 = my per-row tally (hall: P0004, P0008,
  P0009-P0019; hybrid: P0001, P0003, P0020-P0031; hts: P0002, P0007,
  P0032-P0046; power: P0005, P0006, P0047-P0062), sum 62. PASS.
- duplicate_dois: none found on my scan of all 62 DOI cells (all distinct,
  incl. the near-neighbor MDPI strings); consistent with the B12 verifier's
  manual comparison. PASS.
- correction_concern_count 1 = my count (only P0012 carries a correction
  notice — Nat Commun 12:554, 2021 — verified live by the B12 verifier);
  retracted_count 0, inaccessible_count 0, unresolved_count 0 = my counts
  (every row "none found" / opened-record status). PASS.
- accepted_paper_ids: set-compared — exactly the 62 ledger IDs P0001-P0062,
  no extras, no gaps. PASS.

## 5. Retracted/unresolved-support rule and P0012 handling (gate 5)

All 62 corpus papers are accepted_core with zero retractions, so the rule
reduces to P0012's disclosed correction. My check: P0012 appears in exactly
one evidence row (EV11), used at metadata level for platform coverage with no
quantitative figure drawn from it; the correction is disclosed in
SOURCE_AUDIT.json limitations and LIT_REVIEW §8, correctly distinguished from
a retraction per LIT_POLICY. No claim row is supported by any retracted or
unresolved item. PASS.

## 6. Quantitative fidelity — my live spot-checks (gate 6, critical)

I opened 15 distinct paper records live and checked 12 evidence rows,
covering all three pilot-carried priority rows (EV01-EV03) and eight
full-run rows that cite papers no earlier chain layer had opened
(P0010, P0017, P0018, P0024, P0030, P0038, P0040, P0043, P0048, P0050,
P0056), plus the paywalled P0007.

| Row | Record(s) I opened | Result |
|---|---|---|
| EV01 | P0008 (jsss.copernicus.org) | Exact: FH55 reference probe, ±150 mT range, 3.2 mV/A/T ± 0.3%, ±(7 mT + 13%) k=2, five-component budget, graphene 9.3% day-to-day. Faithful. |
| EV02 | P0001 (IOP ac8aad), P0004 (IOP ae6c59), P0017 (PMC3274123) | P0001: 2009-2021, 19117 pulses, ~1e13 cm-2 s-1 D-T flux, 2e18 cm-2 stability, ±0.07% scatter, coils not bench-calibrated, ~19% pulses lost — all verbatim-class matches. P0004: 89.6 mV/A/T, 500 nm W-Ti 90-10, 350C/50h + 220C/120h, ±2.5 T, 1.4e20 cm-2 at ≤2.3% — faithful; my check confirms the fluence datum is cited from earlier/ongoing group work, exactly as the candidate's limitations hedge states. P0017: -270 to +300 C, TC < 0.04%/K — faithful. |
| EV03 | P0003 (IOP adb599), P0001 | P0003: synthetic-only validation, σ_H = 0.1 T and σ_C = 0.02 T/s as printed ("extreme scenarios"), 10 kHz, 10 s + 1 h records, ~30x SNR, Wiener bias, hardware challenges acknowledged; P0001: 18 Hall + 18 coils, hybrid probe proposed not built. Faithful; strength "moderate" correctly withholds hardware status. |
| EV05/EV21 | P0043 (PMC9652021), P0040 (PMC8127627), P0007 (IOP 045007) | P0043: 655 turns, ~4.2 K, quench at 350 A (100-300 A decayed cleanly) in ~450 ms, 1.92 mΩ shunt eliminates quench, τ 4.37→15.28 s, stress 428→115 MPa, experiment + FE — all faithful. P0040: 125 A, semi-adiabatic, NZP 82 μm/s, 1 K margin, model "acceptably matched" — faithful. P0007: 70 μΩ·cm², 12 J/40 ms at 80 A, 115 A turn overcurrent, ~145 K, recovery, detection-difficulty statement all present in the article content my fetch retrieved. Simulation-vs-experiment provenance correctly separated throughout. |
| EV06 | P0038 (IOP adb0dd) | EAST CS/PF, CNN+LSTM, 1000 training / 2000 test shots, >50% noise cut, >2 V → <0.5 V, 500 mV/1 s threshold, residual may still exceed 100 mV and authors flag inadequacy for HTS, LTS magnets with simulated quench events — all verbatim-class matches, incl. the candidate's own caveat wording. |
| EV11 | P0010 (IOP abf7e2) | Best graphene 0.03-0.05 μT/√Hz, InSb film 0.08, GaAs/AlGaAs and Si ~1 μT/√Hz, gate-instability open challenge, review compiling primaries — figures faithful. Platform label caveat: my extraction attributes the 0.03 record device to CVD-on-SiO2/hBN-passivated, not "CVD-on-SiC" as the row states (see defect 2). |
| EV13 | P0017, P0008, P0010 | AlGaN/GaN 2DEG mobility ~1000 → ~300 cm2/Vs at 300 C and the no-published-data statement confirmed verbatim in P0017; 2011-staleness correctly disclosed by the candidate. Faithful. |
| EV15 | P0018 (PMC7412317) | TCAD-only (Sentaurus), no experimental validation, 50 nm film, +28.9% Hall voltage / +29.1% sensitivity (86.49→111.75 mV/T) at 1e16 cm-2, dose rates 5e8-5e12 rad(Si)/s, LET 0-100, "most published studies focus on III-V" — all faithful; simulation status correctly weighted. |
| EV16 | P0030 (PMC9329379) | 1.9e-3 at 60 sensors, 4.1e-2 at 18 sensors under σ=1e-2 noise, beats multipole expansion, Bartington triple-axis lab validation, nEDM context, uniqueness caveat — all faithful. |
| EV19 | P0024 (PMC7288339) | 724 probes / 1088 signals, fraction-of-1% target via 0.1%-class elements, ~0.6 mT integrator error over 10 s for 10 mT-0.5 T, inductive-only design, ~10 s pulses, bench/prototype validation — all faithful; the "mixed" direction and regime caveat are well calibrated. |
| EV27 | P0048 (PMC10221569), P0056 (PMC6806593), P0050 (PMC10386427, two targeted opens) | P0048: ~100 MHz, 4% max error at 50 A, ~$20, >5 kV insulation, CT-based AC-only with saturation/reset — faithful. P0056: 84 turns, ~6.1 nH, linear 10 Hz-1 MHz, resonance >110 MHz, tested to 400 A, distortion at 550 A ("above ~500 A" is fair) — faithful. P0050: the no-single-method conclusion is verbatim-confirmed; BUT the "~50 MHz minimum bandwidth" and "10-15 kV" figures did not surface in either of my two targeted opens of P0050 — both appear verbatim in P0048 ("required bandwidth should be above 50 MHz"; "higher operating voltage 10~15 kV for WBG devices") — see defect 1. |
| EV28 | P0050 | Hall "response speeds way lower than 100 kHz" + temperature-drift compensation, TMR low-pass filtered "usually less than 50 kHz" near switching nodes, multi-scheme combination named as way forward — all verbatim-class matches. |

Calibration of strength/direction labels: no simulation-only work is
presented as demonstrated hardware anywhere I checked (P0003, P0007, P0018,
P0032 all correctly tagged); review-level figures are consistently separated
from primary measurements (EV07, EV08, EV11, EV25, EV27/28); gap rows carry
"not applicable" strength and corpus-bounded wording. No overstated
evidence-strength grade found; several grades are conservative (e.g. EV05's
single-lineage caveat despite experimental corroboration). PASS (with the
two minor attribution/descriptor defects below).

## 7. The two disclosed B12 typing adjudications (gate 7)

- **P0017** (B12: review_article): my own live open of PMC3274123 shows a
  primary research article — the authors fabricate, anneal-stabilize, and
  characterize their own InSb sensors, with original experimental results and
  the conclusion "the first complete ETHS has been manufactured". **B15 is
  right.**
- **P0050** (B12: journal_article, i.e. primary): my own live open of
  PMC10386427 shows a review/survey ("A study of existing single-scheme (SS)
  current sensors' performance is presented...") with no original experiment
  as its main contribution. **B15 is right.**
- Presentation: both are recorded in LIT_REVIEW §1.3 and SOURCES.csv S02/S13
  as B15's own adjudication judgments with disclosed extraction-layer
  provenance; the B12 ledger file itself is untouched (my full read confirms
  it still carries B12's original classifications; neither classification
  affects stream counts, journal_count, or accepted status). PASS.

## 8. LIT_REVIEW / GAPS coverage (gate 8)

- (a) PhD-established vs literature-suggested: LIT_REVIEW §3, with resolving
  C-refs on both sides and the double-edged silence point made explicitly. PASS.
- (b) Transferable vs enabling vs loose analogy: §4, three-tier triage with
  corpus citations. PASS.
- (c) Hybrid architecture, both directions: §5 supports the Hall→coil
  direction (P0003/P0001/P0024/P0031/P0050) while explicitly finding the
  reverse coil→Hall direction unsupported across all 62 papers (EV32), with
  P0001's uncalibrated-coils point and B10 C23's structural explanation;
  contradictions/cautions (coil-only incumbent practice, TMR) included. The
  reverse direction is treated as unsupported per the corpus, exactly as
  required. PASS.
- (d) Power-conversion benefit analysis: §6, four-tier judgment incl. an
  explicit "not a genuine beneficiary" tier. PASS.
- (e) Established / plausible inference / unknown: separated per stream (§2)
  and in summary (§7); map rows carry falsifiers. PASS.
- GAPS.md: contradictions G1-G6, missing experiments M1-M7, weak regimes,
  novelty uncertainties keyed to C26 gaps (a)-(d), and prioritized bridge
  tests BT-1..BT-8 with a stated ranking criterion, each grounded in specific
  corpus rows and mapped to B10's FT ladder; corpus-boundedness restated in
  §6. The specific figures reused in GAPS (0.6 mT/10 s; ≥350 A/~450 ms;
  70/27 μΩ·cm²) match the records I opened. PASS.

## 9. Honesty, disclosures, consistency (gate 9)

- 23-never-opened disclosure: my own reconstruction — pilot opened P0001-P0008
  (verified from pilot SOURCES.csv S01-S08); B12 verifier live-checked 20 rows
  (verified from the B12 verification report's table; list matches the
  candidate's exactly); this run opened 14 (SOURCES.csv S01-S14 = RUN_META's
  14-fetch log, one-to-one, no overlap with earlier layers). Union
  8 + 17 + 14 = **39**; complement = **23**, and my computed complement set
  equals the candidate's 23-row list exactly (identical in LIT_REVIEW §1.2,
  SOURCE_AUDIT limitations, and RUN_META). No quantitative figure in the map
  is sourced to a never-opened row (checked row by row; metadata-level rows
  EV12, EV17, EV18, EV20, EV24, EV29, EV30, EV31 deliberately omit
  quantitative claims and say so). Honest and consistent. PASS.
- No pilot labels: no "PILOT SAMPLE"/"NOT FINAL" string in any of the seven
  candidate files; references to "the accepted pilot" are provenance
  descriptions. PASS.
- Pilot continuity: EV01-EV10 carried with IDs and substance intact;
  strengthenings (EV02 +P0017, EV04 +P0031, EV05 +P0040/42/43, EV06 +P0038,
  EV07 +P0052/54/57, EV08 +P0053, EV09 +P0018/19) are disclosed in SELF_CHECK
  §2; no pilot adjudication reversed (my side-by-side read). PASS.
- Model/effort record: RUN_META names `pap06-fable-xhigh`, requested
  Fable 5 / xhigh (matching the route and the agent frontmatter
  `model: fable`, `effort: xhigh`); observed effort `NOT_EXPOSED`, model
  self-identification reported but explicitly not treated as proof. Treated
  here as missing observation — not a mismatch, not proof. PASS.
- SELF_CHECK recounts: I reproduced every recount it asserts (rows, streams,
  62-paper usage, audit numbers, 39/23 partition, recency 43); all correct.
  Web log consistent with SOURCES.csv; corrected recency figure used
  consistently; no budget/limit stop claimed. PASS.

## Defects

1. **Minor — misattributed source for two quantitative requirement figures
   (EV27; LIT_REVIEW §2.4 and §6; GAPS.md G5/M6 phrasing "P0050 sets the
   requirements").** The "minimum bandwidth ~50 MHz" requirement and the
   "10-15 kV" WBG voltage/isolation context are attributed to P0050
   (review); my two targeted live opens of P0050 did not surface either
   (its "50 MHz" occurrences are a probe-spec caption; no 10/15 kV mention),
   while both statements appear verbatim in P0048 — which the same evidence
   row also cites, and whose own figures verify exactly. The figures are
   real, in-corpus, and not overstated; the defect is prose-level source
   attribution within a correctly-cited row (it also slightly mislabels a
   primary paper's requirement statement as review-synthesis). Affected
   files: `outputs/B15_lit_synth/attempt-1/EVIDENCE_MAP.csv` (EV27 claim and
   conditions), `LIT_REVIEW.md` §2.4/§6, `GAPS.md` G5/M6. Acceptance test on
   repair: each quantitative requirement figure is attributed to the paper
   whose record contains it. (Residual possibility that P0050's full text
   contains a 50 MHz statement my extractions missed is acknowledged; the
   candidate's own extraction-risk disclosure covers the same layer.)
2. **Minor — platform descriptor in EV11.** The 0.03-0.05 μT/√Hz record
   graphene devices are labeled "(CVD-on-SiC and hBN-encapsulated)"; my live
   open of P0010 attributes the 0.03 record to CVD graphene on SiO2
   (hBN-passivated) and 0.05 to hBN-encapsulated exfoliated graphene. The
   numeric range, the InSb/GaAs/Si comparators, and the review-level
   weighting are all faithful; only the substrate descriptor is doubtful
   (extraction uncertainty on both sides). Affected file: EVIDENCE_MAP.csv
   (EV11). Acceptance test on repair: platform labels match P0010's table.
3. **Minor — presentational stream-listing inconsistency.** LIT_REVIEW §2.2's
   heading lists EV34 among the hybrid_diagnostics rows ("EV32-EV34") while
   EVIDENCE_MAP assigns EV34 to power_conversion (§2.4 also lists it). The
   heading's paper-count claim ("14 papers, all cited") remains true and the
   map/SELF_CHECK counts are correct; this is a heading-level ambiguity only.
   Affected file: LIT_REVIEW.md §2.2. Acceptance test on repair: section
   headings list only rows assigned to that stream (or say "rows citing this
   stream's papers").

No critical defects. No major defects. None of the three touches a hard
gate: all counts, IDs, source mappings, and quantitative figures verify; the
two content defects concern attribution/labeling of figures that are genuine
and faithfully quoted from papers cited in the same evidence rows.

## Limitations

- I live-checked 15 of the 39 opened records (all high-load rows and both
  typing adjudications); the remaining opened records (e.g. P0032, P0033,
  P0046) were verified through the candidate's logged opens plus B12/B12-
  verifier layers, not re-opened by me. The 23 never-opened rows carry no
  quantitative load by design and were not opened by me either.
- WebFetch summarization is itself an extraction layer; defects 1-2 rest on
  targeted extractions that could in principle miss text, which I have
  disclosed inline where it matters.
- No second-source retraction screening (Retraction Watch/Crossref) was
  performed by me — the same disclosed limitation as every earlier layer.
- Observed worker model/effort is `NOT_EXPOSED` beyond self-identification;
  requested route intent verified from the agent frontmatter; no observation
  contradicts it.

VERDICT: PASS
