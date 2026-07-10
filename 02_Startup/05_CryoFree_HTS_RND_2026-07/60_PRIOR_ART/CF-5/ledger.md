# CF-5 Prior-Art Ledger — Rotating-frame heat extraction for NI motor coils

**Candidate:** CF-5 — thermal architecture removing heat from a spinning conduction-cooled
NI HTS winding (rotor-mounted) within a fixed cooling-power budget; anchor exemplar
Hinetics CRUISE-class aviation motor field coils. Core technical question: how heat crosses
the rotating→stationary interface when there is no cryogen bath and the cryocooler cold
head is typically stationary while the winding spins.

**Wave:** W1 prior-art harvest. **Model logged:** `models=harvest:sonnet`. **Date:** 2026-07-10.
**Scope note:** This is a "very high" CF-relevance candidate per the mission seed table —
harvest was run deep, not shallow. Do NOT read this ledger as a novelty verdict; that is
G-NOVEL's job (fable-5). Every hit below enters the CF-5 `IDS_pool`, including hits that
directly anticipate or narrow the candidate.

---

## Query pack used

**English:** rotating cryocooler, rotating-frame heat extraction, superconducting rotor
cooling system, cryogenic rotary joint, cryo-rotary joint, thermal strap rotary interface,
conduction-cooled rotor, on-board cryocooler, spoke-supported superconducting rotor,
no-insulation HTS rotor field coil, HTS synchronous motor rotor cooling, thermosiphon rotor.

**Chinese (简体中文):** 超导 转子 传导冷却 (conduction-cooled superconducting rotor);
制冷机 冷头 旋转 (refrigerator cold head rotating); 无绝缘 超导线圈 (no-insulation HTS coil);
旋转密封 低温 (cryogenic rotary seal); 磁流体密封 (magnetic fluid seal).

**Japanese (日本語):** 超電導 回転子 伝導冷却 (conduction-cooled superconducting rotor);
冷凍機 コールドヘッド 回転 (refrigerator cold head rotating); 無絶縁 超電導コイル
(no-insulation HTS coil); 極低温 回転継手 (cryogenic rotary joint).

**Korean (한국어):** 초전도 회전자 전도냉각 (conduction-cooled superconducting rotor);
극저온냉동기 콜드헤드 회전 (cryocooler cold head rotating); 무절연 초전도 코일
(no-insulation HTS coil); 자성유체 실링 (magnetic fluid seal); 회전기 극저온 조인트
(rotating machine cryogenic joint).

**CPC/IPC walk:** H02K55/00 / H02K55/04 (superconducting rotating machines), H01F6/06,
H01F6/04, F25B9/14 (cryocoolers), F28F27/00 (rotating heat exchange), F16L39/04 (rotary
fluid couplings — cryogenic rotary joints frequently classed here too), G01R33 (checked,
no additional rotating-frame hits beyond diagnostic-adjacent noise already excluded by
prong-a scope).

**Assignee watches hit:** Hinetics, American Superconductor Corp (AMSC)/Reliance Electric,
Sumitomo Electric Industries, Sumitomo Heavy Industries, HD Hyundai Heavy Industries
(formerly Hyundai Heavy Industries), Dongfang Electric, Tokyo University of Marine
Science and Technology / Kitano Seiki. **Assignee watches searched but NOT found with
rotating-frame-specific hits in this pass:** GE (aviation-motor-specific filings not
separately located from AMSC/Reliance family — GE's HTS generator patents in this space
often trace through licensed AMSC IP; flagged as a gap, see below), Toshiba, Mitsubishi,
Fujikura, Furukawa, SuperPower, Shanghai Superconductor, IEE-CAS, Tokamak Energy, CFS,
Bruker, Siemens Healthineers, Korea Univ/KERI, MIT. KAIST hit via NPL only (no patent
found in this pass). Rolls-Royce/magniX/Safran: no rotor-cryocooler-specific patents
located; only general aviation-electric-motor context (NPL survey hit, see NPL section).

