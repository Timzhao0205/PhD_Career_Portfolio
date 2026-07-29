# CS-H — Fast-control, coil-array drive & quench-protection electronics (C11 absorber space)

Segment question (load-bearing): who could bundle converters + protection + detection into one offer before 2029, and does ANY commercial catalog quench-detection (QD) product for HTS magnets exist? Answer to the second: **no — verified absence** (EN + zh sweeps, 2026-07-04): only in-house lab systems [CS-H-22][CS-H-18], QD bundled free inside magnet/supply products [CS-H-16][CS-H-17], general-purpose interrogators [CS-H-10][CS-H-11], and tenders for bespoke units [CS-H-13]. Fusion startup Startorus is filing its own QD patents rather than buying [CS-H-15].

---

## Card 1 — D-TACQ Solutions Ltd (Blantyre, Scotland; private micro-firm)
**Product:** "Intelligent DAQ appliances": ACQ2106/ACQ2206 carriers (ACQ2206: up to 192 simultaneous ch in 1U, Zynq-7030 SoC, Linux+EPICS IOC on board, White Rabbit sync, 10 Gb/s streaming, 2 GB/s to 16 GB buffer) [CS-H-02]; CPCI/FMC/MTCA.4 module families [CS-H-01]. De-facto standard front end for fusion diagnostics/control loops; its ACQ196CPCI cards sit inside third-party PXI plasma-diagnostic builds (COMPASS) [CS-H-03].
**2024-26 moves:** ACQ2206 refresh (serial links 6→10 Gb/s, White Rabbit clusters) [CS-H-02].
**Price signals:** none published — quotation-only; no lead-time commitments visible [CS-H-01][CS-H-02].
**Patenting posture (record for P2):** assignee "D-TACQ Solutions Ltd"; no zh variant; posture = trade-secret firmware, patents unlikely.
**Channel:** direct + EU distributor (Acquitek).
**Weakness:** digitize-and-stream only — no actuation, no protection logic product, no functional-safety rating; customers write their own quench/interlock firmware on its Zynq. Micro-company key-person risk.

## Card 2 — NI (Emerson) PXI/cRIO platform + integrator ecosystem
**Identity:** National Instruments, Emerson-owned since 2023; PXI/PXIe, LabVIEW/FPGA.
**Product:** modular platform, published per-module list pricing; fusion labs assemble their own systems (COMPASS Thomson scattering: PXI-5152 digitizers + PXI-6653 timing, <300 ps skew, built in-house by IPP Prague with integrator Elcom) [CS-H-03]. Thea's Canis array control also rode NI real-time Linux + user-programmed FPGA [CS-H-19].
**2024-26 moves:** platform continuity under Emerson; no fusion/magnet vertical product surfaced in searches (absence).
**Price signals:** catalog modules $k-class; integration labor dominates (labs self-build) [CS-H-03].
**Patenting posture:** "National Instruments Corporation"; "NI"; "Emerson Electric Co."; zh 恩艾(中国)/美国国家仪器, 艾默生电气. Heavy generic T&M portfolio; nothing magnet-protection-specific claimed.
**Weakness (customer-side evidence):** platform ≠ solution — KSTAR had to develop an in-house FPGA "Backup Signal-processing System" when its commercial VME QD processors faced discontinuance [CS-H-04]; every validation burden stays with the lab.

## Card 3 — General Atomics PCS lineage (+ open MARTe2 world)
**Identity:** GA Energy Group, San Diego; DIII-D operator.
**Product:** DIII-D Plasma Control System — "most widely used in the world, presently operating eight fusion experiments" incl. EAST, KSTAR, NSTX, MAST, Pegasus/MST, KTX [CS-H-05]. Delivered via lab-to-lab agreements/"design resources", not a catalog product.
**2024-26 moves:** PCS2MDS data-modernization with PPPL/MIT (year 2 in 2025; 849 GB archived 2025); ML-based control demos [CS-H-05].
**Price signals:** none public; collaboration-priced.
**Patenting posture:** "General Atomics"; zh 通用原子. Control software largely unpatented/lab-licensed.
**Weakness:** services model, government-lab cadence; no power/protection hardware bundle; private fusion firms (CFS, TE, Thea) conspicuously build their own stacks instead of buying PCS [CS-H-19].

