# Stage 20 — Prior-Art Search Log

Run: HSXIP-20260805T071311Z. Scope authority: `IP_SCOPE.md`, `CLAUDE.md`,
`SOURCE_POLICY.md`, `schemas/OUTPUT_GATES.md`. This log records what was
searched, where, when, by whom, and why each search branch was judged
saturated. It does not decide legal disposition — closest references, deltas,
and gaps are recorded in `outputs/20_PRIOR_ART.csv`; novelty/obviousness/
eligibility/patentability conclusions are Stage 30/40's job.

Accessed date for every source in this log and the accompanying CSV is
**2026-08-05**. Working reference date for timeline discipline is the
manuscript PDF's creation date, **2026-07-02** (per `submission.pdf` metadata,
confirmed in Stage 00) — a working proxy, not a confirmed invention or filing
date. Material dated after 2026-07-02 is explicitly flagged as post-date
rather than silently treated as prior art (see §8).

## 0. Research method and an honest process note

The orchestrating stage-20 session dispatched **six parallel research
sub-agents ("forks")**, each scoped to exactly one `SOURCE_POLICY.md`
coverage area, with explicit instructions to report findings back rather
than write the final deliverables themselves (the orchestrating session
retained responsibility for assembling `20_PRIOR_ART.csv` and this log):

1. Fusion/plasma Hall-diagnostic seeds S015–S021 (JET/ITER/DEMO/HSX).
2. AlGaN/GaN and III-nitride Hall device patents/papers, seeds S008–S014.
3. UHV encapsulation, ceramic carriers, epoxy, vacuum bake, grounded
   conductive/graphite shields, GDC/arcing protection (seed S022, otherwise
   unseeded — the highest-priority, most-open-ended search lane).
4. Deployment/validation methods (biased/unbiased, coil-only, independent-
   diagnostic correlation) — unseeded.
5. MPEP 2112/2104 and combination/new-use patentability doctrine, seeds
   S004–S005.
6. Stanford OTL disclosure/sponsorship procedure and arXiv procedure, seeds
   S001–S003, S006–S007.

Four of the six forks (areas 1, 2, 3, 5) completed cleanly within their
assigned scope and reported structured findings back to the orchestrating
session without touching any output file, as instructed. **Two forks (area 4
and area 6) experienced a context-compaction event mid-task.** On resuming
from compaction they could no longer see their own narrow assignment in
context, defaulted to reading `inputs/prior_art_seeds.csv` directly, and
each independently re-ran a near-complete pass over all six coverage areas,
writing directly to `outputs/20_PRIOR_ART.csv` and this log (each found the
file already partially populated by the other and extended it rather than
overwriting). This is a process deviation from the original assignment, not
an intended design, and is recorded here rather than concealed, per the
project's integrity requirements.

The orchestrating session treated the resulting files as an **unverified
draft**, not an accepted deliverable, and performed the following before
accepting it:

