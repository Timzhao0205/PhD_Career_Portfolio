# D06 — Semiconductor Equipment Adjacencies (post-cleanroom)

## Landscape

This domain covers equipment plugging into the back end of chipmaking — advanced packaging
(hybrid bonding periphery), device/wafer test, WBG (SiC/GaN) burn-in/reliability, and niche
metrology — without fab ownership. Three sub-markets stand out.

**Hybrid bonding periphery.** Cu-Cu direct bonding at sub-1µm pitch (chiplets, HBM, CIS) is
scaling; EV Group demonstrated 300mm wafer-to-wafer 1µm-pitch bonding with 500nm pads and 195nm
(3σ) overlay [D06-01], and in Sept 2025 launched the EVG40 D2W die-to-wafer overlay metrology
tool: 2,800 measurement points per 300mm wafer in 4 minutes, 15x prior throughput [D06-02]. The
pain: D2W overlay metrology traditionally traded sampling density for speed, leaving fabs blind
to misalignment until yield loss appears [D06-02]. NIST flags that bond-quality prediction
("Known Good Process") is still trial-and-error, not predictive metrology, and is funding
surface-characterization research via the CHIPS R&D program [D06-13]. Peer-reviewed work
confirms sub-1nm overlay uncertainty is achievable in production CIS lines and sub-300nm W2W
overlay at 1µm pitch in room-temperature Cu-Cu schemes like DBI Ultra, though reviews note
chiplet-level scaling challenges remain [D06-17][D06-18][D06-19][D06-22].

**WBG (SiC/GaN) test and burn-in.** SiC/GaN power devices need high-voltage, high-temperature
stress screening (HTRB, dynamic Ron, short-circuit, gate overstress) legacy Si boards can't do
[D06-11][D06-16]. Aehr Test Systems leads wafer-level burn-in for SiC/GaN; a lead AI-processor
customer placed a $14M order for multiple FOX-XP systems plus consumables (Feb 2026) [D06-04].
Aehr's revenue is volatile — $20.6M in Q1 FY24 during the SiC/EV boom vs. $10.3M in Q3 FY26 as
EV-linked SiC demand softened while AI-processor bookings picked up ($37.2M/quarter, 3.5x
book-to-bill) [D06-03]. Short-circuit withstand time and critical energy for 1200V SiC MOSFETs
are still being characterized and standardized across labs — active Tier-1 research [D06-20].

**Wafer/device test niches.** The advanced probe-card/wafer-probing market is $4.3B (2025) to
$10.4B by 2036 (8.2% CAGR); specialized suppliers (QA Technology, Feinmetall) own RF niches while
Asian cost players (Da-Chung, AIKOSHA) compete in mainstream probing [D06-07]. Double-pulse
testing (DPT), the standard WBG switching-loss method, is automated by general T&M vendors and
offered as a shared service by UK's CSA Catapult (1.5kV/1kA, 25-150°C, per IEC 60747-8-4)
[D06-08][D06-23] — a signal that in-house automated DPT capability stays scarce.

## Pain points & buyers

