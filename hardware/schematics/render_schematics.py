#!/usr/bin/env python3
# SPDX-License-Identifier: CERN-OHL-W-2.0
"""
render_schematics.py — the rig's schematics, generated from code (schemdraw):
the schematic IS the design source; regenerate = python render_schematics.py.

sch1 — stage 2 driver: IR2110 + 2×IRF540 (half-bridge) + bootstrap + transformer.
sch2 — stage 1 receiver: 4×SS14 bridge → RC → TVS → ADS1115.
sch3 — stage 1 wiring: Raspberry Pi ↔ AD9833 ↔ piezo ↔ ADS1115.
sch4 — stage 4 node: RX → GY-LTC3588 (bridge built in) → supercap → ESP32.

All display strings live in labels.json (one section per language, matching
i18n.json). Each run renders every language: the primary set lands next to the
script, every other language goes to translations/<lang>/hardware/schematics/
with the same file names.

Run: uv run --with schemdraw --with matplotlib python render_schematics.py [--lang <code>|all]
Output: PNG+SVG.
"""

import argparse
import json
import os
import sys
from pathlib import Path

import matplotlib

import schemdraw
import schemdraw.elements as elm

# The rendered figures are committed, so their bytes have to be a function of
# labels.json and this file — nothing else. Matplotlib's SVG writer breaks that
# twice over: it stamps every file with the wall-clock render time, and it salts
# the clip-path ids it generates from a per-process seed, so two identical runs
# differ in ~86 lines per schematic. That is why the nightly sync rewrote all 56
# schematic SVGs every night with no content change — the job was not comparing
# anything wrongly, it was staging real byte differences. PNG output has neither
# property, which is why only the SVGs churned.
#
# Both knobs below are documented matplotlib behaviour, and both have to be set
# here: schemdraw's save() forwards neither (it calls savefig with a fixed
# argument list, so metadata={'Date': None} cannot be passed through). The
# environment variable is read at savefig time, not at import, so it does not
# have to precede the imports above.
os.environ["SOURCE_DATE_EPOCH"] = "0"  # -> <dc:date>1970-01-01T00:00:00+00:00</dc:date>
matplotlib.rcParams["svg.hashsalt"] = "through-metal-link"

OUT = Path(__file__).resolve().parent
REPO_ROOT = OUT.parents[1]
FS = 10.5

# ---------- lazy-loaded i18n data ----------

_LABELS: dict | None = None
_I18N: dict | None = None


def _load_labels() -> dict:
    global _LABELS
    if _LABELS is None:
        _LABELS = json.loads((OUT / "labels.json").read_text(encoding="utf-8"))
    return _LABELS


def _load_i18n() -> dict:
    global _I18N
    if _I18N is None:
        _I18N = json.loads((REPO_ROOT / "i18n.json").read_text(encoding="utf-8"))
    return _I18N


def save(d, name, out):
    for ext in ("png", "svg"):
        d.save(str(out / f"{name}.{ext}"), dpi=200)
    print(f"{out / name}: png+svg")


# ---------- sch1: driver (stage 2) ----------

