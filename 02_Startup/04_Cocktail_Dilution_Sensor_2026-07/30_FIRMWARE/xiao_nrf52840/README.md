# XIAO nRF52840 Sense firmware — scope (Phase 1)

Not started; Phase 0 uses the TI GUI. When P0-E0/E1 pass:
1. I2C driver for FDC2214 (4 ch continuous, max rate).
2. NTC ADC sampling @ 20 Hz with Beta conversion.
3. LSM6DS3 IMU @ 104 Hz -> stir/strike/idle classifier (thresholds
   from P0-E3 data).
4. Framed binary stream over USB-serial (dev) and BLE NUS (product).
5. On-device v0 estimator only AFTER the Python reference in
   50_ANALYSIS is validated — firmware ports, never invents, math.
Toolchain: Arduino/PlatformIO nRF52 core (decide at Phase-1 start;
log in DECISIONS.md).