## Card 4 — Tokamak Energy / TE Magnetics (Oxfordshire; VC + Furukawa strategic)
**Product:** quench-safe HTS magnets sold as systems, not electronics: "even if quench does occur… energy is dissipated uniformly, leaving the magnet undamaged" [CS-H-07]. Demo4: 16-magnet HTS tokamak set, 11.8 T at ~30 K, deliberate ramp-to-quench with no degradation (2025-11) [CS-H-06].
**2024-26 moves:** TE Magnetics commercial division launched 2024; Ridgway Machines acquired 2025-09 (UK manufacturing scale-up); GA partnership (MHD pump); DOE FIRE/INFUSE links [CS-H-06].
**Price signals:** none public; magnet-system quotes.
**Patenting posture (public statements only, per charter):** claims "200+ granted patents" with categories explicitly including "Quench management" and "Quench detection" [CS-H-07]. Assignee variants: "Tokamak Energy Ltd", "Tokamak Energy Limited"; zh 托卡马克能源.
**Weakness:** protection is captive inside the magnet sale — TE does not sell detection/protection electronics to third-party coil builders; buyers who wind their own coils get nothing from TE, and TE's patent wall deters imitation rather than serving demand [CS-H-07].

## Card 5 — Dawonsys Co., Ltd. (KR, KOSDAQ 068240) — closest existing bundler
**Product:** fusion/accelerator magnet power systems: ITER TF/CS/VS/CC AC/DC converters incl. master controllers, dummy load, spares — one scope covering design→commissioning [CS-H-08]; KSTAR magnet + heating power heritage.
**2024-26 moves:** 2025-06-19 task agreement: six more CS AC/DC converter units **plus master-control upgrade integrating stage-1/stage-2** — design, prototyping, manufacturing, integrated testing, on-site commissioning [CS-H-09].
**Price signals:** program-priced; contract values undisclosed [CS-H-09].
**Patenting posture:** "Dawonsys Co., Ltd." (다원시스); zh renders 大元系统/다원시스 rarely — search both.
**Channel:** domestic-agency-mediated big science; no catalog, multi-year cycles.
**Weakness:** thyristor-era architectures, no HTS-specific detection capability shown; wins ride Korean in-kind procurement, unproven in commercial fusion accounts.

## Card 6 — Detection instrument layer: Luna Innovations, HBK FiberSensing, JH Engineering
**Luna (Roanoke, VA):** ODiSI Rayleigh interrogators are the research default for HTS fiber sensing, but corporate state is distress: Nasdaq delisting 2025-02-06, no SEC reports since, take-private by TJC at $1.39/share (~$45.8M) announced 2026-06, closing 2H2026 [CS-H-10].
**HBK FiberSensing (Porto; Hottinger Brüel & Kjær):** catalog FBG sensors + interrogators (QuantumX MXFS); no magnet/quench application productized on current pages (absence) [CS-H-11].
**JH Engineering (KR):** with KFE built high-voltage signal conditioners for ITER QD, reliability-tested through the 2024-25 KSTAR campaign — component maker inside programs, not a merchant vendor [CS-H-04].
**Patenting posture:** "Luna Innovations Incorporated"; "Hottinger Brüel & Kjær"/"HBK FiberSensing S.A." (ex-HBM); "JH Engineering" (KR).
**Weakness:** interrogators are lab instruments — no trigger-rated ms-latency QD output, no safety certification, and the category leader is now PE-owned mid-restructuring [CS-H-10].

