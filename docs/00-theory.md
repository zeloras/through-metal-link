# Channel theory (the minimum you need to work)

> English (primary) · [Русский](../translations/ru/docs/00-theory.md) · [Deutsch](../translations/de/docs/00-theory.md) · [Português](../translations/pt/docs/00-theory.md) · [中文](00-theory.md) · [日本語](../translations/ja/docs/00-theory.md)

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
- **A (40 kHz, Langevin transducers).** A 3–5 mm plate ≪ λ — it behaves as a membrane; the resonance is set by the transducer pair, not by the wall. Simpler and more powerful than mode B — the one to start with. Lab existence proof (not a garage target): NASA JPL ~24.5 kHz, hundreds of W up to a kW through 5 mm Ti with purpose-built hardware.
- **B (0.6–1 MHz, discs).** Thickness resonance of the wall itself, and a sharp one (a ~6% frequency shift ⇒ transmission drops ~10× in the Fabry–Perot model). The RPI/Moss class of results: hundreds of mW plus data at hundreds of kbit/s under lab bonding and matching. Requires automatic frequency tracking.

## Main losses
Resonance mismatch within the transducer pair (cheap Langevin transducers spread ±1 kHz), quality of the acoustic contact (epoxy > thick grease couplant + clamp > dry pressure), misalignment, resonance drift with temperature. The answer to all of it is the same: run a sweep map before every change to the setup.

## Effect on the wall and the media behind it

Short version: at platform power levels the wall and any gas behind it are untouched. A liquid behind the wall mostly affects *the channel*; the channel only starts affecting *the liquid* near the cavitation threshold. Ballpark numbers below are for mode A: 40 kHz, ~1 W/cm² into 3 mm steel.

**Wall — no deformation, no fatigue, ever.** Particle velocity v = √(2I/ρc) ≈ 21 mm/s ⇒ displacement ≈ 80 nm, plane-wave strain ε = v/c ≈ 3.5·10⁻⁶. Two equivalent stress ballparks: elastic E·ε ≈ 0.7 MPa (E ≈ 200 GPa) and acoustic p = Z·v ≈ 1.0 MPa (Z_steel ≈ 4.6·10⁷ Pa·s/m). Steel yields at 250+ MPa and its fatigue endurance limit is ~200 MPa — still a >200× margin either way, and below the endurance limit steel takes unlimited cycles. The mechanically fragile parts are elsewhere: the piezo ceramic (brittle, depoles when overheated) and the bond line (epoxy heats up and fatigues first) — see [02-safety](02-safety.md).

**Gas behind the wall — zero effect.** The steel→air impedance mismatch (~4.6·10⁷ vs ~400 Pa·s/m) transmits a fraction of order 10⁻⁵ of the power. No measurable heating or agitation; electronics inside a sealed box don't notice nm-scale wall motion.

**Liquid behind the wall — two directions:**

- *Liquid → channel (always).* Water loads the far face with ~1.5 MRayl instead of air: part of the power radiates into the liquid, Q drops, the sweep peak shifts and broadens. Mode B is hit hardest — the thickness-resonance comb is computed for steel–air boundaries and moves with liquid loading. The standing rule covers this: **re-sweep against the real, full vessel**, never trust a sweep taken against an empty one. Side benefit: liquid damping shortens resonator ringing (τ), so the OOK eye opens at higher bitrates. Bubbles in the path (fermenting liquid!) scatter strongly — see the workaround in [04-hybrid-channels](04-hybrid-channels.md).
- *Channel → liquid (only at high power).* Peak pressure radiated into water: p ≈ ρc·v ≈ 1.5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0.3 atm. The inertial-cavitation threshold at 40 kHz in ordinary (gassy) water is ~1–2 atm, so at 1 W/cm² the margin is 3–10×. But p grows as √power, and standing waves in a closed vessel create local hot spots — tens of W/cm² continuous into a liquid-filled tank can reach the threshold. Crossing it means CO₂ degassing, sonochemistry (off-flavors in food products), and long-term cavitation erosion of the inner surface (exactly how ultrasonic cleaners clean). Practical ceiling for continuous power into liquid-backed walls: **≲1 W/cm²**. Mode B is exempt: at MHz the threshold is an order of magnitude higher and the powers are hundreds of mW.

## Receiver power budget (ballpark)
LED 20 mW; ESP32 duty-cycled 1–5 mW average; BLE radio ~150 mW while the radio is on. Buffer: a 1 F supercapacitor @ 3.3 V stores E = ½CV² = 5.4 J. How many transmissions that buys depends on on-air time: a short BLE advertising event (~2–5 ms at ~150 mW) is only ~0.3–0.8 mJ → on the order of **10⁴ packets** from a full cap; a long connection / burst (~100 ms radio-on) is ~15 mJ → on the order of **10² bursts**. Average draw still has to stay inside the harvested watts (stage-2 target ≥0.5 W into the load is the gate; until that is measured, treat multi-watt mode-A bands on the simulator plots as targets, not data).
