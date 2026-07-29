"""Corrected cost-down HSX three-axis package -- NOT FOR FABRICATION.

This Stage-50D model supersedes the Stage-30D mechanical geometry.  A single
folded CP-Ti trihedral bracket carries three protected, independently removable
cartridges.  Each cartridge has a formed CP-Ti perimeter caddy, an internal LCC
envelope and one identical flat ceramic guard.  The clamp reacts only through
the caddy and three bracket lands; it does not load the guard, LCC, bonds,
fanout or electrical joints.

The model validates nominal envelope, discrete-part collision, required
contacts, true open hook slots, service swept volumes, cable corridors and
export/re-import identity.  Finished dimensions are millimetres.  It does not
release material lots, bend tooling, stamped/laser edges, clamp force, fatigue,
magnetic stability, cartridge internal stack, cable construction or UHV life.
"""

from __future__ import annotations

import struct
from math import atan2, degrees, hypot
from pathlib import Path

from build123d import (
    Align,
    Box,
    Circle,
    Compound,
    Cylinder,
    Location,
    Plane,
    Rectangle,
    export_step,
    export_stl,
    extrude,
    import_step,
    import_stl,
)

OUT = Path(__file__).resolve().parent

# Hard installed envelope and retained feedthrough keepout.
ENV_R = 31.75 / 2
ENV_H = 27.50
FT_KEEP_R = 22.10 / 2
FT_KEEP_H = 10.41

# Folded bracket and face system.
BASE_Z = 12.20
SHEET_T = 0.50
BASE_TOP = BASE_Z + SHEET_T
FACE = 13.60
FACE_HALF = FACE / 2
FACE_CZ = BASE_TOP + FACE_HALF - 0.05
FACE_OUT = FACE_HALF + SHEET_T
WINDOW = 6.40

# Protected cartridge.  One flat guard geometry is repeated by rotations only.
LAND_H = 0.05
LAND_R = 0.55
LAND_UV = ((-4.30, -4.40), (4.30, -4.40), (0.00, 4.40))
CADDY_OUT = 11.30
CADDY_IN = 11.00
CADDY_T = 2.45
CADDY_REAR_T = 0.20
CADDY_REAR_OPEN = 7.20
CADDY_FRONT_T = 0.20
CADDY_FRONT_OPEN = 10.20
LCC = 8.89
LCC_T = 1.35
LCC_START = LAND_H + CADDY_REAR_T
GUARD = 10.90
GUARD_T = 0.635
GUARD_START = LCC_START + LCC_T
PIGTAIL_NOTCH_W = 1.50
PIGTAIL_NOTCH_H = 2.20

# One screw plus two edge hooks per face; two-screw fallback remains a release gate.
CLAMP = 13.40
CLAMP_T = 0.40
CLAMP_OPEN = WINDOW + 0.80
CLAMP_START = LAND_H + CADDY_T
SCREW_UV = (0.00, -5.50)
HOOK_UV = ((-2.30, -5.80), (2.30, -5.80))
SCREW_R = 0.50
SCREW_CLEAR_R = 0.72
HEAD_R = 1.00
HEAD_T = 0.35
NUT_T = 0.70
SLOT_W = 0.95
SLOT_V0 = -7.15
SLOT_V1 = -5.20
SLOT_LEN = SLOT_V1 - SLOT_V0
SLOT_CV = (SLOT_V0 + SLOT_V1) / 2
HOOK_STEM_W = 0.70
HOOK_STEM_V = 0.60
HOOK_LIP_W = 1.30
HOOK_LIP_V = 0.60
SERVICE_SLIDE = 1.40

# Support posts and installed harness corridors.
POST_XY = 9.00
POST_R = 1.15
POST_HOLE_R = 0.72
POST_HEAD_R = 1.05
POST_HEAD_T = 0.35
HARNESS_CORRIDOR = 3.80
HARNESS_XY = ((-6.30, 3.80), (3.80, -6.30), (-6.30, -3.80))
# Each attachment is outside the vertical face projection and beside its open
# cable notch; the integral base lug bridges it back to the flat blank.
STRAIN_SCREW_XY = ((-7.90, 6.70), (6.70, -7.90), (-7.90, -6.70))
STRAIN_HOLE_R = 0.65
STRAIN_CLIP_W = 0.80
STRAIN_CLIP_T = 0.40
STRAIN_NUT_R = 1.00
STRAIN_NUT_T = 0.70
STRAIN_HEAD_R = 1.00
STRAIN_HEAD_T = 0.35


