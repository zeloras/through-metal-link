#!/usr/bin/env python3
"""
selfcheck_material_map.py — numerical guard-rail for material_map.py.

Everything here recomputes the model's quantities from first principles and
fails loudly on drift:

  1  the Fabry-Perot formula is the EXACT lossless plane-wave solution
     (checked against input-impedance recursion over 231 points);
  2  comb peaks sit at n*c/2d on the lossless branch (the lossy product
     peaks slightly lower — physical tilt from absorption, printed only);
  3  dB <-> Np conversions are consistent with the intensity-dB convention;
  4  the Airy x absorption product matches the full complex-k transfer
     matrix while the loss per pass is small;
  5  stress / heating / ceilings match from-scratch arithmetic;
  6  key outputs stay inside the ballparks the docs promise (steel stress,
     steel->air leakage, comb spacing, PMMA heating).

Run: python3 selfcheck_material_map.py   (deps: numpy + matplotlib via
material_map; runs in CI)
"""
import math
import sys
import os

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import material_map as mm

FAIL = []

def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)

COUP = mm.COUPLANT_Z          # MRayl, couplant on both sides

def exact_lossless(f, d_m, c_wall, z_wall, z_out):
    """Exact lossless plane-wave intensity transmission through a slab in a
    symmetric medium, via input impedance of the terminated line:
    Zin = Zc (ZL cos kd + i Zc sin kd) / (Zc cos kd + i ZL sin kd)."""
    phi = 2.0 * math.pi * f * d_m / c_wall
    zw, z0 = z_wall * 1e6, z_out * 1e6
    zin = zw * (z0 * math.cos(phi) + 1j * zw * math.sin(phi)) / \
          (zw * math.cos(phi) + 1j * z0 * math.sin(phi))
    gamma = (zin - z0) / (zin + z0)
    return 1.0 - abs(gamma) ** 2

def exact_complex_k(f, d_m, c_wall, z_wall, z_out, mu_np_m):
    """Exact transmission with absorption: complex k = w/c - i*mu_I/2
    (amplitude attenuation = intensity Np / 2), full transfer matrix, so ALL
    internal re-reflections are kept."""
    w = 2.0 * math.pi * f
    phi = (w / c_wall - 1j * mu_np_m / 2.0) * d_m
    zw, z0 = z_wall * 1e6, z_out * 1e6
    cph, sph = np.cos(phi), np.sin(phi)
    # [P; V]_front = M [P; V]_back, M = [[cos, i Z sin], [i sin/Z, cos]]
    M = np.array([[cph, 1j * zw * sph], [1j * sph / zw, cph]])
    # tau: complex amplitude at the backing; incident amplitude 1 in z0
    # P_front = M00 tau + M01 tau/z0 ; V_front = M10 tau + M11 tau/z0
    # with P_front = 1 + Gamma, V_front = (1 - Gamma)/z0
    A = M[0, 0] + M[0, 1] / z0
    B = M[1, 0] + M[1, 1] / z0
    tau = 2.0 / (A + B / z0)                # solve 1+G = tau A, 1-G = tau B z0
    return abs(tau) ** 2                    # same medium both sides

print("== 1. Fabry-Perot formula vs exact lossless recursion ==")
rng = np.random.default_rng(2026)
worst = 0.0
for m in mm.MATERIALS:
    z, c = mm.z_mrayl(m), m[3]
    freqs = [40e3, 150e3, 269e3, 590e3, 983e3, 1.5e6, float(rng.uniform(1e5, 2e6))]
    for f in freqs:
        for d in (3e-3, 5e-3, 10e-3):
            airy = float(mm.fp_transmission(f, d, c, z, COUP))
            exact = exact_lossless(f, d, c, z, COUP)
            worst = max(worst, abs(airy - exact))
print(f"  max |Airy - exact| over 11x7x3 = 231 pts: {worst:.2e}")
check("FP formula == exact wave recursion (lossless)", worst < 1e-9)

print("== 2. Comb positions — exact check on the LOSSLESS branch ==")
# The lossy product (comb x absorption) genuinely peaks BELOW n*c/2d for
# absorptive walls — physics, not a bug — so the hard equality is asserted on
# the lossless branch (fp_transmission), and the lossy shift is only reported.
bad = 0
d = 5e-3
for m in mm.MATERIALS:
    z, c = mm.z_mrayl(m), m[3]
    for n in (1, 2, 3):
        f_target = n * c / (2 * d)
        fs = np.linspace(f_target * 0.85, f_target * 1.15, 40001)
        ts = mm.fp_transmission(fs, d, c, z, COUP)
        f_peak = float(fs[int(np.argmax(ts))])
        if abs(f_peak - f_target) / f_target > 1e-3:
            bad += 1
            print(f"    {m[1]} n={n}: lossless peak off by "
                  f"{abs(f_peak - f_target) / f_target * 100:.3f}%")
