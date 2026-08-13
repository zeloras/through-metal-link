# Kanal teorisi (çalışmak için bilmeniz gereken asgari düzey)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · [Deutsch](../../de/docs/00-theory.md) · [Português](../../pt/docs/00-theory.md) · [Español](../../es/docs/00-theory.md) · [Français](../../fr/docs/00-theory.md) · [Italiano](../../it/docs/00-theory.md) · [Polski](../../pl/docs/00-theory.md) · Türkçe · [Українська](../../uk/docs/00-theory.md) · [Tiếng Việt](../../vi/docs/00-theory.md) · [中文](../../zh/docs/00-theory.md) · [日本語](../../ja/docs/00-theory.md) · [한국어](../../ko/docs/00-theory.md) · [हिन्दी](../../hi/docs/00-theory.md)

## İlke
Duvara bastırılmış/yapıştırılmış bir TX piezo elemanı duvar içinde boyuna dalga uyarır; diğer taraftaki bir piezo RX bunu tekrar elektriğe çevirir. Duvar bir rezonatördür: kalınlık rezonanslarında (yarım dalga boyunun katları) iletim maksimumdur.

## Temel sayılar
Çelikte boyuna ses hızı: ~5900 m/s.

| Çelik kalınlığı | Yarım-dalga rezonansı |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Çelikte dalga boyu: 40 kHz'de 148 mm; 1 MHz'de 5.9 mm.

## İki mod
- **A (40 kHz, Langevin transdüserler).** 3–5 mm plaka ≪ λ — membran gibi davranır; rezonans duvar tarafından değil transdüser çifti tarafından belirlenir. Mod B'den daha basit ve daha güçlüdür — başlangıç için tercih edilmesi gereken mod. Laboratuvar varlık kanıtı (garaj hedefi değil): NASA JPL ~24.5 kHz, özel donanımla 5 mm Ti üzerinden W'dan kW'a kadar yüzlerce W.
- **B (0.6–1 MHz, diskler).** Duvarın kendi kalınlık rezonansı, üstelik keskin olanı (~%6 frekans kayması ⇒ Fabry–Perot modelinde iletim ~10× düşer). RPI/Moss sınıfı sonuçlar: laboratuvar koşullarında yapıştırma ve eşleştirme ile yüzlerce mW artı yüzlerce kbit/s veri. Otomatik frekans takibi gerektirir.

## Ana kayıplar
Transdüser çifti içindeki rezonans uyumsuzluğu (ucuz Langevin transdüserler ±1 kHz dağılır), akustik temasın kalitesi (epoksi > kalın gres kuplan + kelepçe > kuru basınç), hizalama hatası, sıcaklıkla rezonans kayması. Bunların tümüne yanıt aynıdır: kurulumda her değişiklikten önce bir tarama haritası çalıştırın.

## Duvar ve arkasındaki medya üzerindeki etki

Kısa versiyon: platform güç seviyelerinde duvar ve arkasındaki herhangi bir gaz dokunulmamış durumdadır. Duvarın arkasındaki bir sıvı asıl olarak *kanalı* etkiler; kanal *sıvıyı* yalnızca kavitasyon eşiğine yakın etkilemeye başlar. Aşağıdaki kabaca sayılar mod A içindir: 40 kHz, 3 mm çeliğe ~1 W/cm².

**Duvar — hiçbir zaman deformasyon, hiçbir zaman yorulma.** Parçacık hızı v = √(2I/ρc) ≈ 21 mm/s ⇒ yer değiştirme ≈ 80 nm, düzlem dalga gerinimi ε = v/c ≈ 3.5·10⁻⁶. İki eşdeğer gerilme tahmini: elastik E·ε ≈ 0.7 MPa (E ≈ 200 GPa) ve akustik p = Z·v ≈ 1.0 MPa (Z_steel ≈ 4.6·10⁷ Pa·s/m). Çelik 250+ MPa'da akar ve yorulma dayanım limiti ~200 MPa'dır — her iki durumda da >200× marjın mevcut ve dayanım limitinin altında çelik sınırsız döngü alır. Mekanik olarak kırılgan parçalar başka yerdedir: piezo seramik (kırılgan, aşırı ısındığında kutuplaşmasını yitirir) ve yapıştırma hattı (epoksi önce ısınır ve yorulur) — bkz. [02-safety](../../../docs/02-safety.md).