def face_planes():
    """Local +Z is outward; every face uses the same non-mirrored local part."""
    return {
        "X": Plane(origin=(FACE_OUT, 0, FACE_CZ), x_dir=(0, 1, 0), z_dir=(1, 0, 0)),
        "Y": Plane(origin=(0, FACE_OUT, FACE_CZ), x_dir=(1, 0, 0), z_dir=(0, 1, 0)),
        "Z": Plane(origin=(0, 0, BASE_TOP), x_dir=(1, 0, 0), z_dir=(0, 0, 1)),
    }


def square_ring(pl: Plane, start: float, outer: float, inner: float, depth: float):
    ring = extrude(pl.offset(start) * Rectangle(outer, outer), depth)
    ring -= extrude(
        pl.offset(start - 0.05) * Rectangle(inner, inner),
        depth + 0.10,
    )
    return ring


def through_profile(pl: Plane, start: float, depth: float, profile):
    return extrude(pl.offset(start) * profile, depth)


def make_folded_bracket():
    """One conceptual laser-cut/formed blank with open reliefs and added lugs."""
    bracket = Box(
        FACE,
        FACE,
        SHEET_T,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((0, 0, BASE_Z)))

    for x in (-POST_XY, POST_XY):
        for y in (-POST_XY, POST_XY):
            angle = 45 if x * y > 0 else -45
            bracket += Box(4.20, 1.20, SHEET_T).locate(
                Location(
                    (x * 7.75 / 9.0, y * 7.75 / 9.0, BASE_Z + SHEET_T / 2),
                    (0, 0, angle),
                )
            )

    # Adjacent 0.05-mm intersections represent a connected bend zone only.
    bracket += Box(
        SHEET_T,
        FACE,
        FACE,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((FACE_HALF + SHEET_T / 2, 0, BASE_TOP - 0.05)))
    bracket += Box(
        FACE,
        SHEET_T,
        FACE,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((0, FACE_HALF + SHEET_T / 2, BASE_TOP - 0.05)))

    # Integral flat lugs place each strain screw beside, not over, its cable notch.
    for x, y in STRAIN_SCREW_XY:
        bracket += Cylinder(
            1.10,
            SHEET_T,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        ).locate(Location((x, y, BASE_Z)))

    # Open active-area windows.
    bracket -= Box(WINDOW, WINDOW, SHEET_T + 0.60).locate(
        Location((0, 0, BASE_Z + SHEET_T / 2))
    )
    bracket -= Box(SHEET_T + 0.60, WINDOW, WINDOW).locate(
        Location((FACE_HALF + SHEET_T / 2, 0, FACE_CZ))
    )
    bracket -= Box(WINDOW, SHEET_T + 0.60, WINDOW).locate(
        Location((0, FACE_HALF + SHEET_T / 2, FACE_CZ))
    )

    # The bracket has three open cable notches, never blind cable pockets.
    for x, y in HARNESS_XY:
        bracket -= Box(
            HARNESS_CORRIDOR + 0.40,
            HARNESS_CORRIDOR + 0.40,
            SHEET_T + 0.80,
        ).locate(Location((x, y, BASE_Z + SHEET_T / 2)))

    # Four post fastener holes and three supported strain-fastener holes.
    for x in (-POST_XY, POST_XY):
        for y in (-POST_XY, POST_XY):
            bracket -= Cylinder(
                POST_HOLE_R,
                SHEET_T + 0.80,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
            ).locate(Location((x, y, BASE_Z - 0.40)))
    for x, y in STRAIN_SCREW_XY:
        bracket -= Cylinder(
            STRAIN_HOLE_R,
            SHEET_T + 0.40,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        ).locate(Location((x, y, BASE_Z - 0.20)))

    # All faces share the same local screw and hook coordinates.  SLOT_V0 is
    # beyond the local -Y face edge, making each pair a true open U-slot.
    for pl in face_planes().values():
        u, v = SCREW_UV
        bracket -= through_profile(
            pl,
            -0.90,
            1.80,
            Circle(SCREW_CLEAR_R).locate(Location((u, v))),
        )
        for hu, _ in HOOK_UV:
            bracket -= through_profile(
                pl,
                -0.90,
                1.80,
                Rectangle(SLOT_W, SLOT_LEN).locate(Location((hu, SLOT_CV))),
            )

    return bracket


