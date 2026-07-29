# Stage 10A — GaN/WBG/Hall-sensor evidence batch

Develop a verified peer-reviewed evidence batch focused on the Senesky group’s
technical fields and the sensor itself. Aim for 65 sources and do not finish
with fewer than 55 valid, unique, peer-reviewed papers.

Coverage must include:

- AlGaN/GaN 2DEG Hall devices and comparable III-V Hall platforms;
- Hall geometry, current-related and voltage-related sensitivity, carrier
  density/mobility, offset, planar Hall effects, cross-axis response;
- spinning-current/current-reversal/offset-cancellation methods;
- noise, drift, linearity, bandwidth, parasitics, contacts, wire bonds,
  packaging, calibration, temperature coefficients, and repeatability;
- GaN/SiC/WBG devices and sensors in harsh temperature, vacuum, radiation
  context, and extreme-environment instrumentation;
- prior GaN Hall-sensor performance tables or reviews relevant to the novelty
  criticism.

Create `evidence/10A_GAN_WBG_SOURCES.csv` with the exact final-ledger header
from `SOURCE_POLICY.md`. Use provisional IDs `A0001`, `A0002`, ... .

For each row:

- verify peer-reviewed publication status from a publisher/DOI/venue record;
- normalize DOI and use a DOI URL when available;
- set `access_level` honestly;
- assign semicolon-delimited topic tags;
- state exactly which claim(s) it supports;
- exclude unverifiable candidates rather than padding the count.

Create `evidence/10A_SYNTHESIS.md` with:

- search and verification method;
- venue and year distribution;
- performance/novelty comparison dimensions suitable for a manuscript table;
- established results versus unresolved questions;
- implications for the submitted GaN Hall sensor;
- limitations caused by abstract-only access;
- count of valid, unique, verified peer-reviewed rows.

Do not decide the PhD direction or publication route yet.

Next stage: `10b_literature_fusion`.
