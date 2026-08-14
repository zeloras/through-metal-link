# Uygulama haritası: bu teknoloji yığınına kimin ihtiyacı var ve neden

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · [Deutsch](../../de/docs/05-applications-map.md) · [Português](../../pt/docs/05-applications-map.md) · [Español](../../es/docs/05-applications-map.md) · [Français](../../fr/docs/05-applications-map.md) · [Italiano](../../it/docs/05-applications-map.md) · [Polski](../../pl/docs/05-applications-map.md) · Türkçe · [Українська](../../uk/docs/05-applications-map.md) · [Tiếng Việt](../../vi/docs/05-applications-map.md) · [中文](../../zh/docs/05-applications-map.md) · [日本語](../../ja/docs/05-applications-map.md) · [한국어](../../ko/docs/05-applications-map.md) · [हिन्दी](../../hi/docs/05-applications-map.md)

Platform yığını: kör duvarlar boyunca aktif bir güç ve veri kanalı — piezo-akustik / EMAT / LF manyetik. Aşağıda: bunun gerçek dünyada nerede gerekli olduğu, kimin zaten orada olduğu ve bizim için neyin kaldığı.

## 1. Mühürlü batarya paketleri (EV, ev/endüstriyel enerji depolama)
- Acı noktası: termal kaçak erken tespiti — gazlar (CO₂, H₂, elektrolit buharları) paketin içinde yangından dakikalar ila saatler önce ortaya çıkar; muhafazada bir sensör geçişi = hermetik sızdırmazlık ve sertifikasyon kaybı.
- Yığınımız: paketin içinde bir gaz/sıcaklık düğümü, 2–3 mm alüminyum boyunca piezo çifti ile güç ve telemetri. Sıfır delik.
- Kim zaten orada: Liminal Insights — *dışarıdan* akustik tanı (analiz yöntemleri üzerine patentler, kanal üzerine değil). Paketin *içinde* düğüm satan kimse yok.
- Niş olgunluğu: pazar patlayarak büyüyor, raf boş. Platform için — vitrin uygulaması #1.

## 2. Lab ekipmanları: vakum odaları, kriyostatlar, eldiven kutuları
- Acı noktası: bir vakum odasına giden her elektrik geçişi yüzlerce dolarlık bir flanş ve sızıntı kaynağıdır; kriyostatta bir kablo = ısı sızıntısı.
- Yığınımız: odanın içinde bir sensör, çelik duvar boyunca sesle güç/veri; dewar vakum sandviçleri için — LF manyetik (bir T-logger için bit/s yeterli).
- Kim zaten orada: duvardan kablosuz geçiş yapan kimse yok; laboratuvarlar geçiş flanşlarıyla yaşıyor.
- Ogunluk: açık kaynak için ideal başlangıç nişi — laboratuvarlar açık donanımın tam hedef kitlesidir (TinyLev yolu): sertifikasız satın alır ve makalelerde sizi atıf gösterir.

## 3. Gıda üretimi: fermantasyon tankları, otoklavlar (bira, şarap, süt)
- Acı noktası: hijyen yönetmelikleri geçişlerden nefret eder (CIP yıkama, ölü bölgeler); tankın içindeki yoğunluk/T/basınç değerini her zaman bilmek istersiniz.
- Yığınımız: paslanmaz tankın iç duvarında bir düğüm, dışarıdan el tipi tarayıcı veya sabit bir çiftle sorgulanır.
- Kim zaten orada: sıradan delinmiş sensörler; duvardan kablosuz geçiş çözümü yok.
- Ogunluk: bir garaj testinin tamamen erişilebilir mesafesinde (herhangi bir butik bira fabrikası yürüme mesafesinde bir test alanıdır).
- Fiziksel uyarı: dolu bir tank duvarı yükler — tam kap against yeniden tarama yapın ve sürekli gücü ≲1 W/cm² tutun; bunun üzerinde üründe kavitasyon (CO₂ gazdan ayrışması, istenmeyen tatlar, uzun vadeli duvar erozyonu) — [teori](00-theory.md#duvar-ve-arkasındaki-medya-üzerindeki-etki).

## 4. Boru hatları, basınç kapları, endüstriyel NDT
- Acı noktası: kapatma veya delme olmadan içten korozyon/parametre izleme; yüzeyler sıcak, boyalı, kirli.
- Yığınımız: bir EMAT "tarayıcı tabancası" — sıfır yüzey hazırlığı ile bir boruya bastırın, içeriden pasif bir rezonans işaretini okuyun.
- Kim zaten orada: kelepçeli ultrasonik akış ölçerler ve kalınlık ölçerler (olgun bir pazar), ama içeride etkileşimli işaret yok.
- Ogunluk: orta seviye; EMAT dalını gerektirir (aşama ~6).

## 5. Petrol ve gaz / kuyu içi ve nükleer
- Kim zaten orada: Metrol, Acoustic Data, Baker Hughes (kuyu içi, 30 yıl, servis modeli); DOE/UNT/Westinghouse Ar-Ge (nükleer kaplar).
- Dürüst karar: dolu ve sıkı düzenlemeli — biz oraya gitmiyoruz, ama varlıkları = bu fiziğin ciddi paraya satıldığının kanıtı. README'de referans olarak kullanın.

## 6. Deniz lojistiği ve sualtı yapıları
- Acı noktası: mühürlü bir konteynerde "kargo canlı mı"; gemi gövdesinin iç tarafından veri.
- Kim zaten orada: CSignum (su/bölme duvarları boyunca LF EM) — hibrit felsefede tek doğrudan komşu.
- Ogunluk: uzun vadeli; bizim için, şimdilik, yalnızca bir düşünce yönü.

## Öncelikler (ne yapılacağı, hangi sırayla)
1. **Şimdi:** vitrin senaryosu "lab odası / kaynakla kapatılmış kutu" üzerinde platform aşamaları 1–4 (niş #2 — açık kayaba en açık olan).
2. **Sonra:** niş #3'ten canlı bir nesne üzerinde demo (bir bira fabrikası tankı) — ucuz, fotojenik, gerçek bir kullanıcı.
3. **Orta vade:** batarya senaryosu (niş #1) yayın için amiral vakası olarak; niş #4 için EMAT dalı.

*Pasif görüntüleme (müon radyografisi) ayrı bir projeye ayrıldı — bilgi tabanında muon-lab'a bakın.*
