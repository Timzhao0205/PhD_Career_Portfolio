# tools/cad — visual generation for ST8 (validated pipeline)

ST8 must produce, per concept, an isometric + orthographic + section view and exportable
geometry. Use this toolchain (primary → fallback), and record which was used in the run log.

## Primary: OpenSCAD (parametric, PNG + STL) — VALIDATED in this pack
`concept_cube_slots.scad` is a working parametric starter (Concept A = the user's slotted cube)
and renders cleanly. It echoes the envelope-fit checks. Extend it and author sibling files
`concept_*.scad` for the other concepts.

```powershell
# Windows: install once (winget) if not present, then render/export
winget install --id OpenSCAD.OpenSCAD -e   # or download from openscad.org
openscad -o conceptA.png --imgsize=1400,1000 --viewall --autocenter --projection=p concept_cube_slots.scad
openscad -o conceptA_top.png --imgsize=1200,1200 --camera=0,0,20,0,0,0 --viewall concept_cube_slots.scad
openscad -o conceptA.stl --render concept_cube_slots.scad
```
Headless Linux equivalent: prefix with `xvfb-run -a`.

## For STEP (machining interchange): build123d / CadQuery (Python)
`build123d_concept.py` is a template. STEP is preferred for anything you'll hand to a machine
shop; STL (OpenSCAD) is fine for 3D-print prototypes and previews.

```powershell
pip install build123d
python build123d_concept.py   # writes conceptA.step + conceptA.stl
```
The run must VALIDATE this installs/runs on the user's machine; if build123d is heavy or fails,
fall back to OpenSCAD STL + note it in the log (a machine shop can accept STL or re-CAD from the
dimensioned drawing).

## Always-available fallback: annotated diagrams
If no CAD renders, produce dimensioned orthographic SVG/PNG with matplotlib (see how
`envelope_reference.png` was made) so every concept still has a clear visual + numbers.

## Required outputs per concept (write to 80_3D_PACKAGING/<concept>/)
- `<concept>.scad` and/or `<concept>.py` (source, parametric)
- `<concept>_iso.png`, `<concept>_top.png`, `<concept>_front.png`, `<concept>_section.png`
- `<concept>.step` and/or `<concept>.stl`
- envelope-fit numbers (cross-section corner radius ≤ 15.875 mm; height ≤ 27.5 mm)

## Loading the user's existing CAD (for fit-check + critique)
His parts are STEP: `01_MISSION/REFERENCE/cad/{new_3d_idea_assembled,new_3d_idea_disassembled,old_1d_sensor}.stp`.
Load with a real kernel to get true dimensions (assembly transforms make text point-extents
wrong):
```python
from build123d import import_step
p = import_step("../../01_MISSION/REFERENCE/cad/new_3d_idea_assembled.stp")
print(p.bounding_box())   # true overall size in mm
```
(or CadQuery `importers.importStep(...).val().BoundingBox()`).
