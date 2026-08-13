# 선행 기술: 우리가 기반으로 삼는 것

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · 한국어 · [हिन्दी](../../hi/docs/01-prior-art.md)

## 규칙
이 저장소의 모든 기술적 결정은 "자유" 목록(만료 특허, 논문)의 출처로 추적 가능해야 한다. 유효 특허는 읽기 전용이다 — 문제에 대한 통찰을 캐내되, 그 청구항을 절대 복사하지 마라(이는 미국에서의 상용화에 중요하다; 프로젝트의 특허 지도를 참고하라).

## 자유 기반 (만료/포기된 특허 = 퍼블릭 도메인)
- **US5982297** (Aerospace Corp, 1997) — 기본 레시피: 벽을 통과하는 압전 소자 쌍, 전력 + 양방향 데이터. 메인 요리책.
- US5594705 (Dynamotive, 1994) — 선체를 통과하는 "음향 트랜스포머".
- US6037704, US6127942 (Aerospace Corp) — 센서에 전력 공급, 데이터를 다시 읽어냄.
- **US7902943** (Caltech/JPL, 유지비 미납으로 2019년 만료) — Sherrit 피드스루: 반사기, 음향 트랜스포머.
- US9748870 (Caltech/JPL) — 벽을 통한 기계적 일.
- **US9361877** (Univ. Oklahoma, 유지비 미납으로 만료) — 현대적인 완비형 트랜시버 시스템.
- US20100027379 / WO2008105947 (DOE+RPI, 포기) — 외부에서의 캐리어 + 내부에서의 부하 변조.

## 핵심 논문
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s, 63.5 mm 강철.
- Sherrit et al., NASA NTRS 20080048150 — 벽을 통해 전력을 공급받는 100 W 램프.
- Yang et al., Sensors 2015 (10.3390/s151229870) — 리뷰, 수치에 대한 최고 요약.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — 메타물질, 1 mm 스테인리스를 통과해 2%→66% (2026년 7월 기준 특허 없음).

이 논문들은 **물리학 및 특허 위생 기준선**이다. 여기에 사용된 전력/비트레이트 수치는 실험실 트랜스듀서, 본딩, 매칭을 기준으로 한 것이다 — [QUICKSTART.md](../QUICKSTART.md)의 알리익스프레스 Langevin + 그리스 BOM이 아니다. 이들을 존재 증명으로 인용하라; 프로젝트 자체의 통과 기준은 [experiments/](../../../experiments)에 있다.

## 유효한 동안 복사하지 않는 것 (미국 한정, ~2032년까지; 어차피 단계 1–4에는 필요 없음)
전력 채널의 고조파를 피하도록 배치된 서브캐리어를 가진 OFDM(RPI US9054826); 단일 방식으로서의 전이중 "AM 다운링크 + 부하 변조 업링크 + 주파수 추적"(RPI US9455791); Drexel 방식에 따른 곡면용 컨포멀 트랜스듀서(US10594409).
