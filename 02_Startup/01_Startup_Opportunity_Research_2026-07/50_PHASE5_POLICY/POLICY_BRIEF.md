# PHASE 5 — GEOPOLITICS & REGULATORY BRIEF (US–China, hardware deep tech)

**Status:** research current as of 2026-07-03. All rules verified against sources gathered this
session (IDs `[P-##]`, ledger: `50_PHASE5_POLICY/policy_sources.json`).

> **RESEARCH, NOT LEGAL ADVICE.** This brief is an analyst's synthesis of public sources. Export
> control, sanctions, investment-security, and PRC regulatory questions are fact-specific and the
> rules below changed repeatedly in 2024–2026 and will change again (several key rules are
> *suspended*, not repealed, and re-activate on fixed dates in late 2026). Any actual structuring,
> classification (ECCN), hiring, or investment decision requires licensed export-control counsel,
> CFIUS/outbound-investment counsel, and PRC counsel. Every "tripwire" below carries an implicit
> **CONSULT COUNSEL** flag.

---

## EXECUTIVE SUMMARY (1 page)

**The single most important fact for this founder:** if he is a "U.S. person" (citizen or green
card holder — status at founding time, not at PhD time, is what matters), U.S. law now follows
him *personally* into China. Since 2025-01-02 the Treasury Outbound Investment Security Program
(31 CFR Part 850) prohibits or requires notification of U.S.-person investments — **explicitly
including founding a company (greenfield) or a JV in China** — in semiconductors, quantum, and
AI [P-01][P-02][P-05]. The COINS Act (signed 2025-12-18 in the FY2026 NDAA) codified the program,
added high-performance computing/supercomputing and hypersonics, extended it to China+HK/Macau,
Cuba, Iran, North Korea, Russia, Venezuela, gave Treasury authority to add further sectors, and
ordered new regulations within 450 days (~March 2027) — i.e., **the regime will be broader, not
narrower, by his 2029 launch window** [P-03][P-04].

**Archetype-critical detail:** fabricating "integrated circuits manufactured from a gallium-based
compound semiconductor" in China is on the *prohibited* list — a U.S. person cannot found a
Chinese GaN-IC fab venture at all, and *any* IC design/fab/packaging in China is at minimum
*notifiable* [P-01][P-02]. Power converters, magnets, coil-winding machines, and quench-protection
hardware are **not currently covered sectors** — this is the widest legal lane for China-first —
but Treasury's new sector-adding authority makes that lane revocable [P-03].

**Export controls (EAR):** most power-electronics products are EAR99, but this mission's domains
sit near four controlled clusters: (1) nuclear-proliferation ECCNs that catch *precision power
conversion* — 3A225 frequency changers (>600 Hz, ≥40 VA multiphase, frequency control <0.2%)
[P-14][P-15]; (2) superconductivity — 1C005 superconductive composite conductors, 3A001.e.3
superconducting solenoidal electromagnets (with 3A201 nuclear overlay), and the Sept-2024 quantum
rule's 3A904 cryocoolers (sub-4 K pulse-tube, sub-100 mK systems) [P-10][P-11][P-15]; (3)
semiconductor-manufacturing items — 3B001 (incl. GaN-relevant epitaxy/MOCVD tools) massively
expanded Dec-2024 with new FDP rules [P-12][P-13]; (4) space/rad-hard — 9x515/ITAR, effectively
embargoed to China [P-19]. Separately, EAR §744.6 restricts **U.S.-person "support"** of advanced
(≤16/14 nm logic, adv. DRAM/NAND) Chinese fabs *even when no U.S.-origin item is involved*
[P-42][P-43]. Hiring PRC-national (non-green-card) engineers in a U.S. company that holds
controlled technology requires **deemed-export licenses** [P-08][P-09].

**Entity List:** 80+ additions in Mar-2025, 32 more in Sep-2025 (incl. Chinese chipmakers)
[P-16][P-17]. The 50%-ownership "Affiliates Rule" was issued 2025-09-29, then **suspended to
2026-11-09/10** as part of the US–China truce — plan for it to be live by 2029 [P-06][P-07].
Penalties (frozen at 2025 levels through 2026): up to $374,474 per EAR violation or 2× transaction
value, criminal exposure higher; outbound-investment civil cap $377,700 or 2× amount [P-03][P-18].

