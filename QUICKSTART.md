# QUICKSTART: from absolute zero to the stage 1–2 test rig

> English (primary) · [Русский](QUICKSTART.ru.md) · [Deutsch](QUICKSTART.de.md)

Scenario: you have nothing but a desk and some money. Everything below gets you to a working rig — "sweep map + first watts through steel". Prices are ballpark, USD.

## Basket 1 — tools (a base for years, ~$120)

| Item | Why | Price | Where |
|---|---|---|---|
| Soldering station (T12 clone) | everything | 35–50 | Ali |
| Multimeter (AN8008/UT61 class) | voltages, continuity, capacitance | 15–25 | Ali |
| Bench PSU 30V/5A with current limiting | powers the driver; the current limit is your insurance against burnt MOSFETs | 45–60 | Ali/local |
| Helping hands, solder, flux, desoldering braid, side cutters, tweezers | the small stuff you can't do without | 15 | Ali/local |
| Dupont wires + breadboard + heat-shrink | prototyping | 8 | Ali |

## Basket 2 — rig electronics (~$70)

| Item | Qty | Price | Note |
|---|---|---|---|
| Raspberry Pi (Zero 2 W is enough; 4/5 is comfier) + SD | 1 | 20–60 | the brain: sweep, logs, plots |
| Langevin transducer 40 kHz 50–60 W | **4** | 40 | buy 4 from ONE batch; we'll pick the best pair by sweep |
| AD9833 DDS module | 2 | 8 | the second one is a spare |
| IR2110 + IRF540 ×4 (or an EGS002 module) | 1 set | 10 | driver half-bridge |
| ADS1115 ADC | 2 | 4 | the Pi has no ADC of its own |
| Ferrite toroid + 0.5 mm magnet wire | 2 | 4 | matching transformer |
| Schottky bridge (SS14 ×8), supercapacitor 1F 5.5V ×2 | 1 | 4 | receiver chain |
| TVS SMBJ5.0A ×3 + SMBJ15CA ×2 | 1 | 2 | protection. DO NOT SKIMP |
| GY-LTC3588 module | 1 | 7 | harvester (stage 4, but let it ship now) |
| Resistor/capacitor assortment, LEDs | 1 | 8 | if you have nothing at all |
| Support passives: UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | pennies; full list — BOM items 11–12 |

## Basket 3 — mechanics (~$20, locally)

Steel plate 3 mm ~150×150 — 2 pcs (metal yard / laser cutting); F-style clamps ×2; thick consistent grease couplant (lithium grease); epoxy; sandpaper (to clean up the contact patch).

## Optional, but strongly recommended (~$90)

| Item | Why | Price |
|---|---|---|
| USB/handheld oscilloscope (FNIRSI/Hantek, 2 channels; you don't need ≥40 MHz of bandwidth — 10 is plenty) | see the waveform on the gate and on the piezo; saves days of driver debugging | 60–80 |
| ESP32 DevKit ×2 | stage 4 (the node behind the wall) | 8 |

**Total: bare minimum ~$210, comfortable ~$300.** (If you already have a Pi, a soldering station and a bench PSU in your stash — subtract ~$120.)

## Purchase order (the critical path is shipping)

1. Today: basket 2 from Ali (3–4 weeks shipping — it is the critical path) + the oscilloscope.
2. This week: baskets 1 and 3 locally.
3. While it ships: `raspi-config` → SPI+I2C, run `software/sweep-map/sweep_map.py --mock` without hardware (synthetic channel — the whole CSV+plot pipeline works on any computer), read docs/00–03, look at the expectation plots in docs/img and the schematics in hardware/schematics (the stage 1 build follows sch3 and sch2).

## What you will see (simulator: software/simulator/channel_sim.py → docs/img)

- `sim0-rig-sketch.png` — the whole rig in one sketch.
- `sim1-sweep-contacts.png` — sweep frequency response: a narrow peak near ~40 kHz; grease + clamp gives ~4× more than a dry press-fit and ~50× more than an air gap. No peak — the problem is the contact or the pair, see sim2.
- `sim2-pair-mismatch.png` — why 4 Langevin transducers and not 2: a 1.5 kHz resonance mismatch within a pair drops power 10×; the sweep picks the best pair out of 4.
- `sim3-thickness-comb.png` — for later (mode B, MHz): the plate is transparent as a comb of thickness resonances, so the frequency has to be tracked.
- `sim4-power-budget.png` — target watts versus the loads: mode A feeds everything up to Wi-Fi peaks, mode B feeds an ESP32 with a supercapacitor buffer.
- `sim5-ook-datarate.png` — stage 3: why OOK on Langevin transducers tops out at ~1–2 kbit/s (resonator ring-down τ≈0.3 ms), and why that is fine for a sensor node.

## Criteria for "the rig works"

1. Sweep 25–45 kHz in two consecutive runs: the peak reproduces to within <200 Hz.
2. At resonance, ≥0.5 W into a resistive load through 3 mm of steel.
3. The LED behind the plate is lit. Photo in experiments/001 — and the stage is closed.

Safety before first power-up: docs/02-safety.md (TVS on the receiver, PSU current limit at 0.2 A, never drive a Langevin transducer without clamping pressure).
