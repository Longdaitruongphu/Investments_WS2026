import sys

out_file = "/media/minh/DISK/Downloads/Investments_WS2026/MASTER_EXAM_PREPARATION_ULTIMATE_GUIDE.md"

sec4_5_6 = r"""
---

# PHẦN 4: TOÀN BỘ CÂU HỎI TRÊN LỚP (IN-CLASS QUESTIONS & PROOFS) TỪ LECTURE 01 ĐẾN LECTURE 07

---

## 4.1. LECTURE 01: MÔI TRƯỜNG ĐẦU TƯ & CÁC CÔNG CỤ TÀI CHÍNH

### Khung Lý Thuyết & Bản Chất Kinh Tế
1. **Tài sản Thực (Real Assets) vs Tài sản Tài chính (Financial Assets)**:
   - *Tài sản thực*: Đất đai, máy móc, nhà xưởng, công nghệ, con người. Trực tiếp tạo ra hàng hóa, dịch vụ và của cải ròng cho xã hội.
   - *Tài sản tài chính*: Cổ phiếu, trái phiếu, phái sinh, tiền gửi. Là quyền đòi pháp lý đối với dòng tiền sinh ra từ tài sản thực. Tổng giá trị tài sản tài chính trong toàn bộ nền kinh tế luôn triệt tiêu bằng 0 ($\sum \text{Assets} - \sum \text{Liabilities} = 0$).
2. **Thị trường Sơ cấp (Primary) vs Thứ cấp (Secondary)**:
   - *Sơ cấp*: Doanh nghiệp phát hành chứng khoán mới (IPO, phát hành thêm) $\implies$ **Doanh nghiệp nhận được vốn mới**.
   - *Thứ cấp*: Nhà đầu tư mua đi bán lại với nhau trên sàn $\implies$ **Doanh nghiệp KHÔNG nhận được đồng vốn nào**, nhưng thị trường thứ cấp cung cấp tính thanh khoản và chức năng định giá (Price Discovery).
3. **Quy trình Đầu tư**:
   - *Top-Down*: Phân bổ tài sản vĩ mô (Asset Allocation: Cổ phiếu %, Trái phiếu %, Tiền mặt %) trước $\implies$ Chọn mã cụ thể (Security Selection) sau.
   - *Bottom-Up*: Đi thẳng vào tìm kiếm cổ phiếu định giá rẻ/hấp dẫn, không quan tâm tỷ trọng vĩ mô.

---

## 4.2. LECTURE 02: ĐỊNH GIÁ TRÁI PHIẾU, LỢI SUẤT (YTM) & CẤU TRÚC KỲ HẠN

### Giải Chi Tiết Toàn Bộ In-Class Questions 2.1 – 2.5

#### Question 2.1: Lãi Suất Kỳ Hạn Ngụ Ý & Các Lý Thuyết Cấu Trúc Kỳ Hạn
- **Đề bài**: Lãi suất zero-coupon 1 năm là $s_1 = 4\%$, 2 năm là $s_2 = 5\%$ (ghép lãi hàng năm).
  - (a) Tính lãi suất kỳ hạn 1 năm cho năm thứ 2 ($f_{1,2}$)?
  - (b) Theo Giả thuyết Kỳ vọng thuần túy (PEH), lãi suất ngắn hạn kỳ vọng trong năm 2 là bao nhiêu?
  - (c) Theo Lý thuyết Ưu tiên Thanh khoản (LPT), lãi suất ngắn hạn kỳ vọng có thể giữ nguyên ở mức 4% không? Giải thích.
- **Lời giải chi tiết**:
  - (a) **Tính lãi suất kỳ hạn $f_{1,2}$**:
    $$(1 + s_2)^2 = (1 + s_1)^1 \times (1 + f_{1,2}) \implies (1.05)^2 = (1.04)(1 + f_{1,2})$$
    $$\mathbf{f_{1,2} = \frac{(1.05)^2}{1.04} - 1 = \frac{1.1025}{1.04} - 1 \approx 0.060096\ (6.01\%/\text{năm})}$$
  - (b) **Theo Giả thuyết Kỳ vọng Thuần túy (PEH)**:
    - PEH giả định nhà đầu tư trung lập rủi ro, không đòi hỏi phần bù thanh khoản ($LP_2 = 0$).
    - Do đó, lãi suất kỳ hạn là ước lượng không chệch của lãi suất ngắn hạn tương lai:
      $$\mathbf{E(r_2) = f_{1,2} \approx 6.01\%}$$
    - Thị trường kỳ vọng lãi suất ngắn hạn sẽ tăng từ 4% lên 6.01%.
  - (c) **Theo Lý thuyết Ưu tiên Thanh khoản (LPT)**:
    - LPT khẳng định nhà đầu tư ngại rủi ro luôn đòi hỏi phần bù thanh khoản dương ($LP_2 > 0$) để bù đắp rủi ro biến động giá của trái phiếu dài hạn:
      $$f_{1,2} = E(r_2) + LP_2$$
    - Nếu lãi suất ngắn hạn kỳ vọng giữ nguyên ở mức $E(r_2) = 4\%$, thì:
      $$LP_2 = f_{1,2} - E(r_2) = 6.01\% - 4.00\% = \mathbf{2.01\%}$$
    - Vì $LP_2 = 2.01\% > 0$ hoàn toàn hợp lý, đường cong lợi suất dốc lên ($s_2 = 5\% > s_1 = 4\%$) hoàn toàn có thể xảy ra ngay cả khi lãi suất ngắn hạn tương lai không hề tăng!

#### Question 2.2: Giá Sạch (Clean Price), Lãi Dồn Tích (Accrued Interest) & Giá Hóa Đơn (Dirty Price)
- **Đề bài**: Trái phiếu mệnh giá 1,000 USD, coupon 6% trả bán niên (mỗi kỳ 30 USD). Ngày trả coupon trước cách đây 60 ngày, kỳ tính lãi kéo dài 182 ngày. Giá sạch niêm yết là 985 USD. Tính Lãi dồn tích và Giá hóa đơn thực trả.
- **Lời giải chi tiết**:
  - Tỷ lệ thời gian dồn tích: $f = \frac{60}{182} \approx 0.329670$.
  - Lãi dồn tích (Accrued Interest):
    $$\mathbf{AI = \text{Coupon bán niên} \times \left(\frac{\text{Ngày đã trôi qua}}{\text{Tổng số ngày trong kỳ}}\right) = 30 \times \left(\frac{60}{182}\right) \approx \$9.89}$$
  - Giá hóa đơn (Dirty / Invoice Price):
    $$\mathbf{\text{Dirty Price} = \text{Clean Price} + AI = 985 + 9.89 = \$994.89}$$
  - *Bẫy thi*: Người mua trả cho người bán Dirty Price ($994.89$), nhưng khi đến ngày trả coupon tiếp theo, người mua sẽ nhận trọn vẹn 30 USD tiền coupon từ tổ chức phát hành.

#### Question 2.3: Định Giá Trái Phiếu Bằng Đường Cong Lãi Suất Giao Ngay (Spot Rate Curve)
- **Đề bài**: Đường cong lãi suất spot: $s_1 = 3.0\%, s_2 = 3.8\%, s_3 = 4.4\%$. Trái phiếu 3 năm mệnh giá 1,000 USD, coupon 5%/năm.
  - (a) Định giá trái phiếu theo đường cong giao ngay.
  - (b) Tính YTM của trái phiếu. Trái phiếu giao dịch ở mức Premium hay Discount?
- **Lời giải chi tiết**:
  - (a) **Định giá theo Spot Rate**:
    $$P = \frac{50}{1 + s_1} + \frac{50}{(1 + s_2)^2} + \frac{1,050}{(1 + s_3)^3} = \frac{50}{1.03} + \frac{50}{(1.038)^2} + \frac{1,050}{(1.044)^3}$$
    $$P = 48.5437 + 46.4055 + 922.8427 = \mathbf{\$1,017.79}$$
  - (b) **Tính YTM**:
    $$1,017.79 = \frac{50}{1 + y} + \frac{50}{(1 + y)^2} + \frac{1,050}{(1 + y)^3} \implies \mathbf{y \approx 4.35\%/\text{năm}}$$
    Vì $P = 1,017.79 > 1,000$ USD (Mệnh giá) và $YTM = 4.35\% < \text{Coupon} = 5.0\%$, trái phiếu giao dịch ở mức **THẶNG DƯ (Premium)**.

#### Question 2.4: Trái Phiếu Có Thể Thu Hồi (Callable Bond) & Độ Lồi Âm (Negative Convexity)
- **Đề bài**: So sánh đường cong giá - lợi suất giữa Straight Bond và Callable Bond có giá thu hồi $P_{\text{call}} = 1,050$ USD. Giải thích hiện tượng Negative Convexity.
- **Lời giải chi tiết**:
  - Trái phiếu có thể thu hồi là một gói tài sản:
    $$\mathbf{\text{Giá Callable Bond} = \text{Giá Straight Bond} - \text{Giá Call Option trên Trái phiếu}}$$
  - Khi lãi suất thị trường giảm sâu:
    - Giá Straight Bond tăng vọt lên cao do hiệu ứng chiết khấu dòng tiền.
    - Tuy nhiên, tổ chức phát hành sẽ kích hoạt quyền mua lại (Call option) để tái tài trợ nợ ở lãi suất thấp hơn. Do đó, giá Callable Bond bị **chặn trên tại giá thu hồi (Call Price)**.
  - *Hiện tượng Độ lồi âm (Negative Convexity)*:
    - Tại mức lãi suất thấp, đường cong giá của Callable Bond chuyển từ dạng lồi (convex) sang **dạng lõm (concave)**.
    - Khi lãi suất giảm, giá tăng rất chậm; nhưng khi lãi suất tăng, giá sụt giảm rất nhanh. Nhà đầu tư chịu bất đối xứng rủi ro bất lợi.

#### Question 2.5: Tỷ Suất Sinh Lời Kỳ Nắm Giữ (HPR) vs YTM
- **Đề bài**: Mua trái phiếu coupon 6% kỳ hạn 3 năm tại $YTM = 5\%$ ($P_0 = 1,027.23$ USD). Sau 1 năm, nhận coupon 60 USD và bán trái phiếu khi $YTM$ tăng lên 8%. Tính HPR 1 năm và so sánh với $YTM$ ban đầu.
- **Lời giải chi tiết**:
  - Sau 1 năm, trái phiếu còn 2 năm đáo hạn. Giá bán tại $YTM = 8\%$:
    $$P_1 = \frac{60}{1.08} + \frac{1,060}{(1.08)^2} = 55.5556 + 908.7791 = \mathbf{964.33\ \text{USD}}$$
  - Tỷ suất sinh lời kỳ nắm giữ (HPR):
    $$\mathbf{HPR = \frac{\text{Coupon} + P_1 - P_0}{P_0} = \frac{60 + 964.33 - 1,027.23}{1,027.23} = \frac{-2.90}{1,027.23} \approx -0.28\%}$$
  - *Kết luận*: Mua tại $YTM = 5\%$ **KHÔNG HỀ ĐẢM BẢO** lợi nhuận 5% nếu bán trước khi đáo hạn! Rủi ro biến động giá thị trường (Price Risk) khi lãi suất tăng có thể xóa sạch thu nhập coupon và gây ra HPR âm.

---

## 4.3. LECTURE 03: DURATION, CONVEXITY & MIỄN DỊCH RỦI RO LÃI SUẤT

### Giải Chi Tiết Toàn Bộ In-Class Questions 3.1 – 3.7

#### Question 3.1 & 3.2: Phân Biệt Macaulay Duration vs Modified Duration
- **Định nghĩa**:
  - **Macaulay Duration ($D$)**: Thời gian bình quân gia quyền mà nhà đầu tư thu hồi lại dòng tiền của trái phiếu, đo bằng **năm**:
    $$\mathbf{D = \sum_{t=1}^T t \times \left[\frac{CF_t / (1+y)^t}{P}\right]}$$
  - **Modified Duration ($D^*$)**: Thước đo độ nhạy cảm phần trăm của giá trái phiếu đối với sự thay đổi của lợi suất:
    $$\mathbf{D^* = \frac{D}{1 + y/m}} \qquad (m \text{ là số lần ghép lãi/năm})$$
    $$\mathbf{\frac{\Delta P}{P} \approx -D^* \times \Delta y}$$

#### Question 3.3: Duration Của Danh Mục & DV01
- **Đề bài**: Danh mục gồm 2 trái phiếu: Trái phiếu A (Giá trị 60,000 USD, $D_A^* = 3$ năm); Trái phiếu B (Giá trị 40,000 USD, $D_B^* = 8$ năm).
  - (a) Tính Duration danh mục.
  - (b) Tính DV01 (Dollar Value of 01) và ước lượng mức thay đổi giá trị danh mục khi lãi suất tăng 25 bps.
- **Lời giải chi tiết**:
  - Tổng giá trị $V = 60,000 + 40,000 = 100,000$ USD. Tỷ trọng: $w_A = 0.60, w_B = 0.40$.
  - (a) **Duration Danh Mục**:
    $$\mathbf{D_{\text{port}}^* = w_A D_A^* + w_B D_B^* = 0.60(3) + 0.40(8) = 1.8 + 3.2 = \mathbf{5.0\ \text{năm}}}$$
  - (b) **DV01 & Ước lượng Biến động Giá trị**:
    - Dollar Duration: $D_{\$} = D^* \times V = 5.0 \times 100,000 = 500,000$ USD.
    - DV01 (Giá trị đô-la khi lãi suất đổi 1 bp = 0.0001):
      $$\mathbf{DV01 = D_{\$} \times 0.0001 = 500,000 \times 0.0001 = \$50/\text{bp}}$$
    - Khi lãi suất tăng 25 bps ($\Delta y = +0.0025$):
      $$\mathbf{\Delta V \approx -DV01 \times 25 = -50 \times 25 = -\$1,250}$$
      (Tương đương phần trăm: $\frac{\Delta V}{V} \approx -5.0 \times 0.0025 = -1.25\%$).

#### Question 3.4: Quy Tắc Xấp Xỉ Bậc 2 (Duration + Convexity Rule)
- **Đề bài**: Trái phiếu giá $P_0 = 1,000$ USD, $D^* = 6.0$ năm, Độ lồi $C = 50\ \text{năm}^2$. Lãi suất giảm 150 bps ($\Delta y = -0.015$). Ước lượng giá mới dùng Duration và dùng Duration + Convexity.
- **Lời giải chi tiết**:
  - **Dùng Duration đơn thuần (Bậc 1)**:
    $$\frac{\Delta P}{P} \approx -D^* \times \Delta y = -6.0 \times (-0.015) = +0.0900\ (+9.00\%)$$
    $$P_{\text{new}} \approx 1,000 \times (1 + 0.09) = \mathbf{\$1,090.00}$$
  - **Dùng Duration + Convexity (Bậc 2)**:
    $$\frac{\Delta P}{P} \approx -D^* \Delta y + \frac{1}{2} C (\Delta y)^2$$
    $$\text{Đóng góp của Convexity} = \frac{1}{2} \times 50 \times (-0.015)^2 = 25 \times 0.000225 = +0.005625\ (+0.5625\%)$$
    $$\frac{\Delta P}{P} \approx +9.00\% + 0.5625\% = +9.5625\%$$
    $$\mathbf{P_{\text{new}} \approx 1,000 \times (1 + 0.095625) = \$1,095.63}$$
  - *Bản chất*: Convexity luôn mang dấu dương ($\frac{1}{2}C(\Delta y)^2 > 0$). Khi lãi suất giảm, Convexity giúp giá tăng mạnh hơn ước lượng của Duration; khi lãi suất tăng, Convexity giúp giá giảm ít hơn.

#### Question 3.6 & 3.7: Chiến Lược Miễn Dịch Danh Mục (Redington Immunization)
- **Đề bài**: Quỹ hưu trí có nghĩa vụ nợ phải trả sau 5 năm là 1,000,000 USD. Lãi suất thị trường phẳng ở mức $6\%$/năm ($EAR = 1.06$). Quỹ đầu tư vào Trái phiếu A (Zero 3 năm, $D_A = 3$) và Trái phiếu B (Zero 7 năm, $D_B = 7$).
  - (a) Xác định số tiền đầu tư vào Trái phiếu A và B để miễn dịch hoàn toàn nghĩa vụ nợ.
  - (b) Ngay sau đó, lãi suất tăng 50 bps lên 6.5%. Kiểm tra xem danh mục có còn đủ tiền trả nợ không? Tại sao vẫn phải tái cân bằng định kỳ?
- **Lời giải chi tiết**:
  - (a) **Điều kiện Miễn Dịch Redington**:
    1. Giá trị hiện tại Tài sản = Giá trị hiện tại Nợ ($PV(A) = PV(L)$):
       $$PV(L) = \frac{1,000,000}{(1.06)^5} \approx \mathbf{747,258.17\ \text{USD}}$$
    2. Duration Tài sản = Duration Nợ ($D_A w_A + D_B w_B = D_L = 5.0$ năm):
       $$3 w_A + 7 (1 - w_A) = 5 \implies 7 - 4 w_A = 5 \implies 4 w_A = 2 \implies \mathbf{w_A = 0.50, \quad w_B = 0.50}$$
    - Phân bổ số tiền:
      - Trái phiếu A: $0.50 \times 747,258.17 = \mathbf{\$373,629.09}$ (Mệnh giá $= 373,629.09 \times (1.06)^3 = 445,000$ USD).
      - Trái phiếu B: $0.50 \times 747,258.17 = \mathbf{\$373,629.09}$ (Mệnh giá $= 373,629.09 \times (1.06)^7 = 561,792$ USD).
  - (b) **Khi Lãi Suất Tăng Lên 6.5%**:
    - $PV_{\text{new}}(L) = \frac{1,000,000}{(1.065)^5} \approx 729,880.84$ USD.
    - $PV_{\text{new}}(A) = \frac{445,000}{(1.065)^3} + \frac{561,792}{(1.065)^7} = 368,397.64 + 361,501.91 = \mathbf{729,899.55\ \text{USD}}$.
    - **Thặng dư**: $PV(A) - PV(L) = 729,899.55 - 729,880.84 = \mathbf{+\$18.71 > 0}$!
    - *Vì sao phải tái cân bằng (Rebalancing)*:
      1. Thời gian trôi qua làm Duration của tài sản và nợ giảm với tốc độ khác nhau.
      2. Khi lãi suất biến động mạnh, Duration của từng trái phiếu cũng thay đổi. Muốn duy trì sự bảo vệ hoàn hảo, nhà quản lý phải tái cân bằng định kỳ để đưa $D_{\text{asset}} = D_{\text{liability}}$.

---

## 4.4. LECTURE 04: LỢI SUẤT, RỦI RO & PHÂN BỔ VỐN DANH MỤC

### Giải Chi Tiết Toàn Bộ In-Class Questions 1 – 5

#### Question 1: Bình Quân Số Học (Arithmetic) vs Bình Quân Hình Học (Geometric)
- **Đề bài**: Chuỗi lợi suất 3 năm: Năm 1: -20%, Năm 2: +25%, Năm 3: +10%. Tính Mean Arithmetic và Mean Geometric. Con số nào đo lường của cải thực tế?
- **Lời giải chi tiết**:
  - Bình quân số học (Arithmetic Mean):
    $$\mathbf{\bar{r}_{\text{arith}} = \frac{-20\% + 25\% + 10\%}{3} = \frac{15\%}{3} = +5.00\%/\text{năm}}$$
  - Bình quân hình học (Geometric Mean / Compound Return):
    $$(1 + g)^3 = (1 - 0.20)(1 + 0.25)(1 + 0.10) = (0.80)(1.25)(1.10) = 1.00 \times 1.10 = 1.10$$
    $$\mathbf{g = (1.10)^{1/3} - 1 \approx 1.03228 - 1 = +3.23\%/\text{năm}}$$
  - *Ý nghĩa*: Bình quân hình học ($3.23\%$) luôn nhỏ hơn bình quân số học ($5.00\%$) do hiện tượng **Volatility Drag (Sức cản biến động)**. Bình quân hình học là con số duy nhất tái hiện chính xác của cải thực tế tăng trưởng sau 3 năm ($12,000 \times 1.10 = 13,200$ USD).

#### Question 2: Phân Tích Lợi Suất Kỳ Vọng, Phương Sai & Độ Lệch Chuẩn
- **Công thức cốt lõi**:
  $$E(r) = \sum p_s r_s, \qquad \sigma^2 = \sum p_s [r_s - E(r)]^2, \qquad \sigma = \sqrt{\sigma^2}$$

#### Question 3: Tỷ Số Sharpe & Quy Tắc Hóa Năm (Annualization)
- Tỷ số Sharpe hàng tháng: $\text{SR}_m = \frac{\bar{R}_m}{\sigma_m}$.
- Hóa năm theo quy tắc BKM:
  $$\text{Mean annualized} = 12 \times \bar{R}_m, \qquad \sigma_{\text{annualized}} = \sqrt{12} \times \sigma_m$$
  $$\mathbf{\text{SR}_{\text{annualized}} = \frac{12 \bar{R}_m}{\sqrt{12} \sigma_m} = \sqrt{12} \times \text{SR}_m}$$

#### Question 4: Hàm Thỏa Dụng Bậc Hai (Mean-Variance Utility)
- **Công thức**:
  $$\mathbf{U = E(r) - \frac{1}{2} A \sigma^2}$$
  Trong đó: $A$ là hệ số ngại rủi ro (Risk-aversion coefficient). Lãi suất và phương sai bắt buộc dùng dạng số thập phân.
- Tỷ suất sinh lời chắc chắn tương đương (Certainty Equivalent Return):
  $$r_{\text{CE}} = U$$
  Là mức lãi suất phi rủi ro chắc chắn khiến nhà đầu tư cảm thấy thỏa mãn đúng bằng khi nắm giữ danh mục rủi ro.

#### Question 5: Đường Phân Bổ Vốn (CAL) & Lựa Chọn Tối Ưu
- Kết hợp tài sản rủi ro $P$ với tài sản phi rủi ro $r_f$:
  $$E(r_c) = r_f + y [E(r_p) - r_f], \qquad \sigma_c = y \sigma_p$$
- Phương trình CAL:
  $$\mathbf{E(r_c) = r_f + \left[\frac{E(r_p) - r_f}{\sigma_p}\right] \sigma_c}$$
- Tỷ trọng tối ưu vào tài sản rủi ro:
  $$\mathbf{y^* = \frac{E(r_p) - r_f}{A \sigma_p^2}}$$
  - Nếu $y^* < 1$: Nhà đầu tư cho vay một phần vốn tại $r_f$ (Lending).
  - Nếu $y^* > 1$: Nhà đầu tư đi vay nợ tại $r_f$ để đòn bẩy thêm vào tài sản rủi ro (Borrowing).

---

## 4.5. LECTURE 05: LỰA CHỌN DANH MỤC MARKOWITZ & ĐƯỜNG THỊ TRƯỜNG VỐN (CML)

### Giải Chi Tiết Toàn Bộ In-Class Questions 1 – 5

#### Question 1: Danh Mục 2 Tài Sản Rủi Ro & Danh Mục Phương Sai Tối Thiểu (MVP)
- Tỷ trọng của tài sản 1 trong MVP (Global Minimum Variance Portfolio):
  $$\mathbf{w_1^{\text{MVP}} = \frac{\sigma_2^2 - \text{Cov}(r_1, r_2)}{\sigma_1^2 + \sigma_2^2 - 2\text{Cov}(r_1, r_2)}}, \qquad w_2^{\text{MVP}} = 1 - w_1^{\text{MVP}}$$
- *Điều kiện đa dạng hóa hoàn hảo*: Khi hệ số tương quan $\rho = -1$, ta có thể triệt tiêu 100% rủi ro ($\sigma_{\text{port}} = 0$) bằng cách chọn:
  $$w_1 = \frac{\sigma_2}{\sigma_1 + \sigma_2}, \quad w_2 = \frac{\sigma_1}{\sigma_1 + \sigma_2}$$

#### Question 3: Danh Mục Tiếp Điểm (Tangency / Optimal Risky Portfolio)
- Với 2 tài sản rủi ro, tỷ trọng tối đa hóa tỷ số Sharpe:
  $$\mathbf{w_1^* = \frac{[E(r_1) - r_f]\sigma_2^2 - [E(r_2) - r_f]\text{Cov}(r_1, r_2)}{[E(r_1) - r_f]\sigma_2^2 + [E(r_2) - r_f]\sigma_1^2 - [E(r_1) - r_f + E(r_2) - r_f]\text{Cov}(r_1, r_2)}}$$

#### Question 5: Định Lý Phân Tách Hai Quỹ (Two-Fund Separation Theorem)
- **Nội dung định lý**: Quá trình tối ưu hóa danh mục đầu tư được tách rời thành **2 bước hoàn toàn độc lập**:
  1. *Bước 1 (Kỹ thuật - Khách quan)*: Xác định danh mục tài sản rủi ro tối ưu (Tangency Portfolio) bằng cách tìm tiếp điểm giữa tia xuất phát từ $r_f$ với đường biên hiệu quả Markowitz. Bước này **hoàn toàn không phụ thuộc vào mức độ ngại rủi ro $A$** của nhà đầu tư.
  2. *Bước 2 (Cá nhân hóa - Chủ quan)*: Mỗi nhà đầu tư dựa vào hệ số ngại rủi ro $A$ của mình để quyết định phân bổ bao nhiêu tiền vào Danh mục tiếp điểm và bao nhiêu tiền vào Tài sản phi rủi ro ($r_f$).

---

## 4.6. LECTURE 06: MÔ HÌNH CHỈ SỐ ĐƠN (SIM) & CAPM

### Giải Chi Tiết Toàn Bộ In-Class Questions 1 – 5

#### Question 1: Phân Rã Phương Sai OLS Của Single-Index Model
- Phương trình hồi quy chỉ số đơn: $R_i = \alpha_i + \beta_i R_M + e_i$.
- **Phân rã phương sai tổng thể**:
  $$\mathbf{\sigma_i^2 = \underbrace{\beta_i^2 \sigma_M^2}_{\text{Rủi ro Hệ thống (Systematic)}} + \underbrace{\sigma^2(e_i)}_{\text{Rủi ro Đặc thù / Phi hệ thống (Firm-specific)}}}$$
- Hệ số xác định $R^2$:
  $$R^2 = \frac{\text{Systematic Variance}}{\text{Total Variance}} = \frac{\beta_i^2 \sigma_M^2}{\sigma_i^2}$$
- Hiệp phương sai giữa 2 cổ phiếu trong SIM:
  $$\mathbf{\text{Cov}(r_i, r_j) = \beta_i \beta_j \sigma_M^2}$$

#### Question 2 & 3: Mô Hình CAPM, Đường SML & Alpha của Jensen
- Phương trình CAPM:
  $$\mathbf{E(r_i) = r_f + \beta_i [E(r_M) - r_f]}$$
- Trong đó: $\beta_i = \frac{\text{Cov}(r_i, r_M)}{\sigma_M^2}$.
- **Alpha của Jensen**: $\alpha_i = E(r_i) - E(r_i)_{\text{CAPM}}$.
  - $\alpha > 0$: Cổ phiếu nằm **phía trên đường SML** $\implies$ Định giá rẻ (Underpriced), nên Mua.
  - $\alpha < 0$: Cổ phiếu nằm **phía dưới đường SML** $\implies$ Định giá đắt (Overpriced), nên Bán.
  - $\alpha = 0$: Định giá đúng theo lý thuyết cân bằng thị trường.

#### Question 4: Kỹ Năng Đọc Bảng Hồi Quy OLS / Excel LINEST Đề Thi
| Thống kê | Ký hiệu | Công thức tính nhanh |
|---|---|---|
| Hệ số góc (Slope) | $\hat{\beta}$ | $\hat{\beta} = \frac{\text{Cov}(R_i, R_M)}{\text{Var}(R_M)}$ |
| Hệ số chặn (Intercept) | $\hat{\alpha}$ | $\hat{\alpha} = \bar{R}_i - \hat{\beta} \bar{R}_M$ |
| Bậc tự do hồi quy | $df$ | $df = N - 2$ |
| Phương sai phần dư | $s_e^2$ | $s_e^2 = \frac{SSE}{N - 2}$ |
| Thống kê t của Beta | $t_{\beta}$ | $t = \frac{\hat{\beta}}{SE(\hat{\beta})}$ (Bác bỏ giả thuyết $\beta=0$ khi $|t| > 2.0$) |

---

## 4.7. LECTURE 07: MÔ HÌNH ĐA NHÂN TỐ & LÝ THUYẾT ĐỊNH GIÁ CHÊNH LỆCH (APT)

### Giải Chi Tiết Toàn Bộ In-Class Questions 1 – 6

#### Question 1 & 2: Cơ Chế Kinh Doanh Chênh Lệch Giá Thuần Túy Trong APT (Pure Arbitrage)
- Để tạo ra một danh mục Arbitrage trong mô hình APT:
  1. **Không bỏ vốn ban đầu (Zero Investment)**: $\sum w_i = 0$.
  2. **Không chịu bất kỳ rủi ro nhân tố nào (Zero Factor Risk)**: $\sum w_i \beta_{i1} = 0, \sum w_i \beta_{i2} = 0$.
  3. **Lợi nhuận kỳ vọng dương chắc chắn**: $\sum w_i E(r_i) > 0$.

#### Question 3: Mô Hình Fama-French 3 Nhân Tố (FF3 Model)
- Phương trình định giá:
  $$\mathbf{E(R_i) = \alpha_i + \beta_{i,M} R_M + \beta_{i,SMB} SMB + \beta_{i,HML} HML}$$
  - $SMB$ (Small Minus Big): Phần bù rủi ro quy mô công ty.
  - $HML$ (High Minus Low): Phần bù rủi ro giá trị (Value vs Growth).
- **Hiện tượng Alpha Biến Mất (Disappearing Alpha)**: Rất nhiều nhà quản lý quỹ khoe có $\alpha_{\text{CAPM}} > 0$. Nhưng khi đưa vào mô hình FF3, hóa ra quỹ đó chỉ đơn giản là mua nhiều cổ phiếu vốn hóa nhỏ ($SMB > 0$) hoặc cổ phiếu giá trị ($HML > 0$). Alpha thực sự sau khi kiểm soát các nhân tố rủi ro này tụt về 0!

---

# PHẦN 5: BẢN ĐỒ CHIẾN THUẬT & TÓM TẮT 100 CÂU THỰC HÀNH LECTURES 01 – 07

Toàn bộ 100 câu hỏi bài tập thực hành Lectures 01 đến 07 đã được giải chi tiết 100% trong cẩm nang `MASTER_PRACTICE_Q01_Q100_SOLUTIONS.md`. Dưới đây là ma trận phân loại dạng bài, công thức giải siêu tốc trong 30 giây và các câu bẫy hay thi nhất:

| Khối Bài Tập | Câu Hỏi | Trọng Tâm Thi Cử | Công Thức Bấm Máy 30 Giây | Câu Hay Bẫy Nhất Cần Ôn Kỹ |
|---|---|---|---|---|
| **L01: Instruments** | Q01 – Q08 | Real vs Financial, Repo rate, Call/Put profit table | $r_{\text{repo}} = \frac{\Delta \text{Price}}{\text{Sale Price}} \times \frac{360}{\text{Days}}$ | **Q08**: Danh mục Call + Cash đòn bẩy |
| **L02: Bonds I** | Q09 – Q24 | Định giá bond, Clean/Dirty, Spot curve, Implied Forward | $(1+s_t)^t = (1+s_{t-1})^{t-1}(1+f_{t-1,t})$ | **Q15**: Callable YTC vs YTM; **Q24**: HPR phân phối xác suất |
| **L03: Bonds II** | Q25 – Q38 | Duration, Convexity xấp xỉ, Immunization | $\Delta P / P \approx -D^* \Delta y + \frac{1}{2} C (\Delta y)^2$ | **Q32**: So sánh sai số; **Q38**: Miễn dịch danh mục 2 trái phiếu |
| **L04: Returns & Risk** | Q39 – Q56 | Geometric mean, Mean-Variance Utility, CAL | $U = E(r) - \frac{1}{2} A \sigma^2; y^* = \frac{E(r_p)-r_f}{A\sigma_p^2}$ | **Q50**: Certainty equivalent; **Q55**: Protective put distribution |
| **L05: Portfolios** | Q57 – Q71 | 2-asset MVP, Tangency portfolio, Two-fund separation | $w_1^{\text{MVP}} = \frac{\sigma_2^2 - \text{Cov}}{\sigma_1^2 + \sigma_2^2 - 2\text{Cov}}$ | **Q64**: Tangency weights; **Q70**: Ràng buộc cấm bán khống |
| **L06: SIM & CAPM** | Q72 – Q86 | Phân rã OLS, CAPM required return, SML vs CML | $\sigma_i^2 = \beta_i^2 \sigma_M^2 + \sigma_e^2; \alpha = E(r) - [r_f + \beta(E(r_M)-r_f)]$ | **Q80**: Phục hồi OLS table; **Q86**: Danh mục tối ưu theo SIM |
| **L07: APT & FF3** | Q87 – Q100 | APT Arbitrage, Factor loadings, FF3 Alpha | $r_B = r_f + \beta_M R_M + \beta_{SMB} SMB + \beta_{HML} HML$ | **Q92**: Sửa sai danh mục Arbitrage; **Q100**: CAPM vs FF3 Alpha |

---

# PHẦN 6: DERIVATIVES MASTER CHEAT-SHEET ($\ge 40\%$ ĐIỂM SỐ BÀI THI)

### 1. Bảng Tổng Hợp Công Thức Phái Sinh Bắt Buộc Mang Vào Phòng Thi

| Nhóm Công Cụ | Đại Lượng | Công Thức Chuẩn | Ghi Chú Cốt Tử |
|---|---|---|---|
| **Forward / Futures** | Tài sản không cổ tức | $F_0 = S_0 (1+r)^T = S_0 e^{rT}$ | Lãi suất năm vs liên tục |
| | Cổ tức tiền mặt $D$ | $F_0 = (S_0 - PV(D)) e^{rT}$ | Trừ $PV(D)$ trước khi nhân $e^{rT}$ |
| | Tỷ suất cổ tức liên tục $q$ | $F_0 = S_0 e^{(r - q)T}$ | Áp dụng cho Chỉ số chứng khoán |
| | Tỷ giá hối đoái (CIP) | $F_0 = S_0 e^{(r_{\text{base}} - r_{\text{quote}})T}$ | Tỷ giá tính theo Ngoại tệ/Nội tệ |
| | Hàng hóa có chi phí lưu kho $U$ & Convenience Yield $y$ | $F_0 = S_0 e^{(r + u - y)T}$ | $y > r+u \implies$ Backwardation |
| **Swaps** | Giá trị Net Settlement | $\text{Net} = \text{Notional} \times (L - K) \times \Delta t$ | Pay-Fixed nhận tiền khi $L > K$ |
| | Tỷ giá Swap tiền tệ | $S_{\text{swap}} = \text{Tỷ giá giao ngay tại } t=0$ | Hoán đổi gốc tại đầu và cuối kỳ |
| **Quyền Chọn Cơ Bản** | Put-Call Parity (Châu Âu) | $\mathbf{C + PV(K) = S_0 + P}$ | $PV(K) = K e^{-rT}$ hoặc $K / (1+r)^T$ |
| | Vị thế nhân tạo Synthetic Call | $C = S_0 + P - PV(K)$ | Mua Cổ phiếu + Mua Put + Vay nợ |
| | Vị thế nhân tạo Synthetic Put | $P = C + PV(K) - S_0$ | Mua Call + Gửi tiết kiệm + Bán khống Cổ phiếu |
| **Cây Nhị Thức** | Xác suất trung lập rủi ro | $\mathbf{p = \frac{R - d}{u - d}}$ | $R = 1+r$ hoặc $e^{r\Delta t}$ |
| | Định giá lùi từng bước | $V_0 = \frac{p V_u + (1-p) V_d}{R}$ | Luôn lùi từ phải qua trái |
| | Số cổ phiếu sao chép $\Delta$ | $\mathbf{\Delta = \frac{f_u - f_d}{S_u - S_d}}$ | Bằng 0 với OTM, bằng 1 với Deep ITM |
| | Giá trạng thái Arrow-Debreu | $P_u = \frac{R-d}{R(u-d)}, P_d = \frac{u-R}{R(u-d)}$ | Kiểm tra $P_u + P_d = 1/R$ |
| **Black-Scholes** | Giá Call & Put | $C = S N(d_1) - PV(K) N(d_2)$ | $P = PV(K) N(-d_2) - S N(-d_1)$ |
| | Thông số $d_1, d_2$ | $d_1 = \frac{\ln(S/PV(K))}{\sigma \sqrt{T}} + \frac{\sigma \sqrt{T}}{2}$ | $d_2 = d_1 - \sigma \sqrt{T}$ |
| | Delta của Call và Put | $\Delta_{\text{call}} = N(d_1) \in (0, 1)$ | $\Delta_{\text{put}} = N(d_1) - 1 \in (-1, 0)$ |
| | Beta của Quyền chọn | $\mathbf{\beta_{\text{opt}} = \left(\frac{S_0 \Delta}{V_{\text{opt}}}\right) \beta_S}$ | Call có Beta dương lớn; Put có Beta âm |

---

### 2. Mười Quy Tắc Vàng Khi Làm Bài Thi Phái Sinh
1. **Kiểm tra loại ghép lãi ngay từ dòng đầu tiên**: Nhìn kỹ đề cho lãi suất liên tục ($e^{rT}$) hay lãi suất hiệu dụng năm ($(1+r)^T$) hay lãi suất danh nghĩa gộp theo quý/bán niên ($1 + r/m$).
2. **Không bao giờ dùng Put-Call Parity cho quyền chọn Mỹ**: Put-Call Parity dạng đẳng thức $C - P = S_0 - PV(K)$ chỉ đúng cho quyền chọn châu Âu. Với quyền chọn Mỹ, nó là bất đẳng thức do có giá trị thực thi sớm.
3. **Khi lập bảng Arbitrage**: Luôn thiết lập sao cho dòng tiền tại $t=0$ triệt tiêu bằng 0. Dòng tiền tại đáo hạn phải $\ge 0$ ở mọi trạng thái và có ít nhất 1 trạng thái $> 0$.
4. **Cây nhị thức cộng tính (Additive Tree)**: Tuyệt đối không lấy xác suất tại nút gốc áp dụng cho các nút con; phải tính lại $u_t, d_t, p_t$ tại từng nút!
5. **Thực thi sớm American Call**: Không bao giờ tối ưu nếu cổ phiếu không có cổ tức. Chỉ xem xét thực thi ngay trước ngày giao dịch không hưởng quyền cổ tức (Ex-dividend date) nếu cổ tức lớn hơn phần lãi chiết khấu bị mất do nộp tiền thực thi sớm ($D > K(1 - e^{-r\Delta t})$).

"""

with open(out_file, "a", encoding="utf-8") as f:
    f.write(sec4_5_6)

print("Appended Sections 4, 5, and 6 successfully!")
