# INCUMBENTS — The Round-1 Best-of-Best (scores FROZEN from GEN3/02_FULL_RANKING.md)

These five theses are the reigning slate. Their final scores were re-derived at max effort in
Round 1 (post-red-team, post-deep-dive, post-policy) and are **frozen here — never re-derived in
this mission**. V-candidates compete against these numbers under the identical rubric and the
Round-1 comparability convention (deep-dived = full adjusted; RT-only = RT−8.9e; raw = raw−11.4e).

---

## 1. C12 cluster — NI/MI-HTS coil winding & jointing cells + recipe software + inline QC — **83.6** (DD, Medium conviction)

Includes the attach modules C33 (coil QC instruments, 71.2), C11 (detection-first MPMU, 71.2),
C15 (fusion test/background magnets, 69.6). Holds the mission's single allowed HTS slot.

Evidence summary:
1. Every HTS magnet is wound; for NI coils the winding recipe IS the electromagnetic design — turn-to-turn contact resistance is set by winding tension [DD-C12-02].
2. Winding uniformity, joints, screening currents are the industry's named failure modes [S054][S089].
3. REBCO demand on a ~10x curve driven by fusion [S080]; fusion supply-chain spend $434M (2024) → $538M (2025) → $681M projected 2026 [DD-C12-26][DD-C12-27].
4. Red team correctly killed the naive "no vendor exists" version (Broomfield/Ridgway/BOW sell winding machines; big magnet makers wind in-house).
5. Decisive deep-dive fact: Tokamak Energy acquired Ridgway Sept 2025, removing the West's only neutral supplier of this machinery [DD-C12-19].
6. Venture form = family: winding cell + recipe software + inline QC (C33) + test magnets (C15); $3–8M/yr machines, $20–60M/yr family ceiling.
7. Founder built the core artifact once already (laser-aligned automated NI-HTS winding machine, undergrad).
8. C33's red-team patent kill overturned on claim language (US11749434B2 requires inter-coil comparison; US11101059B2 requires striated secondary tape) [DD-C33-01/02].
9. China is supply chain + competitive intelligence, not a market (国产替代 procurement preference; domestic-only tenders) [DD-C12-08][P-32].
10. Capital to v1 ~$2.5–3.5M; first revenue 2030.

**Kill gate:** 3 paid commitments from non-integrated magnet builders by mid-2030 (interview gate mid-2027: <3 credible machine/QC buyers → pivot to C06).

## 2. C10 — Precision magnet & scientific power converters, fast-dynamics wedge — **76.8** (DD, Medium)

1. Verified wedge: fast-dynamics, telemetry-rich, modular converters 5 kW–multi-kA, sold as product with weeks–months lead time.
2. 48% of surveyed fusion companies name power systems their #1 supply bottleneck [DD-C10-14][S058].
3. Catalog-ppm framing dead: CAENels FAST-PS stops at 900 W; Danfysik owns slow-dynamics high-stability [DD-C10-01/02]; ppm lives in the DCCT, not the switch [DD-C10-06].
4. China fusion tenders captured domestically (爱科赛博, 荣信汇科, 英杰电气) [DD-C10-23/24] — radar, not market.
5. Beachhead SAM ~$15–25M/yr; SOM $1.5–4M by 2031; must earn Series A through expansion.
6. Natural seller of electronics into the C12 customer base; designated absorber of C11 protection line + C35 LLRF assets.
7. DOE-milestone fusion companies hit PDRs 2027–2029 [S058].
8. Capital to v1 ~$2.5–4M; first revenue 2030.

**Kill gate:** if 2026–27 interviews show fusion buyers won't pay for lead time + dynamics, stop.

## 3. C06-pivot — Protection-intelligence modules for 800 VDC AI data centers — **74.8** (DD, Medium; strongest non-magnet alternative)

1. Original SSCB dead: ABB SACE Infinitus and Siemens SENTRON 3QD2 ship today [DD-C06-03/04].
2. Survives as the layer NVIDIA itself names the open innovation area: per-rack ground-fault LOCATION + series-arc discrimination on ungrounded 800 VDC buses [DD-C06-01].
3. Sold through power-system integrators, not hyperscalers directly.
4. Red-team "China slot taken" claim rebutted by vendors' own filings: TYT pilot-stage share, Liangxin pre-research [DD-C06-16/18].
5. China's 800 V standards window opened later than the US one (first white paper Aug 2025) [DD-C06-20].
6. Cleanest policy archetype in the Round-1 mission (d: ✅✅✅).
7. Beachhead $15–35M/yr run-rate by 2030–31; capital to v1 ~$1.5–3M; first revenue ~2031.

**Kill gate:** if NVIDIA/OCP reference designs embed protection intelligence in power-shelf firmware by end-2027, fold.

## 4. C01/C03-merge — Aviation-class power bricks (50–500 kW, ≥10 kW/kg) for uncrewed/fast electric craft — **69.6** (DD, Med-Low pivot; diversified third lane)

1. Catalog-PEBB and crewed-marine tiers occupied: GE Vernova holds ONR PEBB productization [DD-C01-01]; Danfoss iC7-Marine/ABB own the cabinet tier [DD-C01-06/25].
2. Surviving wedge: marine-ruggedized continuous-density bricks for USVs and foiling craft, procured outside heavyweight shock-qual.
3. Real budgets: $200M obligated to one 24-ft USV vendor Dec 2025 [DD-C01-12]; Navy STTR topic specifies "approaching 100 kW/L" [DD-C01-10].
4. Red-team $2–5M test-capex objection belongs to the retired MVDC framing; pivot needs $150–400K regen rig [DD-C01-11].
5. China: zero option value (defense lane) [P-19][P-20]; CSSC-captive chain [DD-C01-21].
6. Watch H3X — can flank from integrated motor drives into standalone bricks [DD-C01-08].
7. SOM ~$10–15M/yr by 2032; first revenue 2030 (NRE) / 2031 (product).

**Kill gate:** USV-builder LOI by end-2028.

## 5. C27 — 250 °C multi-market harsh-environment power platform — **68.0** (DD, Low-Med)

1. Merchant power slot above ~230 °C verified empty: Honeywell/Ozark sell chips/loggers, not power [DD-C27-01/05]; Watt&Well stops at 220 °C [DD-C27-12].
2. 250 °C buildable from catalog + screened parts (no cleanroom) [DD-C27-06].
3. But current merchant POs ≈ zero; beachhead $2–9M/yr and grant-fed [DD-C27-13]; oil capex falling.
4. Needs the DOE superhot-geothermal bridge plus aero/space adjacents to become venture-scale.
5. Founder fit strong (harsh-env packaging, UHV/high-T experience).

**Kill gate:** DOE superhot awards materialize (passive tripwire); no merchant PO path by 2028 → shelve.

---

## Fallback chain (frozen from Round 1)

**C12 (primary) → C06-pivot → C01/C03 → C27 → C23** (deep-fit emergency fallback: JEP203
SC-bench + compliance software wedge, 65.6).

A V-candidate displaces an incumbent only by beating it within the comparability convention AND
surviving the identical red-team + deep-dive discipline. The Phase-6 showdown renders that verdict.
