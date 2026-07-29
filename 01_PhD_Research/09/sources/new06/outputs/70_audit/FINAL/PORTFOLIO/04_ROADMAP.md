# Validation roadmap 2026-2030 — budgets, pass thresholds, kill thresholds

Every experiment below is executable by 2028 (enforced at stage 40) and
carries a written kill. Tier-1 budgets total $3.47M; all-24 exposure is
$8.30M, with the staged experiments (A-14, C-09) gating internally.
Sources for thresholds: deep dives D01-D10 for the top ten; stage-20 G3
gate definitions for the other fourteen.

## 2026 (H2) — setup and cheapest information first

- **Standing monitors open (no capital):** JBCS solicitation (D-10);
  OCP methodology cadence (C-05); DG Matrix/ABB certification status
  (C-01, quarterly); SPARC installation progress (D-01, D-02); hydrogen
  FID trajectory (C-22, F-23); D-16 downselect tracking; F-16 tender
  watch.
- **Tier-1 starts:** D-02 scanner segment build; C-05 OCP workstream
  participation + TTV design; A-14 packaging-partner selection (stage
  one); D-10 SBIR topic engagement.

## 2027 — the kill-gate year (ten Tier-1 verdicts in flight)

| Idea | Experiment | Budget | Pass threshold | Kill threshold |
|------|-----------|--------|----------------|----------------|
| D-02 | 100 m two-producer blind scan, 50 cut samples | $120k | Ic prediction <5% error on ≥90% of samples; seeded defect classes detected | blind correlation cannot reach 5% across architectures, or mechanical defects indistinguishable from Ic noise |
| C-05 | 16-zone 1.2 kW TTV + 3-lab blind round-robin | $150k | commanded hotspot maps held; calorimetric closure; round-robin discriminates products at stated confidence | TTV cannot hold maps, or lab variance exceeds product differences |
| C-01 | 800 V/250 A hybrid SSCB brassboard (Q2) | $350k | <100 µs bidirectional clearing; 10,000 hot-swap cycles; zero nuisance trips on transient library | clearing or discrimination misses at rated current |
| D-10 | 16-channel CBC lock under 1g vibration (Q2) | $250k | λ/30 rms; >90% combining efficiency; dropout ride-through | either threshold fails under vibration |
| E-14 | HIL benchmark of 3 algorithms + <1 ms relay prototype (Q3) | $300k | ≥1 algorithm family <1 ms with published-grade discrimination; prototype reproduces bench | no algorithm discriminates on the 4-terminal model, or <1 ms unreachable in hardware |
| D-01 | Instrumented REBCO pancake, driven quenches | $250k | ≥100 ms warning; <1% false triggers; fiber survives winding/cycling | warning or false-trigger threshold fails on a real coil |
| A-14 (stage 1) | Packaging stack, 500 thermal cycles to 300 °C (Q2) | $250k | shear + electrical integrity post-cycling | stack fails 500 cycles — stops before stage 2 |
| A-10 | Closed-loop ±2 eV IEDF hold under drift (Q4) + FTO + CN counsel gate | $450k | ±2 eV held across drift matrix; profile-metric correlation shown | hold or correlation fails; FTO conflict unresolved |
| C-09 | Two-module 50 kV/500 A stack, 1% droop, module-swap requalification (Q3); interface spec v1.0 published (Q1) | $500k | droop ≤1% at composition; swap requalifies inside protocol | droop fails at composition, or swap needs bespoke rework |
| C-22 | 50 kW stress bench, 90-day two-vendor campaign (Q4) | $250k | ≥2 literature degradation signatures reproduced on command with mechanism attribution | commanded stress cannot reproduce signatures, or attribution fails |

