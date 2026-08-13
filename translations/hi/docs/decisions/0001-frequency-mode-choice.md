# ADR-0001: स्टेज 1 के लिए फ़्रीक्वेंसी मोड चयन

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · हिन्दी

- स्थिति: स्वीकृत (स्टेज 2 के बाद पुनर्विचार किया जाएगा)
- तिथि: 2026-07-24

## संदर्भ
दो मोड (देखें docs/00-theory.md): A — लांगेविन ट्रांसड्यूसर पर 28–40 kHz, B — दीवार की मोटाई अनुनाद पर चलने वाले डिस्क पर 0.6–1 MHz।

## निर्णय
स्टेज 1–2 मोड A पर चलेंगे। कारण: सस्ता ($10–30 प्रति टुकड़ा), अधिक शक्तिशाली (वाट बनाम सैकड़ों mW), ट्यून करने में अधिक सहनशील (व्यापक अनुनाद), और ड्राइवर को IR2110 के चारों ओर एक हाफ-ब्रिज से बनाया जा सकता है। मोड B तब आएगा जब हम पहले वाट प्राप्त कर लेंगे — हाई-स्पीड डेटा के लिए एक अलग शाखा के रूप में।

## परिणाम
स्टेज 3 पर डेटा धीमा होगा (kbit/s) — एक सेंसर नोड के लिए पर्याप्त। ADS1115 ADC (860 SPS) रेक्टिफायर के बाद 40 kHz पर एनवेलप के लिए ठीक है, लेकिन सीधे सैंपलिंग के लिए नहीं — सीधे सैंपलिंग को मोड B में टाला गया है (एक अलग ADC की आवश्यकता है)।

स्टेज 1 (स्वीप) केवल कमजोर DDS ड्राइव का उपयोग करता है; स्टेज 2 (वाट) एक अलग प्रयोग और ब्रिंग-अप है ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md))। सिम्युलेटर पावर बैंड 002 मापे जाने तक लक्ष्य बने रहते हैं।