**China side:** the 15th Five-Year Plan (adopted 2026-03) names **hydrogen + nuclear fusion
energy** among six future-industry "new growth points," and lists integrated circuits, industrial
machine tools, **high-end instruments**, base software, and advanced materials as
key-core-technology 攻关 targets [P-24][P-25][P-26][P-27][P-28]. Money and demand-pull are real:
Big Fund III (RMB 344B, equipment/materials-weighted) [P-33]; 首台套 first-unit equipment insurance
subsidy (≤80% of premium; catalog explicitly covers precision instruments, electronic special
equipment, machine tools) [P-31]; and from **2026-01-01 a 20% price-evaluation preference for
"domestic products" in government procurement** — nominally ownership-neutral, so a
foreign-founded company *producing in China* qualifies, while imports are penalized [P-32].
Fusion is a "national team" play: China Fusion Energy Co. (Shanghai, RMB 15B registered capital,
CNNC-led) [P-29][P-30], BEST burning-plasma device targeted for end-2027 in Hefei, with reported
total investment raised to ~RMB 30B and reported central-SOE future-industry commitments >RMB 300B
by 2030 (tier-3 figures) [P-37][P-38]. China's own export controls (gallium/germanium/antimony ban
to the U.S.; Oct-2025 rare-earth rules) are **suspended only until Nov-2026**; Apr-2025 rare-earth
licensing (Sm, Gd, Tb, Dy…) and the ban on supplying U.S. military end-users remain in force —
a structural materials advantage for China-based magnet/HTS production and a supply risk for
U.S.-based production [P-36].

**Bottom line by archetype (detail in §5):** power-systems archetypes (d, f, c, g) are legally
open to China-first or parallel today; superconducting-equipment archetypes (a, i, b) are open but
sit near nuclear/quantum ECCNs and near Treasury's expansion authority; fab-facing (e) and
GaN-IC-adjacent plays trigger §744.6 / OISP as a U.S. person; satellite (h) is U.S.-only. Anything
China-facing must be built to survive: Affiliates Rule reactivation (Nov-2026), COINS regulations
(~2027), and both governments' willingness to weaponize the other's chokepoints. A U.S. person
cannot escape the outbound rules by using a foreign shell he "knowingly directs" — structure
choices change *which* rules apply, not *whether* rules apply. **Consult counsel before any step.**

---

## 1. US EXPORT CONTROLS TOUCHING THE MISSION'S DOMAINS

### 1.1 Framework in one paragraph

The EAR (15 CFR 730–774, administered by BIS) governs U.S.-origin dual-use items, U.S.-content
foreign items, foreign direct products of U.S. tech/tools, and certain *activities of U.S.
persons*; the ITAR (State/DDTC) governs the U.S. Munitions List. Controls attach at three layers:
**what** (ECCN on the Commerce Control List), **who** (Entity List, MEU List, sanctioned parties),
and **what for** (end-use rules like §744.6, and China-wide license policies). For a hardware
company, classification of every product, subassembly, and its "technology" (drawings, source
code, know-how) is the foundational compliance task.

### 1.2 ECCN map for this mission's product space

| Domain | Relevant controls (verify each classification with counsel) | Practical read |
|---|---|---|
| Commodity power electronics (800VDC modules, GPU-cluster buffers) | Mostly **EAR99**; AT-only. | Freely exportable to non-listed Chinese civil customers; the risk is *who* buys (Entity List, military end-use/user rules), not the item. |
| Precision magnet / scientific power converters | **3A225** — frequency changers/generators: multiphase ≥40 VA, ≥600 Hz output, frequency control better than 0.2% (NSG/nuclear controls; industry deliberately caps drives at 599 Hz to stay out) [P-14][P-15]. Adjacent nuclear-detonation ECCNs (3A228/3A229 pulse equipment) for high-current pulsed supplies. | A high-precision magnet supply can *accidentally* meet 3A225. Design-out or license. NP-controlled items to China = license required, tight review. |
| Superconductors & magnets | **1C005** superconductive composite conductors (length/mass thresholds); **3A001.e.3** superconducting solenoidal electromagnets (with **3A201** nuclear-related overlay for high-field solenoids; MRI-type exclusions exist) [P-15]. Whether REBCO coated conductor and NI-HTS coils fall in/out of 1C005/3A001.e.3 is a classic classification question — counsel. | HTS magnets and even tape shipments US→China can require licenses; China-based production avoids the U.S. control but not U.S.-person/tech questions. |
| Cryogenics / quantum-adjacent | Sept-2024 IFR (FR 2024-19633) added quantum computing, cryogenic systems: **3A904** (≥600 µW at ≤100 mK for >48 h; specified two-stage pulse-tube cryocoolers rated <4 K), plus quantum ECCNs with worldwide license requirements and deemed-export reach [P-10][P-11]. | HTS instruments using sub-4 K pulse-tube coolers can drag a controlled item into the BOM. Quench-protection electronics per se are not named. |
| WBG semiconductor making/testing | **3B001** semiconductor manufacturing equipment — expanded by the 2024-12-05 rule (new 3B993/3B994 ECCNs, new FDP rules); GaN epitaxy (MOCVD) tools are within 3B001's scope [P-12][P-13]. GaN RF/MMIC parts sit in 3A001.b sub-items. Burn-in/test instruments: classification varies; many are 3B992/EAR99, but end-user rules dominate. | Selling U.S.-origin test/burn-in gear into Chinese fabs = license territory whenever the fab is listed or advanced-node; see §1.4 for U.S.-person exposure even without U.S. items. |
| Precision manufacturing equipment (coil winders) | No ECCN names "coil winding machine" for HTS; filament-winding (1B001/1B101/1B201 composites) and machine-tool (2B001) parameters are the nearest controls; Sept-2024 rule also added metal additive-manufacturing controls [P-10][P-15]. Software/技术 for the machine may be controlled even if the machine is not. | Likely EAR99/low-control as hardware — but a winder marketed for fusion/defense magnet production invites end-use scrutiny. |
| Fusion-adjacent | No fusion-specific ECCN regime exists today; control arrives via the nuclear ECCNs above, cryo/quantum ECCNs, deemed exports, and Entity-List status of Chinese fusion institutions. | Watch this space: fusion is exactly the kind of sector both BIS and Treasury (COINS §sector-adding authority) could designate before 2029 [P-03]. |
| Satellite / rad-hard electronics | **ITAR USML Cat XV** for military/intel spacecraft; **9A515.d/.e** rad-hard microelectronics on the EAR with 9D515/9E515 software/tech; 9E515 "required" technology is broad [P-19]. China: effectively embargoed for both regimes. | U.S.-only archetype. Even hiring non-U.S.-persons onto ITAR programs is restricted. |

