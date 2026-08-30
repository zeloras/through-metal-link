# Vật liệu vách tường ngoài thép: vách nào truyền được điện năng và dữ liệu

> [English (primary)](../../../docs/06-materials.md) · [Русский](../../ru/docs/06-materials.md) · [Deutsch](../../de/docs/06-materials.md) · [Português](../../pt/docs/06-materials.md) · [Español](../../es/docs/06-materials.md) · [Français](../../fr/docs/06-materials.md) · [Italiano](../../it/docs/06-materials.md) · [Polski](../../pl/docs/06-materials.md) · [Türkçe](../../tr/docs/06-materials.md) · [Українська](../../uk/docs/06-materials.md) · Tiếng Việt · [中文](../../zh/docs/06-materials.md) · [日本語](../../ja/docs/06-materials.md) · [한국어](../../ko/docs/06-materials.md) · [हिन्दी](../../hi/docs/06-materials.md)

Phần còn lại của repo này giả định thép. Trang này đặt câu hỏi đơn giản hơn, lớn hơn: **với vật liệu vách nào thì kênh hai-bộ-transducer hoạt động được**, và ở chế độ nào? Đây là một nghiên cứu mô phỏng (kiểu `--mock`, không có dữ liệu thực nghiệm — trực giác về thứ đáng để làm thử nghiệm phần cứng), được xây dựng từ cùng mô hình bán thực nghiệm như [channel_sim](../../../software/simulator/channel_sim.py) và mở rộng với hấp thụ khối.

Sinh: `python3 software/simulator/material_map.py` (cần numpy + matplotlib). Mô hình và giả thuyết: [../software/simulator/material_map.py](../../../software/simulator/material_map.py).

## Mô hình trong một phút

Ba đại lượng quyết định xem một vách tường có dùng được hay không, và cho bao nhiêu điện năng:

1. **Tương phản trở kháng và pha** — mô hình tấm Fabry–Perot không tổn thất, giống hệt [channel_sim](../../../software/simulator/channel_sim.py):
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_wall / Z_couplant, couplant Z = 1.5 MRayl (mỡ).
   Tại cộng hưởng nửa bước sóng (f = c/2d) một tấm đối xứng không tổn thất hoàn toàn trong suốt *bất kể r*; tương phản r quyết định **rộng** bao nhiêu của các răng lược (dung sai sai số tần số), tốc độ âm thanh c quyết định khoảng cách giữa chúng (Δf = c/2d).
2. **Hấp thụ khối**, không nhìn thấy trong mô hình không tổn thất và là yếu tố quyết định cho nhựa, bê tông và cao su:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, một chiều, dọc],
   trong đó α₁ₘₕᶻ là giá trị tại 1 MHz.
   γ ≈ 1 = tổn thất nhớt/khuếch tán; γ > 2 = tán xạ trên các không đồng nhất (cốt liệu bê tông).
