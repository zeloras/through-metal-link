# Çelik ötesi duvar malzemeleri: hangi duvarlar güç ve veri taşır

> [English (primary)](../../../docs/06-materials.md) · [Русский](../../ru/docs/06-materials.md) · [Deutsch](../../de/docs/06-materials.md) · [Português](../../pt/docs/06-materials.md) · [Español](../../es/docs/06-materials.md) · [Français](../../fr/docs/06-materials.md) · [Italiano](../../it/docs/06-materials.md) · [Polski](../../pl/docs/06-materials.md) · Türkçe · [Українська](../../uk/docs/06-materials.md) · [Tiếng Việt](../../vi/docs/06-materials.md) · [中文](../../zh/docs/06-materials.md) · [日本語](../../ja/docs/06-materials.md) · [한국어](../../ko/docs/06-materials.md) · [हिन्दी](../../hi/docs/06-materials.md)

Bu deponun geri kalanı çeliği varsayar. Bu sayfa daha basit, daha büyük soruyu sorar: **iki transdüserli kanal hangi duvar malzemeleri için hiç çalışır** ve hangi kipte? Bu bir simülasyon çalışmasıdır (`--mock` tarzı, laboratuvar verisi yok — donanım deneyini hak eden şey için sezgi), [channel_sim](../../../software/simulator/channel_sim.py) ile aynı yarı-ampirik modelden oluşturulmuş ve hacimsel soğurma ile genişletilmiştir.

Üret: `python3 software/simulator/material_map.py` (numpy + matplotlib gerektirir). Model ve varsayımlar: [../software/simulator/material_map.py](../../../software/simulator/material_map.py).

## Modeli bir dakikada anlatan

Bir duvarın hiç kullanılabilir olup olmadığına ve ne kadar güç için karar veren üç nicelik:

1. **Empedans kontrastı ve fazı** — kayıpsız Fabry–Perot levha modeli, [channel_sim](../../../software/simulator/channel_sim.py) ile özdeş:
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_duvar / Z_kuplan, kuplan Z = 1.5 MRayl (gres).
   Yarım-dalga rezonansında (f = c/2d) kayıpsız simetrik bir levha *r'den bağımsız olarak* tamamen şeffaftır; kontrast r tarak dişlerinin **ne kadar geniş** olduğunu (frekans hatasına tolerans) belirler, ses hızı c ise ne kadar aralıklı olduklarını belirler (Δf = c/2d).
2. **Hacimsel soğurma**, kayıpsız modele görünmeyen ve plastikler, beton ve kauçuk için belirleyici olan:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, tek yönlü, boyuna],
   burada α₁ₘₕᶻ 1 MHz değeridir.
   γ ≈ 1 = viskoz/relaksasyon kaybı; γ > 2 = homojensizliklerden saçılma (beton agrega).
