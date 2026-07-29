# LIT_REVIEW — B15_lit_synth (FULL)

Stage: `B15_lit_synth` | Mode: `FULL` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Scope: independent Fable-level synthesis and evidence adjudication over the
full accepted B12 corpus (62 verified peer-reviewed papers, P0001-P0062),
read against the B10 PhD claim ledger (C01-C50). Every paper-ID citation
below resolves to `outputs/B12_lit_search/attempt-1/PAPER_LEDGER.csv`; every
EVxx citation resolves to this stage's `EVIDENCE_MAP.csv`; every Cxx citation
resolves to `outputs/B10_phd/attempt-1/PHD_FACTS.json`. This document
adjudicates evidence. It does not rank startup options (reserved for B40).
Absence of a topic from this 62-paper corpus is never treated as proof that
no such work exists anywhere.

## 1. Source audit and independent adjudication of B12

### 1.1 My own recounts of the entire ledger

- Ledger rows: **62** (P0001-P0062, sequential, no gaps). All 62 are
  `evidence_status = accepted_core`; zero supplement, zero unresolved.
- Per-stream (my row-by-row tally): hall_metrology **13**,
  hybrid_diagnostics **14**, hts_quench_current **17**, power_conversion
  **18**; sum 62. Matches B12's FLOW.json.
- 2020-2026 recency, accepted-core only (my own year-column recount):
  **43** (hall 7, hybrid 10, hts 11, power 15). This confirms the B12
  verifier's corrected figure of 43, not B12's stated 42 — B12 omitted
  P0043 (2022) from its hts tally.