def sch1_driver(L, out):
    d = schemdraw.Drawing(show=False)
    d.config(unit=2.0, fontsize=FS)

    ic = d.add(elm.Ic(
        pins=[
            elm.IcPin(name="VDD", pin="9", side="left", slot="5/5"),
            elm.IcPin(name="HIN", pin="10", side="left", slot="4/5"),
            elm.IcPin(name="LIN", pin="12", side="left", slot="3/5"),
            elm.IcPin(name="SD", pin="11", side="left", slot="2/5"),
            elm.IcPin(name="VSS", pin="13", side="left", slot="1/5"),
            elm.IcPin(name="VB", pin="6", side="right", slot="5/5"),
            elm.IcPin(name="HO", pin="7", side="right", slot="4/5"),
            elm.IcPin(name="VS", pin="5", side="right", slot="3/5"),
            elm.IcPin(name="LO", pin="1", side="right", slot="2/5"),
            elm.IcPin(name="COM", pin="2", side="right", slot="1/5"),
            elm.IcPin(name="VCC", pin="3", side="top", slot="1/1"),
        ],
        edgepadW=1.1, edgepadH=0.6, pinspacing=1.2, label="IR2110",
    ).at((0, 0)))

    # logic side: shaper producing complementary HIN/LIN with dead time
    fmr = d.add(elm.Ic(
        pins=[
            elm.IcPin(name="IN", side="left", slot="1/1"),
            elm.IcPin(name="H", side="right", slot="2/2"),
            elm.IcPin(name="L", side="right", slot="1/2"),
        ],
        edgepadW=0.9, edgepadH=0.5, pinspacing=1.2,
    ).right().at((ic.HIN[0] - 3.2, ic.HIN[1])).anchor("H")
        .label(L["sch1.shaper"], "top", fontsize=FS - 1))
    d.add(elm.Line().at(fmr.H).to(ic.HIN))
    d.add(elm.Line().at(fmr.L).to(ic.LIN))
    d.add(elm.Line().at(fmr.IN).left(1.2).label(L["sch1.in"], "left", fontsize=FS - 1))
    d.add(elm.Line().at(ic.VDD).left(1.6).label(L["sch1.vdd"], "left", fontsize=FS - 1))
    d.add(elm.Line().at(ic.SD).left(0.8))
    d.add(elm.Ground().label(L["sch1.sd"], "bottom", fontsize=FS - 2))
    d.add(elm.Line().at(ic.VSS).left(0.8))
    d.add(elm.Ground())
    d.add(elm.Line().at(ic.COM).right(0.8))
    d.add(elm.Ground())

    x_boot = ic.VB[0] + 3.2          # bootstrap column
    x_fet = ic.VB[0] + 7.0           # switch column
    vbus_y = ic.VB[1] + 2.6

    # high-side switch: drain on the supply rail
    q1 = d.add(elm.NFet(bulk=False).at((x_fet, vbus_y)).anchor("drain").theta(0)
               .label("IRF540", "right", fontsize=FS - 1))
    d.add(elm.Line().at((x_fet, vbus_y)).up(1.0)
          .label(L["sch1.bus"], "right", fontsize=FS - 1))
    # local bulk capacitance right at the half-bridge legs — mandatory
    d.add(elm.Dot().at((x_fet, vbus_y + 0.5)))
    d.add(elm.Line().at((x_fet, vbus_y + 0.5)).left(1.8))
    d.add(elm.Capacitor(polar=True).down(1.5).label(L["sch1.buscap"], "top", fontsize=FS - 2))
    d.add(elm.Ground())
    d.add(elm.Line().at(q1.source).down(0.3))
    swn = d.here                      # switch node

    q2 = d.add(elm.NFet(bulk=False).at(swn).anchor("drain").theta(0)
               .label("IRF540", "right", fontsize=FS - 1))
    d.add(elm.Line().at(q2.source).down(0.4))
    d.add(elm.Ground())

    # gates: HO/LO -> Rg -> gate (orthogonal routing)
    d.add(elm.Line().at(ic.HO).right(0.5))
    r1 = d.add(elm.Resistor().right(1.7).label(L["sch1.rg"], "top", fontsize=FS - 1))
    d.add(elm.Wire("-|").at(r1.end).to(q1.gate))
    d.add(elm.Line().at(ic.LO).right(0.5))
    r2 = d.add(elm.Resistor().right(1.7).label(L["sch1.rg"], "top", fontsize=FS - 1))
    d.add(elm.Wire("-|").at(r2.end).to(q2.gate))

    # bootstrap: VCC -> UF4007 -> VB rail; C from VB to VS
    d.add(elm.Line().at(ic.VCC).up(0.5))
    d.add(elm.Label().at((ic.VCC[0] - 4.8, ic.VCC[1] + 1.0)).label(
        L["sch1.vcc"], fontsize=FS - 1, halign="left"))
    d.add(elm.Line().right(x_boot - 1.6 - d.here[0]))
    d.add(elm.Diode().right(1.6).label("UF4007", "top", fontsize=FS - 1))
    d.add(elm.Line().toy(ic.VB))
    d.add(elm.Dot())
    d.add(elm.Line().at(ic.VB).tox(x_boot))
    # keep the cap short so its plates stay clear of the HO wire; then plain wire
    d.add(elm.Capacitor().at((x_boot, ic.VB[1])).down(0.7))
    d.add(elm.Label().at((x_boot + 0.25, ic.VB[1] + 0.3)).label(
        L["sch1.bootcap"], fontsize=FS - 1, halign="left"))
    d.add(elm.Line().toy(ic.VS))
    d.add(elm.Dot())
    # VS: to the bootstrap and to the switch node
    d.add(elm.Line().at(ic.VS).tox(x_boot))
    d.add(elm.Line().at((x_boot, ic.VS[1])).tox(x_fet))
    d.add(elm.Line().toy(swn[1]))

    # output: DC-block + transformer + Langevin
    d.add(elm.Dot().at(swn))
    d.add(elm.Line().at(swn).right(1.1))
    d.add(elm.Capacitor().right(1.5).label(L["sch1.dcblock"], "top", fontsize=FS - 1))
    tr = d.add(elm.Transformer(t1=5, t2=8).anchor("p1")
               .label(L["sch1.xfmr"], "bottom", fontsize=FS - 1, ofst=0.6))
    d.add(elm.Line().at(tr.p2).left(0.6))
    d.add(elm.Line().toy(swn[1] - 3.4))
    d.add(elm.Ground())
    d.add(elm.Line().at(tr.s1).right(1.1))
    xt = d.add(elm.Crystal().toy(tr.s2).label(L["sch1.tx"], "right", fontsize=FS - 1))
    d.add(elm.Line().at(xt.end).to(tr.s2))

    d.add(elm.Label().at((-4.5, vbus_y + 2.4)).label(
        L["sch1.title"], fontsize=12, halign="left"))
    save(d, "sch1-driver-halfbridge", out)


