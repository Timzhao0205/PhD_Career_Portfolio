# DD_C06 — Solid-State DC Arc-Fault & Ground-Fault Protection for 800 VDC Data Centers

**Candidate:** C06 | **Date:** 2026-07-03 | **Sources:** 23 (log: `DD_C06_sources.json`, IDs DD-C06-01…23)
**Headline finding:** The red team is substantially right about the *breaker*. The original concept — a
startup-built, certified 800 V/kA-class rack SSCB — is not survivable for a 2029 solo entrant. A narrower
beachhead survives: **protection intelligence for the ungrounded 800 VDC bus** (per-rack ground-fault
location + series-arc discrimination, sold as modules/firmware through power-system integrators), with an
option to graduate into second-generation breaking hardware via partnership or acquisition. This report
scores the pivoted version and states explicitly where the original claim died.

---

## 1. Problem & who has it

800 VDC power architecture for AI racks is now committed roadmap, not speculation. NVIDIA states it is
"leading the transition to 800 VDC data center power infrastructure to support 1 MW IT racks and beyond,
starting in 2027," coinciding with Kyber rack-scale systems, and explicitly flags that "fault detection and
serviceability in VDC systems is a key area for innovation" [DD-C06-01]. OCP's Mt. Diablo specification
(Google, Meta, Microsoft) defines the disaggregated sidecar power rack at ±400 VDC or 800 VDC for
100 kW–1 MW IT racks [DD-C06-09]; OCP spec material indicates the 800 VDC option is operated
safety-isolated from ground (IT-network practice) [DD-C06-10, snippet — verify in spec text].

Three physics facts create the pain:

- **DC arcs do not self-extinguish** (no current zero-crossing), so series arcs on an 800 V bus burn until
  something interrupts them; detection on a bus fed by hundreds of switching converters is a
  discrimination problem notorious for nuisance trips — the central unsolved issue in the closest analog
  field, PV arc-fault detection [DD-C06-11][DD-C06-12].
- **An ungrounded (IT) 800 V system tolerates the first ground fault but must find it fast.** The
  standard industrial toolkit is insulation monitoring plus pulse-based fault location (e.g., Bender
  ISOMETER + EDS), which today is cataloged for generic industrial systems, not for GW-scale AI halls
  with enormous distributed Y-capacitance and sub-rack granularity requirements [DD-C06-13].
- **The cost of a wrong answer is extreme in both directions:** a missed arc is a fire in a hall drawing
  hundreds of MW; a nuisance trip drops a ~$3–4M NVL72-class rack mid-training-run.

Who has the problem, concretely: (a) facility-electrical and commissioning teams at hyperscalers deploying
Kyber-class halls from 2027; (b) the **power-system integrators** who actually build the sidecar racks and
power shelves — Delta, Flex, LiteOn, Megmeet, Vertiv, Eaton, Schneider are the named NVIDIA ecosystem
tier [DD-C06-01][DD-C06-02]; (c) colocation and neocloud operators retrofitting toward 800 V without
hyperscaler engineering depth; (d) Chinese 智算中心 operators (telecom carriers, ByteDance-class) whose
800 V supply chain and standards are still forming [DD-C06-20]. Demand backdrop: US data-center load
176 TWh (2023) → 325–580 TWh projected 2028 (6.7–12% of US electricity) [DD-C06-14]; ABB cites global
data-center demand ~80 GW (2024) → ~220 GW (2030) with AI ≈70% of the growth [DD-C06-03].

## 2. Product definition & the extreme-performance edge

**Pivoted product (beachhead): the "protection intelligence layer" for ungrounded 800 VDC.**

- **P1 — Rack Guard module** (~1U/DIN, one per MW-class rack or per busway drop): wideband current
  sensing (DC–>10 MHz) on the rack feed, series/parallel arc-signature discrimination in firmware,
  residual-current monitoring, and coordination output that commands the existing disconnect/SSCB or
  power-shelf shutdown. Target spec: detection-to-trip-command <100 µs; nuisance-trip rate engineered
  and *proven* on a published 800 V converter-noise dataset — the metric no vendor currently publishes.
- **P2 — Ground-fault location master** (one per sidecar/row): active test-pulse injection plus the P1 CT
  network to locate first ground faults to a specific rack/branch while the system stays live — Bender-style
  EDS function [DD-C06-13] re-engineered for 800 V, high distributed capacitance, and fleet software.
