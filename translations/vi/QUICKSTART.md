# QUICKSTART: từ con số 0 đến dàn thử nghiệm giai đoạn 1–2

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · [Português](../pt/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · [Français](../fr/QUICKSTART.md) · [Italiano](../it/QUICKSTART.md) · [Polski](../pl/QUICKSTART.md) · [Türkçe](../tr/QUICKSTART.md) · [Українська](../uk/QUICKSTART.md) · Tiếng Việt · [中文](../zh/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [한국어](../ko/QUICKSTART.md) · [हिन्दी](../hi/QUICKSTART.md)

Kịch bản: bạn chẳng có gì ngoài một chiếc bàn và chút tiền. Mọi thứ dưới đây sẽ đưa bạn đến một dàn chạy được — "bản quét + vài watt đầu tiên xuyên thép". Giá chỉ là ước lượng, tính bằng USD.

## Rổ 1 — dụng cụ (nền tảng dùng nhiều năm, ~$120)

| Vật dụng | Lý do | Giá | Mua ở đâu |
|---|---|---|---|
| Trạm hàn (bản sao T12) | mọi thứ | 35–50 | Ali |
| Đồng hồ vạn năng (hạng AN8008/UT61) | điện áp, thông mạch, điện dung | 15–25 | Ali |
| Nguồn bàn 30V/5A có giới hạn dòng | cấp cho driver; giới hạn dòng là bảo hiểm chống cháy MOSFET | 45–60 | Ali/địa phương |
| Tay giữ, nhựa hàn, flux, băng tháo hàn, kìm cắt cạnh, nhíp | mấy món nhỏ không thể thiếu | 15 | Ali/địa phương |
| Dây Dupont + breadboard + co nhiệt | làm nguyên mẫu | 8 | Ali |

## Rổ 2 — điện tử cho dàn (~$70)

| Vật dụng | Số lượng | Giá | Ghi chú |
|---|---|---|---|
| Raspberry Pi (Zero 2 W là đủ; 4/5 thoải mái hơn) + SD | 1 | 20–60 | bộ não: quét, nhật ký, vẽ đồ thị |
| Biến áp Langevin 40 kHz 50–60 W | **4** | 40 | mua 4 từ MỘT lô; ta sẽ chọn cặp tốt nhất bằng cách quét |
| Module DDS AD9833 | 2 | 8 | cái thứ hai là dự phòng |
| IR2110 + IRF540 ×4 (hoặc module EGS002) | 1 bộ | 10 | driver nửa cầu |
| ADC ADS1115 | 2 | 4 | Pi không có ADC riêng |
| Lõi ferrite + dây đồng 0.5 mm | 2 | 4 | biến áp khớp |
| Cầu Schottky (SS14 ×8), siêu tụ 1F 5.5V ×2 | 1 | 4 | mạch thu |
| TVS SMBJ5.0A ×3 + SMBJ15CA ×2 | 1 | 2 | bảo vệ. ĐỪNG TIẾT KIỆM |
| Module GY-LTC3588 | 1 | 7 | mạch thu năng (giai đoạn 4, nhưng cứ đặt hàng luôn) |
| Bộ điện trở/tụ, LED | 1 | 8 | nếu bạn chẳng có gì |
| Linh kiện thụ động bổ trợ: UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | vài xu; danh sách đầy đủ — BOM mục 11–12 |

## Rổ 3 — cơ khí (~$20, mua địa phương)

Tấm thép 3 mm ~150×150 — 2 cái (xưởng kim loại / cắt laser); kẹp kiểu F ×2; mỡ bôi trơn đồng nhất đặc (mỡ lithium); epoxy; giấy nhám (để làm sạch bề mặt tiếp xúc).

## Tùy chọn, nhưng rất nên có (~$90)

| Vật dụng | Lý do | Giá |
|---|---|---|
| Máy hiện sóng USB/cầm tay (FNIRSI/Hantek, 2 kênh; bạn không cần băng thông ≥40 MHz — 10 là dư) | xem dạng sóng trên cổng và trên piezo; tiết kiệm hàng ngày gỡ lỗi driver | 60–80 |
| ESP32 DevKit ×2 | giai đoạn 4 (node phía sau tường) | 8 |

**Tổng cộng: tối thiểu ~$210, thoải mái ~$300.** (Nếu bạn đã có sẵn Pi, trạm hàn và nguồn bàn — trừ đi ~$120.)

## Đơn đặt hàng (đường tới hạn là thời gian giao hàng)

1. Hôm nay: rổ 2 từ Ali (giao 3–4 tuần — đây là đường tới hạn) + máy hiện sóng.
2. Tuần này: rổ 1 và 3 mua địa phương.
3. Trong lúc chờ giao: `raspi-config` → SPI+I2C, chạy `software/sweep-map/sweep_map.py --mock` không cần phần cứng (kênh mô phỏng — toàn bộ pipeline CSV+đồ thị chạy được trên bất kỳ máy nào), đọc docs/00–03, xem các đồ thị kỳ vọng trong docs/img và sơ đồ nguyên lý trong hardware/schematics (bản dựng giai đoạn 1 theo sch3 và sch2).

## Bạn sẽ thấy gì (mô phỏng: software/simulator/channel_sim.py → docs/img)

Các PNG này là **kỳ vọng từ mô hình**, không phải số đo thực tế. Tỷ lệ tiếp xúc, Q tải ≈40, và hiệu suất mạch ≤40% là các giả định tường minh trong `channel_sim.py` — thay bằng dữ liệu quét/công suất khi dàn đã có.

- `sim0-rig-sketch.png` — toàn bộ dàn trong một bản phác (mạch giai đoạn 2; giai đoạn 1 bỏ qua nửa cầu và kích TX bằng sóng sin DDS yếu).
- `sim1-sweep-contacts.png` — dạng quét kỳ vọng: đỉnh hẹp gần ~40 kHz; mô hình dùng tỷ lệ mỡ:khô:khe ≈ 1 : 0.25 : 0.02 làm giá trị tạm. Không có đỉnh — gỡ lỗi tiếp xúc hoặc sai lệch cặp trước (sim2).
- `sim2-pair-mismatch.png` — lý do cần 4 biến áp Langevin chứ không 2: với Q≈40, lệch cộng hưởng 1.5 kHz trong một cặp làm công suất mô hình giảm ~10×; bước quét chọn cặp tốt nhất trong 4.
- `sim3-thickness-comb.png` — dành cho sau này (mode B, MHz): tấm thép trong suốt như một lược các cộng hưởng theo chiều dày, nên tần số phải được bám theo.
- `sim4-power-budget.png` — dòng tải so với các **dải công suất thu** mục tiêu. Dải mode A (0.5–5 W) là tham vọng giai đoạn 2 nếu khớp và tiếp xúc phối hợp; mode B là dải thấp hơn. Wi-Fi liên tục là điểm đánh dấu tải đỉnh, không phải lời hứa — ESP32/BLE/LED chu kỳ nhiệm vụ là những tiêu thụ thực tế đầu tiên.
- `sim5-ook-datarate.png` — giai đoạn 3: lý do OOK trên biến áp Langevin dừng ở ~1–2 kbit/s với Q≈40 (ring-down τ≈0.3 ms), và lý do điều đó ổn cho một node cảm biến.

## Tiêu chí "dàn chạy được"

Chia theo giai đoạn — đừng đánh dấu giai đoạn 1 xong bằng số của giai đoạn 2.

**Giai đoạn 1 — bản quét** ([experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md)):
1. Quét 25–45 kHz trong hai lần chạy liên tiếp: tâm đỉnh lặp lại trong sai số <200 Hz.
2. Thưởng tùy chọn: mỡ+kẹp so với ép khô trên cùng cặp (biên độ tương đối, không phải watt tuyệt đối).

**Giai đoạn 2 — watt đầu tiên** ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)):
1. Nửa cầu + biến áp khớp hoạt động; bật nguồn có giới hạn dòng theo [docs/02-safety.md](../../docs/02-safety.md) và [hardware/driver/](../../hardware/driver/README.md).
2. Tại cộng hưởng giai đoạn 1, ≥0.5 W vào tải điện trở đã biết xuyên qua 3 mm thép (đo V và I phía DC sau cầu RX).
3. LED phía sau tấm sáng từ năng lượng thu được; ảnh + CSV trong experiments/002.

An toàn trước khi cấp điện lần đầu: [docs/02-safety.md](../../docs/02-safety.md) (TVS phía thu, giới hạn dòng nguồn ở 0.2 A khi bật, không chạy Langevin công suất cao ngoài không khí).
