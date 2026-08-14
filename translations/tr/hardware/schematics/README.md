# Test düzeneği şemaları

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · Türkçe · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Dosya | İçerik | Aşama |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | sürücü: IR2110 + 2×IRF540, bootstrap, eşleştirme transformatörü | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | alıcı: 4×SS14 köprü → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | pinout: Pi ↔ AD9833 ↔ piezo çifti ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | düğüm: RX → GY-LTC3588 → süperkapasitör → ESP32 (+ yük modülasyonu) | 4 |

Bunlar **breadboard-prototip** şemalarıdır (bileşen değerleri başlangıç noktalarıdır, osiloskopta ayarlanan yerler `*` ile işaretlenmiştir). Prototip bizzat doğrulandıktan sonra PCB yerleşimi içeren bir KiCad projesi gelecektir — [driver/README.md](../driver/README.md) dosyasında söz verildiği gibi.
