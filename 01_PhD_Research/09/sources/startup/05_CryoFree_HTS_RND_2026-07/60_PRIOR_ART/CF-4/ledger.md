# CF-4 Prior-Art Ledger — "Cold-Head-Budget Ramp Governor"

**Candidate:** CF-4 — charge/ramp controller for an HTS magnet that bounds AC + eddy-current
loss during ramping to the *measured instantaneous* cryocooler headroom (real-time cold-head
lift budget), instead of a fixed/worst-case ramp-rate limit.

**Wave:** W1 prior-art harvest · **models=prior-art:sonnet x1** (intended; per CLAUDE.md routing
table, prior-art harvest is sonnet/medium) · Run date: 2026-07-10 · Analyst: prior-art-scout
persona, single pass, **REAL WebSearch/WebFetch tool calls this session** (see §0).

**Duty of candor:** every hit below (favorable or damaging) enters CF-4's `IDS_pool`. No
novelty judgment is rendered here — that is the G-NOVEL Fable-5 gate's job downstream.

---

## 0. Access statement (read first) — SUPERSEDES prior version of this file

A prior pass on this candidate claimed "no live web/API access" and filled this ledger with
16 reconstructed/guessed entries (fake patent numbers marked "unverified," invented titles
marked "illustrative reconstruction"). **That claim was false.** This session confirmed
WebSearch and WebFetch both work and return real, current results with working URLs. This
version of the ledger **replaces that one entirely**. Every hit below was returned by an actual
WebSearch or WebFetch tool call made in this session; every number, assignee, date, and URL was
read from a real search result or a real fetched patent page (Google Patents / Justia /
USPTO image-ppubs / ScienceDirect / arXiv / Springer). Nothing here is reconstructed from
training-data memory. Where a jurisdiction/angle genuinely returned nothing on-point after a
real search attempt, that is stated plainly in §2 rather than filled with a guess.

Interesting note for the record: two of the fabricated "reconstructed" entries in the prior
version (a hypothetical Toshiba/Mitsubishi JP excitation-control filing referencing refrigerator
state, and a hypothetical Sumitomo filing combining cryocooler telemetry with magnet charging
control) turned out, on real search, to correspond to **actual** patents — JP2000012326A
(Toshiba) and US6094333A (Sumitomo Electric) respectively (see T1-01, T1-02 below). This is
coincidence / informed-guessing from real domain knowledge of who plays in this space, not
verification of the prior ledger's specific fabricated claims — the actual documents' language,
numbers, and claim scope differ from what was invented, and must be read on their own terms.

---

## 1. Query pack (as actually run)

### Core mechanism terms (EN / ZH / JA / KO) — queries executed this session
| Concept | Query actually run |
|---|---|
| EN core | "patent superconducting magnet ramp rate control cryocooler cooling capacity real-time" |
| EN core | "superconducting magnet excitation control refrigerator temperature patent site:patents.google.com" |
| EN core | "quench-safe charging current limit cryocooler headroom patent HTS magnet" |
| EN assignee | "conduction-cooled superconducting magnet AC loss ramp rate control patent Toshiba Mitsubishi" |
| EN core | "cryocooler cooling capacity margin dynamic ramp rate limit superconducting magnet control patent" |
| JA (伝導冷却/励磁/冷凍機/冷却能力/ランプレート) | "超伝導磁石 励磁 冷凍機 冷却能力 ランプレート 制御 特許" |
| ZH (超导磁体/励磁速率/制冷机/冷却功率) | "超导磁体 励磁速率 制冷机 冷却功率 控制 专利" |
| KO (초전도자석/여자속도/냉동기/냉각능력) | "초전도 자석 여자 속도 냉동기 냉각 능력 제어 특허" |
| ZH assignee (IEE-CAS) | "中国科学院电工研究所 高温超导磁体 励磁 冷头 温度 反馈 控制 专利" |
| ZH CNIPA-focused | "CNIPA 传导冷却 超导磁体 励磁速率 实时 冷量 裕度 控制方法" |
| EN assignee | "Hinetics patent conduction-cooled no-insulation motor coil ramp charging control" |
| EN assignee | "Commonwealth Fusion Systems patent magnet charging ramp rate cooling capacity" |
| EN assignee | "Tokamak Energy patent HTS magnet charging quench protection cryocooler" |
| EN assignee | "Sumitomo Electric OR Sumitomo Heavy Industries patent superconducting magnet charging control cooling capacity refrigerator temperature" |
| EN assignee | "GE Healthcare patent MRI magnet ramp rate refrigerator temperature feedback control quench" |
| EN phrase | "\"cold head\" \"lift budget\" OR \"cooling margin\" superconducting magnet ramp rate real-time control" |
| NPL | "arXiv HTS magnet charging rate limited by cryocooler cooling power adaptive control" |
| NPL | "IEEE Transactions Applied Superconductivity ramp rate cryocooler cooling power feedback control charging" |
| NPL | "Cryogenics journal pulse tube cryocooler cooling power load line temperature dependence characterization" |
| Family check | "US6094333 family JP patent Sumitomo Electric 超電導コイル 冷凍機 冷却曲線 制御" (no useful family result surfaced) |
| Espacenet-style | "espacenet superconducting magnet charging rate limited cooling capacity refrigerator real time" |
| JP family | "JP2000012326A family US CN patent equivalent Toshiba superconducting magnet refrigerator inverter excitation speed" (no distinct family member surfaced beyond JP2000012326A itself) |

