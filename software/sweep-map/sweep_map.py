#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
sweep_map.py — sweep map of the acoustic channel frequency response through a
metal wall.

Hardware (stage 1):
  Raspberry Pi
    ├── SPI0  → AD9833 DDS module (sine generator) → driver → piezo TX
    └── I2C   → ADS1115 ADC, channel A0 ← rectified voltage from piezo RX
                (Schottky bridge + RC filter 100n||10k; TVS diode at the input
                is mandatory!)

What it does: steps the frequency from F_START to F_STOP by F_STEP, measures
the receiver voltage at every point, writes a CSV and plots the frequency
response. The peak on the plot = the resonance of the "TX — wall — RX" pair,
i.e. the working frequency for stages 2-4.

Run:  python3 sweep_map.py --start 25000 --stop 45000 --step 50
      (CSV and the plot land in data/ at the repo root, regardless of cwd)
No hardware (any computer): python3 sweep_map.py --mock
Dependencies: pip install spidev smbus2 matplotlib (matplotlib alone is enough
for --mock)
"""

import argparse
import csv
import math
import random
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------- AD9833 (SPI) ----------

AD9833_FMCLK = 25_000_000  # module reference crystal, Hz

class AD9833:
    def __init__(self, bus=0, device=0, max_speed_hz=1_000_000):
        import spidev
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = max_speed_hz
        self.spi.mode = 0b10  # CPOL=1, CPHA=0

    def _write16(self, word: int):
        self.spi.xfer2([(word >> 8) & 0xFF, word & 0xFF])

    def set_frequency(self, freq_hz: float):
        freq_word = int(round(freq_hz * (1 << 28) / AD9833_FMCLK))
        lsb = 0x4000 | (freq_word & 0x3FFF)
        msb = 0x4000 | ((freq_word >> 14) & 0x3FFF)
        self._write16(0x2100)  # reset + two-word write mode
        self._write16(lsb)
        self._write16(msb)
        self._write16(0xC000)  # phase 0
        self._write16(0x2000)  # release reset → sine out

    def off(self):
        self._write16(0x2100)

# ---------- ADS1115 (I2C) ----------

ADS1115_ADDR = 0x48
_FSR_CONFIG = {6.144: 0x0000, 4.096: 0x0200, 2.048: 0x0400, 1.024: 0x0600}

def ads1115_read_v(bus, channel: int = 0, fsr: float = 4.096) -> float:
    """Single-shot measurement, channel AINx against GND, 128 SPS."""
    if not 0 <= channel <= 3:
        raise ValueError(f"ADS1115 channel must be 0-3, got {channel}")
    if fsr not in _FSR_CONFIG:
        raise ValueError(f"ADS1115 fsr must be one of {sorted(_FSR_CONFIG)}, got {fsr}")
    config = 0x8000 | (0x4000 | (channel << 12)) | _FSR_CONFIG[fsr] | 0x0100 | 0x0080 | 0x0003
    bus.write_i2c_block_data(ADS1115_ADDR, 0x01, [(config >> 8) & 0xFF, config & 0xFF])
    time.sleep(0.010)
    raw = bus.read_i2c_block_data(ADS1115_ADDR, 0x00, 2)
    value = (raw[0] << 8) | raw[1]
    if value & 0x8000:
        value -= 1 << 16
    return value * fsr / 32768.0

# ---------- Mock mode (pipeline check without hardware) ----------

class MockRig:
    """Synthetic channel: a pair of Lorentzians (the same model as in
    channel_sim.py) + ADC noise. Lets the whole sweep → CSV → PNG pipeline run
    on any computer."""

    F_TX, F_RX, Q, V_PEAK = 39.8e3, 40.4e3, 40, 0.55  # "dry contact"
    _freq = 30e3

    def set_frequency(self, freq_hz):
        self._freq = freq_hz

    def off(self):
        pass

    def read_v(self):
        def lorentz(f, f0):
            return 1.0 / math.sqrt(1.0 + (self.Q * (f / f0 - f0 / f)) ** 2)
        v = self.V_PEAK * lorentz(self._freq, self.F_TX) * lorentz(self._freq, self.F_RX)
        return max(0.0, v + random.gauss(0, 0.004))

# ---------- Sweep ----------

def run_sweep(f_start, f_stop, f_step, settle_s, samples, out_dir, mock=False):
    if mock:
        rig = MockRig()
        dds, read_v = rig, rig.read_v
        settle_s = 0.0
        print("Mock mode: no hardware needed, synthetic channel (peak ~40.1 kHz)")
    else:
        try:
            from smbus2 import SMBus
        except ImportError:
            raise SystemExit("No smbus2/spidev — this is probably not a Raspberry Pi. "
                             "To run without hardware: sweep_map.py --mock")
        bus = SMBus(1)
        dds = AD9833()
        read_v = lambda: ads1115_read_v(bus)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = Path(out_dir) / f"sweep_{f_start:.0f}-{f_stop:.0f}_{ts}.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    # try/finally is mandatory: on Ctrl-C or an I2C failure the generator must
    # go silent, otherwise the half-bridge keeps driving the piezo at the last
    # frequency indefinitely
    try:
        with open(out_path, "w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["freq_hz", "v_rx_mean", "v_rx_max"])
            # frequency by index, not by accumulation: a float step drifts off
            # the grid
            for i in range(int(round((f_stop - f_start) / f_step)) + 1):
                freq = f_start + i * f_step
                dds.set_frequency(freq)
                if settle_s:
                    time.sleep(settle_s)  # let the resonance settle (high Q!)
                readings = [read_v() for _ in range(samples)]
                v_mean = sum(readings) / len(readings)
                writer.writerow([freq, round(v_mean, 5), round(max(readings), 5)])
                rows.append((freq, v_mean))
                print(f"{freq:>8.0f} Hz  ->  {v_mean:.4f} V")
    finally:
        dds.off()
        if not mock:
            bus.close()

    if not rows:
        raise SystemExit("No sweep points generated — check --start/--stop/--step")
    peak_f, peak_v = max(rows, key=lambda r: r[1])
    print(f"\nPeak: {peak_f:.0f} Hz, {peak_v:.3f} V  →  working-frequency candidate")
    print(f"CSV: {out_path}")
    plot(rows, peak_f, out_path.with_suffix(".png"))
    return out_path

def plot(rows, peak_f, png_path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib is not installed — skipping the plot")
        return
    freqs, volts = zip(*rows)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot([f / 1000 for f in freqs], volts)
    ax.axvline(peak_f / 1000, linestyle="--", alpha=0.5)
    ax.set_xlabel("Frequency, kHz")
    ax.set_ylabel("Receiver voltage, V")
    ax.set_title(f"Channel frequency response. Peak: {peak_f/1000:.2f} kHz")
    fig.tight_layout()
    fig.savefig(png_path, dpi=150)
    print(f"Plot: {png_path}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Sweep map of the through-wall channel response")
    p.add_argument("--start", type=float, default=25_000)
    p.add_argument("--stop", type=float, default=45_000)
    p.add_argument("--step", type=float, default=50)
    p.add_argument("--settle", type=float, default=0.05, help="pause per point, s")
    p.add_argument("--samples", type=int, default=8, help="measurements per point")
    p.add_argument("--out", default=None,
                   help="output directory (default: data/ at the repo root)")
    p.add_argument("--mock", action="store_true",
                   help="no hardware: synthetic channel, pipeline check")
    a = p.parse_args()
    if a.stop <= a.start or a.step <= 0 or a.samples < 1:
        raise SystemExit("Check the arguments: need start < stop, step > 0, samples >= 1")
    out_dir = a.out or Path(__file__).resolve().parent.parent.parent / "data"
    run_sweep(a.start, a.stop, a.step, a.settle, a.samples, out_dir, mock=a.mock)
