# D10 — Energy Storage, Hydrogen & Grid Edge

## Landscape

Three forces are converging on power conversion hardware at the "grid edge": (1) AI data
centers are pulling gigawatts onto grids that cannot interconnect fast enough, pushing
developers to behind-the-meter (BTM) generation and microgrids [S/D10-06]; (2) grid operators
are mandating grid-forming (GFM) inverter-based resources as inverter-based generation
displaces synchronous machines, with NERC standards (PRC-028/029/030) and China's NDRC/NEA
2025–2027 storage buildout plan both codifying GFM requirements [D10-10, D10-11]; (3) the
electrolyzer power-electronics and second-life battery segments are maturing but remain
fragmented between cheap-but-crude (thyristor) and expensive-but-precise (IGBT/SiC) hardware
[D10-09]. Power density, response time (sub-cycle to sub-millisecond), and reliability under
harsh/weak-grid conditions are the common technical axes — exactly where wide-bandgap (SiC/GaN)
power electronics and fast digital control offer step-function gains over legacy silicon.

Data centers are the dominant 2026–2030 demand driver: IEA projects global data-center
electricity consumption roughly doubling to 945 TWh by 2030, with the US adding ~240 TWh (+130%)
and China ~175 TWh (+170%) — together ~80% of global growth [D10-04]. IEEE Spectrum reports
synchronized GPU clusters swing power draw 70%+ in milliseconds, a load profile legacy UPS,
diesel gensets, and gas turbines cannot track, forcing operators to oversize infrastructure
[D10-02]. In parallel, the industry is shifting rack power delivery from 415–480V AC (four
conversion stages) to 800V DC at the facility perimeter, targeted for commercial deployment in
H2 2026, promising ~5% efficiency gain, 45% less copper, and 30% lower TCO at gigawatt scale
[D10-01].

## Pain points & buyers

- **Millisecond-scale load transients on AI clusters**: legacy passive backup (diesel, gas
  turbines, standard UPS) cannot react to synchronized GPU power spikes, forcing
  infrastructure oversizing. Buyers: hyperscalers, colocation operators, BTM microgrid
  developers [D10-02].
- **Interconnection queues of 3–7 years** vs. 18–24 month data-center build times push
  developers toward on-site generation (fuel cells, gas, BTM microgrids) that still needs
  grid-quality power conditioning [D10-06].
- **Grid-forming compliance gap**: NERC (US) and NDRC/NEA (China, >30% GFM penetration mandate
  in weak-grid/renewable-concentrated regions) are imposing GFM requirements faster than
  incumbent inverter vendors can certify products [D10-10, D10-11].
- **Electrolyzer power source cost/performance split**: in China, thyristor rectifiers run
  RMB 200–300k per 5 MW/1000 Nm³/h unit vs. RMB 1.2–1.5M for IGBT units with far better harmonic
  performance and fluctuation response — a 4–6x price gap buyers must navigate depending on
  grid quality [D10-09]. Buyers: green-hydrogen EPCs, especially wind/solar-direct
  ("off-grid") projects.
- **Second-life battery grading throughput**: certifying retired EV packs (China's mandatory
  梯次利用 product certification since 2023; UL 1974 in the US) requires SOH/DCIR/BMS testing
  that is slow and inconsistent at scale, gating the second-life BESS pipeline [D10-08, D10-16].
- **800V DC ecosystem immaturity**: no mature solid-state DC protection standard exists yet for
  800V/MW-class DC buses, even as Meta, Microsoft, Google, and vendors (Delta, Eaton, Schneider,
  Vertiv, Nvidia) commit to the architecture [D10-01].

## Incumbents & gaps

Grid-forming inverters/PCS: Sungrow, Hopewind, Inovance, and SMA/GE Vernova dominate volume,
but GFM firmware is largely bolted onto grid-following hardware; DOE/NREL's UNIFI consortium
and NERC still lack a single interoperable GFM spec, leaving room for a purpose-built,
certifiably-compliant product from a small team [D10-10, D10-11, D10-12]. Electrolyzer power
sources: China's IGBT segment (Hopewind, Sungrow, Inovance, Raodong Zhichuang, Zhongke
Zhihuan) is new and margin-rich but still optimizing for grid-tied plants, not the harder
off-grid/fluctuating-renewable case [D10-09]. Fuel cells for data centers: FuelCell Energy now
ships packaged 2.5–12.5 MW "power blocks" and is tripling Torrington manufacturing capacity
(100→350 MW) on a 275% pipeline surge since Feb 2025 [D10-07] — but power conditioning/
interconnection electronics between fuel cell stacks and IT load remain a bottleneck, not the
stack itself. Second-life battery repurposing: B2U (patented EV-Pack-Storage, UL 9540-certified
Sierra site) and Smartville are the leading US integrators [D10-21, D10-22], but both rely on
manual/semi-automated grading; no dominant vendor sells fast automated grading hardware as a
standalone capital good. 800V DC: vendors are racing on converters and busbars, but DC arc
fault detection/protection is still an open research problem in industry press and early IEEE
work [D10-01, D10-13].

## 2029 inflections

- **US 45V hydrogen credit sunsets January 1, 2028** under the 2025 reconciliation law (One Big
  Beautiful Bill Act, Section 70511) [D10-06]. A 2029/2030 launch means the US market shifts
  from subsidy-chasing electrolyzer projects to efficiency/opex-driven ones — favoring
  higher-efficiency SiC/IGBT power electronics over subsidized low-cost thyristor builds.
- **DOE PEM electrolyzer system cost target: $250/kW and $2/kg H2 by 2026**, versus $1,000/kW in
  2022 [D10-03] — the power-electronics share of system cost becomes proportionally larger and
  more contested as stack costs fall faster than power conversion costs.
