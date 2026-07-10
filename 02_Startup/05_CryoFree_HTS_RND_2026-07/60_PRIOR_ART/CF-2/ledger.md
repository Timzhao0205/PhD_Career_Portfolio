# Prior-Art Ledger — CF-2: Thermal-Margin-Aware Quench Detection

**Candidate:** Quench-detection (QD) trip thresholds dynamically referenced to a conduction-cooled
temperature map (cryocooler-state telemetry + conduction thermal model of the winding), instead of a
fixed threshold calibrated for LN2/He bath-cooled magnets.

**Wave:** W1 prior-art harvest · **models=prior-art-scout:sonnet** (intended; log per CLAUDE.md model-routing rule)
**Run date:** 2026-07-10
**Search channels used:** WebSearch/WebFetch (general web + Google Patents / Justia / USPTO PatentsPublicSearch
mirrors + patsnap Eureka + IEEE Xplore/ResearchGate/arXiv/OSTI abstracts). No direct authenticated session to
J-PlatPat, KIPRIS, CNIPA, or Espacenet was available in this environment — see **Gaps** section. All searches
personal-access, read-only; nothing was posted or submitted anywhere.

---

## Multilingual Query Pack Used

| Language | Terms |
|---|---|
| English | quench detection; dynamic/adaptive threshold; thermal margin; conduction-cooled; cryocooler; cold head; temperature map; no-insulation; hot-spot forecast; digital twin |
| Chinese (简体) | 失超检测; 传导冷却; 无绝缘; 冷头; 阈值; 温度; 温升预测; 超导磁体; 失超保护 |
| Japanese | クエンチ検出; 伝導冷却; 無絶縁; コールドヘッド; しきい値; 温度マップ |
| Korean | 퀜치 감지; 전도냉각; 무절연; 냉각헤드; 임계값; 초전도자석 |

CPC/IPC walk attempted (no direct class-browse session available; used as search-term qualifiers instead):
H01F6/06, H02H7/00 (quench/overcurrent protection), G01R33 (magnetic measurement), F25B (refrigeration/cryocoolers).

Assignee watches queried: Hinetics, GE (Healthcare), Airbus/UpNext, Toshiba, Mitsubishi, Sumitomo (Electric),
Fujikura, Furukawa (Electric/SuperPower), Shanghai Superconductor, IEE-CAS, Tokamak Energy, CFS, Bruker,
Siemens Healthineers, Korea Univ/KERI/KAIST, MIT, Florida State University Research Foundation (organically
surfaced), Energy Singularity / 星环聚能 (organically surfaced, China fusion HTS magnet developer).

---

## Hits

### Tier 1 — granted / near-scope patents

**1. US11101059B2 — "Quench detection in superconducting magnets"**
- Assignee: Tokamak Energy Ltd
- Priority: 2017-03-31 (filed 2018-03-27) · Granted 2021-08-24
- Jurisdiction: US (family likely includes GB/WO — not separately confirmed here)
- Status: Granted
- Relevance (1 sentence): Discloses a striated-HTS-tape voltage-amplification quench sensor for indirectly-cooled (non-bath) HTS magnets, but detection is a **static, predetermined voltage threshold** ("voltage difference in excess of a predetermined value") with no cryocooler-state or thermal-model input — supports novelty of CF-2's dynamic-reference mechanism while confirming the problem space (indirect/conduction-cooled HTS, reduced "spot" cooling power) is already patent-literate.
- Original title/abstract (EN, no translation needed): "A superconducting magnet ... HTS tape divided into strips connected in series ... detection unit configured to detect onset of loss of superconductivity by detecting a voltage difference in excess of a predetermined value or a rate of change of voltage difference in excess of a predetermined value."
- Tier: 1

**2. US7876100B2 — "Method and apparatus for actively controlling quench protection of a superconducting magnet"**
- Assignee: General Electric Company
- Priority: 2007-01-09
- Jurisdiction: US
- Status: Granted
- Relevance: MRI-magnet quench controller comparing induced/integrated coil voltage to **fixed thresholds** (e.g., "0.1 Vs or 0.2 Vs", "ten times typical coil induced voltage") and triggering blanket heater response; explicitly contemplates cryocooler-cooled ("4K cryocooler") closed systems but ties detection only to voltage, never to cryocooler operating state or a thermal model — a clean contrast case for CF-2, and an assignee to watch (GE Healthcare) given its cryocooler-based MRI product line.
- Tier: 1