- **P3 (later) — breaking hardware:** a hybrid rack-level SSCB using purchased 1200 V SiC modules, entered
  only via an integrator partnership or as the acquisition story, after P1/P2 revenue exists.

**Where the original "extreme edge" claim died:** sub-ms solid-state clearing is *catalog reality*, not
whitespace. ABB's SACE Infinitus is an IEC-certified SSCB now in an NVIDIA-collaboration for 800 VDC
[DD-C06-03]; Siemens' SENTRON 3QD2 interrupts in microseconds ("up to 1,000× faster than
electromechanical") using Infineon 1200 V CoolSiC 62 mm modules, aimed at data centers [DD-C06-04];
Atom Power ships UL-listed digital SSCBs marketed at data centers [DD-C06-05]. The defensible extreme
spec is therefore **not interruption speed but discrimination quality**: (i) provable series-arc detection with
quantified false-positive rates on realistic GPU-rack load signatures, and (ii) first-fault *location* in seconds
at rack granularity on an ungrounded 800 V system. Both are sensing + algorithms + system-integration
problems — the founder's exact stack (WBG device physics, precision low-noise readout, embedded
firmware) — and neither requires kA interruption certification to sell.

## 3. Technical feasibility & TRL path (sellable unit by 2029–2031)

Everything in P1/P2 is buildable from purchased components; cleanroom dependence: **none**.

- BOM sketch (P1): Rogowski/fluxgate + shunt hybrid current front-end, 800 V-rated isolated sensing,
  AFE + SoC (Zynq-class or MCU+NPU), IEC 61010-style insulation design, PoE/RS-485/CAN out.
  Component cost ~$150–400; target ASP $1,500–2,500. P2 master: pulse injector + relay matrix +
  compute, ASP ~$8,000. (ASPs are my estimates benchmarked on industrial IMD/EDS gear; no public
  800 V price list exists yet — flagged as assumption.)
- Hard parts: (1) the labeled arc dataset — must build an 800 V arc generator + converter-noise testbed
  (~$30–60k of hardware; feasible in a garage lab, and partially during the PhD); (2) nuisance-trip
  statistics at fleet scale — solvable by shipping in "monitor-only" shadow mode first, which monitoring
  products can do and breakers cannot; (3) EMC at 800 V busway proximity.
- What must NOT be built: the interrupting element. UL 489I requires integral galvanic-isolation contacts
  and semiconductor-specific safety testing [DD-C06-06][DD-C06-07]; that is P3/partner territory.
- TRL path: testbed + algorithms 2026–2028 (PhD-adjacent, publishable); alpha module 2029; monitor-mode
  pilots with one integrator and one colo 2030; certified (UL 61010 / functional-safety, CE/CCC) production
  units and first meaningful revenue **2031**. This honestly concedes the red team's timing point: a 2029
  entrant cannot ship *protection that trips things* into 2027 design-ins; it can ship *protection that watches,
  locates, and commands* into the much larger 2029–2033 buildout and retrofit wave.

## 4. Competitive landscape — global and China

**Global (all verified 2025–2026):**

| Player | Status | Note |
|---|---|---|
| ABB | SACE Infinitus IEC-certified SSCB; NVIDIA collaboration for 800 VDC/1 MW racks; HiPerGuard MV solid-state UPS; ~40% of electrification research on DC/data centers [DD-C06-03] | Feeder/distribution class; not rack-granular sensing |
| Siemens + Infineon | SENTRON 3QD2 SiC SSCB, µs interruption, data centers/DC grids; CoolSiC 1200 V modules announced June 2026 [DD-C06-04] | Same layer as ABB |
| Eaton, Schneider, Vertiv | Named NVIDIA 800 VDC power-system partners [DD-C06-01][DD-C06-02] | Integrator tier = channel, not just competitor |
| Atom Power | First UL-listed digital SSCB, panel products, marketing to data centers [DD-C06-05] | US branch-level; AC-heritage |
| Bender | Incumbent IMD + EDS ground-fault location for ungrounded AC/DC systems [DD-C06-13] | The real competitor for P2; industrial-generic, not AI-rack-integrated |
| Standards | UL 489I Ed.1 ANSI-approved 2025-10-22 (SSCB ≤1000 Vac/1500 Vdc) [DD-C06-06]; IEC 60947-2:2024 covers breakers ≤1500 Vdc [DD-C06-08, snippet] | New — everyone's 800 V cert clock started ~2025 |

**China (Chinese-language sourcing):**

