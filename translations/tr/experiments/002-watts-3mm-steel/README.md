# Deney 002: 3 mm Çelikten İlk Wattlar (PLANLANMIŞ)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · Türkçe · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **Aşama:** 2 ([001](../001-sweep-map-3mm-steel/README.md) deneyinde bulunan rezonansta bilinen bir yüke güç iletimi).
- **Hedef:** yarım-köprü sürücü ve eşleştirme transformatörü ile 3 mm çelikten geçirilen gerçek DC gücü ölçmek.
- **Hipotez:** aynı partiden Langevin çifti, gres+kelepçe (veya epoksi) teması ve ayarlanmış eşleştirme transformatörü ile, aşama-1 tepe noktasında dirençli yüke ≥0.5 W ulaşılabilir. (Literatürdeki çok watt/kW değerleri farklı transdüserler ve bağlama yöntemleri kullanmıştır — bunları tavan olarak kabul edin, geçiş çizgisi olarak değil.)
- **Önkoşullar:**
  - Deney 001 tamamlandı (tekrarlanabilir tepe, frekans kaydedildi).
  - Herhangi bir sürücü gücünden önce RX zincirine TVS takıldı ([docs/02-safety.md](../../docs/02-safety.md)).
  - Sürücü devreye alma sırası izlendi ([hardware/driver/README.md](../../../../hardware/driver/README.md)).
- **Kurulum (asgari):**
  - TX: Pi → AD9833 kare → ölü-zaman şekillendirici → IR2110 yarım-köprü → eşleştirme transformatörü → plakaya kelepçelenmiş Langevin ([sch1](../../../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Duvar: 3 mm çelik, temas yöntemi kaydedildi (gres+kelepçe / epoksi / diğer).
  - RX: Langevin → Schottky köprü → bilinen R_yük (güç direnci) ve/veya LED; köprüden sonra V_dc ve I_dc ölçülür ([sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) topolojisi, yalnızca ADC yerine yük).
- **Prosedür (taslak):**
  1. Akustik güç iddia etmeden 0.2 A PSU limitinde elektriksel devreye alma.
  2. TX/RX kelepçele, sürüş frekansını deney-001 tepe noktasına ayarla.
  3. Akım limitini yavaşça artır; PSU V/I, MOSFET/transformatör sıcaklığı, yük üzerinde V_dc ve I_dc değerlerini kaydet.
  4. P_yük = V_dc · I_dc. İsteğe bağlı: P_yük bilindikten sonra kısa LED demo fotoğrafı çek.
  5. Soğuma sonrası bir kez tekrarla; tepe frekansı sıcaklıkla kayabilir — güç düşerse mini-tarama ile yeniden kontrol et.
- **Başarı ölçütleri:**
  1. Belgelendirilmiş frekansta ve temas yönteminde 3 mm çelikten P_yük ≥ 0.5 W.
  2. Aynı kelepçe/kuplaj altında iki çalıştırma P_yük değerini ~%20 içinde doğruluyor (mertebe düzeyinde kararlılık, henüz metroloji sınıfı değil).
  3. LED (veya diğer yük) fotoğrafı + CSV/günlük bu dosya altında `data/` dizininden bağlanmış.
- **Başarısızlık da veridir:** P_yük ≪ 0.5 W'da kalırsa, çift Δf (001'den), temas yöntemi, transformatör sarımları ve dalga formlarını kaydet — bu, bir sonraki ADR'ye girdidir, simülatörü sessizce düzenlemek için bir neden değil.
