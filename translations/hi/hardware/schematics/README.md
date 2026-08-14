# टेस्ट-रिग योजनात्मक चित्र

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · हिन्दी

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| फ़ाइल | क्या | चरण |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | ड्राइवर: IR2110 + 2×IRF540, बूटस्ट्रैप, मैचिंग ट्रांसफार्मर | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | रिसीवर: 4×SS14 ब्रिज → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | पिनआउट: Pi ↔ AD9833 ↔ पीज़ो पेयर ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | नोड: RX → GY-LTC3588 → सुपरकैपेसिटर → ESP32 (+ लोड मॉड्यूलेशन) | 4 |

ये **ब्रेडबोर्ड-प्रोटोटाइप** स्कीमैटिक्स हैं (कॉम्पोनेंट वैल्यूज़ शुरुआती बिंदु हैं, जहाँ उन्हें ऑसिलोस्कोप पर ठीक किया जाता है वहाँ `*` से चिह्नित किया गया है)। PCB लेआउट के साथ KiCad प्रोजेक्ट तब आएगा जब प्रोटोटाइप व्यवहार में सत्यापित हो जाए — जैसा कि [driver/README.md](../driver/README.md) में वादा किया गया है।
