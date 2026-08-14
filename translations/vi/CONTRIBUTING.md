# Cách đóng góp

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · Tiếng Việt · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Cảm ơn bạn đã muốn thúc đẩy kênh xuyên thép mở. Ba quy tắc dưới đây không phải là thủ tục hành chính — chúng là lớp giáp bằng sáng chế của dự án (xem [LICENSES.md](LICENSES.md) để biết lý do).

## 1. Giấy phép đóng góp (vào = ra)

Bằng việc gửi một đóng góp, bạn đồng ý rằng nó được cấp phép theo cùng cách như phần còn lại của tài liệu trong thư mục của nó:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Cấp bằng sáng chế.** Ngoài ra — vì CC-BY-4.0 không cấp phép sáng chế — bạn cấp cho dự án và tất cả những người nhận tài liệu của nó một giấy phép sáng chế vĩnh viễn, không thể thu hồi, trên toàn thế giới, miễn phí bản quyền, không độc quyền để chế tạo, yêu cầu người khác chế tạo, sử dụng, chào bán, bán, nhập khẩu và chuyển giao đóng góp của bạn theo những cách khác, cả tự độc lập lẫn như một phần của dự án — trong phạm vi các yêu cầu bảo hộ sáng chế của bạn mà tất yếu bị vi phạm bởi chính đóng góp đó hoặc bởi sự kết hợp của nó với dự án mà nó được gửi tới. Các điều khoản tuân theo §3 của Apache-2.0, bất kể đóng góp được đặt trong thư mục nào. Nếu bạn khởi kiện tụng sáng chế chống lại bất kỳ ai (bao gồm cả phản tố) cho rằng tài liệu của dự án vi phạm bằng sáng chế của bạn, thì tất cả các giấy phép **sáng chế** được cấp cho bạn bởi dự án và các đóng góp viên của nó theo điều khoản này và theo các giấy phép của dự án sẽ chấm dứt kể từ ngày vụ kiện tụng đó được nộp.

## 2. DCO: chữ ký về nguồn gốc

