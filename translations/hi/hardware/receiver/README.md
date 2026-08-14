# रिसीवर

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · [中文](../../../zh/hardware/receiver/README.md) · [日本語](../../../ja/hardware/receiver/README.md) · [한국어](../../../ko/hardware/receiver/README.md) · हिन्दी

स्कीमैटिक्स: [स्टेज 1 — sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) · [स्टेज 4 — sch4](../../../../hardware/schematics/sch4-receiver-node.png) ([../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py) द्वारा जनित)

- स्टेज 1 (माप): लैंजेविन ट्रांसड्यूसर RX (दोनों लीड फ्लोटिंग — ग्राउंड न करें!) → शॉट्की ब्रिज (4×SS14) → RC फ़िल्टर (10k || 100n) → 5 V TVS → **47 kΩ श्रृंखला में** → ADS1115 A0 (यह रेज़िस्टर ADC के सुरक्षा डायोड में जाने वाली धारा को सीमित करता है: TVS इनपुट के निरपेक्ष अधिकतम से लगभग 9 V ऊपर क्लैंप करता है)।
- स्टेज 2 (वाट): RX → वही ब्रिज → ज्ञात प्रतिरोधी लोड (और/या LED), ब्रिज के बाद DC V और I मापें; शक्ति उस लोड में V·I है। प्रोटोकॉल: [experiments/002](../../experiments/002-watts-3mm-steel/README.md)।
- स्टेज 4 (नोड): RX → GY-LTC3588 **सीधे PZ1/PZ2 में** (ब्रिज LTC3588-1 के अंदर ही बना है, किसी बाहरी ब्रिज की आवश्यकता नहीं) → 1 F सुपरकैपेसिटर → ESP32 (डीप स्लीप + ड्यूटी साइकल)। लोड मॉड्यूलेशन — 2N7002 + 100 Ω **DC साइड** पर (मॉड्यूल का VIN पिन, sch4 देखें); AC पीज़ो के आरपार एकल MOSFET काम नहीं करता — बॉडी डायोड एक अर्ध-तरंग को शंट कर देता है (docs/03)।

महत्वपूर्ण: पहली बार पावर ऑन करने से पहले TVS लगाएँ — अनुनाद पर खुला पीज़ो दसियों से सैकड़ों वोल्ट देता है। ब्रिज के बाद DC साइड पर — एक यूनिडायरेक्शनल SMBJ5.0A; नोड के पीज़ो (AC) के आरपार — केवल एक बायडायरेक्शनल SMBJ15CA।
