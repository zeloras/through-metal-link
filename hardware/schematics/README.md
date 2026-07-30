# Test-rig schematics

> English (primary) · [Русский](../../translations/ru/hardware/schematics/README.md) · [Deutsch](../../translations/de/hardware/schematics/README.md) · [Português](../../translations/pt/hardware/schematics/README.md) · [中文](../../translations/zh/hardware/schematics/README.md) · [日本語](../../translations/ja/hardware/schematics/README.md)

The schematics are generated from code — [render_schematics.py](render_schematics.py) doubles as the design source (schemdraw); to make changes, edit the script, then regenerate:

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| File | What | Stage |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | driver: IR2110 + 2×IRF540, bootstrap, matching transformer | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | receiver: 4×SS14 bridge → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | pinout: Pi ↔ AD9833 ↔ piezo pair ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | node: RX → GY-LTC3588 → supercapacitor → ESP32 (+ load modulation) | 4 |

These are **breadboard-prototype** schematics (component values are starting points, marked `*` where they get dialed in on the oscilloscope). A KiCad project with the PCB layout will come once the prototype has been verified in the flesh — as promised in [driver/README.md](../driver/README.md).