# ---------- sch2: stage 1 receiver ----------

def sch2_receiver_stage1(L, out):
    d = schemdraw.Drawing(show=False)
    d.config(unit=2.0, fontsize=FS)

    y_ac = 1.3          # bridge AC-node level
    y_dcp = 3.6         # DC+ rail
    y_dcm = -1.0        # DC- rail
    x1, x2 = 3.4, 5.6   # bridge columns

    xt = d.add(elm.Crystal().at((0.9, 0)).up(2.6).label(L["sch2.rx"], "left", fontsize=FS))
    d.add(elm.Line().at(xt.end).right(1.2))
    d.add(elm.Line().toy(y_ac))
    d.add(elm.Line().tox(x1))
    d.add(elm.Dot())
    # bottom piezo lead -> AC2 (crossings without dots = no connection)
    d.add(elm.Line().at(xt.start).right(1.2))
    d.add(elm.Line().tox(6.8))
    d.add(elm.Line().toy(y_ac))
    d.add(elm.Line().tox(x2))
    d.add(elm.Dot())

    # Graetz bridge: two legs of two diodes each (anodes at the bottom)
    for x in (x1, x2):
        d.add(elm.Diode().at((x, y_dcm)).up().toy(y_ac))
        d.add(elm.Dot().at((x, y_ac)))
        d.add(elm.Diode().at((x, y_ac)).up().toy(y_dcp))
    d.add(elm.Line().at((x1, y_dcp)).tox(x2))
    d.add(elm.Line().at((x1, y_dcm)).tox(x2))
    d.add(elm.Line().at(((x1 + x2) / 2, y_dcm)).down(0.5))
    d.add(elm.Ground())
    d.add(elm.Label().at((x1 - 0.4, y_dcp + 0.35)).label(L["sch2.bridge"], fontsize=FS - 1, halign="left"))

    # DC+ chain: C || R || TVS -> Rseries -> A0
    d.add(elm.Line().at((x2, y_dcp)).right(2.0))
    n1 = d.here
    d.add(elm.Dot())
    d.add(elm.Capacitor().at(n1).down(2.2).label(L["sch2.c"], "top", fontsize=FS - 1, ofst=0.35))
    d.add(elm.Ground())
    d.add(elm.Line().at(n1).right(2.4))
    n2 = d.here
    d.add(elm.Dot())
    d.add(elm.Resistor().at(n2).down(2.2).label(L["sch2.r"], "top", fontsize=FS - 1, ofst=0.35))
    d.add(elm.Ground())
    d.add(elm.Line().at(n2).right(2.4))
    n3 = d.here
    d.add(elm.Dot())
    d.add(elm.DiodeTVS().at(n3).down(2.2).label(L["sch2.tvs"], "bottom", fontsize=FS - 1, ofst=0.4))
    d.add(elm.Ground())
    # series resistor: limits current into the ADC protection diodes
    # (TVS clamps at ~9 V > ADS1115 input abs.max = VDD+0.3)
    d.add(elm.Line().at(n3).right(0.5))
    d.add(elm.Resistor().right(1.7).label(L["sch2.rseries"], "top", fontsize=FS - 1))
    d.add(elm.Line().right(0.7).label(L["sch2.out"], "right", fontsize=FS))

    d.add(elm.Label().at((0, y_dcp + 1.3)).label(
        L["sch2.title"], fontsize=12, halign="left"))
    save(d, "sch2-receiver-stage1", out)


