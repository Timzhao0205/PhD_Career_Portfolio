# POWER_SKILLS — B25_power (FULL)

Stage: `B25_power` | Mode: `FULL` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Present-vs-missing skills across the full 31-row POWER_MAP set, grounded
strictly in B10's demonstrated-vs-proposed ledger (the accepted capability
ground truth) and B20's five founder-fit corrections, extended by one new
correction this stage documents against the startup corpus. Acquisition
paths are strategic order-of-magnitude estimates (EST) drawn from records
where the records themselves state figures — not hiring, legal, or
professional advice. **Governing rule, stated up front and applied to every
row: magnetic-sensor expertise alone does not suffice to design, qualify,
or certify a power converter, protection product, or power supply. Nothing
below implies otherwise.**

## 1. Present skills (B10 "demonstrated" only)

| Skill | B10 evidence | Honest bound |
|---|---|---|
| Hall readout-chain design, EMI-disciplined bench measurement | C03, C13 | Small-signal instrumentation; offset suppression shown on a resistor-ring EMULATOR, not the real die; the ~109x anomaly (C04) is open and, by the project's own rule, blocks calibration work |
| Harsh-environment sensor packaging and in-vessel deployment | C46, C01 | One execution (LCC/encapsulation/150C vacuum bake/graphite shield); 150C bake is not power-converter thermal design; deployed module's location/health unknown (C45) |
| Component-level UHV practice | C46 | Component scale, not chamber/system scale |
| Qualitative in-plasma measurement campaign execution | C01 | Voltage-domain, uncalibrated output; qualitative correlation only |
| Commissioning/directing AI-agent research and evidence-ledger missions | C16, C17, C50 | Explicit provenance caveat (C50): ledgers/roadmaps were produced by commissioned AI missions, not personal research labor; hardware/bench work is researcher-attributed |

None of these are power-conversion skills. B10's demonstrated ledger
contains no converter, gate-drive, magnetics, HV, protection, dump,
cryogenic, HIL, certification, or manufacturing entry of any kind — for
any of the 31 rows.

## 2. Proposed-only (NOT present; may never be)

| Skill claim | B10 status | Gate |
|---|---|---|
| Traceable calibration with GUM/Monte-Carlo uncertainty budgets (WP-C) | C06 proposed | Gated by C04 anomaly closure; no calibration of the real device has ever been attempted (C15) |
| Estimator/identifiability methodology (fusion, honesty tests) | C23 inferred, C31 proposed | Folder-08 pre-redteam (C40); FT-02 honesty test unexecuted |
| Bandwidth-fusion design | C08 proposed | Blocked in practice by the unverified 1 MHz readout figure (C05, status unknown) |
| Radiation-compensation architecture | C09 proposed | Zero GaN/AlGaN radiation data exists (C29/M1); collaborator-led by design |

Every wedge argument in POWER.md §9 depends on converting the first two
rows from proposed to demonstrated. That conversion is the acquisition
plan for the founder's side of this stage — and none of it makes the
founder a converter designer.

## 3. Founder-fit corrections applied (B20's five, plus one documented here)

1. **C-01 (new06 D02 §14):** "power-electronics engineering... the
   founder's core stack" is NOT supported by B10. Carried into C-01 and
   the whole DC-protection family (A-02, F-12, C-15, ST01-C06P).
2. **A-10 (new06 D08 §14):** system-identification/deterministic-control
   claims are proposed Opt2 elements (C23/C31, pre-redteam C40). Applied
   to every smart-protection/discrimination claim (C-01, ST01-C06P,
   ST01-C11, D-01) and every control-loop claim (C-13, F-01, F-23,
   ST05-CF-4).
3. **C-05 (new06 D03):** bench DAQ is demonstrated (C03/C13);
   scaled/domain metrology is not. Applied to C-05 (multi-kW calorimetry),
   F-06 (station-grade metrology), G-03 (field acceptance), D-09
   (dosimetry-grade traceability).
4. **D-02 (new06 D01 §14):** array instrumentation and industrial DAQ are
   not demonstrated. Applied to ST03-ID_13's array measurement layer and
   F-06's multi-channel station ambitions.
5. **D-10 (new06 D04):** "founder's home ground" claims without ledger
   support are rejected — the general rule for every row.
6. **NEW this stage — startup-corpus founder profile (documented
   divergence, not adopted).** `startup/03 .../FOUNDER_PROFILE_V3.md`
   asserts "high-power-density power electronics," undergrad applied
   superconductivity (a "fully automated laser-aligned NI-HTS coil winding
   machine"), battery magnetic imaging, full-stack hardware breadth, and a
   ~2029 finish; DD_C10 asserts "exceptional founder fit (power
   electronics x precision instrumentation)." **None of this appears in
   B10's accepted ground truth**, which covers the PhD corpus (graduation
   target ~summer 2028 per C42; zero accepted publications per C49; no
   power-conversion, cryogenic, or battery-imaging hardware anywhere in
   C01-C50). This stage records the assertions as corpus-internal,
   unverified statements and does NOT adopt them as capabilities — per
   correction rule 5. If they were later independently evidenced, the
   ST01-C10/ST03 rows' founder-fit calls (not their market analysis)
   would need revisiting; until then, treating them as true would repeat
   exactly the overstatement pattern B20 corrected five times.