- **泰永长征 TYT (002927)** — the claimed "SSCB leader": its own 2024 annual report confirms SSCB
  commercialized in multiple niches and an industry-leading 1U DC breaker line, but total company revenue
  was RMB 892M (~$125M), **down 14.1%**, net profit RMB 37M [DD-C06-16]; management told investors
  in Nov 2025 that SSCB orders are still "a small share of total sales," in pilot/demonstration stage
  [DD-C06-17]. Stock commentary describing TYT as Delta's exclusive SSCB supplier into Google/NVIDIA
  chains with 2026 mass production [DD-C06-19] is Tier-3 and partially contradicted by the company's own
  cautious disclosure — I report both.
- **良信 Liangxin (002706)**: its official Sept 2025 investor-relations record states SSCB is at
  **技术预研与产品布局 (pre-research/planning)** — not shipping — while noting foreign brands still
  dominate China's data-center electrical market, leaving "较大的替代空间" (large domestic-substitution
  space) [DD-C06-18]. Broker/forum claims of imminent volume delivery to Vertiv-class customers
  [DD-C06-19] again run ahead of the company's own statements.
- **正泰 Chint**: patents/research only, no product [DD-C06-19].
- 中熔电气 (Sinofuse, fuse backup layer) was flagged by the red team; I could not verify its 800 V
  data-center positioning in Tier 1–2 sources within this dive — treat as a real but unquantified player.
- **Standards vacuum is real and still open:** China's first 800 V DC white paper (Delta-led, with China
  Telecom design institute) appeared only Aug 2025, with a 2.0 drafting effort started Sept 2025
  [DD-C06-20] — i.e., the "standards-shaping" window in China is *later* than the US one, not closed.

**Resolution of red-team objection 1 (what niche remains):** Incumbent SSCBs (Infinitus, 3QD2) are
distribution/feeder-class boxes; NVIDIA's own architecture blog treats compute-rack protection as fuses/
disconnects/emerging solid-state devices and names fault detection as the open innovation area
[DD-C06-01]; the Oct 2025 ecosystem partner list contains **no protection-intelligence category at all**
[DD-C06-02]. Chinese "leaders" are, by their own filings, at pilot or pre-research stage [DD-C06-16–18].
The surviving niches, in descending attractiveness: (a) **ground-fault location analytics for the ungrounded
800 V bus** (weakest incumbent, Bender, is generic-industrial); (b) **series-arc discrimination
intelligence** riding on others' interrupting hardware; (c) retrofit/colo/neocloud tier that big vendors
serve late; (d) second-generation cost-down breaking hardware post-2031 via partnership. The niche that
does NOT survive: prime-vendor certified breakers for 2027 hyperscaler design-ins.

## 5. Market: bottom-up beachhead, then triangulation

**Bottom-up (beachhead = P1+P2 protection-intelligence content):**

- Capacity anchor: 80 GW (2024) → ~220 GW (2030) global data-center demand, AI ≈70% of growth
  [DD-C06-03] → AI additions ≈ 95–100 GW cumulative 2025–2030, back-loaded (~20 GW/yr by 2029–30).
- 800 VDC-native share of AI additions (Kyber-class from 2027 [DD-C06-01]): assume 15% (2028) → 35%
  (2030) — assumption, stated; OCP tri-author sponsorship [DD-C06-09] supports the high case. That gives
  **≈10–25 GW cumulative 800 V IT capacity by end-2030**, i.e., roughly 10,000–25,000 MW-class racks
  (1 GW ≈ 1,000 × 1 MW racks).
- Content per GW: 1,000 rack modules × $2,000 + ~125 location masters × $8,000 ≈ **$3.0M/GW**, plus
  ~15%/yr fleet-software attach.
- Beachhead pool: 10–25 GW × $3.0M ≈ **$30–75M cumulative through 2030; ~$15–35M/yr run-rate by
  2030–31**, growing with 800 V share and the retrofit tail. A startup winning 2–3 integrator design-ins
  plus colo retrofits (10–20% share) ⇒ **$3–7M revenue in 2031, $10–20M by 2033.** Small but winnable
  and priced on avoided downtime, not on copper.
- If P3 breaking hardware is added (ASP $5–25k/module — the one-pager's unverified guess; no public
  pricing exists), per-GW content rises ~10×, to ~$30M/GW — that is the expansion prize, not the entry.

