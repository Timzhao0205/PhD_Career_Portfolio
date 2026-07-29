# Stage 20 - three-board readout, control, grounding, and feedthrough architecture

Date: 2026-07-12  
Boundary: all three Hall die/LCC cartridges, their protected pigtails, and the vacuum harness are
inside the 250 deg C UHV vessel. All readout boards, controller, current sources, interface
junction, acquisition, and ordinary connectors are ambient.

## 1. Outcome first

Use **three identical independent `hsx_2026_v2` analog boards adjacent to one ambient interface
junction**, one board per X/Y/Z sensor. Use one Pico 2 only as the shared phase-state and sync
generator. Fan its a0/a1/a2/EN lines through three independent quad-buffer branches on the
interface junction, one branch per board. Each analog board retains its own RS6 isolated supply
and its own independently floating 100-uA bias source. Acquire the three J4 analog outputs in
parallel on three genuinely simultaneous channels; use the fourth acquisition channel for Pico
sync.

No analog board receives data and transfers it to either of the other boards. The boards have no
digital data path and no architectural reason to become a chain. Shared items are controller,
state timing, ambient 24-V source upstream of per-board protection, DAQ timebase, and a deliberate
ambient ground/chassis star. Independent items are the three sensor four-wire nets, six twisted
pairs, three bias sources/loops, three analog chains, three isolated DC/DC output domains up to the
intentional star, three buffer output branches, calibration records, faults, and removable
cartridges.

The 19C-275 map uses all 12 sensor conductors and reserves pins 13-19. No sensor return or shield
uses a signal pin. Six pair screens terminate at the CF flange/chassis and float at the cartridge
and board ends. The map is complete in `outputs/20_PIN_AND_CABLE_MAP.csv`, including the
male-to-male feedthrough mirror.

## 2. Architecture comparison

| Option | Description | Benefits | Problems | Disposition |
|---|---|---|---|---|
| Three boards directly cabled | Pico wires and six sensor pairs go directly to three nearby boards; scope captures outputs. | Fewest parts and lowest initial cost. | Uncontrolled fanout stubs, inconsistent ground returns, weak labeling/test access, one GPIO fault can disturb all boards, and the 19C mirror is easy to wire incorrectly. | Functional prototype only after bench fanout test; not the installation baseline. |
| Interface junction plus three boards | A passive/active star panel maps the 19C circuits, bonds screens, provides test points/keyed branch cables, per-board 24-V protection, three quad buffers, AGND star, three analog returns, and sync breakout. | Lowest wiring/short risk, explicit mirror control, individual branch isolation, reproducible test points, simple board replacement, no readout-board redesign. | One small ambient junction assembly to build and document. | **Recommended cost/reliability baseline.** |
| One board as master/data relay | One analog board receives or digitizes all data and relays to the other two. | None for the existing hardware. | Boards have analog outputs, not a data network; creates a single point of failure and asymmetric timing/grounding. | **Reject.** Pico and DAQ are the only shared control/data endpoints. |
| Local ambient simultaneous digitizer | Put a 3- or 4-channel simultaneous ADC at the interface panel and send digital data onward. | Deterministic capture, smaller analog cable loop, easier long-distance transport. | New ADC/front-end/clock/firmware/calibration design; unnecessary while the four-channel scope is available. | Credible upgrade if long analog runs or automated campaigns justify it. |
| In-vessel digitization | Place ADC/control near the dies. | Short analog wires. | Violates locked hot-UHV boundary, adds electronics/material/thermal qualification, compromises reuse and cost. | **Reject.** |

## 3. Complete 12-conductor feedthrough allocation

### 3.1 Naming and mirror convention

`V1..V19` are feedthrough conductor IDs defined by the **vacuum-side mating pattern**. The 19C
feedthrough is male-to-male and straight-through. Accu-Glass warns that pin position reverses from
vacuum side to air side, and its 110240 female-connector rear-view drawing says the numbers are not
printed on the part. Therefore the air connector cavities in the table are the horizontal mirror
of the vacuum reference and must be proven by first-article continuity before any contact is
locked into a connector.

