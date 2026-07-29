# B20 — bidirectional PhD/startup impact

Independently inspect source files plus B00, B10, and the accepted B15
literature evidence; correct support-stage errors. Map every material technical
claim to B15 paper IDs or a stronger primary/official source. Do not cite a
paper merely because B12 found it.
Analyze both directions rather than accepting the user's expectation:

- PhD → startup: technical moat, credibility, data, tools, buyer access,
  validation assets, timing, constraints, and opportunity cost.
- Startup → PhD: useful requirements, experiments, datasets, collaborators,
  publication risk, scope drift, conflicts, and research value.

Cover the complete set of serious old/new directions and retain stable idea
IDs. Distinguish direct leverage, adjacent leverage, speculative transfer, and
negative interference. Show counterfactuals: outcome with Opt2 versus without
Opt2. Avoid claiming causation from thematic similarity.

Required outputs:

- `ALIGNMENT.csv`: idea_id,idea_name,source_version,phd_to_startup,
  startup_to_phd,mechanism,evidence,dependency,time_horizon,conflict,
  confidence,falsifier,action.
- `ALIGNMENT.md`: patterns, strongest/weakest links, asymmetries, and caveats.
- `IMPACT_MAP.md`: causal chains and counterfactuals.
- `SOURCES.csv`: claim-level primary/official or accepted peer-reviewed
  sources, including B15 paper IDs where applicable.

Pilot: analyze six ideas across strong, medium, weak, and adverse alignment.
