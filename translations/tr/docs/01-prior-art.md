# Önceki çalışmalar: ne üzerine inşa ediyoruz

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · Türkçe · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## Kural
Bu repodaki her teknik karar, "özgür" listeden bir kaynağa (süresi dolmuş patentler, makaleler) izlenebilir olmalıdır. Yürürlükteki patentler salt okunurdur — sorunları anlamak için kazın, asla istemlerini kopyalamayın (bu, ABD'de ticarileştirme için önemlidir; projedeki patent haritasına bakın).

## Özgür temel (süresi dolmuş/terk edilmiş patentler = kamu malı)
- **US5982297** (Aerospace Corp, 1997) — temel reçete: duvardan geçen bir piezo çifti, güç + çift yönlü veri. Ana yemek kitabı.
- US5594705 (Dynamotive, 1994) — gövdeden geçen bir "akustik transformatör".
- US6037704, US6127942 (Aerospace Corp) — sensörleri besleme, veriyi geri okuma.
- **US7902943** (Caltech/JPL, ödenmemiş bakım ücretleri nedeniyle 2019'da düştü) — Sherrit feed-through: reflektör, akustik transformatör.
- US9748870 (Caltech/JPL) — duvardan mekanik iş.
- **US9361877** (Univ. Oklahoma, ödenmemiş bakım ücretleri nedeniyle düştü) — modern, eksiksiz bir alıcı-verici sistemi.
- US20100027379 / WO2008105947 (DOE+RPI, terk edilmiş) — dışarıdan bir taşıyıcı + içeriden yük modülasyonu.

## Temel makaleler
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s, 63.5 mm çelik.
- Sherrit et al., NASA NTRS 20080048150 — bir duvardan beslenen 100 W lamba.
- Yang et al., Sensors 2015 (10.3390/s151229870) — derleme, sayıların en iyi özeti.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — metamalzeme, 1 mm paslanmaz çelikten %2→%66 (07.2026 itibarıyla patent bulunamadı).

Bu makaleler **fizik ve patent-hijyeni taban çizgisidir**. Güç/bit hızları laboratuvar transdüserleri, bağlama ve eşleştirme kullanır — [QUICKSTART.md](../QUICKSTART.md) içindeki AliExpress Langevin + gres BOM'u değil. Varlıksal kanıt olarak atıf yapın; projenin kendi geçiş çubukları [experiments/](../../../experiments) içinde yatar.

## Yaşarken kopyalamadığımız şeyler
Bu listenin eski çekirdeği yalnızca ABD'ye özgüdür ve 2032–2033 civarında süresi dolar, ve aşama 1–4 bunların hiçbirine ihtiyaç duymaz: güç kanalının harmoniklerinden kaçınmak için alt taşıyıcıları yerleştirilen OFDM (RPI US9054826); tek bir şema olarak tam çift yönlü "AM aşağı bağlantı + yük modülasyonu yukarı bağlantı + frekans takibi" (RPI US9455791); Drexel yaklaşımına göre kavisli yüzeyler için uyumlu transdüserler (US10594409). Aşağıdaki ailelerin hiçbiri böyle değildir: biri aşama 2'nin çıplak güç kanalını kapsar, biri de Avrupa'da 2039'a kadar yürürlükte kalır.

**2026-08 aramasıyla eklenen (durumlar Google Patents işaretleridir — herhangi bir ticari kullanımdan önce USPTO Patent Center / EP Sicilinde yeniden kontrol edin):**
- **US8594572B1** (US Navy, öncelik 2011-06, 12 yıllık ücret 2025'te ödendi, 2032-01'e kadar yürürlükte, yalnızca ABD) — istem 1 "duvar + güç kaynağı + akımı duvardan ultrasona dönüştüren transdüser + geri dönüştüren transdüser + beslenen elektronik cihaz" şeklindedir; frekans, malzeme veya kalınlık sınırlaması yoktur: ABD'de çıplak güç kanalını birebir kapsar. Welle'nin US5982297 (1997) aynı düzenlemeyi açıklar, dolayısıyla süresi dolmuş katman aynı zamanda geçersizlik savunmasıdır; yine de bir ABD ticari fork'u FTO görüşü almalıdır.
- **EP3723304B1** (ABB, öncelik 2019-04, 2023-08'de verilmiş, **yalnızca DE ve GB'de sürdürülmektedir** — CH 2024-04'te düştü, kayıt verilerinde başka doğrulama bulunamadı; 2039-04'e kadar; ABD üyesi yok) — bir sensör platformuna güç *ve* veri dönüşü taşıyan bir "akustik dalga iletkeni" (açıklamada kap duvarı), **güç taşıyan spektrumun veri spektrumundan daha düşük olduğu durumda**. Bu sınırlama, verilme sürecinde bağımsız bir istemden ithal edilmiştir ve bizim tasarım etrafında dolanma yolumuz budur: planlanan yukarı bağlantı, *aynı* 40 kHz taşıyıcı üzerinde yük modülasyonudur ([docs/03](03-discovery-protocol.md)) — güç taşıyıcısının etrafında yan bantlar, daha yüksek bir bant değil (bir istem okuması, FTO görüşü değil). DE/GB için bir üründe, A modu güç bağlantısına ayrı bir daha yüksek frekanslı veri taşıyıcısı (ABB'nin kendi örneği: düşük frekanslı güç üzerinden 200–300 kHz veri) eklemeyin.
- **Ultrapower ailesi** (öncelik 2014-03, 2035-03'e kadar): US10295500B2 — metalik bir *boru* içinde sensör, dışarıda alıcı-verici, **konveks/konkav** transdüser dizileri; US10684260B2 / US10948457B2 — duvardan *geçen* bir metal çubuk. Biz düz tesviyeli padler kullanırız ve çubuk kullanmayız.
- **US9602221B2** (Zackat Inc.; güvenlik menfaati/devir olayları Anelto Inc. / Instant Care Inc. adını zikreder; öncelik 2014-03, 2021'de yeniden yürürlüğe konmuş, ücret 2024'te ödendi, 2035-10'a kadar, ABD) — istem 1: patlama riskli bölge içinde bir "Sınıf 1 cihaz" üzerinde ultrasonik verici, dışarıda alıcı, uzak operatöre uyarı; **bağımsız istem 14 Sınıf-1-cihaz sınırlamasını çıkarır** (patlama riskli bölge içinde herhangi bir sensör + ultrasonik bağlantı + uyarı). Yalnızca bir düğüm tehlikeli bir alandan uyarı gönderirse ilgili olur — bu tür bir uygulamayı ABD'de laboratuvar ölçeğinde tutmak için bir neden.
- Teğet, not edilen: GE US9146266B2 (güç üretim yapılarından telemetri, 2033'e kadar), UNT US11415555 (pasif SAW/BAW duvardan geçiş), CEA EP4080791B1 (empedans taraması frekans optimizasyonu), RPI US9331879B2 (MIMO), US9505031B2 (yaylı muhafaza). RPI US9455791B2 istem 1, iç transdüserin MOSFET yük modülasyonunu içerir — ancak yalnızca diferansiyel AM aşağı bağlantı, Barker dizisi senkronize örnekleme ve frekans adım/takip algoritması ile birlikte; [docs/03](03-discovery-protocol.md) bilinçli olarak AM/Barker aşağı bağlantısının hiçbirini içermez ve patent yaşarken o bütün kombinasyon uygulanmamalıdır.
- Özgür, ek olarak doğrulanan: Progeny/General Dynamics US20120127833A1 (ayrı güç/veri frekansları — **terk edilmiş**), RPI/DOE US20100027379A1 (yük modülasyonu yukarı bağlantı — terk edilmiş).
