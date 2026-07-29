# G04 — Industrial Process Electrification Beyond RF/Induction

## Landscape
About 70% of global industrial energy use is heat/steam. Heat pumps and electric boilers already
cover roughly 0-350°C; >350°C (lime/cement calcination ~900-1250°C, clinkering ~1450°C, steel
reheat, chemicals) is this lane's electrification frontier. Three product families compete for
it: direct resistive/radiant systems (mature MV resistive elements cap near 600-1000°C; Coolbrook's
rotating dynamic heater reaches 1700°C) for >1000°C process heat; discharge power stages that turn
brick/particle/molten-salt thermal batteries (e.g., Rondo, 2-100+ MWth modules) into on-demand
steam/hot air; and extreme-temperature-lift heat pumps (MAN/Everllence, SPH Sustainable Process
Heat) pushing compression cycles past 100 K lift for 150-300°C steam. Ultrasonic and UV process
intensification are smaller but real standalone-product categories. China anchors global demand:
~2.5 Bt/yr cement output produces ~1.2 Bt CO2/yr, 90% from clinker calcination, within an
industrial sector that is ~two-thirds of national emissions.

## Pains & buyers
Plant owners (cement: Conch, CNBM, Heidelberg, Holcim; chemicals/pharma/food processors) fund
process-heat capex/opex; IEA cites unfavorable electricity:gas price ratios and multi-year
grid-connection queues as top deployment barriers. Kiln/furnace OEMs (FLSmidth, thyssenkrupp) and
EPCs want retrofit-compatible power/control modules, not full-plant rebuilds. Utilities and
governments co-fund flagship projects: RheinEnergie paid MAN/Everllence EUR 280M for a 150 MW/110°C
river-water heat-pump system (EUR 100M EU+federal grant); DOE put $43M into 16-plus cross-cutting
electrification projects (2024) under the Industrial Heat Shot (>=85% GHG-intensity cut target by
2035). Process-intensification buyers (chemicals, pharma, food/beverage, battery) still buy
ultrasonic/UV skids as bespoke-quoted capex, not catalog products — an opening for a small
standardized-product team.

## Incumbents & gaps
- **Coolbrook RDH** (Finland): to 1700°C, >90% efficiency, MoUs with Cemex/UltraTech, commercial
  launch targeted 2025+; bundled tech+EPC, not a discrete power-stage product.
- **Rondo Energy Heat Battery**: 2-100+ MWth, brick storage to 1500°C, discharge to steam/hot
  air/thermal oil/turbine, 97%+ efficiency, steam-as-a-service (~$30/MWh target, not yet hit);
  first 100 MWh unit running at a California oilfield (2025). Storage medium and discharge
  electronics are sold together — a vendor-agnostic discharge/controls product for other storage
  integrators is open.
- **MAN/Everllence + SPH Sustainable Process Heat**: turbocompressor HTHP, 60-300°C, 10-100
  MWth/unit, EUR 280M/150 MW reference project; extreme lifts (>100 K) still need bespoke
  two-stage cascades and custom piston compressors — no standardized drive-electronics line.
- **Chromalox-class MV resistive heaters**: 1-7.2 kV, ~99% efficient, mature but capped near
  600-1000°C; most US chemical plants still run legacy 480V gear — an MV-retrofit gap.
- **Dongfang Electric** (China SOE): 165°C steam from 40°C waste heat, COP 2.7, 330→890 kW
  ton-scale unit at a Fuling pharma plant (Feb 2026) — domestic incumbents climbing the <200°C
  ladder; >1000°C resistive and >150 K-lift segments are unclaimed domestically.
- **Ultrasonic**: Hielscher/Sonics (West) sell custom-quoted 0.5-16 kW sonoreactors; China's
  public ultrasonic leader SBT/骄成超声 (688392.SH) draws >50% revenue from EV-battery-tab
  welding, not chemical process intensification.
- **UV**: Excelitas/Nordson/IST Metz dominate curing (~$2.8-3.0B 2025/26, 8.3% CAGR, APAC
  fastest); Enviolet leads AOP wastewater — both adjacent, not high-temperature-process
  integrators.

## 2029 inflections
DOE's Industrial Heat Shot targets cost-competitive electrified heat by ~2035, implying a
demo-to-early-commercial transition around 2028-2031. China's national ETS is set to absorb
cement (plus steel/aluminum) around 2027, squeezing margins just as a 2029/2030 launch window
opens. The June-2025 NDRC/MIIT/NEA zero-carbon industrial-park program (first cohort chosen by
Aug 2025; multi-year 2026-2030 build-out) creates a park-level China anchor-customer channel.
McKinsey projects the large-temperature-lift heat-pump market growing >15%/yr to ~$12B by 2030,
forcing compressor/drive standardization out of today's bespoke-engineering mode. Coolbrook-class
>1000°C electric heaters moving pilot-to-commercial (2025-2027) should open a picks-and-shovels
retrofit-electronics window by 2029.

## China notes
Largest addressable calciner-electrification base globally (see Landscape stats above).
National-ETS entry for cement (~2027) and the June-2025 zero-carbon industrial-park notice
(funded via central funds, local bonds, policy-bank credit) are the near-term levers. Industrial
heat-pump electricity share is still ~4-5%, matching global averages. Dongfang Electric's
SASAC-owned HTHP unit (165°C/COP 2.7, Fuling, 2026) shows state OEMs targeting the easier <200°C
tier, leaving extreme-lift and >1000°C resistive segments open domestically. China is also the
world's fastest-growing molten-salt storage market (part of a 6.1 GW global base, end-2022) — an
existing supply chain a discharge-electronics product could plug into rather than fight.

## Opportunity seeds
1. **Vendor-agnostic discharge power-stage/controls** for brick, particle, or molten-salt
   thermal batteries: sell only the electronics converting stored heat to dispatchable
   steam/hot-air/power at the process interface, deployable across Rondo-, Antora-, EnergyNest-,
   or Chinese molten-salt-EPC storage banks. Avoids **RID-015** (the 700°C particle storage
   module itself) by never touching the storage medium — only its discharge interface.
2. **MV-rated, dust/vibration-hardened resistive-element power controller** with SiC/GaN drive
   electronics for >1000°C calciner/kiln retrofits, sold as a bolt-on to kiln OEMs (FLSmidth,
   Sinoma) rather than a full electrified-kiln EPC. Stays purely Joule/radiant resistive,
   avoiding both **N05** (RF/microwave process heat) and **C16** (induction heating) as the
   heating mechanism.
3. **Standardized compressor-drive/VFD package for extreme-lift (>100 K) industrial heat
   pumps**, targeting the 150-300°C steam band MAN/Everllence and SPH now solve with one-off
   engineering. A heat-pump power stage only, explicitly distinct from **PWR-15** (an LDES
   power-conversion skid) and **C39** (electrolyzer power modules) — no batteries, no
   electrolysis.
4. **Continuous-duty sonochemical/process-intensification ultrasonic reactor line** for
   chemicals/pharma/food, filling the space China's SBT (battery-tab-welding focused) and
   boutique Western players (Hielscher, custom/small-batch) leave open. Acoustic-cavitation
   hardware only, explicitly not the pulsed-electric-field mechanism of **N08** (industrial
   pulsed power/PEF).
5. **Vertical-specific high-temperature/corrosive-duty UV system** (post-calciner off-gas
   treatment, high-temp intermediate curing) rather than commodity curing (Excelitas/Nordson) or
   wastewater AOP (Enviolet). A UV product only, explicitly not a microwave/RF heating system
   (**N05**) or an induction variant (**C16**).
