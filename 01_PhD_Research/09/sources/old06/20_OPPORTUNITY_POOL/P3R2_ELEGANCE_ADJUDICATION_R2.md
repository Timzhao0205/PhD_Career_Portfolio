# P3R2 elegance/novelty adjudication — second pass (wave F + fix verification)

Adjudicator: independent judge, claude-fable-5 / xhigh (configured route; no delegation).
Date: 2026-07-13. Inputs: `P3R2_F_cn_topup.{json,md}` (23 seeds), the first-pass ruling
`P3R2_ELEGANCE_ADJUDICATION.md` (calibration + survivor list), the post-fix seed files
`P3R2_A–E *.json` (elegance_verdict / fix_applied_notes fields), `P3R2_FIX_APPLICATION_LOG.md`,
`10_SOURCE_ATLAS/ATLAS.md` (negative findings), lane ledgers for source spot-checks, and
`05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.md` + prefilter (42 quarantined IDs). Firewall respected:
founder profile and prior `SEEDS_A–D` drafts were NOT read; no founder-fit content appears
below. No seed files were modified.

## 1. Method and compliance checks

Same protocol as the first pass: scores 0–10 on novelty / elegance / controllability / vision /
timing-robustness; verdict PROMOTE / FIX (exact repairs) / REJECT (reason); no curve — a CN
quota need does not lower the bar.

- **Quarantine:** grep of all 42 quarantined India-origin IDs against `P3R2_F_cn_topup.json`:
  zero matches. Clean.
