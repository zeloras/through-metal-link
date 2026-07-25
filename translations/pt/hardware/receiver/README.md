# Receptor

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · Português

Esquemáticos: [etapa 1 — sch2](../../schematics/sch2-receiver-stage1.png) · [etapa 4 — sch4](../../schematics/sch4-receiver-node.png) (gerado por [../../schematics/render_schematics.py](../../schematics/render_schematics.py))

- Etapa 1 (medidas): transdutor Langevin RX (ambos terminais flutuando — não aterre!) → ponte Schottky (4×SS14) → filtro RC (10k || 100n) → TVS 5 V → **47 kΩ em série** → ADS1115 A0 (o resistor limita a corrente nos diodos de proteção do ADC: o TVS limita ~9 V acima do máximo absoluto de entrada).
- Etapa 2 (watts): RX → mesma ponte → carga eletrônica/resistiva, medir V e I.
- Etapa 4 (nó): RX → GY-LTC3588 **diretamente para PZ1/PZ2** (a ponte está incorporada ao LTC3588-1, não é necessária uma externa) → supercapacitor 1 F → ESP32 (sono profundo + ciclo de trabalho). Modulação de carga — 2N7002 + 100 Ω no **lado DC** (pino VIN do módulo, veja sch4); um único MOSFET através do piezo AC não funciona — o diodo do corpo deriva uma meia-onda (docs/03).

IMPORTANTE: instale o TVS antes do primeiro ligamento — um piezo aberto em ressonância produz dezenas a centenas de volts. No lado DC após a ponte — um SMBJ5.0A unidirecional; através do piezo do nó (AC) — apenas um SMBJ15CA bidirecional.
