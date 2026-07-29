# B40 — combined portfolio decision

Use A30 and all B-stage evidence, including B15's adjudicated literature map,
to produce an integrated portfolio. Re-read primary source artifacts and
underlying publications where a decision depends on a support-stage claim.
Preserve exact IDs and avoid double-counting semantic duplicates.

Rank exactly 24 directions. Score with explicit uncertainty and sensitivity to
founder goal, time horizon, capital, geography, regulation, technical proof,
PhD leverage, shared skills, buyer access, defensibility, and downside. Include
power-electronics opportunities without forcing them into the top tier.

Required outputs:

- `RANKING.csv`: exactly 24 unique ranks 1–24 with idea_id,name,origin,
  disposition (keep/bridge/watch/stop), score, uncertainty, PhD leverage,
  power relevance, first proof, capital band, main risk, falsifier.
- `DECISION.json`: top 10, portfolio buckets, dependencies, sensitivity cases,
  and explicit rejected alternatives.
- `PORTFOLIO.md`: reasoning, changes versus old/new top 24, and next decisions.
- `SOURCES.csv`: claim-level sources used for portfolio decisions, with B15
  paper IDs for literature-backed technical claims.

Pilot: rank a six-idea mixed sample and run one weighting sensitivity check.
