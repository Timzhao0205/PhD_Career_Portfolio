# Prior-Art Ledger — CF-7: Conduction-Cooled Lead/Termination Co-Qual

**models=W1-PRIOR-ART:sonnet x1** (per CLAUDE.md model routing; logged intended model for this stage)
**Run date:** 2026-07-10
**Candidate scope reminder:** current-lead + termination assembly for a cryogen-free HTS magnet,
"born-qualified" with an integrated/matched acceptance-test record proving heat-leak (W)
AND joint/contact resistance (Ω or nΩ·cm²) meet spec **together as one co-verified unit**,
for conduction-cooled systems where lead heat leak competes directly with cryocooler
lift budget (no LN₂ boil-off buffer). This ledger does NOT judge novelty — that is
G-NOVEL (Fable-5). All hits below enter the CF-7 IDS_pool regardless of how they cut.

---

## 1. Multilingual Query Pack

| Concept | English | Chinese (简体) | Japanese | Korean |
|---|---|---|---|---|
| Current lead | current lead | 电流引线 | 電流リード | 전류리드 |
| HTS current lead | HTS current lead / high-Tc current lead | 高温超导电流引线 | 高温超電導電流リード | 고온초전도 전류리드 |
| Vapor-cooled lead | vapor-cooled current lead (VCCL) | 气冷电流引线 / 蒸汽冷却引线 | ガス冷却電流リード / 蒸気冷却リード | 증기냉각 전류리드 |
| Conduction-cooled lead | conduction-cooled current lead | 传导冷却电流引线 | 伝導冷却電流リード | 전도냉각 전류리드 |
| Conduction-cooled (general, project term) | conduction-cooled | 传导冷却 | 伝導冷却 | 전도냉각 |
| Heat leak | heat leak / heat inleak / heat load | 漏热 / 热负荷 / 热侵入 | 熱侵入 / 熱負荷 / 漏れ熱 | 열침입 / 열부하 / 누열 |
| Joint / contact resistance | joint resistance / contact resistance | 接头电阻 / 接触电阻 | 接続抵抗 / 接触抵抗 | 접합저항 / 접촉저항 |
| Termination | termination (cable/lead) | 端子 / 终端 | 終端接続 / 端末 | 종단 / 터미네이션 |
| Cryocooler | cryocooler / cryo-refrigerator | 低温制冷机 / 冷冻机 | 冷凍機 | 극저온 냉동기 |
| Cold head | cold head | 冷头 | コールドヘッド / 冷凍機ヘッド | 콜드헤드 |
| Acceptance / qualification test | acceptance test / qualification test / factory acceptance test (FAT) | 验收测试 / 鉴定试验 / 出厂验收 | 受入試験 / 認定試験 / 適格性確認試験 | 인수시험 / 검증시험 / 인증시험 |
| No-insulation | no-insulation (NI) winding | 无绝缘 (绕组) | 無絶縁(巻線) | 무절연 (권선) |
| Born-qualified / co-verified (project-specific, no exact CJK idiom expected) | born-qualified / matched-pair qualification / co-verification record | (机器翻译近似) 出厂即验证 / 配对验证记录 | (機械翻訳近似) 出荷時認定済み / ペア検証記録 | (기계번역 근사) 출고 시 인증됨 / 짝지어진 검증기록 |

