# Source Notes - R&D Strategy

Date checked: 2026-07-09

These links were used to ground tool and component claims in
`RD_STRATEGY_2026-07.md`.

## Capacitive Readout

- Texas Instruments FDC2214 product/datasheet family:
  https://www.ti.com/product/FDC2214
- Texas Instruments FDC2214EVM:
  https://www.ti.com/tool/FDC2214EVM

Relevant strategy use:

- FDC2214/FDC2x1x are high-resolution multichannel capacitance-to-digital
  converters.
- The EVM is intended for flexible capacitive-sensing prototyping.
- The project should model the external LC tank and parasitics rather than
  pretending LTspice can reproduce the full digital converter behavior without
  a validated vendor macromodel.

## Microcontrollers

- Seeed Studio XIAO nRF52840 Sense product page:
  https://www.seeedstudio.com/Seeed-XIAO-BLE-Sense-nRF52840-p-5253.html
- Seeed Studio XIAO nRF52840 wiki:
  https://wiki.seeedstudio.com/XIAO_BLE/
- Raspberry Pi Pico documentation:
  https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
- Raspberry Pi Pico 2 product page:
  https://www.raspberrypi.com/products/raspberry-pi-pico-2/
- Raspberry Pi Bluetooth support note for Pico W:
  https://www.raspberrypi.com/news/new-functionality-bluetooth-for-pico-w/

Relevant strategy use:

- XIAO nRF52840 Sense is a strong default for Phase 1 because the project
  needs BLE plus onboard IMU for motion/strike gating.
- Pico W/Pico 2 W are useful bench alternatives, especially where Wi-Fi,
  MicroPython, or extra compute matter, but they require an external IMU for
  this sensor concept.

## EDA / Simulation Tools

- Analog Devices LTspice:
  https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html
- KiCad main site:
  https://www.kicad.org/
- KiCad 9 getting started documentation:
  https://docs.kicad.org/9.0/en/getting_started_in_kicad/getting_started_in_kicad.html
- KiCad 9.0 release note:
  https://www.kicad.org/blog/2025/02/Version-9.0.0-Released/

Relevant strategy use:

- LTspice is suitable for support-circuit simulation: NTC divider, LC tank,
  leakage/parasitics, and power integrity.
- KiCad is suitable for schematic, PCB, ERC/DRC, and integrated SPICE workflow.

