# EXECUTIVE SUMMARY — Startup Opportunity Research for a 2029/2030 Launch (max-effort revision)

*Mission output: 40 candidates from 10 domain scans · 15 adversarial red-teams · 12 deep dives ·
1 policy brief · 689 unique sources. This revision re-derives all scoring at maximum reasoning
depth from the mission's own evidence (no new research); every change vs. the prior version is
logged in `03_MAX_EFFORT_DELTA.md`. Everything traces to `[S###]` in `90_BIBLIOGRAPHY/`,
`[DD-Cxx-##]` in the deep dives, and `[P-##]` in the policy brief.*

---

## The one-sentence conclusion

The research still converges on one strongest position — **own the manufacturing infrastructure of
the HTS magnet industry (winding cells, inline QC, and the precision electronics around the
magnet) as one product family, launched US-first into the 2027–2031 fusion-supply-chain buildout**
— and the re-derivation *strengthens* that conclusion: five of the top seven final scores are now
facets of that single cluster, with AI-data-center protection intelligence the strongest unrelated
alternative.

## Top 7 (final scores, post-red-team, post-deep-dive, post-policy)

**1. C12 — Automated NI/MI-HTS coil winding cells with recipe software and inline QC (83.6,
Medium conviction; the lead bet).** Every HTS magnet is wound; for no-insulation coils the
winding recipe *is* the electromagnetic design (turn-to-turn contact resistance is set by tension
during fabrication [DD-C12-02]), and winding uniformity, joints, and screening currents are the
industry's named failure modes [S054][S089]. REBCO demand is on a 10x curve driven by fusion
[S080]; fusion supply-chain spend ran $434M (2024) → $538M (2025) → $681M projected 2026, with
precision-manufacturing capacity the top stated worry [DD-C12-26][DD-C12-27]. The red team
correctly killed the naive version — Broomfield, Ridgway, and BOW already sell superconducting
winding machines, and the biggest magnet makers wind in-house — but the deep dive found the
decisive fact: **Tokamak Energy acquired Ridgway in September 2025, removing the West's only
neutral supplier of this machinery** [DD-C12-19] just as second-tier magnet programs need
production lines they cannot buy from a competitor's subsidiary. The venture-scale version is the
family: winding cell + recipe software + inline QC (C33, rank 5) + test magnets (C15, rank 6) —
honestly a $3–8M/yr machine business with a credible $20–60M/yr equipment+software+coil-services
ceiling. He has already built this machine once. China is supply chain and competitive
intelligence, not a market [DD-C12-08][P-32]. Governing gate: **3 paid commitments from
non-integrated magnet builders by mid-2030.**

**2. C10 — Precision magnet & scientific power converters, fast-dynamics wedge (76.8, Medium).**
The catalog-ppm framing is dead (CAENels FAST-PS stops at 900 W; Danfysik owns slow-dynamics
high-stability [DD-C10-01][DD-C10-02]), ppm lives in the DCCT not the switch [DD-C10-06], and
Chinese fusion tenders are captured domestically (爱科赛博, 荣信汇科, 英杰电气
[DD-C10-23][DD-C10-24]) — but the verified wedge is real: **fast-dynamics, telemetry-rich,
modular converters from 5 kW to multi-kA sold as product with weeks–months lead time**, into a
market where 48% of surveyed fusion companies name power systems their top supply bottleneck
[DD-C10-14] and DOE-milestone companies hit PDRs 2027–2029 [S058]. Beachhead SAM ~$15–25M/yr;
SOM $1.5–4M by 2031 — a wedge that must earn its Series A through expansion. It is also the
natural seller of electronics into the C12 customer base, and the designated absorber of C11's
protection line (rank 4) and C35's LLRF assets (rank 9). Kill test: if 2026–27 interviews show
fusion buyers won't pay for lead time and dynamics, stop.

