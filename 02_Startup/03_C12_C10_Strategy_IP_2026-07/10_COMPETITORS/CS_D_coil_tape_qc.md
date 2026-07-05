# CS-D — Coil/Tape QC & Instrumentation (C33 space)

Analyst: competitor-analyst CS-D · Date: 2026-07-04 · Sources: `CS_D_sources.json` [CS-D-01..20]
Mandate answer up front: **nobody sells inline (during-winding) coil QC today** — absence documented in §Structure with the searches run and where the nearest offerings stop.

## Card 1 — THEVA Dünnschichttechnik GmbH (DE): the tape-level standard

- **Identity:** private GmbH, Ismaning; tape producer + instrument line. Patent-posture variants: "THEVA Dünnschichttechnik GmbH", "THEVA Duennschichttechnik".
- **Product:** TAPESTAR (lab) / TAPESTAR XL (production): non-contact reel-to-reel Ic scan, mm resolution, works on 1G/2G incl. laminated/insulated tape (7-Hall-sensor array, 77 K, 8–10 mT). 2024 variants: **XL-HF** (Ic mapping under fields to 1 T at 77 K), **XL-W** (widths to 40 mm), inkjet defect-marking option [CS-D-01].
- **Price signal:** quote-only; no public list found (also no public tender price located).
- **2024–26 moves:** XL-HF/XL-W launches; Pro-Line tape "+70% current capacity"; custom coils to 1.4 m OD with a partner (EcoSwing lineage) [CS-D-01].
- **Channel:** direct + regional distributors (Quantum Design Singapore-class).
- **Weakness (evidence):** product page shows nothing above tape level — no wound-coil, joint, or during-winding instrument; "all well-known tape producers rely on this method" is a tape claim [CS-D-01]. Even XL-HF answers a tape question (in-field Ic), not a coil question (Rc, joints).

## Card 2 — Tape majors bundling QC data with tape (Faraday Factory Japan · Fujikura · SuperPower/Furukawa)

- **What they sell:** QC **data**, not instruments. Faraday: LN2 Ic on every tape + machine vision + thickness; 5,000 km (1 GA·m) cumulative to fusion by 2024-09; customers CFS, Thea, Proxima, OpenStar [CS-D-08]. Fujikura: FYSC/FESC lines, Ic ≥165 A (4 mm) / ≥250 A (12 mm) 77 K s.f., "Highly uniform critical current", no degradation to 400 MPa [CS-D-09]; MT-29 (2025-07) slides show σ(Ic)=1.3 A on a 1,400 m AP tape. SuperPower: 2–12 mm widths, piece lengths 200–500 m (>900 m), Ic classes 80–160 A/4 mm; spec page publishes **no QC protocol** [CS-D-07].
- **Patent posture:** "Faraday Factory Japan LLC" (legacy "SuperOx Japan LLC"); "Fujikura Ltd." / 株式会社フジクラ / 藤仓; "SuperPower Inc." + "Furukawa Electric Co., Ltd." / 古河电气. Phase-2 lead: 2025 US grant titled "Method for production quality control of flexible superconducting tapes" surfaced in search — scout to fetch and attribute.
- **Weakness (evidence):** warranty and data end at the spool. No vendor sells coil-level qualification or warrants wound-coil performance; Faraday's release quantifies km shipped, silent on anything post-spool [CS-D-08].

## Card 3 — 上海超导 Shanghai Superconductor Technology (CN)

