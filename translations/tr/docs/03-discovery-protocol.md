# Alıcı keşfi ve otomatik ayarlama protokolü (taslak; uygulama 2–4. aşamalarda)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · [Português](../../pt/docs/03-discovery-protocol.md) · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · Türkçe · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

Hedef: cihaz kendi başına duvarın arkasında bir alıcı olup olmadığını anlasın, frekansı ve gücü kendisi seçsin ve biri "alıcıyı kaynatmayı unuttuysa" duvarı boşuna kızartmasın.

Rol modeli Qi şarj cihazlarıdır: tam olarak bu problemi (bobinin üzerinde telefon var mı?) tam olarak bu sırayla çözerler. Akustik analogumuz:

## Aşama 0 — analog ping (alıcı tamamen boşalmış olabilir)
TX, bant boyunca düşük güçlü bir tarama yapar ve **kendi akımını ve fazını** ölçer (şönt + tepe dedektörü → ADS1115). Duvarın arkasındaki rezonanslı bir alıcı, TX'e duvar üzerinden bağlı bir yüktür: varlığı, içeride hiçbir şey güçsüz olsa bile TX empedans eğrisinde karakteristik bir çukur/tümsek olarak görünür. Metal dedektörü ve Qi'nin analog ping'iyle aynı prensip.
- İmza var → aşama 1. İmza yok → "alıcı bulunamadı", bekleme ping'inde kal (her N saniyede bir), gücü artırma.
- Bonus: "boş" duvarın empedans eğrisi, kurulum sırasında referans olarak kaydedilir — böylece "alıcı yok" ile "alıcı gevşedi / hizası kaydı" birbirinden ayırt edilebilir.

## Aşama 1 — dijital el sıkışma
TX, aday frekansta (aşama 0 tepe noktası) durur ve güç verir. RX hasatçısı süperkapasitörü şarj eder, MCU uyanır ve **yük modülasyonu** ile yanıt verir: bir MOSFET, piezosunu periyodik olarak bir koda (ID + protokol sürümü) göre kısa devre eder. TX bunu kendi akımının modülasyonu olarak görür. İçeride hiç verici gerekmez — bu bir RFID şemasıdır, terk edilmiş DOE/RPI başvurusu US20100027379'dakiyla aynı (bedel önceki sanat).

## Aşama 2 — frekans servo ayarı (pertürb & gözlem)
RX, baras voltajını raporlayabilir (yük modülasyonu üzerinden telemetri). TX ±Δf adımlar yapar ve alınan gücün maksimumunu tutar — klasik bir MPPT döngüsü. Bu, sıcaklıkla rezonans kaymasını kapatır (nişin ana tuzağı: ~%6 kayma = ~10× verim düşüşü).

## Aşama 3 — güç müzakeresi ve watchdog
RX bir seviye ister (hayatta / şarj oluyor / daha fazla ver), TX gücü istenen seviyede sınırlandırır. M döngü boyunca yanıt gelmezse → TX düşük güçte aşama 0'a geri döner.

## Bunun gerektirdiği donanım (BOM kalemi 12, şematik — hardware/schematics/sch4)
- TX: 0.1 Ω şönt + ikinci ADS1115 kanalında doğrultucu/tepe dedektörü (akım), isteğe bağlı faz karşılaştırıcısı.
- RX: 2N7002 + doğrultucunun **DC tarafında** ~100 Ω (LTC3588 modülünün VIN pini) + GPIO — yük köprüden sonra anahtarlanır ve TX bunu kendi akımının modülasyonu olarak görür. AC piezo boyunca tek bir MOSFET çalışmaz (gövde diyodu yarım dalgalı kısa devre yapar, gate'in yüzen düğümde referansı yoktur); piezo boyunca varyasyon yalnızca arka arkaya seri bir MOSFET çiftiyle çalışır.

## Sınırlar
Analog ping, duvar kalınlığı ve temas kayıpları arttıkça zayıflar (imza gürültüde boğulur) — algılama eşiği özel bir deneyde ölçülmelidir (experiments/). Kalın duvarlar için geri dönüş: RX, yeterli şarj biriktirdiğinde, periyodik olarak kendi işaretiyle "vurur".