**3. GB2514372A — "Quench Protection System for a Superconducting Magnet"**
- Assignee: (Oxford Instruments-adjacent per GB filing family; not independently confirmed — flag for counsel verification)
- Jurisdiction: GB
- Status: Granted (GB)
- Relevance: Lorentz-force-actuated heater contact triggered by a fixed voltage threshold across a resistor; explicitly discusses both wet (bath) and cryocooler (pulse-tube) cooled magnets but the threshold is static and not linked to cooling mode — directly on-point contrast art (same problem framing: bath vs. cryocooler cooling affecting protection needs) but does NOT anticipate dynamic thermal-margin referencing.
- Tier: 1

**4. US7649720B2 — "Quench protection of HTS superconducting magnets"**
- Assignee: Florida State University Research Foundation, Inc.
- Priority: 2005-05-06 · Granted 2010-01-19
- Jurisdiction: US
- Status: Granted
- Relevance: Distributed-heater HTS quench protection with pre-calculated (geometry-based, not real-time) temperature-rise targets (e.g., ΔT=34K, 25K/s); detection is event-reactive to a quench detector, not continuously thermally adaptive — relevant as background art for "temperature-rise-based" protection concepts but not to the dynamic/live-referencing mechanism of CF-2.
- Tier: 1

**5. US10515749B2 / US11217373 — "Frequency loss induced quench protection system for high temperature superconductors and associated method of use"**
- Assignee: The Florida State University Research Foundation, Inc.
- Priority: 2017-10-20 (filed 2018-10-22)
- Jurisdiction: US
- Status: Granted (continuation US11217373 also granted)
- Relevance: Detects transport-current imbalance via Hall-effect sensors and induces deliberate inductive (FLIQ) heating to homogenize a hot spot — a fundamentally different (current-imbalance, not temperature-map) detection mechanism; low direct overlap but same problem space (HTS coil hot-spot protection) and should stay in the IDS pool.
- Tier: 1

**6. US20200091702A1 / US11190006B2 — "Quench protection in superconducting magnets"**
- Assignee: Tokamak Energy Ltd
- Priority: 2016-12-21 (filed 2017-12-14) · Granted 2021-11-30
- Jurisdiction: US
- Status: Granted
- Relevance: Toroidal/poloidal field coil quenchable sections with material-based (resistivity/heat-capacity ratio) energy absorption; hybrid bath+conduction cooling (not cryocooler-only); detection described as event-based, not adaptive-threshold. Background art for fusion-magnet quench protection; low direct overlap with dynamic thermal-margin referencing.
- Tier: 1

**7. US20230384356A1 / US12578370B2 — "Quench detection in superconductors"**
- Assignee: University of Houston System
- Priority: 2022-05-28 · Granted 2026-03-17
- Jurisdiction: US
- Status: Granted
- Relevance: Standing-wave/transmission-line reflectometry quench sensing (frequency-domain Q-factor disturbance), a binary/passive detection method with no threshold-adaptation or thermal-model tie-in — different sensing modality, low overlap, IDS-pool entry.
- Tier: 1

**8. CN102214911B — 一种超导磁体失超保护装置 ("A Superconducting Magnet Quench Protection Device")**
- Assignee: Institute of Electrical Engineering, Chinese Academy of Sciences (IEE-CAS)
- Priority: 2011-05-27
- Jurisdiction: CN
- Status: Granted
- Relevance (translated): Heater-circuit quench protection for MRI/NMR superconducting magnets, gated by **fixed diode voltage thresholds** ("二极管组件的电压阈值") with explicitly no temperature-dependent or cooling-state logic — direct contrast art from the IEE-CAS assignee watch list; confirms static-threshold baseline is the norm in Chinese patent literature too.
- Tier: 1

