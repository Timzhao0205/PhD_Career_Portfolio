# Project brief - Magnetic-field sensors review (MDPI *Sensors*)

The master reference for every stage. When in doubt, follow this file plus
`prompts/_shared_system.md`.

## 1. What the paper is
A broad, vendor-neutral **review** of magnetic-field sensors: the commercial and
pioneering device families, their strengths and weaknesses, where they are used
today across four application domains, where the field is going (data-driven
modeling, machine-learning control, multi-modality / digital-twin), and the
industry standards + commercial potential that a business or investor audience
needs to orient themselves.

Two audiences, addressed without dumbing either down:
- **Technical** (sensor/instrumentation researchers, hardware engineers).
- **Business / investor** (needs TRL, market framing, standards, risk).

Target journal: **MDPI *Sensors*** (ISSN 1424-8220). Submission target: **before
30 Oct 2026**. Stage 00 fetches the live Instructions for Authors; honor whatever
it records in `outputs/00_target_journal_brief.md` (structure, reference style,
review-article expectations, structured abstract, ethics/《author-contribution》
sections).

## 2. Structure (author's 5-part plan; middle three are ~equal thirds)
1. **Introduction** - why magnetic sensing matters; the measurement problem
   (field range vs resolution vs bandwidth vs size/cost/power/temperature);
   scope and contributions of the review; how it is organized.
2. **Sensor types + current applications** - taxonomy with operating principle,
   performance envelope, strengths/weaknesses, commercial maturity vs pioneering
   status, representative devices/vendors; then current use across the four
   domains.
3. **Future applications** - data-driven modeling, ML-based readout/control,
   sensor fusion, multi-modality, and digital twins built on magnetic sensing.
4. **Potential + standards** - market/《TRL》framing, the standards landscape,
   qualification and metrology traceability; what a company/investor should look
   for and de-risk.
5. **Conclusion** - synthesis, open challenges, outlook.

## 3. Sensor taxonomy to cover (Section 2 backbone)
For EACH family: physical principle; typical field range & resolution
(state units, e.g. pT/nT/µT and noise floor in pT/√Hz where known); bandwidth;
size/power/cost tier; temperature behavior; strengths; weaknesses/failure modes;
commercial maturity (mass-market / niche / lab-only) with representative vendors
or devices; and pioneering directions. Cite everything.

Commercial / established:
- **Hall effect** (Si, and wide-bandgap GaN/2DEG variants; spinning-current
  offset cancellation; integrated CMOS Hall).
- **Magnetoresistive**: AMR, GMR (spin-valve), **TMR** (magnetic tunnel
  junctions) - the workhorse of position/angle/current sensing.
- **Fluxgate** (weak-field, high accuracy).
- **Search-coil / induction** (ac fields, geophysics).
- **Giant magnetoimpedance (GMI)**.

High-sensitivity / specialized & pioneering:
- **SQUID** (ultimate sensitivity, cryogenic).
- **Optically pumped magnetometers (OPM / SERF)** - wearable MEG/MCG.
- **NV-diamond (nitrogen-vacancy) magnetometry** - room-temperature quantum,
  spatial resolution, current/battery sensing.
- **Magnetoelectric composites**, **MEMS/Lorentz-force**, **fiber-optic /
  magneto-optic**, resonance (NMR/Overhauser) magnetometers.

A compact comparison table (range, resolution, bandwidth, cost, maturity,
typical use) is expected - populate only with sourced numbers.

## 4. The four application domains (current use, Section 2 tail)
Give concrete, cited deployments per domain; note which sensor family fits and
why.
- **Energy**: current sensing in power electronics & inverters, smart-grid /
  substation monitoring, battery-management (EV pack current & state-of-charge),
  contactless dc metering, wind/renewables condition monitoring.
- **Transportation**: automotive position/angle/speed (steering, throttle,
  BLDC/EV motor commutation, wheel-speed/ABS), current sensing for traction
  inverters, e-compass/navigation, rail and aerospace.
- **Industrial & manufacturing**: non-destructive testing / eddy-current & MFL
  pipeline inspection, motor & bearing condition monitoring / predictive
  maintenance, robotics & encoders, proximity/position, process metrology.
- **Biomedical**: MEG and MCG (OPM & TMR/OPM arrays), magnetic particle imaging,
  GMR/TMR biosensors & lab-on-chip, catheter/instrument tracking, wearables.

## 5. Future methods (Section 3)
- **Data-driven modeling**: learned calibration, temperature/《aging》drift
  compensation, offset & 1/f-noise mitigation, soft-sensing/virtual sensors.
- **Machine-learning control & readout**: ML denoising and fast readout (e.g.
  quantum-sensor readout), adaptive biasing, closed-loop compensation, anomaly
  detection / predictive maintenance.
- **Sensor fusion & multi-modality**: magnetic + inertial/optical/thermal;
  gradiometer arrays; array signal processing; source localization.
- **Digital twin**: model-based twins of the sensor + its environment for
  calibration transfer, health monitoring, and design optimization.
Highest hallucination risk lives here - be conservative and cite hard.

## 6. Potential + standards (Section 4)
- **Functional safety & automotive**: ISO 26262 (and its IEC 61508 parent),
  ISO/PAS 21448 (SOTIF), ISO/SAE 21434 (cybersecurity), ASIL context for
  position/current sensors; redundancy/diagnostics (SEooC).
- **Industrial**: IEC 61508, IEC 62443 (OT security), relevant IEC/IEEE sensor
  and EMC standards.
- **Medical**: IEC 60601, ISO 13485, ISO 14971, and regulatory pathway framing
  (FDA/CE) for magnetic biosensing/MEG devices.
- **Metrology / traceability**: calibration to NIST/PTB references, magnetic
  field standards, uncertainty budgets.
- **Commercial framing**: TRL ladder per family, representative market sizing
  (cite market/industry analyses; label estimates), IP/patent landscape signals,
  supply-chain & qualification risk. Clearly separate sourced facts from framing.

## 7. Quality bar
Submission-grade: accurate, current (favor last ~5 years for state-of-the-art,
classics for fundamentals), quantitative where the literature allows, and
honest about maturity and open problems. Every number and non-obvious claim is
cited. Peer-reviewed preferred; preprints only to discover, then cite the
version of record; vendor material tagged and used only for device facts.

## 8. Deliverables (what the run must leave in `outputs/`)
- `10_titles.md` - 15 title options.
- `20_outlines.md` - 3-4 complete outlines, detailed to subtopics.
- `30_litreview_sensor_types.md`, `40_litreview_applications.md`,
  `50_litreview_future_methods.md`, `60_standards_and_business.md` - sourced
  section briefs (annotated, citation-carrying, not final prose).
- `references.bib` + `reference_registry.csv` - deduplicated, DOI-verified,
  peer-review status flagged.
- `00_DELIVERABLE_paper_plan.md` - the finalize-by-Friday pack: recommended
  title + shortlist, recommended outline, section-by-section annotated briefs
  with citations, and a coverage/gap matrix.
- `00_target_journal_brief.md` - the digested *Sensors* requirements.
- `PATCH_NOTES.md` - what ran, models/effort/cost, and what to improve next.
