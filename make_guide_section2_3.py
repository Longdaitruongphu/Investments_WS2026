import sys

out_file = "/media/minh/DISK/Downloads/Investments_WS2026/MASTER_EXAM_PREPARATION_ULTIMATE_GUIDE.md"

sec2_3 = r"""
---

## 2.3. LECTURE 11: ĐỊNH GIÁ QUYỀN CHỌN - MÔ HÌNH NHỊ THỨC (BOPM) & BLACK-SCHOLES-MERTON (BSM)

### 2.3.1. Khung Lý Thuyết Cốt Tử & Bản Chất Toán - Kinh Tế

#### A. Mô Hình Nhị Thức 1 Thời Kỳ (One-Period Binomial Model)
1. **Ba phương pháp định giá tương đương (Đều cho ra cùng 1 đáp số duy nhất)**:
   - **Phương pháp 1: Danh mục Sao chép (Replicating Portfolio)**
     - Mua $\Delta$ cổ phiếu và đầu tư/vay $B$ trái phiếu phi rủi ro:
       $$\begin{cases} \text{Kịch bản Tăng (Up): } \Delta S_0 u + B r = f_u \\ \text{Kịch bản Giảm (Down): } \Delta S_0 d + B r = f_d \end{cases}$$
     - Giải hệ phương trình:
       $$\mathbf{\Delta = \frac{f_u - f_d}{S_0 (u - d)}}, \qquad \mathbf{B = \frac{u f_d - d f_u}{r(u - d)} = \frac{f_u - \Delta S_0 u}{r}}$$
     - Giá trị quyền chọn hôm nay: $f_0 = \Delta S_0 + B$.
     - *Lưu ý*: $B < 0$ nghĩa là **đi vay (Borrowing)** tiền mặt; $B > 0$ nghĩa là **cho vay/gửi tiết kiệm (Lending)**.
   - **Phương pháp 2: Giá Trạng Thái Arrow-Debreu (State Prices)**
     - $P_u$: Giá hôm nay của chứng khoán trả 1 USD nếu thị trường Tăng, 0 USD nếu Giảm:
       $$P_u = \frac{r - d}{r(u - d)}$$
     - $P_d$: Giá hôm nay của chứng khoán trả 0 USD nếu Tăng, 1 USD nếu Giảm:
       $$P_d = \frac{u - r}{r(u - d)}$$
     - **Quy tắc bảo toàn không chênh lệch giá**: $P_u + P_d = \frac{1}{r}$ (tổng giá trị 2 chứng khoán trạng thái đúng bằng giá trái phiếu zero-coupon phi rủi ro mệnh giá 1 USD).
     - Định giá bất kỳ chứng khoán phái sinh nào: $f_0 = f_u P_u + f_d P_d$.
   - **Phương pháp 3: Định giá Trung lập Rủi ro (Risk-Neutral Valuation)**
     - Xác suất trung lập rủi ro (Risk-neutral probability) $p$:
       $$\mathbf{p = \frac{r - d}{u - d}}, \qquad 1 - p = \frac{u - r}{u - d}$$
     - Giá trị quyền chọn là kỳ vọng toán học chiết khấu theo lãi suất phi rủi ro:
       $$\mathbf{f_0 = \frac{p f_u + (1 - p) f_d}{r}}$$
     - *Bản chất kinh tế cốt lõi*: $p$ **KHÔNG PHẢI** là xác suất thực tế (physical probability) trong thế giới thực. $p$ là một thước đo xác suất nhân tạo đã hấp thu toàn bộ phần bù rủi ro của nhà đầu tư. Trong thế giới trung lập rủi ro, mọi tài sản (kể cả cổ phiếu rủi ro) đều có tỷ suất sinh lời kỳ vọng đúng bằng lãi suất phi rủi ro: $E^Q(S_T) = p S_0 u + (1-p) S_0 d = S_0 r$.

#### B. Mô Hình Cây Nhị Thức Đa Thời Kỳ & Thực Thi Sớm American Option
1. **Nguyên lý Quy nạp Lùi (Backward Induction)**:
   - Tính giá cổ phiếu tại tất cả các nút: $S_{jk} = S_0 u^j d^{k-j}$.
   - Tính payoff quyền chọn tại các nút đáo hạn cuối cùng $T$: $f_T = \max(S_T - K, 0)$ hoặc $\max(K - S_T, 0)$.
   - Lùi dần từng bước về quá khứ: Giá trị tại nút cha = chiết khấu kỳ vọng trung lập rủi ro từ 2 nút con.
2. **Quy tắc Kiểm tra Thực thi Sớm Quyền chọn Mỹ (American Option Early Exercise)**:
   - Tại mỗi nút trung gian $t$, giá trị quyền chọn Mỹ là:
     $$V_{\text{Amer}} = \max\left(\text{Giá trị Nội tại (Intrinsic Value)}, \text{Giá trị Tiếp tục Giữ (Continuation Value)}\right)$$
     $$V_{\text{Amer}} = \max\left(\text{Payoff nếu thực thi ngay}, \frac{p V_u + (1-p) V_d}{r}\right)$$
   - Nếu $\text{Intrinsic Value} > \text{Continuation Value} \implies$ **THỰC THI NGAY (Early Exercise)**.
   - Khi đó, dùng giá trị thực thi này để tiếp tục quy nạp lùi về các nút trước đó!

#### C. Mô Hình Black-Scholes-Merton (BSM) & The Greeks
1. **Công thức Chuẩn**:
   $$\mathbf{C_0 = S_0 N(d_1) - K e^{-rT} N(d_2)}$$
   $$\mathbf{P_0 = K e^{-rT} N(-d_2) - S_0 N(-d_1) = K e^{-rT}[1 - N(d_2)] - S_0[1 - N(d_1)]}$$
   Trong đó:
   $$d_1 = \frac{\ln(S_0 / K) + (r + \sigma^2 / 2)T}{\sigma \sqrt{T}} = \frac{\ln[S_0 / PV(K)]}{\sigma \sqrt{T}} + \frac{\sigma \sqrt{T}}{2}$$
   $$d_2 = d_1 - \sigma \sqrt{T}$$
2. **Ý nghĩa Kinh tế của Các Thành phần**:
   - $\Delta_{\text{call}} = N(d_1) \in (0, 1)$: Hệ số Delta, số lượng cổ phiếu cần mua để sao chép 1 Call.
   - $N(d_2) \in (0, 1)$: **Xác suất quyền chọn Call kết thúc In-the-money** trong thế giới trung lập rủi ro, tức $P^Q(S_T > K)$.
   - $K e^{-rT} N(d_2)$: Số tiền mặt cần đi vay tại lãi suất phi rủi ro.
   - $\Delta_{\text{put}} = N(d_1) - 1 = -N(-d_1) \in (-1, 0)$: Hệ số Delta của Put.
3. **Đòn Bẩy & Beta của Quyền Chọn (Signed Leverage & Option Beta)**:
   - Tỷ số đòn bẩy có dấu (Signed Leverage):
     $$\mathbf{\Omega = \frac{S_0 \Delta}{V_{\text{option}}}}$$
   - Beta của quyền chọn theo mô hình CAPM:
     $$\mathbf{\beta_{\text{option}} = \Omega \times \beta_S = \left(\frac{S_0 \Delta}{V_{\text{option}}}\right) \beta_S}$$
   - *Tính chất*:
     - Với cổ phiếu có $\beta_S > 0$: Call luôn có $\Delta_C > 0 \implies \Omega_C > 1 \implies \mathbf{\beta_{\text{call}} > \beta_S > 0}$ (Call khuếch đại rủi ro thị trường).
     - Put luôn có $\Delta_P < 0 \implies \mathbf{\beta_{\text{put}} < 0}$ (Put là công cụ phòng vệ có beta âm).

---

### 2.3.2. Giải Chi Tiết Toàn Bộ Bài Tập Lớn Trong Slide Lecture 11

#### Bài 1: Cổ phiếu Gamma - So Sánh Quyền Chọn ATM, Deep ITM & Quyền Chọn Mỹ (Slide 16-17)
- **Đề bài**: Cổ phiếu Gamma giá $S_0 = 50$ USD. Sau 1 năm, giá tăng 40% ($u=1.40 \implies S_u = 70$) hoặc giảm 40% ($d=0.60 \implies S_d = 30$). Lãi suất $r = 8\%$ ($EAR = 1.08$).
  - (a) Tính giá Put châu Âu ATM kỳ hạn 1 năm ($K=50$).
  - (b) Tính giá Call châu Âu ATM kỳ hạn 1 năm ($K=50$).
  - (c) Tính giá Put châu Âu Deep ITM kỳ hạn 1 năm ($K=70$).
  - (d) Nếu các quyền chọn Put ở câu (a) và (c) là quyền chọn Mỹ, giá trị của chúng là bao nhiêu? Có nên thực thi sớm không?
- **Lời giải chi tiết**:
  - Xác suất trung lập rủi ro:
    $$p = \frac{r - d}{u - d} = \frac{1.08 - 0.60}{1.40 - 0.60} = \frac{0.48}{0.80} = 0.60, \qquad 1 - p = 0.40$$
  - (a) **Put châu Âu ATM ($K=50$)**:
    - Payoff: $P_u = \max(50 - 70, 0) = 0$; $P_d = \max(50 - 30, 0) = 20$.
    - Giá Put: $P_0 = \frac{0.60(0) + 0.40(20)}{1.08} = \frac{8.00}{1.08} \approx \mathbf{\$7.41}$.
  - (b) **Call châu Âu ATM ($K=50$)**:
    - Payoff: $C_u = \max(70 - 50, 0) = 20$; $C_d = \max(30 - 50, 0) = 0$.
    - Giá Call: $C_0 = \frac{0.60(20) + 0.40(0)}{1.08} = \frac{12.00}{1.08} \approx \mathbf{\$11.11}$.
    - *Kiểm tra Put-Call Parity*: $C_0 - P_0 = 11.11 - 7.41 = 3.70$. Vế phải: $S_0 - K/r = 50 - 50/1.08 = 50 - 46.30 = 3.70$ (Khớp tuyệt đối!).
  - (c) **Put châu Âu Deep ITM ($K=70$)**:
    - Payoff: $P_u = \max(70 - 70, 0) = 0$; $P_d = \max(70 - 30, 0) = 40$.
    - Giá Put: $P_0 = \frac{0.60(0) + 0.40(40)}{1.08} = \frac{16.00}{1.08} \approx \mathbf{\$14.81}$.
  - (d) **Định giá American Put**:
    - *Với Put ATM ($K=50$)*: Giá trị nội tại hôm nay $= \max(50 - 50, 0) = 0$. Giá trị tiếp tục giữ $= 7.41$. Vì $0 < 7.41 \implies$ Tiếp tục giữ (Hold). Giá American Put = **\$7.41**.
    - *Với Put Deep ITM ($K=70$)*: Giá trị nội tại hôm nay $= \max(70 - 50, 0) = \mathbf{\$20.00}$. Giá trị tiếp tục giữ $= \$14.81$.
    - Vì $\mathbf{\$20.00 > \$14.81} \implies$ **THỰC THI NGAY LẬP TỨC (Exercise Now)!**
    - Giá trị của American Put Deep ITM hôm nay = **\$20.00**.

#### Bài 2: Cây Nhị Thức 2 Thời Kỳ Phức Tạp (Delta Corp - Slide 21-22)
- **Đề bài**: Cổ phiếu Delta Corp giá $S_0 = 10$ USD. Trong mỗi năm của 2 năm tới, giá cổ phiếu **tăng 3 USD** hoặc **giảm 2 USD** (Mô hình cộng tính absolute dollar moves). Không cổ tức. Lãi suất hiệu dụng $r = 4\%$/năm ($r = 1.04$).
  - (a) Tính giá quyền chọn Call châu Âu kỳ hạn 2 năm, strike $K = 12$ USD.
  - (b) Tính giá quyền chọn Put châu Âu kỳ hạn 2 năm, strike $K = 12$ USD.
- **Lời giải chi tiết**:
  - **Xây dựng Cây Giá Cổ Phiếu**:
    - $t=0$: $S_0 = 10$.
    - $t=1$: $S_u = 10 + 3 = 13$; $S_d = 10 - 2 = 8$.
    - $t=2$:
      - Từ $S_u=13 \to S_{uu} = 13 + 3 = 16$; $S_{ud} = 13 - 2 = 11$.
      - Từ $S_d=8 \to S_{du} = 8 + 3 = 11$; $S_{dd} = 8 - 2 = 6$.
  - *Bẫy thi cực kỳ nguy hiểm*: Vì giá biến động theo số tiền tuyệt đối (+3, -2), tỷ lệ tăng giảm $u, d$ và xác suất trung lập rủi ro $p$ **KHÁC NHAU TẠI TỪNG NÚT!** Không được lấy xác suất tại gốc áp dụng cho nút sau!
  - **(a) Định giá Call($K=12$)**:
    - Payoff tại $t=2$: $C_{uu} = \max(16-12, 0) = 4$; $C_{ud} = \max(11-12, 0) = 0$; $C_{du} = 0$; $C_{dd} = 0$.
    - *Tại nút $u$ ($S_u = 13$)*:
      - $u_u = 16/13 \approx 1.2308$, $d_u = 11/13 \approx 0.8462$.
      - $p_u = \frac{1.04 - 11/13}{16/13 - 11/13} = \frac{1.04 \times 13 - 11}{5} = \frac{13.52 - 11}{5} = \frac{2.52}{5} = \mathbf{0.504}$.
      - $C_u = \frac{0.504(4) + 0.496(0)}{1.04} = \frac{2.016}{1.04} \approx 1.9385$ USD.
    - *Tại nút $d$ ($S_d = 8$)*: Cả 2 nút con đều có payoff $= 0 \implies C_d = 0$.
    - *Tại gốc $t=0$ ($S_0 = 10$)*:
      - $u_0 = 13/10 = 1.30$, $d_0 = 8/10 = 0.80$.
      - $p_0 = \frac{1.04 - 0.80}{1.30 - 0.80} = \frac{0.24}{0.50} = \mathbf{0.48}$.
      - $C_0 = \frac{0.48 C_u + 0.52 C_d}{1.04} = \frac{0.48(1.9385) + 0}{1.04} = \frac{0.93046}{1.04} \approx \mathbf{\$0.89}$.
  - **(b) Định giá Put($K=12$)**:
    - Payoff tại $t=2$: $P_{uu} = 0$; $P_{ud} = \max(12-11, 0) = 1$; $P_{du} = 1$; $P_{dd} = \max(12-6, 0) = 6$.
    - *Tại nút $u$ ($S_u = 13$)*: $p_u = 0.504$.
      $$P_u = \frac{0.504(0) + (1 - 0.504)(1)}{1.04} = \frac{0.496}{1.04} \approx 0.4769\ \text{USD}$$
    - *Tại nút $d$ ($S_d = 8$)*:
      - $u_d = 11/8 = 1.375$, $d_d = 6/8 = 0.75$.
      - $p_d = \frac{1.04 - 0.75}{1.375 - 0.75} = \frac{0.29}{0.625} = \mathbf{0.464}$.
      - $P_d = \frac{0.464(1) + (1 - 0.464)(6)}{1.04} = \frac{0.464 + 3.216}{1.04} = \frac{3.68}{1.04} \approx 3.5385\ \text{USD}$
    - *Tại gốc $t=0$ ($S_0 = 10$)*: $p_0 = 0.48$.
      $$P_0 = \frac{0.48 P_u + 0.52 P_d}{1.04} = \frac{0.48(0.4769) + 0.52(3.5385)}{1.04} = \frac{0.2289 + 1.8400}{1.04} = \frac{2.0689}{1.04} \approx \mathbf{\$1.99}$$

#### Bài 3: Định Giá Black-Scholes & Lập Danh Mục Sao Chép (Lambda - Slide 39-40)
- **Đề bài**: Cổ phiếu Lambda giá $S_0 = 90$ USD, không cổ tức, $\sigma = 30\%$/năm, lãi suất liên tục $r = 6\%$/năm.
  - (a) Định giá Call châu Âu ATM kỳ hạn 6 tháng ($T = 0.5, K = 90$).
  - (b) Xác định danh mục tự cấp vốn (Replicating Portfolio) để tạo ra vị thế Long Call này hôm nay.
- **Lời giải chi tiết**:
  - (a) **Tính toán BSM**:
    $$PV(K) = 90 e^{-0.06 \times 0.5} = 90 e^{-0.03} \approx 87.3401\ \text{USD}$$
    $$\sigma \sqrt{T} = 0.30 \times \sqrt{0.5} = 0.30 \times 0.707107 = 0.212132$$
    $$d_1 = \frac{\ln(90/90) + (0.06 + 0.09/2) \times 0.5}{0.212132} = \frac{0.0525}{0.212132} \approx 0.2475$$
    $$d_2 = d_1 - \sigma \sqrt{T} = 0.2475 - 0.2121 = 0.0354$$
    Tra bảng chuẩn: $N(d_1) = N(0.2475) \approx 0.597734$; $N(d_2) = N(0.0354) \approx 0.514102$.
    $$C_0 = 90(0.597734) - 87.3401(0.514102) = 53.7961 - 44.9017 = \mathbf{\$8.89}$$
  - (b) **Danh Mục Sao Chép**:
    - Thành phần cổ phiếu: Mua $\Delta = N(d_1) \approx \mathbf{0.597734\ \text{cổ phiếu}}$. Số tiền mua $= 0.597734 \times 90 = \mathbf{\$53.80}$.
    - Thành phần tiền mặt: Đi vay ngân hàng số tiền $PV(K) N(d_2) = \mathbf{\$44.90}$ tại lãi suất $r=6\%$.
    - Chi phí vốn tự có ròng hôm nay $= 53.80 - 44.90 = \mathbf{\$8.89}$ (Đúng bằng giá Call!).

---

### 2.3.3. Giải Chi Tiết Toàn Bộ Questions 26 – 40 (Practice L08-L11)

#### Question 26 (Easy): Sao Chép Quyền Chọn 1 Thời Kỳ
- **Đề bài**: Cổ phiếu Omicron giá $S_0 = 72$ USD. Sau 9 tháng ($T=0.75$), giá sẽ là 90 USD hoặc 60 USD. Call strike $K=76$. Lãi suất $EAR = 8\%$.
  - (a) Xác định vị thế cổ phiếu và tiền mặt sao chép 1 Call. Vị thế tiền mặt là vay hay cho vay?
  - (b) Tính giá trị Call và kiểm tra payoff của danh mục sao chép ở cả hai trạng thái.
- **Lời giải chi tiết**:
  - (a) Hệ số tăng giảm và lãi suất:
    $$u = 90 / 72 = 1.25, \quad d = 60 / 72 = 0.833333$$
    $$R = (1 + 0.08)^{0.75} = (1.08)^{0.75} \approx 1.059419$$
    Payoff tại $T$: $C_u = \max(90 - 76, 0) = 14$ USD; $C_d = \max(60 - 76, 0) = 0$ USD.
    - Số lượng cổ phiếu:
      $$\Delta = \frac{C_u - C_d}{S_u - S_d} = \frac{14 - 0}{90 - 60} = \frac{14}{30} = \mathbf{\frac{7}{15} \approx 0.466667\ \text{cổ phiếu}}$$
    - Vị thế tiền mặt $B$:
      $$B = \frac{C_d - \Delta S_d}{R} = \frac{0 - (14/30) \times 60}{1.059419} = \frac{-28}{1.059419} \approx \mathbf{-\$26.43}$$
      Dấu âm xác nhận đây là **VỊ THẾ ĐI VAY (Borrowing)** số tiền 26.43 USD.
  - (b) **Giá trị Call & Kiểm tra Payoff**:
    $$C_0 = \Delta S_0 + B = \left(\frac{14}{30}\right) \times 72 - 26.43 = 33.60 - 26.43 = \mathbf{\$7.17}$$
    - Kiểm tra trạng thái Tăng ($S_T = 90$): Payoff $= \Delta (90) + B R = (14/30)(90) - 28 = 42 - 28 = \mathbf{14\ \text{USD}} = C_u$.
    - Kiểm tra trạng thái Giảm ($S_T = 60$): Payoff $= \Delta (60) + B R = (14/30)(60) - 28 = 28 - 28 = \mathbf{0\ \text{USD}} = C_d$.

#### Question 27 (Easy): Giá Trạng Thái Arrow-Debreu & Định Giá Put
- **Đề bài**: Cổ phiếu Pi giá 42 USD, sau 4 tháng sẽ là 54 USD hoặc 34 USD. Trái phiếu phi rủi ro giá 100 USD hôm nay trả 104 USD sau 4 tháng ($r = 1.04$). Quyền chọn Put có strike $K=44$.
  - (a) Tìm giá hôm nay của chứng khoán trả 1 USD ở trạng thái Tăng ($P_u$) và chứng khoán trả 1 USD ở trạng thái Giảm ($P_d$). Kiểm tra tổng của chúng.
  - (b) Dùng giá trạng thái để định giá Put.
- **Lời giải chi tiết**:
  - (a) $u = 54/42$, $d = 34/42$, $r = 1.04$.
    - Chứng khoán Tăng: Trả $(1, 0)$. Hệ phương trình sao chép:
      $$54\Delta + 1.04B = 1; \quad 34\Delta + 1.04B = 0 \implies 20\Delta = 1 \implies \Delta = 0.05$$
      $$B = \frac{-34(0.05)}{1.04} = \frac{-1.70}{1.04} \approx -1.634615$$
      $$\mathbf{P_u = 42(0.05) - 1.634615 = 2.10 - 1.634615 \approx \$0.4654}$$
    - Chứng khoán Giảm: Trả $(0, 1)$.
      $$54\Delta + 1.04B = 0; \quad 34\Delta + 1.04B = 1 \implies -20\Delta = 1 \implies \Delta = -0.05$$
      $$B = \frac{-54(-0.05)}{1.04} = \frac{2.70}{1.04} \approx 2.596154$$
      $$\mathbf{P_d = 42(-0.05) + 2.596154 = -2.10 + 2.596154 \approx \$0.4962}$$
    - Kiểm tra tổng:
      $$P_u + P_d = 0.465385 + 0.496154 = 0.961538 = \frac{1}{1.04} = \mathbf{\frac{1}{r}}\quad (\text{Chính xác!})$$
  - (b) **Định giá Put ($K=44$)**:
    - $P_u = \max(44 - 54, 0) = 0$ USD.
    - $P_d = \max(44 - 34, 0) = 10$ USD.
    - Giá Put:
      $$\mathbf{P_0 = P_u \times P_u + P_d \times P_d = 0(0.4654) + 10(0.4962) = \$4.96}$$

#### Question 28 (Easy): Điều Kiện No-Arbitrage Của Cây Nhị Thức
- **Đề bài**: Cổ phiếu Rho giá 80 USD. Trong 6 tháng tới, giá tăng 8% ($u=1.08$) hoặc giảm 6% ($d=0.94$). Lãi suất $EAR = 10.25\%$.
  - (a) Tính tỷ suất sinh lời phi rủi ro 6 tháng và xác suất trung lập rủi ro $p$.
  - (b) Nếu lãi suất năm sửa thành 21%, mô hình còn đảm bảo No-Arbitrage không? Nếu không, chỉ ra chiến lược kinh doanh chênh lệch giá chi phí bằng 0.
- **Lời giải chi tiết**:
  - (a) Tỷ suất sinh lời phi rủi ro 6 tháng:
    $$R = (1 + 0.1025)^{0.5} = \sqrt{1.1025} = \mathbf{1.05}$$
    Xác suất trung lập rủi ro:
    $$\mathbf{p = \frac{R - d}{u - d} = \frac{1.05 - 0.94}{1.08 - 0.94} = \frac{0.11}{0.14} \approx 0.7857\ (78.57\%)}$$
  - (b) Với $EAR = 21\% \implies R_{\text{new}} = \sqrt{1.21} = \mathbf{1.10}$:
    - Điều kiện không chênh lệch giá bắt buộc: $d < R < u$.
    - Ở đây: $R = 1.10 > u = 1.08 > d = 0.94$ $\implies$ **VI PHẠM ĐIỀU KIỆN NO-ARBITRAGE!** Lãi suất phi rủi ro sinh lời cao hơn cả kịch bản tốt nhất của cổ phiếu.
    - **Chiến lược Arbitrage (Chi phí 0)**:
      - Hôm nay ($t=0$): Bán khống 1 cổ phiếu Rho thu về 80 USD. Đem toàn bộ 80 USD gửi tiết kiệm phi rủi ro ở mức $R = 1.10$. Chi phí ròng ban đầu = **0**.
      - Sau 6 tháng ($t=0.5$): Tiền gửi ngân hàng thu về $80 \times 1.10 = \mathbf{88\ \text{USD}}$.
        - Nếu cổ phiếu Tăng ($S_T = 80 \times 1.08 = 86.4$ USD): Mua lại cổ phiếu trả nợ, lãi ròng $= 88 - 86.4 = \mathbf{+1.60\ \text{USD}}$.
        - Nếu cổ phiếu Giảm ($S_T = 80 \times 0.94 = 75.2$ USD): Mua lại cổ phiếu trả nợ, lãi ròng $= 88 - 75.2 = \mathbf{+12.80\ \text{USD}}$.
      - Dòng tiền luôn $\ge 0$ ở mọi trạng thái mà không tốn vốn ban đầu $\implies$ Pure Arbitrage!

#### Question 29 (Easy): Tính Toán Black-Scholes Cơ Bản
- **Đề bài**: Cổ phiếu Sigma giá 68 USD, Call 9 tháng ($T=0.75$) strike $K=72$, $\sigma = 26\%$, $r = 4.5\%$ liên tục.
  - (a) Tính $PV(K)$, $d_1$, $d_2$.
  - (b) Tính giá Call theo BSM. Giải thích vì sao quyền chọn có giá dương dù hiện đang Out-of-the-money.
- **Lời giải chi tiết**:
  - (a) **Tính toán**:
    $$PV(K) = 72 e^{-0.045 \times 0.75} = 72 e^{-0.03375} = 72(0.966813) \approx \mathbf{69.6105\ \text{USD}}$$
    $$\sigma \sqrt{T} = 0.26 \times \sqrt{0.75} = 0.26 \times 0.866025 = 0.225167$$
    $$d_1 = \frac{\ln(68 / 69.6105)}{0.225167} + \frac{0.225167}{2} = \frac{-0.023415}{0.225167} + 0.112583 = -0.103989 + 0.112583 = \mathbf{0.008623}$$
    $$d_2 = d_1 - \sigma \sqrt{T} = 0.008623 - 0.225167 = \mathbf{-0.216544}$$
  - (b) **Giá Call**:
    $$N(d_1) = N(0.0086) \approx 0.503440, \quad N(d_2) = N(-0.2165) \approx 0.414282$$
    $$C_0 = 68(0.503440) - 69.6105(0.414282) = 34.2339 - 28.8384 = \mathbf{\$5.40}$$
    - *Giải thích*: Giá trị nội tại hiện tại là $\max(68 - 72, 0) = 0$ (OTM). Tuy nhiên, quyền chọn có thời gian 9 tháng và cổ phiếu có độ biến động 26%. Có xác suất đáng kể là trong 9 tháng tới, giá cổ phiếu sẽ vượt qua 72 USD ($N(d_2) \approx 41.4\%$ xác suất). Quyền chọn có giá dương hoàn toàn đến từ **Giá trị Thời gian (Time Value)**.

#### Question 30 (Easy): Ước Lượng Độ Biến Động Hàng Tuần & Hóa Năm (Square-Root-of-Time Rule)
- **Đề bài**: Lợi suất log tuần của Tau: [0.020, -0.010, 0.030, -0.020, 0.010, 0.000].
  - (a) Ước lượng độ lệch chuẩn mẫu tuần ($s$) dùng mẫu số $n-1$.
  - (b) Tính độ biến động năm $\sigma_{\text{annual}}$ (52 tuần/năm) và độ lệch chuẩn lợi suất 13 tuần.
- **Lời giải chi tiết**:
  - (a) Số quan sát $n=6$. Trung bình mẫu $\bar{r} = \frac{0.020 - 0.010 + 0.030 - 0.020 + 0.010 + 0.000}{6} = \frac{0.030}{6} = 0.005$.
    Các độ lệch bình phương $(r_t - \bar{r})^2$:
    - $t=1$: $(0.020 - 0.005)^2 = 0.015^2 = 0.000225$
    - $t=2$: $(-0.010 - 0.005)^2 = (-0.015)^2 = 0.000225$
    - $t=3$: $(0.030 - 0.005)^2 = 0.025^2 = 0.000625$
    - $t=4$: $(-0.020 - 0.005)^2 = (-0.025)^2 = 0.000625$
    - $t=5$: $(0.010 - 0.005)^2 = 0.005^2 = 0.000025$
    - $t=6$: $(0.000 - 0.005)^2 = (-0.005)^2 = 0.000025$
    Tổng $= 0.001750$.
    Phương sai mẫu: $s^2 = \frac{0.001750}{6 - 1} = 0.000350$.
    Độ lệch chuẩn tuần: $\mathbf{s = \sqrt{0.000350} \approx 0.018708\ (1.871\%)}$.
  - (b) **Quy tắc Căn bậc hai Thời gian**:
    - Độ biến động năm:
      $$\mathbf{\sigma_{\text{annual}} = s \times \sqrt{52} = 0.018708 \times 7.211103 \approx 0.1349\ (13.49\%/\text{năm})}$$
    - Độ lệch chuẩn lợi suất 13 tuần:
      $$\mathbf{\sigma_{13\text{-week}} = s \times \sqrt{13} = 0.018708 \times 3.605551 \approx 0.0675\ (6.75\%)}$$

#### Question 31 (Average): Tìm Strike Price Khuyết & Định Giá Put
- **Đề bài**: Cổ phiếu Upsilon giá 64 USD, sau 1 năm là 80 USD ($u=1.25$) hoặc 48 USD ($d=0.75$). Lãi suất $r=5\%$ ($R=1.05$). Giá Call 1 năm là 10 USD.
  - (a) Khôi phục giá thực thi $K$ và kiểm tra lại payoff.
  - (b) Tính giá quyền chọn Put châu Âu tương ứng.
- **Lời giải chi tiết**:
  - (a) Xác suất trung lập rủi ro:
    $$p = \frac{1.05 - 0.75}{1.25 - 0.75} = \frac{0.30}{0.50} = 0.60, \quad 1 - p = 0.40$$
    Công thức định giá Call:
    $$C_0 = \frac{p C_u + (1-p) C_d}{R} \implies 10 = \frac{0.60 C_u + 0.40 C_d}{1.05} \implies 0.60 C_u + 0.40 C_d = 10.50$$
    Vì $C_0 = 10 > 0$, Call bắt buộc phải In-the-money ở trạng thái Tăng ($C_u > 0$).
    Giả định Call Out-of-the-money ở trạng thái Giảm ($C_d = 0$):
    $$0.60 C_u = 10.50 \implies C_u = 17.50\ \text{USD}$$
    $$C_u = S_u - K \implies 80 - K = 17.50 \implies \mathbf{K = 62.50\ \text{USD}}$$
    *Kiểm tra tính nhất quán*: Ở trạng thái Giảm, $S_d = 48 < K = 62.50 \implies C_d = \max(48 - 62.50, 0) = 0$ (Đúng như giả định ban đầu!).
  - (b) **Định giá Put bằng Put-Call Parity**:
    $$P_0 = C_0 + \frac{K}{1+r} - S_0 = 10 + \frac{62.50}{1.05} - 64 = 10 + 59.5238 - 64 = \mathbf{\$5.52}$$

#### Question 32 (Average): Cây Nhị Thức 2 Bước & Lỗi Chiết Khấu Sai Bước Nhảy
- **Đề bài**: Cổ phiếu Phi giá 96 USD. Sau mỗi quý trong 2 quý tới, giá tăng 25% ($u=1.25$) hoặc giảm 20% ($d=0.80$). Put 6 tháng strike $K=100$. Lãi suất $8\%$/năm gộp lãi theo quý ($r_{\text{quarter}} = 2\% \implies R = 1.02$).
  - (a) Xác định giá cổ phiếu tại $T$, payoff của Put, giá trị Put sau 3 tháng và giá trị Put hôm nay.
  - (b) Zeta chiết khấu nhầm bằng $(1.02)^2$ tại mỗi bước lùi và ra giá 11.152863 USD. Đánh giá sai số của Zeta.
- **Lời giải chi tiết**:
  - (a) $q = \frac{1.02 - 0.80}{1.25 - 0.80} = \frac{0.22}{0.45} = \frac{22}{45} \approx 0.488889$; $1 - q = \frac{23}{45} \approx 0.511111$.
    - Cây giá cổ phiếu tại $t=2$ (6 tháng):
      - $S_{uu} = 96(1.25)^2 = 150 \implies P_{uu} = \max(100 - 150, 0) = 0$.
      - $S_{ud} = 96(1.25)(0.80) = 96 \implies P_{ud} = \max(100 - 96, 0) = 4$.
      - $S_{dd} = 96(0.80)^2 = 61.44 \implies P_{dd} = \max(100 - 61.44, 0) = 38.56$.
    - Quy nạp lùi về $t=1$ (3 tháng):
      - $P_u = \frac{q(0) + (1-q)(4)}{1.02} = \frac{(23/45)(4)}{1.02} \approx \mathbf{2.004357\ \text{USD}}$.
      - $P_d = \frac{q(4) + (1-q)(38.56)}{1.02} = \frac{(22/45)(4) + (23/45)(38.56)}{1.02} \approx \mathbf{21.239216\ \text{USD}}$.
    - Quy nạp lùi về $t=0$:
      - $P_0 = \frac{q P_u + (1-q) P_d}{1.02} = \frac{(22/45)(2.004357) + (23/45)(21.239216)}{1.02} \approx \mathbf{\$11.603438}$.
  - (b) **Đánh giá sai lầm của Zeta**:
    - Mỗi bước của cây đại diện cho **1 quý (3 tháng)**, hệ số chiết khấu đúng phải là $1.02$. Zeta lại chiết khấu bằng $(1.02)^2 = 1.0404$ (tương đương 6 tháng) tại **mỗi bước đơn lẻ**, dẫn đến việc chiết khấu thành 4 quý (1 năm) thay vì 2 quý!
    - Sai số tuyệt đối $= 11.152863 - 11.603438 = \mathbf{-\$0.450575}$.
    - Sai số tương đối $= \frac{-0.450575}{11.603438} = \mathbf{-3.88\%}$ (Định giá thấp quyền chọn Put).

#### Question 33 (Average): Mô Hình Cây Cộng Tính (Varying Up Probabilities)
- **Đề bài**: Cổ phiếu Chi giá 40 USD. Trong mỗi năm của 2 năm tới, giá tăng 12 USD hoặc giảm 8 USD. Lãi suất $EAR = 10\%$ ($R=1.10$). Put 2 năm strike $K=48$.
  - (a) Tính xác suất trung lập rủi ro tại gốc và tại từng nút 1 năm, sau đó định giá Put.
  - (b) Psi dùng xác suất tại gốc cho mọi nút. Tính giá của Psi và giải thích nguyên nhân sai lệch.
- **Lời giải chi tiết**:
  - (a) Cây giá cổ phiếu:
    - $S_0 = 40 \implies S_u = 52, S_d = 32$.
    - Từ $S_u = 52 \implies S_{uu} = 64, S_{ud} = 44$.
    - Từ $S_d = 32 \implies S_{du} = 44, S_{dd} = 24$.
    Payoff tại $T=2$: $P_{uu} = 0, P_{ud} = 4, P_{du} = 4, P_{dd} = 24$.
    - *Xác suất tại gốc*: $u_0 = 52/40 = 1.30, d_0 = 32/40 = 0.80 \implies \mathbf{p_0 = \frac{1.10 - 0.80}{1.30 - 0.80} = 0.60}$.
    - *Xác suất tại nút $u$ ($S_u=52$)*: $u_u = 64/52 \approx 1.2308, d_u = 44/52 \approx 0.8462$.
      $$\mathbf{p_u = \frac{1.10 - 44/52}{20/52} = \frac{57.2 - 44}{20} = 0.66}$$
      $$P_u = \frac{0.66(0) + 0.34(4)}{1.10} = \frac{1.36}{1.10} \approx 1.236364\ \text{USD}$$
    - *Xác suất tại nút $d$ ($S_d=32$)*: $u_d = 44/32 = 1.375, d_d = 24/32 = 0.75$.
      $$\mathbf{p_d = \frac{1.10 - 0.75}{1.375 - 0.75} = \frac{0.35}{0.625} = 0.56}$$
      $$P_d = \frac{0.56(4) + 0.44(24)}{1.10} = \frac{2.24 + 10.56}{1.10} = \frac{12.80}{1.10} \approx 11.636364\ \text{USD}$$
    - Giá Put tại $t=0$:
      $$\mathbf{P_0 = \frac{0.60(1.236364) + 0.40(11.636364)}{1.10} = \frac{0.741818 + 4.654545}{1.10} = \frac{5.396364}{1.10} \approx \$4.91}$$
  - (b) **Định giá của Psi (áp dụng $p=0.60$ cho toàn bộ các nút)**:
    - $P_u' = \frac{0.60(0) + 0.40(4)}{1.10} = \frac{1.60}{1.10} \approx 1.454545$.
    - $P_d' = \frac{0.60(4) + 0.40(24)}{1.10} = \frac{2.40 + 9.60}{1.10} = \frac{12.00}{1.10} \approx 10.909091$.
    - $P_0' = \frac{0.60(1.454545) + 0.40(10.909091)}{1.10} = \frac{0.872727 + 4.363636}{1.10} = \frac{5.236364}{1.10} \approx \mathbf{\$4.76}$.
    - *Giải thích*: Mô hình cộng tính (+12, -8) làm cho tỷ suất sinh lời phần trăm thay đổi tùy theo mức giá khởi điểm của từng nút ($12/52 \ne 12/32$). Do đó, tỷ lệ tăng trưởng và xác suất trung lập rủi ro bắt buộc phải phụ thuộc vào nút (node-dependent). Giả định xác suất không đổi của Psi là sai về mặt toán học.

#### Question 34 (Average): BSM Put, Put-Call Parity & Đánh Giá Tuyên Bố Arbitrage
- **Đề bài**: Cổ phiếu Omega giá 60 USD, Put 1 năm strike $K=75$, $\sigma = 15\%$, $r=8\%$ liên tục.
  - (a) Tính giá Put theo BSM và kiểm tra bằng Put-Call Parity.
  - (b) Một nhà phân tích cho rằng nếu giá Put dưới 15 USD thì có cơ hội Arbitrage thực thi ngay. Đánh giá tuyên bố này đối với quyền chọn châu Âu và quyền chọn Mỹ.
- **Lời giải chi tiết**:
  - (a) **Tính toán BSM**:
    $$PV(K) = 75 e^{-0.08} \approx 69.233726\ \text{USD}$$
    $$d_1 = \frac{\ln(60/75) + (0.08 + 0.0225/2)}{0.15} = \frac{-0.223144 + 0.091250}{0.15} = \frac{-0.131894}{0.15} \approx -0.879290$$
    $$d_2 = d_1 - 0.15 = -1.029290$$
    $$N(d_1) \approx 0.189622, \quad N(d_2) \approx 0.151672$$
    $$N(-d_1) = 1 - 0.189622 = 0.810378, \quad N(-d_2) = 1 - 0.151672 = 0.848328$$
    $$P_0 = PV(K) N(-d_2) - S_0 N(-d_1) = 69.233726(0.848328) - 60(0.810378) = 58.7329 - 48.6227 = \mathbf{\$10.11}$$
    - Giá Call tương ứng: $C_0 = 60(0.189622) - 69.233726(0.151672) = 11.3773 - 10.5008 = \$0.88$.
    - Put-Call Parity: $P_0 = C_0 - S_0 + PV(K) = 0.88 - 60 + 69.23 = \mathbf{\$10.11}$ (Khớp 100%).
  - (b) **Đánh giá tuyên bố Arbitrage**:
    - Giá trị nội tại hiện tại là $K - S_0 = 75 - 60 = \mathbf{15\ \text{USD}}$.
    - **Với European Put**: Tuyên bố của nhà phân tích là **SAI**. Quyền chọn châu Âu không được phép thực thi trước hạn. Cận dưới của Put châu Âu không phải là $K - S_0$ mà là $PV(K) - S_0 = 69.23 - 60 = 9.23$ USD. Vì $10.11 > 9.23$, mức giá 10.11 USD hoàn toàn hợp lý và **KHÔNG HỀ CÓ ARBITRAGE**.
    - **Với American Put**: Tuyên bố **ĐÚNG**. Quyền chọn Mỹ có quyền thực thi bất kỳ lúc nào. Nếu giá American Put $< 15$ USD, nhà đầu tư mua Put và thực thi ngay lập tức để thu về $75 - 60 = 15$ USD, kiếm lợi nhuận chênh lệch giá tức thì.

#### Question 35 (Average): Tái Cân Bằng Danh Mục Sao Chép & Gamma Risk
- **Đề bài**: Cổ phiếu Alpha giá 84 USD, Call 6 tháng strike 86 USD, $\sigma = 25\%$, $r=4\%$ liên tục. Hợp đồng gồm 100 cổ phiếu.
  - (a) Định giá hợp đồng và xác định số cổ phiếu và tiền mặt cần giữ ban đầu để sao chép vị thế Long Call.
  - (b) Giá cổ phiếu tăng ngay lập tức lên 90 USD (không có thời gian trôi qua). So sánh giá trị danh mục sao chép chưa tái cân bằng với giá thị trường mới của quyền chọn Call. Giải thích nguyên nhân chênh lệch.
- **Lời giải chi tiết**:
  - (a) **Định giá Call ban đầu ($S_0 = 84$)**:
    $$PV(K) = 86 e^{-0.04 \times 0.5} \approx 84.297086\ \text{USD}$$
    $$\sigma \sqrt{T} = 0.25 \sqrt{0.5} \approx 0.176777$$
    $$d_1 \approx 0.068417 \implies N(d_1) \approx 0.527273; \quad d_2 \approx -0.108360 \implies N(d_2) \approx 0.456855$$
    $$C_0 = 84(0.527273) - 84.297086(0.456855) = 44.2909 - 38.5116 = 5.779384\ \text{USD/cổ phiếu}$$
    - Giá trị hợp đồng (100 cổ phiếu) $= \mathbf{\$577.94}$.
    - **Danh mục sao chép**: Mua $\Delta \times 100 = \mathbf{52.73\ \text{cổ phiếu}}$ (giá trị $52.73 \times 84 = \$4,429.09$) và Vay ngân hàng số tiền $\mathbf{\$3,851.16}$.
  - (b) **Khi giá cổ phiếu tăng lên 90 USD**:
    - Giá trị danh mục sao chép chưa tái cân bằng:
      $$V_{\text{port}} = 52.7273 \times 90 - 3,851.16 = 4,745.46 - 3,851.16 = \mathbf{\$894.30}$$
    - Định giá lại quyền chọn Call tại $S = 90$:
      $$d_1 = \frac{\ln(90/86) + (0.04 + 0.03125) \times 0.5}{0.176777} \approx 0.4589 \implies N(d_1) \approx 0.6768$$
      $$d_2 = 0.2821 \implies N(d_2) \approx 0.6111$$
      $$C_{\text{new}} = 90(0.6768) - 84.2971(0.6111) \approx 9.4043\ \text{USD/cổ phiếu} \implies \text{Hợp đồng} = \mathbf{\$940.43}$$
    - **Chênh lệch**: Hợp đồng Call có giá trị cao hơn danh mục sao chép là $940.43 - 894.30 = \mathbf{\$46.13}$.
    - *Nguyên nhân kinh tế*: Danh mục sao chép là một **đường tiếp tuyến tuyến tính** tại điểm $S = 84$. Trong khi đó, đường giá quyền chọn Call là một **đường cong lồi (convex curve)** do có hệ số **Gamma dương ($\Gamma > 0$)**. Khi giá cổ phiếu tăng mạnh, hệ số Delta thực tế tăng từ $0.53$ lên $0.68$, nhưng danh mục chưa tái cân bằng chỉ giữ cố định $52.73$ cổ phiếu, do đó bị tụt lại phía sau đường cong của quyền chọn.

#### Question 36 (Average): Nội Suy Biến Động Ngụ Ý (Implied Volatility)
- **Đề bài**: Cổ phiếu Beta giá 100 USD, Call 1 năm strike 100 USD giao dịch ở giá 10.40 USD. Lãi suất liên tục $r=3\%$. Bảng giá BSM:
  - $\sigma = 18\% \implies C = 8.640660$ USD
  - $\sigma = 20\% \implies C = 9.413403$ USD
  - $\sigma = 25\% \implies C = 11.348477$ USD
  - $\sigma = 30\% \implies C = 13.283308$ USD
  - (a) Xác định khoảng chứa Implied Volatility và ước lượng bằng nội suy tuyến tính.
  - (b) Độ biến động lịch sử là 18%. Chênh lệch giá thị trường so với ước lượng lịch sử có đảm bảo bán Call là có lãi không?
- **Lời giải chi tiết**:
  - (a) Giá thị trường là 10.40 USD, nằm giữa 9.413403 ($\sigma = 20\%$) và 11.348477 ($\sigma = 25\%$).
    - Khoảng chứa Implied Volatility: $\mathbf{[20\%, 25\%]}$.
    - Nội suy tuyến tính:
      $$\sigma_{\text{implied}} \approx 0.20 + (0.25 - 0.20) \times \frac{10.40 - 9.413403}{11.348477 - 9.413403} = 0.20 + 0.05 \times \frac{0.986597}{1.935074} \approx 0.20 + 0.025492 = \mathbf{22.55\%}$$
  - (b) Với $\sigma_{\text{hist}} = 18\%$, giá trị lý thuyết là 8.64 USD. Thị trường đang định giá 10.40 USD, cao hơn 1.76 USD.
    - Việc bán Call **KHÔNG ĐẢM BẢO CHẮC CHẮN CÓ LÃI (No guaranteed profit)**. Độ biến động lịch sử phản ánh quá khứ, trong khi Implied Volatility phản ánh kỳ vọng của thị trường về tương lai. Nếu trong năm tới cổ phiếu thực sự biến động mạnh (ví dụ biến động thực tế đạt 26%), quyền chọn sẽ có giá trị cao hơn và người bán khống Call sẽ chịu lỗ nặng.

#### Question 37 (Average): Phân Biệt Xác Suất Trung Lập Rủi Ro vs Xác Suất Thực Tế
- **Đề bài**: Cây 1 năm: $S_0=50$, $S_u=65$, $S_d=40$, $r=4\%$. Xác suất trung lập rủi ro $p = 48\%$. Mô hình dự báo đưa ra xác suất trạng thái Tăng trong thực tế là 60%. Đánh giá 2 nhận định:
  - (a) "Dự báo chắc chắn sai vì điều kiện không chênh lệch giá cố định xác suất thực tế của trạng thái Tăng ở mức 48%."
  - (b) "Cổ phiếu khác có Call 1 năm với biến động ngụ ý 28%, nên biến động thực tế trong năm tới sẽ là 28%."
- **Lời giải chi tiết**:
  - (a) Nhận định này **HOÀN TOÀN SAI**.
    - Xác suất trung lập rủi ro $p = 48\%$ là một công cụ toán học nhân tạo dùng để định giá phái sinh, được tính toán từ nguyên lý No-Arbitrage sao cho tỷ suất sinh lời kỳ vọng bằng lãi suất phi rủi ro: $E^Q(S_T) = S_0 (1+r_f)$.
    - Trong thế giới thực, nhà đầu tư ngại rủi ro (Risk-averse) đòi hỏi phần bù rủi ro vốn chủ sở hữu (Equity Risk Premium) dương, tức là $E^P(S_T) > S_0(1+r_f)$. Do đó, xác suất thực tế $P(\text{Up}) = 60\%$ lớn hơn $p = 48\%$ là hoàn toàn bình thường và phù hợp với lý thuyết kinh tế tài chính!
  - (b) Nhận định này **SAI**.
    - Implied Volatility (28%) là kỳ vọng bình quân của thị trường tại thời điểm hiện tại dựa trên mô hình BSM. Nó chứa đựng cả phần bù rủi ro biến động (Variance Risk Premium).
    - Biến động thực tế (Realized Volatility) trong năm tới sẽ phụ thuộc vào các thông tin và cú sốc kinh tế thực tế diễn ra trong tương lai, có thể cao hơn hoặc thấp hơn 28%.

#### Question 38 (Hard): Chính Sách Thực Thi Quyền Chọn Mỹ Sai Lầm & Đo Lường Tổn Thất
- **Đề bài**: Cổ phiếu Delta giá 60 USD. Sau mỗi năm trong 2 năm tới, giá tăng 25% ($u=1.25$) hoặc giảm 20% ($d=0.80$). Lãi suất $EAR = 2\%$ ($R=1.02$). Put Mỹ strike $K=76$ kỳ hạn 2 năm.
  - Epsilon đề xuất: "Hôm nay không thực thi. Tại cuối năm 1, cứ thấy In-the-money là thực thi ngay; nếu không thì giữ đến đáo hạn."
  - (a) Tính giá trị hiện tại của dòng tiền tạo ra từ chính sách của Epsilon.
  - (b) Xác định quyết định thực thi tối ưu tại mọi nút và giá trị đúng của Put Mỹ. Tính giá Put châu Âu và tổn thất giá trị do chính sách sai lầm của Epsilon gây ra.
  - (c) Tính giá Call châu Âu tương ứng. So sánh với giá Call tính từ việc đưa giá Put Mỹ vào công thức Put-Call Parity châu Âu và giải thích.
- **Lời giải chi tiết**:
  - $q = \frac{1.02 - 0.80}{1.25 - 0.80} = \frac{0.22}{0.45} = \frac{22}{45} \approx 0.488889$.
  - Cây giá cổ phiếu:
    - $t=1$: $S_u = 75, S_d = 48$.
    - $t=2$: $S_{uu} = 93.75 (P=0), S_{ud} = 60 (P=16), S_{dd} = 38.4 (P=37.6)$.
  - **Giá trị tiếp tục giữ (Continuation Value)** tại $t=1$:
    - Tại nút $u$ ($S_u = 75$): $V_u^{\text{cont}} = \frac{q(0) + (1-q)(16)}{1.02} = \frac{(23/45)(16)}{1.02} \approx \mathbf{8.0174\ \text{USD}}$.
      - Giá trị nội tại $= \max(76 - 75, 0) = \mathbf{1.00\ \text{USD}}$.
    - Tại nút $d$ ($S_d = 48$): $V_d^{\text{cont}} = \frac{q(16) + (1-q)(37.6)}{1.02} = \frac{(22/45)(16) + (23/45)(37.6)}{1.02} \approx \mathbf{26.5098\ \text{USD}}$.
      - Giá trị nội tại $= 76 - 48 = \mathbf{28.00\ \text{USD}}$.
  - (a) **Chính sách của Epsilon**:
    - Tại nút $u$: Thấy $S_u = 75 < 76$ (In-the-money), Epsilon dại dột **thực thi ngay** để nhận 1 USD (bỏ phí giá trị tiếp tục giữ lên tới 8.02 USD!).
    - Tại nút $d$: Epsilon thực thi nhận 28 USD.
    - Giá trị của chính sách Epsilon tại $t=0$:
      $$V_{\text{Epsilon}} = \frac{q(1.00) + (1-q)(28.00)}{1.02} = \frac{(22/45)(1) + (23/45)(28)}{1.02} = \frac{0.4889 + 14.3111}{1.02} = \frac{14.80}{1.02} \approx \mathbf{\$14.5098}$$
  - (b) **Quyết Định Tối Ưu & Định Giá American Put**:
    - Tại nút $u$: So sánh Nội tại (1.00) vs Tiếp tục giữ (8.02) $\implies$ **GIỮ TIẾP (Hold)**! Giá trị tại nút $u = \mathbf{8.0174\ \text{USD}}$.
    - Tại nút $d$: So sánh Nội tại (28.00) vs Tiếp tục giữ (26.51) $\implies$ **THỰC THI NGAY (Exercise)**! Giá trị tại nút $d = \mathbf{28.00\ \text{USD}}$.
    - Tại gốc $t=0$: Giá trị tiếp tục giữ:
      $$H_0 = \frac{q(8.0174) + (1-q)(28.00)}{1.02} = \frac{3.9196 + 14.3111}{1.02} = \frac{18.2307}{1.02} \approx \mathbf{17.8733\ \text{USD}}$$
      Giá trị nội tại tại $t=0 = 76 - 60 = 16.00 < 17.87 \implies$ **GIỮ TIẾP (Hold)**.
    - Giá Put Mỹ: $\mathbf{P_A = \$17.8733}$.
    - Giá Put châu Âu (không được thực thi sớm tại nút $d$):
      $$P_E = \frac{q(8.0174) + (1-q)(26.5098)}{1.02} \approx \mathbf{\$17.1266}$$
    - **Tổn thất do chính sách của Epsilon**:
      $$\text{Tổn thất} = P_A - V_{\text{Epsilon}} = 17.8733 - 14.5098 = \mathbf{\$3.3635}$$
  - (c) **Định Giá Call Châu Âu & Bẫy Put-Call Parity**:
    - Giá Call châu Âu: Tại $t=2$, chỉ có $C_{uu} = 93.75 - 76 = 17.75$.
      $$C_u = \frac{q(17.75)}{1.02} \approx 8.5076; \quad C_0 = \frac{q(8.5076)}{1.02} \approx \mathbf{\$4.0777}$$
    - Nếu lắp $P_A$ vào công thức Parity châu Âu:
      $$C_{\text{pseudo}} = P_A + S_0 - \frac{K}{(1+r)^2} = 17.8733 + 60 - \frac{76}{(1.02)^2} = 77.8733 - 73.0488 = \mathbf{\$4.8245}$$
    - Chênh lệch $= 4.8245 - 4.0777 = \mathbf{\$0.7467}$.
    - *Giải thích*: Put-Call Parity đẳng thức $C - P = S_0 - PV(K)$ **CHỈ ĐÚNG CHO QUYỀN CHỌN CHÂU ÂU**. Quyền chọn Mỹ có thêm đặc quyền thực thi sớm nên $P_A > P_E$. Chênh lệch đúng bằng phần bù thực thi sớm của Put Mỹ ($P_A - P_E = 17.8733 - 17.1266 = 0.7467$ USD).

#### Question 39 (Hard): Phòng Ngừa Rủi Ro Động (Dynamic Delta Hedging Rebalancing)
- **Đề bài**: Zeta bán khống 1 Call châu Âu. Cổ phiếu giá 80 USD, strike 82 USD, kỳ hạn 1 năm gồm 2 bước 6 tháng. $u=1.20, d=0.90$. Lãi suất $6\%$/năm gộp lãi bán niên ($r_{\text{semi}} = 3\% \implies R = 1.03$).
  - (a) Tính giá Call $C_0$ và vị thế cổ phiếu $\Delta_0$, tiền mặt $B_0$ cần thiết ban đầu để phòng ngừa.
  - (b) Tại từng nút 6 tháng, tính vị thế tái cân bằng $\Delta_1, B_1$. Chứng minh giao dịch tự cấp vốn (không cần nộp thêm tiền mặt bên ngoài).
  - (c) Kiểm tra danh mục tái cân bằng thanh toán đủ payoff tại mọi kịch bản ở $T=1$. Chứng minh bằng số nếu giữ nguyên vị thế ban đầu (Static hedge) sẽ thất bại nặng nề.
- **Lời giải chi tiết**:
  - $q = \frac{1.03 - 0.90}{1.20 - 0.90} = \frac{0.13}{0.30} = \frac{13}{30} \approx 0.433333; \quad 1 - q = \frac{17}{30} \approx 0.566667$.
  - Cây cổ phiếu: $S_0 = 80 \implies S_u = 96, S_d = 72$.
    - $S_{uu} = 115.2 \implies C_{uu} = 115.2 - 82 = 33.2$.
    - $S_{ud} = 86.4 \implies C_{ud} = 86.4 - 82 = 4.4$.
    - $S_{dd} = 64.8 \implies C_{dd} = 0$.
  - (a) **Định giá Call & Vị thế Ban đầu**:
    - $C_u = \frac{(13/30)(33.2) + (17/30)(4.4)}{1.03} \approx \mathbf{16.388350\ \text{USD}}$.
    - $C_d = \frac{(13/30)(4.4) + 0}{1.03} \approx \mathbf{1.851133\ \text{USD}}$.
    - $C_0 = \frac{(13/30)(16.388350) + (17/30)(1.851133)}{1.03} \approx \mathbf{\$7.913197}$.
    - **Delta ban đầu**:
      $$\mathbf{\Delta_0 = \frac{C_u - C_d}{S_u - S_d} = \frac{16.388350 - 1.851133}{96 - 72} = \frac{14.537217}{24} \approx 0.605717\ \text{cổ phiếu}}$$
    - Giá trị cổ phiếu mua $= 0.605717 \times 80 = 48.457390$ USD.
    - Dùng tiền bán Call thu về 7.913197 USD $\implies$ Vay thêm tiền mặt:
      $$\mathbf{B_0 = 7.913197 - 48.457390 = -\$40.544192}$$
  - (b) **Tái Cân Bằng Tại $t=1$ (Sau 6 tháng)**:
    - *Kịch bản Tăng (Nút $u$, $S_u = 96$)*:
      - Giá trị danh mục trước tái cân bằng:
        $$V_u = \Delta_0 S_u + B_0 R = 0.605717(96) - 40.544192(1.03) = 58.148867 - 41.760518 = \mathbf{16.388350\ \text{USD}} = C_u$$
      - Delta mới cần có:
        $$\Delta_u = \frac{C_{uu} - C_{ud}}{S_{uu} - S_{ud}} = \frac{33.2 - 4.4}{115.2 - 86.4} = \frac{28.8}{28.8} = \mathbf{1.000000\ \text{cổ phiếu}}$$
      - Cần mua thêm: $1.00 - 0.605717 = \mathbf{0.394283\ \text{cổ phiếu}}$.
      - Chi phí mua thêm $= 0.394283 \times 96 = \mathbf{37.851132\ \text{USD}}$.
      - Vay thêm tiền mặt: Khoản nợ mới $= -41.760518 - 37.851132 = \mathbf{-\$79.611650} = B_u$.
      - *Kiểm tra tự cấp vốn*: Giá trị danh mục sau giao dịch $= 1.00(96) - 79.611650 = 16.388350$ USD (Đúng bằng trước giao dịch, không cần nạp tiền ngoài!).
    - *Kịch bản Giảm (Nút $d$, $S_d = 72$)*:
      - Giá trị danh mục trước tái cân bằng:
        $$V_d = \Delta_0 S_d + B_0 R = 0.605717(72) - 41.760518 = 43.611650 - 41.760518 = \mathbf{1.851133\ \text{USD}} = C_d$$
      - Delta mới cần có:
        $$\Delta_d = \frac{C_{ud} - C_{dd}}{S_{ud} - S_{dd}} = \frac{4.4 - 0}{86.4 - 64.8} = \frac{4.4}{21.6} \approx \mathbf{0.203704\ \text{cổ phiếu}}$$
      - Cần bán bớt: $0.605717 - 0.203704 = \mathbf{0.402014\ \text{cổ phiếu}}$.
      - Tiền thu về $= 0.402014 \times 72 = \mathbf{28.944984\ \text{USD}}$.
      - Đem trả bớt nợ: Nợ còn lại $= -41.760518 + 28.944984 = \mathbf{-\$12.815534} = B_d$.
  - (c) **Kiểm Tra Thanh Toán Tại $T=1$ & Thất Bại của Static Hedge**:
    - *Danh mục tái cân bằng (Dynamic Hedge)*:
      - Đường $uu$: $1.00(115.2) - 79.611650(1.03) = 115.2 - 82.00 = \mathbf{33.20\ \text{USD}} = C_{uu}$.
      - Đường $ud$: $1.00(86.4) - 82.00 = \mathbf{4.40\ \text{USD}} = C_{ud}$.
      - Đường $du$: $0.203704(86.4) - 12.815534(1.03) = 17.60 - 13.20 = \mathbf{4.40\ \text{USD}} = C_{du}$.
      - Đường $dd$: $0.203704(64.8) - 13.20 = 13.20 - 13.20 = \mathbf{0.00\ \text{USD}} = C_{dd}$.
      $\implies$ Khớp hoàn hảo 100% ở mọi kịch bản!
    - *Nếu giữ nguyên vị thế ban đầu (Static Hedge - không tái cân bằng)*:
      - Khoản nợ sau 1 năm nở thành: $40.544192 \times (1.03)^2 = \mathbf{43.013334\ \text{USD}}$.
      - Nếu kịch bản $uu$ xảy ra ($S_T = 115.2$):
        $$\text{Giá trị danh mục} = 0.605717(115.2) - 43.013334 = 69.7786 - 43.0133 = \mathbf{26.77\ \text{USD}}$$
        Trong khi nghĩa vụ phải trả cho người mua Call là $\mathbf{33.20\ \text{USD}}$.
        $\implies$ **THIẾU HỤT NGHIÊM TRỌNG: $26.77 - 33.20 = -6.43\ \text{USD/cổ phiếu}$!** Thất bại hoàn toàn trong việc phòng ngừa.

#### Question 40 (Hard): Đòn Bẩy Quyền Chọn, Option Beta & Cấu Trúc Danh Mục
- **Đề bài**: Cổ phiếu Eta giá $S=100$ USD, $\beta_S = 1.25$. Put châu Âu giá $P=10$ USD, $\Delta_P = -0.40$.
  - Theta có 100,000 USD để phân bổ vào: Cổ phiếu Eta, Put và Tiền mặt phi rủi ro.
  - Ràng buộc: Đúng 20,000 USD phải để ở tiền mặt; không bán khống, không vay nợ; số lượng hợp đồng Put không vượt quá số cổ phiếu ($N_P \le N_S$).
  - (a) Tính tỷ số đòn bẩy có dấu và Beta của quyền chọn Put.
  - (b) Xác định số lượng cổ phiếu và quyền chọn Put để đạt Beta danh mục hiện tại là 0.60.
  - (c) Theta có thể đạt Beta bằng 0.50 không? Chứng minh bằng số.
  - (d) Tính tỷ suất sinh lời kỳ vọng CAPM tức thời của danh mục ở câu (b) với $r_f = 3\%$/năm, $E(r_M) = 9\%$/năm.
- **Lời giải chi tiết**:
  - (a) **Đòn bẩy & Beta của Put**:
    - Tỷ số đòn bẩy có dấu:
      $$\mathbf{\Omega_P = \frac{S_0 \Delta_P}{P_0} = \frac{100 \times (-0.40)}{10} = -4.00}$$
    - Beta của quyền chọn Put:
      $$\mathbf{\beta_P = \Omega_P \times \beta_S = (-4.00) \times 1.25 = -5.00}$$
  - (b) **Xác định tỷ trọng cho $\beta_{\text{portfolio}} = 0.60$**:
    - Tổng vốn 100,000 USD. Tiền mặt cố định 20,000 USD $\implies w_{\text{cash}} = 0.20$ ($\beta_{\text{cash}} = 0$).
    - Số tiền đầu tư vào cổ phiếu và Put là 80,000 USD $\implies w_S + w_P = 0.80 \implies w_P = 0.80 - w_S$.
    - Beta danh mục:
      $$\beta_{\text{port}} = w_S \beta_S + w_P \beta_P + w_{\text{cash}} \beta_{\text{cash}}$$
      $$0.60 = w_S (1.25) + (0.80 - w_S)(-5.00) + 0 = 1.25 w_S - 4.00 + 5.00 w_S = 6.25 w_S - 4.00$$
      $$6.25 w_S = 4.60 \implies \mathbf{w_S = \frac{4.60}{6.25} = 0.736\ (73.6\%)}$$
      $$\mathbf{w_P = 0.80 - 0.736 = 0.064\ (6.4\%)}$$
    - Số tiền phân bổ:
      - Cổ phiếu: $0.736 \times 100,000 = \mathbf{\$73,600} \implies N_S = \frac{73,600}{100} = \mathbf{736\ \text{cổ phiếu}}$.
      - Quyền chọn Put: $0.064 \times 100,000 = \mathbf{\$6,400} \implies N_P = \frac{6,400}{10} = \mathbf{640\ \text{quyền chọn Put}}$.
    - *Kiểm tra các ràng buộc*:
      - $N_P = 640 \le N_S = 736$ $\implies$ **THỎA MÃN!**
      - $w_S, w_P \ge 0$, không vay nợ $\implies$ **THỎA MÃN!**
  - (c) **Kiểm tra khả năng đạt $\beta = 0.50$**:
    $$0.50 = 6.25 w_S - 4.00 \implies 6.25 w_S = 4.50 \implies w_S = 0.720\ (72.0\%)$$
    $$w_P = 0.80 - 0.720 = 0.080\ (8.0\%)$$
    - Số lượng tương ứng:
      - Cổ phiếu: $N_S = \frac{72,000}{100} = \mathbf{720\ \text{cổ phiếu}}$.
      - Put: $N_P = \frac{8,000}{10} = \mathbf{800\ \text{quyền chọn Put}}$.
    - So sánh ràng buộc: $N_P = 800 > N_S = 720 \implies$ **VI PHẠM RÀNG BUỘC $N_P \le N_S$!**
    - *Kết luận*: Theta **KHÔNG THỂ** đạt được Beta bằng 0.50 nếu tuân thủ đầy đủ các quy định đề bài.
  - (d) **Tỷ suất sinh lời kỳ vọng CAPM**:
    $$\mathbf{E(r_{\text{port}}) = r_f + \beta_{\text{port}} [E(r_M) - r_f] = 3.0\% + 0.60 \times (9.0\% - 3.0\%) = 3.0\% + 3.6\% = 6.60\%/\text{năm}}$$

"""

with open(out_file, "a", encoding="utf-8") as f:
    f.write(sec2_3)

print("Appended Section 2.3 (Lecture 11 & Questions 26-40) successfully!")
