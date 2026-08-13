# Bản đồ ứng dụng: ai cần bộ công nghệ này, và tại sao

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · [Deutsch](../../de/docs/05-applications-map.md) · [Português](../../pt/docs/05-applications-map.md) · [Español](../../es/docs/05-applications-map.md) · [Français](../../fr/docs/05-applications-map.md) · [Italiano](../../it/docs/05-applications-map.md) · [Polski](../../pl/docs/05-applications-map.md) · [Türkçe](../../tr/docs/05-applications-map.md) · [Українська](../../uk/docs/05-applications-map.md) · Tiếng Việt · [中文](../../zh/docs/05-applications-map.md) · [日本語](../../ja/docs/05-applications-map.md) · [한국어](../../ko/docs/05-applications-map.md) · [हिन्दी](../../hi/docs/05-applications-map.md)

Bộ nền tảng: một kênh cấp nguồn và truyền dữ liệu chủ động xuyên qua vách kín — piezo-acoustic / EMAT / từ trường tần số thấp (LF). Dưới đây: nơi nào cần điều này trong thế giới thực, ai đã ở đó, và còn gì lại cho chúng tôi.

## 1. Khối pin kín (xe điện, lưu trữ năng lượng gia dụng/công nghiệp)
- Nỗi đau: phát hiện sớm hiện tượng thoát nhiệt — các khí (CO₂, H₂, hơi chất điện phân) xuất hiện bên trong khối pin từ vài phút đến vài giờ trước khi cháy; một lỗ cảm biến xuyên qua vỏ = mất kín khí và mất chứng nhận.
- Bộ công nghệ của chúng tôi: một node khí/nhiệt độ bên trong khối pin, cấp nguồn và telemetry qua một cặp piezo xuyên 2–3 mm nhôm. Không khoan lỗ.
- Ai đã ở đó: Liminal Insights — *chẩn đoán âm thanh từ bên ngoài* (bằng sáng chế về phương pháp phân tích, không phải về kênh truyền). Chưa ai bán node *bên trong* khối pin.
- Độ chín của ngách: thị trường đang tăng trưởng bùng nổ, kệ vẫn trống. Đối với nền tảng — ứng dụng trình diễn số 1.

## 2. Thiết bị phòng thí nghiệm: buồng chân không, cryostat, hộp găng tay
- Nỗi đau: mỗi đường dẫn điện xuyên vào buồng chân không là một mặt bìa trị giá hàng trăm đô la và là nguồn rò rỉ; trong cryostat, một dây cáp = rò nhiệt.
- Bộ công nghệ của chúng tôi: một cảm biến bên trong buồng, cấp nguồn/dữ liệu bằng âm thanh xuyên qua vách thép; cho cấu trúc chân không dạng sandwich của dewar — từ trường LF (vài bit/s là đủ cho logger nhiệt độ).
- Ai đã ở đó: chưa ai có giải pháp xuyên vách không dây; các phòng lab sống dựa vào mặt bìa feedthrough.
- Độ chín: ngách khởi đầu lý tưởng cho mã nguồn mở — phòng lab chính xác là đối tượng của phần cứng mở (con đường TinyLev): họ mua mà không cần chứng nhận và trích dẫn bạn trong bài báo.

## 3. Sản xuất thực phẩm: bồn lên men, nồi hấp tiệt trùng (bia, rượu vang, sữa)
- Nỗi đau: quy định vệ sinh ghét mọi lỗ xuyên (rửa CIP, vùng chết); bạn muốn biết mật độ/nhiệt độ/áp suất bên trong bồn liên tục.
- Bộ công nghệ của chúng tôi: một node trên thành trong của bồn inox, truy vấn từ bên ngoài bằng máy quét cầm tay hoặc một cặp cố định.
- Ai đã ở đó: cảm biến gắn lỗ thông thường; chưa có giải pháp xuyên vách không dây.
- Độ chín: hoàn toàn trong tầm tay một bài kiểm tra trong gara (bất kỳ xưởng bia thủ công nào cũng là bãi thử trong tầm đi bộ).
- Lưu ý vật lý: một bồn đầy sẽ tải trọng lên vách — quét lại đối với vessel đầy, và giữ công suất liên tục ≲1 W/cm²; vượt mức đó, cavitation sẽ xảy ra trong sản phẩm (thoát khí CO₂, vị lạ, xói mòn vách lâu dài) — [lý thuyết](00-theory.md#effect-on-the-wall-and-the-media-behind-it).

## 4. Đường ống, bình chịu áp, NDT công nghiệp
- Nỗi đau: theo dõi ăn mòn/thông số bên trong mà không cần ngừng máy hay khoan lỗ; bề mặt nóng, đã sơn, bẩn.
- Bộ công nghệ của chúng tôi: một "súng quét" EMAT — áp vào ống với không cần chuẩn bị bề mặt, đọc beacon thụ động cộng hưởng từ bên trong.
- Ai đã ở đó: đồng hồ lưu lượng siêu âm gắn ngoài và đo độ dày (một thị trường trưởng thành), nhưng chưa có beacon tương tác bên trong.
- Độ chín: tầm trung; yêu cầu nhánh EMAT (giai đoạn ~6).

## 5. Dầu khí / giếng khoan, và hạt nhân
- Ai đã ở đó: Metrol, Acoustic Data, Baker Hughes (giếng khoan, 30 năm, mô hình dịch vụ); R&D DOE/UNT/Westinghouse (thùng chứa hạt nhân).
- Phán quyết thẳng thắn: đã bị chiếm và bị quản lý nặng — chúng tôi không vào đó, nhưng chính sự tồn tại của họ = bằng chứng rằng vật lý này bán được giá trị lớn. Dùng làm tài liệu tham khảo trong README.

## 6. Hàng hải và cấu trúc dưới nước
- Nỗi đau: "hàng hóa còn sống không" trong container kín; dữ liệu từ mặt trong vỏ tàu.
- Ai đã ở đó: CSignum (EM tần số thấp xuyên nước/vách ngăn) — người láng giềng trực tiếp duy nhất trong triết lý lai.
- Độ chín: dài hạn; đối với chúng tôi, hiện nay chỉ là một hướng suy nghĩ.

## Ưu tiên (làm gì, theo thứ tự nào)
1. **Ngay bây giờ:** các giai đoạn nền tảng 1–4 trên kịch bản trình diễn "buồng lab / hộp hàn kín" (ngách #2 — cởi mở nhất với mã nguồn mở).
2. **Tiếp theo:** một demo trên đối tượng thực tế từ ngách #3 (bồn bia) — rẻ, ăn ảnh, người dùng thật.
3. **Tầm trung:** kịch bản pin (ngách #1) làm case flagship để công bố; nhánh EMAT cho ngách #4.

*Tầm nhìn thụ động (chụp xạ muon) đã được tách thành một dự án riêng — xem muon-lab trong knowledge base.*