- **Power-device makers** (Wolfspeed, onsemi, Infineon, China's SiC/GaN fabs) need cheaper
  qualification against new JEDEC guidelines — JEP203 (short-circuit) and JEP204
  (stress-procedure catalog), both June 2026 — replacing fragmented methods where "results have
  varied across vendors and test labs" [D06-09][D06-16].
- **OSATs/chiplet integrators** need die-level overlay/void metrology keeping pace with sub-1µm
  hybrid bonding without slowing throughput [D06-02][D06-13].
- **Automotive/industrial power-module makers** need burn-in for 1000-hr HTRB and short-circuit
  screening before EV inverter qualification, gated by $-per-die economics [D06-11][D06-20].
- **University, DoE-lab, and DoD/NASA power-electronics groups** doing DPT/reliability work lack
  affordable automated setups — Sandia runs a dedicated WBG reliability program and NASA's NEPP
  program catalogs GaN reliability guidelines because this capability isn't commercially
  accessible off-the-shelf [D06-14][D06-24]; CSA Catapult built shared national DPT capacity for
  the same reason [D06-08].
- **Chinese fabs/OSATs** under localization pressure — 2023 domestic equipment revenue $4B
  (11.7% localization) toward a projected $5.1B (13.6%) in 2024 against a $34.2-37.5B total China
  equipment market [D06-06] — qualify local vendors where localization is lowest (~5% in
  die-attach/wire-bond/grinding, per one estimate) [D06-05].

## Incumbents & gaps

Hybrid-bonding metrology is owned by EVG, Onto Innovation and KLA — full-line fab suppliers no
2-5 person team can unseat directly. WBG burn-in is dominated by Aehr (FY26 revenue guided to the
high end of $45-50M) [D06-03], selling systems priced for production-volume fabs — leaving a gap
in **cheaper, modular, R&D-scale WBG stress/burn-in rigs** for labs and startups that can't
justify multi-million-dollar systems [D06-04]. DPT automation is fragmented among general T&M
vendors bolting DPT firmware onto oscilloscopes — no vendor sells a purpose-built, affordable,
automated SiC/GaN switching-characterization appliance with a clean sweep/export software stack;
a government-funded Catapult center having to build shared national capacity for this is itself
evidence of the gap [D06-08]. Government labs (Sandia, NIST) fund upstream reliability *science*
[D06-13][D06-14], and ARPA-E funds device cost reduction [D06-15][D06-21] — but none ship turnkey
commercial instruments, which is the translation gap a small team can close.

## 2029 inflections

By 2028-2030, JEDEC's new SiC guideline set (JEP203/204, June 2026) will likely become de facto
qualification for automotive/grid SiC, forcing mid-tier device makers to buy compliant test
capacity or outsource it [D06-09][D06-16]. Hybrid bonding moves from HBM/CIS toward mainstream
chiplet logic as 300mm D2W tools reach high-volume manufacturing — EVG40 D2W units were running
at customer sites within months of the 2025 launch [D06-02] — pulling overlay-metrology demand
down-market to OSATs that can't afford EVG's flagship tier. China's 15th Five-Year Plan
(2026-2030) is expected to keep wide-bandgap semiconductors a named priority, continuing the 14th
Plan's (2021-2025) SiC/GaN push [D06-12]; with sub-15% domestic equipment localization even in
2024 [D06-06], Chinese SiC/GaN fabs will likely keep seeking non-US test/packaging suppliers
through 2029-2031 — an opening for a team with China ties. ARPA-E's SWITCHES program still
targets WBG cost parity with silicon (WBG devices remain up to 10x pricier today) [D06-15][D06-21],
so test/qualification cost stays a visible line item as volumes ramp.

## China notes

China's SiC/GaN policy dates to the 14th Five-Year Plan (2021), naming SiC/GaN wide-bandgap
semiconductors an accelerated-industrialization target, with 10+ new SiC projects reported
launched nationwide the year it issued [D06-12]. Shanghai's third-generation-semiconductor
roadmap emphasizes GaN/SiC for 5G, EV charging, UHV transmission and rail, with parallel policy
support in Shenzhen, Beijing, Changsha, Zhejiang, Chengdu and Guangzhou [D06-10]. Packaging/test
equipment localization stays critically low even in prioritized categories — roughly 5% in
die-attach/wire-bond/grinding by one estimate, versus 11.7-13.6% for semiconductor equipment
overall in 2023-2024 [D06-05][D06-06]. This combination — strong policy pull, weak domestic
tooling — is the clearest China-side opening here: a small non-Chinese team selling standalone,
fab-independent SiC/GaN test/packaging instruments can sell into Chinese fabs directly or
license designs, with founder fluency and network lowering go-to-market friction versus
competitors with no China presence.

## Opportunity seeds

1. **Modular, sub-$150K automated DPT + Ron/HTRB bench for SiC/GaN R&D labs.** Device makers,
   national labs and university groups need JEDEC-JEP203/204-compliant data but can't justify
   full-stack T&M pricing or Aehr's multi-million-dollar systems [D06-08][D06-04][D06-09]. Buyer:
   R&D/qualification labs at mid-tier fabs and university/DoE labs. Extreme performance wins
   because kV-class switching parasitics demand precision instrumentation matching the founder's
   WBG/precision-analog background. A 2-5 person team builds one purpose-built rig and sells
   direct; China's fab buildout plus US university/DoD labs give a two-market wedge.

2. **Affordable high-voltage probe-card line for SiC/GaN wafers.** High-power probing needs
   field-replaceable, arc-resistant contacts rated for kV-class testing; specialized incumbents
   are few, and Chinese fabs face near-total import dependence on test-interface hardware
   [D06-05][D06-07]. Buyer: OSATs/IDMs qualifying new wafer lots. A small team iterates faster
   than majors locked into standard lines, selling into China (thin local supply) or the US
   (custom short-run automotive-grade cards).

3. **Standalone die-to-wafer overlay/void inspection station for mid-tier OSATs.** EVG40
   D2W-class tools are priced for HVM leaders; smaller OSATs doing chiplet/HBM overflow still
   align dies with undersampling legacy tools, causing yield loss [D06-02][D06-17]. Buyer: OSAT
   process-engineering teams. A single-purpose optical/IR overlay station undercuts EVG/KLA for
   the mid-volume tier; China's OSATs scaling advanced-packaging capacity need this tier of tool
   as domestic equipment localizes [D06-05].

4. **Compact wafer-level burn-in cell for GaN power-IC startups and R&D fabs.** Aehr's FOX
   systems target AI-processor and automotive-volume customers placing multi-million-dollar
   orders [D06-03][D06-04]; sub-scale GaN startups have no affordable WLBI option and often skip
   burn-in, hurting automotive design-in credibility. Buyer: GaN power-IC startups in the US and
   China. Low-cost, high-parallelism benchtop stress is a hardware problem suited to a small
   team; it's a manufacturing-test product, not a monitoring service, avoiding
   condition-monitoring overlap.

5. **Purpose-built dynamic-Ron / JEDEC-RDS(on) compliance tester for GaN HEMT lines.** Current
   setups patch dynamic-Ron measurement from general lab equipment or one-off research circuits,
   even as JEDEC standardizes methodology [D06-09][D06-16]. Buyer: GaN HEMT fabs and design
   houses needing datasheet-grade numbers for customer qualification. A small team owns this
   standard-compliance niche as early ATE boutiques did, selling one dedicated instrument; strong
   China angle given the country's GaN buildout under continuing Five-Year-Plan support [D06-12].

6. **Turnkey JEP203/204-compliant short-circuit/ruggedness qualification bench.** JEP203 is
   brand-new (June 2026); most mid-tier fabs lack matching in-house rigs, mirroring the gap CSA
   Catapult filled for DPT, while short-circuit ruggedness itself is still active research across
   SiC MOSFET generations [D06-08][D06-09][D06-20]. Buyer: second-tier SiC fabs (Chinese and
   US/EU) without an internal reliability lab. A standalone bench instrument, not a
   diagnostic/monitoring service; a tiny team can beat large ATE vendors to a compliant turnkey
   box.