Mirror pairs used here are `1->1`, `2->12`, `3->11`, `4->10`, `5->9`, `6->8`, `7->7`,
`8->6`, `9->5`, `10->4`, `11->3`, `12->2`; spare mappings continue
`13->14`, `14->13`, `15->18`, `16->17`, `17->16`, `18->15`, `19->19`.
This mapping is taken from the official connector pattern but is still verified electrically
because cavity numbers are not molded/printed.

### 3.2 Signal assignment

| Vacuum ref | Air cavity | Axis | Terminal | Pair | Board endpoint |
|---:|---:|---|---|---|---|
| V1 | A1 | X | p1 | XA | Board X J1.1 |
| V2 | A12 | X | p3 | XA | Board X J1.2 |
| V3 | A11 | X | p2 | XB | Board X J1.6 |
| V4 | A10 | X | p4 | XB | Board X J1.7 |
| V5 | A9 | Y | p1 | YA | Board Y J1.1 |
| V6 | A8 | Y | p3 | YA | Board Y J1.2 |
| V7 | A7 | Y | p2 | YB | Board Y J1.6 |
| V8 | A6 | Y | p4 | YB | Board Y J1.7 |
| V9 | A5 | Z | p1 | ZA | Board Z J1.1 |
| V10 | A4 | Z | p3 | ZA | Board Z J1.2 |
| V11 | A3 | Z | p2 | ZB | Board Z J1.6 |
| V12 | A2 | Z | p4 | ZB | Board Z J1.7 |
| V13-V19 | mirrored A14/A13/A18/A17/A16/A15/A19 | spare | none | none | capped, labeled, individually accessible |

Each cartridge's physical q/lane mapping is translated to p1-p4 only by the signed stage-10
traveler. The feedthrough and board maps never use q1-q4, pad 8/3/19/14, or color as a substitute
for p-identity.

### 3.3 Pairing and screens

- Pair A on every axis is p1/p3 and lands on board J1.1/J1.2.
- Pair B on every axis is p2/p4 and lands on board J1.6/J1.7.
- Roles alternate during spinning; durable pair labels are XA/XB/YA/YB/ZA/ZB, not “bias” and
  “sense.”
- The six in-vessel cable screens stop before the cartridge guard and bond mechanically/electrically
  to the CF flange at the feedthrough. Air-side pair screens also bond to the same flange/chassis
  region and float at J1. No screen uses V13-V19.
- J1 shell-to-GND1 is still unverified. Until the physical board/connector check closes G00-10,
  do not use the J1 shell as a screen termination.
- Keep each pair twisted to the closest practical point at the 19C contact field; document the
  necessary local untwist. Sequential pin numbering was chosen to minimize labeling errors;
  connector-field untwist is accepted only after injected-noise testing.

## 4. Independent bias and analog paths

Each board receives one external **floating 100-uA current source** at its own J2/J7 loop. The
three current-source outputs have no shared positive lead, return, sense lead, compliance return,
or chassis bond. A multi-channel source is acceptable only if the manufacturer explicitly states
channel-to-channel galvanic isolation at the required compliance and the bench verifies it. Three
nominal channels in one grounded instrument are not automatically independent.

The source currents enter the corresponding board's chopper/bias mux and reach the four-terminal
sensor through that board's four unique 19C circuits. No extra feedthrough bias-return conductor is
needed; the loop closes through the selected Hall-plate diagonal and its same board. Current-source
compliance is set only high enough for the sensor, muxes, R9/R10, wiring and verified margin;
per-axis current limiting/fault logging is required.

The three analog paths are:

`sensor X -> Board X U1/U2/U3/U4 -> Board X J4`, and identically for Y and Z.

