# CF-6 Prior-Art Ledger — "Thermal-contraction-matched NI interface"

`models=stage:W1-prior-art-harvest:sonnet[x1]` (per CLAUDE.md model-routing table; logged as intended model=sonnet)

Wave: W1 prior-art harvest. Candidate core mechanism: a turn-to-turn NI interface in an
HTS coil engineered to hold BOTH Rc and thermal contact across cooldown + repeated
cryocooler thermal cycling, in cryogen-free/conduction-cooled operation specifically
(vs. steadier bath-cooled environments). Related concepts: compliant/spring-loaded
contact layers, CTE-matched/graded interlayers, solder-joint thermal fatigue, contact
pressure maintenance across cooldown.

Duty of candor: every hit below enters CF-6's `IDS_pool`, including hits that hurt
this candidate. No novelty judgment is made here — that is G-NOVEL's job (Fable-5, W3).

---

## 1. Query pack (English + machine-translated CN/JP/KR)

| Concept | EN | 简体中文 | 日本語 | 한국어 |
|---|---|---|---|---|
| Conduction cooling | conduction-cooled / conduction cooling | 传导冷却 | 伝導冷却 | 전도냉각 |
| No-insulation coil | no-insulation (NI) HTS coil | 无绝缘线圈 / 无绝缘高温超导线圈 | 無絶縁コイル / 無絶縁高温超電導コイル | 무절연 코일 / 무절연 고온초전도 코일 |
| Contact resistance | turn-to-turn contact resistance (Rc) | 接触电阻 / 匝间接触电阻 | 接触抵抗 / ターン間接触抵抗 | 접촉저항 / 턴간 접촉저항 |
| Thermal contraction / CTE mismatch | thermal contraction, CTE mismatch, differential thermal contraction | 热收缩 / 热膨胀系数失配 | 熱収縮 / 熱膨張係数不整合 | 열수축 / 열팽창계수 불일치 |
| Thermal cycling degradation | thermal cycling degradation, cooldown cycling fatigue | 热循环退化 / 冷热循环劣化 | 熱サイクル劣化 | 열사이클 열화 |
| Cold head | cold head, cryocooler cold stage | 冷头 | コールドヘッド | 콜드헤드 |
| Cryocooler | cryocooler, refrigerator | 低温制冷机 / 低温冷冻机 | 冷凍機 / クライオクーラー | 극저온냉동기 / 냉동기 |
| Other | spring-loaded contact, compliant interlayer, solder joint fatigue, contact pressure maintenance | 弹簧接触 / 柔顺中间层 / 焊点疲劳 / 接触压力保持 | ばね接点 / コンプライアント中間層 / はんだ接合疲労 | 스프링 접촉 / 컴플라이언트 중간층 / 솔더 조인트 피로 |

