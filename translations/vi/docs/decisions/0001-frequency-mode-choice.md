# ADR-0001: Lựa chọn chế độ tần số cho Giai đoạn 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · Tiếng Việt · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Trạng thái: ĐÃ CHẤP NHẬN (sẽ xem xét lại sau Giai đoạn 2)
- Ngày: 2026-07-24

## Bối cảnh
Hai chế độ (xem docs/00-theory.md): A — 28–40 kHz trên bộ biến đổi Langevin, B — 0.6–1 MHz trên đĩa tận dụng cộng hưởng theo chiều dày vách.

## Quyết định
Giai đoạn 1–2 chạy chế độ A. Lý do: rẻ hơn ($10–30 mỗi cái), mạnh hơn (watt so với hàng trăm mW), dễ điều chỉnh hơn (cộng hưởng rộng), và mạch điều khiển có thể xây dựng từ nửa cầu quanh IR2110. Chế độ B đến sau khi ta đưa được những watt đầu tiên xuyên qua — như một nhánh riêng cho dữ liệu tốc độ cao.

## Hệ quả
Dữ liệu ở Giai đoạn 3 sẽ chậm (kbit/s) — đủ cho một nút cảm biến. ADC ADS1115 (860 SPS) là phù hợp cho bao biên tại 40 kHz sau bộ chỉnh lưu, nhưng không đủ cho lấy mẫu trực tiếp — lấy mẫu trực tiếp bị hoãn sang chế độ B (cần một ADC khác).

Giai đoạn 1 (quét) chỉ dùng tín hiệu DDS yếu; Giai đoạn 2 (watt) là một thí nghiệm và triển khai riêng ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)). Các dải công suất của bộ mô phỏng vẫn là mục tiêu cho đến khi 002 được đo.
