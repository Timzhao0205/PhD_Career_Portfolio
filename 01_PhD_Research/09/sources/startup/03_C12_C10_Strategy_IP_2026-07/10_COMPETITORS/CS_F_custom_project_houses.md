# CS-F — Custom/Project Houses & Lab Self-Supply (verified 2026-07-04)

Charter: who serves magnet power above the catalog ceiling; what they refuse to productize; what CERN licenses out; which labs self-build. **Evidenced answer:** above ~10 kW every physics-grade purchase is project-quoted NRE on 1–13-year cycles; the one 2-week-lead-time player (Magna-Power) stops at <50 ppm/slow dynamics; CERN's licensable 4-quadrant folders (to 80 kW/1,800 A) show one evidenced licensee; CERN and ASIPP still design in-house.

---

## Card 1 — OCEM Power Electronics (Bologna, IT) — the reference custom house
- **Identity:** part of Cocchi Technologies (ex Aretè & Cocchi Technology, renamed 2026-02-11), 14 companies, 800+ staff; science power electronics "since 1943" [CS-F-01][CS-F-03].
- **Verified position:** references 10 A–16,000 A, 2 V–110 kV, 1–500 ppm (10 ppm common); LHC 13 kA; ITER gyrotron 60 kV/80 A; SPIDER/MITICA; JT-60SA framework services; ALBA 248 correctors [CS-F-02]. Marketing: 50 kA/5 ppm, 3,500+ converters, "hundreds" of hadron-therapy PSUs [CS-F-05, snippet]. Semi-catalog ceiling: NGPS digital series tops at **200 A/50 V (10 kW)**, <1 ppm/°C HS option, EPICS [CS-F-04].
- **Price signals:** €8M DTT fast-discharge/protection order; €5M JT-60SA/Rokkasho support; €5M ITER heating tranche of a €15.5M program "initiated 9 years prior" [CS-F-06]. DTT FDU executive design alone took 1 year [CS-F-03].
- **2024–26 moves:** US hub Franklin Park, IL (2024-05); group rename 2026-02; no product launches since on news feed [CS-F-03].
- **Patent posture (Phase-2 variants):** OCEM S.p.A.; OCEM Power Electronics; Energy Technology S.r.l. No zh name. Expect thin filings — know-how house.
- **Channel/lead time:** direct tenders; multi-year frameworks [CS-F-02][CS-F-06].
- **Weaknesses (evidence):** product line stops at 10 kW [CS-F-04]; all else year-scale project cycles [CS-F-03][CS-F-06]; no published lead time or price.

## Card 2 — Ampegon Power Electronics (Baden, CH) — Cocchi's HV/RF sibling
- **Identity:** Ampegon AG assets bought by Energy Technology Srl (Cocchi) 2019-07 [CS-F-06 context].
- **Verified position:** HVPS for gyrotrons/klystrons/NBI (marketed to 320 kV/10 MW CW, snippet); first European ITER EC HVPS handed over **2026-03-02 after working with F4E since 2013 — 13 years** [CS-F-07].
- **2024–26 moves:** only power-electronics member among 30+ firms of Proxima Fusion's Alpha Alliance (2026-02-25) [CS-F-08].
- **Patent posture:** Ampegon Power Electronics AG; Ampegon AG; Thomcast legacy. No zh name.
- **Weaknesses (evidence):** decade-class flagship delivery [CS-F-07]; no DC magnet-converter line — the fusion DC layer is not its business [CS-F-08].

