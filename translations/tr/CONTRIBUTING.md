# Nasıl Katkıda Bulunulur

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · Türkçe · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Çelikten geçen açık kanalı ilerletmek istediğiniz için teşekkür ederiz. Aşağıdaki üç kural bürokrasi değildir — projenin patent zırhıdır (nedenini görmek için [LICENSES.md](LICENSES.md) dosyasına bakın).

## 1. Katkı lisansları (gelen = giden)

Bir katkı sunarak, bu katkının bulunduğu dizindeki diğer materyallerle aynı şekilde lisanslandığını kabul etmiş olursunuz:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Patent lisansı.** Ayrıca — CC-BY-4.0 patentleri lisanslamadığından — projeye ve materyallerinin tüm alıcılarına, katkınızı tek başına ve projenin bir parçası olarak yapmak, yaptırmak, kullanmak, satışa sunmak, satmak, içe aktarmak ve başka şekillerde devretmek için süresiz, geri alınamaz, dünya çapında, telifsiz, münhasır olmayan bir patent lisansı vermiş olursunuz; bu lisans, katkının tek başına veya sunulduğu projeyle birlikte kullanılmasıyla zorunlu olarak ihlal edilen patent iddialarınız kapsamındadır. Koşullar, katkının hangi dizine yerleştirildiğine bakılmaksızın Apache-2.0 §3 bölümüne uygun şekilde uygulanır. Herhangi birine karşı (karşı dava dahil) projenin materyallerinin patentinizi ihlal ettiğini iddia eden patent davası açarsanız, bu madde ve projenin lisansları kapsamında size proje ve katkıda bulunanlar tarafından verilen tüm **patent** lisansları, böyle bir davanın açıldığı tarihte sona erer.

## 2. DCO: kaynak üzerine bir imza

