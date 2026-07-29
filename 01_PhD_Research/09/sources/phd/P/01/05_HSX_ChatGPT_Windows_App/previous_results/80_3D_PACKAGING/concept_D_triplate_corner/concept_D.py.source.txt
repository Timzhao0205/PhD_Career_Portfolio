"""concept_D.py — build123d STEP export for CONCEPT D "TriPlate corner" (runner-up).

Exports concept_D.step containing the three shop-relevant parts, positioned:
  - zirconia SEAT PLATE (13.4 x 13.4 x 3.2, through-window pocket, 2 bolt
    holes, wire-exit notch) -- the only precision ceramic part; make spares
  - zirconia CORE CUBE (12 mm, through-holes + wire grooves only)
  - Ti grade-2 base flange
Fired (post-sinter) dimensions; vendor applies the green scale factor.

Run:  python concept_D.py
"""
from build123d import (Box, Cylinder, Rectangle, Circle, Location, Plane,
                       Align, extrude, export_step, export_stl, Compound)

ENV_D, ENV_H = 31.75, 27.5
CORE, PLATE, PLATE_T = 12.0, 13.4, 3.2
POCKET, POCK_D, PEEK_T = 9.40, 2.15, 1.0
FRAME_T = 1.0
STAND_H, BASE_T, BASE_D, EAR_Y = 6.5, 1.5, 18.0, 12.5
Z0 = STAND_H + BASE_T
ZC = Z0 + CORE / 2

SX = [(5.00, -5.00), (-5.00, 5.00)]
SY = [(5.20, 4.80), (-5.20, -4.80)]
SZ = [(4.90, -5.15), (-4.90, 5.15)]

r_corner = ((CORE/2 + PLATE_T + FRAME_T + 1.3)**2 + (PLATE/2)**2) ** 0.5
assert r_corner <= ENV_D/2, "corner exceeds envelope"
assert Z0 + CORE + PLATE_T + FRAME_T + 1.3 <= ENV_H, "stack exceeds envelope"

FACES = {
    "+X": (Plane(origin=(0, 0, ZC), x_dir=(0, 1, 0), z_dir=(1, 0, 0)), SX),
    "+Y": (Plane(origin=(0, 0, ZC), x_dir=(1, 0, 0), z_dir=(0, 1, 0)), SY),
    "+Z": (Plane(origin=(0, 0, ZC), x_dir=(1, 0, 0), z_dir=(0, 0, 1)), SZ),
}

# ---- core cube: through-holes + vertical wire grooves only ----
core = Box(CORE, CORE, CORE).locate(Location((0, 0, ZC)))
for name, (pl, scr) in FACES.items():
    for (u, v) in scr:
        core -= extrude(pl.offset(CORE/2 + PLATE_T + 4) *
                        Circle(1.1).locate(Location((u, v))),
                        -(CORE + 2*PLATE_T + BASE_T + 12))
core -= Box(1.5, 2.0, CORE).locate(Location((-CORE/2 + 0.74, 0, ZC)))
core -= Box(2.0, 1.5, CORE).locate(Location((0, -CORE/2 + 0.74, ZC)))

# ---- three identical seat plates, placed on the faces ----
plates = []
for name, (pl, scr) in FACES.items():
    p = extrude(pl.offset(CORE/2) * Rectangle(PLATE, PLATE), PLATE_T)
    p -= extrude(pl.offset(CORE/2 - 1) * Rectangle(POCKET, POCKET), PLATE_T + 2)
    for (u, v) in scr:
        p -= extrude(pl.offset(CORE/2 - 1) * Circle(1.1).locate(Location((u, v))),
                     PLATE_T + 2)
    p -= extrude(pl.offset(CORE/2 - 1) *
                 Rectangle(2.0, 2.6).locate(Location((0, -PLATE/2 + 1.2))),
                 PLATE_T + 2)   # wire-exit notch
    plates.append(p)

# ---- Ti base flange ----
base = Cylinder(BASE_D/2, BASE_T, align=(Align.CENTER, Align.CENTER, Align.MIN)
                ).locate(Location((0, 0, STAND_H)))
for s in (1, -1):
    base += Box(5, EAR_Y - 7 + 5, BASE_T, align=(Align.CENTER, Align.CENTER, Align.MIN)
                ).locate(Location((0, s * (EAR_Y + 7) / 2, STAND_H)))
    base += Cylinder(2.5, BASE_T, align=(Align.CENTER, Align.CENTER, Align.MIN)
                     ).locate(Location((0, s * EAR_Y, STAND_H)))
    base -= Cylinder(1.1, BASE_T + 2, align=(Align.CENTER, Align.CENTER, Align.MIN)
                     ).locate(Location((0, s * EAR_Y, STAND_H - 1)))
base -= Cylinder(2.5, BASE_T + 2, align=(Align.CENTER, Align.CENTER, Align.MIN)
                 ).locate(Location((0, 0, STAND_H - 1)))
for (u, v) in SZ:   # the +Z plate bolts continue through the base
    base -= Cylinder(1.1, BASE_T + 4, align=(Align.CENTER, Align.CENTER, Align.MIN)
                     ).locate(Location((u, v, STAND_H - 2)))

asm = Compound(children=[core] + plates + [base])
export_step(asm, "concept_D.step")
export_stl(plates[2], "concept_D_seat_plate.stl")
print("wrote concept_D.step (+ seat-plate STL)")
print("corner radius:", round(r_corner, 2), "<=", ENV_D/2,
      "; height:", Z0 + CORE + PLATE_T + FRAME_T + 1.3, "<=", ENV_H)
