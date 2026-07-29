# PHD_CORE — PhD research core (PILOT)

**PILOT SAMPLE — NOT FINAL**

This document summarizes only what is evidenced by the ten pilot claims in
`PHD_FACTS.json` (C01–C10). It is a pilot-scope sample of a much larger
corpus (`sources/phd`, 1145 files) and must not be read as a complete
account of the PhD research, its assets, or its gaps. Extraction, not
ranking: nothing below scores, ranks, or recommends a portfolio decision.

## 1. Recent/current work, as evidenced by the pilot sample

- **Deployment (demonstrated, C01).** A packaged AlGaN/GaN Hall-effect
  sensor module was fabricated, packaged, and deployed in-vessel near the
  HSX stellarator plasma edge during the August 2025 campaign. Raw
  shot-resolved voltage transients and a qualitative correlation with
  diamagnetic-loop stored energy exist in the raw data archive
  (`sources/phd/P/01/07_HSX_august2025_results/hsx_20250821/`).
- **Publication status (demonstrated, C02).** The resulting manuscript
  (IEEE Sensors Letters, Manuscript ID SENSL-26-07-RL-1061) was submitted
  2-Jul-2026 and declined 23-Jul-2026, with an invitation to revise and
  resubmit under a new Manuscript ID. Zero accepted first-author
  publications currently exist.
- **Bench readout-architecture validation (demonstrated, C03/C04).** On a
  resistor-ring bench emulator (not the real sensor die), current-spinning
  demodulation suppressed a raw offset by ≥130× — but the same test also
  produced an unresolved ~109× magnitude anomaly relative to the expected
  bridge output. The project's own rule is that no calibration work may
  start until this anomaly is closed; it is the single highest-priority
  open bench task in the corpus's own plan.
- **Unverified figure (unknown, C05).** The manuscript's stated 1 MHz
  readout bandwidth is asserted twice with no derivation anywhere in the
  manuscript, its references, or the project's own specs. The reviewer
  letter explicitly disputes it. This pilot marks the true bandwidth as
  unknown rather than accepting the manuscript's own unverified figure.

## 2. Assets, as evidenced by the pilot sample

- A packaged, previously-deployed AlGaN/GaN Hall sensor module and its
  associated readout electronics (bias/demod chain), firmware, and
  analysis scripts (evidenced by C01, C03, C04; hardware/firmware
  directories at `sources/phd/P/01/02_HSX_Hall_Sensor_Readout/`).
  These pilot claims did not extract firmware/circuit file inventories in
  depth — a full run should catalog them explicitly.
- Raw HSX August-2025 shot data (scope traces, coil-current logs,
  stored-energy data) usable for further supplied-data analysis without
  new hardware or campaign time (C01; corroborated in
  `sources/phd/P/01/06/outputs/03_MANUSCRIPT_DIAGNOSIS.md` §4.1, not itself
  one of the ten pilot claims but read as supporting context).
- A documented, not-yet-executed calibration plan (WP-C) and a documented,
  not-yet-built reusable simulation/estimator package specification
  (C06, C10).

## 3. Evidence quality, as evidenced by the pilot sample

- Demonstrated claims in this pilot (C01–C04) trace to primary artifacts:
  raw HSX data files, a dated lab-notebook-style project NOTES.md, and a
  manuscript/decision-letter audit. C02 (submission/decline status) is
  read from a corpus synthesis document, not the original decision letter
  PDF directly — the pilot did not re-open the underlying PDF.
- Two of the five current-work claims are explicitly non-final: C04 (open
  anomaly) is an unresolved discrepancy, and C05 (bandwidth) is marked
  unknown rather than accepted at face value.
- The Opt2-related claims (C06–C10) trace to
  `sources/phd/P/01/06/outputs/` (the completed, redteamed, and
  stage-80-synthesized folder-06 mission) and to
  `sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/outputs/`
  (the folder-08 mission, which per the B00 inventory has completed only
  10 of 12 stages and has **not** passed its own `70_redteam` or
  `80_synthesis` steps). Every C06–C10 claim in this pilot notes that
  caveat explicitly where the citation is to folder 08.

## 4. Gaps, as evidenced by the pilot sample

- No calibration of the real (non-emulator) Hall die exists (gap behind
  C06, blocked by C04's open anomaly).
- No hardware demonstration of coil→Hall gain tracking exists in fusion
  conditions; the coil→Hall direction rests on structural-identifiability
  derivation, not experiment (C07).
- No GaN/AlGaN Hall-plate radiation (neutron) dataset exists in the
  literature reviewed by the corpus; the radiation-drift magnitude for
  this device family is Unknown (C09).
- No reusable simulation/estimator code has been built yet; only a module
  boundary specification exists (C10).
- This pilot did not extract publication/venue-route claims, the
  disclosure/IP-hold gates, the 24-month roadmap milestones, or the
  advisor-meeting materials in any depth — those exist in the corpus
  (`sources/phd/P/01/06/outputs/`) but are out of the ten-claim pilot
  scope and must be covered in the full run.

## 5. Transferable skills, as evidenced by the pilot sample

Evidenced directly by C01, C03, and C04: in-vessel sensor packaging and
deployment in a live fusion research device; bench emulator-based
readout-chain design, current-spinning bias/demodulation circuit design
and firmware development; systematic bench-anomaly diagnosis (leakage and
gain-resistor elimination) under an explicit no-calibrate-until-resolved
discipline. Evidenced by C06/C08/C09/C10 as *proposed* (not yet
demonstrated) skill areas the Opt2 continuation would exercise: traceable
absolute calibration methodology (GUM/Monte-Carlo uncertainty budgeting),
multi-channel sensor-fusion estimator design (Kalman-filter-class), and
scientific software packaging with a frozen interface/regression
discipline. The pilot does not have enough claims to state this list is
exhaustive; a full run should extract skills evidence more broadly (e.g.,
literature synthesis work, IP screening, and grant/roadmap planning
visible elsewhere in `sources/phd/P/01/06/outputs/`).

## 6. What the full run must add

See `OPT2.md` for the corresponding Opt2-side list. On the PHD_CORE side,
the full run must add: complete publication/venue-route history; full
hardware/firmware/circuit inventory; full raw-data inventory across all
HSX campaigns (not just August 2025); the disclosure/IP-hold checklist
status; the 24-month roadmap and its milestone/gate detail; and a
complete transferable-skills list drawn from the entire corpus rather
than the ten pilot claims.
