# data/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · [Español](../../es/data/README.md) · [Français](../../fr/data/README.md) · [Italiano](../../it/data/README.md) · [Polski](../../pl/data/README.md) · [Türkçe](../../tr/data/README.md) · [Українська](../../uk/data/README.md) · [Tiếng Việt](../../vi/data/README.md) · [中文](../../zh/data/README.md) · [日本語](../../ja/data/README.md) · [한국어](../../ko/data/README.md) · हिन्दी

कच्चे मापन लॉग: `software/sweep-map/sweep_map.py` से प्राप्त CSV और PNG आउटपुट।

- फ़ाइल नामों में एक UTC टाइमस्टैम्प होता है: `sweep_25000-45000_20260801T120000Z.csv`।
- CSV/PNG फ़ाइलें git से बाहर रखी जाती हैं (`.gitignore` देखें) — ये बड़ी और पुनरुत्पादनीय होती हैं; केवल चुने हुए प्लॉट्स ही git में जाते हैं, जिन्हें संबंधित प्रयोग की डायरेक्टरी `experiments/NNN-*/` में कॉपी किया जाता है।

मॉक-मोड रन (`sweep_map.py --mock`) भी यहाँ लिखते हैं — उन फ़ाइलों को किसी भी समय सुरक्षित रूप से हटाया जा सकता है।