def make_post(x: float, y: float):
    post = Cylinder(
        POST_R,
        BASE_Z,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((x, y, 0)))
    post -= Cylinder(
        POST_HOLE_R,
        BASE_Z + 0.40,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((x, y, -0.20)))
    return post


def make_post_bolt(x: float, y: float):
    shaft = Cylinder(
        0.50,
        1.50,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((x, y, BASE_Z - 1.00)))
    head = Cylinder(
        POST_HEAD_R,
        POST_HEAD_T,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((x, y, BASE_TOP)))
    return shaft + head


def make_land(pl: Plane, u: float, v: float):
    return extrude(pl * Circle(LAND_R).locate(Location((u, v))), LAND_H)


def make_guard(pl: Plane, start: float):
    guard = square_ring(pl, start, GUARD, WINDOW, GUARD_T)
    guard -= through_profile(
        pl,
        start - 0.05,
        GUARD_T + 0.10,
        Rectangle(PIGTAIL_NOTCH_W, PIGTAIL_NOTCH_H).locate(
            Location((-GUARD / 2 + PIGTAIL_NOTCH_W / 2, 0))
        ),
    )
    guard -= through_profile(
        pl,
        start - 0.05,
        GUARD_T + 0.10,
        Circle(SCREW_CLEAR_R).locate(Location(SCREW_UV)),
    )
    return guard


def make_caddy(pl: Plane):
    side = square_ring(pl, LAND_H, CADDY_OUT, CADDY_IN, CADDY_T)
    rear = square_ring(
        pl,
        LAND_H,
        CADDY_OUT,
        CADDY_REAR_OPEN,
        CADDY_REAR_T,
    )
    front = square_ring(
        pl,
        LAND_H + CADDY_T - CADDY_FRONT_T,
        CADDY_OUT,
        CADDY_FRONT_OPEN,
        CADDY_FRONT_T,
    )
    caddy = side + rear + front

    cut_start = LAND_H - 0.10
    cut_depth = CADDY_T + 0.20
    # The local -X pigtail exit and local -Y screw relief are identical on all axes.
    caddy -= through_profile(
        pl,
        cut_start,
        cut_depth,
        Rectangle(PIGTAIL_NOTCH_W + 0.20, PIGTAIL_NOTCH_H + 0.20).locate(
            Location((-CADDY_OUT / 2 + (PIGTAIL_NOTCH_W + 0.20) / 2, 0))
        ),
    )
    caddy -= through_profile(
        pl,
        cut_start,
        cut_depth,
        Circle(SCREW_CLEAR_R + 0.05).locate(Location(SCREW_UV)),
    )
    # Hook passages and two additional edge vents prevent closed perimeter channels.
    for hu, hv in HOOK_UV:
        caddy -= through_profile(
            pl,
            cut_start,
            cut_depth,
            Rectangle(1.10, 1.40).locate(Location((hu, hv))),
        )
    caddy -= through_profile(
        pl,
        cut_start,
        cut_depth,
        Rectangle(1.20, 0.80).locate(Location((CADDY_OUT / 2, 0))),
    )
    caddy -= through_profile(
        pl,
        cut_start,
        cut_depth,
        Rectangle(0.80, 1.20).locate(Location((0, CADDY_OUT / 2))),
    )
    return caddy


def make_lcc_envelope(pl: Plane):
    return extrude(pl.offset(LCC_START) * Rectangle(LCC, LCC), LCC_T)


