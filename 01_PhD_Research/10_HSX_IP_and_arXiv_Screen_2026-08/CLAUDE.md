# Binding project rules

This workspace has one task: evaluate potential intellectual property disclosed
in the manuscript **AlGaN/GaN Hall-Effect Sensor for In-Situ Magnetic Field
Monitoring of the HSX Stellarator**, then prepare an arXiv/OTL decision package.

## Scope

- Read `IP_SCOPE.md` before analysis.
- Treat the supplied PDF, TeX file, and original source ZIP as the only technical
  disclosure to evaluate.
- Do not import startup concepts, TCAD/simulation work, three-axis probes,
  Hall-coil architectures, radiation-compensation architectures, future PhD
  plans, or unpublished readout inventions.
- A cited paper or a sentence naming future work is prior art/context; it does
  not make that cited or future technology part of this manuscript's invention.
- Never broaden the task merely because excluded archives existed elsewhere.

## Operation

- Work only inside this folder despite the parent session's full permission.
- Use the named stage agents in `MODEL_PLAN.md` sequentially. Do not substitute a
  cheaper model for a Fable-assigned accepted result.
- Update `state/STATE.json`, `state/WORKLOG.md`, and `state/MODEL_LOG.csv` after
  every stage. Checkpoint after every accepted stage.
- Preserve existing accepted outputs on resume. Repair only the failed gate.
- Do not invent telemetry. Record `not_exposed` when the interface does not
  expose actual model, effort, tokens, turns, cost, or duration.
- Do not send email, submit an OTL disclosure, file a patent, upload to arXiv,
  modify the manuscript, or communicate externally. Drafts and checklists only.

## Evidence

- Search current sources; follow `SOURCE_POLICY.md`.
- No arbitrary source quota exists. The stage passes when every coverage area is
  searched to reasonable saturation and each material proposition is traceable.
- Distinguish a patentability screen from freedom-to-operate. This package does
  neither a legal opinion nor an exhaustive clearance search.
- Do not infer patentability from novelty of scientific publication, "first"
  deployment, commercial usefulness, or successful experimentation alone.

## Fable integrity policy

- `switchModelsOnFlag` is false. Never accept a safety-fallback result as a
  Fable result.
- On the first Fable flag, refusal, or unverified model substitution: quarantine
  that attempt, log the event, restate the same benign research outcome in
  narrower professional language, and retry once on Fable 5/xhigh.
- On the second such event for the same stage: stop, set state to `PAUSED`, write
  `state/PAUSE.md`, and preserve all outputs and logs for manual continuation.
- Availability errors are not safety downgrades. Log them and pause without
  silently routing to any other provider or model.

## Deliverable standard

Every conclusion must state: manuscript feature, evidence, closest prior art,
delta, uncertainty, practical value, and recommended action. The final brief
must lead with a decision and explicitly address whether (1) the Hall sensor
itself, (2) its fusion-diagnostic use, and (3) the UHV/GDC package combination
merit OTL review before arXiv.