3. **Liều lượng mà vách nhận lại** — xem phần [bên dưới](#the-dose-what-the-wave-does-to-the-wall-frequency-by-frequency): ứng suất σ = √(2·I·Z), *không* phụ thuộc tần số, và tự gia nhiệt ΔT ∝ α(f)·I, có phụ thuộc.

**Giả thuyết, nêu nơi mà code nêu chúng:** thuộc tính sổ tay điển hình (sóng dọc, ~20 °C); vật liệu thực tế thay đổi — hạt, chất độn, cốt liệu, quá trình đóng rắn. Mọi thứ dưới đây là một bảng xếp hạng, không phải datasheet.

| Vách | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | lược Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | ghi chú |
|---|---|---|---|---|---|---|---|---|
| steel | 7850 | 5900 | 46.3 | 0.02 | 590 | 148 | 0.21 | thép kết cấu hạt mịn |
| aluminum | 2700 | 6320 | 17.1 | 0.02 | 632 | 158 | 0.69 | lớp 6061 |
| titanium | 4430 | 6100 | 27.0 | 0.03 | 610 | 152 | 0.45 | Ti-6Al-4V |
| copper | 8960 | 4760 | 42.6 | 0.05 | 476 | 119 | 0.17 | đặc, Z rất cao |
| borosilicate glass | 2230 | 5640 | 12.6 | 0.01 | 564 | 141 | 0.77 | tổn thất rất thấp |
| alumina ceramic | 3890 | 9900 | 38.5 | 0.08 | 990 | 248 | 0.51 | âm nhanh, tổn thất thấp |
| PMMA (acrylic) | 1180 | 2690 | 3.2 | 2.5 | 269 | 67 | 0.95 | trong suốt, bị hấp thụ giới hạn tại MHz |
| PVC (rigid) | 1400 | 2380 | 3.3 | 6 | 238 | 60 | 0.92 | tổn thất hơn PMMA |
| HDPE | 950 | 2340 | 2.2 | 12 | 234 | 58 | 0.98 | mềm, tổn thất cao |
| concrete | 2300 | 3500 | 8.1 | 5 | 350 | 88 | 0.77 | tán xạ cốt liệu trội; thay đổi nhiều bậc độ lớn |
| rubber (filled) | 1100 | 1500 | 1.6 | 60 | 150 | 38 | 0.85 | ngõ cụt thành thật |

## Các biểu đồ

**Chế độ B (MHz) — lược độ dày theo từng vật liệu.** Trái: kim loại kết cấu; phải: phi kim. Tất cả vách 5 mm, ghép bằng mỡ. Đỉnh mô hình không tổn thất đạt T = 1 tại cộng hưởng chính xác; đỉnh thực thấp hơn do tổn thất tiếp xúc, và hấp thụ giới hạn trực tiếp các vật liệu tổn thất cao:

<img src="../../../docs/img/mat1-thickness-comb-materials.png" width="880">

**Bản đồ vật liệu** — hai trục quyết định tất cả: trở kháng (độ khó ghép/tiếp xúc) so với hấp thụ tại 1 MHz (khả thi ở MHz). Góc Z cao + α thấp là góc cấp điện năng; góc Z thấp + α cao là "40 kHz vẫn mở, MHz chết"; góc cao su là ngõ cụt ở mọi tần số chúng ta nhắm tới:

<img src="../../../docs/img/mat2-material-map.png" width="720">

**Proxy ghép chế độ A (40 kHz)** — cùng mô hình truyền đánh giá tại 40 kHz qua vách 3 mm, chuẩn hóa theo thép. *Bảng xếp hạng, không phải watt:* cặp Langevin cộng hưởng nhân mỗi thanh xấp xỉ bằng nhau và mô hình không có tải transducer bên trong; hệ số nhân đó là lĩnh vực giai đoạn-2 ([experiments/002](../experiments/002-watts-3mm-steel/README.md)):

<img src="../../../docs/img/mat3-modea-coupling-materials.png" width="720">

## Quét cho biết gì

- **Tại 40 kHz, vách Z thấp (nhựa, lớp lót cao su) ghép *dễ hơn* thép** — qua mỡ chúng gần như khớp trở kháng, nên lược rộng và truyền qua mỗi lần cao. Cái giết nhựa ở tần số cao hơn là **hấp thụ khối**, không phải tiếp xúc hay trở kháng. Thang vật liệu ở 40 kHz do đó đảo ngược so với trực giác: HDPE/PMMA/PVC > kính/bê tông > nhôm > alumina > titan > thép > đồng — với cảnh báo mạnh rằng số 40 kHz của cao su ngoại suy α tuyến tính xuống từ 1 MHz, điều mà tính nhớt đàn hồi không đảm bảo.
- **Chế độ B chia vật liệu rõ ràng.** Kim loại, kính và alumina chịu MHz với hấp thụ không đáng kể (α ≤ 0.1 dB/cm); lược *sắc* cho vách Z cao (thép, alumina — cần theo dõi tần số, bài học ~6% ⇒ ~10× của [00-theory](00-theory.md)) và *rộng* cho kính/PMMA (dung sai lớn, nhưng PMMA trả ~1.3 dB một chiều tại 1 MHz qua 5 mm — chỉ cấp mW).
- **Bê tông là vật liệu 40 kHz, không phải MHz.** Tán xạ cốt liệu (λ tại 1 MHz ≈ 3.5 mm ≈ kích thước cốt liệu) đẩy γ lên ~2.5 và giết MHz; thực hành đo vận tốc siêu âm (40–80 kHz qua đường ≥1 m) chính xác là chế độ A.
- **Ngách pin ([05](05-applications-map.md)) có lợi về mặt âm:** vách nhôm 2–3 mm có proxy ghép ~3× thép và hấp thụ không đáng kể — trường hợp flagship cũng là trường hợp dễ nhất.
- **Thang tần số cần lên kế hoạch trong chế độ B** (vách 5 mm, lược đầu tiên): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, đồng ≈ 480, thép ≈ 590, titan ≈ 610, nhôm ≈ 630, kính ≈ 560, alumina ≈ 990. Vách mỏng hơn ⇒ cao hơn tỷ lệ thuận.

## Liều lượng: sóng làm gì với vách, tần số từng tần số

Truyền trả lời "bao nhiêu đi qua"; phần này trả lời câu hỏi ngược — **bao nhiêu sóng ở lại trong vách, và điều đó có hại không?** Tổn thương sóng-trong-vách có đúng hai mặt:

- **Ứng suất** σ = √(2·I·Z) — động lượng sóng phẳng; *không phụ thuộc tần số*. So sánh với giới hạn mỏi chu kỳ cao (kim loại), cường độ uốn/kéo (gốm, kính, bê tông, cao su).
- **Tự gia nhiệt** ΔT = α(f)·I·d²/(8k), trạng thái dừng, hai mặt làm mát — *phụ thuộc tần số* qua α(f), và đó là nơi tần số cắn: mọi vật liệu cách nhiệt đều có điểm gãy mà trên đó mỗi quãng tám tần số thêm vào nhân bội nhiệt tích lũy.

Tại 1 W/cm² (đã vượt quá mục tiêu của dự án này: mục tiêu giai đoạn-2 là 0.5–5 W trải trên mặt transducer ~19 cm² là 0.03–0.26 W/cm²):

| Vách | σ @1 W/cm², MPa | giới hạn σ_e, MPa | biên độ ứng suất | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | trần @40 kHz, W/cm² | trần @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| steel | 0.96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| aluminum | 0.58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| titanium | 0.74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| copper | 0.92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| borosilicate glass | 0.50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| alumina ceramic | 0.88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (acrylic) | 0.25 | 15 | 60× | 0.2 | 9.5 | 65 | ~100 | 2.1 |
| PVC (rigid) | 0.26 | 15 | 58× | 0.6 | 28.8 | 199 | ~33 | 0.7 |
| HDPE | 0.21 | 8 | 38× | 0.15 | 19.2 | 215 | ~58 | 1.0 |
| concrete | 0.40 | 2.5 | 6× | ~0 | 2.1 | 118 | 1.6 | 1.6 |
| rubber (filled) | 0.18 | 1.5 | 8× | 11.5 | 288 | 1440 | 1.7 | 0.07 |

"Trần" = cường độ liên tục mà tại đó vách nằm trong 20% giới hạn mỏi/cường độ và dưới +20 K tự gia nhiệt (trạng thái dừng, hai mặt giữ ở nhiệt môi trường). Chạy chu kỳ nhiệm vụ ít nóng hơn; vách chỉ neo một mặt — trường hợp thường gặp, không khí một bên — nóng tới 4× nhiều hơn ở mặt tự do. Các con số này là cắt đầu tiên, không phải bảo đảm thiết kế. Một lưu ý quy ước: giá trị α là intensity-dB (10·log₁₀, quy ước đo liều — giảm 3 dB thì I giảm một nửa); tài liệu NDT pulse-echo dùng amplitude-dB (20·log₁₀) mô tả CÙNG α với số lớn gấp đôi — kiểm tra quy ước nào mà nguồn dùng trước khi chép số vào bảng này.

<img src="../../../docs/img/mat4-harm-materials.png" width="920">

Quét liều lượng cho biết:

- **Phán quyết thép của [00-theory](00-theory.md) vẫn đứng và tổng quát hóa**: mọi kim loại kết cấu chịu 1 W/cm² với biên độ 65–680× về ứng suất và micro-kelvin về tự gia nhiệt. Kim loại không nhạy tần số về tổn thương — tổn thất của chúng quá nhỏ để nóng ở bất kỳ công suất nào ta có thể ghép.
- **Tổn thương tần số trên polyme là nhiệt, không cơ học.** Biên độ ứng suất PMMA thoải mái 60× ngay cả tại 1 W/cm², nhưng điểm gãy nhiệt nằm ngay khoảng 1 MHz: lành (~0.2 K) tại 40 kHz, +9.5 K tại 1 MHz, +65 K tại 5 MHz — vùng mềm hóa ở vài W/cm². PVC vượt đường +10 K đã tại ~0.35 W/cm² @ 1 MHz; cao su hấp thụ ~288 K mỗi W·cm⁻² tại 1 MHz (và ~12 K ngay cả tại 40 kHz) — gia nhiệt trễ là *lý do* vách lót elastomer chết, không phải lược. HDPE ở giữa và nhớ điểm nóng chảy: +215 K mỗi W·cm⁻² tại 5 MHz.
- **Biên độ hẹp của bê tông là kéo, không nhiệt**: ứng suất sóng 0.40 MPa so với cường độ kéo tĩnh ~2.5 MPa (mỏi còn thấp hơn) chỉ để lại biên ~6× tại 1 W/cm². Chế độ 40–80 kHz vẫn ổn ở mật độ công suất của dự án; chùm tập trung đa-W/cm² vào bê tông nên tránh, MHz lại càng (tán xạ nóng các bề mặt tiếp xúc cốt liệu).
- **Kết luận cho lộ trình:** ở mật độ công suất chế độ A (≤0.3 W/cm²) không vật rắn nào trong bảng bị đe dọa — biên ứng suất ≥11× (hẹp nhất là mỏi kéo của bê tông ở 11×; mọi thứ khác ≥15×) và gia nhiệt ≤0.2 K cho mọi vật rắn kỹ thuật (cao su, ngoại lệ không ai nhắm tới, ~3.5 K). Bản đồ tổn thương biện minh cho kế hoạch tăng công suất của dự án: giới hạn vật liệu thực đầu tiên xuất hiện *trên* mục tiêu giai đoạn-2, đầu tiên trong chất lỏng (xâm thực, quy tắc ≤1 W/cm² của [00-theory](00-theory.md)), rồi trong mỏi kéo của bê tông, rồi trong polyme tại MHz. Các bộ phận thực sự cần theo dõi ở công suất cao vẫn là gốm piezo và đường dán — [02-safety](02-safety.md) — không phải vách.

## Phán quyết theo vật liệu

| Vách | Chế độ A — công suất 40 kHz | Chế độ B — công suất/dữ liệu MHz | Phán quyết |
|---|---|---|---|
| steel | ✓✓ tham chiếu | ✓ lược sắc — theo dõi tần số | đường cơ sở |
| aluminum | ✓✓ (proxy ~3× thép) | ✓ lược khá sắc | vách kết cấu tốt nhất (pin!) |
| titanium | ✓✓ | ✓ khá sắc, tổn thất thấp | ngách ăn mòn/nhiệt, drone, vỏ tàu |
| copper | ✓ (ghép khó nhất trong kim loại) | ✓ | ngách: thanh cái hàn kín/tế bào điện hóa |
| borosilicate glass | ✓✓ | ✓ lược rộng nhất — dễ chịu nhất | cửa sổ phòng thí nghiệm, viewport |
| alumina ceramic | ✓✓ | ✓ lược nhanh nhất (990 kHz @ 5 mm), tổn thất thấp | vách quy trình nóng/cách nhiệt |
| PMMA | ✓ băng rộng | ⚠ cấp mW ≤ ~0.5 MHz | bồn, vỏ bọc; không phải vách điện năng ở MHz |
| PVC / HDPE | ✓ vách mỏng | ✗ hấp thụ | vỏ bọc cấp thấp, nút dữ liệu nhẹ |
| concrete | ✓ 40–80 kHz (thực hành UPV) | ✗ tán xạ | móng, ống — chỉ chế độ A |
| rubber (filled) | ⚠ ngoại suy mô hình chưa kiểm chứng | ✗ | thực nghiệm là ngõ cụt — [04](04-hybrid-channels.md) |

Vách nhựa Z thấp có nhiều dư địa cho liên kết chế độ A *dung sai sai lệch* nhưng cung cấp ít dư địa công suất tuyệt đối trước hấp thụ khi vượt ~200 kHz; đo trước khi hứa bất cứ điều gì.

## Bê tông với thép đai — trường hợp đa lớp

Bê tông thực tế không bao giờ thuần: lưới thép nằm ở độ sâu bảo vệ, và mô hình tấm đơn 1D ở trên không thấy chúng. `chart_rebar` / `rebar_table` mở rộng mô hình cho các chồng tổng quát ([`stack_transmission`](../../../software/simulator/material_map.py), đệ quy đa lớp chính xác với hấp thụ từng lớp, được bảo vệ trong self-check). Hình học mô phỏng: vách kết cấu 150 mm, một lưới thép có độ dày tương đương phẳng Ø16 mm ở lớp phủ 40 mm; mô hình *phẳng* là trường hợp xấu nhất — một thanh thực chỉ che phần chùm mà nó cắt qua, nên coi đây là các vùng lõm bao, không phải dự đoán:

| Chồng (bê tông 150 mm) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| thuần 150 mm | 0.135 | 0.133 | 8.9e-09 |
| thép đai Ø16 @ 40 mm | 0.013 | 0.069 | 6.6e-09 |
| hai lưới Ø16 @ 40 mm | 0.003 | 0.001 | 5.1e-09 |

<img src="../../../docs/img/mat5-rebar.png" width="880">

Mô hình chồng cho biết:

- **Một lưới phẳng dưới chùm tốn ×10 tại đúng 40 kHz** (can thiệp dải chặn từ lớp thép), nhưng vùng lõm hẹp: tại 100 kHz cùng chồng đó chỉ mất ×2. Đọc thực tế cho ngách ống/tự hóa: *quét tần số quanh 40–120 kHz, không phải tần số cố định*, là thứ đưa liên kết chế độ A qua thép đai — và các vùng lõm dịch theo độ sâu lớp phủ, nên quét cũng lấy dấu hình học (cơ sở của ước tính độ sâu thép đai).
- **Lưới thứ hai (lưới mắt) gần như giết vách trong trường hợp xấu nhất này** (×45 xuống và phẳng dải rộng gần 40–100 kHz): thép đai dày trong đường truyền là chỉ báo "chọn chỗ khác trên tường" thành thật, không phải bài toán xử lý tín hiệu.
- **Chế độ B qua bê tông kết cấu đã chết có hoặc không có thép đai** (mức 1e-8 tại 1 MHz: 5 dB/cm × 15 cm). Thép đai không bao giờ vào câu chuyện ở MHz.
- Lưu ý, theo thứ tự quan trọng: giả thuyết lớp phẳng (trường hợp xấu nhất — thanh Ø16 che dưới một nửa tiết diện chùm 40–50 mm), giả định sóng song song trục thép đai, và truyền 1D (không nhiễu xạ quanh thanh). Thử nghiệm phần cứng đúng là giàn quét trên tấm thực: lập bản đồ T(x, y) tại 40/80/120 kHz trên lưới thép đai và khớp vị trí lõm của mô hình phẳng với bước lưới.

## Phần tiếp theo phần cứng nên đo gì

Trước khi tin bất kỳ tấm cụ thể nào: phương pháp hai độ dày theo vật liệu (hai tấm d và 2d ở cùng tiếp xúc) để trích α(f) và c thực — bộ dữ liệu đó thay thế mọi hàng của bảng trên. Các lượt thưởng tự nhiên trong giao thức hiện có: lặp lại quét thực nghiệm [001](../experiments/001-sweep-map-3mm-steel/README.md) trên tấm PMMA 5 mm, tấm borosilicate hoặc alumina 99%, và khối bê tông cấp đã biết; kỳ vọng đỉnh *thấp nhưng rộng hơn* cho nhựa, lược sắc cho gốm, và tiếp xúc nhạy nhiệt mọi nơi. Trong chạy công suất thực nghiệm [002](../experiments/002-watts-3mm-steel/README.md), gắn nhiệt kế IR (hoặc cặp nhiệt mịn) vào mặt xa của mỗi loại vách — ΔT đo được tại đầu vào đã biết là con số duy nhất kiểm chứng hoặc giết cột gia nhiệt của bảng liều lượng. Không có gì trong trang này được đo — đây là bản đồ của thứ cần đo đầu tiên.
