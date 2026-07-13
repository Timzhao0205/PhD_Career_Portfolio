"""Corrected final-direction CAD for the HSX 250 C UHV three-axis head.

All dimensions are finished millimetres.  This model resolves the Stage-40
free-nut-reaction and 3.00-mm cable-corridor contradictions at architecture
level.  It remains NOT FOR FABRICATION because material lots, flexure force,
connector datum, cable selection and vendor DFM are open release gates.
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

ENV_R = 31.75 / 2
ENV_H = 27.50
FT_KEEP_R = 22.10 / 2
FT_KEEP_H = 10.41
BRIDGE_Z = 11.50
BRIDGE_T = 1.00
POST_XY = 9.00
POST_R = 1.15
HEAD_Z0 = BRIDGE_Z + BRIDGE_T

SPAN = 10.00
SEAT = 9.60
SEAT_T = 1.00
CART = 10.90
CART_T = 2.40
CLAMP = 15.60
CLAMP_T = 0.50
WINDOW = 6.40
FASTENER_CLEAR_R = 0.90
SCREW_R = 0.55

# Two delivered KAP301 pairs can require 2*(1.50+0.15)=3.30 mm.
# 3.80 mm leaves 0.50 mm total installation allowance; still a proposal.
HARNESS_CORRIDOR = 3.80
HARNESS_XY = ((-6.30, 3.80), (3.80, -6.30), (-6.30, -3.80))
STRAIN_XY = ((-6.30, 2.60), (2.60, -6.30), (-6.30, -6.30))


def face_planes(center_z: float, half: float):
    """Local XY lies on face; local +Z points outward."""
    return {
        "X": Plane(origin=(0, 0, center_z), x_dir=(0, 1, 0), z_dir=(1, 0, 0)),
        "Y": Plane(origin=(0, 0, center_z), x_dir=(1, 0, 0), z_dir=(0, 1, 0)),
        "Z": Plane(origin=(0, 0, center_z), x_dir=(1, 0, 0), z_dir=(0, 0, 1)),
    }


def axis_plane(axis: str, origin):
    if axis == "X":
        return Plane(origin=origin, x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    if axis == "Y":
        return Plane(origin=origin, x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    return Plane(origin=origin, x_dir=(1, 0, 0), z_dir=(0, 0, 1))


def cylinder_along(axis: str, origin, radius: float, length: float):
    return extrude(axis_plane(axis, origin) * Circle(radius), length)


def open_ring(axis: str, face: float, center_z: float):
    """Connected CP-Ti open backframe that reacts a flat zirconia seat."""
    pl = face_planes(center_z, SPAN / 2)[axis]
    if axis in ("X", "Y"):
        outer = extrude(pl.offset(face - 0.30) * Rectangle(9.80, 10.00), 0.30)
        inner = extrude(pl.offset(face - 0.35) * Rectangle(7.60, 7.60), 0.40)
    else:
        outer = extrude(pl.offset(face - 0.30) * Rectangle(9.80, 9.80), 0.30)
        inner = extrude(pl.offset(face - 0.35) * Rectangle(7.60, 7.60), 0.40)
    return outer - inner


def make_connected_cage(center_z: float):
    """Single CP-Ti base/backframe/nut-reaction solid with open access."""
    cage = Box(15.0, 15.0, BRIDGE_T, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
        Location((0, 0, BRIDGE_Z))
    )

    # Four feedthrough posts overlap the bridge by 0.20 mm, making one solid.
    for x in (-POST_XY, POST_XY):
        for y in (-POST_XY, POST_XY):
            cage += Cylinder(
                POST_R,
                BRIDGE_Z + 0.20,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
            ).locate(Location((x, y, 0)))
            if x > 0 and y > 0:
                angle = 45
            elif x < 0 and y > 0:
                angle = 135
            elif x > 0 and y < 0:
                angle = -45
            else:
                angle = -135
            # Diagonal corner spoke stays outside the square side-clamp swept
            # volumes while overlapping both the bridge corner and post.
            cage += Box(3.20, 0.80, BRIDGE_T).locate(
                Location((x * 8.25 / 9, y * 8.25 / 9, BRIDGE_Z + BRIDGE_T / 2), (0, 0, angle))
            )

    # Open cable slots sized to the new 3.80-mm corridor.
    cage -= Box(4.2, HARNESS_CORRIDOR, BRIDGE_T + 2).locate(
        Location((-7.5, 3.80, BRIDGE_Z + BRIDGE_T / 2))
    )
    cage -= Box(HARNESS_CORRIDOR, 4.2, BRIDGE_T + 2).locate(
        Location((3.80, -7.5, BRIDGE_Z + BRIDGE_T / 2))
    )
    cage -= Box(4.2, HARNESS_CORRIDOR, BRIDGE_T + 2).locate(
        Location((-7.5, -3.80, BRIDGE_Z + BRIDGE_T / 2))
    )

    # The X/Y cartridges extend 0.45 mm below the nominal bridge top.  Open
    # edge reliefs prevent the base plate from occupying those service volumes.
    cage -= Box(1.70, 11.20, 0.80).locate(Location((6.65, 0.0, 12.20)))
    cage -= Box(11.20, 1.70, 0.80).locate(Location((0.0, 6.65, 12.20)))

    # Open through-holes in posts and bridge: no blind lower attachment volume.
    for x in (-POST_XY, POST_XY):
        for y in (-POST_XY, POST_XY):
            cage -= Cylinder(
                0.72,
                BRIDGE_Z + BRIDGE_T + 0.6,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
            ).locate(Location((x, y, -0.2)))

    # Three seat backframes, connected through the bridge and reaction rails.
    cage += open_ring("X", SPAN / 2, center_z)
    cage += open_ring("Y", SPAN / 2, center_z)
    cage += open_ring("Z", SPAN / 2, center_z)

    # Four continuous rails reach all six clamp-nut reaction sites.
    cage += Box(1.55, 2.20, 9.00, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
        Location((5.575, -6.70, BRIDGE_Z + 0.80))
    )
    cage += Box(2.20, 1.55, 9.00, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
        Location((-6.70, 5.575, BRIDGE_Z + 0.80))
    )
    cage += Box(2.20, 1.40, 11.75, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
        Location((-6.70, 0.0, BRIDGE_Z + 0.80))
    )
    cage += Box(1.40, 2.20, 11.75, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
        Location((0.0, -6.70, BRIDGE_Z + 0.80))
    )

    # Six open-sided nut-cassette pockets; the remaining outward lip is the
    # clamp-load reaction surface.  Retaining keepers carry no clamp load.
    for z in (center_z - 2.0, center_z + 2.0):
        cage -= Box(0.85, 2.10, 1.55).locate(Location((5.375, -6.80, z)))
        cage -= cylinder_along("X", (4.70, -6.50, z), 0.70, 1.90)
        cage -= Box(2.10, 0.85, 1.55).locate(Location((-6.80, 5.375, z)))
        cage -= cylinder_along("Y", (-6.50, 4.70, z), 0.70, 1.90)
    cage -= Box(2.10, 0.85, 0.70).locate(Location((-6.80, 0.0, center_z + 5.65)))
    cage -= cylinder_along("Z", (-6.50, 0.0, center_z + 4.85), 0.70, 1.90)
    cage -= Box(0.85, 2.10, 0.70).locate(Location((0.0, -6.80, center_z + 5.65)))
    cage -= cylinder_along("Z", (0.0, -6.50, center_z + 4.85), 0.70, 1.90)

    # Strain-relief through-holes remain in Ti only.
    for x, y in STRAIN_XY:
        cage -= Cylinder(
            0.75,
            BRIDGE_T + 0.6,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        ).locate(Location((x, y, BRIDGE_Z - 0.3)))

    return cage


def make_nut(axis: str, center):
    """Replaceable vented CP-Ti nut-plate envelope; thread form remains HOLD."""
    if axis == "X":
        nut = Box(0.75, 1.30, 1.30).locate(Location(center))
        start = (center[0] - 0.50, center[1], center[2])
    elif axis == "Y":
        nut = Box(1.30, 0.75, 1.30).locate(Location(center))
        start = (center[0], center[1] - 0.50, center[2])
    else:
        nut = Box(1.30, 0.75, 0.70).locate(Location(center)) if center[0] < 0 else Box(0.75, 1.30, 0.70).locate(Location(center))
        start = (center[0], center[1], center[2] - 0.50)
    nut -= cylinder_along(axis, start, 0.62, 1.60)
    # Longitudinal hole is open at both ends; exact vented screw/nut thread is gated.
    return nut


def make_nuts_and_keepers(center_z: float):
    nuts, keepers = [], []
    for z in (center_z - 2.0, center_z + 2.0):
        nuts.append(("X", make_nut("X", (5.425, -6.50, z))))
        keepers.append(Box(1.55, 0.30, 1.75).locate(Location((5.55, -7.95, z))))
        nuts.append(("Y", make_nut("Y", (-6.50, 5.425, z))))
        keepers.append(Box(0.30, 1.55, 1.75).locate(Location((-7.95, 5.55, z))))
    nuts.append(("Z", make_nut("Z", (-6.50, 0.0, center_z + 5.65))))
    keepers.append(Box(0.30, 1.55, 1.05).locate(Location((-7.95, 0.0, center_z + 5.65))))
    nuts.append(("Z", make_nut("Z", (0.0, -6.50, center_z + 5.65))))
    keepers.append(Box(1.55, 0.30, 1.05).locate(Location((0.0, -7.95, center_z + 5.65))))
    return nuts, keepers


def cartridge_clamp_bolts(pl: Plane, seat_outer_face: float, hole_uv):
    cartridge = extrude(pl.offset(seat_outer_face) * Rectangle(CART, CART), CART_T)
    cartridge -= extrude(
        pl.offset(seat_outer_face + CART_T - 0.70) * Rectangle(WINDOW, WINDOW), 0.80
    )
    clamp = extrude(pl.offset(seat_outer_face + CART_T) * Rectangle(CLAMP, CLAMP), CLAMP_T)
    clamp -= extrude(
        pl.offset(seat_outer_face + CART_T - 0.20) * Rectangle(WINDOW + 0.80, WINDOW + 0.80),
        CLAMP_T + 0.50,
    )
    bolts = []
    for u, v in hole_uv:
        clamp -= extrude(
            pl.offset(seat_outer_face + CART_T - 0.50)
            * Circle(FASTENER_CLEAR_R).locate(Location((u, v))),
            CLAMP_T + 1.50,
        )
        shaft = extrude(
            pl.offset(seat_outer_face - 1.00) * Circle(SCREW_R).locate(Location((u, v))),
            CART_T + CLAMP_T + 1.35,
        )
        head = extrude(
            pl.offset(seat_outer_face + CART_T + CLAMP_T)
            * Circle(1.10).locate(Location((u, v))),
            0.35,
        )
        bolts.append(shaft + head)
    return cartridge, clamp, bolts


def conservative_metrics(shape):
    bb = shape.bounding_box()
    x = max(abs(bb.min.X), abs(bb.max.X))
    y = max(abs(bb.min.Y), abs(bb.max.Y))
    radial = hypot(x, y)
    return bb, radial, ENV_R - radial, ENV_H - bb.max.Z


def collision_report(items):
    maximum, pair = 0.0, "none"
    for i, (na, sa) in enumerate(items):
        for nb, sb in items[i + 1 :]:
            vol = (sa & sb).volume
            if vol > maximum:
                maximum, pair = vol, f"{na}<->{nb}"
    return maximum, pair


def main():
    center_z = HEAD_Z0 + SPAN / 2
    half = SPAN / 2
    planes = face_planes(center_z, half)
    holes = {
        "X": [(-6.50, -2.00), (-6.50, 2.00)],
        "Y": [(-6.50, -2.00), (-6.50, 2.00)],
        "Z": [(-6.50, 0.00), (0.00, -6.50)],
    }

    cage = make_connected_cage(center_z)
    if len(cage.solids()) != 1:
        raise RuntimeError(f"connected cage has {len(cage.solids())} solids, expected one")

    seats, cartridges, clamps, bolts = [], [], [], []
    for key, pl in planes.items():
        seat = extrude(pl.offset(half) * Rectangle(SEAT, SEAT), SEAT_T)
        seat -= extrude(pl.offset(half - 0.20) * Rectangle(WINDOW, WINDOW), SEAT_T + 0.40)
        seat -= extrude(
            pl.offset(half - 0.20)
            * Rectangle(2.20, 2.80).locate(Location((0, -SEAT / 2 + 1.20))),
            SEAT_T + 0.40,
        )
        seats.append(seat)
        cart, clamp, face_bolts = cartridge_clamp_bolts(pl, half + SEAT_T, holes[key])
        cartridges.append(cart)
        clamps.append(clamp)
        bolts.extend(face_bolts)

    axis_nuts, keepers = make_nuts_and_keepers(center_z)
    nuts = [n for _, n in axis_nuts]

    strain_parts = []
    for x, y in STRAIN_XY:
        clip = Box(1.00 if abs(x) > abs(y) else 3.80, 3.80 if abs(x) > abs(y) else 1.00, 0.40).locate(
            Location((x, y, HEAD_Z0 + 0.20))
        )
        clip -= Cylinder(0.75, 0.80, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
            Location((x, y, HEAD_Z0 - 0.20))
        )
        lower_nut = Box(1.60, 1.60, 0.40).locate(Location((x, y, BRIDGE_Z - 0.20)))
        lower_nut -= Cylinder(0.55, 0.80, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
            Location((x, y, BRIDGE_Z - 0.60))
        )
        strain_parts.extend([clip, lower_nut])

    harness_keepouts = [
        Box(HARNESS_CORRIDOR, HARNESS_CORRIDOR, BRIDGE_Z + 0.80, align=(Align.CENTER, Align.CENTER, Align.MIN)).locate(
            Location((x, y, 0))
        )
        for x, y in HARNESS_XY
    ]

    physical_items = (
        [("cage", cage)]
        + [(f"seat_{i+1}", s) for i, s in enumerate(seats)]
        + [(f"cartridge_{i+1}", s) for i, s in enumerate(cartridges)]
        + [(f"clamp_{i+1}", s) for i, s in enumerate(clamps)]
        + [(f"bolt_{i+1}", s) for i, s in enumerate(bolts)]
        + [(f"nut_{i+1}", s) for i, s in enumerate(nuts)]
        + [(f"keeper_{i+1}", s) for i, s in enumerate(keepers)]
        + [(f"strain_{i+1}", s) for i, s in enumerate(strain_parts)]
    )
    max_overlap, overlap_pair = collision_report(physical_items)
    if max_overlap > 1e-6:
        raise RuntimeError(f"unintended overlap {max_overlap:.6f} mm3 at {overlap_pair}")

    assembly = Compound([shape for _, shape in physical_items])
    keepout_assembly = Compound([solid for shape in harness_keepouts for solid in shape.solids()])
    invalid_items = [name for name, shape in physical_items if not shape.is_valid]
    if invalid_items:
        raise RuntimeError(f"invalid physical shapes: {invalid_items}")
    if not assembly.is_valid:
        raise RuntimeError("physical assembly compound is invalid")
    bb, radial, radial_margin, height_margin = conservative_metrics(assembly)
    kb, kradial, kradial_margin, _ = conservative_metrics(Compound(children=[assembly, keepout_assembly]))

    if radial > ENV_R or bb.min.Z < -1e-6 or bb.max.Z > ENV_H:
        raise RuntimeError("physical assembly violates hard envelope")
    if kradial > ENV_R or kb.min.Z < -1e-6 or kb.max.Z > ENV_H:
        raise RuntimeError("assembly plus harness keepouts violates hard envelope")

    min_post_radius = hypot(POST_XY, POST_XY) - POST_R
    keepout_ok = BRIDGE_Z > FT_KEEP_H and min_post_radius > FT_KEEP_R
    if not keepout_ok:
        raise RuntimeError("feedthrough keepout violated")

    # Nut inserts must contact the connected cage reaction lips; their keeper
    # geometry remains replaceable and externally accessible.
    nut_distances = [n.distance_to(cage) for n in nuts]
    if max(nut_distances) > 1e-5:
        raise RuntimeError(f"nut reaction contact open: {nut_distances}")

    # Short filenames avoid an OCCT Windows writer failure on the full workspace
    # path; the controlling NOT-FOR-FABRICATION status is in the model/report.
    step_path = OUT / "50A_FINAL_NFF.step"
    stl_path = OUT / "50A_CERAMIC_NFF.stl"
    keep_path = OUT / "50A_HARNESS_KEEPOUTS_NFF.step"
    for artifact in (step_path, stl_path, keep_path):
        if artifact.exists():
            artifact.unlink()
    try:
        export_assembly = Compound(children=[shape for _, shape in physical_items])
        export_step(export_assembly, step_path)
    except RuntimeError as exc:
        failed = []
        for i, (name, shape) in enumerate(physical_items):
            probe = OUT / f"_50_export_probe_{i:02d}.step"
            try:
                export_step(shape, probe)
            except RuntimeError:
                failed.append(name)
        first_group_failure = None
        for count in range(2, len(physical_items) + 1):
            probe = OUT / "_50_export_group_probe.step"
            group = Compound(children=[shape for _, shape in physical_items[:count]])
            try:
                export_step(group, probe)
            except RuntimeError:
                first_group_failure = (count, physical_items[count - 1][0])
                break
        raise RuntimeError(
            f"assembly STEP export failed; individual failures={failed}; "
            f"first incremental group failure={first_group_failure}"
        ) from exc
    export_stl(Compound(children=seats), stl_path)
    export_step(Compound(children=harness_keepouts), keep_path)

    reimport = import_step(step_path)
    rb, rradial, _, _ = conservative_metrics(reimport)
    delta = max(abs(rradial - radial), abs(rb.min.Z - bb.min.Z), abs(rb.max.Z - bb.max.Z))
    mesh = import_stl(stl_path)
    if delta > 0.001 or len(mesh.faces()) <= 0:
        raise RuntimeError("export re-import validation failed")

    lines = [
        "HSX Stage-50 corrected final-direction CAD — NOT FOR FABRICATION",
        f"hard envelope: radius<={ENV_R:.3f} mm height<={ENV_H:.3f} mm",
        f"physical bbox=({bb.min.X:.3f},{bb.max.X:.3f})x({bb.min.Y:.3f},{bb.max.Y:.3f}) z=({bb.min.Z:.3f},{bb.max.Z:.3f}) mm",
        f"physical conservative radial={radial:.3f} mm margin={radial_margin:.3f} mm height_margin={height_margin:.3f} mm",
        f"with 3x {HARNESS_CORRIDOR:.2f}x{HARNESS_CORRIDOR:.2f} mm harness keepouts: radial={kradial:.3f} margin={kradial_margin:.3f} mm zmax={kb.max.Z:.3f} mm",
        f"two-pair cable arithmetic: 2*(1.50+0.15)=3.30 mm; corridor total allowance={HARNESS_CORRIDOR-3.30:.2f} mm",
        f"connected cage solid count={len(cage.solids())}; cage volume={cage.volume:.3f} mm3",
        f"six nut-to-cage reaction contact distances={[round(x, 6) for x in nut_distances]} mm",
        f"unintended physical overlap={max_overlap:.6f} mm3 ({overlap_pair})",
        f"feedthrough keepout: post_min_radius={min_post_radius:.3f} mm vs {FT_KEEP_R:.3f}; bridge_z={BRIDGE_Z:.3f} vs {FT_KEEP_H:.3f}; pass={keepout_ok}",
        f"STEP reimport bound delta={delta:.6f} mm; ceramic STL faces={len(mesh.faces())}",
        "ceramic geometry count=1 unique repeated seat geometry; quantity=3; tapped/internal ceramic thread count=0",
        "architectural corrections: connected base/backframe/reaction cage; six open-sided replaceable vented nut-plate envelopes; external keeper envelopes; 3.80-mm cable corridors",
        "release holds: exact keeper retention, flexure geometry/force, Ti hardware/finish/galling, zirconia DFM/GD&T, delivered cable/lay/bend, feedthrough datum and all hot-vacuum qualification",
    ]
    report = "\n".join(lines) + "\n"
    (OUT / "50_CAD_KERNEL_REPORT.txt").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
