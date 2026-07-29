// view_user.scad — render the USER'S STEP geometry (converted to STL via
// build123d) against the Ø31.75 x 27.5 mm envelope for the ST8 critique.
// The envelope is placed on the measured flange top face (z = -6.64 mm in his
// model coordinates) and centered on his head-block axis (x=0, y=0).
// Usage: openscad -o user_iso.png -D 'WHICH="assembled"' view_user.scad ...
WHICH = "assembled";   // "assembled" | "disassembled"
FLANGE_TOP = -6.64;    // measured: flange solid spans z -22.64..-6.64
show_envelope = true;

color([0.75,0.78,0.82])
  import(str("user_", WHICH, ".stl"));
if (show_envelope) color([0.8,0.1,0.1,0.12])
  translate([0,0,FLANGE_TOP]) cylinder(h=27.5, d=31.75, $fn=96);
