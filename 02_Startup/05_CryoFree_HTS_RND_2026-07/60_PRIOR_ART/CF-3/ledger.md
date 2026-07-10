# CF-3 Prior-Art Ledger — "Thermal-aware current steering"

**Candidate:** In an NI (no-insulation) HTS coil under conduction cooling with limited
cryocooler power, turn-to-turn bypass/thermal sites are engineered/actively controlled
to redistribute current AWAY from thermally weak cooling paths (poor conduction to
cold head), cutting hot-spot risk under a fixed cooling-power budget. Composes with
CF-1 (dual-function interface); CF-3's emphasis is directing current flow based on a
known/measured thermal-conduction map, not just interface material choice.

Wave: W1 harvest. models=harvest:sonnet. Autonomous, no user check-in.
Duty of candor: ALL hits below enter CF-3's IDS_pool, including hits that hurt novelty.
No novelty judgment made here — that is G-NOVEL's job (Fable-5, Wave 3).

---

## Query Pack (multilingual)

| Concept | EN | ZH (simplified) | JA | KO |
|---|---|---|---|---|
| No-insulation coil | no-insulation HTS coil | 无绝缘高温超导线圈 | 無絶縁高温超伝導コイル | 무절연 고온초전도 코일 |
| Conduction-cooled | conduction-cooled, cryocooler | 传导冷却 | 伝導冷却 | 전도냉각 |
| Turn-to-turn contact resistance | turn-to-turn contact resistance | 匝间接触电阻 | 巻線間接触抵抗 | 턴간 접촉저항 |
| Current bypass/redistribution | current bypass, current redistribution, current steering | 电流分流 / 电流重新分布 | 分流電流 / 電流再分配 | 전류 분류 / 전류 재분배 |
| Hot spot | hot spot | 热点 | ホットスポット | 열점 |
| Cold head | cold head, cryocooler | 冷头 / 冷指 | コールドヘッド / コールドフィンガー | 콜드헤드 |
| Thermal map / thermal conduction | thermal conduction map, cooling path | 热传导图 / 冷却路径 | 熱伝導マップ / 冷却経路 | 열전도 맵 / 냉각경로 |

