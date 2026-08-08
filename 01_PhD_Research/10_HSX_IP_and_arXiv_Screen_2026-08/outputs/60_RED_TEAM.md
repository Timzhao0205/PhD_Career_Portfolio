# Stage 60 — Red Team: Adversarial Challenge of Every Surviving Filing Case

Run: HSXIP-20260805T071311Z. Scope authority: `IP_SCOPE.md`, `CLAUDE.md`,
`schemas/OUTPUT_GATES.md` (§60 gate). Inputs: `outputs/30_IP_SCREEN.md`
(dispositions, §7), `outputs/40_UHV_PACKAGE_VERDICT.md` + `40_EVIDENCE_GAPS.md`
(C3 narrowed hold; V40-A; G1–G11; §6 narrowest combination; §7 design-arounds),
`outputs/50_ARXIV_RISK.md` (`HOLD_ARXIV_FOR_OTL`), `outputs/20_PRIOR_ART.csv` /
`20_SEARCH_LOG.md`, `outputs/10_DISCLOSURE_MAP.csv`, and the manuscript re-read
this session (`regular_lsens.tex` L451, L453, L457, L465, L469, L479–L487,
L496, L503–L506, L514; `submission.pdf` p.8–9 facts as inherited from Stages
00/50).

**What this document is and is not.** This is the adversarial-review stage of a
research-grade patentability triage. The examiner, fusion-engineer, and
competitor arguments below are **constructed adversarial positions** — the best
case each adversary could plausibly assemble from the verified record — stated
as calibrated research judgments. **Nothing here is legal advice, a
patentability/validity opinion, an FTO opinion, or a prediction of what any
actual examiner would do.** Fact **[F]**, inference **[I]**, uncertainty
**[U]**, and action **[A]** are marked throughout. Provenance: authored by the
stage-60 agent on model `claude-fable-5` as reported by the harness;
effort/token/cost telemetry `not_exposed` at this interface. No safety
fallback, refusal, or model substitution occurred during this stage.

---

## 0. Red-team verdict in one paragraph

The only surviving candidate, **C3 (UHV/GDC module; load-bearing element the
grounded graphite shield, F16)**, does not withstand the best adversarial case
on the current record. The examiner case (§1) assembles every claim element
from verified references with documented motivation and no rebuttal evidence
of record; the fusion-engineer case (§2) recharacterizes the shield as
facility-hygiene engineering plausibly conceived outside the author list; the
competitor case (§3) shows that even a granted claim would be undetectable,
avoidable at zero cost, and aimed at a market that is standardizing on
different sensor materials anyway. The earlier stages' verbal hedges were
honest, but their operational output — a three-stage `conditional_hold` —
survives only as an inventor-evidence lottery ticket, and §5 finds the ticket
was kept alive partly by inheritance momentum and by two assumptions (implicit
GDC exposure; a "latent" skin-depth delta) that the manuscript does not
support. The steelman (§6) — the narrowest manuscript-supported combination
plus the full G1+G2+G3(+G4/G5) evidence bundle — is coherent but requires
roughly six independent contingent facts to break favorably. Its plausible
commercial scope (§7) does not justify full prosecution on any evidenced
scenario and justifies even a defensive provisional only if the core evidence
bundle materializes essentially immediately. Plainly (§8): this is a
scientifically valuable first demonstration with **no useful patent position
identified from the publication alone**. The arXiv hold survives this
challenge, but only in its bounded, condition-released form, and Stage 70
should time-box it (§5.6).

---

## 1. Skeptical patent examiner: the case against C3

Target: the Stage 40 §6 narrowest combination (in-vessel magnetic sensing
module = AlGaN/GaN die + Al wire bonds + ceramic LCC + EPO-TEK 353ND epoxy +
vacuum bake + zirconia holder + stainless standoff/flange + grounded graphite
shield, in a GDC-exposed vessel; `regular_lsens.tex` L465/L469).

### 1.1 Obviousness: every element and every motivation is on the record

