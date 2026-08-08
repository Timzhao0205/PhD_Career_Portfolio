# Stage 30 — Publication-Only IP Screen

Run: HSXIP-20260805T071311Z. Scope authority: `IP_SCOPE.md`, `CLAUDE.md`,
`schemas/OUTPUT_GATES.md`. Inputs: `outputs/00_SCOPE_AUDIT.md`,
`outputs/10_DISCLOSURE_MAP.csv` / `10_PUBLICATION_TECH.md` (F01–F51),
`outputs/20_PRIOR_ART.csv` / `20_SEARCH_LOG.md` (S001–S022, N001–N018), and the
three controlling manuscript artifacts (key passages independently re-read at
`regular_lsens.tex` L457, L465, L479–487, L496, L503–506 and `submission.pdf`
p.9).

**What this document is and is not.** This is a research-grade patentability
*triage* screen for OTL-decision support. It is **not legal advice, not a
patentability or validity opinion, not an FTO opinion, and not an exhaustive
search**. All risk and confidence labels are calibrated research judgments,
not legal conclusions. The accompanying `30_CLAIM_CHART.csv` is an
element-comparison research aid, **not drafted claims**. Per `20_SEARCH_LOG.md`,
the two `lead_only` ledger rows (N004, N012) carry no conclusions here; where
they are mentioned, it is only to document that limitation.

## 0. Method and label calibration

Six questions are kept conceptually separate throughout: **novelty** (is there
a material delta over the closest single reference), **obviousness** (would
the delta be a predictable variation/combination under the MPEP 2141/2143 KSR
framework on the current evidence record), **enablement/written support**
(does the manuscript disclose enough to support and reproduce the element),
**inventorship** (who conceived it — flagged as questions, never resolved
here), **practical/commercial claim value** (scope, market, detectability,
design-arounds), and **FTO** (third-party rights — expressly out of scope; one
observation is recorded in §8 and labeled as such).

Calibrated labels:

- `novelty_risk`: **high** = likely no material delta over a verified
  reference / effectively anticipated; **medium** = a literal delta survives
  the bounded search, but the search cannot exclude closer art; **low** = a
  well-evidenced delta (no element in this screen earns `low`).
- `obviousness_risk`: **high** = on the current record the delta reads as a
  predictable substitution/combination of documented elements with documented
  motivation and no unexpected result; **medium** = a colorable non-obviousness
  argument exists but is currently unevidenced; **low** = documented unexpected
  result or teaching away (none on record).