CPC/IPC walk performed (via Google Patents / WebSearch text search, not native classification
browse — see Gaps): H01F6/06, H01F6/04, H02K55/*, F25B, G01R33.

Jurisdictions searched: US (USPTO full text via image-ppubs + Google Patents), CN (CNIPA
records via Google Patents CN + Chinese-language WebSearch), JP (JP family members via
Google Patents + Japanese-language WebSearch; no direct J-PlatJ portal access — see Gaps),
KR (KR family members via Google Patents + Korean-language WebSearch; no direct KIPRIS
portal access — see Gaps), EP/WO (Espacenet-equivalent via Google Patents/WIPO family data).

---

## Hits

### Tier 1 — Granted / near-scope patents

**1. US 12,196,792 B2 (also referenced in search as application/grant) — "Non-destructive
measurement method and apparatus for the turn-to-turn resistivity distribution in
non-insulation superconducting coils"**
- Jurisdiction: US. Status: Granted (USPTO grant number 12,196,792).
- Assignee: not confirmed — PDF was CCITT-fax image-encoded and did not OCR cleanly;
  bibliographic page not independently re-verified. **Assignee/priority date = GAP, retry
  needed against USPTO Patent Full-Text/PatFT or PatentsView API directly.**
- Relevance (1 sentence): Discloses measuring the spatial (turn-to-turn) resistivity
  distribution (TTRD) inside an NI HTS coil non-destructively — i.e., building the exact
  "thermal/electrical conduction map" that CF-3 proposes to act upon for current steering,
  though this patent appears to stop at *measurement*, not steering/control.
- Title/abstract (EN, machine-derived from search snippets): "...relates to a
  non-destructive measurement method and apparatus for the turn-to-turn resistivity
  distribution (TTRD) in non-insulation (NI) superconducting coils... NI HTS coils are
  coils wound with HTS tapes without any organic insulation layer between turns... TTRD
  significantly affects coil performance."
- **This hurts CF-3**: establishes that TTRD-mapping-as-precursor-to-behavior-prediction
  is already claimed territory; CF-3 must clearly differentiate on the *active steering /
  redistribution decision* built on top of such a map, not the mapping itself.

**2. CN115485868A — 高温超导体场线圈 (High-Temperature Superconductor Field Coil)**
- Jurisdiction: CN. Assignee: Tokamak Energy Ltd. Priority date: 2020-05-04.
  Publication: 2022-12-16. Status: Granted (per Google Patents legal-status field, granted
  2026-04-07).
- Relevance: Selectively removes conductive cladding from HTS tape edges to raise
  turn-to-turn resistance in a spatially-graded way, explicitly to keep I/Ic approximately
  constant across coil regions — a passive, geometry-engineered analog of "steering current
  away from" over-stressed regions, though driven by field/critical-current profile rather
  than a thermal-conduction-to-cold-head map.
- Title/abstract (ZH): "围绕绕组中的一个或多个绕组的至少一部分从所述HTS条带中的一个或多个
  HTS条带的轴向边缘去除材料" — material removed from axial edges of HTS tape around part of
  one or more turns to reduce turn-to-turn conductivity in a controlled, spatially-varying way.
  EN translation (machine): "Removing material from the axial edge of one or more HTS tapes
  around at least a portion of one or more windings in the winding, to reduce turn-to-turn
  conductivity."
- **This hurts CF-3**: shows the same assignee family (Tokamak Energy) already patents
  spatially-engineered turn-to-turn resistance to shape current distribution; CF-3's
  novelty must rest on tying the spatial pattern to a *thermal/cooling-path* map specifically
  (cryocooler cold-head conduction), not an electromagnetic field-profile map.

**3. WO2013180802A1 (granted US9,117,578 B2) — "No-insulation multi-width winding for
high temperature superconducting magnets"**
- Jurisdiction: WO (PCT) / US. Assignee: Massachusetts Institute of Technology (MIT).
  Inventors: Seung-Yong Hahn, Yukikazu Iwasa, Juan Bascunan. Priority date: 2012-03-13.
  WO status: Ceased (national phase deadlines lapsed in non-US states, per Google Patents);
  US9,117,578 granted.
- Relevance: Varies HTS tape width turn-by-turn/coil-by-coil (narrow at low-field center,
  wide at high perpendicular-field top/bottom) to equalize I/Ic and current density —
  another passive, pre-engineered (not actively controlled, not thermally-mapped) current-
  steering mechanism in an NI-adjacent winding.
- Abstract (EN, paraphrased from fetch): tape width of double-pancake coils gradually
  increases from magnet center to top/bottom to compensate field-dependent Ic degradation;
  ~22% more field vs. single-width counterpart at same stability.
- **This hurts CF-3**: MIT/Hahn group already has a granted US patent on deliberately
  varying conductor geometry to steer current distribution across the coil; again the
  differentiator for CF-3 must be the *thermal-map-driven* (cold-head-conduction-driven)
  basis for the steering, and/or *active* (measured/controlled in operation) vs. this
  patent's *fixed-at-winding-time* geometry.

**4. US20190074118A1 (granted US10,861,626 B2) — "High-Temperature Superconducting
Coil Having Smart Insulation, High-Temperature Superconducting Wire Used Therefor, and
Manufacturing Method Therefor"**
- Jurisdiction: US (WO2017039299A1 family). Assignee: Korea Electrotechnology Research
  Institute (KERI). Inventors: Seog Whan Kim, Young Sik Jo, Rock Kil Ko, Dong Woo Ha,
  Hyung Wook Kim, Chan Park. Priority date: 2015-09-04. Publication: 2019-03-07.
  Granted: 2020-12-08.
- Relevance: Metal-insulator-transition (MIT, vanadium-oxide-class) material layer between
  turns that is insulating at operating temperature and turns conductive (10^3-10^5x) above
  a transition temperature during a local quench — an intrinsic, temperature-responsive
  bypass, i.e., a *materials-physics* analog to "steer current away from a hot region"
  without any externally measured or engineered spatial thermal map.
- Abstract translation (EN, from fetch): insulating layer with interposed MIT material
  between adjacent superconducting wires; conductivity increases sharply at/above
  transition temperature, enabling autonomous bypass without external monitoring.
- **This hurts CF-3 moderately**: shows temperature-triggered current bypass is already
  patented, though it is autonomous/material-driven rather than steered according to a
  known, spatially-resolved cooling-path map back to a specific cold head; CF-3's
  "known/measured thermal-conduction map"-based *engineering or active control* framing is
  the needed distinguishing feature.

**5. US11,094,438 B2 / US11,551,840 B2 / US20190088391A1 / US20220102040A1 — "Feedback
control for no-insulation high-temperature superconducting magnet"**
- Jurisdiction: US (multiple continuations). Assignee: Florida State University Research
  Foundation, Inc. Inventors: Seungyong Hahn, David Larbalestier. Priority date: 2016-05-06.
  Earliest US filing: 2018-11-06 (US20190088391A1). US11,094,438 granted 2021-08-17;
  US11,551,840 is a continuation, granted subsequently; US20220102040A1 is a further
  continuation application (published 2022-03-31).
- Relevance: A PI (proportional-integral) active feedback controller adjusts the *external
  power-supply current* of an NI HTS magnet based on the discrepancy between reference and
  measured (global) magnetic field, to eliminate charging delay/linearize field response —
  i.e., "active control of current in an NI magnet" is already claimed, though the control
  variable is the bulk power-supply current (a single global knob), not a spatially
  distributed, per-location redistribution driven by a thermal-conduction map.
- Abstract (EN, from fetch): establishes reference field, excites NI HTS coil via power
  supply, monitors reference-vs-measured field difference, controls power-supply current
  per a transfer function including magnet inductance and contact resistance.
- **This hurts CF-3 significantly on the "actively controlled" prong**: prior art already
  covers *active, real-time feedback control of current* in an NI HTS magnet from the same
  MIT/Hahn lineage. CF-3 must clearly claim spatial/local redistribution (turn-level or
  zone-level, tied to a thermal-conduction/cold-head map) rather than a single global
  current-control loop, to avoid reading directly onto this family.

**6. EP4012730A1 / WO2019150123A1 / AU2019214510A1 / CN114512293A / KR20220025932A /
KR102631117B1 — "Partially-Insulated HTS Coils"**
- Jurisdiction family: EP, WO, AU, CN, KR (US family member likely exists as
  US2020365304A1 per FreePatentsOnline title match — unconfirmed, flagged as gap).
  Assignee: Tokamak Energy Ltd. Inventors: Robert Slade, Marcel Kruip, Bas van Nugteren,
  Greg Brittles, Enrique Ruiz de Villa Valdés, Rod Bateman, Alun Down. Priority date:
  2018-02-01. EP filing: 2019-01-31. EP publication: 2022-06-15. EP status: Withdrawn.
  KR102631117B1 status: Granted (per WebSearch summary).
- Relevance: Insulating layer between turns has spatially-staggered "windows" that create
  deliberate, geometrically-placed current paths of controlled resistance between turns —
  directly analogous to "engineering turn-to-turn bypass sites at specific spatial
  locations" to control current distribution and heat generation, addressing ramp-heat vs.
  quench-protection trade-offs.
- Abstract (EN, from fetch): "A superconducting field coil incorporating layers with
  spatially-selective electrical resistance between turns, enabling controlled current
  distribution while maintaining passive quench protection capabilities."
- **This hurts CF-3 significantly**: this is the closest architecture match found — spatial
  engineering of turn-to-turn resistance/contact sites to control current distribution and
  local heating is already claimed by Tokamak Energy across a 5-6 jurisdiction family
  including a granted KR patent. CF-3's necessary differentiator: tying the window/site
  placement pattern specifically to a *measured or known thermal-conduction-to-cold-head
  map* (i.e., cooling-path-aware, not just field/stress-aware) under a cryocooler's limited
  cooling-power budget, and/or making the steering *active/adjustable in operation* rather
  than fixed at winding time.

**7. EP4078630A1 (granted EP4078630B1) — "HTS Linked Partial Insulation for HTS Field
Coils"**
- Jurisdiction: EP (family likely includes WO/US/CN/KR — unconfirmed, flagged as gap).
  Assignee: Tokamak Energy Ltd. Inventor: Greg Brittles. Priority date: 2019-12-20.
  Filing: 2020-12-15. Publication: 2022-10-26. Granted: 2023-11-15. Status: Active.
- Relevance: HTS "bridges" (superconducting material in series with normal metal) placed
  at specific spatial locations act as self-regulating current limiters — regions that
  quench faster become more resistive locally, pushing current toward slower-quenching
  (i.e., relatively "healthier"/cooler) regions; thermal and electrical properties are
  explicitly claimed as independently tunable via geometry.
- Abstract (EN, from fetch, paraphrased): each electrically conductive path comprises an
  HTS bridge in series with normally-conducting material; bridges self-regulate based on
  local temperature during quenching, redistributing current to slower-quenching/cooler
  regions and evening out heating.
- **This hurts CF-3 significantly**: this is functionally very close to "redirect current
  away from thermally weak/hot regions" — but it is (a) self-regulating via local HTS
  critical-temperature physics, not driven by an externally known/measured cold-head
  conduction map, and (b) triggered by quench/local heating events rather than steady-state
  optimization against a fixed cryocooler cooling-power budget. CF-3's distinguishing claim
  should rest on proactive routing based on a *known cooling topology* (distance/conduction
  to the cold head) rather than reactive, temperature-triggered self-limiting.

**8. US11,581,115 B2 — "Superconducting Coil Module"**
- Jurisdiction: US. Assignee: SNU R&DB Foundation (Seoul National University). Inventors:
  Seungyong Hahn, Uijong Bong, Jaemin Kim, Chaemin Im, Jeseok Bang, Soobin An, Jung Tae Lee.
  Priority date: 2019-04-19. Filing: 2020-09-17. Publication: 2023-02-14. Status: Active
  (expiry ~2041-03-27).
- Relevance: A "heating device providing a customized heating path," positioned radially
  across the coil according to each turn's threshold-current profile, deliberately raises
  local temperature where threshold current is highest to equalize critical current and
  suppress screening-current-field (SCF) effects — i.e., an *engineered thermal map
  imposed on the coil itself* to shape electromagnetic behavior, conceptually adjacent to
  CF-3's "use a thermal map to steer current," though the goal here is SCF/critical-current
  equalization (charging-time-scale), not steady-state hot-spot avoidance under fixed
  cryocooler cooling power.
- **This hurts CF-3 moderately-to-significantly**: prior art already discloses deliberately
  engineering a *spatial temperature profile* inside the coil (via heating elements, not
  cooling-path variation) to control current/field behavior. CF-3 should differentiate on
  cooling-path-map-driven (rather than heater-imposed) temperature engineering, and on the
  goal (hot-spot/cooling-budget management vs. SCF/critical-current equalization).

### Tier 2 — Applications (not yet granted / status uncertain)
(See CN114512293A and KR20220025932A within Hit 6's family — status not independently
confirmed beyond the EP-level "Withdrawn"; treated as Tier 2 pending confirmation of
national-phase prosecution status in each jurisdiction.)

### Tier 3 — Peer-reviewed / NPL

**9.** "Hot-Spot Modeling of REBCO NI Pancake Coil: Analytical and Experimental
Approaches" — MIT (PMC/IEEE, and MIT DSpace record). Analytical/experimental hot-spot
temperature modeling in NI pancake coils; foundational physics for predicting where hot
spots form, which any thermal-map-driven steering scheme (CF-3) would need to build on
or distinguish from as background art.

**10.** "Control of turn-to-turn contact resistivity in resistively insulated REBCO
coils" — arXiv 2604.15587 (full text not machine-readable in this session — flagged
partial gap, title/venue only confirmed via search snippet). Title directly suggests
active or engineered control of turn-to-turn contact resistivity, closely adjacent to
CF-3's mechanism; requires a follow-up read before G-NOVEL.

**11.** "Explicit Turn Resolution with Anisotropic Homogenisation for Efficient 3D
Magneto-Thermal Finite-Element Simulation of Large-Scale No-Insulation HTS Magnets" —
arXiv 2605.31009. Simulation-tool NPL; relevant as background modeling capability for
predicting where redistributed current would flow, not itself a steering mechanism.

**12.** "Surface Contact Approximation for Magneto-Thermal Finite Element Analysis of
No-Insulation HTS Coils" — arXiv 2605.28574. Same category as #11.

**13.** "Electromagnetic-Thermal-Mechanical Characteristics With Active Feedback Control
in a High-Temperature Superconducting No-Insulation Magnet" — Science China Physics,
Mechanics & Astronomy (Springer). Analyzes the same Hahn/Larbalestier-style PI active
feedback control (see Hit 5) from a physics/safety-analysis angle; corroborating NPL for
Hit 5's "active but global, not spatial" prior art.

**14.** "Determining Operating Current of No-Insulation Field Coil in HTS Generators" —
(ResearchGate). Addresses how much current an NI coil should run given turn-to-turn
bypass behavior; adjacent background art, not itself a steering claim.

**15.** "Current Bypassing and Transient Stability in a Partially Insulated HTS Coil" —
IEEE Trans. Applied Superconductivity (document 8239865). Directly documents current
bypassing behavior in partially-insulated coils under transient conditions — background
physics for CF-3's mechanism, corroborates that turn-to-turn bypass site engineering
("partial insulation") already has an established NPL literature independent of Tokamak
Energy's patents (Hits 6-7).

**16.** "Electromagnetic Behaviour and Thermal Stability of a Conduction-Cooled,
No-Insulated 2G-HTS Coil at Intermediate Temperatures" — Cryogenics journal
(ScienceDirect S0011227520300722). Directly on point for CF-3's operating regime:
conduction-cooled (cryocooler, no cryogen bath) + NI coil + thermal stability. Does not
appear to include active/engineered spatial current steering — mainly characterizes
baseline behavior — but is the closest NPL match to CF-3's *physical setting* and should
be treated as core background/comparator art for G-PHYS as well as G-NOVEL.

**17.** "Turn-to-Turn Contact Resistance Measurement of No-Insulation REBCO Pancake
Coil: External Field Dependence" — IEEE Trans. Applied Superconductivity (document
9392348). Measurement methodology background, corroborates Hit 1 (US12,196,792) territory.

**18.** "Experimental and Numerical Study on Current Distribution in Parallel Co-Wound
No-Insulation Coils" — arXiv 2507.08552. Documents non-uniform current distribution
among stacked/co-wound tapes; background art on current-distribution phenomena in NI
coils, no steering claim identified.

### Tier 4 — Other / lower-relevance but logged

**19.** US8,823,476 B2 — "Superconducting Magnet Apparatus and Control Method Thereof."
Assignee: Samsung Electronics Co., Ltd. Inventor: Stephen M. Harrison. Priority:
2011-10-11. Publication: 2014-09-02. Status: Expired (fee-related, lapsed 2022-09-02).
Relevance: automated switch (bellows/gas-pressure or shape-memory-alloy) to
connect/disconnect external power to a superconducting coil — a bulk on/off control
mechanism, not turn-level current steering or thermal-map-based redistribution. Logged
because it surfaced in the "active control + superconducting magnet" query cluster and
touches temperature-responsive switching (shape memory alloy), which is tangentially
adjacent to CF-3's "engineered thermal-response bypass site" concept. Low relevance;
included for completeness/candor.

---

## Gaps / Retries (logged, not resolved — move on per instructions)

1. **US 12,196,792 bibliographic data (assignee, inventors, exact priority date)** —
   image-encoded PDF from image-ppubs.uspto.gov would not OCR through WebFetch. Retried
   once (same result). GAP: needs direct PatentsView API or USPTO Patent Public Search
   query, or a Google Patents lookup by number, before G-NOVEL relies on it.
2. **Direct J-PlatJ (Japan Platform for Patent Information) portal access** — not
   available in this environment; JP coverage above is limited to JP family members
   surfaced through Google Patents / WebSearch, which may miss JP-only filings never
   published as WO/EP/US/CN/KR family members (e.g. Toshiba, Mitsubishi, Sumitomo,
   Fujikura, Furukawa domestic-only JP applications). GAP, retried with two additional
   Japanese-language queries; only background NPL/company pages surfaced, no new
   assignee-specific JP patent hits for the CF-3 mechanism. Flagged for a follow-up pass
   with native J-PlatJ or a paid patent-search tool.
3. **Direct KIPRIS (Korea) portal access** — same limitation; KR coverage above is
   limited to KR family members of EP/WO filings (Tokamak Energy family) found via
   Google Patents. No standalone KIPRIS-only search was possible. GAP.
4. **Direct CNIPA portal / native full-text search** — same limitation; CN coverage
   above is limited to CN family members visible via Google Patents (Google Patents CN
   mirror) plus Chinese-language WebSearch, which returned mostly integrated-circuit
   layout-design notices (irrelevant noise) rather than CNIPA's own patent search
   interface. GAP, retried once with a reformulated query; no additional CN-only
   (non-family) hits found for the specific CF-3 mechanism (thermal-map-driven current
   steering) beyond Hit 2 (CN115485868A, a Tokamak Energy family member).
5. **CN/KR/US family members of EP4012730A1 and EP4078630A1** — WebSearch surfaced
   CN114512293A and KR20220025932A/KR102631117B1 for the EP4012730A1 family, and a
   probable US family member for EP4012730A1 (US2020365304A1, matched via
   FreePatentsOnline title only, not independently confirmed via Google Patents). No
   confirmed non-EP family members were found for EP4078630A1 in the time available.
   GAP: full family tree for both Tokamak Energy filings should be pulled directly from
   Espacenet INPADOC family data before G-NOVEL/G-CLAIM finalize on this prior art.
6. **arXiv 2604.15587 full text** — PDF fetch returned only binary/encoded content;
   title ("Control of turn-to-turn contact resistivity in resistively insulated REBCO
   coils") strongly suggests direct relevance to CF-3 but the abstract/authors/venue
   were not independently confirmed. Retried once (same result). GAP: needs direct
   arxiv.org abstract-page fetch (not PDF) in a follow-up pass.
7. **CPC/IPC classification-code browsing (H01F6/06, H01F6/04, H02K55/*, F25B, G01R33)**
   was performed via text-query proxies (Google Patents / WebSearch), not a native
   classification-code browse/export from Espacenet or PatentsView. This is a
   methodology gap: a true CPC-code walk could surface additional unindexed-by-keyword
   hits. Flagged for follow-up with PatentsView API `cpc_current.cpc_group_id` filtering.
8. **GE, Airbus/UpNext, Toshiba, Mitsubishi, Sumitomo, Bruker, Siemens Healthineers,
   IEE-CAS, MIT (beyond Hahn group)** assignee watches: no CF-3-specific hits (thermal-
   map-driven current steering) were found for these assignees in the searches run.
   This is recorded as a negative result, not a confirmed absence of art — these
   companies are prolific HTS patent filers and a keyword-only search is not equivalent
   to an assignee-indexed patent-database pull. GAP: recommend a dedicated
   assignee-field search (not just keyword) via PatentsView/Espacenet applicant-name
   query for each name before relying on "no hits" as clearance.

---

## Summary counts

- Tier 1 (granted/near-scope patents): 8 hits (US12,196,792; CN115485868A; WO2013180802A1/
  US9,117,578; US20190074118A1/US10,861,626; US11,094,438/US11,551,840 family;
  EP4012730A1 family; EP4078630A1; US11,581,115)
- Tier 2 (applications): 0 standalone (family members noted within Tier 1 entries)
- Tier 3 (NPL): 10 hits
- Tier 4 (other): 1 hit
- **Total logged hits: 19**
- Gaps logged: 8

**Notable closest art (for downstream G-NOVEL attention):**
1. EP4012730A1 / KR102631117B1 family (Tokamak Energy, "Partially-Insulated HTS Coils") —
   spatially-selective turn-to-turn resistance windows controlling current distribution.
2. EP4078630B1 (Tokamak Energy, "HTS Linked Partial Insulation") — self-regulating,
   spatially-placed current limiters that redirect current toward cooler/slower-quenching
   regions.
3. US11,094,438/US11,551,840 family (Florida State Univ. Research Foundation / Hahn) —
   already-granted *active* current control of an NI HTS magnet (global, not spatial).
4. US11,581,115 (SNU R&DB Foundation / Hahn) — engineered spatial *temperature* map
   (via heaters) imposed on an NI coil to shape electromagnetic behavior.

All four compose a strong background against which CF-3 will need a tightly-drawn
claim: **active or engineered turn-to-turn current steering specifically driven by a
known/measured thermal-CONDUCTION-TO-COLD-HEAD map** (as opposed to a field/stress map,
an SCF/critical-current map, or a global feedback loop) under a cryocooler's fixed,
limited cooling-power budget. This is a G-NOVEL/G-CLAIM judgment, not made here.