**3. C06-pivot — Protection-intelligence modules for 800 VDC AI data centers (74.8, Medium; the
strongest non-magnet alternative).** The original solid-state-breaker idea is dead — ABB SACE
Infinitus and Siemens SENTRON 3QD2 ship today [DD-C06-03][DD-C06-04]. What survives is the layer
NVIDIA itself calls the open innovation area [DD-C06-01]: **per-rack ground-fault *location* and
series-arc discrimination on ungrounded 800 VDC buses**, sold through power-system integrators.
The re-derivation *raised* this candidate's relative standing on one point: the red team's "China
slot already taken" claim is contradicted by the Chinese vendors' own filings — TYT reports SSCB
orders as a small pilot-stage share and Liangxin describes itself as at pre-research
[DD-C06-16][DD-C06-17][DD-C06-18] — and China's 800 V standards window opened *later* than the
US one (first white paper Aug 2025 [DD-C06-20]). Policy archetype (d) is the cleanest in the
mission (✅✅✅). First revenue ~2031. Kill check: if NVIDIA/OCP reference designs embed this in
power-shelf firmware by end-2027, fold.

**4. C11-rescope — Detection-first magnet protection & management units (71.2, Medium-Low
rescoped; a product line, not a company).** The pitched sub-millisecond kA dump is physics
theater — dump speed is capped by insulation voltage; ITER extracts 41 GJ over ~30 s at ≤10 kV
[DD-C11-01] — and the deep dive renounces it. What survives is real: detection is the genuinely
unsolved problem in HTS protection [DD-C11-06], "self-protecting" NI coils actually operate in a
narrow engineered window that needs management electronics [DD-C11-03], and ASIPP's 2025 public
tender for a productized 100 kA quench-protection switch proves the hardware layer is bought,
not only built in-house [DD-C11-15]. But the bottom-up category ceiling is <$150M/yr, so the
honest disposition is **the margin-rich attach product inside C10/C12**, with the founder's
detection-latency benchmark as the cheapest validation experiment in the portfolio.

**5. C33 — Cryogenic coil QC instruments, "TapeStar for coils" (71.2, Low standalone /
Medium-High as module).** The only candidate whose score *rose* under maximum scrutiny. The red
team's kill shot — Tokamak Energy's quench-detection patents — **does not survive reading the
claims**: US11749434B2 requires inter-coil comparison across a plurality of coils in an assembled
magnet, and US11101059B2 requires a striated secondary HTS tape; a single-coil, model-referenced
factory instrument omits both [DD-C33-01][DD-C33-02]. The physics is demonstrated (LBNL Hall-array
+ inverse Biot-Savart on CICC terminations, named for QC [DD-C33-03]), the founder's stellarator
Hall-array work is the strongest capability match in the portfolio, and v1 is 12–18 months of
work. But the recount confirms ~8–15 realistic buyers → $2–4M/yr steady state: **a good product
line and a bad company** — carried as C12's QC module and the founder's credibility engine.

