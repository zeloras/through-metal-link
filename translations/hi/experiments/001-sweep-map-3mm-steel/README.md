# प्रयोग 001: चैनल स्वीप मानचित्र, 3 मिमी स्टील (योजनाबद्ध)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · हिन्दी

- **चरण:** 1 (केवल आवृत्ति मानचित्र — यहाँ कोई वाट लक्ष्य नहीं; शक्ति [002](../../../../experiments/002-watts-3mm-steel/README.md) में है)।
- **लक्ष्य:** 3 मिमी प्लेट के माध्यम से एक लांगेविन ट्रांसड्यूसर जोड़ी के अनुनाद को खोजें; चैनल की पहली आवृत्ति प्रतिक्रिया प्राप्त करें।
- **परिकल्पना:** लगभग 38–42 kHz के आसपास एक शिखर (लांगेविन ट्रांसड्यूसर अनुनाद), ग्रीस+क्लैम्प संपर्क के तहत कुछ kHz की शिखर चौड़ाई।
- **ड्राइव:** चरण-1 कनेक्शन — AD9833 साइन (~0.6 Vpp) TX में, **कोई** हाफ-ब्रिज नहीं ([sch3](../../../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png))।
- **प्रक्रिया:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (हार्डवेयर के बिना पाइपलाइन को ड्राई-रन करने के लिए `--mock` का उपयोग करें)।
- **सफलता मानदंड:** एक प्रतिलिप्शील शिखर (लगातार दो स्वीप, केंद्र विचलन <200 Hz)। CSV/PNG को `data/` के अंतर्गत सहेजें और जब वास्तविक हो तो उन्हें इस फ़ाइल से लिंक करें।
- **बोनस माप:** "ग्रीस कप्लेंट + क्लैम्प" बनाम "शुष्क प्रेस-ऑन" के साथ वही स्वीप — केवल सापेक्ष आयाम; पूर्ण वोल्ट ड्राइव स्तर पर निर्भर करते हैं और अंशांकन तक सिम्युलेटर के प्लेसहोल्डर स्केल से तुलनीय नहीं हैं।
- **दायरे से बाहर:** ≥0.5 W, LED-फ्रॉम-हार्वेस्ट, हाफ-ब्रिज ब्रिंग-अप → प्रयोग 002।

>>>
