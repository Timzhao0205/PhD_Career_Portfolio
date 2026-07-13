"""Cost-down HSX three-axis package concept -- NOT FOR FABRICATION.

The selected concept deletes all fixed ceramic seats.  A single flat-cut,
two-bend CP-Ti trihedral bracket supports three existing protected sensor/LCC
cartridges.  Each cartridge retains one identical flat ceramic guard; the
guard travels with the high-value bonded assembly.  One screw and two open
edge hooks retain each face.  Dimensions are finished millimetres.

This kernel model validates envelope, adjacency, tool axes, cable corridors
and discrete-part collisions.  It does not release the flexure, hook, nut-
retaining lance, ceramic edge condition, contact preload or feedthrough datum.
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

BASE_Z = 12.20
SHEET_T = 0.50
BASE_TOP = BASE_Z + SHEET_T
FACE = 13.60
FACE_HALF = FACE / 2
FACE_CZ = BASE_TOP + FACE_HALF - 0.05
FACE_OUT = FACE_HALF + SHEET_T

WINDOW = 6.40
CART = 10.90
CART_T = 2.40
GUARD_T = 0.635
CLAMP = 13.40
CLAMP_T = 0.40
SCREW_R = 0.50
SCREW_CLEAR_R = 0.70
HEAD_R = 1.00
HEAD_T = 0.35
NUT_T = 0.70

POST_XY = 9.00
POST_R = 1.15
POST_HOLE_R = 0.72

HARNESS_CORRIDOR = 3.80
HARNESS_XY = ((-6.30, 3.80), (3.80, -6.30), (-6.30, -3.80))
STRAIN_XY = HARNESS_XY


def axis_plane(axis: str, origin):
    if axis == "X":
        return Plane(origin=origin, x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    if axis == "Y":
        return Plane(origin=origin, x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    return Plane(origin=origin, x_dir=(1, 0, 0), z_dir=(0, 0, 1))


def cylinder_along(axis: str, origin, radius: float, length: float):
    return extrude(axis_plane(axis, origin) * Circle(radius), length)


def face_planes():
    """Local +Z points outward; local X/Y are the cartridge face coordinates."""
    return {
        "X": Plane(origin=(FACE_OUT, 0, FACE_CZ), x_dir=(0, 1, 0), z_dir=(1, 0, 0)),
        "Y": Plane(origin=(0, FACE_OUT, FACE_CZ), x_dir=(1, 0, 0), z_dir=(0, 1, 0)),
        "Z": Plane(origin=(0, 0, BASE_TOP), x_dir=(1, 0, 0), z_dir=(0, 0, 1)),
    }


def make_folded_bracket():
    """One conceptual laser-cut blank after two 90-deg face bends."""
    bracket = Box(
        FACE,
        FACE,
        SHEET_T,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    ).locate(Location((0, 0, BASE_Z)))

    # Diagonal planar arms reach four simple vented standoffs.  Their holes,
    # the face windows, cable notches and hook slots are cut in the flat blank.
    for x in (-POST_XY, POST_XY):
        for y in (-POST_XY, POST_XY):
            angle = 45 if x * y > 0 else -45
            bracket += Box(4.20, 1.20, SHEET_T).locate(
                Location((x * 7.75 / 9.0, y * 7.75 / 9.0, BASE_Z + SHEET_T / 2), (0, 0, angle))
            )

    # The 0.05-mm modeling overlap represents the continuous bend radius; the
    # production neutral axis and bend relief are deliberately not released.
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

    # Open active-area windows.  No pocket, blind feature or ceramic thread.
    bracket -= Box(WINDOW, WINDOW, SHEET_T + 0.60).locate(
        Location((0, 0, BASE_Z + SHEET_T / 2))
    )
    bracket -= Box(SHEET_T + 0.60, WINDOW, WINDOW).locate(
        Location((FACE_HALF + SHEET_T / 2, 0, FACE_CZ))
    )
    bracket -= Box(WINDOW, SHEET_T + 0.60, WINDOW).locate(
        Location((0, FACE_HALF + SHEET_T / 2, FACE_CZ))
    )

    # Open harness notches are wider than the delivered-cable keepout boxes.
    for x, y in HARNESS_XY:
        bracket -= Box(
            HARNESS_CORRIDOR + 0.40,
            HARNESS_CORRIDOR + 0.40,
            SHEET_T + 0.80,
        ).locate(Location((x, y, BASE_Z + SHEET_T / 2)))

    # Vented standoff through-holes.
    for x in (-POST_XY, POST_XY):
        for y in (-POST_XY, POST_XY):
            bracket -= Cylinder(
                POST_HOLE_R,
                SHEET_T + 0.80,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
            ).locate(Location((x, y, BASE_Z - 0.40)))

    # Face screw clearances and two hook slots per clamp.  Slots are open to
    # an outside edge in the production blank; exact keyhole/lead-in detail is
    # a gated drawing item.
    planes = face_planes()
    # X/Y use lower-edge screws and upper-edge hooks so no retention part
    # occupies their shared vertical corner.  The Y plane's local +Y points
    # toward -global-Z, hence the opposite local signs for the same global
    # lower/upper arrangement.
    screw_uv = {"X": (0.00, -5.50), "Y": (0.00, 5.50), "Z": (0.00, -5.50)}
    hook_uv = {
        "X": ((-2.30, 5.80), (2.30, 5.80)),
        "Y": ((-2.30, -5.80), (2.30, -5.80)),
        "Z": ((-2.30, 5.80), (2.30, 5.80)),
    }
    for axis, pl in planes.items():
        u, v = screw_uv[axis]
        bracket -= extrude(
            pl.offset(-0.90) * Circle(SCREW_CLEAR_R).locate(Location((u, v))),
            1.80,
        )
        for hu, hv in hook_uv[axis]:
            bracket -= extrude(
                pl.offset(-0.90) * Rectangle(0.95, 0.90).locate(Location((hu, hv))),
                1.80,
            )

    return bracket, screw_uv, hook_uv


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


def make_guard(pl: Plane):
    guard = extrude(pl * Rectangle(CART, CART), GUARD_T)
    guard -= extrude(pl.offset(-0.10) * Rectangle(WINDOW, WINDOW), GUARD_T + 0.20)
    # One open fanout/pigtail notch; chamfer/orientation remains controlled by
    # the cartridge traveler rather than this symmetric structural bracket.
    guard -= extrude(
        pl.offset(-0.10) * Rectangle(1.60, 2.20).locate(Location((-CART / 2 + 0.70, 0))),
        GUARD_T + 0.20,
    )
    return guard


def make_face_parts(axis: str, pl: Plane, screw_uv, hook_uv):
    # Protected cartridge is a Stage-10 envelope.  The separate thin guard is
    # exported for flat-substrate DFM; it is included inside this envelope,
    # not counted twice in the physical collision assembly.
    cartridge = extrude(pl * Rectangle(CART, CART), CART_T)
    cartridge -= extrude(pl.offset(-0.10) * Rectangle(WINDOW, WINDOW), CART_T + 0.20)
    cartridge -= extrude(
        pl.offset(-0.10) * Rectangle(1.80, 2.20).locate(Location((-CART / 2 + 0.80, 0))),
        CART_T + 0.20,
    )
    u, v = screw_uv
    cartridge -= extrude(
        pl.offset(-0.10) * Circle(SCREW_CLEAR_R).locate(Location((u, v))),
        CART_T + 0.20,
    )

    clamp = extrude(pl.offset(CART_T) * Rectangle(CLAMP, CLAMP), CLAMP_T)
    clamp -= extrude(
        pl.offset(CART_T - 0.10) * Rectangle(WINDOW + 0.80, WINDOW + 0.80),
        CLAMP_T + 0.20,
    )

    clamp -= extrude(
        pl.offset(CART_T - 0.20) * Circle(SCREW_CLEAR_R).locate(Location((u, v))),
        CLAMP_T + 0.40,
    )

    # Two T-hooks are integral with the flat clamp.  The rear lip is behind
    # the face and the narrow stem passes through the open slot.
    for hu, hv in hook_uv:
        stem = extrude(
            pl.offset(-0.70) * Rectangle(0.70, 0.60).locate(Location((hu, hv))),
            CART_T + CLAMP_T + 0.70,
        )
        lip = extrude(
            pl.offset(-0.90) * Rectangle(1.30, 0.60).locate(Location((hu, hv))),
            0.20,
        )
        clamp += stem + lip

    nut = extrude(
        pl.offset(-0.50 - NUT_T) * Rectangle(1.80, 1.80).locate(Location((u, v))),
        NUT_T,
    )
    nut -= extrude(
        pl.offset(-0.60 - NUT_T) * Circle(0.60).locate(Location((u, v))),
        NUT_T + 0.20,
    )

    shaft = extrude(
        pl.offset(-0.50 - NUT_T) * Circle(SCREW_R).locate(Location((u, v))),
        CART_T + CLAMP_T + NUT_T + 0.50,
    )
    head = extrude(
        pl.offset(CART_T + CLAMP_T) * Circle(HEAD_R).locate(Location((u, v))),
        HEAD_T,
    )
    bolt = shaft + head

    # The thin guard occupies the front layer inside the Stage-10 cartridge.
    guard = make_guard(pl.offset(CART_T - GUARD_T))
    return cartridge, guard, clamp, nut, bolt


def conservative_metrics(shape):
    bb = shape.bounding_box()
    x = max(abs(bb.min.X), abs(bb.max.X))
    y = max(abs(bb.min.Y), abs(bb.max.Y))
    radial = hypot(x, y)
    return bb, radial, ENV_R - radial, ENV_H - bb.max.Z


def collision_report(items):
    maximum, pair = 0.0, "none"
    positive = []
    for i, (na, sa) in enumerate(items):
        for nb, sb in items[i + 1 :]:
            vol = (sa & sb).volume
            if vol > 1e-6:
                positive.append((na, nb, vol))
            if vol > maximum:
                maximum, pair = vol, f"{na}<->{nb}"
    return maximum, pair, positive


def main():
    bracket, screw_uv, hook_uv = make_folded_bracket()
    if len(bracket.solids()) != 1:
        raise RuntimeError(f"folded bracket has {len(bracket.solids())} solids, expected one")

    posts = [make_post(x, y) for x in (-POST_XY, POST_XY) for y in (-POST_XY, POST_XY)]
    cartridges, guards, clamps, nuts, bolts = [], [], [], [], []
    for axis, pl in face_planes().items():
        cart, guard, clamp, nut, bolt = make_face_parts(axis, pl, screw_uv[axis], hook_uv[axis])
        cartridges.append(cart)
        guards.append(guard)
        clamps.append(clamp)
        nuts.append(nut)
        bolts.append(bolt)

    strain_clips = []
    for i, (x, y) in enumerate(STRAIN_XY):
        if i == 1:
            clip = Box(3.80, 1.00, 0.40).locate(Location((x, y, BASE_TOP + 0.20)))
        else:
            clip = Box(1.00, 3.80, 0.40).locate(Location((x, y, BASE_TOP + 0.20)))
        strain_clips.append(clip)

    physical_items = (
        [("folded_bracket", bracket)]
        + [(f"post_{i+1}", s) for i, s in enumerate(posts)]
        + [(f"cartridge_{i+1}", s) for i, s in enumerate(cartridges)]
        + [(f"clamp_{i+1}", s) for i, s in enumerate(clamps)]
        + [(f"nut_{i+1}", s) for i, s in enumerate(nuts)]
        + [(f"bolt_{i+1}", s) for i, s in enumerate(bolts)]
        + [(f"strain_clip_{i+1}", s) for i, s in enumerate(strain_clips)]
    )

    invalid = [name for name, shape in physical_items if not shape.is_valid]
    if invalid:
        raise RuntimeError(f"invalid shapes: {invalid}")

    # Export the untouched assembly before pairwise Boolean diagnostics.  Some
    # OCCT builds retain Boolean-operation history on shared shapes, which can
    # make a later STEP writer call fail even though all solids remain valid.
    # The subsequent checks still fail the run if any overlap or gate fails.
    step_path = OUT / "30D_NFF.step"
    assembly_stl_path = OUT / "30D_NFF.stl"
    guard_path = OUT / "30D_GUARD_NFF.stl"
    bracket_path = OUT / "30D_BRACKET_NFF.step"
    keep_path = OUT / "30D_KEEP_NFF.step"
    temp_step = OUT / "a.step"
    temp_assembly_stl = OUT / "a.stl"
    temp_guard = OUT / "g.stl"
    temp_bracket = OUT / "b.step"
    temp_keep = OUT / "k.step"
    for path in (
        step_path,
        assembly_stl_path,
        guard_path,
        bracket_path,
        keep_path,
        temp_step,
        temp_assembly_stl,
        temp_guard,
        temp_bracket,
        temp_keep,
    ):
        if path.exists():
            path.unlink()
    # The OCCT writer in this Windows runtime fails on some deeper output
    # names, so it writes short temporary names and then performs a filesystem
    # rename.  Geometry and re-import validation use the final names.
    export_step(bracket, temp_bracket)
    temp_bracket.replace(bracket_path)
    export_stl(Compound(children=guards), temp_guard)
    temp_guard.replace(guard_path)
    assembly = Compound(children=[shape for _, shape in physical_items])
    export_stl(assembly, temp_assembly_stl)
    temp_assembly_stl.replace(assembly_stl_path)
    export_step(assembly, temp_step)
    temp_step.replace(step_path)

    maximum, pair, positive = collision_report(physical_items)
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
    keepout_assembly = Compound(children=harness_keepouts)
    export_step(keepout_assembly, temp_keep)
    temp_keep.replace(keep_path)

    bb, radial, radial_margin, height_margin = conservative_metrics(assembly)
    kb, kradial, kradial_margin, _ = conservative_metrics(
        Compound(children=[assembly, keepout_assembly])
    )
    if radial > ENV_R or bb.min.Z < -1e-6 or bb.max.Z > ENV_H:
        raise RuntimeError("physical assembly violates hard envelope")
    if kradial > ENV_R or kb.max.Z > ENV_H:
        raise RuntimeError("assembly plus harness keepouts violates hard envelope")

    min_post_radius = hypot(POST_XY, POST_XY) - POST_R
    lowest_central_hardware = BASE_Z - 0.50 - NUT_T
    keepout_ok = min_post_radius > FT_KEEP_R and lowest_central_hardware > FT_KEEP_H
    if not keepout_ok:
        raise RuntimeError("feedthrough keepout violated")

    # Nut plates and simple standoffs must contact their reaction surfaces.
    nut_distances = [n.distance_to(bracket) for n in nuts]
    post_distances = [p.distance_to(bracket) for p in posts]
    if max(nut_distances + post_distances) > 1e-5:
        raise RuntimeError(
            f"reaction contact open: nuts={nut_distances}, posts={post_distances}"
        )

    # Cable paths must clear the folded structural bracket; the strain clips
    # deliberately bridge the paths and are excluded from this clearance test.
    cable_frame_overlap = max((k & bracket).volume for k in harness_keepouts)
    if cable_frame_overlap > 1e-6:
        raise RuntimeError(f"harness corridor intersects bracket by {cable_frame_overlap:.6f} mm3")

    reimport = import_step(step_path)
    rb, rradial, _, _ = conservative_metrics(reimport)
    delta = max(abs(rradial - radial), abs(rb.min.Z - bb.min.Z), abs(rb.max.Z - bb.max.Z))
    guard_mesh = import_stl(guard_path)
    assembly_mesh = import_stl(assembly_stl_path)
    if delta > 0.001 or len(guard_mesh.faces()) <= 0 or len(assembly_mesh.faces()) <= 0:
        raise RuntimeError("export/re-import validation failed")

    # First-order CTE arithmetic only; not a preload qualification.
    lateral_delta = (9.5 - 7.2) * 1e-6 * CART * 230
    normal_delta = (9.5 - 7.2) * 1e-6 * CART_T * 230
    face_parts_old = 3 + 6 + 6 + 6
    face_parts_new = 3 + 3 + 3
    support_frame_volume = bracket.volume + sum(p.volume for p in posts)
    prior_cage_volume = 440.917
    volume_reduction = 1 - support_frame_volume / prior_cage_volume

    lines = [
        "HSX Stage-30 cost-down flat-package CAD -- NOT FOR FABRICATION",
        f"hard envelope: radius<={ENV_R:.3f} mm height<={ENV_H:.3f} mm",
        f"physical bbox=({bb.min.X:.3f},{bb.max.X:.3f})x({bb.min.Y:.3f},{bb.max.Y:.3f}) z=({bb.min.Z:.3f},{bb.max.Z:.3f}) mm",
        f"physical conservative radial={radial:.3f} mm margin={radial_margin:.3f} mm height_margin={height_margin:.3f} mm",
        f"assembly plus 3x {HARNESS_CORRIDOR:.2f}-mm square cable keepouts: radial={kradial:.3f} mm margin={kradial_margin:.3f} mm zmax={kb.max.Z:.3f} mm",
        f"folded bracket solid count={len(bracket.solids())}; bracket volume={bracket.volume:.3f} mm3; intended main bends=2",
        f"folded bracket plus four vented posts volume={support_frame_volume:.3f} mm3 vs prior connected cage={prior_cage_volume:.3f} mm3; geometric reduction={100*volume_reduction:.1f} percent (not a price estimate)",
        f"unintended physical overlap={maximum:.6f} mm3 ({pair}); physical solid envelopes={len(physical_items)}",
        f"nut-to-bracket distances={[round(x, 6) for x in nut_distances]} mm; post-to-bracket distances={[round(x, 6) for x in post_distances]} mm",
        f"feedthrough keepout: post_min_radius={min_post_radius:.3f} vs {FT_KEEP_R:.3f} mm; lowest central hardware={lowest_central_hardware:.3f} vs {FT_KEEP_H:.3f} mm; pass={keepout_ok}",
        f"cable-to-folded-bracket maximum overlap={cable_frame_overlap:.6f} mm3",
        f"STEP reimport bound delta={delta:.6f} mm; assembly STL faces={len(assembly_mesh.faces())}; guard STL faces={len(guard_mesh.faces())}",
        "structural ceramic count=0; custom flat ceramic guard geometry count=1; guard quantity=3; tapped/internal ceramic threads=0",
        "flat guard nominal=10.90 x 10.90 x 0.635 mm with 6.40-mm window and one open tongue notch; material/process HOLD",
        f"face-retention discrete parts old={face_parts_old} vs cost-down={face_parts_new}; reduction={face_parts_old-face_parts_new} parts (straps+screws+nuts/keepers basis)",
        f"first-order Ti-minus-alumina expansion 20-to-250C: lateral over 10.90 mm={lateral_delta:.6f} mm; normal over 2.40 mm={normal_delta:.6f} mm; force not qualified",
        "release holds: flat-guard material/UHV lot and laser edge quality; formed-bracket bend relief/GD&T; hook/slot strength and insertion; one-screw clamp preload/FEA/coupon; captive nut lance; cartridge internal stack and loop clearance; exact cable/strain hardware; feedthrough datum; magnetic error budget; full hot-UHV qualification",
    ]
    report = "\n".join(lines) + "\n"
    (OUT / "30D_CAD_KERNEL_REPORT.txt").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