- **800V DC commercial rollout (H2 2026)** matures into a multi-gigawatt installed base by
  2029–2030 as new AI campuses reach commissioning, creating a window for second-mover
  component vendors (DC breakers, fast power modules) once the architecture stabilizes
  [D10-01].
- **China's GFM storage mandate (>30% penetration in Northwest/Xinjiang new projects, 2025–2027
  action plan)** matures into enforced grid-code compliance by 2028–2029, likely followed by a
  similar US NERC PRC-028/029/030 enforcement cycle [D10-10, D10-11].
- **IEA base case: data-center electricity nearly triples in AI-optimized facilities and reaches
  945 TWh globally by 2030** [D10-04], sustaining multi-year demand for grid-interface and
  buffering hardware well past a 2029/2030 launch.

## China notes

China's NDRC/NEA jointly issued the 新型储能规模化建设专项行动方案 (2025–2027) explicitly
prioritizing grid-forming (构网型) storage for grid-side applications, mandating >30% GFM
penetration for new renewable-heavy projects in the Northwest/Xinjiang and enabling GFM storage
to earn market-priced ancillary services (inertia, ramp rate) [D10-10]. A China Energy Storage
Alliance (CNESA) group standard for GFM PCS technical specs is already in draft [D10-12], and
GB/T 34120-2023 sets national PCS technical requirements. On hydrogen, China's IGBT-based
制氢电源 (hydrogen power source) segment is nascent but fast-growing — Sinopec ran the world's
first 9.6 MW IGBT hydrogen power-source demonstration with real electrolyzer load in Yinchuan
(March 2023) [D10-09] — and the market could reach RMB 5.6–33.3 billion once green-hydrogen
demand hits 100 Mt. On compute infrastructure, Chinese 智算中心 (AI computing centers) are
piloting hydrogen fuel-cell and PV-hydrogen "zero-carbon" microgrids (e.g., Yulin site; Tsinghua
Carbon Neutrality Institute's national R&D project on user-side fuel-cell microgrid integration)
[D10-20], mirroring the US BTM trend but with stronger state direction and mandatory retired-EV-
battery certification rules (2023 MIIT/SAMR joint circular on 梯次利用 product certification).

## Opportunity seeds

**1. Grid-forming power-conversion system for behind-the-meter compute-campus microgrids.**
Data-center developers face 3–7 year interconnection queues and need utility-facing power
electronics that can black-start, ride through faults, and meet NERC PRC-028/029/030 or China's
>30% GFM mandate without waiting for incumbent giants (Sungrow, SMA, GE Vernova) to retrofit
firmware. Buyers are BTM microgrid integrators and hyperscaler infrastructure teams who will
pay a premium for certified compliance and faster response than legacy grid-following gear. A
2–5 person team with SiC/GaN device and fast-control expertise can build a focused PCS product
line before the GFM spec fully standardizes and the incumbents catch up. Both US (NERC) and
China (NDRC mandate) markets are moving in lockstep on this requirement through 2027–2029.

**2. Row/rack-level ultra-fast power buffer for GPU pulse loads.**
Synchronized AI training clusters swing 70%+ of rated power in milliseconds — faster than
diesel, gas turbines, or conventional UPS can track — forcing operators to over-provision
transformers and generators. A compact SiC-based buffer module (battery/supercap front end with
sub-millisecond digital control) sitting between the facility power train and IT racks lets
operators right-size infrastructure instead of over-building it. Buyers are hyperscalers and UPS
OEMs (Vertiv, Eaton) looking for a component to integrate or white-label. A small team can win by
demonstrating response time and power density incumbents' legacy UPS platforms cannot match, with
both US AI campuses and China's 智算中心 buildout as addressable markets.

**3. High-efficiency SiC/IGBT power source modules for off-grid, fluctuating-renewable
electrolyzers.** China's own market data shows a 4–6x price gap between crude thyristor and
precise IGBT hydrogen power sources, and the IGBT segment is still optimizing for grid-tied,
not off-grid, wind/solar-direct plants where power quality and fast dynamic response most
matter. With the US 45V credit sunsetting in 2028, post-2029 hydrogen projects (both US export-
oriented and China off-grid) will compete on kWh/kg efficiency, not subsidy — rewarding compact,
high-switching-frequency modules over commodity rectifiers. A small power-electronics team can
sell a drop-in rectifier/power-supply product to EPC integrators rather than competing with full
electrolyzer-stack makers.

**4. Solid-state DC protection and fast power modules for the emerging 800V DC data-center
bus.** The industry-wide shift to 800V DC (targeted for commercial systems in H2 2026, backed by
Meta/Microsoft/Google's Mt. Diablo Initiative and vendors like Delta, Eaton, Schneider, Vertiv)
still lacks a mature DC arc-fault/protection standard at MW scale. A small team building a
SiC-based solid-state DC breaker or fast power module can enter as a second-mover component
supplier once the 800V architecture stabilizes around 2027–2028, selling into a market that will
scale with gigawatt-class AI campuses through 2029–2030 in both the US and China.

**5. Automated grading and sorting test benches for second-life EV battery repurposing plants.**
China's mandatory 梯次利用 product certification (since 2023) and the US UL 1974 standard both
require SOH/DCIR/BMS assessment of retired packs, but existing grading is manual and slow,
gating the pipeline into second-life BESS integrators like B2U and Smartville in the US and
similarly certified plants in China. A 2–5 person team can sell fast, automated, multi-channel
grading/sorting equipment as capital equipment to repurposing facilities — a standalone product,
distinct from passive condition-monitoring services — leveraging precision-instrumentation and
automated-fixture experience. China's larger EV retirement volume and the founder's China network
make it a natural first market, with US expansion following UL 1974-certified facility growth.