Signed-off-by: Firstname Lastname <email@example.com>
```

Các PR không có sign-off sẽ không được merge; việc kiểm tra là tự động — CI job [.github/workflows/dco.yml](../../.github/workflows/dco.yml) sẽ làm PR thất bại ngay cả khi chỉ một commit thiếu sign-off. Việc bảo vệ bằng sáng chế của lớp tài liệu dựa chính xác vào chuỗi này — không có ngoại lệ.

**Di chuyển tài liệu giữa các lớp.** Tài liệu tồn tại trong lớp mà nó được đưa vào (và dưới giấy phép của lớp đó). Việc di chuyển văn bản/mã giữa các lớp có giấy phép khác nhau chỉ được phép nếu đó là tài liệu của chính bạn, hoặc kèm theo một ghi chú rõ ràng về giấy phép gốc của đoạn tài liệu đó.

## 3. Vệ sinh bằng sáng chế và giao thức thử nghiệm

- Mọi quyết định kỹ thuật phải truy ngược được đến một nguồn tự do — một bằng sáng chế đã hết hạn hoặc một bài báo trong [docs/01-prior-art.md](docs/01-prior-art.md). Các triển khai của các yêu cầu còn hiệu lực (cũng được liệt kê tại đó) sẽ không được chấp nhận cho đến khi các yêu cầu đó hết hạn.
- Kết quả thực nghiệm — chỉ thông qua mẫu [experiments/TEMPLATE.md](experiments/TEMPLATE.md): một quy trình có ngày tháng và có thể tái lập chính xác là thứ cấu thành nên kỹ thuật đi trước của chúng ta.
- Các quyết định về kiến trúc được thực hiện thông qua các ADR trong [docs/decisions/](docs/decisions/).
- Chú thích mã, docstring, định danh và thông điệp commit chỉ dùng tiếng Anh. Tài liệu là đa ngôn ngữ (xem bên dưới); nhãn hình ảnh hiển thị với người dùng nằm trong `labels.json`.

## 4. Tài liệu đa ngôn ngữ: chỉnh sửa một ngôn ngữ, CI đồng bộ phần còn lại

Tiếng Anh là ngôn ngữ chính và sở hữu các đường dẫn chuẩn. Mọi ngôn ngữ khác là một cây phản chiếu dưới [translations/](..) với tên tệp giống hệt nhau — bao gồm markdown, BOM CSV và các hình ảnh được tạo; văn bản hình ảnh được điều khiển bởi `labels.json`. Bạn **không** phải duy trì các bản phản chiếu bằng tay:

- Hãy chỉnh sửa bất kỳ ngôn ngữ nào mà bạn thấy thoải mái. Khi đẩy (push) lên, quy trình [Translation sync](../../.github/workflows/translate.yml) sẽ dịch các bản tương ứng bằng một LLM có trọng số mở (`glm-5.2` trên Ollama Cloud), tạo lại hình ảnh khi quá trình đồng bộ cập nhật `labels.json`, và commit kết quả trở lại với dấu `[translate-sync]`. Bất kỳ điểm cuối nào tương thích với OpenAI đều hoạt động — chỉ cần đặt `OPENAI_BASE_URL` và `TRANSLATE_MODEL`.
- Những gì vẫn cần làm việc được theo dõi trong `translations/.sync-state.json`, nơi ghi lại nội dung chính mà mỗi bản dịch được tạo ra. Một lần chạy bị cắt ngắn bởi hạn ngạch hoặc thời gian chờ do đó sẽ không mất gì: các cặp chưa hoàn thành vẫn được đánh dấu là cũ và sẽ được tiếp tục bởi lần đẩy tiếp theo hoặc bởi lần chạy hàng đêm. Đừng chỉnh sửa tệp đó bằng tay.
- Nếu bạn tự chỉnh sửa **một số** ngôn ngữ của một tài liệu, mọi phiên bản bạn đã chạm vào đều được giữ nguyên như cách bạn viết; bot chỉ điền vào các ngôn ngữ mà bạn chưa chạm vào.
- **`labels.json` là ngoại lệ đối với "chỉnh sửa bất kỳ ngôn ngữ nào".** Các nhãn hình ảnh chỉ chảy từ chính → phản chiếu. Chỉnh sửa một nhãn đã dịch sẽ sửa ngôn ngữ đó và dừng lại ở đó; nó không quay ngược trở lại tiếng Anh. Để thay đổi những gì một nhãn *nói*, hãy chỉnh sửa phần chính. Lý do là sự bất đối xứng: một chỉnh sửa nhãn gần như luôn luôn là ai đó đang sửa lỗi diễn đạt của máy, và để điều đó viết lại phần chính sẽ định nghĩa lại nguồn mà tất cả mười bốn bản phản chiếu được tạo ra từ đó. Các khóa mà bot chưa từng tạo ra vẫn lan truyền ngược lại, do đó một nhãn được viết tay không bị mắc kẹt trong một ngôn ngữ.
- Bản dịch máy được commit — hãy lướt qua commit của bot và chỉnh sửa lại cách diễn đạt nếu nó bị sai giọng văn; bản sửa của bạn sẽ không bị ghi đè (bot ghi lại phiên bản của bạn là phiên bản hiện tại).
- Một phản hồi bị cắt ngắn hoặc có các trình giữ chỗ `labels.json` bị hỏng sẽ bị loại bỏ thay vì được commit, và cặp đó sẽ được thử lại — do đó một khoảng trống trông kỳ lạ trong bản phản chiếu là một cặp cũ, không phải là một quyết định.
- **PR bên ngoài:** bot chạy trên `master`, do đó một PR có thể chỉ thay đổi một ngôn ngữ — các bản phản chiếu (bao gồm cả tiếng Anh) sẽ tự động cập nhật ngay sau khi hợp nhất. Bạn không cần biết tiếng Anh để đóng góp tài liệu.
- **Thêm một ngôn ngữ:** thêm mã và tên của nó vào [i18n.json](../../i18n.json) (ví dụ: `"fr": "Français"`) và đẩy lên — quy trình sẽ xây dựng toàn bộ bản phản chiếu `translations/fr/`: mọi tài liệu, một phần `fr` trong mỗi `labels.json`, bộ hình ảnh và các công tắc chuyển đổi ngôn ngữ ở mọi nơi.
- **Chữ viết không phải Latinh:** CI cài đặt các họ phông chữ Noto (`fonts-noto-core`, `fonts-noto-cjk`) và các trình kết xuất đi qua ngăn xếp phông chữ trong `i18n.json` → `render.fonts`, do đó Cyrillic, Han, kana và Hangul hiển thị chính xác. Một trình kết xuất hiện kiểm tra mức độ bao phủ glyph trước khi vẽ và **thất bại thay vì vẽ các hộp `.notdef`** — kiểm tra đó tồn tại vì các hình ảnh tiếng Trung từng được xuất dưới dạng một lưới tofu và không có gì trong CI nhìn vào các điểm ảnh. Nếu nó kích hoạt, hãy thêm mặt Noto cho chữ viết đó vào ngăn xếp.
- **Chữ viết cần định hình theo ngữ cảnh** — tiếng Ả Rập và tiếng Ba Tư (RTL, các dạng nối), tiếng Devanagari và tiếng Bengal (các phụ âm ghép) — không thể được vẽ chính xác bởi matplotlib, vốn không có công cụ định hình: ngay cả với đúng phông chữ, các glyph vẫn xuất hiện không nối và sai thứ tự. Liệt kê các ngôn ngữ đó trong `i18n.json` → `render.skip_figures`. Văn xuôi của chúng không bị ảnh hưởng; tài liệu của chúng chỉ đơn giản liên kết đến các hình ảnh chính, mà việc sửa liên kết trong [tools/translate_sync.py](../../tools/translate_sync.py) tự động trỏ tới. `hi` được thiết lập theo cách này.
- **Bảo vệ chữ viết:** `SCRIPTS` trong [tools/i18n_render.py](../../tools/i18n_render.py) ghi lại chữ viết nào mà nhãn của mỗi ngôn ngữ phải chứa. Một phản hồi không có chữ viết đó — các phần `ja` từng được xuất đi đầy bằng tiếng Nga — sẽ bị từ chối và thử lại thay vì được commit. Một ngôn ngữ bị thiếu trong bảng đó đơn giản là không có bảo vệ, do đó việc thêm một ngôn ngữ vào `i18n.json` sẽ không bao giờ bị hỏng; hãy thêm mục vào để có được kiểm tra.

## 5. Các kiểm tra bạn có thể chạy trước khi đẩy

python tools/check_repo.py
```

Kiểm tra những gì bot dịch thuật có thể làm hỏng mà không có công cụ nào khác bắt được: mọi liên kết tương đối đều phân giải đúng, mọi phần trong `labels.json` khớp với `i18n.json` và mang cùng các khóa cũng như cùng các chỗ giữ chỗ `str.format` như bản chính, mọi tài liệu chuẩn đều có bản sao trong mọi ngôn ngữ, và mọi tệp markdown đều có thanh ngôn ngữ của nó. CI chạy nó trên cả hai luồng công việc; nó không cần dependency nào.

Phần còn lại của CI ([ci.yml](../../.github/workflows/ci.yml)) biên dịch các script và chạy toàn bộ pipeline hình ảnh. Để tái hiện chính xác — bao gồm cả các hình ảnh đã được commit — hãy cài đặt toolchain đã được ghim, chứ không phải toolchain lỏng lẻo:

```bash
python -m pip install -r tools/requirements-ci.txt