**[I — constructed examiner position, each link cited to a verified source.]**
Under the MPEP 2141/2143 KSR framework (N001,
https://www.uspto.gov/web/offices/pac/mpep/s2141.html — "combining prior art
elements according to known methods to yield predictable results"), a
plausible rejection sketch needs no single all-elements reference:

1. **Base configuration.** N016 (Stevenson et al. 2014,
   https://pubs.aip.org/aip/rsi/article/85/9/093502/362290/, DOI
   10.1063/1.4894209): a 16-element **semiconductor (GaAs) Hall array
   deployed in-vessel** at the stellarator-class CTH device, in a protective
   housing, 12 years before the manuscript. In-vessel semiconductor Hall
   sensing in a non-axisymmetric device, with environmental packaging, is
   taught.
2. **Material substitution.** Swapping GaAs for AlGaN/GaN is a KSR simple
   substitution whose motivation the manuscript itself recites (L451: GaN's
   thermal tolerance) and whose enabling data are the group's **own prior
   publications** (S012, https://doi.org/10.1063/1.5139911, 576 °C; S014,
   https://doi.org/10.1063/1.2201339, independent 2006 precedent). The
   applicant's own introduction reads as the motivation statement.
3. **Package elements.** Ceramic-LCC wire-bond packaging for vacuum service:
   N009 (https://ieeexplore.ieee.org/document/8739428/). EPO-TEK 353ND with a
   150 °C/1 h bake is the **vendor's standard cure** (S022,
   https://www.epotek.com/product/353nd/), independently UHV-qualified by
   LIGO (N007, https://dcc.ligo.org/LIGO-E1300653/public). Ceramic insulating
   mounts and stainless vacuum hardware are generic (Stage 40 §2).
4. **Graphite cover over an in-vessel magnetic diagnostic.** N015 (USH24H,
   1985 DOE, https://patents.google.com/patent/USH24): graphite armor
   enclosing a magnetic flux-loop diagnostic. N017 (W7-X,
   https://iopscience.iop.org/article/10.1088/1361-6587/abc395): in-vessel
   Mirnov coils "covered by graphite wall protection panels" in an operating
   stellarator. Graphite-over-magnetic-diagnostic is standard practice.
5. **Grounding the cover, for arcing.** N006 (US5216690A,
   https://patents.google.com/patent/US5216690A): grounded conductive shield
   suppresses vacuum arc-down — a decades-old general principle. V40-A
   (Dylla et al., PPPL 1979, https://www.osti.gov/servlets/purl/5515925):
   GDC arcing was a known hazard by 1979; floating objects in GDC sit at
   100–200 V relative to the grounded vessel; grounded-vs-floating coupling
   behavior was documented. N017 additionally documents grounding part of an
   in-vessel magnetic diagnostic at a stellarator (coil center tap to vessel
   ground) to prevent DC charging. N008
   (https://www.sciencedirect.com/science/article/abs/pii/S092037961530404X):
   protecting in-vessel components during GDC is a recognized concern with
   documented covers.
6. **No rebuttal evidence of record.** No unexpected result (no
   with/without-shield comparison — F42), no verified teaching away (Stage 40
   §9.2 weakened the float-vs-ground lead at primary source), no evidence of
   long-felt unresolved need, failure of others, or commercial success. The
   secondary-considerations column is empty.

**Calibrated label: obviousness risk high — unchanged from Stages 30/40, but
here stated as the affirmative case rather than a risk.** The Stage 20/30
"saturated gap" (no single reference combining grounded + graphite +
epoxy-encapsulated sensor + GDC purpose; `20_SEARCH_LOG.md` §3) is a novelty
datum only; an obviousness case never needed that reference to exist.

### 1.2 Inherent-result attack on the functional language

**[I.]** The claim's only environment-specific language — "positioned to
reduce arcing and epoxy degradation during GDC and plasma operation" — is a
statement of intended result. Under the MPEP 2112 inherency framing (S004,
https://www.uspto.gov/web/offices/pac/mpep/s2112.html), where the structure
(a grounded conductive low-Z cover over a packaged component in a
discharge-cleaned vessel) is taught or obvious, the recited protective result
is what that structure **necessarily does** — V40-A supplies the mechanism
(grounding pins the surface potential that drives arcs; the cover takes the
ion flux). The functional recital therefore does no distinguishing work: the
examiner strips it, and what remains is the §1.1 combination. **[U:]** a
drafter could convert function into structure (specific grounding-path,
aperture, thickness limitations) — but only with the unpublished G3/G4
material, which leads to §1.3.

### 1.3 Enablement / written-description attack on anything narrower

**[F.]** The shield's entire public disclosure is one sentence (L465) plus
small photographs; no dimensions, apertures, clearances, grounding route,
acceptance criterion, or comparative datum appears in any controlling
artifact (F40–F43, F46, F48). **[I.]** Consequences, stated adversarially:
(a) the publication cannot itself support any claim narrower than the
concept-level combination of §1.1 — and that combination is where the
obviousness case is strongest; (b) every escape route to a narrower,
more defensible claim runs through inventor-held records that this workflow
has not seen and that no artifact proves exist; (c) if those records do not
exist, there is nothing to draft. The candidate is caught in scissors: broad
enough to be supported → obvious; narrow enough to be arguable → unsupported.

### 1.4 Inventorship and origin attack

**[F.]** No artifact states who conceived the shield or when (F44); the
sentence is passive — "a grounded graphite shield **was installed** over the
packaged sensor module" (L465) — and names no originator. **[I — adversarial
scenario, plausible on the record:]** in-vessel hardware at a DOE-funded
facility ordinarily passes through facility vacuum/machine-protection review;
a grounded graphite cover over an organic-potted package is exactly the kind
of condition a facility engineer imposes before allowing epoxy into a
GDC-conditioned vessel (V40-A documents the underlying concern since 1979;
N008 documents GDC-protection practice). If conception sits with HSX staff —
whether the UW-Madison co-authors (G11) or **facility engineers outside the
author list entirely** (G2/G9) — then: (a) the "invention" is facility
practice applied to a guest instrument (routine-engineering
characterization strengthened); (b) Stanford may not control, or may not
solely control, any filing (S003,
https://otl.stanford.edu/researchers/otls-process); (c) the published
author list would diverge from any true inventor list, which is precisely the
scenario MPEP 2153.01(a) flags as requiring "additional evidence" before the
U.S. grace-period exception applies cleanly (Stage 50 §2.1,
https://www.uspto.gov/web/offices/pac/mpep/s2153.html); and (d) if a
non-author conceived it, the shield sentence in the six-author manuscript is
not self-evidently an inventor-originated disclosure at all. **[U:]** this is
a scenario, not a finding — but the burden of disproving it sits entirely on
inventor records that have not been produced. **[A:]** G2/G9/G11 remain the
controlling questions; no filing decision is meaningful before they are
answered.

### 1.5 Evidence-quality attack

**[F.]** GDC exposure of this module is implicit only (F17): the paper never
narrates a GDC event, cycle count, or post-exposure inspection (F46). The
efficacy evidence is 68 shots of survival with, per the manuscript's own
numbers (L496), a ~50 ms flat-top window per shot — **[I, arithmetic]**
≈ 3.4 s cumulative plasma-phase exposure and tens of seconds of coil-field
exposure, in a short-pulse university device, versus 19,000+ pulses over 11+
years for the JET in-vessel Hall system (S016,
https://iopscience.iop.org/article/10.1088/1741-4326/ac8aad). **[I.]** An
examiner or opposer reads the record as: protective function possibly never
exercised (if no GDC ran while the module was installed), demonstrated
environment mild, efficacy asserted by purpose only. Successful
experimentation at this scale supports feasibility, not patentability
(`CLAUDE.md` hard rule).

---

## 2. Experienced fusion-diagnostics engineer: "this is a work order, not an invention"

**[I — constructed practitioner position.]**

- **The shield is what any of us would do, and have done.** Graphite is the
  default low-Z sacrificial material in-vessel (N015, N017); grounding
  anything conductive near a discharge is default electrical hygiene (N006;
  V40-A's floating-potential data are 47 years old); covering delicate
  in-vessel items during GDC is documented practice (N008). Given an
  epoxy-potted package — an organic surface in a discharge whose stated job
  is carbon and oxygen removal (V40-A) — *some* grounded cover is the first
  design meeting's answer, not the last.
- **The G4 "latent delta" is being over-credited.** The skin-depth/bandwidth
  trade-off (Stage 40 §4.4) is a standard EM design consideration for any
  conductive diagnostic housing; W7-X engineering literature already reflects
  the conductive-housing/bandwidth concern for Mirnov systems (lead-grade,
  per Stage 40). More importantly, the manuscript's demonstrated signals are
  coil ramp-up (sub-kHz) and an ignition transient (L496); the 1 MHz figure
  is amplifier bandwidth (F23, L483), not a demonstrated through-shield field
  bandwidth. For those timescales, any plausible few-mm graphite wall is
  simply transparent — no engineered trade-off is needed, so none should be
  presumed. **[U:]** an inventor-held calculation could still exist (G4);
  **[I:]** the probability that a rigorous parameter optimization was done
  but omitted entirely from the paper is low.
- **The demonstration does not qualify the package.** No temperature data
  (F39), no calibration (F38/F47), no noise floor (F45), non-hermetic and
  non-serviceable encapsulation versus the welded housings used for long-life
  systems (S016), radiation behavior explicitly future work (F36). As a
  fusion instrument-package qualification, this is a successful first
  plasma-adjacent bench test — good science, early engineering.
- **Origin skepticism.** Same as §1.4, from the practitioner side: at every
  machine I know, the vacuum group tells the visiting sensor team what may
  enter the vessel and under what covering. The default presumption for a
  guest instrument's GDC armor is facility conception until records show
  otherwise.

---

## 3. Commercial competitor: "we would not even need to notice this patent"

**[I — constructed competitor position.]**

- **Design-arounds are free.** All six Stage 40 §7 routes remain open; N016
  is the existence proof — a fielded in-vessel semiconductor Hall array using
  *none* of C3's elements (boron-nitride-sheathed stainless tube, no epoxy,
  no graphite, no dedicated grounded cover). Ceramic covers (N008), floating
  covers, hermetic welded housings (S016), getter-sealed LCCs (N009),
  wall-panel integration (N017), or simply retracting the probe during GDC
  each avoid the claim.
- **Detection is effectively impossible.** Practice occurs inside a
  competitor's own vacuum vessel; nothing observable from outside
  distinguishes a grounded graphite cover from any other cover. A right that
  cannot be policed prices at approximately zero.
- **The paying market is walking away from the claimed platform.** The
  funded, standardizing fusion-diagnostics programs use InSb (S015/S016),
  bismuth (S018/S020), metal-film (S017), and antimony with diffusion
  barriers as of June 2026 (N018,
  https://iopscience.iop.org/article/10.1088/1361-6587/ae6c59). The GaN Hall
  field itself is active and crowded on the device side (N003, 2025; N004,
  lead-only) — but for *fusion* deployment the manuscript's radiation
  question is explicitly unanswered (F36). A competitor building for
  ITER/DEMO-class service has documented non-GaN paths; a competitor building
  GaN Hall products has no fusion-package need. The claim sits in the empty
  intersection.
- **License value.** What a fusion developer would actually want from this
  group is know-how and collaboration (fab recipe, packaging experience,
  deployment data) — obtainable by consortium agreement or hiring, none of it
  dependent on a patent whose one distinctive element their own vacuum group
  would re-derive in an afternoon. **Calibrated label: standalone licensing
  value ≈ zero; defensive value marginal.**

---

## 4. Stress test of the screened-out groups (C1, C2, C4, C5)

**Was anything killed too quickly? [I] No.** Re-examined against the ledger:

- **C1 (device/fab):** every element is purchased (F01), the group's own
  published prior work (S011/S012 — prior art against this manuscript), or
  routine processing; geometry genus patented across material systems since
  1999 (N014, N013). No revival path exists inside the four corners of this
  paper. Screen-out stands at high confidence.
- **C2 (fusion use):** the *In re May* side of the MPEP 2112.02 fork (S004)
  is correctly applied — the exploited properties are the group's own
  published knowns (S011/S012, recited at L451). Red-team check for an
  overlooked *In re Hack* path: is there any **unknown property** exploited
  in-vessel? None on the record (no radiation datum, no GDC-specific 2DEG
  behavior, no quantified anything — F38/F39/F45/F47). Screen-out stands.
- **C4 (readout):** catalog parts in catalog configurations; the honest
  search-depth limitation (N012 `lead_only`) does not matter because the
  intrinsic record is dispositive — there is no disclosed circuit delta to
  search for. Stands.
- **C5 (validation):** routine commissioning controls (N011); zero
  enforceability. Stands. A hypothetical C2+C3+C5 "system/method" picture
  claim was also re-checked: literal novelty likely, but it inherits C3's
  obviousness core, C5's undetectability, and C2's known-property problem —
  a longer claim, not a stronger one.

**Was any disposition too generous to the filing case? [I] Yes, mildly, in
three places — all in C3's favor, none in the kill decisions:**

1. C2's "novelty risk: medium" for the GaN-in-a-stellarator pairing is
   technically defensible (bounded-search absence) but functionally inert —
   the pairing survives on a GaAs-vs-GaN material label and a
   torsatron-vs-stellarator taxonomy label against N016. Carrying "medium"
   forward risks reading as residual hope; as a use-claim matter the
   effective posture is the high-risk side of the fork.
2. The repeated "saturated gap" formulation for F16, while always footnoted
   as "absence, not novelty evidence," structurally functioned as C3's
   survival basis (see §5.1).
3. G4's rank in the gap register ("strongest latent technical delta") credits
   an engineering calculation whose existence nothing in the record suggests
   (see §2). It is a legitimate inventor question; it is not a pillar.

---

## 5. Confirmation-bias audit of Stages 00–50: unsupported or fragile assumptions

The run converged 00→50 with no internal dissent. The dispositions survive
this audit, but five shared assumptions deserve explicit adversarial
treatment, and one (5.6) changes how Stage 70 should frame the arXiv hold.

### 5.1 Over-reliance on the bounded-search absence

**[F]** Stages 20–40 all correctly labeled the four-way conjunction gap
(grounded + graphite + epoxy-encapsulated sensor + GDC purpose) as "a
documented absence, not evidence of novelty." **[I]** But operationally, the
absence is what kept C3 alive at Stage 30 — remove it and C3 screens out with
the others. The red-team point is statistical: the more specific a
conjunction, the weaker the evidential value of its absence from indexed
literature, because facility packaging engineering lives in internal
drawings, ops reviews, and travelers, not journals or patents. HSX's own
drawing archive (G9) is exactly the un-indexed place where a pre-existing
grounded graphite probe cover would sit. The absence is real; its probative
weight for both novelty and non-obviousness is low; the hold should be
understood as resting **almost entirely on the possibility of inventor-held
evidence, and only cosmetically on the search gap.** Stage 40 §0 already said
nearly this; Stage 70 should say it without the cosmetic layer.

### 5.2 The journal-confidentiality assumption

**[F]** Stage 50 §1.3 treats the 2026-07-02 IEEE submission as
"presumptively confidential," flagged as a norm-based presumption with no
venue-specific verification. **[I]** Two fragilities: (a) the presumption was
never tested against IEEE's own reviewer-confidentiality policy text (not
fetched in any stage — an evidence limitation, not a finding of leakage);
(b) more importantly, the journal pipeline is not the only channel — the
module was built, installed, and operated at a DOE-funded user facility over
a multi-shot campaign, with facility staff, ops reviews, group seminars, and
possibly public shot logs as candidate disclosure surfaces (G10, which Stage
50 correctly called the controlling unknown). **[U]** No artifact shows any
such earlier exposure; none rules it out. **Net:** premise 2 of the hold
("concept not yet confirmed public") is fragile in both directions — if an
earlier exposure exists, foreign options are already gone and the hold's
marginal value collapses to U.S. grace-period bookkeeping. **[A]** The G10
earliest-disclosure inventory is not optional homework; it is the fact that
decides whether the hold is protecting anything.

### 5.3 The GDC-exposure assumption

**[F]** F17 is `implicit` in the disclosure map; no GDC event is narrated
anywhere in the manuscript (F46). **[I]** Stage 40 §4.6 argued the shield was
"*necessary*" because bare epoxy in a GDC vessel is untenable — a physics
argument that quietly assumes GDC actually ran while the module was
installed. If HSX ran no GDC during the module's residence (short campaign;
GDC at many machines is a between-campaign conditioning activity), then:
(a) the shield's core stated function was never exercised; (b) the only
documented "result" is survival of a mild 68-shot plasma campaign; (c) the
already-negative Stage 40 §5 gate answer becomes unambiguous. **[U]**
Resolution requires facility logs (G5). **Direction:** this assumption only
ever cut in C3's favor; the red team removes the benefit of the doubt.

### 5.4 The G4 lifeline

Covered at §2 and §4: the skin-depth trade-off is field-standard, the
manuscript's demonstrated band does not require it, and no artifact hints a
calculation exists. **[A]** Keep G4 on the inventor-question list; strike it
from any weighing of C3's current strength.

### 5.5 Inheritance momentum

**[I]** Each stage individually chose the lowest-regret label
(`conditional_hold`) while stating an expectation of eventual failure. Strung
together, three stages of "hold, but expect it to die" manufactured an
appearance of a persistent candidate that no stage actually believed in.
This is the run's one systematic bias pattern. It changed no disposition —
but Stage 70 must not inherit the hold by momentum: absent the minimum
bundle (G1+G2+G3), the calibrated conclusion already reached at Stage 40 §0
is that no publication-specific filing case survives, and Stage 70 should
say so as its lead finding rather than as a hedge.

### 5.6 Is `HOLD_ARXIV_FOR_OTL` itself defensible? Challenged, then sustained in bounded form

**The attack [I]:** Stages 30/40's own calibrated expectation is that C3
fails. Holding a researcher's preprint — in a fast-moving field where
adjacent groups published GaN Hall work in 2025–2026 (N003; N018 is
four weeks pre-manuscript) and where scientific priority, not patent
priority, is the author's real asset — to protect a candidate everyone
expects to die looks like process for its own sake. The publication itself is
what secures the "first demonstration" credit; delay has a real, uncompensated
career cost and a nonzero scooping cost.

**The defense [I]:** the hold as written survives because of three
asymmetries and one structural feature:
1. **Irrevocability asymmetry.** An arXiv post is permanent and license-
   irrevocable (S006, https://info.arxiv.org/help/license/index.html); a
   short delay is fully recoverable. The expected cost of a bounded delay is
   days; the cost of a wrong post is unbounded in the small set of worlds
   where the evidence bundle exists.
2. **Unresolved ownership.** The decision irrevocably disposes of rights that
   may not be the posting author's alone to dispose of (G2/G11:
   UW-Madison/facility conception scenarios; §1.4). Posting before knowing
   whose rights are affected is the actual risk being managed — this
   justification is independent of whether C3 is patentable.
3. **Sponsor duties are patentability-independent.** Bayh-Dole reporting
   applies "whether or not those inventions are considered patentable"
   (S003, https://otl.stanford.edu/researchers/otls-process); the DOE/SLAC/
   NSF/TomKat and unstated HSX-side terms (L514; Stage 50 §4.1) exist
   regardless of this screen's outcome.
4. **Release condition (b) already caps the cost.** The hold is released by
   an informed PI/author decision *without* OTL completion
   (`50_ARXIV_RISK.md` §6). It is a checkpoint, not a gate on OTL's
   calendar.

**Red-team verdict: the hold survives, with a mandatory reframe. [A]** Stage
70 must present the hold as a **short, time-boxed checkpoint** — put the
intake and the G1–G3/G5/G9–G11 questions to the PI/inventors and OTL, ask
OTL's current response timeline on submission day (Stage 50's own action),
and set an explicit decision date (order of one-to-two weeks, chosen by the
PI, not this workflow) after which release condition (b) is exercised by
default. If the hold is instead operationalized as "wait until the evidence
bundle is assembled," it becomes exactly the unjustified publication delay
the attack describes, because the modal outcome — no filing case — is
already the calibrated expectation. The honest framing to the researcher:
*the most likely result of this checkpoint is a documented "no filing —
clear to post," obtained in days, plus discharge of sponsor-reporting and
inventorship hygiene that is owed anyway.*

---

## 6. Steelman: the narrowest combination that might survive, and what must be true

### 6.1 The steelman itself

**[I — best genuine case, not a drafted claim.]** The invention story with
the best chance is the **system-level economic insight**, not any single
part: *commodity, non-hermetic, epoxy-grade sensor packaging — ordinarily
excluded from discharge-cleaned vessels — is made GDC-compatible by adding a
sacrificial, electrically grounded, low-Z conductive cover, trading a
welded-hermetic housing (S016-style) for a disposable potted module plus a
facility-standard shield.* The narrowest manuscript-supported embodiment is
exactly Stage 40 §6 (all elements at L465/L469): AlGaN/GaN die, Al-wire
bonds, ceramic LCC, low-outgassing epoxy + vacuum bake, insulating zirconia
holder on a grounded-structure standoff, and a grounded graphite shield over
the module, in a GDC-operated magnetic-confinement vessel. The strongest
*claimable* version would add a functional-structural limitation only G4
evidence could support: cover conductivity/thickness selected to pin surface
potential during GDC **while** passing the magnetic-field measurement band.

### 6.2 What would have to exist (all inventor-held; none currently in evidence)

1. **G1** — a dated no-shield failure/arcing/epoxy-damage record or any
   with/without comparison (the only realistic unexpected-result or
   problem-recognition evidence; F42).
2. **G2** — conception records naming identifiable inventors, with dates and
   rationale, showing the shield was designed for this module rather than
   inherited (F44).
3. **G3** — enabling drawings: geometry, apertures, clearances, grounding
   route (F40/F41).
4. Strongly reinforcing: **G5** (GDC exposure logs + intact-epoxy
   inspection — proves the function was exercised) and **G4** (the
   conductivity/thickness/bandwidth calculation — converts a generic cover
   into an engineered parameter choice).
5. Non-events that must also hold: **G9** negative (not pre-existing HSX
   practice), **G8** negative (W7-X panels not grounded), and no earlier
   public exposure (**G10**).

**[I — calibrated assessment:]** roughly six independent contingencies must
all break favorably. Even in the all-favorable world, the claim remains
narrow (one packaging pattern in GDC-operated vessels), obviousness risk
falls only from high to medium (G1/G4 supply a documented problem–solution
narrative and a non-arbitrary parameter, not a surprising result), and
enforceability remains near zero. **Probability-weighted, this is a weak
candidate even fully steelmanned.**

## 7. Filing economics: does the plausible scope justify the expense?

**[I, with cost statements kept qualitative — no ledger source prices legal
services, and no figure is invented.]**

- **Scope if granted (steelman world):** one narrow packaging claim,
  practiced (if ever) inside research and private fusion developers' vacuum
  vessels. Practitioner population: dozens of institutions worldwide.
  Detection: effectively impossible (§3). Design-around cost to any
  practitioner: near zero (§3; N016). Licensing demand: none identified —
  the value a partner would pay for is know-how, not the claim.
- **Provisional route:** USPTO provisional filing fees are modest (current
  USPTO fee schedule,
  https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule;
  tier depends on entity status); the real costs are attorney/OTL drafting
  effort and the forced conversion decision at 12 months. A provisional is
  rationally defensible **only** if the G1+G2+G3 bundle surfaces essentially
  immediately (within the pre-posting checkpoint window) — it then buys 12
  months of optionality at low cost while the paper posts freely. Absent the
  bundle, a provisional would memorialize a one-sentence concept with no
  enabling detail and no non-obviousness evidence: optionality on nothing.
- **Full prosecution:** non-provisional drafting, examination, and
  maintenance costs are, as an order of magnitude, one to two decimal orders
  above provisional filing fees over the asset's life (general practitioner
  knowledge, order-of-magnitude only, labeled as such — no precise figure
  asserted). Against a claim with ≈zero enforceable and ≈zero licensable
  value, **full prosecution is not justified on any scenario evidenced in
  this record, including the full steelman.**
- **Bottom line [A]:** recommend to Stage 70: no filing recommendation from
  the publication record; a defensive provisional only as a contingent
  option if the inventor-evidence bundle appears during the checkpoint
  window and OTL judges the drafting cost acceptable; no scenario supporting
  full prosecution economics.

## 8. The plain statement

**[I, stated without hedging:]** This manuscript reports a genuine and
useful scientific first — on the verified record, the first GaN-based
Hall-effect deployment inside a stellarator-labeled device (bounded-search
finding, `20_SEARCH_LOG.md` §1; nearest miss N016, GaAs, stellarator-class
CTH, 2014). That achievement is real, publishable, and career-relevant.
**It does not translate into a useful patent position.** The device is the
group's own published prior art; the use exploits known, group-published
properties; the readout is catalog electronics; the validation is standard
commissioning practice; and the one candidate element with any residual
life — the grounded graphite shield — is, on everything now verified, a
predictable assembly of 40-year-old fusion-engineering practices whose
public disclosure is a single unquantified sentence. Scientific priority
here is best protected by publishing promptly and visibly. Patent priority,
on this record, has nothing of value to attach to. These two facts are
compatible, and the recommendation machinery should stop treating the second
as a deficiency of the first.

## 9. Decisive facts that would change this outcome

**Toward a real filing case (any materially helps; 1–3 are the minimum
bundle):**
1. A dated HSX incident/log record of arcing or epoxy damage on an
   unshielded in-vessel package (G1).
2. Conception records naming inventors, dates, and design rationale for the
   shield (G2).
3. Enabling drawings including the grounding route (G3).
4. A shield conductivity/thickness/bandwidth design calculation (G4).
5. GDC exposure logs with post-campaign intact-epoxy inspection (G5).
6. A verified facility document teaching *floating* diagnostics for
   protection during GDC — genuine teaching-away (G7; currently weakened by
   V40-A).

**Toward final screen-out / hold release (any one materially; two should end
the matter):**
7. Confirmation the shield was pre-existing HSX hardware/practice or
   specified by facility staff (G9/G2).
8. Confirmation W7-X's graphite panels are grounded (G8 — the single
   cheapest external check still open; paywalled 2013 companion paper,
   ScienceDirect PII S0920379613005279).
9. Confirmation no GDC ran during the module's in-vessel residence (G5
   negative).
10. Any pre-submission public exposure of the module/shield — ops review
    slides, seminar, poster, thesis, webpage (G10).
11. A documented, informed PI/author decision to post (release condition (b),
    `50_ARXIV_RISK.md` §6).

## 10. Gate compliance and limitations

- **Best examiner/competitor case against each surviving candidate:** C3 is
  the only surviving candidate (Stage 30 §7); §§1–3 argue the examiner,
  practitioner, and competitor cases against it; §4 re-attacks the four
  screened-out groups and confirms no premature kill.
- **Unsupported assumptions identified:** §5.1–5.5 (bounded-search absence
  weight; journal-confidentiality presumption; implicit GDC exposure; G4
  lifeline; inheritance momentum), each with direction-of-error stated.
- **Narrowest plausible surviving combination:** §6.1, with explicit
  survival conditions (§6.2).
- **Commercial scope vs. filing expense:** §7, answered plainly (no full
  prosecution on any evidenced scenario; provisional only as a contingent,
  evidence-triggered option).
- Fact/inference/uncertainty/action are labeled throughout; calibrated
  research labels only; no legal conclusions, no FTO or exhaustive-search
  claim; adversarial positions are marked as constructed.
- Material propositions carry ledger source_ids with URLs (S004, S006,
  S016–S018, S022, N001, N003, N005–N009, N011–N018, V40-A, S001–S003) and
  `regular_lsens.tex` line cites re-verified this session.
- Excluded concepts (`IP_SCOPE.md`) were not evaluated as manuscript IP; the
  design-around discussion reuses only Stage 40 §7's previously published
  alternatives and invents no new package design as a disclosed invention.
- Bounded-search caveats inherited from `20_SEARCH_LOG.md` apply to every
  absence-based statement; G8 and G10 remain open.
- No external communication, submission, upload, or manuscript modification
  was performed. `state/` was not modified by this stage agent (per the
  orchestrator's instruction, state updates are the orchestrator's task).

## 11. Handoff to Stage 70

Recommended framing for the final brief, from this red team: lead with
`NO_PUBLICATION_SPECIFIC_FILING_CASE_IDENTIFIED` **unless** the G1+G2+G3
bundle has actually been produced by then, while retaining the bounded,
time-boxed pre-posting OTL checkpoint of §5.6 (whose justification is
irrevocability, unresolved inventorship/ownership, and patentability-
independent sponsor duties — not C3's prospects). The three user questions
resolve as: (1) Hall device — no case (C1, §4); (2) fusion-diagnostic use —
no standalone case (C2, §4); (3) UHV/GDC package — no case on the public
record; contingent narrow case only if inventor evidence per §6.2 exists
(C3, §§1–3, 6–7).
