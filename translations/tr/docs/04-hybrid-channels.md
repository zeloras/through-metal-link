# Hibrit kanallar: bariyer → fizik → sayılar

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · [Deutsch](../../de/docs/04-hybrid-channels.md) · [Português](../../pt/docs/04-hybrid-channels.md) · [Español](../../es/docs/04-hybrid-channels.md) · [Français](../../fr/docs/04-hybrid-channels.md) · [Italiano](../../it/docs/04-hybrid-channels.md) · [Polski](../../pl/docs/04-hybrid-channels.md) · Türkçe · [Українська](../../uk/docs/04-hybrid-channels.md) · [Tiếng Việt](../../vi/docs/04-hybrid-channels.md) · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

İlke ("geçiş paradoksu"nun bir sonucu): bir dalga, bir bariyerden tam olarak onunla zayıf etkileştiği ölçüde geçer — işte bu yüzden evrensel bir kanal yoktur. Platform tek bir kanalın peşinden koşmaz; her bariyer için, bariyerin şeffaf olduğu ve alıcının rezonans olarak "açgözlü" olduğu fiziği seçer.

## Kanal seçim tablosu

| Bariyer | Çalışma kanalı | Beklenen (büyüklük dereceleri) | Notlar |
|---|---|---|---|
| Çelik/alüminyum 1–60 mm, temas mümkün | Piezo-akustik (bizim birincilimiz) | watt; kbit/s (MHz modunda Mbit/s'e kadar) | akustik temas gerekir (gres kuplaj/epoksi) |
| Metal: kirli, boyalı, sıcak, temas istenmeyen | EMAT (manyetik → duvarda ses) | mW; kbit/s; ~3 mm'ye kadar boşluk | yalnızca iletken duvarlar; güç değil, veri |
| Piezo içermeyen ferromanyetik duvar | Manyetostrüksiyon (bir bobin çeliğin kendini sürer) | kırıntılar; bit/s–kbit/s | deneysel dal, test etmesi ucuz |
| Vakumlu çift duvar (termos, kriyostat, dewar) | LF manyetik (onlarca–yüzlerce Hz) | µW–mW; bit/s | deri etkisi: çelikte δ≈0.6 mm @1 kHz — frekansı aşağı itin |
| Metal olmayan: cam, plastik, seramik | Piezo-akustik (metalden daha kolay) | watt; kbit/s | + düz RF de çoğu zaman geçer — önce onu kontrol edin |
| Kauçuk/köpük katmanlı duvar, kompozit | Açıkçası: neredeyse çıkmaz sokak | — | soğurucu her şeyi yutar; geçici çözüm, kaplamasız bir noktadır |
| Duvar arkasında sıvı (dolu tank) | Piezo-akustik, bozulmuş | güç − birkaç dB; daha kısa çınlama | sıvı yüklemesi rezonansı kaydırır/söndürür — tam kap karşıya yeniden tarama yapın; kavitasyonun altında kalmak için sürekli yoğunluğu ≲1 W/cm²'te tutun ([teori](00-theory.md#effect-on-the-wall-and-the-media-behind-it)) |
| Akustik yolda kabarcıklı sıvı | Mimari geçici çözüm | — | alıcıyı duvara monte edin, sıvıyı yoldan uzak tutun |

## Hibrit düğüm mimarisi

- Güç katmanı: rezonansta piezo çifti (aşama 1–4).
- Temassız veri katmanı: çıkarılabilir bir "tarayıcı tabancası" olarak EMAT kafası (~aşama 6).
- Yedek katman: vakumlu sandviçler için LF bobinleri (görev gerektirdiğinde).
- Keşif protokolü (docs/03), "frekans üzerinden tarama"dan "fizik üzerinden tarama"ya genişler: piezo'ya ping → EMAT'a ping → LF'ye ping; düğüm kendi başına geçen kanalı seçer ve gördüğü bariyeri raporlar.

## Kanala göre örnek uygulamalar

1. **Mühürlü batarya paketleri (EV/depolama):** reçineyle doldurulmuş bir muhafaza içinde T/gaz sensörü; 2–3 mm alüminyumdan piezo çifti ile güç+veri. Pazar hızla büyüyor ve batarya muhafazasına bir geçiş = sertifikasyon cehennemi.
2. **Kriyostat/dewar:** içeride bir sıcaklık kaydedici, vakum ceketi üzerinden LF manyetik ile dakikada bir bit-paket gönderir. Akustik için temelden erişilemez — hibritin yerini doldurulamaz olduğu yer burasıdır.
3. **Basınç altında boru hattı/otoklav: sıfır yüzey hazırlığıyla sıcak boyalı bir boruya bastırılan EMAT tarayıcı — içeriden pasif bir rezonans işaretini okur.
4. **Fermentasyon tankları (bira/şarap, paslanmaz çelik):** tank içinde tek bir delik açmadan yoğunluk/T sensörü — hijyen yönetmelikleri deliksizliği sever.
5. **Deniz konteyneri/kasa:** "kargo hayatta mı" — oluklu çelikten piezo çifti, el tipi tarayıcıyla sorgulanır.

## Hiçbir katmanın çözemediği sınırlamalar
Güç — yalnızca temas piezo (EMAT ve LF manyetik derece katı daha zayıf). Kompozit/kauçuk astarlı duvarlar platformun dışındadır. LF kanal hızı saniyede bit cinsindendir — bu telemetridir, akış değil.