**Known gaps (logged honestly, not retried a third time within this wave):**
- No direct authenticated queries were run against native CNIPA, J-PlatPat, KIPRIS, or
  Espacenet/WIPO PatentScope search consoles (no live session credentials in this
  environment). All non-English-jurisdiction hits below were surfaced via Google Patents'
  aggregated index and Google web search with native-language query strings, then
  cross-checked on the Google Patents record page for that publication number. This is a
  reasonable proxy (Google Patents mirrors CNIPA/JPO/KIPO/EPO full text) but is NOT
  equivalent to a native-database professional search and should be re-run by a search
  professional before any filing-relevant reliance.
- US Patent 12,531,457 and US Patent 12,494,701 (Google/USPTO PDF full-text) returned
  OCR/binary-image content that WebFetch could not parse into text; bibliographic data
  below for these two is partial (numbers, likely subject matter, and — for '457 —
  strong contextual inference of assignee from claim language matching Hinetics'
  spoke-strap architecture). Flagged for manual re-pull.
- Two IOPscience article pages (Cooling method for the rotor of a superconducting motor;
  Additive manufacturing materials for cryo-electric aircraft motors) returned HTTP 403
  on WebFetch (paywall/bot-block). Retried once per protocol; still blocked. Logged from
  search-snippet metadata only — abstract not independently verified past the snippet.
- GE-assignee-specific rotor-cryocooler filings were not independently isolated from the
  AMSC/Reliance Electric family in this pass; worth a dedicated re-run keyed to GE Aviation
  / GE Global Research superconducting-generator dockets before relying on "no GE hit."

---

## TIER 1 — Granted / near-scope patents (highest weight for G-NOVEL)

### T1-01. US 2022/0302816 A1 → granted **US 12,506,395 B2**
- **Assignee:** Hinetics LLC
- **Priority:** 2021-03-16 · Filed 2021-10-11 · Pub 2022-09-22 · Granted 2025-12-23
- **Jurisdiction/status:** US, active (granted)
- **Relevance (one sentence):** Discloses the anchor exemplar's own architecture — a
  cryocooler cold end extending through a hollow driveshaft into the rotor, with
  thermally conductive straps extending radially at equal angles from the cold end to
  axially-extending thermal leads on the rotor shell, i.e. essentially CF-5's proposed
  mechanism disclosed by the anchor company itself.
- **Title/abstract:** "Superconducting Motor with Spoke-Supported Rotor Windings" — a
  wound-field rotor suspended from a driveshaft by low-thermal-conductivity tensile
  spokes (Kevlar-class), cooled by a rotating cryocooler via radial conductive straps.
- **IDS_pool:** YES — this is the single most damaging reference for CF-5 novelty; it is
  Hinetics' own filing covering the exact rotating-frame conduction path CF-5 targets.

