# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · [Italiano](../../../it/software/sweep-map/README.md) · [Polski](../../../pl/software/sweep-map/README.md) · [Türkçe](../../../tr/software/sweep-map/README.md) · [Українська](../../../uk/software/sweep-map/README.md) · [Tiếng Việt](../../../vi/software/sweep-map/README.md) · [中文](../../../zh/software/sweep-map/README.md) · [日本語](../../../ja/software/sweep-map/README.md) · [한국어](../../../ko/software/sweep-map/README.md) · हिन्दी

चैनल आवृत्ति प्रतिक्रिया का स्वीप मानचित्र। हार्डवेयर, वायरिंग और इसे चलाने के तरीके के लिए sweep_map.py के हेडर देखें।

परिवेश (हाल के Raspberry Pi OS रिलीज़ में venv आवश्यक है):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — केवल Pi पर
```

Pi पर: `raspi-config` → SPI और I2C सक्षम करें।

बिना हार्डवेयर के ड्राई रन, किसी भी कंप्यूटर पर (matplotlib पर्याप्त है):

```bash
python3 sweep_map.py --mock
```
