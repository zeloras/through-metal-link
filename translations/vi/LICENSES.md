# Giấy phép và bảo vệ bằng sáng chế

> [English (primary)](../../LICENSES.md) · [Русский](../ru/LICENSES.md) · [Deutsch](../de/LICENSES.md) · [Português](../pt/LICENSES.md) · [Español](../es/LICENSES.md) · [Français](../fr/LICENSES.md) · [Italiano](../it/LICENSES.md) · [Polski](../pl/LICENSES.md) · [Türkçe](../tr/LICENSES.md) · [Українська](../uk/LICENSES.md) · Tiếng Việt · [中文](../zh/LICENSES.md) · [日本語](../ja/LICENSES.md) · [한국어](../ko/LICENSES.md) · [हिन्दी](../hi/LICENSES.md)

Mục tiêu của sơ đồ này: dự án hoàn toàn mở, bất kỳ ai cũng có thể fork và phát triển tiếp (kể cả thương mại), trong khi rủi ro kiện tụng sáng chế được cắt giảm xuống mức tối thiểu có thể đạt được bằng các biện pháp pháp lý và thủ tục.

## Sơ đồ (ba lớp; văn bản đầy đủ trong [LICENSES/](../../LICENSES))

| Khu vực | Giấy phép | Văn bản | Điều khoản sáng chế |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](../../LICENSES/Apache-2.0.txt) | §3: mọi người đóng góp tự động cấp giấy phép sáng chế cho đóng góp của họ; khởi kiện sáng chế và bạn mất giấy phép **sáng chế** (đáp trả; giấy phép bản quyền trong §2 không thể thu hồi và vẫn có hiệu lực sau vụ kiện) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](../../LICENSES/CERN-OHL-W-2.0.txt) | §7.1: giấy phép sáng chế (Make / have Made / use / sell / import…) từ mỗi bên cấp phép — nhưng chỉ cho các claim tất yếu bị vi phạm bởi Covered Source đã cho; §7.2: vụ kiện sáng chế (kể cả nỗ lực vô hiệu hóa sáng chế của người khác) chấm dứt **mọi** quyền theo giấy phép |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](../../LICENSES/CC-BY-4.0.txt) | cấp **không** quyền sáng chế (§2(b)(2)) — khoảng trống được lấp bởi sự cấp sáng chế rõ ràng trong [CONTRIBUTING.md](../../CONTRIBUTING.md) |
| mọi thứ khác (root `README.md`, `QUICKSTART.md`, file này, `data/`, v.v.) | CC-BY-4.0 | — | dự phòng: không file nào trong kho bị bỏ lại "all rights reserved" |

Các file mã mang tiêu đề SPDX (Apache-2.0); bản đồ phủ máy đọc được là [REUSE.toml](../../REUSE.toml). Dòng bản quyền nằm trong [NOTICE](../../NOTICE); file [LICENSE](../../LICENSE) ở thư mục gốc là con trỏ tới sơ đồ này.

**Tại sao CERN-OHL-W, không phải S hay P.** W là điểm trung gian: thiết kế và các sửa đổi của nó phải giữ mở khi phân phối, nhưng sản phẩm tích hợp thiết kế có thể thương mại và độc quyền — điều này giữ mở các ngách từ docs/05 (phòng thí nghiệm, nhà máy bia, khối pin). S (copyleft mạnh) sẽ đóng cửa nhúng; P (cho phép) sẽ cho phép fork đóng. Siết chặt về phía S được tích hợp sẵn trong chính giấy phép: §8.3 cho phép bất kỳ ai coi tài liệu cấp phép W như cấp phép S (miễn là điều kiện Available Components được đáp ứng) — không cần xin phép. Nới lỏng (về phía P hoặc giấy phép khác), ngược lại, chỉ khả thi khi toàn bộ tài liệu thuộc về một tác giả duy nhất; sau đóng góp bên ngoài đầu tiên — chỉ với sự đồng ý của mọi người đóng góp.

