# Stage 40 — UHV/GDC Package Deep-Dive Verdict

Run: HSXIP-20260805T071311Z. Scope authority: `IP_SCOPE.md`, `CLAUDE.md`,
`schemas/OUTPUT_GATES.md` (§40 gate). Inputs: `outputs/30_IP_SCREEN.md` §4
(candidate C3, inherited as `conditional_hold` — the single surviving
candidate), `outputs/20_PRIOR_ART.csv` / `20_SEARCH_LOG.md` §3,
`outputs/10_DISCLOSURE_MAP.csv` (F10–F17, F40–F44, F46),
`outputs/10_PUBLICATION_TECH.md`, and the manuscript re-read this session at
`regular_lsens.tex` L465 (§II-B), L469 (Fig. 2 caption), L479–L487 (§II-C),
L496 (§III-A), plus `submission.pdf` p.8 (graphical abstract).

**What this document is and is not.** This is a research-grade packaging-
engineering and patentability-triage deep-dive supporting an OTL/arXiv
decision. It is **not legal advice, not a patentability/validity opinion, not
an FTO opinion, and not an exhaustive search**. All labels are calibrated
research judgments. Fact, inference, uncertainty, and action are marked
throughout. Provenance: produced by the stage-40 agent on model
`claude-fable-5` as reported by the harness; effort/token/cost telemetry
`not_exposed` at this interface.

---

## 0. Verdict

**On the current public record, the disclosed UHV/GDC module is NOT
established as more than routine packaging.** Six of its seven elements are
individually conventional, manufacturer-directed, or industry-standard
choices, uncited and unclaimed as new by the authors themselves. The entire
potentially-more-than-routine content concentrates in one element — the
grounded graphite shield (F16) — whose public disclosure is a single sentence
(L465) plus small photographs, with **no documented unexpected result, no
with/without comparison, no failure-mode narrative, and no reproducible
geometry/grounding detail** (F40–F42).

- **Novelty (shield element / exact combination): literal bounded-search gap
  survives** (no reference found combining grounded + graphite + protecting an
  epoxy-encapsulated solid-state sensor + against GDC/plasma arcing and epoxy
  degradation; `20_SEARCH_LOG.md` §3). A documented absence, not evidence of
  novelty. Risk label unchanged from Stage 30: **medium**.
- **Obviousness: high risk, now on a stronger evidentiary footing than at
  Stage 30.** This stage's primary-source verification (§9) documents that (a)
  GDC arcing was a known hazard by 1979, (b) the grounded-vs-floating
  electrical behavior of objects in GDC was documented at PPPL in 1979, and
  (c) W7-X grounds part of its in-vessel Mirnov diagnostic to vessel ground
  specifically to prevent DC charging. Every link in the KSR chain
  (known problem → known building blocks → predictable result) is now
  supported by an A/B-tier source. The one identified teaching-away lead
  (float-vs-ground GDC practice, N008 snippet) was tested and **weakened**,
  not confirmed (§9.2).
- **Enablement/written support: thin — unchanged and controlling.** The
  publication would not support a specific, distinguishing shield claim
  without inventor-supplied material beyond the paper (F40, F41, F43).
- **Documented, unexpected, commercially useful result from the shield: none
  on the record** (§5). The gate question is answered in the negative as
  disclosed.

**Disposition carried to Stages 50/60: C3 remains `conditional_hold`, but
narrowed** — the hold now rests almost entirely on the possibility of
inventor-held evidence (a documented no-shield failure/arcing/epoxy-damage
event, conception records, and design calculations; see
`40_EVIDENCE_GAPS.md`). Absent at least the minimum evidence bundle in §10,
the calibrated expectation is that Stage 60/70 will find no
publication-specific filing case in this module. **Confidence: medium-high**
(high on the routine-elements and obviousness-chain findings, which rest on
verified sources and the manuscript's own text; medium on the residual hold,
which depends on unresolved inventor-held facts). This stage does not decide
the arXiv gate; that is Stage 50's task.

---

## 1. What is actually disclosed (facts, with locations)

The module's entire textual disclosure is one paragraph, `regular_lsens.tex`
L465 (§II-B), plus the Fig. 2 caption (L469) and small photographs (Fig. 2;
`submission.pdf` p.8):

1. Die wire-bonded to a ceramic leadless chip carrier "(LCC; Spectrum
   Semiconductor Materials) using aluminum wire" (F10).
