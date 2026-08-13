# ADR-0001: Aşama 1 için Frekans Modu Seçimi

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · Türkçe · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Durum: KABUL EDİLDİ (Aşama 2'den sonra yeniden değerlendirilecek)
- Tarih: 2026-07-24

## Bağlam
İki mod mevcuttur (bkz. docs/00-theory.md): A — Langevin transdüserlerinde 28–40 kHz, B — duvarın kalınlık rezonansına binen disklerde 0.6–1 MHz.

## Karar
Aşama 1–2 mod A'da çalışır. Nedenleri: daha ucuz ($10–30 adet başına), daha güçlü (yüzlerce mW'a karşı watt), ayarlamaya daha hoşgörülü (geniş rezonans) ve sürücü bir IR2110 etrafındaki yarım köprü ile kurulabilir. Mod B, ilk watt'ları geçirdikten sonra gelir — yüksek hızlı veri için ayrı bir dal olarak.

## Sonuçlar
Aşama 3'teki veri yavaş olacaktır (kbit/s) — bir sensör düğümü için yeterli. ADS1115 ADC (860 SPS), doğrultucudan sonra 40 kHz'deki zarf için uygundur, ancak doğrudan örnekleme için değil — doğrudan örnekleme mod B'ye ertelenmiştir (farklı bir ADC gerektirir).

Aşama 1 (tarama) yalnızca zayıf DDS sürüşünü kullanır; aşama 2 (watt) ayrı bir deney ve kurulumdur ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)). Simülatör güç bantları, 002 ölçülene kadar hedef olarak kalır.