**Top-down triangulation:** global SSCB market $4.81B (2025) → $7.12B (2030), 8.15% CAGR, across all
sectors [DD-C06-15] — a data-center protection slice of even 5–10% by 2030 ($350–700M) is consistent
with the bottom-up pool once breaking hardware (~10× sensor content) is included. Note market-size
estimates for "SSCB" vary by an order of magnitude across firms depending on definition; I anchor on the
bottom-up build. TAM (frontier vision — protection layer of DC electrification: microgrids, marine, EV-DC,
storage): the broader DC-breaker + monitoring space, plausibly multi-$B by mid-2030s [DD-C06-15];
SAM (data-center DC protection incl. hardware) ~$0.4–1B/yr by 2031; SOM as above ($3–7M 2031).

## 6. Go-to-market: China-first vs US-first

**Resolution of red-team objection 2 (will hyperscalers buy from a startup):** Direct evidence says
hyperscalers do not buy rack-power components from seed-stage vendors — NVIDIA's named ecosystem is
incumbent-only [DD-C06-01][DD-C06-02]. But the same evidence shows the **integrator channel is how
small vendors enter**: the sidecar and shelf are built by Delta/Flex/LiteOn/Megmeet/Vertiv, and in China the
TYT-supplies-Delta-supplies-Google structure (claimed in Tier-3 sources [DD-C06-19]) is precisely a
component maker reaching a hyperscaler through an integrator. OCP membership is open and its specs are
community-contributed [DD-C06-09] — a startup can join the Mt. Diablo/protection workstreams, put its
detection interface into contributed text, and sell through integrators without ever holding hyperscaler
prime-vendor status. Monitor-mode products additionally dodge the life-safety liability screen that blocks
startup breakers (a monitoring module that fails is an alarm gap, not a fire).

**US sequence (lead):** 2026–2028 OCP participation + published arc/GF dataset → 2029–2030 shadow-mode
pilots with one integrator (Vertiv/Flex-class) and one neocloud/colo → 2031 UL-61010-class certified product
+ fleet software. US leads because the 800 V spec-setting (NVIDIA, OCP) is US-centered and reference
customers transfer globally.

**China sequence (fast-follow, 6–12 months behind):** the founder's native networks matter here. Entry via
(a) CDCC/白皮书 2.0 drafting participation [DD-C06-20]; (b) carrier 智算中心 pilots — procurement is
tender-driven and domestic-substitution-friendly ("国产替代" named by both TYT and Liangxin filings
[DD-C06-16][DD-C06-18]); (c) manufacturing partnership with a Liangxin-class incumbent (they have DC
breaker channels but, by their own admission, early SSCB/intelligence capability [DD-C06-18]).
Policy tailwind: 300 EFLOPS national compute target [DD-C06-21] and NDRC PUE mandates (fleet ≤1.5,
new large DCs ≤1.25, hub nodes ≤1.2 by end-2025) push direct-DC architectures [DD-C06-22].
**Do not do China-first**: the buyer set that defines the category (NVIDIA/OCP ecosystem) is US-based,
and Chinese incumbents will out-localize a solo founder on hardware cost the moment volume appears.

## 7. Regulatory & geopolitical exposure (provisional — no Phase 5 brief existed at write time)

- **Certification is the dominant burden, not export control.** UL 489I Ed.1 (ANSI, 2025-10-22) governs
  SSCBs to 1000 Vac/1500 Vdc with mandatory galvanic isolation contacts [DD-C06-06]; UL testing itself
  runs "two or three weeks to a few months," but that excludes development, functional-safety assessment,
  and high-power lab campaigns [DD-C06-07]. **Resolution of red-team objection 3:** for a full 800 V/kA
  SSCB, a realistic startup timeline is 18–30 months and seven figures post-prototype — first breaker
  revenue ~2032–33, confirming the red team. For the P1/P2 monitoring layer (UL 61010/functional-safety
  route, CE, CCC), certification is months and low six figures — **first revenue 2031** is credible.
- **Export controls:** SiC power modules and protection electronics at these ratings are not, to my
  knowledge, on controlled lists; I found no evidence of EAR capture in this dive — flag for Phase 5
  verification rather than asserting EAR99.
- **US outbound-investment rule (31 CFR Pt. 850, effective 2025-01-02)** restricts US persons' investments
  in China entities in semiconductors/microelectronics, quantum, and AI [DD-C06-23]. A US-person founder
  building or funding a China-domiciled entity that *designs power semiconductor-based systems* needs
  counsel review; a US-domiciled company selling modules into China via partners is the cleaner structure.
  This makes China-first **structurally hard** and reinforces US-lead sequencing.
