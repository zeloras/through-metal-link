# Nasıl Katkıda Bulunulur

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · Türkçe · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Çelik içinden geçen açık kanalı ilerletmek istediğiniz için teşekkür ederiz. Aşağıdaki üç kural bürokrasi değil — projenin patent zırhdır (nedenini [LICENSES.md](LICENSES.md) dosyasında görebilirsiniz).

## 1. Katkı lisansları (gelen = giden)

Bir katkı göndererek, bulunduğu dizindeki diğer materyallerle aynı şekilde lisanslandığını kabul etmiş olursunuz:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Patent izni.** Buna ek olarak — CC-BY-4.0 patentleri lisanslamadığından — projeye ve materyallerinin tüm alıcılarına, katkınızı tek başına ve projenin parçası olarak yapmak, yaptırmak, kullanmak, satışa sunmak, satmak, ithal etmek ve başka şekillerde devretmek için süresiz, geri alınamaz, dünya çapında, telifsiz, münhasır olmayan bir patent lisansı verirsiniz — bu izin, katkının tek başına veya gönderildiği projeyle birlikte kullanılmasıyla kaçınılmaz olarak ihlal edilen patent taleplerinizin kapsamıyla sınırlıdır. Şartlar, katkının hangi dizine yerleştiğine bakılmaksızın Apache-2.0 §3'ü izler. Eğer projenin materyallerinin patentinizi ihlal ettiğini iddia ederek herhangi birine (karşı dava dahil) patent davası açarsanız, o davın açıldığı tarihten itibaren bu madde ve projenin lisansları kapsamında size verilen tüm **patent** lisansları sona erer.

## 2. DCO: kaynak üzerine bir imza