## Card 3 — Jema Energy (Lasarte-Oria, ES; Grupo Irizar) — veteran drifting to e-mobility
- **Identity:** Irizar Group since 2009; 70 years in 2023 [CS-F-09][CS-F-10].
- **Verified position:** "customized power conversion systems for particle accelerators and nuclear fusion devices" — coil HCPS, NBI HVPS, precision magnet PS; references TAE C-2W, JT-60SA, ESS, HL-LHC, ALBA [CS-F-09].
- **2024–26 moves / price signals:** news feed 2022–26 dominated by bus charging (1,000 charge points; megawatt MCS); zero new big-science awards announced [CS-F-10].
- **Patent posture:** Jema Energy, S.A.; JEMA ENERGY SA; Grupo Irizar. No zh name.
- **Channel/lead time:** project tenders (F4E/labs); no lead-time claims.
- **Weaknesses (evidence):** attention visibly shifted to EV charging [CS-F-10]; custom-only, no catalog, no published specs/prices [CS-F-09].

## Card 4 — JEMA (CE+T Group, BE/FR) — the other JEMA; absorbed Sigmaphi Electronics
- **Identity:** JEMA SA (Belgium, DC supplies since 1937), CE+T Group; acquired Sigmaphi Electronics (Haguenau, 25 staff) 2021-03 → JEMA France; combined turnover target only **€10M for 2022** [CS-F-11].
- **Verified position:** envelopes 1 kW–3 MW+, 0.1 A–30 kA+, 0.5 V–100 kV+, stability "down to 10⁻⁵", 4-quadrant, SC supplies with quench detection/energy management [CS-F-13]. FRIB: **450+ supplies over ~7 years**, 4Q 6 V units 20–1,250 A, 20 ppm dipole class [CS-F-12]. RAL "Septum One Dipole" 9,500 A/50 V redundant modular one-off (LinkedIn-level, Q1-2024 — discovery only).
- **Patent posture:** JEMA SA; JEMA France SAS; Sigmaphi Electronics SAS; CE+T Power. No zh name.
- **Channel/lead time:** project quotes; FRIB shows multi-year campaign rhythm [CS-F-12].
- **Weaknesses (evidence):** micro revenue base (€10M ambition) [CS-F-11]; 20 ppm class, not fast-dynamics telemetry-rich product; no catalog/lead time.

## Card 5 — Magna-Power Electronics (Flemington, NJ) — the productized counterexample
- **Identity:** founded 1981; 115 employees; vertically integrated; 50,000+ units shipped [CS-F-14].
- **Verified position:** catalog DC 1.5 kW–10 MW+; 2025: TSD8 **0–8 V / up to 10,000 A (80 kW, 16U)** aimed at "high-power superconducting magnets"; ML to 3 MW; SLx 1U [CS-F-15][CS-F-25]. Superconductor page: tokamak field coils, 54 kA paralleled system, DBx **<50 ppm** with fluxgate DCCT [CS-F-16].
- **Price signals / lead time:** "industry-leading standard **2-week lead-time**," made-to-order [CS-F-14].
- **Patent posture:** Magna-Power Electronics, Inc. Trade-secret manufacturing posture. No zh name.
- **Weaknesses (evidence):** <50 ppm only with DCCT option [CS-F-16]; current-fed heritage = slow dynamics; no EPICS/telemetry story in the 2025 recap [CS-F-25] — 2-week logistics proven, but not at physics-grade spec.

## Card 6 — EEI, Equipaggiamenti Elettronici Industriali (Vicenza, IT) — DISCOVERED custom specialist
- **Verified position:** DMPS/CMPS/SMPS/RMPS magnet PS; custom to **20 kA / 3 MW, ripple <5 ppm, repeatability ±2.5 ppm**; hadron-therapy scanning supplies, full excursions "in 30 µs" [CS-F-22].
- **Posture:** integrates customer-designed control boards — bespoke by design [CS-F-22].
- **Patent posture:** E.E.I. S.p.A.; Equipaggiamenti Elettronici Industriali. No zh name.
- **Weaknesses:** custom-only economics; no published lead times/prices; scanning IP locked in one-offs [CS-F-22].

