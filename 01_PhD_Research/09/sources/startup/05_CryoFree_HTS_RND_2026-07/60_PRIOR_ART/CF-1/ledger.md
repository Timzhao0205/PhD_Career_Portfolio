# Prior-Art Ledger — CF-1: Dual-function turn-to-turn interface
(spatial co-optimization of Rc and radial thermal conductance to cold head, conduction-cooled NI HTS pancake coil)

> Research aid, not legal advice. Wave 1 harvest. Personal-access, read-only web
> sources only (Google Patents / Espacenet-indexed text, USPTO PPUBS, IEEE/IOP/arXiv
> abstracts, ResearchGate/PubMed abstracts, KIPRIS-indexed Google Patents Korean text).
> No web-posting performed. models=harvest:sonnet[x1] (log per CLAUDE.md).
> Novelty judgment is OUT OF SCOPE here (Fable G-NOVEL gate). Every hit below,
> including ones that hurt CF-1, enters the IDS_pool.

## Query pack used

**English:** no-insulation HTS coil contact resistance conduction cooled cryocooler;
turn-to-turn interface radial thermal conduction cold head; spatially graded /
variable / non-uniform contact resistance no-insulation coil; metal co-wound /
co-winding thermal; charging delay vs hot-spot trade-off; CPC/IPC walk H01F6/06,
H01F6/04, H02K55/*, F25B, G01R33.

**Chinese (simplified):** 无绝缘 高温超导 线圈 接触电阻 传导冷却 专利; 高温超导体场线圈;
无液氦.

**Japanese:** 無絶縁 高温超電導 コイル 接触抵抗 伝導冷却 特許; 部分絶縁巻線.

**Korean:** 무절연 고온초전도 코일 접촉저항 전도냉각 특허; 도전성 물질 함침 무절연 초전도 코일.

**Assignee watches searched:** Tokamak Energy, MIT, Korea University (Seungyong Hahn
group), SuNAM, Fujikura, Furukawa, Sumitomo, Florida State University (NHMFL),
Hinetics, Bar-Ilan/RICOR, Korean Basic Science Institute. GE, Airbus/UpNext,
Toshiba, Mitsubishi, IEE-CAS, CFS, Bruker, Siemens Healthineers, KERI, KAIST,
Shanghai Superconductor were queried but produced no CF-1-specific hits this wave
(gap noted below, not exhaustive — see Coverage Gaps).

---

## TIER 1 — Granted / near-scope patents

### T1-1. EP4078630A1 / WO2021122522A1 — "HTS linked partial insulation for HTS field coils"
- **Assignee:** Tokamak Energy Ltd (UK)
- **Priority date:** 2019-12-20 (GB priority); PCT filed 2020-12-15
- **Jurisdiction / status:** EP granted (active as of 2023-11-15 per Espacenet-indexed
  legal status); WO/PCT national-phase family; EP4233081A2 is a related divisional
  (see T1-2).
- **Relevance (one sentence):** Discloses varying the number/spacing of HTS-bridge
  conductive paths through a partially-insulating turn-to-turn layer so that the
  layer's **thermal properties can be varied independently of its electrical
  (resistance) properties**, and separately teaches varying effective inter-turn
  resistance **circumferentially** (l/lc-triggered regions) — i.e., independent
  electrical/thermal control of the same interface layer is already claimed,
  though the disclosed variation axis is circumferential/local-hotspot-triggered,
  not a designed **radial** (inner-turn vs outer-turn-near-cold-head) map keyed to
  a cryocooler thermal budget.
- **Original text (verbatim, English-language document):** "By varying the size of
  these regions and the number of connections between them and the metal connection
  layer, the thermal properties of the partially insulating layer can be varied
  independently of the electrical properties" (re: Fig. 11, "thermal regions 1131").
  Also: "The HTS bridges may be distributed throughout the field coil, or may be
  used only in regions with high l/lc during normal operation."
- **Tier rationale:** Tier 1 — granted EP family member, same CPC space (H01F6),
  directly teaches independent electrical/thermal tuning of a turn-to-turn interface.
- **IDS_pool:** YES — flag as closest single reference found this wave; hurts CF-1's
  novelty on the general concept of "decoupling electrical and thermal control of
  the same interface layer," though not on the radial/cold-head-budget mapping.

### T1-2. EP4233081A2 — "High temperature superconductor field coil" (Tokamak Energy divisional/continuation family)
- **Assignee:** Tokamak Energy Ltd
- **Priority date:** 2020-10-20; filed 2021-10-20
- **Jurisdiction / status:** EP, published 2023-08-30, status **Pending** (not yet granted)
- **Relevance:** Temperature-dependent-resistivity insulator between turns with
  conductor "bridges" whose number density is varied along the tape so **turn-to-turn
  resistance is held constant per turn** — i.e., the opposite design goal from CF-1
  (CF-1 wants Rc to vary by design across turns; this patent teaches evening it out).
  Useful as a contrast reference and as evidence the assignee is actively patenting
  in exactly this interface-engineering sub-space.
- **Original text (verbatim):** "metal bridges described above may be varied along
  the insulator tape to ensure that the turn-to-turn resistance provided by the
  insulator tape remains (at least approximately) constant for each turn."
  Temperature-dependent resistivity: "first resistivity at a temperature less than
  a generation temperature... lower, second resistivity at a second temperature."
- **Tier rationale:** Tier 2 in practice (application, not yet granted) but grouped
  here with T1-1 because it is the same assignee/family and defines the boundary
  of what's already claimed in this space. Re-tag as Tier 2 in sources.json.

### T1-3. US11101060B2 — "Partially-Insulated HTS Coils"
- **Assignee:** Tokamak Energy Ltd
- **Priority date:** 2018-02-01; filed 2019-01-31; **granted 2021-08-24**
- **Jurisdiction / status:** US, granted, active. Family members AU2019214510A1,
  WO2019150123A1, EP4012730A1 (EP/AU/WO — same disclosure, different jurisdictions).
- **Relevance:** Parent of the T1-1/T1-2 family. Conductive strip with insulating
  coatings on both sides, windows offset between sides, R_TT = d²ρ/(4wtL); explicitly
  claims **varying window spacing along the coil so total per-turn resistance is
  constant**, and separately discloses a metal-insulator-transition material
  (vanadium oxide) as an alternative interface with temperature-triggered resistance
  collapse. No mention of cryocooler/cold head or of intentionally engineering a
  radial Rc gradient for a cooling-power budget.
- **Original text (verbatim):** "distance between windows... may be varied along
  the partially insulating layer so that the total resistance of each turn of the
  coil is constant." Vanadium oxide: "very high resistance when cool, and a
  relatively low resistance (at least 10 times lower) when warmed above a
  transition temperature (approx. 110 K)."
- **Tier rationale:** Tier 1 — granted US patent, core CPC overlap, closest single
  US reference to the general "engineered spatial variation of turn-to-turn
  interface resistance" concept.

### T1-4. US9117578B2 / WO2013180802A1 — "No-insulation multi-width winding for high temperature superconducting magnets"
- **Assignee:** Massachusetts Institute of Technology (MIT)
- **Priority date:** 2012-03-13; filed 2013-03-13; **granted 2015-08-25**; active (expires 2033-07-19)
- **Jurisdiction / status:** US granted; WO family.
- **Relevance:** Stacks double-pancake NI coils of *varying conductor width* by
  axial position (widest at top/bottom, narrowest at midpoint) to manage field
  quality/protection — a spatially-varying design parameter across an NI coil
  stack, but the varied parameter is **tape width**, not turn-to-turn interface
  material/Rc, and no thermal-conductance-to-cold-head claim. Relevant as an
  "already-accepted-that-spatial-variation-across-an-NI-stack-is-patentable-subject-
  matter" reference and CPC-adjacent (H01F6/06).
- **Tier rationale:** Tier 1 (granted, on-point CPC, MIT assignee on the watch list)
  but mechanistically distant from CF-1's electro-thermal co-design claim.

### T1-5. KR101665038B1 — "도전성 물질로 함침된 무절연 초전도 코일 및 그의 제조장치" (No-insulation superconducting coil impregnated with conductive material, and manufacturing apparatus)
- **Assignee:** Korea Basic Science Institute (한국기초과학지원연구원)
- **Priority/filing date:** 2016-01-11; **granted 2016-10-13**
- **Jurisdiction / status:** KR, granted, active (est. expiry 2036-01-11)
- **Relevance:** Conductive impregnation layer (polymer matrix + conductive
  particles + conductive balls) between turns, resistance higher than the
  superconductor but low enough to bypass hot-spot current — a uniform (not
  spatially mapped) interface material solution. No radial/thermal-to-cold-head
  claim.
- **Original text (KO, machine-translated):** "보빈 상에 감겨진 초전도 선재의 복수의
  인접한 권선 턴들 사이에 배치된 도전성 함침 층" → "a conductive impregnation layer
  disposed between a plurality of adjacent winding turns of superconducting wire
  wound on a bobbin."
- **Tier rationale:** Tier 1 — granted KR patent, on-point NI-coil interface subject
  matter; found via Korean-language query pack (dup-check would be worthless in
  English only, per mission brief — confirms the value of the multilingual pass).

### T1-6. US20060071747A1 — "Method for manufacturing superconducting coils" (abandoned)
- **Assignee:** Bar-Ilan University; RICOR Cryogenic and Vacuum Systems
- **Priority date:** 2004-10-04; filed 2005-09-30; published 2006-04-06
- **Jurisdiction / status:** US, **status: Abandoned** (no continuation found this wave)
- **Relevance:** Directly frames the CF-1 problem statement — "[l]ow thermal
  conductivity [of turn-to-turn insulation] increases cooling time and decreases
  heat removal during operation thus worsening coil stability" **"in conduction-
  cooled coils"** specifically — then solves it with a *uniform* high-thermal-
  conductivity ceramic-filled (alumina/BN) epoxy between all turns. This is the
  closest reference found to CF-1's problem framing (conduction-cooled + turn-to-
  turn interface thermal bottleneck) but its solution is uniform, not a spatial
  Rc/thermal co-map, and it predates practical NI (bare-contact) winding — it
  still uses an "insulating" resin layer, just a thermally conductive one.
- **Tier rationale:** Tier 1 nominally (was a granted-track application) but
  **abandoned** — weak as a blocking reference, strong as IDS background/problem
  statement. Include in IDS_pool regardless (duty of candor; abandonment doesn't
  erase disclosure date for prior-art purposes).

---

## TIER 2 — Applications (published, not granted / pending / ceased)

### T2-1. WO2021122522A1 (same family as T1-1; PCT-stage record)
- **Status:** Ceased (per Espacenet/Google Patents legal-status field) at PCT stage;
  live descendants are EP4078630A1 (granted, T1-1) and EP4233081A2 (pending, T1-2).
  Logged separately here because the WO publication text contains the clearest
  statement of the "vary electrical and thermal independently" teaching.

### T2-2. US12196792 (image-only PPUBS record) — "Non-destructive measurement method and apparatus for the turn-to-turn resistivity distribution in non-insulation superconducting coils"
- **Assignee:** not confirmed this wave — PDF is CCITT-encoded image, text not
  machine-extractable via available tools; companion NPL (T3, IOP article,
  DOI-indexed as "non-destructive method for detecting turn-to-turn resistivity
  distribution in NI REBCO coils," iopscience.org/10.1088/1361-6668/acef6a)
  strongly suggests a Chinese or Korean university/institute origin (topic and
  author-network match groups publishing on TTRD reconstruction — likely a
  China-based group given the SST/IOP venue pattern seen elsewhere in this
  search set; **not independently confirmed — flag as gap**).
- **Relevance:** Measures/reconstructs the *spatial (turn-by-turn) distribution*
  of contact resistivity in an existing NI coil non-destructively. This is a
  **diagnostic/characterization** method for an *existing, already-spatially-
  non-uniform* Rc pattern (arising from winding-tension variation etc.), not a
  method of *engineering* a designed spatial Rc/thermal map. Adjacent but
  distinguishable: CF-1 claims deliberate design of the spatial map; T2-2 claims
  measuring whatever spatial map resulted from manufacturing variability.
- **Tier rationale:** Tier 2 — patent application/grant record found but text not
  fully verified (image PDF); flagged for a retry with an OCR-capable tool in a
  later wave.

### T2-3. CN115485868A — "高温超导体场线圈" (High-temperature superconductor field coil)
- **Application number:** CN202180032673.3
- **Assignee:** not resolved this wave (Google Patents snippet did not surface
  assignee/applicant field; needs a direct CNIPA or full Google Patents page fetch)
- **Relevance:** Title-level match ("HTS field coil") surfaced by the Chinese-
  language query pack; full claims not reviewed this wave — **gap, retry needed**.
- **Tier rationale:** Tier 2 (unconfirmed) pending full-text review.

---

## TIER 3 — Peer-reviewed NPL (highest scientific relevance; several are the
### closest conceptual prior art to CF-1, even though not patents)

### T3-1. Wang, Hahn et al., "Improved stability, magnetic field preservation and recovery speed in (RE)Ba2Cu3Ox-based no-insulation magnets via a graded-resistance approach" — IEEE Trans. Appl. Supercond., ~2017 (vol. 27, no. 4 timeframe, per co-located search hit; exact vol/issue not independently confirmed this wave — **gap: confirm citation**)
- **Relevance (one sentence, and this is the single most important NPL hit this
  wave):** Proposes **patterned resistive-conductive layers inserted between
  SELECTED turn-to-turn contacts** (i.e., a spatial, non-uniform Rc map by design,
  not by manufacturing accident) specifically to contain hot-spot heat propagation
  while preserving turn-wise current sharing for self-protection — this is
  conceptually the closest published antecedent to CF-1's "spatial map resolves
  the Rc trade-off" insight, though the objective optimized is **quench/hot-spot
  self-protection + field preservation**, not the CF-1-specific **radial thermal-
  conductance-to-cold-head / cryocooler-power-budget** objective. CF-1's
  distinguishing angle (conduction-cooled, limited-lift-power cold head as the
  second design objective, with a Pareto front against charging delay) is not
  addressed in the abstract-level material retrieved.
- **Original text (paraphrase from indexed abstract, English NPL, no translation
  needed):** "A novel graded-resistance method has been proposed to tackle
  problems in no-insulation magnets while maintaining thermal stability and
  self-protection capability. Patterned resistive-conductive layers are inserted
  between selected turn-to-turn contacts to contain hot-spot heat propagation
  while maintaining turn-wise current sharing required for self-protection,
  resulting in faster post-quench recovery and reduced magnetic field transient."
- **Tier rationale:** Tier 3, but treat as a **must-address reference** at G-NOVEL —
  recommend the adjudicator specifically compare CF-1's radial/cold-head-budget
  objective function against this paper's hot-spot/field-preservation objective
  function to determine if the difference is claim-worthy (non-obviousness) or
  merely a relabeled application of the same graded-resistance idea.

### T3-2. Bonura et al., "Systematic Study of the Contact Resistance Between REBCO Tapes: Pressure Dependence in the Case of No-Insulation, Metal Co-Winding and Metal-Insulation," IEEE Trans. Appl. Supercond., 2019, DOI 10.1109/TASC.2019.2893564
- **Relevance:** Establishes Rc vs. contact-pressure curves for NI / metal-co-wind /
  metal-insulation interfaces at 77 K, 10–200 MPa — background data CF-1's sim
  (thermal_network.py) should cite/validate against; not itself a spatial-map
  claim, but core numeric grounding for "interface choice sets both Rc and thermal
  path" (the ~130x copper-vs-stainless swing cited in MISSION.md draws on this
  literature family).
- **Tier rationale:** Tier 3, foundational background NPL.

### T3-3. "Study of contact resistivity of a no-insulation superconducting coil," Supercond. Sci. Technol. (IOPscience, DOI 10.1088/1361-6668/abd14d)
- **Relevance:** Confirms "spatial non-uniformity of contact resistance" is
  observed as a *manufacturing artifact* (winding-tension variation) and its
  effect on AC current distribution was studied numerically — again the
  as-built-variability framing, not the deliberately-engineered-map framing of
  CF-1. Useful as evidence the field already treats spatial Rc non-uniformity as
  a first-order effect worth modeling — supports feasibility, weakens the
  "nobody thought about spatial Rc" angle, but does not disclose intentional
  co-design against a cold-head thermal budget.
- **Tier rationale:** Tier 3.

### T3-4. "Hot-Spot Modeling of REBCO NI Pancake Coil: Analytical and Experimental Approaches," PMC/open-access (PMC8127627)
- **Relevance:** Analytical hot-spot models for NI coils; background for CF-1's
  peak-hotspot-ΔT objective.
- **Tier rationale:** Tier 3.

### T3-5. "Surface Contact Approximation for Magneto-Thermal Finite Element Analysis of No-Insulation HTS Coils," arXiv:2605.28574 (2026)
### T3-6. "Explicit Turn Resolution with Anisotropic Homogenisation... No-Insulation HTS Magnets," arXiv:2605.31009 (2026)
### T3-7. "Control of turn-to-turn contact resistivity in resistively insulated REBCO coils," arXiv:2604.15587 (2026)
- **Relevance (T3-5–T3-7):** Very recent (2026) simulation-methods literature
  building coupled electro-thermal contact models for NI coils, including explicit
  turn-by-turn resolution and control of Rc. These are the most contemporaneous
  hits and should be re-checked at every refresh pass — if any of them proposes
  a designed (not measured/incidental) spatial Rc-vs-thermal-conductance map
  keyed to an external cold-head budget, they would become Tier-1-equivalent
  blocking NPL. On the abstract-level text retrieved this wave, T3-7 in
  particular ("control of turn-to-turn contact resistivity") is the closest
  title match and **should be fetched in full text next wave** (gap, see below).
- **Tier rationale:** Tier 3, high-priority re-check items.

### T3-8. "A novel winding method for a no-insulation layer-wound REBCO coil to provide a short magnetic field delay and self-protect characteristics," Supercond. Sci. Technol. (IOPscience, doi ab016e)
- **Relevance:** Layer-wound (not pancake) NI variant trading charging delay vs.
  self-protection — same trade-off axis as CF-1 (charging delay vs. thermal/
  protection performance) but no thermal-conductance-to-cold-head or spatial-map
  claim; different winding topology (layer- vs pancake-wound).
- **Tier rationale:** Tier 3.

---

## TIER 4 — Other (background, non-blocking, context)

- Hinetics CRUISE-class conduction-cooled NI racetrack field coils (Illinois
  Grainger news release; AIAA SciTech 2026-0999 paper; ARPA-E project page) —
  confirms the anchor exemplar is real and active but no patent numbers were
  surfaced this wave for Hinetics itself (gap — Hinetics patents, if any, were
  not found under public assignee search; likely too new / not yet published or
  filed under a different corporate name — **retry next wave with USPTO assignee
  search directly on "Hinetics Inc" once PatentsView/USPTO full-text access is
  available**).
- CN105869782B "高温超导线的制备方法" (HTS wire preparation method) — wire
  manufacturing, not coil interface; Tier 4, low relevance.
- CN101512829B "高温超导导线和线圈" (HTS wire and coil) — general HTS coil patent,
  not reviewed in full text this wave; Tier 4 pending review.
- JP2017-535948 "部分絶縁巻線を用いた超電導コイル" (Superconducting coil using
  partially-insulated winding) — appears to be the JP national-phase entry of the
  Tokamak Energy WO2019150123A1/US11101060B2 family (T1-3); listed here to avoid
  double-counting until family membership is confirmed.
- JP2012033947A "高温超電導コイルおよびその製造方法" — addresses substrate-peeling
  degradation, not turn-to-turn interface Rc/thermal co-design; Tier 4.
- KR101446866B1, KR101116866B1, KR20120004367U — HTS wireless power transfer,
  hybrid cooling apparatus, coil cooling system respectively; surfaced by Korean
  query pack but off-target (general cooling hardware, not turn-to-turn interface
  co-design); Tier 4.
- EP0974849A2 "Thermal conductance gasket for zero boiloff superconducting
  magnet"; US7616083B2 "Resin-impregnated superconducting magnet coil comprising
  a cooling layer"; US5446433, US6002315, US20200150203 "Superconducting magnet
  with cold head thermal path cooled by heat exchanger" — all address
  coil-to-cold-head thermal *hardware* (gaskets, cooling layers, cold-warm
  supports) rather than the turn-to-turn *interface* doing double duty; useful
  CPC-adjacent background (H01F6/04 cooling arrangements) but not on-point.
  Tier 4.

---

## Coverage gaps / retry log (per instructions: note gap, do not stall)

1. **CNIPA direct portal, J-PlatPat direct portal, KIPRIS direct portal, Espacenet
   Advanced Search UI, WIPO PatentScope UI** were not directly queryable with
   available tools this wave (no authenticated/API access configured); all
   non-English hits above were obtained via Google-Patents-indexed full text and
   web search snippets, which is a reasonable proxy but not equivalent to a native
   CNIPA/JPO/KIPRIS full-text/legal-status search. **Recommend a follow-up wave
   with direct portal access (or PatentsView API key) before any filing-relevant
   reliance.**
2. **US12196792** (T2-2) full text not extracted — PPUBS PDF is a scanned image
   (CCITT fax encoding); assignee unconfirmed. Retry with OCR-capable fetch or
   direct USPTO Patent Public Search text export.
3. **CN115485868A** (T2-3) assignee and full claims not resolved — retry with a
   direct Google Patents page load (first attempt returned only a search snippet).
4. **Hinetics Inc.** — no patents found under that name this wave; genuinely may
   not have published filings yet (company is young, product unveiled 2025), or
   filings may sit under a parent/inventor name not searched. Retry with
   inventor-name search once available (e.g., known Hinetics/Illinois PI names).
5. **T3-1 (graded-resistance IEEE TAS paper)** exact volume/issue/author list not
   independently confirmed — cited secondhand via a co-located search snippet.
   Retry with a direct IEEE Xplore query to pin the full citation before this
   becomes a G-NOVEL blocking reference.
6. Assignee watches with **zero hits this wave**: GE, Airbus/UpNext, Toshiba,
   Mitsubishi, IEE-CAS, CFS, Bruker, Siemens Healthineers, Korea University
   (beyond the general Hahn-group NPL), KERI, KAIST, Shanghai Superconductor. This
   does not mean no art exists — it means this wave's queries did not surface any
   CF-1-specific hit for these assignees. Recommend targeted per-assignee patent
   searches in a refresh wave rather than concluding a clean field.

## Summary for adjudication (G-NOVEL will decide; this is evidence, not verdict)

The single most important finding this wave: **nobody found this wave discloses
CF-1's exact combination** — (i) a *designed* (not incidental) spatial map, (ii)
that is *radial* (inner-turn-charging-control vs outer-turn-near-cold-head), (iii)
jointly optimizing Rc *and* thermal conductance *to a cryocooler cold head under a
fixed limited-lift-power budget*, (iv) evidenced by a Pareto front no uniform
interface can reach. However, **three references sit uncomfortably close** and
must be squarely addressed at G-NOVEL: T1-1/EP4078630A1 (independent electrical/
thermal tuning of the same interface layer, same assignee actively patenting in
this space), T3-1 (designed spatial/graded Rc map for a different objective:
hot-spot/field-preservation rather than cold-head-budget), and T1-6/US20060071747A1
(states the conduction-cooled turn-to-turn-thermal-bottleneck problem almost
verbatim, solves it with a uniform rather than mapped material). All three, plus
every other hit above, are entered into the CF-1 IDS_pool regardless of how this
adjudicates.
