// concept_B.scad — CONCEPT B "SpringClamp Cube"  (RECOMMENDED)
// -----------------------------------------------------------------------------
// Monolithic yttria-stabilized ZIRCONIA cube (15 mm) + integral base flange.
// Per carrier face (+X, +Y, +Z):
//   - drop-in pocket 9.4 sq x 2.15 deep (NO sliding -- carrier placed face-up)
//   - PEEK contact insert 9.3 sq x 1.0 carrying 4 gold-plated BeCu leaf springs
//     at the LCC mid-side pad positions (pads 1/6/11/16 per ST7)
//   - Ti grade-2 picture-frame clamp 13.4 sq x 1.0, window 7.0 sq (clears the
//     open cavity + bond wires), bearing on the carrier's outer/seal-ring rim
//   - 2x Ti M1.6 through-bolts to hex nuts on the opposite (bare) face; frame
//     lands METAL-ON-CERAMIC FLUSH -> preload set by spring geometry (0.35 mm
//     deflection), NOT by screw torque -> cannot crush the carrier
// Wire grooves (2.0 x 1.5) green-machined into the faces route each face's 4
// conductors to the bottom center hole -> down between the two Sub-C towers.
// Render: openscad -o concept_B_iso.png --imgsize=1400,1050 --projection=p \
//         --camera=0,0,0,55,0,25,0 --viewall --autocenter concept_B.scad
// Section: add -D SECTION=1
// -----------------------------------------------------------------------------

SECTION = 0;                 // 1 = cut away y>0 half for section view

// ---- envelope (hard constraints) ----
ENV_D = 31.75;               // cylinder diameter [mm]
ENV_H = 27.5;                // cylinder height   [mm] (from flange face z=0)
show_envelope = true;

// ---- LCC02046 carrier ----
LCC    = 8.89;               // body square [mm] (+0.254/-0.127 tol)
LCC_T  = 1.65;               // thickness [mm]
SEAL_OD= 7.98;               // seal-ring band OD (frame bears outside cavity)
CAV_OP = 6.10;               // cavity opening (keep-out: die + bond wires)

// ---- structure ----
CUBE     = 15.0;             // zirconia cube edge
POCKET   = 9.40;             // pocket square (LCC max 9.14 + 0.26 as-sintered margin)
POCK_D   = 2.15;             // total pocket depth = PEEK 1.0 + carrier seat 1.15
PEEK_T   = 1.0;              // contact-insert thickness
PROUD    = LCC_T - (POCK_D - PEEK_T);   // carrier proud of face = 0.50 mm
DEFLECT  = 0.35;             // spring working deflection (sets preload)
FRAME    = 13.4;             // Ti clamp frame square
FRAME_T  = 1.0;
WIN      = 7.0;              // frame window (<= SEAL_OD; > CAV_OP + margin)
STAND_H  = 6.5;              // Ti standoff height (ADJUSTABLE - Sub-C tower
                             // protrusion UNVERIFIED; spacer washers trim this)
BASE_T   = 2.0;              // integral zirconia base flange thickness
BASE_D   = 18.0;
EAR_Y    = 12.5;             // heritage 1D-mount standoff pattern (measured)
GROOVE_W = 2.0; GROOVE_D = 1.5;
Z0 = STAND_H + BASE_T;       // cube bottom face
ZC = Z0 + CUBE/2;            // cube center height

// screw line offsets per face — all magnitudes distinct so no two through-
// bolts intersect inside the cube (see doc §B)
SX = [[ 5.05,-5.05],[-5.05, 5.05]];   // +X face (u,v = y,z_local)
SY = [[ 5.15, 4.90],[-5.15,-4.90]];   // +Y face
SZ = [[ 4.95,-5.20],[-4.95, 5.20]];   // +Z face

// ---- envelope-fit echoes ----
r_frame_corner = sqrt(pow(CUBE/2+FRAME_T+1.3,2)+pow(FRAME/2,2));
echo(str("corner radius, side frame + screw head = ", r_frame_corner,
         " mm  (must be <= ", ENV_D/2, ")"));
echo(str("ear radius = ", EAR_Y+2.5, " mm (<= ", ENV_D/2, ")"));
echo(str("stack height = ", Z0+CUBE+FRAME_T+1.3, " mm (<= ", ENV_H, ")"));
echo(str("carrier proud of face = ", PROUD, " mm; spring deflection = ", DEFLECT));

$fn = 48;

module envelope() { color([0.8,0.1,0.1,0.10]) cylinder(h=ENV_H, d=ENV_D); }

// ---------- per-face features, local coords: face plane at z=CUBE/2, +z out --
module face_cuts(scr) {                       // subtracted from the cube
  // pocket
  translate([0,0,CUBE/2-POCK_D/2+0.01]) cube([POCKET,POCKET,POCK_D+0.02],center=true);
  // wire groove: from pocket -v edge to face edge (runs "down" local -y)
  translate([0,-(POCKET/2+(CUBE/2-POCKET/2)/2),CUBE/2-GROOVE_D/2+0.01])
    cube([GROOVE_W, CUBE/2-POCKET/2+0.05, GROOVE_D+0.02], center=true);
  // through-holes for the 2 frame bolts
  for (p = scr) translate([p[0],p[1],0]) cylinder(h=CUBE+6, d=1.8, center=true);
}

