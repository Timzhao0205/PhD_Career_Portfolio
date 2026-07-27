# Mission

Produce a defensible research decision package—not a sales pitch—for a
Hall-effect plus inductive-coil magnetic diagnostic that may need to operate
under neutron, gamma, thermal, electromagnetic, and long-duration drift
stresses.

The mission starts from the user's working hypothesis:

> Validate and measure the Hall device first; add an inductive coil as a
> complementary hybrid; then provide a reusable module and simulation package.

Treat that as a hypothesis to test. Do not make the conclusion fit it.

The most important technical question is structural identifiability. A coil
measures field change while a Hall device measures field with unknown
sensitivity and bias. Redundancy does not automatically reveal which device
drifted. The analysis must explicitly determine when the combined system can
estimate field, Hall gain, Hall bias, coil gain/effective area, and integrator
drift, and when those quantities remain confounded.

## Scope

- Additional peer-reviewed literature beyond folder `06`.
- Direct and enabling evidence on radiation effects in Hall materials,
  contacts, biasing, packaging, readout electronics, cables, coils, and
  integrators.
- Observer/state-estimator design requirements and calibration references.
- Simulation and staged validation plan, including synthetic fault injection.
- Application and collaborator prioritization.
- Limitations and comparison against credible alternatives.
- Accuracy-versus-budget options and go/no-go gates.

## Boundary conditions

- Folder `06` and all other siblings are read-only context.
- Write only in this folder.
- Do not claim that the user has performed neutron or gamma experiments.
- The user's current first-author HSX work does not automatically acquire a
  radiation-test requirement. Radiation can remain a later, coauthored, or
  collaborator-led work package if the evidence supports that boundary.
- Do not contact any group, submit anything, or alter external resources.
- No geographic or affiliation exclusion applies to scientific sources.
  Evaluate evidence on quality and relevance.
- Do not confuse radiation species, spectrum, dose, fluence, dose rate,
  temperature, annealing, or device technology.

## Success

The package succeeds only if a skeptical advisor can trace each major claim,
see the failure cases, understand what the coil can and cannot calibrate, and
decide the next experiment without relying on undocumented model intuition.
