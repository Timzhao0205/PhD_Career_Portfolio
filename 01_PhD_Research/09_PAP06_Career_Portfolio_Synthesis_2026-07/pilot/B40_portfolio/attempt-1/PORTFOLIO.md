# PORTFOLIO — B40_portfolio PILOT attempt-1

**PILOT SAMPLE — NOT FINAL.**

Stage `B40_portfolio` | Mode `PILOT` | Attempt 1 | Worker `pap06-fable-xhigh`
(requested Fable 5 / xhigh). Six-idea mixed sample exercising the full-run
scoring method. Nothing here is a portfolio decision; the full 24-ranking
supersedes every number and disposition in this file.

## 1. Scope and inputs

First stage allowed to rank. Inputs: B20 ALIGNMENT.csv (39 rows / 41-ID
universe, classes STRONG/MEDIUM/WEAK/ADVERSE), B25 POWER_MAP.csv + POWER.md
§9 (wedges W1/W2, non-wedge rule), B30 SKILLS.md + BRIDGES.json (capability
ground truth and gates BR-A..BR-I), B15 LIT_REVIEW.md (§4/§6/§7 evidence
boundaries), A30 COMPARE.json + VERDICT.md (membership, SEM ledger, four
verified disagreements, rerun list), B10 OPT2.md (founder constraints,
critical path, kill criteria). One decision-critical live recheck was made
this run (merchant SSCB status pressing C-01; SOURCES.csv B40P-01/02).

## 2. Sample selection (deterministic)

Rules stated before scoring (full text in DECISION.json):

1. The unique STRONG (D-02) and the unique ADVERSE (D-10) — task-mandated
   and unambiguous.
2. The task-named killed-by-both-baselines exemplar C-07 — the only killed
   idea whose kill facts A30 verified on opened primaries.
3. The WEAK with the highest cross-run consensus (C-01: BLIND 1 via SEM-01
   / NEW 2 / OLD 5) — maximal consensus-vs-alignment tension.
4. One MEDIUM per wedge family with the strongest verified/triple-
   intersection support: C-05 (W1; A30-verified revival) and D-01 (W2
   anchor; BLIND 3 / OLD 3 / NEW 7).

Sample: **D-02, D-01, C-05, C-01, C-07, D-10** — spanning all four B20
classes, both wedges, an old-kill/new-revival, a verified blind error, and
a consensus/alignment conflict.

## 3. Scoring method (the full run will use exactly this)

Eleven criteria — founder goal, time horizon, capital, geography,
regulation, technical proof, PhD leverage, shared skills, buyer access,
defensibility, downside — each scored 0-4 coarse ordinal with a per-score
half-width band (0.5 well-evidenced / 1.0 record-level or proposed-only /
1.5 pool-record-only). Definitions and the anti-double-counting lines
(phd_leverage = B20 mechanism class; shared_skills = B30 acquisition path;
founder_goal_fit = plan compatibility; downside = failure severity;
geography = market friction; regulation = burden incl. person-status) are
in DECISION.json. Aggregation: declared fixed weights (sum 1.00), with the
commercial-evidence side at 0.60, founder side at 0.30, downside at 0.10 —
so PhD leverage (0.12) structurally cannot override commercial evidence.
Aggregate uncertainty is the conservative linear-combined half-width;
overlapping bands are disclosed as non-separation. Dispositions:
keep / bridge / watch / stop, defined in DECISION.json; bridge is always
contingent on named BR-x gates from B30.

## 4. Sample result

| # | Idea | Class | Score | Disposition |
|---|---|---|---|---|
| 1 | P3R2-D-02 REBCO tape QC metrology | STRONG | 3.0 +/-0.8 | bridge (BR-D/C04; BR-B; 2027 Ic-correlation kill rule) |
| 2 | P3R2-D-01 HTS quench detection | MEDIUM | 2.8 +/-0.8 | bridge (BR-A P0 -> P1, BR-C, BR-G) |
| 3 | P3R2-C-05 liquid-cooling conformance metrology | MEDIUM (boundary) | 2.6 +/-0.9 | watch (BR-B dossier outcome; OCP-vacuum resolution; round-robin feasibility) |
| 4 | P3R2-C-01 800VDC rack protection | WEAK | 1.6 +/-0.7 | watch (BR-G outcome; OCP/NVIDIA embed check end-2027; SSCB shipping status) |
| 5 | P3R2-C-07 AFE rectification retrofits | WEAK (boundary), killed | 1.1 +/-0.6 | stop |
| 6 | P3R2-D-10 coherent beam combining | ADVERSE | 0.7 +/-0.7 | stop |

