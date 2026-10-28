import sys

out_file = "/media/minh/DISK/Downloads/Investments_WS2026/MASTER_EXAM_PREPARATION_ULTIMATE_GUIDE.md"

sec2_1 = r"""
---

# PHẦN 2: CHỨNG KHOÁN PHÁI SINH CHUYÊN SÂU ($\ge 40\%$ ĐIỂM THI)
## (DERIVATIVES DEEP-DIVE: LECTURES 09, 10, 11)

---

## 2.1. LECTURE 09: HỢP ĐỒNG KỲ HẠN (FORWARDS), TƯƠNG LAI (FUTURES) & HOÁN ĐỔI (SWAPS)

### 2.1.1. Khung Lý Thuyết & Nguyên Lý Định Giá Không Chênh Lệch Giá (No-Arbitrage)

#### A. Khái niệm & Nguyên lý Sao chép (Replication)
1. **Hợp đồng Kỳ hạn (Forward Contract)**: Thỏa thuận riêng biệt (OTC) mua hoặc bán tài sản tại ngày tương lai $T$ với mức giá giao hàng $F_0$ cố định hôm nay.
   - **Long**: Bắt buộc mua tại $T$ $\implies$ Payoff: $S_T - F_0$.
   - **Short**: Bắt buộc bán tại $T$ $\implies$ Payoff: $F_0 - S_T$.
   - **Tính chất cốt tử**: Tại $t=0$, giá trị hợp đồng $V_0 = 0$. Không có tiền trao tay ban đầu.
2. **Chứng minh Công thức Định giá Cơ bản $F_0 = S_0 (1+r)^T$ (hoặc $S_0 e^{rT}$)**:
   - *Mục tiêu*: Muốn sở hữu 1 đơn vị tài sản tại ngày $T$.
   - *Cách 1 (Mua vật lý)*: Bỏ $S_0$ mua ngay hôm nay $\implies$ Chi phí hôm nay = $S_0$.
   - *Cách 2 (Sao chép phái sinh)*: Ký Long Forward giá $F_0$ (tốn $0) và gửi tiết kiệm $\frac{F_0}{(1+r)^T}$ vào ngân hàng. Đến ngày $T$, tiền gửi nở thành $F_0$, lấy tiền này mua tài sản.
   - Cả 2 cách cho kết quả y hệt nhau tại $T$. Theo **Quy luật Một Giá (Law of One Price)**:
     $$S_0 = \frac{F_0}{(1+r)^T} \iff F_0 = S_0 (1+r)^T$$
3. **Cơ chế Arbitrage khi Giá Lệch Chuẩn**:
   - **Nếu $F_{\text{market}} > F^*$ (Forward bị ĐẮT)** $\implies$ **Cash-and-Carry Arbitrage**:
     - Hôm nay: Vay tiền $S_0$ $\rightarrow$ Mua tài sản giao ngay $\rightarrow$ Short Forward ở giá cao $F_{\text{market}}$. Dòng tiền $t=0$ là $0$.
     - Đáo hạn $T$: Giao tài sản thu về $F_{\text{market}}$ $\rightarrow$ Trả nợ ngân hàng $S_0(1+r)^T$ $\rightarrow$ Bỏ túi lợi nhuận ròng chắc chắn: $\Pi = F_{\text{market}} - S_0(1+r)^T > 0$.
   - **Nếu $F_{\text{market}} < F^*$ (Forward bị RẺ)** $\implies$ **Reverse Cash-and-Carry Arbitrage**:
     - Hôm nay: Mượn tài sản bán khống thu $S_0$ $\rightarrow$ Đem gửi ngân hàng $S_0$ $\rightarrow$ Long Forward ở giá rẻ $F_{\text{market}}$. Dòng tiền $t=0$ là $0$.
     - Đáo hạn $T$: Rút tiền ngân hàng $S_0(1+r)^T$ $\rightarrow$ Thực hiện Long Forward trả $F_{\text{market}}$ nhận tài sản $\rightarrow$ Trả tài sản cho chủ nợ $\rightarrow$ Lợi nhuận chắc chắn: $\Pi = S_0(1+r)^T - F_{\text{market}} > 0$.

#### B. Các Biến Thể Định Giá Kỳ Hạn
1. **Có cổ tức tiền mặt rời rạc $D$ tại thời điểm $t_D$**:
   $$F_0 = (S_0 - PV(D)) (1+r)^T = S_0 (1+r)^T - D (1+r)^{T - t_D}$$
2. **Có tỷ suất cổ tức liên tục $q$**:
   $$F_0 = S_0 e^{(r - q)T}$$
3. **Hàng hóa vật chất có chi phí lưu kho ($u$) và lợi suất tiện dụng ($y$ - Convenience Yield)**:
   $$F_0 = S_0 e^{(r + u - y)T}$$
   - Nếu $y > r + u \implies F_0 < S_0$: Thị trường ở trạng thái **Bù hoãn mua (Backwardation)**.
   - Nếu $F_0 > S_0$: Thị trường ở trạng thái **Bù hoãn bán (Contango)**.
4. **Ngang giá Lãi suất có Phòng hộ (Covered Interest Parity - CIP)**:
   $$F = S_0 \times \frac{(1 + r_{\text{quote}})^T}{(1 + r_{\text{base}})^T} \quad \text{hoặc} \quad F = S_0 e^{(r_{\text{quote}} - r_{\text{base}})T}$$
   *(với tỷ giá niêm yết dạng quote/base, ví dụ USD/EUR thì quote = USD, base = EUR)*.

#### C. Hợp đồng Hoán đổi (Swaps)
- **Interest Rate Swap (IRS - Vanilla)**: Một bên trả lãi cố định (Fixed payer), một bên trả lãi thả nổi (Floating payer).
- Thanh toán ròng kỳ $k$ đối với bên trả cố định, nhận thả nổi:
  $$\text{Net Cash Flow}_k = \text{Notional} \times (L_k - K) \times \Delta t$$
- **Tỷ suất Hoán đổi Cố định $K$ (Swap Rate)**: Được xác định sao cho giá trị ban đầu của Swap bằng 0:
  $$K = \frac{1 - P(0, T_n)}{\sum_{i=1}^n \Delta t_i \times P(0, T_i)}$$

---

### 2.1.2. Giải Chi Tiết Toàn Bộ Questions 1 – 11 trong Slide Lecture 09

#### Question 1 (Lecture 09): Khám phá Giá trong Thị trường Tương lai
- **Đề bài**: Trong thị trường đồng đỏ, tất cả nhà sản xuất (Kappa) và nhà máy sản xuất cáp (Lambda) đều phòng hộ 100% sản lượng và nhu cầu mua cho 6 tháng tới bằng hợp đồng tương lai. Spot price có còn đóng vai trò kinh tế không? Thị trường nào dẫn dắt quá trình khám phá giá (Price discovery)?
- **Lời giải & Bản chất Kinh tế**:
  1. *Vai trò của Spot Price*: Vẫn còn nguyên giá trị kinh tế. Việc phòng hộ chỉ khóa mức giá cho các giao dịch cam kết trước; nó không làm cho các quyết định biên trong tương lai (tăng giảm công suất khai thác, quản lý tồn kho đột xuất, nhu cầu mới phát sinh) trở nên trơ lì với giá.
  2. *Khám phá Giá (Price Discovery)*: Thị trường tương lai (Futures) thường **dẫn dắt thị trường giao ngay** vì:
     - Tính thanh khoản cao vượt trội.
     - Chi phí giao dịch cực thấp và đòn bẩy ký quỹ cao.
     - Cho phép bán khống dễ dàng mà không cần mượn hàng vật chất. Do đó thông tin vĩ mô và kỳ vọng mới phản ánh vào giá Futures nhanh hơn giá Spot.

#### Question 2 (Lecture 09): Giá trị Hợp đồng Kỳ hạn Trung gian
- **Đề bài**: Hợp đồng Long Forward 9 tháng trên cổ phiếu Theta (không cổ tức) được ký tại giá công bằng. $S_0 = \$84$, $r = 4\%$ liên tục.
  1. Tính giá giao hàng ban đầu $K$?
  2. Sau 4 tháng, giá cổ phiếu $S_t = \$82$. Tính giá Forward mới và giá trị hợp đồng đã ký $V_t$?
- **Lời giải**:
  1. Giá giao hàng ban đầu:
     $$K = F_0 = S_0 e^{rT} = 84 e^{0.04 \times (9/12)} = 84 e^{0.03} \approx 84 \times 1.030455 = \$86.56$$
  2. Sau $t = 4$ tháng, thời gian còn lại là $T - t = 5$ tháng ($5/12$ năm):
     - Giá Forward mới niêm yết trên thị trường:
       $$F_t = S_t e^{r(T-t)} = 82 e^{0.04 \times (5/12)} = 82 e^{0.016667} \approx 82 \times 1.016806 = \$83.38$$
     - Giá trị của hợp đồng Long Forward hiện tại ($V_t$):
       $$V_t = S_t - K e^{-r(T-t)} = 82 - 86.56 e^{-0.04 \times (5/12)} = 82 - 86.56 \times 0.983471 = 82 - 85.13 = -\$3.13$$
       *Hoặc dùng công thức chênh lệch*: $V_t = (F_t - K) e^{-r(T-t)} = (83.38 - 86.56) \times 0.983471 = -3.18 \times 0.983471 \approx -\$3.13$.
       *Kết luận*: Vị thế Long Forward đang bị **lỗ \$3.13** do giá cổ phiếu giảm từ 84 xuống 82.

#### Question 3 (Lecture 09): Kỳ hạn Mua Trái phiếu Zero-Coupon
- **Đề bài**: Ký hợp đồng Forward mua trái phiếu zero-coupon kỳ hạn 4 năm sẽ được phát hành sau 3 năm nữa. Mệnh giá $2,000. Lãi suất giao ngay: $s_3 = 3\%$, $s_7 = 5\%$ (ghép lãi hàng năm). Tính giá Forward?
- **Lời giải**:
  - Trái phiếu phát hành tại $t=3$ và đáo hạn tại $t = 3 + 4 = 7$ năm.
  - Giá trị hiện tại hôm nay ($t=0$) của khoản thanh toán mệnh giá tại $t=7$:
    $$PV_0 = \frac{2,000}{(1 + s_7)^7} = \frac{2,000}{(1.05)^7} = \frac{2,000}{1.407100} \approx \$1,421.36$$
  - Giá Forward thanh toán tại $t=3$ phải tương đương giá trị hiện tại nhân với lãi suất tích lũy 3 năm:
    $$F_{0,3} = PV_0 \times (1 + s_3)^3 = \frac{2,000 \times (1.03)^3}{(1.05)^7} = 1,421.36 \times 1.092727 \approx \$1,553.16$$

#### Question 4 (Lecture 09): Forward trên Chỉ số với Cổ tức Biến đổi theo Giai đoạn
- **Đề bài**: Chỉ số Sigma $S_0 = 2,400$. Kỳ hạn 6 tháng. $r = 5\%$ liên tục. Tỷ suất cổ tức 2 tháng đầu là $q_1 = 1.5\%$, 4 tháng sau là $q_2 = 3.0\%$. Tính giá Forward?
- **Lời giải**:
  - Thời gian: $T_1 = 2/12 = 1/6$ năm; $T_2 = 4/12 = 1/3$ năm.
  - Số mũ chiết khấu ròng tích lũy:
    $$\text{Exponent} = (r - q_1) T_1 + (r - q_2) T_2 = (0.05 - 0.015)\left(\frac{2}{12}\right) + (0.05 - 0.03)\left(\frac{4}{12}\right) = 0.035 \times \frac{1}{6} + 0.020 \times \frac{1}{3} = \frac{0.035 + 0.040}{6} = \frac{0.075}{6} = 0.0125$$
  - Giá Forward:
    $$F_0 = 2,400 e^{0.0125} \approx 2,400 \times 1.012578 \approx 2,430.19\ \text{điểm chỉ số}$$

#### Question 5 (Lecture 09): Ngang giá Lãi suất Có phòng hộ (CIP) tìm Lãi suất Ẩn
- **Đề bài**: Spot $S_0 = 1.2500$ USD/GBP. Forward 1 năm $F = 1.2300$ USD/GBP. Lãi suất USD $r_{\text{USD}} = 4\%$ liên tục. Tìm lãi suất GBP ($r_{\text{GBP}}$) theo CIP?
- **Lời giải**:
  - Theo CIP: $F = S_0 e^{(r_{\text{USD}} - r_{\text{GBP}}) T}$.
  - Lấy logarit tự nhiên hai vế:
    $$\ln\left(\frac{F}{S_0}\right) = (r_{\text{USD}} - r_{\text{GBP}}) T \implies r_{\text{GBP}} = r_{\text{USD}} - \frac{\ln(F/S_0)}{T}$$
  - Thay số với $T=1$:
    $$r_{\text{GBP}} = 0.04 - \ln\left(\frac{1.23}{1.25}\right) = 0.04 - \ln(0.984) = 0.04 - (-0.016129) = 0.056129 \approx 5.61\%$$

#### Question 6 (Lecture 09): Arbitrage Vi phạm CIP
- **Đề bài**: Spot $S_0 = 1.1600$ USD/EUR. $r_{\text{USD}} = 4.5\%$, $r_{\text{EUR}} = 2.5\%$ liên tục. Kỳ hạn 6 tháng ($T=0.5$).
  - Giá lý thuyết: $F^* = 1.16 e^{(0.045 - 0.025) \times 0.5} = 1.16 e^{0.01} \approx 1.17166 \approx 1.1717$ USD/EUR.
  - (a) Nếu $F_{\text{market}} = 1.1900$ (Forward EUR bị ĐẮT): Chiến lược Arbitrage là gì?
  - (b) Nếu $F_{\text{market}} = 1.1500$ (Forward EUR bị RẺ): Chiến lược Arbitrage là gì?
- **Lời giải**:
  - **Trường hợp (a) $F = 1.1900 > 1.1717$ (Bán cái đắt, Mua cái rẻ)**:
    - Ký **Short Forward EUR** ở giá cao 1.1900.
    - Để có EUR giao hàng: Vay USD (ví dụ 400,000 USD) $\rightarrow$ Đổi sang EUR theo tỷ giá giao ngay $1.16$ được $\frac{400,000}{1.16} = 344,827.59$ EUR $\rightarrow$ Đem gửi ngân hàng EUR với lãi suất 2.5%.
    - Tại $T=0.5$: Nhận gốc và lãi EUR: $344,827.59 \times e^{0.025 \times 0.5} = 349,157.19$ EUR $\rightarrow$ Giao theo hợp đồng Short Forward thu về $349,157.19 \times 1.19 = 415,497.06$ USD $\rightarrow$ Trả nợ vay USD: $400,000 \times e^{0.045 \times 0.5} = 409,102.16$ USD $\rightarrow$ **Lợi nhuận ròng chắc chắn = 415,497.06 - 409,102.16 = +6,394.90 USD**.
  - **Trường hợp (b) $F = 1.1500 < 1.1717$ (Forward EUR bị rẻ)**:
    - Ký **Long Forward EUR** ở giá rẻ 1.1500.
    - Vay EUR $\rightarrow$ Đổi sang USD ở spot 1.16 $\rightarrow$ Gửi ngân hàng USD hưởng 4.5% $\rightarrow$ Đáo hạn nhận USD, dùng USD thực hiện hợp đồng Long Forward mua lại EUR trả nợ vay gốc và lãi. Bỏ túi lợi nhuận chênh lệch chắc chắn.

#### Question 7 (Lecture 09): Suy ra Spot từ Futures & Trái phiếu Coupon
- **Đề bài**:
  - (a) Futures chỉ số Sigma 6 tháng có giá $F = 4,200$. $r = 3\%$, $q = 1.2\%$ liên tục. Tìm mức điểm giao ngay $S_0$?
  - (b) Trái phiếu 10 tháng có giá $S_0 = 100$. Trả coupon $C = 3$ USD sau 4 tháng. Lãi suất hiệu dụng năm là $r = 4\%$. Tính giá Forward 10 tháng?
- **Lời giải**:
  - (a) $S_0 = F e^{-(r - q)T} = 4,200 e^{-(0.03 - 0.012) \times 0.5} = 4,200 e^{-0.009} \approx 4,200 \times 0.991040 \approx 4,162.37$ điểm.
  - (b) Cổ tức coupon rời rạc nhận tại $t_1 = 4/12$ năm:
    $$PV(\text{Coupon}) = \frac{3}{(1.04)^{4/12}} = \frac{3}{(1.04)^{1/3}} \approx \frac{3}{1.013159} \approx 2.9610$$
    Giá Forward 10 tháng ($T = 10/12$ năm):
    $$F_0 = [S_0 - PV(\text{Coupon})] \times (1.04)^{10/12} = [100 - 2.9610] \times (1.04)^{5/6} = 97.0390 \times 1.033223 \approx \$100.26$$

#### Question 8 (Lecture 09): Hàng hóa Vật chất có Chi phí Lưu kho
- **Đề bài**: Spot vàng $S_0 = 1,250$ USD/ounce. Forward 1 năm $F = 1,375$. Chi phí lưu kho trả vào cuối năm bằng 2% giá giao ngay hôm nay ($C = 0.02 \times 1,250 = \$25$). Lãi suất hiệu dụng năm $r$.
  - 1(a) Tìm lãi suất ẩn $r$?
  - 1(b) Nếu lãi suất thực tế là 5%, hãy chỉ ra cơ hội Arbitrage?
- **Lời giải**:
  - 1(a) Theo mô hình chi phí lưu trữ: $F = S_0 (1+r) + C \implies 1,375 = 1,250 (1+r) + 25 \implies 1,250(1+r) = 1,350 \implies 1+r = 1.08 \implies r = 8\%$.
  - 1(b) Nếu lãi suất thực tế là $5\%$:
    - Giá Forward lý thuyết công bằng: $F^* = 1,250 \times 1.05 + 25 = 1,312.50 + 25 = \$1,337.50$.
    - Thị trường đang niêm yết $F_{\text{market}} = 1,375 > 1,337.50 \implies$ Forward bị **định giá quá cao (Overvalued)**.
    - **Chiến lược Cash-and-Carry Arbitrage**:
      - Hôm nay: Vay $1,250 USD lãi suất 5% $\rightarrow$ Mua 1 ounce vàng $\rightarrow$ Ký Short Forward bán vàng sau 1 năm ở giá $1,375$.
      - Cuối năm: Giao vàng thu về $1,375 USD $\rightarrow$ Trả chi phí lưu kho $\$25$ $\rightarrow$ Trả nợ ngân hàng $1,250 \times 1.05 = \$1,312.50$.
      - **Lợi nhuận ròng chắc chắn** = $1,375 - 25 - 1,312.50 = +\$37.50$ mỗi ounce!

#### Question 9 (Lecture 09): Tính Dòng tiền Hợp đồng Hoán đổi Lãi suất (IRS)
- **Đề bài**: Lambda ký hợp đồng IRS 1 năm với Mu: Notional = 24 triệu USD; thanh toán hàng quý ($\Delta = 0.25$); Lambda **trả lãi cố định 4.2%** và **nhận lãi thả nổi**. Lãi suất thả nổi thực tế 4 quý lần lượt là: 3.6%, 4.8%, 4.1%, 5.1%.
  - Tính dòng tiền từng vế và dòng tiền ròng của Lambda mỗi quý?
- **Lời giải**:
  - Chân cố định mỗi quý (Lambda trả):
    $$\text{Fixed Leg} = 24,000,000 \times 4.2\% \times 0.25 = \$252,000$$
  - Chân thả nổi mỗi quý (Lambda nhận): $\text{Floating Leg}_k = 24,000,000 \times L_k \times 0.25$.
  - Dòng tiền ròng của Lambda: $\text{Net}_k = \text{Floating}_k - 252,000$.

| Quý ($k$) | Lãi suất thả nổi ($L_k$) | Chân Cố định (Trả) | Chân Thả nổi (Nhận) | Thanh toán Ròng (Lambda nhận + / trả -) |
|:---:|:---:|:---:|:---:|:---:|
| **Quý 1** | 3.6% | $252,000 | $216,000 | **-\$36,000** (Lambda trả Mu $36,000) |
| **Quý 2** | 4.8% | $252,000 | $288,000 | **+\$36,000** (Lambda nhận từ Mu $36,000) |
| **Quý 3** | 4.1% | $252,000 | $246,000 | **-\$6,000** (Lambda trả Mu $6,000) |
| **Quý 4** | 5.1% | $252,000 | $306,000 | **+\$54,000** (Lambda nhận từ Mu $54,000) |
| **Tổng cả năm** | - | $1,008,000 | $1,056,000 | **+\$48,000** (Lambda lãi ròng $48,000) |

#### Question 10 (Lecture 09): Chuyển đổi Trạng thái Nợ bằng Swap (Fixed-to-Floating Transformation)
- **Đề bài**: Swap hoán đổi lãi suất cố định 4.4% lấy thả nổi $L$.
  - Khoản vay hiện tại:
    - Eta đang có khoản vay thả nổi: $L + 0.7\%$. Eta muốn cố định chi phí vay.
    - Theta đang có khoản vay cố định: $5.2\%$. Theta muốn chuyển sang thả nổi.
- **Lời giải**:
  - **Với Eta**: Đang nợ thả nổi $\rightarrow$ Cần **Trả cố định, Nhận thả nổi** trong Swap:
    $$\text{Chi phí ròng của Eta} = \text{Trả nợ cũ} + \text{Trả Swap cố định} - \text{Nhận Swap thả nổi} = (L + 0.7\%) + 4.4\% - L = 5.10\%\ (\text{Cố định hoàn toàn})$$
  - **Với Theta**: Đang nợ cố định $\rightarrow$ Cần **Trả thả nổi, Nhận cố định** trong Swap:
    $$\text{Chi phí ròng của Theta} = \text{Trả nợ cũ} + \text{Trả Swap thả nổi} - \text{Nhận Swap cố định} = 5.20\% + L - 4.4\% = L + 0.80\%\ (\text{Thả nổi})$$

#### Question 11 (Lecture 09): Hoán đổi Tiền tệ (Currency Swap)
- **Đề bài**: Epsilon cần 10 triệu EUR trong 3 năm. Vay 12 triệu USD tại lãi suất 5%/năm (trả gốc cuối năm 3). Ký Currency Swap với Zeta: Spot ban đầu 1.20 USD/EUR. Lãi suất EUR cố định là 3.6%/năm.
  - Trình bày chi tiết dòng tiền của Epsilon qua các năm?
- **Lời giải**:
  - Tại $t=0$: Epsilon vay 12 triệu USD $\rightarrow$ Đưa 12 triệu USD cho Zeta trong Swap và nhận về 10 triệu EUR (tỷ giá 1.20). Epsilon dùng 10 triệu EUR này đầu tư. Dòng tiền ròng USD = 0, nhận được 10 triệu EUR.
  - Hàng năm (Năm 1, 2, 3):
    - Về USD: Epsilon nhận 12M $\times 5\% = +0.60$ triệu USD từ Zeta trong Swap $\rightarrow$ Trả nợ lãi vay USD $-0.60$ triệu USD. Triệt tiêu ròng USD = 0!
    - Về EUR: Epsilon trả Zeta tiền lãi EUR: $10\text{M} \times 3.6\% = -0.36$ triệu EUR.
  - Tại đáo hạn ($t=3$):
    - Epsilon nhận lại 12 triệu USD gốc từ Zeta $\rightarrow$ Trả nợ gốc ngân hàng USD.
    - Epsilon hoàn trả 10 triệu EUR gốc cho Zeta.
  - **Kết luận**: Epsilon đã chuyển đổi thành công khoản nợ từ USD sang **khoản nợ hoàn toàn bằng EUR với lãi suất cố định chỉ 3.6%/năm**!

---

### 2.1.3. Giải Chi Tiết Toàn Bộ Questions 6 – 15 trong File Bài Tập Thực Hành (Practice L08–L11)

#### Question 6 (Practice L08-L11 - Easy): Giá trị Hợp đồng Kỳ hạn
- **Đề bài**: Alpha ký Long Forward 9 tháng trên 150 cổ phiếu (không cổ tức) ở giá công bằng. $S_0 = 68$ USD, $r = 4\%$ hiệu dụng năm ($EAR$).
  - 3 tháng sau ($t = 3/12$), giá cổ phiếu $S_t = 72$ USD. Lãi suất không đổi.
  - (a) Tính giá Forward ban đầu $F_0$?
  - (b) Tính giá Forward mới 6 tháng $F_t$ và giá trị hiện tại hợp đồng $V_t$?
- **Lời giải**:
  - (a) Giá giao hàng ban đầu ($T = 9/12 = 0.75$ năm):
    $$F_0 = S_0 (1+r)^{0.75} = 68 \times (1.04)^{0.75} \approx 68 \times 1.029853 \approx \$70.03\ \text{mỗi cổ phiếu}$$
  - (b) Tại $t = 3$ tháng, thời gian còn lại là $T - t = 6$ tháng = $0.5$ năm:
    - Giá Forward mới:
      $$F_t = S_t (1+r)^{0.5} = 72 \times (1.04)^{0.5} \approx 72 \times 1.019804 \approx \$73.43\ \text{mỗi cổ phiếu}$$
    - Giá trị hợp đồng của Alpha (150 cổ phiếu):
      $$V_t = 150 \times \left[ S_t - \frac{F_0}{(1+r)^{0.5}} \right] = 150 \times \left[ 72 - \frac{70.03}{1.019804} \right] = 150 \times [72 - 68.67] = 150 \times 3.33 = +\$499.50$$

#### Question 7 (Practice L08-L11 - Easy): Ký quỹ Futures & Margin Call
- **Đề bài**: Beta bán khống (Short) 4 hợp đồng tương lai tại mức giá 45.50 USD/đơn vị. Mỗi hợp đồng gồm 250 đơn vị (Tổng quy mô = $4 \times 250 = 1,000$ đơn vị).
  - Ký quỹ ban đầu (Initial Margin): \$8,000.
  - Ký quỹ duy trì (Maintenance Margin): \$6,000.
  - Quy tắc: Nếu số dư tài khoản ký quỹ rớt dưới \$6,000, bắt buộc phải nộp tiền (Variation Margin) để **khôi phục về mức Initial Margin (\$8,000)**.
- **Lời giải & Phân tích Từng Bước**:
  - Lưu ý vị thế **SHORT**: Beta có lãi khi giá Futures GIẢM, và **BỊ LỖ khi giá Futures TĂNG**!
  - Lỗ tối đa cho phép trước khi bị Margin call:
    $$\Delta \text{Equity} = 8,000 - 6,000 = \$2,000$$
  - Vì quy mô là 1,000 đơn vị, mức tăng giá làm phát sinh Margin call:
    $$\Delta F = \frac{2,000}{1,000} = \$2.00 \implies F_{\text{call}} = 45.50 + 2.00 = \$47.50$$
  - Bất cứ khi nào giá Futures vượt quá 47.50 USD, tài khoản sẽ dưới \$6,000 và Beta phải nộp tiền bổ sung đầy đủ về lại \$8,000.

#### Question 8 (Practice L08-L11 - Easy): Hoán đổi Lãi suất & Tìm Lãi suất Thả nổi
- **Đề bài**: Gamma trả cố định 3.80% và nhận thả nổi trên hợp đồng swap 18 triệu USD với Delta. Thanh toán hàng quý ($\Delta t = 0.25$).
  - Quý 1: Lãi suất thả nổi là 3.20%.
  - Quý 2: Gamma nhận thanh toán ròng \$18,000 từ Delta.
  - (a) Tính tiền thanh toán mỗi chân và số tiền ròng quý 1? Ai trả cho ai?
  - (b) Tìm lãi suất thả nổi hàng năm của quý 2 ($L_2$)?
- **Lời giải**:
  - (a) Quý 1:
    - Chân cố định (Gamma trả): $18,000,000 \times 3.80\% \times 0.25 = \$171,000$.
    - Chân thả nổi (Gamma nhận): $18,000,000 \times 3.20\% \times 0.25 = \$144,000$.
    - Thanh toán ròng: $144,000 - 171,000 = -\$27,000 \implies$ **Gamma trả Delta \$27,000**.
  - (b) Quý 2: Gamma nhận ròng \$18,000:
    $$\text{Floating}_2 - 171,000 = +18,000 \implies \text{Floating}_2 = \$189,000$$
    Lãi suất thả nổi hàng năm quý 2:
    $$L_2 = \frac{189,000}{18,000,000 \times 0.25} = \frac{189,000}{4,500,000} = 0.042 = 4.20\%$$

#### Question 9 (Practice L08-L11 - Average): Forward Chỉ số với Cổ tức Biến đổi
- **Đề bài**: Chỉ số Epsilon $S_0 = 3,200$. Forward 9 tháng ($T = 0.75$) niêm yết $F = 3,248.36$. $r = 4.80\%$ liên tục.
  - Tỷ suất cổ tức 3 tháng đầu $q_1 = 1.20\%$. 6 tháng còn lại là $q_2$ (hằng số chưa biết).
  - (a) Tìm $q_2$?
  - (b) Nếu sau khi ký hợp đồng, thông tin mới làm $q_2$ tăng thêm 1% (lên $q_2 + 1\%$), giá Forward mới là bao nhiêu? Người giữ vị thế Long Forward có được lợi không?
- **Lời giải**:
  - (a) Công thức:
    $$F = S_0 e^{rT - q_1 T_1 - q_2 T_2} = 3,200 e^{0.048(0.75) - 0.012(0.25) - q_2(0.5)} = 3,200 e^{0.036 - 0.003 - 0.5 q_2} = 3,200 e^{0.033 - 0.5 q_2} = 3,248.36$$
    $$\frac{3,248.36}{3,200} = 1.0151125 \implies 0.033 - 0.5 q_2 = \ln(1.0151125) = 0.015000$$
    $$0.5 q_2 = 0.033 - 0.015 = 0.018 \implies q_2 = 0.036 = 3.60\%$$
  - (b) Nếu $q_2$ tăng thêm 1% thành $4.60\%$:
    - Giá Forward mới: $F_{\text{new}} = 3,200 e^{0.033 - 0.5(0.046)} = 3,200 e^{0.033 - 0.023} = 3,200 e^{0.010} \approx 3,232.16$.
    - Người nắm giữ vị thế Long Forward **BỊ THIỆT HẠI** (không được lợi), vì giá trị hợp đồng giảm: Cổ tức tăng làm giá cổ phiếu tương lai giảm đi, trong khi người Long Forward đã bị chốt mức giá mua cao hơn ở $3,248.36$.

#### Question 10 (Practice L08-L11 - Average): Hàng hóa & Lợi suất Tiện dụng Ròng (Net Convenience Yield)
- **Đề bài**: Spot $S_0 = 96$ USD/đơn vị. Forward 6 tháng $F = 94.20$ USD. Lãi suất $r = 4\%$ liên tục.
  - Hàng hóa không thể bán khống và không có thu nhập cổ tức.
  - (a) Tính tỷ suất lợi dụng tiện dụng ròng hàng năm ($y_{\text{net}} = y - u$)?
  - (b) Nếu $y_{\text{net}}$ giảm đi 2% (tức giảm 0.02), tính giá Forward mới?
  - (c) Đánh giá đề xuất Cash-and-Carry của Eta và khả năng Reverse trade?
- **Lời giải**:
  - (a) Theo công thức:
    $$F = S_0 e^{(r - y_{\text{net}}) T} \implies 94.20 = 96 e^{(0.04 - y_{\text{net}}) \times 0.5}$$
    $$\ln\left(\frac{94.20}{96}\right) = \ln(0.98125) = -0.018928$$
    $$(0.04 - y_{\text{net}}) \times 0.5 = -0.018928 \implies 0.04 - y_{\text{net}} = -0.037856 \implies y_{\text{net}} = 0.077856 \approx 7.79\%$$
  - (b) Nếu $y_{\text{net}}$ mới $= 7.7856\% - 2\% = 5.7856\%$:
    $$F_{\text{new}} = 96 e^{(0.04 - 0.057856) \times 0.5} = 96 e^{-0.008928} \approx 96 \times 0.991112 \approx \$95.15$$
  - (c) Đề xuất của Eta: Vay tiền mua hàng và bán Forward ở 94.20 sẽ chịu **LỖ CHẮC CHẮN** vì $F = 94.20 < S_0 e^{rT} = 96 e^{0.02} = 97.94$ USD.
    - Đảo ngược vị thế (Reverse Cash-and-Carry) có thực hiện được không? **KHÔNG THỂ**, vì đề bài nêu rõ: hàng hóa không thể mượn để bán khống và người sở hữu phải giữ hàng để sản xuất. Đây là hiện tượng **Short-sale restriction** tạo ra giới hạn kinh doanh chênh lệch giá (Limits to Arbitrage).

#### Question 11 (Practice L08-L11 - Average): Futures vs Forwards & Rủi ro Thanh khoản Ký quỹ
- **Đề bài**: Doanh nghiệp Omicron sẽ bán sản lượng sau 4 tháng và nhận tiền khi giao hàng. Omicron có đủ tiền nộp ký quỹ ban đầu Futures nhưng không có khả năng tài chính nộp thêm bất kỳ Margin call nào. Omicron muốn dùng Long Futures để phòng hộ.
- **Lời giải & Phân tích**:
  - (a) **Sai hướng phòng hộ (Hedge direction)**: Omicron đang có tài sản để bán sau 4 tháng $\implies$ Omicron phải **SHORT (Bán)** để bảo hiểm giá giảm, chứ không phải Long!
    - Hơn nữa, lập luận của Omicron sai lầm nghiêm trọng: Nếu giá giảm, vị thế Long Futures sẽ liên tục bị trừ tiền hàng ngày (Marking-to-Market), phát sinh Margin calls ngay lập tức trong khi doanh thu bán hàng 4 tháng nữa mới về $\implies$ Công ty sẽ bị giải chấp (default) vì thiếu thanh khoản!
  - (b) **Hợp đồng tối ưu**: Omicron nên chọn **Hợp đồng Kỳ hạn (Forward)** của ngân hàng và chọn vị thế **SHORT FORWARD**. Hợp đồng này không có thanh toán ký quỹ trung gian, dòng tiền chỉ thanh toán 1 lần duy nhất tại ngày giao hàng, khớp hoàn hảo với dòng tiền của doanh nghiệp.

#### Question 12 (Practice L08-L11 - Average): Currency Swap
- **Đề bài**: Pi cần vốn EUR trong 3 năm. Vay 9.6 triệu USD tại 4.50%/năm. Ký Currency Swap với Rho:
  - Tỷ giá giao ngay ban đầu: 1.20 USD/EUR.
  - Swap: Mỗi năm Pi nhận 432,000 USD và trả 280,000 EUR. Cuối năm 3 hoàn trả gốc.
  - (a) Tìm mệnh giá EUR và lãi suất cố định mỗi chân?
  - (b) Bảng dòng tiền và chi phí vay EUR thực tế?
  - (c) Nếu lãi suất vay USD tăng lên 5.25%, chi phí có còn cố định bằng EUR không?
- **Lời giải**:
  - (a) Mệnh giá EUR ban đầu:
    $$\text{EUR Notional} = \frac{9.6\ \text{triệu USD}}{1.20\ \text{USD/EUR}} = 8.0\ \text{triệu EUR}$$
    - Chân USD: $432,000 / 9,600,000 = 4.50\%$/năm.
    - Chân EUR: $280,000 / 8,000,000 = 3.50\%$/năm.
  - (b) Chi phí vay EUR ròng hàng năm của Pi:
    $$\text{EUR Borrowing Cost} = \frac{280,000\ \text{EUR}}{8,000,000\ \text{EUR}} = 3.50\%/\text{năm}$$
  - (c) Nếu nợ USD phải trả 5.25% ($9.6\text{M} \times 5.25\% = \$504,000$), nhưng Swap chỉ trả Pi \$432,000 $\implies$ Pi phải tự bù thêm khoản chênh lệch:
    $$504,000 - 432,000 = \$72,000\ \text{USD/năm}$$
    Khoản nợ **không còn cố định hoàn toàn bằng EUR nữa**, vì Pi phải chịu thêm rủi ro biến động tỷ giá đối với khoản thanh toán \$72,000 USD hàng năm!

#### Question 13 (Practice L08-L11 - Average): Hoán đổi Lãi suất & Rủi ro Cơ sở (Basis Risk)
- **Đề bài**: Sigma vay 32 triệu USD lãi suất thả nổi $L + 0.85\%$. Ký IRS hoán đổi $L$ lấy cố định $K$ để đưa tổng chi phí về 4.50%.
  - (a) Xác định chiều giao dịch và tìm $K$?
  - (b) Nếu khoản vay của Sigma bị neo theo lãi suất $M + 0.85\%$ trong khi Swap vẫn neo theo $L$, tính lãi suất và số tiền trả trong 2 quý: Quý 1 ($M=3.4\%, L=3.1\%$), Quý 2 ($M=2.7\%, L=3.0\%$)? Chi phí có còn cố định không?
- **Lời giải**:
  - (a) Sigma cần **Trả Cố định $K$, Nhận Thả nổi $L$**.
    $$\text{Tổng chi phí} = (L + 0.85\%) + K - L = K + 0.85\% = 4.50\% \implies K = 3.65\%$$
  - (b) Nếu khoản vay neo theo $M$:
    $$\text{Chi phí thực tế} = (M + 0.85\%) + 3.65\% - L = 4.50\% + (M - L)$$
    - Quý 1: $M - L = 3.40\% - 3.10\% = +0.30\% \implies \text{Tỷ suất} = 4.50\% + 0.30\% = 4.80\%$.
      Số tiền trả = $32,000,000 \times 4.80\% \times 0.25 = \$384,000$.
    - Quý 2: $M - L = 2.70\% - 3.00\% = -0.30\% \implies \text{Tỷ suất} = 4.50\% - 0.30\% = 4.20\%$.
      Số tiền trả = $32,000,000 \times 4.20\% \times 0.25 = \$336,000$.
    - **Kết luận**: Chi phí **không còn cố định** do xuất hiện **Rủi ro Cơ sở (Basis Risk)** giữa hai lãi suất tham chiếu $M$ và $L$.

#### Question 14 (Practice L08-L11 - Hard): Arbitrage Kinh Doanh Chênh Lệch Tỷ Giá Kỳ Hạn (CIP Arbitrage)
- **Đề bài**: Kỳ hạn 9 tháng ($T = 0.75$). Spot: $1.0800$ USD/EUR. Forward: $1.1200$ USD/EUR. Lãi suất USD: $5.00\%$ EAR. Lãi suất EUR: $2.00\%$ EAR.
  - Tau đề xuất: Vay 200,000 EUR $\rightarrow$ Đổi ra USD gửi tiết kiệm $\rightarrow$ Bán 200,000 EUR forward ở giá 1.12. Tau tuyên bố chắc chắn lãi $8,000 USD vì $(1.12 - 1.08) \times 200,000 = 8,000$.
  - (a) Tính tỷ giá Forward lý thuyết theo CIP?
  - (b) Đánh giá tuyên bố của Tau?
  - (c) Xây dựng chiến lược Arbitrage chuẩn với quy mô vốn vay 216,000 USD (tương đương 200,000 EUR)?
- **Lời giải**:
  - (a) Tỷ giá Forward CIP công bằng:
    $$F^* = S_0 \times \frac{(1 + r_{\text{USD}})^{0.75}}{(1 + r_{\text{EUR}})^{0.75}} = 1.0800 \times \frac{(1.05)^{0.75}}{(1.02)^{0.75}} = 1.0800 \times \frac{1.037286}{1.014925} \approx 1.1038\ \text{USD/EUR}$$
  - (b) Tuyên bố của Tau **SAI**: Tau đã bỏ qua lãi suất chênh lệch phải trả cho khoản vay EUR so với lãi thu được từ USD.
  - (c) **Chiến lược Arbitrage Khai thác $F_{\text{market}} = 1.1200 > F^* = 1.1038$ (Forward EUR bị đắt)**:
    - *Hôm nay ($t=0$)*:
      - Vay 200,000 EUR với lãi suất 2%/năm trong 9 tháng.
      - Đổi 200,000 EUR sang USD tại spot 1.08 $\rightarrow$ Thu được 216,000 USD.
      - Đem 216,000 USD gửi ngân hàng với lãi suất 5%/năm trong 9 tháng.
      - Bán Forward (Short Forward) số tiền EUR phải trả khi đáo hạn.
        Số EUR phải trả tại $t=0.75$: $200,000 \times (1.02)^{0.75} = 200,000 \times 1.014925 = 202,985$ EUR.
        Ký Short Forward bán đúng 202,985 EUR tại tỷ giá 1.1200.
    - *Tại đáo hạn ($t=0.75$)*:
      - Tiền gửi USD thu về: $216,000 \times (1.05)^{0.75} = 216,000 \times 1.037286 = \$224,053.84$ USD.
      - Giao 202,985 EUR theo hợp đồng Forward, thu về: $202,985 \times 1.1200 = \$227,343.20$ USD.
      - Nhưng để trả nợ vay EUR, ta cần đúng 202,985 EUR!
      - Vậy dùng USD từ tiền gửi để mua lại EUR hay dùng Forward?
      - Chính xác là: Giao hợp đồng Forward thu về $\$227,343.20$ USD, dùng số EUR thu được từ việc đóng vị thế trả hết nợ gốc + lãi EUR.
      - **Lợi nhuận ròng bằng USD thu được**:
        $$\Pi = 202,985 \times (1.1200 - 1.1038) \approx \$3,289\ \text{USD chắc chắn 100%!}$$

#### Question 15 (Practice L08-L11 - Hard): Forward Nhân Tạo & Arbitrage với Hợp Đồng Kỳ Hạn
- **Đề bài**: Cổ phiếu Phi (không cổ tức), kỳ hạn 6 tháng ($T = 0.5$).
  - Call($K=70$): \$6.20. Put($K=70$): \$3.80.
  - Hợp đồng Forward 6 tháng niêm yết giá giao hàng $F_{\text{market}} = 73.20$ USD/cổ phiếu.
  - Lãi suất phi rủi ro: $r = 4\%$ hiệu dụng năm ($EAR$).
  - (a) Dùng Call, Put và vay/gửi để tạo ra vị thế Long Forward nhân tạo? Tìm giá giao hàng ẩn?
  - (b) Xây dựng chiến lược Arbitrage với 1,000 cổ phiếu?
  - (c) Giá Call bằng bao nhiêu thì triệt tiêu cơ hội Arbitrage?
- **Lời giải**:
  - (a) **Long Synthetic Forward = Mua Call(70) + Bán Put(70)**:
    - Chi phí ban đầu hôm nay: $C - P = 6.20 - 3.80 = \$2.40$ (cần bỏ tiền túi ra trả).
    - Để tạo vị thế không tốn chi phí ban đầu ($V_0 = 0$): Ta vay thêm $\$2.40$ từ ngân hàng.
    - Tại đáo hạn $T=0.5$:
      - Payoff từ Options: $\max(S_T - 70, 0) - \max(70 - S_T, 0) = S_T - 70$.
      - Trả nợ vay ngân hàng: $2.40 \times (1.04)^{0.5} = 2.40 \times 1.019804 = \$2.4475$.
      - Dòng tiền ròng nhận được: $(S_T - 70) - 2.4475 = S_T - 72.4475$.
    - **Giá giao hàng ngụ ý của Synthetic Forward**:
      $$F_{\text{synthetic}} = 70 + 2.4475 = \$72.45\ \text{USD/cổ phiếu}$$
  - (b) **Chiến lược Arbitrage (Khai thác $F_{\text{market}} = 73.20 > F_{\text{synthetic}} = 72.45$)**:
    - Vì Forward thị trường đắt hơn Synthetic Forward:
      - **BÁN (Short) 1 hợp đồng Forward thị trường** (1,000 cổ phiếu) ở giá 73.20 USD.
      - **MUA (Long) Synthetic Forward** (Mua 10 hợp đồng Call, Bán 10 hợp đồng Put, vay \$2,400 ngân hàng).
    - *Dòng tiền hôm nay ($t=0$)*:
      $$-1,000 \times 6.20 + 1,000 \times 3.80 + 2,400 = 0\ \text{USD (Tự tài trợ 100%)}.$$
    - *Dòng tiền tại $T = 6$ tháng*:
      - Thu từ Short Forward: $1,000 \times (73.20 - S_T)$.
      - Thu từ Long Options: $1,000 \times (S_T - 70)$.
      - Trả nợ ngân hàng: $-2,400 \times (1.04)^{0.5} = -\$2,447.53$.
      - **Tổng dòng tiền ròng**:
        $$\Pi_T = 1,000(73.20 - S_T) + 1,000(S_T - 70) - 2,447.53 = 1,000(3.20) - 2,447.53 = 3,200 - 2,447.53 = +\$752.47$$
        Lợi nhuận là **dương chắc chắn trong mọi kịch bản của $S_T$**!
  - (c) Để triệt tiêu chênh lệch giá, giá giao hàng ngụ ý phải bằng giá thị trường ($F_{\text{synthetic}} = 73.20$):
    $$70 + (C - 3.80)(1.04)^{0.5} = 73.20 \implies (C - 3.80) \times 1.019804 = 3.20$$
    $$C - 3.80 = \frac{3.20}{1.019804} = 3.13785 \implies C = 3.80 + 3.13785 = \$6.94$$
"""

with open(out_file, "a", encoding="utf-8") as f:
    f.write(sec2_1)

print("Section 2.1 appended successfully.")
