# Channel theory (the minimum you need to work)

> English (primary) · [Русский](../translations/ru/docs/00-theory.md) · [Deutsch](../translations/de/docs/00-theory.md)

## Principle
A TX piezo element pressed/glued against the wall excites a longitudinal wave in it; a piezo RX on the other side turns it back into electricity. The wall is a resonator: at thickness resonances (multiples of a half-wavelength) transmission is at its maximum.

## Key numbers
Longitudinal speed of sound in steel: ~5900 m/s.

| Steel thickness | Half-wave resonance |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Wavelength in steel: 148 mm @ 40 kHz; 5.9 mm @ 1 MHz.

## Two modes
- **A (40 kHz, Langevin transducers).** A 3–5 mm plate ≪ λ — it behaves as a membrane; the resonance is set by the transducer pair, not by the wall. The NASA JPL regime (~24.5 kHz, hundreds of W up to a kW through 5 mm Ti). Simpler, more powerful, the one to start with.
- **B (0.6–1 MHz, discs).** Thickness resonance of the wall itself, and a sharp one (a ~6% frequency shift ⇒ efficiency drops ~10×). The RPI/Moss regime: hundreds of mW plus data at hundreds of kbit/s. Requires automatic frequency tracking.

## Main losses
Resonance mismatch within the transducer pair (cheap Langevin transducers spread ±1 kHz), quality of the acoustic contact (epoxy > thick grease couplant + clamp > dry pressure), misalignment, resonance drift with temperature. The answer to all of it is the same: run a sweep map before every change to the setup.

## Receiver power budget (ballpark)
LED 20 mW; ESP32 duty-cycled 1–5 mW average; BLE packet ~150 mW peak — buffer: a 1 F supercapacitor @ 3.3 V = 5.4 J ≈ 360 transmissions.