### CPC/IPC walk (as specified; not separately queryable via WebSearch — folded into assignee/keyword queries above)
`H01F6/06`, `H01F6/04`, `H02K55/*`, `F25B`, `G01R33`, `H02J`, `H02M`, `H02H7/00` (SC-magnet
protection), `G05B` (feedback control). No dedicated CPC-classification browse tool was
available in this session; class codes were folded into keyword/assignee search strings instead.
This is a gap — see §5.

### Assignee watch — actually searched
Hinetics, GE/GE HealthCare, Toshiba, Mitsubishi Electric, Sumitomo (Electric + Heavy
Industries), Samsung Electronics (surfaced unprompted — not on original watch list but real
hits found under it), Florida State University/NHMFL (surfaced unprompted), Philips (surfaced
unprompted), Commonwealth Fusion Systems, Tokamak Energy, IEE-CAS. Not separately searched this
pass (no hits surfaced under general queries, ran out of budget for dedicated per-assignee
passes): Airbus/UpNext, Fujikura, Furukawa, SuperPower, Shanghai Superconductor, Bruker, Siemens
Healthineers, Korea Univ/KERI/KAIST, MIT. **Flagged for a follow-up pass.**

---

## 2. Per-jurisdiction search log (real results this session)

| Jurisdiction | System reached | Status | Notes |
|---|---|---|---|
| US | Google Patents / Justia / USPTO image-ppubs (via WebSearch + WebFetch) | **ACCESSED — real hits** | See T1-01 (Sumitomo US6094333A), T1-03 (Samsung US9014769B2), T2-02 (Toshiba US20150051079A1/US9305691B2), T2-03 (FSU/NHMFL US11551840B2 family), T4 entries (Philips US8058873B2, US8027139B2, US7412835). |
| Japan | Google Patents JP-language pages (via WebSearch + WebFetch) | **ACCESSED — 1 strong direct hit** | JP2000012326A (Toshiba) — see T1-02, the single closest hit found this session. |
| Korea | Google Patents KO-language pages (via WebSearch + WebFetch) | **ACCESSED — hits found, none directly on point** | KR20130142201A (Taiyo Nippon Sanso, HTS cooling-device turbo-compressor capacity control, not tied to magnet ramp) and KR101406947B1 (Samsung, switch mechanism, not on point) — both real, both ruled adjacent/off-point on inspection, recorded in T4. |
| China | Google Patents ZH-language pages + CJK keyword search (via WebSearch) | **ACCESSED — searched multiple angles, no direct on-point hit found** | Multiple real CN patents surfaced (CN102840708B, CN112562960B, CN117292914A, CN101012982B) — all are cooling-system/cryostat patents, none does ramp-rate-vs-live-cooling-capacity feedback control specifically. IEE-CAS searches surfaced real IEE-CAS conduction-cooled-magnet research (3T animal MRI magnet, high-power-microwave conduction-cooled magnet) as NPL/institutional pages, not a patent on CF-4's specific mechanism. **Stating plainly: no CN patent directly on CF-4's core mechanism was found in this session's searches** — this does not rule one out; CNIPA's own search portal was not directly reachable via WebFetch (returns non-indexable dynamic content) and only Google-Patents-indexed CN documents were reachable. Follow-up via a CNIPA-specific tool is recommended. |
| EP/PCT | Google Patents (EP/WO prefixed documents surfaced organically via WebSearch) | **ACCESSED — family members found, no independent EP-only hit** | EP2624262A2 (Samsung family member of US9014769B2) and WO2017193129A1 (FSU/NHMFL family member of US11551840B2) found; no EP/WO document independent of a US/JP family was found on point. |
| NPL | Google/WebSearch surfacing IEEE Xplore, ScienceDirect, Springer, arXiv, ResearchGate pages | **ACCESSED — several real hits** | See Tier 3 below. IEEE Xplore full-text was not directly fetchable (paywalled), so NPL entries are recorded from search-result abstracts/metadata, with URLs, not from full-text reading. |