### 1.3 Entity List dynamics (the fastest-moving layer)

- 2025-03-25: 80+ additions across two rules, China-heavy (advanced computing, AI) [P-16].
- 2025-09: 32 additions, incl. Shanghai Fudan Microelectronics and affiliates — i.e., *civilian
  chipmakers that would be natural customers for archetype (e)* [P-17].
- **Affiliates Rule** (IFR 2025-09-29): any entity ≥50% owned, directly/indirectly, in aggregate,
  by Entity List/MEU/sanctioned parties inherits the listing; imposes an affirmative
  beneficial-ownership diligence duty (new Red Flag 29) [P-07]. Suspended 2025-11-10 →
  **2026-11-09** as part of the U.S.–China deal; the legal text remains and re-activates
  automatically [P-06]. Planning assumption for 2029: live. Every Chinese customer needs an
  ownership tree, not just a name-screen.
- Listings are how "fusion-adjacent" restrictions will most likely arrive (institute-by-institute)
  rather than by new ECCN — selling *any* EAR item, even EAR99, to a listed CAS institute
  requires a license, typically with presumption of denial.

### 1.4 U.S.-person activity controls — beyond items

EAR **§744.6** requires a BIS license for U.S. persons who "support" — ship, transmit, transfer,
facilitate, or service, *even for items not subject to the EAR* — the development or production of
ICs at Chinese fabs meeting advanced criteria (non-planar logic / ≤16/14 nm, advanced DRAM/NAND)
[P-42][P-43]. Consequence: a U.S.-person founder **cannot simply "build the tester in China from
Chinese parts" to serve advanced Chinese fabs** — his own activity is the controlled thing.
Support to legacy-node fabs is outside these criteria today, but node verification burden falls on
him, and criteria have only ever tightened.

### 1.5 Deemed exports — hiring as an export event

Releasing controlled technology/source code to a foreign national in the U.S. is an export to
their home country; a license is needed whenever one would be needed to ship the tech there.
Exempt: U.S. citizens, **permanent residents**, protected individuals; also exempt: published
information and *fundamental research* (which is why the same person can do things in a
university lab that his startup cannot do) [P-08]. BIS issued ~1,350 deemed-export licenses in
2022, ~35% for Chinese nationals [P-09]. Practical design rule for a U.S. entity in these domains:
either keep the tech stack EAR99, or gate controlled tech to USP/green-card staff, or budget
licensing time per hire. For the founder himself: as a green-card holder/citizen he faces no
deemed-export issue *receiving* tech in the U.S. — his issue is §744.6/OISP-type *outbound
activity* controls.

---

## 2. US OUTBOUND-INVESTMENT RESTRICTIONS (the "reverse-CFIUS" regime)

### 2.1 The rule in force today: 31 CFR Part 850

Effective 2025-01-02 under EO 14105 [P-05]. Core mechanics:

