# Wall materials beyond steel: which walls carry power and data

> English (primary) · [Русский](../translations/ru/docs/06-materials.md) · [Deutsch](../translations/de/docs/06-materials.md) · [Português](../translations/pt/docs/06-materials.md) · [Español](../translations/es/docs/06-materials.md) · [Français](../translations/fr/docs/06-materials.md) · [Italiano](../translations/it/docs/06-materials.md) · [Polski](../translations/pl/docs/06-materials.md) · [Türkçe](../translations/tr/docs/06-materials.md) · [Українська](../translations/uk/docs/06-materials.md) · [Tiếng Việt](../translations/vi/docs/06-materials.md) · [中文](../translations/zh/docs/06-materials.md) · [日本語](../translations/ja/docs/06-materials.md) · [한국어](../translations/ko/docs/06-materials.md) · [हिन्दी](../translations/hi/docs/06-materials.md)

The rest of this repo assumes steel. This page asks the simpler, bigger question: **for which wall materials does the two-transducer channel work at all**, and in which mode? It is a simulation study (`--mock`-style, no lab data — intuition for what deserves a hardware experiment), built from the same semi-empirical model as [channel_sim](../software/simulator/channel_sim.py) and extended with bulk absorption.

Generate: `python3 software/simulator/material_map.py` (needs numpy + matplotlib). Model and assumptions: [../software/simulator/material_map.py](../software/simulator/material_map.py).

## The model in one minute

Three quantities decide whether a wall is usable at all, and for how much power:

1. **Impedance contrast and phase** — the lossless Fabry–Perot slab model, identical to [channel_sim](../software/simulator/channel_sim.py):
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_wall / Z_couplant, couplant Z = 1.5 MRayl (grease).
   At a half-wave resonance (f = c/2d) a lossless symmetric slab is fully transparent *regardless of r*; the contrast r sets how **wide** the comb teeth are (tolerance to frequency error), the sound speed c sets how far apart they are (Δf = c/2d).
2. **Bulk absorption**, invisible to the lossless model and the decider for plastics, concrete and rubber:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, one-way, longitudinal],
   where α₁ₘₕᶻ is the 1 MHz value.
   γ ≈ 1 = viscous/relaxation loss; γ > 2 = scattering off inhomogeneities (concrete aggregate).