---

## 3. Hits (grouped by tier) — ALL REAL, tool-verified this session

### TIER 1 — granted/near-scope patent directly on point (highest priority for G-NOVEL)

**T1-01 — MOST DAMAGING HIT FOUND**
- **Number:** US6094333A ("Operation control method for superconducting coil")
- **Assignee:** Sumitomo Electric Industries, Ltd.
- **Priority date:** 1997-10-24 · **Filing date:** 1998-10-22
- **Jurisdiction:** US (granted)
- **Status:** Expired (lifetime expiration; term has run) — an expired patent is prior art for
  novelty purposes but confers no live enforcement risk.
- **Relevance to CF-4:** Directly on point. Claims a control method for a refrigerator
  conduction-cooling-type superconducting coil that (a) derives an "effective cooling curve"
  from the refrigerator's rated cooling capacity and the measured/calculated thermal resistance
  between refrigerator and coil, and (b) controls coil energization so that generated heat
  (resistive + AC hysteresis/coupling losses) stays below that curve — including a real-time
  monitoring variant where current is automatically reduced if monitored temperature/voltage
  exceeds preset thresholds. This is functionally very close to CF-4's "bound loss to cryocooler
  headroom" mechanism; the main open question for G-NOVEL is whether CF-4's *continuously
  measured, time-varying instantaneous* headroom signal (vs. this patent's precomputed curve +
  threshold-trip real-time variant) is distinguishable.
- **Title/abstract (English, as granted; no translation needed):** "A control method allowing
  stable operation of a refrigerator conduction cooling type superconducting coil employing an
  oxide high temperature superconductor is provided."
- **Source:** https://patents.google.com/patent/US6094333A/en
- **Tier:** 1
- **Verified:** true (fetched directly)