2. "encapsulated with epoxy (EPO-TEK 353ND)" (F11).
3. "vacuum-baked at 150 °C for 1 hour to meet the ultra-high-vacuum (UHV)
   requirements of the HSX facility" (F12).
4. "mounted on a custom zirconia ceramic holder" (F13).
5. "attached to a stainless-steel standoff for insertion into the HSX vessel"
   (F14); "custom flange" appears only in the Fig. 2 caption, L469 (F15).
6. "To reduce the risk of arcing and epoxy degradation during glow discharge
   cleaning (GDC) and plasma operations, a grounded graphite shield was
   installed over the packaged sensor module." (F16; GDC exposure itself is
   implicit only — F17.)

No packaging element is attributed to any bibliography reference
(`10_PUBLICATION_TECH.md` §4) and none carries a novelty claim in the body
(`10_PUBLICATION_TECH.md` §3). No dimension, drawing, aperture, clearance,
grounding route, acceptance criterion, exposure log, or comparative datum for
the shield or bake appears anywhere in the three controlling artifacts
(F40–F43, F46, F48).

## 2. Routine parts vs. the asserted combination

| Element | Convention evidence | Assessment |
|---|---|---|
| Al wire bonds to ceramic LCC (F10) | N009 (ceramic-LCC UHV packaging, https://ieeexplore.ieee.org/document/8739428/); vendor-catalog carrier | Routine (fact: uncited, unclaimed; inference: standard die-attach practice) |
| EPO-TEK 353ND encapsulation (F11) | S022 (vendor datasheet, https://www.epotek.com/product/353nd/ — marketed for semiconductor/UHV sealing; ASTM E595 low-outgassing); N007 (LIGO UHV qualification, https://dcc.ligo.org/LIGO-E1300653/public) | Routine, manufacturer-directed, independently pre-qualified for UHV service |
| 150 °C/1 h vacuum bake (F12) | S022: vendor's standard recommended cure is exactly 150 °C/1 h | Routine (see §3) |
| Custom zirconia holder (F13) | Insulating ceramic mounts for in-vessel diagnostics are standard (N008 ceramic covers, https://www.sciencedirect.com/science/article/abs/pii/S092037961530404X; S019 ceramic-substrate fusion Hall sensors, https://www.mdpi.com/1424-8220/21/3/721) | Routine class; "custom" describes fit, not disclosed innovation (no drawing — F40-class gap). Why zirconia vs. alumina is undisclosed (uncertainty) |
| Stainless standoff + flange (F14/F15) | Universal vacuum-facility hardware | Routine |
| Grounded graphite shield (F16) | No single-reference match found (saturated gap, `20_SEARCH_LOG.md` §3); nearest analogs N017, N015, N005, N006, N008 | **The only load-bearing element** — evaluated in §§4–5 |

**Inference:** the combination of elements 1–5 is an ordinary lab-grade UHV
sensor package a skilled vacuum-instrumentation engineer would assemble from
catalog parts and vendor instructions. The asserted combination is
distinguishable from its parts **only** through the shield and the
GDC-environment context it serves.

## 3. Is "pour epoxy and bake" merely an obvious qualification step? Yes, as disclosed.

**Fact:** the manuscript's bake (150 °C, 1 h) exactly matches the vendor's
standard recommended cure schedule for EPO-TEK 353ND (S022,
https://www.epotek.com/product/353nd/). **Inference:** on either available
reading — (a) the standard cure performed in a vacuum oven, or (b) a separate
post-cure outgassing bake at the same mild, standard parameters — the step is
manufacturer-directed or textbook vacuum practice. The stated purpose ("to
meet the ultra-high-vacuum (UHV) requirements of the HSX facility", L465)
recites a qualification goal, not a process delta: no pressure target,
outgassing rate, RGA trace, or leak-test criterion is disclosed (F43), so
there is nothing to distinguish this bake from ordinary practice even at the
parameter level. The epoxy itself was independently UHV-qualified by LIGO
years earlier (N007). **Conclusion (calibrated): the epoxy-plus-bake element
is a routine, manufacturer-directed qualification step; it contributes no
independent candidate content.** The gate's "epoxy plus bake alone is
routine" test is answered affirmatively. **Uncertainty:** whether HSX imposed
a specific acceptance criterion the bake was engineered to meet is unknowable
from the paper (F43) — an inventor question, but even a documented criterion
would show diligence, not invention, unless the process deviated from vendor
practice in a documented way.

## 4. Engineering evaluation of the module across the gate dimensions

Labels: **[F]** manuscript fact, **[I]** engineering inference from cited
sources/first principles, **[U]** uncertainty.

**4.1 Vacuum/outgassing.** [F] Epoxy and bake per §3; survival across 68
shots (L496) is the only vacuum-compatibility evidence; no RGA/leak/pressure
data (F43). [I] Adding a graphite body introduces a porous, gas-adsorbing
surface into the vessel — a known outgassing burden managed by bakeout;
graphite is nevertheless ubiquitous in-vessel in fusion devices (N017, N015),
so this is accepted practice, not a departure. [U] Whether the shield was
separately baked/conditioned is undisclosed. **No documented result beyond
survival.**

**4.2 Thermal.** [F] No temperature data for this deployment (F39 absent);
the 576 °C figure is prior group work (ref11/S012, L451). [I] EPO-TEK 353ND
is a thermally limited organic (vendor-rated service well below plasma-facing
temperatures; S022); a graphite cover plausibly reduces radiant/particle heat
flux to the epoxy — the same thermal-protection purpose W7-X states for its
graphite panels over Mirnov coils (N017) and USH24H states for flux-loop
armor (N015). [I] HSX's short-pulse (~50 ms flat-top, L496) regime makes the
thermal load mild relative to W7-X/JET conditions. **Predictable function,
documented in the field; no thermal measurement in the paper.**

**4.3 Electrical grounding/arcing — the core of the shield's stated purpose.**
[F] The paper asserts the purpose ("reduce the risk of arcing…", L465) and
provides no arcing/degradation measurement (F42). Verified external record
(§9): PDX (1979) documents that "[i]nitial glow discharge operation was
accompanied by frequent arcing", that floating objects in GDC sit at
100–200 V floating potential relative to the grounded vessel, and that
grounded surfaces couple an order of magnitude more strongly to the discharge
(V40-A). N006 (US5216690A, https://patents.google.com/patent/US5216690A)
supplies the decades-old general principle that a grounded conductive shield
suppresses vacuum arc-down. N017 (verified this session, §9.1) documents
W7-X grounding a Mirnov-coil center tap to vessel ground "to prevent
potential DC charging during plasma operation." [I] The engineering logic is
therefore fully documented in the art: an exposed floating/dielectric package
in GDC charges to a ~100–200 V differential (arc driver) and, being organic,
is directly attacked by a discharge whose stated purpose is carbon removal
(V40-A: PDX GDC "chosen to maximize C and O removal"); a grounded conductive
cover pins the surface to cathode potential and takes the ion flux
sacrificially; graphite is the standard low-Z sacrificial material over
in-vessel magnetic diagnostics (N017, N015). **Every link is a documented
prior practice or principle — the mechanism is predictable, and no unexpected
electrical result is reported.**

**4.4 Magnetic transparency/perturbation.** [F] With the shield installed,
the biased sensor tracked coil ramp-up (~sub-kHz) and plasma-ignition
transients and fluctuations (Fig. 4, L496) — the record therefore does
document field penetration through the shield at those timescales. The 1 MHz
figure (L483) is the readout chain's bandwidth, not a demonstrated
through-shield field bandwidth (no spectral data; F45/F48). [I] Graphite is
non-ferromagnetic and weakly diamagnetic — negligible DC field perturbation.
Its electrical conductivity (handbook range ~10^4–10^5 S/m for bulk/isostatic
grades) implies an eddy-current skin depth of roughly 1.6–5 mm at 1 MHz, so
for plausible few-mm shield walls the top of the readout band could be
partially attenuated — **whether it is depends on thickness and geometry the
paper does not disclose (F40); no dimension is assumed here.** [I] The
underlying trade-off (a cover conductive enough to ground/arc-suppress yet
resistive/thin enough to pass fast field components) is the one place a
genuinely engineered, potentially claimable design choice could live — but it
is entirely undocumented in the publication, and the field's awareness of the
conductive-housing/bandwidth problem for in-vessel magnetic diagnostics is
itself documented at W7-X (metallic housings avoided for Mirnov coils to
preserve high-frequency response — lead-grade attribution to the W7-X
magnetic-diagnostics engineering-design literature, S0920379615302453 family;
not independently fetched, carried as a lead, not load-bearing). **Action:**
if inventor records contain a thickness/conductivity/bandwidth calculation,
that is the strongest latent technical delta (see `40_EVIDENCE_GAPS.md` G4).

**4.5 Mechanical/serviceability.** [F] The stack (LCC → zirconia holder →
stainless standoff → flange) enters through a port; the shield was "installed
over" the module — attachment undisclosed (F40). [I] Epoxy encapsulation is
non-hermetic and non-serviceable: a failed die means repotting/rebuilding,
versus the welded/brazed hermetic housings used for long-life in-vessel Hall
systems at JET (S016, https://iopscience.iop.org/article/10.1088/1741-4326/ac8aad).
[I] The flange-mounted assembly is straightforwardly removable — appropriate
for a 68-shot campaign, unproven for long-pulse service. **Routine
lab-instrument mechanics; the serviceability trade-off is cost/simplicity,
not disclosed innovation.**

**4.6 GDC exposure.** [F] Exposure is implicit only (F17): the shield's
stated purpose plus in-vessel residence; no GDC cycle count, duration,
current density, or before/after inspection is reported (F46). [I] GDC's
carbon-removal chemistry makes bare epoxy in a GDC vessel untenable
(V40-A) — which cuts two ways: it makes the shield *necessary*, and it makes
providing *some* cover the predictable response of any skilled operator
(SST-1 already documents protecting in-vessel components during GDC with
ceramic covers — N008). **Efficacy asserted, not demonstrated.**

**4.7 Facility integration.** [F] Custom flange (L469), external electronics
via feedthroughs (L479); HSX UHV requirement invoked but never quantified
(F43). [I] The zirconia holder electrically isolates the package from the
grounded standoff — a sensible isolation scheme consistent with the grounded
shield being the *only* deliberately grounded surface near the die; but the
isolation/grounding topology is nowhere stated (F41). [U] Whether the shield
grounds through the standoff, a dedicated strap, or vessel contact is
unknown — a reproducibility-blocking gap.

**4.8 Commercial value.** [I] The realistic claim market is fusion-device
diagnostics packaging (research devices now; commercial-fusion
instrumentation prospectively). The strongest commercial framing available on
this record: *enabling cheap, fast epoxy-grade packaging inside a
GDC-conditioned vessel by adding a sacrificial grounded low-Z cover* —
i.e., a cost alternative to welded hermetic housings (S016). Value is
modest/defensive: tiny practitioner population, in-vessel infringement
essentially undetectable, and design-arounds abundant (§7). No revenue-grade
licensing thesis is identifiable from the publication alone.

## 5. The gate test: did the shield produce a documented, unexpected, commercially useful result?

Tested per attribute, on the record only:

- **Material (graphite):** standard low-Z protective material over in-vessel
  magnetic diagnostics (N017 W7-X panels; N015 USH24H flux-loop armor; N005
  US4858817 graphite-ceramic shield). Not unexpected.
- **Geometry:** undisclosed (F40). Nothing to evaluate; nothing documented.
- **Grounding:** documented general principle (N006) + documented GDC
  electrical behavior (V40-A) + documented in-vessel-diagnostic grounding
  practice at a stellarator (N017 center tap, §9.1). Predictable.
- **Placement ("over the packaged sensor module"):** concept-level only;
  clearances/apertures undisclosed (F40).
- **Interaction with the sensor:** the only documented interaction datum is
  indirect — the sensor functioned through 68 shots with the shield in place
  and detected field transients through it (L496). No with/without
  comparison, arcing log, or epoxy-condition report exists (F42).

**Finding (calibrated): NO — on the current record the shield contributes no
documented unexpected result.** Its function is the predictable sum of
documented mechanisms. Sixty-eight-shot survival is successful
experimentation, which under this project's rules (`CLAUDE.md`) does not
support patentability. The steelman — that the *system-level insight* of
pairing disposable epoxy packaging with a sacrificial grounded graphite cover
is itself the invention — is preserved for Stage 60, but as disclosed it is a
combination of known elements by known methods for the expected benefit
(MPEP 2141/2143 rationale, N001,
https://www.uspto.gov/web/offices/pac/mpep/s2141.html), with no evidenced
surprise and no teaching away (§9.2).

## 6. Narrowest combination plausibly supported by the paper

Everything below is supported at L465/L469; nothing narrower is (research
aid, not a drafted claim):

> An in-vessel magnetic-field sensing module for a magnetically confined
> plasma device that undergoes glow-discharge cleaning, comprising: (1) a
> solid-state AlGaN/GaN Hall-effect die aluminum-wire-bonded to a ceramic
> leadless chip carrier; (2) a low-outgassing epoxy encapsulating the die and
> bonds, vacuum-baked; (3) the carrier mounted on an electrically insulating
> zirconia holder carried by a stainless standoff and insertion flange; and
> (4) an electrically grounded graphite shield installed over the
> encapsulated module, positioned to reduce arcing and epoxy degradation
> during GDC and plasma operation.

**Support caveats:** element (4) is supported at concept level only —
geometry, apertures, clearance, and grounding route are absent (F40/F41), so
any claim needing those limitations requires inventor material *beyond the
publication* (with the disclosure-timing consequence flagged at Stage 30 §4
for Stage 50: the concept is published; only the detail is not).
**Assessment:** even this narrowest form carries high obviousness risk (§4.3,
§5) and near-zero detectability; its realistic scope is a single facility
practice pattern.

## 7. Design-around assessment: easy

A competitor needing the same capability can avoid every distinctive element
with already-documented alternatives:

1. **Different housing entirely:** boron-nitride-sheathed stainless tube over
   an in-vessel semiconductor Hall array — already fielded at CTH in 2014
   (N016, https://pubs.aip.org/aip/rsi/article/85/9/093502/362290/): an
   existence proof that none of C3's elements is necessary.
2. **Different shield material:** ceramic covers (N008, SST-1 practice), BN,
   SiC, or coated metal.
3. **Different electrical configuration:** floating/isolated cover, or
   grounding the package structure rather than a cover (W7-X grounds the coil
   center tap, not a sensor cover — N017/§9.1).
4. **Non-epoxy encapsulation:** welded/brazed hermetic housings (JET, S016);
   getter-sealed ceramic LCC packages (N009); glass frit.
5. **Operational avoidance:** remove, retract, or shutter the sensor during
   GDC ([I] — an operations option, no citation needed).
6. **Wall-integration:** place the sensor behind existing graphite wall
   protection panels (N017) rather than a dedicated shield.

**Conclusion: design-around difficulty low; detection difficulty extreme**
(practice occurs inside research-device vacuum vessels). This combination
compounds the modest commercial value in §4.8.

## 8. Interaction with excluded scope

Nothing here evaluates three-axis probes, Hall-coil hybrids,
current-spinning/radiation-compensation, TCAD/startup material, or
future-work readout/radiation items as manuscript IP (`IP_SCOPE.md`); the
design-around list in §7 contains only *prior published* alternatives plus
one labeled operations inference, and no new package design invented here is
represented as a disclosed invention.

## 9. External verification performed this stage (both open questions from `20_SEARCH_LOG.md` §9)

**9.1 W7-X graphite panel grounding — PARTIALLY RESOLVED; panel question
still open.** Direct re-fetch of N017
(https://iopscience.iop.org/article/10.1088/1361-6587/abc395, 2026-08-05)
confirmed verbatim: "During plasma operation the coils are covered by
graphite wall protection panels" and — a fact not previously in the ledger —
"Between the two winding layers of the coil a center tap is directly
connected to the plasma vessel ground to prevent potential DC charging during
plasma operation." No statement grounds the *panels* themselves; no
GDC/arcing mention. The 2013 companion engineering paper (ScienceDirect PII
S0920379613005279) remains paywalled (fetch blocked; abstract-grade only);
the openly available W7-X first-operation-phase magnetics paper (Rahbarnia et
al., EPS conf. P1.077, PDF retrieved via
https://pure.mpg.de/rest/items/item_2065910/component/file_3319871/content
and text-extracted this session) contains **no grounding statement for the
panels either**. **Net effect:** the "grounded" element of F16 is *narrowed*
(grounding part of an in-vessel magnetic diagnostic against charging is
documented stellarator practice — obviousness-supporting) but the exact
analog (grounded *graphite cover*) remains unconfirmed either way. The
weaken-to-screen-out trigger in Stage 30 §4 ("confirmation that W7-X's
panels are grounded") has **not** fired. Documented as an evidence
limitation; it did not block this verdict.

**9.2 Float-vs-ground GDC practice — RESOLVED AGAINST THE TEACHING-AWAY
THEORY, at primary source.** Retrieved and read in full (text-extracted from
the OSTI PDF this session): H. F. Dylla, S. A. Cohen, S. M. Rossnagel, G. M.
McCracken, Ph. Staib, "Glow Discharge Conditioning of the PDX Vacuum Vessel,"
Princeton Plasma Physics Laboratory, 26th AVS National Symposium (Oct. 1979),
OSTI 5515925, https://www.osti.gov/servlets/purl/5515925 — cited here as
**V40-A** (A-tier, national-lab primary; verified_full). Verbatim findings:
"floating potentials of 100–200 V were measured on both Langmuir probes and
the surface analysis probe when they were introduced into the plasma column";
"We observed an order of ma[g]nitude decrease in cleaning efficiency if the
surface probe was introduced into the glow discharge floating, rather than
grounded"; "Initial glow discharge operation was accompanied by frequent
arcing which subsequent[l]y decreased with time"; discharge parameters were
chosen for "minimizing sputtering of metals because of sensitive internal
hardware" and to "maximize C and O removal." **Net effect (inference):** (a)
the arcing hazard and the protect-sensitive-hardware motivation behind F16
are documented in the art since 1979; (b) grounded-vs-floating GDC coupling
physics was documented knowledge — the electrical-configuration "toolbox" was
known; (c) **no verified source documents floating diagnostics as an accepted
*protective* practice during GDC** — the N008 snippet-grade float-philosophy
lead is not corroborated at primary level and PDX frames grounding as the
efficient-coupling configuration. The potential teaching-away argument for
C3 is therefore currently **unevidenced and weakened**; only inventor/facility
documentation of an actual float-for-protection practice could revive it
(`40_EVIDENCE_GAPS.md` G7).

## 10. Minimum inventor evidence OTL would need (ranked; detail in `40_EVIDENCE_GAPS.md`)

1. A documented no-shield failure, arcing, or epoxy-degradation event — or
   any with/without-shield comparison (F42). The only realistic
   unexpected-result path.
2. Conception records: who/when/why; drawings/CAD, dimensions, apertures,
   clearances, grounding route (F40/F41/F44).
3. GDC exposure logs for this module: cycles, duration, current density,
   post-exposure inspection (F17/F46).
4. Any design calculation tying shield material/thickness to arc suppression
   and field-transmission bandwidth (§4.4 latent delta).
5. The HSX UHV acceptance criterion and the module's qualification records
   (RGA/leak/pressure) (F43).
6. A statement of UW-Madison personnel contribution and whether the shield
   derives from existing HSX probe hardware or facility practice (F44) —
   controls both inventorship and the routine-practice question.
7. Earliest disclosure of shield details to anyone without confidentiality
   duties (feeds Stage 50's timeline).

## 11. Gate compliance and limitations

- Conventional pieces vs. asserted combination: §2. Epoxy-plus-bake
  routineness: §3 (affirmative). Shield non-obvious-documented-result test:
  §5 (negative on the record). Magnetic, electrical, thermal, GDC, vacuum,
  serviceability, commercial value: §4. Evidence that could change the
  recommendation: §10 and `outputs/40_EVIDENCE_GAPS.md`.
- Material propositions carry ledger source_ids with URLs
  (S016/S019/S022/N001/N005–N009/N015–N017) or the new verified item V40-A
  with its OSTI URL; manuscript propositions carry `regular_lsens.tex` line
  numbers re-verified this session.
- No missing dimension or test datum was invented; where first-principles
  reasoning appears it is labeled [I] and conditioned on undisclosed
  parameters. `lead_only` material (N004, N012, the W7-X engineering-design
  bandwidth attribution in §4.4) carries no conclusion.
- Bounded-search caveat: all absence findings inherit `20_SEARCH_LOG.md`'s
  English-language, indexed-literature limits; the W7-X panel-grounding
  question remains open (§9.1).
- Nothing here is legal advice, a validity/patentability opinion, or an FTO
  clearance; no external submission or upload was performed.

## 12. Files produced

- `outputs/40_UHV_PACKAGE_VERDICT.md` (this file)
- `outputs/40_EVIDENCE_GAPS.md`
