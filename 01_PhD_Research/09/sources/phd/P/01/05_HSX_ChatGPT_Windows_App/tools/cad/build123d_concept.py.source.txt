"""
build123d_concept.py — STEP/STL export template for ST8 (the run validates + extends this).

Concept A = the user's slotted cube, parametric. Mirrors concept_cube_slots.scad but exports
STEP (preferred for machining). This is a TEMPLATE: the ST8 run must install build123d, run it,
confirm the STEP opens, then author the other concepts as sibling scripts.

    pip install build123d
    python build123d_concept.py     # -> conceptA.step, conceptA.stl

If build123d fails to install on the user's machine, fall back to the OpenSCAD path (STL) and
log it. Numbers below are STARTING values, not a finalized design — ST8 fit-checks them.
"""
from build123d import (BuildPart, Box, Cylinder, Pos, Rot, Location, Mode,
                        export_step, export_stl, Align)

# ---- envelope (hard constraints) ----
ENV_D, ENV_H = 31.75, 27.5          # cylinder Ø x H [mm]
# ---- carrier LCC02046 ----
LCC, LCC_T, CLR = 8.89, 1.65, 0.15
# ---- cube + retention ----
CUBE = 18.0                         # must satisfy CUBE*2**0.5 <= ENV_D
LIP, STAND_D, STAND_H = 0.8, 8.0, 3.0
SLOT_D = LCC_T + 0.3

assert CUBE * 2**0.5 <= ENV_D, "cube cross-section exceeds envelope diameter"
assert STAND_H + CUBE <= ENV_H, "stack height exceeds envelope height"

def face_pocket(part):
    """Cut an LCC pocket + retention-lip opening on the +Z face of `part`."""
    with BuildPart(part.part, mode=Mode.SUBTRACT):
        Box(LCC + 2*CLR, LCC + 2*CLR, SLOT_D,
            align=(Align.CENTER, Align.CENTER, Align.MAX),
            mode=Mode.SUBTRACT).move(Location((0, 0, CUBE/2)))

with BuildPart() as concept_a:
    Cylinder(STAND_D/2, STAND_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    with BuildPart(mode=Mode.ADD) as cube:
        Box(CUBE, CUBE, CUBE).move(Location((0, 0, STAND_H + CUBE/2)))
    # TODO(ST8): subtract LCC pockets on the 3 orthogonal faces (+Z,+X,+Y) with a
    # retention lip, add harness channels down to the stand, add a pin-1 keying notch.
    # Use Rot() to reorient face_pocket() onto +X and +Y. Keep it parametric.

export_step(concept_a.part, "conceptA.step")
export_stl(concept_a.part, "conceptA.stl")
print("wrote conceptA.step + conceptA.stl ; cube corner radius =",
      round(CUBE*2**0.5/2, 2), "mm (<=", ENV_D/2, ")")