No analog signal crosses from one board to another. A board failure cannot be “worked around” by
sharing a sensor terminal or current source. The stage-00 approximately 109x amplitude anomaly
must be resolved on one board, then regression-tested on all three before absolute calibration.

## 5. Control fanout: exact live-net loads

The live netlist, not the historical generic estimate, gives:

| Shared net | J3 pin | Loads per board | Silicon C per board | Three-board silicon C |
|---|---:|---|---:|---:|
| a0 | 3 | U1 A0 + U2 A0 | `2 * 2 pF = 4 pF typ` | `12 pF typ` |
| a1 | 2 | U1 A1 + U2 A1 | `2 * 2 pF = 4 pF typ` | `12 pF typ` |
| a2 | 1 | U3 IN1 + U3 IN2 | `2 * 3 pF = 6 pF typ` | `18 pF typ` |
| EN | 4 | U1 EN + U2 EN | `2 * 2 pF = 4 pF typ` | `12 pF typ` |

ADG1209 and ADG5236 require `V_INH >= 2.0 V`; Pico 3.3-V logic is compatible. R5-R8 are physical
pulldowns, but their values are absent from the netlist/BOM. Measure all twelve populated
resistors and include their parallel DC load before releasing direct fanout.

### Recommended buffered star

Use three `SN74LVC125A` quad buffers at 3.3 V on the junction, one package per board. Each package
receives the four Pico lines and drives only its board branch. TI lists 5-pF typical buffer input
capacitance, so each Pico net sees `3 * 5 pF = 15 pF typ` plus local trace, instead of the remote
star. TI specifies 3.3-V propagation delay in the few-nanosecond range and adequate 3.3-V drive.
Separate packages prevent one shorted branch output from directly loading the other two outputs.
Give each branch an independent output series-resistor footprint and test point; default
population `33 ohm` is `ENGINEERING PROPOSAL - VALIDATE`, with a 22-68-ohm tuning range based on
measured cable impedance/ringing. Tie each active-low OE into a safe hardware scheme so outputs
are disabled during junction power-up; the boards' EN pulldowns must keep muxes disabled when the
controller/junction is absent.

### Direct-bypass and buffer thresholds

The junction may include a documented buffer-bypass option for bench comparison, but bypass is
released only if all of these `ENGINEERING PROPOSAL - VALIDATE` criteria pass on the final cable:

- every R5-R8 value is recorded and total high-state current leaves verified GPIO drive margin;
- farthest-board steady levels are at least 2.4 V high and at most 0.4 V low (project margins around
  sourced 2.0/0.8-V device thresholds);
- no ringing or slow edge recrosses either input threshold;
- inter-board threshold-crossing skew is at most 100 ns and repeatable over power/temperature;
- total measured line capacitance is at most 200 pF and each star branch is at most 0.5 m;
- phase-state settling and raw analog output pass at the highest intended phase rate.

Exceeding any threshold, seeing a cable branch outside the junction bundle, or observing a branch
fault requires the buffered configuration. Even when direct fanout passes, the buffered star is
the installation recommendation because its cost is small relative to the feedthrough/sensors and
it improves branch containment/testability.

For any branch, estimate first-order edge loading as `tau = (R_driver + R_series) *
(C_input + C_cable)`, then verify with a scope; a star/reflection problem cannot be cleared by the
RC calculation alone. Firmware samples only after
`t_blank >= max(line settling, data-sheet switch timing, measured analog settling) + margin`.
The numeric blanking margin is `ENGINEERING PROPOSAL - VALIDATE` from injected-signal tests.

## 6. Phase rate, sync, and simultaneous acquisition

At phase rate `f_phase`, one 8-phase recombination update takes `8/f_phase`:

| f_phase | Phase dwell | Maximum completed 8-phase updates before filtering |
|---:|---:|---:|
| 40 kHz nominal | 25 us | 5 kHz |
| 80 kHz | 12.5 us | 10 kHz |
| 100 kHz stated upper usable | 10 us | 12.5 kHz |
| 160 kHz | 6.25 us | 20 kHz |