**9. CN101446610B — 高温超导磁体的失超检测电路 ("Quench-detection circuit of high-temperature superconducting magnet")**
- Assignee: China Electric Power Research Institute
- Priority: not confirmed from available abstract (flag for verification)
- Jurisdiction: CN
- Status: Granted (per Patsnap Eureka listing)
- Relevance (translated): Analog comparator circuit (correction circuit + optocoupler isolation + differential op-amp) comparing paired-coil voltages; static comparison circuit, no temperature or cooling-state input — contrast art, confirms field-standard voltage-comparator baseline in China.
- Tier: 1

### Tier 2 — pending applications

**10. CN122194022A — 一种用于超导磁体的失超检测系统及方法 ("A quench detection system and method for superconducting magnets")**
- Assignee: Suzhou Xinghuan Junen (Energy Singularity) Technology Co., Ltd. / Shanghai Xinghuan Junen Technology Co., Ltd.
- Priority/filing: reported filed ~April 2026 (Chinese fusion-energy HTS magnet developer; publication surfaced via secondary Chinese news source, not the primary CNIPA record — **flag for direct CNIPA verification**)
- Jurisdiction: CN
- Status: Application (pending, per secondary source)
- Relevance (translated): Coupling-coil + bridge-circuit + comparator system that outputs a quench signal "in the case that the difference between the first and second voltage signals exceeds a first preset threshold" (差值超过第一预设阈值) — a **preset (fixed) threshold**, not a dynamically-referenced one; notable because this is a live 2026 Chinese fusion-magnet HTS assignee actively patenting quench detection in the same technical neighborhood as CF-2's theme (conduction-cooled/cryocooler-only HTS coils for compact fusion) — worth a refresh pass before filing given this applicant's cadence.
- **This hit hurts the candidate somewhat**: it establishes that a directly relevant, currently-active Chinese HTS-magnet assignee is filing quench-detection IP in 2026, raising the chance of an undisclosed co-pending filing on a more elaborated (dynamic-threshold) version. Recommend a follow-up CNIPA-direct search closer to any filing decision.
- Tier: 2

**11. US20190074118A1 — "High-Temperature Superconducting Coil Having Smart Insulation, High-Temperature Superconducting Wire Used Therefor, and Manufacturing Method Therefor"**
- Assignee: not independently confirmed (Korean-origin filing per search context — flag for verification; likely Korea Univ / KERI-adjacent given "smart insulation" MIT-material NI coil terminology common in that literature)
- Jurisdiction: US (likely KR priority — unconfirmed)
- Status: Application (per search snippet; grant status not confirmed)
- Relevance: Uses a metal-insulator-transition (MIT) phase-change material layer co-wound with the HTS tape as a passive, materials-based local quench/temperature sensor — an interesting adjacent "smart" detection concept, but the adaptivity is a material phase transition at a fixed physical temperature, not a live cryocooler-telemetry-driven trip-threshold recompute. Contrast art; recommend fetching full text before G-NOVEL.
- Tier: 2

### Tier 3 — peer-reviewed / preprint NPL (highest-relevance non-patent hits)

**12. "A Quench Protection Method for HTS Coils Based on Temperature Rise Forecast," IEEE Xplore doc #9893361 (2022)**
- Venue: IEEE Transactions on Applied Superconductivity (or related IEEE venue per Xplore doc numbering — exact journal/volume not independently confirmed from the snippet; verify before relying on this citation)
- Relevance (1 sentence): **This is the single closest piece of prior art found for CF-2.** It explicitly targets *conduction-cooled* HTS energy-storage magnets, notes that temperature-based detection lags current-based triggers due to thermal hysteresis, and proposes a **temperature-rise forecast** (i.e., a predictive/model-based estimate of impending temperature rise, used as the protection trigger) that the authors validate specifically "under overcurrent or **poor refrigeration conditions**" — i.e., degraded cryocooler/cooling-state scenarios materially change when the trigger fires. This is conceptually adjacent to CF-2's "thermal-margin estimate referenced to cryocooler state" but (from the abstract-level detail available) appears to forecast a single lumped/coil-level temperature-rise trajectory driven by measured current, rather than building a spatial conduction-cooled temperature **map** across the winding referenced against live cryocooler telemetry. This distinction (single forecast point vs. spatial thermal-margin map tied to cooler-state telemetry) is exactly the kind of narrow-but-real difference the G-NOVEL/G-CLAIM gates need to evaluate — flagged as the top item for the Fable gates.
- Original title: as given (English-language IEEE paper; no translation needed)
- Tier: 3 — **HIGH PRIORITY: obtain full text before G-NOVEL gate.**