- Cross-checked the compaction-recovered passes' factual claims (patent
  numbers, assignees, priority/publication dates, DOIs, author lists)
  against the four cleanly-scoped forks' independent findings for the same
  sources. Agreement was strong everywhere the two overlapped (e.g. S008–
  S010 patent claim text, S011/S012 group-paper identity, the S009/N002
  Senesky–Arkansas collaboration link, the central "no close graphite-shield
  match" finding) — this cross-validation is the basis for treating the
  compaction-recovered content as reliable rather than discarding it.
- Identified and added three high-value sources the compaction-recovered
  passes had **not** surfaced but the dedicated coverage-area-3 (UHV/GDC)
  fork had: **N016** (a 2014 GaAs Hall sensor array deployed in-vessel at
  the stellarator-class Compact Toroidal Hybrid device — directly relevant
  to the manuscript's "first ... deployed inside a stellarator" cover-letter
  claim, F49) and **N017** (Wendelstein 7-X's in-vessel Mirnov-coil graphite
  wall-protection panels — the closest same-diagnostic-class graphite-
  shield analog found in either pass). The orchestrating session directly
  re-verified both via `WebFetch`/`WebSearch` before adding them. It also
  added **N018**, a June 2026 ITER/DEMO antimony-Hall-sensor paper found
  while independently verifying the UHV fork's report, as an update to the
  fusion-diagnostic state of the art immediately pre-dating the manuscript.
- Reconciled `source_id` numbering (no collisions occurred; N001–N015 were
  assigned by the compaction-recovered passes, N016–N018 by the
  orchestrating session) and re-validated the full CSV against
  `SOURCE_POLICY.md`'s exact 17-column schema and its four allowed
  `verification_status` values (columns validated programmatically: 40 data
  rows, 17 columns each, no duplicate IDs).
- Did **not** re-run the two cleanly-scoped forks' work (areas 1 and 5),
  since their reports were self-contained, internally consistent, and
  already reflected in the CSV either directly or via the compaction-
  recovered passes' independent confirmation of the same sources.

All findings below are organized by coverage area regardless of which
fork(s) originally surfaced them; each area's section states which
agent(s) contributed and notes where the orchestrating session performed
its own supplementary verification.

## 1. Hall sensors as fusion/plasma magnetic diagnostics (`coverage_area: fusion_hall`)

**Contributed by:** the dedicated coverage-area-1 fork (primary) and the
compaction-recovered passes (independent confirmation of the same seven
seeds); N016/N018 added by the orchestrating session.

**Seeds verified:** S015–S021 (7/7). All seven exist at the stated
identifier with title/author/year matching the seed record; none required
correction. **S016 confirmed as the manuscript's ref5** (Quercia et al.
2022, JET); **S017 confirmed as ref6** (Bolshakova et al. 2017, DEMO);
**S021 confirmed as ref17** (Chlechowitz et al. 2015, HSX diagnostics).

**Databases/sites used:** DOI resolution to publisher pages (AIP
`pubs.aip.org`, IOPscience, ScienceDirect), ResearchGate/PubMed/PMC
secondary mirrors where the primary publisher page blocked direct fetch,
and the HSX facility's own document repository (`hsx.wisc.edu`) for S021's
full text.

**Queries run:** "GaN Hall effect sensor tokamak stellarator in-vessel
magnetic diagnostic deployment"; "AlGaN GaN Hall sensor fusion plasma
diagnostic semiconductor wide bandgap"; "HSX stellarator Hall probe
magnetic diagnostic history"; "Wendelstein 7-X Hall sensor GaN magnetic
diagnostic in-vessel"; "LHD stellarator Hall probe semiconductor magnetic
field sensor in-vessel"; per-seed title+abstract confirmation queries;
"Compact Toroidal Hybrid Hall sensor array magnetic diagnostic boron
nitride in-vessel"; "Duran Hall sensor antimony ITER DEMO Plasma Physics
and Controlled Fusion 2026 diffusion barrier".

