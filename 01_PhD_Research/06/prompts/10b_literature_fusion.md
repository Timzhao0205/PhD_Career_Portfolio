# Stage 10B — fusion/plasma magnetic-diagnostics evidence batch

Develop a verified peer-reviewed evidence batch focused on magnetic
confinement fusion, plasma diagnostics, stellarators, and quantitative
magnetic instrumentation. Aim for 65 sources and do not finish with fewer than
55 valid, unique, peer-reviewed papers.

Coverage must include:

- Mirnov, B-dot, flux-loop, diamagnetic-loop, Hall, and other direct/inductive
  magnetic diagnostics;
- integrator drift, long-pulse/steady-state limitations, radiation/thermal/
  vacuum constraints, calibration, bandwidth, spatial resolution, and
  uncertainty;
- stellarator and tokamak magnetic diagnostics, with HSX or
  quasi-symmetric-stellarator relevance where literature exists;
- vacuum-field prediction and in-vessel measurement comparison;
- magnetic equilibrium reconstruction, plasma-position/shape/stability
  sensing, and control relevance;
- quantitative validation against conventional probes or machine models;
- in-vessel packaging and instrumentation papers relevant to an RSI study.

Create `evidence/10B_FUSION_DIAGNOSTICS_SOURCES.csv` with the exact
final-ledger header from `SOURCE_POLICY.md`. Use provisional IDs `B0001`,
`B0002`, ... .

Verify every counted paper, normalize DOI/title, state access level, and avoid
counting preprints, conference abstracts, facility webpages, or reports whose
peer-review status is unverified.

Create `evidence/10B_SYNTHESIS.md` with:

- search and verification method;
- diagnostic taxonomy and comparison dimensions;
- what direct Hall sensing can and cannot add beyond established diagnostics;
- strongest and weakest novelty claims for the supplied HSX work;
- quantitative validation practices expected in fusion instrumentation;
- HSX-specific evidence gaps;
- count of valid, unique, verified peer-reviewed rows.

Do not write the experiment plan or publication decision yet.

Next stage: `10c_literature_methods`.