Ranks 1-3 overlap within bands (not separated); the top-3-vs-bottom-2
separation is clean. No idea earns **keep**: every non-WEAK mechanism in
the universe runs through proposed-only capabilities gated by C04 and
FT-02 (B30), so the portfolio's top is bridge-shaped — that is a finding
about the evidence, not a hedge.

## 5. Reasoning per idea

**1. P3R2-D-02 (bridge).** The only idea where B20 found a STRONG
bidirectional mechanism: demonstrated Hall readout + harsh-environment
packaging carry the product's core sensor, and the decisive risk (traceable
Ic within 5%) IS the WP-C credential the PhD needs for G5 anyway — the
rare case where venture proof and thesis credential are the same work.
Scored down where the evidence says so: technical_proof 2 (TapeStar
incumbency, correlation kill rule untested), defensibility 2, phd_leverage
uncertainty widened to 1.0 because the calibration leg is proposed-only and
C04-gated, and B20 correction 1 (array instrumentation, thermography not
demonstrated) is carried, not smoothed. Bridge, never keep, until C04
closes and BR-D exits.

**2. P3R2-D-01 (bridge).** Triple-intersection winner class whose honest
founder lane is methodology, not hardware: false-trigger statistics under
EMI are the same problem class B15 documents (EV06/EV23) and the same
estimator-honesty discipline as FT-02/BR-A — which costs $0 to gate.
No Hall channel exists in the product; the fiber/RF/dump core is
collaborator territory; demand is ecosystem-level pending a 2028 co-test.
The cheap decisive gate plus community-overlapping buyers (S-B20-02) put
it second; commercial maturity keeps technical_proof at 2.

**3. P3R2-C-05 (watch).** The strongest verified commercial evidence in
the sample (A30 re-opened the Deschutes/Nidec primaries) and a genuine
W1-class moat thesis (method authority with published uncertainty
budgets — the corpus-scarce skill, EV01/EV35/G3). Held at watch, below
both bridges, because the founder transfer is methodology-not-domain (B20
correction 4: multi-kW calorimetry and two-phase fluids are nowhere in
the ledger), no C-05-specific bridge gate exists, and the
conformance-vacuum predicate is still discovery-level (OCP 403-blocked;
A30 rerun item 1). B25's own verdict is carried: it proves the wedge class
generalizes; it is not the founder's first wedge.

**4. P3R2-C-01 (watch).** The corpus's strongest cross-run commercial
consensus (SEM-01: BLIND 1 / NEW 2 / OLD 5) and the sample's sharpest
lesson: consensus is not founder fit. B10's ledger contains no
power-electronics, protection, or certification capability; B25 rules the
founder-led breaker a non-wedge; capital and regulation burdens are the
sample's heaviest. The surviving founder-relevant object is the
protection-intelligence sliver (EV27-class telemetry + arc
discrimination) that ST01-C06P independently scoped as a product and BR-G
tests at founder scale. Live recheck this run: Siemens launched the
SENTRON 3QD2 SSCB at Hannover Messe 2026 (opened primary, B40P-01) —
merchant entries are pressing the venture's own window; the ABB
Infinitus shipping claim stays record/discovery-level (fetches timed
out, disclosed). Watch, with the sliver's triggers named; not stop,
because the sliver's falsifier (a paid design-in pricing the telemetry
layer) remains live and cheap to monitor.

**5. P3R2-C-07 (stop).** Killed by both baselines; A30 verified the kill
facts on opened primaries — the 45V construction-start deadline pulled to
pre-2028 by statute and Ingeteam's shipping <3%-THD rectifier line. B20
found no mechanism and no evidenced buyer for the only conceivable sliver.
Time spent here buys neither durable position nor PhD progress. Its BLIND
rank 10 is A30's clearest verified blind error; scoring it 5th of 6
demonstrates the method absorbs verified kills correctly.