def make_clamp(pl: Plane):
    clamp = square_ring(pl, CLAMP_START, CLAMP, CLAMP_OPEN, CLAMP_T)
    clamp -= through_profile(
        pl,
        CLAMP_START - 0.10,
        CLAMP_T + 0.20,
        Circle(SCREW_CLEAR_R).locate(Location(SCREW_UV)),
    )
    for hu, hv in HOOK_UV:
        stem = through_profile(
            pl,
            -0.70,
            CLAMP_START + CLAMP_T + 0.70,
            Rectangle(HOOK_STEM_W, HOOK_STEM_V).locate(Location((hu, hv))),
        )
        lip = through_profile(
            pl,
            -0.90,
            0.20,
            Rectangle(HOOK_LIP_W, HOOK_LIP_V).locate(Location((hu, hv))),
        )
        clamp += stem + lip
    return clamp


def make_face_nut(pl: Plane):
    nut = through_profile(
        pl,
        -0.50 - NUT_T,
        NUT_T,
        Rectangle(1.80, 1.80).locate(Location(SCREW_UV)),
    )
    nut -= through_profile(
        pl,
        -0.60 - NUT_T,
        NUT_T + 0.20,
        Circle(0.60).locate(Location(SCREW_UV)),
    )
    return nut


def make_nut_lance(pl: Plane):
    """Vented C-pocket envelope; final spring-form tooling remains a release hold."""
    u, v = SCREW_UV
    lance = through_profile(
        pl,
        -1.15,
        0.65,
        Rectangle(2.40, 2.40).locate(Location((u, v))),
    )
    lance -= through_profile(
        pl,
        -1.20,
        0.75,
        Rectangle(1.90, 1.90).locate(Location((u, v))),
    )
    lance -= through_profile(
        pl,
        -1.20,
        0.75,
        Rectangle(0.60, 0.80).locate(Location((u + 1.15, v))),
    )
    return lance


def make_face_bolt(pl: Plane):
    shaft_start = -0.50 - NUT_T
    shaft_end = CLAMP_START + CLAMP_T
    shaft = through_profile(
        pl,
        shaft_start,
        shaft_end - shaft_start,
        Circle(SCREW_R).locate(Location(SCREW_UV)),
    )
    head = through_profile(
        pl,
        shaft_end,
        HEAD_T,
        Circle(HEAD_R).locate(Location(SCREW_UV)),
    )
    return shaft + head


def make_clip_and_hardware(screw_xy, cable_xy):
    sx, sy = screw_xy
    cx, cy = cable_xy
    dx, dy = cx - sx, cy - sy
    length = hypot(dx, dy) + 1.00
    angle = degrees(atan2(dy, dx))
    mx, my = (sx + cx) / 2, (sy + cy) / 2
    clip = Box(length, STRAIN_CLIP_W, STRAIN_CLIP_T).locate(
        Location((mx, my, BASE_TOP + STRAIN_CLIP_T / 2), (0, 0, angle))
    )
    clip -= Cylinder(
        STRAIN_HOLE_R,
        STRAIN_CLIP_T + 0.20,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((sx, sy, BASE_TOP - 0.10)))

    nut = Cylinder(
        STRAIN_NUT_R,
        STRAIN_NUT_T,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((sx, sy, BASE_Z - STRAIN_NUT_T)))
    nut -= Cylinder(
        0.60,
        STRAIN_NUT_T + 0.20,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((sx, sy, BASE_Z - STRAIN_NUT_T - 0.10)))

    shaft = Cylinder(
        0.50,
        STRAIN_NUT_T + SHEET_T + STRAIN_CLIP_T,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((sx, sy, BASE_Z - STRAIN_NUT_T)))
    head = Cylinder(
        STRAIN_HEAD_R,
        STRAIN_HEAD_T,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((sx, sy, BASE_TOP + STRAIN_CLIP_T)))
    return clip, nut, shaft + head


def make_service_keepouts(pl: Plane):
    driver = through_profile(
        pl,
        CLAMP_START + CLAMP_T + HEAD_T,
        8.00,
        Circle(2.00).locate(Location(SCREW_UV)),
    )
    # Rectangular sweep spans the starting clamp outline and -local-Y release motion.
    slide = through_profile(
        pl,
        CLAMP_START,
        CLAMP_T + HEAD_T,
        Rectangle(CLAMP, CLAMP + SERVICE_SLIDE).locate(
            Location((0, -SERVICE_SLIDE / 2))
        ),
    )
    withdrawal = through_profile(
        pl,
        LAND_H,
        12.00,
        Rectangle(CADDY_OUT, CADDY_OUT),
    )
    return driver, slide, withdrawal