- Duplicate DOIs: **0** (all 62 normalized DOIs distinct on my scan of the
  full ledger; consistent with the B12 verifier's manual comparison).
- Corrections: **1** — P0012 carries a disclosed published correction
  (Nat Commun 12:554, 2021); a correction is not a retraction and does not
  bar acceptance under LIT_POLICY. Retractions: **0** found on any record
  opened by the pilot, the B12 verifier, or this run. Inaccessible: **0**
  (every row has an opened publisher page or PMC mirror; P0007's full text
  is paywalled but its record is open — disclosed, not counted
  inaccessible). Unresolved: **0**.

### 1.2 Verification chain and this run's fresh spot-audit

Three independent layers now cover the corpus:

1. The accepted pilot re-opened **P0001-P0008** (8 rows) and confirmed all
   eight B12 classifications.
2. The B12 verifier live-checked **20 rows** (P0002, P0004, P0008, P0009,
   P0012, P0013, P0016, P0020, P0021, P0022, P0028, P0031, P0034, P0037,
   P0039, P0041, P0045, P0049, P0051, P0057) with zero fabricated or
   materially wrong rows found. Per the task card these are treated as
   verified; my fresh checks were focused elsewhere.
3. **This run opened 14 additional rows** — a risk-weighted sample of the
   papers this synthesis leans on for quantitative claims: P0010, P0017,
   P0018 (hall); P0024, P0030 (hybrid); P0032, P0033, P0038, P0040, P0043,
   P0046 (hts); P0048, P0050, P0056 (power). All 14 records matched the
   B12 ledger on title/authors/year/venue/DOI; no correction, expression
   of concern, or retraction notice was found on any of them. See
   SOURCES.csv (S01-S14).

Union of all three layers: **39 of 62 rows** (63%) have now been opened by
at least one independent check in this stage chain. The remaining 23 rows
(P0011, P0014, P0015, P0019, P0023, P0025, P0026, P0027, P0029, P0035,
P0036, P0042, P0044, P0047, P0052, P0053, P0054, P0055, P0058, P0059,
P0060, P0061, P0062) are used in this synthesis **only at ledger-metadata
level** (titles, venues, B12's relevance notes), never as sources of
quantitative figures. Every quantitative number in EVIDENCE_MAP.csv is
attributed to an opened record (pilot or this run) in that row's
limitations field.

### 1.3 Corrections to B12 classifications found this run

Two publication-type adjudications (neither affects accepted_core status,
stream counts, or the journal count, since both types are journal-published
peer-reviewed articles):

- **P0017** — B12 classified `review_article`. The opened PMC record shows
  a primary research article: it develops and characterizes a specific
  annealing-stabilized InSb/GaAs extreme-temperature Hall sensor
  (-270C to +300C, TC < 0.04%/K) and states the "first completely
  developed extreme-temperature Hall sensor" conclusion. It contains
  survey elements but its evidentiary weight here is as a **primary
  experiment**, and this synthesis treats it as such (EV02, EV13).
- **P0050** — B12 classified `journal_article`. The opened record is a
  **review** (a synthesis of current-sensing technologies and integration
  issues, no primary experiment). This synthesis treats its conclusions as
  review-level consensus, kept separate from primary evidence (EV27,
  EV28), per LIT_POLICY.

Both discrepancies rest on this run's automated WebFetch extraction of the
records; the extraction layer itself can err, so both are recorded as
adjudication judgments with disclosed provenance, not as proof of B12
error. All other spot-checked classifications were confirmed as recorded,
including the pilot's 8/8 confirmation.

## 2. Stream syntheses — established / plausible inference / unknown

### 2.1 hall_metrology (13 papers, all cited: EV01, EV02, EV09, EV11-EV15, EV35)

**Established (primary experiments):**
- Traceable Hall calibration with a real component-level uncertainty
  budget exists at room temperature and ±150 mT: 3.2 mV/A/T ± 0.3%
  against a traceably calibrated reference probe; full-system expanded
  uncertainty ±(7 mT + 13%), k=2 (P0008) [EV01].
- Harsh-environment Hall sensing is demonstrated in narrow-gap III-V
  materials: 11+ years of InSb probes on JET including D-T campaigns with
  ±0.07% calibration scatter (P0001); Sb sensors with W-Ti barriers stable
  through 350 C and reported neutron tolerance to 1.4e20 cm-2 at ≤2.3%
  sensitivity shift (P0004); annealed InSb thin films from -270 C to
  +300 C at TC < 0.04%/K (P0017) [EV02].
- The sensitivity/noise performance landscape is mature and occupied:
  best-in-class minimum detectable fields of 0.03-0.05 µT/√Hz (graphene),
  ~0.08 µT/√Hz (InSb film), ~1 µT/√Hz (GaAs 2DEG, Si CMOS) per the opened
  review P0010, with corpus primaries spanning 1996-2020 (P0009, P0012,
  P0014, P0016) [EV11].
- Radiation-effects methodology (TID/TDR/SET separation in TCAD; gamma
  campaigns) exists in adjacent systems — silicon FD-SOI simulation with
  quantified predicted shifts (P0018), gamma-irradiated MR sensors
  (P0019) [EV15].

**Plausible inference:** the P0008 calibration methodology transfers in
principle to fusion-relevant Hall sensors; temperature-drift engineering of
the kind demonstrated for InSb (P0017) is plausibly achievable for
AlGaN/GaN, whose high-temperature mobility degradation was already noted in
2011 with "insufficient published data" (P0017) [EV13].

**Unknown:** any GaN/AlGaN Hall-plate radiation dataset — absent from all
62 papers, exactly matching B10 C29's Unknown [EV09]; any traceable
uncertainty-budgeted calibration at tesla-scale/fusion conditions — the
corpus has the method (P0008) and the regime (P0001/P0004) but never
together [EV35].

### 2.2 hybrid_diagnostics (14 papers, all cited: EV03, EV04, EV10, EV16-EV20, EV32-EV34)

**Established:** Hall and coil channels co-deployed for 11+ years on JET
(P0001); Kalman fusion of the two channels removes integrator drift with
~30x SNR gain **on synthetic data** (P0003) [EV03]. Inverse reconstruction
from external magnetics is an established method family: seminal theory
(P0020), DIII-D practice (P0021), arc localization (P0025), and PINN field
mapping with quantified error-vs-sensor-count scaling (P0030) [EV16].
Sensor-array current measurement with engineered positional-error budgets
is a developed sub-field (P0022, P0023, P0026, P0027) [EV17]. A hardware
DC+AC fused current sensor exists outside fusion — TMR + current
transformer (P0031) [EV18]. Diagnostic-system design is a quantified
discipline: RFX-mod2's redesign targets fraction-of-1% accuracy via
0.1%-class element calibration and quantifies integrator drift at ~0.6 mT
over 10 s — and it is deliberately coil-only (P0024); Bayesian coil-set
design exists for WEST (P0028) [EV19]. FOCS current sensing was assessed
under JET D-T neutron conditions (P0029) [EV20].

**Plausible inference:** a built hybrid probe of the P0001-proposed class
would plausibly work; a P0003-class estimator would plausibly survive real
data at degraded performance; the long-pulse regime (where coil drift
accumulates for 1000 s) is the regime where a Hall channel plausibly earns
its place — P0024's coil-only choice on a 10 s machine does not refute
this, but it shows incumbent practice defaults to coils [EV19].

**Unknown / open:** no hardware demonstration of fused Hall+coil operation
under fusion conditions anywhere in the corpus [EV04]; the coil→Hall
reverse-calibration direction is unsupported across all 62 papers and both
domains [EV32]; no stellarator-specific Hall/coil work [EV33]; the
idealized-simulation vs real-installation validation gap remains unbridged
[EV10].

### 2.3 hts_quench_current (17 papers, all cited: EV05, EV06, EV21-EV26)

**Established (with provenance carefully separated):**
- NI self-protection is a real but **conditional** mechanism: simulation
  anchored to measured 70 µΩ·cm² contact resistivity (P0007), corroborated
  experimentally at 125 A/77 K with an analytical hot-spot model matching
  semi-adiabatic experiments (P0040), and bounded by a demonstrated fault
  mode — sudden discharge from ≥350 A at 4.2 K quenches a 655-turn NI coil
  in ~450 ms, preventable with an engineered 1.92 mΩ shunt (P0043; also
  P0037, P0041, P0042) [EV05, EV21].
- Quench detection is weak-signal-limited and an active multi-modal
  frontier: ≤9 mV native signatures (P0007); ML detection at 0.9861
  accuracy on augmented data degrading cross-geometry and in noise
  (P0002); EAST CNN-LSTM EMI compensation cutting noise >50% yet leaving
  >100 mV residual against a 500 mV/1 s threshold — explicitly flagged
  as inadequate for HTS (P0038); FBG strain-rate early warning of 1-2 s at
  tape level (P0033); microwave sensor-free detection proposed (P0039)
  [EV06, EV23].
- Current redistribution among parallel paths is the stream's unifying
  physics (P0034, P0035, P0044, P0045) [EV24]; open-source 3D FE quench
  simulation now exists (P0032, computational-only validation disclosed)
  [EV22].
- Review-level (kept separate): mechanical/screening-current stress
  dominates high-field reliability; the 45.5 T record's NI insert was
  damaged after quench; the review explicitly calls for real-time
  stress/strain monitoring and better quench detection (P0046) [EV25].

**Plausible inference:** an instrumentation niche exists in transient/
charging-phase HTS magnet monitoring, since every corpus detection method
fights the same weak-signal/EMI problem and P0046 names the monitoring gap
directly [EV25, EV26].

**Unknown:** whether any Hall-based or hybrid method can serve that niche —
no corpus paper tries [EV26]; NI protection scaling beyond lab coils
(P0043's own caveat) [EV21].

### 2.4 power_conversion (18 papers, all cited: EV07, EV08, EV27-EV31, EV34)

**Established (primaries):** high-bandwidth AC current sensing for WBG
switching exists as point solutions — a ~100 MHz, 4%-at-50 A, $20 CT
(P0048); PCB Rogowski coils linear 10 Hz-1 MHz with >110 MHz resonance,
tested to 400 A (P0056); integrated Rogowski for press-pack IGBTs (P0055)
[EV27]. MR-based DC-capable sensing is deployed-adjacent (P0060, P0061,
P0062) [EV28]. On-chip current sensing is entering GaN power ICs (P0047)
[EV29]. Specialized converters (electroporation pulse generation P0049;
EV multimodule DC-DC P0051) are application-driven engineering [EV30].
Device reliability work continues (P0058, P0059) [EV31].

**Established (review-level, kept separate):** the requirement synthesis —
≥50 MHz bandwidth for SiC switching, 10-15 kV isolation targets, and the
explicit conclusion that **no single sensing method provides size,
bandwidth, linearity, isolation, accuracy, and cost simultaneously**, with
multi-scheme fusion named as the way forward (P0050); WBG capability
consensus (P0005, P0006, P0052, P0054, P0057) and gate-drive burdens
(P0005, P0006, P0053) [EV07, EV08, EV27].

**Plausible inference:** the DC-capable half of the WBG current-measurement
problem — which CT/Rogowski solutions structurally cannot supply — is the
genuine skill-transfer target for the PhD's fused-channel methodology
[EV27, EV34].

**Unknown:** whether Hall beats TMR in a switching-EMI environment — no
head-to-head benchmark exists in the corpus; P0050 describes weaknesses on
both sides (Hall: <100 kHz typical response, drift; TMR: EMI-driven
<50 kHz filtering) [EV28].

## 3. (a) What the PhD has established vs what literature only suggests

**The PhD's own established artifacts (B10, demonstrated):** an in-vessel
AlGaN/GaN Hall module deployed at HSX with qualitative shot data (C01);
bench current-spinning readout validation with a >=130x offset suppression
and an unresolved ~109x anomaly (C03/C04); a demonstrated UHV packaging
process (C46); zero accepted publications (C49). Nothing in the 62-paper
corpus duplicates the HSX GaN deployment — and nothing validates its
quantitative worth either; the corpus keeps C44's constraint sharp: a
fusion-Hall lineage (InSb at JET, Sb for ITER/DEMO) long predates it
(P0001, P0004) [EV02].

**What the corpus supports (external evidence exists):**
- Radiation-hard Hall sensing feasibility — in other materials (P0001,
  P0004, P0017) [EV02].
- The Hall→coil drift-correction direction of the hybrid (P0003) [EV03].
- The calibration method template WP-C would emulate (P0008; procedure and
  algorithm literature P0011, P0015) [EV01, EV12].
- The estimator/reconstruction methodology direction, including B10's
  fallback direction C47 (P0020, P0021, P0030) [EV16].
- The failure-motivated need for drift-managed magnetics in long-pulse
  devices (P0024's quantified integrator drift; P0003's motivation)
  [EV19].

**What literature only suggests (no external demonstration):**
- That a GaN die can reach WP-C's targets (u(k)/k ≤ 2%, C06) — P0008 is a
  different material, field range, and environment [EV01, EV35].
- That a hybrid probe delivers its promised accuracy on a real machine —
  P0003 is synthetic; P0001's probe is a proposal [EV04, EV10].
- That the fused-channel methodology transfers profitably to WBG
  converters — the need is documented (P0050) but no Hall-based fused
  sensor has been demonstrated there [EV27, EV34].

**Where literature is silent exactly where the PhD is most exposed:**
GaN radiation-drift magnitude (C29) [EV09]; the coil→Hall reverse
direction (C23/C26 gap b) [EV32]; stellarator Hall/coil work (C26 gap d)
[EV33]. Silence preserves the claimed novelty gaps **and** withholds
external support from the PhD's assumptions. Both edges are real; neither
may be cited without the other.

## 4. (b) Directly transferable vs enabling infrastructure vs loose analogy

**Directly transferable (corpus names the need; PhD work addresses it):**
- Fused DC+AC current/field sensing methodology: the power-conversion
  corpus explicitly calls for multi-scheme fused sensing (P0050) and has a
  TMR+CT hardware precedent (P0031); the fusion corpus has the Kalman
  formulation (P0003). The PhD's Element-2 estimator work (C07, C08, C23)
  sits squarely on this convergence [EV27, EV32, EV34].
- Measurement-under-EMI discipline and calibration/uncertainty practice
  (C03's spinning readout, C06's planned GUM budgets) map onto the
  documented EMI-compensation struggles of quench detection (P0038) and
  WBG switching metrology (P0048, P0050) [EV23, EV27].

**Enabling infrastructure (available to the PhD, not differentiating):**
- Calibration algorithms/procedures (P0011, P0015) [EV12]; quantum-rooted
  traceability (P0013, P0008) [EV14]; open-source magnet-simulation tools
  (P0032) [EV22]; reconstruction methods (P0020, P0021, P0030) [EV16];
  array-design error budgets (P0022, P0023, P0026, P0027) [EV17].

**Loose skill analogy (shared vocabulary, different specialization):**
- WBG power-device engineering (P0052-P0054, P0058, P0059): GaN materials
  familiarity aids comprehension; converter topology/control and device
  reliability engineering are distinct disciplines the PhD does not
  evidence (consistent with B10's own skill separation, C50) [EV30, EV31].
- HTS magnet protection engineering (P0043's shunt design, P0046's
  mechanics): adjacent instrumentation opportunity, not a demonstrated PhD
  capability [EV21, EV25, EV26].

## 5. (c) Support and contradiction for the Hall/coil hybrid architecture

**Supports (direction 1 — Hall corrects coil):** P0003 demonstrates the
Kalman fusion benefit synthetically (~30x SNR, drift removal); P0001
documents the system-level pairing and proposes the compact hybrid probe;
P0024 quantifies the integrator-drift problem the Hall channel would fix
(0.6 mT over just 10 s — the long-pulse extrapolation is the argument);
the cross-domain convergence on fused DC+AC sensing (P0031, P0050) shows
the architecture class is independently reinvented where bandwidth spans
matter [EV03, EV19, EV34]. This direction is well supported — and
therefore not novel (26 years of prior art, B10 C26; corroborated here by
P0001's own proposal and 2025 Kalman papers in B12's search trail).

**Does not support (direction 2 — coil calibrates Hall):** zero corpus
support in either domain [EV32], confirming the pilot's finding on the
full corpus. The flagship deployed system's coils were never
bench-calibrated (P0001) — the trusted coil chain the reverse direction
presupposes did not exist even there [EV04]. B10's own Theorem 1 (C23)
explains the structural half of this: offset can never come from the coil;
gain only conditionally. The corpus neither contradicts the theorem nor
supplies the missing hardware demonstration. The reverse direction remains
the PhD's most distinctive and least externally supported claim.

**Contradicts / cautions:**
- Incumbent practice remains coil-only even in a new 2020 flagship
  redesign (P0024) — the hybrid must argue its regime (long-pulse), not
  the generic architecture [EV19].
- TMR spans DC-to-broadband in one channel (P0031, P0060; B10 C43),
  removing the two-channel motivation in gamma-only environments; P0050
  adds TMR's EMI filtering weakness, keeping the harsh-environment
  question open in both directions [EV18, EV28].
- The idealized-vs-real validation gap (P0003 vs P0001) is unclosed
  [EV10].

Net adjudication: the architecture's forward direction is established but
occupied; the reverse direction is open but unsupported; the specific
four-gap framing B10 adopts (C26) survives contact with this corpus — no
corpus paper closes any of gaps (a)-(d), and EV32/EV33 verify (b) and (d)
explicitly within corpus bounds.

## 6. (d) Which power-conversion work genuinely benefits from the PhD direction

Judged strictly from corpus evidence:

1. **WBG switching-current metrology (genuine, strongest):** the field
   states quantified unmet requirements (≥50 MHz, isolation, DC content,
   size, cost — P0050) and its demonstrated solutions are AC-only (P0048,
   P0056, P0055). The missing DC-capable, EMI-robust, fused-channel piece
   is methodologically the PhD's Element-2 problem restated [EV27, EV34].
2. **Converter/power-equipment condition monitoring with DC-capable
   magnetic sensing (genuine but contested):** the niche exists (P0060,
   P0061, P0062) and is currently being taken by MR technologies; a
   Hall-based entry needs a demonstrated EMI/temperature/radiation
   advantage that no corpus paper establishes [EV28].
3. **High-temperature/harsh converters (plausible only):** SiC converters
   target 200-300 C (P0057, review-level), where P0017-class
   extreme-temperature Hall practice is relevant precedent; no corpus
   paper connects the two [EV07, EV13].
4. **Not a genuine beneficiary:** converter topology/control design
   (P0049, P0051) and WBG device/reliability engineering (P0053, P0058,
   P0059) — loose analogy only [EV30, EV31].

## 7. (e) Established evidence vs plausible inference vs unknowns — summary

**Established (multi-source primary evidence):** harsh-environment III-V
Hall sensing (EV02); traceable calibration methodology at low field
(EV01); Hall→coil fusion algorithm value on synthetic data plus system
coexistence (EV03); inverse-reconstruction method family (EV16);
conditional NI self-protection with an experimentally bounded fault mode
(EV05, EV21); weak-signal/EMI-limited quench detection (EV06, EV23);
quantified WBG current-metrology requirements with AC-only point solutions
(EV27).

**Plausible inference (stated as inference, with falsifiers in the map):**
transferability of P0008's method to fusion-relevant sensors (EV01/EV35);
the long-pulse regime argument for the Hall channel (EV19); the
HTS-monitoring instrumentation niche (EV25/EV26); the fused-DC-channel
transfer into WBG metrology (EV27/EV34).

**Unknown (no corpus evidence either way):** GaN/AlGaN radiation response
(EV09); coil→Hall reverse calibration in practice (EV32); stellarator
Hall/coil work (EV33); tesla-scale traceable calibration (EV35); Hall vs
TMR head-to-head under switching EMI (EV28); NI protection at large-magnet
scale (EV21).

## 8. Method and limitations

- No citation counts or venue prestige entered any judgment; weights
  derive from study design, calibration traceability, uncertainty
  reporting, conditions, controls, replication, relevance, and disclosed
  limitations (LIT_POLICY). Review conclusions are separated from primary
  experiments throughout (P0005, P0006, P0010, P0015, P0046, P0050,
  P0052-P0054, P0057 treated as review-level; P0017 re-adjudicated to
  primary, P0050 to review, per §1.3).
- Retraction rule: zero retracted items found (0/62 on all opened-record
  checks); no claim rests on retracted work. The single correction
  (P0012) is disclosed; P0012 is cited only in EV11 at metadata level for
  platform coverage, with no load-bearing number drawn from it. No
  unresolved correction or peer-review status exists in the corpus; the
  P0006 fast-review caveat is disclosed where used (EV07, EV08).
- 23 of 62 rows were never content-opened by pilot, verifier, or this run;
  they are used only at ledger-metadata level, and every EVIDENCE_MAP row
  states its provenance. This is a disclosed depth limitation, not a
  concealment.
- WebFetch extraction is automated; load-bearing numbers were quoted as
  returned, and residual extraction-error risk is disclosed (it is the
  stated basis for treating the two §1.3 reclassifications as judgments,
  not proofs).
- This synthesis did not run fresh discovery searches beyond the B12
  corpus; corpus-bounded absence claims (EV09, EV26, EV32, EV33, EV35)
  are explicitly bounded and feed GAPS.md bridge tests rather than
  novelty verdicts.
