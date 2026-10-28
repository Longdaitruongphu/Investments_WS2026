import sys

out_file = "/media/minh/DISK/Downloads/Investments_WS2026/MASTER_EXAM_PREPARATION_ULTIMATE_GUIDE.md"

sec2_2 = r"""
---

## 2.2. LECTURE 10: THỊ TRƯỜNG QUYỀN CHỌN, CÁC CHIẾN LƯỢC & NGANG GIÁ MUA – BÁN (PUT-CALL PARITY)

### 2.2.1. Khung Lý Thuyết & Bản Chất Kinh Tế

#### A. 4 Vị Thế Cơ Bản, Đồ Thị Payoff / Profit & Điểm Hòa Vốn

| Vị thế (Position) | Payoff tại đáo hạn ($T$) | Lợi nhuận ròng (Net Profit) | Lãi tối đa (Max Gain) | Lỗ tối đa (Max Loss) | Điểm hòa vốn (Break-even) |
|---|---|---|---|---|---|
| **Long Call** | $\max(S_T - K, 0)$ | $\max(S_T - K, 0) - C_0$ | Vô hạn ($\infty$) | Phí mua $C_0$ | $S_T = K + C_0$ |
| **Short Call** | $-\max(S_T - K, 0)$ | $C_0 - \max(S_T - K, 0)$ | Phí nhận $C_0$ | Vô hạn ($-\infty$) | $S_T = K + C_0$ |
| **Long Put** | $\max(K - S_T, 0)$ | $\max(K - S_T, 0) - P_0$ | $K - P_0$ (khi $S_T=0$) | Phí mua $P_0$ | $S_T = K - P_0$ |
| **Short Put** | $-\max(K - S_T, 0)$ | $P_0 - \max(K - S_T, 0)$ | Phí nhận $P_0$ | $-(K - P_0)$ | $S_T = K - P_0$ |

#### B. Các Chiến Lược Quyền Chọn Kinh Điển
1. **Covered Call (Mua Cổ phiếu + Bán Call $K$)**:
   - Mục đích: Kiếm thêm thu nhập phí (premium) từ cổ phiếu đang nắm giữ khi dự báo thị trường đi ngang hoặc tăng nhẹ.
   - Payoff: $S_T - \max(S_T - K, 0) = \min(S_T, K)$. Bị chặn trên tại $K$.
   - Max Profit: $(K - S_0) + C_0$.
2. **Protective Put (Mua Cổ phiếu + Mua Put $K$)**:
   - Mục đích: Bảo hiểm danh mục (Portfolio Insurance), chặn đứng rủi ro giảm giá.
   - Payoff: $S_T + \max(K - S_T, 0) = \max(S_T, K)$. Chặn dưới tại $K$.
   - Max Loss: $(S_0 - K) + P_0$.
3. **Bull Spread (Chênh lệch giá lên)**:
   - Mua Call $K_1$ (hoặc Put $K_1$) và Bán Call $K_2$ (hoặc Put $K_2$) với $K_1 < K_2$.
4. **Bear Spread (Chênh lệch giá xuống)**:
   - Mua Put $K_2$ và Bán Put $K_1$ với $K_1 < K_2$.
5. **Butterfly Spread**:
   - Kết hợp 4 quyền chọn ở 3 mức strike cách đều: Mua 1 Call($K_1$), Bán 2 Call($K_2$), Mua 1 Call($K_3$) với $K_2 - K_1 = K_3 - K_2$.
   - Lãi tối đa khi cổ phiếu đứng im chính xác tại $K_2$. Lỗ tối đa giới hạn ở mức phí ròng bỏ ra.
6. **Straddle (Vị thế Mua/Bán Cặp)**:
   - Mua 1 Call($K$) + Mua 1 Put($K$) cùng ngày đáo hạn.
   - Kỳ vọng biến động giá cực mạnh (Big Volatility) theo bất kỳ hướng nào (ví dụ trước thềm công bố báo cáo tài chính hoặc phán quyết của tòa án).
7. **Collar (Vòng đai bảo hiểm)**:
   - Mua Cổ phiếu + Mua Protective Put($K_1$) + Bán Covered Call($K_2$) với $K_1 < S_0 < K_2$.
   - Phí bán Call tài trợ một phần hoặc toàn bộ phí mua Put (Zero-cost Collar).

#### C. Ngang Giá Mua - Bán (Put-Call Parity)
- **Công thức gốc**:
  $$C + PV(K) = P + S_0 \iff C + K e^{-rT} = P + S_0$$
- **Chứng minh bằng Danh mục Sao chép (Replication)**:
  - *Danh mục A*: Mua 1 European Call($K$) + Gửi tiết kiệm $K e^{-rT}$ vào ngân hàng.
    - Tại đáo hạn $T$: Nhận $K$ từ ngân hàng.
    - Nếu $S_T > K$: Thực thi Call, trả $K$ nhận cổ phiếu $\implies$ Tổng giá trị = $S_T$.
    - Nếu $S_T \le K$: Call hết hạn, giữ $K$ tiền mặt $\implies$ Tổng giá trị = $K$.
    - Vậy giá trị danh mục A tại $T$ luôn là $\max(S_T, K)$.
  - *Danh mục B*: Mua 1 European Put($K$) + Mua 1 Cổ phiếu $S_0$.
    - Nếu $S_T > K$: Bán cổ phiếu ngoài thị trường thu $S_T$, Put hết hạn $\implies$ Tổng giá trị = $S_T$.
    - Nếu $S_T \le K$: Thực thi Put bán cổ phiếu thu $K$ $\implies$ Tổng giá trị = $K$.
    - Vậy giá trị danh mục B tại $T$ luôn là $\max(S_T, K)$.
  - Vì hai danh mục có dòng tiền tương lai giống hệt nhau trong mọi trường hợp, chi phí hôm nay bắt buộc phải bằng nhau:
    $$C + K e^{-rT} = P + S_0$$

#### D. Chứng Minh Định Lý Merton: Không Bao Giờ Thực Thi Sớm American Call (Non-Dividend)
- **Định lý**: Một quyền chọn mua kiểu Mỹ (American Call) trên cổ phiếu **không trả cổ tức** thì **không bao giờ nên thực thi trước ngày đáo hạn** ($C_{\text{American}} = C_{\text{European}}$).
- **Chứng minh toán học chặt chẽ**:
  1. Theo Put-Call Parity: $C = P + S_t - K e^{-r(T-t)}$.
  2. Vì quyền chọn bán kiểu Âu luôn có giá trị không âm ($P \ge 0$) và với lãi suất $r > 0 \implies K e^{-r(T-t)} < K$:
     $$C = P + S_t - K e^{-r(T-t)} \ge S_t - K e^{-r(T-t)} > S_t - K$$
  3. Giá trị thực thi ngay lập tức của quyền chọn mua là $S_t - K$ (Intrinsic Value).
  4. Như vậy:
     $$\text{Giá trị thị trường của Call } C > \text{Giá trị thực thi ngay } (S_t - K)$$
  5. **Bản chất kinh tế**:
     - Khi giữ quyền chọn, bạn chưa phải bỏ ra số tiền $K$, số tiền này vẫn nằm trong tài khoản sinh lãi suất $r$ cho đến ngày đáo hạn (Time value of money).
     - Bạn vẫn được bảo hiểm chống lại rủi ro giá cổ phiếu sụt giảm (Downside insurance).
     - Nếu nhà đầu tư muốn tiền mặt, họ chỉ việc **bán quyền chọn trên thị trường** để thu về $C$, số tiền này luôn lớn hơn số tiền $S_t - K$ thu được từ việc thực thi sớm!

#### E. Mô Hình Cấu Trúc Doanh Nghiệp Merton (Merton Structural Model)
- Doanh nghiệp có tổng giá trị tài sản hoạt động $V_t$, tài trợ bằng Vốn chủ sở hữu ($E_t$) và Nợ zero-coupon mệnh giá $D$ đáo hạn tại $T$:
  $$V_t = E_t + D_t$$
- Tại ngày đáo hạn $T$:
  - Nếu $V_T > D$: Doanh nghiệp trả đủ $D$ cho chủ nợ, cổ đông nhận phần thặng dư: $E_T = V_T - D$.
  - Nếu $V_T \le D$: Doanh nghiệp vỡ nợ, cổ đông thực hiện quyền trách nhiệm hữu hạn (Limited liability) tuyên bố phá sản nhận $0$, chuyển giao toàn bộ tài sản $V_T$ cho chủ nợ: $E_T = 0, D_T = V_T$.
- **Bản chất phái sinh**:
  - **Vốn chủ sở hữu (Equity)** chính là một **European Call Option** trên tổng tài sản doanh nghiệp $V$ với giá thực hiện bằng mệnh giá nợ $D$:
    $$E_T = \max(V_T - D, 0) \implies E_0 = \text{Black-Scholes-Call}(V_0, D, T, r, \sigma_V)$$
  - **Nợ rủi ro (Risky Debt)** chính là Nợ phi rủi ro trừ đi một **European Put Option** bán tài sản doanh nghiệp cho chủ nợ:
    $$D_T = \min(V_T, D) = D - \max(D - V_T, 0) \implies D_0 = D e^{-rT} - \text{Black-Scholes-Put}(V_0, D, T, r, \sigma_V)$$
  - Giá trị doanh nghiệp bảo toàn: $E_0 + D_0 = V_0$.

---

### 2.2.2. Giải Chi Tiết Toàn Bộ Questions 1 – 10 trong Slide Lecture 10

#### Question 1 (Lecture 10): Payoff của Người Mua European Call
- **Đề bài**: Nắm giữ European Call trên cổ phiếu Gamma, strike $K = \$65$, kỳ hạn 4 tháng.
  - Nếu tại đáo hạn $S_T = \$82$, payoff là bao nhiêu?
  - Nếu tại đáo hạn $S_T = \$58$, payoff là bao nhiêu?
- **Lời giải**:
  - Công thức: $\text{Payoff} = \max(S_T - K, 0)$.
  - Khi $S_T = 82$: $\max(82 - 65, 0) = \max(17, 0) = +\$17$ mỗi cổ phiếu.
  - Khi $S_T = 58$: $\max(58 - 65, 0) = \max(-7, 0) = \$0$ (quyền chọn không được thực thi).

#### Question 2 (Lecture 10): Payoff của Người Bán (Writer) European Call
- **Đề bài**: Bán (Short) European Call trên cổ phiếu Gamma, strike $K = \$65$, kỳ hạn 4 tháng.
  - Nếu $S_T = \$82$, payoff của người bán là bao nhiêu?
  - Nếu $S_T = \$58$, payoff của người bán là bao nhiêu?
- **Lời giải**:
  - Công thức: $\text{Payoff} = -\max(S_T - K, 0)$.
  - Khi $S_T = 82$: $-\max(82 - 65, 0) = -\$17$ mỗi cổ phiếu (người bán bị lỗ \$17 do phải giao cổ phiếu ở giá 65 trong khi giá thị trường là 82).
  - Khi $S_T = 58$: $-\max(58 - 65, 0) = \$0$.

#### Question 3 (Lecture 10): So Sánh Lỗ Tối Đa giữa Short Call và Short Put
- **Đề bài**: Delta cân nhắc bán unhedged European Call hoặc bán European Put cùng strike $K = \$80$, kỳ hạn 9 tháng (bỏ qua phí nhận được). So sánh lỗ tối đa giữa hai vị thế.
- **Lời giải & Phân tích**:
  - **Short Call**: Lỗ tiềm tàng là **Vô hạn ($-\infty$)**, vì giá cổ phiếu $S_T$ trên thị trường có thể tăng lên vô cùng ($S_T \to \infty$). Lỗ = $-(S_T - 80) \to -\infty$.
  - **Short Put**: Lỗ bị **chặn dưới tại mức $\$80$**, vì giá cổ phiếu $S_T$ thấp nhất chỉ có thể rơi về $0$. Khi công ty phá sản hoàn toàn ($S_T = 0$), người bán Put phải mua cổ phiếu vô giá trị với giá $80 \implies$ Lỗ tối đa = $-(80 - 0) = -\$80$ mỗi cổ phiếu.
  - *Kết luận*: Bán Call không phòng hộ có rủi ro đuôi (tail risk) lớn hơn vô cùng so với bán Put!

#### Question 4 (Lecture 10): Tìm Giá Call Không Chênh Lệch Giá từ Put-Call Parity
- **Đề bài**: Cổ phiếu Epsilon $S_0 = \$72$ (không cổ tức). European Put strike $K = \$75$, đáo hạn 9 tháng ($T = 0.75$) có giá $P = \$6.20$. Lãi suất $r = 5\%$ hiệu dụng năm ($EAR$). Tính giá Call công bằng?
- **Lời giải**:
  - Thừa số chiết khấu: $PV(K) = \frac{75}{(1.05)^{0.75}} = \frac{75}{1.037286} \approx \$72.304$.
  - Theo Put-Call Parity:
    $$C + PV(K) = P + S_0 \implies C + 72.304 = 6.20 + 72.00 = 78.20$$
    $$C = 78.20 - 72.304 = \$5.896 \approx \$5.90$$

#### Question 5 (Lecture 10): Tìm Lãi Suất Ẩn từ Cặp Quyền Chọn Parity
- **Đề bài**: Cổ phiếu Zeta $S_0 = \$92$ (không cổ tức). Quyền chọn 9 tháng ($T = 0.75$) có strike $K = \$90$. Call $C = \$8.40$, Put $P = \$4.10$. Tìm lãi suất phi rủi ro ghép lãi liên tục $r$?
- **Lời giải**:
  - Theo Put-Call Parity:
    $$C + K e^{-rT} = P + S_0 \implies 8.40 + 90 e^{-r(0.75)} = 4.10 + 92 = 96.10$$
    $$90 e^{-0.75 r} = 96.10 - 8.40 = 87.70$$
    $$e^{-0.75 r} = \frac{87.70}{90} \approx 0.974444$$
  - Lấy logarit tự nhiên hai vế:
    $$-0.75 r = \ln(0.974444) = -0.025888 \implies r = \frac{0.025888}{0.75} \approx 0.034518 = 3.45\%/\text{năm}$$

#### Question 6 (Lecture 10): Khai Thác Arbitrage Vi Phạm Put-Call Parity
- **Đề bài**: Cổ phiếu Eta $S_0 = \$54$. Kỳ hạn 1 năm ($T=1$), $K = \$50$. Put $P = \$3.40$, Call $C = \$9.00$. Lãi suất $r = 6\%$ EAR.
  - (a) Kiểm tra Put-Call Parity xem vế nào bị định giá sai?
  - (b) Xây dựng danh mục Arbitrage tự tài trợ (Self-financing)?
- **Lời giải**:
  - (a) Kiểm tra hai vế của Parity:
    - Vế trái (Fiduciary Call):
      $$\text{LHS} = C + \frac{K}{1+r} = 9.00 + \frac{50}{1.06} = 9.00 + 47.1698 = \$56.1698$$
    - Vế phải (Protective Put):
      $$\text{RHS} = P + S_0 = 3.40 + 54.00 = \$57.4000$$
    - So sánh: $\text{LHS} (\$56.17) < \text{RHS} (\$57.40) \implies$ **Vế phải (Cổ phiếu + Put) bị ĐẮT, Vế trái (Call + Trái phiếu) bị RẺ**!
  - (b) **Chiến lược Arbitrage (Reversal / Reverse Conversion)**:
    - **Mua cái rẻ**: Mua 1 Call(50) tốn \$9.00, Gửi ngân hàng \$47.17.
    - **Bán cái đắt**: Bán 1 Put(50) thu \$3.40, Bán khống 1 cổ phiếu thu \$54.00.
    - *Dòng tiền hôm nay ($t=0$)*:
      $$-9.00 - 47.17 + 3.40 + 54.00 = +\$1.23\ \text{USD (Thu ngay tiền tươi thóc thật!)}$$
    - *Dòng tiền tại đáo hạn ($T=1$)*:
      - Thu từ ngân hàng: $\$47.17 \times 1.06 = \$50.00$.
      - Dòng tiền từ Options: $\max(S_T - 50, 0) - \max(50 - S_T, 0) = S_T - 50$.
      - Hoàn trả vị thế bán khống cổ phiếu: $-S_T$.
      - **Tổng dòng tiền tại $T$**:
        $$\Pi_T = 50 + (S_T - 50) - S_T = 0\ \text{USD}$$
    - *Kết luận*: Nhà đầu tư bỏ túi ngay **\$1.23 tiền lời chắc chắn hôm nay mà không chịu bất kỳ rủi ro nào tại đáo hạn**!

#### Question 7 (Lecture 10): Giá Trị Nội Tại, Giá Trị Thời Gian & Giá Call
- **Đề bài**: Cổ phiếu Theta $S_0 = \$88$. Kỳ hạn 6 tháng ($T=0.5$), strike $K = \$95$. Put $P = \$10.80$. $r = 4.5\%$ liên tục.
  - Tìm giá trị nội tại (Intrinsic Value) và giá trị thời gian (Time Value) của Put?
  - Dùng Parity tìm giá Call?
- **Lời giải**:
  - Với Put Option ($K=95, S_0=88$):
    - **Giá trị nội tại (Intrinsic Value)**: $\max(K - S_0, 0) = \max(95 - 88, 0) = \$7.00$.
    - **Giá trị thời gian (Time Value)**:
      $$\text{Time Value} = \text{Giá thị trường} - \text{Giá trị nội tại} = 10.80 - 7.00 = \$3.80$$
  - Giá Call theo Put-Call Parity:
    $$C = P + S_0 - K e^{-rT} = 10.80 + 88 - 95 e^{-0.045 \times 0.5} = 98.80 - 95 e^{-0.0225} = 98.80 - 95(0.977751) = 98.80 - 92.886 = \$5.914 \approx \$5.91$$

#### Question 8 (Lecture 10): Giá Trị Thời Gian Âm của Call Khi Có Cổ Tức
- **Đề bài**: Chỉ số Iota ở mức 1,800 điểm. Quyền chọn Call 1 năm strike $K = 1,200$ có giá trị thời gian âm ($C < S_0 - K$). $r = 5\%$ EAR. Một khoản cổ tức tiền mặt duy nhất $D$ điểm trả vào cuối năm ngay trước khi quyền chọn đáo hạn. Tìm giá trị cổ tức tối thiểu $D$ để quyền chọn có giá trị thời gian âm?
- **Lời giải**:
  - Với quyền chọn Call có cổ tức trả tại $T$:
    $$C \ge S_0 - PV(D) - PV(K)$$
    Ở đây cổ tức $D$ trả tại $T=1 \implies PV(D) = \frac{D}{1+r}$.
    $$C \ge S_0 - \frac{D}{1+r} - \frac{K}{1+r}$$
  - Giá trị thời gian của Call là: $\text{Time Value} = C - (S_0 - K)$.
  - Để Time Value âm ($C < S_0 - K$):
    $$S_0 - \frac{D}{1+r} - \frac{K}{1+r} \le C < S_0 - K \implies -\frac{D + K}{1+r} < -K \implies \frac{D + K}{1+r} > K$$
    $$D + K > K(1+r) \implies D > K \times r$$
  - Thay số với $K = 1,200$ và $r = 5\%$:
    $$D > 1,200 \times 0.05 = 60\ \text{điểm chỉ số}$$
  - *Ý nghĩa kinh tế*: Cổ tức làm giá tài sản cơ sở giảm mạnh. Khi cổ tức lớn hơn phần tiền lãi tiết kiệm được từ việc trì hoãn nộp tiền mua ($D > K \times r$), giá trị của quyền chọn Call sẽ thấp hơn cả giá trị thực thi ngay lập tức!

#### Question 9 (Lecture 10): Ứng Dụng Mô Hình Merton trong Tài Chính Doanh Nghiệp
- **Đề bài**: Doanh nghiệp Lambda ban đầu không có nợ, có 150 triệu cổ phiếu giao dịch ở giá $\$320$/cổ phiếu (Tổng giá trị tài sản $V_0 = 150\text{M} \times 320 = 48$ tỷ USD).
  - Công ty dự kiến phát hành nợ zero-coupon mệnh giá $D = 36$ tỷ USD đáo hạn sau 2 năm.
  - Toàn bộ số tiền thu được từ phát hành nợ sẽ được trả ngay cho cổ đông dưới dạng cổ tức đặc biệt. Tài sản hoạt động không đổi.
  - Giải thích cấu trúc quyền chọn và xác định giá trị nợ, vốn chủ sở hữu theo mô hình Merton?
- **Lời giải**:
  - Theo mô hình Merton:
    - Vốn chủ sở hữu của Lambda sau khi phát hành nợ là một **Call Option** trên tài sản công ty với strike $D = 36$ tỷ USD.
    - Số tiền nợ thu về được trả thẳng cho cổ đông cũ dưới dạng cổ tức, do đó tổng của cải của cổ đông cũ vẫn được bảo toàn:
      $$\text{Tổng của cải cổ đông} = \text{Giá trị vốn chủ sở hữu mới } (E_0) + \text{Cổ tức tiền mặt nhận được } (D_0) = V_0 = 48\ \text{tỷ USD}$$
    - Vì tài sản công ty không thay đổi và không có chi phí kiệt quệ tài chính hay thuế, định lý Modigliani-Miller hoàn toàn được thỏa mãn!

#### Question 10 (Lecture 10): Định Giá Put Khi Biết Call
- **Đề bài**: Cổ phiếu Mu $S_0 = \$28$ (không cổ tức). Call 1 năm strike $K = \$30$ có giá $C = \$2.60$. $r = 4\%$ EAR. Tìm giá Put không chênh lệch giá?
- **Lời giải**:
  - Theo Put-Call Parity:
    $$P = C + \frac{K}{1+r} - S_0 = 2.60 + \frac{30}{1.04} - 28 = 2.60 + 28.8462 - 28 = \$3.4462 \approx \$3.45$$

---

### 2.2.3. Giải Chi Tiết Toàn Bộ Questions 16 – 25 trong File Bài Tập Thực Hành (Practice L08–L11)

#### Question 16 (Practice L08-L11 - Easy): Khôi Phục Phí Quyền Chọn từ Covered Call
- **Đề bài**: Alpha mua 100 cổ phiếu ở giá 48 USD/cổ phiếu và bán 1 hợp đồng Call (100 cổ phiếu) strike 52 USD. Tại đáo hạn, giá cổ phiếu $S_T = 55$ USD. Alpha báo cáo tổng lợi nhuận từ toàn bộ vị thế là 650 USD. Tìm phí quyền chọn Call $C$ mà Alpha đã nhận được trên mỗi cổ phiếu?
- **Lời giải**:
  - Tại $S_T = 55 > K = 52$, quyền chọn Call bị người mua thực thi:
    - Alpha buộc phải bán 100 cổ phiếu với giá strike 52 USD.
    - Lợi nhuận từ việc bán cổ phiếu:
      $$\text{Profit}_{\text{stock}} = 100 \times (52 - 48) = 100 \times 4 = \$400$$
    - Lợi nhuận từ phí Call nhận được ban đầu:
      $$\text{Profit}_{\text{call}} = 100 \times C$$
  - Tổng lợi nhuận:
    $$\text{Total Profit} = 400 + 100 C = 650 \implies 100 C = 250 \implies C = \$2.50/\text{cổ phiếu}$$

#### Question 17 (Practice L08-L11 - Easy): Bear Put Spread
- **Đề bài**: Beta mua 1 hợp đồng Put strike 64 giá 7.10 USD/cổ phiếu và bán 1 hợp đồng Put strike 56. Cùng ngày đáo hạn, quy mô 100 cổ phiếu. Mức lỗ tối đa của toàn bộ chiến lược là 280 USD.
  - (a) Tìm phí nhận được trên mỗi cổ phiếu từ việc bán Put strike 56 ($P_{56}$)?
  - (b) Xác định mức giá hòa vốn (Break-even) và lợi nhuận tối đa?
- **Lời giải**:
  - (a) Trong Bear Put Spread ($K_{\text{buy}} = 64 > K_{\text{sell}} = 56$):
    - Lỗ tối đa xảy ra khi giá cổ phiếu tăng vượt 64 USD (cả 2 put đều hết hạn vô giá trị). Khi đó mức lỗ chính bằng **chi phí phí ròng ban đầu bỏ ra**:
      $$\text{Max Loss} = 100 \times (P_{64} - P_{56}) = 280 \implies P_{64} - P_{56} = 2.80$$
      $$7.10 - P_{56} = 2.80 \implies P_{56} = 7.10 - 2.80 = \$4.30/\text{cổ phiếu}$$
  - (b) Giá hòa vốn & Lợi nhuận tối đa:
    - Điểm hòa vốn:
      $$\text{Break-even} = K_{\text{buy}} - \text{Net Premium} = 64 - 2.80 = \$61.20$$
    - Lợi nhuận tối đa xảy ra khi $S_T \le 56$:
      $$\text{Max Profit per share} = (K_{\text{buy}} - K_{\text{sell}}) - \text{Net Premium} = (64 - 56) - 2.80 = 8.00 - 2.80 = \$5.20$$
      $$\text{Total Max Profit} = 100 \times 5.20 = \$520$$

#### Question 18 (Practice L08-L11 - Easy): Thừa Số Chiết Khấu & Lãi Suất từ Put-Call Parity
- **Đề bài**: $S_0 = 84$ USD. Quyền chọn 9 tháng ($T = 0.75$) strike $K = 80$ có giá Call $C = 9.60$ USD, Put $P = 4.10$ USD. Giả sử thỏa mãn Parity và $r \ge 0$.
  - (a) Tìm thừa số chiết khấu 9 tháng $DF$?
  - (b) Tính lãi suất phi rủi ro ghép lãi liên tục hàng năm và kiểm tra xem có thỏa mãn $r \ge 0$ không?
- **Lời giải**:
  - (a) Theo Put-Call Parity:
    $$C + K \times DF = P + S_0 \implies 9.60 + 80 \times DF = 4.10 + 84.00 = 88.10$$
    $$80 \times DF = 88.10 - 9.60 = 78.50 \implies DF = \frac{78.50}{80} = 0.98125$$
  - (b) Tính lãi suất liên tục:
    $$DF = e^{-r T} \implies 0.98125 = e^{-0.75 r} \implies -0.75 r = \ln(0.98125) = -0.018928$$
    $$r = \frac{0.018928}{0.75} \approx 0.025237 = 2.52\%/\text{năm} \ge 0\ (\text{Thỏa mãn điều kiện!})$$

#### Question 19 (Practice L08-L11 - Average): So Sánh Straddle vs Strangle
- **Đề bài**: Cổ phiếu Delta $S_0 = 100$ USD. Quyền chọn 3 tháng, $r = 0$.
  - Put(90): \$2; Put(100): \$6; Call(100): \$6; Call(110): \$3.
  - Chiến lược 1 (Straddle): Mua Put(100) + Mua Call(100).
  - Chiến lược 2 (Strangle): Mua Put(90) + Mua Call(110). Quy mô 100 cổ phiếu.
  - (a) Tính chi phí ban đầu và lợi nhuận ròng tại các mức giá đáo hạn: 86, 100, 114 USD?
  - (b) Tìm điểm hòa vốn và lỗ tối đa của mỗi chiến lược?
  - (c) Nếu Epsilon chỉ chấp nhận mức lỗ tối đa \$600, chiến lược nào phù hợp và phân tích sự đánh đổi (trade-off)?
- **Lời giải**:
  - (a) Bảng so sánh Dòng tiền & Lợi nhuận:
    - **Straddle**: Chi phí ban đầu $= 100 \times (6 + 6) = \$1,200$ (\$12/cổ phiếu).
      - Tại $S_T = 86$: Payoff $= 100 \times \max(100 - 86, 0) = \$1,400 \implies \text{Net Profit} = 1,400 - 1,200 = +\$200$.
      - Tại $S_T = 100$: Payoff $= 0 \implies \text{Net Profit} = 0 - 1,200 = -\$1,200$.
      - Tại $S_T = 114$: Payoff $= 100 \times \max(114 - 100, 0) = \$1,400 \implies \text{Net Profit} = 1,400 - 1,200 = +\$200$.
    - **Strangle**: Chi phí ban đầu $= 100 \times (2 + 3) = \$500$ (\$5/cổ phiếu).
      - Tại $S_T = 86$: Payoff $= 100 \times \max(90 - 86, 0) = \$400 \implies \text{Net Profit} = 400 - 500 = -\$100$.
      - Tại $S_T = 100$: Payoff $= 0 \implies \text{Net Profit} = 0 - 500 = -\$500$.
      - Tại $S_T = 114$: Payoff $= 100 \times \max(114 - 110, 0) = \$400 \implies \text{Net Profit} = 400 - 500 = -\$100$.
  - (b) Điểm hòa vốn & Lỗ tối đa:
    - **Straddle**:
      - Hòa vốn: $100 \pm 12 \implies \mathbf{88\ \text{USD}}$ và $\mathbf{112\ \text{USD}}$.
      - Lỗ tối đa: $\mathbf{\$1,200}$ (xảy ra tại đúng $S_T = 100$).
    - **Strangle**:
      - Hòa vốn: $90 - 5 = \mathbf{85\ \text{USD}}$ và $110 + 5 = \mathbf{115\ \text{USD}}$.
      - Lỗ tối đa: $\mathbf{\$500}$ (xảy ra khi $S_T \in [90, 110]$).
  - (c) Đánh giá:
    - Chiến lược **Strangle** đáp ứng giới hạn lỗ tối đa $\le \$600$ (vì lỗ tối đa chỉ là \$500).
    - **Sự đánh đổi (Trade-off)**: Strangle có chi phí rẻ hơn và lỗ tối đa ít hơn (\$500 vs \$1,200), nhưng đòi hỏi giá cổ phiếu phải biến động mạnh hơn rất nhiều mới có lãi (vùng hòa vốn rộng hơn: $<85$ hoặc $>115$, so với $<88$ hoặc $>112$ của Straddle).

#### Question 20 (Practice L08-L11 - Average): Bắt Lỗi Định Giá & Arbitrage Vi Phạm Giới Hạn Dưới
- **Đề bài**: Cổ phiếu Zeta $S_0 = 100$ USD. Quyền chọn 1 năm, $r = 10\%$ EAR.
  - Call(90): \$17; Call(110): \$9; Put(110): \$9.
  - (a) Kiểm tra Parity cho cặp $K=110$ và kiểm tra các giới hạn giá riêng lẻ?
  - (b) Xây dựng giao dịch Arbitrage tự tài trợ?
- **Lời giải**:
  - (a) Kiểm tra:
    - Với cặp $K=110$:
      $$\text{LHS} = C(110) + \frac{110}{1.10} = 9 + 100 = 109$$
      $$\text{RHS} = P(110) + S_0 = 9 + 100 = 109$$
      $\implies$ Put-Call Parity cho $K=110$ **hoàn toàn thỏa mãn**!
    - Tuy nhiên, hãy kiểm tra **Giới hạn dưới (Lower Bound) của Call(90)**:
      $$C(90) \ge \max\left(0, S_0 - \frac{90}{1+r}\right) = 100 - \frac{90}{1.10} = 100 - 81.82 = \$18.18$$
      Nhưng trên thị trường Call(90) chỉ được niêm yết với giá **\$17.00 < \$18.18**!
      $\implies$ **Call(90) bị vi phạm giới hạn dưới nghiêm trọng (bị định giá quá rẻ)!**
  - (b) **Chiến lược Arbitrage Khai thác Call(90) bị rẻ**:
    - **Hôm nay ($t=0$)**:
      - Mua 1 Call(90) giá \$17.
      - Bán khống 1 cổ phiếu thu \$100 tiền mặt.
      - Đem số tiền dư $100 - 17 = \$83$ gửi ngân hàng với lãi suất 10%. Dòng tiền ròng hôm nay $= 0$.
    - **Tại đáo hạn ($T=1$)**:
      - Tiền gửi ngân hàng thu về: $83 \times 1.10 = \$91.30$.
      - Thực hiện Call(90): Bỏ ra \$90 mua lại cổ phiếu để trả lại cho vị thế bán khống. (Nếu $S_1 < 90$, ta mua trực tiếp ngoài chợ với giá $S_1 < 90$, chi phí còn thấp hơn nữa!).
      - **Lợi nhuận ròng chắc chắn**:
        $$\Pi_1 \ge 91.30 - 90 = +\$1.30\ \text{USD mỗi cổ phiếu!}$$

#### Question 21 (Practice L08-L11 - Average): Butterfly Spread
- **Đề bài**: $S_0 = 90$ USD. 3 quyền chọn Call cùng kỳ hạn, $r = 0$:
  - Call(80): \$13; Call(90): \$7; Call(100): \$3.
  - Mục tiêu tạo đồ thị hình lều (Payoff = 0 khi $S_T \le 80$ hoặc $S_T \ge 100$; Payoff cực đại = 10 khi $S_T = 90$).
  - (a) Xác định số lượng vị thế từng quyền chọn?
  - (b) Tính chi phí ban đầu, lãi tối đa, lỗ tối đa và điểm hòa vốn?
- **Lời giải**:
  - (a) Cấu trúc Butterfly Spread:
    $$\mathbf{+1\ \text{Call}(80) - 2\ \text{Call}(90) + 1\ \text{Call}(100)}$$
    - Kiểm tra Payoff:
      - Khi $S_T \le 80$: $0 - 0 + 0 = 0$.
      - Khi $S_T = 90$: $(90 - 80) - 0 + 0 = 10$.
      - Khi $S_T \ge 100$: $(S_T - 80) - 2(S_T - 90) + (S_T - 100) = S_T - 80 - 2S_T + 180 + S_T - 100 = 0$.
  - (b) Các thông số tài chính:
    - Chi phí ban đầu: $\text{Cost} = 13 - 2(7) + 3 = 13 - 14 + 3 = \$2.00$.
    - Lãi tối đa (tại $S_T = 90$): $\text{Max Profit} = 10 - 2 = \$8.00$.
    - Lỗ tối đa (khi $S_T \le 80$ hoặc $\ge 100$): $\text{Max Loss} = -\$2.00$ (chính bằng chi phí ban đầu).
    - Điểm hòa vốn: $K_1 + \text{Cost} = 80 + 2 = \mathbf{82\ \text{USD}}$ và $K_3 - \text{Cost} = 100 - 2 = \mathbf{98\ \text{USD}}$.

#### Question 22 (Practice L08-L11 - Average): Quyết Định Thực Thi Sớm American Call Trước Cổ Tức
- **Đề bài**: Iota giữ American Call, $K = 80$. Ngay trước ngày chốt quyền:
  - Giá cổ phiếu trước cổ tức: $S_{\text{cum}} = 92.60$ USD.
  - Cổ tức tiền mặt trả ngay: $Div = 1.60$ USD $\implies$ Giá sau cổ tức $S_{\text{ex}} = 92.60 - 1.60 = 91.00$ USD.
  - Thời gian còn lại: 6 tháng ($T = 0.5$). $r = 4\%$ EAR. Put(80) sau cổ tức có giá $P_{\text{ex}} = 0.25$ USD.
  - Kappa khuyên: "Nên thực thi ngay lập tức để lấy cổ tức 1.60 USD vì cổ tức lớn hơn tiền lãi bị mất khi trả tiền sớm".
  - (a) Đánh giá lời khuyên của Kappa bằng cách so sánh Giá trị Thực thi (Exercise Value) và Giá trị Tiếp tục (Continuation Value)?
  - (b) Tìm mức cổ tức làm người nắm giữ bàng quan (Indifferent)?
- **Lời giải**:
  - (a) **So sánh Giá trị**:
    - **Nếu Thực thi ngay trước giờ chốt quyền (Early Exercise)**:
      $$\text{Exercise Value} = S_{\text{cum}} - K = 92.60 - 80 = \$12.60$$
    - **Nếu Giữ tiếp quyền chọn (Continuation)**:
      Sau khi chốt quyền, cổ phiếu không còn cổ tức nào khác, giá trị quyền chọn Call là $C_{\text{ex}}$.
      Theo Put-Call Parity sau cổ tức:
      $$C_{\text{ex}} = P_{\text{ex}} + S_{\text{ex}} - \frac{K}{(1+r)^{0.5}} = 0.25 + 91.00 - \frac{80}{(1.04)^{0.5}} = 91.25 - \frac{80}{1.019804} = 91.25 - 78.4465 = \$12.8035$$
      Vì $C_{\text{ex}} = \$12.80 > \$12.60$, **Giá trị Tiếp tục nắm giữ LỚN HƠN Giá trị Thực thi ngay**!
      $\implies$ **Lời khuyên của Kappa là HOÀN TOÀN SAI LẦM**! Không nên thực thi sớm.
  - (b) **Mức cổ tức làm bàng quan**:
    Người nắm giữ bàng quan khi:
    $$\text{Exercise Value} = \text{Continuation Value} \iff (S_{\text{ex}} + Div) - K = C_{\text{ex}}$$
    $$Div = C_{\text{ex}} - (S_{\text{ex}} - K) = 12.8035 - (91.00 - 80.00) = 12.8035 - 11.00 = \$1.8035$$
    Cổ tức phải đạt ít nhất **\$1.80** thì mới bõ công thực thi sớm!

#### Question 23 (Practice L08-L11 - Average): Tác Động Của Kỳ Hạn & Lãi Suất Lên Giá Quyền Chọn
- **Đề bài**: Đánh giá 2 nhận định bằng lập luận kinh tế:
  - (a) "American Put 12 tháng không thể rẻ hơn American Put 6 tháng. Do đó, quy luật thứ tự kỳ hạn này cũng bắt buộc phải đúng với European Put."
  - (b) "Nếu lãi suất tăng trong khi các yếu tố khác không đổi, cả Call và Put kiểu Âu đều tăng giá vì tiền sinh lời nhanh hơn."
- **Lời giải & Phân tích**:
  - (a) **Nhận định SAI**:
    - Với **American Put**: Người giữ có quyền thực thi bất cứ lúc nào, nên kỳ hạn dài hơn luôn chứa đựng toàn bộ các cơ hội thực thi của kỳ hạn ngắn hơn $\implies P_{\text{American}}(T_2) \ge P_{\text{American}}(T_1)$ (luôn đúng).
    - Nhưng với **European Put**: Chỉ được thực thi tại đúng ngày đáo hạn $T$. Khi $T$ càng dài, giá trị hiện tại của khoản tiền strike nhận được $PV(K) = K e^{-rT}$ càng bị chiết khấu mạnh (càng nhỏ đi). Do đó, đối với European Put có độ sâu ITM cao, **European Put kỳ hạn dài CÓ THỂ RẺ HƠN European Put kỳ hạn ngắn**!
  - (b) **Nhận định SAI**:
    - Khi lãi suất $r$ tăng:
      - Giá trị hiện tại của giá thực hiện $PV(K) = K e^{-rT}$ **giảm xuống**.
      - Với **Call**: $C = S_0 - PV(K) \implies$ Phải trả ít tiền hơn về mặt giá trị hiện tại $\implies$ **Call TĂNG GIÁ**.
      - Với **Put**: $P = PV(K) - S_0 \implies$ Khoản tiền nhận được trong tương lai bị mất giá trị hiện tại $\implies$ **Put GIẢM GIÁ**.

#### Question 24 (Practice L08-L11 - Hard): Thiết Lập Chiến Lược Collar Phòng Hộ Danh Mục
- **Đề bài**: Mu sở hữu 1,000 cổ phiếu Nu, $S_0 = 50$ USD. Trong mỗi quý tới (2 quý, tổng 6 tháng), giá tăng 20% ($u=1.2$) hoặc giảm 20% ($d=0.8$). Lãi suất $r = 0$.
  - Bảng quyền chọn 6 tháng: Put(46): \$3.50; Call(56): \$4.00; Call(64): \$2.00. Put(50): Chưa biết giá.
  - Mu muốn đảm bảo giá trị danh mục tại đáo hạn **tối thiểu là \$50,000** (sàn 50 USD/cổ phiếu $\implies$ Cần mua Put strike 50).
  - Ngân sách trả phí ròng tối đa là **\$2,000** (tối đa \$2.00/cổ phiếu). Mu có thể bán 1 Call cùng số lượng để tài trợ chi phí.
  - (a) Định giá Put(50) bằng cây nhị thức?
  - (b) Xác định chiến lược Collar hợp lệ? Nêu rõ số lượng, chi phí ròng, mức sàn và trần lợi nhuận?
  - (c) So sánh với việc chỉ mua Put(50)?
- **Lời giải**:
  - (a) **Định giá Put(50) trên cây nhị thức 2 thời kỳ**:
    - Vì $r = 0 \implies R = 1.0$.
    - Xác suất trung lập rủi ro: $p = \frac{R - d}{u - d} = \frac{1.0 - 0.8}{1.2 - 0.8} = \frac{0.2}{0.4} = 0.50$.
    - Cây giá cổ phiếu sau 2 kỳ:
      - $S_{uu} = 50 \times 1.2^2 = 72$ USD $\implies$ Payoff Put(50) $= 0$.
      - $S_{ud} = 50 \times 1.2 \times 0.8 = 48$ USD $\implies$ Payoff Put(50) $= \max(50 - 48, 0) = 2$ USD.
      - $S_{dd} = 50 \times 0.8^2 = 32$ USD $\implies$ Payoff Put(50) $= \max(50 - 32, 0) = 18$ USD.
    - Định giá lùi (Backward Induction) vì $r=0$:
      - Node $u$: $P_u = 0.5(0) + 0.5(2) = 1.0$ USD.
      - Node $d$: $P_d = 0.5(2) + 0.5(18) = 10.0$ USD.
      - Gốc $t=0$: $P_0 = 0.5(P_u) + 0.5(P_d) = 0.5(1.0) + 0.5(10.0) = \$5.50/\text{cổ phiếu}$.
  - (b) **Chiến lược Collar**:
    - Mu bắt buộc phải mua Put(50) với giá \$5.50/cổ phiếu.
    - Nếu không bán Call, chi phí là $1,000 \times 5.50 = \$5,500 > \$2,000$ (vượt ngân sách!).
    - Để đưa chi phí ròng $\le \$2.00$/cổ phiếu, Mu cần bán Call có phí $\ge 5.50 - 2.00 = \$3.50$.
    - Nhìn vào bảng giá Call:
      - Call(56) có phí \$4.00 > \$3.50 $\implies$ **HỢP LỆ!**
      - Call(64) có phí \$2.00 (không đủ bù ngân sách).
    - **Cấu trúc chiến lược đã chọn**:
      - Giữ nguyên 1,000 cổ phiếu Nu.
      - Mua 10 hợp đồng Put strike 50 (chi \$5,500).
      - Bán 10 hợp đồng Call strike 56 (thu \$4,000).
      - **Chi phí phí ròng**: $5,500 - 4,000 = \mathbf{\$1,500 \le \$2,000}$ (Thỏa mãn ngân sách!).
      - **Mức sàn (Floor)**: \$50/cổ phiếu $\implies$ Giá trị danh mục tối thiểu luôn là **\$50,000**.
      - **Mức trần (Cap)**: \$56/cổ phiếu $\implies$ Giá trị danh mục tối đa bị chặn ở **\$56,000**.
  - (c) **So sánh & Sự đánh đổi**:
    - Tiết kiệm được: $5,500 - 1,500 = \$4,000$ chi phí tiền mặt ban đầu.
    - Cái giá phải trả (Trade-off): Mu đã **từ bỏ toàn bộ phần lợi nhuận tiềm năng khi giá cổ phiếu tăng vượt 56 USD** (nếu cổ phiếu tăng lên 72 USD, Mu vẫn chỉ nhận được tối đa 56 USD/cổ phiếu).

#### Question 25 (Practice L08-L11 - Hard): Mô Hình Cấu Trúc Merton Định Giá Nợ & Vốn Chủ Sở Hữu
- **Đề bài**: Doanh nghiệp Xi có giá trị tài sản hoạt động $V_0 = 120$ triệu USD, độ biến động tài sản $\sigma_V = 30\%$/năm. Lãi suất liên tục $r = 4\%$/năm.
  - Xi đề xuất phát hành nợ zero-coupon mệnh giá $D = 100$ triệu USD kỳ hạn 2 năm ($T=2$). Toàn bộ số tiền thu được trả cổ tức đặc biệt cho cổ đông.
  - (a) Xác định giá trị thị trường của Vốn chủ sở hữu ($E_0$) và Nợ ($D_0$) sau đợt phân phối?
  - (b) Tính lợi suất hứa hẹn hiệu dụng năm của nợ ($YTM$) và Phần bù rủi ro tín dụng (Credit Spread)?
  - (c) Phương án 2: Phát hành nợ mệnh giá $D = 120$ triệu USD, giá trị vốn chủ sở hữu theo mô hình là 24.3358 triệu USD. So sánh chi phí đi vay và số vốn huy động?
  - (d) So sánh tổng của cải của cổ đông cũ giữa hai phương án?
- **Lời giải chi tiết**:
  - (a) **Định giá theo Black-Scholes ($V_0 = 120, K = D = 100, T = 2, r = 0.04, \sigma = 0.30$)**:
    $$\ln(V_0 / D) = \ln(120 / 100) = \ln(1.20) = 0.182322$$
    $$\sigma \sqrt{T} = 0.30 \times \sqrt{2} = 0.30 \times 1.414214 = 0.424264$$
    $$d_1 = \frac{\ln(V_0/D) + (r + \sigma^2/2)T}{\sigma \sqrt{T}} = \frac{0.182322 + (0.04 + 0.045) \times 2}{0.424264} = \frac{0.182322 + 0.170000}{0.424264} = \frac{0.352322}{0.424264} \approx 0.830431$$
    $$d_2 = d_1 - \sigma \sqrt{T} = 0.830431 - 0.424264 = 0.406167$$
    Tra bảng phân phối chuẩn tích lũy $N(d)$:
    $$N(d_1) = N(0.8304) \approx 0.79685, \quad N(d_2) = N(0.4062) \approx 0.65768$$
    $$PV(D) = 100 e^{-0.04 \times 2} = 100 e^{-0.08} = 100 \times 0.923116 = 92.3116\ \text{triệu USD}$$
    - Giá trị Vốn chủ sở hữu (Equity):
      $$E_0 = V_0 N(d_1) - PV(D) N(d_2) = 120(0.79685) - 92.3116(0.65768) = 95.622 - 60.712 = \mathbf{34.91\ \text{triệu USD}}$$
    - Giá trị Nợ (Debt):
      $$D_0 = V_0 - E_0 = 120 - 34.91 = \mathbf{85.09\ \text{triệu USD}}$$
  - (b) **Lợi suất Hứa hẹn & Credit Spread**:
    - Lợi suất ghép lãi liên tục của nợ:
      $$y = \frac{1}{T} \ln\left(\frac{D}{D_0}\right) = \frac{1}{2} \ln\left(\frac{100}{85.09}\right) = \frac{1}{2} \ln(1.175226) = \frac{0.161461}{2} = 8.073\%/\text{năm}$$
    - Lợi suất hiệu dụng năm của nợ:
      $$EAR_{\text{debt}} = \left(\frac{100}{85.09}\right)^{1/2} - 1 = \sqrt{1.175226} - 1 = 1.084078 - 1 = 8.41\%/\text{năm}$$
    - Lợi suất hiệu dụng phi rủi ro: $EAR_{\text{rf}} = e^{0.04} - 1 = 4.081\%/\text{năm}$.
    - **Credit Spread**:
      $$\text{Spread} = 8.073\% - 4.00\% = 4.073\%/\text{năm}\ (\text{hoặc theo EAR: } 8.41\% - 4.08\% = 4.33\%)$$
  - (c) **Phương án 2 ($D = 120$ triệu USD)**:
    - Vốn chủ sở hữu: $E_0 = 24.3358$ triệu USD.
    - Giá trị Nợ thu về: $D_0 = 120 - 24.3358 = 95.6642$ triệu USD.
    - Lợi suất nợ liên tục:
      $$y_2 = \frac{1}{2} \ln\left(\frac{120}{95.6642}\right) = \frac{1}{2} \ln(1.254388) = \frac{0.226647}{2} = 11.33\%/\text{năm}$$
    - So sánh: Phương án 2 huy động được nhiều tiền mặt hơn (95.66M so với 85.09M), nhưng mức độ đòn bẩy tài chính cao hơn khiến rủi ro vỡ nợ tăng vọt, đẩy chi phí vay $y$ từ **8.07% lên 11.33%** (Credit spread tăng từ 4.07% lên 7.33%).
  - (d) **Tổng của cải của Cổ đông cũ**:
    - Phương án 1: Cổ tức 85.09M + Vốn chủ mới 34.91M = **120 triệu USD**.
    - Phương án 2: Cổ tức 95.66M + Vốn chủ mới 24.34M = **120 triệu USD**.
    - *Kết luận*: Cổ đông cũ nhận được **tổng giá trị y hệt nhau (120 triệu USD)** trong cả hai phương án! Đây là minh chứng hoàn hảo cho định lý Modigliani-Miller: Cấu trúc vốn chỉ tái phân chia chiếc bánh doanh nghiệp chứ không làm thay đổi tổng giá trị của chiếc bánh khi không có ma sát thị trường.
"""

with open(out_file, "a", encoding="utf-8") as f:
    f.write(sec2_2)

print("Section 2.2 appended successfully.")