**T1-02 — SECOND MOST DAMAGING HIT**
- **Number:** JP2000012326A ("伝導冷却型超電導磁石システム" / "Conduction-cooled superconducting
  magnet system")
- **Assignee:** Toshiba Corp (株式会社東芝)
- **Priority/filing date:** 1998-06-26
- **Jurisdiction:** JP (granted 2007-06-13, per Google Patents legal-status data)
- **Status:** Expired (fee-related, per Google Patents)
- **Relevance to CF-4:** Directly on point. Claim 4 gives the controller a "function to control
  the output of the magnet power supply" based on temperature detected by a temperature sensor,
  and the system simultaneously adjusts compressor (refrigerator) inverter frequency and magnet
  excitation to prevent quenching, with "magnetization/demagnetization speed freely adjustable
  within [a] non-quench range." This ties ramp/excitation rate to a measured refrigerator/coil
  temperature signal used as a real-time proxy for cooling margin — squarely in CF-4's space
  and, on its face, one of the closer anticipating references identified this session.
- **Title (JA, original):** 「伝導冷却型超電導磁石システム」
- **Title (translation):** "Conduction-cooled superconducting magnet system"
- **Abstract (JA, as fetched):** "冷凍機の冷凍能力を可変して最小の電力で安定した超電導磁石を実現
  し、コンプレッサの消費電力を調整して省エネ効果を得ることにある。"
- **Abstract (translation):** "The invention achieves a stable superconducting magnet with
  minimal power by varying the refrigerator's cooling capacity, adjusting compressor power
  consumption for an energy-saving effect."
- **Source:** https://patents.google.com/patent/JP2000012326A/ja
- **Tier:** 1
- **Verified:** true (fetched directly)

**T1-03**
- **Number:** US9014769B2 (also published as EP2624262A2) — "Cryocooler system and
  superconducting magnet apparatus having the same"
- **Assignee:** Samsung Electronics Co., Ltd.
- **Priority date:** 2012-02-06 · Filing date: 2013-01-28
- **Jurisdiction:** US (granted); EP family member EP2624262A2
- **Status:** Expired — Fee Related (expired 2023-04-21)
- **Relevance to CF-4:** On point but distinguishable. Claims a "thermal inertia member" with
  high heat capacity, thermally contacting the cryocooler cold stage, that passively reduces the
  *rate of temperature rise* in a current lead when heat is generated during magnet ramp-up/
  ramp-down — i.e., it manages the consequence of ramping heat passively (thermal buffering)
  rather than actively throttling ramp *rate* to a measured instantaneous cooling-headroom
  signal. Relevant as adjacent/motivating art and a candidate combination reference for an
  obviousness argument (add active headroom-based rate throttling to this passive buffer), but
  does not itself do what CF-4 does.
- **Abstract (as fetched):** "A cryocooler system having a structure in which a
  temperature-increasing rate in a current lead is reduced when heat is generated while a
  current is ramped-up or ramped-down," using a thermal inertia member at the cold stage.
- **Source:** https://patents.google.com/patent/US9014769B2/nl ; EP family:
  https://patents.google.com/patent/EP2624262A2/nl
- **Tier:** 1
- **Verified:** true (fetched directly)

### TIER 2 — patent application / adjacent granted patent, not directly anticipating but close

**T2-01**
- **Number:** US20150051079A1, granted as US9305691B2 — "Superconducting magnet apparatus"
- **Assignee:** Toshiba Corp (Kabushiki Kaisha Toshiba)
- **Priority date:** 2013-06-28 · Filing date: 2014-06-26
- **Jurisdiction:** US
- **Status:** Active (granted 2016-04-05)
- **Relevance to CF-4:** Adjacent, not anticipating. Uses two independently controlled cooling
  units (different refrigeration methods) for two coil sections to absorb the large transient
  heat load of excitation/demagnetization, and explicitly *tolerates* a temperature rise (up to
  ~10 K) during ramp rather than throttling ramp rate to cooling headroom. Useful as a
  "conventional alternative approach" contrast in a disclosure's background section, and as a
  combination-obviousness risk (temperature-tolerant design + cooling-capacity-based rate
  throttling).
- **Abstract (as fetched):** "A superconducting magnet apparatus includes: a first
  superconducting coil and a second superconducting coil respectively arranged in a vacuum
  container; a first cooling unit configured to cool the first superconducting coil; and a
  second cooling unit configured to cool the second superconducting coil and controlled
  independently from the first cooling unit by a cooling method different from the cooling
  method of the first cooling unit."
- **Source:** https://patents.google.com/patent/US20150051079A1
- **Tier:** 2
- **Verified:** true (fetched directly)

**T2-02**
- **Number family:** US20190088391A1 → US11094438 and continuation US11551840B2; WIPO family
  member WO2017193129A1 — all titled "Feedback control for no-insulation high-temperature
  superconducting magnet"
- **Assignee:** Florida State University Research Foundation, Inc. (work performed at the
  National High Magnetic Field Laboratory, NHMFL, per patent text; government-supported)
- **Priority date:** 2016-05-06 (per US11551840B2 record) · Filing (continuation) 2021-07-27
- **Jurisdiction:** US (granted, active); WO/PCT family member published
- **Status:** Active, expires 2037-05-08 (per Google Patents legal-status data on US11551840B2)
- **Relevance to CF-4:** Close domain (active feedback control of an NI HTS magnet's charging
  current) but a different control variable: this family's PI feedback controller drives the
  power-supply current so *measured field* tracks a *reference field ramping at a fixed,
  predetermined rate* (e.g., 2.5 mT/s) — the ramp-rate setpoint itself is fixed, not derived from
  or bounded by measured instantaneous cryocooler cooling headroom. Strong background/IDS-pool
  entry and a plausible obviousness-combination reference (their field-tracking feedback loop +
  a cooling-headroom-derived ramp-rate setpoint), but does not anticipate CF-4's core mechanism
  as claimed.
- **Abstract (as fetched, US11551840B2):** "An active feedback controller for a power supply
  current of a no-insulation (NI) high-temperature superconductor (HTS) magnet to reduce or
  eliminate the charging delay of the NI HTS magnet and to linearize the magnet constant."
- **Source:** https://patents.google.com/patent/US20190088391A1/en ;
  https://patents.google.com/patent/WO2017193129A1/en ; PDF copies at
  https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11551840 and
  https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11094438
- **Tier:** 2
- **Verified:** true (fetched directly; abstract/claims text confirmed via Google Patents page,
  PDF fetch itself returned corrupted OCR/image data and was not usable for full-text quoting)

### TIER 3 — peer-reviewed NPL directly on point (background/motivating, favorable)

**T3-01**
- **Reference:** "Electromagnetic-thermal-mechanical characteristics with active feedback
  control in a high-temperature superconducting no-insulation magnet," *Science China Physics,
  Mechanics & Astronomy* (Springer Nature Link).
- **Relevance to CF-4:** Directly relevant NPL — active feedback control of NI HTS magnet
  charging with thermal/mechanical coupling; same technical neighborhood as the T2-02 patent
  family. Supports the physics premise (ramp-induced heating in NI coils interacts with
  thermal/mechanical state) without itself being a cooling-headroom-adaptive ramp controller.
- **Source:** https://link.springer.com/article/10.1007/s11433-022-1929-4
- **Tier:** 3
- **Verified:** true (found via WebSearch result listing; full text not fetched — abstract-level
  characterization only)

**T3-02**
- **Reference:** "Systematic approach to determine the transient cooling power and heat leak of
  a commercial pulse tube cryocooler," *Cryogenics-adjacent* (ScienceDirect).
- **Relevance to CF-4:** Directly supports CF-4's problem statement — pulse-tube cryocooler
  cooling power is not a fixed number but a transient, measurable quantity, which is the
  empirical premise for treating cold-head lift budget as something to be measured
  instantaneously rather than assumed worst-case. Favorable background, not competing art.
- **Source:** https://www.sciencedirect.com/science/article/pii/S0011227520302307
- **Tier:** 3
- **Verified:** true (found via WebSearch result listing; abstract-level only)

**T3-03**
- **Reference:** "Record High Ramping Rates in HTS Based Super-conducting Accelerator Magnet,"
  arXiv:2111.06459.
- **Relevance to CF-4:** Discusses cryogenic cooling power required to sustain high ramp rates
  (up to ~300 T/s reported) in HTS accelerator magnets — directly relevant motivating background
  connecting ramp rate to cooling-power demand, supporting rather than anticipating CF-4.
- **Source:** https://arxiv.org/pdf/2111.06459
- **Tier:** 3
- **Verified:** true (found via WebSearch; PDF link real, not separately fetched for full text)

**T3-04**
- **Reference:** "Feedback control for no-insulation high-temperature superconducting magnet"
  related experimental paper reporting linear ramping at 0.09 A/s and significant charging delay
  without feedback control (surfaced in IEEE TAS-focused WebSearch alongside the T2-02 patent
  family; same NHMFL/Florida State research program).
- **Relevance to CF-4:** Companion NPL to T2-02 — establishes the charging-delay/AC-loss physics
  the patent family and CF-4 both act on. Background, not itself a cooling-headroom-adaptive
  scheme.
- **Source:** surfaced via IEEE Xplore search result (https://ieeexplore.ieee.org/document/11106331/
  and related; full text paywalled, not fetched — recorded as a search-result-level NPL hit only)
- **Tier:** 3
- **Verified:** partial (search-result metadata only; full text not independently fetched — flag
  for follow-up before relying on this citation's specifics)

### TIER 4 — adjacent/ruled-out patents and general background (real hits, judged off-point)

**T4-01**
- **Number:** KR20130142201A — "고온 초전도 기기의 냉각 장치 및 그 운전 방법" (Cooling apparatus
  for high-temperature superconducting devices and its operating method)
- **Assignee:** Taiyo Nippon Sanso Corporation (다이요 닛산 가부시키가이샤)
- **Priority date:** 2012-04-13 · Filing 2013-04-12
- **Jurisdiction:** KR
- **Status:** Expired — Fee Related (lapsed 2023-02-25)
- **Relevance to CF-4:** Real, on-topic hit but off-point on inspection: claims dynamic
  turbo-compressor speed control to hold coolant temperature constant against load
  fluctuations (raising/lowering compressor RPM as coolant temperature falls/rises) — i.e.,
  cooling-capacity modulation for steady-state load regulation, with **no link to magnet
  charging/ramp-rate control**. Recorded for candor/completeness.
- **Source:** https://patents.google.com/patent/KR20130142201A/ko
- **Tier:** 4
- **Verified:** true

**T4-02**
- **Number:** KR101406947B1 — "초전도 자석 장치 및 그 제어방법" (Superconducting magnet apparatus
  and its control method)
- **Assignee:** Samsung Electronics Co., Ltd.
- **Priority/filing date:** 2011-10-11
- **Jurisdiction:** KR
- **Status:** Expired — Fee Related (terminated 2021-06-06, unpaid annual fees)
- **Relevance to CF-4:** Real hit, off-point: claims an automatic bellows-type/shape-memory-alloy
  switch for connecting/disconnecting external power and the superconducting coil — a
  persistent-current-switch mechanism, not ramp-rate/cooling-capacity control. Recorded for
  candor.
- **Source:** https://patents.google.com/patent/KR101406947B1/ko
- **Tier:** 4
- **Verified:** true

**T4-03**
- **Number:** US8058873B2 — "Prevention quench in a magnetic resonance examination system"
- **Assignee:** Koninklijke Philips N.V.
- **Priority date:** 2006-11-10 · Filing 2007-11-05
- **Jurisdiction:** US
- **Status:** Expired — Fee Related (expired 2023-11-15)
- **Relevance to CF-4:** Real hit, off-point: predicts *gradient-coil-induced* heat load from
  imaging-sequence protocols and rejects/modifies protocols feedforward to prevent main-magnet
  quench — addresses gradient-field heating, not magnet-excitation/ramp AC loss, and does not
  throttle ramp rate to a measured instantaneous cooling-headroom signal. Recorded for candor as
  a nearby but distinct control philosophy (feedforward protocol rejection vs. CF-4's real-time
  ramp-rate throttling).
- **Source:** https://patents.google.com/patent/US8058873B2/en
- **Tier:** 4
- **Verified:** true

**T4-04**
- **Number:** US8027139B2 — "System and method for superconducting magnet ramp-down"
- **Assignee:** (per Google Patents record — GE-affiliated per search context; assignee field
  not independently re-confirmed by direct fetch this pass, flag for follow-up)
- **Relevance to CF-4:** Real hit; describes a controller receiving magnet parameter values and
  determining current based on present magnet state, with a slow (24–48 hour) fixed-schedule
  ramp-down to avoid quench — this is the "fixed/conventional worst-case ramp schedule" baseline
  CF-4 is positioned against, not a competing live-adaptive scheme. Contrastive background.
- **Source:** https://patents.google.com/patent/US8027139B2/en
- **Tier:** 4
- **Verified:** true (assignee needs a follow-up direct fetch to confirm with certainty)

**T4-05**
- **Number:** US7412835 (also referenced as Patent 7,412,835, issued 2008-08-19) — "Apparatus
  and method for controlling a cryocooler by adjusting cooler gas flow oscillating frequency"
- **Relevance to CF-4:** Real hit; controls cryocooler cooling capacity by adjusting gas-flow
  oscillating frequency in response to cryogen pressure-vessel variation, for an MRI system —
  cooling-capacity modulation on the refrigerator side, but not linked to bounding magnet
  ramp-rate/AC-loss to that capacity. Background only.
- **Source:** https://patents.justia.com/patent/7412835
- **Tier:** 4
- **Verified:** true

**T4-06 (China — real hits found, judged off-point)**
- **Numbers:** CN102840708B ("一种基于传导冷却的超导电机的制冷系统" — conduction-cooling
  refrigeration system for a superconducting motor); CN112562960B ("超导磁体系统、核磁共振设备以及
  核磁共振设备冷却方法" — SC magnet system / NMR equipment / NMR cooling method); CN117292914A
  ("超导磁体冷却系统" — SC magnet cooling system); CN101012982B ("Refrigerator with magnetic
  shield")
- **Relevance to CF-4:** All four are real, found via direct CJK-language search, and all
  address cryostat/refrigeration hardware/cooling-loop design, not ramp-rate-vs-cooling-capacity
  feedback control of magnet charging. Recorded for candor and as confirmation that the CN
  searches run this session were substantive (not merely translated-and-abandoned), even though
  no directly-on-point CN hit was found.
- **Sources:** https://patents.google.com/patent/CN102840708B/zh ;
  https://patents.google.com/patent/CN112562960B/zh ;
  https://patents.google.com/patent/CN117292914A/zh ;
  https://patents.google.com/patent/CN101012982B/en
- **Tier:** 4
- **Verified:** true

**T4-07**
- **Item:** IEE-CAS (Institute of Electrical Engineering, Chinese Academy of Sciences) real,
  publicly-listed research: a 3T conduction-cooled animal-MRI superconducting magnet (dual-stage
  GM cryocooler, passive quench protection via segmentation) and a conduction-cooled magnet for
  high-power microwave devices (four small air-cooled Stirling cryocoolers, 40-50K). Found via
  direct search of IEE-CAS's own institutional pages and a Chinese electrotechnical-society
  journal article.
- **Relevance to CF-4:** Confirms IEE-CAS is real, active, and publishing in exactly this
  conduction-cooled-HTS-magnet space (consistent with the assignee-watch rationale), but no
  patent or paper specifically doing cooling-headroom-adaptive ramp-rate control was located for
  this group in this session's searches. Flagged for a dedicated follow-up CNIPA/assignee-name
  pass.
- **Sources:** https://iee.cas.cn/kxcb/201908/t20190819_5366361.html ;
  https://www.hplpb.com.cn/cn/article/doi/10.11884/HPLPB202436.230334 ;
  https://dgjsxb.ces-transaction.com/fileup/HTML/2023-4-879.htm
- **Tier:** 4
- **Verified:** true (institutional/journal pages real; no specific on-point patent/paper found)

**T4-08 — assignee watches with no hits surfaced this session**
- Hinetics: WebSearch for Hinetics + ramp/charging control surfaced only general product news
  (Illinois Grainger College coverage, AIAA SciTech paper on aircraft propulsion motors with
  cryogen-free SC rotor) and the unrelated T2-02 NI-magnet feedback patent family — **no Hinetics
  patent was found** on ramp-rate/cooling-headroom control. Real search, genuinely empty on this
  specific ask.
- Commonwealth Fusion Systems: real search surfaced CFS's public PIT-VIPER/HTS-magnet technical
  claims (50 kA charging, 3.7 MJ stored energy, 4 T/s discharge) and a Justia assignee list
  (https://patents.justia.com/assignee/commonwealth-fusion-systems-llc) but **no specific patent
  on ramp-rate-vs-cooling-capacity control** was identified in the results returned; the Justia
  assignee page itself would need a manual page-by-page read to rule this out completely — flag
  as an incomplete negative, not a confirmed absence.
- Tokamak Energy: real search surfaced a substantial quench-protection/quench-detection patent
  family (WO2017042541A1, US11101059, US11190006, US11776721, US12562298) — all about detecting
  and safely dissipating a quench (canary-tape detection, controlled LTS-core quenching), **not**
  about bounding ramp rate to live cooling headroom. Recorded in case G-NOVEL/G-CLAIM want the
  quench-protection family as combination-obviousness background.
- **Tier:** 4 (mixed: some entries are real-but-off-point patents, some are confirmed absence of
  a hit)
- **Verified:** true for the patents named; the "no hit" conclusions for Hinetics/CFS are
  time-boxed, not exhaustive.

---

## 4. Prominent flag — closest/most damaging art

**T1-01 (US6094333A, Sumitomo Electric)** and **T1-02 (JP2000012326A, Toshiba)** are the two
closest pieces of art identified this session, and should be the first two documents the G-NOVEL
Fable-5 gate reads in full. Both tie a superconducting coil's excitation/energization behavior
to a refrigerator-derived cooling-capacity or temperature signal; T1-01 explicitly frames this as
staying under an "effective cooling curve" derived from "the refrigerator's rated cooling
capacity," which is conceptually close to CF-4's "measured instantaneous cold-head lift budget."
The key open distinction for G-NOVEL/G-CLAIM to adjudicate: whether CF-4's claim to a
*continuously time-varying, live-measured* headroom signal (as opposed to T1-01's precomputed
curve + threshold-trip real-time variant, or T1-02's temperature-sensor-driven but not
necessarily continuously-optimized ramp-rate modulation) is a patentably distinct improvement.
T1-03 (Samsung US9014769B2) and T2-02 (Florida State/NHMFL NI-magnet feedback family) are
next-closest and should also be read in full before any filing decision.

**Both T1-01 and T1-02 are expired patents** (US6094333A term has run; JP2000012326A expired for
fee non-payment) — expiry does not remove them as prior art for novelty purposes but does mean
they carry no live infringement/FTO risk on their own; T1-03 is also expired. T2-02 (Florida
State/NHMFL family) is **active** through 2037 and its claims should be checked carefully for
freedom-to-operate as well as novelty if CF-4's disclosure ever touches PI-style field-tracking
feedback as an implementation detail.

---

## 5. Gaps / Limitations (honest, this session)

1. **CPC/IPC classification browsing was not available as a distinct tool** in this session —
   WebSearch does not support a true classification-code browse/query the way Espacenet's
   "Classification search" or PatentsView's CPC field query would. All CPC codes named in the
   task (H01F6/06, H01F6/04, H02K55/*, F25B, G01R33, H02J, H02M, H02H7/00, G05B) were folded into
   keyword/assignee search strings rather than run as structured classification queries. A
   follow-up pass with a PatentsView API key or Espacenet CQL query would close this gap.
2. **CNIPA's own search portal (english or chinese UI) was not directly reachable via WebFetch**
   in this session (dynamic/JS-rendered results, not fetchable as static content); all CN
   coverage came from Google-Patents-indexed CN documents surfaced via WebSearch. This is
   probably adequate for major-assignee CN filings but may miss utility-model-only filings not
   well-indexed by Google Patents. **Given CLAUDE.md's China-no-grace-period hard rule, a direct
   CNIPA-portal or commercial CN-patent-database follow-up pass is recommended before any filing
   reliance.**
3. **J-PlatPat and KIPRIS native portals were not directly queried** — all JP/KR coverage came
   from Google-Patents-indexed JP/KR-language pages surfaced via WebSearch. Google Patents'
   JP/KR coverage is generally good for post-1990s filings (consistent with what was found here)
   but a native-portal pass is still recommended for completeness, especially for older or
   utility-model-type JP/KR filings.
4. **Several assignees on the original watch list surfaced no hits this session and were not
   given a fully dedicated, multi-query pass**: Airbus/UpNext, Fujikura, Furukawa, SuperPower,
   Shanghai Superconductor, Bruker, Siemens Healthineers, Korea Univ/KERI/KAIST, MIT. This is a
   real gap (budget/time-boxing), not a confirmed absence of relevant art from these assignees —
   flagged for a follow-up harvest pass.
5. **NPL entries (T3-01 through T3-04) were recorded at search-result/abstract level**; full text
   of the IEEE Xplore and Springer items was paywalled and not independently fetched. Citation
   details (volume/issue/page/DOI) should be confirmed against the publisher page before use in
   any disclosure's background section.
6. **T4-04's assignee** (US8027139B2) was not independently re-confirmed by a direct patent-page
   fetch this pass — flagged for a quick follow-up fetch before relying on the assignee
   attribution.
7. This ledger is now a **completed real-search pass**, not a reconnaissance map: every entry
   carries a real URL and was returned by an actual tool call this session. It is not
   exhaustive (see gaps above) and should be refreshed before any filing-relevant reliance,
   consistent with CLAUDE.md's duty-of-candor and China-no-grace-period rules.
