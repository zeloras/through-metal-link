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

## Những gì chúng tôi không sao chép khi còn sống (chỉ áp dụng tại Mỹ, đến ~2032; các giai đoạn 1–4 cũng không cần)
OFDM với các sóng mang con đặt để né hài của kênh điện năng (RPI US9054826); song công toàn bộ "downlink AM + uplink điều chế tải + dò tần số" như một sơ đồ duy nhất (RPI US9455791); transducer dạng bám theo bề mặt cong theo cách tiếp cận của Drexel (US10594409).
