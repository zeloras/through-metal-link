# Prüfstand-Schemata

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · Deutsch · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Datei | Beschreibung | Phase |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | Treiber: IR2110 + 2×IRF540, Bootstrap, Anpassungstrafo | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | Empfänger: 4×SS14-Brücke → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | Pinbelegung: Pi ↔ AD9833 ↔ Piezo-Paar ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | Knoten: RX → GY-LTC3588 → Superkondensator → ESP32 (+ Lastmodulation) | 4 |

Dies sind **Steckbrett-Prototyp**-Schaltpläne (Bauteilwerte sind Startwerte, mit `*` markiert, wo sie am Oszilloskop justiert werden). Ein KiCad-Projekt mit dem PCB-Layout wird folgen, sobald der Prototyp in der Praxis verifiziert wurde — wie in [driver/README.md](../driver/README.md) versprochen.