**New sources found:** N002 (Lalwani et al. 2024, same-group device-physics
paper, not fusion), N003 (IEEE Access 2025, GaN power-electronics current
sensor, not fusion), N004 (IEEE "Portable Gauss Meter," date unresolved,
`lead_only`), **N016** (Stevenson et al. 2014, Rev. Sci. Instrum. 85,
093502, DOI 10.1063/1.4894209 — a 16-element GaAs Hall sensor array
inserted in-vessel, in a boron-nitride-sheathed stainless tube, at the
Compact Toroidal Hybrid (CTH) device at Auburn University, described in
that paper as a "non-axisymmetric hybrid torsatron/tokamak"), and **N018**
(Ďuran et al., *Plasma Phys. Control. Fusion* 68(6), online 2026-06-05, DOI
10.1088/1361-6587/ae6c59 — a fourth-generation antimony Hall sensor with a
W–Ti diffusion barrier and Al2O3 passivation for ITER/DEMO steady-state
diagnostics, published before the manuscript's 2026-07-02 reference date).

**Family consolidation:** S018 and S020 are companion papers (ITER OVSS
final design and its calibration procedure) from the same program.

**Key finding:** No GaN or AlGaN Hall sensor was found deployed in-vessel or
near-plasma-edge in any fusion device (JET, ITER, DEMO-scale programs,
Wendelstein 7-X, LHD, or HSX itself) prior to this manuscript. Every fusion
Hall-sensor deployment found uses a different material: InSb (S015, S016),
gold/metal film (S017), bismuth (S018/S020), ceramic-chromium (S019), or
antimony (N018). S021 (the manuscript's own ref17) documents HSX's pre-2015
diagnostic set — Rogowski coils, diamagnetic loops, poloidal coil belts,
internal coils — with no Hall probe of any material. **N016 is the single
closest pre-existing analog to the manuscript's F49 cover-letter claim**
("first GaN-based Hall-effect sensor deployed inside a stellarator"): a
semiconductor (GaAs) Hall sensor array was already inserted in-vessel in a
stellarator-class (non-axisymmetric torsatron/tokamak hybrid) device 12
years earlier. This does not anticipate the claim as literally worded (GaAs
≠ GaN; CTH is a torsatron/tokamak hybrid, not identically labeled a
"stellarator" the way HSX is), but it materially narrows how broadly F49
should be read. This is an absence/near-miss finding from a bounded,
English-language search, not proof of a negative.

**Saturation statement:** Two additional, materially different query
formulations per candidate facility (tokamak/stellarator/Wendelstein/LHD/
HSX/CTH) produced no new close reference beyond the seven verified seeds
and N002/N003/N004/N016/N018. Closed as saturated with an identified
closest-reference set (N016 for the "stellarator-class deployment" prong;
S016/S018 for the general in-vessel/ex-vessel Hall-deployment concept) and
an explicit documented gap (no GaN/AlGaN material found in any fusion
deployment, before or after the manuscript's reference date).

## 2. AlGaN/GaN and III-nitride Hall device patents and papers (`coverage_area: gan_hall`, `group_prior_work`)

**Contributed by:** the dedicated coverage-area-2 fork (primary, including
direct patent-claim reading and the Tower Semiconductor/TI/Kumar-2021
searches noted below) and the compaction-recovered passes (independent
confirmation plus N013/N014).

**Seeds verified:** S008–S014 (7/7). S008–S010 verified by directly reading
Google Patents independent-claim text. S011–S013 verified via their arXiv
preprint versions (publisher pages blocked direct fetch). S014 verified via
aggregated abstract sources.

**Databases/sites used:** Google Patents, USPTO image-ppubs PDF mirror,
arXiv, IEEE Xplore (metadata only), Justia Patents (inventor-name search).

**Queries run:** "Alpert Senesky Stanford AlGaN GaN Hall sensor patent
assignee Stanford University"; "patents.google.com inventor Senesky Hall
sensor"; "patents.google.com inventor Alpert Hall effect Stanford"; "Debbie
Senesky inventor patent Micro-Hall effect sensor GaN AlGaN Stanford";
"patents.justia.com inventor Debbie Senesky"; "AlGaN/GaN Hall sensor
octagonal geometry patent 200 micron"; "wide bandgap Hall sensor harsh
environment patent high temperature biasing offset"; "GaN sensor controlled
and stable threshold voltage patent Stanford Senesky"; USPTO full-text
search for "octagonal" + "Hall" + geometry claims (yielding N013/N014).

**New sources found:** N003, N004 (see §1); N012 (general Hall-readout
patent, `lead_only`, low priority per stage scope); **N013** (US10809318B2,
SK Keyfoundry, active, priority 2013 — independent claim covers an
"angulated or rounded corner" Hall active area, dependent claim 10
specifically covers octagon shape, in silicon CMOS); **N014** (US6639290B1,
Fraunhofer, expired, priority 1999 — claim 5 covers a "regular polygon"
Hall active area, a genus including octagon, also silicon CMOS). Two
additional leads were checked and ruled out as non-material: a Tower
Semiconductor GaN MIS-HEMT threshold-stability patent (US11195933B2/
US11843043B2 — fabrication-method claims unrelated to Hall-plate geometry
or packaging, no Senesky/Stanford inventorship) and a Kumar et al. 2021
AlGaN/GaN-on-Si paper (different substrate, not independently fetched,
would be `lead_only`); neither changes any closest-reference conclusion.

**Family/lineage consolidation:** S011 and S012 are the manuscript's own
ref10/ref11 — same-group prior publications, the manuscript's own stated
source for its octagonal geometry (F02) and anneal recipe (F04), not
independent third-party art. S013 is a same-group current-spinning paper
the manuscript does not implement (current-spinning is excluded per
`IP_SCOPE.md`); recorded only as a same-group comparator.

**Key finding:** No patent claiming the manuscript's specific regular
octagonal 200 µm Hall-plate geometry, and no Stanford-assigned or
Alpert/Senesky-inventor patent of any kind, was found despite direct
inventor-name searches on Google Patents and Justia — the group's own
geometry (ref10) and high-temperature characterization (ref11) work appears
to exist only as publications, not patents (an evidence gap, not a
conclusion that no such filing exists). The closest independent device-level
patent is **S009** (US11137310B2, University of Arkansas at Little Rock):
claim 1 recites an AlGaN/GaN Hall sensor with bias and Hall-voltage terminal
pairs matching the manuscript's basic arrangement, but additionally requires
**simultaneous temperature measurement**, a function the manuscript's
device does not perform (Stage 10 F39/F45). A collaboration link was found
between the manuscript's corresponding author (Senesky, via N002, a 2024
co-authored paper) and three of S009's five named inventors (Shetty,
Mantooth, Salamo) — flagged for Stage 30/50 inventorship/awareness
questions, not a legal conclusion. Separately, **N013/N014 establish that
the octagon/regular-polygon Hall-active-area shape itself is old and
cross-material-system generic** (patented in silicon CMOS since 1999):
S011/ref10's actual contribution is applying a known geometry family to a
new material system (AlGaN/GaN 2DEG), which is itself the group's own prior
publication, not this manuscript's contribution.

**Saturation statement:** Two materially different formulations of the
inventor-name search (direct Google Patents query and Justia inventor-index
query) for both "Alpert" and "Senesky" produced no Stanford- or
group-assigned patent. Geometry-specific search ("octagonal"+"Hall
plate"/"AlGaN") produced no new *III-nitride* geometry patent beyond
S008–S010, though it did surface the material-agnostic N013/N014. Closed as
saturated.

## 3. UHV encapsulation, ceramic carriers, epoxy, vacuum bake, grounded conductive/graphite shields, GDC/plasma protection (`coverage_area: uhv_package`)

**This is the highest-priority coverage area per the stage brief** — the
grounded graphite shield (F16) is Stage 00/10's single most enablement-thin,
most open element, and was searched across the full set of terminology
families specified in the task brief: encapsulation/potting, ceramic
carriers, graphite/conductive grounded shields, plasma cleaning, arcing,
outgassing, and in-vessel magnetic probes generally.

**Contributed by:** the dedicated coverage-area-3 fork (primary — ran all
seven terminology families below to at least two reformulations each) and
the compaction-recovered passes (independent confirmation of N005/N006/
N008–N010/N015); N016/N017 (the two most valuable additions in this whole
coverage area) were surfaced by the dedicated fork but had not made it into
either compaction-recovered pass, and were independently re-verified and
added by the orchestrating session.

**Seed verified:** S022 (EPO-TEK 353ND datasheet) — current manufacturer
page confirmed directly; recommended cure schedule (150°C/1 h) matches the
manuscript's bake exactly, i.e. the manuscript's bake is the epoxy's
standard manufacturer cure recommendation, not a custom UHV regimen devised
for this work. Independent (non-manufacturer) qualification corroboration
found: N007, a LIGO material-qualification RGA outgassing test record for
this same epoxy.

**Databases/sites used:** manufacturer site (`epotek.com`), USPTO
image-ppubs PDF mirror, Google Patents, OSTI.gov, ScienceDirect, IOPscience,
LIGO Document Control Center (`dcc.ligo.org`), general web search.

**Query families run** (each carried through at least two materially
different formulations before being judged saturated):

1. **Encapsulation/potting:** "potted sensor ultra high vacuum";
   "encapsulated diagnostic sensor tokamak"; "epoxy potting compound UHV
   sensor package"; "conformal coating UHV electronics fusion".
2. **Ceramic carriers/holders:** "ceramic leadless chip carrier vacuum
   sensor"; "ceramic holder in-vessel diagnostic"; "zirconia sensor mount
   plasma vessel"; "ceramic sensor housing fusion diagnostic".
3. **Graphite/conductive grounded shields (the priority search, six
   reformulations):** "grounded graphite shield sensor"; "graphite shield
   Langmuir probe"; "graphite shield Mirnov coil"; "conductive shield
   magnetic probe tokamak"; "graphite guard ring diagnostic probe";
   "Faraday shield magnetic probe plasma"; "electrostatic shield Hall probe
   tokamak"; "grounded conductive shield encapsulated sensor plasma arcing
   patent"; "graphite ceramic RF Faraday thermal shield plasma limiter
   patent"; "Mirnov coil protective shield graphite tokamak in-vessel
   diagnostic"; "graphite armor plate enclose magnetic flux loop diagnostic
   minimize plasma power patent" (→ N015); "Wendelstein 7-X Mirnov coil
   graphite cap" (→ N017); "Compact Toroidal Hybrid Hall sensor array...
   boron nitride in-vessel" (→ N016, cross-relevant to both areas 1 and 3).
4. **Plasma cleaning / GDC:** "glow discharge cleaning diagnostic
   protection"; "GDC sensor shield tokamak"; "sensor protection glow
   discharge cleaning fusion"; "Modelling of tokamak glow discharge
   cleaning"; "Conditioning of SST-1 Tokamak Vacuum Vessel by Baking and
   Glow Discharge Cleaning".
5. **Arcing:** "arcing protection in-vessel sensor"; "arc suppression
   diagnostic tokamak vacuum vessel"; "electron beam gun grounded shield
   prevent arc down patent" (→ N006).
6. **Outgassing:** "outgassing qualification epoxy space UHV"; "NASA
   outgassing database EPO-TEK 353ND"; "ASTM E595 epoxy vacuum
   qualification"; "LIGO EPO-TEK 353ND RGA outgassing" (→ N007).
7. **In-vessel magnetic probes generally:** "in-vessel magnetic probe
   package tokamak"; "magnetic probe protective housing fusion reactor";
   "micro-Torr vacuum packaging ceramic chip carrier" (→ N009).

**Key finding — the central result of this stage.** No reference of any
kind (patent, paper, engineering report, or vendor documentation) was found
that combines all elements of the manuscript's F16 disclosure: (a) a
**grounded**, (b) **graphite** shield, (c) specifically protecting an
**epoxy-encapsulated sensor package** against **GDC/plasma arcing and epoxy
degradation**. This is an **explicit, saturated-search gap**, not evidence
of novelty — a documented absence in a bounded, English-language search is
not the same as a finding that no closer art exists anywhere.

Ranked by closeness, the analogs found are:

- **N017** (Wendelstein 7-X in-vessel Mirnov coils, graphite wall-protection
  panels over a ceramic coil former) — closest in kind, since it shields a
  **magnetic diagnostic** in a currently-operating stellarator, but its
  stated purpose is plasma-radiation/thermal shielding, not arcing/epoxy
  protection, its diagnostic is an inductive coil (not a solid-state Hall
  sensor), and no grounding statement was found for the panels despite
  direct reading of the primary paper's text.
- **N015** (USH24H, 1985 DOE) — shields a magnetic **flux-loop** diagnostic
  specifically, but the purpose is bulk plasma/neutral-beam thermal-power
  protection, and the structure is a large vessel-integrated ring, not a
  small shield over a discrete encapsulated module.
- **N005** (US4858817, 1989 DOE) — a brazed graphite-ceramic Faraday-thermal
  shield for an RF antenna/limiter, not a sensor, with a thermal/RF (not
  arcing/epoxy) purpose.
- **N006** (US5216690/RE35024, electron-beam gun) — supplies only the
  general, non-fusion, non-sensor engineering principle that a grounded
  conductive shield suppresses vacuum arc-down.
- **N008** (SST-1 GDC conditioning paper) — confirms protecting in-vessel
  diagnostics during GDC is a recognized general tokamak concern, but its
  documented measure is a ceramic (not graphite) cover on the GDC electrode
  itself; search snippets also surfaced a competing design philosophy
  (electrically floating/isolating diagnostics from vessel ground during
  GDC, rather than grounding a shield) worth weighing in Stage 30/40 as an
  alternative documented approach, not a close match either way.

EPO-TEK 353ND (S022/N007) and ceramic-LCC UHV packaging (N009) are both
confirmed as routine, manufacturer-directed/industry-standard choices with
no indication of novel formulation or process in this manuscript's use of
them.

**Saturation statement:** Query family 3 (the priority search) was run
through roughly a dozen materially different formulations across both the
dedicated fork and the orchestrating session's supplementary verification;
no formulation surfaced a source combining all three elements of F16. This
coverage area is closed as saturated with a ranked set of partial analogs
(N017 closest) and an explicit, clearly stated gap for the exact
combination — the single most important finding of this stage.

## 4. Deployment/validation methods (biased/unbiased, coil-only, independent-diagnostic correlation) (`coverage_area: validation_method`)

**Contributed by:** the dedicated coverage-area-4 fork, which (per its own
final report) completed this area directly after its own attempt to
delegate further sub-searches was rejected by the harness, and separately
by the compaction-recovered continuation of the same fork, which reached
the same conclusions.

**Databases/sites used:** general web search, IOPscience, AIP Physics of
Plasmas, ScienceDirect, USPTO image-ppubs PDF mirror, Google Patents.

**Queries run:** "plasma diagnostic validation biased unbiased control
coil-only comparison method"; "new magnetic diagnostic cross-validation
diamagnetic loop correlation tokamak commissioning"; "'method of
validating' magnetic sensor bias voltage patent"; "JT-60SA diamagnetic
energy measurement evaluation poloidal beta first operational phase
validation"; "diagnostic validation independent measurement correlation
tokamak"; "sensor commissioning bias voltage control method patent".

**New source found:** N011 (Diamagnetic energy measurement vs. equilibrium
reconstruction cross-validation at JT-60SA, IOP 2025, DOI
10.1088/1741-4326/adaed0), used as a representative, current (2025) example
of the general methodological pattern.

**Key finding:** No patent or paper was found describing the manuscript's
specific three-part validation combination (biased-vs-unbiased comparison,
plus plasma-vs-coil-only comparison, plus temporal correlation against an
independent established diagnostic) as a named or previously claimed
methodology. What was found instead is converging evidence that each
individual technique — and the general strategy of validating a new
diagnostic by comparing its time series against an established, physically
related diagnostic (e.g. stored-energy/W_dia vs. equilibrium-reconstructed
W_mhd cross-checks, documented at JT-60SA and other tokamaks) — is routine,
standard commissioning practice in the fusion-diagnostics field, not a
separately patented technique. No patent-search formulation surfaced
anything closer than generic magnetic-sensor offset-cancellation/biasing
patents unrelated to this validation-methodology question.

**Saturation statement:** Two materially different formulations each for
the general cross-validation-methodology search and the bias-validation-
patent search produced no new close reference. Closed as saturated with a
routine-practice characterization and no closer single reference
identified.

## 5. Patentability doctrine: new use and combination claims (`coverage_area: new_use`, `eligibility`, `patentability`)

**Contributed by:** the dedicated coverage-area-5 fork (primary — direct
`WebFetch` of every MPEP section cited) and the compaction-recovered
passes (independent confirmation of S004/S005 plus the N001 addition).

**Seeds verified:** S004 (MPEP 2112/2112.02) and S005 (MPEP 2104) — both
directly fetched. **Note:** S004's exact current section title is "2112
Requirements of Rejection Based on Inherency; Burden of Proof" (the seed's
paraphrase "Inherency and new uses" is a loose gloss, not the literal
title); the new-use doctrine specifically lives in subsection **2112.02**,
confirmed on the same fetched page. Both pages live and current; revision
R-01.2024 (§2112/2112.02) and R-07.2022 (§2104).

**Databases/sites used:** `uspto.gov` MPEP pages, directly fetched.

**Queries run / URLs fetched:** direct `WebFetch` of
`uspto.gov/web/offices/pac/mpep/s2112.html` (general + 2112.02-focused),
`s2104.html`, `s2141.html`, `s2143.html`; WebSearch cross-check "MPEP 2141
combination of familiar elements KSR Teleflex obviousness standard"; "USPTO
MPEP subject matter eligibility guidance update 2026" (checked and ruled
out as non-material — see below).