# ---------- sch3: stage 1 wiring ----------

def sch3_stage1_wiring(L, out):
    d = schemdraw.Drawing(show=False)
    d.config(unit=2.0, fontsize=FS)

    pi = d.add(elm.Ic(
        pins=[
            elm.IcPin(name="3V3", pin="1", side="right", slot="6/6", anchorname="V33"),
            elm.IcPin(name="MOSI", pin="19", side="right", slot="5/6"),
            elm.IcPin(name="SCLK", pin="23", side="right", slot="4/6"),
            elm.IcPin(name="CE0", pin="24", side="right", slot="3/6"),
            elm.IcPin(name="SDA", pin="3", side="right", slot="2/6"),
            elm.IcPin(name="SCL", pin="5", side="right", slot="1/6"),
            elm.IcPin(name="GND", pin="6", side="bottom", slot="1/1"),
        ],
        edgepadW=1.4, edgepadH=0.7, pinspacing=1.2, label=L["sch3.pi"],
    ).at((0, 0)))
    d.add(elm.Line().at(pi.GND).down(0.4))
    d.add(elm.Ground())

    # AD9833: pins aligned with the Pi rows -> straight wires
    dds = d.add(elm.Ic(
        pins=[
            elm.IcPin(name="VCC", side="left", slot="5/5"),
            elm.IcPin(name="SDATA", side="left", slot="4/5"),
            elm.IcPin(name="SCLK", side="left", slot="3/5"),
            elm.IcPin(name="FSYNC", side="left", slot="2/5"),
            elm.IcPin(name="DGND", side="left", slot="1/5"),
            elm.IcPin(name="OUT", side="right", slot="2/2"),
            elm.IcPin(name="AGND", side="right", slot="1/2"),
        ],
        edgepadW=1.2, edgepadH=0.7, pinspacing=1.2, label="AD9833",
    ).right().at((pi.V33[0] + 5.0, pi.V33[1])).anchor("VCC"))

    d.add(elm.Line().at(pi.V33).to(dds.VCC).label(L["sch3.v33"], "top", fontsize=FS - 2))
    d.add(elm.Line().at(pi.MOSI).to(dds.SDATA).label(L["sch3.spi"], "top", fontsize=FS - 2))
    d.add(elm.Line().at(pi.SCLK).to(dds.SCLK))
    d.add(elm.Line().at(pi.CE0).to(dds.FSYNC))
    d.add(elm.Line().at(dds.DGND).left(0.5))
    d.add(elm.Line().down(0.8))
    d.add(elm.Ground())

    # ADS1115 below
    adc = d.add(elm.Ic(
        pins=[
            elm.IcPin(name="VDD", side="left", slot="5/5"),
            elm.IcPin(name="SDA", side="left", slot="4/5"),
            elm.IcPin(name="SCL", side="left", slot="3/5"),
            elm.IcPin(name="ADDR", side="left", slot="2/5"),
            elm.IcPin(name="GND", side="left", slot="1/5"),
            elm.IcPin(name="A0", side="right", slot="3/3"),
        ],
        edgepadW=1.2, edgepadH=0.7, pinspacing=1.2, label="ADS1115",
    ).right().at((dds.VCC[0], pi.SCL[1] - 7.6)).anchor("VDD"))

    d.add(elm.Line().at(adc.VDD).left(0.9).label(L["sch3.vdd"], "left", fontsize=FS - 2))
    # I2C: each wire gets its own jog
    d.add(elm.Line().at(pi.SDA).right(0.7))
    d.add(elm.Line().toy(adc.SDA))
    d.add(elm.Line().to(adc.SDA).label(L["sch3.sda"], "bottom", fontsize=FS - 2))
    d.add(elm.Line().at(pi.SCL).right(1.3))
    d.add(elm.Line().toy(adc.SCL))
    d.add(elm.Line().to(adc.SCL).label(L["sch3.scl"], "bottom", fontsize=FS - 2))
    d.add(elm.Line().at(adc.ADDR).left(0.9).label(L["sch3.addr"], "left", fontsize=FS - 2))
    d.add(elm.Line().at(adc.GND).left(0.5))
    d.add(elm.Line().down(0.6))
    d.add(elm.Ground())

    # signal path: OUT -> TX | steel | RX -> sch2 -> A0
    d.add(elm.Line().at(dds.OUT).right(1.2).label(L["sch3.vpp"], "top", fontsize=FS - 2))
    tx = d.add(elm.Crystal().down(2.0).label(L["sch3.tx"], "left", fontsize=FS - 1))
    d.add(elm.Line().at(dds.AGND).right(0.5))
    d.add(elm.Wire("|-").at(d.here).to(tx.end))

    wall_x = tx.start[0] + 1.1
    d.add(elm.Rect(corner1=(0, 0), corner2=(0.5, -3.4), fill="#cccccc")
          .at((wall_x, dds.OUT[1] + 0.6)))
    d.add(elm.Label().at((wall_x + 0.25, dds.OUT[1] + 0.9)).label(L["sch3.wall"], fontsize=FS - 1))

    # both RX leads are floating AC inputs of the bridge (sch2) — do not ground!
    rx = d.add(elm.Crystal().at((wall_x + 1.7, dds.OUT[1])).down(2.0).label(L["sch3.rx"], "right", fontsize=FS - 1))
    d.add(elm.Line().at(rx.start).right(1.0))
    box = d.add(elm.Ic(pins=[elm.IcPin(name="", side="left", slot="2/2", anchorname="AC1"),
                             elm.IcPin(name="", side="left", slot="1/2", anchorname="AC2"),
                             elm.IcPin(name="", side="bot", anchorname="DCOUT")],
                       edgepadW=0.9, edgepadH=0.5,
                       label=L["sch3.box"]).right().anchor("AC1"))
    d.add(elm.Line().at(rx.end).right(0.5))
    d.add(elm.Line().toy(box.AC2))
    d.add(elm.Line().to(box.AC2))
    d.add(elm.Wire("|-").at(box.DCOUT).to(adc.A0))

    d.add(elm.Label().at((-2.2, pi.V33[1] + 2.2)).label(
        L["sch3.title"], fontsize=12, halign="left"))
    save(d, "sch3-stage1-wiring", out)