**Tier-2 experiments run in the same year where evaluation bandwidth
allows:** C-13 8-channel 1 kA driver + TMI trial ($180k; pass:
closed-loop TMI suppression demonstrated; kill: <2 paid OEM evaluations
by 2028 → fold into D-10); F-01 5 kW matcher <10 µs re-match ($250k;
kill: AE/MKS platform integration first); A-05 TiZrV 1-m pipes ($250k;
pass: ≤200 °C activation, sticking within 20% of SAES-class); G-03
perturbation injector on 100 kW testbed ($300k; pass: instability
prediction across ≥20 configurations); E-04 256-channel flex + 4 K mux
($500k; pass: <1% crosstalk, <20% coax heat load); D-09 three-way
FLASH comparison ($150k; pass: <1% calorimetry agreement).

## 2028 — conversion year (demand milestones with dates)

- **Dated conversion milestones (red-team repairs, all binding):**
  D-01 magnet-builder co-test agreement; C-05 paid conformance campaign;
  A-10 fab process-group evaluation LOI; C-09 OEM paid evaluation;
  C-22 paid lender/hub/tender pilot; E-14 developer or ISO/RTO study
  engagement; C-13 two paid OEM evaluations (else fold-in executes).
- **Stage-2 spends unlock on 2027 passes:** A-14 stage two — 8-channel
  front-end, 300 °C/1,000 h, <1% drift ($600k; kill gate two); C-08
  subscale transient rig — 1,000 cycles ≥20 °C/min, 550 °C peaks, ASTM
  E139 creep ($600k); A-22 skid prototype — >99.99% destruction at
  ≤50 kWh/kg, closed fluorine balance ($550k); D-19 rotor rig — 100k
  microcycles, <1% loss growth ($350k); F-23 2,000 h A/B — measurable
  degradation-rate reduction required ($300k, contingent on C-22 pass);
  D-16 turboalternator rig ≥20% cycle efficiency ($500k, contingent on
  the ~April-2027 downselect showing two teams' written interest).
- 64-channel D-10 scaling; C-01 UL/IEC pre-submission already filed
  (2027-Q3); C-04 fluid-pair loop + 1,000 h assay ($400k) as the
  regulatory clock confirms the non-fluorinated wedge.

## 2029 — qualification and pre-launch

- Certification completions: C-01 (two embed design-wins targeted),
  E-14 first paid qualification campaign on a named project, C-05
  protocol published with licensing live.
- Field placements: A-14 module in an R&D well; D-01 qualified dump
  prototype + dossier v1; D-02 paid acceptance pilot + cable/CICC
  station prototype; F-19 aging-loop library complete ($300k); F-16
  premium-commitment beta decision (kill if none by end-2028 carried
  into exercise decision).
- Portfolio checkpoint: every Tier-1 idea has either a named customer
  engagement or an executed kill by 2029-Q4. Ideas killed are not
  replaced (frozen identities); their capital releases to the surviving
  set.

## 2030 — launch year

Launches ride the dated external triggers: Kyber/800 VDC fleet (C-01,
G-03), Shanghai Superconductor's 20,000 km/yr target year and
ARC-class magnet procurement (D-02, D-01), KEPCO first phase and the
HVDC construction wave (E-14), BH/XGS full operation (A-14), CHIPS-fab
production ramps (A-10, F-01), JLWS 300-500 kW scale-up decisions
(D-10, C-13), and the electrolyzer fleet's warranty era (C-22, F-23).
Launch-readiness test per idea: kill gates passed, one paid
customer relationship live, and the 2030-2034 adoption plan in its
deep dive (top ten) or card (others) still matching observed reality.

## Budget recap

| Tier | Ideas | Decisive-experiment total |
|------|-------|---------------------------|
| 1 | 10 | $3.47M |
| 2 | 6 | $2.08M |
| 3 | 8 | $2.75M (trigger-gated; D-16/F-23 additionally contingent) |
| All | 24 | $8.30M |

Worst-case 2027 calendar-year exposure is materially lower than the
headline: staged gates (A-14 $250k first, C-09 single-module first),
trigger-gated Tier 3, and the fold-in discipline (C-13→D-10) mean
capital follows verdicts, never precedes them.