- **Who:** "U.S. persons" — U.S. citizens and lawful permanent residents *wherever located*,
  U.S.-organized entities, anyone in the U.S. U.S. persons must also refrain from *knowingly
  directing* prohibited transactions of non-U.S. entities, and controlled foreign subsidiaries of
  U.S. persons are reached — a foreign holding company is not an exit (counsel).
- **What transactions:** equity/contingent-equity acquisitions, certain convertible debt,
  **greenfield or corporate expansion**, **joint ventures**, certain LP fund commitments [P-05].
  → *Founding and capitalizing a Chinese company is squarely a covered transaction type.*
- **Covered foreign person:** a person of a country of concern engaged in a covered activity —
  i.e., the founder's own new Chinese entity, if it does a covered activity.
- **Prohibited** (850.224, fetched text): EDA for ICs/advanced packaging; front-end volume-fab
  SME; advanced-packaging SME; EUV-exclusive items; design of ICs meeting 3A090.a or designed for
  ≤4.5 K operation; fabrication of advanced logic (non-planar / ≤16/14 nm), NAND ≥128 layers,
  DRAM ≤18 nm half-pitch, **"integrated circuits manufactured from a gallium-based compound
  semiconductor"**, graphene/CNT ICs, ≤4.5 K ICs; advanced packaging; supercomputers ≥100 PFLOPS
  FP64 (≥200 FP32) per 41,600 ft³; quantum computer development/critical-component production;
  **quantum sensing platforms designed for military/intel/surveillance use**; quantum networking
  for those ends; AI trained ≥10^25 ops (10^24 with biodata) or designed for exclusive
  military/intel end uses [P-01].
- **Notifiable** (850.217): design, fabrication, or packaging of **any other integrated circuit**
  (i.e., *all* IC activity in China is at least notifiable); AI systems for certain
  military/intel/cyber/robotics applications or trained ≥10^23 ops [P-02].

### 2.2 The 2025 statute: COINS Act (FY2026 NDAA, signed 2025-12-18)

Codifies the program in statute; **adds high-performance computing/supercomputing and hypersonic
systems**; defines countries of concern as China (incl. HK & Macau), Cuba, Iran, North Korea,
Russia, Venezuela; switches the covered-foreign-person test toward a **direct/indirect ≥50%
ownership** standard; authorizes the Treasury Secretary to designate *additional* prohibited or
notifiable technologies that enable a country of concern's military/intel/surveillance/cyber
capabilities; requires new/amended regulations within **450 days (~March 2027)**; existing 31 CFR
850 stays in force meanwhile; pre-2025-12-18 transactions grandfathered from the *new* rules only
[P-03][P-04]. Analyst judgment: superconducting/fusion and power infrastructure for HPC are
plausible future designations under the new authority — a 2029 plan should carry that scenario.

### 2.3 What "U.S.-person founder of a Chinese entity" concretely triggers

1. **Formation itself** — greenfield establishment/capitalization of a Chinese entity that will
   engage in a covered activity = covered transaction (prohibited or notifiable per the activity)
   [P-01][P-02][P-05].
2. **Every later round he touches** — his own follow-on investments; his solicitation of U.S. LPs;
   U.S. VC money into the Chinese entity makes each U.S. investor a party with its own OISP
   analysis (this alone deters most U.S. funds from covered-sector China deals).
3. **Ongoing conduct** — as an officer he cannot "knowingly direct" a prohibited transaction even
   if the investing vehicle is foreign; and expansions of the Chinese entity into covered
   activities later (e.g., the power-converter company adds an in-house GaN IC line) create new
   covered transactions at that time.
4. **Notification mechanics** — notifiable deals file with Treasury within 30 days post-closing;
   records retention; false statements are independently punishable (counsel for current filing
   details).
5. **Status arbitrage is a real but drastic variable** — the rule attaches to citizenship/LPR
   status. Abandoning a green card before founding changes the analysis entirely (and forecloses
   the U.S.-first path, and has tax/exit consequences). Flag for counsel; not a recommendation.
6. **What it does NOT cover today:** power electronics using purchased dies, magnets, winding
   machines, quench protection, RF amplifiers, converters — none are listed covered activities
   unless they cross into IC production, quantum-critical components, supercomputing, or
   (post-COINS regs) whatever Treasury adds [P-01][P-02][P-03].

### 2.4 Penalties

Civil: up to **$377,700 per violation or 2× the transaction amount** (IEEPA-based, inflation
frozen for 2026); criminal referral possible under IEEPA (up to $1M / 20 years for willful
violations); divestment can be ordered [P-03]. EAR violations separately: up to **$374,474 per
violation or 2× value**, plus denial orders and criminal exposure [P-18].

---

