"""Parametric concept CAD for the HSX 3-axis 250 C UHV sensor head.

All dimensions are fired/finished millimetres.  All exports are NOT FOR FABRICATION.
The script validates conservative bounding boxes and an explicit feedthrough keep-out.
It intentionally models the package at concept/clearance level; vendor tolerances,
fastener preload, exact contacts, and the mated 19C height remain release gates.
"""

from __future__ import annotations

from math import hypot
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

# Hard envelope and conservative unresolved feedthrough keep-out.
ENV_R = 31.75 / 2
ENV_H = 27.5
FT_KEEP_R = 22.10 / 2       # drawing reference diameter 0.87 in
FT_KEEP_H = 10.41           # drawing feature 0.410 in; interpretation HOLD
BRIDGE_Z = 11.50            # exposed parameter; 1.09 mm above FT_KEEP_H

# Common fired concept dimensions.
BRIDGE = 15.0
BRIDGE_T = 1.0
POST_XY = 9.0
POST_R = 1.15
HEAD_Z0 = BRIDGE_Z + BRIDGE_T
LCC = 8.89
LCC_T = 1.65
CART = 10.90                # protected cartridge guard outer width, PROPOSAL
CART_T = 2.40               # LCC + vented guard envelope, PROPOSAL
CLAMP = 15.60              # external Ti ears keep all fasteners outside ceramic
CLAMP_T = 0.50
WINDOW = 6.4
HOLE_R = 0.90               # M1.6-class Ti-frame clearance; exact fastener HOLD
HARNESS = 3.0                # reserved four-conductor branch corridor, PROPOSAL
HARNESS_XY = ((-6.3, 3.8), (3.8, -6.3), (-6.3, -3.8))
STRAIN_XY = ((-6.3, 1.6), (1.6, -6.3), (-6.3, -6.3))


def face_planes(center_z: float, half: float):
    """Local XY lies on face; local +Z points outward."""
    return {
        "X": Plane(origin=(0, 0, center_z), x_dir=(0, 1, 0), z_dir=(1, 0, 0)),
        "Y": Plane(origin=(0, 0, center_z), x_dir=(1, 0, 0), z_dir=(0, 1, 0)),
        "Z": Plane(origin=(0, 0, center_z), x_dir=(1, 0, 0), z_dir=(0, 0, 1)),
    }


def common_supports():
    """Connected CP-Ti base frame plus four conceptual CP-Ti support posts."""
    bridge = Box(
        BRIDGE, BRIDGE, BRIDGE_T,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((0, 0, BRIDGE_Z)))
    # Four simple L-shaped ears connect the central frame to all four posts.
    for sx in (-1, 1):
        for sy in (-1, 1):
            bridge += Box(3.0, 1.5, BRIDGE_T).locate(
                Location((sx * 8.0, sy * 6.75, BRIDGE_Z + BRIDGE_T / 2))
            )
            bridge += Box(1.5, 3.0, BRIDGE_T).locate(
                Location((sx * POST_XY, sy * 8.0, BRIDGE_Z + BRIDGE_T / 2))
            )
    # All support holes are in titanium, never zirconia.
    for x in (-POST_XY, POST_XY):
        for y in (-POST_XY, POST_XY):
            bridge -= Cylinder(
                HOLE_R, BRIDGE_T + 2,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
            ).locate(Location((x, y, BRIDGE_Z - 1)))
    # Three non-crossing open edge slots, one per four-conductor branch.
    bridge -= Box(4.0, HARNESS, BRIDGE_T + 2).locate(Location((-BRIDGE / 2, 3.8, BRIDGE_Z + BRIDGE_T / 2)))
    bridge -= Box(HARNESS, 4.0, BRIDGE_T + 2).locate(Location((3.8, -BRIDGE / 2, BRIDGE_Z + BRIDGE_T / 2)))
    bridge -= Box(4.0, HARNESS, BRIDGE_T + 2).locate(Location((-BRIDGE / 2, -3.8, BRIDGE_Z + BRIDGE_T / 2)))

    # Three independent external strain-relief clips. Their fasteners pass only
    # through the Ti base frame and replaceable Ti nut pads.
    strain_parts = []
    for x, y in STRAIN_XY:
        bridge -= Cylinder(
            HOLE_R, BRIDGE_T + 0.4,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        ).locate(Location((x, y, BRIDGE_Z - 0.2)))
        clip_x, clip_y = (1.0, 3.2) if abs(x) > abs(y) else (3.2, 1.0)
        clip = Box(clip_x, clip_y, 0.4, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
            Location((x, y, BRIDGE_Z + BRIDGE_T))
        )
        clip -= Cylinder(
            HOLE_R, 0.8, align=(Align.CENTER, Align.CENTER, Align.MIN)
        ).locate(Location((x, y, BRIDGE_Z + BRIDGE_T - 0.2)))
        nut = Box(1.6, 1.6, 0.4, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
            Location((x, y, BRIDGE_Z - 0.4))
        )
        nut -= Cylinder(
            0.55, 0.8, align=(Align.CENTER, Align.CENTER, Align.MIN)
        ).locate(Location((x, y, BRIDGE_Z - 0.6)))
        screw = Cylinder(
            0.55, 1.9, align=(Align.CENTER, Align.CENTER, Align.MIN)
        ).locate(Location((x, y, BRIDGE_Z - 0.2)))
        strain_parts.extend([clip, nut, screw])

    posts = []
    for x in (-POST_XY, POST_XY):
        for y in (-POST_XY, POST_XY):
            posts.append(Cylinder(
                POST_R, BRIDGE_Z,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
            ).locate(Location((x, y, 0))))
    # Reserved installed-harness volumes below the ceramic bridge. They are
    # deliberately included in envelope metrics; exact wire OD is a release gate.
    harnesses = [
        Box(HARNESS, HARNESS, HEAD_Z0, align=(Align.CENTER, Align.CENTER, Align.MIN))
        .locate(Location((x, y, 0)))
        for x, y in HARNESS_XY
    ]
    return bridge, posts, harnesses, strain_parts


