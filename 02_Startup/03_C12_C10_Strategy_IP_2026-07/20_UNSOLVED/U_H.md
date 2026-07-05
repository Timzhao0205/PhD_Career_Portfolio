# U_H — Unsolved problems, segment CS-H (fast-control, coil-array drive, quench-protection electronics)

Schema: `U-id | lane | problem (<=30 words) | who suffers | evidence | severity 1-5 | why unsolved | small-team-exploitable | linked clusters`
Evidence ids resolve in 10_COMPETITORS/CS_H_sources.json. All refs fetched 2026-07-04 unless marked.

U-H-1 | C10 | No commercial catalog quench-detection instrument for HTS magnets exists; every program self-builds, bundles, or tenders bespoke units. | Fusion startups without protection staff (Startorus files own QD patents); labs (Fermilab 3-tier in-house QD; KIT UniQD institutional-only) | [CS-H-15][CS-H-22][CS-H-18][CS-H-16] | 4 | Incentive: magnet incumbents bundle QD free inside systems, starving a standalone instrument market | Y | P08

U-H-2 | C10 | No bipolar per-coil array-drive product with integrated protection: Thea powered its 9-coil HTS array with unipolar Magna-Power SL10-250 supplies plus mechanical relay H-bridges for polarity. | Coil-array stellarator builders (Thea Energy Canis/Eos); RMP/trim-coil upgrades | [CS-H-19][CS-H-14] | 4 | Economic: converter vendors have not seen array-scale channel counts; market younger than product cycles | Y | P09,P10

U-H-3 | C10 | Detection-to-dump chain is split across suppliers with no end-to-end latency owner; ITER QD alone spans 3,000 sensors and 20+ tenders (~EUR 25M) inside a 2-3 s budget. | Big-science programs (ITER IO Magnet Division); HTS test-stand operators buying converters, detectors, breakers separately | [CS-H-12][CS-H-09] | 4 | Incentive: program procurement fragments scope; no vendor accepts cross-domain trip liability | Y | P08,P10

U-H-4 | C10 | Protection-grade electronics go obsolete mid-machine-life: KSTAR rebuilt QD signal processing in-house on COTS FPGAs when commercial VME processors faced discontinuation; KFE+JH Engineering hand-built ITER HVSC conditioners. | National fusion labs (KFE/KSTAR; ITER QD chain) | [CS-H-04] | 3 | Technical/economic: 20-30 yr machine life vs ~5 yr COTS platform cycles; no vendor commits to lifetime support | Y | P08

U-H-5 | C10 | kA-class quench-dump switches are not products: ASIPP issued a tender for a "定型产品" (productized) 100 kA QPS main switch (2025-09) because no off-shelf unit exists. | CRAFT/BEST-class programs (ASIPP); Western HTS test stands needing multi-kA dump on <18-month timelines | [CS-H-13] | 4 | Economic: each program specs bespoke current/voltage/di-dt, so switchgear firms see no repeat volume worth productizing | Y | P10

U-H-6 | C12 | Winding-integrated fiber QD is stuck at research grade: interrogators (Luna ODiSI, HBK MXFS) have no trigger-rated ms-latency output or safety cert, and lead vendor Luna is in PE take-private at $1.39/share after delisting. | HTS coil builders adopting fiber QD (VIPER-lineage magnet teams, NHMFL-class labs) | [CS-H-10][CS-H-11] | 3 | Incentive: interrogator vendors chase aerospace/civil volume; magnet trip duty is low-volume, high-liability. Counts both ways: vendors SAY sensing is solved, yet no QD trigger product exists | Y | P08

U-H-7 | C10 | "Self-protecting NI coil" evidence holds only at kJ scale (Canis: 4.4 kJ/coil, passive safety claimed); multi-MJ NI/PI HTS systems have no purchasable active-protection path — TE's proven quench-safe methods are captive patents inside its magnet sales. | Second-wave fusion and lab builders of MJ-class NI/PI coils (Thea Eos scale-up; TE Demo4-class 16-magnet systems as the in-house benchmark) | [CS-H-19][CS-H-06][CS-H-07] | 4 | Technical: passive dissipation does not scale with stored energy; incentive: the one demonstrated solution is proprietary and not sold as electronics | Y | P08,P10

## Notes
- U-H-1 absence claim: EN sweep returned only research/in-house systems and bundled features [CS-H-22][CS-H-18][CS-H-16][CS-H-17]; zh sweep (失超检测 系统 产品) returned patent filings and MRI-integrated designs, no merchant product [CS-H-15]. Re-run both sweeps at Phase 5 before relying on absence.
- U-H-5 tender PDF is fetch-verified (title/buyer/date); the document body is access-restricted — switch-topology details (mechanical bypass + vacuum transfer per index snippet) are snippet-level, not load-bearing.
- U-H-2 links P10 secondarily: relay-commutated polarity switching is itself a protection hazard (arc/dead-time during array fault).