**6. C15-reframe — US-built, fast-turnaround HTS test & background-field magnets (69.6, Low-Med;
Medium as C12's expansion).** The benchtop-NMR OEM story is dead — HTS-110 ships exactly that
product line, and the segment standardized on Halbach permanent magnets specifically to avoid
cryogenics [DD-C15-13][DD-C15-14]. What survives: conductor-qualification and background-field
magnets for the fusion test economy (~11–20 units/yr, $11–35M/yr SAM), where the US domestic
angle matters (NASEM calls US magnet capability lagging [DD-C15-08]) and China's import door is
visibly closing (Beijing tender: imported bids invalid [DD-C15-09]). Requires a cryogenics
co-founder; sequenced behind C12, whose winding know-how it monetizes vertically.

**7. C01/C03-merge — Aviation-class power bricks (50–500 kW, ≥10 kW/kg continuous) for uncrewed
and fast electric craft (69.6, Med-Low pivot; the diversified third lane).** The catalog-PEBB and
crewed-marine versions are occupied (GE Vernova holds the ONR PEBB productization [DD-C01-01];
Danfoss iC7-Marine/ABB own the cabinet tier [DD-C01-06][DD-C01-25]; China's chain is CSSC-captive
[DD-C01-21]). The surviving wedge: marine-ruggedized continuous-density bricks for USVs and
foiling craft — platforms procured outside the heavyweight-shock qualification stack, with real
budgets ($200M obligated to one 24-ft USV vendor in Dec 2025 [DD-C01-12]) and a Navy STTR topic
literally specifying the product ("approaching 100 kW/L" [DD-C01-10]). The re-derivation restored
one red-team overreach: the $2–5M test-infrastructure objection belongs to the retired MVDC
framing; the pivot needs a $150–400K regenerative rig [DD-C01-11]. Watch H3X, which can flank
from integrated motor drives into standalone bricks at any time [DD-C01-08].

**Fallen from the prior top 7:** C27 (250°C harsh-environment platform, now #8 at 68.0 — the
merchant slot above 230°C is verifiably empty, but current merchant purchase orders are ~zero and
the beachhead is grant-fed [DD-C27-13]) and C08 (facility ride-through, now #11 at 65.6 — the
attach rate behind its entire beachhead is unverifiable before 2027, and the commoditization that
killed the rack version is already running one level up [DD-C08-03]). Both remain gated options
with explicit 2027 tripwires.

## Comparison table

| # | Idea (final form) | Final score | DD conviction | Beachhead SAM | First revenue | Capital to v1 | Founder-fit | China role (per policy brief) | Kill gate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | C12 winding cells + QC + software | 83.6 | Medium | $3–8M/yr machines; $20–60M/yr family | 2030 | ~$2.5–3.5M | Exceptional (built it once) | supply chain + intel [P-32] | 3 paid commitments by mid-2030 |
| 2 | C10 magnet power (fast-dynamics) | 76.8 | Medium | $15–25M/yr | 2030 | ~$2.5–4M | Excellent | radar + cost base, not revenue [DD-C10-24] | WTP evidence by end-2027 |
| 3 | C06 protection intelligence | 74.8 | Medium (pivot) | $15–35M/yr run-rate by 2030–31 | 2031 | ~$1.5–3M | Strong | fast-follow via CDCC/partners [DD-C06-20] | OCP/NVIDIA embed check end-2027 |
| 4 | C11 detection-first MPMU | 71.2 | Med-Low (rescoped) | <$150M/yr category ceiling | 2030 H2 | ~$0.75–1.5M | Excellent | OEM co-dev channel (archetype c ✅) | 2 non-fusion LOIs by end-2027 |
| 5 | C33 coil QC module | 71.2 | Med-High as module | $2–4M/yr standalone | 2030 H1 | ~$1.5–2.5M | Strongest in portfolio | component supply + intel | 3 written buy-intents by end-2027 |
| 6 | C15 fusion test magnets | 69.6 | Medium (reframed) | $11–35M/yr, lumpy | mid/late 2030 | ~$3–5M | Excellent (needs cryo hire) | closed (domestic-only tenders [DD-C15-09]) | 5 of 15 buyer interviews positive by end-2027 |
| 7 | C01/C03 USV power bricks | 69.6 | Med-Low (pivot) | ~$10–15M/yr SOM by 2032 | 2030 (NRE), 2031 (product) | ~$2.5–4M | Strong | zero (defense lane [P-19][P-20]) | USV builder LOI by end-2028 |

## The biggest surprises

1. **Full-pipeline stress-testing costs −11.4 points on average — half again what the red teams
   alone found.** Red-team adjustments averaged −7.0; the new deep-dive/policy layer averaged a
   further −4.5 across the 12 deep-dived candidates (range: +0.8 to −11.6). The modal failure
   mode remains a product that already ships (Keysight PD1500A [DD-C23-01], Allegro's 10 MHz TMR
   [RT-C30-01], HTS-110's OEM magnets [DD-C15-14], ABB's 800 V SSCB [DD-C06-03], Chroma's
   energy-recycling formation racks [RT-C20-01]). Any un-stress-tested idea in this portfolio
   should be assumed ~11 points overrated — which is how the full ranking now discounts them.
2. **Red teams overshoot too — verification cuts both ways.** Two red-team pillars failed
   primary-source verification in the deep dives: Tokamak Energy's patents do *not* block C33's
   factory QC instrument (claim language requires inter-coil comparison [DD-C33-01]), and C06's
   "China slot already taken" rested on stock-forum claims contradicted by the vendors' own
   filings [DD-C06-16][DD-C06-18]. Two candidates' scores *rose* under deeper scrutiny (C33
   +0.4, C01 +0.8). Scouts find pain; red teams find incumbents; only deep dives read the claim
   language — the ranking now weights evidence by that hierarchy.