## 3. CFIUS AND INBOUND CAPITAL (if a China-linked company later raises in the US)

- **Jurisdiction:** CFIUS reviews foreign acquisitions of control of any U.S. business, and
  non-controlling "covered investments" in **TID** businesses (critical Technology,
  Infrastructure, sensitive Data) [P-20].
- **Mandatory filings:** (1) covered investments in a U.S. business that produces/designs/tests
  critical technologies where an export license would be needed to send that tech to the
  investor's country — most of this mission's controlled-item archetypes qualify as "critical
  technology" businesses; (2) foreign-government "substantial interest" deals (foreign person
  gets ≥25% voting; a foreign government holds ≥49% of that person) [P-20][P-21]. Chinese
  state-linked VC money into a U.S. entity holding 3A225/3A001/9x515-class tech is therefore a
  mandatory-filing event, not a choice.
- **Direction of policy:** the America First Investment Policy memo (2025-02-21) pairs *more*
  restriction on China-linked investment in U.S. technology/critical infrastructure with *faster*
  lanes for allies; implementation is underway via the CFIUS **Known Investor Program** (pilot
  announced May-2025; RFI published 2026-02-06, comments closed 2026-03-18) — eligibility keys on
  "verifiable distance and independence" from adversary countries [P-22][P-23][P-20].
- **Concrete implications for the founder's structures:**
  1. *US-first, clean cap table:* no CFIUS issue at all until a foreign investor arrives; keep it
     that way through Series A if defense/space (h) is in scope.
  2. *Parallel structure:* if the Chinese arm (or any Chinese entity) holds equity in the U.S.
     arm, or the founder holds the U.S. arm *through* a Chinese/HK vehicle, U.S. raises and exits
     acquire a CFIUS overlay; acquirers will price that in. Cleanest pattern seen in practice:
     two sibling companies under a neutral (US or founder-personal) top, no cross-shareholding,
     documented IP provenance and separate engineering records. Counsel must design this.
  3. *China-linked history:* CFIUS can also chill informally — U.S. VCs diligence founder ties,
     PRC talent-program participation (§4.5), and any PRC government funding in the group. CFIUS
     has non-notified-transaction outreach; "we never filed" is not a safe harbor.
  4. *Defense customers:* FOCI (foreign ownership, control or influence) review under DCSA is a
     separate, stricter screen than CFIUS for archetype (h) and any classified work.

---

## 4. CHINA 2026–2030: PLAN, MONEY, PROCUREMENT, AND PRACTICE

### 4.1 The 15th Five-Year Plan (十五五, adopted at the NPC, 2026-03)

- **Future industries — the founder's domains are named at the top of the plan.** The 纲要 calls
  for "推动量子科技、生物制造、氢能和核聚变能、脑机接口、具身智能、第六代移动通信等成为新的经济增长点"
  (making quantum, biomanufacturing, **hydrogen & fusion energy**, BCI, embodied AI, 6G into new
  growth points), with a "future-industry full-chain cultivation system," national
  future-industry research institutes, and proof-of-concept centers [P-24].
- **Key-core-technology 攻关 list:** 集成电路、工业母机、高端仪器、基础软件、先进材料、生物制造 —
  integrated circuits, machine tools, **high-end instruments**, base software, advanced materials
  [P-24]. Precision instruments and equipment (archetypes a, b, e) are on the national
  import-substitution list by name.
- **Energy:** a "clean, low-carbon, safe, efficient new energy system"; the State Council
  Information Office briefing named **可控核聚变 (controllable fusion)** — with long-duration
  storage and green hydrogen — as a major R&D 攻关 direction for the plan period [P-24][P-25].
- **Talent:** the plan commits to "健全海外引进人才支持保障机制，建立高技术人才移民制度"
  (overseas-talent support mechanisms and a high-tech immigration system) — the pull for a
  Stanford PhD returnee is explicit state policy [P-24].
- Think-tank consensus reads (MERICS, Bruegel, CRS): AI is the organizing logic (52 mentions vs 6
  in the 14th plan); semiconductors elevated to "pillar industry" status with subsidies,
  procurement preference, and regulatory support; self-reliance targets aim at exactly the
  equipment/instrument/software categories where China depends on the US/EU/Japan
  [P-26][P-27][P-28].

### 4.2 Import substitution (国产替代) money relevant to the mission

- **Big Fund III** (国家集成电路产业投资基金三期): registered 2024-05-24, **RMB 344.0B** —
  larger than phases I+II combined; reported deployment logic ~70% toward equipment/materials
  localization, channeled via sub-funds (华芯鼎新 ~RMB 93B; 国投集新 ~RMB 71B targeting
  equipment/materials/advanced packaging) [P-33]. Consequence for archetype (e): Chinese fabs are
  *paid* to qualify domestic test/burn-in equipment — a Chinese-incorporated instrument company
  rides this; a U.S. exporter fights it.