This exposes an existing requirement tension: the retained hardware note says 10-100 kHz phase
rate usable and 40 kHz nominal, while the locked system statement says 10-20 kHz after
recombination is sufficient. A 20-kHz completed-cycle rate requires 160-kHz phases before filter
margin, outside the stated usable range. Do not claim 20-kHz recombined bandwidth from the current
40-kHz mode. Architecture and acquisition support the test; achievable sensor bandwidth is
`G20-04 HOLD - VALIDATE` with switching/settling/noise data.

Pico GP19 supplies sync to acquisition channel 4. Firmware makes sync encode either phase zero or
the start of each eight-phase cycle and records the exact convention/version. All three boards
receive the same buffered state in parallel. Acquisition channels 1-3 sample the three J4 outputs
at the same timebase and channel 4 records sync. Trigger on sync, retain raw samples and state
metadata, then demodulate all axes with the same phase boundaries.

The Keysight DSOX1204G is the current lowest-change acquisition path: four analog channels, 8-bit
ADC, up to 2 GSa/s and 2 Mpoints per its live data. Verify the actual installed mode, channel-on
sample-rate/memory sharing, skew, vertical range, probe attenuation, and export configuration.
For an engineering target of at least ten raw samples per phase,
`f_sample_per_channel >= 10*f_phase`; at 160 kHz this is `>=1.6 MS/s/channel`, explicitly an
`ENGINEERING PROPOSAL - VALIDATE` acquisition criterion rather than a manufacturer requirement.

Do not use Pico's three ADC pins as a simultaneous three-axis converter; RP2350 exposes a shared
multiplexed ADC. A future junction ADC must have simultaneous sample/hold or documented deterministic
channel skew small enough for the phase-error allocation.

## 7. Anti-aliasing and calibration

The live board has no verified output anti-alias pole at J4; J4.1 is U4 output with R4 to GND1.
Do not low-pass below the phase waveform before current-spinning demodulation. For the scope path:

1. sample raw outputs well above the phase rate;
2. apply the identical phase blanking/window to X/Y/Z;
3. perform eight-phase recombination;
4. digitally low-pass/decimate to the verified science bandwidth with recorded coefficients;
5. verify alias rejection using injected tones/noise above the retained band.

A future lower-rate ADC needs an analog anti-alias filter whose passband includes the raw phase
content needed by its demodulator; filter topology/cutoff is not released until phase rate and
settling are resolved.

Calibration order:

- electrical identity/continuity and mirror check;
- per-board injected differential delta-V gain/offset/linearity check resolving the 109x anomaly;
- current-source magnitude/compliance/noise and independence;
- phase-state truth table and inter-board skew;
- zero-field raw-phase offsets, recombined offset/noise and thermal drift;
- known-field gain/polarity for each axis;
- 3-by-3 vector sensitivity/orthogonality matrix after final mechanical installation;
- repeated calibration after cartridge/service/thermal-vacuum events.

Never use the current emulator amplitude as proof of absolute gain until the anomaly closes.

## 8. Ground, chassis, and shield architecture

### Intentional ambient common reference

The DSOX1204G BNC shells are common to protective earth, so a three-channel direct capture
intentionally commons the three board GND1 references. The cost baseline embraces this fact and
controls it at one **AGND_STAR interface panel** instead of claiming galvanic independence that the
scope defeats.

For each board, use one shielded branch bundle from the panel containing a0/a1/a2/EN, their
co-routed returns, VMEAS and its return. All return conductors in that one branch join GND1 at the
board and AGND_STAR at the panel; they do not take another chassis route. Overall branch shield
bonds at the panel only and floats at the board. The panel presents three short BNC outputs to
scope channels 1-3 and the sync BNC to channel 4. Do not simultaneously attach separate long J4
coaxes and separate Pico-GND straps; that would create undocumented parallel loops.