**Duvarın arkasındaki gaz — sıfır etki.** Çelik→hava empedans uyumsuzluğu (~4.6·10⁷ vs ~400 Pa·s/m) gücün 10⁻⁵ mertebesinde bir kısmını iletir. Ölçülebilir ısınma veya çalkalanma yok; mühürlü bir kutunun içindeki elektronikler nm ölçeğindeki duvar hareketini fark etmez.

**Duvarın arkasındaki sıvı — iki yön:**

- *Sıvı → kanal (her zaman).* Su karşı yüzeyi ~1.5 MRayl ile yükler (hava yerine): gücün bir kısmı sıvıya yayılır, Q düşer, tarama tepe noktası kayar ve genişler. Mod B en çok etkilenir — kalınlık-rezonans tarağı çelik–hava sınırları için hesaplanır ve sıvı yüklemesiyle yer değiştirir. Geçerli kural bunu kapsar: **gerçek, tam kap karşı yeniden tarama yapın**, boş bir kaba karşı alınmış taramaya asla güvenmeyin. Yan fayda: sıvı sönümlemesi rezonatör zil sesini (τ) kısaltır, böylece OOK gözü daha yüksek bit hızlarında açılır. Yoldaki kabarcıklar (fermente sıvı!) güçlü saçılım yapar — [04-hybrid-channels](../../../docs/04-hybrid-channels.md) içindeki geçici çözüme bakın.
- *Kanal → sıvı (yalnızca yüksek güçte).* Suya yayılan tepe basınç: p ≈ ρc·v ≈ 1.5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0.3 atm. 40 kHz'de normal (gazlı) suda eylemsizlik-kavitasyon eşiği ~1–2 atm'dir, dolayısıyla 1 W/cm²'de marj 3–10×'tir. Ama p √gücü ile büyür ve kapalı bir kapta duran dalgalar yerel sıcak noktalar yaratır — sıvı dolu bir tanka sürekli onlarca W/cm² eşiğe ulaşabilir. Eşiği aşmak CO₂ gazından arınma, sonokimya (gıda ürünlerinde istenmeyen tatlar) ve iç yüzeyin uzun süreli kavitasyon erozyonu (ultrasonik temizleyicilerin tam olarak nasıl temizlediği) anlamına gelir. Sıvı destekli duvarlara sürekli güç için pratik tavan: **≲1 W/cm²**. Mod B muaf: MHz'de eşnek bir merteb daha yüksektir ve güçler yüzlerce mW'dır.

## Alıcı güç bütçesi (kabaca)
LED 20 mW; ESP32 görev-döngülü ortalama 1–5 mW; BLE radyosu açıkken ~150 mW. Tampon: 3.3 V'da 1 F süperkapasitör E = ½CV² = 5.4 J depolar. Bunun kaç iletim satın aldığı yayın süresine bağlıdır: kısa bir BLE reklam olayı (~150 mW'da ~2–5 ms) yalnızca ~0.3–0.8 mJ → dolu bir kapasitörden yaklaşık **10⁴ paket**; uzun bir bağlantı / burst (~100 ms radyo açık) ~15 mJ → yaklaşık **10² burst**. Ortalama çekim yine de toplanan watt'lar içinde kalmalıdır (aşama-2 hedefi yükte ≥0.5 W kapıdır; bu ölçülene kadar simülatör grafiklerindeki çok watt'lı mod-A bantlarını veri değil, hedef olarak değerlendirin).