- **首台套 first-(set)-of-kind major technical equipment**: 2025 MIIT/MOF/NFRA notice subsidizes
  ≤**80% of the insurance premium** for first-unit domestic equipment in the 2024 catalog —
  which explicitly covers 高端工业母机, 电子专用装备, **精密仪器仪表** (precision instruments) —
  de-risking the first Chinese buyer of a new domestic machine [P-31]. Directly usable by
  archetypes (a), (b), (e) if incorporated and producing in China.
- **Fusion national team:** China Fusion Energy Co., unveiled Shanghai 2025-07-22, registered
  capital **RMB 15B** (~$2.1B), CNNC-led, mandated to industrialize fusion [P-29][P-30]; CAS
  burning-plasma international science program launched Nov/Dec-2025 opening BEST and other
  devices to international collaboration [P-37]; BEST (Hefei) targets D-T burning-plasma
  experiments after end-2027 completion, 20–200 MW fusion-power demonstrations; trade press
  reports Hefei BEST total investment raised from RMB 15B to ~RMB 30B and SASAC future-industry
  commitments >RMB 300B by 2030 (tier-3 figures, directionally consistent across outlets)
  [P-37][P-38]. Hefei, Shanghai, and Chengdu are competing fusion clusters with local incentive
  packages [P-38]. For archetypes (a)(b)(c)(i): the world's largest and fastest-growing buyer
  pool for magnet systems, precision converters, and quench protection is being assembled inside
  China's state system — reachable realistically only via a Chinese entity (procurement rules
  below), and *unreachable for controlled U.S.-origin items* (§1).

### 4.3 Government-procurement preference — the decisive demand-side rule

国办发〔2025〕34号 (State Council General Office), **effective 2026-01-01**: government
procurement applies a **20% price deduction in bid evaluation for "domestic products"** — defined
by (i) production in China with substantial transformation, (ii) domestic component-cost ratios
to be set product-by-product by MOF, (iii) for specified products, key components/processes done
in China. If ≥80% of a supplier's offered product cost qualifies, the whole bid gets the 20%
deduction. Explicitly ownership-neutral: SOEs, private, **and foreign-invested enterprises
producing in China are treated identically** [P-32]. Since fusion institutes, CAS labs,
universities, and SOE-linked hospitals (proton therapy, archetype g) buy through government
procurement, the practical rule for archetypes (a)(b)(g)(i) is: **to sell to Chinese state
buyers at scale, manufacture in China**. Conversely, the same rule quantifies the handicap of a
US-first exporter into China: ~20% evaluation penalty plus localization-ratio exclusions.

### 4.4 China's own export controls — the materials leverage

- Suspended (truce, expiring **Nov-2026**): the Dec-2024 ban on gallium/germanium/antimony/
  superhard-material exports to the U.S. (Announcement 46 Art. 2, suspended to 2026-11-27) and
  the six Oct-2025 announcements (rare-earth equipment/tech, medium/heavy REs, battery materials,
  extraterritorial Chinese-nexus RE rules; suspended to 2026-11-10) [P-36].
- Still in force: Announcement 46 Art. 1 (no dual-use exports to U.S. military end users);
  2025 No. 10 (W, Te, Bi, Mo, In); **2025 No. 18 licensing on seven medium/heavy rare earths
  (incl. Sm, Gd, Tb, Dy)** — inputs for magnets and REBCO-adjacent supply chains [P-36].
- Read for the decision framework: a U.S.-based HTS/magnet manufacturer carries Chinese
  materials-control risk; a China-based one carries U.S. equipment/tech-control risk. Parallel
  structures carry both, plus the compliance wall between them.

### 4.5 Practical realities for a US-educated returnee founder

- **Incentive parks & clusters:** future-industry status (fusion, quantum) unlocks provincial
  packages — Hefei (BEST/ASIPP ecosystem), Shanghai (China Fusion Energy Co., 环流 devices),
  Chengdu (SWIP) [P-38][P-29]. Typical packages: subsidized space, equipment grants, hiring
  subsidies, returnee (海归) startup grants; negotiated case-by-case — PRC counsel + local
  government relations needed.
- **Talent-program tripwire (both directions):** PRC recruitment programs are the standard
  vehicle for returnee incentives, but U.S. law (42 U.S.C. §19232, CHIPS & Science Act) bars
  participants in **malign foreign talent recruitment programs** from federal R&D awards, and
  SBIR/STTR agencies must deny awards where any owner/covered individual is party to one
  [P-39][P-40][P-41]. A parallel-structure founder who signs a Chinese talent-program contract
  can permanently forfeit U.S. SBIR/DOE funding eligibility — often the cheapest U.S. capital for
  archetypes (b)(c)(g)(h). Take park incentives as commercial contracts, not talent-program
  membership, and have counsel screen the contract text.