def cartridge_and_clamp(pl: Plane, face: float, hole_uv):
    """Simplified protected cartridge plus external CP-Ti clamp frame and bolts."""
    cartridge = extrude(pl.offset(face) * Rectangle(CART, CART), CART_T)
    # Cavity/guard visualization window does not open through the cartridge base.
    cartridge -= extrude(pl.offset(face + CART_T - 0.70) * Rectangle(WINDOW, WINDOW), 0.80)

    clamp = extrude(pl.offset(face + CART_T) * Rectangle(CLAMP, CLAMP), CLAMP_T)
    clamp -= extrude(pl.offset(face + CART_T - 0.2) * Rectangle(WINDOW + 0.8, WINDOW + 0.8), CLAMP_T + 0.5)
    bolts = []
    for u, v in hole_uv:
        clamp -= extrude(pl.offset(face + CART_T - 0.5) * Circle(HOLE_R).locate(Location((u, v))), CLAMP_T + 1.5)
        # Concept-level external fastener envelope: 0.6 mm rear engagement and
        # 0.3 mm head/projection beyond the clamp. Exact hardware remains HOLD.
        nutpad = extrude(
            pl.offset(face - 0.6) * Rectangle(1.6, 1.6).locate(Location((u, v))),
            0.6,
        )
        nutpad -= extrude(
            pl.offset(face - 0.7) * Circle(0.65).locate(Location((u, v))),
            0.8,
        )
        bolts.extend([nutpad, extrude(
            pl.offset(face - 0.6) * Circle(0.65).locate(Location((u, v))),
            CART_T + CLAMP_T + 0.9,
        )])
    return cartridge, clamp, bolts


def conservative_metrics(shape, name: str):
    bb = shape.bounding_box()
    x = max(abs(bb.min.X), abs(bb.max.X))
    y = max(abs(bb.min.Y), abs(bb.max.Y))
    radial_box = hypot(x, y)   # conservative: combines independent x/y extrema
    zmin, zmax = bb.min.Z, bb.max.Z
    passed = radial_box <= ENV_R + 1e-6 and zmin >= -1e-6 and zmax <= ENV_H + 1e-6
    return {
        "name": name,
        "xmin": bb.min.X, "xmax": bb.max.X,
        "ymin": bb.min.Y, "ymax": bb.max.Y,
        "zmin": zmin, "zmax": zmax,
        "radial_box": radial_box,
        "radial_margin": ENV_R - radial_box,
        "height_margin": ENV_H - zmax,
        "envelope_pass": passed,
    }