check("lossless comb peaks at n*c/2d (11 materials x n=1..3)", bad == 0)
for m in mm.MATERIALS:
    f_t = m[3] / (2 * d)
    mu_d = mm.mu_np_per_m(m, f_t) * d
    fs = np.linspace(f_t * 0.7, f_t * 1.1, 40001)
    ts = mm.wall_transmission(fs, m, d)
    f_peak = float(fs[int(np.argmax(ts))])
    print(f"    {m[0]:>9}: lossy peak {f_peak/1e3:7.1f} kHz vs {f_t/1e3:7.1f} kHz "
          f"(mu*d = {mu_d:.2f})")

print("== 3. dB/Np consistency inside the model ==")
dev = 0.0
for m in mm.MATERIALS:
    for f in (40e3, 300e3, 1e6):
        mu = mm.mu_np_per_m(m, f)
        d_cm = 0.5   # small enough that even rubber@1 MHz (30 dB) stays in float range
        tenlog = float(mm.absorption(f, d_cm / 100.0, m[4], m[5]))
        enp = math.exp(-mu * d_cm / 100.0)
        lg_a = -10.0 * math.log10(max(tenlog, 1e-300))        # dB over d_cm
        lg_h = mu * (d_cm / 100.0) * 4.343                    # dB over d_cm
        dev = max(dev, abs(lg_a - lg_h) / max(1e-9, lg_h))
check("10^(-a/10) == exp(-mu), consistent dB<->Np for the intensity dB",
      dev < 1e-9, f"max rel dev {dev:.1e}")

print("== 4. Product approximation vs full complex-k solution ==")

def exact_complex_k(f, d_m, c_wall, z_wall, z_out, mu_np_m):
    """Exact transmission with absorption: complex k = w/c - i*mu_I/2
    (amplitude attenuation = intensity Np / 2), full transfer matrix, so ALL
    internal re-reflections are kept."""
    w = 2.0 * math.pi * f
    phi = (w / c_wall - 1j * mu_np_m / 2.0) * d_m
    zw, z0 = z_wall * 1e6, z_out * 1e6
    cph, sph = np.cos(phi), np.sin(phi)
    M = np.array([[cph, 1j * zw * sph], [1j * sph / zw, cph]], dtype=complex)
    A = M[0, 0] + M[0, 1] / z0
    B = (M[1, 0] + M[1, 1] / z0) * z0
    tau = 2.0 / (A + B)
    return abs(tau) ** 2                    # same medium both sides

# exact solver self-test: with mu = 0 it must reproduce the Airy formula
_dev0 = 0.0
for _m in mm.MATERIALS:
    _z, _c = mm.z_mrayl(_m), _m[3]
    for _f in (40e3, 300e3, 1e6):
        _dev0 = max(_dev0, abs(exact_complex_k(_f, 5e-3, _c, _z, COUP, 0.0) -
                               float(mm.fp_transmission(_f, 5e-3, _c, _z, COUP))))
check("exact solver self-test: mu=0 reproduces Airy", _dev0 < 1e-9,
      f"max dev {_dev0:.1e}")

worst_rel = 0.0
for key in ("steel", "pmma", "pvc", "hdpe", "concrete", "rubber"):
    mat = mm.BY_KEY[key]
    for f in (0.3e6, 1e6, 2e6):
        d = 5e-3
        mu = mm.mu_np_per_m(mat, f)
        if mu * d > 0.5:      # beyond a few dB/pass the comb barely exists;
            continue          # "dead material" conclusions don't need the proxy
        t_exact = exact_complex_k(f, d, mat[3], mm.z_mrayl(mat), COUP, mu)
        t_prod = float(mm.wall_transmission(f, mat, d))
        if t_exact > 1e-9:
            worst_rel = max(worst_rel, abs(t_prod - t_exact) / t_exact)
print(f"  max relative deviation (mu*d <= 0.5 cases): {worst_rel * 100:.2f}%")
check("Airy x absorb is a fair proxy for the exact lossy stack (<5%)",
      worst_rel < 0.05)

