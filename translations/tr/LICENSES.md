# Lisanslama ve patent koruması

> [English (primary)](../../LICENSES.md) · [Русский](../ru/LICENSES.md) · [Deutsch](../de/LICENSES.md) · [Português](../pt/LICENSES.md) · [Español](../es/LICENSES.md) · [Français](../fr/LICENSES.md) · [Italiano](../it/LICENSES.md) · [Polski](../pl/LICENSES.md) · Türkçe · [Українська](../uk/LICENSES.md) · [Tiếng Việt](../vi/LICENSES.md) · [中文](../zh/LICENSES.md) · [日本語](../ja/LICENSES.md) · [한국어](../ko/LICENSES.md) · [हिन्दी](../hi/LICENSES.md)

Bu düzenin amacı: proje tamamen açıktır, herkes çatallayıp (ticari amaçlarla dahi) üzerine inşa edebilir; aynı zamanda patent davası riski, hukuki ve usuli yollarla ulaşılabilen en düşük düzeye indirilir.

## Düzen (üç katman; tam metinler [LICENSES/](../../LICENSES) içinde)

| Alan | Lisans | Metin | Patent hükümleri |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](../../LICENSES/Apache-2.0.txt) | §3: her katkıda bulunan, katkısı için otomatik olarak bir patent lisansı verir; bir patent davası açarsanız **patent** lisansını kaybedersiniz (karşılık; §2'deki telif hakkı lisansı geri alınamaz ve davadan sonra da yürürlükte kalır) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](../../LICENSES/CERN-OHL-W-2.0.txt) | §7.1: her lisans verenden patent lisansı (Üret / ürettir / kullan / sat / ithal et…) — ancak yalnızca verilen Covered Source tarafından zorunlu olarak ihlal edilen talepler için; §7.2: bir patent davası (başkasının patentini geçersiz kılmaya yönelik bir girişim dahil) lisans altındaki **tüm** hakları sonlandırır |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](../../LICENSES/CC-BY-4.0.txt) | **hiçbir** patent hakkı vermez (§2(b)(2)) — bu boşluk [CONTRIBUTING.md](../../CONTRIBUTING.md) içindeki açık patent hibesi ile kapatılır |
| geri kalan her şey (kök `README.md`, `QUICKSTART.md`, bu dosya, `data/` vb.) | CC-BY-4.0 | — | yedek: depoda hiçbir dosya "tüm hakları saklıdır" durumunda bırakılmaz |

Kod dosyaları SPDX başlıkları taşır (Apache-2.0); makine tarafından okunabilir kapsam haritası [REUSE.toml](../../REUSE.toml). Telif hakkı satırı [NOTICE](../../NOTICE) içinde bulunur; kök [LICENSE](../../LICENSE) bu düzene bir işaretçidir.

**Neden CERN-OHL-W, S veya P değil.** W orta yoldur: tasarım ve değişiklikleri herhangi bir dağıtımda açık kalmalıdır, ancak tasarımın yerleştirildiği ürün ticari ve kapalı olabilir — bu, docs/05'teki nişleri (laboratuvarlar, bira fabrikaları, batarya paketleri) açık tutar. S (güçlü copyleft) gömme kapısını kapatır; P (izin verici) kapalı çatallara izin verir. S'ye doğru sıkılaştırma lisansın kendisinde mevcuttur: §8.3, herkesin W ile lisanslı materyali S ile lisanslı olarak değerlendirmesine izin verir (Available Components koşulu sağlandığında) — izin gerekmez. Gevşetme (P'ye veya başka bir lisansa doğru) ise yalnızca tüm materyal tek bir yazara aitken mümkündür; ilk dış katkıdan sonra — yalnızca her katkıda bulunanın onayıyla.

**Proje adı.** "through-metal-link" tescilli bir marka değildir; lisansların kendisi isim üzerinde hiçbir hak vermez (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Projeye atıfta bulunmak ("through-metal-link temelinde") herkes için ücretsizdir; uyumsuz değişiklikler içeren çatalların kendi adı altında dağıtılması rica edilir.

## Bu neyi korur — ve neyi korumaz (dürüstçe)

**Korur:**
1. **Katkıda bulunanlardan davalar.** Katkıda bulunan herkes, o katkı üzerindeki patent haklarını otomatik olarak lisanslamıştır (Apache §3, CERN-OHL §7.1 ve docs için CONTRIBUTING). Bir dava davacıya pahalıya patlar: Apache-2.0 altında kodun patent lisanslarını kaybeder; CERN-OHL-W altında donanım katmanındaki tüm hakları doğrudan kaybeder (§7.2 — başkasının patentine itiraz etme girişimi tarafından bile tetiklenir).
2. **Donanım çatallarının özelleştirilmesi.** CERN-OHL-W, dağıtan herkesi (bir ürünün veya kaynakların Conveyance'i) tasarım değişikliklerini yayımlamaya zorlar — iyileştirmeler açık katmana geri akar ve kendileri önceki teknik haline gelir. (Üçüncü taraflara asla iletilmeyen bir çekmece çatalının yayımlama yükümlülüğü yoktur — herhangi bir copyleft altında olduğu gibi.)
3. **Başkalarının *gelecekteki* patentleri.** Tarih ile yayımlanan her şey, sonraki başvurular için yeniliği yok eder: burada başvuru tarihlerinden önce açıklanan bir çözüm için artık geçerli bir patent verilemez. Yayınımızdan *önce* başvuru edilenler için bu işe yaramaz — onlar için tek kalkan, süresi dolmuş patentler katmanıdır (aşağıya bakın).

**Korumaz:**
- **Halihazırda mevcut üçüncü taraf patentleri.** Hiçbir lisans bunu yapamaz. Onlara karşı işe yarayan, docs/01-prior-art.md'nin mühendislik disiplinidir: yalnızca süresi dolmuş katmandan (kamu malı) inşa edin, orada listelenen canlı talepleri uygulamayın (RPI, Drexel ve 2026-08'de eklenen Navy/ABB/Ultrapower aileleri — bunların tamamı ABD'ye özgü değildir ve tamamı ~2032'de dolmaz) ve her tasarım kararını özgür bir kaynağa geri izleyin. Bu bir garanti değildir, ancak bir davayı anlamsız kılan tam olarak bu uygulamadır.
- Ticari üretime yönelen bir çatal, kendi yargı bölgesi ve tasarımı için kendi FTO (işletme özgürlüğü) analizini yapar — depo hiçbir patent beyanı yapmaz (üç lisansın tamamında feragatnameler).

## Savunmacı yayınlama protokolü (kilometre taşları yayımlandıkça yürütmeye devam edin)

Yayımlanan her sonuç, aynı çözüm için sonraki tüm üçüncü taraf başvurularını engelleyen tarihli önceki sanattır:

1. Tam herkese açık git geçmişini koruyun (commit'ler = zaman damgaları).
2. **Zenodo**'ya anlık görüntü → DOI: yasal olarak anlamlı tarihe sahip, makalelerde atıf yapılabilen bağımsız bir arşiv.
3. **Software Heritage**'te sabitleme (archive.softwareheritage.org — sürekli bir ayna).
4. Tamamlanan her `experiments/NNN` — tarih, sayılar ve grafiklerle: bu, belirli bir teknik çözümün yayınıdır.
5. Önemli kilometre taşları (ilk wattlar, ilk düğüm) — dünyaya bir yazı (Hackaday.io / arXiv / blog): yayılma ne kadar geniş olursa, önceki sanat durumu o kadar güçlü olur.

## Katkıda bulunanlar için

Kurallar [CONTRIBUTING.md](../../CONTRIBUTING.md) içinde bulunur: DCO imzası, inbound=outbound, dizinden bağımsız her katkıda açık patent hibesi, tasarım kararlarının özgür önceki sanata izlenebilirliği.

Depo zaten herkese açıktır. Tarihli önceki sanat, sonuçlar geldikçe güçlü kalsın diye her kilometre taşında yukarıdaki protokolü sürdürün (Zenodo anlık görüntüsü, Software Heritage sabitlemesi, deney yazıları).
