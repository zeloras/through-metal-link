# QUICKSTART: sıfırdan 1.–2. aşama test düzeneğine

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · [Português](../pt/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · [Français](../fr/QUICKSTART.md) · [Italiano](../it/QUICKSTART.md) · [Polski](../pl/QUICKSTART.md) · Türkçe · [Українська](../uk/QUICKSTART.md) · [Tiếng Việt](../vi/QUICKSTART.md) · [中文](../zh/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [한국어](../ko/QUICKSTART.md) · [हिन्दी](../hi/QUICKSTART.md)

Senaryo: elinizde sadece bir masa ve biraz para var. Aşağıdaki her şey sizi çalışan bir düzeneğe götürür — "tarama haritası + çelikten geçen ilk watt'lar". Fiyatlar yaklaşık, USD cinsindendir.

## Sepet 1 — aletler (yıllarca sürecek bir temel, ~$120)

| Ürün | Neden | Fiyat | Nereden |
|---|---|---|---|
| Lehimleme istasyonu (T12 klonu) | her şey | 35–50 | Ali |
| Multimetre (AN8008/UT61 sınıfı) | voltajlar, süreklilik, kapasitans | 15–25 | Ali |
| Akım sınırlamalı masa PSU 30V/5A | sürücüyü besler; akım limiti, yanık MOSFET'lere karşı sigortanızdır | 45–60 | Ali/yerel |
| Yardımcı eller, lehim, flux, leim sökme örgüsü, yan keski, cımbız | onsuz yapılamayan küçük şeyler | 15 | Ali/yerel |
| Dupont kablolar + breadboard + ısı büzülmüş kılıf | prototipleme | 8 | Ali |

## Sepet 2 — düzenek elektronigi (~$70)

| Ürün | Adet | Fiyat | Not |
|---|---|---|---|
| Raspberry Pi (Zero 2 W yeterli; 4/5 daha rahat) + SD | 1 | 20–60 | beyin: tarama, loglar, grafikler |
| Langevin transdüser 40 kHz 50–60 W | **4** | 40 | tek partiden 4 adet alın; taramayla en iyi çifti seçeceğiz |
| AD9833 DDS modülü | 2 | 8 | ikincisi yedek |
| IR2110 + IRF540 ×4 (veya bir EGS002 modülü) | 1 set | 10 | sürücü half-bridge |
| ADS1115 ADC | 2 | 4 | Pi'nin kendi ADC'si yok |
| Ferrit toroid + 0.5 mm manyetik tel | 2 | 4 | eşleştirme transformatörü |
| Schottky köprü (SS14 ×8), süperkapasitör 1F 5.5V ×2 | 1 | 4 | alıcı zinciri |
| TVS SMBJ5.0A ×3 + SMBJ15CA ×2 | 1 | 2 | koruma. CİMRİ DAVRANMAYIN |
| GY-LTC3588 modülü | 1 | 7 | hasat edici (aşama 4, ama şimdi sipariş etsin) |
| Direnç/kapasitör seti, LED'ler | 1 | 8 | hiçbir şeyiniz yoksa |
| Destek pasifleri: UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | kuruşlar; tam liste — BOM kalemleri 11–12 |

## Sepet 3 — mekanik (~$20, yerel)

3 mm çelik plaka ~150×150 — 2 adet (metal hırdavatçı / lazer kesim); F-tipi kelepçe ×2; kalın homojen gres akışkan (lityum gres); epoksi; zımpara (temas bölgesini temizlemek için).

## Opsiyonel, ama güçlükle tavsiye edilir (~$90)

| Ürün | Neden | Fiyat |
|---|---|---|
| USB/el osiloskobu (FNIRSI/Hantek, 2 kanal; ≥40 MHz bant genişliğine ihtiyacınız yok — 10 yeterli) | gate'teki ve piezo'daki dalga formunu görün; günlerce süren sürücü hata ayıklamasını kurtarır | 60–80 |
| ESP32 DevKit ×2 | aşama 4 (duvarın arkasındaki düğüm) | 8 |

**Toplam: asgari ~$210, rahat ~$300.** (Eğer zaten bir Pi'niz, lehimleme istasyonunuz ve masa PSU'nuz varsa — ~$120 çıkarın.)

## Satın alma emri (kritik yol nakliyedir)

1. Bugün: Ali'den sepet 2 (3–4 hafta nakliye — kritik yol budur) + osiloskop.
2. Bu hafta: sepet 1 ve 3 yerel olarak.
3. Nakliye sürerken: `raspi-config` → SPI+I2C, donanım olmadan `software/sweep-map/sweep_map.py --mock` çalıştırın (sentetik kanal — tüm CSV+grafik boru hattı herhangi bir bilgisayarda çalışır), docs/00–03 okuyun, docs/img'deki beklenti grafiklerine ve hardware/schematics'teki şemalara bakın (aşama 1 yapımı sch3 ve sch2'yi izler).

## Göreceğiniz şey (simülatör: software/simulator/channel_sim.py → docs/img)

Bu PNG'ler **model beklentileridir**, laboratuvar ölçümleri değil. Temas oranları, yüklenmiş Q≈40 ve zincir verimi ≤40%, `channel_sim.py` içinde açık varsayımlardır — düzenek kurulduğunda bunları tarama/güç verileriyle değiştirin.

- `sim0-rig-sketch.png` — tüm düzenek tek çizimde (aşama 2 zinciri; aşama 1, half-bridge'i atlar ve TX'i zayıf DDS sinüsünden sürer).
- `sim1-sweep-contacts.png` — beklenen tarama şekli: ~40 kHz yakınında dar bir tepe; model, yer tutucu olarak gres:kuru:boşluk ≈ 1 : 0.25 : 0.02 kullanır. Tepe yoksa — önce teması veya çift uyumsuzluğunu hata ayıklayın (sim2).
- `sim2-pair-mismatch.png` — neden 2 değil de 4 Langevin transdüser: Q≈40 ile bir çift içindeki 1.5 kHz rezonans uyumsuzluğu model gücünü ~10× düşürür; tarama 4 içinden en iyi çifti seçer.
- `sim3-thickness-comb.png` — daha sonra için (mod B, MHz): plaka, kalınlık rezonansları taradığı gibi şeffaftır, bu yüzden frekans takip edilmelidir.
- `sim4-power-budget.png` — yük çekimi ile **hedef** alınan-güç bantları karşılaştırması. Mod A bandı (0.5–5 W), eşleştirme ve temas işbirliği yaparsa aşama 2 hedefidir; mod B daha alt bandır. Sürekli Wi-Fi bir tepe-yük işaretidir, bir vaat değil — görev-döngülü ESP32/BLE/LED gerçekçi ilk tüketicilerdir.
- `sim5-ook-datarate.png` — aşama 3: Langevin transdüserlerde OOK'un Q≈40 altında neden ~1–2 kbit/s'te tavan yaptığı (ring-down τ≈0.3 ms) ve bunun bir sensör düğümü için neden yeterli olduğu.

## "Düzenek çalışıyor" kriterleri

Aşamaya göre ayrılmış — aşama 1'i aşama 2 sayılarıyla tamamlanmış saymayın.

**Aşama 1 — tarama haritası** ([experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md)):
1. Ardışık iki çalıştırmada 25–45 kHz tarama: tepe merkezi <200 Hz içinde tekrarlanır.
2. Opsiyonel bonus: aynı çiftte gres+kelepçe vs kuru basınç (göreli genlikler, mutlak watt değil).

**Aşama 2 — ilk watt'lar** ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)):
1. Half-bridge + eşleştirme transformatörü çalışır durumda; [docs/02-safety.md](../../docs/02-safety.md) ve [hardware/driver/](../../hardware/driver/README.md) uyarınca PSU akım-sınırlı devreye alma.
2. Aşama 1 rezonansında, 3 mm çelikten bilinen bir dirençli yüke ≥0.5 W (RX köprüsünden sonra DC tarafında V ve I ölçün).
3. Plakanın arkasındaki LED, hasat edilen güçten yanar; foto + CSV experiments/002'de.

İlk güç verme öncesi güvenlik: [docs/02-safety.md](../../docs/02-safety.md) (alıcıda TVS, devreye alma için PSU akım limiti 0.2 A, havada yüksek güçlü Langevin çalıştırma yok).