def conservative_metrics(shape):
    bb = shape.bounding_box()
    x = max(abs(bb.min.X), abs(bb.max.X))
    y = max(abs(bb.min.Y), abs(bb.max.Y))
    radial = hypot(x, y)
    return bb, radial, ENV_R - radial, ENV_H - bb.max.Z


def boxes_overlap(a, b, tolerance=1e-7):
    aa, bb = a.bounding_box(), b.bounding_box()
    return not (
        aa.max.X < bb.min.X - tolerance
        or bb.max.X < aa.min.X - tolerance
        or aa.max.Y < bb.min.Y - tolerance
        or bb.max.Y < aa.min.Y - tolerance
        or aa.max.Z < bb.min.Z - tolerance
        or bb.max.Z < aa.min.Z - tolerance
    )


def collision_report(items):
    maximum, pair = 0.0, "none"
    positive = []
    checked = 0
    for i, (na, sa) in enumerate(items):
        for nb, sb in items[i + 1 :]:
            if not boxes_overlap(sa, sb):
                continue
            checked += 1
            vol = (sa & sb).volume
            if vol > 1e-6:
                positive.append((na, nb, vol))
            if vol > maximum:
                maximum, pair = vol, f"{na}<->{nb}"
    return maximum, pair, positive, checked


def overlap_with_exclusions(service, items, excluded_prefixes):
    result = []
    for name, shape in items:
        if any(name.startswith(prefix) for prefix in excluded_prefixes):
            continue
        if boxes_overlap(service, shape):
            vol = (service & shape).volume
            if vol > 1e-6:
                result.append((name, vol))
    return result


def binary_stl_triangles(path: Path):
    data = path.read_bytes()
    if len(data) < 84:
        raise RuntimeError(f"short STL: {path}")
    count = struct.unpack_from("<I", data, 80)[0]
    expected = 84 + count * 50
    if len(data) != expected:
        raise RuntimeError(f"binary STL length mismatch: {len(data)} != {expected}")
    return count


def export_with_short_name(shape, temp: str, final: str, kind: str):
    temp_path = OUT / temp
    final_path = OUT / final
    for path in (temp_path, final_path):
        if path.exists():
            path.unlink()
    if kind == "step":
        export_step(shape, temp_path)
    else:
        export_stl(shape, temp_path)
    temp_path.replace(final_path)
    return final_path


