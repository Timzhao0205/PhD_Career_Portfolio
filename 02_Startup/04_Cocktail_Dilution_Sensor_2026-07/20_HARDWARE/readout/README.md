# Readout chain — Phase 0

FDC2214EVM (B01):
- 4 channels: ch0-2 = three pitch coupons, ch3 = sealed reference
  coupon in air (common-mode/temp drift ref).
- Keep coupon-to-EVM leads <10 cm shielded twisted pair; parasitic
  cable C is the enemy. Later revisions put the FDC die in the probe.
- Bench flow: TI GUI -> CSV streaming for P0-E0/E1; then XIAO
  (30_FIRMWARE) reads FDC2214 over I2C and streams USB-serial/BLE for
  dynamic runs.

NTC divider: 10k NTC + 10k 0.1% fixed, 3.3 V, into XIAO ADC; Beta
from datasheet, verify against calibrated thermometer at 3 points
(ice bath / room / warm water).

Contingency: EVAL-AD7746 (B19) if FDC SNR insufficient — mind the
+/-4 pF input range; needs series/guard capacitance scheme.
