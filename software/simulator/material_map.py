#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
material_map.py — which wall materials carry power and data between two
piezoelectric devices, and under which mode. The steel-only companion of
channel_sim.py, covering titanium, aluminum, glass, ceramics, plastics,
concrete — and the honest dead ends.

Derived from the same semi-empirical model as channel_sim.py (NOT FEM, NOT
lab data — intuition for which materials deserve a hardware experiment):
two losses govern the wall crossing:

  1. Impedance-contrast / thickness phase (lossless Fabry-Perot, identical to
     channel_sim.py):
        T(f) = 1 / (1 + ((r - 1/r)/2)^2 * sin(2*pi*f*d/c_wall)^2),
        r  = Z_wall / Z_couplant   (grease couplant, 1.5 MRayl)
     At a half-wave resonance (f = c/2d) a lossless symmetric slab is fully
     transparent regardless of r; the contrast r sets how wide those comb
     teeth are (how tolerant to frequency error), the sound speed c sets how
     far apart they are.

  2. Bulk absorption, which the lossless model cannot see and which decides
     the fate of plastics, concrete and rubber:
        A(f) = 10 ^ (-alpha(f) * d / 10 [dB]),
        alpha(f) = alpha_1MHz * (f/1MHz)^gamma   [dB/cm, one-way, longitudinal]

Material properties are TYPICAL HANDBOOK VALUES (longitudinal wave, room
temperature). Real stocks vary — grain structure, fillers, aggregates and
cure all move c and alpha by tens of percent or orders of magnitude; replace
with measured data before trusting any specific plate.

Also included: relative coupling at 40 kHz (mode A) — the same T(f) evaluated
on the mode-A working frequency with a 3 mm wall, used ONLY as a ranking
proxy (see docs/06-materials.md for why the absolute watts are not claimed).

Labels are hardcoded English for now; promote to labels.json (i18n) if this
becomes a primary figure set.