AGND_STAR bonds to chassis/protective earth at exactly one verified location, normally through the
grounded acquisition instrument. With power off, measure the existing vessel/scope/supply bonds
before installing a separate link; if scope earth already makes the bond, do not add another.
Route each complete board branch together so the intentional parallel returns enclose minimal area.

### Power domains

- One ambient 24-V source may be shared upstream, but distribute it in a star with per-board fuse
  or current limit, disconnect and indicator. Common input return is `PWR_RET`.
- Each board's RS6 produces isolated +/-15 V and GND1. RECOM calls the barrier functional,
  1.6-kVDC one-minute with 110-pF maximum capacitance. It reduces conducted loops from 24 V but is
  not a protective-earth safety barrier.
- The three GND1 nodes become intentionally common only at AGND_STAR through their documented
  branch bundles. No GND1 crosses the vacuum feedthrough.
- Pico/buffer 3.3-V ground is AGND_STAR. Current-source outputs remain floating and do not use
  AGND_STAR as bias return.
- CF flange/vessel is `CHASSIS`. Six sensor-pair screens terminate there; no Hall terminal does.

### Upgrade if the common-ground baseline fails

If measured loop current, switching feedthrough, common-mode range, or facility grounding is
unacceptable, use galvanically isolated four-channel logic branches plus genuinely differential or
isolated simultaneous acquisition. Do not install digital isolators while leaving grounded scope
coaxes and then claim isolation; both control and acquisition paths must be treated together.

## 9. Exactly what is shared and independent

| Item | Shared? | Rule |
|---|---|---|
| Pico state machine and phase truth | Yes | One versioned firmware/state sequence for all axes. |
| a0/a1/a2/EN source logic | Yes at Pico inputs to junction | Three independent buffer packages/outputs after the junction. |
| Sync/timebase | Yes | One sync captured with all three analog channels. |
| 24-V source | May be shared | Star distribution; per-board protection; no daisy-chain power. |
| AGND_STAR / scope reference | Intentionally shared ambient | One controlled point and one branch bundle per board; no vacuum connection. |
| Sensor terminals and 19C pins | No | Twelve unique nets, never paralleled. |
| 100-uA source outputs/returns | No | Three galvanically independent floating channels. |
| RS6 output rails/GND1 before star | No | One isolated converter per board; intentional common only at panel. |
| Analog amplification/J4 output | No | Three parallel channels into simultaneous DAQ. |
| Sensor pair shields | Chassis only | Six independent screens bond at flange; open at cartridge/board. |
| Calibration | Common procedure, independent coefficients | Per-axis gain/offset plus final vector matrix. |
| Faults | Contained by branch | EN/OE, fuse/current limit, label and disconnect per axis; AGND fault remains a known common-mode path. |

## 10. Pre-power and injected-signal acceptance sequence

1. Photograph vacuum and air 19C key/position marks and label the view.
2. With all connectors loose, prove V1-V19 to their mirrored air cavities using a continuity probe;
   record the entire permutation, not only used pins.
3. Verify all V13-V19 spares are open to signals/chassis and capped.
4. Verify each cartridge signed p-identity to the correct V circuit and board J1 pin using
   `20_PIN_AND_CABLE_MAP.csv`; two-person sign-off.
5. With boards disconnected, measure every signal conductor end-to-end and all-pairs/chassis
   isolation; flex only at approved harness test points while monitoring.
6. Verify each screen is continuous to the CF flange and open at cartridge/J1; verify no signal
   pin is a shield/return.
7. Inspect/continuity-test J1 footprint pin numbers and shell-to-GND1; do not infer from cable view.
8. Measure R5-R8 on all boards, buffer branch series resistors, buffer/OE safe states and J3 map.
9. Verify three current sources are mutually isolated and isolated from AGND_STAR/chassis while
   off; set compliance/current limits before connection.
10. Power 24-V branches one at a time with EN low; verify each RS6 rail/GND1 and absence of
    unexpected cross-board current.
