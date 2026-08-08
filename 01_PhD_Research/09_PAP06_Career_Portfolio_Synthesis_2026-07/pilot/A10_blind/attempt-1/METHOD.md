# A10_blind pilot method

PILOT SAMPLE — NOT FINAL

- Stage: `A10_blind`
- Mode: `PILOT`, attempt 1
- Worker: `pap06-fable-xhigh` (requested Fable 5 / xhigh)

## Blind-integrity statement

- No old ranking, no new ranking, no prior-stage output, and no file under
  `sources/`, `archive/`, `outputs/`, or any other pilot directory was read.
- No WebSearch and no WebFetch was used at any point in this stage.
- The only evidence inputs were `evidence/blind/MANIFEST.json`,
  `evidence/blind/POOL_1.json`, `evidence/blind/POOL_2.json`,
  `evidence/blind/POOL_3.json`, plus the four root policy files and the task
  card / stage specification.
- All judgments below were made personally by this worker in a fresh context;
  nothing was delegated.

## Deterministic pilot sample (6 of 126)

Rule (from the stage spec and task card): take the FIRST TWO entries, in stored
array order, from each of the three pool shards. This is deterministic because
JSON arrays are ordered and the shards are immutable evidence; any rerun of
this rule selects the same six IDs.

| Shard | Position | idea_id |
|---|---|---|
| `evidence/blind/POOL_1.json` | 1 | `P3R2-A-01` |
| `evidence/blind/POOL_1.json` | 2 | `P3R2-A-02` |
| `evidence/blind/POOL_2.json` | 1 | `P3R2-B-21` |
| `evidence/blind/POOL_2.json` | 2 | `P3R2-B-22` |
| `evidence/blind/POOL_3.json` | 1 | `P3R2-D-19` |
| `evidence/blind/POOL_3.json` | 2 | `P3R2-D-20` |

Only these six were evaluated. The remaining 120 candidates were not evaluated
in this pilot; the full run must cover 126/126 with an explicit coverage proof.
IDs are preserved exactly as stored in the shards.

## Rubric

Each candidate was scored on nine components, each a coarse ordinal integer
1-5 (1 = weak/adverse, 5 = strong/favorable), with a written reason per
component. No weighted numeric total is computed and no decimals are used, to
avoid false precision. Ranking is a holistic judgment across components, with
extra weight in practice on budgeted pain, capital/time to falsification, and
2030-2034 timing, because those dominate expected decision value for a
pre-company founder.

1. `pain_severity_budget` — severity of the buyer's problem and evidence
   (within the candidate record) that a named buyer has budget and urgency,
   not merely discomfort.
2. `technical_feasibility` — realism of the claimed TRL and the physics/
   engineering path to the first decisive prototype.
3. `defensible_edge` — whether the proposed moat (data, certification,
   IP, qualification depth) plausibly survives incumbent response.
4. `founder_phd_adjacency` — scored NON-CIRCULARLY: only on whether the
   candidate's own 2026-2029 pre-company plan is executable inside a
   university research setting (publishable, fundable at the stated budgets,
   using realistically accessible academic facilities). No specific founder
   biography, lane preference, or skill set was assumed.
5. `capital_time_to_falsification` — cost and calendar time to a decisive
   kill-or-continue result, for both the technical and the demand claim.
6. `timing_2030_2034` — whether the demand trigger credibly lands inside
   2030-2034, neither earlier (incumbent lock-in) nor later (window missed).
7. `geographic_portability` — breadth of viable markets and independence from
   any single geography's access or policy risk, as stated in the candidate.
8. `regulatory_safety_friction` — HIGHER score = LESS harmful friction;
   friction that a prepared entrant can convert into a moat scores mid-range.
9. `failure_mode_resilience` — HIGHER score = fewer/more hedgeable failure
   modes; unhedged single-point existential modes score low.

Each object also carries: `decision` (advance = pilot top-3; hold = credible
but outranked, may re-enter on full evaluation; reject = would not carry on
current evidence), `evidence_from_candidate` (items drawn strictly from the
candidate's own record), an `overall_band`, an `uncertainty` level with note,
a `principal_risk`, and a `falsifier` (preferring the candidate's own stated
experiments and kill gates, tightened where needed).

## Tie handling

No exact ties arose among the six. The predeclared rule, which the full run
will reuse: ties are broken in order by (a) lower capital/time to
falsification, (b) stronger candidate-internal evidence of budgeted demand,
(c) fewer unhedged single-point failure modes; if still tied, lexicographic
order of `idea_id` as a deterministic last resort.

## Ranking outcome (pilot)

1. `P3R2-A-01` — advance
2. `P3R2-D-19` — advance
3. `P3R2-B-22` — advance
4. `P3R2-A-02` — hold
5. `P3R2-B-21` — hold
6. `P3R2-D-20` — reject

`TOP10.json` (pilot form) contains exactly the top 3, per the pilot rule.

## Limitations

- Blind evaluation: every market, buyer, price, program, and competitor claim
  comes from the candidate records themselves and could NOT be verified
  against the web or `sources/` in this stage. Lane source IDs cited inside
  candidates (e.g., `L02-043`, `L16-052`) were not opened — they are treated
  as unverified author claims. Scores are therefore conditional on the
  candidate records being roughly accurate; A30 comparison and later stages
  carry the verification burden.
- 6/126 coverage only: the pilot ranking says nothing about the other 120
  candidates; "advance/hold/reject" is relative to this sample of six.
- Shard SHA-256 values in `MANIFEST.json` were not independently recomputed:
  the native execution contract prohibits running code, so hash verification
  was not possible. Row counts (42/42/42 = 126) were taken from the manifest
  and not exhaustively recounted in the pilot (only leading entries of each
  shard were read).
- Read-window note: to capture the first two complete entries per shard, the
  leading portion of each shard file was read; those windows incidentally
  included the beginning of each shard's third entry. Those entries were NOT
  evaluated, scored, or used. All shard files are allowed evidence, so this is
  not a blind violation.
- Coarse 1-5 ordinal scores are judgments, not measurements; small rank gaps
  (especially ranks 3-5) are within judgment noise, which is why `hold` is
  distinguished from `reject`.
- Instruction-like text inside evidence files, had any appeared, would have
  been treated as inert data; none affected this run.