- **Capital controls / structure:** PRC residents using an offshore SPV over a Chinese OpCo must
  register under **SAFE Circular 37** (round-trip investment; registration before capitalizing
  the SPV) — the founder's own status (PRC citizen? U.S. LPR? both rules can apply to different
  actors in the deal) determines filings; unregistered structures block profit repatriation and
  poison later financings [P-34][P-35]. Standard menu: WFOE (foreign-funded, easiest for a U.S.
  person, but then the *founding is his outbound transaction* — §2), domestic entity + offshore
  holding (Circular 37), or VIE (disfavored for hardware). RMB venture money increasingly
  requires onshore (境内) structures and China-kept IP.
- **IP:** the 攻关/国产替代 machinery rewards domestically-owned IP (procurement catalogs, 首台套
  qualification, subsidy audits). Splitting one IP estate across a parallel structure without
  contaminating either side (U.S. export-controlled tech → Chinese entity is an *export*;
  Chinese-subsidized IP → U.S. entity raises CFIUS/funding-agency questions) is the hardest
  operational problem of the parallel path.
- **Hiring:** in China, unrestricted access to top power-electronics and superconductivity
  engineers (ASIPP/USTC pipeline in Hefei). In the U.S., PRC-national hires interact with deemed
  exports (§1.5).

---

## 5. DECISION FRAMEWORK BY ARCHETYPE

> **RESEARCH, NOT LEGAL ADVICE — every row assumes founder is a U.S. person at founding; every
> "open" is "open as of 2026-07 and revocable"; every tripwire requires counsel.**

Legend: **CN** = China-first (Chinese entity, China market first) · **US** = US-first ·
**PAR** = parallel siblings. Ratings: ✅ legally workable today / ⚠️ workable with material
compliance engineering / ⛔ blocked or near-blocked.

