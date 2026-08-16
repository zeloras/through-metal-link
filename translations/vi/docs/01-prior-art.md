# Tiền nhân: những gì chúng tôi kế thừa

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · Tiếng Việt · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## Quy tắc
Mọi quyết định kỹ thuật trong repo này phải truy ngược được đến một nguồn thuộc danh sách "miễn phí" (bằng sáng chế đã hết hạn, bài báo). Bằng sáng chế còn hiệu lực chỉ được đọc — khai thác chúng để hiểu vấn đề, không bao giờ sao chép claims của chúng (điều này quan trọng cho thương mại hóa tại Mỹ; xem bản đồ bằng sáng chế trong dự án).

## Nền tảng miễn phí (bằng sáng chế hết hạn/bỏ ngang = thuộc về công cộng)
- **US5982297** (Aerospace Corp, 1997) — công thức cơ bản: một cặp piezo xuyên qua vách, điện năng + dữ liệu hai chiều. Sách hướng dẫn chính.
- US5594705 (Dynamotive, 1994) — một "biến áp âm" xuyên qua vỏ.
- US6037704, US6127942 (Aerospace Corp) — cấp nguồn cho cảm biến, đọc dữ liệu trả về.
- **US7902943** (Caltech/JPL, bỏ ngang do không đóng phí duy trì năm 2019) — feed-through Sherrit: phản xạ, biến áp âm.
- US9748870 (Caltech/JPL) — truyền cơ học xuyên qua vách.
- **US9361877** (Univ. Oklahoma, bỏ ngang do không đóng phí duy trì) — một hệ thu phát hoàn chỉnh hiện đại.
- US20100027379 / WO2008105947 (DOE+RPI, bỏ ngang) — sóng mang từ bên ngoài + điều chế tải từ bên trong.

## Các bài báo chủ chốt
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s, thép 63.5 mm.
- Sherrit et al., NASA NTRS 20080048150 — một bóng đèn 100 W được cấp nguồn xuyên qua vách.
- Yang et al., Sensors 2015 (10.3390/s151229870) — bài tổng quan, tóm tắt tốt nhất các con số.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — siêu vật liệu, 2%→66% xuyên qua 1 mm thép không gỉ (chưa tìm thấy bằng sáng chế tính đến 07.2026).

Các bài báo này là **chuẩn cơ sở về vật lý và vệ sinh bằng sáng chế**. Các con số công suất/tốc độ bit của họ dùng transducer phòng thí nghiệm, kết dính và matching — không phải BOM Langevin AliExpress + mỡ trong [QUICKSTART.md](../QUICKSTART.md). Trích dẫn chúng như bằng chứng tồn tại; các tiêu chuẩn đạt riêng của dự án nằm trong [experiments/](../../../experiments).

## Những gì chúng tôi không sao chép khi còn sống
Lõi cũ của danh sách này chỉ áp dụng tại Mỹ và hết hạn vào khoảng 2032–2033, và các giai đoạn 1–4 không cần bất kỳ điều nào trong đó: OFDM với các sóng mang con đặt để né hài của kênh điện năng (RPI US9054826); song công toàn bộ "downlink AM + uplink điều chế tải + dò tần số" như một sơ đồ duy nhất (RPI US9455791); transducer dạng bám theo bề mặt cong theo cách tiếp cận của Drexel (US10594409). Các họ dưới đây không thuộc nhóm đó: một họ đọc trên kênh điện năng trần của giai đoạn 2, và một họ có hiệu lực tại châu Âu đến 2039.

