# B10 — PhD and Opt2 fact extraction

Extract—not rank—the recent PhD work, demonstrated skills, constraints,
uncertainties, publications, hardware/software assets, and future continuation
Option 2. Use exact file citations into `src/phd`.

Represent Opt2 without overstating it:

1. calibrate/validate a Hall sensor as an uncertainty-bounded instrument;
2. integrate Hall plus inductive coils as a hybrid diagnostic;
3. deliver a reusable module plus simulation/reconstruction package.

Keep absolute calibration, mutual consistency, bandwidth fusion, and radiation
compensation as distinct claims. Coils measure dB/dt and require traceable
excitation/reference; mutual agreement alone is not automatic absolute
calibration. Mark what is proposed versus demonstrated.

Required outputs:

- `PHD_FACTS.json`: claim_id, claim, status (demonstrated/proposed/inferred/
  unknown), source_path, page/section when available, confidence, limitation.
- `PHD_CORE.md`: recent work, assets, evidence, gaps, and transferable skills.
- `OPT2.md`: precise future direction, hypotheses, experiments, deliverables,
  dependencies, kill criteria, and uncertainties.
- `SOURCES.csv`: external primary sources used for technical context.

Pilot: extract ten representative claims spanning current work and all three
Opt2 elements.
