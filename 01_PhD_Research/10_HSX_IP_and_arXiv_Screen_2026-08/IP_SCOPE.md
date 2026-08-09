# Publication-only IP scope

## Controlling publication

Title: **AlGaN/GaN Hall-Effect Sensor for In-Situ Magnetic Field Monitoring of
the HSX Stellarator**

Artifacts:

- `inputs/manuscript/submission.pdf` — nine-page submission bundle containing
  the paper, graphical abstract, and cover letter.
- `inputs/manuscript/source_original.zip` — original 17-entry source archive.
- `inputs/manuscript/source/regular_lsens/regular_lsens.tex` — extracted TeX for
  transparent text and comment review.

## Disclosed technical groups to evaluate

1. **Hall device and fabrication**
   - Purchased AlGaN/GaN heterostructure with a 2DEG sensing channel.
   - Regular octagonal Hall plate with 200 micrometre inscribed diameter.
   - Mesa etch, Ti/Al/Mo/Au contacts, anneal, 7 nm Al2O3 passivation, vias,
     Ti/Au bond metal, and 5 mm by 5 mm die.
2. **UHV/GDC module**
   - Aluminum wire bonds to a ceramic leadless chip carrier.
   - EPO-TEK 353ND encapsulation and 150 degrees C vacuum bake for one hour.
   - Custom zirconia holder, stainless-steel standoff, and insertion flange.
   - Grounded graphite shield over the packaged module to reduce arcing and
     epoxy degradation during glow-discharge cleaning and plasma operation.
3. **Bias and readout**
   - Voltage-biased Hall plate; INA849 plus two OPA814 stages; total gain 200
     V/V and 1 MHz bandwidth; external electronics through vacuum feedthroughs.
4. **Deployment and validation method**
   - In-vessel deployment near the HSX plasma edge; 68 consecutive shots.
   - Biased versus unbiased and plasma-discharge versus coil-only comparisons.
   - Temporal comparison with stored energy from the HSX diamagnetic loop.

## Explicitly incomplete or future work

- No absolute magnetic-field calibration is demonstrated.
- Temperature-dependent offset correction remains future work.
- Radiation and neutron irradiation characterization remains future work.
- Lower-noise readout for MHD fluctuations remains future work.
- The paper reports temporal correlation, not interchangeable measurement of
  local field and volumetric stored energy.

## Excluded from this review

- Three-axis or vector Hall probes.
- Hall-plus-inductive-coil hybrid probes or mutual calibration.
- Radiation compensation, current-spinning, self-calibration, or sensitivity
  recovery architectures not implemented and enabled in this paper.
- TCAD, simulation publications, startup ideas, power electronics, power
  converters, future PhD directions, and any other folder-06 concepts.
- New package designs invented during this analysis. They may be listed only as
  future design-around ideas, never mislabeled as disclosed inventions.

## Questions that materially affect the strongest candidate

The workflow should flag these for the inventors/OTL rather than assume answers:

- Who conceived the grounded graphite shield, its geometry, grounding route,
  clearance, apertures, and placement, and when?
- Was it standard HSX/GDC engineering, adapted from an existing probe, or a new
  solution developed for this module?
- Was there a documented failure mode or comparison without the shield?
- Are there drawings, photographs, dimensions, current paths, thermal data,
  outgassing records, residual-gas analysis, leak tests, or GDC exposure data?
- What UHV acceptance criterion did the one-hour bake satisfy?
- What was the earliest disclosure to people without confidentiality duties?
- Did UW-Madison personnel contribute to any potential claimed element?
- Which DOE, NSF, SLAC, Stanford, UW, or other sponsorship terms apply?

These gaps do not block triage. They control confidence and the recommended
pre-arXiv OTL action.
