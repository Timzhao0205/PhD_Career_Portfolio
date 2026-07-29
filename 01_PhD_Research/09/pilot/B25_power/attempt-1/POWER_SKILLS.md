# POWER_SKILLS — B25_power (PILOT)

**PILOT SAMPLE — NOT FINAL**

Stage: `B25_power` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Present-vs-missing skills for the four pilot architectures (P3R2-C-01,
P3R2-C-13, P3R2-F-06, P3R2-E-10), grounded strictly in B10's
demonstrated-vs-proposed ledger and B20's five founder-fit corrections.
Acquisition paths are strategic estimates, labeled as such — not hiring or
professional advice. **Governing rule, stated up front: magnetic-sensor
expertise alone does not suffice to design, qualify, or certify a power
converter. Nothing below implies otherwise.**

## 1. Present skills (B10 "demonstrated" only)

| Skill | B10 evidence | Honest bound |
|---|---|---|
| Hall readout-chain design, EMI-disciplined bench measurement | C03, C13 | Small-signal instrumentation; offset suppression shown on a resistor-ring EMULATOR, not the real die; the ~109x anomaly (C04) is open and, by the project's own rule, blocks calibration work |
| Harsh-environment sensor packaging and in-vessel deployment | C46, C01 | One execution (LCC/encapsulation/150C vacuum bake/graphite shield); 150C bake ≠ power-converter thermal design; deployed module's location/health unknown (C45) |
| Component-level UHV practice | C46 | Component scale, not chamber/system scale |
| Qualitative in-plasma measurement campaign execution | C01 | Voltage-domain, uncalibrated output; qualitative correlation only |
| Commissioning/directing AI-agent research and evidence-ledger missions | C16, C17, C50 | Explicit provenance caveat (C50): ledgers/roadmaps were produced by commissioned AI missions, not personal research labor; hardware/bench work is researcher-attributed |

None of these are power-conversion skills. B10's demonstrated ledger
contains no converter, gate-drive, magnetics, HV, protection, HIL,
certification, or manufacturing entry of any kind.

## 2. Proposed-only (NOT present; may never be)

| Skill claim | B10 status | Gate |
|---|---|---|
| Traceable calibration with GUM/Monte-Carlo uncertainty budgets (WP-C) | C06 proposed | Gated by C04 anomaly closure; no calibration of the real device has ever been attempted (C15) |
| Estimator/identifiability methodology (fusion, honesty tests) | C23 inferred, C31 proposed | Folder-08 pre-redteam (C40); FT-02 honesty test unexecuted |
| Bandwidth-fusion design | C08 proposed | Blocked in practice by the unverified 1 MHz readout figure (C05, status unknown) |
| Radiation-compensation architecture | C09 proposed | Zero GaN/AlGaN radiation data exists (C29/M1); collaborator-led by design |

## 3. B20's five founder-fit corrections, applied here

1. **C-01 (new06 D02 §14 corrected):** "power-electronics engineering...
   the founder's core stack" is NOT supported — no power-electronics work
   exists in B10's demonstrated ledger. Carried into the C-01 row.
2. **A-10 (new06 D08 §14 corrected):** "system identification and
   deterministic closed-loop control are the founder's core" — those are
   proposed Opt2 elements (C23/C31, pre-redteam C40). Applied here to every
   smart-protection/discrimination claim (C-01) and any control-loop claim
   (C-13): estimator skill is proposed, not demonstrated.
3. **C-05 (new06 D03 corrected):** bench DAQ is demonstrated (C03/C13);
   scaled/domain metrology is not. Applied to F-06: bench-scale precision
   discipline does not equal station-grade, utility-qualified metrology.
4. **D-02 (new06 D01 §14 corrected):** array instrumentation and
   line-speed/industrial DAQ are not demonstrated skills. Applied to F-06's
   multi-channel station-instrumentation ambitions.
5. **D-10 (new06 D04 corrected):** "founder's home ground" claims without
   ledger support are rejected. Applied as the general rule: no row in this
   stage accepts a founder-fit assertion that B10 cannot back.

## 4. Missing skills per architecture, with acquisition paths

