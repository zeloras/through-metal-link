# प्रयोग 002: 3 मिमी स्टील के पार पहले वाट (योजनाबद्ध)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · हिन्दी

- **चरण:** 2 ([001](../001-sweep-map-3mm-steel/README.md) में मिले अनुनाद पर एक ज्ञात लोड में शक्ति)।
- **लक्ष्य:** हाफ-ब्रिज ड्राइवर और मैचिंग ट्रांसफार्मर के साथ 3 मिमी स्टील के पार वितरित वास्तविक DC शक्ति को मापना।
- **परिकल्पना:** एक ही बैच के लैंगेविन जोड़े, ग्रीस+क्लैंप (या एपॉक्सी) संपर्क, और एक ट्यून किए गए मैचिंग ट्रांसफार्मर के साथ, चरण-1 शिखर पर एक प्रतिरोधी लोड में ≥0.5 W प्राप्त करना संभव है। (साहित्य के मल्टी-वाट/kW आंकड़े अलग ट्रांसड्यूसर और बॉन्डिंग का उपयोग करते थे — इन्हें ऊपरी सीमा मानें, पास-बार नहीं।)
- **पूर्व-आवश्यकताएँ:**
  - प्रयोग 001 बंद (प्रत्यावर्तनीय शिखर, आवृत्ति दर्ज)।
  - किसी भी ड्राइवर शक्ति से पहले RX श्रृंखला पर TVS लगाया गया ([docs/02-safety.md](../../docs/02-safety.md))।
  - ड्राइवर ब्रिंग-अप अनुक्रम का पालन किया गया ([hardware/driver/README.md](../../../../hardware/driver/README.md))।
- **सेटअप (न्यूनतम):**
  - TX: Pi → AD9833 square → dead-time shaper → IR2110 half-bridge → matching transformer → प्लेट पर क्लैंप किया गया लैंगेविन ([sch1](../../../../hardware/schematics/sch1-driver-halfbridge.png))।
  - दीवार: 3 मिमी स्टील, संपर्क विधि दर्ज (grease+clamp / epoxy / other)।
  - RX: लैंगेविन → Schottky bridge → ज्ञात R_load (पावर रेजिस्टर) और/या LED; ब्रिज के बाद V_dc और I_dc मापें ([sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) टोपोलॉजी, केवल-ADC के बजाय लोड)।
- **प्रक्रिया (रूपरेखा):**
  1. ध्वनिक शक्ति का दावा किए बिना 0.2 A PSU सीमा पर विद्युत ब्रिंग-अप।
  2. TX/RX को क्लैंप करें, ड्राइव आवृत्ति को प्रयोग-001 शिखर पर सेट करें।
  3. धीरे-धीरे धारा सीमा बढ़ाएँ; PSU V/I, MOSFET/ट्रांसफार्मर तापमान, लोड पर V_dc और I_dc लॉग करें।
  4. P_load = V_dc · I_dc। वैकल्पिक: P_load ज्ञात होने के बाद एक छोटा LED डेमो फोटो।
  5. ठंडा होने के बाद एक बार दोहराएँ; शिखर आवृत्ति तापमान के साथ बदल सकती है — यदि शक्ति गिरती है तो एक मिनी-स्वीप से फिर से जाँच करें।
- **सफलता के मानदंड:**
  1. एक प्रलेखित आवृत्ति और संपर्क विधि पर 3 मिमी स्टील के पार P_load ≥ 0.5 W।
  2. एक ही क्लैंप/कप्लैंट के तहत दो रन P_load पर ~20% के भीतर सहमत हों (परिमाण-क्रम स्थिरता, अभी तक मेट्रोलॉजी-ग्रेड नहीं)।
  3. LED (या अन्य लोड) का फोटो + CSV/लॉग इस फ़ाइल से `data/` के अंतर्गत लिंक किया गया।
- **विफलता भी डेटा है:** यदि P_load ≪ 0.5 W बनी रहती है, तो जोड़ी Δf (001 से), संपर्क विधि, ट्रांसफार्मर टर्न, और तरंगरूप लॉग करें — वह अगले ADR का इनपुट है, सिम्युलेटर को चुपचाप संपादित करने का कारण नहीं।