3. **The dose the wall takes back** — see the section [below](#the-dose-what-the-wave-does-to-the-wall-frequency-by-frequency): stress σ = √(2·I·Z), which does *not* depend on frequency, and self-heating ΔT ∝ α(f)·I, which does.

**Assumptions, stated where the code states them:** typical handbook properties (longitudinal wave, ~20 °C); real stocks vary — grain, fillers, aggregates, cure. Everything below is a ranking, not a datasheet.

| Wall | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | comb Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | note |
|---|---|---|---|---|---|---|---|---|
| steel | 7850 | 5900 | 46.3 | 0.02 | 590 | 148 | 0.21 | fine-grained structural |
| aluminum | 2700 | 6320 | 17.1 | 0.02 | 632 | 158 | 0.69 | 6061-class |
| titanium | 4430 | 6100 | 27.0 | 0.03 | 610 | 152 | 0.45 | Ti-6Al-4V |
| copper | 8960 | 4760 | 42.6 | 0.05 | 476 | 119 | 0.17 | dense, very high Z |
| borosilicate glass | 2230 | 5640 | 12.6 | 0.01 | 564 | 141 | 0.77 | very low loss |
| alumina ceramic | 3890 | 9900 | 38.5 | 0.08 | 990 | 248 | 0.51 | fast sound, low loss |
| PMMA (acrylic) | 1180 | 2690 | 3.2 | 2.5 | 269 | 67 | 0.95 | transparent, absorption-limited at MHz |
| PVC (rigid) | 1400 | 2380 | 3.3 | 6 | 238 | 60 | 0.92 | lossier than PMMA |
| HDPE | 950 | 2340 | 2.2 | 12 | 234 | 58 | 0.98 | soft, lossy |
| concrete | 2300 | 3500 | 8.1 | 5 | 350 | 88 | 0.77 | aggregate scattering dominates; varies by orders of magnitude |
| rubber (filled) | 1100 | 1500 | 1.6 | 60 | 150 | 38 | 0.85 | the honest dead end |

## The plots

**Mode B (MHz) — the thickness comb per material.** Left: structural metals; right: non-metals. All walls 5 mm, grease coupling. Lossless-model peaks reach T = 1 at exact resonances; real peaks are lower by contact losses, and absorption caps the lossy materials outright:

<img src="img/mat1-thickness-comb-materials.png" width="880">

**The material map** — the two axes that decide everything: impedance (coupling/contact difficulty) vs 1 MHz absorption (MHz viability). High-Z + low-α is the power-grade corner; low-Z + high-α is "40 kHz still open, MHz dead"; the rubber corner is a dead end at every frequency we target:

<img src="img/mat2-material-map.png" width="720">

**Mode A (40 kHz) coupling proxy** — the same transmission model evaluated at 40 kHz through a 3 mm wall, normalized to steel. *A ranking, not watts:* the resonant Langevin pair multiplies every bar roughly equally and the model has no transducer loading inside; that multiplier is stage-2 territory ([experiments/002](../experiments/002-watts-3mm-steel/README.md)):

<img src="img/mat3-modea-coupling-materials.png" width="720">

## What the sweep says

- **At 40 kHz, low-Z walls (plastics, rubber lining) couple *more easily* than steel** — through grease they are almost impedance-matched, so the comb is broad and transmission per pass is high. What kills plastics at higher frequencies is **bulk absorption**, not contact or impedance. The material ladder at 40 kHz is therefore inverted vs intuition: HDPE/PMMA/PVC > glass/concrete > aluminum > alumina > titanium > steel > copper — with the strong caveat that the rubbers' 40 kHz number extrapolates α linearly down from 1 MHz, which viscoelasticity does not guarantee.
- **Mode B divides materials cleanly.** Metals, glass and alumina take MHz with negligible absorption (α ≤ 0.1 dB/cm); the comb is *sharp* for high-Z walls (steel, alumina — needs frequency tracking, the ~6% ⇒ ~10× lesson of [00-theory](00-theory.md)) and *wide* for glass/PMMA (tolerant, but PMMA pays ~1.3 dB one-way at 1 MHz through 5 mm — mW-class only).
- **Concrete is a 40 kHz material, not a MHz one.** Aggregate scattering (λ at 1 MHz ≈ 3.5 mm ≈ aggregate size) throws γ up to ~2.5 and kills MHz; ultrasonic pulse-velocity practice (40–80 kHz through ≥1 m paths) is exactly mode A.
- **The battery-pack niche ([05](05-applications-map.md)) is acoustically favorable:** a 2–3 mm aluminum wall has a coupling proxy ~3× steel's and negligible absorption — the flagship case is also the easy case.
- **The frequency ladder to plan for in mode B** (5 mm wall, first comb): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, copper ≈ 480, steel ≈ 590, titanium ≈ 610, aluminum ≈ 630, glass ≈ 560, alumina ≈ 990. Thinner wall ⇒ proportionally higher.

## The dose: what the wave does to the wall, frequency by frequency

Transmission answers "how much gets through"; this section answers the reverse question — **how much of the wave stays in the wall, and does that hurt it?** Wave-in-wall harm has exactly two faces:

- **Stress** σ = √(2·I·Z) — plane-wave momentum; *frequency-independent*. Compare against the high-cycle fatigue limit (metals), flexural/tensile strength (ceramics, glass, concrete, rubber).
- **Self-heating** ΔT = α(f)·I·d²/(8k), steady state, both faces cooled — *frequency-dependent* through α(f), and that is where frequency bites: every insulating material has a knee above which each extra octave of frequency multiplies the deposited heat.

At 1 W/cm² (already beyond what this project targets: the stage-2 goal of 0.5–5 W spread over a ~19 cm² transducer face is 0.03–0.26 W/cm²):

| Wall | σ @1 W/cm², MPa | limit σ_e, MPa | stress margin | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | ceiling @40 kHz, W/cm² | ceiling @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| steel | 0.96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| aluminum | 0.58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| titanium | 0.74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| copper | 0.92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| borosilicate glass | 0.50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| alumina ceramic | 0.88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (acrylic) | 0.25 | 15 | 60× | 0.2 | 9.5 | 65 | ~100 | 2.1 |
| PVC (rigid) | 0.26 | 15 | 58× | 0.6 | 28.8 | 199 | ~33 | 0.7 |
| HDPE | 0.21 | 8 | 38× | 0.15 | 19.2 | 215 | ~58 | 1.0 |
| concrete | 0.40 | 2.5 | 6× | ~0 | 2.1 | 118 | 1.6 | 1.6 |
| rubber (filled) | 0.18 | 1.5 | 8× | 11.5 | 288 | 1440 | 1.7 | 0.07 |

"Ceiling" = continuous intensity at which the wall stays inside 20% of its fatigue/strength limit and under +20 K of self-heating (steady state, both faces held at ambient). Duty-cycled runs heat less; a wall anchored on only one face — the usual case, air on one side — heats up to 4× more at the free face. These numbers are a first cut, not a design guarantee. One convention callout: the α values are intensity-dB (10·log₁₀, the dosimetry convention — a 3 dB drop halves I); pulse-echo NDT literature quoting amplitude-dB (20·log₁₀) describes the SAME α with numbers twice as large — check which convention a source uses before copying its numbers into this table.

<img src="img/mat4-harm-materials.png" width="920">

What the dose sweep says:

- **The steel verdict of [00-theory](00-theory.md) holds and generalizes**: every structural metal carries 1 W/cm² with margins of 65–680× in stress and micro-kelvins of self-heating. Metals are frequency-insensitive in harm terms — their loss is too small to heat at any power we can couple.
- **Frequency harm on polymers is thermal, not mechanical.** PMMA's stress margin is a comfortable 60× even at 1 W/cm², but the heating knee sits right around 1 MHz: benign (~0.2 K) at 40 kHz, +9.5 K at 1 MHz, +65 K at 5 MHz — softening territory at a few W/cm². PVC crosses the +10 K line already at ~0.35 W/cm² @ 1 MHz; rubber absorbs ~288 K per W·cm⁻² at 1 MHz (and ~12 K even at 40 kHz) — hysteretic heating is *the* reason elastomer-lined walls die, not the comb. HDPE splits the difference and remembers its melt point: +215 K per W·cm⁻² at 5 MHz.
- **Concrete's tight margin is tensile, not thermal**: 0.40 MPa wave stress against a ~2.5 MPa static tensile strength (fatigue lower still) leaves only a ~6× margin at 1 W/cm². The 40–80 kHz regime stays fine at the project's power density; concentrated multi-W/cm² beams into concrete should be avoided, MHz doubly so (scattering heats the aggregate interfaces).
- **Bottom line for the roadmap:** at mode-A power densities (≤0.3 W/cm²) no solid in the table is endangered — stress margins ≥11× (the tightest is concrete's tensile fatigue at 11×; everything else ≥15×) and heating ≤0.2 K for every engineered solid (rubber, the exception nobody targets, ~3.5 K). The harm map justifies the project's plan to escalate power: the first real material limits appear *above* the stage-2 targets, first in liquids (cavitation, the ≤1 W/cm² rule of [00-theory](00-theory.md)), then in concrete's tensile fatigue, then in polymers at MHz. The parts that actually need watching at high power remain the piezo ceramic and the bond line — [02-safety](02-safety.md) — not the wall.

## Verdict per material

| Wall | Mode A — 40 kHz power | Mode B — MHz power/data | Verdict |
|---|---|---|---|
| steel | ✓✓ reference | ✓ sharp comb — track frequency | the baseline |
| aluminum | ✓✓ (proxy ~3× steel) | ✓ sharp-ish comb | best structural wall (batteries!) |
| titanium | ✓✓ | ✓ sharp-ish, low loss | corrosive/hot niches, drones, hulls |
| copper | ✓ (hardest coupling of metals) | ✓ | niche: sealed busbars/electrochemical cells |
| borosilicate glass | ✓✓ | ✓ widest comb — most forgiving | lab windows, viewports |
| alumina ceramic | ✓✓ | ✓ fastest combs (990 kHz @ 5 mm), low loss | hot/insulating process walls |
| PMMA | ✓ broadband | ⚠ mW-class ≤ ~0.5 MHz only | tanks, enclosures; not a power wall at MHz |
| PVC / HDPE | ✓ thin walls | ✗ absorption | low-grade enclosures, data-light nodes |
| concrete | ✓ 40–80 kHz (UPV practice) | ✗ scattering | foundations, pipes — mode A only |
| rubber (filled) | ⚠ model extrapolation unvalidated | ✗ | empirically the dead end — [04](04-hybrid-channels.md) |

A low-Z plastic wall has more headroom for *misalignment-tolerant* mode-A links but delivers less absolute power headroom against absorption once you go above ~200 kHz; measure before promising anything.

## Concrete with rebar — the multilayer case

Real concrete is never plain: reinforcement mats sit at a cover depth, and the 1D single-slab model above cannot see them. `chart_rebar` / `rebar_table` extend the model to general stacks ([`stack_transmission`](../software/simulator/material_map.py), exact multilayer recursion with per-layer absorption, guarded in the self-check). Modeled geometry: a 150 mm structural wall, one steel mat of planar-equivalent thickness Ø16 mm at 40 mm cover; the *planar* model is the worst case — a real rod shadows only the part of the beam it intersects, so think of these as envelope dips, not predictions:

| Stack (150 mm concrete) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| plain 150 mm | 0.135 | 0.133 | 8.9e-09 |
| rebar Ø16 @ 40 mm | 0.013 | 0.069 | 6.6e-09 |
| two mats Ø16 @ 40 mm | 0.003 | 0.001 | 5.1e-09 |

<img src="img/mat5-rebar.png" width="880">

What the stack model says:

- **One planar mat under the beam costs ×10 at exactly 40 kHz** (stop-band interference from the steel layer), but the dip is narrow: at 100 kHz the same stack loses only ×2. The practical reading for the pipeline/autoclave niche: *a frequency scan around 40–120 kHz, not a fixed frequency*, is what gets a mode-A link past reinforcement — and the dips move with cover depth, so a scan also fingerprints the geometry (the basis of a rebar-depth estimate).
- **A second mat (a mesh) is close to a wall-killer in this worst case** (×45 down and broadband-flat near 40–100 kHz): dense reinforcement in the path is the honest "pick another spot on the wall" indicator, not a signal-processing problem.
- **Mode B through structural concrete is dead with or without rebar** (1e-8 level at 1 MHz: 5 dB/cm × 15 cm). Rebar never even enters the story at MHz.
- Caveats, in order of importance: planar-layer assumption (worst case — a Ø16 rod blocks well under half of a 40–50 mm beam's cross-section), wave-parallel-to-rebar axis assumed, and 1D propagation (no diffraction around the bar). The right hardware experiment is a scanning rig on a real slab: map T(x, y) at 40/80/120 kHz over a rebar grid and fit the planar model's dip positions to the grid pitch.

## What a hardware follow-up should measure

Before trusting any specific plate: two-thickness method per material (two plates of d and 2d at the same contact) to extract real α(f) and c — that single dataset replaces every row of the table above. Natural bonus passes inside the existing protocols: repeat the experiment [001](../experiments/001-sweep-map-3mm-steel/README.md) sweep on a 5 mm PMMA plate, a borosilicate or 99% alumina plate, and a concrete block of known grade; expect a *lower but broader* peak for the plastics, a sharp comb for the ceramics, and a temperature-sensitive contact everywhere. During the experiment [002](../experiments/002-watts-3mm-steel/README.md) power run, strap an IR thermometer (or a fine thermocouple) to the far face of each wall type — the measured ΔT at known input is the one number that validates or kills the heating column of the dose table. Nothing in this page is measured — it is the map of what to measure first.