Time/cost figures are order-of-magnitude strategic estimates (labeled EST),
not quotes. Routes: HIRE (bring in specialists), PARTNER (design house /
manufacturer / lab), TRAIN (founder retraining), BUY (purchase capability
as equipment/services).

**P3R2-C-01 — full end product (protection shelf).** Missing: SiC
fault-interruption design; energy absorption/coordination; kA
busbar/thermal; arc discrimination at power scale; IEC 62477-1-class
certification execution (S-B25-01); DFMEA/manufacturing/reliability; OCP
spec design-in. Acquisition: HIRE a senior power-electronics/protection
team plus a certification lead (EST: 2-4 senior engineers, 12-24 months to
a certifiable prototype; multi-$M program per the corpus-dated venture
record) — this is a company build, not a skills add-on. TRAIN is not
realistic inside the ~2028 PhD horizon (C38/C42). The founder-shaped entry
is the telemetry/qualification sliver via PARTNER (sell measurement
discipline to the breaker builder), which PB-1 tests for
~$8k-25k EST.

**P3R2-C-13 — subsystem (OEM module).** Missing: GaN gate drive (EV08);
nanosecond pulse-shaping stages and low-inductance layout; magnetics;
EMC compliance; laser-diode application engineering; OEM qualification;
export-compliance handling. Acquisition: HIRE/PARTNER (a small
power-design team or a contract design house; EST: 1-2 senior power
engineers, 9-18 months to an evaluable module — consistent with the
record's own $72k make-vs-buy first gate before any build). TRAIN:
gate-drive and pulsed-power layout competence is plausibly the cheapest
converter skill for an instrumentation person to acquire (bench-scale,
low-voltage variants exist), but EST 1-2 years of dedicated practice and it
still would not cover OEM qualification. Founder-shaped entry: calibrated
pulse-current telemetry qualification (PB-1) — measurement, not the
module.

**P3R2-F-06 — measurement-qualification tool.** Missing: FOCS sensor
physics; zero-flux DCCT electronics at incumbent 1 ppm grade (S-B25-02);
HV insulation coordination; utility/station qualification + field service;
instrument manufacturing. Acquisition: the modality hardware should be
BUY/PARTNER, not build — merchant zero-flux references exist at grades a
startup will not beat (S-B25-02; LEM per the old06 record fetch), so the
buildable layer is the qualification protocol, uncertainty budgets, and
system integration on purchased transducers. That layer is exactly the
WP-C methodology (C06) — currently proposed-only, gated by C04; executing
WP-C inside the PhD is therefore the acquisition path (EST per the corpus:
~19-29 bench-days to a Tier-1 calibration package once C04 closes, C06),
plus PARTNER with one utility/EPC or magnet lab for a first qualification
engagement. Utility-facing field-safety competence: HIRE/PARTNER (field
commissioning is a safety-rated trades domain — same honesty note as
B20's G-03 row).

**P3R2-E-10 — reference design (space PPU).** Missing: space
power-electronics design; SET/SEB mitigation; ECSS/AIAA qualification
flows; thermal-vacuum design; flight heritage. Acquisition: not
realistically acquirable founder-side in any relevant window; the only
sensible route is COLLABORATE — join someone else's irradiation campaign
with Hall-plate coupons (BT-5/FT-11, collaborator-led per C09). Recorded
as an experiment channel, not a skills plan.

## 5. Cross-cutting acquisition summary

- The founder's realistic near-term capability growth is entirely on the
  measurement/qualification side: close C04, execute WP-C (C06), pass FT-02
  (C31) — converting proposed methodology into demonstrated credential.
  Every power-facing wedge in this pilot depends on that conversion; none
  of it makes the founder a converter designer.
- Converter-stack capability comes only by HIRE/PARTNER at company scale;
  any plan that assumes otherwise repeats the founder-fit overstatements
  B20 corrected.
- Safety/certification competence (IEC 62477-1-class campaigns, utility
  acceptance, space qualification) is organizational, not individual — it
  is acquired by building or joining an organization that has it. This
  stage's analyses are research planning, not safety or certification
  approvals.
