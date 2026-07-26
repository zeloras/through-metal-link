#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
channel_sim.py — semi-empirical simulator of the through-wall acoustic channel.

Not CAD, not FEM, and not lab data: a model for intuition — "what the sweep
should look like and what to aim at". Replace assumed constants with measured
values after experiments 001/002.

Physics inside:
  Mode A (40 kHz): a Langevin pair = two Lorentzian resonances (Q~40 loaded,
  assumed), channel ∝ |H_tx·H_rx| · k_contact. A 3-5 mm plate ≪ λ (148 mm) —
  a transparent membrane. Contact k and chain η_max are placeholders.
  Mode B (MHz): a comb of plate thickness resonances (Fabry-Perot):
  T(f) = 1 / (1 + ((r - 1/r)/2 · sin(2πfd/v))²), r — impedance step.

All display strings live in labels.json (one section per language, matching
i18n.json). Each run renders every language: the primary set goes to --out,
every other language goes to translations/<lang>/docs/img/ with the same file
names.

Run: python3 channel_sim.py [--out docs/img] [--lang <code>|all]
Dependencies: numpy, matplotlib.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

REPO_ROOT = Path(__file__).resolve().parents[2]
LABELS = json.loads((Path(__file__).resolve().parent / "labels.json").read_text(encoding="utf-8"))
I18N = json.loads((REPO_ROOT / "i18n.json").read_text(encoding="utf-8"))
PRIMARY = I18N["primary"]

# ---------- palette (light mode, validated) ----------
SURFACE = "#fcfcfb"
INK     = "#0b0b0b"
INK2    = "#52514e"
MUTED   = "#898781"
GRID    = "#e1e0d9"
BASE    = "#c3c2b7"
S1, S2, S3 = "#2a78d6", "#eb6834", "#1baf7a"   # blue, orange, aqua

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

def lorentz(f, f0, q):
    """Resonator amplitude response (normalized to 1 at the peak)."""
    return 1.0 / np.sqrt(1.0 + (q * (f / f0 - f0 / f)) ** 2)

# ---------- Mode A ----------

F = np.linspace(25e3, 45e3, 2000)
Q_LOADED = 40                         # assumed loaded Q; measure from sweep width
F_TX, F_RX = 39.8e3, 40.4e3          # example cheap-pair spread ~0.6 kHz