- China side: CCC applies to low-voltage breaker categories; the 800 V DC standard itself is still in white-paper
  stage [DD-C06-20] — early participation is an asset, but expect domestic-substitution preference in tenders.

## 8. Capital & milestones (2029 → 2032)

- **2026–2028 (in-PhD, ~$40–80k):** arc/GF testbed; dataset + 1–2 publications; OCP + CDCC presence;
  10+ buyer interviews. Funded by lab access + small grants.
- **2029 (found; pre-seed/seed $1.5–3M):** team of 3–4 (founder + firmware + power-hardware + FAE);
  alpha P1/P2; two shadow-mode pilot LOIs. Burn ~$1.2M/yr.
- **2030 (seed extension or A-minus, +$3–5M):** monitor-mode fleet pilots (≥3 sites, ≥200 racks);
  UL 61010/CE cert start; nuisance-trip statistics whitepaper.
- **2031: first revenue $1–3M** (modules + software); one integrator design-in. **Series A ($8–15M)** gated
  on that design-in.
- **2032–2033:** $5–15M revenue; P3 decision — build hybrid SSCB with integrator/partner funding, or
  position for acquisition by ABB/Siemens/Eaton/Vertiv-class (the red team's steelman exit, which I endorse
  as a legitimate plan-B).

## 9. Risks & kill criteria

1. **Integration risk (top risk):** integrators (Delta/Flex/Vertiv) or NVIDIA embed arc/GF intelligence
   directly in power-shelf silicon/firmware before 2029, collapsing the module into a feature.
   *Kill:* if by end-2027 the OCP/NVIDIA reference designs specify built-in per-rack arc detection + GF
   location with quantified specs, kill the standalone product (pivot to licensing the dataset/algorithms).
2. **Discrimination edge doesn't materialize:** incumbents' fielded-breaker data advantage [red team] wins.
   *Kill:* if the PhD-era testbed cannot beat published PV-AFDD-class false-positive performance by ≥10× on
   converter-noise data by mid-2028, kill.
3. **800 V ramp slips or fragments** (±400 V wins at OCP; 800 V stays NVIDIA-only).
   *Kill/adjust:* if by end-2028 cumulative 800 V-native deployments are <3 GW, shrink to China 智算中心
   HVDC retrofit niche or kill.
4. **Buyer refusal:** monitor-mode still fails the procurement screen at integrators.
   *Kill:* if 2030 pilots convert <1 of 3 to paid design-in discussions, kill.
5. **China squeeze:** TYT/Liangxin-class vendors bundle "good-enough" intelligence with cheap breakers in
   China tenders; margin evaporates there → treat China as partner/licensing market only.

## 10. Verdict

**Conviction: MEDIUM for the pivoted beachhead (protection intelligence layer); LOW for the original
certified-breaker concept.** The red team's core objections stand against the original one-pager: incumbents
ship 800 V-class SSCBs now, hyperscaler protection lists are incumbent-only, and UL 489I breaker
certification pushes startup breaker revenue past 2032. But three verified facts keep a real company alive
here: NVIDIA itself names VDC fault detection as the open innovation area [DD-C06-01]; the ungrounded-bus
ground-fault-location problem has only a generic industrial incumbent [DD-C06-13]; and China's supposed
category leaders state in their own filings that they are at pilot/pre-research stage [DD-C06-16–18]. The
founder's WBG + precision-sensing + firmware stack maps exactly onto the surviving niche, and the niche
can be validated for tens of thousands of dollars during the PhD.

**Cheapest validation experiments (2026–2028):**
1. Build the 800 V series-arc + ground-fault testbed with GPU-class converter noise; publish the dataset and
   a discrimination benchmark (~$30–60k; also a thesis-adjacent paper). Directly tests risk #2.
2. Join OCP (and CDCC via China network); sit in the Mt. Diablo / power-quality workstreams; run 10+
   structured interviews with integrator and colo electrical engineers on GF-location and nuisance-trip pain,
   and on whether they would buy monitor-mode gear from a startup (~$2k + time). Tests risks #1 and #4.
3. Track 2027 Kyber-generation deployments and the UL 489I certification queue (which vendors list, at what
   ratings); if rack-level protection intelligence appears as a built-in spec line, execute kill #1 early (~$0).

**Kill criteria:** as enumerated in §9 — the two sharpest are (a) reference designs absorbing detection
intelligence by end-2027, and (b) failure to demonstrate ≥10× discrimination improvement on own data by
mid-2028.