**Thêm vào bởi lần tìm kiếm 2026-08 (trạng thái là cờ Google Patents — kiểm tra lại trong USPTO Patent Center / Sổ đăng ký EP trước khi sử dụng thương mại):**
- **US8594572B1** (Hải quân Mỹ, ưu tiên 2011-06, đóng phí 12 năm năm 2025, có hiệu lực đến 2032-01, chỉ tại Mỹ) — claim 1 là "vách + nguồn điện + transducer chuyển dòng điện thành siêu âm xuyên qua vách + transducer chuyển ngược lại + thiết bị điện tử được cấp nguồn", không giới hạn tần số, vật liệu hay độ dày: nó đọc theo nghĩa đen trên kênh điện năng trần tại Mỹ. Bằng sáng chế US5982297 của Welle (1997) công bố cùng cách bố trí, nên lớp đã hết hạn cũng là phòng thủ vô hiệu; tuy nhiên, một nhánh thương mại tại Mỹ nên xin ý kiến FTO.
- **EP3723304B1** (ABB, ưu tiên 2019-04, cấp 2023-08, duy trì **chỉ tại DE và GB** — CH hết hạn 2024-04, không tìm thấy xác nhận nào khác trong dữ liệu sổ đăng ký đã đọc; đến 2039-04; không có thành viên tại Mỹ) — một "dẫn sóng âm" (vách bình trong phần mô tả) truyền điện năng *và* dữ liệu trả về cho nền tảng cảm biến, **nơi phổ mang điện năng thấp hơn phổ dữ liệu**. Giới hạn đó được nhập từ một claim phụ trong quá trình xét duyệt để được cấp, đây là cách thiết kế lách của chúng tôi: uplink dự kiến là điều chế tải trên *cùng* sóng mang 40 kHz ([docs/03](03-discovery-protocol.md)) — các dải biên quanh sóng mang điện năng, không phải dải tần cao hơn (đọc claim, không phải ý kiến FTO). Không thêm sóng mang dữ liệu tần số cao riêng (ví dụ của ABB: dữ liệu 200–300 kHz trên điện năng tần số thấp) vào liên kết điện năng mode-A trong sản phẩm cho DE/GB.
- **Họ Ultrapower** (ưu tiên 2014-03, đến 2035-03): US10295500B2 — cảm biến bên trong *ống* kim loại, thu phát bên ngoài, mảng transducer **lồi/lõm**; US10684260B2 / US10948457B2 — thanh kim loại *xuyên qua* vách. Chúng tôi dùng đệm phay mặt phẳng và không dùng thanh.
- **US9602221B2** (Zackat Inc.; các sự kiện bảo đảm/chuyển nhượng ghi tên Anelto Inc. / Instant Care Inc.; ưu tiên 2014-03, phục hồi 2021, đóng phí 2024, đến 2035-10, Mỹ) — claim 1: bộ phát siêu âm trên "thiết bị Class 1" bên trong vùng có nguy cơ cháy nổ, bộ thu bên ngoài, cảnh báo cho vận hành viên từ xa; **claim độc lập 14 bỏ giới hạn thiết bị Class 1** (bất kỳ cảm biến nào bên trong vùng có nguy cơ cháy nổ + liên kết siêu âm + cảnh báo). Chỉ liên quan nếu một node từng phát cảnh báo ra khỏi vùng nguy hiểm — lý do để giữ mọi ứng dụng như vậy ở quy mô phòng thí nghiệm tại Mỹ.
- Liên quan gián tiếp, ghi chú: GE US9146266B2 (telemetry xuyên qua cấu trúc phát điện, đến 2033), UNT US11415555 (SAW/BAW thụ động xuyên vách), CEA EP4080791B1 (tối ưu tần số quét trở kháng), RPI US9331879B2 (MIMO), US9505031B2 (vỏ có lò xo). Claim 1 của RPI US9455791B2 có chứa điều chế tải MOSFET cho transducer bên trong — nhưng chỉ đi kèm với downlink AM vi sai, lấy mẫu đồng bộ chuỗi Barker và thuật toán dò/tìm tần số; [docs/03](03-discovery-protocol.md) cố ý không có downlink AM/Barker nào, và toàn bộ tổ hợp đó không được triển khai khi bằng sáng chế còn hiệu lực.
- Miễn phí, xác nhận thêm: Progeny/General Dynamics US20120127833A1 (tần số điện/dữ liệu riêng — **bỏ ngang**), RPI/DOE US20100027379A1 (uplink điều chế tải — bỏ ngang).
