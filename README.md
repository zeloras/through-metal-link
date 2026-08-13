

# through-metal-link

> English (primary) · [Русский](translations/ru/README.md) · [Deutsch](translations/de/README.md) · [Português](translations/pt/README.md) · [Español](translations/es/README.md) · [Français](translations/fr/README.md) · [Italiano](translations/it/README.md) · [Polski](translations/pl/README.md) · [Türkçe](translations/tr/README.md) · [Українська](translations/uk/README.md) · [Tiếng Việt](translations/vi/README.md) · [中文](translations/zh/README.md) · [日本語](translations/ja/README.md) · [한국어](translations/ko/README.md) · [हिन्दी](translations/hi/README.md)

An open platform for ultrasonic power and data transfer through solid metal walls — "through steel without a single hole", built with garage-grade means.

**Try it now (no hardware needed):** `python3 software/sweep-map/sweep_map.py --mock`

**Status:** stage 0 — preparation · 💰 **[$250 bounty for the first independent build](https://github.com/zeloras/through-metal-link/issues)** · shopping list: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

Docs are multilingual: English is primary and lives at the canonical paths; every other language mirrors the tree under [translations/](translations/). Edit any language — CI translates and commits the rest (see [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Stage 1 rig: Pi → DDS → half-bridge → transformer → piezo TX | steel | piezo RX → bridge → ADC → Pi" width="900"></p>

## The idea in one paragraph

Radio waves don't pass through metal (Faraday cage), and a cable penetration means a hole, a seal, and a point of failure. Ultrasound, on the other hand, travels through metal just fine: a piezo element on each side of the wall turns it into a channel for power and data. Lab literature already proved the physics at serious levels (RPI: 50 W + 12 Mbit/s through 63.5 mm of steel; NASA JPL: up to ~kW through 5 mm of titanium) — those are existence proofs with specialized hardware, not this repo's garage BOM. The foundational patents have expired, and no open, reproducible platform exists yet — this repository is building one, starting at **watts-class power and kbit/s data through 3–5 mm steel** once stage 2 is measured.

## Roadmap

| Stage | Deliverable | Success criterion | Expectation |
|---|---|---|---|
| 1. Sweep map | frequency response of the "Langevin–3 mm steel–Langevin" channel | pair resonance found, plot in [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. Watts | power into the load at resonance | ≥0.5 W through 3 mm of steel, protocol in [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](docs/img/sim4-power-budget.png) |
| 3. Data | FSK/OOK over the same pair | ≥1 kbit/s error-free | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. Node | ESP32 + sensor in a welded-shut box, powered and telemetered by sound alone | ≥1 h of autonomous operation | [sim4](docs/img/sim4-power-budget.png) |
| 5. Publication | repo goes public, article/how-to | reproduction by a third party | — |

## Repository map

Every block below expands: inside is a digest sufficient to work from, plus a link to the full document.

<details>
<summary><b>🛒 From zero to a working rig: what to buy and in what order</b> — <a href="QUICKSTART.md">QUICKSTART.md</a></summary>

**Budget:** ~$210 minimum, ~$300 comfortable (knock off ~$120 if you already own a Pi, a soldering iron, and a bench power supply). Three baskets: tools (~$120), rig electronics (~$70, [full BOM](hardware/bom/bom-stage1.csv)), mechanics (~$20). Optional but strongly recommended: a USB oscilloscope (~$60–80).

**Critical path — AliExpress shipping (3–4 weeks):** order the electronics on day one. Key decision: buy **4 Langevin transducers from the same batch** — the sweep will pick the best pair ([why](docs/img/sim2-pair-mismatch.png)).

**While it ships:** dry-run the pipeline with no hardware —

```bash
python3 software/sweep-map/sweep_map.py --mock
```

**Done when (by stage):** stage 1 — sweep peak reproduces across two runs to within <200 Hz ([experiments/001](experiments/001-sweep-map-3mm-steel/README.md)); stage 2 — ≥0.5 W into a known load through 3 mm of steel and an LED lit from the RX side ([experiments/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Theory in a minute</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

The piezo TX is pressed against the wall and drives a longitudinal wave into it; the piezo RX on the other side turns it back into electricity. Speed of sound in steel: ~5900 m/s.

Two operating modes:

| Mode | Frequency | Resonance set by | Yields | Status |
|---|---|---|---|---|
| **A** — Langevin transducers | 40 kHz | the transducer pair (wall ≪ λ — a "membrane") | watts, kbit/s | starting mode (stages 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — discs | 0.6–1 MHz | thickness resonance of the wall ([comb](docs/img/sim3-thickness-comb.png)) | hundreds of mW, hundreds of kbit/s | branch after the first watts; needs automatic frequency tracking |

The main losses: resonance mismatch within the pair (±1 kHz for cheap Langevin transducers), acoustic contact quality (epoxy > grease couplant + clamp > dry pressure), misalignment, resonance drift with temperature. The answer to all of them is the same: **a sweep map before every change to the setup**.

</details>

<details>
<summary><b>📈 What the rig should show: expectation plots from the simulator</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

A semi-empirical channel model (not FEM, **not lab data** — intuition for "what the sweep should look like and what to aim at"). Assumptions are explicit in `channel_sim.py` (loaded Q≈40, contact k-factors, chain η≤40%). Regenerate with: `python3 channel_sim.py --out ../../docs/img`.

**Stage 1 — sweep.** A narrow peak near ~40 kHz; the model’s placeholder contact multipliers are grease:dry:gap = 1 : 0.25 : 0.02 (i.e. grease ≈4× dry and ≈50× air gap). No peak means a problem with the contact or the pair:

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**Why 4 Langevin transducers, not 2.** Under Q≈40, a 1.5 kHz resonance mismatch within the pair drops model power ~10×:

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**Stage 3 — data.** OOK runs into resonator ringing (model Q~40 → τ≈0.3 ms): 1 kbit/s is clean, at 5 kbit/s the eye is closed. Going faster takes mode B:

<img src="docs/img/sim5-ook-datarate.png" width="720">

**Receiver power budget.** Shaded bands are **targets** (mode A 0.5–5 W if stage 2 lands; mode B lower). Realistic first loads are duty-cycled ESP32 / BLE / LED; Wi-Fi is shown as a peak-draw marker, not a continuous promise:

<img src="docs/img/sim4-power-budget.png" width="720">

**For later (mode B).** The plate turns transparent at a comb of thickness resonances — the frequency has to be tracked:

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Safety — read before first power-up</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Tens to hundreds of volts on the piezo** once the stage-2 driver is online — the TVS on the receive side goes in BEFORE the first powered run; keep your hands off the leads.
2. **Mains** — only through a bench power supply / isolation; ultrasonic-cleaner driver boards are galvanically tied to the mains.
3. **Ears** — at non-trivial power, operate transducers pressed against metal; never run high-power airborne ultrasound without an enclosure.
4. **Heat** — an unclamped Langevin transducer overheats in minutes at power; clamp before raising current (brief low-current electrical bring-up only — see driver README).
5. **Shards** — piezoceramic is brittle: an overtightened bolt or an impact means shards; wear safety glasses for any mechanical work.

First driver power-up: bench supply current limit 0.2 A; full sequence in [hardware/driver/](hardware/driver/README.md) and [docs/02-safety.md](docs/02-safety.md).

</details>

<details>
<summary><b>🧭 Prior art and patent hygiene</b> — <a href="docs/01-prior-art.md">docs/01-prior-art.md</a></summary>

Every technical decision must trace back to a "free" source (expired patents, papers). The foundation: **US5982297** (Aerospace Corp — the basic recipe for a through-wall piezo pair), **US7902943** (Caltech/JPL — Sherrit's feed-through), **US9361877** (Univ. Oklahoma — a complete transceiver system); all dead. Key papers: Lawry 2013 (50 W + 12.4 Mbit/s through 63.5 mm of steel), Sherrit/NASA (a 100 W lamp), Yang 2015 (survey).

Not to be copied while still alive (US-only, until ~2032; stages 1–4 don't need it): RPI's OFDM allocation, RPI's full-duplex scheme, Drexel's conformal transducers.

Architecture decisions are recorded in [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md) (ADR).

</details>

<details>
<summary><b>🔌 Hardware and firmware</b> — hardware/, firmware/</summary>

- [hardware/bom/bom-stage1.csv](hardware/bom/bom-stage1.csv) — stage 1 shopping list.
- [hardware/schematics/](hardware/schematics/README.md) — **circuit schematics** (generated from code): driver, receiver, Pi pinout, harvester node.
- [hardware/driver/](hardware/driver/README.md) — TX driver: IR2110 half-bridge + 2×IRF540, matching transformer (a Langevin transducer is a capacitive load!). KiCad board comes after the breadboard prototype checks out.
- [hardware/receiver/](hardware/receiver/README.md) — receiver, stage by stage: Schottky bridge → ADC (stage 1) → load (stage 2) → LTC3588 + supercapacitor + ESP32 (stage 4).
- [firmware/node-esp32/](firmware/node-esp32/README.md) — stage 4 node (stub): deep sleep, sensor readout, BLE advertising, budget of 1–5 mW average.

</details>

<details>
<summary><b>💻 Software: measurements and the simulator</b> — software/</summary>

- [software/sweep-map/sweep_map.py](software/sweep-map/sweep_map.py) — the stage 1 workhorse: DDS sweep → ADC readings → CSV + frequency-response plot. Has `--mock` for a run without hardware. On the Pi: `raspi-config` → enable SPI and I2C; `pip install spidev smbus2 matplotlib`.
- [software/simulator/channel_sim.py](software/simulator/channel_sim.py) — generator of the expectation plots (`pip install numpy matplotlib`).
- [data/](data/README.md) — raw logs; CSV/PNG stay out of git, only curated plots go into git inside the experiment's directory.

</details>

<details>
<summary><b>🗺️ Where to apply this: barriers, channels, niches</b> — [docs/04-hybrid-channels.md](docs/04-hybrid-channels.md), <a href="docs/05-applications-map.md">docs/05</a></summary>

There is no universal channel — the platform matches the physics to the barrier: piezo-acoustics (primary: steel/aluminum with contact — watts and kbit/s), EMAT (dirty/hot metal, no contact — data), low-frequency magnetics (vacuum sandwich walls of dewars — bits/s). Honest dead ends: rubber-lined/composite walls, bubbling liquid in the path.

Niche priority: **(1)** lab vacuum chambers and cryostats — the open-source-hardware audience, no certifications; **(2)** fermentation tanks — a proving ground within walking distance; **(3)** sealed battery packs — the flagship case (thermal-runaway detection without a penetration into the pack). The receiver discovery and auto-tuning protocol (a Qi analog): [docs/03-discovery-protocol.md](docs/03-discovery-protocol.md).

</details>

<details>
<summary><b>📁 Directory layout</b></summary>

```
docs/            theory, prior art, safety, applications, decision log (ADR)
docs/img/        expectation plots (generated by software/simulator/channel_sim.py)
hardware/        BOM, driver (half-bridge), receiver (rectifier/harvester)
firmware/        node firmware (ESP32 — stub until stage 4)
software/        measurement scripts (frequency-response sweep map) and channel simulator
experiments/     experiment protocols — from the template, one directory = one experiment
data/            raw logs (large files stay out of git)
```

</details>

## Principles

1. **Reproducibility from zero.** Anyone with a soldering iron and ~$210 can reproduce the result from this repo alone.
2. **Every experiment is a protocol.** No "it kind of worked": [experiments/TEMPLATE.md](experiments/TEMPLATE.md) is mandatory.
3. **Patent hygiene.** We build on the expired layer ([docs/01-prior-art.md](docs/01-prior-art.md)); decisions are recorded in [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md).
4. **Measurement first, opinion second.** A sweep map before any conclusions about the channel.

## Licenses and patents

Code — Apache-2.0, hardware — CERN-OHL-W v2, documentation — CC-BY-4.0; full texts in [LICENSES/](LICENSES/). Anyone may fork and build on this, commercially included; patent protection comes from the grants and retaliation clauses in the licenses plus a prior-art strategy. The full scheme and the defensive-publication protocol: [LICENSES.md](LICENSES.md); contribution rules: [CONTRIBUTING.md](CONTRIBUTING.md).
