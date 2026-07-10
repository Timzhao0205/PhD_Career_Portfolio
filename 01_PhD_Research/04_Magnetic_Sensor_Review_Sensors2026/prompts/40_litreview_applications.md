# Stage 40 - Literature review: current applications (four domains)

think hard

Read `docs/PROJECT_BRIEF.md` (section 4), `refs_raw/00_seed.jsonl`, and
`outputs/30_litreview_sensor_types.md` if present (so you map families to uses
consistently and avoid re-deriving device facts).

Produce `outputs/40_litreview_applications.md`: a sourced brief on how magnetic
sensors are used TODAY across the four domains. For each domain, give concrete,
cited deployments; for each deployment note which sensor family is used and the
practical reason (performance, cost, isolation, size, temperature), and where
possible a quantitative requirement it must meet.

**Energy** - current sensing in inverters/power electronics; smart-grid &
substation monitoring; EV battery-management (pack current, SoC/SoH); contactless
dc metering; renewables condition monitoring.
**Transportation** - automotive position/angle/speed (steering, throttle,
BLDC/EV commutation, wheel-speed/ABS); traction-inverter current sensing;
e-compass/navigation; rail; aerospace/space magnetometry.
**Industrial & manufacturing** - NDT (eddy-current, magnetic-flux-leakage
pipeline inspection); motor/bearing condition monitoring & predictive
maintenance; robotics, encoders, proximity/position; process metrology.
**Biomedical** - MEG and MCG (OPM and TMR arrays); magnetic particle imaging;
GMR/TMR biosensors & lab-on-chip; catheter/instrument tracking; wearables.

For each domain also note: the dominant incumbent family and any disruptive
challenger, and one or two representative commercial systems or landmark studies.
Include a compact **domain x sensor-family fit matrix** (which families serve
which domain, and why). Log every source to `refs_raw/40.jsonl`.

Prefer peer-reviewed application papers, authoritative reviews, and standards;
vendor systems may be cited for existence/《specs》with a `[VENDOR]` tag. Aim for
~30-50 real sources. Do not overstate adoption; distinguish "widely deployed"
from "demonstrated in research." Finish by writing the file and its refs log.