- **Identity:** 上海超导科技股份有限公司; STAR-board IPO accepted 2025-06-18, raising ¥1.2B (CICC sponsor); revenue ¥239.5M 2024 (+187% YoY), net profit ¥72.95M; >80% domestic 2G-tape share 2022–24 [CS-D-15]. In IPO inquiry stage since 2025-07.
- **QC-adjacent services sold (zh services page):** 定制超高性能带材 (to 3,800 A/mm² at 4.2 K/12 T), 激光精密分切 (laser slitting), 铜银合金封装 (Cu-Ag encapsulation) — full-flow tech support "从方案设计到产品交付" [CS-D-06]. EN site additionally lists a "2G-HTS Coil Winding" technical service (title-level evidence only) [CS-D-20].
- **Patent posture:** 上海超导科技股份有限公司; "Shanghai Superconductor Technology Co., Ltd."; co-filings with 上海交通大学.
- **Weakness (evidence):** the services page contains **no testing/inspection service and no instrument SKU** — QC stays internal; the winding service makes coils, it does not certify them [CS-D-06]. For a C12 cell buyer, SSTC is a data-source partner (tape Ic maps), not a QC competitor — unless the IPO war chest funds forward integration.

## Card 4 — HTS-110 / Robinson Research Institute (NZ): sample-level Ic metrology

- **Identity:** HTS-110 Ltd (Scott Technology group), Lower Hutt; systems built with Robinson (Victoria Univ. Wellington). Posture variants: "HTS-110", "Scott Technology Ltd", "Victoria Link Ltd", "Wellington UniVentures".
- **Product:** SuperCurrent cryogen-free transport-Ic systems: 5/8/12 T split-pair (20 T option in development), samples to 15 K, >1,600 A, 0–360° field angle; powers the public Robinson wire database; "built, installed, serviced to order" [CS-D-02].
- **Price signal:** quote-only; institutional one-off builds.
- **Weakness (evidence):** short-sample wires/tapes only — no coil fixture on the product page [CS-D-02]; full (B,T,θ) characterization takes up to ~24 h/sample (throughput ceiling for production QC). Owns the "tape truth" layer, blind one level up.

## Card 5 — Components bench: Lake Shore · Senis · Metrolab/GMW · AREPOC

- **Lake Shore Cryotronics, Inc. (US):** cryogenic Hall probes, teslameters, temperature instrumentation. **Acquired by DwyerOmega (Arcline PE) 2026-06-10**, rationale naming fusion among end markets [CS-D-04]; 2025: Infinite Helium (R&D 100), Model 346 controller preview.
- **Senis AG (CH):** MMS mappers: MMS-1X-RS scans 570×570×390 mm, 50 mT–2 T ranges, 0.1% accuracy, ±5 µm positioning — room-temperature magnet mapping; no cryo option on spec page; quote-only [CS-D-03].
- **Metrolab Technology SA (CH), via GMW:** THM1176-MF 3-axis Hall to 3 T (family "nT to 20 T"), 1% accuracy — **list $7,210** (LF $5,990; TFM1186 $9,080); marketed for MRI QC/5-gauss mapping, no cryogenic capability stated [CS-D-18].
- **AREPOC s.r.o. (SK):** cryogenic Hall probes to 30 T; catalog price-list distribution only.
- **Weakness (evidence):** everything is a probe, meter, or room-temp mapper — no vendor packages a 77 K coil-QC station [CS-D-03][CS-D-18]. PE roll-up of Lake Shore adds portfolio-focus risk just as fusion demand arrives [CS-D-04].

## Card 6 — Fiber-optic sensing: Luna Innovations · FBGS

- **Luna Innovations Inc. (US):** ODiSI 6000 (0.65 mm gage to 20 m, ±15,000 µε, up to 8 ch) — **discontinued, replaced by ODiSI 7100** [CS-D-13]. Corporate: delisted from Nasdaq 2025-02-06, OTC Expert Market, then **take-private by TJC at $1.39/share announced 2026-06** (close 2H-2026) [CS-D-05]. Posture: "Luna Innovations Incorporated" (+ subsidiaries "Silixa Ltd", "LIOS Sensing").
- **FBGS (DE/BE):** draw-tower gratings (DTG), AGF, femtosecond gratings, interrogators; eight listed markets — superconductivity/cryogenics absent [CS-D-17]. Posture: "FBGS Technologies GmbH", "FBGS International NV".
- **Usage evidence:** LBNL wired DFOS into a subscale CCT HTS dipole itself (SUST 38:035029, 2025), stating "traditional instrumentation, such as voltage taps and strain gauges, has become inadequate" [CS-D-14].
- **Weakness (evidence):** interrogators are general-purpose; cryo calibration, coil integration, and analytics are all customer DIY [CS-D-14][CS-D-17]; flagship vendor spent 2024–26 in delisting/PE limbo — continuity risk for anyone standardizing on ODiSI [CS-D-05][CS-D-13].

