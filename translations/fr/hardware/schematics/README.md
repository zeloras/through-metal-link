# Schémas du banc de test

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · Français · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

Les schémas sont générés à partir du code — [render_schematics.py](../../../../hardware/schematics/render_schematics.py) fait également office de source de conception (schemdraw) ; pour faire des modifications, éditez le script, puis régénérez :

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Fichier | Description | Étape |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | driver : IR2110 + 2×IRF540, bootstrap, transformateur d'adaptation | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | récepteur : pont 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | brochage : Pi ↔ AD9833 ↔ paire de piézos ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | nœud : RX → GY-LTC3588 → supercondensateur → ESP32 (+ modulation de charge) | 4 |

Ce sont des schémas de **prototype sur breadboard** (les valeurs des composants sont des points de départ, marqués `*` là où elles seront ajustées à l'oscilloscope). Un projet KiCad avec le layout du PCB arrivera une fois le prototype vérifié pour de bon — comme promis dans [driver/README.md](../driver/README.md).