3. **Duvarın geri aldığı doz** — aşağıdaki [bölüme](#the-dose-what-the-wave-does-to-the-wall-frequency-by-frequency) bakın: gerilim σ = √(2·I·Z), frekanstan *bağımsız değil* ve öz-ısınma ΔT ∝ α(f)·I, bağımlı.

**Varsayımlar, kodun belirttiği yerlerde belirtilmiştir:** tipik el kitabı özellikleri (boyuna dalga, ~20 °C); gerçek stoklar değişir — tane, dolgu, agregalar, kürlenme. Aşağıdakilerin tamamı bir sıralamadır, veri sayfası değil.

| Duvar | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | tarak Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | not |
|---|---|---|---|---|---|---|---|---|
| çelik | 7850 | 5900 | 46.3 | 0.02 | 590 | 148 | 0.21 | ince taneli yapısal |
| alüminyum | 2700 | 6320 | 17.1 | 0.02 | 632 | 158 | 0.69 | 6061 sınıfı |
| titanyum | 4430 | 6100 | 27.0 | 0.03 | 610 | 152 | 0.45 | Ti-6Al-4V |
| bakır | 8960 | 4760 | 42.6 | 0.05 | 476 | 119 | 0.17 | yoğun, çok yüksek Z |
| borosilikat cam | 2230 | 5640 | 12.6 | 0.01 | 564 | 141 | 0.77 | çok düşük kayıp |
| alümina seramik | 3890 | 9900 | 38.5 | 0.08 | 990 | 248 | 0.51 | hızlı ses, düşük kayıp |
| PMMA (akrilik) | 1180 | 2690 | 3.2 | 2.5 | 269 | 67 | 0.95 | şeffaf, MHz'de soğurma-sınırlı |
| PVC (sert) | 1400 | 2380 | 3.3 | 6 | 238 | 60 | 0.92 | PMMA'dan daha kayıplı |
| HDPE | 950 | 2340 | 2.2 | 12 | 234 | 58 | 0.98 | yumuşak, kayıplı |
| beton | 2300 | 3500 | 8.1 | 5 | 350 | 88 | 0.77 | agrega saçılması baskın; mertebelerce değişir |
| kauçuk (dolu) | 1100 | 1500 | 1.6 | 60 | 150 | 38 | 0.85 | dürüst çıkmaz yol |

## Grafikler

**Mod B (MHz) — malzeme başına kalınlık tarağı.** Sol: yapısal metaller; sağ: metaller dışı. Tüm duvarlar 5 mm, gres kuplajı. Kayıpsız model tepeleri tam rezonansta T = 1'e ulaşır; gerçek tepeler temas kayıplarıyla daha düşüktür ve soğurma kayıplı malzemeleri doğrudan sınırlar:

<img src="../../../docs/img/mat1-thickness-comb-materials.png" width="880">

**Malzeme haritası** — her şeyi belirleyen iki eksen: empedans (kuplaj/temas zorluğu) ve 1 MHz soğurma (MHz uygulanabilirliği). Yüksek-Z + düşük-α güç sınıfı köşesidir; düşük-Z + yüksek-α "40 kHz hala açık, MHz ölü"; kauçuk köşesi hedeflediğimiz her frekansta bir çıkmazdır:

<img src="../../../docs/img/mat2-material-map.png" width="720">

**Mod A (40 kHz) kuplaj vekili** — aynı iletim modelinin 3 mm duvardan 40 kHz'de değerlendirilmiş hali, çeliğe normalize edilmiş. *Bir sıralama, watt değil:* rezonans Langevin çifti her çubuğu kabaca eşit çarpar ve modelin içinde transdüser yüklemesi yoktur; o çarpan 2. aşama işidir ([experiments/002](../experiments/002-watts-3mm-steel/README.md)):

<img src="../../../docs/img/mat3-modea-coupling-materials.png" width="720">

## Tarama ne diyor

- **40 kHz'de düşük-Z duvarlar (plastikler, kauçuk kaplama) çelikten *daha kolay* kuplaj yapar** — gres üzerinden neredeyse empedans eşleşmesidirler, bu yüzden tarak geniştir ve geçiş başına iletim yüksektir. Plastikleri daha yüksek frekanslarda öldüren şey **hacimsel soğurmadır**, temas veya empedans değil. 40 kHz'deki malzeme merdiveni bu yüzden sezgiye göre tersinedir: HDPE/PMMA/PVC > cam/beton > alüminyum > alümina > titanyum > çelik > bakır — kauçuğun 40 kHz sayısının α'yı 1 MHz'den doğrusal olarak aşağı ekstrapole ettiği güçlü uyarıyla, ki viskoelastisite bunu garanti etmez.
- **Mod B malzemeleri temizce böler.** Metaller, cam ve alümina MHz'i ihmal edilebilir soğurmaya alır (α ≤ 0.1 dB/cm); tarak yüksek-Z duvarlar için *keskindir* (çelik, alümina — frekans izleme gerektirir, [00-teori](00-theory.md)'nin ~%6 ⇒ ~10× dersi) ve cam/PMMA için *geniştir* (toleranslı, ama PMMA 5 mm'de 1 MHz'de tek yönlü ~1.3 dB öder — yalnızca mW sınıfı).
- **Beton 40 kHz malzemesidir, MHz malzemesi değil.** Agrega saçılması (1 MHz'de λ ≈ 3.5 mm ≈ agrega boyutu) γ'yi ~2.5'e çıkarır ve MHz'i öldürür; ultrasonik darbe-hızı uygulaması (≥1 m yollardan 40–80 kHz) tamamen mod A'dır.
- **Batarya paketi nişi ([05](05-applications-map.md)) akustik olarak elverişli:** 2–3 mm alüminyum duvarın kuplaj vekili çeliğin ~3 katıdır ve soğurma ihmal edilebilir — amiral gemisi durum aynı zamanda kolay durumdur.
- **Mod B'de planlanacak frekans merdiveni** (5 mm duvar, ilk tarak): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, bakır ≈ 480, çelik ≈ 590, titanyum ≈ 610, alüminyum ≈ 630, cam ≈ 560, alümina ≈ 990. Daha ince duvar ⇒ orantılı olarak daha yüksek.

## Doz: dalga duvara ne yapıyor, frekanstan frekansa

İletim "ne kadar geçiyor" sorusunu yanıtlar; bu bölüm ters soruyu yanıtlar — **dalganın ne kadarı duvarda kalır ve bu duvara zarar verir mi?** Duvardaki dalga zararı tam olarak iki yüze sahiptir:

- **Gerilim** σ = √(2·I·Z) — düzlem-dalga momentumu; *frekanstan bağımsız*. Yüksek-çevrim yorgunluk sınırı (metaller), eğme/çekme mukavemeti (seramikler, cam, beton, kauçuk) ile karşılaştırın.
- **Öz-ısınma** ΔT = α(f)·I·d²/(8k), kararlı durum, her iki yüz soğutulmuş — α(f) üzerinden *frekansa bağlıdır* ve frekansın ısırdığı yer burasıdır: her yalıtkan malzemenin üzerinde her ekstra oktavın biriken ısıyı katladığı bir diz noktası vardır.

1 W/cm²'de (bu projenin hedeflediğinin ötesinde: ~19 cm² transdüser yüzeyine yayılmış 0.5–5 W'lık 2. aşama hedefi 0.03–0.26 W/cm²'dir):

| Duvar | σ @1 W/cm², MPa | sınır σ_e, MPa | gerilim marjı | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | tavan @40 kHz, W/cm² | tavan @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| çelik | 0.96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| alüminyum | 0.58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| titanyum | 0.74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| bakır | 0.92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| borosilikat cam | 0.50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| alümina seramik | 0.88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (akrilik) | 0.25 | 15 | 60× | 0.2 | 9.5 | 65 | ~100 | 2.1 |
| PVC (sert) | 0.26 | 15 | 58× | 0.6 | 28.8 | 199 | ~33 | 0.7 |
| HDPE | 0.21 | 8 | 38× | 0.15 | 19.2 | 215 | ~58 | 1.0 |
| beton | 0.40 | 2.5 | 6× | ~0 | 2.1 | 118 | 1.6 | 1.6 |
| kauçuk (dolu) | 0.18 | 1.5 | 8× | 11.5 | 288 | 1440 | 1.7 | 0.07 |

"Tavan" = duvarın yorgunluk/mukavemet sınırının %20'si içinde ve +20 K öz-ısınmanın altında kaldığı sürekli yoğunluk (kararlı durum, her iki yüz ortamda tutulmuş). Görev-döngülü çalışmalar daha az ısınır; yalnızca bir yüzde sabitlenmiş bir duvar — her zamanki durum, bir taraf hava — serbest yüzde kadar 4× daha fazla ısınır. Bu sayılar ilk bir kesittir, tasarım garantisi değil. Bir sözleşme notu: α değerleri yoğunluk-dB'dir (10·log₁₀, dozimetri sözleşmesi — 3 dB düşüş I'yı yarıya indirir); genlik-dB (20·log₁₀) kullanan darbe-eko NDT literatürü AYNI α'yı iki kat büyük sayılarla tanımlar — bir kaynağın sayılarını bu tabloya kopyalamadan önce hangi sözleşmeyi kullandığını kontrol edin.

<img src="../../../docs/img/mat4-harm-materials.png" width="920">

Doz taraması ne diyor:

- **[00-teori](00-theory.md)'nin çelik kararı geçerli ve genellenir**: her yapısal metal 1 W/cm²'yi gerilimde 65–680× marjlarla ve mikro-kelvin öz-ısınmayla taşır. Metaller zarar açısından frekans-duyarsızdır — kayıpları kuplayabileceğimiz her güçte ısıtmak için çok küçüktür.
- **Polimerlerde frekans zararı termaldir, mekanik değil.** PMMA'nın gerilim marjı 1 W/cm²'de bile rahat bir 60×'tir, ama ısınma diz tam 1 MHz civarındadır: 40 kHz'de iyi huylu (~0.2 K), 1 MHz'de +9.5 K, 5 MHz'de +65 K — birkaç W/cm²'de yumuşama bölgesi. PVC +10 K çizgisini 1 MHz'de ~0.35 W/cm²'de çoktan geçer; kauçuk 1 MHz'de W·cm⁻² başına ~288 K emer (ve 40 kHz'de bile ~12 K) — histerezik ısınma elastomer kaplı duvarların ölümünün *nedeni*, tarak değil. HDPE farkı böler ve erime noktasını hatırlar: 5 MHz'de W·cm⁻² başına +215 K.
- **Betonun dar marjı çekmedir, termal değil**: ~2.5 MPa statik çekme mukavemetine karşı 0.40 MPa dalga gerilimi (yorgunluk daha da düşük) 1 W/cm²'de yalnızca ~6× marj bırakır. 40–80 kHz rejimi projenin güç yoğunluğunda sorun kalır; betona odaklı çoklu-W/cm² ışınlar kaçınılmalıdır, MHz iki kat öyle (saçılma agrega arayüzlerini ısıtır).
- **Yol haritası için alt çizgi:** mod-A güç yoğunluklarında (≤0.3 W/cm²) tablodaki hiçbir katı tehlikede değildir — gerilim marjları ≥11× (en darı betonun çekme yorgunluğu 11×; gerisi ≥15×) ve her mühendislik katısı için ısınma ≤0.2 K (kauçuk, kimsenin hedeflemediği istisna, ~3.5 K). Zarar haritası projenin gücü artırma planını haklı çıkarır: ilk gerçek malzeme sınırları 2. aşama hedeflerinin *üstünde* görünür, önce sıvılarda (kavitasyon, [00-teori](00-theory.md)'nin ≤1 W/cm² kuralı), sonra betonun çekme yorgunluğunda, sonra MHz'de polimerlerde. Yüksek güçte gerçekten izlenmesi gereken parçalar piezo seramik ve bağ hattıdır — [02-güvenlik](02-safety.md) — duvar değil.

## Malzeme başına karar

| Duvar | Mod A — 40 kHz güç | Mod B — MHz güç/veri | Karar |
|---|---|---|---|
| çelik | ✓✓ referans | ✓ keskin tarak — frekans izle | temel |
| alüminyum | ✓✓ (vekil ~3× çelik) | ✓ keskinimsi tarak | en iyi yapısal duvar (bataryalar!) |
| titanyum | ✓✓ | ✓ keskinimsi, düşük kayıp | korozif/sıcak nişler, dronlar, gövdeler |
| bakır | ✓ (metallerin en zor kuplajı) | ✓ | niş: mühürlü busbarlar/elektrokimyasal hücreler |
| borosilikat cam | ✓✓ | ✓ en geniş tarak — en hoşgörülü | laboratuvar pencereleri, gözetim camları |
| alümina seramik | ✓✓ | ✓ en hızlı taraklar (990 kHz @ 5 mm), düşük kayıp | sıcak/yalıtkan işlem duvarları |
| PMMA | ✓ geniş bant | ⚠ mW sınıfı ≤ ~0.5 MHz sadece | tanklar, muhafazalar; MHz'de güç duvarı değil |
| PVC / HDPE | ✓ ince duvarlar | ✗ soğurma | düşük sınıf muhafazalar, veri-az düğümler |
| beton | ✓ 40–80 kHz (UPV uygulaması) | ✗ saçılma | temeller, borular — yalnızca mod A |
| kauçuk (dolu) | ⚠ model ekstrapolasyonu doğrulanmamış | ✗ | ampirik olarak çıkmaz yol — [04](04-hybrid-channels.md) |

Düşük-Z plastik duvar, *hizalama-toleranslı* mod-A bağlantıları için daha fazla başlık alanına sahiptir ama ~200 kHz üzerine çıktığınızda soğurmaya karşı daha az mutlak güç başlık alanı sunar; bir şey vaat etmeden önce ölçün.

## Donatı betonu — çok katmanlı durum

Gerçek beton hiçbir zaman sade değildir: donatı hasırları bir kap derinliğinde oturur ve yukarıdaki 1D tek-levha modeli onları göremez. `chart_rebar` / `rebar_table` modeli genel yığınlara genişletir ([`stack_transmission`](../../../software/simulator/material_map.py), katman başına soğurma ile tam çok katmanlı özyineleme, öz-kontrolde korunmuş). Modellenen geometri: 150 mm yapısal duvar, 40 mm kapta düzlem-eşdeğer kalınlığı Ø16 mm olan bir çelik hasır; *düzlem* modeli en kötü durumdur — gerçek bir çubuk yalnızca kesiştiği ışının parçasını gölgeler, bu yüzden bunları zarf düşüşleri olarak düşünün, tahminler olarak değil:

| Yığın (150 mm beton) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| sade 150 mm | 0.135 | 0.133 | 8.9e-09 |
| donatı Ø16 @ 40 mm | 0.013 | 0.069 | 6.6e-09 |
| iki hasır Ø16 @ 40 mm | 0.003 | 0.001 | 5.1e-09 |

<img src="../../../docs/img/mat5-rebar.png" width="880">

Yığın modeli ne diyor:

- **Işın altındaki bir düzlem hasır tam 40 kHz'de ×10 maliyet çıkarır** (çelik katmandan dur-bant girişimi), ama düşüş dardır: 100 kHz'de aynı yığın yalnızca ×2 kaybeder. Boru/otoklav nişi için pratik okuma: *40–120 kHz civarında bir frekans taraması, sabit bir frekans değil*, mod-A bağlantısını donatının ötesine geçiren şeydir — ve düşüşler kap derinliğiyle hareket eder, bu yüzden bir tarama aynı zamanda geometriyi de parmak iziyle tanımlar (donatı derinliği tahmininin temeli).
- **İkinci hasır (bir ağ) bu en kötü durumda neredeyse duvar-katilidir** (×45 aşağı ve 40–100 kHz civarında geniş-bant düz): yolda yoğun donatı dürüst "duvarda başka bir nokta seç" göstergesidir, sinyal işleme sorunu değil.
- **Yapısal betondan mod B donatı olsun ya da olmasın ölüdür** (1 MHz'de 1e-8 seviyesi: 5 dB/cm × 15 cm). Donatı MHz'de hiç hikayeye girmez.
- Uyarılar, önem sırasına göre: düzlem-katman varsayımı (en kötü durum — bir Ø16 çubuk 40–50 mm ışının kesitinin yarısından azını bloke eder), dalga-donatı eksenine paralel varsayıldı, ve 1D yayılım (çubuk etrafında kırınım yok). Doğru donanım deneyi gerçek bir plakada tarama düzeneğidir: bir donatı ızgarası üzerinden 40/80/120 kHz'de T(x, y) haritalayın ve düzlem modelinin düşüş konumlarını ızgara aralığına uydurun.

## Bir donanım takibi neyi ölçmeli

Belirli bir plakaya güvenmeden önce: malzeme başına iki-kalınlık yöntemi (aynı temasta d ve 2d iki plaka) gerçek α(f) ve c çıkarır — bu tek veri seti yukarıdaki tablonun her satırını değiştirir. Mevcut protokoller içinde doğal bonus geçişleri: deneyi [001](../experiments/001-sweep-map-3mm-steel/README.md) taramasını 5 mm PMMA plakada, bir borosilikat veya %99 alümina plakada ve bilinen sınıfta bir beton blokta tekrarlayın; plastikler için *daha düşük ama daha geniş* bir tepe, seramikler için keskin bir tarak ve her yerde sıcaklık-duyarlı temas bekleyin. Deneyi [002](../experiments/002-watts-3mm-steel/README.md) güç çalışması sırasında bir IR termometre (veya ince bir termokupl) her duvar tipinin uzak yüzüne bağlayın — bilinen girişte ölçülen ΔT, doz tablosunun ısınma sütununu doğrulayan veya öldüren tek sayıdır. Bu sayfada hiçbir şey ölçülmemiştir — önce neyi ölçeceğinizin haritasıdır.
