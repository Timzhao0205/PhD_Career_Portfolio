# Stage 70 — Final OTL Decision Brief

## 0. Decision

### `NO_PUBLICATION_SPECIFIC_FILING_CASE_IDENTIFIED`

Run: HSXIP-20260805T071311Z. Date: 2026-08-05. Scope authority: `IP_SCOPE.md`,
`CLAUDE.md`, `schemas/OUTPUT_GATES.md` (§70 gate). This brief synthesizes the
accepted outputs of Stages 00–60 and resolves their conflicts; it does not
re-run their research. Companion documents: `outputs/70_EXEC_SUMMARY.md` (one
page) and `outputs/70_MODEL_REPORT.md` (model/effort audit). Provenance:
authored by the stage-70 agent under requested configuration Fable 5/xhigh;
observed model telemetry `not_exposed` (see the model report).

**What this document is and is not.** This is the accepted final synthesis of a
research-grade patentability *triage* and pre-arXiv disclosure review. It is
**not legal advice, not a patentability or validity opinion, not a
freedom-to-operate (FTO) opinion, and not an exhaustive search**. It makes no
filing decision — that belongs to the PI, the inventors, Stanford OTL (and, if
applicable, UW-Madison's technology-transfer office), and counsel. Fact,
inference, uncertainty, and action are distinguished throughout; risk labels
are calibrated research judgments, not legal conclusions.

**Rationale (one paragraph).** After a saturated bounded search (22/22 seeds
verified, 18 added sources, one primary source added at Stage 40), a five-group
IP screen, a packaging deep-dive, and an adversarial red team, no element of
this publication supports a useful patent position on the public record. The
Hall device and its fabrication are the authors' own published 2019/2020 prior
art plus purchased and routine inputs (S011, https://doi.org/10.1109/JSEN.2019.2895546;
S012, https://doi.org/10.1063/1.5139911); the fusion-diagnostic use exploits
known, group-published properties of a known device — the *In re May* side of
the MPEP 2112.02 new-use fork (S004,
https://www.uspto.gov/web/offices/pac/mpep/s2112.html) — against a field with
documented in-vessel semiconductor Hall deployments since at least 2005
(S015, https://doi.org/10.1063/1.2018628; N016,
https://pubs.aip.org/aip/rsi/article/85/9/093502/362290/); the readout is
catalog electronics; the validation is standard commissioning practice (N011,
https://iopscience.iop.org/article/10.1088/1741-4326/adaed0); and the single
surviving candidate — the grounded graphite shield of the UHV/GDC module (C3,
F16) — is, on everything verified, a predictable assembly of documented
fusion-engineering practices (V40-A 1979 PPPL GDC report,
https://www.osti.gov/servlets/purl/5515925; N006,
https://patents.google.com/patent/US5216690A; N015,
https://patents.google.com/patent/USH24; N017,
https://iopscience.iop.org/article/10.1088/1361-6587/abc395) whose entire
public disclosure is one unquantified sentence (`regular_lsens.tex` L465), with
no unexpected result, no with/without comparison, and no enabling detail on
record. A narrow contingent case for C3 exists only if inventor-held evidence
(G1+G2+G3, §7) materializes; none has been produced. This label states the
patentability-triage outcome; it does **not** by itself clear an arXiv posting
— a short, time-boxed pre-posting checkpoint remains warranted on grounds
independent of patentability (§0.1, §4).

### 0.1 How this label relates to the arXiv gate — explicit and unambiguous

Two different questions were decided by two different stages, and both answers
stand because they answer different things:

- **Stage 70 decision label (this document):** *Is there a
  publication-specific filing case?* Answer: **no case identified** on the
  current record (above). This resolves — rather than averages — the apparent
  conflict between Stage 50 and Stage 60: Stage 30/40's `conditional_hold` on
  C3 was, per the Stage 60 audit (60_RED_TEAM.md §5.5), sustained partly by
  inheritance momentum; the calibrated expectation every stage actually held
  (Stage 40 §0) is adopted here as the lead finding, not a hedge.
- **arXiv gate condition (Stage 50's `HOLD_ARXIV_FOR_OTL`, as reframed by
  Stage 60 §5.6 and adopted here):** *Should the researcher post to arXiv
  today, before anyone with authority has looked?* Answer: **not today — hold
  briefly, as a time-boxed checkpoint with a default release**, because three
  justifications survive even with no filing case: (1) an arXiv post is
  permanent and its license irrevocable (S006,
  https://info.arxiv.org/help/license/index.html) while a short delay is fully
  recoverable; (2) posting irrevocably disposes of rights that may not be the
  posting author's alone to dispose of — shield conception may sit with
  UW-Madison co-authors or HSX facility staff outside the author list entirely
  (G2/G9/G11, §8); and (3) sponsor duties are patentability-independent —
  Stanford must report federally funded inventions under Bayh-Dole "whether or
  not those inventions are considered patentable" (S003,
  https://otl.stanford.edu/researchers/otls-process).

**In one sentence:** *no filing case was identified, and the recommended
pre-posting checkpoint exists to confirm ownership and discharge sponsor
duties — not to protect C3's filing prospects.* The exact hold/release
condition is in §4. If the checkpoint were instead operationalized as "wait
until the evidence bundle is assembled," it would become an unjustified
publication delay (Stage 60 §5.6); it is not so operationalized here.

**Why not the other labels.** `OTL_REVIEW_BEFORE_ARXIV` would overstate C3: it
would present OTL a candidate whose own record shows high obviousness risk,
thin enablement, and near-zero enforceable value, contradicting Stages 40/60.
`INSUFFICIENT_EVIDENCE_PAUSE` would be wrong because the evidence is
sufficient to decide the triage question asked: every coverage area reached
documented saturation or a documented, explicitly-carried limitation (§9); the
facts that remain unknown (G1–G3, G5, G8–G11) are inventor/facility-held facts
that no further search by this workflow could produce, and their absence *is*
the finding — a case that exists only if unseen records exist is not an
identified case.

---

## 1. Separation of questions (read this before acting on anything below)

This package keeps four decisions separate; conflating them is the main way
this brief could be misused:

1. **Patentability triage (done here):** no publication-specific filing case
   identified. A screen, not an opinion.
2. **FTO (not done):** no clearance search was performed and no FTO opinion is
   given. Two third-party patents were flagged for awareness only, without
   analysis: S009 (US11137310B2,
   https://patents.google.com/patent/US11137310B2/en — claim 1 requires
   simultaneous temperature measurement, which the manuscript's device does not
   perform on the record read) and N013 (US10809318B2,
   https://patents.google.com/patent/US10809318B2/en — octagon-geometry
   dependent claim in silicon CMOS, recorded expiry 2036). Google Patents
   status labels are not legal conclusions. Commercialization of anything
   would need its own clearance work.
3. **Ownership/inventorship (open):** unresolved questions listed in §8. These
   are not blocked by, and do not wait on, the triage outcome.
4. **Filing and posting decisions (not this workflow's to make):** the PI and
   OTL decide; §4 gives the recommended mechanism and default.

---

## 2. The three questions, answered directly

### 2.1 Q1 — Can the disclosed AlGaN/GaN Hall sensor itself plausibly be patented now? **No.**

- **Manuscript feature (fact):** purchased NTT-AT AlGaN/GaN heterostructure;
  mesa etch; Ti/Al/Mo/Au 850 °C/35 s anneal; 7 nm Al2O3 passivation; Ti/Au
  bond metal; 5×5 mm die; regular octagonal plate, 200 µm inscribed diameter
  (`regular_lsens.tex` L457; F01–F09).
- **Evidence:** the manuscript itself cites the geometry to the group's own
  2019 paper (ref10 = S011) and the anneal recipe and 576 °C characterization
  to its own 2020 paper (ref11 = S012) — both public for 6–7 years and prior
  art against this manuscript; the heterostructure is a commercial input.
- **Closest prior art:** S009 (US11137310B2) — AlGaN/GaN micro-Hall sensor
  with bias/Hall terminal sets plus simultaneous temperature measurement; S010
  (US8026718B2, https://patents.google.com/patent/US8026718B2/en) — GaN/AlGaN
  Hall composition/fabrication, priority 2007; S014
  (https://doi.org/10.1063/1.2201339) — independent AlGaN/GaN high-temperature
  Hall sensors, 2006; N013/N014
  (https://patents.google.com/patent/US6639290B1/en) — octagon/regular-polygon
  Hall geometry patented across material systems since 1999.
- **Delta:** none attributable to this manuscript. The only delta against
  S009's claim is a subtraction (no temperature function) — an FTO-side
  observation, not new subject matter.
- **Uncertainty:** low. The dispositive references are the group's own cited
  publications plus verified claim text. Bounded-search caveat: an unpublished
  pre-2019 group filing was searched for by inventor name and not found (an
  absence, not proof).
- **Practical value:** none identified from this publication.
- **Recommended action:** none for the device from this paper. (Confidence:
  high. Stage 30 §2; Stage 60 §4 confirmed no premature kill.)

### 2.2 Q2 — Does use as a stellarator/fusion magnetic diagnostic support a meaningful new-use case? **No — not as a standalone case.**

- **Manuscript feature (fact):** in-vessel deployment near the HSX plasma
  edge, 68 consecutive shots, 200 V/V / 1 MHz readout; the "first GaN-based
  Hall-effect sensor deployed inside a stellarator" claim appears only in the
  cover letter (`submission.pdf` p.9), not the peer-reviewed body (F25–F32,
  F49–F51).
- **Evidence:** the properties exploited in-vessel — 2DEG Hall sensitivity and
  thermal tolerance to 576 °C — are known, published properties, published by
  this same group (S011/S012) and recited as motivation in the manuscript's
  own introduction (L451). Under MPEP 2112.02 (S004), a use claim survives
  (*In re Hack*) only if it exploits a previously **unknown** property; using
  a known device for its inherent, known response in a new location is the
  *In re May* side of the fork.
- **Closest prior art:** in-vessel semiconductor Hall deployments are
  established — InSb edge-plasma arrays since 2005 (S015), the JET in-vessel
  InSb system with 19,000+ pulses over 11+ years (S016,
  https://iopscience.iop.org/article/10.1088/1741-4326/ac8aad), a GaAs Hall
  array inserted in-vessel at the stellarator-class CTH device in 2014 (N016),
  and active bismuth/metal/antimony programs for ITER/DEMO (S017, S018, N018,
  https://iopscience.iop.org/article/10.1088/1361-6587/ae6c59). HSX's own
  pre-existing magnetics contained no Hall probe (S021,
  https://doi.org/10.1088/0029-5515/55/11/113012).
- **Delta:** literal novelty of the narrow pairing "GaN Hall sensor inside a
  stellarator" survives the bounded search (a documented absence, not proof of
  novelty) — but it rests on a GaAs-vs-GaN material label and a
  torsatron/hybrid-vs-stellarator taxonomy label against N016, and the
  substitution reads directly onto the KSR simple-substitution rationale
  (N001, https://www.uspto.gov/web/offices/pac/mpep/s2141.html) with the
  motivation stated in the authors' own introduction. No unexpected result is
  on record (no calibration, no noise floor, no temperature or radiation datum
  from this deployment — F38/F39/F45/F47). Sixty-eight-shot survival is
  successful experimentation, which under this project's rules does not
  support patentability.
- **Uncertainty:** high confidence on the doctrinal disposition (the
  known-property record is the group's own); medium on the literal-pairing
  novelty sub-finding (bounded search; N004 date unresolved, `lead_only`).
- **Practical value:** the scientific first is real and career-relevant
  (Stage 60 §8); the standalone use claim is not — tiny practitioner
  population, near-zero detectability, easy design-arounds (any established
  fusion Hall material).
- **Recommended action:** protect scientific priority by publishing promptly
  once §4's checkpoint completes. No standalone use filing. A use limitation
  could at most have served as a contextual element of a C3 claim, which
  itself did not survive (§2.3). (Stage 30 §3; Stage 60 §4 — the "medium"
  novelty label is functionally inert and should not be read as residual
  hope.)

### 2.3 Q3 — Is the epoxy/bake/ceramic/grounded-graphite UHV/GDC module worth OTL review, or likely too routine/thin? **Too routine/thin to present as a filing candidate on the public record — but include it in the checkpoint intake anyway, because sponsor-reporting duty does not depend on patentability.**

- **Manuscript feature (fact):** Al wire bonds to a ceramic LCC; EPO-TEK 353ND
  encapsulation; 150 °C/1 h vacuum bake; custom zirconia holder; stainless
  standoff and insertion flange; "a grounded graphite shield was installed
  over the packaged sensor module" "[t]o reduce the risk of arcing and epoxy
  degradation during glow discharge cleaning (GDC) and plasma operations"
  (L465, L469; F10–F17). The shield's entire public disclosure is that one
  sentence plus small photographs.
- **Evidence:** six of seven elements are individually conventional,
  manufacturer-directed, or industry-standard — the bake exactly matches the
  vendor's standard cure schedule (S022, https://www.epotek.com/product/353nd/),
  the epoxy was independently UHV-qualified by LIGO years earlier (N007,
  https://dcc.ligo.org/LIGO-E1300653/public), and ceramic-LCC vacuum packaging
  is established practice (N009, https://ieeexplore.ieee.org/document/8739428/)
  (Stage 40 §§2–3: the "epoxy plus bake alone is routine" gate test is
  answered affirmatively).
- **Closest prior art (for the shield, the only load-bearing element):**
  graphite covers over in-vessel magnetic diagnostics are standard (N017 —
  W7-X Mirnov coils under graphite wall-protection panels; N015 — 1985 DOE
  graphite armor enclosing a flux-loop diagnostic; N005 — US4858817A
  graphite-ceramic fusion shield); grounding a conductive shield to suppress
  vacuum arcing is a decades-old principle (N006); GDC arcing, 100–200 V
  floating potentials, and grounded-vs-floating coupling were documented at
  PPPL in 1979 (V40-A); protecting in-vessel components during GDC is
  recognized practice (N008,
  https://www.sciencedirect.com/science/article/abs/pii/S092037961530404X).
  Every link of the KSR chain is supported by a verified source; the one
  teaching-away lead (float-for-protection during GDC) was tested at primary
  source and weakened, not confirmed (Stage 40 §9.2).
- **Delta:** the exact four-way conjunction (grounded + graphite + protecting
  an epoxy-encapsulated solid-state sensor + against GDC/plasma arcing and
  epoxy degradation) was not found — a saturated bounded-search **absence**
  whose probative weight is low, because facility packaging engineering lives
  in internal drawings and ops records, not indexed literature (Stage 60
  §5.1). No unexpected result, no with/without comparison, no failure-mode
  narrative, no geometry/grounding detail is on record (F40–F43, F46); GDC
  exposure of this module is implicit only and may never have occurred during
  its residence (F17; Stage 60 §5.3). The candidate is caught in the Stage 60
  scissors: broad enough to be supported → obvious; narrow enough to argue →
  unsupported by the one-sentence disclosure.
- **Uncertainty:** medium — inventor-held records (G1–G5, G9) could still move
  this in either direction; nothing seen so far suggests they exist.
- **Practical value:** modest-to-nil — in-vessel practice is effectively
  undetectable, design-arounds are free and already fielded (N016's
  boron-nitride/stainless housing uses none of C3's elements), and the funded
  fusion-diagnostics programs are standardizing on non-GaN materials
  (S016/S017/S018/N018). Stage 60 §7: full prosecution is not justified on any
  evidenced scenario; a defensive provisional is rational only if G1+G2+G3
  surface within the checkpoint window.
- **Recommended action:** do **not** present C3 to OTL as a substantive filing
  candidate; do include it — candidly framed exactly as in
  `outputs/50_OTL_INTAKE.md` §1 — in the checkpoint conversation, because (a)
  Bayh-Dole reporting applies regardless of patentability (S003), (b) the
  conception/ownership questions must be answered before an irrevocable
  posting anyway (§8), and (c) if the G1+G2+G3 bundle unexpectedly
  materializes, OTL can weigh a low-cost provisional inside the window.

---

## 3. Concept ranking

| Rank | Concept | Basis | Confidence |
|---|---|---|---|
| **Strong** | — none — | No concept on this record supports a filing case | — |
| **Conditional** | C3 UHV/GDC module (shield F16 as load-bearing element) | Contingent narrow case **only if** inventor-held G1+G2+G3 evidence exists; roughly six independent contingencies must all break favorably, and even fully steelmanned the obviousness risk falls only to medium with ≈zero enforceability (Stage 60 §6). Default expectation: no case. | medium |
| **Weak (screened out)** | C2 fusion/stellarator use | Literal narrow-pairing novelty survives the bounded search but is functionally inert; *In re May* known-property problem; KSR substitution with self-recited motivation | high (doctrine) / medium (pairing) |
| **Weak (screened out)** | C1 Hall device/fabrication | Group's own published prior art + purchased/routine inputs; generic geometry genus (N013/N014) | high |
| **Weak (screened out)** | C4 readout chain | Catalog parts in catalog configurations; no disclosed circuit delta; search-depth limitation carried honestly (§9) | medium |
| **Weak (screened out)** | C5 deployment/validation method | Routine commissioning controls (N011); ≈zero enforceable value | high |
| **Excluded (by scope — never evaluated as manuscript IP)** | Three-axis/vector probes; Hall+coil hybrids; current-spinning/radiation-compensation/self-calibration; TCAD/simulation; startup concepts; future-PhD directions; the future-work items themselves (absolute calibration, radiation characterization, lower-noise readout — F33–F37); any package design invented during this analysis | `IP_SCOPE.md` exclusions; future-work sentences are context, not inventions | n/a |

---

## 4. The arXiv gate: exact hold and release condition

**Hold (inherited from Stage 50, reframed per Stage 60 §5.6, adopted here):**
Do not post this manuscript — or any version substantively disclosing the C3
concept (the L465 shield sentence) — to arXiv or any other public preprint
server until one of the release conditions below is met. The hold does not
extend to C1/C2/C4/C5 content in the abstract (no hold attaches to them), does
not instruct anything about the already-submitted IEEE manuscript, and is
**not** conditioned on assembling the evidence bundle.

**Checkpoint mechanics (the "time-box"):**
1. On day 0 (within 48 hours), the PI sets an explicit **decision date** —
   order of one to two weeks out; the date is the PI's choice, not this
   workflow's — and the intake (`outputs/50_OTL_INTAKE.md`) plus the §7
   question list go to the co-authors, relevant HSX staff, and Stanford OTL.
2. On submission day, ask OTL directly what its current initial-response
   timeline is (verified guidance: an OTL licensing manager makes contact
   "[s]hortly after" submission — https://doresearch.stanford.edu/how-to/disclose-invention
   — but no business-day figure is published; do not assume one).
3. At the decision date, the default applies.

**Release conditions (any one suffices; letters match `50_ARXIV_RISK.md` §6):**
- **(a)** OTL completes intake and either affirmatively clears posting or
  files a provisional (after which posting the same content is no longer
  novelty-destroying for that filing).
- **(b) — the default at the decision date:** a documented, informed PI/author
  decision to post without an OTL filing, made with the §7 evidence-gap list
  and §8 sponsor/inventorship questions in hand. Given this brief's decision
  label, **condition (b) is the expected and recommended exit** absent
  surprises; the modal outcome of the checkpoint is a documented "no filing —
  clear to post," obtained in days, plus discharge of sponsor-reporting and
  inventorship hygiene that is owed anyway.
- **(c)** documented confirmation that the shield concept was already public
  through an earlier independent channel (G10) — in which case the marginal
  risk of posting is much reduced and any grace-period clock is already
  running from that earlier date (a fact for OTL/counsel, not this workflow).

**What posting requires regardless of the gate (source hygiene, from
`50_SOURCE_SCRUB.md`):** strip `regular_lsens.aux`, `.log`, `.synctex.gz`, and
the ZIP's own `regular_lsens.pdf` (this also removes the local-path privacy
leak, and matches arXiv's own rules — S007,
https://info.arxiv.org/help/submit_tex.html); resolve the `.eps`/converted-PDF
figure duplication with a clean recompile; make a deliberate decision on the
graphical abstract; never upload `submission.pdf` or the cover letter in any
form (its F49–F51 "first"/sensitivity claims are unsupported by the paper's
own data); obtain coauthor approval of the exact arXiv file set; choose the
arXiv license deliberately (irrevocable per version — S006); and, if the paper
is later accepted by IEEE, update the arXiv record per IEEE policy (verified:
IEEE permits arXiv posting before/during/after submission and does not treat
it as prior publication —
https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/post-publication-policies/).
The IEEE venue relationship is not a reason to hold; the checkpoint reasons
are those in §0.1 only.

---

## 5. 48-hour actions (prioritized)

1. **PI sets the checkpoint decision date** (one to two weeks out, PI's
   choice) and adopts release condition (b) as the default exit (§4).
2. **Circulate the question list:** send §7's G-questions — highest priority
   G2/G9/G11 (who conceived the shield; pre-existing HSX practice?; UW-Madison
   contribution), G10 (earliest-disclosure inventory: talks, posters, ops
   reviews, theses, webpages), G5 (did GDC actually run during the module's
   residence?), and G1 (any no-shield failure/arcing/epoxy-damage record) — to
   all six co-authors and the relevant HSX operations/vacuum staff.
3. **Open the OTL conversation:** the PI/inventors review
   `outputs/50_OTL_INTAKE.md`, transfer its content into Stanford's own
   Invention and Technology Disclosure Form via the Researcher Portal (S003),
   and ask OTL's current initial-response timeline the same day. Frame C3
   candidly per §2.3 — this is a reporting/ownership conversation, not a
   filing pitch. (The researcher submits; this workflow transmits nothing.)
4. **Establish the IEEE review status** of the 2026-07-02 submission
   (submitted/revising/accepted) — it sets which IEEE posting obligations
   attach and how much calendar pressure exists.
5. **Start the mechanical source scrub** (§4 hygiene items) so that a
   release-condition-(b) exit can be executed the same day it is reached.

## 6. One-week actions

1. **Collect G-answers** as they return; if — against expectation — G1+G2+G3
   all materialize, put the bundle to OTL immediately and let OTL weigh a
   defensive provisional inside the window (Stage 60 §7: the only scenario in
   which any filing spend is rational; full prosecution is not justified on
   any evidenced scenario).
2. **Close G8 cheaply if convenient** (library access to the paywalled 2013
   W7-X Mirnov thermal-analysis paper, ScienceDirect PII S0920379613005279, or
   an IPP author query): panels-confirmed-grounded would end the C3 question
   outright; it matters only if the evidence bundle shows signs of life.
3. **If G11 indicates UW-Madison contribution,** open the parallel contact
   with UW-Madison's technology-transfer office and ask OTL about
   inter-institutional handling (§8).
4. **Obtain coauthor approval of the exact arXiv file set** (distinct from the
   journal-submission approval already on record).
5. **At the decision date, execute:** default — document the informed PI
   decision (condition (b)), post the scrubbed source set, and record the
   posting date for the sponsor/OTL file; alternative — condition (a) if OTL
   has acted first.
6. **Optional author decision (not a workflow requirement):** consider
   softening the introduction's categorical claim that conventional Hall
   platforms "cannot be deployed near the plasma edge" (L451), which sits in
   tension with verified InSb/GaAs in-vessel deployments (S015/S016/N016) —
   an accuracy nuance only; it played no role in the gate decision.

---

## 7. Evidence-request list (G1–G11, with Stage 60 adjustments applied)

Full register with directions and thresholds: `outputs/40_EVIDENCE_GAPS.md`;
candid OTL-facing restatement: `outputs/50_OTL_INTAKE.md` §2.

| ID | Ask (short form) | Why it matters | Stage 60 adjustment |
|---|---|---|---|
| G1 | Documented no-shield failure/arcing/epoxy-damage event; any with/without comparison | The only realistic unexpected-result path (F42) | Unchanged — part of the minimum bundle |
| G2 | Shield conception records: who/when/why, notebooks, e-mails, CAD | Controls inventorship, which institution leads, and the routine-practice question (F44) | Unchanged — minimum bundle |
| G3 | Drawings: geometry, thickness, apertures, clearances, fastening, grounding route | Cures the enablement deficit; nothing narrower is draftable without it (F40/F41) | Unchanged — minimum bundle; note this detail is unpublished, with disclosure-timing consequences for OTL to manage |
| G4 | Conductivity/thickness/bandwidth design calculation | Would convert a generic cover into an engineered parameter choice | **Struck from any weighing of C3's current strength** (Stage 60 §5.4: field-standard consideration; demonstrated signal band does not require it; nothing suggests the calculation exists) — **kept as an inventor question only** |
| G5 | GDC exposure logs + post-campaign inspection | Determines whether the protective function was ever exercised; benefit of the doubt withdrawn at Stage 60 §5.3 | Now treated as an open question cutting against C3 until answered |
| G6 | HSX UHV acceptance criterion and qualification records for the bake | Record quality only; cannot rescue epoxy/bake as a candidate (vendor-standard cure, S022) | Unchanged, minor |
| G7 | Any facility doc prescribing *floating* diagnostics during GDC for protection | Only surviving teaching-away route; tested and weakened at primary source (V40-A) | Unchanged — currently unsupported |
| G8 | Are W7-X's graphite panels themselves grounded? (2013 companion paper, paywalled) | Cheapest external fact that could end C3 (grounded → near-complete analog) | Unchanged — still open |
| G9 | Was the shield pre-existing HSX/standard facility practice? | Pre-existing → screen-out plus prior-use questions; also an ownership fact | Unchanged — a controlling question |
| G10 | Earliest disclosure of shield/module to anyone without confidentiality duties | Decides whether the checkpoint is protecting anything and when any grace clock started; the run's single biggest unknown | Elevated (Stage 60 §5.2): "not optional homework" |
| G11 | UW-Madison (Goodman/Gallenberger/Geiger) contribution statement | Inventorship + which sponsor terms and which OTL control | Unchanged — controlling for ownership |

**Thresholds (unchanged from Stage 40 §2, adopted by Stage 60):** G1+G2+G3 is
the minimum bundle to present C3 as a substantive (still narrow) candidate.
Any one of G5-negative (no real GDC exposure), G8-grounded, or G9-preexisting
independently ends the matter; two should end it without further inventor
effort.

---

## 8. Inventorship and sponsor questions (for the PI/OTL conversation; none answered here)

**Inventorship — authorship is not inventorship** (S002,
https://otl.stanford.edu/patent: inventorship follows conception of the
claimed idea, "not ... authorship or institutional role"):

- Who conceived the grounded graphite shield, its grounding route, and its
  placement, and when? The manuscript's sentence is passive ("was installed",
  L465) and names no originator (F44).
- **The facility-conception scenario (Stage 60 §1.4 — a scenario, not a
  finding):** in-vessel hardware at a DOE-funded user facility ordinarily
  passes facility vacuum/machine-protection review; a grounded graphite cover
  over an organic-potted package is exactly the kind of condition a facility
  engineer imposes. If conception sits with UW-Madison co-authors or with HSX
  staff outside the author list entirely, then the "invention" may be facility
  practice applied to a guest instrument, Stanford may not (solely) control
  any filing, and the published disclosure may not be self-evidently
  inventor-originated.
- **MPEP 2153.01(a) authorship nuance** (verified verbatim at
  https://www.uspto.gov/web/offices/pac/mpep/s2153.html): the U.S. one-year
  grace period applies cleanly when the publication is "readily apparent" as
  inventor-originated. A publication whose author list is **larger** than the
  eventual application's inventor list is treated as *not* readily apparent —
  requiring additional evidence. With six authors and an unknown (likely
  narrower) C3 inventor list, this is a concrete reason to resolve
  inventorship *before* relying on the grace period — not a prediction the
  exception would fail.
- If UW-Madison personnel are co-inventors of any element: does an
  inter-institutional ownership/co-filing arrangement exist or need to be
  negotiated, and how much time does a two-institution process add?

**Sponsors** (Acknowledgment, `regular_lsens.tex` L514):

- DOE Contract DE-AC02-76SF00515 and SLAC FWP 101264 — does Bayh-Dole
  reporting attach to any element of this work? Reporting applies "whether or
  not those inventions are considered patentable" (S003) — **this duty is
  independent of this brief's decision label and does not wait on it.**
- NSF ECCS-2026822 funded the fabrication facility (C1) — do its terms reach
  the downstream packaging/deployment work?
- TomKat Center (Stanford) — non-government sponsor; IP clauses unknown (terms
  not supplied to this workflow).
- **UW-Madison/HSX facility funding is not named in the Acknowledgment** despite
  three UW-Madison authors and HSX being a DOE-supported UW-Madison facility —
  identify the governing HSX-side contract(s) and any independent reporting
  terms.
- PI authorization: "the PI's authorization is required even if the PI is not
  an inventor" (S003) — identify the PI of record for each governing award and
  obtain authorization for both the OTL disclosure and the posting decision.

---

## 9. Search and evidence limitations (state of the record)

- **Bounded search.** All absence findings are from a bounded,
  English-language, indexed-literature search (patents, journals, official
  policy pages). They are documented absences, not proof of novelty — and for
  the C3 conjunction specifically, the probative weight of the absence is low,
  because facility packaging engineering lives in un-indexed internal
  documentation (Stage 60 §5.1). This package is not an exhaustive search and
  performed no FTO clearance.
- **Open external questions:** G8 (W7-X panel grounding — paywalled companion
  paper) and G10 (earliest disclosure — outside the controlling artifacts'
  boundary) remain open; G10 is the single biggest unknown in the entire
  review.
- **Readout chain (C4) not searched to saturation** — a deliberate, documented
  depth limitation (`20_SEARCH_LOG.md` §9); N012 is `lead_only` and supports
  no conclusion. The screen-out rests on the manuscript-intrinsic record
  (catalog parts, no disclosed circuit delta), discounted one confidence step
  accordingly.
- **S015 depth caveat:** S015 (2005 InSb edge-plasma array) is verified at
  abstract/metadata level only (publisher fetch blocked); its array-detail
  content is not verified_full. Its role here (a non-GaN in-vessel Hall
  deployment existed by 2005) is corroborated independently by S016 and N016,
  so no conclusion rests on S015 alone.
- **Other verification-depth notes:** N004 (`lead_only`, date unresolved)
  supports no conclusion; S001–S003 (Stanford OTL pages) are
  `verified_abstract` via cached quotations after HTTP 403 blocks; N017's
  10 mm/thermal-purpose sub-details are abstract-grade from the paywalled 2013
  companion; the journal-confidentiality premise for the IEEE submission is a
  norm-based presumption, not venue-verified (Stage 60 §5.2).
- **Timeline discipline:** the 2026-07-02 `submission.pdf` creation date is a
  working proxy for the disclosure timeline, not a confirmed invention or
  filing date; the deployment campaign's calendar dates are unknown.
- **No legal advice.** Nothing here is a legal opinion, validity opinion, or
  clearance; calibrated research labels only.

## 10. Conflict-resolution record (what was resolved, not averaged)

1. **Stage 50 `HOLD_ARXIV_FOR_OTL` vs. Stage 60 lead recommendation:**
   resolved per §0.1 — the decision label is
   `NO_PUBLICATION_SPECIFIC_FILING_CASE_IDENTIFIED`; the hold survives only as
   the §4 time-boxed checkpoint with default release (b), justified by
   irrevocability, unresolved ownership, and patentability-independent
   sponsor duties — not by C3's prospects.
2. **Three-stage `conditional_hold` vs. each stage's stated expectation of
   failure:** the momentum was named at Stage 60 §5.5; this brief adopts the
   calibrated expectation as its lead finding and demotes C3 to a contingent,
   evidence-triggered footnote of the checkpoint (§2.3, §3).
3. **C2's "novelty risk: medium":** carried technically but declared
   functionally inert (Stage 60 §4) — this brief treats C2 as having no
   standalone case, full stop.
4. **G4 "latent delta":** struck from weighing, kept as an inventor question
   (§7), per Stage 60 §5.4.
5. **Implicit GDC exposure (F17):** benefit of the doubt withdrawn (Stage 60
   §5.3); G5 is now a question that cuts against C3 until answered.
6. **Bounded-search absence as C3's survival basis:** de-cosmeticized per
   Stage 60 §5.1 — stated plainly in §2.3 and §9.

## 11. Gate compliance

- Leads with exactly one decision label plus a one-paragraph rationale (§0);
  label-vs-arXiv-gate relationship made explicit (§0.1, §4).
- Answers the three user questions directly, each with manuscript feature,
  evidence, closest prior art, delta, uncertainty, practical value, and
  recommended action (§2).
- Concepts separated strong/conditional/weak/excluded (§3); excluded concepts
  never evaluated as manuscript IP.
- Prioritized 48-hour (§5) and one-week (§6) actions; evidence-request list
  with Stage 60 adjustments (§7); inventorship/sponsor questions (§8); exact
  hold/release condition (§4); patentability triage separated from FTO,
  ownership, and filing (§1); limitations stated (§9).
- Citations (ledger source_ids with URLs, `regular_lsens.tex` line numbers,
  `submission.pdf` page references) placed adjacent to the claims they
  support; `lead_only` rows (N004, N012) support no conclusion.
- No patentability inferred from scientific novelty, "first" deployment,
  commercial usefulness, or successful experimentation; no combination treated
  as non-obvious without evidenced unexpected result or teaching away.
- No legal advice, exhaustive-search, or FTO claim; no external communication,
  upload, submission, or manuscript modification performed by this workflow;
  nothing under `state/` was written by this stage agent.

## 12. Where to read more

| Question | File |
|---|---|
| What exactly does the paper disclose? | `outputs/10_PUBLICATION_TECH.md`, `outputs/10_DISCLOSURE_MAP.csv` |
| What prior art exists and how was it searched? | `outputs/20_PRIOR_ART.csv`, `outputs/20_SEARCH_LOG.md` |
| Why each concept screened in/out | `outputs/30_IP_SCREEN.md`, `outputs/30_CLAIM_CHART.csv` |
| The packaging deep-dive and evidence gaps | `outputs/40_UHV_PACKAGE_VERDICT.md`, `outputs/40_EVIDENCE_GAPS.md` |
| Disclosure timing, IEEE/arXiv policy, intake draft | `outputs/50_ARXIV_RISK.md`, `outputs/50_SOURCE_SCRUB.md`, `outputs/50_OTL_INTAKE.md` |
| The adversarial case and bias audit | `outputs/60_RED_TEAM.md` |
| Model/effort audit for this run | `outputs/70_MODEL_REPORT.md` |