11. Toggle a0/a1/a2/EN at low rate; scope every far-end J3 pin relative to that board GND1; verify
    truth, level, monotonicity, skew and no threshold recrossing.
12. Inject a known small differential signal into each board sensor connector; verify J4 gain,
    polarity, clipping margin and resolve the 109x anomaly before attaching a die.
13. Run the complete eight-phase sequence with emulator loads on all three boards; capture three
    outputs plus sync simultaneously; verify phase table, demod sign, crosstalk and noise.
14. Connect one real cartridge/axis at a time at current-limited 100 uA; verify terminal identity,
    plate resistance and zero-field output before adding the next axis.
15. Repeat continuity/isolation/injected-signal checks after final strain relief, vessel bake,
    service, and any connector re-termination.

All numerical resistance, insulation, skew, drift and crosstalk acceptance not sourced from an
exact component is `ENGINEERING PROPOSAL - VALIDATE` and must be frozen with the experiment error
budget.

## 11. Procurement-ready list and holds

| Qty | Item / candidate | Verified facts | Status / action |
|---:|---|---|---|
| 1 | Accu-Glass 19C-275, P/N 110210 | 19 male/male pins, 2.75-in CF, UHV 1e-10 Torr, -200 to 250 deg C, current live product. | `HOLD - DO NOT ORDER`: close G05-04 magnetic/mated-geometry/continuous-duty/UW-port gate. |
| 1 set | Vacuum-side 19C mate/contact solution | Accu-Glass 110240 pattern/contact sizes documented; PEEK assemblies are max 250 deg C. | `HOLD`: exact-max PEEK/BeCu system not continuous-life-qualified; stage 30/vendor must choose qualified ceramic/custom or tested exact assembly. |
| 6 pairs + spares | Allectra KAP301 shielded twisted pair or qualified equivalent | 300 deg C, UHV typical 1e-12 mbar, 32-AWG SP-Cu, 1.5-mm OD, published capacitance/current. | Candidate; verify length/fit, screen alloy/underplate, termination and procure same lot. |
| 3 | Existing `hsx_2026_v2` boards | Live netlist/BOM and J1/J3/J4 maps traced. | Replicate/inspect; physical J1 footprint and shell bond still require first-article verification. |
| 1 | Raspberry Pi Pico 2 | 3.3-V GPIO capability; production commitment; existing GP16/17/18/20/19 plan. | Use as controller, not simultaneous ADC. |
| 3 | TI SN74LVC125APW/PWR quad buffer | Active, 1.65-3.6 V, four 3-state channels, 5-pF typical input, 3.3-V high-current drive, fast propagation. | Baseline junction buffer; exact package/availability refresh at order. |
| 12 | Branch source-series resistors | 33 ohm start value. | `ENGINEERING PROPOSAL - VALIDATE`; populate/tune 22-68 ohm from final cable waveforms. |
| 3 sets | Keyed branch connector/cable, five signal/return pairs plus overall shield | Functional requirement defined. | Exact MPN `UNVERIFIED`; select by ambient voltage/current, locking, shielding and service availability. |
| 3 | Mating male DE-9 sensor cable plugs/backshells | Board J1 is a female socket/receptacle. | Exact MPN `UNVERIFIED`; continuity-verify front/rear view and shell strategy before order. |
| 3 | Independent floating 100-uA current-source channels | Electrical requirement defined. | Exact instrument/module `HOLD - DO NOT ORDER`; require channel-to-channel isolation/compliance/noise evidence. |
| 1 | 24-V ambient supply plus 3 branch fuses/current limit/disconnects | RS6 input is 18-36 V. | Size after measured per-board load/inrush; exact MPN `UNVERIFIED`. |
| 1 | Keysight DSOX1204G or equivalent simultaneous 4-channel acquisition | Four analog channels, 8-bit, up to 2 GSa/s, 2 Mpoints. | Verify installed options, multi-channel mode/skew/memory/export; existing instrument preferred. |
| 4 | Short panel-to-scope BNC cables | Three analog + sync. | Equal/recorded lengths; exact MPN `UNVERIFIED`. |
| 1 | Ambient interface junction enclosure/panel | Functional content and net rules defined here. | Design/build after branch cable/ground survey; no sensor-net commoning. |