- `confidence`: **high** = disposition rests on verified references plus the
  manuscript's own text; **medium** = disposition rests partly on bounded-search
  absences or unresolved factual questions; **low** = materially incomplete
  record (only C4's search depth approaches this).
- `disposition` (claim-chart vocabulary): **screen_out** = no
  publication-specific candidate identified for this element; **weak** = a
  literal delta may survive but is not recommended as a standalone candidate
  on the current record; **conditional_hold** = potentially material — held
  for Stage 40 deep-dive and inventor evidence before any OTL recommendation.

Hard rules applied (per `CLAUDE.md`): patentability is **not** inferred from
novelty of scientific publication, "first" deployment, commercial usefulness,
or successful experimentation; combination claims are **not** treated as
non-obvious without an evidenced unexpected result or teaching away; future
work and excluded concepts are not evaluated as manuscript IP.

## 1. Doctrinal anchors (research framework, with identifiers)

- **New use of a known device** — MPEP 2112/2112.02
  (S004, https://www.uspto.gov/web/offices/pac/mpep/s2112.html): *In re Hack*
  — a new use for an old structure "based on unknown properties of the
  structure might be patentable ... as a process of using"; *In re May* — a
  claim reciting use of an old structure "directed to a result or property of
  that composition or structure" is anticipated. Applied to Group 2.
- **Combination of known elements** — MPEP 2141/2143, KSR v. Teleflex
  (N001, https://www.uspto.gov/web/offices/pac/mpep/s2141.html): caution in
  granting patents on combinations of known elements; "combining prior art
  elements according to known methods to yield predictable results" is an
  obviousness rationale. Applied to Groups 3 and 5.
- **Disclosure/inventorship context** — Stanford OTL pages (S001–S003,
  https://otl.stanford.edu/researchers/submit-invention-otl,
  https://otl.stanford.edu/patent,
  https://otl.stanford.edu/researchers/otls-process): public disclosure
  forecloses OTL filing; inventorship follows conception of claimed subject
  matter, not authorship. These frame the inventorship questions below; the
  disclosure-timing analysis itself is Stage 50's job.

## 2. Group 1 — Existing AlGaN/GaN Hall element and fabrication (C1)

**Manuscript feature (fact).** F01–F09, F18: purchased NTT-AT AlGaN/GaN
heterostructure; mesa etch; Ti/Al/Mo/Au 850 °C/35 s ohmic anneal (cited to
ref11); 7 nm Al2O3 passivation; vias; Ti/Au bond metal; 5×5 mm die; regular
octagonal plate, 200 µm inscribed diameter (cited to ref10); two-terminal
voltage bias with orthogonal Hall readout (`regular_lsens.tex` L457, L479–483).

**Closest references.**
- S009 — US11137310B2 (https://patents.google.com/patent/US11137310B2/en),
  Univ. of Arkansas at Little Rock: closest device-level patent; claim 1
  recites an AlGaN/GaN micro-Hall sensor with a bias-terminal set and a
  Hall-voltage-terminal set, **plus** simultaneous temperature measurement.
- S010 — US8026718B2 (https://patents.google.com/patent/US8026718B2/en), NGK,
  priority 2007: GaN/AlGaN heterojunction Hall element composition and
  fabrication-method claims.
- S014 — Lu et al. 2006 (https://doi.org/10.1063/1.2201339): independent
  high-temperature AlGaN/GaN Hall sensors, predating the group's entry.
- S011/S012 — the manuscript's **own ref10/ref11**
  (https://doi.org/10.1109/JSEN.2019.2895546,
  https://doi.org/10.1063/1.5139911): the octagonal geometry and the anneal
  recipe / 576 °C characterization are the authors' own prior publications and
  are prior art against this manuscript.
- N013/N014 — US10809318B2, US6639290B1
  (https://patents.google.com/patent/US10809318B2/en,
  https://patents.google.com/patent/US6639290B1/en): octagon / regular-polygon
  Hall active-area geometry is old and generic across material systems.

**Feature delta (inference).** None attributable to this manuscript. Every
device/fabrication element is either a purchased commercial input (F01), the
group's own published prior design (F02, F04 — cited by the authors
themselves), or routine III-nitride processing (F03, F05–F08). The only delta
against the closest patent claim (S009's simultaneous-temperature element) is
a *subtraction*, not an addition — the manuscript's device does less than
S009's claim, which matters for FTO framing (§8), not for patentability of
anything new here.

**Novelty risk: high. Obviousness risk: high.**

**Enablement/written support.** Adequate for what it describes (a process
summary reproducible by a skilled III-nitride fab practitioner with the cited
group papers in hand), but the manuscript adds no device-level detail beyond
ref10/ref11 (no wafer-lot characterization, no contact-resistance data — F39,
F45, F47 absences). Nothing here to support a device claim that ref10/ref11 do
not already support — and those are already published.

**Inventorship questions.** If (contrary to this screen) any device-level
claim were pursued, conception would trace to the ref10/ref11 authors
(Alpert, Dowling, et al.), largely not this manuscript's author list — an
immediate inventorship mismatch flag. Also noted for OTL awareness: the
corresponding author co-published in 2024 (N002,
https://arxiv.org/abs/2402.11393) with three named inventors of S009 —
a documented collaboration relationship, recorded as fact, no conclusion drawn.

**Practical claim value.** None identified from this manuscript: any claim
would be anticipated by, or obvious over, the group's own 2019/2020
publications, which have been public for 6–7 years.

**Confidence: high** (verified claim text of S009/S010/N013/N014; the
manuscript's own citations concede the provenance of the two most specific
choices).

**Recommended action: screen out.** No device/fabrication candidate from this
publication. **Evidence that could reverse:** discovery of a device
modification unique to this manuscript (none appears in the text), or an
unpublished pre-2019 group patent filing covering the geometry/recipe (direct
inventor-name searches found none; bounded-search caveat).

## 3. Group 2 — New use as an in-vessel fusion/stellarator diagnostic (C2)

**Manuscript feature (fact).** F25–F32, F49–F51: the packaged sensor was
deployed inside the HSX vessel near the plasma edge and operated across 68
consecutive shots with a 200 V/V, 1 MHz readout; the cover letter (not the
peer-reviewed body) asserts "the first GaN-based Hall-effect sensor deployed
inside a stellarator" (submission.pdf p.9). The body's strongest
self-description is a feasibility statement (L506).

**Closest references.**
- N016 — Stevenson et al. 2014 (https://doi.org/10.1063/1.4894209): 16-element
  **GaAs** Hall array deployed in-vessel at the Compact Toroidal Hybrid, a
  stellarator-class (non-axisymmetric torsatron/tokamak hybrid) device, 12
  years earlier.
- S015 — 2005 InSb Hall array for edge-plasma field measurements
  (https://doi.org/10.1063/1.2018628); S016 — JET in-vessel InSb Hall probes,
  11+ years / 19,000+ pulses (https://iopscience.iop.org/article/10.1088/1741-4326/ac8aad);
  S017/S018/N018 — metal/bismuth/antimony Hall programs for ITER/DEMO.
- S021 — Chlechowitz 2015 (https://doi.org/10.1088/0029-5515/55/11/113012):
  HSX's pre-existing magnetics set contained no Hall probe of any material.
- Doctrinal frame: S004 (MPEP 2112.02).

**The MPEP 2112.02 fork, applied (inference).** A use claim survives *In re
May* only if it is a concrete process exploiting a **previously unknown**
property of the old device. Here the properties relied on — 2DEG Hall
sensitivity and thermal tolerance to 576 °C — are **known, published
properties**, published by this same group (S011/S012) and recited as the
motivation in the manuscript's own introduction (L451). The sensed quantity is
the device's inherent Hall response. Stripped of the Group-3 packaging, the
"new use" is a known device producing its inherent magnetic response in a new
location. That is the *In re May* side of the fork: **not a concrete
non-obvious process of use as disclosed**. The concrete process steps that do
appear (bias control, coil-only control, diamagnetic-loop correlation) are the
routine commissioning practices screened in Group 5; the only genuinely
environment-specific engineering content is the packaging, which belongs to
Group 3.

**Novelty and obviousness (inference).** Literal novelty of the narrow pairing
"GaN Hall sensor inside a fusion vessel" survives the bounded search — no
GaN/AlGaN Hall sensor was found in any fusion deployment (saturated-gap
finding, `20_SEARCH_LOG.md` §1). **Novelty risk: medium** for that narrow
pairing (a bounded English-language absence is not proof of novelty; N004
remains `lead_only` with an unresolved date). **Obviousness risk: high**: the
deployment concept is established across InSb/GaAs/bismuth/metal platforms
(S015, S016, S018, N016); substituting a material whose harsh-environment
suitability the group itself had already published (S012, S014) into a known
diagnostic deployment reads directly onto the KSR simple-substitution
rationale, with the motivation stated in the manuscript's own introduction. No
unexpected result is on the record: no calibrated sensitivity, no quantified
noise floor, no temperature or radiation data from this deployment (F38, F39,
F45, F47). Sixty-eight-shot survival is successful experimentation, which
under this project's rules does not support patentability. The
cover-letter-only "first" (F49/F50) is a scientific-priority statement that
survives N016 only on GaN-vs-GaAs and stellarator-vs-torsatron/hybrid labeling
distinctions; it is not a patentability basis, and it is notable that the
peer-reviewed body itself claims no "first."

**A record tension worth flagging (inference, calibrated).** The
introduction's categorical premise that Si/GaAs/InAs/InSb Hall devices
"cannot be deployed near the plasma edge" (L451) sits in tension with
verified deployments of InSb (S015, S016 — JET, 19,000+ pulses) and GaAs
(N016) in-vessel hardware, at least in short-pulse/current-generation
machines. Uncertainty: those environments are less severe than
reactor-grade long-pulse conditions, which may be what the sentence intends.
Consequences: (a) it removes any teaching-away argument that the field
believed semiconductor Hall probes could not go in-vessel; (b) it is an
accuracy nuance the authors may want to soften pre-arXiv (Stage 50 note).

**Enablement/written support.** The deployment itself is well documented at
the narrative level (shots, comparisons, figures), but nothing quantitative
that a use claim could recite as a distinguishing functional limitation is
disclosed (no field values, no sensitivity, no environmental spec met).

**Inventorship questions.** Who conceived deploying this sensor in HSX —
Stanford authors, UW-Madison HSX personnel (Goodman, Gallenberger, Geiger), or
jointly? Materially affects any hypothetical use-claim inventorship and the
Stage 50 sponsor analysis (DOE/SLAC vs. UW/DOE facility funding).

**Practical claim value.** Low as a standalone use claim: the realistic scope
(a method of monitoring field inside a stellarator using an AlGaN/GaN Hall
sensor) has a tiny population of potential practitioners (fusion labs),
near-zero detectability, and an easy design-around (any other wide-bandgap or
established fusion Hall material — InSb, Sb, Bi programs already active).

**Confidence: high** on the doctrinal disposition (the known-property record
is the group's own publications); **medium** on the novelty-of-the-pairing
sub-finding (bounded-search absence).

**Recommended action: screen out as a standalone candidate.** Whatever
protectable content exists in the deployment resides in the Group-3 package;
a use limitation could at most serve as a dependent/contextual element of a
C3-anchored claim (Stage 40/60 to test). **Evidence that could reverse:**
(a) data showing an *unknown* property exploited in-vessel — e.g., a measured,
unexpected radiation- or GDC-environment behavior unique to the 2DEG platform
under fusion conditions (none reported; radiation work is explicitly future
work, F36, and must not be imported); (b) a verified teaching-away reference
stating GaN unsuitable for in-vessel use (none found); (c) confirmation that
N004 predates and discloses something closer (would further weaken, not
strengthen).

## 4. Group 3 — UHV/GDC module combination (C3)

**Manuscript feature (fact).** F10–F17: Al wire bonds to ceramic LCC; EPO-TEK
353ND encapsulation; 150 °C/1 h vacuum bake "to meet the ultra-high-vacuum
(UHV) requirements of the HSX facility"; custom zirconia holder;
stainless-steel standoff; insertion flange; and "a grounded graphite shield
... installed over the packaged sensor module" "[t]o reduce the risk of
arcing and epoxy degradation during glow discharge cleaning (GDC) and plasma
operations" (L465 — the shield's entire disclosure is that one sentence plus
small photographs).

**Closest references (ranked, per the saturated coverage-area-3 search).**
- N017 — W7-X in-vessel Mirnov coils "covered by graphite wall protection
  panels" (https://iopscience.iop.org/article/10.1088/1361-6587/abc395):
  closest same-class analog (graphite over a magnetic diagnostic in an
  operating stellarator), but stated purpose is plasma-exposure/thermal
  protection, the diagnostic is an inductive coil, and **no grounding
  statement was found** despite direct reading.
- N015 — USH24H (https://patents.google.com/patent/USH24), 1985 DOE: graphite
  armor enclosing a magnetic flux-loop diagnostic (thermal-power purpose).
- N005 — US4858817A
  (https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4858817):
  brazed graphite-ceramic Faraday/thermal shield for a fusion RF antenna.
- N006 — US5216690A (https://patents.google.com/patent/US5216690A): grounded
  shield suppresses vacuum arc-down — the general engineering principle behind
  the shield's stated rationale, known for decades outside fusion.
- N008 — SST-1 GDC conditioning
  (https://www.sciencedirect.com/science/article/abs/pii/S092037961530404X):
  protecting in-vessel diagnostics during GDC is a recognized concern (ceramic
  covers used there); its notes also record a **competing float-vs-ground
  design philosophy** (electrically isolating diagnostics during GDC rather
  than grounding) — currently search-snippet grade only, not independently
  verified, so it is treated as a lead for Stage 40, not evidence.
- S022/N007/N009 — epoxy, bake, and ceramic-LCC elements individually
  conventional (manufacturer datasheet https://www.epotek.com/product/353nd/;
  LIGO qualification https://dcc.ligo.org/LIGO-E1300653/public; MEMS UHV
  packaging https://ieeexplore.ieee.org/document/8739428/). The bake exactly
  matches the vendor's standard 150 °C/1 h cure recommendation — i.e., the
  "UHV bake" is the epoxy's ordinary cure schedule.

**Feature delta (inference).** Elements 1–4 (LCC, epoxy, bake, mounting
hardware) have no individual delta: each is a conventional,
manufacturer-directed or industry-standard choice, uncited and unclaimed as
new by the authors themselves. The entire combination-level delta concentrates
in the shield (F16): **no reference found combines (a) grounded, (b) graphite,
(c) protecting an epoxy-encapsulated solid-state sensor package, (d) against
GDC/plasma arcing and epoxy degradation** — an explicit, saturated
bounded-search gap (`20_SEARCH_LOG.md` §3), which is a documented absence, not
evidence of novelty.

**Novelty risk: medium** (for the shield element and for the combination as a
whole — the literal combination was not found, but near-analogs are dense and
the search is bounded). **Obviousness risk: high on the current record.**
Under MPEP 2141/2143 (N001), a skilled fusion-diagnostics engineer facing a
known concern (GDC/plasma stress on in-vessel diagnostics, N008/N010) had
documented building blocks each performing its established function: graphite
as the standard low-Z protective material over in-vessel magnetic diagnostics
(N017, N015), and grounding a conductive shield to suppress arcing in
vacuum/discharge conditions (N006). Combining them over an epoxy package looks
like known elements combined by known methods for the predictable result. The
manuscript supplies **no unexpected result** (no with/without-shield
comparison, no arcing/epoxy-degradation measurement — F42) and **no verified
teaching away** (the float-vs-ground philosophy, if verified as accepted
practice, could become one — currently unverified). Per project rules, the
combination is not converted into a non-obvious one without such evidence.

**Enablement/written support: thin — the governing weakness.** The shield's
public disclosure is one sentence. No drawings, dimensions, apertures,
clearances, grounding route, or current path (F40, F41); no failure-mode or
comparative data (F42); no UHV acceptance criterion behind "meet the UHV
requirements" (F43). The manuscript as published would not support a
specific, distinguishing shield claim without inventor-supplied detail beyond
the publication. (Corollary for Stage 50: the publication discloses the
*concept* at exactly the one-sentence level while the implementation detail
remains undisclosed — the disclosure-timing consequences of that split are
Stage 50's question, not this stage's.)

**Inventorship questions (open, controlling for the OTL decision).** Per
`IP_SCOPE.md` and F44: Who conceived the grounded graphite shield, its
geometry, grounding route, and placement, and when? Was it standard HSX/GDC
facility engineering (which would point toward UW-Madison HSX staff
conception and/or toward it being routine practice), adapted from an existing
HSX probe, or newly developed for this module? Was there a documented no-shield
failure or arcing event? UW-Madison co-author contribution here directly
affects both inventorship and which institution's OTL/sponsor terms control.
These are questions for the inventors/OTL; this screen does not assume answers.

**Practical claim value.** Modest at best: any defensible claim would be
narrow (grounded graphite shield + epoxy-encapsulated solid-state magnetic
sensor + GDC/plasma environment), addressing a small market (fusion-device
diagnostics packaging; possibly future commercial-fusion instrumentation);
infringement would occur inside vacuum vessels (hard to detect); and
design-arounds are readily available (different shield material, floating
configuration, non-epoxy encapsulation, welded metal housings as used at JET —
S016). Realistic value is defensive/portfolio or licensing-adjacent rather
than standalone.

**Confidence: medium** — the disposition depends on unresolved factual
questions (conception, without-shield history, W7-X grounding status) that
inventor records could change in either direction.

**Recommended action: conditional hold — the single strongest surviving
candidate.** Carry to Stage 40 deep-dive and put the `IP_SCOPE.md` inventor
questions to the authors before any arXiv posting decision (Stage 50 sets the
gate). Do not represent it to OTL as more than a narrow, evidence-contingent
candidate. **Evidence that could reverse (both directions):**
- *Strengthens:* inventor-held drawings and conception records; a documented
  no-shield failure/arcing/epoxy-degradation event or with/without comparison
  (unexpected-result evidence); independent verification that standard
  practice taught floating (not grounding) diagnostics during GDC (teaching
  away); GDC exposure logs quantifying survival conditions.
- *Weakens to screen-out:* confirmation that W7-X's graphite panels are
  grounded (open question, `20_SEARCH_LOG.md` §9); evidence the shield was
  pre-existing HSX standard practice for in-vessel probes; or inventor
  confirmation that the shield was copied from an existing facility design.

## 5. Group 4 — Readout chain (C4)

**Manuscript feature (fact).** F19–F24: Keysight DSOX1204G waveform-generator
bias; INA849 instrumentation amplifier plus two OPA814 stages (×10/×10/×2);
total gain 200 V/V; 1 MHz bandwidth; vacuum feedthroughs to external
electronics (L479–483, Fig. 3).

**Closest references.** None verified — this coverage area was deliberately
searched only to lead level (N012, https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7902820,
recorded `lead_only` and **carrying no conclusion**; documented limitation,
`20_SEARCH_LOG.md` §9). The disposition therefore rests on
manuscript-intrinsic evidence: the chain consists entirely of named
off-the-shelf commercial ICs and a lab instrument used in their intended
amplifier/bias configurations, with no disclosed circuit topology, novel
interconnection, compensation scheme, or performance figure beyond the parts'
catalog capabilities. The manuscript claims nothing new for it, and the
lower-noise readout mentioned at L506 is explicitly future work (F37,
excluded from evaluation as manuscript IP).

**Feature delta:** none disclosed. **Novelty risk: high. Obviousness risk:
high.** **Enablement/support:** block-diagram level only (stage gains appear
only in Fig. 3); adequate for reproduction precisely because the parts are
catalog items. **Inventorship questions:** none material. **Practical claim
value:** none identified. **Confidence: medium** — high on the intrinsic
record, discounted one step because the prior-art search here was not taken to
saturation (documented evidence limitation, honestly carried rather than
papered over).

**Recommended action: screen out.** **Evidence that could reverse:** discovery
of an undisclosed non-obvious circuit detail (nothing in the three artifacts
suggests one exists); a saturated readout search is not warranted on this
record.

## 6. Group 5 — Deployment/validation method (C5)

**Manuscript feature (fact).** F27–F30: biased (0.4 V) vs. unbiased (0 V)
comparison; plasma-discharge vs. coil-only comparison; temporal comparison
against the HSX diamagnetic loop (ref16) across high-energy, late-breakdown,
and failed-breakdown shots with a stated ~30 ms DAQ offset (L487, L496,
L503–504). The manuscript itself frames the diamagnetic comparison as
correlation of "physically distinct quantities," not equivalence.

**Closest references.** N011
(https://iopscience.iop.org/article/10.1088/1741-4326/adaed0) — cross-checking
a magnetics diagnostic against an independent, physically related diagnostic
is routine current commissioning practice (JT-60SA, 2025); S021 — the HSX
comparison instrument set predates the manuscript; S012/ref15 — the
bias-linearity/offset physics used for the bias control is the group's own
published understanding; N001 — KSR combination standard.

**Feature delta (inference).** Each of the three parts is a routine control or
commissioning practice; the physics exploited (V_H ∝ V_bias, V_off
bias-independent) is textbook and group-published. No named prior source
claims the exact three-part combination (`20_SEARCH_LOG.md` §4), but the
combination is a predictable arrangement of routine controls with no
unexpected result — and per project rules that does not make it non-obvious.

**Novelty risk: high** (parts) / **medium** (exact combination, as a literal
matter only). **Obviousness risk: high.** **Enablement/support:** adequate
narratively; no quantitative repeatability statistic, correlation coefficient,
or raw data (F30, F32, F48). **Inventorship questions:** none material — if
anything, the protocol design likely involved HSX operations staff, another
UW-Madison contribution question folded into Stage 50's list.
**Practical claim value: effectively zero** — a lab commissioning method,
practiced privately inside research facilities, undetectable and
unenforceable. **Confidence: high.**

**Recommended action: screen out.** **Evidence that could reverse:** none
realistic; an exact-match methods reference would only confirm the screen-out.

## 7. Summary of dispositions

| Group | Candidate | Novelty risk | Obviousness risk | Enablement | Commercial value | Confidence | Disposition |
|---|---|---|---|---|---|---|---|
| 1 | C1 Hall device/fabrication | high | high | adequate (but nothing new to support) | none | high | screen_out |
| 2 | C2 fusion/stellarator use | medium (narrow pairing) / high (concept) | high | narrative only; nothing quantitatively claimable | low | high (doctrine) / medium (pairing) | screen_out standalone; contextual element for C3 at most |
| 3 | C3 UHV/GDC module | medium (shield/combination) | high on current record | thin (one sentence; F40–F43) | modest, narrow | medium | **conditional_hold — strongest surviving candidate** |
| 4 | C4 readout chain | high | high | block-diagram level | none | medium (search-depth limit) | screen_out |
| 5 | C5 deployment/validation | high / medium (literal combo) | high | adequate narrative | ~zero | high | screen_out |

**Single strongest surviving candidate:** C3, and within it specifically the
grounded graphite shield element (F16) as the load-bearing feature of the
combination — held **conditionally**, on documented-gap novelty and currently
unevidenced non-obviousness, pending Stage 40's deep-dive and the inventor
answers to `IP_SCOPE.md`'s conception/failure-history/UW-contribution
questions. Nothing in this screen should be read as predicting that C3 would
support a filing; on the present record its obviousness risk is high and its
enablement is thin.

**Decisive evidence gaps (ranked):**
1. Shield conception and records (who/when/why; drawings, grounding route) —
   F40, F41, F44.
2. Any without-shield failure mode or with/without comparison (the only
   plausible unexpected-result evidence) — F42.
3. Verification of the float-vs-ground GDC practice question (potential
   teaching away — currently snippet-grade) and of W7-X panel grounding
   (potential closer analog) — `20_SEARCH_LOG.md` §9.
4. UHV acceptance criterion behind the bake claim — F43.
5. UW-Madison personnel contribution to package/deployment elements
   (inventorship and institutional-rights control) — F44.

## 8. FTO separation note (out of scope; recorded only to keep concepts distinct)

This package performs no clearance search and renders no FTO opinion. Two
verified third-party patents are flagged for any future commercialization
discussion, without analysis: S009 (US11137310B2) — claim 1 requires
simultaneous temperature measurement, which the manuscript's device does not
perform on the record read at Stage 20; and N013 (US10809318B2, octagon-shape
dependent claim, silicon-CMOS structure limitations per its claim 1, active,
recorded expiry 2036). Google Patents legal-status labels are not treated as
legal conclusions per `SOURCE_POLICY.md`. Patentability dispositions above are
independent of, and unaffected by, these FTO-side observations.

## 9. Scope discipline and gate compliance

- Excluded concepts (three-axis probes, Hall-coil hybrids, current-spinning/
  radiation-compensation architectures, TCAD/startup/future-PhD material,
  lower-noise readout, radiation characterization) were **not** evaluated as
  manuscript IP; where they surfaced (S013, S016's hybrid proposal, F36/F37
  future work) they are cited only as prior-art/context.
- `lead_only` rows N004 and N012 support no conclusion in this document; each
  is mentioned only to document that limitation.
- All five gate groups are separately answered (§§2–6), each with closest
  references, feature delta, novelty risk, obviousness risk,
  enablement/support, inventorship questions, practical claim value,
  confidence, and recommended action, plus reversal evidence.
- Fact / inference / uncertainty / action are labeled throughout; calibrated
  risk labels only; no legal conclusions ("clear," "valid," "guaranteed" do
  not appear as judgments).
- Material propositions carry ledger source_ids with URLs/identifiers reused
  from `outputs/20_PRIOR_ART.csv`; manuscript propositions carry
  `regular_lsens.tex` line cites verified against the source this session.
- No patentability was inferred from scientific novelty, "first" deployment,
  commercial usefulness, or successful experimentation; no combination was
  treated as non-obvious without evidenced unexpected result or teaching away.

## 10. Files produced

- `outputs/30_IP_SCREEN.md` (this file)
- `outputs/30_CLAIM_CHART.csv` (22 element rows across C1–C5; exact gate
  schema `candidate_id,concept,element_no,element,manuscript_support,closest_source,source_support,delta,novelty_risk,obviousness_risk,evidence_gap,disposition`)