def collision_report(items):
    """Return the largest unintended pairwise solid overlap in mm^3."""
    maximum, pair = 0.0, "none"
    for i, (name_a, shape_a) in enumerate(items):
        for name_b, shape_b in items[i + 1:]:
            volume = (shape_a & shape_b).volume
            if volume > maximum:
                maximum, pair = volume, f"{name_a}<->{name_b}"
    return maximum, pair


def export_concept(name: str, parts, ceramic_export, metrics):
    asm = Compound(children=parts)
    export_step(asm, OUT / f"{name}_NOT_FOR_FABRICATION.step")
    export_stl(ceramic_export, OUT / f"{name}_ceramic_NOT_FOR_FABRICATION.stl")
    metrics.append(conservative_metrics(asm, name))
    return asm


def concept_a(metrics):
    """A: three identical flat zirconia seat plates in an external Ti rear cage."""
    bridge, posts, harnesses, strain_parts = common_supports()
    span, size, pt = 10.0, 9.60, 1.00
    half, cz = span / 2, HEAD_Z0 + span / 2
    planes = face_planes(cz, half)
    holes = {
        "X": [(-6.5, -2.0), (-6.5, 2.0)],
        "Y": [(-6.5, -2.0), (-6.5, 2.0)],
        "Z": [(-6.5, 0.0), (0.0, -6.5)],
    }
    plates, carts, clamps, bolts = [], [], [], []
    for key, pl in planes.items():
        p = extrude(pl.offset(half) * Rectangle(size, size), pt)
        p -= extrude(pl.offset(half - 0.2) * Rectangle(WINDOW, WINDOW), pt + 0.4)
        # Open one-side tongue/harness notch; no hidden groove.
        p -= extrude(pl.offset(half - 0.2) * Rectangle(2.2, 2.8).locate(Location((0, -size/2 + 1.2))), pt + 0.4)
        plates.append(p)
        c, f, b = cartridge_and_clamp(pl, half + pt, holes[key])
        carts.append(c); clamps.append(f); bolts.extend(b)

    # External CP-Ti rear rails; plate geometry remains three identical ceramics.
    rails = [
        Box(1.0, 1.0, span).locate(Location((-half + 0.5, -half + 0.5, cz))),
        Box(1.0, span, 1.0).locate(Location((-half + 0.5, 0, HEAD_Z0 + 0.5))),
        Box(span, 1.0, 1.0).locate(Location((0, -half + 0.5, HEAD_Z0 + 0.5))),
    ]
    ceramic = Compound(children=plates)
    parts = [bridge] + posts + harnesses + strain_parts + plates + carts + clamps + bolts + rails
    asm = export_concept("30A_triplate_cage", parts, ceramic, metrics)
    check_items = (
        [(f"plate{i+1}", s) for i, s in enumerate(plates)]
        + [(f"cartridge{i+1}", s) for i, s in enumerate(carts)]
        + [(f"clamp{i+1}", s) for i, s in enumerate(clamps)]
        + [(f"fastener_part{i+1}", s) for i, s in enumerate(bolts)]
        + [(f"strain_part{i+1}", s) for i, s in enumerate(strain_parts)]
    )
    metrics[-1]["collision_max"], metrics[-1]["collision_pair"] = collision_report(check_items)
    return asm


