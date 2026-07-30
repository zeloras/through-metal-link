# Esquemas do teste

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · Português · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md)

Os esquemas são gerados a partir de código — [render_schematics.py](../../../../hardware/schematics/render_schematics.py) serve como fonte de design (schemdraw); para fazer alterações, edite o script, então regenere:

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Arquivo | O que é | Estágio |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | driver: IR2110 + 2×IRF540, bootstrap, transformador de acoplamento | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | receptor: 4×SS14 ponte → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | pinout: Pi ↔ AD9833 ↔ par de piezo ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | nó: RX → GY-LTC3588 → supercapacitor → ESP32 (+ modulação de carga) | 4 |

Estes são esquemas de **protótipo de breadboard** (os valores dos componentes são pontos de partida, marcados `*` onde são ajustados no osciloscópio). Um projeto KiCad com o layout da PCB virá uma vez que o protótipo tenha sido verificado na prática — como prometido em [driver/README.md](../driver/README.md).