**6. P3R2-D-10 (stop).** The universe's only ADVERSE: zero mechanism in
either direction plus an idea-specific conflict — controlled/classified
directed-energy work structurally collides with the PhD's open-publication
gates (G5/C49, C33/C34) and with C42. A30's verification cuts both ways
and both are carried: OLD's hard kill overstated (procurement is live and
funded), NEW's rank 4 overstated (the awardee holds CBC proprietary and
vertically integrated). Under an integrated founder-portfolio scoring the
verdict is unambiguous: last, stop, do not co-plan with the PhD.

## 6. Relation to the old/new/blind verdicts (A30)

- The pilot ranking agrees with the three-way consensus where mechanisms
  exist (D-02, D-01 near the top of all three finals) and *disagrees with
  all three* where alignment evidence demands it: no prior run ranked
  C-01 below third place — this pilot ranks it 4th of 6 because founder
  evidence, not consensus, is the integrating axis.
- It adopts A30's verified adjudications exactly: C-07's kill facts
  (stop), D-10's split verdict (stop, against NEW's 4), C-05's revival
  predicate (ranked on merits, watch on founder grounds).
- It preserves A30's calibration lesson: BLIND was right where
  record-internal reasoning sufficed and wrong where 2025-2026 external
  facts moved; this stage therefore re-opened one live window question
  (SSCB shipping) rather than trusting record vintage.
- SEM ledger honored: E-01 appears only inside C-01's origin; no
  double-counted concept anywhere in the sample.

## 7. What the full 24-ranking must add

1. **Coverage:** all 24 slots from the 41-ID universe (SEM-consolidated),
   including every remaining MEDIUM (A-10, D-09, F-06, A-14, E-04), the
   W1 family's nearest-term member G-03, and the killed/revived families —
   with power-electronics ideas included without forcing them up or down.
2. **The real flip zone:** adjacent pairs where alignment and commercial
   evidence pull opposite ways (C-22 vs D-09/F-06; G-03 vs C-05; E-04's
   deemed-export friction) — the sample's total sensitivity stability will
   NOT generalize there and flips must be reported.
3. **Origin discipline at scale:** per-idea A30 membership summaries and
   explicit changes versus the old and new top-24s, including the three
   CONTRADICTED-provenance old06 supplementals (S01, CN-01, CN-03) which
   A30 says need independent regeneration before inclusion weight.
4. **Unverified-swing handling:** F-19's +28.0 unaudited reversal and the
   other seven unverified OLD->NEW reversals need cautious venture-fact
   treatment or targeted rechecks (A30 rerun items 5-7).
5. **Startup-corpus rows:** decide whether ST01/ST03 objects rank as
   ideas or serve only as wedge evidence (this pilot used them as
   evidence only, per B25/B30 practice).
6. **Dependency-aware portfolio structure:** the full run should express
   the C04/FT-02/G5 spine as portfolio-level dependencies (as begun in
   DECISION.json) so bucket membership updates mechanically on gate
   outcomes.
7. **More live rechecks where decisions hinge:** this pilot re-opened one
   window (SSCB); the full run must re-open the small set of
   record-vintage facts that sit under close calls (its own judgment,
   logged claim-by-claim).

## 8. Honesty notes

- Scores are coarse ordinal aggregates; two-decimal values exist only for
  ordering audit. Overlapping bands are non-separation and are labeled as
  such in RANKING.csv.
- The sensitivity result (zero flips at halved/doubled PhD weight, provably
  stable for any weight) is real but partly a sample-construction artifact;
  DECISION.json says so explicitly.
- No new market size, competitor, customer, or measurement fact was
  invented; every current-market claim traces to SOURCES.csv (A30/B20/B25
  opened primaries, two this-run web actions, or internal evidence rows),
  and corpus-dated facts are labeled record-vintage.
- This stage is research planning and strategic screening, not legal,
  safety, export, or certification advice (SOURCE_POLICY).
