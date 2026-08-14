# Schémas du banc d'essai

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · Français · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Fichier | Description | Étape |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | pilote : IR2110 + 2×IRF540, bootstrap, transformateur d'adaptation | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | récepteur : pont 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | brochage : Pi ↔ AD9833 ↔ paire piézo ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | nœud : RX → GY-LTC3588 → supercondensateur → ESP32 (+ modulation de charge) | 4 |

Ce sont des schémas de **prototype sur breadboard** (les valeurs des composants sont des points de départ, marqués `*` là où ils seront ajustés à l'oscilloscope). Un projet KiCad avec le layout du PCB arrivera une fois le prototype vérifié en vrai — comme promis dans [driver/README.md](../driver/README.md).