**Tên dự án.** "through-metal-link" không phải là nhãn hiệu đã đăng ký; bản thân các giấy phép không cấp quyền nào đối với tên (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Việc nhắc đến dự án theo sự thật ("based on through-metal-link") là tự do cho bất kỳ ai; các fork với thay đổi không tương thích được yêu cầu phát hành dưới tên riêng của chúng.

## Điều này bảo vệ khỏi gì — và điều nó không bảo vệ (thật thà)

**Nó bảo vệ khỏi:**
1. **Vụ kiện từ người đóng góp.** Bất kỳ ai đã đóng góp đều đã tự động cấp quyền sáng chế cho đóng góp đó (Apache §3, CERN-OHL §7.1, và CONTRIBUTING cho docs). Vụ kiện làm plaintiff trả giá đắt: theo Apache-2.0 họ mất giấy phép sáng chế cho mã; theo CERN-OHL-W họ mất toàn bộ quyền đối với lớp phần cứng (§7.2 — kích hoạt ngay cả khi nỗ lực thách thức sáng chế của người khác).
2. **Tư nhân hóa fork phần cứng.** CERN-OHL-W bắt buộc bất kỳ ai phân phối (Conveyance sản phẩm hoặc mã nguồn) phải công bố các sửa đổi thiết kế — cải tiến chảy ngược vào lớp mở và bản thân trở thành kỹ thuật trước. (Một fork trong ngăn kéo, không bao giờ truyền cho bên thứ ba, không có nghĩa vụ công bố — giống như dưới bất kỳ copyleft nào.)
3. **Sáng chế *tương lai* của người khác.** Mọi thứ được công bố có ngày tháng phá hủy tính mới cho các đơn sau: đối với giải pháp được mô tả ở đây trước ngày nộp của họ, không thể cấp sáng chế hợp lệ. Đối với đơn nộp *trước* khi chúng tôi công bố, điều này không hiệu quả — cho những cái đó, lá chắn duy nhất là lớp sáng chế đã hết hạn (xem bên dưới).

**Nó không bảo vệ khỏi:**
- **Sáng chế của bên thứ ba đã tồn tại.** Không giấy phép nào có thể làm điều đó. Cái hiệu quả chống lại chúng là kỷ luật kỹ thuật của docs/01-prior-art.md: chỉ xây dựng từ lớp đã hết hạn (public domain), không triển khai các claim còn sống được liệt kê ở đó (RPI, Drexel, và các họ Navy/ABB/Ultrapower được thêm vào 2026-08 — lưu ý rằng chúng không phải tất cả chỉ ở Mỹ và không phải tất cả hết hạn vào khoảng 2032), và truy ngược mọi quyết định thiết kế về một nguồn tự do. Đó không phải là bảo đảm, nhưng chính xác là thực hành làm cho vụ kiện trở nên vô ích.
- Một fork hướng tới sản xuất thương mại tự làm phân tích FTO (freedom to operate) cho khu vực pháp lý và thiết kế của riêng mình — kho không đưa ra tuyên bố sáng chế nào (tuyên bố từ chối trong cả ba giấy phép).

## Giao thức công bố phòng thủ (tiếp tục thực thi khi các cột mốc được công bố)

Mọi kết quả công bố là kỹ thuật trước có ngày tháng, chặn mọi đơn ứng dụng bên thứ ba sau này cho cùng giải pháp:

1. Giữ nguyên lịch sử git công khai đầy đủ (commits = timestamps).
2. Chụp vào **Zenodo** → DOI: một kho lưu trữ độc lập với ngày tháng có ý nghĩa pháp lý, có thể trích dẫn trong bài báo.
3. Ghim vào **Software Heritage** (archive.softwareheritage.org — một bản sao vĩnh viễn).
4. Mỗi thử nghiệm hoàn thành `experiments/NNN` — với ngày tháng, con số, và biểu đồ: đó là công bố một giải pháp kỹ thuật cụ thể.
5. Các cột mốc lớn (watt đầu tiên, node đầu tiên) — một bài viết ra thế giới bên ngoài (Hackaday.io / arXiv / blog): lan rộng càng rộng, trạng thái kỹ thuật trước càng mạnh.

## Dành cho người đóng góp

Các quy tắc nằm trong [CONTRIBUTING.md](../../CONTRIBUTING.md): DCO sign-off, inbound=outbound, một sự cấp sáng chế rõ ràng trên mỗi đóng góp bất kể thư mục, khả năng truy ngược quyết định thiết kế tới kỹ thuật trước tự do.

Kho đã công khai. Tiếp tục giao thức trên ở mỗi cột mốc (chụp Zenodo, ghim Software Heritage, bài viết thử nghiệm) để kỹ thuật trước có ngày tháng giữ vững khi kết quả đến.
