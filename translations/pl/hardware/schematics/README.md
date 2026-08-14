# Schematy stanowiska testowego

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · Polski · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Plik | Co | Etap |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | sterownik: IR2110 + 2×IRF540, bootstrap, transformator dopasowujący | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | odbiornik: 4×SS14 mostek → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | pinout: Pi ↔ AD9833 ↔ para piezo ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | węzeł: RX → GY-LTC3588 → superkondensator → ESP32 (+ modulacja obciążenia) | 4 |

To są schematy **prototypu na płytce stykowej** (wartości elementów to punkty wyjściowe, oznaczone `*` tam, gdzie są dostrajane na oscyloskopie). Projekt KiCad z układem PCB pojawi się, gdy prototyp zostanie zweryfikowany w rzeczywistości — zgodnie z obietnicą w [driver/README.md](../driver/README.md).
