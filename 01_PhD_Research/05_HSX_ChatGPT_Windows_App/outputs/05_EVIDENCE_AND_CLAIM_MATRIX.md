# Stage 05 - primary-source evidence and claim matrix

Date accessed: 2026-07-12  
Scope: evidence only; this stage does **not** freeze a bond map, external joint, contact design,
board architecture, package geometry, purchase, or fabrication release.

## 1. Evidence rules used

- `VERIFIED FACT` means a directly opened manufacturer drawing/data sheet, active standard,
  government report, or peer-reviewed source supports the statement.
- `CALCULATION` means the arithmetic is shown and its inputs are traceable.
- `CONDITIONAL` means the technology is credible but the exact material, geometry, process, or
  continuous-life evidence is missing.
- `REJECTED CLAIM` means the available source does not support the stronger conclusion previously
  drawn from it.
- `ENGINEERING PROPOSAL - VALIDATE` is a future acceptance criterion or design direction, not a
  supplier rating.
- `HOLD - DO NOT FABRICATE/ORDER` is used where an irreversible action could embed an unresolved
  orientation, material, magnetic, dimensional, or lifetime error.

The direct URLs and source-specific limitations are also captured in
`outputs/SOURCE_LEDGER.csv`. Catalog maxima are treated as boundary values, not life margin. ASTM
E595 screening, a bake, reflow peak, melting point, or short thermal soak is not treated as proof of
continuous service at 250 deg C.

## 2. LCC02046 construction, numbering, and connectivity

| Claim | Classification | Evidence and exact support | Consequence / limitation |
|---|---|---|---|
| LCC02046 is a 20-lead, 5-by-5, 0.050-in-pitch, 0.350-in-square ceramic carrier with a 0.160-in-square cavity. | VERIFIED FACT | Spectrum's live LCC table lists LCC02046 as 20 leads, 5-by-5, 0.050-in pitch, 0.35-in body, 0.16-in cavity; its drawing PB-CA8272-B supplies the chamfered mechanical datum. [Spectrum product page](https://www.spectrum-semi.com/products/leadless-chip-carrier), [drawing](https://www.spectrum-semi.com/sites/default/files/pdfs/LCC02046.pdf) | Use 8.89 mm body and 4.064 mm nominal cavity only with drawing tolerances; inspect actual lots. |
| Each internal shelf trace terminates at its corresponding metallized side/bottom castellation. | VERIFIED FACT | Spectrum describes short internal traces extending from the inside cavity to metallized castellations on all sides and bottom. | This supports die-to-shelf-to-same-numbered-castellation continuity. It does **not** support arbitrary pad-to-pad continuity inside the carrier. |
| The local cavity-up pad sequence is top 8-7-6-5-4 left-to-right, right 3-2-1-20-19 top-to-bottom, bottom 14-15-16-17-18 left-to-right, and left 9-10-11-12-13 top-to-bottom; the separate bottom view is mirrored. | VERIFIED LOCAL OBSERVATION | Original-resolution inspection of both views in `inputs/reference/user_2026-07-12_LCC_routing_annotated.png`, reconciled to the live Spectrum drawing. | This is the controlling view convention for later drawings, but physical carrier continuity/chamfer sign-off remains mandatory. |
| Spectrum's drawing calls out Au on the bonding/metallized surface without a Ni barrier, with minimum Au thickness in the thin-film range relevant to Al-Au bond literature. | VERIFIED FACT, LOT CHECK REQUIRED | Live drawing and supplied manufacturer drawing call out the finish; the 0.508-um-equivalent minimum is within the approximately 1-um upper range discussed by Johannessen et al. | Drawing finish is not a certificate of conformance for the purchased lot; obtain lot stack and verify shelf/castellation plating. |
| The user's four red die bonds are shown at shelf pads 8, 3, 19, and 14. | VERIFIED LOCAL OBSERVATION | The annotated image explicitly draws red bonds to these pads. | The die terminal identities are not authoritative because p1-p4 physical orientation evidence is absent. |
| External routes 8->4, 3->9, 19->13, and 18->14 are directional signal paths. | REJECTED CLAIM / NOTATION RESOLVED IN STAGE 10 | The green routes are drawn on the mirrored bottom view; 18 is left and 14 is right there. Passive jumpers have no signal-flow direction, so normalize them as `8<->4`, `3<->9`, `19<->13`, and `14<->18`; q4 remains bonded to 14. | The notation no longer blocks analysis. The jumper network is still not an internal LCC route or an accepted one-side breakout, and die p1-p4 sign-off remains mandatory. |
| The historical p1->1, p3->16, p2->11, p4->6 map is physically authoritative. | REJECTED CLAIM | Those are the mid-side pads, but the historical association is not registered to the supplied chamfered view and the actual die p1-p4 orientation is missing. | Keep an orientation-parametric mapping; never guess p1-p4. |
| Direct soldering or a socket is generally contemplated by the LCC vendor. | VERIFIED GENERAL CAPABILITY | Spectrum says LCCs may mount directly or in sockets. | No listed socket or assembly process is qualified by Spectrum for this exact 250 deg C UHV continuous-life application. |