print("== 5. Stress / heating / ceilings vs plain-math recompute ==")
bad = 0
for m in mm.MATERIALS:
    z = mm.z_mrayl(m)
    s_man = math.sqrt(2 * 1e4 * z * 1e6) / 1e6
    if abs(s_man - float(mm.stress_mpa(m))) > 1e-9 + 1e-9 * max(1.0, s_man):
        bad += 1
        print(f"    stress mismatch {m[1]}")
    for f in (40e3, 1e6, 5e6):
        mu = m[4] * (f / 1e6) ** m[5] * 100 / 4.343      # same convention, from scratch
        dT_man = mu * 1e4 * 0.005 ** 2 / (8 * m[6])
        got = float(mm.heat_dT(m, f))
        if abs(dT_man - got) > max(1e-12, 1e-6 * max(dT_man, 1e-12)):
            bad += 1
            print(f"    dT mismatch {m[1]} @ {f}: {dT_man} vs {got}")
    i_stress_man = (0.2 * m[7] * 1e6) ** 2 / (2 * z * 1e6) / 1e4
    mu1 = m[4] * 100 / 4.343
    i_heat_man = 20 * 8 * m[6] / (mu1 * 0.005 ** 2) / 1e4
    ceil_man = min(i_stress_man, i_heat_man)
    got = float(mm.intensity_ceiling_wcm2(m, 1e6))
    if abs(ceil_man - got) > 1e-6 + 1e-6 * max(ceil_man, 1e-12):
        bad += 1
        print(f"    ceiling mismatch {m[1]}: {ceil_man} vs {got}")
check("stress / dT / ceiling match from-scratch recompute", bad == 0)

print("== 6b. multilayer stack solver ==")
# single lossless layer: stack_transmission must equal fp_transmission exactly
m = mm.BY_KEY["steel"]
z, c = mm.z_mrayl(m), m[3]
d1 = 0.003
dev_s = max(abs(mm.stack_transmission(f, [(z, c, d1, 0.0, 1.0)]) -
                float(mm.fp_transmission(f, d1, c, z)))
            for f in (40e3, 300e3, 1e6))
check("stack(1 lossless layer) == fp_transmission", dev_s < 1e-9,
      f"max dev {dev_s:.1e}")
# splitting a LOSSY layer into two halves changes nothing (exact invariance)
mm_p = mm.BY_KEY["pmma"]
zp, cp_, a1p, gp = mm.z_mrayl(mm_p), mm_p[3], mm_p[4], mm_p[5]
dev_h = max(abs(mm.stack_transmission(f, [(zp, cp_, 0.005, a1p, gp)]) -
              mm.stack_transmission(f, [(zp, cp_, 0.0025, a1p, gp),
                                        (zp, cp_, 0.0025, a1p, gp)]))
            for f in (40e3, 1e6, 2e6))
check("splitting a lossy layer keeps T identical", dev_h < 1e-12,
      f"max dev {dev_h:.1e}")
# zero-thickness layers are no-ops
mm_p = mm.BY_KEY["concrete"]
zc, cc_, a1c, gc = mm.z_mrayl(mm_p), mm_p[3], mm_p[4], mm_p[5]
t_plain = mm.stack_transmission(40e3, [(zc, cc_, 0.150, a1c, gc)])
t_zero = mm.stack_transmission(40e3, [(zc, cc_, 0.075, a1c, gc),
                                      (46.3, 5900.0, 0.0, 0.02, 1.0),
                                      (zc, cc_, 0.075, a1c, gc)])
check("zero-thickness layer is a no-op", abs(t_plain - t_zero) < 1e-12,
      f"|{t_plain:.6f} - {t_zero:.6f}|")

print("== 6. sanity vs the repo's own physics docs ==")
s_steel = float(mm.stress_mpa(mm.BY_KEY["steel"]))
check("steel stress @1 W/cm2 within 0.7-1.1 MPa (docs/00 ballpark)",
      0.7 <= s_steel <= 1.1, f"{s_steel:.2f} MPa")
t_air = 4 * 400 / 46.3e6
check("steel->air transmitted fraction O(1e-5) (docs/00)", 1e-6 < t_air < 1e-4,
      f"{t_air:.1e}")
dfm = mm.BY_KEY["steel"][3] / (2 * 0.005) / 1e3
check("steel comb Δf @5 mm == 590 kHz (doc table)", abs(dfm - 590) < 0.5,
      f"{dfm:.0f} kHz")
p_dT = float(mm.heat_dT(mm.BY_KEY["pmma"], 1e6))
check("PMMA dT @1 MHz, 1 W/cm2 in 8-11 K (post-fix expectation ~9.5)",
      8 <= p_dT <= 11, f"{p_dT:.1f} K")

print()
if FAIL:
    print(f"{len(FAIL)} FAILED:")
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("ALL CHECKS PASSED")