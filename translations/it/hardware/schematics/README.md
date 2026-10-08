# Schemi del banco di prova

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · Italiano · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

Gli schemi sono generati da codice — [render_schematics.py](../../../../hardware/schematics/render_schematics.py) funge anche da sorgente di progetto (schemdraw); per apportare modifiche, modifica lo script e poi rigenera:

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| File | Cosa | Fase |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | driver: IR2110 + 2×IRF540, bootstrap, trasformatore di adattamento | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | ricevitore: ponte 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | pinout: Pi ↔ AD9833 ↔ coppia piezo ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | nodo: RX → GY-LTC3588 → supercondensatore → ESP32 (+ modulazione di carico) | 4 |

Questi sono schemi di **prototipo su breadboard** (i valori dei componenti sono punti di partenza, contrassegnati con `*` dove vanno tarati all'oscilloscopio). Un progetto KiCad con il layout del PCB arriverà una volta che il prototipo sarà stato verificato di persona — come promesso in [driver/README.md](../driver/README.md).