### Stage-10 evidence gate created here

`HOLD - DO NOT BOND`: close only with (1) physical LCC chamfer and pad-continuity traveler, (2)
authoritative die p1-p4/GDS or microscope orientation sign-off, (3) explicit cavity-up/view datum,
(4) resolution of 14 versus 18, and (5) purchased-lot metallization evidence.

## 3. Aluminum wedge bonds and dissimilar-metal aging

| Claim | Classification | Evidence and exact support | Consequence / limitation |
|---|---|---|---|
| Al wedge bonding from the die to a thin-Au LCC shelf is technically credible at 250 deg C. | CONDITIONAL | Johannessen et al. aged 25-um Al wedge bonds for 6-12 months at temperatures up to 250 deg C and reported Al on thin-film Au reliable for Au thickness up to about 1 um. [SINTEF publication record](https://www.sintef.no/en/publications/publication/1274740/) | Strongest directly relevant source found, but not the actual die pad, LCC lot, wedge tool, loop, cure, or UHV environment. |
| A successful initial pull test proves continuous 250 deg C life. | REJECTED CLAIM | NASA reported significant pull-strength losses after only 72 h at 150 deg C for tested Al bonds on thick- and thin-film Au. [NASA NTRS](https://ntrs.nasa.gov/citations/19750024389) | Qualification needs unaged controls plus aged distributions, resistance tracking, and failure-mode inspection. |
| Gold wire on an aluminum die pad is an equivalent substitute without new aging evidence. | REJECTED CLAIM | Peer-reviewed Au-Al work at 175/250 deg C documents intermetallic evolution, cavity growth, and failure mechanisms. [Journal of Materials Research](https://www.cambridge.org/core/journals/journal-of-materials-research/article/degradation-and-failure-mechanisms-in-thermally-exposed-aual-ball-bonds/C4FF4BA55BF4F1AFED224396ECB84E85) | Avoid changing wire metallurgy casually; if considered, treat as a separate coupon program. |
| MIL-STD-883 Method 2011 is a valid pull-test framework. | VERIFIED FACT | DLA lists MIL-STD-883 active; Part 2 Method 2011 defines destructive bond-pull apparatus, representative specimens, and force criteria. [DLA landing](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=283310), [Part 2 PDF](https://landandmaritimeapps.dla.mil/Downloads/MilSpec/Docs/MIL-STD-883/std883-2.pdf) | Freeze the active revision/change in the traveler. MIL minimum force is a workmanship floor, not this project's life criterion. |
| Exact loop height, heel clearance, wire diameter, die-pad metallurgy, and pull threshold can be frozen from present evidence. | UNVERIFIED | The 2023 paper establishes earlier Al-wire assembly, but the current gen-2 die pad stack/orientation, actual wire, tool, and bonder capability are missing. | `HOLD - DO NOT BOND`. |

### Qualification direction, not yet a released criterion

`ENGINEERING PROPOSAL - VALIDATE`: fabricate same-lot die/LCC coupons and record wire alloy,
diameter, wedge/tool, ultrasonic power, force, time, substrate temperature, loop height, heel
clearance, pad coordinates, and operator. Use unaged controls and staged 250 deg C vacuum aging;
measure four-wire path resistance and pull distributions after each interval; inspect fracture mode
and intermetallic/cavity cross-sections. Duration, sample count, allowable drift, and lower-confidence
bound remain open until the continuous duty duration is specified.

## 4. Die attach: EPO-TEK 353ND

| Claim | Classification | Evidence and exact support | Consequence / limitation |
|---|---|---|---|
| 353ND has a recommended 150 deg C/1 h cure and passes low-outgassing screening with proper cure. | VERIFIED FACT | The March 2025 TDS gives the cure and ASTM E595 statement. The supplier guide lists an example TML 0.81% and CVCM 0.01% after 120 deg C/1 h cure. [TDS](https://www.epotek.com/docs/en/Datasheet/353ND.pdf), [test guide](https://www.epotek.com/docs/en/Related/Epoxy%20Adhesive%20Test%20Measurement%20Guide.pdf) | Cure-dependent; record lot, ratio, mass, cure, post-cure, bondline, and cleanliness. |
| E595 pass proves continuous 250 deg C UHV suitability. | REJECTED CLAIM | NASA explains that E595 is a 125 deg C vacuum screening test reporting TML/CVCM/WVR. [NASA GSFC guide](https://etd.gsfc.nasa.gov/capabilities/outgassing-database/user-guide/) | It does not measure 250 deg C outgassing rate, long-term adhesion, electrical leakage, or contamination at HSX conditions. |
| Supplier weight-loss data and a suggested `<350 deg C intermittent` limit qualify continuous 250 deg C use. | REJECTED CLAIM | The TDS explicitly labels the high-temperature operating suggestion intermittent, gives Tg >=90 deg C, CTE above Tg 206 ppm/K, and says typical data are guidance rather than guaranteed specification. | Continuous 250 deg C is far above Tg; bondline creep, modulus loss, fatigue, contamination, and remount reuse require same-stack life evidence. |
| 353ND can be released as the reusable-head baseline now. | UNVERIFIED / HOLD | No current source supplies continuous-250C UHV mechanical/electrical lifetime for the actual die/LCC stack. | `HOLD - DO NOT FABRICATE` bonded production heads; coupons may be built under a controlled qualification traveler. |

## 5. External electrical transition candidates at continuous 250 deg C UHV

### 5.1 Solder and braze

| Technology claim | Classification | Evidence | Result for later trade study |
|---|---|---|---|
| 80Au20Sn is high-temperature solder with a 280 deg C eutectic. | VERIFIED FACT | [Indium PDS](https://documents.indium.com/qdynamo/download.php?docid=328) | At 250 deg C the absolute-temperature ratio is `523.15 K / 553.15 K = 0.946`; only 30 deg C liquidus margin. This is not a conservative unsupported structural or strain-relief joint. |
| AuGe and AuSi provide higher melting temperatures than AuSn. | VERIFIED FACT | Indium table lists AuGe 356 deg C and AuSi 363 deg C. [Indium alloy table](https://scp.indium.com/download-files/power_semiconductor_assembly_98464_r0.pdf) | Potential separate-terminal processes; high process temperature and metallization compatibility may damage an assembled sensor/LCC. |
| Accu-Glass UHV solder 110796 is a settled 250 deg C joint. | REJECTED CLAIM | The catalog text identifies about 280 deg C flow/melting and a flux-cleaning procedure, while a nearby heading says 480 deg C. [Accu-Glass catalog](https://www.accuglassproducts.com/sites/default/files/catalog/wiring_accessories.pdf) | Internal documentation inconsistency plus 30 deg C nominal margin. Get written composition/liquidus/process confirmation and run creep/resistance aging. |
| A high-temperature braze can be applied to the fully assembled reusable sensor carrier. | REJECTED CLAIM | High-temperature brazes exist, but their process temperatures are far above sensor/LCC adhesive and bond limits. | Braze only a separately manufactured terminal/ceramic-to-metal subassembly, never the completed sensor/LCC without a new qualified stack. |

### 5.2 Weld, crimp, screw terminal, and separable contact

| Technology claim | Classification | Evidence | Result for later trade study |
|---|---|---|---|
| Resistance welding stranded Cu to a compatible terminal is credible. | CONDITIONAL | microJoining documents the method and the strong dependence on conductor/terminal/plating. [wire-weld paper](https://www.microjoining.com/docs/1352551504_microtip_resistance_stranded_copper_wire.pdf), [plating paper](https://www.microjoining.com/docs/1352550977_microtip_plating_issues.pdf) | Requires actual-material DOE, weld schedule, cross-sections, pull, resistance, and aged vacuum coupons. It is a candidate permanent pigtail-to-terminal joint, not a presumed LCC weld. |
| Crimp workmanship can be controlled by an active standard. | VERIFIED FACT | [NASA-STD-8739.4](https://standards.nasa.gov/standard/nasa/nasa-std-87394) and [Change-2 PDF](https://standards.nasa.gov/sites/default/files/standards/NASA/A/2/nasa-std-87394a_w_change_2.pdf) | Use only with a contact specified for the conductor gauge/material and temperature; workmanship does not qualify materials at 250 deg C UHV. |
| Bare screw-secured in-line contacts exist for 400 deg C vacuum. | VERIFIED FACT | Accu-Glass lists Au-plated BeCu in-line connectors with SS screws for 400 deg C vacuum. [product page](https://www.accuglassproducts.com/specialty-connectors/push-line-connectors) | Strong proof that a high-temperature serviceable terminal concept is commercially real, but available sizes are much larger than an LCC castellation. Independent strain relief is mandatory. |
| A standard push-on BeCu contact is safe at 250 deg C. | REJECTED AS GENERAL CLAIM | Accu-Glass's generic push-on range is 200 deg C; one larger crimp contact is separately cataloged at 250 deg C/UHV. [product page](https://www.accuglassproducts.com/specialty-connectors/push-line-connectors), [catalog](https://www.accuglassproducts.com/sites/default/files/catalog/wiring_accessories.pdf) | Never transfer a rating across contact sizes. BeCu retained force at continuous 250 deg C remains unproven. |
| A catalog LCC02046 socket qualified for continuous 250 deg C UHV was found. | NOT FOUND | Spectrum permits sockets generally; Deringer-Ney offers custom high-temperature contacts; no primary source found for the exact LCC/UHV/life combination. | Reusable LCC connection must be a controlled custom cartridge/contact subsystem or a service disconnect placed away from a permanent LCC pigtail. |
| Precious-metal spring contacts can operate at 250 deg C. | CONDITIONAL | Deringer-Ney describes custom separable contacts to 250 deg C and publishes Paliney stress-relaxation curves. [contacts](https://deringerney.com/products/electrical-contacts/), [manual](https://deringerney.com/wp-content/uploads/2022/04/Ney-Contact-Manual-Revised-1st-Edition.pdf) | No UHV, magnetic-permeability, exact-alloy/temper, force window, or miniature geometry qualification. Vendor consultation and coupons are required. |

### 5.3 Strain relief and electrical-joint load path

`VERIFIED DESIGN RULE FROM FAILURE PHYSICS`: none of the cited electrical joining sources makes
the joint a structural harness anchor. Therefore every candidate remains conditional on a separate
ceramic/metal strain-relief path that takes cable mass, handling, thermal-expansion, and service
loads without loading die bonds, shelf jumpers, castellations, solder fillets, weld nuggets, crimps,
or contact normal force.

`ENGINEERING PROPOSAL - VALIDATE`: after assembly and after aging, apply a documented harness
proof load at the service direction while monitoring four-wire resistance and isolation. The proof
load magnitude is open pending harness mass, routing, acceleration/handling envelope, and contact
supplier limits.

## 6. Conductor and insulation evidence

| Claim | Classification | Evidence and calculation | Consequence / limitation |
|---|---|---|---|
| 300 deg C UHV Kapton/silver-plated-copper wire is commercially available. | VERIFIED FACT | Allectra KAP301 pair is rated 300 deg C, UHV typical `1e-12 mbar`, and typical 0.4 A at 250 deg C. The 100-uA sensor bias uses `0.0001/0.4 = 0.00025`, or 0.025% of that typical current. [datasheet](https://www.allectra.com/wp-content/uploads/2025/02/301-KAPM-025-PAIR1.pdf) | Current capacity is irrelevant to selection; geometry, capacitance, magnetic finish, termination, thermal conduction, and serviceability dominate. |
| Six shielded KAP301 pairs automatically fit the head exit. | UNVERIFIED | Nominal six-cable cross-sectional material area is `6*pi*(1.5 mm)^2/4 = 10.6 mm^2` before packing voids/strain relief. | The 31.75-mm by 27.5-mm installed envelope and exit direction require CAD routing; a shared external screen or 12 smaller singles may be preferable. |
| Accu-Glass's 19C PEEK/Kapton cable is qualified with useful temperature margin. | REJECTED CLAIM | Its maximum operating and bake temperature is exactly 250 deg C. | Zero declared margin; connector retention, PEEK creep, and lowest-component rule keep it conditional. |
| PEEK is a safe continuous-preload material because the family is called continuous-temperature capable. | REJECTED CLAIM | Victrex gives Tg about 143 deg C, much higher CTE above Tg, and category-dependent RTI. [product guide](https://www.victrex.com/-/media/downloads/technical-guides/victrex-product-guide-victrex-peek-properties-en-09-2018.pdf) | Exact grade, stress, geometry, vacuum history, and retained dimension/force at 250 deg C must be demonstrated. No PEEK preload part in the reusable-head baseline. |
| BeCu spring force is stable indefinitely at 250 deg C. | REJECTED CLAIM | Materion explains time-temperature stress relaxation and notes C17200 precipitation begins near 260 deg C. [Materion](https://www.materion.com/en/insights/blog/in-our-element-temperature-affect-material-properties) | 250 deg C is too close to a metallurgy transition to assume retained force; exact temper/stress/time data or coupons are mandatory. |

## 7. Magnetic-material screen

| Item / claim | Classification | Source support | Gate |
|---|---|---|---|
| 19C-275 pins are Au-plated Ni-Fe alloy. | VERIFIED FACT | [Accu-Glass product page](https://www.accuglassproducts.com/mil-c-26482/cf-feedthroughs/19c-275) | Ni-Fe is deliberately magnetic in many seal alloys. Calculate distance/field only after UW port and magnetic perturbation budget are known; do not assume harmlessness. |
| Nickel-plated connector shells or steel/nickel terminals are acceptable near the Hall die. | REJECTED AS UNSCREENED | Molex's live 73100-0105 drawing, for example, calls out a nickel-plated zinc-alloy body; Accu-Glass lists steel/nickel for some lugs. [Molex drawing](https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/731/73100/731000105_sd.pdf) | Ambient board connectors may be distant; any in-head use requires material-by-material magnetic screening. |
| Titanium or a named precious-metal contact is automatically nonmagnetic. | UNVERIFIED | No supplier magnetic-permeability declaration for the exact fastener/contact lot has been obtained. | `HOLD - DO NOT ORDER` critical near-sensor fasteners/contacts until alloy, cold-work state, coating/underplate, and magnetic acceptance method are stated. |

## 8. Feedthrough and boundary evidence

| Claim | Classification | Evidence | Consequence / limitation |
|---|---|---|---|
| 19C-275 has enough circuits for three isolated four-terminal sensors. | VERIFIED FACT + CALCULATION | P/N 110210 has 19 pins. Required sensor conductors are `3 axes * 4 = 12`, leaving `19 - 12 = 7` spare pins. [product page](https://www.accuglassproducts.com/mil-c-26482/cf-feedthroughs/19c-275) | No sensor return may be shared merely to save pins. Shields should terminate to chassis/flange separately unless a verified pin use is deliberately assigned. |
| The feedthrough meets UHV and nominal temperature boundary ratings. | VERIFIED FACT | Manufacturer gives UHV `1e-10 Torr`, -200 to 250 deg C, 500 VDC, and 5 A/pin at 20 deg C. [drawing](https://www.accuglassproducts.com/sites/default/files/PDF/Partpdf/110210.pdf) | Exact 250 deg C maximum is not life margin. Current rating at 20 deg C is not needed for 100 uA and is not a 250 deg C derating value. |
| 19C-275 and its PEEK cable can be ordered now as a qualified system. | REJECTED / HOLD | Live pages establish current part numbers/prices, but magnetic pins, protrusion, contact range, PEEK retention, continuous-life interpretation, and UW port datum remain unresolved. | `HOLD - DO NOT ORDER` until written vendor/UW confirmations and architecture freeze. |
| Live indicative procurement cost is known. | VERIFIED TIME-STAMPED FACT | Feedthrough page listed 434 USD and female vacuum connector cable page 398 USD on 2026-07-12. | Not a quote; exclude from released BOM until refreshed. |

## 9. Three-board control, bias, acquisition, and grounding evidence

The electronics are ambient by locked constraint; the purpose here is to establish component facts
and reject unsafe architectural shortcuts, not select the final topology.

| Claim | Classification | Evidence / calculation | Consequence / limitation |
|---|---|---|---|
| One Pico 2 can logically fan out the shared phase controls to three boards. | CONDITIONAL, STRONGLY CREDIBLE | Pico GPIO offers 2/4/8/12-mA drive and slew control. ADG1209 digital input capacitance is 2 pF typical at dual supply; ADG5236 is 3 pF typical; both accept 3.3-V logic with `V_INH=2.0 V`. [RP2350](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf), [ADG1209](https://www.analog.com/media/en/technical-documentation/data-sheets/ADG1208_1209.pdf), [ADG5236](https://www.analog.com/media/en/technical-documentation/data-sheets/adg5236.pdf) | Actual netlist input count, cable capacitance/length, common logic reference, edge ringing, and simultaneous board switching must be measured. |
| Net-specific silicon-only fanout is small. | CALCULATION, SUPERSEDED/REFINED BY STAGE 20 LIVE TRACE | Per board, a0/a1/EN each reach two 2-pF ADG1209 inputs and a2 reaches two 3-pF ADG5236 inputs. Three-board totals are therefore a0=12 pF, a1=12 pF, a2=18 pF, EN=12 pF typical before PCB/cable/pulldown effects. | Exact R5-R8 values are absent from the netlist/BOM; cable capacitance, edge ringing and branch skew remain measured release criteria. Stage 20 recommends independent buffered branches. |
| The Pico ADC's three pins provide simultaneous three-axis acquisition. | REJECTED CLAIM | RP2350 has a shared ADC peripheral and muxed input channels; the Pico product page's three ADC-capable pins do not claim three simultaneous converter cores. [RP2350](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf), [Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/) | Use a simultaneous external DAQ/scope or independently synchronized ADCs; do not infer simultaneity from pin count. |
| A four-channel DSOX1204G can observe the three analog outputs plus sync. | VERIFIED CAPABILITY | Keysight lists four analog channels, 8-bit ADC, up to 2 GSa/s, and 2 Mpoints. [data sheet](https://www.keysight.com/zz/en/assets/7018-06411/data-sheets/5992-3484.pdf), [product page](https://www.keysight.com/sg/en/product/DSOX1204G/oscilloscope-70-100-200-mhz-4-analog-channels-waveform-generator.html) | Confirm acquisition mode, effective simultaneous timing/skew, sample-rate sharing, installed options, anti-alias strategy, and export workflow. |
| The existing analog components have bandwidth headroom for testing a 10-20-kHz recombined target. | VERIFIED COMPONENT HEADROOM, SYSTEM TEST REQUIRED | AD8429 is 1.2 MHz at gain 100; ADG switching is sub-microsecond under specified loads. [AD8429](https://www.analog.com/media/en/technical-documentation/data-sheets/AD8429.pdf), [ADG1209](https://www.analog.com/media/en/technical-documentation/data-sheets/ADG1208_1209.pdf) | Component bandwidth alone does not prove system bandwidth. Stage 20 shows 8-phase updates are 5 kHz at 40-kHz phase rate and 20-kHz updates would require 160-kHz phases before filter margin, outside the retained 100-kHz stated usable rate. The approximately 109x amplitude anomaly and full settling/demod/filter response remain gates. |
| One shared nonisolated bias return is acceptable because phase lines are shared. | REJECTED CLAIM | The locked design requires three independently floating 100-uA bias sources; shared logic does not authorize shared sensor current return. | Each board/sensor bias loop must remain electrically identifiable and independently fault-contained through the feedthrough. |
| RS6-2415D isolation alone eliminates all inter-board coupling. | REJECTED CLAIM | RECOM specifies functional isolation, 110-pF maximum isolation capacitance, and 1.6-kVDC one-minute rating. [RECOM](https://recom-power.com/pdf/Econoline/RS6.pdf) | Three independent modules help contain DC loops, but common 24-V input, 110-pF barriers, logic-ground bonds, scopes, shields, and chassis still form AC paths. |
| J3 alone provides a correct Pico interface. | REJECTED CLAIM | Authoritative local netlist says J3 has only a2/a1/a0/EN and no ground. | A separate Pico ground-to-each-board GND1 connection or deliberate isolated logic interface is mandatory. |

## 10. Zirconia package DFM evidence

| Claim | Classification | Evidence | Consequence / limitation |
|---|---|---|---|
| Identical flat zirconia plates with smooth through-holes are a credible cost-oriented prototype direction. | ENGINEERING PROPOSAL - VALIDATE | Precision Ceramics says green/biscuit machining is easier, while post-fire diamond grinding is needed for tight tolerances; CoorsTek guidance favors uniform sections, radii, and adequate webs. [zirconia](https://precision-ceramics.com/uk/materials/zirconia/), [CoorsTek guide](https://www.coorstek.com/media/4221/thick-film-ceramic-substrates-design-guide.pdf) | This supports the contract preference but is not a vendor quote or released tolerance stack. |
| Near-net green machining eliminates dimensional risk. | REJECTED CLAIM | Zirconia shrinks about 20% during sintering, so pre-sintered tight tolerances cannot simply be assumed. | Use generous assembly clearance, datum strategy, and post-fire grinding only at functional faces/holes. |
| Internal zirconia threads are cost-neutral and serviceable. | REJECTED DESIGN DIRECTION | No source establishes robust prototype internal threads; ceramic DFM sources favor radiused, supported features and post-fire precision operations are costly. | Binding baseline remains zero tapped/internal zirconia threads; use smooth through-holes and replaceable accessible external nuts/nut plates. |
| Exact minimum wall, radius, hole tolerance, flatness, and 1/3/10-set price are known. | UNVERIFIED | Available guidance is generic and material/process-specific. | `HOLD - DO NOT FABRICATE`; issue a vendor drawing/RFQ after stage-30 geometry is checked. |

### Vendor-RFQ evidence package required before ceramic release

Request exact zirconia grade, lot traceability, green/biscuit/fired process, nominal shrink
compensation, as-fired/post-ground faces, flatness/parallelism, hole diameter/location, edge chip
allowance, minimum web/radius, surface finish, inspection method, cleaning/bake compatibility,
lead time, nonrecurring tooling, and 1/3/10-set prices. Ask the vendor to redline any fragile or
costly feature rather than silently accepting the drawing.

## 11. Technology disposition for later stages

This table is intentionally not a final design selection.

| Decision family | Verified now | Conditional candidate | Rejected or on hold |
|---|---|---|---|
| Die-to-LCC | Al wedge to thin Au has relevant 250C aging precedent | Same-stack Al wedge coupon program | Fixed p1-p4 map; initial pull alone; casual Au-wire substitution |
| Die attach | 353ND cure/outgassing screening facts | Same-stack controlled coupons | Continuous-250C qualification inferred from intermittent limit/E595 |
| LCC shelf/castellation | Corresponding trace-to-castellation architecture | Permanent qualified pigtail plus remote service terminal; custom high-temp contact | Assumed catalog 250C-UHV LCC socket |
| External joint | 400C vacuum in-line terminals exist; welding/crimp standards/processes exist | Resistance weld/crimp/custom precious-metal contact after DOE | AuSn as unvalidated structural joint; load through an electrical joint |
| Wire | 300C UHV Kapton/SP-Cu products exist | 12 singles/shared screen or six pairs after CAD/EMI trade | Exact-250C PEEK cable accepted without margin |
| Feedthrough | 19 pins cover 12 independent conductors; UHV/temp facts verified | 19C-275 after written magnetic/mechanical/life confirmation | Order before UW port/contact/magnetic closure |
| Control | Pico 3.3-V logic and device thresholds/capacitance support fanout feasibility | Direct fanout with measured cable/edge limits or buffered star | One board receives analog data and retransmits to the other analog boards without a defined need |
| Acquisition | Four-channel scope can capture three outputs plus sync | Simultaneous external DAQ or synchronized ADCs | Pico ADC assumed simultaneous |
| Ceramic | Green machining and post-fire grinding trade is verified | Identical flat thread-free parts | Internal zirconia threads; unquoted tight all-over tolerances |

## 11A. Stage-30 material and fastener supplement

| Claim | Classification | Evidence and exact support | Consequence / limitation |
|---|---|---|---|
| Representative zirconia CTE is close to commercially pure titanium through the operating range. | VERIFIED REPRESENTATIVE DATA / CALCULATION INPUT | Kyocera lists 10.4e-6/K from 40-400 C for its ZO206N zirconia; TIMET lists 9.5e-6/K from 20-300 C for TIMETAL 75A Grade 4. [Kyocera](https://global.kyocera.com/prdct/fc/technologies/001.html), [TIMET](https://www.timet.com/assets/local/documents/datasheets/cpgrades/75a.pdf) | Supports the small displacement-change calculation in Stage 30. It is not a guarantee for the selected ceramic lot or formed clamp; exact grade and hot force remain qualification gates. |
| CP-Ti Grade 4 is a credible nonmagnetic 250 C structural/flexure material. | CONDITIONAL | TIMET identifies the alloy as nonmagnetic, lists elevated-temperature tensile data, and states typical continuous service to 425 C. | Material survival is credible, but formed-flexure creep/relaxation, surface condition, galling, fastener reuse, and UHV cleaning are unqualified. `HOLD - DO NOT FABRICATE`. |
| Cleanroom titanium M1.6 miniature screws are commercially available. | VERIFIED PRODUCT GEOMETRY ONLY | NBK lists SNZT-M1.6 in 3-6 mm lengths, Grade 1 Ti, cleanroom wash/pack, and representative permeability 1.0001. [NBK](https://www.nbk1560.com/en-US/products/specialscrew/nedzicom/titaniumscrew/SNZT/SNZT-M1.6/) | The part is a dimensional candidate only; NBK does not provide continuous-250 C UHV qualification and the part is not vented. Use open through-holes or custom venting; do not order from this evidence alone. |
| Blind threaded holes are avoidable and vacuum venting is a recognized hardware requirement. | VERIFIED GENERAL PRACTICE | NBK's vacuum-fastener page explains that ventilation holes release trapped gas beneath threads and offers vented titanium families. [NBK](https://www.nbk1560.com/en/products/specialscrew/nedzicom/vacuumscrew/) | The modeled miniature size was not found as a qualified titanium vented catalog part. Stage 30 therefore uses open through-holes and replaceable external nut pads, with exact hardware held. |
| Representative alumina CTE can be used to bound LCC/zirconia pocket clearance. | CONDITIONAL CALCULATION INPUT | Kyocera lists 7.2e-6/K from 40-400 C for a representative alumina. [Kyocera](https://global.kyocera.com/prdct/fc/technologies/003.html) | Spectrum must confirm the LCC02046 ceramic grade; the resulting approximately 0.007-mm clearance increase is sensitivity analysis, not release evidence. |

## 12. Newly sharpened open gates

1. `G05-01 HOLD - DO NOT BOND`: die p1-p4 orientation, LCC chamfer continuity, purchased-lot
   plating, and 14/18 route semantics.
2. `G05-02 HOLD - DO NOT RELEASE BONDED HEAD`: actual die-pad metallurgy, 353ND lot/cure/bondline,
   Al wire/process, and continuous-250C vacuum-aging plan.
3. `G05-03 HOLD - DO NOT FABRICATE CONTACTS`: reusable LCC contact/pigtail architecture lacks
   exact alloy, temper, UHV declaration, magnetic declaration, normal-force window, contact
   resistance, equipment capability, and aged qualification.
4. `G05-04 HOLD - DO NOT ORDER FEEDTHROUGH SYSTEM`: vendor/UW confirmation needed for the 19C
   mated vacuum geometry, contact range, exact continuous-temperature interpretation, Ni-Fe field
   budget, port/datum, and connector retention.
5. `G05-05`: freeze continuous duty duration, ramp, cycle count, pressure/outgassing acceptance,
   magnetic perturbation budget, and handling/proof-load envelope.
6. `G05-06`: inspect the live board source for J1 shell/GND1 and net-specific digital fanout; resolve
   the bench amplitude anomaly before using measured sensitivity.
7. `G05-07 HOLD - DO NOT FABRICATE CERAMIC`: obtain drawing-specific zirconia vendor redlines,
   fired tolerances, minimum features, processes, and 1/3/10-set quotes.
8. `G05-08 HOLD - DO NOT ORDER NEAR-SENSOR HARDWARE`: exact fastener/contact/conductor alloy,
   coating/underplate, magnetic permeability or screened field, and UHV cleaning declaration.

## 13. Stage acceptance check

- LCC numbering/connectivity/plating/dimension evidence: **PASS WITH PHYSICAL SIGN-OFF GATE**.
- Wirebond/dissimilar-metal/pull qualification evidence: **PASS; CONTINUOUS-LIFE COUPONS OPEN**.
- Solder/weld/crimp/braze/terminal/contact alternatives: **PASS; EXACT JOINT NOT SELECTED**.
- Conductor/insulation/PEEK/BeCu/magnetic alternatives: **PASS; MATERIAL GATES EXPLICIT**.
- Reusable LCC technology evidence: **PASS AS CONDITIONAL; NO FALSE CATALOG SOCKET CLAIM**.
- Three-board fanout/bias/acquisition/grounding evidence: **PASS FOR STAGE 20 INPUT**.
- Zirconia process/cost-driver evidence: **PASS; VENDOR TOLERANCES/QUOTE OPEN**.
- Direct, deduplicated URLs and limitations in source ledger: **PASS**.
- Final design chosen prematurely: **NO**.

Stage 05 result: **COMPLETE WITH OPEN QUALIFICATION AND PROCUREMENT GATES**.