- **Source spot-checks (load-bearing CN anchors):** L06-042/043/044/048/051/052/054 (STAR-market
  filings, localization reporting), L01-037/038 (ASIPP tender PDFs), L04-048/051 (Chaotan
  One / CCTV, RMB100B correctly single-source-flagged), L05-012/013/035/036/038 (IHEP, CGN
  filings, mofcom cyclotron tender), L08-034 (XJ RMB1.275bn), L10-028/031/034/035/040/045/046
  (XCMG–Fortescue, SPIC Oyu Tolgoi, China Gold / Baogang tenders, CCS 2025 rules, GB/T
  45926-2025), L11-049/050/051 (Kuqa, LONGi/Peric, CEC 125-set), L16-028..033 (Jiaocheng
  filing 2022 — stale, flagged; MPW literature), L01-114/115 (Wuxi Shennan tender, Nordson
  10-K), L12-037/038/050 (Han's/Raycus filings, ISO 11553-2:2007), L14-035/039/043/048 — all
  exist in the ledgers, accepted, country-specific, non-quarantined. The wave's CN evidence is
  genuinely CN-specific; no seed leans on a bare "Asia" claim, and F-19 explicitly refuses the
  debunked L14-036 "100% liquid-cooling mandate." One external spot-check (F-17 EU enforcement
  on handheld Class-4 welders) found ecosystem safety activity (European welding associations'
  handheld-laser materials) but **no dated enforcement action** — F-17's trigger remains
  undated, adjudicated accordingly.
- **Atlas negative findings:** no F seed sells electrolyzer stacks (F-15/F-23 are
  balance-of-plant/controls and say so), none relies on grid-forming service procurement, none
  proposes two-phase cooling without a fluid plan (F-07 names water-glycol/low-GWP non-PFAS).
  EM pulse welding (F-11) is not an atlas enthusiasm zone; its bridge is the documented
  equipment-buyer channel — accepted, with the demand caveat below.
- **Datacenter cap:** 1/23 self-declared (F-19); within cap.

Verdict totals for wave F: **3 PROMOTE, 15 FIX, 5 REJECT** (of the rejects, F-18 and F-21 are
self-flagged merges into F-03 and F-02; F-08 and F-14 carry import notes).

## 2. Wave-F duplication map (vs pool F and vs surviving A–E canonicals)

| F seed | Nearest survivor(s) | Ruling |
|---|---|---|
| F-01 | A-10 (IEDF process control) | Distinct complement — A-10 senses/serves the process; F-01 delivers impedance. Confirmed. |
| F-02 | D-01 (quench detect/protect), C-09 | Distinct complement — D-01 triggers, F-02 drives and dumps; mirrors the endorsed A-02/E-14 split. |
| F-03 | C-08 (PCHE), C-19 (seals/bearings) | Distinct — electrical vs thermal-mechanical side of the same machines. **F-18 merges in** as CN chapter. |
| F-04 | C-19, D-19 | Distinct — no survivor sells bearing electronics; D-19 is a customer. |
| F-05 | A-21 (charging), B-14 (interface) | Distinct — vehicle-side kit; B-14's interface bought as a module, not rebuilt. |
| F-06 | E-14 (DC protection relay/qual) | Distinct complement — measurement layer under E-14's intelligence layer. |
| F-07 | B-14, A-21, B-01 | Distinct — duty-cycle thermal/contact engineering; B-01 is rack cooling, different market. |
| F-08 | A-02 (MVDC breaker) | Component to A-02-class OEMs — **REJECT**, import die-characterization workstream into A-02. |
| F-09 | C-09, D-07 | Distinct component niche (RF-vacuum interface); pair commercially with C-09/D-07. |
| F-10 | D-02 (style only) | No NDT survivor; distinct. |
| F-11 | C-09 (different application) | Distinct; same CN demand anchor as F-10 (L16-028) — evidence overlap, not concept overlap. |
| F-12 | C-01 (different rules/buyers) | Distinct; only marine class-rule play in the pool. |
| F-13 | A-21/B-14/A-14 (none close) | Distinct but **REJECT** on merit (below). |
| F-14 | F-01 / A-10 / rejected B-15, B-12 | **REJECT** — licensing-variant of F-01's CN chapter; B-12 precedent. Import licensing mechanics into F-01. |
| F-15 | C-07 (rectifier), C-22 (benches), F-23 | Distinct socket (park DC distribution / per-stack management); boundary coordination required. |
| F-16 | A-22, rejected B-15 | Distinct (metrology-differentiated tool, not plasma power). |
| F-17 | C-13 (laser industry only) | Distinct — new territory (photonics safety). |
| F-18 | F-03, C-08/C-19 | **Duplicate of F-03** (self-flagged) — merge as CN plant-integration chapter. |
| F-19 | C-05 (qual benches), E-02 (control) | Boundary confirmed by this adjudication: C-05 = lab qualification; F-19 = in-service operations + consumables. Distinct; pair, do not merge. |
| F-20 | C-09 (pulsed vs DC) | Distinct product class; fold-down path into C-09 family if OEM appetite fails. |
| F-21 | F-02, E-04/C-12 (not close) | **Duplicate of F-02** (self-flagged) — entry SKU. |
| F-22 | F-01 (component vs system) | Conditionally distinct — pre-agree P4 merge into one RF-components company if both survive. |
| F-23 | C-22 (offline benches), C-07 | Distinct complement — always-on plant device; C-22 calibrates the maps F-23 enforces. |

**Cluster-concentration warnings for the freeze:** (1) L06 RF chain now carries A-10 + F-01 +
F-22 (+ B-06): cap final picks. (2) L11 now carries C-07 + C-22 + F-15 + F-23 against documented
Western hydrogen fragility: final portfolio should carry at most two. (3) L10 heavy
electrification carries A-21 + B-14 + F-05 + F-07 + F-12: coordinate, do not double-fund
interface work. (4) Superconducting BOP (D-01, D-02, F-02, C-12) is fusion-schedule-correlated.

## 3. Per-seed adjudication (scores: Novelty / Elegance / Controllability / Vision / Timing)

**F-01 — 6/7/7/7/7 — PROMOTE.** Solid-state microsecond matching is the strongest new dual seed:
the atlas documents matching as unresolved research (L06-001/002/003) yet none of the 100
first-round seeds proposed it — genuine non-obviousness by the convergence test. Clean
complement to A-10 (impedance delivery vs process control), honest key uncertainty (vacuum-cap
voltage/Q parity at 60 MHz), cheap decisive experiment, and a CN leg built on eligible
country-specific evidence (<12% component localization L06-054; named growing buyers) with
mature-node scoping and a 2027 export gate. Main risk is incumbent absorption (Comet Synertia
is exactly a fast-match platform) — the kill trigger covers it. Absorb F-14's
licensing-with-golden-reference mechanics as the CN chapter's IP structure.

**F-02 — 5/7/7/7/7 — PROMOTE.** Drive-and-dump skids ride a real structural change (merchant
magnet commerce, L03-035) with dated CN tender evidence (ASIPP L01-037/038) and honest
big-science-only CN access. The D-01 complement split mirrors the endorsed A-02/E-14 pattern.
Two promote-conditions: P4 must map OCEM/Danfysik-class catalog magnet-PSU incumbency (the
"nobody productized" claim is overbroad — precision converters are catalog items; the true
white space is the integrated extraction/dump + leads + acceptance-protocol island), and CFS
bundling stays the named ceiling. **Absorb F-21** as the entry SKU (catalog leads/feedthroughs,
certified heat-load data, end-2031 <$1M entry-milestone).

**F-03 — 5/6/5/7/6 — FIX.** The electrical cartridge fills a real in-pool gap (no survivor owns
the electrical half of heat-to-power machines) with dual dated anchors (Fervo–Turboden
turbine constraint; Chaotan One + first-set follow-on). But the merchant white-space claim must
survive Calnetix-class incumbency (they sell exactly high-speed PM + converter for ORC), and
the CN TAM is single-source. Fixes: (1) P4 incumbent map centered on Calnetix/turbine-OEM
in-house before promotion; (2) the 2029 machine-builder co-development agreement becomes a
binding gate; (3) CN retrofit TAM triangulated from eligible sources before any scale
assumption; (4) **absorb F-18** as the CN plant-integration/licensing chapter; (5) stage the
$900k experiment (largest in the wave) behind the requirements-interview findings.

**F-04 — 5/6/6/6/6 — FIX.** Merchant AMB electronics with semiconductor-grade shock recovery is
a defensible instrument-adjacent wedge (L07-010..013 documents 30+ years of unresolved
reliability), but the thesis lives or dies on OEM externalization, and the CN leg is the
wave's thinnest (INFICON APAC revenue attribution is not buyer evidence). Fixes: (1) 2028 paid
OEM evaluation as binding proof pump OEMs will externalize; (2) P4 teardown of SKF S2M /
Calnetix / Waukesha merchant controllers vs the semiconductor-duty claim; (3) CN leg
conditional: name a CN pump/tool-OEM design-in channel in P4 or downgrade primary_market to
US; (4) keep the 2032 internal kill.

**F-05 — 5/5/6/6/6 — FIX.** The genuinely novel leg is selling Western-certification competence
to CN exporters (XCMG–Fortescue needing UL/IEC/MCS-certified electronics) — an honest
foreign-founder position. The US "no standardized repower kit" claim is likely overstated.
Fixes: (1) P4 competitive teardown vs Danfoss Editron / Dana TM4 / BAE off-highway kits; state
the defensible core as the UL/IEC/GB certification matrix + dual-personality interface, not
kit existence; (2) CN OEM export-certification engagement LOI by 2028; (3) unsubsidized
repower economics by 2028 (EPA grants mostly fund new equipment — the repower inference needs
evidence); (4) buy B-14's interface personality as a module, do not rebuild it.

**F-06 — 5/7/7/6/6 — FIX.** Elegant measurement-layer complement to E-14 with a cheap
round-robin decisive experiment. But the seed's own text concedes State Grid is domestic-only
and CN revenue is "license royalties at best" — the same condition that downgraded C-12/C-21.
Fixes: (1) **honesty flag change: primary_market US+CN → US, china_beachhead → false** (CN
license chapter stays in text; do not count this seed toward CN quota); (2) the 2029 OEM/EPC
evaluation agreement becomes binding, and go/no-go is paired with E-14-class third-party
protection traction (the merchant sensing socket exists only if that layer wins); (3) P4 map
of Hitachi/ABB optical-CT incumbency — the wedge must be demonstrated combined
accuracy+bandwidth+open-protocol, not asserted.

**F-07 — 6/6/6/6/6 — FIX.** Duty-cycle thermal/contact engineering for MW charging and swap
couplers is real no-man's-land, and the CN swap evidence (SPIC, GB/T 45926, CCS) is genuinely
country-specific. But the seed itself flags that no eligible source documents CN conductive
MW-charging demand and swap-side procurement openness is unproven. Fixes: (1) P4 confirmation
that CN swap-equipment component procurement is open to licensed outsiders — the CN leg's
binding gate; (2) 2028 charger-OEM co-development binding; (3) connector-major incumbent map
(Staubli/Phoenix/Huber+Suhner) — wedge must be proven by the 10,000-mate-cycle dataset;
(4) sequence port/mining (funded) before trucking (MCS-volume risk).

**F-08 — 5/6/4/7/3 — REJECT.** Double contingency: a component supplier to breaker/valve OEMs
whose own market (meshed MVDC) is the atlas's documented unconverged "showstopper" — one level
deeper into the same unproven stack as A-02, without A-02's productization wedge. The offered
demand anchors don't hold: GEV's datacenter electrification orders are not MVDC-protection
procurement, and State Grid valve tenders are license-out-only. If meshed DC arrives,
Infineon/Hitachi/Fuji press-pack scale absorbs the socket before a startup qualifies
breaker-grade die. Import into A-02: the 2027 interruption-duty SiC die-characterization study
and fail-short press-pack qualification concept as A-02's device-strategy workstream — cheap,
publishable, and useful regardless.

**F-09 — 5/6/6/5/6 — FIX.** Documented failure mode (L05-014), real qualification wedge, honest
small-TAM admission. The killer question is whether tube primes buy reliability-critical
"internal art" from a startup. Fixes: (1) 2028 evaluation windows inside one named rebuild
program (ARDAP channel) as binding gate; (2) P4 evidence on prime merchant-buy behavior — if
negative, re-scope to lab spares/aftermarket and size honestly; (3) keep the
two-paying-customers-by-2032 kill; (4) evaluate one beam-components portfolio company with
C-09/D-07 adjacency at P4.

**F-10 — 7/7/6/6/5 — FIX.** Highest-novelty dual seed (no NDT play existed in 100 prior seeds);
laser-UT at line rate is a real mechanism with a make-or-break metric the seed itself names
(POD-at-speed). The US pipeline leg's trigger (ISO/ASTM edition cycles) is too soft to carry
demand. Fixes: (1) CN demand bridge binding: battery-equipment OEM co-development/design-in
LOI by 2028 (equipment channel documented; inline volumetric QC demand is inferential); (2)
refresh L16-028 (2022-vintage buyer concentration) with a current filing; (3) de-weight the
pipeline leg until a named operator/NDT-service evaluation exists by 2028; (4) POD/speed kill
(end-2029) binding; (5) P4 incumbent check incl. Tecnar-class industrial laser-UT.

**F-11 — 7/7/6/6/5 — FIX.** Productizing magnetic-pulse welding for Al–Cu interconnects is
genuinely non-obvious (15-year "renaissance" never productized — and the seed correctly
identifies coil-consumable economics as both the historical blocker and the wedge). It is
technology-push: no battery maker has asked for MPW. Fixes: (1) coil-life gate (>=10,000 shots
at spec by end-2028) binding — it is the entire engineering thesis; (2) CN integrator
co-development agreement by 2028 with the IP split contractualized (founder retains pulsed
power + recipes; integrator sells); (3) cost-per-joint and line-rate model vs ultrasonic AND
laser welding by 2028 — laser is the real substitute; (4) refresh the 2022 L16-028 evidence.

**F-12 — 6/6/7/6/7 — PROMOTE.** The best CN-primary seed of the wave and the model for what
this wave was commissioned to produce: a dated, country-specific regulatory trigger (CCS
Rules 2025 edition, effective 2025-12-31, with a documented ~2-year revision cadence), a
national-benchmark vessel class (Jining "6006"), a clause-mapped product whose moat is the
type-approval dossier, an honest JV access structure that concedes manufacturing and retains
protection IP + type approval, a clever $300k decisive experiment (class design appraisal),
and a named kill condition (CATL bundling the full electrical stack). P4: confirm the
non-CATL integrator/shipyard share and map CSSC-affiliated suppliers; scope the DNV/ABS export
hedge.

**F-13 — 5/4/6/5/5 — REJECT.** The tenders are real and dated (Baogang, July 2026) but the
structure fails the mission's wedge rule in the hardest-access market: Huawei-ecosystem
integrators self-supply hardware, CRRC-class suppliers can replicate a functional-safety kit
quickly (nothing in the physics is hard), foreign content in SOE mine-safety chains is
politically fragile (self-flagged), tender scale (RMB3.75M inside an RMB18.06M project)
implies project-shaped, thin-margin revenue, and the seed admits the atlas technical base is
thin. Demand without a defendable technical wedge — the archetypal rejection for this wave.

**F-14 — 4/5/5/5/4 — REJECT.** B-12 precedent applies in full: in a license-into-China model
for process know-how, the licensee is the accumulating asset. The seed names its own central
mechanism as the kill risk (licensee R&D, poached teams) and Hengyunchang's RMB1.5B IPO
proceeds fund in-house capability, not durable dependence; golden-reference retention does
not survive the seed's own 2032 absorption horizon. The lawful-scope question A-10 already
carries is not improved by making the CN side the whole company. Import into F-01: the
licensing-with-golden-reference/test-bench structure and the Hengyunchang/Injet buyer evidence
as the mechanics of F-01's CN chapter.

**F-15 — 6/7/6/6/5 — FIX.** "String-inverter moment for hydrogen" is the wave's most elegant
CN-primary framing, built on documented multi-set procurement (L11-050/051), documented
underutilization (Kuqa), and documented shunt/stray-current physics — while respecting the
L11 stack-overcapacity negative finding. The demand mechanism (SOE audits forcing utilization
retrofits) is inferential; no park-management tender exists yet. Fixes: (1) the 2028 EPC
retrofit-study partnership is the binding demand gate — measured park losses must justify skid
cost (>=3% target); (2) Sungrow/LONGi verticalization kill trigger kept (product before a 2031
pilot = kill); (3) P4: evidence that a licensed JV can win park-management retrofit scope at
one named SOE park; (4) boundary coordination with C-07 (rectifier) and F-23 (stack
envelope) — one L11 power story, three sockets, at most two funded.

**F-16 — 5/6/7/6/6 — FIX.** Metrology-differentiated plasma treatment converts the rejected
B-15 knife-fight into a treat-to-spec premium tool, with a documented open procurement channel
(L01-114) and a durable category (Nordson 10-K). What's documented is category demand, not
metrology-premium demand. Fixes: (1) the 2028 beta must carry a paid premium commitment
(>=30% premium thesis tested before the 2030 gate, not at it); (2) the 2027 experiment must
validate inline surface-energy proxy robustness at line rate — the stated key uncertainty;
(3) P4: Nordson MARCH / Panasonic / Samco roadmap check, since closed-loop treat-to-spec is
absorbable by the incumbent premium tier.

**F-17 — 6/6/7/5/4 — FIX.** Real gap (no laser-tool-specific safety silicon; ISO 11553-2 dated
2007 vs documented export explosion), tiny option cost, honest self-labeling. But the entire
demand thesis is an undated regulatory contingency — verified by this judge's external check:
European welding-association safety materials exist, but no dated enforcement action was
found. Fixes: (1) hold as a priced option — cap pre-company spend at the $150k prototype until
a dated signal exists; (2) 2028 gate: a documented ISO/IEC revision work-item, an EU/US
market-surveillance action on handheld Class-4 welders, or an insurer/OEM requirement — one of
the three, or kill at the existing end-2030 trigger; (3) P4 chases the welding-association
safety materials for an eligible dated anchor; (4) OEM design-in LOI remains the second gate.

**F-18 — 4/5/5/6/5 — REJECT (duplicate of F-03; self-flagged).** The CN-primary licensing
variant of F-03's cartridge in the same CNNC ecosystem with the same single-source TAM.
Import into F-03: the EPC co-bidding memorandum concept, Xinjiang first-set timeline
alignment, and the rollout-industrialization framing.

**F-19 — 6/6/6/7/6 — FIX.** The water-treatment-industry analogy (consumables + telemetry on
installed fluid) is a real business archetype and the only F seed with a defensible
datacenter-correlated position (aging fluid is downturn-resistant). Direct pain evidence is
admittedly thin and CDU-vendor absorption is the default outcome. Fixes: (1) P4 must source
operator incident/warranty data (the seed's own flag); (2) 2028 colocation pilot + one
operator LOI binding; (3) the 12-month aging study must produce the failure-signature dataset
that IS the moat, else the concept is a Vertiv feature — the existing bundling kill trigger
stands; (4) boundary with C-05 confirmed (lab qualification vs in-service operations): pair
commercially, do not merge prematurely.

**F-20 — 4/5/6/5/5 — FIX.** The thesis rests on a competitive claim held only as judgment
("effectively one dominant vendor"). Adversarial reality: Advanced Energy (HiTek/UltraVolt),
AMETEK/Glassman, Matsusada, iseg, Heinzinger, Technix and CN HV makers all sell precision HV —
if any is a credible OEM second source, this collapses to niche lab supply. Fixes: (1) P4
competitor map is a pre-promotion requirement — the mid-band-gap claim must survive it;
(2) two paid OEM evaluations by 2028 binding; (3) CN leg reduced pending evidence: CGN Dasheng
builds accelerators, but no eligible source shows CN OEMs outsourcing precision HV — name a
CN OEM/tender channel in P4 or the CN chapter becomes license notes; (4) pre-agree the
fold-down of the DC-HV line into C-09's platform family if OEM appetite fails.

**F-21 — 4/6/7/5/6 — REJECT (duplicate of F-02; self-flagged fold).** Import into F-02: the
catalog binary-lead SKU as entry product, instrumented feedthroughs, certified heat-load
datasheets, and the end-2031 <$1M standalone milestone (becomes F-02's entry-SKU gate).

**F-22 — 5/5/6/5/6 — FIX.** Single-source arbitrage on the tuning component (Comet's own
23.8% single-customer concentration evidences the brittle structure) with a sensible
dual-track hedge into solid-state elements. The craft barrier cuts both ways: precision
brazing/bellows is the moat and the reason a $450k experiment does not make a qualified line.
Fixes: (1) the vacuum-components manufacturing-partner route becomes a binding 2027 gate;
(2) P4 must map existing CN vacuum-capacitor makers — if credible domestic caps exist, the CN
licensing leg collapses; also verify the Comet/Jennings supply structure; (3) one OEM paid
qualification by 2029; (4) portfolio pre-agreement: if F-01 and F-22 both survive P4, merge
into one RF-components company — two L06 RF-chain startups is one too many.

**F-23 — 6/7/7/7/6 — FIX.** The most intelligent new L11 seed: converts published
stress-degradation science into envelope enforcement + notarized evidence — bankability
hardware, with genuinely independent legs (H2Hub lender exposure US; Kuqa-class utilization
audits CN) and a strong 2,000 h A/B decisive experiment. The demand mechanism is
anticipatory: developers buy only if lenders force it. Fixes: (1) binding 2029 gate: one named
H2Hub lender/financier technical requirement or a developer LOI referencing instrumented
warranty evidence, plus one OEM design-in agreement; (2) the A/B experiment must show a
measurable degradation-rate reduction — it is the product's existence proof; (3) data-interface
pre-agreement with C-22 (its benches calibrate F-23's maps) — no duplicate bench build;
(4) the battery/fuel-cell warranty retarget hedge must be scoped by 2029, not asserted.

### Wave-F summary table

| Seed | N | E | C | V | T | Verdict | Duplicate of |
|---|---|---|---|---|---|---|---|
| F-01 | 6 | 7 | 7 | 7 | 7 | PROMOTE | — |
| F-02 | 5 | 7 | 7 | 7 | 7 | PROMOTE | — |
| F-03 | 5 | 6 | 5 | 7 | 6 | FIX | — |
| F-04 | 5 | 6 | 6 | 6 | 6 | FIX | — |
| F-05 | 5 | 5 | 6 | 6 | 6 | FIX | — |
| F-06 | 5 | 7 | 7 | 6 | 6 | FIX (flag → US) | — |
| F-07 | 6 | 6 | 6 | 6 | 6 | FIX | — |
| F-08 | 5 | 6 | 4 | 7 | 3 | REJECT | import → A-02 |
| F-09 | 5 | 6 | 6 | 5 | 6 | FIX | — |
| F-10 | 7 | 7 | 6 | 6 | 5 | FIX | — |
| F-11 | 7 | 7 | 6 | 6 | 5 | FIX | — |
| F-12 | 6 | 6 | 7 | 6 | 7 | PROMOTE | — |
| F-13 | 5 | 4 | 6 | 5 | 5 | REJECT | — |
| F-14 | 4 | 5 | 5 | 5 | 4 | REJECT | import → F-01 |
| F-15 | 6 | 7 | 6 | 6 | 5 | FIX | — |
| F-16 | 5 | 6 | 7 | 6 | 6 | FIX | — |
| F-17 | 6 | 6 | 7 | 5 | 4 | FIX (option) | — |
| F-18 | 4 | 5 | 5 | 6 | 5 | REJECT | F-03 |
| F-19 | 6 | 6 | 6 | 7 | 6 | FIX | — |
| F-20 | 4 | 5 | 6 | 5 | 5 | FIX | — |
| F-21 | 4 | 6 | 7 | 5 | 6 | REJECT | F-02 |
| F-22 | 5 | 5 | 6 | 5 | 6 | FIX | — |
| F-23 | 6 | 7 | 7 | 7 | 6 | FIX | — |

## 4. Fix-verification (first-round FIX seeds and flag changes)

Sample of 8 of the 25 first-round FIX seeds, spread across batches, checked against required
fixes in the first-pass ruling by reading current JSON content (not just the log):

| Seed | Required fixes | Ruling |
|---|---|---|
| A-03 | Field-hardware demand documentation gate; drop GFM leg (NESO); complement to E-14 | **VERIFIED** — 2027 written-guidance/LOI gate in plan; GFM leg dropped with NESO cited and AEMO demoted to watch-item; E-14 complement positioning in competition field. |
| A-16 | Productized SKU + process license; 2028 anchor-packager LOI; head-to-head kill gate | **VERIFIED** — product rewritten as SKU family + licensed dispensing package, services bounded; both gates present verbatim. |
| B-14 | 2028 named-export-program procurement evidence; pre-agreed fold-in to A-21; keep certification-moat argument | **VERIFIED** — gate, fold-in path, and "contingent option" demand classification all present; certification-burden argument retained. |
| B-22 | Named design-win LOI by 2028; retrofit SKU + cross-vendor database moat; US market kept active | **VERIFIED** — all three present in product/plan/risk fields. |
| C-04 | Adopt B-01 negative-pressure mechanism as primary; fluid-menu dataset second moat; retain 2031 fluid kill | **VERIFIED** — product rewritten around the subatmospheric loop (L14-053 added), dataset moat named, kill trigger retained and extended; confidence downgraded high→medium (appropriate). |
| C-12 | P4 competitor map pre-promotion; license-only CN; staged capex | **VERIFIED** — all three present; D-03/B-11 imports (catalog skids, buyers) applied; flags changed. |
| D-11 | E-13 stricter CE>=4%/2033 gate; acqui-license exit stated; no capital before gate; Gigaphoton hedge | **VERIFIED** — kill date moved to 2033-12 with the imported gate; capital rule and open acqui-license statement in plan; Gigaphoton (L12-053) added. |
| E-02 | Two OEM development agreements by 2028; merge fallback into B-01/C-04 stack; shipment-share kill binding | **VERIFIED** — HARD GATE wording present incl. the "as consultant/licensor, not operating company" pre-company nuance; fallback and binding kill present. |

**Market-flag changes:** A-10 `primary_market` US → **US+CN** with `china_beachhead: true`
(partitioned >=28nm entity, B-05/C-06 imports, eligible CN sources added) — matches ruling.
C-12 US+CN → **US**, `china_beachhead: false` — matches. C-21 US+CN → **US**,
`china_beachhead: false`, v1 capex capped to $10–25M — matches. All three confirmed in file.

Fix-verification outcome: **8/8 VERIFIED, 3/3 flag changes correct.** The
`P3R2_FIX_APPLICATION_LOG.md` accurately reflects file state everywhere sampled.

## 5. Quota reckoning — final distinct-concept survivor set across A–F

Survivors = PROMOTE + FIX_APPLIED/FIX records after all merges (merged and rejected records
are not counted).

- **A–E (44):** A-02, A-03, A-05, A-10, A-11, A-13, A-14, A-16, A-21, A-22 | B-01, B-06,
  B-14, B-22 | C-01, C-02, C-03, C-04, C-05, C-07, C-08, C-09, C-12, C-13, C-19, C-21, C-22 |
  D-01, D-02, D-07, D-08, D-09, D-10, D-11, D-12, D-13, D-16, D-18, D-19, D-20 | E-02, E-04,
  E-11, E-14.
- **F (18):** F-01, F-02, F-12 (PROMOTE); F-03 (+F-18), F-04, F-05, F-06, F-07, F-09, F-10,
  F-11, F-15, F-16, F-17, F-19, F-20, F-22, F-23 (FIX). F-02 absorbs F-21.
- **Total distinct concepts: 62.**

Market counts (using post-fix flags, with this ruling's F-06 downgrade to US applied; F-04
counted dual-conditional):

| Gate | Requirement | Count | Result |
|---|---|---|---|
| Total distinct concepts | >=48 | **62** | PASS |
| Lanes covered | >=14 | **16** (L01–L16) | PASS |
| Credible US legs (US or US+CN) | >=36 | **53** (A–E 40; F 13 incl. F-06 as US) | PASS |
| Credible CN legs (CN or US+CN) | >=36 | **35** (A–E 18: B-01/B-06/B-14/B-22 + 14 dual; F: 12 dual + 5 CN-primary F-11/F-12/F-15/F-16/F-17) | **FAIL by 1** |
| Dual (US+CN) | >=24 | **26** (A–E 14 + F 12) | PASS |
| JP/TW/KR-primary | <=8 | **0** | PASS |

**Verdict: the pool does NOT yet pass all longlist gates — the CN gate stands at 35/36.**
The swing item is this ruling's honesty downgrade of F-06 (CN = license royalties at best, the
same condition that downgraded C-12/C-21); reversing it to hit the quota would fabricate CN
credibility and is refused. Sensitivity: if P4 fails to evidence F-04's CN OEM channel or
F-20's CN outsourcing channel, CN drops to 33–34; if F-17's undated trigger is judged
disqualifying at freeze, 34.

**What is missing and how to close it honestly (in preference order):**
1. **Targeted micro-wave G (2–3 CN-credible seeds)** in eligible-evidenced spaces no survivor
   uses: (a) CN big-science vacuum/components against the HEPS tender cadence (L07-045);
   (b) CN accelerator/cyclotron component localization against the mofcom centralized
   procurement pattern (L05-036) beyond F-20's HV slice; (c) CN 800VDC conversion-base
   retrofit/commissioning instrumentation against documented integration pain (L02-054),
   distinct from C-01's protection product. Route wave G through this judge before freeze.
2. **P4-conditional upgrades already wired:** if F-04's named CN pump/tool-OEM design-in
   channel or F-20's named CN OEM/tender channel is evidenced, CN reaches 36–37 without new
   seeds (these seeds are counted dual-conditional; their failure is also priced above).
3. **Do not** resurrect F-13/F-14, re-flag F-06, or promote CN chapters that are license-only
   upside — that is quota-driven fabrication, the exact failure mode this review exists to
   block.

## 6. Structural notes for the orchestrator

1. **The wave achieved its purpose with real evidence, not mirrors.** All 23 CN legs cite
   country-specific eligible sources (tenders, GB/CCS standards, STAR/SZSE filings); access
   paths (licensing, JV, OEM design-in, HK structures) are stated with margin/IP caveats.
   Weakest CN legs in surviving seeds — F-04 (revenue attribution), F-20 (no outsourcing
   evidence), F-07 (swap procurement openness), F-19 (audit-event inference) — are all gated.
2. **Stale-source flag:** L16-028 (Jiaocheng buyer concentration) is 2022-vintage and carries
   both F-10 and F-11's CN channel; refresh before final scoring per rule 18.
3. **Single-source flag:** the RMB100B sintering-retrofit TAM (L04-051) touches F-03/F-18;
   triangulation is a pre-scale gate, correctly carried.
4. **Import obligations from this ruling:** F-21→F-02 (entry SKU); F-18→F-03 (CN chapter);
   F-14→F-01 (licensing mechanics); F-08→A-02 (SiC interruption-duty workstream).
5. **Concentration caps at portfolio selection:** L06 RF chain (A-10/F-01/F-22/B-06), L11
   (C-07/C-22/F-15/F-23 — max two), L10 (A-21/B-14/F-05/F-07/F-12), fusion-correlated BOP
   (D-01/D-02/F-02/C-12).