Run: python3 material_map.py [--out docs/img]
Dependencies: numpy, matplotlib.
"""

import argparse
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------- palette (same light mode as channel_sim.py) ----------
SURFACE = "#fcfcfb"
INK     = "#0b0b0b"
INK2    = "#52514e"
MUTED   = "#898781"
GRID    = "#e1e0d9"
BASE    = "#c3c2b7"

def style_ax(ax, title, xlabel, ylabel):
    ax.set_facecolor(SURFACE)
    ax.figure.set_facecolor(SURFACE)
    ax.set_title(title, color=INK, fontsize=13, loc="left", pad=12)
    ax.set_xlabel(xlabel, color=INK2, fontsize=10)
    ax.set_ylabel(ylabel, color=INK2, fontsize=10)
    ax.tick_params(colors=MUTED, labelsize=9)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(BASE)
    ax.grid(True, color=GRID, linewidth=0.8, alpha=0.9)
    ax.set_axisbelow(True)

# ---------- wall materials ----------
# Typical handbook values (longitudinal, ~20 °C). NOT measurements of specific
# stock — batch-dependent: grain, fillers, aggregate, cure.
#   rho   kg/m^3        density
#   c     m/s           longitudinal sound speed
#   a1    dB/cm@1MHz    bulk absorption at 1 MHz (one-way, longitudinal)
#   gamma               alpha(f) = a1*(f/1MHz)^gamma  (1 = viscous/relaxation,
#                       > 2 = scattering off inhomogeneities)
#   cls   "metal" | "nonmetal"
MATERIALS = [
    # key        label           rho     c      a1     gamma  cls        note
    ("steel",    "steel",        7850.0, 5900.0, 0.02, 1.0,  "metal",
     "fine-grained structural"),
    ("alum",     "aluminum",     2700.0, 6320.0, 0.02, 1.0,  "metal",
     "6061-class"),
    ("ti",       "titanium",     4430.0, 6100.0, 0.03, 1.0,  "metal",
     "Ti-6Al-4V"),
    ("cu",       "copper",       8960.0, 4760.0, 0.05, 1.0,  "metal",
     "dense, very high Z"),
    ("glass",    "borosilicate glass", 2230.0, 5640.0, 0.01, 1.0, "nonmetal",
     "very low loss"),
    ("alumina",  "alumina ceramic",    3890.0, 9900.0, 0.08, 1.0, "nonmetal",
     "fast sound, low loss"),
    ("pmma",     "PMMA (acrylic)",     1180.0, 2690.0, 2.5, 1.2, "nonmetal",
     "transparent, absorption-limited at MHz"),
    ("pvc",      "PVC (rigid)",        1400.0, 2380.0, 6.0, 1.2, "nonmetal",
     "lossier than PMMA"),
    ("hdpe",     "HDPE",               950.0,  2340.0, 12.0, 1.5, "nonmetal",
     "soft, lossy"),
    ("concrete", "concrete",           2300.0, 3500.0, 5.0, 2.5, "nonmetal",
     "aggregate scattering dominates; varies by orders of magnitude"),
    ("rubber",   "rubber (filled)",    1100.0, 1500.0, 60.0, 1.0, "nonmetal",
     "the honest dead end"),
]
BY_KEY = {m[0]: m for m in MATERIALS}

COLOR = {"steel": "C0", "alum": "C1", "ti": "C2", "cu": "C3",
         "glass": "C4", "alumina": "C5", "pmma": "C6", "pvc": "C7",
         "hdpe": "C8", "concrete": "C9", "rubber": MUTED}

COUPLANT_Z = 1.5         # MRayl — grease couplant, same as channel_sim.py
WALL_MM = 5              # Mode B chart: all walls at one thickness
MODE_A_MM = 3            # Mode A proxy: the project's reference 3 mm wall
F_MODE_A = 40e3          # Hz

def z_mrayl(m) -> float:
    return m[2] * m[3] / 1e6

def fp_transmission(f, d_m, c, z_wall, z_med=COUPLANT_Z):
    """Lossless Fabry-Perot intensity transmission of a slab (same model as
    channel_sim.py chart_fabry_perot)."""
    r = z_wall / z_med
    finesse = ((r - 1.0 / r) / 2.0) ** 2
    phase = 2.0 * np.pi * f * d_m / c
    return 1.0 / (1.0 + finesse * np.sin(phase) ** 2)

def absorption(f, d_m, a1, gamma):
    """One-way bulk absorption factor, 1.0 = lossless."""
    alpha = a1 * (f / 1e6) ** gamma          # dB/cm
    return 10.0 ** (-alpha * (d_m * 100.0) / 10.0)

def wall_transmission(f, m, d_m):
    return fp_transmission(f, d_m, m[3], z_mrayl(m)) * absorption(
        f, d_m, m[4], m[5])

def chart_comb(out: Path):
    """Mode B (MHz): thickness-resonance comb of a 5 mm wall per material."""
    f_metals = np.linspace(0.1e6, 2.0e6, 8000)
    f_nonmet = np.linspace(0.05e6, 1.2e6, 8000)
    d = WALL_MM / 1000.0
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    panels = [(axes[0], f_metals, "Structural metals", "metal"),
              (axes[1], f_nonmet, "Non-metals", "nonmetal")]
    for ax, f, title, cls in panels:
        for m in MATERIALS:
            if m[6] != cls:
                continue
            df_comb = m[3] / (2.0 * d) / 1e3          # kHz
            styled = dict(color=COLOR[m[0]], linewidth=1.8,
                          label=f"{m[1]}  (Δf = {df_comb:.0f} kHz)")
            if m[0] == "rubber":
                styled.update(linewidth=1.4, linestyle="--")
            t = wall_transmission(f, m, d)
            ax.plot(f / 1e6, t, **styled)
        style_ax(ax, title, "Frequency, MHz",
                 "Transmission (no contact loss)")
        ax.axhline(1.0, color=MUTED, linewidth=0.7, alpha=0.6)
        ax.legend(frameon=False, labelcolor=INK2, fontsize=7.5)
    fig.suptitle(
        f"Thickness-resonance comb through a {WALL_MM} mm wall, grease coupling "
        f"({COUPLANT_Z} MRayl) — T × absorption (lossless model peaks reach T = 1)",
        x=0.02, ha="left", fontsize=12, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(out / "mat1-thickness-comb-materials.png", dpi=160)
    plt.close(fig)

def chart_map(out: Path):
    """The money plot: acoustic impedance vs 1 MHz absorption, both log."""
    fig, ax = plt.subplots(figsize=(9, 5.4))
    for m in MATERIALS:
        z = z_mrayl(m)
        ax.scatter(m[4], z, s=210, color=COLOR[m[0]], edgecolor=SURFACE,
                   linewidth=1.6, zorder=3)
        ax.annotate(m[1], (m[4], z), textcoords="offset points",
                    xytext=(9, 4), color=INK, fontsize=9.5, zorder=4)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(2e-3, 3e2)
    ax.set_ylim(0.8, 200)
    # couplant line: below Z(couplant) the wall is acoustically an "easier"
    # medium than the grease that wets it to the transducer
    ax.axhline(COUPLANT_Z, color=MUTED, linewidth=0.9, linestyle="--", alpha=0.8)
    ax.annotate(f"couplant ({COUPLANT_Z} MRayl)", (0.0026, 1.9),
                color=MUTED, fontsize=9)
    ax.axvline(1.0, color=MUTED, linewidth=0.9, linestyle="--", alpha=0.8)
    ax.annotate("1 dB/cm @ 1 MHz", (1.15, 150), color=MUTED, fontsize=9,
                rotation=90, va="top")
    ax.annotate("power-grade walls:\nhigh Z, low loss", (0.004, 70),
                color=INK2, fontsize=10)
    ax.annotate("MHz limited by loss —\n40 kHz still open", (18, 30),
                color=INK2, fontsize=10)
    ax.annotate("nothing here\nworks", (30, 1.15), color=INK2, fontsize=10)
    style_ax(ax, "Wall material map — impedance vs absorption",
             "Bulk absorption α @ 1 MHz, dB/cm (log)",
             "Acoustic impedance Z = ρ·c, MRayl (log)")
    fig.tight_layout()
    fig.savefig(out / "mat2-material-map.png", dpi=160)
    plt.close(fig)

def _mode_a_values():
    """Mode A (40 kHz) relative coupling proxy: T·absorption at 40 kHz through
    the reference 3 mm wall.

    A RANKING only: the resonant transducer pair multiplies every material
    roughly equally in the real rig, and the model has no transducer loading.
    Absolute watts are stage-2 target territory (experiments/002), not here.
    """
    d = MODE_A_MM / 1000.0
    return [(m[1], wall_transmission(F_MODE_A, m, d), z_mrayl(m), m[3])
            for m in MATERIALS]


def chart_mode_a(out: Path):
    vals = _mode_a_values()
    ref = dict((v[0], v[1]) for v in vals)["steel"]
    names = [v[0] for v in vals]
    rel = [v[1] / ref for v in vals]
    y = np.arange(len(vals))
    fig, ax = plt.subplots(figsize=(9, 5.6))
    colors = [COLOR[BY_KEY_LOOKUP[n]] for n in names]
    ax.barh(y, rel, height=0.6, color=colors, edgecolor=SURFACE, linewidth=1.4)
    ax.set_yticks(y, names)
    ax.set_xscale("log")
    ax.set_xlim(0.5, 6)
    for yi, (name, t, _, _), r in zip(y, vals, rel):
        ax.annotate(f"{r:.1f}×", (r, yi), textcoords="offset points",
                    xytext=(7, -3), color=INK2, fontsize=9)
    style_ax(ax,
             f"Mode A coupling proxy at 40 kHz, {MODE_A_MM} mm wall "
             "(steel = 1.0)",
             "T(40 kHz) × absorption, relative to steel (ranking only)",
             "")
    ax.grid(True, axis="x", color=GRID, linewidth=0.8)
    ax.grid(False, axis="y")
    ax.text(0.55, len(vals) - 0.4,
            "the resonant transducer pair multiplies all bars\n"
            "roughly equally — compare ratios, not watts",
            color=MUTED, fontsize=9, va="top")
    fig.tight_layout()
    fig.savefig(out / "mat3-modea-coupling-materials.png", dpi=160)
    plt.close(fig)
    vals.sort(key=lambda v: v[1])
    names = [v[0] for v in vals]
    rel = [v[1] / ref for v in vals]
    y = np.arange(len(vals))
    fig, ax = plt.subplots(figsize=(9, 5.6))
    colors = [COLOR[BY_KEY_LOOKUP[n]] for n in names]
    ax.barh(y, rel, height=0.6, color=colors, edgecolor=SURFACE, linewidth=1.4)
    ax.set_yticks(y, names)
    ax.set_xscale("log")
    ax.set_xlim(0.5, 6)
    ax.text(0.55, len(vals) - 0.4,
            "the resonant transducer pair multiplies all bars\n"
            "roughly equally — compare ratios, not watts",
            color=MUTED, fontsize=9, va="top")
    fig.tight_layout()
    fig.savefig(out / "mat3-modea-coupling-materials.png", dpi=160)
    plt.close(fig)

# label -> material key reverse lookup for the bar colors
BY_KEY_LOOKUP = {m[1]: m[0] for m in MATERIALS}

def summary_table() -> str:
    d_b = WALL_MM / 1000.0
    d_a = MODE_A_MM / 1000.0
    rows = [
        "| Wall | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | "
        "comb Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | note |",
        "|---|---|---|---|---|---|---|---|---|"]
    for m in MATERIALS:
        z = z_mrayl(m)
        df_comb = m[3] / (2.0 * d_b) / 1e3
        lam40 = m[3] / F_MODE_A * 1000.0
        t40 = fp_transmission(F_MODE_A, d_a, m[3], z) * absorption(
            F_MODE_A, d_a, m[4], m[5])
        rows.append(f"| {m[1]} | {m[2]:.0f} | {m[3]:.0f} | {z:.1f} | "
                    f"{m[4]:g} | {df_comb:.0f} | {lam40:.0f} | {t40:.2f} | {m[7]} |")
    return "\n".join(rows)

if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Material sweep of the through-wall acoustic channel")
    p.add_argument("--out", default=str(
        Path(__file__).resolve().parents[2] / "docs" / "img"))
    a = p.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for chart in (chart_comb, chart_map, chart_mode_a):
        chart(out)
    print("OK: mat1/mat2/mat3 PNG →", out.resolve())
    print()
    print(summary_table())