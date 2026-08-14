# Receptor

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · Português · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · [中文](../../../zh/hardware/receiver/README.md) · [日本語](../../../ja/hardware/receiver/README.md) · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

Esquemas: [estágio 1 — sch2](../schematics/sch2-receiver-stage1.png) · [estágio 4 — sch4](../schematics/sch4-receiver-node.png) (gerados por [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

- Estágio 1 (medições): transdutor Langevin RX (ambos os terminais flutuantes — não aterrar!) → ponte Schottky (4×SS14) → filtro RC (10k || 100n) → TVS 5 V → **47 kΩ em série** → ADS1115 A0 (o resistor limita a corrente nos diodos de proteção do ADC: o TVS limita em ~9 V acima do abs. max. da entrada).
- Estágio 2 (potência): RX → a mesma ponte → carga resistiva conhecida (e/ou LED), medir V e I DC após a ponte; a potência é V·I nessa carga. Protocolo: [experiments/002](../../experiments/002-watts-3mm-steel/README.md).
- Estágio 4 (nó): RX → GY-LTC3588 **direto em PZ1/PZ2** (a ponte já está embutida no LTC3588-1, nenhuma externa necessária) → supercapacitor de 1 F → ESP32 (deep sleep + duty cycle). Modulação de carga — 2N7002 + 100 Ω no **lado DC** (pino VIN do módulo, ver sch4); um único MOSFET em paralelo com o piezo AC não funciona — o diodo de corpo desvia meia onda (docs/03).

IMPORTANTE: instale o TVS antes da primeira energização — um piezo em aberto na ressonância gera dezenas a centenas de volts. No lado DC após a ponte — um SMBJ5.0A unidirecional; em paralelo com o piezo do nó (AC) — apenas um SMBJ15CA bidirecional.
