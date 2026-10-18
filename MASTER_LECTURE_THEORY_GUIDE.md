# BFIN INVESTMENTS (WS2026): CẨM NANG TOÀN DIỆN LÝ THUYẾT & BÍ KÍP GIẢI TOÁN
## MASTER LECTURE THEORY & SPEED-RUN EXAM GUIDE (LECTURES 01 – 07)
**Phương pháp giảng dạy Feynman: Siêu trực quan, Dễ hiểu như kể chuyện cho một đứa trẻ, Cô đọng, Đầy đủ 100% kiến thức thi cử**  
*Trọng tâm đặc biệt: Định giá & Miễn nhiễm Trái phiếu (Bonds) + Mô hình Hồi quy OLS & Định giá Tài sản (OLS Regression & Asset Pricing)*

---

## MỤC LỤC CHIẾN LƯỢC (STRATEGIC TABLE OF CONTENTS)
1. [Triết lý Học Nhanh & Bản đồ Tư duy Ôn thi (Mindset & Exam Roadmap)](#triet-ly-hoc-nhanh--ban-do-tu-duy-on-thi)
2. [Lecture 01: Môi trường Đầu tư & Công cụ Tài chính (Investment Environment & Instruments)](#lecture-01-moi-truong-dau-tu--cac-cong-cu-tai-chinh)
3. [Lecture 02: TRỌNG TÂM BOND I - Định giá Trái phiếu & Cấu trúc Kỳ hạn Lãi suất (Bond Pricing & Term Structure)](#lecture-02-trong-tam-bond-i---dinh-gia-trai-phieu--cau-truc-ky-han-lai-suat)
4. [Lecture 03: TRỌNG TÂM BOND II - Duration, Convexity & Miễn nhiễm Rủi ro (Duration, Convexity & Immunization)](#lecture-03-trong-tam-bond-ii---duration-convexity--chien-luoc-mien-nhiem-rui-ro)
5. [Lecture 04: Lợi suất, Rủi ro & Phân bổ Vốn Danh mục (Returns, Risk, Utility & CAL)](#lecture-04-loi-suat-rui-ro--phan-bo-von-danh-muc)
6. [Lecture 05: Lựa chọn Danh mục Đầu tư, Markowitz Frontier & CML (Portfolio Theory, MVP & CML)](#lecture-05-lua-chon-danh-muc-dau-tu-markowitz-frontier--cml)
7. [Lecture 06: TRỌNG TÂM OLS I - Mô hình Chỉ số Đơn (SIM), CAPM & Bản chất Hồi quy OLS](#lecture-06-trong-tam-ols-i---mo-hinh-chi-so-don-sim-capm--hoi-quy-ols)
8. [Lecture 07: TRỌNG TÂM OLS II - Mô hình Đa nhân tố, Lý thuyết APT & Fama-French 3 Nhân tố](#lecture-07-trong-tam-ols-ii---mo-hinh-da-nhan-to-apt--fama-french-3-nhan-to)
9. [Chuyên đề Đặc biệt: "Bắt bài" Đọc Bảng Kết quả Hồi quy OLS / Excel LINEST trong Đề thi](#chuyen-de-dac-biet-bat-bai-doc-bang-hoi-quy-ols--excel-linest-trong-de-thi)
10. [Cẩm nang Bấm máy Siêu tốc & 10 Lỗi sai Chết người khi Làm bài tập (Speed-Run Playbook & Fatal Pitfalls)](#cam-nang-bam-may-sieu-toc--10-loi-sai-chet-nguoi-khi-lam-bai-tap)

---

# TRIẾT LÝ HỌC NHANH & BẢN ĐỒ TƯ DUY ÔN THI
Môn Đầu tư tài chính (Investments) thoạt nhìn có vẻ ngập tràn công thức toán học và ký hiệu Hy Lạp ($\alpha, \beta, \sigma, \rho, \lambda, \Delta$). Nhưng thực chất, toàn bộ môn học chỉ xoay quanh **3 câu hỏi lớn của cuộc đời đầu tư**:
1. **Một dòng tiền trong tương lai hôm nay đáng giá bao nhiêu?** $\implies$ *Định giá Trái phiếu & Lợi suất (Lectures 02, 03).*
2. **Nếu muốn sinh lời cao hơn, tôi phải trả giá bằng bao nhiêu rủi ro và phân bổ tiền thế nào?** $\implies$ *Lý thuyết Danh mục Đầu tư Markowitz & Phân bổ Vốn (Lectures 04, 05).*
3. **Thị trường định giá rủi ro như thế nào, và làm sao biết một cổ phiếu hay một nhà quản lý quỹ thực sự giỏi hay chỉ là kẻ ăn may?** $\implies$ *Hồi quy OLS, Mô hình CAPM, APT & Fama-French (Lectures 06, 07).*

Khi bạn nắm được "bản chất câu chuyện" (intuition), công thức toán học sẽ tự khắc xuất hiện trong đầu một cách tự nhiên mà không cần học vẹt!

---

# LECTURE 01: Môi trường Đầu tư & Các Công cụ Tài chính
*(Investment Environment and Financial Instruments)*

### 1. Giải thích cho một đứa trẻ: "Tài sản Thực" vs. "Tài sản Tài chính"
- **Tài sản Thực (Real Assets)**: Hãy tưởng tượng bạn nuôi một **con bò sữa**, xây một **cái chuồng trại**, và mua một **cỗ máy vắt sữa**. Đây là những thứ có thể sờ, nắm được, trực tiếp tạo ra sữa (của cải thực tế) cho xã hội.
  - *Ví dụ*: Nhà xưởng, đất đai, máy móc, bằng sáng chế công nghệ, kỹ năng lao động của con người.
- **Tài sản Tài chính (Financial Assets)**: Bây giờ, bạn không đủ tiền mua cả con bò, nên 10 người góp tiền cùng mua và in ra 10 **tờ giấy chứng nhận cổ phần** (Cổ phiếu), hoặc một tờ giấy cam kết "Vay bạn 100k, mỗi tháng trả 5k tiền lãi" (Trái phiếu).
  - Tờ giấy đó không tự vắt ra sữa! Nó chỉ là **chứng từ xác lập ai được hưởng bao nhiêu sữa từ con bò**.
  - **Nguyên lý Bù trừ Toàn xã hội (Zero-Sum Identity)**: Nếu gộp toàn bộ nền kinh tế lại, tờ giấy nợ là tài sản của bạn nhưng lại là khoản nợ của người nuôi bò. Chúng cộng lại triệt tiêu bằng 0! **Tổng của cải ròng thực sự của cả xã hội chỉ bằng đúng tổng giá trị của các Tài sản Thực!**

### 2. Chợ Đầu Mối (Sơ cấp) vs. Chợ Trao Tay (Thứ cấp)
- **Thị trường Sơ cấp (Primary Market)**: Công ty bán cổ phiếu/trái phiếu mới toanh cho bạn để lấy tiền xây nhà xưởng mới. **Công ty thực sự nhận được tiền vốn mới (New Capital).**
- **Thị trường Thứ cấp (Secondary Market)**: Tuần sau, bạn kẹt tiền nên bán lại tờ cổ phiếu đó cho bạn hàng xóm trên sàn giao dịch (như sàn HoSE, NYSE). Công ty phát hành **không nhận được thêm một xu nào cả**! Thị trường này chỉ giúp bạn có thanh khoản (muốn rút tiền lúc nào cũng được) và giúp định giá công ty minh bạch hàng ngày.

### 3. Phân biệt Cổ phiếu, Trái phiếu, Ưu đãi & Phái sinh
- **Bonds (Trái phiếu - Nợ)**: Bạn là chủ nợ. Công ty bắt buộc phải trả lãi coupon đúng hạn. Nếu quỵt nợ, công ty bị kiện phá sản ngay lập tức. Khi phá sản, chủ nợ được đền bù đầu tiên.
- **Common Stock (Cổ phiếu thường - Vốn chủ)**: Bạn là chủ sở hữu. Bạn có quyền biểu quyết nhưng hưởng quyền đòi sau cùng (Residual Claim). Công ty làm ăn có lãi mới chia cổ tức, lỗ thì nhịn. Trách nhiệm hữu hạn (Limited Liability): Bạn chỉ mất tối đa số tiền đã bỏ ra mua cổ phiếu, không ai được siết nhà riêng của bạn.
- **Preferred Stock (Cổ phiếu ưu đãi)**: Con lai giữa nợ và vốn. Được nhận cổ tức cố định như trái phiếu, được ưu tiên trả trước cổ đông thường nhưng xếp sau trái chủ. **Điểm thi then chốt**: Nếu công ty không trả cổ tức ưu đãi, công ty **KHÔNG bị tuyên bố phá sản** (khác hoàn toàn với trái phiếu!).
- **Options (Quyền chọn)**:
  - *Call Option (Quyền chọn mua)*: Vé mua đồ giảm giá. Cho bạn quyền (không ép buộc) được mua ở giá $X$. Nếu giá thị trường lên cao, bạn lãi: $\text{Payoff} = \max(0, S_T - X)$.
  - *Put Option (Quyền chọn bán)*: Hợp đồng bảo hiểm. Cho bạn quyền được bán ở giá $X$ khi thị trường sụp đổ: $\text{Payoff} = \max(0, X - S_T)$.
- **Futures / Forward (Hợp đồng tương lai / Kỳ hạn)**: Không phải là quyền chọn! Cả hai bên bị **bắt buộc** phải giao dịch ở giá $F$. Được ăn cả, ngã về không (Lãi của người này là lỗ của người kia).

### 4. Bẫy thi thường gặp ở Lecture 01
> [!WARNING]
> **Bẫy thi 1**: Đề bài hỏi: *"Giao dịch bán trái phiếu đã phát hành giữa 2 nhà đầu tư tư nhân có tạo ra nguồn vốn tài trợ mới cho doanh nghiệp phát hành không?"*  
> $\implies$ **Câu trả lời**: **KHÔNG**. Đó là giao dịch thứ cấp (Secondary), công ty không nhận thêm dòng tiền nào.  
> **Bẫy thi 2**: Chỉ số giá (Price-weighted index như Dow Jones) bị ảnh hưởng nặng khi cổ phiếu thị giá cao chia tách cổ phiếu (stock split), phải tính lại mẫu số Divisor. Trong khi chỉ số vốn hóa (Market-cap weighted như S&P 500) tự động triệt tiêu tác động của chia tách.

---

# LECTURE 02: TRỌNG TÂM BOND I - Định giá Trái phiếu & Cấu trúc Kỳ hạn Lãi suất
*(Bond Prices, Yields, and the Term Structure of Interest Rates)*

### 1. Giải thích cho một đứa trẻ: "Trò chơi Bập Bênh" giữa Giá và Lãi suất
Hãy tưởng tượng **Giá trái phiếu** và **Lãi suất thị trường (Yield)** ngồi ở 2 đầu của một chiếc bập bênh:
- Năm ngoái, bạn mua một trái phiếu cam kết trả lãi $10\%$/năm (rất hấp dẫn).
- Năm nay, ngân hàng tăng lãi suất tiết kiệm lên $12\%$/năm.
- Bây giờ, không ai muốn mua lại trái phiếu $10\%$ của bạn với giá gốc nữa, vì gửi ngân hàng được $12\%$ ngon hơn! Để bán được nó, bạn bắt buộc phải hạ giá xuống (bán rẻ, bán chiết khấu).
- $\implies$ **Lãi suất thị trường TĂNG thì Giá trái phiếu GIẢM. Lãi suất thị trường GIẢM thì Giá trái phiếu TĂNG.** Đó là quy luật bất biến!

```
      Lãi suất TĂNG (Yield UP) ▲
              \
               \   (BẬP BÊNH)
                \
                 ▼ Giá GIẢM (Price DOWN)
```

### 2. Các Công thức Định giá Bắt buộc Thuộc Lòng
#### A. Định giá Trái phiếu Hàng năm (Annual Compounding)
$$P = \sum_{t=1}^n \frac{C}{(1+y)^t} + \frac{M}{(1+y)^n} = C \left[ \frac{1 - (1+y)^{-n}}{y} \right] + \frac{M}{(1+y)^n}$$
- $M$: Mệnh giá (Face Value, thường là 1,000 USD hoặc 100 USD).
- $C$: Khoản coupon trả hàng năm ($C = c \times M$, với $c$ là coupon rate).
- $y$: Lợi suất đáo hạn (Yield to Maturity - YTM).
- $n$: Số năm còn lại đến ngày đáo hạn.

#### B. Trái phiếu Bán niên (Semiannual Compounding) - QUY TẮC "3 BƯỚC CƯA ĐÔI VÀ NHÂN ĐÔI"
Nếu đề bài có từ khóa **"semiannual"** (trả lãi nửa năm một lần):
1. **Coupon mỗi kỳ**: $C_{\text{period}} = \frac{C}{2} = \frac{c \times M}{2}$ (Cưa đôi).
2. **Lợi suất mỗi kỳ**: $r = \frac{y_{\text{nom}}}{2}$ (Cưa đôi).
3. **Số kỳ chiết khấu**: $n = 2 \times T$ (Nhân đôi số năm).
$$P = \frac{C}{2} \left[ \frac{1 - (1 + r)^{-2T}}{r} \right] + \frac{M}{(1 + r)^{-2T}}$$
- **Lợi suất Hiệu dụng Hàng năm (Effective Annual Yield - EAY / EAR)**:
  $$EAY = (1 + r)^2 - 1 = \left(1 + \frac{y_{\text{nom}}}{2}\right)^2 - 1$$
  *Luôn nhớ*: Do được ghép lãi kép nửa năm, $EAY > y_{\text{nom}}$!

#### C. Lãi Dồn tích (Accrued Interest) & Giá Hóa đơn (Dirty Price)
$$\text{Accrued Interest } (AI) = \frac{\text{Số ngày đã trôi qua kể từ coupon trước}}{\text{Tổng số ngày trong một kỳ coupon}} \times \text{Coupon của kỳ đó}$$
$$\text{Dirty Price (Invoice Price)} = \text{Clean Price} + AI$$

### 3. Spot Rates (Lãi suất Giao ngay) & Forward Rates (Lãi suất Kỳ hạn)
- **Spot Rate ($s_t$)**: Lãi suất từ hôm nay (năm 0) gửi liên tục một mạch đến năm $t$.
  - Định giá chuẩn xác nhất không dùng 1 YTM cào bằng, mà mỗi kỳ chiết khấu bằng $s_t$:
    $$P = \frac{C_1}{1+s_1} + \frac{C_2}{(1+s_2)^2} + \cdots + \frac{C_T + M}{(1+s_T)^T}$$
- **Forward Rate ($f_{t-1, t}$)**: Lãi suất vay mượn 1 năm trong tương lai, từ năm $t-1$ đến năm $t$.
  - **Nguyên lý không có kinh doanh chênh lệch giá (No-Arbitrage)**: Gửi tiền 2 năm một mạch ($s_2$) phải có kết quả sinh lời đúng bằng gửi năm 1 ($s_1$) rồi tái đầu tư tiếp năm 2 ($f_{1,2}$):
    $$(1 + s_t)^t = (1 + s_{t-1})^{t-1} \times (1 + f_{t-1, t})$$
  - **RÚT RA CÔNG THỨC TÍNH NHANH FORWARD RATE 1 NĂM**:
    $$f_{t-1, t} = \frac{(1 + s_t)^t}{(1 + s_{t-1})^{t-1}} - 1$$
    *Ví dụ*: Cho $s_1 = 4\%$, $s_2 = 5\%$. Tính $f_{1,2}$?
    $$f_{1,2} = \frac{(1.05)^2}{1.04} - 1 = \frac{1.1025}{1.04} - 1 = 6.01\%$$

### 4. Ba Lý thuyết Cấu trúc Kỳ hạn Lãi suất
1. **Pure Expectations Hypothesis (Lý thuyết Kỳ vọng Thuần túy - PEH)**:
   - Cho rằng $f_{t-1, t} = E(s_t)$. Không có phần bù rủi ro kỳ hạn nào cả. Nếu đường cong dốc lên ($s_1 < s_2$), chắc chắn thị trường kỳ vọng lãi suất tương lai sẽ tăng.
2. **Liquidity Preference Theory (Lý thuyết Ưu tiên Thanh khoản - LPT)**:
   - Nhà đầu tư ghét bị chôn vốn lâu vì sợ rủi ro lãi suất, nên muốn họ mua trái phiếu dài hạn, bạn phải trả thêm **Phần bù thanh khoản dương ($LP > 0$)**:
     $$f_{t-1, t} = E(s_t) + LP_t \quad (LP_t > 0)$$
   - **Hệ quả vàng trong thi cử**: Ngay cả khi ai cũng nghĩ lãi suất tương lai **đứng yên không đổi** ($E(s_t) = s_{t-1}$), đường cong lãi suất vẫn **tự động dốc lên** vì cộng thêm $LP$!
3. **Market Segmentation (Thị trường Phân đoạn)**: Cung cầu ngắn hạn quyết định lãi suất ngắn hạn; cung cầu dài hạn quyết định lãi suất dài hạn; không ai nhảy qua lại.

### 5. Chiến lược Tính toán Siêu tốc & Lỗi sai Thường gặp ở Lecture 02
> [!TIP]
> **CHIẾN LƯỢC BẤM MÁY TÍNH NHANH ĐỊNH GIÁ TRÁI PHIẾU (Casio 580 / Tài chính BA II Plus):**  
> - Với Casio: Nhập trực tiếp biểu thức: `C * (1 - (1+y)^(-n)) / y + M * (1+y)^(-n)`.  
> - Nếu là bán niên: Thay ngay $C \rightarrow C/2$, $y \rightarrow y/2$, $n \rightarrow 2n$. Đừng tính lẻ từng năm rồi cộng lại, mất 5 phút và dễ làm tròn sai!

> [!WARNING]
> **LỖI SAI CHẾT NGƯỜI 1**: Đề bài cho "Face value 5,000, 3 years zero coupon yields 4%". Sinh viên bấm nhầm thành có coupon! Zero coupon nghĩa là $C = 0$, công thức chỉ vỏn vẹn: $P = \frac{5000}{(1.04)^3} = 4,444.98$ USD.  
> **LỖI SAI CHẾT NGƯỜI 2**: Quên nhân đôi số kỳ $n$ khi đề bài cho "semiannual". Trái phiếu 10 năm bán niên thì $n = 20$ kỳ, không phải 10 kỳ!

---

# LECTURE 03: TRỌNG TÂM BOND II - Duration, Convexity & Chiến lược Miễn nhiễm Rủi ro
*(Duration, Convexity, and Immunization)*

### 1. Giải thích cho một đứa trẻ: "Duration" và "Convexity" là gì?
- **Duration (Thời lượng) - "Trọng tâm đòn bẩy của dòng tiền"**:
  - Bạn có một thanh gỗ dài 10 mét. Đầu mút năm thứ 10 có một bao tiền to (Mệnh giá 1,000 USD). Rải rác các năm 1, 2, 3... có những đồng tiền xu nhỏ (tiền coupon).
  - Điểm mà bạn có thể đặt ngón tay vào để thanh gỗ thăng bằng chính là **Duration**!
  - Trái phiếu Zero-coupon không có tiền xu ở giữa, toàn bộ bao tiền nằm ở năm thứ 10 $\implies$ Duration đúng bằng 10 năm.
  - Trái phiếu có coupon trả sớm kéo trọng tâm về gần bạn hơn $\implies$ **Duration luôn nhỏ hơn thời gian đáo hạn ($D < T$)**!
  - **Ý nghĩa thực chiến**: Duration đo độ nhạy cảm của giá trái phiếu trước cú sốc lãi suất. Duration càng dài, chiếc bập bênh càng nhạy, giá biến động càng dữ dội!

```
Trọng tâm đòn bẩy dòng tiền (Duration D < T)
       ▲ (Coupon 1)    ▲ (Coupon 2)               ████ (Mệnh giá + Coupon cuối)
───────┼───────────────┼──────────────────────────┼────────
Năm:   1               2                         T (Đáo hạn)
               ▲
               │ Đặt ngón tay thăng bằng tại đây (Duration)
```

- **Convexity (Độ lồi) - "Tấm đệm lò xo an toàn"**:
  - Quan hệ giữa Giá và Lãi suất không phải là một đường thẳng tắp, mà là một **chiếc bát cong lồi lên**.
  - Nếu bạn dùng Duration để ước tính giá, bạn đang dùng một **cây thước kẻ thẳng** áp vào đáy chiếc bát cong.
  - Vì chiếc bát cong lồi lên trên cây thước kẻ:
    - Khi lãi suất GIẢM: Giá thực tế **bắn vọt lên cao hơn** cây thước kẻ dự đoán!
    - Khi lãi suất TĂNG: Giá thực tế **chỉ rơi xuống một chút**, chiếc bát đỡ lại nên giá giảm **ít hơn** cây thước kẻ dự đoán!
  - $\implies$ **Độ lồi (Convexity) luôn là người bạn tốt nhất của nhà đầu tư! Nó giúp ăn nhiều hơn khi thị trường tốt và lỗ ít hơn khi thị trường xấu.**

```
        Giá Trái phiếu (P)
          ▲           / (Đường cong thực tế - Lồi)
          │          /  .
          │         /  . 
          │        /  .  <-- Độ chênh lệch chính là 1/2 * C * (Δy)^2
          │       / .
          │      /. (Đường thẳng Duration xấp xỉ)
          │     /───────────────────────
          │    /  
          └─────────────────────────────► Lợi suất (y)
```

### 2. Các Công thức Tính Toán Duration & Convexity
#### A. Macaulay Duration ($D$)
$$D = \sum_{t=1}^T t \times w_t, \quad \text{với } w_t = \frac{\frac{CF_t}{(1+y)^t}}{P}$$
*(Trong đó: $w_t$ là tỷ trọng giá trị hiện tại của dòng tiền năm $t$ trên tổng giá trái phiếu, tổng các $w_t$ bằng đúng 1.0).*

#### B. Modified Duration ($D^*$) - Độ nhạy cảm phần trăm
$$D^* = \frac{D}{1 + y/m}$$
*(với $m$ là số lần ghép lãi mỗi năm: $m=1$ nếu ghép lãi năm, $m=2$ nếu bán niên).*
$$\frac{\Delta P}{P} \approx -D^* \times \Delta y$$

#### C. Dollar Duration ($D_{\$}$) và DV01
$$D_{\$} = D^* \times P \implies \Delta P \approx -D_{\$} \times \Delta y$$
$$DV01 = D^* \times P \times 0.0001 \quad (\text{Mức lỗ tính bằng tiền mặt khi lãi suất tăng 1 điểm cơ bản})$$

#### D. Công thức Xấp xỉ Bậc 2 (Kết hợp Duration và Convexity)
$$\frac{\Delta P}{P} \approx -D^* \Delta y + \frac{1}{2} C (\Delta y)^2$$

> [!IMPORTANT]
> **KẾT LUẬN THI CỬ VÀNG VỀ ĐỘ LỒI:**
> Vì số hạng $\frac{1}{2} C (\Delta y)^2$ luôn **DƯƠNG** với mọi biến động $\Delta y \ne 0$:
> **Công thức chỉ dùng Duration luôn luôn ĐÁNH GIÁ THẤP (UNDERESTIMATES) giá trị thực tế của trái phiếu ở CẢ HAI CHIỀU!**
> - Khi lãi suất giảm: Giá thực tế tăng **nhiều hơn** mức Duration dự báo.
> - Khi lãi suất tăng: Giá thực tế giảm **ít hơn** mức Duration dự báo.

### 3. Chiến lược Miễn nhiễm Rủi ro Lãi suất (Bond Immunization)
- **Bản chất trò chơi Kéo Co**: Khi lãi suất tăng:
  - *Rủi ro giá (Price risk)*: Bạn bị lỗ vì giá trái phiếu sụt giảm.
  - *Rủi ro tái đầu tư (Reinvestment risk)*: Bạn lại vui vì các khoản tiền coupon nhận về được đem đi gửi với lãi suất cao hơn!
  - **Miễn nhiễm** là chọn thời điểm sao cho hai lực kéo này triệt tiêu hoàn toàn lẫn nhau!
- **3 Điều kiện Miễn nhiễm Bắt buộc Phải Nhớ**:
  1. **Khớp Giá trị Hiện tại**: $V_A = V_L$ (Giá trị tài sản bằng giá trị nghĩa vụ nợ).
  2. **Khớp Modified Duration**:
     $$D^*_A = D^*_L \times \frac{V_L}{V_A} \quad (\text{Nếu } V_A = V_L \implies D_A = D_L)$$
  3. **Điều kiện Độ lồi (Convexity Condition)**:
     $$C_A > C_L$$
     *(Độ lồi của tài sản phải lớn hơn nghĩa vụ nợ để khi lãi suất biến động theo bất kỳ chiều nào, tài sản cũng tăng nhiều hơn nợ hoặc giảm ít hơn nợ).*
- **Tại sao phải tái cân bằng định kỳ (Rebalancing)?**
  - Khi thời gian trôi qua, Duration của trái phiếu coupon giảm chậm hơn Duration của một nghĩa vụ nợ đơn lẻ.
  - Khi lãi suất thị trường thay đổi, Duration của cả hai cũng biến đổi theo.
  - **Lỗ hổng chết người**: Miễn nhiễm chỉ bảo vệ trước **sự dịch chuyển song song (Parallel Shift)** của đường cong lãi suất. Nếu đường cong bị xoắn (Twist) hoặc thay đổi độ cong (Butterfly shift), danh mục miễn nhiễm vẫn có thể bị thua lỗ nặng!

### 4. Chiến lược Tính toán Siêu tốc & Lỗi sai Thường gặp ở Lecture 03
> [!TIP]
> **CÔNG THỨC GIẢI NHANH TRỌNG SỐ MIỄN NHIỄN 2 TRÁI PHIẾU:**  
> Muốn tạo danh mục có Duration mục tiêu $D_L$ từ Trái phiếu 1 ($D_1$) và Trái phiếu 2 ($D_2$):
> $$w_1 = \frac{D_2 - D_L}{D_2 - D_1}, \quad w_2 = 1 - w_1$$
> *Bấm máy đúng 5 giây là ra tỷ trọng vốn!*

> [!WARNING]
> **LỖI SAI CHẾT NGƯỜI 1**: Đề bài cho lãi suất tăng 35 điểm cơ bản ($35 \text{ bps}$). Rất nhiều bạn lấy $\Delta y = 35$ hoặc $\Delta y = 0.35$! **Nhớ kỹ: $1 \text{ bp} = 0.0001 \implies 35 \text{ bps} = 0.0035$!**  
> **LỖI SAI CHẾT NGƯỜI 2**: Khi tính Modified Duration cho trái phiếu bán niên: $D^* = \frac{D}{1 + y/2}$. Rất nhiều bạn quên chia đôi $y$, lấy luôn $\frac{D}{1+y}$ là mất trắng điểm câu này!

---

# LECTURE 04: Lợi suất, Rủi ro & Phân bổ Vốn Danh mục
*(Returns, Risk, Utility, and Capital Allocation)*

### 1. Giải thích cho một đứa trẻ: "Bẫy Kéo Tụt Biến Động" (Volatility Drag)
- Bạn có 100 triệu.
- Năm 1 bạn lãi $+50\%$ $\implies$ Bạn có $100 \times 1.5 = 150$ triệu (vui mừng!).
- Năm 2 bạn lỗ $-50\%$ $\implies$ Bạn còn $150 \times 0.5 = 75$ triệu (sốc!).
- Bạn nhìn lại: Bình quân số học là $\frac{+50\% - 50\%}{2} = 0\%$. Về lý thuyết "hòa vốn", nhưng sao trong túi bạn lại **mất toi 25 triệu (lỗ 25%)**?
- $\implies$ Đó chính là **Kéo tụt biến động (Volatility Drag)**! Biến động càng lớn, của cải thực tế tích lũy càng bị bào mòn.
- **Công thức xấp xỉ liên hệ giữa Lợi suất Số học và Hình học**:
  $$r_{\text{geometric}} \approx \bar{r}_{\text{arithmetic}} - \frac{1}{2}\sigma^2$$
  - Muốn tính của cải sau nhiều năm (Ending Wealth): **Bắt buộc phải dùng Geometric Mean (CAGR)**!
  - Dùng Arithmetic Mean sẽ thổi phồng ảo tưởng số tiền bạn nhận được!

### 2. Hàm Thỏa Dụng (Utility Function) & Mức độ Ngại Rủi ro ($A$)
$$U = E(r) - \frac{1}{2} A \sigma^2$$
- $E(r)$: Lợi nhuận kỳ vọng (phần thưởng bạn thích).
- $\frac{1}{2} A \sigma^2$: Hình phạt tâm lý vì sự lo âu, sợ hãi trước rủi ro.
- $A > 0$: Người ngại rủi ro (Risk-averse). $A$ càng lớn, càng nhát gan.
- **Certainty Equivalent Rate ($r_{ce}$)**: Mức lãi suất phi rủi ro chắc chắn gửi ngân hàng đem lại độ sướng đúng bằng danh mục rủi ro: $r_{ce} = U$.

### 3. Đường Phân Bổ Vốn (CAL) & Tỷ số Sharpe
- Bạn có tiền mặt, bạn chia thành 2 phần: tỷ lệ $y$ đầu tư vào danh mục rủi ro $P$, và $(1-y)$ gửi vào tài sản phi rủi ro $r_f$.
- Danh mục hoàn chỉnh $C$ có:
  $$E(r_C) = r_f + y [E(r_P) - r_f], \quad \sigma_C = y \sigma_P$$
- **Phương trình đường CAL (Capital Allocation Line)**:
  $$E(r_C) = r_f + \underbrace{\left[ \frac{E(r_P) - r_f}{\sigma_P} \right]}_{\text{Sharpe Ratio (Độ dốc đường CAL)}} \sigma_C$$
- **TỶ TRỌNG TỐI ƯU RÓT VÀO DANH MỤC RỦI RO ($y^*$)**:
  $$y^* = \frac{E(r_P) - r_f}{A \sigma_P^2}$$
  - Nếu $y^* < 1$: Cho vay một phần ở lãi suất $r_f$.
  - Nếu $y^* = 1$: Đầu tư đúng $100\%$ tiền túi vào $P$.
  - Nếu $y^* > 1$: Đi vay nợ ký quỹ (Margin Borrowing at $r_f$) để đòn bẩy!

---

# LECTURE 05: Lựa chọn Danh mục Đầu tư, Markowitz Frontier & CML
*(Portfolio Selection, Minimum-Variance Frontier, and Capital Market Line)*

### 1. Giải thích cho một đứa trẻ: "Trời mưa bán Ô, Trời nắng bán Kem"
- Nếu bạn mở quán bán Kem: Trời nắng lãi to, trời mưa ế ẩm lỗ nặng ($\sigma$ rất cao).
- Nếu bạn mở quán bán Ô: Trời mưa lãi to, trời nắng ế ẩm ($\sigma$ rất cao).
- Nhưng nếu bạn **vừa bán Kem vừa bán Ô** (Tương quan âm $\rho < 0$): Ngày nắng kem bù ô, ngày mưa ô bù kem $\implies$ Ngày nào bạn cũng có thu nhập ổn định! Rủi ro sụt giảm kinh ngạc mà lợi nhuận không hề bị mất đi!
- $\implies$ **Đó là điều kỳ diệu của Đa dạng hóa danh mục Markowitz (Diversification)!**

### 2. Danh mục 2 Tài sản Rủi ro & Danh mục Phương sai Tối thiểu (MVP)
- Phương sai danh mục:
  $$\sigma_P^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \text{Cov}(r_1, r_2) = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$$
- **TỶ TRỌNG DANH MỤC PHƯƠNG SAI THẤP NHẤT (MVP)**:
  $$w_1^{\text{MVP}} = \frac{\sigma_2^2 - \text{Cov}(r_1, r_2)}{\sigma_1^2 + \sigma_2^2 - 2\text{Cov}(r_1, r_2)}, \quad w_2^{\text{MVP}} = 1 - w_1^{\text{MVP}}$$

### 3. Danh mục Tiếp điểm (Tangency Portfolio) & Định lý Phân tách 2 Quỹ
- **Danh mục Tiếp điểm ($P^*$)**: Là danh mục rủi ro tối đa hóa Tỷ số Sharpe: $\max SR = \frac{E(r_P) - r_f}{\sigma_P}$.
- **Two-Fund Separation Theorem (Định lý Tobin)**:
  - *Bước 1*: Bất kể bạn là ai, già hay trẻ, dũng cảm hay nhát gan, danh mục tài sản rủi ro tối ưu $P^*$ tiếp xúc với đường biên Markowitz là **GIỐNG HỆT NHAU** đối với mọi nhà đầu tư!
  - *Bước 2*: Mức độ sợ rủi ro $A$ của riêng bạn chỉ quyết định xem bạn sẽ chia bao nhiêu % tiền vào $P^*$ và bao nhiêu % tiền gửi tiết kiệm $r_f$ ($y^*$).
- **Capital Market Line (CML)**: Khi thị trường cân bằng, danh mục rủi ro tối ưu $P^*$ chính là **Danh mục Thị trường toàn cầu ($M$)**. Đường CML là đường CAL đi qua $M$:
  $$E(r_C) = r_f + \left[ \frac{E(r_M) - r_f}{\sigma_M} \right] \sigma_C$$
  *Lưu ý sống còn*: **CML chỉ áp dụng cho danh mục đã đa dạng hóa hoàn hảo. Không dùng CML cho cổ phiếu lẻ!**

---

# LECTURE 06: TRỌNG TÂM OLS I - Mô hình Chỉ số Đơn (SIM), CAPM & Hồi quy OLS
*(Single-Index Model, CAPM, and OLS Mechanics)*

### 1. Giải thích cho một đứa trẻ: "Con thuyền lênh đênh trên biển cả"
- Hãy tưởng tượng mỗi cổ phiếu là một **con thuyền** đang bơi trên biển:
  - Khi có một **cơn sóng thần vĩ mô** (Thị trường chung $R_M$ dâng lên): Mọi con thuyền đều bị nâng lên! Độ nhạy của thuyền với con sóng gọi là **Beta ($\beta$)**.
  - Nhưng bản thân con thuyền có **động cơ riêng** của nó (sự cố cháy máy, thuyền trưởng tài ba): Đây là phần rủi ro đặc thù riêng biệt **($e_i$)**.
  - Và nếu thuyền trưởng có bí kíp riêng giúp thuyền luôn chạy nhanh hơn mức sóng đẩy: Đó chính là **Alpha ($\alpha$)**!
- $\implies$ **Phương trình Mô hình Chỉ số Đơn (Single-Index Model - SIM)**:
  $$R_{i,t} = \alpha_i + \beta_i R_{M,t} + e_{i,t}$$

```
Biến động Cổ phiếu (Ri) = [Sóng biển thị trường (β * RM)] + [Động cơ riêng (ei)] + [Tài năng (α)]
```

### 2. Toán học OLS & Phân Rã Phương Sai (Variance Decomposition)
- Hồi quy OLS tìm đường thẳng sao cho tổng bình phương sai số nhỏ nhất:
  $$\hat{\beta}_i = \frac{\text{Cov}(R_i, R_M)}{\text{Var}(R_M)} = \frac{\sigma_{iM}}{\sigma_M^2} = \rho_{iM} \frac{\sigma_i}{\sigma_M}$$
  $$\hat{\alpha}_i = \bar{R}_i - \hat{\beta}_i \bar{R}_M$$
- **PHƯƠNG TRÌNH PHÂN RÃ PHƯƠNG SAI KINH ĐIỂN**:
  $$\sigma_i^2 = \underbrace{\beta_i^2 \sigma_M^2}_{\text{Rủi ro Hệ thống (Systematic)}} + \underbrace{\sigma^2(e_i)}_{\text{Rủi ro Đặc thù (Firm-specific)}}$$
- **Ý NGHĨA THỰC CHIẾN CỦA HỆ SỐ XÁC ĐỊNH $R^2$**:
  $$R^2 = \frac{\text{Phương sai Hệ thống}}{\text{Tổng phương sai}} = \frac{\beta_i^2 \sigma_M^2}{\sigma_i^2} = \rho_{iM}^2$$
  - $R^2$ trả lời câu hỏi: **Bao nhiêu phần trăm sự rung lắc của con thuyền là do sóng biển thị trường gây ra?**
  - $1 - R^2$: Tỷ lệ rung lắc do động cơ riêng của thuyền gây ra (có thể triệt tiêu khi buộc 1,000 con thuyền lại với nhau).

### 3. Mô hình CAPM & Đường SML (Security Market Line)
- **Phương trình CAPM**:
  $$E(r_i) = r_f + \beta_i [E(r_M) - r_f]$$
- **Tại sao thị trường KHÔNG BAO GIỜ trả tiền cho rủi ro đặc thù $\sigma^2(e_i)$?**
  - Bởi vì bất kỳ nhà đầu tư nào cũng có thể tự gom 50 - 100 cổ phiếu vào danh mục để xóa sổ rủi ro đặc thù hoàn toàn miễn phí!
  - Thị trường chỉ trả phần thưởng bù đắp cho rủi ro mà bạn **không thể đa dạng hóa được**, đó chính là **Rủi ro Hệ thống đo bằng Beta ($\beta$)**!
- **Jensen's Alpha & Phát hiện Cổ phiếu Định giá Sai**:
  $$\alpha_i = E(r_i)_{\text{dự báo thực tế}} - E(r_i)_{\text{yêu cầu theo CAPM}}$$
  - $\alpha_i > 0$: Cổ phiếu **bị định giá thấp (Undervalued)** $\implies$ Nằm **TRÊN đường SML** $\implies$ Khuyến nghị: **MUA (BUY)**.
  - $\alpha_i < 0$: Cổ phiếu **bị định giá cao (Overvalued)** $\implies$ Nằm **DƯỚI đường SML** $\implies$ Khuyến nghị: **BÁN (SELL)**.
  - $\alpha_i = 0$: Định giá công bằng (Fairly priced), nằm ngay trên đường SML.

---

# LECTURE 07: TRỌNG TÂM OLS II - Mô hình Đa nhân tố, APT & Fama-French 3 Nhân tố
*(Multifactor Models, Arbitrage Pricing Theory, and Fama-French)*

### 1. Giải thích cho một đứa trẻ: "Tay không bắt giặc" (Pure Arbitrage trong APT)
- **Arbitrage (Kinh doanh chênh lệch giá thuần túy)** là gì?
  - Bạn thấy quả táo ở chợ làng bán 5k, sang chợ huyện bán được 10k.
  - Bạn vay tiền mua táo ở làng, mang sang huyện bán ngay lập tức, trả lại tiền vay, đút túi 5k tiền lời chênh lệch.
  - Bạn không tốn một đồng vốn túi nào, không chịu một rủi ro nào mà chắc chắn có lãi!
- **4 Điều kiện Khắt khe của Pure Arbitrage trong đề thi**:
  1. $\sum w_i = 0$: **Vốn tự có ròng bằng 0** (Zero Net Investment - bán khống mã này lấy tiền mua mã kia).
  2. $\sum w_i \beta_{i,k} = 0$: **Rủi ro hệ thống bằng 0** (Zero Factor Beta Risk).
  3. $\sigma^2(e_P) \approx 0$: **Rủi ro đặc thù triệt tiêu về 0** (phải là danh mục đa dạng hóa khổng lồ theo Luật số lớn).
  4. $\sum w_i E(R_i) > 0$: **Lợi nhuận chắc chắn dương**!

### 2. Mô hình Fama-French 3 Nhân tố (FF3 Model)
CAPM chỉ có 1 nhân tố duy nhất là thị trường. Nhưng thực tế có 2 hiện tượng lạ mà CAPM bó tay:
1. **Các công ty nhỏ (Small caps)** thường sinh lời cao hơn công ty lớn.
2. **Các công ty giá trị (Value stocks - tỷ số Book-to-Market cao)** thường sinh lời cao hơn công ty tăng trưởng (Growth).
$\implies$ Fama và French lập ra mô hình 3 nhân tố:
$$R_{i,t} = \alpha_i + \beta_{i,MKT} R_{MKT,t} + \beta_{i,SMB} SMB_t + \beta_{i,HML} HML_t + e_{i,t}$$

- **SMB (Small Minus Big)**: Lợi suất danh mục Mua công ty Nhỏ, Bán khống công ty Lớn.
  - $\beta_{SMB} > 0$: Cổ phiếu nghiêng về **Vốn hóa nhỏ (Small-Cap Tilt)**.
  - $\beta_{SMB} < 0$: Cổ phiếu nghiêng về **Vốn hóa lớn (Large-Cap Tilt)**.
- **HML (High Minus Low)**: Lợi suất danh mục Mua công ty Giá trị (B/M cao), Bán khống công ty Tăng trưởng (B/M thấp).
  - $\beta_{HML} > 0$: Cổ phiếu mang phong cách **Giá trị (Value Tilt)**.
  - $\beta_{HML} < 0$: Cổ phiếu mang phong cách **Tăng trưởng (Growth Tilt)**.

### 3. Vạch mặt "Tài năng Quản lý Quỹ": Alpha Biến Mất (Disappearing Alpha)
- Một ông quản lý quỹ khoe: "Năm qua tôi tạo ra Alpha CAPM $= +3.6\%$/năm, tôi là thiên tài chọn cổ phiếu!"
- Nhưng khi các nhà nghiên cứu đưa dữ liệu vào hồi quy Fama-French 3 nhân tố:
  - Hệ số $\beta_{SMB} = +0.70$ (rất cao) và $\beta_{HML} = +0.65$ (rất cao).
  - Alpha Fama-French tụt xuống bằng $0.03\%$/tháng ($t = 0.28, p = 0.78 > 0.05 \implies$ Không có ý nghĩa thống kê!).
- **SỰ THẬT ĐƯỢC PHƠI BÀY**:
  - Ông ta **hoàn toàn không có tài năng chọn cổ phiếu (No Stock-Picking Skill)**!
  - Lợi nhuận vượt trội ban đầu chỉ là do ông ta đã âm thầm mua một rổ cổ phiếu công ty nhỏ và cổ phiếu giá trị (chịu rủi ro cao hơn nên được bù đắp lợi nhuận). Nhà đầu tư không việc gì phải trả phí quản lý đắt đỏ cho ông ta, chỉ cần mua quỹ ETF Small-Cap Value giá rẻ là xong!

---

# CHUYÊN ĐỀ ĐẶC BIỆT: "BẮT BÀI" ĐỌC BẢNG HỒI QUY OLS / EXCEL LINEST TRONG ĐỀ THI

Trong bài kiểm tra, giảng viên rất thích trích xuất bảng kết quả từ hàm `LINEST` của Excel hoặc phần mềm thống kê. Đây là "mỏ điểm" nếu bạn nắm chắc quy luật:

### 1. Bảng Kết quả Chuẩn Điển hình (Standard Regression Output)
Hồi quy lợi suất vượt trội cổ phiếu TechX theo mô hình Fama-French 3 nhân tố ($N = 120$ tháng):

| Biến số (Variables) | Hệ số ước lượng (Coefficients) | Sai số chuẩn (Standard Error) | Thống kê $t$ ($t$-stat) | Mức ý nghĩa ($p$-value) |
|---|---:|---:|---:|---:|
| **Intercept (Alpha - $\alpha$)** | **0.0036** (0.36%/tháng) | 0.0016 | **2.25** | **0.026** |
| **Market (MKT - $\beta_{MKT}$)** | **1.2500** | 0.0625 | **20.00** | **< 0.001** |
| **Size (SMB - $\beta_{SMB}$)** | **-0.4500** | 0.1500 | **-3.00** | **0.003** |
| **Value (HML - $\beta_{HML}$)** | **-0.6000** | 0.2000 | **-3.00** | **0.003** |

*Các chỉ số phụ:* $R^2 = 0.6400$, Phương sai phần dư $s_e^2 = 0.0010$, $N = 120$.

### 2. 4 Bước "Bắt bài" Xử lý Mọi Câu hỏi Trắc nghiệm / Tự luận
1. **Kiểm tra công thức cột $t$-statistic**:
   $$t\text{-stat} = \frac{\text{Coefficient}}{\text{Standard Error}}$$
   *(Nếu đề bài che mất một ô, bạn lấy Hệ số chia cho SE là ra $t$-stat ngay! Ví dụ: $0.0036 / 0.0016 = 2.25$).*
2. **Kiểm định có ý nghĩa thống kê hay không (Significance Test)**:
   - Nhìn vào cột $p$-value: Nếu $p\text{-value} < 0.05$ (hoặc $|t\text{-stat}| > 2$) $\implies$ **Có ý nghĩa thống kê ở mức 5%** (Hệ số thực sự khác 0, không phải do ngẫu nhiên).
   - Ở bảng trên: Cả Alpha, MKT, SMB, HML đều có $p < 0.05 \implies$ Tất cả đều có ý nghĩa thống kê!
3. **Phân tích Phong cách Cổ phiếu (Style Analysis)**:
   - $\beta_{MKT} = 1.25 > 1 \implies$ Cổ phiếu nhạy cảm hơn thị trường 25% (Rủi ro hệ thống cao).
   - $\beta_{SMB} = -0.45 < 0 \implies$ Cổ phiếu mang phong cách **VỐN HÓA LỚN (Large-Cap)**.
   - $\beta_{HML} = -0.60 < 0 \implies$ Cổ phiếu mang phong cách **TĂNG TRƯỞNG (Growth)**.
   - $\implies$ *TechX là một cổ phiếu Công nghệ Tăng trưởng Vốn hóa Lớn (như Apple hay Microsoft)!*
4. **Ý nghĩa của $R^2 = 0.64$**:
   - $64\%$ sự biến động lợi suất của TechX được giải thích bởi 3 nhân tố MKT, SMB, HML.
   - $36\%$ còn lại ($1 - R^2 = 0.36$) là rủi ro đặc thù riêng của doanh nghiệp.

---

# CẨM NANG BẤM MÁY SIÊU TỐC & 10 LỖI SAI CHẾT NGƯỜI KHI LÀM BÀI TẬP
*(Speed-Run Playbook & Fatal Pitfalls)*

### 1. Bảng Công Thức "Cứu Mạng" 1 Trang Giấy

| Bài toán | Công thức Siêu tốc | Lưu ý Bấm máy |
|---|---|---|
| **Trái phiếu bán niên** | $P = \frac{C}{2} \left[ \frac{1-(1+y/2)^{-2T}}{y/2} \right] + \frac{M}{(1+y/2)^{-2T}}$ | Nhớ: coupon cưa đôi, lợi suất cưa đôi, năm nhân đôi |
| **Lợi suất EAY** | $EAY = (1 + y_{\text{nom}}/2)^2 - 1$ | $EAY$ luôn lớn hơn $y_{\text{nom}}$ |
| **Lãi suất kỳ hạn 1 năm** | $f_{t-1, t} = \frac{(1+s_t)^t}{(1+s_{t-1})^{t-1}} - 1$ | Rút từ chuỗi Spot Rates $s_t$ |
| **Modified Duration** | $D^* = \frac{D}{1 + y/m}$ | Ghép lãi bán niên thì chia cho $1 + y/2$ |
| **Xấp xỉ thay đổi giá** | $\frac{\Delta P}{P} \approx -D^* \Delta y + \frac{1}{2} C (\Delta y)^2$ | Nhớ: Duration có dấu trừ, Convexity có dấu cộng |
| **Trọng số Miễn nhiễm** | $w_1 = \frac{D_2 - D_L}{D_2 - D_1}$ | Khớp Duration danh mục bằng Duration nợ $D_L$ |
| **Kéo tụt biến động** | $r_g \approx \bar{r} - \frac{1}{2}\sigma^2$ | Nhập $\sigma$ ở dạng số thập phân |
| **Tỷ trọng rủi ro tối ưu** | $y^* = \frac{E(r_P) - r_f}{A \sigma_P^2}$ | $y^* > 1$ nghĩa là đi vay margin |
| **Trọng số MVP 2 tài sản** | $w_1 = \frac{\sigma_2^2 - \text{Cov}}{\sigma_1^2 + \sigma_2^2 - 2\text{Cov}}$ | $\text{Cov} = \rho \sigma_1 \sigma_2$ |
| **Beta Hồi quy OLS** | $\beta_i = \frac{\text{Cov}(R_i, R_M)}{\sigma_M^2} = \rho_{iM} \frac{\sigma_i}{\sigma_M}$ | Đo rủi ro hệ thống |
| **Phân rã Phương sai SIM** | $\sigma_i^2 = \beta_i^2 \sigma_M^2 + \sigma^2(e_i)$ | $R^2 = \frac{\beta^2 \sigma_M^2}{\sigma_i^2}$ |
| **Lợi suất kỳ vọng CAPM** | $E(r_i) = r_f + \beta_i [E(r_M) - r_f]$ | Chỉ đền bù cho rủi ro Beta |
| **Jensen\'s Alpha** | $\alpha_i = E(r_i)_{\text{dự báo}} - E(r_i)_{\text{CAPM}}$ | $\alpha > 0$: Định giá thấp (MUA); $\alpha < 0$: Định giá cao (BÁN) |
| **Lợi suất kỳ vọng FF3** | $E(R_i) = \beta_M \lambda_M + \beta_{SMB} \lambda_{SMB} + \beta_{HML} \lambda_{HML}$ | $\lambda$ là phần bù rủi ro của từng nhân tố |

---

### 2. Mười Lỗi Sai Chết Người Phải Tuyệt Đối Tránh Trong Phòng Thi
1. **Lỗi Quên chia đôi khi gặp chữ "Semiannual"**: Cứ thấy semiannual là ngay lập tức lấy bút chì khoanh tròn và ghi: $C/2$, $y/2$, $2n$.
2. **Lỗi Nhầm lẫn đơn vị Basis Points**: $25 \text{ bps} = 0.0025$, $50 \text{ bps} = 0.0050$. Đừng nhập 25 hay 0.25 vào máy tính!
3. **Lỗi Nhập sai đơn vị phương sai trong hàm thỏa dụng $U = E(r) - \frac{1}{2}A\sigma^2$**: Nếu $E(r) = 10\% = 0.10$ và $\sigma = 20\% = 0.20$, phải bấm $0.10 - 0.5 \times A \times (0.20)^2$. Nếu bạn bấm $\sigma^2 = 400$ là sai lệch 100 lần!
4. **Lỗi Quên rằng Duration luôn đánh giá thấp (Underestimate) giá thực tế ở cả 2 chiều**: Cả khi lãi suất tăng hay giảm, giá thực tế của trái phiếu straight luôn nằm cao hơn giá do Duration dự báo.
5. **Lỗi Nhầm lẫn giữa CML và SML**: CML trục hoành là tổng rủi ro $\sigma$ (chỉ dùng cho danh mục hiệu quả); SML trục hoành là Beta $\beta$ (dùng cho mọi tài sản lẻ).
6. **Lỗi Tưởng $R^2$ quyết định lợi suất kỳ vọng**: Trong CAPM, lợi suất kỳ vọng chỉ do Beta quyết định, $R^2$ cao hay thấp không ảnh hưởng đến lợi suất kỳ vọng!
7. **Lỗi Nghĩ rằng Alpha CAPM dương là nhà quản lý giỏi**: Phải kiểm tra Fama-French 3 nhân tố. Nếu Alpha tụt về 0 thì đó chỉ là do mua cổ phiếu nhỏ hoặc cổ phiếu giá trị!
8. **Lỗi Tưởng chiến lược Miễn nhiễm là mua rồi vứt đó**: Phải tái cân bằng liên tục vì Duration thay đổi theo thời gian và lãi suất, và miễn nhiễm thất bại nếu đường cong bị xoắn (non-parallel shift).
9. **Lỗi Nhầm lẫn giữa Zero-coupon bond và Coupon bond**: Zero-coupon bond thì $D = T$ (Duration đúng bằng số năm đáo hạn).
10. **Lỗi Pure Arbitrage đòi hỏi cả 2 loại rủi ro bằng 0**: Không chỉ triệt tiêu Beta ($\beta_p = 0$) mà còn phải triệt tiêu cả rủi ro đặc thù ($\sigma^2(e_p) \approx 0$) thông qua đa dạng hóa lớn.
