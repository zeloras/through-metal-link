# Wall materials beyond steel: which walls carry power and data

> English (primary) · [Русский](../translations/ru/docs/06-materials.md) · [Deutsch](../translations/de/docs/06-materials.md) · [Português](../translations/pt/docs/06-materials.md) · [Español](../translations/es/docs/06-materials.md) · [Français](../translations/fr/docs/06-materials.md) · [Italiano](../translations/it/docs/06-materials.md) · [Polski](../translations/pl/docs/06-materials.md) · [Türkçe](../translations/tr/docs/06-materials.md) · [Українська](../translations/uk/docs/06-materials.md) · [Tiếng Việt](../translations/vi/docs/06-materials.md) · [中文](../translations/zh/docs/06-materials.md) · [日本語](../translations/ja/docs/06-materials.md) · [한국어](../translations/ko/docs/06-materials.md) · [हिन्दी](../translations/hi/docs/06-materials.md)

The rest of this repo assumes steel. This page asks the simpler, bigger question: **for which wall materials does the two-transducer channel work at all**, and in which mode? It is a simulation study (`--mock`-style, no lab data — intuition for what deserves a hardware experiment), built from the same semi-empirical model as [channel_sim](../software/simulator/channel_sim.py) and extended with bulk absorption.

Generate: `python3 software/simulator/material_map.py` (needs numpy + matplotlib). Model and assumptions: [../software/simulator/material_map.py](../software/simulator/material_map.py).

## The model in one minute

Two losses decide whether a wave crosses a wall of thickness d:

1. **Impedance contrast and phase** — the lossless Fabry–Perot slab model, identical to [channel_sim](../software/simulator/channel_sim.py):
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_wall / Z_couplant, couplant Z = 1.5 MRayl (grease).
   At a half-wave resonance (f = c/2d) a lossless symmetric slab is fully transparent *regardless of r*; the contrast r sets how **wide** the comb teeth are (tolerance to frequency error), the sound speed c sets how far apart they are (Δf = c/2d).
2. **Bulk absorption**, invisible to the lossless model and the decider for plastics, concrete and rubber:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, one-way, longitudinal],
   where α₁ₘₕᶻ is the 1 MHz value.
   γ ≈ 1 = viscous/relaxation loss; γ > 2 = scattering off inhomogeneities (concrete aggregate).

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

- **At 40 kHz, low-Z walls (plastics, rubber lining) couple *more easily* than steel** — through grease they are almost impedance-matched, so the comb is broad and transmission per pass is high. What kills plastics at higher frequencies is **bulk absorption**, not contact or impedance. The material ladder at 40 kHz is therefore inverted vs intuition: HDPE/PMMA/PVC > glass/concrete > aluminum > titanium > steel > copper — with the strong caveat that the rubbers' 40 kHz number extrapolates α linearly down from 1 MHz, which viscoelasticity does not guarantee.
- **Mode B divides materials cleanly.** Metals, glass and alumina take MHz with negligible absorption (α ≤ 0.1 dB/cm); the comb is *sharp* for high-Z walls (steel, alumina — needs frequency tracking, the ~6% ⇒ ~10× lesson of [00-theory](00-theory.md)) and *wide* for glass/PMMA (tolerant, but PMMA pays ~1–3 dB one-way at 1 MHz through 5 mm — mW-class only).
- **Concrete is a 40 kHz material, not a MHz one.** Aggregate scattering (λ at 1 MHz ≈ 3.5 mm ≈ aggregate size) throws γ up to ~2.5 and kills MHz; ultrasonic pulse-velocity practice (40–80 kHz through ≥1 m paths) is exactly mode A.
- **The battery-pack niche ([05](05-applications-map.md)) is acoustically favorable:** a 2–3 mm aluminum wall has a coupling proxy ~3× steel's and negligible absorption — the flagship case is also the easy case.
- **The frequency ladder to plan for in mode B** (5 mm wall, first comb): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, copper ≈ 480, steel ≈ 590, titanium ≈ 610, aluminum ≈ 630, glass ≈ 560, alumina ≈ 990. Thinner wall ⇒ proportionally higher.

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

## What a hardware follow-up should measure

Before trusting any specific plate: two-thickness method per material (two plates of d and 2d at the same contact) to extract real α(f) and c — that single dataset replaces every row of the table above. Natural bonus passes inside the existing protocols: repeat the experiment [001](../experiments/001-sweep-map-3mm-steel/README.md) sweep on a 5 mm PMMA plate, a borosilicate or 99% alumina plate, and a concrete block of known grade; expect a *lower but broader* peak for the plastics, a sharp comb for the ceramics, and a temperature-sensitive contact everywhere. Nothing in this page is measured — it is the map of what to measure first.