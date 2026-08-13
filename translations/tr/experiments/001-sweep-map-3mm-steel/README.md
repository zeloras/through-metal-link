# Deney 001: Kanal Tarama Haritası, 3 mm Çelik (PLANLI)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · Türkçe · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **Aşama:** 1 (yalnızca frekans haritası — burada watt hedefi yoktur; güç [002](../../../../experiments/002-watts-3mm-steel/README.md) numaralı deneyedir).
- **Hedef:** bir Langevin transdüser çiftinin 3 mm levha üzerinden rezonansını bulmak; kanalın ilk frekans tepkisini elde etmek.
- **Hipotez:** 38–42 kHz civarında bir tepe (Langevin transdüser rezonansı), gres+kelepçe teması altında birkaç kHz'lik tepe genişliği.
- **Sürücü:** aşama-1 bağlantısı — TX'e AD9833 sinüs (~0.6 Vpp), **half-bridge yok** ([sch3](../../../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png)).
- **Prosedür:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (donanım olmadan hattı denemek için `--mock` kullanın).
- **Başarı ölçütü:** tekrarlanabilir bir tepe (ardı ardına iki tarama, merkez sapması <200 Hz). CSV/PNG dosyalarını `data/` altına kaydedin ve gerçek olduğunda bu dosyadan bağlayın.
- **Ek ölçüm:** aynı tarama "gres kuplan + kelepçe" ile "kuru basınç" karşılaştırması — yalnızca göreli genlikler; mutlak voltlar sürücü seviyesine bağlıdır ve kalibre edilene kadar simülatörün yer tutucu ölçeğiyle karşılaştırılamaz.
- **Kapsam dışı:** ≥0.5 W, hasattan LED, half-bridge devreye alma → deney 002.
