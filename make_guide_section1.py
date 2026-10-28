import sys

out_file = "/media/minh/DISK/Downloads/Investments_WS2026/MASTER_EXAM_PREPARATION_ULTIMATE_GUIDE.md"

sec1 = r"""
# PHẦN 1: CHIẾN LƯỢC PHÒNG THI & 12 BẪY THI CỐT TỬ
## (EXAM SPEED-RUN & FATAL PITFALLS)

---

### 1.1. Ma trận Phân bổ Đề thi & Chiến lược Phân bổ Thời gian (Time Management)

Theo chỉ dẫn của giảng viên: **Ít nhất 40% số điểm đề thi thuộc về Chứng khoán Phái sinh (Derivatives - Lectures 09, 10, 11)**. Cấu trúc đề thi thực tế thường chia như sau:

| Khối Kiến thức | Các Bài giảng | Tỷ trọng Dự kiến | Đặc điểm Câu hỏi | Mục tiêu Thời gian (cho bài 90-120 phút) |
|---|---|:---:|---|:---:|
| **Khối 1: Derivatives (Phái sinh)** | **Lectures 09, 10, 11** | **40% – 50%** | Định giá Forwards/Futures, Swap fixed rate, Put-Call Parity, Arbitrage table, Cây nhị thức 2 thời kỳ, Black-Scholes ($d_1, d_2, N(d)$), Greeks, Option Beta | **40 – 50 phút** (Làm trước để lấy trọn vẹn điểm phần nặng nhất) |
| **Khối 2: Fixed Income (Trái phiếu)** | **Lectures 02, 03** | **25% – 30%** | Spot rate vs Forward rate, Pure Expectations vs Liquidity Premium, Macaulay/Modified Duration, Convexity xấp xỉ giá, Miễn dịch danh mục (Immunization) | **25 – 30 phút** |
| **Khối 3: Portfolio & Asset Pricing** | **Lectures 04, 05, 06, 07, 08** | **25% – 30%** | CAL & Hệ số Sharpe, Danh mục tiếp xúc Markowitz, SIM & CAPM, SML vs CML, Alpha, APT Arbitrage portfolio, EMH & Thiên lệch hành vi | **25 – 30 phút** |

#### Quy tắc Vàng khi Làm bài:
1. **Chiến thuật "Phái sinh trước - Trái phiếu kế - Lý thuyết danh mục sau"**: Làm phần Derivatives trước khi đầu óc còn tỉnh táo nhất vì các bài toán cây nhị thức và Black-Scholes đòi hỏi bấm máy nhiều bước liên tiếp.
2. **Lập bảng Dòng tiền / Arbitrage rõ ràng**: Khi đề bài hỏi *"Construct an arbitrage trade"*, bắt buộc phải kẻ bảng gồm các cột: **Hôm nay ($t=0$)**, **Dòng tiền trung gian (nếu có)**, **Thời điểm đáo hạn ($T$)** theo các kịch bản. Nếu chỉ viết lời giải thích mà không có bảng dòng tiền, giảng viên thường trừ 50% số điểm câu đó.
3. **Giữ nguyên số thập phân trên màn hình máy tính (Store Memory)**: Tuyệt đối không làm tròn số trung gian (ví dụ $d_1 = 0.2341$ làm tròn thành $0.23$ sẽ khiến $N(d_1)$ lệch rất lớn, dẫn tới giá Call/Put sai hàng chục cent). Dùng phím `STO A`, `STO B` trên máy tính Casio / BA II Plus.

---

### 1.2. 12 Bẫy Thi Kinh Điển (Top 12 Fatal Exam Pitfalls) & Cách Né Tránh

> [!CAUTION]
> Dưới đây là 12 cái "bẫy" mà hơn 80% sinh viên mất điểm trong bài thi Investments. Hãy ghi nhớ nằm lòng từng bẫy trước khi vào phòng thi!

#### Bẫy 1: Quy ước Ghép lãi (Compounding Frequency)
- **Sai lầm phổ biến**: Dùng nhầm $e^{rT}$ (ghép lãi liên tục) thay vì $(1+r)^T$ (ghép lãi rời rạc hàng năm - EAR) hoặc ngược lại.
- **Cách nhận diện**:
  - Nếu đề bài ghi *"annual effective rate"* hoặc *"compounded annually"* $\implies$ Thừa số chiết khấu là $\frac{1}{(1+r)^T}$.
  - Nếu đề bài ghi *"continuously compounded risk-free rate"* $\implies$ Thừa số chiết khấu là $e^{-rT}$ và hệ số tăng trưởng là $e^{rT}$.
  - Nếu đề bài ghi *"nominal annual rate compounded quarterly/semiannually"* với tần suất $m$ $\implies$ Lãi suất mỗi kỳ là $r/m$, số kỳ là $m \times T$, và thừa số là $(1 + r/m)^{mT}$.

#### Bẫy 2: Lãi suất Kỳ hạn (Forward Rate) vs Lãi suất Giao ngay (Spot Rate)
- **Sai lầm**: Nhầm lẫn giữa $f_{1,2}$ (lãi suất kỳ hạn 1 năm bắt đầu từ năm 1 đến năm 2) và $s_2$ (lãi suất zero-coupon 2 năm từ $t=0$ đến $t=2$).
- **Công thức chuẩn**:
  $$(1 + s_2)^2 = (1 + s_1)^1 \times (1 + f_{1,2}) \implies f_{1,2} = \frac{(1+s_2)^2}{1+s_1} - 1$$
  Nếu ghép lãi liên tục: $s_2 \times 2 = s_1 \times 1 + f_{1,2} \times 1 \implies f_{1,2} = 2 s_2 - s_1$.

#### Bẫy 3: Macaulay Duration vs Modified Duration ($D^*$ vs $D_{\text{mac}}$)
- **Sai lầm**: Đem $D_{\text{mac}}$ nhân trực tiếp với $\Delta y$ để tính phần trăm biến động giá.
- **Quy tắc chuẩn**:
  - $D_{\text{mac}}$ có đơn vị là **năm** (thời gian đáo hạn bình quân có trọng số).
  - Độ nhạy cảm giá thực sự là **Modified Duration**:
    $$D^* = \frac{D_{\text{mac}}}{1 + y/m}$$ (với $m$ là số lần trả coupon trong năm).
    Nếu ghép lãi liên tục: $D^* = D_{\text{mac}}$.
  - Phần trăm thay đổi giá theo Duration bậc 1: $\frac{\Delta P}{P} \approx -D^* \times \Delta y$.

#### Bẫy 4: Quên Hệ số $\frac{1}{2}$ trong Công thức Độ lồi (Convexity)
- **Sai lầm**: Viết $\frac{\Delta P}{P} \approx -D^* \Delta y + C (\Delta y)^2$ (thiếu số $1/2$).
- **Công thức chuẩn bậc 2**:
  $$\frac{\Delta P}{P} \approx -D^* \times \Delta y + \frac{1}{2} C \times (\Delta y)^2$$
  *Lưu ý*: Với mọi trái phiếu thông thường (straight bond), $C > 0$. Do đó, khi lãi suất tăng ($\Delta y > 0$), độ lồi giúp giá giảm ít hơn; khi lãi suất giảm ($\Delta y < 0$), độ lồi giúp giá tăng nhiều hơn!

#### Bẫy 5: Giá trị Hợp đồng Kỳ hạn ($V_t$) vs Giá Giao hàng Kỳ hạn ($F$)
- **Sai lầm**: Tưởng rằng giá trị hợp đồng kỳ hạn luôn bằng 0.
- **Bản chất**:
  - Tại ngày ký kết ($t=0$): Giá giao hàng $F_0$ được chốt sao cho **Giá trị hợp đồng bằng 0 ($V_0 = 0$)**.
  - Tại thời điểm trung gian ($t > 0$): Giá thị trường biến động, $V_t$ của vị thế Long Forward là:
    $$V_t = S_t - F_0 \times (1 + r)^{-(T-t)} \quad \text{hoặc} \quad V_t = S_t - F_0 e^{-r(T-t)} = \frac{F_t - F_0}{(1+r)^{T-t}}$$
    Đây là khoản lãi/lỗ chưa thực hiện nếu tất toán hợp đồng hôm nay!

#### Bẫy 6: Cổ tức Rời rạc vs Tỷ suất Cổ tức Liên tục trong Định giá Forward
- **Cổ tức tiền mặt rời rạc $D$ tại thời điểm $t_D$**:
  $$F_0 = (S_0 - PV(D)) \times (1 + r)^T = S_0 (1+r)^T - D \times (1+r)^{T - t_D}$$
- **Tỷ suất cổ tức liên tục $q$**:
  $$F_0 = S_0 e^{(r - q)T}$$

#### Bẫy 7: Ngang giá Mua - Bán (Put-Call Parity) & Cổ tức
- **Công thức gốc (không cổ tức)**:
  $$C + PV(K) = P + S_0 \iff C + K e^{-rT} = P + S_0$$
- **Nếu có cổ tức rời rạc $D$**: Cổ tức làm giá cổ phiếu giảm khi chốt quyền, nên tài sản cơ sở thực chất là $S_0 - PV(D)$:
  $$C + PV(K) = P + [S_0 - PV(D)]$$
- **Nếu có tỷ suất cổ tức $q$**:
  $$C + K e^{-rT} = P + S_0 e^{-qT}$$

#### Bẫy 8: Thực thi Sớm Quyền chọn Mỹ (American Option Early Exercise)
- **Đối với Call Option trên cổ phiếu KHÔNG trả cổ tức**: **KHÔNG BAO GIỜ** nên thực thi sớm! ($C_{\text{American}} = C_{\text{European}}$). Nếu muốn thoát vị thế, bán quyền chọn trên thị trường luôn thu được giá cao hơn giá trị thực thi ($C > S - K$ do giá trị thời gian luôn dương).
- **Đối với Call Option trên cổ phiếu CÓ trả cổ tức**: Chỉ nên xem xét thực thi ngay trước ngày giao dịch không hưởng quyền (ex-dividend date) nếu cổ tức lớn hơn phần lãi suất bị mất khi trả tiền mua sớm: $Div > K(1 - e^{-r\Delta t})$.
- **Đối với Put Option (cả có hay không có cổ tức)**: **CÓ THỂ** thực thi sớm tối ưu khi giá cổ phiếu rớt rất sâu về gần 0, vì giá trị tối đa nhận được là $K$ tiền mặt ngay lập tức để đem gửi tiết kiệm sinh lời thay vì chờ đến đáo hạn.

#### Bẫy 9: Xác suất Trung lập Rủi ro ($p$) trong Mô hình Nhị thức
- **Công thức chuẩn**:
  $$p = \frac{R - d}{u - d}$$
  trong đó $R = 1+r$ (nếu rời rạc) hoặc $R = e^{r\Delta t}$ (nếu liên tục), $u = 1 + \% \text{tăng}$, $d = 1 - \% \text{giảm}$.
- **Sai lầm chết người**: Dùng xác suất thực tế chủ quan của thị trường (ví dụ "nhà phân tích dự báo 60% tăng") để định giá quyền chọn. **Trong mô hình nhị thức, xác suất thực tế hoàn toàn không xuất hiện trong công thức định giá!** Giá quyền chọn chỉ phụ thuộc vào xác suất trung lập rủi ro $p$ (do được định giá bằng phương pháp sao chép loại trừ rủi ro).

#### Bẫy 10: Ý nghĩa Toán học & Kinh tế của $N(d_1)$ và $N(d_2)$ trong Black-Scholes
- **Công thức Call**: $C = S_0 N(d_1) - K e^{-rT} N(d_2)$.
- **Bản chất**:
  - $N(d_1) = \Delta_C$: Số lượng cổ phiếu cần mua trong danh mục sao chép (Hedge ratio).
  - $N(d_2)$: Xác suất quyền chọn kết thúc ở trạng thái có lãi trong thế giới trung lập rủi ro: $N(d_2) = \mathbb{P}^*(S_T > K)$.
  - $K e^{-rT} N(d_2)$: Giá trị hiện tại của số tiền trả nợ vay mua cổ phiếu có điều kiện quyền chọn được thực thi.
- **Delta của Put**: $\Delta_P = N(d_1) - 1 < 0$ (luôn mang dấu âm!).

#### Bẫy 11: Đòn bẩy Quyền chọn (Elasticity $\Omega$) và Beta Quyền chọn ($\beta_{\text{Option}}$)
- **Đòn bẩy (Elasticity / Leverage)**:
  $$\Omega = \frac{\% \Delta C}{\% \Delta S} = \frac{\Delta \times S}{C}$$
  Vì $S > C$, đòn bẩy $\Omega$ thường rất lớn (từ 3x đến 10x).
- **Option Beta**:
  $$\beta_{\text{Option}} = \Omega \times \beta_{\text{Stock}} = \left( \frac{\Delta \times S}{C} \right) \times \beta_{\text{Stock}}$$
  Quyền chọn Call luôn có rủi ro hệ thống ($\beta$) cao hơn nhiều so với cổ phiếu cơ sở!

#### Bẫy 12: Phân biệt CML (Capital Market Line) vs SML (Security Market Line)
| Tiêu chí | Capital Market Line (CML) | Security Market Line (SML) |
|---|---|---|
| **Trục hoành (Thước đo rủi ro)** | Tổng rủi ro: Độ lệch chuẩn $\sigma$ | Rủi ro hệ thống: Hệ số Beta $\beta$ |
| **Phạm vi áp dụng** | **Chỉ áp dụng cho các danh mục đầu tư hiệu quả (Efficient Portfolios)** kết hợp giữa Risk-free và Market Portfolio | **Áp dụng cho MỌI tài sản**, dù là cổ phiếu riêng lẻ, danh mục kém hiệu quả hay danh mục hiệu quả |
| **Hệ số góc (Slope)** | Hệ số Sharpe của thị trường: $\frac{E(r_M) - r_f}{\sigma_M}$ | Phần bù rủi ro thị trường (Market Risk Premium): $E(r_M) - r_f$ |
| **Tài sản định giá sai** | Nằm phía dưới đường CML (do có rủi ro riêng lẻ lãng phí) | Nằm phía trên SML = Dưới giá trị (Underpriced, $\alpha > 0$); Nằm dưới SML = Quá giá trị (Overpriced, $\alpha < 0$) |

---

### 1.3. Cẩm nang Bấm máy Siêu tốc (Formula Cheat-Sheet)

```
========================================================================================
                      BẢNG TỔNG HỢP CÔNG THỨC RÚT GỌN (CHEAT-SHEET)
========================================================================================
1. FORWARDS & FUTURES:
   - Cơ bản:                F0 = S0 * (1 + r)^T  hoặc  F0 = S0 * e^(r*T)
   - Có cổ tức rời rạc:     F0 = (S0 - PV(Div)) * (1 + r)^T
   - Tỷ suất cổ tức q:      F0 = S0 * e^((r - q)*T)
   - Chi phí kho u, tiện y: F0 = S0 * e^((r + u - y)*T)
   - Tỷ giá (CIP):          F0 = S0 * e^((r_quote - r_base)*T)
   - Giá trị tại t:         Vt = St - F0 * e^(-r*(T - t))

2. SWAPS:
   - Thanh toán ròng kỳ k:  Net = Notional * (Floating_k - Fixed) * Delta
   - Swap fixed rate K:     K = (1 - P(0, Tn)) / [sum_{i=1}^n Delta * P(0, Ti)]

3. PUT-CALL PARITY & BOUNDS:
   - Parity:                C + K * e^(-r*T) = P + S0  (hoặc C + PV(K) = P + S0)
   - Chặn dưới Call:        C >= max(0, S0 - PV(K))
   - Chặn dưới Put:         P >= max(0, PV(K) - S0)
   - Synthetic Long Stock:  S0 = C - P + PV(K)
   - Synthetic Long Bond:   PV(K) = P + S0 - C

4. CÂY NHỊ THỨC (BOPM):
   - Thừa số tăng/giảm:     u = Su / S0,   d = Sd / S0
   - Xác suất rủi ro p:     p = (e^(r*dt) - d) / (u - d)   hoặc   p = (R - d) / (u - d)
   - Tỷ lệ Hedge Delta:     Delta = (Cu - Cd) / (Su - Sd)
   - Vay/gửi B:             B = (u * Cd - d * Cu) / (R * (u - d))
   - Giá quyền chọn:        f = e^(-r*dt) * [p * fu + (1 - p) * fd]
   - State prices:          Pu = p / R,   Pd = (1 - p) / R   ==>   f = Pu * fu + Pd * fd

5. BLACK-SCHOLES-MERTON (BSM):
   - Call:                  C = S0 * N(d1) - K * e^(-r*T) * N(d2)
   - Put:                   P = K * e^(-r*T) * N(-d2) - S0 * N(-d1)
   - d1:                    d1 = [ln(S0 / K) + (r + sigma^2 / 2) * T] / (sigma * sqrt(T))
   - d2:                    d2 = d1 - sigma * sqrt(T)
   - Liên hệ chuẩn tắc:     N(-x) = 1 - N(x)
   - Delta Call:            Delta_C = N(d1) > 0;     Delta Put: Delta_P = N(d1) - 1 < 0
   - Elasticity Omega:      Omega = (Delta * S0) / C
   - Option Beta:           Beta_Option = Omega * Beta_Stock

6. FIXED INCOME:
   - Lãi suất kỳ hạn:       (1 + s_t)^t * (1 + f_{t, t+k})^k = (1 + s_{t+k})^(t+k)
   - Macaulay Duration:     D_mac = [sum_{t=1}^n t * CF_t / (1+y)^t] / Price
   - Modified Duration:     D* = D_mac / (1 + y/m)
   - Xấp xỉ giá bậc 2:      dP / P ≈ -D* * dy + 0.5 * Convexity * (dy)^2
   - Miễn dịch (Redington): PV_A = PV_L,   D_A = D_L,   Convexity_A > Convexity_L

7. PORTFOLIO & CAPM:
   - Thỏa dụng (Utility):   U = E(r) - 0.5 * A * sigma^2
   - Tỷ trọng rủi ro tối ưu:y* = (E(rp) - rf) / (A * sigma_p^2)
   - Hệ số Sharpe:          SR = (E(rp) - rf) / sigma_p
   - CAPM (SML):            E(ri) = rf + Beta_i * [E(rM) - rf]
   - Beta:                  Beta_i = Cov(ri, rM) / sigma_M^2 = (rho_{i,M} * sigma_i) / sigma_M
   - SIM Phân rã rủi ro:    sigma_i^2 = Beta_i^2 * sigma_M^2 + sigma^2(e_i)
   - Alpha Jensen:          alpha_i = ri - [rf + Beta_i * (rM - rf)]
========================================================================================
```
"""

with open(out_file, "a", encoding="utf-8") as f:
    f.write(sec1)

print("Section 1 appended successfully.")
