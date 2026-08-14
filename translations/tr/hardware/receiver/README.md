# Alıcı

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · Türkçe · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · [中文](../../../zh/hardware/receiver/README.md) · [日本語](../../../ja/hardware/receiver/README.md) · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

Şemalar: [aşama 1 — sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) · [aşama 4 — sch4](../../../../hardware/schematics/sch4-receiver-node.png) ([../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py) tarafından üretilmiştir)

- Aşama 1 (ölçümler): Langevin transdüser RX (her iki uç da yüzer — topraklamayın!) → Schottky köprü (4×SS14) → RC filtre (10k || 100n) → 5 V TVS → **47 kΩ seri** → ADS1115 A0 (direnç, ADC'nin koruma diyotlarına akan akımı sınırlar: TVS, girişin mutlak maksimumunun yaklaşık 9 V üstünde kenetler).
- Aşama 2 (watt): RX → aynı köprü → bilinen dirençli yük (ve/veya LED), köprüden sonra DC V ve I ölçün; güç, o yüke giden V·I'dir. Protokol: [experiments/002](../../experiments/002-watts-3mm-steel/README.md).
- Aşama 4 (düğüm): RX → GY-LTC3588 **doğrudan PZ1/PZ2'ye** (köprü, LTC3588-1'in içine yerleşiktir, harici köprü gerekmez) → 1 F süperkapasitör → ESP32 (derin uyku + görev döngüsü). Yük modülasyonu — 2N7002 + 100 Ω **DC tarafta** (modülün VIN pini, sch4'e bakın); AC piezo boyunca tek bir MOSFET çalışmaz — gövde diyodu bir yarım dalgayı kısa devre eder (docs/03).

ÖNEMLİ: TVS'i ilk güç verme öncesi takın — rezonansta açık bir piezo onlarca ila yüzlerce volt üretir. Köprüden sonraki DC tarafta — tek yönlü SMBJ5.0A; düğümün piezosu (AC) boyunca — yalnızca çift yönlü SMBJ15CA.