| # | Archetype | CN | US | PAR | Binding tripwires |
|---|---|---|---|---|---|
| a | HTS coil-winding machines + magnet subsystems | ✅ | ✅ | ⚠️ | Not an OISP covered sector today — but COINS lets Treasury add sectors [P-03]. Machine likely EAR99; magnet subsystems can hit 3A001.e.3/3A201/1C005 [P-15]. CN: 首台套 + 攻关 status help [P-24][P-31]. PAR: winding know-how developed in the U.S. entity becomes controlled "technology" the moment any of it classifies above EAR99 — one shared design database can be a violation. |
| b | Precision magnet/scientific power converters (incl. sales to CAS fusion institutes) | ✅ | ✅ | ⚠️ | **3A225**: ≥600 Hz multiphase + <0.2% frequency control — precision magnet supplies can meet nuclear-controlled parameters; design-out (cap at 599 Hz where possible) or license [P-14][P-15]. US→CAS sales: Entity-List screening of each institute + Affiliates Rule ownership trees from Nov-2026 [P-06][P-07]. CN: government-procurement 20% preference effectively demands China manufacturing [P-32]. Not OISP-covered today. |
| c | HTS quench-protection hardware | ✅ | ✅ | ⚠️ | Cleanest superconducting archetype: protection electronics are not named in any ECCN reviewed; risk imports via bundling (with magnets → 3A001.e; with sub-4 K cryocoolers → 3A904 [P-10][P-11]) and via customers (listed institutes). Same PAR IP-wall problem as (a). |
| d | 800VDC data-center protection modules | ✅ | ✅ | ✅ | EAR99-class commercial product; no OISP sector. Best structural freedom of all archetypes. CN: domestic-preference + local price war; US: hyperscaler qual cycles. Watch only: Entity-Listed Chinese cloud/HPC customers, and COINS "high-performance computing" scope creep in the ~2027 regs [P-03]. |
| e | WBG semiconductor test/burn-in instruments sold into Chinese fabs | ⚠️ | ⛔→⚠️ | ⛔ | Hardest case. US-first selling into China: many target fabs are Entity-Listed (SMIC ecosystem, Fudan Micro Sep-2025) [P-16][P-17]; Affiliates Rule (Nov-2026) extends to their subsidiaries [P-06][P-07]. **§744.6**: a U.S. person may not "support" advanced-node Chinese fabs even with zero U.S.-origin content — his labor is the controlled item [P-42][P-43]. CN entity serving *legacy-node* fabs only: possible today (test gear is not front-end volume-fab SME on the prohibited list; whether it's OISP-notifiable depends on facts) — but the founder personally must stay out of advanced-node engagements, and node drift at the customer is his liability. If the instrument business ever *makes ICs* in China (incl. GaN ICs): **prohibited** [P-01]. Counsel before any move. |
| f | GPU-cluster power buffers | ✅ | ✅ | ⚠️ | Hardware itself EAR99-class; not AI "development" under OISP. Tripwires are customer-side: Entity-Listed Chinese AI/HPC operators (any-item license requirement), and COINS's new **supercomputing/HPC** category — powering a covered Chinese supercomputer project could be swept into the ~2027 regs [P-03][P-01]. Keep a customer-screening gate from day one. |
| g | Solid-state RF amplifiers for particle-therapy accelerators | ✅ | ✅ | ✅ | Medical end-use, typically below RF-power ECCN thresholds (verify per design; pulsed variants can approach 3A228/3A229 territory — counsel). Not OISP-covered. Real gates are regulatory-medical (NMPA type approval in CN; FDA/CE via the OEM in US/EU) and the 2026 domestic-procurement preference for Chinese hospital systems [P-32]. Rare two-market archetype where PAR is mostly a regulatory (not export-control) problem. |
| h | Satellite/downhole power electronics (ITAR/EAR-heavy) | ⛔ | ✅ | ⛔ | Space: USML Cat XV / 9x515 — China embargoed; 9E515 technology breadth makes any Chinese entity involvement untenable; foreign-person hiring restricted; CFIUS/FOCI kill China-linked cap tables for defense customers [P-19][P-20]. A founder with an active Chinese sibling company should expect disqualifying scrutiny. Downhole-only (non-space) variant is less controlled but shares customers with sanctioned energy projects — separate analysis. U.S.-only play. |
| i | Compact HTS magnets for instrument OEMs | ✅ | ✅ | ⚠️ | Classification pivot: 3A001.e.3 (with MRI-type exclusions) and 1C005 for conductor; sub-4 K coolers pull in 3A904 [P-10][P-15]. If marketed for **quantum sensing with military/intel applications**, OISP prohibited/notifiable categories activate [P-01][P-02]. CN: rides fusion/quantum future-industry demand [P-24]; US: fusion + NMR/analytical OEMs. REBCO/rare-earth supply favors CN manufacturing while the truce holds [P-36]. |

### Cross-cutting decision logic (neutral)

1. **Sector test first (OISP):** ICs (any), quantum-critical, supercomputing/HPC (post-COINS),
   advanced packaging, EDA, SME → China-first as a U.S. person is prohibited or
   notification-burdened [P-01][P-02][P-03]. None of (a)(b)(c)(d)(f)(g) hardware is covered
   *today*; all could be added by a Treasury designation with ~months of notice — build the
   corporate structure so a designation forces a divestiture, not a felony.
2. **Customer test second (Entity List/§744.6):** archetype economics that depend on
   Entity-Listed or advanced-node customers (e; parts of f) are structurally hostile to any
   U.S.-person involvement, whatever the corporate wrapper [P-16][P-17][P-42].
3. **Item test third (ECCN):** design products to sit below control parameters where physics
   allows (599 Hz converters; MRI-excluded magnet configurations; >4 K cryogenics) — this is a
   *product-requirements* decision to make in 2027–2028, before architectures freeze
   [P-14][P-15][P-10].
4. **Sequencing reality:** China-first maximizes demand-pull (FYP future-industry status, 首台套,
   20% procurement preference, fusion national team) at the cost of: OISP exposure now and at
   every future round, forfeiting U.S. federal R&D money (MFTRP/SBIR screens), and a cap on
   later U.S. expansion (CFIUS-shadowed exits) [P-24][P-31][P-32][P-39][P-40]. US-first maximizes
   optionality and defense/space adjacency at the cost of the 20% China procurement handicap and
   Chinese materials-control risk [P-32][P-36]. Parallel is legally available only for
   low-control archetypes (d, g; c with discipline) and requires two engineering organizations,
   two IP estates, and counsel-designed information walls from day one — assume ~1 FTE-equivalent
   of compliance overhead and slower everything.
5. **2029 planning baseline:** COINS implementing regs in force (~2027, broader sectors);
   Affiliates Rule active (Nov-2026); Chinese mineral controls truce expired or renewed
   (Nov-2026); 15th FYP mid-cycle with localization ratios published product-by-product. Re-run
   this entire analysis in 2028 — with counsel — before committing a structure.

---

*Prepared for Phase 5 of the startup-opportunity research mission. Sources P-01…P-43 in
`policy_sources.json`. This document is research synthesis only and is not legal, tax, or
investment advice.*
