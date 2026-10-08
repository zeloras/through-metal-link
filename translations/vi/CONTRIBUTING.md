# Đóng góp như thế nào

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · Tiếng Việt · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Cảm ơn bạn muốn thúc đẩy kênh xuyên thép mở. Ba quy tắc dưới đây không phải là quan liêu — chúng là lớp giáp bằng sáng chế của dự án (xem [LICENSES.md](LICENSES.md) để biết lý do).

## 1. Giấy phép đóng góp (đầu vào = đầu ra)

Khi gửi một đóng góp, bạn đồng ý rằng nó được cấp phép theo cùng cách với phần còn lại của tài liệu trong thư mục chứa nó:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Cấp bằng sáng chế.** Ngoài ra — vì CC-BY-4.0 không cấp phép bằng sáng chế — bạn cấp cho dự án và tất cả người nhận tài liệu của nó một giấy phép bằng sáng chế vĩnh viễn, không thể thu hồi, toàn cầu, miễn phí bản quyền, không độc quyền để chế tạo, thuê chế tạo, sử dụng, chào bán, bán, nhập khẩu và chuyển nhượng đóng góp của bạn theo các cách khác, cả độc lập lẫn như một phần của dự án — trong phạm vi các yêu cầu bằng sáng chế của bạn bị vi phạm tất yếu bởi chính đóng góp đó hoặc bởi sự kết hợp của nó với dự án mà nó được gửi tới. Các điều khoản tuân theo §3 của Apache-2.0, bất kể đóng góp nằm trong thư mục nào. Nếu bạn khởi kiện bằng sáng chế chống lại bất kỳ ai (bao gồm cả phản tố) cho rằng tài liệu của dự án vi phạm bằng sáng chế của bạn, thì tất cả giấy phép **bằng sáng chế** được cấp cho bạn bởi dự án và các đóng góp viên theo điều khoản này và theo giấy phép của dự án sẽ chấm dứt kể từ ngày kiện tụng được nộp.

## 2. DCO: chữ ký xác nhận nguồn gốc