## Card 7 — iTest (FR) — DISCOVERED precision-module house with a hard ceiling
- **Verified position:** 3,000+ modules deployed; BE28xx bipolar modules **±6 A/20 V, ±15 A/15 V**, 4-ch ±1.5 A; "ultra-stable and drift-free performance without requiring DCCT"; 14 modules per 19″ chassis; TANGO/EPICS; MTBF >1M h [CS-F-21].
- **Patent posture:** ITEST; iTest SAS. No zh name.
- **Weaknesses (evidence):** ±15 A ceiling — corrector class only; merchant precision thins out exactly above tens of amps [CS-F-21].

## Card 8 — CERN design-licensing + lab self-supply (the non-market that could arm an entrant)
- **The folders:** CERN KT lists two licensable families with "complete manufacturing folders… available for production": 4Q CUTE (±12.5 A) → MACAO (500 W) → CANCUN (1.5 kW) → COMET (30–120 kW, 250–1,000 A) → SIRIUS (20–80 kW pulsed, 450–1,800 A, energy recovery); short-pulse to 3,000 A/12 ms; FGC controls, EPICS/TANGO [CS-F-17].
- **Licensee evidence:** exactly one — "a Spanish firm… licensed the Sirius design for production for other laboratories" (CERN Courier 2021-12); SIRIUS: 10 ppm, 13 kHz switching, 95% energy cut vs 1960s plant [CS-F-18]. CERN KT signed 23 licenses across ALL domains in 2023; none named for converters [CS-F-20].
- **Self-supply evidence:** CERN MPC designs standardized families (APOLO…SIRIUS, SYRACUSE) in-house; industry builds to print [CS-F-19][CS-F-26]. ASIPP/CRAFT: "complete domestication of the full chain" — 100 kA HTS current leads self-developed, tested 2025-07 (zh) [CS-F-23]. Fermilab field-ran 100+ Transrex 500 kW SCR supplies upgraded in-house (1991 report; fleets of this vintage persist at US labs) [CS-F-24].
- **Read:** the license channel is real, cheap credibility — COMET/SIRIUS is exactly the 20–80 kW 4Q class — and almost unused.

---

## Segment structure
**Power×precision axis:** below ~1 kW/±15 A merchant modules exist (iTest; CAENels in CS-E). From ~10 kW (OCEM's NGPS ceiling [CS-F-04]) to MW, physics-grade purchases become engineered NRE: OCEM, EEI, both JEMAs and Ampegon sell projects, not products — zero published prices or lead times. **Lead-time axis:** Magna-Power proves 2-week made-to-order logistics at 10 kA scale [CS-F-14][CS-F-15], but only at industrial spec. Nobody combines Magna-Power's clock with OCEM/EEI's ppm-and-dynamics spec — that empty cell is where a weeks-lead-time product bites. **What they refuse to productize:** (a) 4Q fast-dynamics 5–100 kW converters — CERN had to design SIRIUS/COMET itself and now offers the folders [CS-F-17]; (b) PS-integrated quench/dump — DTT FDU sold as €8M bespoke [CS-F-06], JEMA embeds energy management only inside campaigns [CS-F-12]; (c) fleet telemetry/orchestration software. **Structural signals:** consolidation (Cocchi = OCEM+Ampegon; CE+T = JEMA+Sigmaphi) plus attention drift (Jema Energy → EV charging [CS-F-10]) are shrinking Western merchant capacity as fusion demand arrives — Alpha Alliance's 30+ members include one power-electronics firm, an HV/RF house [CS-F-08]; the fast-DC magnet layer has no industrial home. Self-suppliers (CERN, ASIPP; Bruker builds its own NMR-magnet PSUs; US labs nurse Transrex-era fleets) absorb demand merchants never see. CERN's near-unused manufacturing-folder license is the documented on-ramp for a product entrant [CS-F-17][CS-F-18]. China note: domestic custom houses (爱科赛博/荣信汇科-class) are CS-G; no CN vendor appeared in the Western PS evidence fetched here.
