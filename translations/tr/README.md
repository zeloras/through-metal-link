# metal-ici-baglanti

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · Türkçe · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Katı metal duvarlardan ultrasonik güç ve veri aktarımı için açık bir platform — "tek bir delik açmadan çelikten geçen", garaj düzeyinde araçlarla geliştirilmiştir.

**Hemen deneyin (donanım gerekmez):** `python3 software/sweep-map/sweep_map.py --mock`

**Durum:** aşama 0 — hazırlık · 💰 **[Bağımsız ilk kurulum için $250 ödül](https://github.com/zeloras/through-metal-link/issues)** · alışveriş listesi: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

Belgeler çok dillidir: İngilizce birincil dildir ve standart yollarda bulunur; diğer tüm diller ağacı [translations/](..) altında yansıtır. Herhangi bir dili düzenleyin — CI kalanını çevirir ve işler (bkz. [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="../../docs/img/sim0-rig-sketch.png" alt="Aşama 1 düzeneği: Pi → DDS → half-bridge → transformatör → piezo TX | çelik | piezo RX → köprü → ADC → Pi" width="900"></p>

## Fikir tek paragrafta

Radyo dalgaları metalden geçmez (Faraday kafesi) ve bir kablo geçişi; bir delik, bir conta ve bir arıza noktası demektir. Öte yandan ultrason, metalden gayet iyi geçer: duvarın her iki tarafındaki birer piezo eleman, onu güç ve veri için bir kanala dönüştürür. Laboratuvar literatürü, fiziği ciddi seviyelerde zaten kanıtladı (RPI: 63,5 mm çelikten 50 W + 12 Mbit/s; NASA JPL: 5 mm titanyumdan ~kW'a kadar) — bunlar özel donanımla yapılmış varlık kanıtlarıdır, bu deponun garaj BOM'u değildir. Temel patentlerin süresi doldu ve henüz açık, tekrarlanabilir bir platform mevcut değil — bu depo, 2. aşama ölçüldüğü andan itibaren **3–5 mm çelikten watt sınıfı güç ve kbit/s veri** ile başlayarak bir tane inşa ediyor.

## Yol haritası

| Aşama | Çıktı | Başarı kriteri | Beklenti |
|---|---|---|---|
| 1. Tarama haritası | "Langevin–3 mm çelik–Langevin" kanalının frekans tepkisi | rezonans çifti bulundu, grafik [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) içinde | [sim1](../../docs/img/sim1-sweep-contacts.png), [sim2](../../docs/img/sim2-pair-mismatch.png) |
| 2. Watt | rezonansta yüke giren güç | 3 mm çelikten ≥0.5 W, protokol [experiments/002](experiments/002-watts-3mm-steel/README.md) içinde | [sim4](../../docs/img/sim4-power-budget.png) |
| 3. Veri | aynı çift üzerinden FSK/OOK | ≥1 kbit/s hatasız | [sim5](../../docs/img/sim5-ook-datarate.png) |
| 4. Düğüm | kaynakla kapatılmış kutuda ESP32 + sensör, yalnızca sesle güçlandırılan ve telemetri yapılan | ≥1 sa otonom çalışma | [sim4](../../docs/img/sim4-power-budget.png) |
| 5. Yayın | repo herkese açık hale gelir, makale/nasıl yapılır | üçüncü bir taraf tarafından çoğaltma | — |

## Depo haritası

python3 software/sweep-map/sweep_map.py --mock
```

**Ne zaman biter (aşamaya göre):** aşama 1 — tarama tepe noktası iki çalıştırmada <200 Hz içinde tekrarlanır ([experiments/001](experiments/001-sweep-map-3mm-steel/README.md)); aşama 2 — 3 mm çelikten bilinen bir yüke ≥0.5 W ve RX tarafından yanan bir LED ([experiments/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Bir dakikada teori</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

Piezo TX duvara bastırılır ve içine bir boyuna dalga sürülür; diğer taraftaki piezo RX bunu tekrar elektriğe çevirir. Çelikteki ses hızı: ~5900 m/s.

İki çalışma modu:

| Mod | Frekans | Rezonansı belirleyen | Verim | Durum |
|---|---|---|---|---|
| **A** — Langevin transdüserler | 40 kHz | transdüser çifti (duvar ≪ λ — bir "zar") | watt, kbit/s | başlangıç modu (aşamalar 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — diskler | 0.6–1 MHz | duvarın kalınlık rezonansı ([tarak](../../docs/img/sim3-thickness-comb.png)) | yüzlerce mW, yüzlerce kbit/s | ilk watt'lardan sonra dallanır; otomatik frekans takibi gerektirir |

Ana kayıplar: çift içindeki rezonans uyuşmazlığı (ucuz Langevin transdüserler için ±1 kHz), akustik temas kalitesi (epoksi > gres kuplaj + kelepçe > kuru basınç), hizalama hatası, sıcaklıkla rezonans kayması. Hepsinin cevabı aynıdır: **kurulumdaki her değişiklikten önce bir tarama haritası**.

</details>

<details>
<summary><b>📈 Düzeneğin göstermesi gerekenler: simülatörden beklenti grafikleri</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Yarı ampirik bir kanal modeli (FEM değil, **laboratuvar verisi değil** — "taramanın nasıl görünmesi gerektiği ve neye nişan alınması gerektiği" konusunda sezgi). Varsayımlar `channel_sim.py` içinde açıktır (yüklenmiş Q≈40, temas k-faktörleri, zincir η≤40%). Şununla yeniden oluşturun: `python3 channel_sim.py --out ../../docs/img`.

**Aşama 1 — tarama.** ~40 kHz yakınında dar bir tepe noktası; modelin yer tutucu temas çarpanları gres:kuru:boşluk = 1 : 0.25 : 0.02'dir (yani gres ≈4× kuru ve ≈50× hava boşluğu). Tepe noktası olmaması, temas veya çiftle ilgili bir sorun olduğu anlamına gelir:

<img src="../../docs/img/sim1-sweep-contacts.png" width="720">

**Neden 2 değil 4 Langevin transdüser.** Q≈40 altında, çift içindeki 1.5 kHz rezonans uyuşmazlığı model gücünü ~10× düşürür:

<img src="../../docs/img/sim2-pair-mismatch.png" width="720">

**Aşama 3 — veri.** OOK, rezonatör zırlamasına çarpar (model Q~40 → τ≈0.3 ms): 1 kbit/s temizdir, 5 kbit/s'de göz kapanır. Daha hızlı gitmek mod B gerektirir:

<img src="../../docs/img/sim5-ook-datarate.png" width="720">

**Alıcı güç bütçesi.** Gölgeli bantlar **hedeflerdir** (aşama 2 gerçekleşirse mod A 0.5–5 W; mod B daha düşük). Gerçekçi ilk yükler görev döngülü ESP32 / BLE / LED'dir; Wi-Fi sürekli bir vaat olarak değil, bir tepe-çekiş işaretçisi olarak gösterilir:

<img src="../../docs/img/sim4-power-budget.png" width="720">

**Daha sonra için (mod B).** Plaka, bir kalınlık rezonansları tarağında şeffaflaşır — frekansın takip edilmesi gerekir:

<img src="../../docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Güvenlik — ilk güç vermeden önce okuyun</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Piezo üzerinde onlarca ila yüzlerce volt** aşama 2 sürücüsü çevrimiçi olur olmaz — alıcı tarafındaki TVS, ilk güçlü çalıştırmadan ÖNCE takılır; kablolarına dokunmayın.
2. **Şebeke** — yalnızca bir masaüstü güç kaynağı / izolasyon üzerinden; ultrasonik temizleyici sürücü kartları şebekeye galvanik olarak bağlıdır.
3. **Kulaklar** — önemli olmayan bir güçte, transdüserleri metale bastırılmış halde çalıştırın; yüksek güçlü hava yüklü ultrasonu hiçbir zaman bir muhafaza olmadan çalıştırmayın.
4. **Isı** — kelepçelenmemiş bir Langevin transdüser güçte dakikalar içinde aşırı ısınır; akımı artırmadan önce kelepçeleyin (yalnızca kısa düşük akımlı elektriksel devreye alma — sürücü README'sine bakın).
5. **Kırıklar** — piezoseramik kırılgandır: fazla sıkılmış bir cıvata veya bir darbe kırık anlamına gelir; herhangi bir mekanik çalışma için güvenlik gözlüğü takın.

</details>

docs/            teori, öncül çalışmalar, güvenlik, uygulamalar, karar günlüğü (ADR)
docs/img/        beklenti grafikleri (software/simulator/channel_sim.py tarafından üretilir)
hardware/        BOM, sürücü (yarım köprü), alıcı (doğrultucu/hasat edici)
firmware/        düğüm bellenimi (ESP32 — 4. aşamaya kadar taslak)
software/        ölçüm betikleri (frekans-tepkisi tarama haritası) ve kanal simülatörü
experiments/     deney protokolleri — şablondan, bir dizin = bir deney
data/            ham günlükler (büyük dosyalar git'e girmez)
```

</details>

## İlkeler

1. **Sıfırdan tekrar üretilebilirlik.** Havyası ve ~210$'ı olan herkes, yalnızca bu repodan yola çıkarak sonucu tekrar üretebilir.
2. **Her deney bir protokoldür.** "Yaklaşık çalıştı" yok: [experiments/TEMPLATE.md](experiments/TEMPLATE.md) zorunludur.
3. **Patent hijyeni.** Süresi dolmuş katmanın üzerine inşa ediyoruz ([docs/01-prior-art.md](docs/01-prior-art.md)); kararlar [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md) altında kayıt altına alınır.
4. **Önce ölçüm, sonra görüş.** Kanal hakkında herhangi bir sonuca varmadan önce bir tarama haritası çıkarılır.

## Lisanslar ve patentler

Kod — Apache-2.0, donanım — CERN-OHL-W v2, dokümantasyon — CC-BY-4.0; tam metinler [LICENSES/](../../LICENSES) içindedir. Herkes bunu çatallayıp geliştirebilir, ticari kullanım dahil; patent koruması, lisanslardaki izin ve misilleme maddelerine ek olarak bir öncül buluş stratejisinden gelir. Tam plan ve savunmacı yayın protokolü: [LICENSES.md](LICENSES.md); katkı kuralları: [CONTRIBUTING.md](CONTRIBUTING.md).
