# Thí nghiệm 001: Bản đồ quét kênh, thép 3 mm (ĐÃ LÊN KẾ HOẠCH)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · Tiếng Việt · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **Giai đoạn:** 1 (chỉ lập bản đồ tần số — không có mục tiêu công suất ở đây; công suất là [002](../../../../experiments/002-watts-3mm-steel/README.md)).
- **Mục tiêu:** tìm cộng hưởng của cặp đầu chuyển Langevin qua tấm thép 3 mm; thu được đáp ứng tần số đầu tiên của kênh.
- **Giả thuyết:** đỉnh quanh 38–42 kHz (tần số cộng hưởng của đầu chuyển Langevin), độ rộng đỉnh vài kHz dưới tiếp xúc mỡ+băng kẹp.
- **Kích:** đấu nối giai đoạn 1 — sin AD9833 (~0.6 Vpp) vào TX, **không** half-bridge ([sch3](../../../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png)).
- **Quy trình:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (dùng `--mock` để chạy thử pipeline mà không cần phần cứng).
- **Tiêu chí thành công:** một đỉnh có thể tái lặp (hai lần quét liên tiếp, độ lệch tâm <200 Hz). Lưu CSV/PNG dưới `data/` và liên kết chúng từ tệp này khi có dữ liệu thật.
- **Đo lường bổ sung:** cùng một lần quét với "mỡ ghép + kẹp" so với "ép khô" — chỉ so biên độ tương đối; điện áp tuyệt đối phụ thuộc vào mức kích và không thể so sánh với thang placeholder của bộ mô phỏng cho đến khi hiệu chuẩn.
- **Ngoài phạm vi:** ≥0.5 W, LED thu năng lượng, đưa half-bridge lên → thí nghiệm 002.
