# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · [Italiano](../../../it/software/sweep-map/README.md) · [Polski](../../../pl/software/sweep-map/README.md) · [Türkçe](../../../tr/software/sweep-map/README.md) · [Українська](../../../uk/software/sweep-map/README.md) · [Tiếng Việt](../../../vi/software/sweep-map/README.md) · [中文](../../../zh/software/sweep-map/README.md) · [日本語](../../../ja/software/sweep-map/README.md) · 한국어 · [हिन्दी](../../../hi/software/sweep-map/README.md)

채널 주파수 응답의 스윕 맵입니다. 하드웨어, 배선 및 실행 방법은 sweep_map.py의 헤더를 참조하세요.

환경 설정 (최신 Raspberry Pi OS 릴리스에서는 venv가 필요합니다):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — Pi 전용
```

Pi에서: `raspi-config` → SPI와 I2C를 활성화하세요.

하드웨어 없이 드라이 런, 아무 컴퓨터에서 (matplotlib만 있으면 됩니다):

```bash
python3 sweep_map.py --mock
```