module peek_insert() color([0.82,0.71,0.55]) // PEEK, 4 BeCu contact bumps gold
  translate([0,0,CUBE/2-POCK_D]) {
    linear_extrude(PEEK_T) difference() {
      square(POCKET-0.1, center=true);
      square(3.0, center=true);              // wire-tail exit window
    }
    // 4 gold leaf-spring crowns at LCC mid-side pad positions
    for (a=[0:90:270]) rotate([0,0,a]) translate([3.55,0,PEEK_T])
      color([1.0,0.84,0.2]) scale([1.4,2.2,1]) sphere(d=0.9);
  }

module carrier() color([1,0.95,0.72]) {       // LCC02046, cavity up, compressed
  translate([0,0,CUBE/2-POCK_D+PEEK_T+DEFLECT]) difference() {
    linear_extrude(LCC_T) square(LCC, center=true);
    translate([0,0,LCC_T-0.75]) linear_extrude(1) square(CAV_OP, center=true);
    translate([0,0,LCC_T-1.15]) linear_extrude(1) square(4.06, center=true);
  }
  // die
  translate([0,0,CUBE/2-POCK_D+PEEK_T+DEFLECT+0.6]) color([0.25,0.28,0.32])
    linear_extrude(0.35) square(2.5, center=true);
}

module frame(scr, nut_drop=0) {                           // Ti clamp frame + button screws
  zf = CUBE/2;                                // lands flush on the ceramic face
  color([0.62,0.65,0.68]) translate([0,0,zf]) linear_extrude(FRAME_T) difference() {
    square(FRAME, center=true);
    square(WIN, center=true);
    for (p = scr) translate(p) circle(d=1.8);
  }
  // window inner relief chamfer pressing the carrier rim (visual: thin land)
  color([0.62,0.65,0.68]) translate([0,0,zf-PROUD+DEFLECT])
    linear_extrude(PROUD-DEFLECT+0.01) difference() {
      square(WIN+1.4, center=true); square(WIN, center=true); }
  for (p = scr) {
    color([0.55,0.58,0.62]) translate([p[0],p[1],zf+FRAME_T])
      cylinder(h=1.2, d=3.0);                                    // head
    color([0.55,0.58,0.62]) translate([p[0],p[1],-zf-1.3-nut_drop])
      cylinder(h=1.3, d=3.4, $fn=6);                             // hex nut
  }
}

module face_pack(scr, nut_drop=0) { peek_insert(); carrier(); frame(scr, nut_drop); }

// rotations mapping local +Z to +X / +Y / +Z
module on_px() { translate([0,0,ZC]) rotate([0, 90,0]) children(); }
module on_py() { translate([0,0,ZC]) rotate([-90,0,0]) children(); }
module on_pz() { translate([0,0,ZC])                    children(); }

module zirconia_body() color([0.93,0.92,0.86]) difference() {
  union() {
    translate([0,0,ZC]) cube(CUBE, center=true);
    translate([0,0,STAND_H]) cylinder(h=BASE_T, d=BASE_D);
    for (s=[1,-1]) translate([0,0,STAND_H])                  // ear tabs
      linear_extrude(BASE_T) hull() {
        translate([0, s*EAR_Y]) circle(d=5); translate([0, s*7]) circle(d=5); }
  }
  on_px() face_cuts(SX);
  on_py() face_cuts(SY);
  on_pz() face_cuts(SZ);
  // bottom-face wire grooves to center + center pass-through
  translate([0,0,STAND_H-0.01]) cylinder(h=BASE_T+GROOVE_D, d=5.0);
  for (a=[0,90,180,270]) rotate([0,0,a]) translate([CUBE/4,0,Z0-0.01])
    cube([CUBE/2+2, GROOVE_W, GROOVE_D*2], center=true);
  // vertical wire runs down the bare -X and -Y faces (top-face + side wires)
  translate([-CUBE/2+GROOVE_D/2-0.01,0,ZC]) cube([GROOVE_D,GROOVE_W,CUBE+0.1],center=true);
  translate([0,-CUBE/2+GROOVE_D/2-0.01,ZC]) cube([GROOVE_W,GROOVE_D,CUBE+0.1],center=true);
  // ear holes for M2 standoff screws
  for (s=[1,-1]) translate([0,s*EAR_Y,STAND_H-1]) cylinder(h=BASE_T+2, d=2.2);
}

module standoffs() color([0.55,0.58,0.62]) for (s=[1,-1])
  translate([0,s*EAR_Y,0]) { cylinder(h=STAND_H, d=4.8, $fn=6);
    translate([0,0,STAND_H]) cylinder(h=BASE_T+1.0, d=2.0); } // M2 Ti screw

module assembly() {
  standoffs();
  zirconia_body();
  on_px() face_pack(SX);
  on_py() face_pack(SY);
  on_pz() face_pack(SZ, BASE_T);
}

difference() {
  union() { assembly(); if (show_envelope && SECTION==0) envelope(); }
  if (SECTION) translate([-50,-100,-10]) cube([100,100,60]);   // cut y<0
}