### T1-02. US Patent 12,531,457 (pub. 2026)
- **Assignee:** Unconfirmed by direct text extraction (PDF was image-only); claim
  language ("thermally conductive straps extend radially from a cold end to a rotor
  shell... flexible to accommodate thermal contractions during cool down") closely
  tracks the Hinetics '395 family — high-confidence same-assignee continuation, NOT
  independently verified.
- **Priority/pub:** Pub. date surfaced as 2026-07-10 in the fetch header (likely a grant
  date artifact of the PDF builder, not a reliable priority date) — **flagged as unreliable,
  needs manual confirmation.**
- **Jurisdiction/status:** US, granted (per title "Superconducting motor with reduced
  coil stress").
- **Relevance:** Adds a mechanical-compliance limitation (flexible straps
  accommodating cooldown thermal contraction) to the same rotating radial-strap heat
  path as T1-01 — narrows CF-5's room to claim strap flexibility/compliance as a
  differentiator.
- **IDS_pool:** YES, with the above confidence caveat noted.

### T1-03. CN 102016461 B
- **Assignee:** American Superconductor Corp (AMSC)
- **Priority:** 2008-03-11 · Pub 2012-11-14
- **Jurisdiction/status:** CN, expired (fee-related)
- **Title (EN, as translated):** "Cooling system in a rotating reference frame"
- **Relevance:** Mounts the cryocooler cold head itself IN the rotating frame (co-rotating
  chiller) specifically to reduce the thermal gradient between chiller and heat load and
  avoid cryogenic rotary joints — a materially different mechanism from CF-5's
  stationary-cold-head-plus-rotating-interface framing, but squarely on-topic for any
  "rotating-frame heat extraction" claim scope and must be distinguished or excluded.
- **IDS_pool:** YES.

### T1-04. DE 199 38 986 B4 (family incl. EP 1206667 B1, US/JP/AT priority claims)
- **Assignee:** Not independently confirmed (German entity, filed pre-Siemens-spinoff
  era — plausible Siemens or Alstom-lineage; not verified, flag as gap).
- **Priority:** Filed 1999-08-17 · Granted 2008-02-14
- **Jurisdiction/status:** DE (+ EP/US/JP family), expired (fee-related)
- **Relevance:** Cold head rotates INSIDE the rotor; compressor stays stationary; a
  ferrofluid gas coupling is the SOLE mechanical connection across the rotating
  interface — an early (1999 priority) "minimize the rotating-to-stationary interface"
  architecture directly on-topic for CF-5's core problem statement.
- **IDS_pool:** YES.

### T1-05. US 2003/0107275 A1 (family: WO 2000/013296 A9, EP 1108281 A1, **US 6,812,601 B2**)
- **Assignee:** American Superconductor Corp / Reliance Electric Co
- **Priority:** 1998-08-26 · Pub 2003-06-12 (US 6,812,601 B2 is the granted member of
  this family)
- **Jurisdiction/status:** US/EP/WO, granted, expired (lifetime, ~2019)
- **Relevance:** Keeps the cryocooler stationary and bridges to the rotating
  superconductor device via a closed circulation system with interleaved stationary/
  rotating copper fins across a small gap (convective/conductive gas-gap heat exchange,
  no fluid seal crossing the interface) — a direct structural precedent for "extract
  heat across the rotating boundary without a fluid rotary seal," which is close to the
  design space CF-5 would need to occupy to avoid T1-01/T1-03.
- **IDS_pool:** YES — high relevance, near-scope.

### T1-06. US 6,347,522 B1
- **Assignee:** American Superconductor Corp
- **Priority:** 2000-01-11 · Pub 2002-02-19
- **Jurisdiction/status:** US, granted, expired (lifetime)
- **Relevance:** Uses high-speed fans (10,000–30,000 rpm) inside the rotating frame to
  circulate helium without phase change, exploiting centrifugal density-driven
  circulation once spun up, coupled to stationary cryocoolers via ferrofluidic rotary
  seals — an alternate "engineered convective loop across the interface" mechanism
  CF-5 must be distinguished from if claiming any forced-circulation variant.
- **IDS_pool:** YES.

### T1-07. US 6,597,082 B1
- **Assignee:** American Superconductor Corp
- **Priority:** 2000-08-04 · Pub 2003-07-22
- **Jurisdiction/status:** US, granted, expired (2020)
- **Relevance:** Explicitly teaches AWAY from rotating the cryocooler ("undesirable
  high gravity heat transfer" if cooler rotates), keeping cryocooler stationary while a
  closed cryogenic loop inside the rotor assembly rotates, connected via rotary
  coupling — directly relevant prior-art reasoning CF-5's disclosure will need to engage
  with (either agree cold head should stay stationary, or claim a design-around that
  overcomes the gravity-heat-transfer objection for a rotating cold head, cf. T1-03).
- **IDS_pool:** YES.

### T1-08. EP 3104100 B1
- **Assignee:** Sumitomo Heavy Industries, Ltd.
- **Priority:** 2015-02-27 · Filed 2016-02-23 · Pub 2019-07-24
- **Jurisdiction/status:** EP, active (est. expiry 2036-02-23)
- **Relevance:** "Cryocooler and rotary joint" — compressor stationary, expander on the
  rotating portion, with a working-gas seal dividing the rotor/stator clearance into
  staged intermediate-pressure zones to reduce leakage; explicitly applied to a
  superconducting wind-power generator rotor. Directly on-topic rotary-joint-across-
  cryogenic-interface prior art from a major HTS-adjacent assignee not previously on the
  watch list's motor work (Sumitomo Heavy Industries, distinct from Sumitomo Electric).
- **IDS_pool:** YES.

### T1-09. US 2012/0133126 A1 ("Cryo-rotary joint")
- **Assignee:** Tokyo University of Marine Science and Technology (NUC) / Kitano Seiki
  Co., Ltd.
- **Priority:** 2009-06-02 · Pub 2012-05-31
- **Jurisdiction/status:** US, granted (active per initial fetch; verify current status)
- **Relevance:** Compact cryo-rotary joint using a magnetic-fluid seal positioned far
  from the main refrigerant body to prevent seal freezing while minimizing parasitic
  heat leak into the refrigerant path — a close structural precedent for any CF-5
  embodiment using a refrigerant-transfer (rather than pure solid-conduction strap)
  rotating interface.
- **IDS_pool:** YES.

### T1-10. US 7,667,358 B2
- **Assignee:** Sumitomo Electric Industries, Ltd.
- **Priority:** 2004-12-24 · Pub 2010-02-23 (expires 2026-10-05)
- **Jurisdiction/status:** US, expired (fee-related, near end of term)
- **Relevance:** Cools the rotor by cutting LN2-carrying grooves into the OUTER surface
  of the rotating shaft (avoiding center-drilling), placing the coolant path closer to
  the HTS coil — a cryogen-based (not cryocooler-conduction-based) rotor thermal-path
  routing precedent; distinguishable from CF-5 on cryogen-free grounds but relevant as
  "alternative heat-path geometry across the same rotor" background art, and worth
  noting since it is a bath/LN2 architecture, not conduction-cooled, so it does NOT
  anticipate the cryogen-free limitation but DOES anticipate "route the thermal path
  through shaft-mounted structure."
- **IDS_pool:** YES.

### T1-11. CN 102840708 B — **CLOSEST CHINESE ART FOUND**
- **Assignee:** Dongfang Electric Co., Ltd.
- **Priority:** 2012-09-29 · Granted 2016-04-06 (est. expiry 2032)
- **Jurisdiction/status:** CN, active
- **Title (EN translation):** "A conduction-cooling-based superconducting motor
  refrigeration system" (原文: 一种基于传导冷却的超导电机的制冷系统)
- **Original abstract (as machine-summarized):** 采用氦气压缩机产生高压氦气，经旋转密封装置
  传输至旋转的制冷机冷头；一级冷头冷却辐射屏（60-80K），二级冷头通过铜/铝导热带将冷量传导至超导
  磁体，取消液氦依赖，降低对密封装置的要求，适用于低转速（<20rpm）海上风电场景。
- **EN translation:** A helium compressor generates high-pressure helium gas at room
  temperature, delivered via a rotary seal to a ROTATING two-stage refrigerator cold
  head; the first stage cools a radiation shield (60–80 K), the second stage conducts
  cooling to the superconducting magnet frame via copper/aluminum thermal-conduction
  straps, eliminating liquid-helium dependence and reducing sealing requirements —
  targeted at low-rotation-speed (<20 rpm) offshore wind applications.
- **Relevance (one sentence):** This is architecturally almost identical to a
  "rotating cold head + conductive straps to the coil" embodiment of CF-5, differing
  mainly in application (wind generator, low RPM) vs. CF-5's aviation motor / high-RPM
  target and NI-specific winding — a strong anticipation/narrowing reference that must
  be squarely addressed in G-NOVEL and any claim drafted around rotating-cold-head
  embodiments.
- **IDS_pool:** YES — flagged HIGH PRIORITY, hurts the candidate.

### T1-12. WO 2013/133487 A1 — **CLOSEST KOREAN-FILED ART FOUND**
- **Assignee:** Hyundai Heavy Industries Co., Ltd. (now HD Hyundai Heavy Industries)
- **Priority:** 2012-03-07 · Filed 2012-07-04 · Pub 2013-09-12
- **Jurisdiction/status:** WO (PCT, KR-origin), status "ceased" (national-phase
  prosecution outcome not separately confirmed — flagged for follow-up)
- **Title (Korean, original):** 전도 냉각 방식 초전도 회전기
- **EN translation:** "Conduction-cooled superconducting rotating machine"
- **Original abstract (as machine-summarized):** 내부에 극저온 냉동기(3단 GM형)를 장착하여
  외부 냉매 유동라인을 간소화하고, 냉동기와 초전도 선재 사이 거리를 단축하여 전도냉각을 구현;
  회전축에 원주방향 홀을 두고 진공챔버 내 구리 열전달 요소로 초전도선을 냉각.
- **EN translation:** Mounting a 3-stage Gifford-McMahon-type cryogenic freezer INSIDE
  the rotor simplifies external refrigerant flow lines and shortens the distance between
  the freezer and the superconducting wire to achieve conduction cooling; circumferential
  holes in the rotating shaft and copper heat-transfer elements inside a vacuum chamber
  cool the superconducting wire via conduction.
- **Relevance (one sentence):** Near-identical core mechanism to CF-5 (cryocooler
  mounted in the rotating frame, conduction path shortened via copper elements to the
  SC winding) from a major heavy-industry HTS-adjacent assignee, filed a decade before
  Hinetics' public architecture — a strong prior-art risk for any "rotating cryocooler
  in the frame" claim scope, though it does not address NI-specific winding thermal/Rc
  co-design.
- **IDS_pool:** YES — flagged HIGH PRIORITY, hurts the candidate.

### T1-13. WO 2013/111934 A1
- **Assignee:** Likely Hyundai Heavy Industries (Korean-origin, companion filing to
  T1-12; assignee not independently re-confirmed in this pass — flag).
- **Priority:** Not independently confirmed this pass (companion-family estimate ~2012).
- **Jurisdiction/status:** WO (PCT, KR-origin)
- **Title (Korean, original):** 초전도 회전기용 다단 구조를 갖는 자성유체 실링 장치
- **EN translation:** "Multi-stage magnetic-fluid sealing device for a superconducting
  rotating machine"
- **Relevance:** A multi-stage ferrofluidic seal for the hollow rotating shaft housing
  the cold rod — sealing/rotary-joint detail art adjacent to T1-12's core mechanism;
  relevant to any CF-5 embodiment needing a vacuum-maintaining rotary seal around a
  rotating cold conduit.
- **IDS_pool:** YES.

### T1-14. US 6,412,289 — "Synchronous machine having cryogenic gas transfer coupling to rotor with super-conducting coils"
- **Assignee:** Not independently confirmed this pass (GE-class subject matter based on
  title/claim framing; not verified — flag).
- **Jurisdiction/status:** US, granted (older-generation cryogenic gas transfer coupling
  patent).
- **Relevance:** Cryogenic gas transfer joint delivering cooled gas from a stationary
  cryorefrigerator, through a stationary bayonet, into a tube rotating with the rotor —
  another stationary-cryocooler / rotating-gas-path architecture bracketing CF-5's
  design space from the "transfer cold gas across the interface" side (as opposed to
  CF-5's likely solid-conduction-strap framing).
- **IDS_pool:** YES.

### T1-15. US 6,351,045 — "Cryogenic rotary transfer coupling for superconducting electromechanical machine"
- **Assignee:** Not independently confirmed this pass — flag.
- **Jurisdiction/status:** US, granted.
- **Relevance:** A dedicated cryogenic rotary transfer coupling patent — core rotary-
  interface hardware directly in CF-5's problem space; needs review for claim overlap
  with any CF-5 rotary-joint embodiment.
- **IDS_pool:** YES.

### T1-16. US 5,548,168 — "Superconducting rotor for an electrical machine"
- **Assignee:** Not independently confirmed this pass (older GE-class filing based on
  title framing — flag).
- **Jurisdiction/status:** US, granted, expired (lifetime).
- **Relevance:** Early-generation superconducting rotor general architecture; background
  art establishing the baseline rotor-cooling problem CF-5 addresses. Lower marginal
  relevance than T1-01–T1-15 but retained for completeness/duty of candor.
- **IDS_pool:** YES.

### T1-17. US 5,482,919 — "Superconducting rotor"
- **Assignee:** Not independently confirmed this pass — flag.
- **Jurisdiction/status:** US, granted, expired (lifetime).
- **Relevance:** Same class as T1-16 — general superconducting rotor background art
  bracketing the field pre-cryocooler-conduction era.
- **IDS_pool:** YES.

---

## TIER 2 — Applications / lower-confidence status

### T2-01. US 2020-class family: US 6,725,683 / US 2002/0170298 A1 — "Cryogenic cooling system for rotor having a high temperature super-conducting field winding"
- **Assignee:** Not independently confirmed this pass (evaporative recondensing-
  cryorefrigerator architecture, GE/AMSC-class subject matter based on title — flag).
- **Priority:** ~2001 (application-family; not independently re-verified this pass).
- **Jurisdiction/status:** US, granted (US 6,725,683 B2, issued 2004-04-27), expired.
- **Relevance:** Evaporative cryogen cooling with a recondensing cryorefrigerator in the
  vapor space above an elevated storage tank — a cryogen-bath-plus-cryocooler hybrid,
  materially different from CF-5's cryogen-free conduction target, but bracketing
  background art for "how rotor heat has historically reached a cryocooler."
- **IDS_pool:** YES (background/bracketing only).

### T2-02. US 7,012,347 B2 — "Superconducting rotor with cooling system"
- **Assignee:** Not independently confirmed this pass — flag.
- **Jurisdiction/status:** US, granted.
- **Relevance:** Addresses complexity of multi-cylindrical cryogenic flow-channel
  structures and thermal insulation inside the rotor — background/complexity-reduction
  precedent adjacent to CF-5's simplification goals.
- **IDS_pool:** YES.

### T2-03. US 2026-pub "High-temperature superconducting rotating machine equipped with fixed-type rotor cryostat for cryogen and stator cooling structure using of vaporized cryogen from rotor" (US 12,494,701, exact number unconfirmed — title captured from search snippet; PDF was image-only and could not be parsed)
- **Assignee:** Unconfirmed — flag for manual re-pull.
- **Jurisdiction/status:** US, recently published (2026) — status not independently
  confirmed.
- **Relevance:** Title alone signals a fixed (non-rotating) rotor cryostat design that
  uses vaporized cryogen boiled off the rotor to additionally cool the stator — an
  adjacent but structurally distinct architecture (still cryogen-bath-based, not pure
  conduction) worth a follow-up pull given its recency and potential overlap with any
  CF-5 claim touching stator-side heat reuse.
- **IDS_pool:** YES, flagged low-confidence / needs manual re-pull before reliance.

### T2-04. KR 10-1665038 B1 — "도전성 물질로 함침된 무절연 초전도 코일 및 그의 제조장치"
- **Assignee:** Not independently confirmed this pass — flag.
- **Jurisdiction/status:** KR, granted.
- **EN translation:** "No-insulation superconducting coil impregnated with conductive
  material, and manufacturing apparatus therefor."
- **Relevance:** On-topic for NI coil thermal/electrical interface engineering (shared
  vocabulary with CF-1/CF-6) but NOT rotating-frame-specific; retained here because it
  surfaced on the CF-5 Korean query pack and touches the NI-winding half of CF-5's
  compound claim scope (NI + rotating). Lower direct relevance to the rotating-frame
  mechanism specifically.
- **IDS_pool:** YES (lower priority).

---

## TIER 3 — Peer-reviewed NPL

### T3-01. "A Spoke-Supported Superconducting Rotor With Rotating Cryocooler," *IEEE Transactions on Magnetics*, vol. 58, no. 8, 2022 (IEEE Xplore doc. 9709844)
- **Authors/venue:** University of Illinois (Haran-group-adjacent, matches Hinetics'
  academic origin) — IEEE Trans. Magnetics.
- **Relevance:** Academic parent publication of the Hinetics T1-01/T1-02 patent family —
  describes the spoke-suspension + rotating-cryocooler mechanism in peer-reviewed form,
  useful both as an enablement reference and as a potential prior public-disclosure date
  check against the Hinetics patent priority date (2021-03-16) for any China-grace-period
  analysis.
- **IDS_pool:** YES.

### T3-02. "Rotating Cryocooler Performance for Superconducting Rotor," IEEE Conference Publication, 2023 (IEEE Xplore doc. 10197681)
- **Relevance:** Follow-on experimental characterization of rotating-cryocooler
  performance on a superconducting rotor test article — directly on-topic empirical data
  for the same architecture family as T3-01/T1-01.
- **IDS_pool:** YES.

### T3-03. "Design and Analysis of Rotor Structure Support for Spoke Type Superconducting Motor," IEEE Xplore doc. 11329170
- **Relevance:** Further structural follow-on in the same spoke-supported rotor family;
  background/enablement art.
- **IDS_pool:** YES.

### T3-04. "High Temperature Superconducting Motor Cooled by On-Board Cryocooler," IEEE Xplore doc. 5677566
- **Relevance:** Earlier-generation on-board (rotating) cryocooler HTS motor
  demonstration — establishes that on-board rotating cryocoolers for HTS motors are
  long-known (predates Hinetics by well over a decade), background art narrowing any
  CF-5 claim to "a cryocooler physically mounted on/in the rotor."
- **IDS_pool:** YES.

### T3-05. "Rotating Cryocooler for Superconducting Motor," KAIST, ~2006 (PURE KAIST record; ResearchGate 234986798)
- **Relevance:** KAIST work selecting a Stirling-type coaxial pulse-tube cryocooler
  mounted in physical/thermal contact with an HTS rotor and rotated together with it on
  an 1800-rpm mock-up — early (2006) demonstrated instance of literally rotating the
  cryocooler with the rotor, which is one of the mechanisms CF-5 must be clearly
  distinguished from or must design around.
- **IDS_pool:** YES.

### T3-06. "Cryogenic Rotary Joints Applied to the Cooling of Superconducting Rotating Machinery," IEEE Xplore doc. 6416012 (also ResearchGate 260513796)
- **Relevance:** Introduces the "Gas Blow Coupling" (GBC) — a non-contact thermal
  coupling using a fluid-based thermal medium across a narrow gap between stationary and
  rotating sides, avoiding mechanical rotary-joint contact — directly relevant
  alternative mechanism to any CF-5 embodiment relying on solid-strap contact conduction;
  a strong candidate "closest mechanism-different NPL reference" for G-CLAIM's
  different-mechanism design-around rung.
- **IDS_pool:** YES.

### T3-07. "Noncontact High-Torque Magnetic Coupler for Superconducting Rotating Machines," ResearchGate 291019525
- **Relevance:** Non-contact torque transfer (magnetic coupling) for isolating the cold
  rotating mass from the warm shaft — adjacent mechanical-isolation art relevant to
  CF-5's broader system context (how torque, not just heat, crosses the interface) but
  not itself a heat-extraction mechanism; retained for completeness.
- **IDS_pool:** YES (background).

### T3-08. "Cooling of Superconducting Motors on Aircraft," *Aerospace* (MDPI) 11(4):317, 2024
- **Relevance:** Review-level survey of aviation HTS motor cooling approaches including
  rotor cryocooling architectures; useful as a landscape reference for G-NOVEL's
  jurisdiction/assignee coverage sanity check. Full text was blocked (HTTP 403) on
  retrieval attempt (retried once per protocol); captured from search-snippet metadata
  only — flagged for manual re-pull before reliance.
- **IDS_pool:** YES, low-confidence pending re-pull.

### T3-09. "Cooling method for the rotor of a superconducting motor," IOP Conf. Series, doi 10.1088/1757-899X/1301/1/012008
- **Relevance:** Directly on-topic title; full text blocked (HTTP 403), retried once,
  still blocked. Captured as a gap — title/topic alone confirms relevance, content
  unverified.
- **IDS_pool:** YES, flagged unverified.

### T3-10. "Additive manufacturing materials for structural optimisation and cooling enhancement of superconducting motors in cryo-electric aircraft," IOPscience, doi 10.1088/1361-6668/acf1d4
- **Relevance:** Adjacent structural/thermal-materials background for cryo-electric
  aircraft motors (not rotating-interface-specific) — lower direct relevance, retained
  for completeness.
- **IDS_pool:** YES (background, lower priority).

### T3-11. "Cooling System Technologies on Superconducting Rotating Machines" and "Rotating Vacuum Heat Transfer, Rotating Cryocoolers, Slip Rings, Rotating Bearings, Ball Bearings," book chapters, Springer, *978-3-031-71408-5* (2024)
- **Relevance:** A dedicated recent (2024) book with chapters titled almost exactly on
  CF-5's problem statement (rotating cryocoolers, rotating vacuum heat transfer) — very
  likely the single richest NPL survey source for this candidate; full chapter text not
  independently pulled in this pass (paywalled Springer chapter, not fetched) — flagged
  as the highest-value follow-up NPL source before any G-NOVEL reliance.
- **IDS_pool:** YES, HIGH PRIORITY follow-up (content not yet reviewed past title/TOC).

---

## TIER 4 — Other / noise (ruled out but logged for candor)

### T4-01. CN 222654905 U — BYD rotor/motor/electrical-device patent
- **Assignee:** BYD
- **Priority:** Filed ~April 2024
- **Relevance:** Conventional (non-superconducting) electric-vehicle motor rotor cooling
  channel patent; surfaced on the Chinese query pack due to keyword overlap
  ("转子"/"冷却") but is NOT cryogenic/superconducting — excluded from IDS_pool as
  off-scope, logged only for search-transparency.

---

## Summary counts

- **Tier 1 (granted/near-scope patents):** 17
- **Tier 2 (applications/lower-confidence status):** 4
- **Tier 3 (peer-reviewed / NPL):** 11
- **Tier 4 (noise, excluded from IDS_pool):** 1
- **Total hits logged:** 33 (32 entered IDS_pool + 1 excluded noise hit)

## Notable close art flagged for G-NOVEL's priority attention
1. **T1-01/T1-02 (Hinetics US 12,506,395 B2 + US 12,531,457):** the anchor exemplar's
   own patent family already covers a rotating-cryocooler + radial-conductive-strap
   architecture. Any CF-5 claim must either (a) claim something Hinetics' filing does
   NOT cover (e.g., an NI-specific co-design of the rotating thermal path with turn-to-
   turn electrical behavior — composing with CF-1's insight), or (b) be scoped as a
   licensable improvement, not a freestanding filing over Hinetics' own architecture.
2. **T1-11 (CN 102840708 B, Dongfang Electric)** and **T1-12 (WO 2013/133487 A1, Hyundai
   Heavy Industries)** are the two strongest non-US/non-Hinetics anticipations: both
   disclose "cryocooler element inside the rotating frame + short conduction path to the
   winding," predating Hinetics by ~9–13 years, in the exact CPC space (H02K55-adjacent).
3. **T3-06 (Gas Blow Coupling)** is the strongest "different mechanism" NPL reference —
   relevant to G-CLAIM's design-around ladder rung 2 (different mechanism) if CF-5 needs
   to move away from solid-strap conduction.

## IDS_pool
All Tier 1–3 hits above (32 items) are entered into CF-5's `IDS_pool` per duty of candor.
Tier 4 (T4-01) is excluded as clearly off-scope (non-superconducting, non-cryogenic).

## Follow-up actions before any filing-relevant reliance
1. Manually re-pull US 12,531,457 and US 12,494,701 full text (OCR/image-PDF blocked
   WebFetch parsing).
2. Manually re-pull the Springer book chapters (T3-11) — highest-value unreviewed NPL.
3. Confirm assignees flagged "not independently confirmed" (T1-04, T1-14–T1-17, T2-01–
   T2-03, T2-04, T1-13) against USPTO/Espacenet assignment records directly.
4. Run a dedicated GE Aviation / GE Global Research assignee search (native Espacenet or
   PatentsView API) — this pass did not isolate GE-specific filings from the AMSC/
   Reliance family.
5. Have a search professional re-run the CN/JP/KR jurisdiction queries against native
   CNIPA/J-PlatPat/KIPRIS consoles; this pass used Google Patents' aggregated mirror only.