def main():
    bracket = make_folded_bracket()
    if len(bracket.solids()) != 1:
        raise RuntimeError(f"folded bracket has {len(bracket.solids())} solids, expected one")

    planes = face_planes()
    posts = [make_post(x, y) for x in (-POST_XY, POST_XY) for y in (-POST_XY, POST_XY)]
    post_bolts = [
        make_post_bolt(x, y) for x in (-POST_XY, POST_XY) for y in (-POST_XY, POST_XY)
    ]

    lands = []
    caddies = []
    lccs = []
    guards = []
    clamps = []
    face_nuts = []
    nut_lances = []
    face_bolts = []
    services = {}
    for axis, pl in planes.items():
        lands.append([make_land(pl, u, v) for u, v in LAND_UV])
        caddies.append(make_caddy(pl))
        lccs.append(make_lcc_envelope(pl))
        guards.append(make_guard(pl, GUARD_START))
        clamps.append(make_clamp(pl))
        face_nuts.append(make_face_nut(pl))
        nut_lances.append(make_nut_lance(pl))
        face_bolts.append(make_face_bolt(pl))
        services[axis] = make_service_keepouts(pl)

    strain_clips, strain_nuts, strain_bolts = [], [], []
    for screw_xy, cable_xy in zip(STRAIN_SCREW_XY, HARNESS_XY):
        clip, nut, bolt = make_clip_and_hardware(screw_xy, cable_xy)
        strain_clips.append(clip)
        strain_nuts.append(nut)
        strain_bolts.append(bolt)

    physical_items = [("folded_bracket", bracket)]
    physical_items += [(f"post_{i+1}", shape) for i, shape in enumerate(posts)]
    physical_items += [(f"post_bolt_{i+1}", shape) for i, shape in enumerate(post_bolts)]
    for ai, axis in enumerate(planes):
        physical_items += [
            (f"{axis}_land_{li+1}", shape) for li, shape in enumerate(lands[ai])
        ]
        physical_items += [
            (f"{axis}_caddy", caddies[ai]),
            (f"{axis}_lcc_envelope", lccs[ai]),
            (f"{axis}_guard", guards[ai]),
            (f"{axis}_clamp", clamps[ai]),
            (f"{axis}_face_nut", face_nuts[ai]),
            (f"{axis}_nut_lance", nut_lances[ai]),
            (f"{axis}_face_bolt", face_bolts[ai]),
        ]
    physical_items += [(f"strain_clip_{i+1}", shape) for i, shape in enumerate(strain_clips)]
    physical_items += [(f"strain_nut_{i+1}", shape) for i, shape in enumerate(strain_nuts)]
    physical_items += [(f"strain_bolt_{i+1}", shape) for i, shape in enumerate(strain_bolts)]

    invalid = [name for name, shape in physical_items if not shape.is_valid]
    if invalid:
        raise RuntimeError(f"invalid shapes: {invalid}")

    # Export untouched shapes before diagnostic Booleans (OCCT history workaround).
    bracket_path = export_with_short_name(
        bracket, "b.step", "50B_BRACKET_NFF.step", "step"
    )
    reference_guard = make_guard(Plane.XY, 0)
    guard_path = export_with_short_name(
        reference_guard, "g.stl", "50B_GUARD_NFF.stl", "stl"
    )
    reference_caddy = make_caddy(Plane.XY)
    caddy_path = export_with_short_name(
        reference_caddy, "c.step", "50B_CADDY_NFF.step", "step"
    )
    assembly = Compound(children=[shape for _, shape in physical_items])
    assembly_stl_path = export_with_short_name(
        assembly, "a.stl", "50B_COST_DOWN_NFF.stl", "stl"
    )
    step_path = export_with_short_name(
        assembly, "a.step", "50B_COST_DOWN_NFF.step", "step"
    )
    service_shapes = [shape for triple in services.values() for shape in triple]
    service_path = export_with_short_name(
        Compound(children=service_shapes),
        "s.step",
        "50B_SERVICE_KEEPOUTS_NFF.step",
        "step",
    )

    maximum, pair, positive, boolean_pairs = collision_report(physical_items)
    if positive:
        raise RuntimeError(f"unintended overlaps: {positive}")

    harness_keepouts = [
        Box(
            HARNESS_CORRIDOR,
            HARNESS_CORRIDOR,
            BASE_TOP + 0.50,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        ).locate(Location((x, y, 0)))
        for x, y in HARNESS_XY
    ]
    cable_frame_overlap = max((shape & bracket).volume for shape in harness_keepouts)
    if cable_frame_overlap > 1e-6:
        raise RuntimeError(
            f"harness corridor intersects bracket by {cable_frame_overlap:.6f} mm3"
        )

    # Service checks exclude only the target face and target fastener.  Sliding
    # occurs after screw removal; withdrawal occurs after clamp removal.
    service_results = []
    for axis, (driver, slide, withdrawal) in services.items():
        exclusions = (f"{axis}_",)
        driver_hits = overlap_with_exclusions(driver, physical_items, exclusions)
        slide_hits = overlap_with_exclusions(slide, physical_items, exclusions)
        withdrawal_hits = overlap_with_exclusions(withdrawal, physical_items, exclusions)
        service_results.append((axis, driver_hits, slide_hits, withdrawal_hits))
    if any(a or b or c for _, a, b, c in service_results):
        raise RuntimeError(f"service keepout interference: {service_results}")

    bb, radial, radial_margin, height_margin = conservative_metrics(assembly)
    if radial > ENV_R or bb.min.Z < -1e-6 or bb.max.Z > ENV_H:
        raise RuntimeError("physical assembly violates hard envelope")

    min_post_radius = hypot(POST_XY, POST_XY) - POST_R
    lowest_central_hardware = BASE_Z - NUT_T
    if min_post_radius <= FT_KEEP_R or lowest_central_hardware <= FT_KEEP_H:
        raise RuntimeError("feedthrough keepout violated")

    # Explicit reaction checks.
    post_contact = [shape.distance_to(bracket) for shape in posts]
    post_head_contact = [
        post_bolts[i].distance_to(bracket) for i in range(len(post_bolts))
    ]
    nut_contact = [shape.distance_to(bracket) for shape in face_nuts]
    lance_contact = [shape.distance_to(bracket) for shape in nut_lances]
    land_bracket_contact = [shape.distance_to(bracket) for group in lands for shape in group]
    land_caddy_contact = [
        lands[ai][li].distance_to(caddies[ai])
        for ai in range(3)
        for li in range(3)
    ]
    clamp_caddy_contact = [clamps[i].distance_to(caddies[i]) for i in range(3)]
    clip_bracket_contact = [shape.distance_to(bracket) for shape in strain_clips]
    strain_nut_contact = [shape.distance_to(bracket) for shape in strain_nuts]
    all_contacts = (
        post_contact
        + post_head_contact
        + nut_contact
        + lance_contact
        + land_bracket_contact
        + land_caddy_contact
        + clamp_caddy_contact
        + clip_bracket_contact
        + strain_nut_contact
    )
    if max(all_contacts) > 1e-5:
        raise RuntimeError(f"required reaction contact open: max={max(all_contacts)}")

    # Open-slot and insertion arithmetic.
    slot_overtravel = -FACE_HALF - SLOT_V0
    required_slide = FACE_HALF + HOOK_LIP_V / 2 - abs(HOOK_UV[0][1])
    slide_margin = SERVICE_SLIDE - required_slide
    if slot_overtravel <= 0 or slide_margin < -1e-9 or SLOT_W <= HOOK_STEM_W:
        raise RuntimeError("hook-slot release geometry failed")

    # Export/re-import and one-geometry identity checks.
    reimport = import_step(step_path)
    rb, rradial, _, _ = conservative_metrics(reimport)
    delta = max(
        abs(rradial - radial),
        abs(rb.min.Z - bb.min.Z),
        abs(rb.max.Z - bb.max.Z),
    )
    guard_mesh = import_stl(guard_path)
    assembly_mesh = import_stl(assembly_stl_path)
    guard_triangles = binary_stl_triangles(guard_path)
    assembly_triangles = binary_stl_triangles(assembly_stl_path)
    guard_volumes = [shape.volume for shape in guards]
    guard_identity_delta = max(guard_volumes) - min(guard_volumes)
    if (
        delta > 0.001
        or guard_triangles <= 0
        or assembly_triangles <= 0
        or len(guard_mesh.faces()) <= 0
        or len(assembly_mesh.faces()) <= 0
        or guard_identity_delta > 1e-6
    ):
        raise RuntimeError("export/re-import or repeated-guard identity validation failed")

    # First-order expansion is displacement arithmetic only, never preload proof.
    lateral_delta = (9.5 - 7.2) * 1e-6 * GUARD * 230
    normal_delta = (9.5 - 7.2) * 1e-6 * CADDY_T * 230
    prior_cage_volume = 440.917
    support_volume = bracket.volume + sum(shape.volume for shape in posts)
    support_reduction = 1 - support_volume / prior_cage_volume

    physical_names = ", ".join(name for name, _ in physical_items)
    lines = [
        "HSX Stage-50D corrected cost-down package CAD -- NOT FOR FABRICATION",
        f"hard envelope: radius<={ENV_R:.3f} mm height<={ENV_H:.3f} mm",
        f"physical bbox=({bb.min.X:.3f},{bb.max.X:.3f})x({bb.min.Y:.3f},{bb.max.Y:.3f}) z=({bb.min.Z:.3f},{bb.max.Z:.3f}) mm",
        f"conservative bbox-corner radial={radial:.3f} mm margin={radial_margin:.3f} mm height_margin={height_margin:.3f} mm",
        f"physical envelopes={len(physical_items)}; bbox-overlap Boolean pairs={boolean_pairs}; unintended overlap={maximum:.6f} mm3 ({pair})",
        f"folded bracket solids={len(bracket.solids())}; volume={bracket.volume:.3f} mm3; intended main bends=2; exact flat pattern/bend relief HOLD",
        f"folded bracket plus four vented posts volume={support_volume:.3f} mm3 vs prior cage={prior_cage_volume:.3f} mm3; geometric reduction={100*support_reduction:.1f} percent (not price)",
        f"true open U-slot: local end={SLOT_V0:.3f} vs face edge={-FACE_HALF:.3f} mm; edge overtravel={slot_overtravel:.3f} mm",
        f"hook release: lip requires {required_slide:.3f} mm center motion; service sweep={SERVICE_SLIDE:.3f} mm; margin={slide_margin:.3f} mm; slot/stem lateral clearance={SLOT_W-HOOK_STEM_W:.3f} mm",
        f"cartridge: caddy={CADDY_OUT:.2f} square x {CADDY_T:.2f} deep; LCC envelope={LCC:.2f} square x {LCC_T:.2f}; guard={GUARD:.2f} square x {GUARD_T:.3f}; no adhesive",
        f"guard reference: local pigtail notch=-X; screw relief=-Y; three volumes={[round(x, 6) for x in guard_volumes]}; identity delta={guard_identity_delta:.9f} mm3",
        "guard arrangement: one reference profile, rotation-only X/Y/Z face frames, never mirrored; LCC chamfer/orientation traveler remains controlling",
        f"explicit reactions: lands=9; post={post_contact}; post-head={post_head_contact}; face-nut={nut_contact}; nut-lance={lance_contact}",
        f"land-bracket={land_bracket_contact}; land-caddy={land_caddy_contact}; clamp-caddy={clamp_caddy_contact}; clip-bracket={clip_bracket_contact}; strain-nut={strain_nut_contact} mm",
        f"feedthrough keepout: post_min_radius={min_post_radius:.3f} vs {FT_KEEP_R:.3f} mm; lowest face/strain hardware={lowest_central_hardware:.3f} vs {FT_KEEP_H:.3f} mm; clearance={lowest_central_hardware-FT_KEEP_H:.3f} mm",
        f"3x cable keepouts={HARNESS_CORRIDOR:.2f}-mm square; cable-to-bracket overlap={cable_frame_overlap:.6f} mm3; clips deliberately cross cable keepouts and react at adjacent lugs",
        f"service checks (non-target hardware): {service_results}",
        f"STEP reimport bound delta={delta:.6f} mm; assembly binary STL triangles={assembly_triangles}; guard binary STL triangles={guard_triangles}",
        "fixed structural ceramic count=0; flat guard geometry count=1; guard quantity=3; tapped/internal ceramic threads=0",
        "guard material is intentionally neutral: quote 99.6% alumina and flat ZTA/zirconia; select only after edge/contact/UHV/hot coupons",
        f"first-order Ti-minus-alumina displacement 20-to-250C: lateral over {GUARD:.2f} mm={lateral_delta:.6f} mm; normal over {CADDY_T:.2f} mm={normal_delta:.6f} mm; force not qualified",
        "one-screw/two-hook baseline is HOLD pending FEA and hot-cycle coupons; use two-screw-per-face fallback if it fails",
        "formed-axis release requires measured lands/planes, full 3x3 calibration at 20/250C, repeat after bake/hot/service, and complete-head magnetic field map",
        "physical item names: " + physical_names,
        f"exports: {step_path.name}; {assembly_stl_path.name}; {bracket_path.name}; {caddy_path.name}; {guard_path.name}; {service_path.name}",
        "release holds: material lots and 250C UHV life; laser/formed edges; bend/developable flat pattern/GD&T; caddy assembly method; clamp load/fatigue; nut-lance forming; post thread/vent detail; exact delivered cable/strain hardware; feedthrough datum; magnetic error budget; full hot-UHV qualification",
    ]
    report = "\n".join(lines) + "\n"
    (OUT / "50B_CAD_KERNEL_REPORT.txt").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