**13. "Overcurrent Quench Detection of Parallel-Wound No-Insulation High Temperature Superconductor Coil Based on Digital Twin Method," IEEE Xplore doc #10412643 (2024)**
- Relevance: Uses an FEM+AI "digital twin" to predict maximum current (and by extension incipient overcurrent quench) within 0.039s for parallel-wound NI HTS coils; the digital-twin/real-time-model-driven trigger concept is structurally analogous to CF-2's "conduction thermal model referenced to live telemetry," but the modeled quantity is coil current/inductance non-uniformity (electromagnetic), not a spatial temperature/thermal-margin map driven by cryocooler-state telemetry. Adjacent methodology, different physical driver — relevant background for the digital-twin framing of any CF-2 disclosure.
- Tier: 3

**14. "Thermal quench modeling of REBCO racetrack coils under conduction cooling at 30 K for aircraft electric propulsion motors," arXiv 2507.20178 (Hussain, Dadhich, Pardo — Institute of Electrical Engineering, Slovak Academy of Sciences, 2025)**
- Relevance: Directly in CF-2's target application space (conduction-cooled REBCO racetrack coils for aircraft-motor-class HTS windings, i.e., the Hinetics/CRUISE-adjacent use case) and explicitly flags "quench detection" and "rapid thermal management" as open challenges, but performs post-hoc fault analysis only — no adaptive-threshold or live thermal-margin-referenced protection scheme is proposed. Useful as a "the problem is acknowledged as open in the literature" citation supporting CF-2's rationale, and it does NOT anticipate the mechanism. Helps the candidate (shows unmet need) rather than hurting it.
- Tier: 3

**15. "Quench Detection and Protection for High-Temperature Superconductor Accelerator Magnets," Instruments 5(3):27 (2021), MDPI/OSTI #1812231, Fermilab-affiliated**
- Relevance: Survey of non-voltage quench-detection techniques (acoustic, MEMS acoustic-array, fiber optic) motivated by the same underlying physics CF-2 relies on — HTS's large thermal margin and slow normal-zone propagation make fixed voltage thresholds unreliable — but the paper catalogs detection-modality alternatives, not threshold-referencing-to-a-live-conduction-cooled-thermal-map. Strong rationale-supporting NPL; does not anticipate.
- Tier: 3

**16. "A Quench Detection and Monitoring System for Superconducting Magnets at Fermilab," arXiv 2112.00823 (2021)**
- Relevance: Describes a deployed QPM (quench protection/monitoring) system on the Fermilab AUP magnet test stand; background/implementation reference for how quench-monitoring electronics are typically built (fixed-threshold voltage taps + DAQ), useful as a baseline-technology citation. Tier 3, low direct overlap.

**17. "Data-Driven Optimisation of Superconducting Magnets at CEA Paris-Saclay," arXiv 2603.29740 (2026)**
- Relevance: CEA is reported to be developing "digital twins of the superconducting systems" in a data-driven optimization context; full-text extraction failed in this pass (PDF encoding issue — see Gaps). Flagged for a follow-up fetch; potentially relevant if CEA's digital twin work touches quench-trigger logic tied to real-time thermal/cooling state.
- Tier: 3 (unconfirmed relevance — **gap, retry recommended**)