Signed-off-by: Firstname Lastname <email@example.com>
```

Sign-off içermeyen PR'lar birleştirilmez; bu denetim otomatiktür — [.github/workflows/dco.yml](../../.github/workflows/dco.yml) CI işi, tek bir commit bile sign-off içermiyorsa PR'ı başarısız sayar. Doküman katmanının patent koruması tam olarak bu zincire dayanır — istisnasız.

**Katmanlar arasında malzeme taşıma.** Malzeme, ilk düştüğü katmanda (ve o katmanın lisansı altında) kalır. Farklı lisanslara sahip katmanlar arasında metin/kod taşınması yalnızca malzeme size aitse veya parçanın orijinal lisansına dair açık bir notla yapılabilir.

## 3. Patent hijyeni ve deney protokolü

- Her teknik kararın izi serbest bir kaynağa dayanmalıdır — süresi dolmuş bir patent veya [docs/01-prior-art.md](docs/01-prior-art.md) içindeki bir makale. Orada da listelenen yürürlükteki patent taleplerinin uygulamaları, bu taleplerin süresi dolana kadar kabul edilmez.
- Deneysel sonuçlar — yalnızca [experiments/TEMPLATE.md](experiments/TEMPLATE.md) şablonu üzerinden: tarihli, tekrarlanabilir bir protokol, öncül sanatımızı oluşturan şeyin ta kendisidir.
- Mimari kararlar [docs/decisions/](docs/decisions/) içindeki ADR'lerden geçer.
- Kod yorumları, docstring'ler, tanımlayıcılar ve commit mesajları yalnızca İngilizcedir. Belgeler çok dillidir (aşağıya bakın); kullanıcıya görünür şekil etiketleri `labels.json` içinde yer alır.

## 4. Çok dilli belgeler: tek bir dili düzenleyin, CI gerisini senkronize eder

İngilizce birincil dildir ve kurallı yollara sahiptir. Diğer her dil, [translations/](..) altında aynı dosya adlarına sahip bir aynalama ağacıdır — markdown, BOM CSV ve oluşturulan şekiller dahil; şekillerdeki metinler `labels.json` tarafından yönetilir. Aynaları elle korumak **zorunda değilsiniz**:

- Rahat ettiğiniz dili düzenleyin. Push yapıldığında, [Translation sync](../../.github/workflows/translate.yml) iş akışı, karşılık gelen dosyaları açık ağırlıklı bir LLM (Ollama Cloud üzerinde `glm-5.2`) ile çevirir, eşitleme `labels.json`'u güncellediğinde şekilleri yeniden oluşturur ve sonucu `[translate-sync]` işaretçisiyle birlikte geri işler. Herhangi bir OpenAI uyumlu uç nokta çalışır — `OPENAI_BASE_URL` ve `TRANSLATE_MODEL` ayarlayın.
- Hâlâ iş gerektiren kısımlar, her çevirinin hangi birincil içerikten yapıldığını kaydeden `translations/.sync-state.json` dosyasında takip edilir. Kota veya zaman aşımı nedeniyle yarıda kesilen bir çalışma bu yüzden hiçbir şey kaybetmez: bitmemiş çiftler eski olarak işaretli kalır ve bir sonraki push veya gece yarışı tarafından devralınır. Bu dosyayı elle düzenlemeyin.
- Bir belgenin **birkaç** dilini kendiniz düzenlediyseniz, dokunduğunuz her sürüm yazdığınız gibi korunur; bot yalnızca dokunmadığınız dilleri doldurur.
- **`labels.json`, "herhangi bir dili düzenle" kuralının istisnasıdır.** Şekil etiketleri yalnızca birincil → aynalar yönünde akar. Çevrilmiş bir etiketi düzenlemek o dili düzeltir ve orada durur; İngilizceye geri dönmez. Bir etiketin *ne söylediğini* değiştirmek için birincil bölümü düzenleyin. Bunun nedeni asimetridir: bir etiket düzenlemesi neredeyse her zaman birinin makinenin söz dizimini düzeltmesidir ve bunun birincili yeniden yazmasına izin vermek, on dört aynanın üretildiği kaynağı yeniden tanımlar. Botun hiç üretmediği anahtarlar hâlâ geri yayılır, bu yüzden elle yazılmış bir etiket tek bir dile sıkışıp kalmaz.
- Makine çevirisi işlenir — bot'un commit'ini gözden geçirin ve tonu kaçırırsa söz dizimini düzeltin; düzeltmenizin üzerine yazılmaz (bot sizin sürümünüzü geçerli sürüm olarak kaydeder).
- Kesilmiş veya `labels.json` yer tutucuları bozuk halde dönen bir yanıt işlenmek yerine atılır ve çift yeniden denenir — yani bir aynadaki tuhaf görünen bir boşluk eski bir çifttir, bir karar değil.
- **Harici PR'ler:** bot `master` üzerinde çalışır, bu yüzden bir PR yalnızca bir dili değiştirebilir — aynalar (İngilizce dahil) birleşmeden hemen sonra otomatik olarak yetişir. Dokümana katkıda bulunmak için İngilizce bilmeniz gerekmez.
- **Dil ekleme:** kodunu ve adını [i18n.json](../../i18n.json) dosyasına ekleyin (ör. `"fr": "Français"`) ve push yapın — işlem hattı tüm `translations/fr/` aynasını oluşturur: her belge, her `labels.json` içinde bir `fr` bölümü, şekil seti ve her yerdeki dil değiştiriciler.
- **Latin alfabesi dışı yazılar:** CI, Noto ailelerini (`fonts-noto-core`, `fonts-noto-cjk`) kurar ve oluşturucular `i18n.json` → `render.fonts` içindeki yazı tipi yığınını tarar, böylece Kiril, Han, kana ve Hangul düzgün çıkar. Bir oluşturucu artık çizmeden önce glif kapsamını kontrol eder ve **`.notdef` kutuları çizmek yerine başarısız olur** — bu kontrol, Çinçe şekillerin bir tofu ızgarası olarak gönderilmesi ve CI'da hiçbir şeyin piksellere bakmaması nedeniyle vardır. Tetiklenirse, o yazı için Noto yüzünü yığına ekleyin.
- **Bağlamsal şekillendirme gerektiren yazılar** — Arapça ve Farsça (RTL, bitişik formlar), Devanagari ve Bengalce (birleşik harfler) — bir şekillendirme motoru olmayan matplotlib tarafından doğru çizilemez: doğru yazı tipi olsa bile glifler bitişik ve sırasız çıkar. Bu dilleri `i18n.json` → `render.skip_figures` içinde listeleyin. Düzyazıları etkilenmez; belgeleri yalnızca birincil şekillere bağlantı verir ve [tools/translate_sync.py](../../tools/translate_sync.py) içindeki bağlantı onarımı bunları otomatik olarak işaretler. `hi` bu şekilde ayarlanmıştır.
- **Yazı koruması:** [tools/i18n_render.py](../../tools/i18n_render.py) içindeki `SCRIPTS`, her dilin etiketlerinin hangi yazıyı içermesi gerektiğini kaydeder. Hiçbirisini içermeyen bir yanıt — `ja` bölümleri bir kez Rusça dolu olarak gönderilmişti — işlenmek yerine reddedilir ve yeniden denenir. O tablodan eksik olan bir dil basitçe koruma almaz, bu yüzden `i18n.json`'a bir tane eklemek asla bozmaz; kontrolü almak için girdiyi ekleyin.

## 5. Göndermeden önce çalıştırabileceğiniz kontroller

python tools/check_repo.py
```

Çeviri botunun bozabileceği ve başka hiçbir şeyin yakalayamayacağı şeyleri doğrular: her göreli bağlantı çözülür, her `labels.json` bölümü `i18n.json` ile eşleşir ve birincil olanla aynı anahtarları ve aynı `str.format` yer tutucularını taşır, her standart belge her dilde bir kopyaya sahiptir ve her markdown dosyasının dil çubuğu vardır. CI bunu her iki iş akışında da çalıştırır; hiçbir bağımlılığa ihtiyaç duymaz.

CI'ın geri kalanı ([ci.yml](../../.github/workflows/ci.yml)) betikleri derler ve tüm şekil işlem hattını çalıştırır. Bunu — gönderilen şekiller dahil — birebir yeniden üretmek için, gevşek olanı değil sabitlenmiş araç zincirini kurun:

```bash
python -m pip install -r tools/requirements-ci.txt