## Card 7 — Interruption/diversion specialists: Mitsubishi-Scibreak; Oxford Sigma consortium
**Scibreak AB (Stockholm, wholly Mitsubishi Electric):** VARC DC breakers — VSC-excited LC oscillation, semiconductors conduct ~0.5 ms, ≥1 ms contact separation; aimed at "power transmission grids"/Supergrid, no magnet product [CS-H-21].
**Oxford Sigma + STEP Fusion + Rockwood Cryogenics + Atled Engineering:** demonstrated magnet-protection "safety valve" redirecting/dispersing stored quench energy; tested at U. Strathclyde, announced 2026-02-02 for STEP (West Burton, 2040) [CS-H-20].
**Patenting posture:** "Mitsubishi Electric Corporation" 三菱电机/三菱電機; "Scibreak AB"; "Oxford Sigma Ltd".
**Weakness:** actuation layer only; neither sells detection or converter integration; STEP valve is a national-program demo, a decade from product [CS-H-20][CS-H-21].

## Card 8 — China ecosystem (zh): ASIPP + Actionpower + Startorus
**ASIPP (中国科学院等离子体物理研究所 / 合肥物质科学研究院):** both buyer and supplier — tenders a **"100 kA 失超保护主开关定型产品"** (productized QPS main switch, 2025-09-23 bid docs) [CS-H-13] while its own consortium won ITER PF/VS converter task agreements (2025-08-19) [CS-H-09]; 2026 tenders continue (HTS insert magnet, TF assembly).
**Actionpower (西安爱科赛博, SSE-STAR 688719):** mid-Dec 2025 won BEST in-vessel fast-control power supplies and became first-ranked bidder for HL-3 RMP upgrade; positions fast plasma-control converters as a product line [CS-H-14].
**Startorus (苏州/上海星环聚能):** filing its own QD patents (coupling coil + bridge + comparator; application publicized 2026) — self-supply, not procurement [CS-H-15].
**Patenting posture:** 中国科学院合肥物质科学研究院; 中国科学院等离子体物理研究所 (ASIPP); 西安爱科赛博电气股份有限公司 (Xi'an Actionpower Electric Co., Ltd.); 苏州星环聚能科技有限公司 + 上海星环聚能科技有限公司 (Startorus Fusion).
**Weakness:** tender channel closed to Western revenue; QPS switches are one-off specs (hence the "定型产品" tender — even ASIPP wants a product nobody sells) [CS-H-13].

---

## Segment structure — the 2029 bundling-threat map

**Axes:** (1) converter supply, (2) interruption/dump, (3) detection instrument, (4) control software. Nobody today sells (1)+(2)+(3) as one offer to third parties.

**Ranked bundling candidates before 2029:**
1. **Dawonsys** — only merchant firm already contracted for converters + master controls + protection-adjacent scope at ITER scale, refreshed 2025 [CS-H-08][CS-H-09]. Missing HTS detection; would bundle if a private-fusion anchor customer asked.
2. **TE Magnetics** — already bundles detection+management+magnet, but inside the magnet sale [CS-H-06][CS-H-07]. Threat mode: absorbs the market (coils-as-product) rather than serving coil builders; its patent estate fences methods.
3. **ASIPP/Hefei ecosystem** (with Actionpower converters) — can assemble the full chain domestically via tenders [CS-H-13][CS-H-14]; geopolitically unavailable to Western buyers, so it caps China SAM rather than contesting the West.
4. **General Atomics** — has PCS + power capability, lab-services DNA; would integrate for a funded US program, won't productize [CS-H-05].
5. **Mitsubishi/Scibreak** — owns the hardest switch layer; no detection; grid-market gravity [CS-H-21].

**The unserved axis:** vendor-neutral, HTS-native detection→protection→drive integration sold as a catalog product with guaranteed end-to-end latency. Evidence of the vacuum: ITER splits QD across 3,000 sensors and 20+ tenders (~EUR 25M) with a 2-3 s budget [CS-H-12]; Fermilab and KIT hand-build their own detectors (UniQD: W7-X 70 coils/500 detectors; "patented at the IPE," last updated 2020, no commercial channel) [CS-H-22][CS-H-18]; Thea drove a 9-coil HTS array with unipolar Magna-Power SL10-250 units plus mechanical relay H-bridges for polarity — a self-build exposing the missing bipolar array-drive + per-coil protection product [CS-H-19]; and lab-tier suppliers give QD away ("The 4G has magnet quench detection built in") — at the bottom of the market protection is free, at the top it is bespoke, and in the HTS middle it is absent [CS-H-16][CS-H-17].
