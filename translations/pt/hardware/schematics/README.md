# Esquemas da bancada de testes

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · Português · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Arquivo | O quê | Etapa |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | driver: IR2110 + 2×IRF540, bootstrap, transformador de casamento | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | receptor: ponte 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | pinout: Pi ↔ AD9833 ↔ par de piezo ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | nó: RX → GY-LTC3588 → supercapacitor → ESP32 (+ modulação de carga) | 4 |

Estes são esquemas de **protótipo em placa de ensaio** (os valores dos componentes são pontos de partida, marcados com `*` onde precisam ser ajustados no osciloscópio). Um projeto KiCad com o layout do PCB virá assim que o protótipo for verificado na prática — como prometido em [driver/README.md](../driver/README.md).
