// concept_cube_slots.scad
// -----------------------------------------------------------------------------
// STARTER TEMPLATE for ST8 (3D packaging). Encodes the USER'S idea — a cube with
// a slot on each face to hold an LCC02046 carrier, no glue — as parametric
// "Concept A". The ST8 run should (a) refine this, (b) author 2-3 genuinely
// different concepts as sibling .scad files, and (c) render + export each.
//
// This is a starting geometry, NOT the final design. It has NOT been fit-checked
// against real bond-wire/harness clearances — that's ST8's job.
//
// Render PNG:   openscad -o conceptA.png --imgsize=1400,1000 --camera=0,0,0,55,0,25,140 --render concept_cube_slots.scad
// Export STL:   openscad -o conceptA.stl --render concept_cube_slots.scad
// (CAD kernel / STEP export path for the run: see build123d_concept.py + README.md)
// -----------------------------------------------------------------------------

// ---- envelope (hard constraints) ----
ENV_D   = 31.75;   // cylinder diameter [mm] = 1.25 in
ENV_H   = 27.5;    // cylinder height  [mm] = 2.75 cm
show_envelope = true;

// ---- carrier (LCC02046) ----
LCC     = 8.89;    // square edge [mm] = 0.350 in
LCC_T   = 1.65;    // thickness   [mm] = 0.065 in
CLR     = 0.15;    // slot clearance per side [mm] (tune vs ceramic tolerance)

// ---- cube + retention ----
cube_edge = 18.0;  // must satisfy cube_edge*sqrt(2) <= ENV_D  (=> <= 22.45)
lip       = 0.8;   // retention lip that overlaps the carrier edge (no glue)
slot_depth= LCC_T + 0.3;
stand_d   = 8.0;   // stand diameter
stand_h   = 3.0;   // stand height
faces_used = 3;    // 3 = orthogonal 3-axis (recommended); set 6 to show all

// ---- envelope fit echo (the run should assert this) ----
echo(str("cube cross-section corner radius = ", cube_edge*sqrt(2)/2,
         " mm  (must be <= ", ENV_D/2, ")"));
echo(str("stack height = ", stand_h + cube_edge, " mm  (must be <= ", ENV_H, ")"));

module envelope() {
  color([0.75,0.1,0.1,0.12])
    translate([0,0,0]) cylinder(h=ENV_H, d=ENV_D, $fn=96);
}

// a slot pocket + carrier cutout on +Z face of a unit cube centered at origin
module face_slot() {
  // pocket the carrier drops into, with a retention lip framing the top opening
  translate([0,0,cube_edge/2 - slot_depth])
    cube([LCC+2*CLR, LCC+2*CLR, slot_depth+0.1], center=true);
  // top opening slightly smaller than the carrier -> lip retains it (no glue)
  translate([0,0,cube_edge/2 - lip/2])
    cube([LCC+2*CLR-2*lip, LCC+2*CLR-2*lip, lip+0.2], center=true);
}

module cube_with_slots() {
  difference() {
    cube(cube_edge, center=true);
    // +Z, +X, +Y faces for orthogonal 3-axis; extend to 6 if faces_used==6
    face_slot();                                   // +Z
    rotate([0,90,0])  face_slot();                 // +X
    rotate([-90,0,0]) face_slot();                 // +Y
    if (faces_used==6) {
      rotate([0,-90,0]) face_slot();               // -X
      rotate([90,0,0])  face_slot();               // -Y
      rotate([180,0,0]) face_slot();               // -Z
    }
    // TODO(ST8): harness routing channels from each pocket down to the stand,
    // wire-bond clearance relief, keying notch for pin-1 orientation.
  }
}

module assembly() {
  // stand on the flange
  color([0.8,0.85,0.9]) translate([0,0,0]) cylinder(h=stand_h, d=stand_d, $fn=64);
  // cube centered above the stand
  color([0.85,0.9,1.0]) translate([0,0,stand_h + cube_edge/2]) cube_with_slots();
  // one carrier shown seated in the +Z slot (for scale)
  color([1,0.95,0.75])
    translate([0,0,stand_h + cube_edge - LCC_T/2])
      cube([LCC,LCC,LCC_T], center=true);
}

assembly();
if (show_envelope) envelope();