## Card 7 — 北京原力辰超导技术有限公司 (Eastforce, CN): the China instrument niche

- **Identity:** Beijing (Haidian) private firm, founded 2014; brand 原力超导; site eastfs.com. Posture: 北京原力辰超导技术有限公司; "Beijing Yuanli Chen / Eastforce Superconducting Technology".
- **Products:** **MCorder** (superconductor/magnetic-material performance monitor — tape/strip defect detection, 带材质量检测), **MCorder2D** (2D/3D magnetic-field scanning platform), **MagT** (RT–77 K phase-transition tester), Tesla-Shielding (40–60 dB, 0.01–1,000 Hz) + EM simulation/consulting [CS-D-11].
- **Weakness (evidence):** material/tape-level and field-scanning only; no coil-level or winding-line product in the exhibited portfolio [CS-D-11]; small-company channel (expo listings, no price/tender trail found).

## Segment structure — tape-level solved, coil-level empty

**Solved axes and their owners.** Tape Ic mapping: THEVA (instrument) + producer-bundled data (Faraday/Fujikura/SuperPower/SSTC) [CS-D-01,07,08,09]. Short-sample (B,T,θ) truth: HTS-110/Robinson [CS-D-02]. Sensor components: Lake Shore/Senis/Metrolab/AREPOC/Luna/FBGS — a commodity bench being consolidated by PE (two flagship deals in June 2026) [CS-D-04][CS-D-05].

**Empty axis 1 — post-wind coil QC station.** No vendor sells a "TapeStar for coils." Cryogenic Ltd tests only its own magnets pre-delivery [CS-D-16]; labs self-build: Fermilab's Mu2e quench-detection/monitoring stack [CS-D-19], LBNL's DIY fiber diagnostics [CS-D-14], HFIPS's in-house insert qualification [CS-D-12]. Chinese-language sweep matches Round 2: 带材检测 instruments exist (MCorder), 线圈级 do not [CS-D-11].

**Empty axis 2 — inline during-winding QC (the mandate).** Searches run 2026-07-04: EN "inline quality control HTS coil winding", "during-winding Ic monitoring REBCO winding machine"; ZH "超导线圈 绕制 在线监测", "超导带材 临界电流测试系统 中标". Nearest hits: (a) conventional-wire inline HV-insulation/continuity testers (DSE Test Solutions — pinholes/cracks in enameled wire, not REBCO) [CS-D-10]; (b) winding-machine tension-control marketing; (c) HFIPS's self-built 激光动态跟随 (laser dynamic-following) winding monitor on its 44.86 T NI insert — research craft incl. 65 nΩ·cm² joints, not a product [CS-D-12]. **No commercial during-winding QC offering exists in EN or ZH.**

**Who could package a coil-QC station fastest:** THEVA (Hall-array reel scanner + LN2 practice + coil partner — ~2–3 quarters if it chose); Senis/GMW (mapper + probes, needs cryo fixture); HTS-110/Robinson (cryostat + kA current + probes, needs coil fixture and throughput); CN: 原力辰 (MCorder2D scanner + 77 K MagT chassis). Hardware entry is low-barrier; what none of them owns is the NI-coil interpretation layer — Rc/joint parametric models and golden-signature fleets (P04) — which is where C12's QC module should anchor.
