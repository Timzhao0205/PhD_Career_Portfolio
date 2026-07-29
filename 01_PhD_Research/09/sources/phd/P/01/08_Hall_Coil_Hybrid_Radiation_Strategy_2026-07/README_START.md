# Start here: Hall + coil hybrid / radiation strategy

This mission performs a fresh, evidence-gated analysis of the proposed
Hall-effect plus inductive-coil architecture. It extends folder `06`; it does
not overwrite it.

## Run

From the parent `01` folder:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1
```

Default `full` mode passes Claude Code `--permission-mode
bypassPermissions`, with the working directory isolated to this folder.
`-Mode guarded` changes the permission mode to `acceptEdits`.

The same command resumes ordinary interruptions. Completed stages are
identified by hashed markers in `state\markers`; partial attempts retain the
Claude session ID, raw JSONL stream, generated prompt, and checkpoint.

## What the run must decide

1. Is the correct sequence Hall-sensor validation first, hybridization second,
   and a reusable module/simulation package third? If not, give a better
   sequence and explain the decision gates.
2. Can coil dynamics help identify radiation-induced Hall gain or bias drift,
   and can Hall DC information correct coil/integrator drift? Under exactly
   what excitation, reference, and observability conditions?
3. Which application or research-group directions deserve collaboration
   effort: tokamak, stellarator, z-pinch/pulsed power, magneto-inertial fusion,
   superconducting machinery/magnets, or another field?
4. What are the architecture's hard limitations, failure modes, prior-art
   constraints, cost/accuracy tradeoffs, and advantages relative to other
   magnetic diagnostics?

## Evidence gates

- At least 120 unique verified peer-reviewed sources in the final ledger.
- At least 75 verified sources new relative to folder `06`.
- Topic quotas: 25 hybrid/coil sources, 30 radiation sources, 25
  applications/alternatives sources, and 20 calibration/identifiability
  sources. One source may support more than one topic.
- Preprints, vendor pages, patents, theses, and general webpages may guide
  discovery but do not count toward the peer-reviewed total.
- Every important recommendation must trace to source IDs or be labeled as an
  inference, proposal, or unanswered question.

## Model policy

Sonnet 5 collects and structures broad evidence. Fable 5 with `xhigh` effort
owns the seven critical-judgment stages. See `MODEL_POLICY.md`.

The runner records requested and reported models, effort, duration, turns,
token usage when reported, cost when reported, web tool counts, validation
status, and source count. See:

- `state\MODEL_EFFORT_LOG.csv`
- `state\PERFORMANCE_LOG.csv`
- `state\OPERATION_LOG.csv`
- `state\CLAUDE_EVENT_LOG.jsonl`

## Fable downgrade policy

Only the model producing the accepted final main response determines a
Fable-stage downgrade. Auxiliary or temporary model use is logged but is not
itself a downgrade.

- First missing/non-Fable final result: save and quarantine outputs, write a
  checkpoint, clarify the benign academic measurement task, start a new Fable
  5 session once with `--safe-mode`, and revalidate.
- Second missing/non-Fable final result in the same cycle: save everything and
  pause. No silent provider fallback.

## Final reading order

1. `outputs\FINAL_EXECUTIVE_DECISION.md`
2. `outputs\FINAL_PLAIN_LANGUAGE_GUIDE.md`
3. `outputs\FINAL_ACTION_PLAN.md`
4. `outputs\02_MUTUAL_CALIBRATION_FEASIBILITY.md`
5. `outputs\03_RADIATION_COMPENSATION_ARCHITECTURE.md`
6. `outputs\04_APPLICATION_SCORECARD.csv`
7. `outputs\05_TECHNOLOGY_COMPARISON.csv`
8. `outputs\FINAL_AUDIT.md`
