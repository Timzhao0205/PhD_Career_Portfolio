# BASELINE — Phase-0 corpus extract (Round 3, written 2026-07-04)

Corpus check: 00_PRIOR_CORPUS complete — DD_C12/C10/C11/C33 (+sources.json), 00_FINAL_SHOWDOWN.md, POLICY_DELTA.md, INCUMBENTS.md, 01_ROADMAP_IMPLICATIONS.md. No missing files.

## A. C12 cluster thesis (83.6, primary; incl. C33 QC module + recipe software)
- Product: turnkey NI/MI coil production cell — laser-aligned winding head (±0.1 N-class tension), inline QC (during-winding turn-to-turn Rc estimation, tape-defect-map-aware feed), joint station with in-situ nΩ verification, recipe/traceability software subscription. Output spec: "coil with predicted Rc ±20% and logged joint resistance."
- Why now: NI/MI is the record-magnet architecture (NHMFL 45.5 T; ASIPP 24.1 T); for NI coils the tension recipe IS the electromagnetic design (tension→Rc, MIT ~71 μΩ·cm²); Tokamak Energy bought Ridgway 2025-09 → no vendor-neutral HTS/NI-native winding-equipment specialist left in the West.
- Honest size: 35–70 machines 2027–2031 ex-China; machines SAM $7–13M/yr, $9–17M/yr with attach; venture-scale only via software/QC attach + coil-foundry expansion ($20–60M/yr family ceiling).
- Buyers: second-wave fusion (10–16 orgs), labs/universities (NHMFL/KIT/CERN-class), industrial HTS producers (induction, motors, NMR/MRI). Non-buyers (integrated): CFS, TE/Ridgway, Proxima, Energy Singularity, Thea.
- China = fast-follower threat + component supply + intelligence, NOT market. Kill gates frozen: 3 paid commitments by mid-2030; mid-2027 interview gate; software+QC ≥15% of revenue by end-2031.

## B. C10 thesis (76.8, second; absorbs C11 protection line)
- Product: "FastCoil" bipolar 4-quadrant SiC rack converter, 5–50 kW/module, ±(50–1000) A, ≤10 ppm/8 h with DCCT option, ≥2 kHz loop, 100 kHz Ethernet telemetry, N+1 paralleling to multi-kA; magnet test-stand systems (1–10 kA/≤50 V) with quench-safe dump (C11 MPMU absorbed); fleet/orchestration software.
- Edge: ppm lives in the DCCT/ADC chain, not the switch; WBG buys control bandwidth + 2–4× density (10× retired). Hole verified: CAENels catalog stops ~900 W/100 A; above that only custom-quote houses (OCEM/Danfysik/Jema) on 12–18-month cycles.
- Demand: power systems = #1 FIA-surveyed fusion bottleneck (48%); supply-chain spend $538M(2025)→$681M(2026E); coil-array architectures (Thea Canis ±140 A/coil) convert magnet complexity into converter count; ALS-U-class ring upgrades ≈1,200 supplies.
- Size: beachhead SAM $15–25M/yr; SOM $1.5–4M by 2031–32; expansion = magnet-power packages, ring upgrades, protection attach.
- China: tenders captured domestically (爱科赛博 BEST fast-control + HL-3 RMP 2025-12; 荣信汇科 ITER ELM-PS 2026-01; 英杰电气; 新风光 BEST ¥108M) — quarterly-intel radar + component cost base only. Kill gate: end-2027 WTP-for-lead-time/dynamics.

## C. Known competitor set per segment (Phase-1 seeds; from DD §4)
- CS-A: Broomfield (LTS-framed winders), Ridgway (TE-owned), Supertek/BOW (HTS cable machines); KIT robot-cell self-build (2025-12); CAS winding-line patents (US11581133B2 — re-fetch before citing).
- CS-B: 联创超导 (27→~81 induction units/yr), 健信超导 (600/yr He-free MRI line; 干式绕线 core IP), 上海超导 (tape QC/rewind adjacency; 4,000→15,000 km/yr), CAS HFIPS 招标 channel, 能量奇点.
- CS-C: CFS (coils-as-product; WHAM 17 T, Realta, Type One), TE Magnetics/Ridgway, Proxima (in-house cable line 2025-09), Thea (planar-coil factory), Energy Singularity (in-house 绕制/浸渍; HH70 >96% localized).
- CS-D: THEVA TapeStar (tape-level standard), Lake Shore/Senis-class (components, not stations), BNL-style in-house 77 K dunk tests, MIT/CFS VIPER fiber lineage, ASIPP fiber QD, Startorus own filings. Coil-level inline QC vendor: none found in Rounds 1–2 (absence to re-verify).
- CS-E: CAENels FAST-PS(-M) 30–100 A/600–900 W/50 ppm; Danfysik S9700 10 ppm, 0.75–100 kW; Heinzinger/Delta/iseg/Matsusada/TDK-Lambda envelopes TBD; Kepco BOP wind-down to verify + who captured bipolar-lab niche.
- CS-F: OCEM (50 kA/5 ppm custom, hadron therapy), Jema (ITER/MAST-U), Magna-Power (10 kA catalog, <50 ppm DCCT option, SCR dynamics), CERN design-licensing (4Q 80 kW/1,800 A folders).
- CS-G: 爱科赛博 (688719), 荣信汇科 (STAR IPO attempt #2), 英杰电气 (300820), 新风光; BEST/CRAFT/HL-3/EAST tender sweeps; ¥17.6B BEST-ecosystem tenders Q1–Q3 2025.
- CS-H: TE protection patents (US11749434B2 inter-coil comparison; US11101059B2 striated-tape dump — re-fetch), ASIPP 100 kA QPS + 2025-09 productized-switch tender, Mitsubishi/Scibreak VARC, Oxford Sigma/STEP valve (2026-02), Cryomagnetics bundles QD free, 南京工程学院 CN111541222A (re-fetch), D-TACQ/PXI-FPGA vendors TBD.

## D. Unsolved-problem hypotheses carried in (to be evidenced as U-###)
Rc unpredictability during winding; production joint yield at nΩ + in-process verification; km-tape handling without Ic degradation; defect-map-synchronized feed; no coil-level QC instrument ("TapeStar for coils"); NI charging-delay/screening-current management; catalog-vs-custom gap in fast precision converters (lead-time pain); coil-array orchestration; HTS quench-detection latency (voltage taps ineffective); He-free MRI quench management as electronics; power systems as #1 fusion bottleneck with no demand visibility for suppliers; test-stand + dump integration.

## E. 2026–2028 validation experiments the strategies must arm (Rule 6 re-sequencing applies)
1. ASC-2026/MT-29 build-vs-buy interviews (~$3K; ≥3 written "would buy at $500–800K"; C33 ask ≥$150K). 2. Tabletop NI benchmark rig <$15K, inline Rc estimation → SUST/IEEE TAS **(file first)**. 3. Recipe/QC software paid pilot $10–25K. 4. SiC ppm-converter benchmark <$40K vs JINST 0.9 ppm design → publication **(file first)**. 5. C10 WTP/LOI probe (premium for 12-week delivery). 6. C11 detection-latency benchmark $15–25K (taps+Hall+fiber, 77 K) → publication **(file first)**. 7. WHAM/HSX-adjacent reference converter deployment <$15K. 8. Quarterly CS-G tender forensics ($0, template deliverable). 9. C33 77 K seeded-defect demo <$12K → ROC publication **(file first)**. HSX GaN Hall letter = already-submitted prior art for adjacent claims.