Mỗi commit đều mang một sign-off (`git commit -s`), thể hiện sự đồng ý với [Developer Certificate of Origin 1.1](https://developercertificate.org/): bạn xác nhận rằng bạn có quyền gửi đóng góp này theo giấy phép của dự án.

```
Signed-off-by: Firstname Lastname <email@example.com>
```

PR thiếu sign-off sẽ không được merge; kiểm tra này là tự động — CI job [.github/workflows/dco.yml](../../.github/workflows/dco.yml) sẽ làm PR thất bại ngay cả khi chỉ một commit duy nhất thiếu sign-off. Việc bảo vệ bằng sáng chế của lớp tài liệu dựa chính xác vào chuỗi này — không có ngoại lệ.

**Di chuyển tài liệu giữa các lớp.** Tài liệu tồn tại trong lớp mà nó được đặt vào (và dưới giấy phép của lớp đó). Việc di chuyển văn bản/mã giữa các lớp có giấy phép khác nhau chỉ được phép nếu đó là tài liệu của chính bạn, hoặc kèm theo ghi chú rõ ràng về giấy phép gốc của đoạn tài liệu đó.

## 3. Vệ sinh bằng sáng chế và giao thức thử nghiệm

- Mọi quyết định kỹ thuật phải truy ngược được đến một nguồn miễn phí — một bằng sáng chế đã hết hạn hoặc một bài báo từ [docs/01-prior-art.md](docs/01-prior-art.md). Các hiện thực hóa của yêu cầu còn hiệu lực (được liệt kê tại đó) sẽ không được chấp nhận cho đến khi các yêu cầu đó hết hạn.
- Kết quả thử nghiệm — chỉ thông qua mẫu [experiments/TEMPLATE.md](experiments/TEMPLATE.md): một giao thức có ngày tháng và có thể tái lặp chính xác là điều cấu thành kỹ thuật trước đây của chúng ta.
- Quyết định kiến trúc đi qua các ADR trong [docs/decisions/](docs/decisions/).
- Chú thích mã, docstring, định danh và thông điệp commit chỉ dùng tiếng Anh. Tài liệu đa ngôn ngữ (xem bên dưới); nhãn hình ảnh hiển thị cho người dùng nằm trong `labels.json`.

## 4. Tài liệu đa ngôn ngữ: chỉnh sửa một ngôn ngữ, CI đồng bộ phần còn lại

Tiếng Anh là ngôn ngữ chính và sở hữu các đường dẫn chuẩn. Mọi ngôn ngữ khác là một cây phản chiếu dưới [translations/](..) với tên tệp giống hệt — bao gồm markdown, CSV BOM và hình ảnh được tạo; văn bản hình ảnh được điều khiển bởi `labels.json`. Bạn **không** cần phải bảo trì các bản phản chiếu thủ công:

- Chỉnh sửa bất kỳ ngôn ngữ nào mà bạn thấy thoải mái. Khi push, workflow [Translation sync](../../.github/workflows/translate.yml) sẽ dịch các bản tương ứng bằng một LLM trọng số mở (`glm-5.2` trên Ollama Cloud), tạo lại hình ảnh khi sync cập nhật `labels.json`, và commit kết quả trở lại với đánh dấu `[translate-sync]`. Bất kỳ endpoint tương thích OpenAI nào cũng hoạt động — chỉ cần đặt `OPENAI_BASE_URL` và `TRANSLATE_MODEL`.
- Những gì vẫn cần làm thêm được theo dõi trong `translations/.sync-state.json`, tệp này ghi lại nội dung chính mà mỗi bản dịch được tạo ra. Một lần chạy bị cắt ngắn bởi hạn ngạch hoặc timeout do đó không mất gì: các cặp chưa hoàn thành vẫn được đánh dấu là cũ và sẽ được nhặt lại bởi lần push tiếp theo hoặc bởi lần chạy hằng đêm. Đừng chỉnh sửa tệp đó bằng tay.
- Nếu bạn đã tự chỉnh sửa **một số** ngôn ngữ của một tài liệu, mọi phiên bản bạn đã chạm vào sẽ được giữ nguyên như bạn đã viết; bot chỉ điền vào các ngôn ngữ mà bạn chưa chạm tới.
- **`labels.json` là ngoại lệ đối với quy tắc "chỉnh sửa bất kỳ ngôn ngữ nào".** Các nhãn hình ảnh chỉ theo hướng chính → phản chiếu. Chỉnh sửa một nhãn đã dịch sẽ sửa ngôn ngữ đó và dừng lại ở đó; nó không quay ngược trở lại tiếng Anh. Để thay đổi nội dung mà một nhãn *nói*, hãy chỉnh sửa phần chính. Lý do là sự bất đối xứng: một lần chỉnh sửa nhãn gần như luôn là ai đó đang sửa cách diễn đạt của máy, và để điều đó ghi đè lên phần chính sẽ định nghĩa lại nguồn mà tất cả mười bốn bản phản chiếu được tạo ra. Các khóa mà bot chưa từng tạo ra vẫn lan truyền ngược trở lại, nên một nhãn viết tay không bị mắc kẹt trong một ngôn ngữ.
- Bản dịch máy được commit — hãy lướt qua commit của bot và chỉnh sửa cách diễn đạt nếu nó bỏ sót giọng văn; bản sửa của bạn sẽ không bị ghi đè (bot ghi lại phiên bản của bạn là phiên bản hiện tại).
- Một phản hồi bị cắt ngắn hoặc có placeholder `labels.json` bị hỏng sẽ bị loại bỏ thay vì commit, và cặp đó sẽ được thử lại — vì vậy một khoảng trống trông kỳ lạ trong bản phản chiếu là một cặp cũ, không phải một quyết định.
- **PR bên ngoài:** bot chạy trên `master`, nên một PR có thể chỉ thay đổi một ngôn ngữ — các bản phản chiếu (bao gồm tiếng Anh) sẽ tự động bắt kịp ngay sau khi merge. Bạn không cần biết tiếng Anh để đóng góp tài liệu.
- **Thêm một ngôn ngữ:** thêm mã và tên ngôn ngữ đó vào [i18n.json](../../i18n.json) (ví dụ `"fr": "Français"`) và push — pipeline sẽ xây dựng toàn bộ bản phản chiếu `translations/fr/`: mọi tài liệu, một phần `fr` trong mỗi `labels.json`, bộ hình ảnh và các bộ chuyển ngôn ngữ ở mọi nơi.
- **Chữ viết không Latinh:** CI cài đặt các bộ phông Noto (`fonts-noto-core`, `fonts-noto-cjk`) và các trình kết xuất duyệt theo ngăn xếp phông trong `i18n.json` → `render.fonts`, nên Cyrillic, Han, kana và Hangul hiển thị đúng. Một trình kết xuất hiện nay kiểm tra độ phủ glyph trước khi vẽ và **thất bại thay vì vẽ các ô `.notdef`** — kiểm tra đó tồn tại vì các hình ảnh tiếng Trung từng xuất bản dưới dạng lưới tofu và không có gì trong CI nhìn vào pixel. Nếu nó kích hoạt, hãy thêm phông Noto cho chữ viết đó vào ngăn xếp.
- **Chữ viết cần định hình theo ngữ cảnh** — Arabic và Persian (RTL, dạng nối), Devanagari và Bengali (conjuncts) — không thể được vẽ đúng bởi matplotlib, vốn không có engine định hình: ngay cả với đúng phông, các glyph vẫn rời rạc và sai thứ tự. Liệt kê các ngôn ngữ đó trong `i18n.json` → `render.skip_figures`. Văn xuôi của chúng không bị ảnh hưởng; tài liệu của chúng chỉ đơn giản liên kết đến hình ảnh chính, mà việc sửa liên kết trong [tools/translate_sync.py](../../tools/translate_sync.py) tự động trỏ tới. `hi` được thiết lập theo cách này.
- **Bảo vệ chữ viết:** `SCRIPTS` trong [tools/i18n_render.py](../../tools/i18n_render.py) ghi lại chữ viết mà nhãn của mỗi ngôn ngữ phải chứa. Một phản hồi không có chữ viết đó — các phần `ja` từng xuất bản đầy tiếng Nga — sẽ bị từ chối và thử lại thay vì commit. Một ngôn ngữ thiếu trong bảng đó đơn giản là không có bảo vệ, nên việc thêm vào `i18n.json` không bao giờ gây hỏng; hãy thêm mục vào để có được kiểm tra.

## 5. Các kiểm tra bạn có thể chạy trước khi push

```bash
python tools/check_repo.py
```

Kiểm tra những gì bot dịch có thể làm hỏng và không gì khác có thể bắt được: mọi liên kết tương đối đều phân giải, mọi phần `labels.json` khớp với `i18n.json` và mang cùng các khóa và cùng các placeholder `str.format` như phần chính, mọi tài liệu chuẩn đều có bản phản chiếu trong mọi ngôn ngữ, và mọi tệp markdown đều có thanh ngôn ngữ của nó. CI chạy nó trên cả hai workflow; nó không cần dependency.

Phần còn lại của CI ([ci.yml](../../.github/workflows/ci.yml)) biên dịch các script và chạy toàn bộ pipeline hình ảnh. Để tái lặp chính xác — bao gồm cả các hình ảnh đã commit — hãy cài đặt toolchain đã ghim, không phải toolchain lỏng lẻo:

```bash
python -m pip install -r tools/requirements-ci.txt
```