CPC/IPC walk terms used alongside query pack: H01F6/06, H01F6/04, F25B (cryocooler/
refrigeration), G01R33 (magnetic field measurement using superconductors), H02K55/*
(superconducting machines).

Assignee watch list applied: Hinetics, GE, Airbus/UpNext, Toshiba, Mitsubishi,
Sumitomo, Fujikura, Furukawa, SuperPower, Shanghai Superconductor, IEE-CAS, Tokamak
Energy, CFS, Bruker, Siemens Healthineers, Korea Univ/KERI/KAIST, MIT, and (added
during harvest per hits found) Florida State University Research Foundation (FSU-NHMFL,
inherits the SuperPower/Iwasa-Hahn NI-coil IP lineage), Korea Basic Science Institute,
Robinson Research Institute (Victoria Univ of Wellington) / OpenStar Technologies.

---

## 2. Search log by channel

**Tooling available this run:** `WebSearch` (general web search engine, not a direct
patent-office query interface) and `WebFetch` (page-content fetch). No direct
authenticated access to USPTO Patent Public Search, CNIPA (patent.cnipa.gov.cn),
J-PlatPat, KIPRIS, or Espacenet/WIPO PatentScope query forms was available in this
session — those are interactive/JS-driven search portals that WebFetch cannot drive.
**Access-gap note (logged honestly, not fabricated):** direct DB query forms for
CNIPA/J-PlatPat/KIPRIS/Espacenet were not reachable as query interfaces; retried once
via targeted native-language WebSearch queries (proxy through Google-indexed patent
text, Google Patents mirrors, and KISTI/koreascience/astamuse aggregators) as a
fallback. This proxy reaches most **published/granted** patent families (Google
Patents indexes CNIPA, JPO, KIPRIS, EPO/WIPO publications) but may under-recall very
recent Chinese utility models, KIPRIS-only unpublished applications, or JPO
gazette-only records not yet mirrored by Google. **This gap must be closed with a
live KIPRIS/J-PlatPat/CNIPA query pass before any filing-relevant reliance
(G-NOVEL/G-CLAIM) on CF-6's novelty conclusion.**

- **US (USPTO/PatentsView, via Google Patents + Justia + USPTO PPUBS PDF mirrors):**
  searched EN query pack + CPC terms + assignee watch. Retrieved and read in full:
  US11282624B2, US20190088391A1 (+ family US11094438, US11551840), US11101060B2.
  Found via secondary hits: US4930318 (cryocooler cold-head interface, Belleville
  washer contact pressure), US5701742 (indium gasket thermal joint in cryocooler).
  No retry needed — good recall.
- **China (CNIPA, via Google Patents zh-mirror + native 简体中文 query pack):**
  searched 无绝缘/传导冷却/接触电阻/热循环/专利 combinations. Retrieved CN115485868A
  (Tokamak Energy CN national-phase filing), CN105869782B (HTS wire prep, lower
  relevance). Found IEE-CAS (中国科学院电工研究所) conduction-cooled magnet R&D
  (HPLPB journal) and a 2024 press mention of 星环聚能 (Xingsheng Juneng, a Chinese
  fusion startup) claiming NI-coil design work validated through repeated thermal
  cycling — **this is a press/news mention, NOT a verified patent number; flagged
  low-confidence, needs direct CNIPA verification, not entered as a numbered patent
  hit.** Retried once with an IEE-CAS-specific query; no additional CN patent number
  surfaced for the CTE/thermal-cycling-specific mechanism — recall gap noted above.
- **Japan (J-PlatPat, via Google Patents ja-mirror + astamuse + native 日本語 query
  pack):** searched 無絶縁/接触抵抗/熱サイクル/特許. Retrieved JP2012033947A and the
  astamuse record for JP2017-535948 (PCT national-phase entry, "部分絶縁巻線を用いた
  超電導コイル" — appears to be the Japanese national-phase sibling of the Tokamak
  Energy partially-insulated-HTS-coils WO family). Neither was fully abstract-verified
  by direct fetch (JP-language patent-office PDF viewers were not fetchable); titles
  and family linkage are moderate-confidence only.
- **Korea (KIPRIS, via Google Patents ko-mirror + KISTI/scienceon + koreascience.kr):**
  searched 무절연/접촉저항/열사이클/특허. Retrieved KR101665038B1 (Korea Basic
  Science Institute, conductive-impregnated NI coil) and identified (not fully
  fetched, title/abstract sourced from KISTI listing only) a KERI patent record titled
  "전도 냉각을 위한 초전도 코일 장치" (superconducting coil apparatus for conduction
  cooling), KISTI record cn=KOR1020130130009 — flagged for direct KIPRIS verification.
  Multiple koreascience.kr NPL hits on MI/SS coil contact resistance under conduction
  cooling were retrieved (Tier 3, see below).
- **EU/PCT (Espacenet/WIPO PatentScope, via Google Patents EP/WO mirrors):** retrieved
  full Tokamak Energy family: EP4078630A1/WO2021122522A1 ("HTS linked partial
  insulation for HTS field coils") and WO2019150123A1/EP4012730A1/AU2019214510A1
  ("Partially-insulated HTS coils"). Both fully fetched and read.
- **NPL (IEEE TAS, SUST/IOPscience, Cryogenics, arXiv):** good recall via WebSearch;
  several IOPscience/ScienceDirect abstracts blocked by publisher paywall on direct
  WebFetch (HTTP 403) — retried once via a second WebSearch query for
  title+author+abstract snippet, which recovered enough detail for a duty-of-candor
  entry in every case (see Tier 3 list). Full-text was not obtainable in this session;
  flagged where only a search-snippet abstract (not the published abstract verbatim)
  was recovered.

---

## 3. Hit list (grouped by tier)

### TIER 1 — Granted / near-scope patents

**T1-1. US 11,282,624 B2 — "Rare earth barium copper oxide magnet coils and methods"**
- Assignee: Florida State University Research Foundation, Inc. (FSU/NHMFL — inherits
  the Iwasa/Hahn NI-coil lineage)
- Priority: 2018-02-23 · Filed: 2019-02-22 · Granted/Pub: 2022-03-22
- Jurisdiction: US · Status: Granted (in force)
- **Relevance to CF-6 (HURTS):** Discloses REBCO tape with resistive coatings
  (Cu-oxide, Cr, Ni, Ni-P) and stainless-steel interlayers (Ni/Cu-plated) specifically
  to *engineer/control* turn-to-turn Rc, and reports experimental data showing (a)
  **thermal cycling** 4.2 K -> 273 K changes Rc only modestly (0.8 -> ~3.1 µΩ·cm²,
  does not reset to as-built value) and (b) **mechanical/pressure cycling** (~1000
  cycles, 2.5–25 MPa contact pressure) drops Rc to ~1/10 of its initial value — i.e.
  it already claims engineered-interlayer control of Rc AND reports the exact
  cycling-driven Rc-degradation phenomenon CF-6 targets. Does not explicitly address
  CTE-mismatch design or spring-loaded/compliant contact-pressure maintenance across
  cooldown, and is not framed around cryocooler-duty-cycling vs. bath-cooled
  comparison — this is CF-6's most viable design-around delta, but counsel review is
  required before relying on that delta.
- Original language: English (native).
- Query terms that found it: "CTE matched interlayer no-insulation HTS coil conduction
  cooled patent"; SuperPower/NI-coil assignee watch.

**T1-2. US 2019/0088391 A1 (+ granted siblings US 11,094,438 B2, US 11,551,840 B2) —
"Feedback control for no-insulation high-temperature superconducting magnet"**
- Assignee: Florida State University Research Foundation, Inc.
- Priority: 2016-05-06 · Filed: 2018-11-06 · Pub: 2019-03-21 (granted siblings later)
- Jurisdiction: US · Status: Application published; sibling patents granted
- **Relevance to CF-6:** Same family/assignee as T1-1; models Rc as a lumped parallel
  resistor and controls charging delay via feedback rather than interface material
  engineering. Does not address thermal-cycling Rc degradation directly — lower
  direct relevance than T1-1, included for family completeness and assignee-watch
  duty of candor.
- Original language: English (native).
- Query terms: "SuperPower no-insulation REBCO coil patent US"; assignee watch (MIT/
  FSU lineage).

**T1-3. US 11,101,060 B2 — "Partially-insulated HTS coils"**
- Assignee: Tokamak Energy Ltd
- Priority: ~2018-02-01 (family priority) · Granted: 2021-08-24
- Jurisdiction: US · Status: Granted
- **Relevance to CF-6:** Uses a metal-insulator-transition material (e.g. vanadium
  oxide) between turns whose resistance changes ~10x+ around ~110 K, giving
  temperature-dependent (not cooldown/cycling-fatigue-dependent) Rc control. Different
  mechanism from CF-6 (phase-transition material vs. CTE-matched/compliant mechanical
  interface) but same problem space (turn-to-turn Rc engineering) — relevant adjacent
  art, does not by itself anticipate CF-6's cycling/CTE-matching claim, must still be
  in IDS_pool.
- Original language: English (native).
- Query terms: "CTE matched interlayer no-insulation HTS coil conduction cooled
  patent."

**T1-4. KR 10-1665038 B1 — "도전성 물질로 함침된 무절연 초전도 코일 및 그의
제조장치" (Electrically-conductive-material-impregnated no-insulation
superconducting coil and manufacturing apparatus thereof)**
- Assignee: 한국기초과학지원연구원 (Korea Basic Science Institute, KBSI)
- Priority/Filed: 2016-01-11 · Pub/Granted: 2016-10-13
- Jurisdiction: KR · Status: Granted (per Google Patents record; active status not
  independently confirmed — verify against live KIPRIS)
- Original title/abstract (KO, snippet): "무절연 초전도 코일의 권선시 전도성 입자를
  함침하여 턴간 저항을 함침 이전보다 낮게 유지하면서 기계적 강도를 보강..." (per
  fetched summary).
- English translation (machine, via fetch): describes a conductive-particle-loaded
  impregnation (polymer matrix + metallic/carbon conductive particles, optionally
  conductive balls sized ~√3× the wire radius for contact geometry) applied during
  winding to give the NI coil mechanical integrity without insulating the turn-to-turn
  interface, and to spread hot-spot current across turns.
- **Relevance to CF-6:** Addresses mechanical robustness of the NI interface via a
  conductive-composite fill, which is adjacent to (but materially different from) a
  CTE-matched or spring-loaded compliant interlayer; does not address thermal-cycling
  fatigue explicitly nor conduction-cooled-specific duty cycling. Moderate relevance,
  flagged as a hit that could be cited against a broad "conductive compliant interlayer"
  claim.
- Query terms: 무절연 고온초전도 코일 접촉저항 열사이클 특허.

**T1-5. US 4,930,318 — "Cryocooler cold head interface receptacle"** (title inferred
from PDF filename/content; number from USPTO PPUBS mirror)
- Assignee: not confirmed in this pass (general cryocooler-hardware patent, pre-HTS-NI
  era) — verify assignee/priority against live USPTO record.
- Jurisdiction: US · Status: likely expired (old filing; verify)
- **Relevance to CF-6:** Discloses a Belleville-washer-loaded cold-head interface that
  maintains/increases contact pressure at a cryocooler cold-stage joint (interface
  pressure up to ~468 psi per fetched snippet; pressure tunable via bellows diameter/
  spring constant). This is a **general mechanical precedent for "spring-loaded
  contact maintaining pressure across cooldown at a cryocooler cold-head interface"**
  — not HTS-coil-specific, but squarely anticipates the generic mechanical concept
  CF-6's "spring-loaded contact layer" embodiment would need to differentiate from.
  Flag as hurting art for any claim drafted broadly around "spring-loaded thermal/
  electrical contact at a cryocooler interface" without HTS-turn-to-turn specificity.
- Original language: English (native). Confidence: MEDIUM (title/mechanism from
  search snippet + PDF mirror path, not independently re-verified against full PDF
  text in this session — verify before reliance).
- Query terms: "Belleville spring washer HTS joint contact pressure cryocooler cycling
  patent."

**T1-6. US 5,701,742 — "Configured indium gasket for thermal joint in cryocooler"**
- Jurisdiction: US · Status: likely expired (pre-1998 filing; verify)
- **Relevance to CF-6:** Discloses a compliant indium-gasket thermal joint for a
  cryocooler cold-head interface — a compliant/CTE-tolerant interlayer material
  precedent (indium is a classic soft, high-thermal-conductivity gasket material used
  specifically because it accommodates differential thermal contraction). Directly
  anticipates the general *category* of "compliant interlayer material accommodating
  CTE mismatch at a cryocooler-cooled joint," though not for an HTS turn-to-turn
  electrical/thermal dual-function interface specifically.
- Original language: English (native). Confidence: MEDIUM (snippet-derived; verify
  full text).
- Query terms: "HTS joint resistance degradation repeated cooldown cryocooler duty
  cycling MRI magnet."

### TIER 2 — Patent applications (published, not confirmed granted) / lower-confidence family members

**T2-1. EP 4078630 A1 / WO 2021/122522 A1 — "HTS linked partial insulation for HTS
field coils"**
- Assignee: Tokamak Energy Ltd
- Priority: 2019-12-20 · Filed: 2020-12-15 · Pub: 2022-10-26 (EP)
- Jurisdiction: EP/PCT (WIPO PatentScope + Espacenet, via Google Patents mirror) ·
  Status: application (grant status per-jurisdiction not confirmed)
- **Relevance to CF-6:** Discloses HTS-bridge conductive paths within a partially
  insulating interlayer for controlled quench-time current sharing; addresses
  electrical Rc engineering but not explicitly CTE-mismatch or thermal-cycling
  fatigue of the interface. Adjacent art, same problem family as T1-3.
- Note: Tokamak Energy's core application is tokamak fusion, unrelated to this
  project's excluded "stellarator" term — no scope conflict, cited purely as prior
  art in the same technical field.
- Query terms: CTE/interlayer query; assignee watch (Tokamak Energy).

**T2-2. WO 2019/150123 A1 / EP 4012730 A1 / AU 2019214510 A1 — "Partially-insulated
HTS coils"**
- Assignee: Tokamak Energy Ltd
- Priority: 2018-02-01 · Filed: 2019-01-31 · Pub: 2019-08-08
- Jurisdiction: PCT/EP/AU · Status: application family (US sibling T1-3 is granted)
- **Relevance to CF-6:** Same family as T1-3; explicitly notes stainless-steel/
  Hastelloy partially-insulating layers give "improved structural stability" —
  gestures at mechanical/thermal-cycling robustness without a CTE-matching claim.
  Adjacent art.
- Query terms: same as T1-3.

**T2-3. CN 115485868 A — "高温超导体场线圈" (High-Temperature-Superconductor Field
Coil)**
- Assignee: Tokamak Energy Ltd (CN national-phase filing)
- Priority: 2020-05-04 · Pub: 2022-12-16
- Jurisdiction: CN (CNIPA, via Google Patents zh-mirror) · Status: application
  (grant status not confirmed — verify against live CNIPA record)
- Original title/abstract (ZH, snippet, machine-fetched): "通过在线圈绕制后对HTS带材
  轴向边缘进行材料去除（机械加工/放电加工/激光切割或化学方法），缩减带材轴向范围并
  改变绕组间电气特性，暴露缓冲层作为匝间绝缘（'缓冲层绝缘'，BLI），无需额外绝缘材料
  即可实现匝间绝缘/电气特性调节。"
- English translation: describes removing conductive cladding (Cu/Ag) from the tape's
  axial edges after winding to expose the buffer-layer stack, creating a
  "Buffer-Layer-Insulator" (BLI) turn-to-turn interface without adding separate
  insulation material; targeted at tokamak TF coils, aerospace, MRI, accelerators.
- **Relevance to CF-6:** Different mechanism (post-wind material removal vs.
  CTE-matched/compliant interlayer material); same broad field (turn-to-turn
  interface engineering for compact HTS coils) and same assignee-watch family as
  T1-3/T2-1/T2-2. Lower direct relevance, included for candor and CN-jurisdiction
  coverage.
- Query terms: 无绝缘/传导冷却/接触电阻 CN query pack; assignee watch (Tokamak
  Energy).

**T2-4. JP 2017-535948 (national-phase entry; likely JP sibling of a Tokamak Energy
or related partially-insulated-HTS-coil WO family) — "部分絶縁巻線を用いた超電導
コイル及び超電導コイルの製造方法" (Superconducting coil using partially-insulated
winding and manufacturing method thereof)**
- Jurisdiction: JP (J-PlatPat, via astamuse listing) · Status: unconfirmed
  (application vs. granted not verified in this pass)
- Confidence: LOW-MEDIUM — title/number sourced from an astamuse aggregator listing
  only; full abstract and assignee not independently fetched/verified this session.
  **Needs direct J-PlatPat verification before reliance.**
- **Relevance to CF-6:** Same "partially-insulated HTS coil" family as T1-3/T2-1/T2-2
  presumed by title match; if confirmed, extends this family's jurisdictional
  footprint to Japan. Not yet confirmed to add distinct technical content re:
  CTE-matching or thermal cycling.
- Query terms: 無絶縁/接触抵抗/熱サイクル/特許 (JP query pack).

**T2-5. JP 2012-033947 A — "高温超電導コイルおよびその製造方法" (High-Temperature
Superconducting Coil and Manufacturing Method Thereof)**
- Jurisdiction: JP (via Google Patents ja-mirror listing) · Status: unconfirmed
- Confidence: LOW — title only, from a search-result listing; abstract/assignee not
  fetched this session. **Needs direct J-PlatPat/Google Patents full-text verification.**
- **Relevance to CF-6:** Unconfirmed; flagged only because title matches the query
  pack closely enough to warrant a follow-up read before the G-NOVEL gate.
- Query terms: 無絶縁 高温超電導 コイル 接触抵抗 熱サイクル 特許.

**T2-6. KISTI record cn=KOR1020130130009 — "전도 냉각을 위한 초전도 코일 장치"
(Superconducting coil apparatus for conduction cooling)**
- Likely assignee: KERI (Korea Electrotechnology Research Institute) — inferred from
  KISTI listing context, not independently confirmed.
- Jurisdiction: KR (via KISTI/scienceon aggregator) · Status: unconfirmed
- Confidence: LOW — title/registration-number only from an aggregator listing, not
  independently fetched from KIPRIS. **Needs direct KIPRIS verification.**
- **Relevance to CF-6:** Title suggests direct on-point coverage (conduction-cooled
  superconducting coil apparatus) but mechanism/claims not yet confirmed — flagged
  high-priority for a follow-up KIPRIS pull before G-NOVEL.
- Query terms: 무절연 고온초전도 코일 접촉저항 열사이클 특허; KERI assignee watch.

### TIER 3 — Peer-reviewed NPL

**T3-1. B. Parkinson, K. Bouloukakis, H.W. Weijers, J. Olatunji, M. Szmigiel,
M.W. Hunter, T. Froelich, J. Bailey, M. Garwood — "Design and manufacture of an
ultra-compact, 1.5 T class, controlled-contact-resistance, REBCO, brain imaging MRI
magnet," Supercond. Sci. Technol., DOI 10.1088/1361-6668/ad80d5, published
2024-10-15.**
- Affiliations: Robinson Research Institute (Victoria Univ. of Wellington, NZ),
  OpenStar Technologies Ltd, Air Liquide SA, Transpower Ltd, Univ. of Minnesota CMRR.
- **Relevance to CF-6 (HURTS somewhat):** A cryogen-free (dome-form, <400 mm) REBCO
  MRI magnet wound with NI-style coils and a **conductive-epoxy encapsulant** whose
  contact resistance is deliberately controlled/tuned to hit a <30 s emergency
  shutdown target. Directly on-point for "cryogen-free + engineered Rc" but the
  encapsulant approach is a fixed-composition conductive epoxy rather than a
  CTE-matched or spring-loaded compliant interlayer explicitly engineered against
  repeated cryocooler thermal cycling — does not appear to report cycling-life data,
  which is a potential CF-6 differentiator, but must be checked against the full
  paper (paywalled; only abstract-level detail obtained this session).
- Query terms: "HTS joint resistance degradation repeated cooldown cryocooler duty
  cycling MRI magnet."

**T3-2. (title exact match) "Contact resistance between two REBCO tapes: the effects
of cyclic loading and surface coating," Supercond. Sci. Technol., DOI
10.1088/1361-6668/aacd2d.**
- Authors/affiliation/year not independently confirmed this session (publisher
  abstract page not fetchable; title/DOI recovered via WebSearch listing only).
  **Needs direct verification.**
- **Relevance to CF-6 (HURTS):** Title directly states the CF-6 mechanism —
  cyclic mechanical loading degrading Rc between REBCO tapes, plus a surface-coating
  (interlayer material) variable — essentially the electrical-contact half of CF-6's
  claim space, in NPL rather than patent form. High-priority for full-text pull
  before G-NOVEL/G-CLAIM.
- Query terms: "arxiv no-insulation coil contact resistance repeated thermal cycling
  degradation mechanism."

**T3-3. (companion/earlier) "Contact resistance between two REBCO tapes under load
and load cycles," Supercond. Sci. Technol., DOI 10.1088/1361-6668/aa5b05.**
- Same note on unconfirmed authors/year — publisher page not fetchable this session.
- **Relevance to CF-6 (HURTS):** Companion paper to T3-2; same load-cycling-degrades-Rc
  mechanism, earlier in the same journal. Reinforces that Rc-vs-cyclic-mechanical-
  load is an already-published NPL topic, narrowing CF-6's novelty headroom on the
  "electrical" half specifically.
- Query terms: same as T3-2.

**T3-4. "A Study on the Electrical Contact Resistance and Thermal Conductivity of
Soldered-Metal Insulation Coil With Conduction Cooling," IEEE Trans. Appl.
Supercond., IEEE Xplore doc. 9769961.**
- Authors/affiliation not independently confirmed (IEEE Xplore abstract page blocked;
  title/topic recovered via WebSearch snippet). Likely Korean group (KERI/Korea Univ
  lineage) given "soldered metal insulation (SMI)" naming convention — unconfirmed.
- **Relevance to CF-6 (directly on-point, HURTS):** Proposes a "soldered metal
  insulation" (SMI) winding to give **controllable** Rc AND thermal conductivity,
  tested in a **conduction-cooling** apparatus below 77 K. This is essentially
  CF-6's dual-function (Rc + thermal conductance) objective, already published for
  a solder-based interlayer under conduction cooling — very close art. Full-text pull
  is high priority before G-NOVEL; thermal-cycling life data not confirmed present
  or absent from abstract-level detail obtained.
- Query terms: "Electrical Contact Resistance and Thermal Conductivity of Soldered-
  Metal Insulation Coil With Conduction Cooling."

**T3-5. "Study of contact resistivity of a no-insulation superconducting coil,"
Supercond. Sci. Technol., DOI 10.1088/1361-6668/abd14d, published 2021-01-29.**
- **Relevance to CF-6:** Distributed circuit model (local contact resistivity +
  inductances + HTS resistance vs. current/field/temperature) for measuring NI-coil
  Rc; foundational modeling reference, not itself a thermal-cycling or CTE study.
  Moderate relevance (methodology reference for CF-6's eventual W2 sim validation,
  not a direct novelty threat).
- Query terms: "Study of contact resistivity of a no-insulation superconducting coil."

**T3-6. "Feasibility Study of the Impregnation of a No-Insulation HTS Coil Using an
Electrically Conductive Epoxy," Cryogenics (ScienceDirect), MIT/Iwasa-Hahn-lineage
group (exact author list not independently re-confirmed this session — historically
attributed to the MIT Francis Bitter Magnet Lab NI-coil group per assignee-watch
prior knowledge).**
- **Relevance to CF-6 (HURTS — directly on point):** Reports that full-surface epoxy
  impregnation across turn-to-turn contacts caused **significant critical-current
  degradation from delamination driven by thermal-contraction mismatch between the
  epoxy composite and the HTS tape** — i.e. this is a published, named instance of
  exactly the CTE-mismatch failure mode CF-6 is trying to solve, and it also
  discloses a **partial-depth impregnation** design-around (epoxy penetrates only
  part-way between turns) already invented to reduce the mismatch-driven
  degradation. This narrows CF-6's novelty headroom substantially on the "solve
  CTE mismatch at the NI interface" framing and should be treated as a leading
  candidate blocking/limiting reference at G-NOVEL.
- Query terms: "no-insulation HTS coil contact resistance thermal cycling degradation
  patent" (NPL surfaced alongside patent query).

**T3-7. "Study on reducing the charge delay of the no-insulation HTS coil after
solder impregnation," Cryogenics (ScienceDirect), DOI
10.1016/j.cryogenics.2018.03.xxx (exact suffix not confirmed).**
- **Relevance to CF-6:** Solder impregnation as an alternative to epoxy for the NI
  interface — relevant to the "solder joint" embodiment named in CF-6's related
  concepts, addresses charge-delay (Rc) more than thermal-cycling fatigue per the
  available snippet. Moderate relevance.
- Query terms: "no-insulation HTS coil contact resistance thermal cycling degradation
  patent."

**T3-8. "Electromagnetic behaviour and thermal stability of a conduction-cooled,
no-insulated 2G-HTS coil at intermediate temperatures," Cryogenics, DOI
10.1016/j.cryogenics.2020.103096 (ScienceDirect, also mirrored on ResearchGate as
publication 340118425).**
- **Relevance to CF-6:** Directly studies a conduction-cooled NI coil's electromagnetic/
  thermal behavior at intermediate temperatures (i.e., the exact CF-6 operating
  regime); relevance to the "no bath, limited cooling" framing is high, though the
  focus (per title) is behavior/stability characterization rather than an
  engineered CTE-matched/spring-loaded interface or explicit cycling-life data.
- Query terms: "no-insulation HTS coil contact resistance thermal cycling degradation
  patent."

**T3-9. Korea Science (koreascience.kr JAKO201810263411647) — "Contact resistance
characteristics of 2G HTS coils with metal insulation," Progress in Superconductivity
and Cryogenics.**
- **Relevance to CF-6:** Reports measured contact-surface resistances (~248.8–724.8
  µΩ·cm²) across different metal-tape metal-insulation (MI) constructions — relevant
  material-selection data for the electrical half of CF-6, no explicit thermal-cycling
  life study per available snippet.
- Query terms: "Sungho Kim Korea University no-insulation coil thermal cycling contact
  resistance IEEE TAS"; KERI/Korea Univ assignee watch.

**T3-10. Korea Science (koreascience.kr JAKO202108062285171) — "Analysis on
electrical and thermal characteristics of MI-SS racetrack coil under conduction
cooling and external magnetic field," Progress in Superconductivity and Cryogenics.**
- **Relevance to CF-6:** Directly combines "MI-SS" (metal-insulation, stainless-steel)
  interlayer + conduction cooling + external-field characterization — on-point for
  CF-6's dual electrical/thermal framing under conduction cooling, no explicit
  cycling-life claim per available snippet.
- Query terms: same as T3-9.

**T3-11. "Reliability modeling of the fatigue life of lead-free solder joints at
different testing temperatures and load levels using the Arrhenius model," Scientific
Reports, 2023 (nature.com, DOI 10.1038/s41598-023-29636-3).**
- **Relevance to CF-6:** General (non-HTS, non-cryogenic — electronics-packaging
  domain) solder-joint thermal-fatigue reliability model; relevant only as a
  cross-domain mechanism analog for "solder joint under thermal fatigue" named in
  CF-6's related concepts. Does not address cryogenic temperatures or HTS
  specifically — low direct relevance, included for candor since it was a top hit
  on the solder-fatigue query branch.
- Query terms: "HTS solder joint thermal fatigue cryocooler thermal cycling
  degradation contact resistance."

**T3-12. "Quantification of relative displacements of electrical contacts subjected
to temperature cycles," Wear (ScienceDirect), DOI 10.1016/j.wear.2026.xxxxx
(published ~3 weeks prior to this search per snippet, i.e. ~June 2026).**
- **Relevance to CF-6:** Cross-domain (general electrical-connector, non-cryogenic)
  mechanism paper explicitly modeling **fretting-driven contact degradation caused by
  differential thermal expansion / micro-displacement under temperature cycling** —
  directly analogous failure mechanism to what CF-6 posits for the NI interface
  (differential CTE between HTS tape / interlayer / cold-head mount driving
  progressive contact degradation), though not in an HTS or cryogenic context. Useful
  as a mechanism-level reference; not a direct patent-scope threat but relevant to
  physics plausibility (feeds G-PHYS) and should stay in IDS_pool.
- Query terms: "Quantification of relative displacements of electrical contacts
  subjected to temperature cycles."

### TIER 4 — Other (technical reports, preprints, press mentions, unverified aggregator listings)

**T4-1. NASA NTRS 20180005427 — "Design, Fabrication, and Critical Current Testing of
No-Insulation [...]" (title truncated in source listing).**
- Source type: NASA technical report (NTRS). Relevance: general NI-coil fabrication/
  testing reference; no explicit CTE/thermal-cycling framing seen in snippet.
- Query terms: "arxiv no-insulation coil contact resistance repeated thermal cycling
  degradation mechanism."

**T4-2. arXiv 2604.15587 — "Control of turn-to-turn contact resistivity in
resistively insulated REBCO coils."**
- Source type: preprint. Relevance: Rc-engineering methods for resistively-insulated
  REBCO coils; adjacent to CF-6's electrical half, cycling/CTE framing not confirmed
  from title alone.
- Query terms: "Electrical Contact Resistance and Thermal Conductivity of
  Soldered-Metal Insulation Coil."

**T4-3. arXiv 2605.28574 — "Surface Contact Approximation for Magneto-Thermal Finite
Element Analysis of No-Insulation HTS Coils."**
- Source type: preprint. Relevance: simulation-methodology reference (useful for
  CF-6's eventual W2 sim, not itself a novelty threat).
- Query terms: multiple (recurring top hit across NI-coil queries).

**T4-4. Press/news mention — 星环聚能 (Xingsheng Juneng), a Chinese fusion startup,
2024 progress claim (via zhihu.com / general Chinese-search results) that it
"mastered no-insulation coil design/manufacturing and validated multiple HTS magnets
through repeated cold/hot cycling with excellent performance stability."**
- Source type: press/industry-news mention, NOT a verified patent or NPL citation.
- Confidence: LOW. **No patent number identified — do not treat as a citable
  reference until/unless a specific CN/PCT filing by this entity is located via a
  direct CNIPA search.** Flagged only as an assignee/competitor-watch lead for a
  follow-up harvest pass (this entity was not on the original assignee watch list
  and should be added).
- Query terms: 传导冷却 无绝缘 高温超导磁体 接触电阻 专利 中国科学院电工研究所.

**T4-5. IEE-CAS (中国科学院电工研究所) HPLPB journal article — "用于高功率微波器件
的传导冷高温磁体研制" (Development of a conduction-cooled high-temperature magnet for
high-power microwave devices), authors 徐策, 刘辉, 刘建华, 戴银明, 陈顺中, 程军胜,
王秋良, 霍少飞, 史彦超, 黄慧杰.**
- Source type: Chinese peer-reviewed journal article (High Power Laser and Particle
  Beams). Relevance: conduction-cooled HTS magnet development by an assignee-watch
  institution (IEE-CAS); general conduction-cooling magnet R&D, no explicit
  CTE-matched/spring-loaded NI-interface content identified from available
  title/context. Tier 4 pending full-text review (Chinese-language PDF not fully
  fetched this session).
- Query terms: 传导冷却 无绝缘 高温超导磁体 接触电阻 专利 中国科学院电工研究所.

---

## 4. Summary

- **Total hits recorded: 29** (6 Tier 1, 6 Tier 2, 12 Tier 3, 5 Tier 4 — matches
  `sources.json`; T2-4/T2-5/T2-6 and T4-4 are low-confidence and flagged for
  mandatory live-database re-verification before any filing-relevant novelty
  reliance).
- **Most notable close/hurting art:** US 11,282,624 B2 (T1-1, FSU/NHMFL) already
  claims engineered-interlayer Rc control and reports both thermal- and mechanical-
  cycling Rc degradation data; the MIT/Iwasa-Hahn-lineage conductive-epoxy
  impregnation NPL (T3-6) already names differential-thermal-contraction/CTE-mismatch
  delamination as a failure mode AND proposes a partial-depth-impregnation
  design-around; the SMI conduction-cooling NPL (T3-4) and the REBCO cyclic-loading
  Rc papers (T3-2/T3-3) collectively cover much of CF-6's "engineer Rc + thermal
  conductance jointly, under cycling" territory in NPL form, even where patent
  claims have not yet been found to cover it.
- **Access gap (repeat, for G-NOVEL awareness):** no live query-form access to CNIPA,
  J-PlatPat, KIPRIS, or Espacenet in this session; all non-US/EP results are via
  Google-indexed mirrors/aggregators. A dedicated live-DB re-pass is recommended
  before CF-6 reaches G-NOVEL, specifically to verify T2-3 through T2-6 and to close
  the CN utility-model / KR-only-publication blind spot flagged above.