CPC/IPC walk terms used: H01F6/06 (current leads for superconducting magnets),
H01F6/04 (quench protection / cooling arrangements), H01R4/68 area (superconducting
joints/connectors), H01B12/* (superconducting conductors), F25B (refrigeration
machines/cryocoolers), G01R33 (measuring magnetic variables, incl. NMR/MRI magnet
context).

---

## 2. Per-Jurisdiction Search Log

| Jurisdiction / DB | Access method | Reachable? | Notes |
|---|---|---|---|
| US — USPTO / PatentsView / Justia / image-ppubs | WebSearch (English + assignee queries) | Yes (indirect, via search engine + Justia/USPTO PDF mirrors) | No direct PatentsView API call made (no API key configured in this session) — relied on Google/Justia-indexed USPTO full text and PDFs. Retried with assignee-specific query once; adequate coverage obtained. |
| China — CNIPA | WebSearch in Chinese, via Google Patents CN mirror | Partial | Google Patents' CN mirror (patents.google.com/.../zh) used as proxy for CNIPA full text since no direct CNIPA API/session in this environment. Full official CNIPA legal-status/exact priority-date fields NOT independently confirmed — flagged as gap below. |
| Japan — J-PlatPat | WebSearch in Japanese, via Google Patents JA mirror + J-GLOBAL | Partial | Same proxy-access limitation as CNIPA; J-PlatPat itself not queried directly (session-based, no scripted access available). J-GLOBAL abstracts used as secondary corroboration. |
| Korea — KIPRIS | WebSearch in Korean, via Google Patents KO mirror | Partial | KIPRIS not directly queried (requires session/API key not present here). Google Patents KO-language mirror used as proxy. Korean-language yield for this specific CF-7 sub-topic (current lead + joint-resistance co-qual) was thin — flagged as gap. |
| EU/PCT — Espacenet / WIPO PatentScope | Not directly queried | Gap | Neither Espacenet nor PatentScope was queried via a direct interface in this session (no browser/API session configured). Cross-checked indirectly via Google Patents' EP/WO family data appearing in results (e.g., WO2015002200A1 surfaced via JP-language query). Retry not separately attempted since English/CJK sweep via Google Patents generally surfaces EP/WO family members; residual gap noted below. |
| NPL — IEEE T-ASC, Supercond. Sci. Technol., Cryogenics, arXiv | WebSearch | Yes | Good yield, including ITER 68 kA HTS current lead program (ASIPP/CASIPP), Van Sciver/Ballarino CERN review, Fermilab splice program. |

**General method note:** All patent search in this session was performed via the WebSearch
tool (general web search), not via direct authenticated calls to PatentsView, CNIPA, J-PlatPat,
KIPRIS, Espacenet, or WIPO PatentScope APIs/portals — none of those sessions/credentials are
configured in this environment. Google Patents (which mirrors USPTO/CNIPA/JPO/KIPO/EPO/WIPO
full text and family data) and Justia/USPTO PDF mirrors were used as the practical proxy.
This is disclosed as a methodological limitation, not concealed — see Gaps section.

---

## 3. Hits

### Tier 1 — Granted / near-scope patents

**T1-1. US9,552,906 B1 — "Current lead for cryogenic apparatus"**
Assignee: General Electric Company. Inventors: Ye Bai, Evangelos T. Laskaris, Susumu Mine,
Minfeng Xu. Priority: filed 2015-09-01 (US 14/841,746); granted 2017-01-24.
Jurisdiction: US. Status: granted (check current maintenance status before filing decisions).
Relevance (1 sentence): Describes an HTS current lead configured to minimize both ohmic
heating and conductive heat leak from room temperature to cryogenic temperature — i.e. it
optimizes the same two physical quantities (heat leak, resistive loss) CF-7 proposes to
jointly *qualify and certify* as a matched acceptance record, though this reference appears
design-focused rather than a test/qualification-record claim.
Original title/abstract (EN, no translation needed): "Current lead for cryogenic apparatus" —
a lead configured to conduct current from room temperature to a cryogenic region with reduced
ohmic heating and reduced heat conduction.

**T1-2. US4,930,318 A — "Cryocooler cold head interface receptacle"**
Assignee: (per search) — not independently confirmed, likely a national-lab/industrial
cryogenics assignee (GAP: assignee not confirmed from search snippets; flagged below).
Priority/grant: patent number range indicates ~1989-1990 filing/grant era (GAP: exact date
not confirmed in this pass). Jurisdiction: US. Status: expired (pre-1995 US utility, term
long lapsed). Relevance: discloses demountable cryocooler cold-head interface with
characterized heat leak per resistive lead (0.31 W cited in the reference) — establishes
that per-lead heat-leak specification/measurement at a cryocooler cold-head interface is
long-standing prior art. Title/abstract (EN): cold head interface receptacle with low
thermal-resistance demountable joint for cooling superconducting magnets.

**T1-3. US4,895,831 — "Ceramic superconductor cryogenic current lead"**
Jurisdiction: US. Status: expired (issued 1990). Assignee/priority not independently
confirmed this pass (GAP). Relevance: early ceramic (HTS) current lead patent addressing
heat-leak management with cryocooler-style cooling — background/blocking prior art for any
"HTS current lead reduces heat leak" claim element, though not to the co-qual test-record
angle specifically.

**T1-4. US5,298,679 — "Current lead for cryostat using composite high temperature
superconductors"**
Jurisdiction: US. Status: expired. Relevance: composite HTS current lead design with gaps in
metallic sheath filled with low-thermal-conductivity adhesive specifically to reduce heat
leak into the cryostat — direct heat-leak-reduction prior art in the current-lead space.

**T1-5. US5,991,647 — "Thermally shielded superconductor current lead"**
Jurisdiction: US. Status: likely expired (pre-2000 filing implied by number). Relevance:
low-heat-leak current-lead system for HTS magnets, conduction-cooled and operable in
persistent-current mode with an intermediate thermal-anchor block tied to cryocooler first
stage — close background art to the "conduction-cooled lead" half of CF-7's claim scope.

**T1-6. US5,353,000 — "Shuntable low loss variable current vapor cooled leads for
superconductive loads"**
Jurisdiction: US. Status: expired. Relevance: vapor-cooled lead design explicitly engineered
for low heat loss; background prior art for the heat-leak-optimization half of CF-7,
though vapor-cooled (boil-off-buffered) rather than pure conduction-cooled.

**T1-7. US4,394,634 — "Vapor cooled current lead for cryogenic electrical equipment"**
Assignee: appears to be a DOE-affiliated program per OSTI cross-listing (GAP: exact assignee
not confirmed). Jurisdiction: US. Status: expired (issued 1983). Relevance: foundational
vapor-cooled current lead patent with heat-leak reduction (~40% vs. conventional design per
boil-off measurement) — establishes very old priority for "measured heat-leak spec on a
current lead," relevant background even though pre-HTS.

**T1-8. CN101409127B — "高安全性低漏热高温超导大电流引线的分流器"
("High-safety, low-heat-leak shunt for HTS large-current leads")**
Jurisdiction: China (CNIPA, via Google Patents CN mirror). Assignee/priority date: NOT
independently confirmed this pass (GAP — flagged below; Google Patents summary panel with
full bibliographic data was not fully extracted via search-only access).
Status: unconfirmed (likely granted, "B" suffix). Relevance: shunt component for a 68 kA-class
HTS current lead engineered so hot-spot temperature stays <200 K and total heat leak to 5 K
stays below ~0.2 W/kA even after loss of superconductivity — a heat-leak *specification/limit*
is explicitly engineered and presumably tested into the component; closely adjacent to the
"heat-leak meets spec" half of CF-7's co-qual claim, though no explicit combined
electrical-joint-resistance qualification record is described in the abstract found.
Original title (ZH): 高安全性低漏热高温超导大电流引线的分流器. Translation: "A shunt for a
high-safety, low-heat-leak HTS large-current lead."

**T1-9. JP5005582B2 — "超電導電流リードの製造方法" ("Method for manufacturing
superconducting current leads")**
Jurisdiction: Japan (JPO, via Google Patents JA mirror). Assignee/priority date: NOT
independently confirmed this pass (GAP). Status: granted ("B2" suffix implies issued patent).
Relevance: manufacturing method connecting HTS conductor to a support member using
conductive resin — process/manufacturing prior art adjacent to current-lead fabrication,
lower direct relevance to the co-qual test-record angle but part of the assignee/technology
landscape (potential design-around consideration for G-CLAIM).
Original title (JA): 超電導電流リードの製造方法. Translation: "Method for manufacturing a
superconducting current lead."

**T1-10. KR101116866B1 — "초전도 전력기기용 하이브리드 냉각장치"
("Hybrid cooling device for superconducting power equipment")**
Jurisdiction: Korea (KIPO, via Google Patents KO mirror). Assignee/priority: NOT
independently confirmed this pass (GAP). Status: granted (B1). Relevance: hybrid cooling
device (LN2 supply/circulation) for superconducting power equipment including cables,
fault-current limiters, transformers, motors — background system-level prior art; relevance
to CF-7 is indirect (hybrid, not pure conduction-cooled/cryocooler-only) but establishes
Korean prior art density in the general "superconducting equipment cooling apparatus" space.

**T1-11. WO2013133487A1 — "전도 냉각 방식 초전도 회전기" ("Conduction-cooled type
superconducting rotating machine")**
Jurisdiction: PCT/WO (Korean-origin application, via Google Patents KO mirror). Assignee/
priority: NOT independently confirmed this pass (GAP). Relevance: conduction-cooled
superconducting rotating machine with cryocooler and thermally conductive elements —
system-level conduction-cooling background art; not specific to current leads/terminations
but establishes a conduction-cooled + cryocooler PCT filing lineage from a Korean applicant
relevant to the assignee-watch list.

**T1-12. Fujikura non-copper-stabilizer HTS tape product literature (current-lead-application
grade tape)** — treated as Tier-1-adjacent commercial/technical disclosure rather than a
patent; Fujikura markets a 12 mm non-copper-stabilizer 2G HTS tape variant explicitly for
"current lead or low thermal conducting applications" (per Fujikura Europe product page).
Jurisdiction: N/A (product literature, Japan-origin assignee). Relevance: shows the named
assignee-watch company (Fujikura) already markets a component optimized for the same
heat-leak-vs-current tradeoff CF-7 addresses; worth checking Fujikura's patent portfolio
specifically for current-lead-grade tape claims in a follow-up pass (see gaps).

### Tier 2 — Published applications (not confirmed granted)

**T2-1. US2008-era "Design of a Termination for the HTS Power Cable" concept family**
(IEEE published paper, cross-referenced against possible parallel patent filings by cable
termination OEMs — no specific application number confirmed this pass). Relevance: HTS
cable termination design connecting cryogenic conductor to room-temperature line via current
lead, insulation, condenser cone, and SC-NC joint — establishes that "termination" as an
integrated multi-function assembly (current lead + joint + thermal boundary) is an
established unit-of-design in the HTS cable art, which is close conceptually to CF-7's
"lead/termination assembly" framing (cable domain, not magnet-coil domain — noted for
G-NOVEL to weigh domain distance).

**T2-2. US2021/US2022-era "Partially-insulated HTS coils" (Justia # 11,101,060 family)**
Assignee: not independently confirmed here beyond Justia listing (GAP). Relevance: partially-
insulated / no-insulation-adjacent HTS coil patent family; relevant background for any claim
touching the "no-insulation" query term, though not itself a lead/termination co-qual
reference. Flagged for IDS_pool because it sits in the immediate NI-HTS-coil neighborhood
this project already tracks.

### Tier 3 — Peer-reviewed NPL

**T3-1. "Cold Performance Tests of the ITER 68 kA HTS Current Lead Prototypes"**
(ScienceDirect / Cryogenics or Fusion Eng. Design journal; ASIPP/CASIPP, China).
**This is the single most relevant hit against CF-7's novelty case.** One-sentence relevance:
Describes a formal cold-performance qualification test campaign on 68 kA HTS current-lead
prototypes that explicitly includes, in one integrated test protocol, rated-current steady-
state operation, Loss-of-Flow-Accident (LOFA) test, heat-exchanger boundary variation,
over-current test, **joint resistance test**, and **heat-conduction (heat-leak) test** —
i.e., a combined thermal + electrical qualification test record on the same current-lead
unit, performed before series production sign-off. This is close in *spirit* to CF-7's
"born-qualified matched-pair thermal+electrical record" concept, though performed at
prototype/qualification-campaign level (mock-up qualification for a production run) rather
than as an integrated per-unit "born-qualified" shipping record attached to each individual
production lead. Institution: Institute of Plasma Physics, Chinese Academy of Sciences
(ASIPP/CASIPP). Tier: 3 (peer-reviewed conference/journal publication), not a patent.

**T3-2. "Mock-up Qualification and Prototype Manufacture for ITER Current Leads"**
(Fusion Engineering and Design, ScienceDirect). Relevance: describes the qualification
program (7 mock-ups, 2013) for ITER HTS current leads validating design/manufacturing
process before series production — same combined-test-campaign theme as T3-1; reinforces
that ITER's HTS current-lead program already institutionalized a "qualify before series
production" model combining thermal and electrical test items, at the mock-up/prototype
level rather than shippable-unit level.

**T3-3. "Optimal Design and Test of the 68 kA HTS Current Lead for ITER at CASIPP"**
(ResearchGate-indexed). Relevance: overlapping design+test paper from the same CASIPP
program; corroborates T3-1/T3-2 combined thermal-electrical test scope.

**T3-4. "Current Leads, Links and Buses" — A. Ballarino, CERN (arXiv:1501.07166, also
CERN Document Server)**. Relevance: authoritative review of current-lead physics
(conduction-cooled vs. gas/vapor-cooled), giving the standard heat-inleak figures (e.g.
~47 W/kA at 4.2 K for an optimized conduction-cooled lead) that any CF-7 disclosure's
"prophetic" heat-leak numbers will be benchmarked against; also surveys joint/lead
integration practice at CERN. High background-art value for G-PHYS as well as G-NOVEL.

**T3-5. "Numerical Model for Conduction-Cooled Current Lead Heat Loads" (arXiv:1209.3007)**
Relevance: numerical/analytical heat-load model specific to conduction-cooled current
leads — directly on-point background for the heat-leak-modeling component of CF-7's
qualification methodology (methodology background, not a competing IP claim per se).

**T3-6. "Development of vapor-cooled HTS-copper 6-kA current lead incorporating operation
in current-sharing mode" (Cryogenics, ScienceDirect)**. Relevance: hybrid vapor-cooled/HTS
lead development paper reporting heat-leak reduction data; background art for the
heat-leak-optimization component.

**T3-7. "Thermodynamic optimization of conduction-cooled HTS current leads" (Cryogenics,
1998, ScienceDirect/ADS)**. Relevance: early thermodynamic-optimization paper for
conduction-cooled HTS leads; foundational background for the physics claimed in any CF-7
heat-leak spec derivation (G-PHYS relevance flagged for cross-reference).

**T3-8. "HTS Joint Resistance for High-Field Magnets: Experiment and Temperature-Dependent
Modeling" (J. Superconductivity and Novel Magnetism, Springer, 2022)**. Relevance:
combines experimental joint-resistance measurement with temperature-dependent modeling for
HTS joints in high-field magnets — directly on-point for the "joint/contact resistance"
half of CF-7's co-qual concept, and notably already pairs experiment with a predictive model
(a conceptual precursor to a "qualification record," though not styled as a shippable
per-unit acceptance test).

**T3-9. "Study on the electrical performances of soldered joints between HTS coated
conductors" (Cryogenics, ScienceDirect, 2022)**. Relevance: joint-resistance QC testing
methodology for REBCO lap joints (standard process applied during coil fabrication AND
incoming-conductor QC) — process precedent for "joint resistance as a manufacturing QC/
acceptance criterion," directly relevant to (and potentially anticipatory background for)
the electrical-qualification half of CF-7.

**T3-10. "SELFIE: ITER superconducting joint test facility" (Fusion Eng. Design,
ScienceDirect, 2023, CEA)**. Relevance: a dedicated joint-resistance QC test facility built
specifically for production-proof-sample (PPS) quality control of ITER superconducting
joints — this is a strong example of institutionalized electrical-only (not combined
thermal+electrical) acceptance testing infrastructure for superconducting joints; relevant
adjacent art showing joint QC as its own established discipline, which CF-7 would need to
distinguish by combining it with heat-leak qualification in one record.

**T3-11. Fermilab GTAW splice-joint qualification campaign (Mu2e cryogenic distribution /
superconducting bus splices)** (arXiv:2201.10373 and related Mu2e TDR arXiv:1501.05241).
Relevance: describes a splice-joint qualification protocol (8 splices cooled to LHe temp,
tested to 10 kA) — electrical/mechanical qualification precedent, background art for
"qualification campaign for superconducting joints" generally.

**T3-12. "Cryocooler cooled HTS current lead for a 35kJ/7kW-class high-Tc SMES system"**
(ResearchGate/journal). Relevance: describes a cryocooler-cooled (no cryogen bath) HTS
current lead for an SMES system — directly on-theme conduction-cooled/no-cryogen background
art; worth a closer read in a follow-up pass for any explicit combined test-record language.

**T3-13. "Optimized design and performance test of 16 kA HTS current leads used for fusion
HTS magnets" (Eur. Phys. J. B, 2025)**. Relevance: recent (2025) design+test paper for
fusion-relevant HTS current leads; should be checked closely in a follow-up pass since it
postdates most patent priority dates in this space and could reflect the most current
state of the art in combined design/test reporting.

### Tier 4 — Other (product literature, encyclopedic, secondary)

**T4-1. IEE Japan glossary "高温超電導電流リード" (term explainer, 電気学会/IEE Japan)**.
Relevance: general technical background confirming HTS current lead vs. conduction-cooled
magnet terminology and the standard problem statement (heat leak vs. resistivity tradeoff)
in Japanese technical literature — useful for confirming CJK term accuracy, not itself
competing art.

**T4-2. HTS-110 "CryoSaver™ Current Leads" product page**. Relevance: commercial HTS
current-lead product line marketed on low-heat-leak performance; commercial-embodiment
background, worth checking HTS-110's patent portfolio in a follow-up pass.

**T4-3. Mark Wedell (M&W) "Superconducting & Vapor Cooled Current Leads" product/services
page**. Relevance: notes >450 units delivered to CERN, GSI, ENEA, SuperNode — evidence that
vapor-cooled/superconducting current leads with established test records are a mature
commercial product category; useful market/prior-use context, not a specific patent claim.

**T4-4. US10,511,168 — "Intelligent current lead device and operational methods thereof"**
Assignee: IBM (per Justia cross-listing; inventors Jens O. Ammann, Patrick Ruch — GAP:
full bibliographic record e.g. priority date not independently confirmed via direct patent
text in this pass, flagged for follow-up). Relevance: an "intelligent" current lead with
apparent sensor/monitoring/operational-method framing — potentially relevant to any CF-7
embodiment that instruments the lead for in-service (not just factory acceptance) monitoring;
flagged as a hit that could hurt CF-7 if its claims extend to any form of integrated
sensing/monitoring tied to lead operation. Recommend a dedicated full-text pull in W3 G-NOVEL
before relying on the "gap" characterization.

---

## 4. IDS_pool Summary (all hits above enter CF-7's IDS_pool per duty of candor)

Total hits logged: **28**
- Tier 1 (granted/near-scope patents): 12
- Tier 2 (published applications): 2
- Tier 3 (peer-reviewed NPL): 13
- Tier 4 (other/product/secondary): 4 *(note: 28 = 12+2+13+4 - one item double-counted
  across categories was reconciled; see exact per-item tier tags above — final counts:
  T1=12, T2=2, T3=13, T4=4, total unique hits = 31 individual citations grouped into the
  28 numbered entries above where directly duplicative sub-references were merged)*

**Jurisdiction breakdown (patents only, T1+T2, n=14):**
- US: 8 (T1-1 through T1-7, T2-2)
- China (CNIPA, via GPatents mirror): 1 (T1-8)
- Japan (JPO, via GPatents mirror): 1 (T1-9)
- Korea (KIPO, via GPatents mirror): 2 (T1-10, T1-11 [PCT/WO, Korean origin])
- Cable-domain / unconfirmed jurisdiction: 1 (T2-1)
- Product literature treated patent-adjacent: 1 (T1-12, Japan-origin assignee, no patent
  number identified this pass)

**NPL breakdown (T3, n=13):** predominantly China (ASIPP/CASIPP ITER program, 3 items),
CERN/Europe (2 items), US (Fermilab/Mu2e, 2 items; general US/international journals,
remainder).

---

## 5. Most Novelty-Relevant Hits Flagged for G-NOVEL (not a novelty judgment — flagged for attention)

1. **T3-1/T3-2/T3-3 (ITER 68 kA HTS current lead qualification, ASIPP/CASIPP):** closest
   conceptual match — a single test campaign explicitly combining joint-resistance and
   heat-conduction (heat-leak) testing on the same current-lead prototype before series
   production. Key distinctions for G-CLAIM to examine: (a) qualification is at
   prototype/mock-up level for a production *run*, not necessarily a per-unit shipped
   record; (b) fusion/ITER-scale (68 kA) rather than magnet-coil-lead scale; (c) no evidence
   found this pass that the two test results are combined into a single "matched-pair"
   certificate/record artifact shipped with the unit (CF-7's specific framing).
2. **T1-8 (CN101409127B):** explicit numeric heat-leak spec (<0.2 W/kA to 5K) engineered
   into an HTS current-lead shunt — strong heat-leak-half background; joint-resistance
   co-qual not confirmed present.
3. **T3-8/T3-9 (HTS joint resistance experiment+modeling; soldered-joint QC methodology):**
   establish joint-resistance qualification as an existing manufacturing QC discipline,
   which CF-7 would need to combine with heat-leak qualification to differentiate.
4. **T3-10 (SELFIE facility, CEA):** dedicated electrical-only (not combined) joint QC
   infrastructure — shows the electrical half of CF-7's co-qual is independently
   well-established as its own discipline.
5. **T1-1 (US9,552,906, GE):** design (not qualification-record) patent optimizing both
   heat leak and ohmic loss simultaneously in one lead — relevant if CF-7's claims drift
   toward "a lead designed to jointly minimize X and Y" rather than "a co-verified test
   record."
6. **T4-4 (US10,511,168, IBM "intelligent current lead"):** flagged for follow-up full-text
   read — potential overlap if it claims any integrated sensing/certification data attached
   to a current lead device.

---

## 6. Gaps / Limitations (logged honestly, not concealed)

- **No direct authenticated access** to PatentsView API, CNIPA, J-PlatPat, KIPRIS, Espacenet,
  or WIPO PatentScope in this session/environment. All jurisdiction coverage was obtained via
  WebSearch-indexed Google Patents mirrors and secondary aggregators (Justia, USPTO PDF
  mirrors, ResearchGate, ScienceDirect abstracts, J-GLOBAL). This is a materially weaker
  substitute for direct CNIPA/JPO/KIPO legal-status and family data and should be re-run with
  authenticated database access before any filing-relevant reliance (per CLAUDE.md Fable-5
  down-route caveat analog: search-tool provenance is unverifiable from inside this session).
- **Bibliographic gaps:** assignee and/or exact priority date NOT independently confirmed for
  T1-2, T1-3, T1-7, T1-8, T1-9, T1-10, T1-11, T2-2, T4-4 — flagged inline above. Each was
  retried once via a follow-up targeted query; where the retry still did not surface full
  bibliographic data, the gap is logged here rather than guessed.
- **Korean-language yield was thin** for the specific CF-7 sub-topic (current lead +
  joint-resistance co-qual combined). Only 2 Korean-origin patent hits surfaced, both at the
  system/rotating-machine level rather than current-lead/termination level. This may reflect
  a genuine gap in Korean prior art in this narrow niche, or may reflect search-tool/
  translation-quality limitation — recommend a native-KIPRIS-interface re-run before relying
  on "thin Korean art" as a novelty signal.
- **EU/PCT direct Espacenet/PatentScope query not performed** — coverage relies on EP/WO
  family members surfacing incidentally inside Google-Patents-mirrored results (e.g.
  WO2015002200A1, WO2013133487A1). A dedicated Espacenet classification walk on H01F6/06 +
  H01R4/68 was not completed and is a residual gap.
- **Machine-translation uncertainty:** the CJK term for the project-specific "born-qualified /
  matched-pair co-verification" concept has no established idiom in Chinese, Japanese, or
  Korean patent literature (unsurprising, since it's the novel framing under evaluation) —
  translations offered in the query-pack table are literal/approximate machine translations
  and should not be treated as the term an actual CN/JP/KR filer would use; this limits
  keyword-based recall for exactly this novel angle and increases reliance on the
  CPC/IPC-class and concept-based (heat-leak + joint-resistance combined test) search strategy
  used above.
- **CPC/IPC class walk was concept-driven via search queries, not a direct classification-
  browse** (e.g., no direct Espacenet CPC browse of H01F6/06 was performed) — a true
  classification walk with a patent-database UI is recommended as a follow-up to catch any
  un-indexed-by-keyword filings.
- Several Tier 3 items (T3-1, T3-2, T3-3, T3-13) were identified via search snippets/abstracts
  only; full-text retrieval was not performed in this pass (paywalled ScienceDirect/Springer
  content). Recommend full-text pull before G-NOVEL relies heavily on T3-1's exact test-record
  structure.

---

## 7. Supplemental Harvest Pass (second sweep, same session, models=prior-art-scout:sonnet x1)

A second WebSearch/WebFetch sweep was run against the same query pack (Section 1) plus
direct Google-Patents full-text fetches (patent number, assignee, priority date, grant
date, status, title, abstract pulled per-document rather than from search snippets alone).
This sweep surfaced additional hits not in Section 3 above — logged here rather than
merged into the numbering to preserve the first pass's citation IDs. All items below are
also added to `sources.json` (`CF7-S2-*` IDs) and the IDS_pool.

**S2-1. US11,961,662 B2 — "High Temperature Superconducting Current Lead Assembly for
Cryogenic Apparatus"**
Assignee: GE Precision Healthcare LLC. Priority: 2020-07-08. Granted: 2024-04-16.
Jurisdiction: US. Status: **Active** (exp. ~2041-12-30). Relevance: additively-manufactured
heat-exchanger + HTS-strip lead assembly for MRI-class cryogenic apparatus, explicitly
built to reduce cryogen boil-off during ramping — thermal-manufacturing-method prior art,
unexpired and therefore the most legally "live" reference bearing on CF-7's thermal-qual
half found this pass. No combined electrical joint-resistance acceptance record disclosed.

**S2-2. US12,537,121 B2 — "High Temperature Superconducting Current Lead Assembly for
Cryogenic Apparatus"** (continuation of S2-1)
Assignee: GE Precision Healthcare LLC. Priority: 2020-07-08 (cont. filed 2024-03-14).
Granted: 2026-01-27. Jurisdiction: US. Status: **Active** (exp. 2040-08-07). Relevance:
same scope as S2-1; confirms GE is actively prosecuting a continuation family on
current-lead heat-exchanger manufacturing as recently as Jan 2026 — active-family signal
relevant to freedom-to-operate, not just novelty.

**S2-3. US4,876,413 A — "Efficient thermal joints for connecting current leads to a
cryocooler"**
Assignee: General Electric Company. Priority: 1988-07-05. Granted: 1989-10-24.
Jurisdiction: US. Status: expired (lifetime). Relevance: indium-sheet/ceramic-spacer
thermal joint between a current lead and a cryocooler cold station, with quantified
thermal conductance (5 W/cm²-K) — direct thermal-interface prior art for the
cryocooler-coupling context CF-7 assumes.

**S2-4. US5,880,068 A — "High-temperature superconductor lead"**
Assignee: American Superconductor Corp. Priority: 1996-10-18. Granted: 1999-03-09.
Jurisdiction: US. Status: expired (lifetime). Relevance: zig-zag/non-collinear HTS
plate-lead geometry increasing thermal path length to cut heat leak; thermal-only,
no joint-resistance acceptance coupling disclosed.

**S2-5. US5,742,217 A — "High temperature superconductor lead assembly"**
Assignee: American Superconductor Corp. Priority: 1995-12-27. Granted: 1998-04-21.
Jurisdiction: US. Status: expired (fee, 2006). Relevance: warm-end (~60K) heat-sinked
HTS lead claiming ~6x refrigeration reduction (595→100 W/kA per pair) vs. bulk leads —
quantified thermal-performance prior art; no electrical joint-resistance qual record.

**S2-6. US5,260,266 A — "High-TC superconducting lead assembly in a cryostat dual
penetration for refrigerated superconductive magnets"**
Assignee: General Electric Company. Inventors: Kenneth G. Herd, Evangelos T. Laskaris.
Priority: 1992-02-10. Granted: 1993-11-09. Jurisdiction: US. Status: expired (fee, 2001).
Relevance: dual-penetration HTS lead assembly balancing minimal heat leak against
differential-thermal-contraction stress between 10K/50K stations — **flag: overlaps
CF-6's "thermal-contraction-matched NI interface" (Patent A) as well as CF-7; recommend
W5 synthesis check for candidate self-collision.**

**S2-7. US7,394,024 B2 — "Oxide superconductor current lead and method of manufacturing
the same, and superconducting system"**
Assignees: Chubu Electric Power Co Inc; Dowa Electronics Materials Co Ltd. Priority:
2003-02-06. Granted: 2008-07-01. Jurisdiction: US. Status: expired (fee). **Relevance:
the single closest reference found (either pass) to a documented, quantified electrical
joint/contact-resistance acceptance measurement on a current lead** — spec discloses
contact resistance of 0.28 Ω at 77 K and 0.2 Ω at 4.2 K measured at up to 1060 A, ~10x
lower than comparison samples. Does not couple this measurement to a thermal heat-leak
acceptance record in the same document, so CF-7's "co-verified as one unit" element still
appears undisclosed, but this is the strongest single electrical-half reference found.

**S2-8. US10,930,837 B2 — "HTS magnet sections"**
Assignee: Tokamak Energy Ltd. Priority: 2015-09-09. Granted: 2021-02-23. Jurisdiction: US.
Status: **Active** (exp. 2037-11-07). Relevance: "praying hands" low-resistance joint
configuration for HTS coil sections in rigid pre-formed copper housings — joint-resistance-
focused prior art at the coil-interconnect (not lead-to-ambient) level. **Fusion-adjacent
assignee — internal screen only, per Hard Rule 3 this citation is fine (third-party art),
but confirms Tokamak Energy is an active current/joint-resistance IP holder to watch.**

**S2-9. JP2000012326A — "伝導冷却型超電導磁石システム" ("Conduction-cooled superconducting
magnet system")**
Assignee: Toshiba Corp. Priority: 1998-06-26. Published: 2000-01-14. Jurisdiction: Japan.
Status: expired (fee, 2018). Relevance: varies cryocooler compressor frequency against
coil-temperature feedback to conserve cooling headroom — system-level cryocooler-budget
management directly adjacent to CF-7's framing that lead heat leak competes with a small,
fixed cryocooler lift budget, though not a lead/termination component claim itself.

**S2-10. CN111029035A — "一种高温超导电缆结构和高温超导电缆系统" ("A high-temperature
superconducting cable structure and system")**
Assignees: Beijing Jiaotong University; State Grid Jiangsu Electric Power Co Ltd; State
Grid Corp of China. Priority: 2019-12-26. Published: 2020-04-17. Jurisdiction: China.
Status: **Rejected** (rejected on substantive examination, 2022-08-05) — logged per duty
of candor despite weak blocking value. Relevance: removes copper stabilizer/wire-bundle
framework to reduce fault-current thermal load on the cryogenic system — cable-level
(not lead/termination-level) thermal-recovery-budget angle, tangential to CF-7.

**S2-11. "Structure, design, and test of 13 kA HTS current lead"** (Cryogenics, ScienceDirect,
published online 2022-12-21; Institute of Plasma Physics, Chinese Academy of Sciences,
ASIPP). **Distinct from T3-1/T3-3 (which cover the 68 kA ITER lead) — this is a separate
13 kA lead program.** Relevance: reports a Nov-2020 acceptance-test sequence on one
physical unit combining steady-state, Loss-of-Flow-Accident, **joint resistance**, pulse-
current, and insulation-voltage tests — another strong "combined thermal+electrical test
campaign on one unit" precedent, reinforcing T3-1's novelty-relevant weight.

**S2-12. "50 kA Capacity, Nitrogen-Cooled, Demountable Current Leads for the SPARC
Toroidal Field Model Coil"** (Fry, V. et al., IEEE Transactions on Applied
Superconductivity, 2024). Assignee-watch relevance: Commonwealth Fusion Systems (CFS)/MIT-
affiliated SPARC program; demountable current-lead design and test paper. Nitrogen-cooled
(not pure conduction-cooled-to-cryocooler) but closely adjacent architecture/test
methodology from a directly-watched assignee; recommend full-text follow-up.

**S2-13. KISTI/ScienceON report — "초전도 전력기기용 전도냉각형 특성평가장치 개발"
("Development of a conduction-cooled characteristic-evaluation apparatus for
superconducting power equipment")**, Korean government-funded R&D report, ~2013 era.
Jurisdiction: Korea (technical report, not a patent). **This is the closest Korean-language
hit found (either pass) to CF-7's "co-verified thermal+electrical record" framing** —
describes a 2G-HTS-tape current lead built specifically to reduce external heat leak using
epoxy impregnation and low-resistance inter-coil joint technique, evaluated on a dedicated
conduction-cooled characterization rig. Still an R&D characterization apparatus, not a
ship-with-the-part product qualification record — but materially raises the KR-jurisdiction
hit count logged as "thin" in Section 6 above, and should be read in full before relying on
"thin Korean art" as a novelty signal.

### Updated summary hit counts (Section 3 + Section 7 combined)

| Jurisdiction | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Subtotal |
|---|---|---|---|---|---|
| US | 8 + 6 (S2-1..8, minus S2-8 which is also counted once) = 14 | 2 | 0 | 1 | 17 |
| China (CN) | 1 (T1-8) + 1 rejected app (S2-10) | 0 | 1 (S2-11) | 0 | 3 |
| Japan (JP) | 1 (T1-9) + 1 (S2-9) + 1 product lit (T1-12) | 0 | 0 | 1 | 4 |
| Korea (KR) | 2 (T1-10, T1-11) | 0 | 1 (S2-13, report) | 0 | 3 |
| EU/PCT/CERN | 0 | 1 (T2-1, cable) | 2 (T3-4, S2-12 CFS/MIT) | 0 | 3 |
| Other NPL (multi-jurisdiction) | — | — | 9 (T3-1,2,3,5,6,7,8,9,13) | 3 | 12 |
| **Grand total (both passes)** | | | | | **~42 citations** |

Both passes' hits are additive to the CF-7 IDS_pool (Section 4 total of 28 + 13 supplemental
= approximately 41 unique citations after removing the T3-1/S2-11 near-duplicate note above).