## 4. Missing skills by family, with acquisition paths

Routes: HIRE (specialists), PARTNER (design house/manufacturer/lab/OEM),
TRAIN (founder retraining), BUY (equipment/services), COLLABORATE
(piggyback on others' campaigns). Time/cost EST unless record-cited.

**(a) Converter design core** (all full-end-product and subsystem rows;
sharpest in ST01-C10, ST03-ID_08/13, C-13, F-01, C-09, C-14): topology and
control; SiC/GaN gate drive (EV08 open burden); magnetics; EMI/EMC; thermal;
DFM/reliability. Acquisition: HIRE/PARTNER at company scale — the startup
corpus's own honest plan is a 3-5 person company by first shipment with a
power-magnetics engineer and compliance-experienced ME by month 12
(record-cited). TRAIN: bench-scale low-voltage converter competence is
plausibly acquirable by an instrumentation person (EST 1-2 years dedicated
practice; the startup records' RTP plans assume exactly this on evenings) —
but bench bring-up is not OEM qualification, and this stage does not adopt
the startup corpus's assumption that the founder already has it (§3.6).

**(b) Protection and interruption engineering** (C-01, A-02, E-14, F-12,
ST03-ID_10, D-01's dump side): fault interruption physics, energy
absorption, kA busbar/thermal, arc validation, dump/crowbar hardware.
Acquisition: HIRE only, company build (EST 2-4 senior engineers, 12-24
months to a certifiable prototype, multi-$M — corpus-dated venture
records). Not founder-trainable inside the PhD horizon (C38/C42).

**(c) Safety certification and compliance** (every product row):
IEC 62477-1-class campaigns (S-B25-01); NRTL UL 61010-class + CE LVD/EMC
(record-cited $150-300K and 6-9 months for a first family, ST01-C10);
marine classification (F-12); space qualification (E-10/D-16); export/
classification handling (C-13, D-10, ST01-C10's ECCN 3A226 flag —
record-level, unverified). Acquisition: organizational — acquired by
building or joining an organization that has it; never an individual
skill add-on. This stage's analyses are research planning, not safety or
certification approvals.

**(d) Field commissioning and utility qualification** (G-03, F-06, E-14,
C-07): safety-rated electrical trades work, station acceptance, protocol
authority with operators. Acquisition: HIRE/PARTNER (field-safety-rated
staff or an EPC partner); the founder-shaped part is only the
measurement-uncertainty/dossier content (PB-2), never the field work.

**(e) Application-domain disciplines:** electrochemistry (C-07/C-22/F-23 —
HIRE/PARTNER; the scarce skill per B20); laser/photonics (C-13, D-10 —
PARTNER at most; D-10 ADVERSE); plasma/RF engineering (F-01, C-14 —
PARTNER); space power (E-10, D-16 — COLLABORATE only, PB-7); cryogenics/
HTS practice (ST01-C10/C11, ST03-ID_10, ST05-CF-4 — literature exists
(EV05/EV21) but B10 evidences no cryo practice; TRAIN at bench-77K scale
is plausible EST months-scale, record RTPs assume it; PARTNER via the
magnet-lab community, S-B20-02); rotating machines (F-03, D-19 — retire).

**(f) Precision electrical metrology at acceptance grade** (the W1/W2
lane: F-06, G-03, C-05, D-09, ST03-ID_12, PB-1/PB-2): the ONE family
adjacent to demonstrated skills. Acquisition path is concrete and mostly
in-plan: close C04; execute WP-C (C06 — record EST ~19-29 bench-days to a
Tier-1 package once C04 closes); pass FT-02 (C31); then exercise the
methodology on current measurands via PB-1/PB-2 (EST $8-25K + $3-10K,
BRIDGE_TESTS.md). BUY the reference hardware (1 ppm-class zero-flux
transducers exist merchant, S-B25-02; 8.5-digit DMM class per the ID_12
record) rather than build it. What this path does NOT buy: qualification
AUTHORITY (round-robin standing, dossier acceptance by operators/lenders)
— that is earned through PARTNER engagements (one utility/EPC, one magnet
lab, or one conformance body) and publication, EST 1-3 years of
engagements after the credential exists.

## 5. Cross-cutting summary

- The founder's realistic near-term capability growth is entirely on the
  measurement/qualification side (family f): close C04, execute WP-C,
  pass FT-02, then PB-1/PB-2. Every wedge in POWER.md §9 depends on that
  conversion; none of it makes the founder a converter designer.
- Converter-stack, protection, and certification capability come only by
  HIRE/PARTNER at company scale; any plan assuming otherwise repeats the
  founder-fit overstatements B20 corrected — including, now, the startup
  corpus's own profile assertions (§3.6), which remain unverified against
  the accepted ground truth.
- The startup corpus's invention RTP plans (ID_08/10/12/13, CF-4) are
  documented, costed engineering plans by their own missions; where this
  stage reuses them it reuses their PROBLEM evidence and measurement
  content, not their assumption of founder converter competence.
- Safety/certification competence is organizational, not individual.
  Research planning here is not a safety approval, an export
  determination, or legal advice (SOURCE_POLICY).