def chart_sweep(out, L):
    """Expected stage-1 sweep shape (weak DDS drive, no half-bridge).

    Contact multipliers are placeholders (grease:dry:gap = 1:0.25:0.02),
    not calibrated measurements — experiment 001 bonus pass replaces them.
    """
    contacts = [(L["sim1.contact.grease"], 1.00, S1),
                (L["sim1.contact.dry"],    0.25, S2),
                (L["sim1.contact.gap"],    0.02, S3)]
    fig, ax = plt.subplots(figsize=(9, 5))
    v_peak_ref = 2.2  # volts at the receiver with ideal contact and weak drive
    for label, k, color in contacts:
        v = v_peak_ref * k * lorentz(F, F_TX, Q_LOADED) * lorentz(F, F_RX, Q_LOADED)
        ax.plot(F / 1e3, v, color=color, linewidth=2, label=label)
        i = np.argmax(v)
        ax.annotate(f"{v[i]:.2f} {L['unit.V']}", (F[i] / 1e3, v[i]),
                    textcoords="offset points", xytext=(8, 4),
                    color=INK2, fontsize=9)
    style_ax(ax, L["sim1.title"], L["sim1.xlabel"], L["sim1.ylabel"])
    ax.legend(frameon=False, labelcolor=INK2, fontsize=9, loc="upper left")
    ax.annotate(L["sim1.note"],
                (40.1, 0.35), xytext=(26.5, 1.15), color=MUTED, fontsize=9,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    fig.tight_layout()
    fig.savefig(out / f"sim1-sweep-contacts.png", dpi=160)
    plt.close(fig)

def chart_mismatch(out, L):
    """Model power into the load vs frequency for a mismatched resonance pair.

    eff_max=0.40 is an optimistic chain ceiling (driver + match + contact +
    transducers), not a measured efficiency. Peak ratios vs Δf are the lesson;
    absolute watts are stage-2 targets until experiment 002 lands.
    """
    fig, ax = plt.subplots(figsize=(9, 5))
    p_drive, eff_max = 10.0, 0.40      # drive watts; assumed max chain efficiency
    for df, color, label in [(0.0, S1, L["sim2.match"]),
                             (700.0, S2, L["sim2.typ"]),
                             (1500.0, S3, L["sim2.bad"])]:
        p = p_drive * eff_max * (lorentz(F, 40.0e3 - df / 2, Q_LOADED)
                                 * lorentz(F, 40.0e3 + df / 2, Q_LOADED)) ** 2
        ax.plot(F / 1e3, p, color=color, linewidth=2, label=label)
        i = np.argmax(p)
        ax.annotate(f"{p[i]:.1f} {L['unit.W']}", (F[i] / 1e3, p[i]),
                    textcoords="offset points", xytext=(8, 2),
                    color=INK2, fontsize=9)
    style_ax(ax, L["sim2.title"], L["sim1.xlabel"], L["sim2.ylabel"])
    ax.legend(frameon=False, labelcolor=INK2, fontsize=9)
    ax.annotate(L["sim2.note"], (32, 2.6), color=MUTED, fontsize=9)
    fig.tight_layout()
    fig.savefig(out / f"sim2-pair-mismatch.png", dpi=160)
    plt.close(fig)

# ---------- Mode B ----------

def chart_fabry_perot(out, L):
    """Comb of thickness resonances of the steel plate (MHz mode)."""
    fig, ax = plt.subplots(figsize=(9, 5))
    v_steel = 5900.0
    # impedance step steel/coupling layer: 46 MRayl (steel) / 1.5 MRayl
    # (grease/epoxy) — resonances are sharp, T drops ~9x at +6% off peak
    r = 46.0 / 1.5
    fmhz = np.linspace(0.3e6, 2.2e6, 8000)
    for d_mm, color in [(3, S1), (4, S2), (5, S3)]:
        d = d_mm / 1000
        t = 1.0 / (1.0 + (((r - 1 / r) / 2) * np.sin(2 * np.pi * fmhz * d / (2 * v_steel) * 2)) ** 2)
        ax.plot(fmhz / 1e6, t, color=color, linewidth=2,
                label=L["sim3.steel"].format(d=d_mm))
    style_ax(ax, L["sim3.title"], L["sim3.xlabel"], L["sim3.ylabel"])
    ax.set_ylim(0, 1.32)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.legend(frameon=False, labelcolor=INK2, fontsize=9, loc="lower right")
    ax.annotate(L["sim3.note"], (0.33, 1.16), color=MUTED, fontsize=9)
    fig.tight_layout()
    fig.savefig(out / f"sim3-thickness-comb.png", dpi=160)
    plt.close(fig)

# ---------- Stage 3: data (OOK) ----------

def chart_ook(out, L):
    """OOK rate is limited by resonator ring-down: τ = Q/(π·f0) ≈ 0.3 ms."""
    f0 = 40.1e3
    tau = Q_LOADED / (np.pi * f0)
    pattern = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0]

    def envelope(bitrate):
        t_bit = 1.0 / bitrate
        dt = t_bit / 400
        t = np.arange(0, t_bit * len(pattern), dt)
        target = np.array([pattern[min(int(x / t_bit), len(pattern) - 1)] for x in t], float)
        v = np.empty_like(target)
        acc = 0.0
        for i, tgt in enumerate(target):
            acc += (tgt - acc) * (1 - np.exp(-dt / tau))
            v[i] = acc
        return t * 1e3, v, target

    fig, axes = plt.subplots(2, 1, figsize=(9, 6.2))
    for ax, bitrate, color, note in [
        (axes[0], 1e3, S1, L["sim5.note.slow"]),
        (axes[1], 5e3, S2, L["sim5.note.fast"]),
    ]:
        t_ms, v, target = envelope(bitrate)
        ax.plot(t_ms, target, color=BASE, linewidth=1.2, drawstyle="steps-post")
        ax.plot(t_ms, v, color=color, linewidth=2)
        ax.axhline(0.5, color=MUTED, linestyle="--", linewidth=0.9, alpha=0.7)
        style_ax(ax, L["sim5.sub"].format(r=f"{bitrate/1e3:g}"),
                 L["sim5.xlabel"], L["sim5.ylabel"])
        ax.set_ylim(-0.08, 1.25)
        ax.text(0.02, 1.08, note, color=MUTED, fontsize=9)
    fig.suptitle(L["sim5.title"].format(q=Q_LOADED, tau=f"{tau*1e3:.1f}"),
                 x=0.02, ha="left", fontsize=13, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(out / f"sim5-ook-datarate.png", dpi=160)
    plt.close(fig)

# ---------- Receiver power budget ----------

def chart_power_budget(out, L):
    consumers = [  # (load, watts)
        (L["sim4.rtc"],    50e-6),
        (L["sim4.charge"], 1.5e-3),
        (L["sim4.esp"],    3e-3),
        (L["sim4.led"],    20e-3),
        (L["sim4.ble"],    150e-3),
        (L["sim4.wifi"],   700e-3),
    ]
    fig, ax = plt.subplots(figsize=(9, 4.8))
    names = [c[0] for c in consumers]
    watts = [c[1] for c in consumers]
    y = np.arange(len(consumers))
    ax.barh(y, watts, height=0.55, color=S1, edgecolor=SURFACE, linewidth=2)
    ax.set_yticks(y, names)
    ax.set_xscale("log")
    ax.set_xlim(1e-5, 20)
    # expected received-power windows
    ax.set_ylim(-0.6, 6.9)
    # Target received-power bands (not measured). Mode A lower edge = stage-2 gate.
    ax.axvspan(0.1, 0.5, color=S3, alpha=0.12)
    ax.axvspan(0.5, 5.0, color=S2, alpha=0.12)
    ax.text(0.22, 6.05, L["sim4.modeB"], color=S3, fontsize=9, ha="center")
    ax.text(1.6, 6.05, L["sim4.modeA"], color=S2, fontsize=9, ha="center")
    def fmt_w(w):
        if w < 1e-3:
            return f"{w*1e6:g} {L['unit.uW']}"
        return f"{w*1000:g} {L['unit.mW']}" if w < 1 else f"{w:g} {L['unit.W']}"
    for yi, w in zip(y, watts):
        ax.annotate(fmt_w(w), (w, yi), textcoords="offset points",
                    xytext=(6, -3), color=INK2, fontsize=9)
    style_ax(ax, L["sim4.title"], L["sim4.xlabel"], "")
    ax.grid(True, axis="x", color=GRID, linewidth=0.8)
    ax.grid(False, axis="y")
    fig.tight_layout()
    fig.savefig(out / f"sim4-power-budget.png", dpi=160)
    plt.close(fig)

# ---------- Rig sketch ----------

def sketch_rig(out, L):
    fig, ax = plt.subplots(figsize=(11, 4.6))
    fig.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 40)
    ax.axis("off")

    def box(x, y, w, h, text, sub="", accent=INK):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6",
                                    fc=SURFACE, ec=accent, lw=1.6))
        ax.text(x + w / 2, y + h / 2 + (1.6 if sub else 0), text,
                ha="center", va="center", fontsize=10, color=INK)
        if sub:
            ax.text(x + w / 2, y + h / 2 - 2.4, sub, ha="center", va="center",
                    fontsize=8, color=MUTED)

    def arrow(x1, y1, x2, y2, label="", color=INK2):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                     mutation_scale=14, color=color, lw=1.4))
        if label:
            ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 1.8, label,
                    ha="center", fontsize=8, color=MUTED)

    # transmit side
    box(2, 24, 14, 9, L["sim0.pi"], L["sim0.pi.sub"], S1)
    box(22, 24, 12, 9, L["sim0.dds"], L["sim0.dds.sub"])
    box(40, 24, 15, 9, L["sim0.bridge"], L["sim0.bridge.sub"])
    box(61, 24, 10, 9, L["sim0.xfmr"], L["sim0.xfmr.sub"])
    box(77, 24, 10, 9, L["sim0.tx"], L["sim0.tx.sub"], S2)
    # the wall
    ax.add_patch(Rectangle((90.2, 20), 2.6, 16, fc=BASE, ec=INK2, lw=1.2))
    ax.text(91.5, 37.2, L["sim0.wall"], ha="center", fontsize=9, color=INK2)
    # receive side
    box(97, 24, 10, 9, L["sim0.rx"], L["sim0.rx.sub"], S2)
    box(97, 8, 10, 8, L["sim0.schottky"], L["sim0.schottky.sub"])
    box(77, 8, 13, 8, L["sim0.cap"], L["sim0.cap.sub"])
    box(56, 8, 14, 8, L["sim0.adc"], L["sim0.adc.sub"])
    box(22, 8, 12, 8, L["sim0.load"], L["sim0.load.sub"])

    arrow(16, 28.5, 21.4, 28.5, L["sim0.spi"])
    arrow(34, 28.5, 39.4, 28.5)
    arrow(55, 28.5, 60.4, 28.5)
    arrow(71, 28.5, 76.4, 28.5)
    arrow(87.3, 28.5, 89.9, 28.5, color=S2)
    arrow(93.1, 28.5, 96.4, 28.5, color=S2)
    arrow(102, 23.4, 102, 16.6)
    arrow(96.4, 12, 90.6, 12)
    arrow(76.4, 12, 70.6, 12)
    arrow(55.4, 12, 34.6, 12)
    arrow(56, 14, 16, 25, L["sim0.i2c"])

    ax.text(2, 2, L["sim0.footer"], fontsize=9, color=MUTED)
    fig.tight_layout()
    fig.savefig(out / f"sim0-rig-sketch.png", dpi=160)
    plt.close(fig)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    # anchored at the repo root, not at cwd: the old cwd-relative default wrote
    # outside the repository when the script was run from anywhere but its own
    # directory
    p.add_argument("--out", default=str(REPO_ROOT / "docs" / "img"))
    p.add_argument("--lang", default="all",
                   help="language code from labels.json, or 'all'")
    a = p.parse_args()
    missing = sorted(set(I18N["names"]) - set(LABELS))
    if missing:
        raise SystemExit(f"labels.json has no section for: {', '.join(missing)} "
                         "(declared in i18n.json) — run tools/translate_sync.py")
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    charts = [sketch_rig, chart_sweep, chart_mismatch, chart_fabry_perot,
              chart_power_budget, chart_ook]
    langs = list(LABELS) if a.lang == "all" else [a.lang]
    n = 0
    for lang in langs:
        if lang not in LABELS:
            raise SystemExit(f"no such language in labels.json: {lang}")
        L = LABELS[lang]
        out_l = out if lang == PRIMARY else REPO_ROOT / "translations" / lang / "docs" / "img"
        out_l.mkdir(parents=True, exist_ok=True)
        for chart in charts:
            chart(out_l, L)
            n += 1
    print(f"OK: {n} PNG ({'+'.join(langs)}) → {out.resolve()}")