**18. Hinetics CRUISE-program public technical disclosures (5 MW, 3000 rpm-class superconducting motor; NI racetrack REBCO field coils, copper thermal-plate reinforced)** — surfaced via search snippets referencing Hinetics' own conduction-cooled coil work.
- Relevance: Confirms Hinetics (the anchor exemplar assignee for this project's theme) is publicly describing conduction-cooled NI field-coil work; no Hinetics quench-detection patent or publication was located in this pass specifically addressing dynamic/adaptive QD thresholds. Recommend a dedicated Hinetics-assignee patent-family search (USPTO assignee search + WIPO PatentScope) in a follow-up wave, since Hinetics is the closest commercial analog and any of their own filings would be the most load-bearing prior art (including potential self-collision if the user has any connection to or awareness of Hinetics IP).
- Tier: 4 (no direct document found — noted as an open thread, not a confirmed hit)

### Tier 4 — other / unconfirmed / background

**19. US20160178716A1 / CN107110928B — "System and method for cooling a magnetic resonance imaging device/apparatus"**
- Assignee: (GE-family per CN107110928B listing context)
- Relevance: Discusses a "ride-through period" after cryocooler interruption during which helium boil-off delays quench — relevant adjacent concept (cooling-interruption tolerance window) but is about extending time-to-quench via cryogen buffering, not about referencing QD trip thresholds to a live thermal map. Background only.
- Tier: 4

**20. EP2624262A2 — "Cryocooler system and superconducting magnet apparatus having the same"**
- Relevance: Cryocooler-magnet system patent surfaced in CPC-adjacent search; abstract-level relevance to cooling architecture, no confirmed quench-detection-threshold content in the snippet obtained. Flag for full-text review.
- Tier: 4

**21. 한국전기연구원(KERI) 전도냉각형 초전도자석 press coverage (Korean-language)**
- Relevance: Confirms KERI's public conduction-cooled (NbTi, 4.9K, cryocooler-based) superconducting magnet program exists and reports quench-free operation at 360A/1MJ, but no patent-level quench-detection-threshold detail was retrievable from press coverage. KERI remains an assignee to re-check directly in KIPRIS.
- Tier: 4

---

## Assessment Note (harvest-level only — NOT a novelty judgment; that is G-NOVEL's job)

The clearest pattern across all Tier-1/2 patent hits: essentially every quench-protection patent found (Tokamak Energy x2, GE, Florida State x2, IEE-CAS, China Electric Power Research Institute, Energy Singularity/Xinghuan Junen) uses a **static/fixed threshold** (voltage, current-imbalance, or diode-gated) even when the underlying magnet is explicitly conduction-cooled or cryocooler-based. The one piece of art that meaningfully narrows CF-2's claim space is the Tier-3 NPL item #12 ("Temperature Rise Forecast," IEEE #9893361), which ties a predictive temperature trigger to refrigeration-condition variability, and to a lesser extent NPL item #13 (digital-twin overcurrent prediction). Neither, on the information retrieved here, builds a **spatially resolved conduction-cooled temperature/thermal-margin map that is referenced against live cryocooler-state telemetry** to set QD trip logic — but full-text review of #12 (and a CNIPA-direct check of #10, CN122194022A) is needed before any confident G-NOVEL call, given this is the closest art and duty-of-candor requires it be weighed honestly.

## Gaps / Retry Log

- No authenticated/direct session available to J-PlatPat, KIPRIS, CNIPA, or Espacenet Advanced Search in this
  environment; all CN/JP/KR coverage here is via secondary sources (Google Patents mirrors, Patsnap Eureka,
  Chinese news aggregators, Korean press/TLO pages). **Retry recommended** with direct API/session access
  before any filing-relevant decision — this is the single biggest coverage gap for a China/Japan/Korea-heavy
  theme per the mission brief.
- IEEE Xplore doc #9893361 (item #12, the top hit) — only abstract-level detail obtained via search snippets;
  full text not fetched (paywalled). **Retry: obtain full text via institutional/personal access before G-NOVEL.**
- arXiv 2603.29740 (CEA digital twin, item #17) — PDF fetch returned corrupted/compressed text; one retry
  attempted and also failed. **Gap logged, not retried a second time per instructions; move on.**
- US7649720 / US10515749 raw USPTO image-PDF fetches failed (CCITT-fax scanned images); successfully
  recovered via Google Patents mirror on retry — no further gap.
- Hinetics' own patent family: no direct hit found this pass despite dedicated queries. **Retry recommended**
  via a direct USPTO PatentsView assignee-name query for "Hinetics" in a follow-up wave (not available as a
  live tool in this session).
- CN122194022A (item #10): only secondary-source (news aggregator) abstract text obtained, not the primary
  CNIPA/patent-office record. **Flag for direct verification before relying on the "fixed threshold" reading.**

## Duty of Candor

All 21 hits above (Tiers 1-4), including the ones that narrow or potentially defeat CF-2 (items #12, #13, and
#10 in particular), are entered into CF-2's `IDS_pool` per the project's duty-of-candor rule. No hit was
withheld or filtered based on whether it helps or hurts the candidate.
