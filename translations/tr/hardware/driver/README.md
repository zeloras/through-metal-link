# Sürücü (aşama 2): IR2110 half-bridge

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · Türkçe · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Şematik:** [../schematics/sch1-driver-halfbridge.png](../../../../hardware/schematics/sch1-driver-halfbridge.png) ([../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py) tarafından üretilmiştir)

Zincir: Pi (SPI) → AD9833 **kare dalga modunda** (OPBITEN biti: MSB çıkışa yönlendirilir, rail-to-rail salınım — ayrı komparatöre gerek yok) → **74HC14 + RC + 1N4148** şekillendirici (~1 µs ölü zaman ile tamamlayıcı HIN/LIN) → IR2110 → 2×IRF540 (half-bridge) → 1 µF DC-bloke kapasitör → eşleştirme transformatörü (ferrit, ~1:3..1:5, tezgâhta ayarlayın) → Langevin transdüser TX.

AD9833'ün sinüs çıkışı (~0.6 Vpp) IR2110 mantığı için uygun değildir — herhangi bir nedenle DDS'ten özellikle sinüs çıkışı almanız gerekiyorsa, aralarına bir komparatör koyun (örneğin LM393, BOM'da yoktur).

Güç katı beslemesi: Akım sınırlamalı 12–24 V tezgâh PSU (**0.2 A'den başlayın**).

Not: 1. aşama taraması piezo'yu zayıf DDS sinüsüyle doğrudan sürer (~0.6 Vpp, bkz. `sweep_map.py`) — **bu sürücü zincire yalnızca 2. aşamada (watt) girer**. 1. aşama DDS-only bağlantısından ≥0.5 W beklemeyin.

Notlar:
- Langevin transdüser kapasitif bir yüktür (tipik olarak birkaç nF). Seri endüktör veya eşleştirme transformatörü zorunludur; olmadan MOSFET'ler reaktif akımı yayarak bozulur.
- **Eşleştirme transformatörü (genel arıza noktası).** Küçük bir ferrit toroid ile başlayın (örn. FT50-43 / benzeri), primer birkaç sipir, sekonder ~3–5×, primerde seri DC-bloke 1 µF film kapasitör. TX **plakaya kelepçelenmiş** ve RX yüklü iken *1. aşama rezonansında* minimum PSU akımı için ayarlayın. Sipir oranı ve kaçak ampiriktir — şematik bunları `*` ile işaretler, sebebi vardır. Son sipir sayısını deney günlüğüne kaydedin.
- **Ölü zaman**: IR2110 bunu kendi başına üretmez. Ayrık parçalı seçenek — 74HC14 girişlerinde RC+1N4148 (yalnızca yükselen kenarları geciktirir, ~1 µs; 40 kHz'de 25 µs periyotla bu <%5 kayıptır). Kolay seçenek — bir EGS002 modülü, her şey içinde hazır.
- **3.3 V mantık**: IR2110'un VDD'sini AD9833 ve 74HC14 ile aynı 3.3 V'dan besleyin — VDD=5 V'da VIH eşiği ≈ 3.1 V'dir ve 3.3 V kare dalga ancak ancak geçer (veri sayfası VDD'yi 3.3 V'a kadar izin verir).
- **Decoupling zorunludur**: VDD ve VCC'de 100 nF (VCC — ek olarak 47 µF), ve güç hattında half-bridge bacaklarının tam yanında 470–1000 µF + 100 nF seramik — bunlar olmadan, breadboard jumper'lardaki bir half-bridge kendi anahtarlama sivri uçlarını yakalar. Güç döngüsü kablolarını kısa tutun; switch node kötü ring ediyorsa, akımı artırmadan önce breadboard'tan bakır kaplı dead-bug / protoboard ground pour'a geçin.
- **İlk güç verme sırası** ([docs/02-safety.md](../../docs/02-safety.md) ile uyumlu):
  1. Sekonderde henüz Langevin yok. PSU = 12 V, akım limiti 0.2 A. Osiloskopla gate sürüşünü (HIN/LIN) ve switch node'u kontrol edin — ölü zamanı ve shoot-through olmadığını doğrulayın.
  2. Eşleştirme transformatörü + TX Langevin **çelik plakaya kelepçelenmiş** (veya kalın kurban metal bloğa) takın. Hâlâ 0.2 A limiti. Yalnızca 1. aşama tepe frekansında akımı ve RX voltajını görmek için kısa süre çalıştırın.
  3. MOSFET ve transformatör sıcaklığını izlerken akım limitini kademeli olarak artırın. Kelepçelenmemiş Langevin'i güç altında asla bırakmayın — serbest havada tam güç çalıştırmak seramiklerin çatlamasına ve sürücülerin ölmesine yol açar.

TODO: Breadboard (veya dead-bug) prototip doğrulandıktan sonra KiCad projesi (PCB). O zamana kadar [`../schematics/`](../../../../hardware/schematics) içindeki şematikler tasarımın asıl kaynağıdır.