## 12. Open gates created by this stage

- `G20-01 HOLD - DO NOT TERMINATE`: first-article 19C V1-V19 vacuum-to-air mirror continuity and
  connector-view traveler, because numbers are not printed and male-male geometry mirrors.
- `G20-02`: measure all R5-R8 values on all boards; freeze branch cable capacitance/length;
  validate buffer/OE/series-resistor levels, skew, ringing and phase settling at maximum rate.
- `G20-03 HOLD - DO NOT POWER REAL SENSORS`: resolve the approximately 109x board amplitude
  anomaly and replicate the delta-V gain/phase test on X/Y/Z.
- `G20-04 HOLD - PERFORMANCE CLAIM`: reconcile nominal/stated 40-100-kHz phase operation with
  the 10-20-kHz post-recombination target; verify analog settling, raw sampling and demodulated
  bandwidth before claiming it.
- `G20-05 HOLD - DO NOT CONNECT BIAS`: exact three-channel current-source architecture/parts must
  prove channel-to-channel and chassis isolation, compliance, noise, current accuracy and fault
  limiting.
- `G20-06`: survey facility vessel/scope/24-V protective-earth paths; freeze AGND_STAR location,
  branch bundle/shield termination, allowable ground current/noise, and isolation-upgrade trigger.
- `G20-07 HOLD - DO NOT ORDER CABLE/CONNECTORS`: close 19C PEEK/contact continuous-250-deg-C
  UHV/magnetic/retention gate and select exact in-vessel/ambient connector/contact/tool parts.
- `G20-08`: select exact ambient branch connectors, DE-9 plugs/backshells, power distribution,
  BNCs and junction enclosure; refresh price/stock and verify mating views.

## 13. Drawing/table consistency

- `drawings/20_end_to_end_block.svg` follows X=V1-V4, Y=V5-V8, Z=V9-V12; J1 p1/p3/p2/p4
  pins 1/2/6/7; three buffers/boards; three analog channels plus sync.
- `drawings/21_ground_and_shield.svg` has no GND/shield feedthrough signal pin; six screens end at
  CF flange; three floating current sources; three RS6 barriers; intentional AGND_STAR and one
  chassis/earth bond; branch fault/protection boundaries.
- `20_PIN_AND_CABLE_MAP.csv` has 12 signal rows, seven spare rows and six shield rows with unique
  net/axis/terminal/pair/label/feedthrough/air-cavity/J1/endpoints/resistance/isolation fields.

Stage-20 result: **complete end-to-end architecture selected; installation/order/performance holds
remain explicit and testable**.

## Sources added/used

- Accu-Glass 19C connector pattern/wiring caution: https://www.accuglassproducts.com/sites/default/files/PDF/Partpdf/110240.pdf
- Accu-Glass 19C feedthrough/product family: https://www.accuglassproducts.com/mil-c-26482/cf-feedthroughs/19c-275
- TI SN74LVC125A data sheet: https://www.ti.com/lit/ds/symlink/sn74lvc125a.pdf
- Raspberry Pi RP2350 data sheet: https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf
- Analog Devices ADG1209: https://www.analog.com/media/en/technical-documentation/data-sheets/ADG1208_1209.pdf
- Analog Devices ADG5236: https://www.analog.com/media/en/technical-documentation/data-sheets/adg5236.pdf
- RECOM RS6: https://recom-power.com/pdf/Econoline/RS6.pdf
- Keysight DSOX1204G family: https://www.keysight.com/zz/en/assets/7018-06411/data-sheets/5992-3484.pdf
- Allectra KAP301: https://www.allectra.com/wp-content/uploads/2025/02/301-KAPM-025-PAIR1.pdf
