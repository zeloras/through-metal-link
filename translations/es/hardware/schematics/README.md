# Esquemas del banco de pruebas

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · Español · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Archivo | Qué es | Etapa |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | driver: IR2110 + 2×IRF540, bootstrap, transformador de adaptación | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | receptor: puente 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | pinout: Pi ↔ AD9833 ↔ par de piezos ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | nodo: RX → GY-LTC3588 → supercapacitor → ESP32 (+ modulación de carga) | 4 |

Estos son esquemáticos de **prototipo en placa de pruebas** (los valores de los componentes son puntos de partida, marcados con `*` donde se ajustan en el osciloscopio). Un proyecto KiCad con el layout del PCB llegará una vez que el prototipo se haya verificado físicamente — como se promete en [driver/README.md](../driver/README.md).
