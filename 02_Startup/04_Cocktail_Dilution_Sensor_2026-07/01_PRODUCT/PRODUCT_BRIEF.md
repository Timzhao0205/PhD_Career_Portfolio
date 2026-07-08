# Product brief — real-time cocktail dilution / ABV sensor

## One-liner
A bar tool (probe → barspoon) that reads dilution % and ABV live
while a drink is stirred, converging in ~1–2 s without pausing
service, so bartenders hit a target dilution instead of guessing.

## User + job
Craft bartenders and serious home enthusiasts ("Liquid Intelligence"
audience). Job: stop stirring at the intended dilution (typ. 20–25 %
water for a stirred whisky drink) reproducibly, drink after drink,
across ice quality and glass temperature.

## Why it can work (physics edge)
Water/ethanol permittivity contrast is enormous (≈78 vs ≈24), and for
spirit+ice, chilling and dilution are thermodynamically locked, so a
$5 sensing pair (IDE capacitor + NTC) plus robust statistics covers
the whisky+ice case. Chaos (bubbles, ice strikes) is transient and
one-sided — handled by burst sampling + mode estimation + IMU gating,
not by asking the bartender to stop.

## Scope ladder
- v1: spirits + ice (binary ethanol-water). In scope now.
- v2: sugared/citrus cocktails — requires a second modality
  (RI or ultrasonic) to close the 3-unknown problem. NOT now.

## Form-factor ladder
Phase 0 benchtop dipstick → Phase 1 clip-on inner-wall probe (may be
the better product: bottom of vessel = cleanest liquid) → Phase 2
instrumented barspoon → stretch: through-glass coaster puck (glass
vessels only; metal tin shields the field).

## Business posture
Niche premium tool, $100–200 price point, Kickstarter-scale.
Primary value to Tim: fast full-stack hardware product reps
(sensing → estimator → BLE → enclosure) as a portfolio piece and
methodology rehearsal for the 2029/2030 startup — not a venture bet.
Feasibility percentages: 01_PRODUCT/FEASIBILITY.md.