3. **The policy landscape inverts the "China-first" premise.** 31 CFR 850 (in force Jan 2025)
   makes a US person founding a Chinese entity in covered sectors a covered — sometimes
   prohibited — transaction, and the COINS Act (Dec 2025) broadens it with new regs due ~March
   2027 [P-01][P-02][P-03]. Independently, China's demand side is 国产替代-locked: a 20%
   procurement evaluation preference for China-manufactured product from 2026-01-01 [P-32],
   首台套 subsidies [P-31], and domestic-only tenders already appearing in the exact niches at
   issue [DD-C15-09]. **The founder's China asset reprices from "market entry" to supply chain,
   competitive intelligence, and bilingual customer development** — still real, no longer an
   entity strategy (research, not legal advice; `50_PHASE5_POLICY/POLICY_BRIEF.md`).
4. **The strongest ideas collapsed into one cluster — now 5 of the top 7.** C12, C10, C11, C33,
   and C15 are the same customer community, the same physics, and the same founder asset viewed
   from five angles: the HTS magnet industry lacks its equipment/electronics/QC layer. The
   re-derivation sharpened this: the two "product line, not company" candidates (C11, C33) rank
   4–5 *because* they are load-bearing modules of the #1 and #2 theses.
5. **Vertical integration is the enemy everywhere.** CFS winds in-house and sells magnets
   [DD-C12-22]; NVIDIA embeds the buffer [DD-C08-01]; IBA builds its own RF [DD-C35-05]; service
   majors build downhole electronics; CSSC captures marine propulsion [DD-C01-21]. The durable
   small-team positions are (a) equipment/tooling sold *to* the integrators, (b)
   intelligence/software-rich modules integrators prefer to buy, (c) niches beneath the
   integrators' minimum deal size.

## What I would do in your position

*(Stated assumptions: you finish the PhD ~mid-2029, can raise a $2–4M pre-seed on your
background, want extreme-performance hardware+software, and will not bet the launch on any
un-stress-tested idea.)*

**Build toward the C12 cluster as the primary bet — one company, staged as machine + QC module +
electronics — with C06-pivot as the diversified fallback.** Concretely:

- **Now–2027: run the cheap experiments that gate everything.** (i) 15+ structured interviews at
  ASC 2026 / MT-29 across non-integrated magnet builders, tape makers, and national labs, asking
  two prices: winding cell, and standalone coil-QC station (tests C12-K1 and C33-K1
  simultaneously). (ii) The C10 willingness-to-pay probe with fusion power-system leads — the
  specific question is *"what premium for 12-week delivery vs an 18-month custom quote?"*
  (iii) The C11 detection benchmark: wind two small NI coils, instrument with voltage taps + Hall
  array + fiber, publish the latency comparison — it validates the #4 product and your #5
  credibility for under $25K. (iv) Passive tripwires: OCP/NVIDIA spec watch (C06), DOE
  superhot-award watch (C27), USV-hybrid watch (C01/C03).
- **2027–2029: steer the thesis toward the cluster.** Cryogenic/magnet instrumentation is
  in-lane for your PhD, conflict-free with Magnefy, and product-adjacent. Land one
  summer/consulting engagement with a fusion or magnet company; file personal provisionals on the
  winding/QC integration (documented clean-room development, no Stanford IP).
- **2029: incorporate US (Delaware); raise seed against signed LOIs.** China participates as
  supplier qualification and market intelligence only, pending counsel review of 31 CFR
  850/COINS and the post-Nov-2026 Affiliates-Rule/materials-truce landscape
  [P-03][P-06][P-36] — do not co-found or take PRC-sourced capital without specialist advice
  [P-39].
- **Fallback logic (evidence-gated, in order):** if the mid-2027 interviews return <3 credible
  machine/QC buyers, pivot to **C06-pivot** (bigger market, weaker moat, cleanest policy lane);
  if 800 V intelligence is absorbed into reference designs, the remaining lanes are **C01/C03**
  (gated on a USV-builder LOI) and **C27** (gated on DOE superhot awards). C23 stays the deep-fit
  emergency fallback — its validation costs almost nothing and its skills are your daily work.

The asymmetry that decides it is unchanged and now better quantified: C12 is the only idea where
you are provably one of a handful of people who has already built the core artifact, where the
customer base is expanding on policy-backed money in both hemispheres (even though only one is
sellable-into), where the #4/#5/#6 products attach to the same customers, and where losing still
leaves you the most employable person in a growing industry. That is what a right-sized first
company looks like.

*(All market sizes are bottom-up estimates with stated uncertainty in the deep dives; policy
statements summarize `50_PHASE5_POLICY/POLICY_BRIEF.md` — research, not legal advice.)*