def concept_b(metrics):
    """B: simplified monolithic zirconia core with open bottom and external clamps."""
    bridge, posts, harnesses, strain_parts = common_supports()
    size = 11.3
    half, cz = size / 2, HEAD_Z0 + size / 2
    planes = face_planes(cz, half)
    holes = {
        "X": [(-6.5, -2.0), (-6.5, 2.0)],
        "Y": [(-6.5, -2.0), (-6.5, 2.0)],
        "Z": [(-6.5, 0.0), (0.0, -6.5)],
    }
    core = Box(size, size, size).locate(Location((0, 0, cz)))
    # Open bottom access: straight tool, no blind nut trap; 2 mm nominal side web.
    core -= Box(8.0, 8.0, 7.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(Location((0, 0, HEAD_Z0 - 0.2)))
    carts, clamps, bolts = [], [], []
    for key, pl in planes.items():
        core -= extrude(pl.offset(half + 0.2) * Rectangle(6.80, 6.80), -0.60)
        # Open harness slot from face pocket toward open bottom/rear.
        core -= extrude(pl.offset(half + 0.2) * Rectangle(2.4, 3.5).locate(Location((0, -half + 1.2))), -2.0)
        c, f, b = cartridge_and_clamp(pl, half, holes[key])
        carts.append(c); clamps.append(f); bolts.extend(b)
    ceramic = Compound(children=[core])
    parts = [bridge] + posts + harnesses + strain_parts + [core] + carts + clamps + bolts
    asm = export_concept("30B_monolithic_core", parts, ceramic, metrics)
    check_items = (
        [("core", core)]
        + [(f"cartridge{i+1}", s) for i, s in enumerate(carts)]
        + [(f"clamp{i+1}", s) for i, s in enumerate(clamps)]
        + [(f"fastener_part{i+1}", s) for i, s in enumerate(bolts)]
        + [(f"strain_part{i+1}", s) for i, s in enumerate(strain_parts)]
    )
    metrics[-1]["collision_max"], metrics[-1]["collision_pair"] = collision_report(check_items)
    return asm


def concept_c(metrics):
    """C: protected split cassettes docking to a small open zirconia core."""
    bridge, posts, harnesses, strain_parts = common_supports()
    core_size = 10.5
    half, cz = core_size / 2, HEAD_Z0 + core_size / 2
    planes = face_planes(cz, half)
    core = Box(core_size, core_size, core_size).locate(Location((0, 0, cz)))
    core -= Box(6.5, 6.5, 7.5, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(Location((0, 0, HEAD_Z0 - 0.2)))
    cassette_outer, rear_t, front_t, cassette_t = 9.80, 1.00, 0.50, 3.25
    split_parts, cassette_ceramics, rails, pins = [], [], [], []
    # Pin axes/ear placement are conceptual; exact transverse holes are frozen in ledger after vendor input.
    holes = {
        "X": [(-6.10, -3.0), (-6.10, -1.5)],
        "Y": [(-6.10, -0.5), (-6.10, -2.0)],
        "Z": [(-6.10, 0.0), (0.0, -6.10)],
    }
    for key, pl in planes.items():
        rear = extrude(pl.offset(half) * Rectangle(cassette_outer, cassette_outer), rear_t)
        rear -= extrude(pl.offset(half - 0.2) * Rectangle(WINDOW, WINDOW), rear_t + 0.5)
        front = extrude(pl.offset(half + cassette_t - front_t) * Rectangle(cassette_outer, cassette_outer), front_t)
        front -= extrude(pl.offset(half + cassette_t - front_t - 0.2) * Rectangle(WINDOW, WINDOW), front_t + 0.5)
        lcc = extrude(pl.offset(half + rear_t) * Rectangle(LCC, LCC), LCC_T)
        # Two straight side rails, externally accessible; cartridge slides normal to face while guarded.
        rail1 = extrude(pl.offset(half) * Rectangle(1.0, cassette_outer + 0.8).locate(Location((-cassette_outer/2 - 0.8, 0))), cassette_t + 0.2)
        rail2 = extrude(pl.offset(half) * Rectangle(1.0, cassette_outer + 0.8).locate(Location((cassette_outer/2 + 0.8, 0))), cassette_t + 0.2)
        for uv in holes[key]:
            # 0.6 mm rear engagement and 0.3 mm exterior projection.
            pin = extrude(pl.offset(half - 0.2) * Circle(0.70).locate(Location(uv)), cassette_t + 0.5)
            pins.append(pin)
        split_parts.extend([rear, front, lcc]); cassette_ceramics.append(rear); rails.extend([rail1, rail2])
    ceramic = Compound(children=[core] + cassette_ceramics)
    rail_cage = rails[0]
    for rail in rails[1:]:
        rail_cage += rail
    parts = [bridge] + posts + harnesses + strain_parts + [core] + split_parts + [rail_cage] + pins
    asm = export_concept("30C_split_cassette", parts, ceramic, metrics)
    body_items = [("core", core), ("shared_rail_cage", rail_cage)] + [
        (f"cassette_part{i+1}", s) for i, s in enumerate(split_parts)
    ] + [(f"strain_part{i+1}", s) for i, s in enumerate(strain_parts)]
    body_max, body_pair = collision_report(body_items)
    pin_max, pin_pair = collision_report(
        [("core", core)]
        + [(f"cassette_part{i+1}", s) for i, s in enumerate(split_parts)]
        + [(f"pin{i+1}", s) for i, s in enumerate(pins)]
    )
    metrics[-1]["collision_max"] = max(body_max, pin_max)
    metrics[-1]["collision_pair"] = body_pair if body_max >= pin_max else pin_pair
    return asm


def main():
    metrics = []
    concept_a(metrics)
    concept_b(metrics)
    concept_c(metrics)

    min_post_radius = hypot(POST_XY, POST_XY) - POST_R
    keepout_ok = BRIDGE_Z > FT_KEEP_H and min_post_radius > FT_KEEP_R
    lines = [
        "HSX stage-30 CAD kernel report — NOT FOR FABRICATION",
        f"ENV_R={ENV_R:.3f} mm ENV_H={ENV_H:.3f} mm",
        f"FT_KEEP_R={FT_KEEP_R:.3f} mm FT_KEEP_H={FT_KEEP_H:.3f} mm BRIDGE_Z={BRIDGE_Z:.3f} mm",
        f"installed harness reservation: three {HARNESS:.1f} x {HARNESS:.1f} mm branch corridors at {HARNESS_XY}",
        f"independent strain-relief axes at {STRAIN_XY}; clips and fasteners included in envelope",
        f"post_min_radius={min_post_radius:.3f} mm keepout_pass={keepout_ok}",
    ]
    for m in metrics:
        lines.append(
            f"{m['name']}: bbox=({m['xmin']:.3f},{m['xmax']:.3f})x"
            f"({m['ymin']:.3f},{m['ymax']:.3f}) z=({m['zmin']:.3f},{m['zmax']:.3f}); "
            f"conservative_radial={m['radial_box']:.3f} margin={m['radial_margin']:.3f}; "
            f"height_margin={m['height_margin']:.3f}; pass={m['envelope_pass']}; "
            f"unintended_pair_overlap={m['collision_max']:.6f} mm^3 ({m['collision_pair']})"
        )
        if m["collision_max"] > 1e-6:
            print("\n".join(lines))
            raise RuntimeError(f"{m['name']} has an unintended modeled collision")
        if not m["envelope_pass"]:
            print("\n".join(lines))
            raise RuntimeError(f"{m['name']} violates envelope")
    # Durable export verification: re-import every STEP with the same CAD kernel
    # and every ceramic STL, then compare bounds/positive volume.
    for m in metrics:
        name = m["name"]
        step_shape = import_step(OUT / f"{name}_NOT_FOR_FABRICATION.step")
        step_m = conservative_metrics(step_shape, f"{name}_reimport")
        delta = max(
            abs(step_m["radial_box"] - m["radial_box"]),
            abs(step_m["zmin"] - m["zmin"]),
            abs(step_m["zmax"] - m["zmax"]),
        )
        stl_shape = import_stl(OUT / f"{name}_ceramic_NOT_FOR_FABRICATION.stl")
        stl_faces = len(stl_shape.faces())
        stl_bb = stl_shape.bounding_box()
        stl_span = max(stl_bb.size.X, stl_bb.size.Y, stl_bb.size.Z)
        lines.append(
            f"{name}: STEP reimport delta={delta:.6f} mm pass={step_m['envelope_pass'] and delta <= 0.001}; "
            f"ceramic_STL_faces={stl_faces} max_span={stl_span:.6f} mm"
        )
        if not step_m["envelope_pass"] or delta > 0.001 or stl_faces <= 0 or stl_span <= 0:
            print("\n".join(lines))
            raise RuntimeError(f"{name} export re-import validation failed")
    if not keepout_ok:
        raise RuntimeError("common support intersects conservative feedthrough keep-out")
    report = "\n".join(lines) + "\n"
    (OUT / "30_CAD_KERNEL_REPORT.txt").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