**New sources found:** **N001** (MPEP 2141, KSR v. Teleflex
combination-of-known-elements obviousness standard — directly fetched by
the dedicated fork); the dedicated fork additionally directly fetched and
read **MPEP 2112.02** in full (quoting *In re Hack* — "the discovery of a
new use for an old structure based on unknown properties of the structure
might be patentable ... as a process of using" — and *In re May* — a claim
reciting use of an old structure "directed to a result or property of that
composition or structure" is anticipated, not patentable) and **MPEP 2143**
(the seven KSR-derived obviousness rationales for combination claims,
including "combining prior art elements according to known methods to
yield predictable results").

**Key finding:** MPEP 2112.02 supplies the controlling "new use of an old
device" test for Concept 2 (fusion-diagnostic deployment of a known/
purchased AlGaN/GaN Hall device): whether in-vessel fusion deployment is a
genuinely new functional use, or merely observing an already-known property
(GaN Hall sensitivity/thermal tolerance, per ref10/ref11) in a new
location, is the *In re Hack* / *In re May* fork Stage 30 must apply. MPEP
2141/2143 (KSR) supply the controlling combination-of-known-elements
standard for Concept 3 (the UHV/GDC module as an assembly of individually
common elements). A tangential lead — an April 2026 USPTO Subject Matter
Eligibility Declaration (SMED) Rule 132 best-practices memo — was checked
and ruled out as non-material: it concerns §101 abstract-idea/
computer-implemented-invention practice, not applicable to this physical-
device/new-use/combination fact pattern.

**Saturation statement:** All controlling MPEP sections relevant to new-use
and combination-claim doctrine (2112, 2112.02, 2104, 2141, 2143) were
directly fetched and read; no further search was pursued once the doctrinal
framework was confirmed complete against `schemas/OUTPUT_GATES.md`'s Stage
30 requirements. Closed as saturated. No legal opinion is rendered here on
whether the manuscript satisfies any of these standards — that is Stage
30's task.

## 6. Stanford disclosure, sponsorship, and preprint procedure (`coverage_area: disclosure`, `sponsorship`, `arxiv`, `source_hygiene`)

**Contributed by:** the dedicated coverage-area-6 fork and the
compaction-recovered passes (both independently fetched the same five
seed URLs with consistent results).

**Seeds verified:** S001–S003 (Stanford OTL), S006–S007 (arXiv) — all five
(5/5). S006 and S007 fetched directly with full text quoted. S001–S003
returned HTTP 403 on direct fetch (bot-blocked) in every pass attempted;
content verified instead via search-engine-cached quotation of the
operative page text, matching each seed's `why_seeded` description —
recorded `verified_abstract` rather than `verified_full` to reflect that
the live page itself was never directly rendered in any pass.

**Databases/sites used:** `otl.stanford.edu`, `info.arxiv.org`, general web
search for cached page text.

**Queries run:** "Stanford OTL 'Submit an Invention' preprint public
disclosure confidential disclosure before publication"; "Stanford OTL
process confidential invention disclosure PI authorization sponsor
compliance"; "Stanford OTL 'Patent' page novelty non-obviousness
inventorship foreign disclosure"; "Bayh-Dole Act invention disclosure
timing requirement"; "NSF DOE funded invention disclosure before
publication"; "SLAC National Accelerator Laboratory invention disclosure
policy" (these last three found only general Bayh-Dole background,
consistent with what S003's own page already states — not separately
added as new sources, since S003 already covers this ground with an A-tier
primary source).