# ---------- sch4: stage 4 node ----------

def sch4_receiver_node(L, out):
    d = schemdraw.Drawing(show=False)
    d.config(unit=2.0, fontsize=FS)

    xt = d.add(elm.Crystal().at((0.6, 0)).up(2.4).label(L["sch4.rx"], "left", fontsize=FS))
    d.add(elm.Line().at(xt.end).right(1.2))
    topn = d.here
    d.add(elm.Dot())
    d.add(elm.Line().at(xt.start).right(1.2))
    botn = d.here
    d.add(elm.Dot())

    # bidirectional TVS on the AC side: a unidirectional one would clip a half-wave
    d.add(elm.DiodeTVS().at(topn).toy(botn[1]).label(L["sch4.tvs"], "bottom", fontsize=FS - 1, ofst=0.35))

    ltc = d.add(elm.Ic(
        pins=[
            elm.IcPin(name="PZ1", side="left", slot="3/3"),
            elm.IcPin(name="PZ2", side="left", slot="1/3"),
            elm.IcPin(name="VIN", side="right", slot="3/3"),
            elm.IcPin(name="VOUT", side="right", slot="2/3"),
            elm.IcPin(name="GND", side="right", slot="1/3"),
        ],
        edgepadW=1.3, edgepadH=0.7, pinspacing=1.4, label="GY-LTC3588",
    ).right().at((topn[0] + 3.4, topn[1])).anchor("PZ1"))
    d.add(elm.Line().at(topn).to(ltc.PZ1))
    d.add(elm.Wire("-|").at(botn).to(ltc.PZ2))
    d.add(elm.Label().at((ltc.PZ1[0] + 0.3, botn[1] - 2.1)).label(
        L["sch4.note"], fontsize=FS - 2, halign="left"))

    d.add(elm.Line().at(ltc.GND).right(0.6))
    d.add(elm.Line().down(1.6))
    d.add(elm.Ground())

    # load modulation (docs/03) — on the DC side of the rectifier (VIN);
    # a single MOSFET across the AC piezo does not work (body diode shunts a half-wave)
    mod_x = ltc.VIN[0] + 3.2
    d.add(elm.Line().at(ltc.VIN).tox(mod_x))
    d.add(elm.Line().toy(ltc.VIN[1] - 1.7))  # crosses VOUT — no junction dot
    d.add(elm.Resistor().down(1.5).label(L["sch4.rmod"], "top", fontsize=FS - 2))
    qm = d.add(elm.NFet(bulk=False).anchor("drain").theta(0)
               .label("2N7002", "right", fontsize=FS - 2))
    d.add(elm.Line().at(qm.source).down(0.3))
    gnd_mod = d.here
    d.add(elm.Ground())
    d.add(elm.Line().at(qm.gate).left(0.4))
    d.add(elm.Line().toy(gnd_mod[1] - 0.9))
    d.add(elm.Label().at((mod_x - 4.9, gnd_mod[1] - 1.5)).label(
        L["sch4.gate"], fontsize=FS - 2, halign="left"))

    d.add(elm.Line().at(ltc.VOUT).right(5.6))
    vnode = d.here
    d.add(elm.Dot())
    d.add(elm.Capacitor(polar=True).at(vnode).down(2.4).label(L["sch4.cap"], "bottom", fontsize=FS - 1, ofst=0.4))
    d.add(elm.Ground())
    d.add(elm.Line().at(vnode).right(1.8))

    esp = d.add(elm.Ic(
        pins=[
            elm.IcPin(name="3V3", side="left", slot="3/3", anchorname="V33"),
            elm.IcPin(name="GND", side="left", slot="1/3"),
            elm.IcPin(name="GPIO", side="right", slot="2/2"),
        ],
        edgepadW=1.2, edgepadH=0.7, pinspacing=1.4, label="ESP32",
    ).right().anchor("V33"))
    d.add(elm.Line().at(esp.GND).left(0.4))
    d.add(elm.Line().down(1.0))
    d.add(elm.Ground())
    d.add(elm.Line().at(esp.GPIO).right(0.8).label(L["sch4.gpio"], "right", fontsize=FS - 2))

    d.add(elm.Label().at((0, topn[1] + 1.6)).label(
        L["sch4.title"], fontsize=12, halign="left"))
    save(d, "sch4-receiver-node", out)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--lang", default="all",
                   help="language code from labels.json, or 'all'")
    a = p.parse_args()
    LABELS = _load_labels()
    I18N = _load_i18n()
    PRIMARY = I18N["primary"]
    sys.path.insert(0, str(REPO_ROOT / "tools"))
    import i18n_render
    fonts = i18n_render.apply(I18N)
    skip = i18n_render.skip_figures(I18N)
    langs = list(LABELS) if a.lang == "all" else [a.lang]
    done, tofu = [], []
    for lang in langs:
        if lang not in LABELS:
            raise SystemExit(f"no such language in labels.json: {lang}")
        if lang in skip and lang != PRIMARY:
            # complex-script language: its docs link to the primary schematics
            print(f"  - {lang}: schematics skipped by i18n.json render.skip_figures")
            continue
        L = LABELS[lang]
        # refuse to paint tofu — see tools/i18n_render.py
        gap = i18n_render.uncovered("".join(map(str, L.values())), fonts)
        if gap:
            print(f"  ! {i18n_render.report_uncovered(lang, gap)}")
            tofu.append(lang)
            continue
        out = OUT if lang == PRIMARY else REPO_ROOT / "translations" / lang / "hardware" / "schematics"
        out.mkdir(parents=True, exist_ok=True)
        sch1_driver(L, out)
        sch2_receiver_stage1(L, out)
        sch3_stage1_wiring(L, out)
        sch4_receiver_node(L, out)
        done.append(lang)
    print(f"OK ({'+'.join(done)}) → {OUT}")
    if tofu:
        raise SystemExit(f"no usable font for: {', '.join(tofu)} — schematics not written")
