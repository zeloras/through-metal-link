# through-metal-link

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · Tiếng Việt · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Một nền tảng mở cho truyền tải điện năng và dữ liệu siêu âm xuyên qua vách kim loại đặc — "xuyên thép mà không cần một lỗ khoan nào", được xây dựng bằng phương tiện cấp garage.

**Thử ngay (không cần phần cứng):** `python3 software/sweep-map/sweep_map.py --mock`

**Trạng thái:** giai đoạn 0 — chuẩn bị · 💰 **[thưởng $250 cho bản dựng độc lập đầu tiên](https://github.com/zeloras/through-metal-link/issues)** · danh sách mua sắm: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

Tài liệu đa ngôn ngữ: tiếng Anh là ngôn ngữ chính và nằm ở các đường dẫn gốc; mọi ngôn ngữ khác phản chiếu cây thư mục dưới [translations/](..). Chỉnh sửa bất kỳ ngôn ngữ nào — CI sẽ dịch và commit phần còn lại (xem [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Giai đoạn 1 rig: Pi → DDS → half-bridge → biến áp → piezo TX | thép | piezo RX → cầu chỉnh lưu → ADC → Pi" width="900"></p>

## Ý tưởng trong một đoạn văn

Sóng radio không đi qua được kim loại (lồng Faraday), và việc đâm cáp xuyên qua đồng nghĩa với một lỗ hổng, một lớp hàn kín, và một điểm dễ hỏng hóc. Ngược lại, sóng siêu âm truyền qua kim loại rất tốt: một phần tử piezo ở mỗi bên của bức tường biến nó thành một kênh truyền tải điện năng và dữ liệu. Các tài liệu nghiên cứu trong phòng thí nghiệm đã chứng minh nguyên lý vật lý ở mức độ nghiêm túc (RPI: 50 W + 12 Mbit/s xuyên qua 63.5 mm thép; NASA JPL: lên tới ~kW xuyên qua 5 mm titan) — đây là những bằng chứng về tính khả thi với phần cứng chuyên dụng, chứ không phải danh sách linh kiện (BOM) tự chế trong gara của repo này. Các bằng sáng chế nền tảng đã hết hạn, và hiện vẫn chưa có một nền tảng mở, có thể tái tạo nào — kho lưu trữ này đang xây dựng một nền tảng như vậy, bắt đầu với **công suất cấp watt và dữ liệu kbit/s xuyên qua 3–5 mm thép** sau khi giai đoạn 2 được đo lường.

## Lộ trình

| Giai đoạn | Sản phẩm bàn giao | Tiêu chí thành công | Kỳ vọng |
|---|---|---|---|
| 1. Bản đồ quét | đáp ứng tần số của kênh "Langevin–3 mm thép–Langevin" | tìm được cặp cộng hưởng, biểu đồ trong [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. Công suất | công suất vào tải tại cộng hưởng | ≥0,5 W xuyên qua 3 mm thép, giao thức trong [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](docs/img/sim4-power-budget.png) |
| 3. Dữ liệu | FSK/OOK qua cùng cặp đó | ≥1 kbit/s không lỗi | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. Nút | ESP32 + cảm biến trong hộp hàn kín, cấp nguồn và truyền dữ liệu chỉ bằng âm thanh | ≥1 giờ hoạt động tự chủ | [sim4](docs/img/sim4-power-budget.png) |
| 5. Xuất bản | repo công khai, bài viết/hướng dẫn | tái tạo được bởi bên thứ ba | — |

## Sơ đồ kho lưu trữ

python3 software/sweep-map/sweep_map.py --mock
```

**Hoàn thành khi (theo từng giai đoạn):** giai đoạn 1 — đỉnh quét tái lặp qua hai lần chạy với sai số <200 Hz ([experiments/001](experiments/001-sweep-map-3mm-steel/README.md)); giai đoạn 2 — ≥0.5 W vào một tải đã biết xuyên qua 3 mm thép và đèn LED sáng từ phía RX ([experiments/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Lý thuyết trong một phút</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

Piezo TX được ép sát vào vách và truyền một sóng dọc vào trong; piezo RX ở phía bên kia chuyển nó trở lại thành điện. Vận tốc âm thanh trong thép: ~5900 m/s.

Hai chế độ hoạt động:

| Chế độ | Tần số | Cộng hưởng đặt bởi | Đầu ra | Trạng thái |
|---|---|---|---|---|
| **A** — biến áp Langevin | 40 kHz | cặp biến áp (vách ≪ λ — một "màng") | watt, kbit/s | chế độ bắt đầu (giai đoạn 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — đĩa | 0.6–1 MHz | cộng hưởng theo độ dày của vách ([lược đồ](docs/img/sim3-thickness-comb.png)) | hàng trăm mW, hàng trăm kbit/s | nhánh sau những watt đầu tiên; cần theo dõi tần số tự động |

Các tổn thất chính: sự không khớp cộng hưởng trong cặp (±1 kHz đối với biến áp Langevin rẻ tiền), chất lượng tiếp xúc âm (epoxy > mỡ bôi trơn + kẹp > áp lực khô), lệch trục, trôi cộng hưởng theo nhiệt độ. Câu trả lời cho tất cả đều giống nhau: **lập bản đồ quét trước mỗi thay đổi đối với thiết lập**.

</details>

<details>
<summary><b>📈 Hệ thống sẽ hiển thị gì: biểu đồ kỳ vọng từ trình mô phỏng</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Mô hình kênh bán thực nghiệm (không phải FEM, **không phải dữ liệu phòng thí nghiệm** — trực giác về "quét trông sẽ như thế nào và hướng tới điều gì"). Các giả định được nêu rõ trong `channel_sim.py` (Q tải ≈40, hệ số tiếp xúc, hiệu suất chuỗi η≤40%). Tạo lại bằng: `python3 channel_sim.py --out ../../docs/img`.

**Giai đoạn 1 — quét.** Một đỉnh hẹp gần ~40 kHz; các hệ số tiếp xúc giữ chỗ của mô hình là mỡ:khô:khe hở = 1 : 0.25 : 0.02 (tức là mỡ ≈4× khô và ≈50× khe hở không khí). Không có đỉnh nghĩa là có vấn đề về tiếp xúc hoặc cặp biến áp:

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**Tại sao 4 biến áp Langevin, chứ không phải 2.** Với Q≈40, sự không khớp cộng hưởng 1.5 kHz trong cặp làm giảm công suất mô hình ~10×:

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**Giai đoạn 3 — dữ liệu.** OOK vấp phải hiện tượng cộng hưởng dao động (mô hình Q~40 → τ≈0.3 ms): 1 kbit/s rất sạch, ở 5 kbit/s mắt đã đóng. Để đi nhanh hơn cần chế độ B:

<img src="docs/img/sim5-ook-datarate.png" width="720">

**Ngân sách công suất thu.** Các dải tô bóng là **mục tiêu** (chế độ A 0.5–5 W nếu giai đoạn 2 thành công; chế độ B thấp hơn). Các tải thực tế ban đầu là ESP32 / BLE / LED chu kỳ nhiệm vụ; Wi-Fi được hiển thị như một điểm đánh dấu tiêu thụ đỉnh, không phải một cam kết liên tục:

<img src="docs/img/sim4-power-budget.png" width="720">

**Cho sau này (chế độ B).** Tấm thép trở nên trong suốt tại một lược đồ cộng hưởng theo độ dày — tần số phải được theo dõi:

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ An toàn — đọc trước khi cấp điện lần đầu tiên</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Hàng chục đến hàng trăm volt trên piezo** ngay khi driver giai đoạn 2 hoạt động — TVS ở phía thu phải được lắp TRƯỚC khi chạy cấp điện lần đầu; không chạm tay vào các dây dẫn.
2. **Điện lưới** — chỉ thông qua nguồn bench / cách ly; mạch driver của máy siêu âm được nối trực tiếp với điện lưới.
3. **Tai** — ở công suất không nhỏ, chỉ vận hành biến áp khi đã ép chặt vào kim loại; không bao giờ chạy siêu âm công suất cao trong không khí mà không có vỏ bọc.
4. **Nhiệt** — một biến áp Langevin không được kẹp sẽ quá nhiệt trong vài phút khi có công suất; kẹp lại trước khi tăng dòng điện (chỉ chạy điện dòng thấp ngắn hạn — xem README của driver).
5. **Mảnh vỡ** — gốm áp điện giòn: một bu-lông siết quá chặt hoặc một va đập sẽ tạo ra mảnh vỡ; đeo kính an toàn cho bất kỳ công việc cơ khí nào.

</details>

docs/            lý thuyết, prior art, an toàn, ứng dụng, nhật ký quyết định (ADR)
docs/img/        đồ thị kỳ vọng (do software/simulator/channel_sim.py sinh ra)
hardware/        BOM, driver (cầu bán), receiver (chỉnh lưu/harvester)
firmware/        firmware nút (ESP32 — stub đến giai đoạn 4)
software/        script đo (bản đồ quét đáp ứng tần số) và mô phỏng kênh
experiments/     giao thức thí nghiệm — từ template, một thư mục = một thí nghiệm
data/            log thô (file lớn không đưa vào git)
```

</details>

## Nguyên lý

1. **Khả năng tái tạo từ con số không.** Bất kỳ ai có một mỏ hàn và khoảng $210 đều có thể tái tạo kết quả chỉ từ repo này.
2. **Mỗi thí nghiệm là một quy trình.** Không có kiểu "nó cũng hoạt động được": [experiments/TEMPLATE.md](experiments/TEMPLATE.md) là bắt buộc.
3. **Vệ sinh bằng sáng chế.** Chúng tôi xây dựng dựa trên lớp đã hết hạn bảo hộ ([docs/01-prior-art.md](docs/01-prior-art.md)); các quyết định được ghi lại tại [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md).
4. **Đo lường trước, ý kiến sau.** Phải có bản đồ quét trước khi đưa ra bất kỳ kết luận nào về kênh truyền.

## Giấy phép và bằng sáng chế

Mã nguồn — Apache-2.0, phần cứng — CERN-OHL-W v2, tài liệu — CC-BY-4.0; toàn văn tại [LICENSES/](../../LICENSES). Bất kỳ ai cũng có thể fork và phát triển dựa trên dự án này, kể cả mục đích thương mại; bảo hộ bằng sáng chế đến từ các điều khoản cấp quyền và phản đòn trong giấy phép, cùng với chiến lược sáng chế trước. Toàn bộ sơ đồ và giao thức công bố phòng ngự: [LICENSES.md](LICENSES.md); quy tắc đóng góp: [CONTRIBUTING.md](CONTRIBUTING.md).