Her commit bir sign-off taşır (`git commit -s`), [Developer Certificate of Origin 1.1](https://developercertificate.org/) ile anlaşmayı ifade eder: bu katkıyı projenin lisansı altında gönderme hakkına sahip olduğunuzu teyit edersiniz.

```
Signed-off-by: Ad Soyad <email@example.com>
```

Sign-off içermeyen PR'lar birleştirilmez; denetim otomatiktür — [.github/workflows/dco.yml](../../.github/workflows/dco.yml) CI işi, tek bir commit bile sign-off içermiyorsa PR'ı başarısız sayar. Doküman katmanının patent koruması tam olarak bu zincire dayanır — istisnasız.

**Materyallerin katmanlar arasında taşınması.** Materyal, yerleştiği katmanda (ve o katmanın lisansı altında) yaşar. Farklı lisanslara sahip katmanlar arasında metin/kod taşınması yalnızca kendi malınız ise veya parçanın orijinal lisansının açık bir notuyla izinlidir.

## 3. Patent hijyeni ve deney protokolü

- Her teknik karar özgür bir kaynağa dayanmalıdır — süresi dolmuş bir patent veya [docs/01-prior-art.md](docs/01-prior-art.md) içindeki bir makale. Orada da listelenen yaşan taleplerin uygulamaları, o taleplerin süresi dolana kadar kabul edilmez.
- Deneysel sonuçlar — yalnızca [experiments/TEMPLATE.md](experiments/TEMPLATE.md) şablonuyla: tarihli, yeniden üretilebilir bir protokol tam olarak bizim önceki sanatımızı oluşturan şeydir.
- Mimari kararlar [docs/decisions/](docs/decisions/) içindeki ADR'lerden geçer.
- Kod yorumları, docstring'ler, tanımlayıcılar ve commit mesajları yalnızca İngilizcedir. Dokümanlar çok dillidir (aşağıya bakın); kullanıcıya görünür şekil etiketleri `labels.json` içinde yaşar.

## 4. Çok dilli dokümanlar: bir dili düzenleyin, CI gerisini senkronize eder

İngilizce birincildir ve kanonik yollara sahiptir. Diğer her dil, [translations/](..) altında aynı dosya adlarına sahip bir ayna ağacıdır — markdown, BOM CSV ve üretilen şekiller dahil; şekil metni `labels.json` tarafından yönlendirilir. Aynaları elle korumak **zorunda değilsiniz**:

- Rahat ettiğiniz dili düzenleyin. Push sırasında [Translation sync](../../.github/workflows/translate.yml) iş akışı, karşıtları açık ağırlıklı bir LLM ile çevirir (Ollama Cloud üzerinde `glm-5.2`), senkronizasyon `labels.json`'u güncellediğinde şekilleri yeniden üretir ve sonucu `[translate-sync]` işaretçisiyle geri commit eder. Herhangi bir OpenAI-uyumlu uç nokta çalışır — `OPENAI_BASE_URL` ve `TRANSLATE_MODEL` ayarlayın.
- Hâlâ iş gerektiren kısımlar `translations/.sync-state.json` içinde izlenir; bu dosya her çevirinin hangi birincil içerikten yapıldığını kaydeder. Kota veya zaman aşımıyla yarıda kesilen bir çalışma bu yüzden hiçbir şey kaybetmez: yarım kalan çiftler eski olarak işaretlenir ve bir sonraki push veya gece çalışması tarafından alınır. O dosyayı elle düzenlemeyin.
- Bir dokümanın **birkaç** dilini kendiniz düzenlediyseniz, dokunduğunuz her sürüm yazdığınız gibi korunur; bot yalnızca dokunmadığınız dilleri doldurur.
- **`labels.json`, "herhangi bir dili düzenle" kuralının istisnasıdır.** Şekil etiketleri yalnızca birincil → aynalar akar. Çevrilmiş bir etiketi düzenlemek o dili düzeltir ve orada durur; İngilizceye geri dönmez. Bir etiketin *ne söylediğini* değiştirmek için birincil bölümü düzenleyin. Bunun nedeni asimetridir: bir etiket düzenlemesi neredeyse her zaman birinin makinenin söz dizimini düzeltmesidir ve bunun birincili yeniden yazması, on dört aynanın üretildiği kaynağı yeniden tanımlamak olur. Botun hiç üretmediği anahtarlar yine de geri yayılır, böylece elle yazılmış bir etiket tek bir dile sıkışıp kalmaz.
- Makine çevirisi commit edilir — bot'un commit'ini gözden geçirin ve tonu kaçırırsa söz dizimini düzeltin; düzeltmenizin üzerine yazılmaz (bot sürümünüzü güncel sürüm olarak kaydeder).
- Kesilmiş veya `labels.json` yer tutucuları bozuk dönen bir yanıt commit edilmez, atılır ve çift yeniden denenir — bu yüzden bir aynadaki tuhaf bir boşluk eski bir çifttir, bir karar değil.
- **Dış PR'lar:** bot `master` üzerinde çalışır, bu yüzden bir PR yalnızca bir dili değiştirebilir — aynalar (İngilizce dahil) birleştirmeden hemen sonra otomatik olarak yetişir. Dokümanlara katkıda bulunmak için İngilizce bilmeniz gerekmez.
- **Dil ekleme:** kodunu ve adını [i18n.json](../../i18n.json) dosyasına ekleyin (ör. `"fr": "Français"`) ve push yapın — pipeline tüm `translations/fr/` aynasını oluşturur: her doküman, her `labels.json` içinde bir `fr` bölümü, şekil seti ve her yerde dil değiştiriciler.
- **Latin alfabesi dışı yazılar:** CI Noto ailelerini kurar (`fonts-noto-core`, `fonts-noto-cjk`) ve renderer'lar `i18n.json` → `render.fonts` içindeki yazı tipi yığınını izler, böylece Kiril, Han, kana ve Hangul düzgün çıkar. Bir renderer artık çizmeden önce glyph kapsamını denetler ve **`.notdef` kutuları çizmek yerine başarısız olur** — bu denetim, Çinçe şekiller bir tofu ızgarası olarak gönderildiği ve CI'da hiçbir şey piksellere bakmadığı için var. Tetiklenirse, o yazı için Noto yüzünü yığına ekleyin.
- **Bağlamsal şekillendirme gerektiren yazılar** — Arapça ve Farsça (RTL, bitişik formlar), Devanagari ve Bengalce (birleşik harfler) — bir şekillendirme motoru olmayan matplotlib tarafından doğru çizilemez: doğru yazı tipi olsa bile glyph'ler bitişik olmayan ve yanlış sıralı çıkar. Bu dilleri `i18n.json` → `render.skip_figures` içinde listeleyn. Düz metinleri etkilenmez; dokümanları yalnızca birincil şekillere bağlantı verir, bu bağlantıları [tools/translate_sync.py](../../tools/translate_sync.py) içindeki bağlantı onarımı otomatik olarak yönlendirir. `hi` bu şekilde ayarlanmıştır.
- **Yazı koruması:** [tools/i18n_render.py](../../tools/i18n_render.py) içindeki `SCRIPTS`, her dilin etiketlerinin hangi yazıyı içermesi gerektiğini kaydeder. Hiçbiri olmayan bir yanıt — `ja` bölümleri bir kez Rusça dolu gönderilmişti — commit edilmez ve yeniden denenir. O tablodan eksik olan bir dil yalnızca koruma almaz, böylece `i18n.json`'a bir tane eklemek asla bozmaz; denetimi almak için girdiyi ekleyin.

## 5. Push öncesi çalıştırabileceğiniz denetimler

```bash
python tools/check_repo.py
```

Çeviri botunun bozabileceği ve başka hiçbir şeyin yakalayamayacağı şeyleri doğrular: her göreli bağlantı çözülür, her `labels.json` bölümü `i18n.json` ile eşleşir ve birincil olanla aynı anahtarları ve aynı `str.format` yer tutucularını taşır, her kanonik dokümanın her dilde bir aynası vardır ve her markdown dosyasının dil çubuğu vardır. CI bunu her iki iş akışında da çalıştırır; bağımlılığa ihtiyaç duymaz.

CI'ın geri kalanı ([ci.yml](../../.github/workflows/ci.yml)) script'leri derler ve tüm şekil pipeline'ını çalıştırır. Bunu tam olarak — commit edilmiş şekiller dahil — yeniden üretmek için gevşek olanı değil, sabitlenmiş araç zincirini kurun:

```bash
python -m pip install -r tools/requirements-ci.txt
```
