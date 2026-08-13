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

## Yaşarken kopyalamadığımız şeyler (yalnızca ABD, ~2032'ye kadar; aşama 1–4 zaten bunlara ihtiyaç duymaz)
Güç kanalının harmoniklerinden kaçınmak için alt taşıyıcıları yerleştirilen OFDM (RPI US9054826); tek bir şema olarak tam çift yönlü "AM aşağı bağlantı + yük modülasyonu yukarı bağlantı + frekans takibi" (RPI US9455791); Drexel yaklaşımına göre kavisli yüzeyler için uyumlu transdüserler (US10594409).