**Key finding:** All five seeds accurately describe currently-live Stanford
OTL and arXiv policy pages; none required correction. S001 and S006
together establish that an arXiv posting is itself an irrevocable public
disclosure event that Stanford OTL treats as foreclosing future patent
filing if it precedes OTL disclosure — directly material to Stage 50's core
timing question. S003 confirms Stanford must report inventions to federal
sponsors under Bayh-Dole "whether or not those inventions are considered
patentable," directly relevant to the manuscript's DOE/SLAC/NSF-funded
status. S007 directly confirms arXiv's own submission rules prohibit
`.log`/`.aux`/`.synctex.gz`/`.pdf` build artifacts of the kind Stage 00
found embedded in `source_original.zip` (with a local compile-machine path
leak) — a concrete, sourced basis for Stage 50's source-hygiene
recommendation.

**Saturation statement:** Each seed's live-page content was confirmed
against its `why_seeded` description; the Bayh-Dole supplementary search
returned no new close reference beyond what S003 itself already states.
Closed as saturated.

## 7. Coverage disposition summary

| Coverage area | Seeds verified | New sources added | Closest reference | Disposition |
|---|---|---|---|---|
| fusion_hall | S015–S021 (7/7) | N002, N003, N004, N016, N018 | N016 (CTH, GaAs, stellarator-class in-vessel deployment) for F49; S016/S018 for general fusion deployment | Saturated; explicit material-gap finding (no GaN/AlGaN in any fusion deployment) |
| gan_hall / group_prior_work | S008–S014 (7/7) | N003, N004, N012, N013, N014 | S009 (US11137310B2) for device-claim material system; N013/N014 for geometry genericity | Saturated; no Stanford/group patent found (gap) |
| uhv_package | S022 (1/1) | N005–N010, N015, N016, N017 | N017 (W7-X Mirnov-coil graphite panels) — closest same-diagnostic-class analog; N005/N015 as fusion-specific but different-purpose analogs | Saturated; explicit gap for the exact grounded-graphite-shield-over-epoxy-sensor-for-GDC combination — the priority finding of this stage |
| validation_method | — (unseeded) | N011 | General routine-practice pattern (W_dia vs W_mhd cross-checks); no specific-combination match | Saturated; routine-practice characterization |
| new_use / patentability doctrine | S004, S005 (2/2) | N001 (+ MPEP 2112.02/2143 read in full, not separately numbered) | MPEP 2112.02 (*In re Hack*/*In re May*) + MPEP 2141/2143 (KSR) | Saturated |
| disclosure / sponsorship / arxiv / source_hygiene | S001–S003, S006–S007 (5/5) | — | — | Saturated |

**Total: 22/22 seeds verified** (identity, dates, and content cross-checked
against each seed's `why_seeded` description; none required a correction to
the seed record itself, beyond noting S004's literal current section title
differs from the seed's paraphrase). **18 new sources added** (N001–N018)
beyond the seed list, concentrated in the two areas with the thinnest seed
coverage (`uhv_package`, 1 seed, and `validation_method`, 0 seeds).

## 8. Timeline discipline

The manuscript PDF's creation date, **2026-07-02**, is used as the working
reference point throughout. All 40 sources in `20_PRIOR_ART.csv` predate
this date **except**: none are confirmed post-date. One source (**N004**,
the "Portable Gauss Meter" IEEE paper) has an internally inconsistent date
signal (a 2025 secondary-index date vs. a 2026 copyright-line snippet) that
could not be resolved to a firm pre- or post-date determination this
session; it is recorded `lead_only` for that reason and must not be used to
support any novelty-destroying or context conclusion until its date is
independently confirmed. **N018** (Ďuran et al., online 2026-06-05) is
close to the reference date but confirmed to predate it by four weeks —
legitimate pre-date prior-art context, not post-date material. No source in
this CSV is flagged post-date; if a later stage identifies one, it should
be added with an explicit post-date tag rather than silently treated as
prior art.

## 9. Remaining gaps for later stages

- Whether the Alpert/Senesky group's own octagonal-geometry and
  high-temperature-anneal work (ref10/ref11) was ever the subject of a
  patent application that this bounded search simply failed to find (as
  opposed to genuinely never having been filed) cannot be resolved by
  search alone.
- The absence findings in §1 and §3 (no GaN/AlGaN Hall sensor in any fusion
  deployment; no exact grounded-graphite-shield-over-epoxy-sensor-for-GDC
  combination) are both bounded, English-language, indexed-literature
  search absences — not proof that no closer reference exists anywhere,
  including in non-English-language, non-indexed, or purely internal
  engineering-documentation sources.
- The readout chain (INA849/OPA814/oscilloscope-bias) was not treated as a
  required `SOURCE_POLICY.md` coverage area and was not searched to
  saturation; N012 is recorded as an unverified `lead_only` placeholder
  only so a later stage does not need to rediscover it from scratch.
- Whether N017's Wendelstein 7-X graphite panels are in fact electrically
  grounded could not be confirmed from the primary paper's text; this
  remains an open question that, if resolved affirmatively via the
  companion engineering paper (not independently fetched — ScienceDirect
  403), would make N017 an even closer analog to F16 than currently
  recorded.
- This log does not determine patentability, novelty, obviousness, or
  freedom-to-operate for any candidate concept — that is Stage 30/40's
  task, using the closest references and deltas recorded in
  `20_PRIOR_ART.csv`.
