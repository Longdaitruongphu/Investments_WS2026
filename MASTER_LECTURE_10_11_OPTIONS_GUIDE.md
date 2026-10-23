# BFIN INVESTMENTS (WS2026) - MASTER STUDY GUIDE: LECTURE 10 & 11
## CẨM NANG TOÀN DIỆN TỰ HỌC & GIẢI CHI TIẾT TỪNG BƯỚC BÀI TẬP (SONG NGỮ VIỆT - ANH)
**Topic: Options Markets, Option Strategies, Put-Call Parity, Binomial Option Pricing Model (BOPM) & Black-Scholes Model (BSOPM)**  
*Phương pháp Sư phạm Feynman: Trực quan, Dễ hiểu như kể chuyện, Chặt chẽ về Toán học, 100% Nội dung Thi cử*

---

# MỤC LỤC CHIẾN LƯỢC (TABLE OF CONTENTS)
1. [Bản đồ Tư duy & Triết lý Học Quyền chọn (Mindset & Roadmap)](#1-bản-đồ-tư-duy--triết-lý-học-quyền-chọn)
2. [Lecture 10: Thị trường Quyền chọn & Các Chiến lược (Options & Strategies)](#2-lecture-10-thị-trường-quyền-chọn--các-chiến-lược)
   - 2.1. Bản chất Call / Put, Moneyness, Intrinsic vs. Time Value
   - 2.2. Payoff vs. Profit (Đồ thị Lãi/Lỗ)
   - 2.3. Các Chiến lược Quyền chọn Kinh điển (Protective Put, Covered Call, Spreads, Straddles)
   - 2.4. Ngang giá Mua - Bán (Put-Call Parity) & Vị thế Nhân tạo (Synthetic Positions)
   - 2.5. Các Yếu tố Tác động lên Giá Quyền chọn
   - 2.6. Thực thi sớm Quyền chọn Mỹ (Early Exercise: American Options)
   - 2.7. Ứng dụng Quyền chọn trong Tài chính Doanh nghiệp (Merton Structural Model & Risky Debt)
   - 2.8. Giới hạn Giá Quyền chọn (Price Bounds, Box Spreads & Butterfly)
3. [Lecture 10: Hướng dẫn & Lời giải Chi tiết 10 Câu hỏi Trên lớp (Questions 1 - 10)](#3-lecture-10-giải-chi-tiết-10-câu-hỏi-trên-lớp)
4. [Lecture 11: Định giá Quyền chọn - Mô hình Nhị thức & Black-Scholes](#4-lecture-11-định-giá-quyền-chọn-mô-hình-nhị-thức--black-scholes)
   - 4.1. Mô hình Cây Nhị thức 1 Thời kỳ (BOPM 1-Period): Danh mục Sao chép & Giá Trạng thái (State Prices)
   - 4.2. Định giá Trung lập Rủi ro (Risk-Neutral Valuation): Bản chất & Công thức $p$
   - 4.3. Mô hình Cây Nhị thức Đa Thời kỳ (Multi-Period Trees) & Thực thi Sớm Quyền chọn Mỹ
   - 4.4. Mô hình Black-Scholes-Merton (BSOPM): Công thức, Giả định & Ý nghĩa $N(d_1), N(d_2)$
   - 4.5. Độ nhạy (Greeks: $\Delta$), Đòn bẩy ($\Omega$) & Rủi ro Hệ thống ($\beta$) của Quyền chọn
   - 4.6. Biến động Ngụ ý (Implied Volatility) & Thước đo Sợ hãi VIX
5. [Lecture 11: Hướng dẫn & Lời giải Chi tiết Tất cả Bài tập & Ví dụ Minh họa](#5-lecture-11-giải-chi-tiết-tất-cả-bài-tập-minh-họa)
   - Bài toán Gamma Stock (European & American ATM/ITM Puts & Calls)
   - Bài toán Cây Nhị thức 2 Thời kỳ (Tỷ lệ phần trăm & Bước nhảy cộng tiền)
   - Bài toán Cây Nhị thức Quyền chọn Mỹ 2 Thời kỳ (Quyết định Thực thi Sớm)
   - Bài toán Định giá Black-Scholes: Cổ phiếu Lambda & Cổ phiếu Sigma/Theta
6. [Bí kíp Bấm máy & 10 Bẫy Thi Sống Còn (Speed-Run Exam Playbook & Fatal Pitfalls)](#6-bí-kíp-bấm-máy--10-bẫy-thi-sống-còn)

---

# 1. BẢN ĐỒ TƯ DUY & TRIẾT LÝ HỌC QUYỀN CHỌN

### Giải thích cho một đứa trẻ (Explain Like I'm 5 - ELI5):
- **Cổ phiếu thông thường**: Giống như bạn mua một chiếc xe máy. Giá xe tăng thì bạn vui, giá xe giảm thì bạn chịu thiệt. Lãi/lỗ chạy thẳng một đường chéo đối xứng.
- **Quyền chọn (Option)**: Giống như bạn trả một khoản tiền cọc nhỏ để giữ quyền mua hoặc bán một món đồ:
  - **Quyền chọn Mua (Call Option)**: Giống như **Phiếu đặt cọc mua căn hộ**. Bạn cọc 50 triệu để có quyền mua căn hộ với giá 2 tỷ trong 6 tháng. Nếu sau 6 tháng giá căn hộ vọt lên 3 tỷ, bạn thực hiện quyền mua ở giá 2 tỷ rồi bán ra lãi đậm 950 triệu. Nếu căn hộ rớt giá xuống 1.5 tỷ, bạn chỉ việc **vứt tờ phiếu cọc đi**, chịu mất tối đa đúng 50 triệu! Quyền chọn cho bạn **lợi nhuận không giới hạn nhưng chặn đứng rủi ro lỗ**!
  - **Quyền chọn Bán (Put Option)**: Giống như **Hợp đồng bảo hiểm xe máy**. Bạn trả phí 500k. Nếu xe không bị tai nạn, bạn mất 500k. Nhưng nếu xe bị đâm nát bét (giá trị về 0), công ty bảo hiểm phải mua lại chiếc xe nát đó từ bạn với giá thỏa thuận ban đầu (ví dụ 30 triệu).
- **Vấn đề cốt lõi của môn học**: Một tờ vé cọc hay hợp đồng bảo hiểm như vậy **hôm nay đáng giá bao nhiêu tiền?** $\implies$ Đó là toàn bộ nội dung của **Lecture 10 & 11**!

---

# 2. LECTURE 10: THỊ TRƯỜNG QUYỀN CHỌN & CÁC CHIẾN LƯỢC
*(OPTIONS MARKETS AND STRATEGIES)*

## 2.1. Khái niệm Cơ bản, Trạng thái Giá (Moneyness) & Giá trị Nội tại
### Thuật ngữ Cốt lõi (Core Terminology):
- **Call Option (Quyền chọn Mua)**: Quyền (nhưng không phải nghĩa vụ) được **MUA** tài sản ở mức giá thực hiện $K$ (Strike Price) vào hoặc trước ngày đáo hạn $T$.
- **Put Option (Quyền chọn Bán)**: Quyền (nhưng không phải nghĩa vụ) được **BÁN** tài sản ở mức giá thực hiện $K$ vào hoặc trước ngày đáo hạn $T$.
- **Long Position (Bên Mua Quyền)**: Trả phí quyền chọn ($C$ hoặc $P$) ngay hôm nay $\implies$ Có **quyền**, không có nghĩa vụ. Lỗ tối đa = Tiền phí đã trả.
- **Short Position / Writer (Bên Bán/Phát hành Quyền)**: Nhận phí quyền chọn ngay hôm nay $\implies$ Chịu **nghĩa vụ bắt buộc** phải thực hiện nếu người mua yêu cầu. Lãi tối đa = Tiền phí nhận được; Rủi ro lỗ là vô hạn (với Short Call) hoặc rất lớn (với Short Put)!

### Trạng thái Giá (Moneyness):
| Trạng thái (Moneyness) | Call Option ($C$) | Put Option ($P$) | Ý nghĩa thực tế |
| :--- | :---: | :---: | :--- |
| **In-the-Money (ITM) - Có lãi** | $S_t > K$ | $S_t < K$ | Nếu thực thi ngay bây giờ sẽ thu được dòng tiền dương. |
| **At-the-Money (ATM) - Hòa vốn** | $S_t = K$ | $S_t = K$ | Giá thị trường bằng đúng giá thực hiện. |
| **Out-of-the-Money (OTM) - Lỗ** | $S_t < K$ | $S_t > K$ | Nếu thực thi ngay bây giờ sẽ bị lỗ (không ai dại dột thực thi). |

### Cấu trúc Giá Quyền chọn (Option Value Structure):
$$\text{Option Price (Tổng giá trị)} = \text{Intrinsic Value (Giá trị nội tại)} + \text{Time Value (Giá trị thời gian)}$$
- **Giá trị Nội tại (Intrinsic Value)**: Số tiền bạn bỏ túi nếu quyền chọn được thực thi NGAY LẬP TỨC:
  - $\text{Intrinsic Value (Call)} = \max(S_t - K, 0)$
  - $\text{Intrinsic Value (Put)} = \max(K - S_t, 0)$
  - *Lưu ý sống còn*: Giá trị nội tại **luôn luôn $\ge 0$**, không bao giờ nhận giá trị âm! Nếu OTM, Intrinsic Value $= 0$.
- **Giá trị Thời gian (Time Value / Speculative Value)**: Phần giá trị vượt trội so với giá trị nội tại, phản ánh kỳ vọng giá cổ phiếu sẽ biến động có lợi trước khi đáo hạn:
  $$\text{Time Value} = \text{Option Price} - \text{Intrinsic Value}$$

---

## 2.2. Dòng tiền Đáo hạn (Payoff) vs. Lợi nhuận Ròng (Profit)
Đề thi rất hay gài bẫy phân biệt giữa **Payoff (Dòng tiền thực nhận tại $T$)** và **Profit (Lợi nhuận sau khi đã trừ phí mua $C_0$ hoặc $P_0$)**:

| Vị thế (Position) | Payoff tại đáo hạn ($T$) | Lợi nhuận ròng (Profit) | Điểm hòa vốn (Breakeven) | Lỗ tối đa (Max Loss) | Lãi tối đa (Max Gain) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Long Call** | $\max(S_T - K, 0)$ | $\max(S_T - K, 0) - C_0$ | $S_T^* = K + C_0$ | $-C_0$ | Vô hạn ($\infty$) |
| **Short Call** | $-\max(S_T - K, 0)$ | $C_0 - \max(S_T - K, 0)$ | $S_T^* = K + C_0$ | Vô hạn ($-\infty$) | $+C_0$ |
| **Long Put** | $\max(K - S_T, 0)$ | $\max(K - S_T, 0) - P_0$ | $S_T^* = K - P_0$ | $-P_0$ | $K - P_0$ (khi $S_T=0$) |
| **Short Put** | $-\max(K - S_T, 0)$ | $P_0 - \max(K - S_T, 0)$ | $S_T^* = K - P_0$ | $-(K - P_0)$ | $+P_0$ |

---

## 2.3. Các Chiến lược Quyền chọn Kinh điển (Option Strategies)

### 1. Protective Put (Bảo hiểm Danh mục - Portfolio Insurance)
- **Cấu trúc**: Mua Cổ phiếu ($S_0$) + Mua Quyền chọn Bán ($P_0$, Strike $K$).
- **Payoff tại $T$**:
  - Nếu $S_T \le K$: Cổ phiếu trị giá $S_T$, Put sinh lời $K - S_T \implies \text{Tổng Payoff} = S_T + (K - S_T) = K$.
  - Nếu $S_T > K$: Put hết hạn ($0$), Cổ phiếu trị giá $S_T \implies \text{Tổng Payoff} = S_T$.
  - $\implies \text{Payoff} = \max(S_T, K)$.
- **Bản chất kinh tế**: Bạn khóa mức giá sàn bảo vệ tài sản tại $K$. Dù thị trường có sụp đổ về 0, bạn vẫn thu về chắc chắn ít nhất $K$. Nếu thị trường tăng vọt, bạn vẫn hưởng trọn vẹn mức tăng! Chi phí phải trả là phí quyền chọn $P_0$.

### 2. Covered Call (Bán Call Có bảo đảm)
- **Cấu trúc**: Mua Cổ phiếu ($S_0$) + Bán Quyền chọn Mua (Short Call, $-C_0$, Strike $K$).
- **Payoff tại $T$**:
  - Nếu $S_T \le K$: Call hết hạn ($0$) $\implies \text{Payoff} = S_T$.
  - Nếu $S_T > K$: Bị đòi thực thi call $-(S_T - K) \implies \text{Payoff} = S_T - (S_T - K) = K$.
  - $\implies \text{Payoff} = \min(S_T, K)$.
- **Bản chất kinh tế**: Tăng thêm thu nhập từ phí bán call ($C_0$) trong giai đoạn thị trường đi ngang, đổi lại bạn phải từ bỏ toàn bộ phần lợi nhuận tăng giá vượt quá mức $K$.

### 3. Spreads (Chiến lược Chênh lệch Giá)
- **Bull Call Spread (Đầu cơ Giá lên có giới hạn)**:
  - Mua Call ở giá thực hiện thấp ($K_L$) + Bán Call ở giá thực hiện cao ($K_H > K_L$).
  - Chi phí ban đầu: $C(K_L) - C(K_H) > 0$ (Net Debit).
  - Payoff: Bằng $0$ nếu $S_T \le K_L$; Bằng $S_T - K_L$ nếu $K_L < S_T < K_H$; Bằng $K_H - K_L$ nếu $S_T \ge K_H$.
  - Giúp giảm chi phí mua call, nhưng chấp nhận chặn trần lợi nhuận tối đa ở mức $K_H - K_L$.
- **Bear Put Spread (Đầu cơ Giá xuống có giới hạn)**:
  - Mua Put ở giá thực hiện cao ($K_H$) + Bán Put ở giá thực hiện thấp ($K_L < K_H$).
  - Chi phí ban đầu: $P(K_H) - P(K_L) > 0$.
  - Payoff: Bằng $K_H - K_L$ nếu $S_T \le K_L$; Bằng $K_H - S_T$ nếu $K_L < S_T < K_H$; Bằng $0$ nếu $S_T \ge K_H$.

### 4. Đặt cược vào Độ biến động (Volatility Bets)
- **Straddle (Mua Quyền chọn Kép)**:
  - Mua 1 Call ($K$) + Mua 1 Put ($K$) cùng ngày đáo hạn $T$.
  - $\text{Payoff} = \max(S_T - K, 0) + \max(K - S_T, 0) = |S_T - K|$.
  - **Khi nào dùng?**: Khi bạn dự báo **thị trường sẽ biến động cực mạnh** (Large Price Move) nhưng không biết tăng hay giảm (ví dụ trước thềm công bố phán quyết FDA của công ty dược, hoặc bầu cử tổng thống).
- **Strangle**: Tương tự Straddle nhưng mua Call ở $K_H$ và Put ở $K_L < K_H$ $\implies$ Rẻ hơn Straddle nhưng đòi hỏi giá phải biến động mạnh hơn nữa mới hòa vốn.

---

## 2.4. Ngang giá Mua - Bán (Put-Call Parity) & Vị thế Nhân tạo
Đây là **ĐỊNH LUẬT BẤT BIẾN QUAN TRỌNG NHẤT** của Lecture 10!

### Định lý Ngang giá Mua - Bán (Put-Call Parity):
Xem xét 2 danh mục đầu tư vào ngày hôm nay ($t=0$):
1. **Danh mục A (Protective Put)**: Mua 1 Cổ phiếu ($S_0$) + Mua 1 European Put ($P_0$, Strike $K$, hạn $T$). Chi phí hôm nay $= S_0 + P_0$.
2. **Danh mục B (Fiduciary Call)**: Mua 1 European Call ($C_0$, Strike $K$, hạn $T$) + Mua 1 Trái phiếu phi rủi ro mệnh giá $K$ đáo hạn tại $T$ (chi phí $= PV(K)$). Chi phí hôm nay $= C_0 + PV(K)$.

**Bảng so sánh dòng tiền tại ngày đáo hạn ($T$):**
| Trạng thái tương lai | Dòng tiền Danh mục A ($S + P$) | Dòng tiền Danh mục B ($C + \text{Bond}$) |
| :--- | :---: | :---: |
| Nếu $S_T \le K$ | $S_T + (K - S_T) = K$ | $0 + K = K$ |
| Nếu $S_T > K$ | $S_T + 0 = S_T$ | $(S_T - K) + K = S_T$ |
| **Kết luận tại $T$** | $\mathbf{\max(S_T, K)}$ | $\mathbf{\max(S_T, K)}$ |

Vì ở MỌI kịch bản tương lai, 2 danh mục đều tạo ra **chính xác cùng một dòng tiền**, nên theo **Luật Một Giá (Law of One Price)**, chi phí ban đầu hôm nay của chúng bắt buộc phải bằng nhau:
$$\mathbf{S_0 + P_0 = C_0 + PV(K)}$$
hay:
$$\mathbf{C_0 - P_0 = S_0 - PV(K)}$$

Trong đó:
- Với lãi suất hiệu dụng năm $r_f$ (EAR): $PV(K) = \frac{K}{(1 + r_f)^T}$
- Với lãi suất ghép liên tục $r$ (Continuously Compounded): $PV(K) = K e^{-r T}$
- Nếu cổ phiếu có chi trả cổ tức bằng tiền mặt với giá trị hiện tại là $PV(D)$ trước khi đáo hạn:
  $$\mathbf{C_0 - P_0 = S_0 - PV(D) - PV(K)}$$

### Các Vị thế Nhân tạo (Synthetic Positions):
Từ đẳng thức Put-Call Parity, ta có thể mô phỏng bất kỳ tài sản nào bằng 3 tài sản còn lại:
- **Synthetic Call (Call nhân tạo)**: $C = S + P - PV(K)$ (Mua cổ phiếu + Mua put + Vay tiền ngân hàng).
- **Synthetic Put (Put nhân tạo)**: $P = C + PV(K) - S$ (Mua call + Gửi tiết kiệm - Bán khống cổ phiếu).
- **Synthetic Stock (Cổ phiếu nhân tạo)**: $S = C - P + PV(K)$ (Mua call + Bán put + Gửi tiết kiệm).
- **Synthetic Bond (Trái phiếu nhân tạo)**: $PV(K) = S + P - C$.

---

## 2.5. Các Yếu tố Tác động lên Giá Quyền chọn (Comparative Statics)
Bảng tra cứu quy luật tác động khi một yếu tố tăng lên (các yếu tố khác giữ nguyên):

| Yếu tố tăng lên (Increase in) | Ký hiệu | Giá Call ($C$) | Giá Put ($P$) | Giải thích bản chất kinh tế (Intuition) |
| :--- | :---: | :---: | :---: | :--- |
| **Giá cổ phiếu hiện tại (Stock Price)** | $S_0 \uparrow$ | **TĂNG ($\uparrow$)** | **GIẢM ($\downarrow$)** | Cổ phiếu tăng làm tăng khả năng Call ITM, giảm khả năng Put ITM. |
| **Giá thực hiện (Strike Price)** | $K \uparrow$ | **GIẢM ($\downarrow$)** | **TĂNG ($\uparrow$)** | Mua đắt hơn thì dở ($C \downarrow$), bán đắt hơn thì lời ($P \uparrow$). |
| **Độ biến động (Volatility)** | $\sigma \uparrow$ | **TĂNG ($\uparrow$)** | **TĂNG ($\uparrow$)** | Quyền chọn có đệm chặn lỗ bằng 0. Biến động càng mạnh thì tiềm năng lãi cực đại càng lớn, trong khi phần lỗ vẫn bị chặn ở 0! |
| **Lãi suất phi rủi ro (Risk-Free Rate)** | $r \uparrow$ | **TĂNG ($\uparrow$)** | **GIẢM ($\downarrow$)** | $r \uparrow \implies PV(K) \downarrow$. Mua Call hoãn trả tiền $K \implies$ có lợi ($C \uparrow$). Bán Put hoãn thu tiền $K \implies$ thiệt hại ($P \downarrow$). |
| **Cổ tức kỳ vọng (Expected Dividend)** | $D \uparrow$ | **GIẢM ($\downarrow$)** | **TĂNG ($\uparrow$)** | Sau ngày chia cổ tức, giá cổ phiếu bị trừ $D \implies S \downarrow \implies C \downarrow, P \uparrow$. |
| **Thời gian đáo hạn (Time to Expiry)** | $T \uparrow$ | **TĂNG / Phụ thuộc** | **TĂNG / Phụ thuộc** | Luôn luôn đúng với quyền chọn Mỹ ($T \uparrow \implies C_A \uparrow, P_A \uparrow$). Với quyền chọn Âu có thể ngoại lệ nếu cổ tức quá lớn hoặc lãi suất cao. |

---

## 2.6. Thực thi Sớm Quyền chọn Mỹ (Early Exercise: American Options)
- **Quyền chọn Mua Mỹ KHÔNG CỔ TỨC (American Call on Non-Dividend Stock)**:
  - **NGUYÊN TẮC VÀNG**: **KHÔNG BAO GIỜ THỰC THI SỚM** ($C_A = C_E$).
  - *Tại sao?*: Nếu muốn rút lui, việc **bán lại quyền chọn trên thị trường** luôn thu được nhiều tiền hơn là thực thi! Khi thực thi, bạn chỉ nhận được Intrinsic Value ($S_t - K$), vứt bỏ toàn bộ Time Value và mất quyền giữ tiền mặt để hưởng lãi suất ($PV(K) < K$).
- **Quyền chọn Mua Mỹ CÓ CỔ TỨC**:
  - Có thể tối ưu khi thực thi sớm **ngay trước ngày giao dịch không hưởng quyền (cum-dividend date)** nếu cổ tức tiền mặt lớn hơn giá trị thời gian của quyền chọn: $D > K(1 - e^{-r(T-t)})$.
- **Quyền chọn Bán Mỹ (American Put)**:
  - **CÓ THỂ VÀ NÊN THỰC THI SỚM** khi quyền chọn rơi vào trạng thái **In-the-Money sâu (Deep ITM)**!
  - *Tại sao?*: Khi $S_t \to 0$, giá trị nội tại đạt mức tối đa là $K$. Việc chờ đợi chỉ làm bạn bị thiệt lãi suất trên khoản tiền $K$ đáng lẽ thu về được ngay hôm nay! Vì vậy, $P_A > P_E$.

---

## 2.7. Ứng dụng trong Tài chính Doanh nghiệp (Merton Structural Model)
Mô hình Cấu trúc Vốn của Robert Merton (Nobel Kinh tế 1997) nhìn nhận doanh nghiệp dưới lăng kính Quyền chọn:
- Giả sử doanh nghiệp có tổng tài sản hoạt động $V_t$ và phát hành trái phiếu chiết khấu zero-coupon có mệnh giá $F$, đáo hạn tại $T$.
- Tại thời điểm đáo hạn $T$:
  - Nếu $V_T > F$: Doanh nghiệp trả đủ nợ $F$ cho trái chủ, phần thặng dư $V_T - F$ thuộc về cổ đông.
  - Nếu $V_T \le F$: Doanh nghiệp vỡ nợ (Default). Do trách nhiệm hữu hạn (Limited Liability), cổ đông giao toàn bộ tài sản $V_T$ cho trái chủ và ra về tay trắng ($0$).
- **Kết luận đột phá của Merton**:
  1. **Vốn chủ sở hữu (Equity - $E_T$) thực chất là một Call Option trên tài sản công ty** với giá thực hiện bằng mệnh giá nợ:
     $$E_T = \max(V_T - F, 0)$$
  2. **Trái phiếu rủi ro (Risky Debt - $D_T$)** có giá trị bằng:
     $$D_T = \min(V_T, F) = F - \max(F - V_T, 0) = \text{Trái phiếu phi rủi ro} - \text{Put Option trên tài sản}$$
  3. Giá trị doanh nghiệp hôm nay:
     $$V_0 = E_0 + D_0$$
  4. Lợi suất cam kết (Promised Yield to Maturity $y$) của trái phiếu thỏa mãn:
     $$D_0 = \frac{F}{(1 + y)^T} \implies y = \left(\frac{F}{D_0}\right)^{1/T} - 1$$
  5. Phần bù rủi ro tín dụng (Credit Spread):
     $$\text{Credit Spread} = y - r_f$$

---

## 2.8. Giới hạn Giá Quyền chọn (Bounds) & Box Spread
1. **Biên dưới Quyền chọn Âu (European Lower Bounds)**:
   - Call: $C \ge \max(0, S_0 - PV(K))$
   - Put: $P \ge \max(0, PV(K) - S_0)$
2. **Biên trên (Upper Bounds)**:
   - $C \le S_0$ (Quyền mua không thể đắt hơn chính cổ phiếu đó).
   - $P \le PV(K)$ với quyền chọn Âu; $P_A \le K$ với quyền chọn Mỹ.
3. **Box Spread (Hộp chênh lệch giá)**:
   - Kết hợp 1 Bull Call Spread ($K_L, K_H$) và 1 Bear Put Spread ($K_L, K_H$).
   - Tại mọi trạng thái tương lai, tổng Payoff **luôn luôn bằng đúng $K_H - K_L$**!
   - Vì không có rủi ro, giá của Box Spread hôm nay bắt buộc phải bằng:
     $$\mathbf{\text{Price of Box Spread} = PV(K_H - K_L) = (K_H - K_L) e^{-r T}}$$
   - Nếu thị trường niêm yết lệch khỏi con số này $\implies$ Cơ hội kinh doanh chênh lệch giá không rủi ro 100%!

---

# 3. LECTURE 10: GIẢI CHI TIẾT 10 CÂU HỎI TRÊN LỚP
*(STEP-BY-STEP SOLUTIONS TO QUESTIONS 1 - 10)*

---

### Question 1: Call Payoff for Holder
**Đề bài gốc (Original Text):**  
You own a European call option on Gamma stock with a strike price of $\$65$. The option expires in four months.
- If Gamma trades at $\$82$ at expiration, what is your payoff per share?
- If Gamma instead trades at $\$58$, what is your payoff per share?

**Dịch đề & Hướng dẫn (Vietnamese):**  
Bạn sở hữu (Long) 1 quyền chọn mua kiểu Âu trên cổ phiếu Gamma, giá thực hiện $K = \$65$, đáo hạn sau 4 tháng.
- Nếu tại ngày đáo hạn giá cổ phiếu $S_T = \$82$, dòng tiền (payoff) mỗi cổ phiếu là bao nhiêu?
- Nếu giá cổ phiếu tại đáo hạn $S_T = \$58$, dòng tiền mỗi cổ phiếu là bao nhiêu?

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. Công thức dòng tiền của người mua Call (Long Call Payoff):
   $$\text{Payoff} = \max(S_T - K, 0)$$
2. Trường hợp 1: $S_T = \$82$:
   - Vì $S_T = 82 > K = 65$, quyền chọn ở trạng thái In-the-Money (ITM).
   - Người nắm giữ sẽ thực thi quyền để mua ở giá 65 và bán ra thị trường ở giá 82:
     $$\text{Payoff} = \max(82 - 65, 0) = \mathbf{\$17.00}$$
3. Trường hợp 2: $S_T = \$58$:
   - Vì $S_T = 58 < K = 65$, quyền chọn ở trạng thái Out-of-the-Money (OTM).
   - Mua trên thị trường tự do ở giá 58 rẻ hơn mua bằng quyền ở giá 65, nên bạn bỏ quyền (không thực thi):
     $$\text{Payoff} = \max(58 - 65, 0) = \mathbf{\$0.00}$$

---

### Question 2: Call Payoff for Writer
**Đề bài gốc (Original Text):**  
You wrote a European call option on Gamma stock with a strike price of $\$65$. The option expires in four months.
- If Gamma trades at $\$82$ at expiration, what is your payoff per share as the writer?
- If Gamma instead trades at $\$58$, what is your payoff per share as the writer?

**Dịch đề & Hướng dẫn (Vietnamese):**  
Bạn phát hành/bán (Short/Write) 1 quyền chọn mua kiểu Âu trên cổ phiếu Gamma, giá thực hiện $K = \$65$, đáo hạn sau 4 tháng.
- Nếu $S_T = \$82$, payoff của người bán là bao nhiêu?
- Nếu $S_T = \$58$, payoff của người bán là bao nhiêu?

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. Bản chất: Người bán quyền chọn nhận tiền cọc trước và chịu nghĩa vụ phục tùng quyết định của người mua. Dòng tiền của bên bán là đối xứng ngược dấu (Zero-Sum) với bên mua:
   $$\text{Payoff}_{\text{writer}} = -\max(S_T - K, 0)$$
2. Trường hợp 1: $S_T = \$82$:
   - Bên mua thực thi quyền đòi mua ở giá 65. Người bán bắt buộc phải mua cổ phiếu ngoài thị trường ở giá 82 để giao cho bên mua ở giá 65:
     $$\text{Payoff}_{\text{writer}} = -\max(82 - 65, 0) = \mathbf{-\$17.00} \quad (\text{Lỗ } \$17 \text{ mỗi cổ phiếu})$$
3. Trường hợp 2: $S_T = \$58$:
   - Bên mua không thực thi quyền chọn:
     $$\text{Payoff}_{\text{writer}} = -\max(58 - 65, 0) = \mathbf{\$0.00}$$

---

### Question 3: Maximum Loss for Option Writers
**Đề bài gốc (Original Text):**  
Delta considers writing either a European call or a European put on the same stock, with a strike of $\$80$ and nine months to expiration.
- Neither position is hedged.
- Ignore premium income.
- Compare the maximum possible loss per share on the two positions. Which direction of stock-price movement creates a loss for each writer?

**Dịch đề & Hướng dẫn (Vietnamese):**  
Delta cân nhắc bán (write) 1 call hoặc 1 put kiểu Âu trên cùng cổ phiếu, giá thực hiện $K = \$80$, hạn 9 tháng. Hai vị thế đều không phòng hộ, bỏ qua thu nhập từ phí quyền chọn.
- So sánh mức lỗ tối đa có thể xảy ra trên mỗi cổ phiếu của 2 vị thế.
- Hướng biến động nào của giá cổ phiếu sẽ gây ra thua lỗ cho mỗi bên bán?

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. **Đối với bên bán Call (Short Call Writer)**:
   - Dòng tiền: $-\max(S_T - 80, 0)$.
   - Hướng giá gây lỗ: **Giá cổ phiếu TĂNG ($S_T > 80$)**. Cổ phiếu càng tăng giá, người bán càng lỗ nặng.
   - Mức lỗ tối đa: Do giá cổ phiếu về mặt lý thuyết có thể tăng đến vô cùng ($S_T \to +\infty$), nên **mức lỗ tối đa là KHÔNG GIỚI HẠN / VÔ HẠN (Unlimited Loss: $-\infty$)**.
2. **Đối với bên bán Put (Short Put Writer)**:
   - Dòng tiền: $-\max(80 - S_T, 0)$.
   - Hướng giá gây lỗ: **Giá cổ phiếu GIẢM ($S_T < 80$)**. Cổ phiếu càng rớt giá, người bán càng lỗ.
   - Mức lỗ tối đa: Giá cổ phiếu chỉ có thể giảm tối đa về mức $0$ (công ty phá sản hoàn toàn). Khi $S_T = 0$, mức lỗ tối đa đạt đỉnh:
     $$\text{Max Loss} = -(80 - 0) = \mathbf{-\$80.00 \text{ per share}}$$
3. **Kết luận so sánh**: Vị thế Short Call có mức độ rủi ro tiềm tàng nguy hiểm hơn nhiều (lỗ vô hạn) so với Short Put (mức lỗ được chặn cận dưới ở đúng giá thực hiện $K = \$80$).

---

### Question 4: Pricing Call via Put-Call Parity
**Đề bài gốc (Original Text):**  
Epsilon stock trades at $\$72$ and pays no dividends.
- A European put with a strike of $\$75$ expires in nine months and costs $\$6.20$.
- The annual effective risk-free rate is 5%.
- What is the no-arbitrage price of a European call with the same strike and expiration?

**Dịch đề & Hướng dẫn (Vietnamese):**  
Cổ phiếu Epsilon có giá $S_0 = \$72$, không trả cổ tức. Quyền chọn bán kiểu Âu giá thực hiện $K = \$75$, hạn 9 tháng ($T = 9/12 = 0.75$ năm), giá $P = \$6.20$. Lãi suất phi rủi ro hiệu dụng hàng năm $r_f = 5\%$ (EAR). Tìm giá phi chênh lệch giá của quyền chọn mua kiểu Âu cùng strike và đáo hạn?

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. Áp dụng Định lý Ngang giá Mua - Bán (Put-Call Parity):
   $$S_0 + P = C + PV(K) \implies C = S_0 + P - PV(K)$$
2. Tính giá trị hiện tại của giá thực hiện $PV(K)$ với lãi suất hiệu dụng năm (EAR):
   $$PV(K) = \frac{K}{(1 + r_f)^T} = \frac{75}{(1 + 0.05)^{0.75}} = \frac{75}{1.05^{0.75}}$$
   - Bấm máy: $1.05^{0.75} \approx 1.037267$
   - $PV(K) = \frac{75}{1.037267} \approx \$72.3052$
3. Tính giá Call ($C$):
   $$C = 72.00 + 6.20 - 72.3052 = 78.20 - 72.3052 = \mathbf{\$5.8948 \approx \$5.89}$$

---

### Question 5: Implied Risk-Free Rate from Parity
**Đề bài gốc (Original Text):**  
European call and put options on Zeta have a strike of $\$90$ and expire in nine months.
- The call costs $\$8.40$ and the put costs $\$4.10$.
- Zeta stock trades at $\$92$ and pays no dividends.
- What annual continuously compounded risk-free rate is implied by these prices?

**Dịch đề & Hướng dẫn (Vietnamese):**  
Quyền chọn mua và bán kiểu Âu trên Zeta có $K = \$90$, hạn 9 tháng ($T = 0.75$ năm). $C = \$8.40$, $P = \$4.10$, $S_0 = \$92$, không cổ tức. Xác định lãi suất phi rủi ro ghép lãi liên tục hàng năm ($r$) được hàm ý bởi các mức giá này?

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. Viết công thức Put-Call Parity với lãi suất ghép liên tục:
   $$C - P = S_0 - K e^{-r T}$$
2. Thay các số liệu đề bài cho vào phương trình:
   $$8.40 - 4.10 = 92 - 90 e^{-r \times 0.75}$$
   $$4.30 = 92 - 90 e^{-0.75 r}$$
3. Giải tìm $r$:
   $$90 e^{-0.75 r} = 92 - 4.30 = 87.70$$
   $$e^{-0.75 r} = \frac{87.70}{90} \approx 0.974444$$
   Lấy logarit tự nhiên ($\ln$) hai vế:
   $$-0.75 r = \ln(0.974444) \approx -0.025887$$
   $$r = \frac{-0.025887}{-0.75} \approx \mathbf{0.034517 \approx 3.45\% \text{ / năm}}$$

---

### Question 6: Arbitrage Opportunity and Strategy Table
**Đề bài gốc (Original Text):**  
Eta stock trades at $\$54$ and pays no dividends.
- One-year European call and put options have the same strike of $\$50$.
- The put costs $\$3.40$ and the call costs $\$9.00$.
- The annual effective risk-free rate is 6%.
- Assume frictionless borrowing, lending and short selling.
- Is there an arbitrage opportunity? If so, specify the trades and show the cash flows today and at expiration.

**Dịch đề & Hướng dẫn (Vietnamese):**  
Cổ phiếu Eta giá $S_0 = \$54$, không cổ tức. Quyền chọn 1 năm ($T=1$), $K = \$50$. $P = \$3.40$, $C = \$9.00$, $r_f = 6\%$ (EAR). Giả định thị trường hoàn hảo. Có cơ hội kinh doanh chênh lệch giá (arbitrage) không? Nếu có, hãy nêu các giao dịch và lập bảng dòng tiền hôm nay và khi đáo hạn.

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. **Kiểm tra điều kiện Put-Call Parity**:
   - Giá trị Danh mục Protective Put trên thị trường:
     $$\text{Cost}(S + P) = S_0 + P = 54 + 3.40 = \mathbf{\$57.40}$$
   - Giá trị Danh mục Fiduciary Call trên thị trường:
     $$\text{Cost}(C + \text{Bond}) = C + \frac{K}{1 + r_f} = 9.00 + \frac{50}{1.06} = 9.00 + 47.1698 = \mathbf{\$56.1698 \approx \$56.17}$$
   - So sánh:
     $$S_0 + P > C + PV(K) \quad (57.40 > 56.17)$$
   - **Kết luận**: Đang có cơ hội Arbitrage!
     - Danh mục **Protective Put ($S + P$) bị ĐẮT (Overvalued)** $\implies$ **BÁN (Short/Sell)**.
     - Danh mục **Fiduciary Call ($C + \text{Bond}$) bị RẺ (Undervalued)** $\implies$ **MUA (Long/Buy)**.

2. **Chiến lược Giao dịch Hôm nay ($t=0$)**:
   - Bán khống 1 cổ phiếu Eta (Short stock): Thu về $+54.00$
   - Bán (phát hành) 1 quyền chọn bán (Write Put): Thu về $+3.40$
   - Mua 1 quyền chọn mua (Buy Call): Trả ra $-9.00$
   - Cho vay ngân hàng (Mua Zero-coupon bond trả 50 tại $T=1$): Trả ra $-\frac{50}{1.06} = -47.17$
   - **Lợi nhuận Arbitrage bỏ túi ngay hôm nay**:
     $$\Pi_0 = +54.00 + 3.40 - 9.00 - 47.17 = \mathbf{+\$1.23 > 0}$$

3. **Bảng Dòng tiền Toàn diện (Cash Flow Table)**:

| Giao dịch (Trades) | Dòng tiền hôm nay ($t=0$) | Dòng tiền khi đáo hạn ($S_T \le 50$) | Dòng tiền khi đáo hạn ($S_T > 50$) |
| :--- | :---: | :---: | :---: |
| Bán khống cổ phiếu (Short stock) | $+54.00$ | Mua trả lại: $-S_T$ | Mua trả lại: $-S_T$ |
| Bán quyền chọn bán (Short Put) | $+3.40$ | Bị thực thi: $-(50 - S_T)$ | Hết hạn: $0$ |
| Mua quyền chọn mua (Long Call) | $-9.00$ | Hết hạn: $0$ | Thực thi quyền: $+(S_T - 50)$ |
| Cho vay rủi ro 0 (Lend $PV(50)$) | $-47.17$ | Thu hồi gốc + lãi: $+50$ | Thu hồi gốc + lãi: $+50$ |
| **DÒNG TIỀN RÒNG (NET CASH FLOW)** | $\mathbf{+\$1.23}$ | $-S_T - 50 + S_T + 50 = \mathbf{0}$ | $-S_T + S_T - 50 + 50 = \mathbf{0}$ |

*Nhận xét*: Bất kể giá cổ phiếu tương lai lên 100 hay rớt về 0, dòng tiền tương lai luôn tự triệt tiêu bằng 0. Nhà đầu tư kiếm được **chắc chắn $\$1.23$ tiền lời ngay hôm nay** mà không chịu rủi ro và không cần bỏ vốn tự có!

---

### Question 7: Intrinsic Value and Time Value Calculation
**Đề bài gốc (Original Text):**  
Theta stock trades at $\$88$ and pays no dividends.
- European call and put options have a strike of $\$95$ and six months to expiration.
- The put costs $\$10.80$.
- The risk-free rate is 4.5% per year, continuously compounded.
- Find the intrinsic value and time value of each option.

**Dịch đề & Hướng dẫn (Vietnamese):**  
Cổ phiếu Theta giá $S_0 = \$88$, không cổ tức. Quyền chọn Âu $K = \$95$, $T = 6/12 = 0.5$ năm. Giá Put $P = \$10.80$. Lãi suất phi rủi ro $r = 4.5\%$ ghép lãi liên tục. Tìm giá trị nội tại và giá trị thời gian của mỗi quyền chọn?

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. **Xét Quyền chọn Bán (Put Option)**:
   - Giá trị nội tại (Intrinsic Value):
     $$\text{Intrinsic Value}(P) = \max(K - S_0, 0) = \max(95 - 88, 0) = \mathbf{\$7.00}$$
   - Giá trị thời gian (Time Value):
     $$\text{Time Value}(P) = \text{Option Price} - \text{Intrinsic Value} = 10.80 - 7.00 = \mathbf{\$3.80}$$

2. **Xét Quyền chọn Mua (Call Option)**:
   - Giá trị nội tại (Intrinsic Value):
     $$\text{Intrinsic Value}(C) = \max(S_0 - K, 0) = \max(88 - 95, 0) = \mathbf{\$0.00} \quad (\text{Do Call đang OTM})$$
   - Để tìm Giá trị thời gian, trước tiên phải tìm giá thị trường lý thuyết của Call ($C$) qua Put-Call Parity:
     $$C = S_0 + P - K e^{-r T}$$
     $$PV(K) = 95 e^{-0.045 \times 0.5} = 95 e^{-0.0225} \approx 95 \times 0.977751 = \$92.8864$$
     $$C = 88.00 + 10.80 - 92.8864 = 98.80 - 92.8864 = \mathbf{\$5.9136 \approx \$5.91}$$
   - Giá trị thời gian của Call:
     $$\text{Time Value}(C) = C - \text{Intrinsic Value} = 5.9136 - 0.00 = \mathbf{\$5.9136 \approx \$5.91}$$

---

### Question 8: Negative Time Value and Dividend Yield
**Đề bài gốc (Original Text):**  
The Iota Index is at 1,800. A one-year European call with a strike of 1,200 has negative time value, so $C < S_0 - K$.
- The annual effective risk-free rate is 5%.
- A single known cash dividend of $D$ index points is paid at year-end, immediately before the option expires.
- What can you infer about the annual dividend yield $D/S_0$?

**Dịch đề & Hướng dẫn (Vietnamese):**  
Chỉ số Iota đang ở mức $S_0 = 1,800$. Quyền chọn mua kiểu Âu 1 năm ($T=1$), $K = 1,200$ có giá trị thời gian bị âm, nghĩa là $C < S_0 - K$. Lãi suất phi rủi ro hiệu dụng năm là $5\%$ ($r_f = 0.05$). Một khoản cổ tức tiền mặt $D$ điểm được trả vào cuối năm ngay trước khi quyền chọn đáo hạn. Bạn có thể suy ra điều gì về tỷ suất cổ tức hàng năm $D/S_0$?

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. **Thiết lập công thức Put-Call Parity khi có cổ tức**:
   $$C - P = S_0 - PV(D) - PV(K)$$
   $$C = S_0 - PV(D) - PV(K) + P$$
2. **Khai thác điều kiện biên không âm của Put ($P \ge 0$)**:
   Vì giá quyền chọn bán không thể âm ($P \ge 0$), ta suy ra cận dưới của Call:
   $$C \ge S_0 - PV(D) - PV(K)$$
3. **Kết hợp với điều kiện đề bài cho ($C < S_0 - K$)**:
   $$S_0 - PV(D) - PV(K) \le C < S_0 - K$$
   $$\implies S_0 - PV(D) - PV(K) < S_0 - K$$
   Triệt tiêu $S_0$ ở hai vế:
   $$- PV(D) - PV(K) < - K \implies PV(D) + PV(K) > K$$
   $$PV(D) > K - PV(K)$$
4. **Thay công thức chiết khấu với $T=1$ và $r_f = 5\%$**:
   - $PV(K) = \frac{K}{1 + r_f}$
   - Do cổ tức trả vào cuối năm ($T=1$), $PV(D) = \frac{D}{1 + r_f}$
   $$\frac{D}{1 + r_f} > K - \frac{K}{1 + r_f} = K \left(1 - \frac{1}{1 + r_f}\right) = \frac{K \cdot r_f}{1 + r_f}$$
   Nhân cả hai vế với $(1 + r_f)$:
   $$\mathbf{D > K \cdot r_f}$$
5. **Tính toán số liệu cụ thể**:
   - $D > 1,200 \times 0.05 = \mathbf{60 \text{ điểm}}$
   - Tỷ suất cổ tức (Dividend Yield):
     $$\frac{D}{S_0} > \frac{K \cdot r_f}{S_0} = \frac{60}{1,800} = \frac{1}{30} \approx \mathbf{3.33\%}$$
- **Kết luận**: Tỷ suất cổ tức hàng năm của chỉ số bắt buộc phải **lớn hơn 3.33%** ($D/S_0 > 3.33\%$).

---

### Question 9: Risky Debt, Promised Yield and Credit Spread
**Đề bài gốc (Original Text):**  
Lambda has no debt and 150 million shares trading at $\$320$ each.
- The firm plans to issue zero-coupon debt with a face value of $\$36$ billion, due in two years.
- All issuance proceeds will be paid immediately as a special dividend; operating assets remain unchanged.
- Assume limited liability, no bankruptcy costs and no further payouts before the debt matures.
- A two-year call on the firm's assets, expressed per existing share, has a strike of $\$240$ and a price of $\$110$.
- The annual effective risk-free rate is 3%.
- Estimate the debt's annual effective promised yield and its credit spread.

**Dịch đề & Hướng dẫn (Vietnamese):**  
Lambda hiện không có nợ, có 150 triệu cổ phiếu đang giao dịch ở giá $\$320$/cổ phiếu. Doanh nghiệp dự định phát hành trái phiếu zero-coupon mệnh giá $\$36$ tỷ, đáo hạn sau 2 năm. Toàn bộ tiền thu được từ phát hành sẽ chi trả ngay lập tức làm cổ tức đặc biệt cho cổ đông; tài sản hoạt động kinh doanh không đổi. Một quyền chọn mua 2 năm trên tài sản công ty (tính trên mỗi cổ phiếu hiện hữu) có giá thực hiện $\$240$ và giá thị trường $\$110$. Lãi suất phi rủi ro hiệu dụng năm là 3%. Hãy ước tính lợi suất cam kết hàng năm và phần bù tín dụng (credit spread) của khoản nợ này.

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. **Quy đổi các đại lượng về cơ sở "trên mỗi cổ phiếu hiện hữu" (Per-Share Basis)**:
   - Tổng giá trị tài sản ban đầu: $V_0 = 150\text{ triệu} \times \$320 = \$48\text{ tỷ}$ $\implies v_0 = \$320$/cổ phiếu.
   - Mệnh giá nợ quy về mỗi cổ phiếu:
     $$k = \frac{\text{Tổng mệnh giá nợ}}{\text{Số lượng cổ phiếu}} = \frac{\$36,000,000,000}{150,000,000} = \mathbf{\$240 \text{ / cổ phiếu}}$$
     *(Nhận xét: Trùng khớp chính xác với Strike của hợp đồng Call: $K = \$240$!)*
2. **Áp dụng Mô hình Cấu trúc Vốn Merton**:
   - Cổ đông có quyền hưởng giá trị thặng dư của công ty sau khi trả nợ, được bảo vệ bởi trách nhiệm hữu hạn: $E_T = \max(V_T - F, 0)$.
   - Do đó, vốn chủ sở hữu trên mỗi cổ phiếu hôm nay chính là giá của Call Option trên tài sản:
     $$e_0 = \text{Call Price} = \mathbf{\$110 \text{ / cổ phiếu}}$$
   - Theo định luật bảo toàn giá trị (Modigliani-Miller / Law of Conservation of Value), tổng tài sản hoạt động của doanh nghiệp $v_0$ phân bổ thành nợ $d_0$ và vốn chủ $e_0$:
     $$v_0 = d_0 + e_0 \implies d_0 = v_0 - e_0$$
     $$d_0 = 320 - 110 = \mathbf{\$210 \text{ / cổ phiếu}}$$
     *(Tổng số tiền thu được từ đợt phát hành trái phiếu $= 210 \times 150\text{ triệu} = \$31.5\text{ tỷ}$)*.
3. **Tính Lợi suất Cam kết Đáo hạn (Promised Yield to Maturity - $y$)**:
   - Trái phiếu là loại zero-coupon: Nhà đầu tư bỏ ra $d_0 = \$210$ hôm nay để nhận về mệnh giá cam kết $k = \$240$ sau $T = 2$ năm:
     $$d_0 = \frac{k}{(1 + y)^2} \implies 210 = \frac{240}{(1 + y)^2}$$
     $$(1 + y)^2 = \frac{240}{210} = \frac{8}{7} \approx 1.142857$$
     $$1 + y = \sqrt{\frac{8}{7}} \approx 1.069045 \implies \mathbf{y \approx 6.9045\% \approx 6.90\% \text{ / năm}}$$
4. **Tính Phần bù Rủi ro Tín dụng (Credit Spread)**:
   - Với lãi suất phi rủi ro $r_f = 3\%$ (EAR):
     $$\text{Credit Spread} = y - r_f = 6.9045\% - 3.00\% = \mathbf{3.9045\% \approx 3.90\% \text{ / năm (hoặc 390 bps)}}$$

---

### Question 10: Put Valuation and Arbitrage Construction
**Đề bài gốc (Original Text):**  
Mu stock trades at $\$28$ and pays no dividends.
- A one-year European call with a strike of $\$30$ costs $\$2.60$.
- The annual effective risk-free rate is 4%.
- Assume frictionless borrowing, lending and short selling.
- What is the no-arbitrage price of a one-year European put with the same strike?
- If this put trades at $\$2.80$, is there an arbitrage opportunity? If so, construct the strategy's cash-flow table.

**Dịch đề & Hướng dẫn (Vietnamese):**  
Cổ phiếu Mu giá $S_0 = \$28$, không cổ tức. Call kiểu Âu 1 năm ($T=1$), $K = \$30$, giá $C = \$2.60$. Lãi suất phi rủi ro hiệu dụng năm là 4% ($r_f = 0.04$). Giả định thị trường hoàn hảo.
- Giá phi chênh lệch giá (no-arbitrage price) của quyền chọn bán 1 năm cùng strike là bao nhiêu?
- Nếu quyền chọn bán này đang được giao dịch ở giá $\$2.80$, có cơ hội arbitrage không? Hãy lập bảng dòng tiền cho chiến lược.

**Lời giải chi tiết từng bước (Step-by-Step Solution):**
1. **Tìm Giá Lý thuyết Không Chênh lệch Giá của Put ($P^*$)**:
   - Dùng Put-Call Parity:
     $$P^* = C + \frac{K}{1 + r_f} - S_0$$
     $$PV(K) = \frac{30}{1.04} \approx \$28.8462$$
     $$P^* = 2.60 + 28.8462 - 28.00 = \mathbf{\$3.4462 \approx \$3.45}$$

2. **Xác định Cơ hội Arbitrage khi Giá Thị trường $P_{\text{market}} = \$2.80$**:
   - So sánh: $P_{\text{market}} = \$2.80 < P^* = \$3.45$.
   - **Quyền chọn Bán trên thị trường đang BỊ ĐỊNH GIÁ QUÁ RẺ (Undervalued)**!
   - Tương đương:
     - Giá trị thị trường Protective Put: $S_0 + P = 28 + 2.80 = \mathbf{\$30.80}$
     - Giá trị thị trường Fiduciary Call: $C + PV(K) = 2.60 + 28.8462 = \mathbf{\$31.45}$
     - Protective Put ($30.80) rẻ hơn Fiduciary Call ($31.45).
   - **Quy tắc vàng**: Mua bên rẻ, Bán bên đắt!
     - **MUA Protective Put** (Mua 1 cổ phiếu + Mua 1 Put).
     - **BÁN Fiduciary Call** (Bán 1 Call + Đi vay ngân hàng khoản tiền $PV(K)$).

3. **Bảng Dòng tiền Toàn diện (Cash Flow Table)**:

| Giao dịch thực hiện | Dòng tiền hôm nay ($t=0$) | Dòng tiền tại $T=1$ ($S_T \le 30$) | Dòng tiền tại $T=1$ ($S_T > 30$) |
| :--- | :---: | :---: | :---: |
| Mua cổ phiếu Mu (Long Stock) | $-28.00$ | Trị giá: $+S_T$ | Trị giá: $+S_T$ |
| Mua quyền chọn bán (Long Put) | $-2.80$ | Thực thi quyền: $+(30 - S_T)$ | Hết hạn: $0$ |
| Bán quyền chọn mua (Short Call) | $+2.60$ | Hết hạn: $0$ | Bị thực thi: $-(S_T - 30)$ |
| Vay ngân hàng (Borrow $PV(30)$) | $+28.8462$ | Trả nợ gốc + lãi: $-30.00$ | Trả nợ gốc + lãi: $-30.00$ |
| **DÒNG TIỀN RÒNG (NET CASH FLOW)** | $\mathbf{+\$0.6462 \approx +\$0.65}$ | $S_T + 30 - S_T - 30 = \mathbf{0}$ | $S_T - S_T + 30 - 30 = \mathbf{0}$ |

*Kết luận*: Bạn bỏ túi ngay khoản tiền lời chắc chắn **$\$0.65$** hôm nay mà không chịu bất kỳ rủi ro nào trong tương lai.

---

# 4. LECTURE 11: ĐỊNH GIÁ QUYỀN CHỌN - NHỊ THỨC & BLACK-SCHOLES
*(OPTION PRICING: BINOMIAL MODEL & BLACK-SCHOLES)*

## 4.1. Mô hình Cây Nhị thức 1 Thời kỳ (One-Period Binomial Model)
### Tư tưởng Cốt lõi:
Giả định trong khoảng thời gian tiếp theo, giá cổ phiếu $S_0$ chỉ có thể đi theo 2 hướng:
- Tăng lên mức: $S_u = S_0 \times u$ ($u > 1$ là hệ số tăng giá) $\implies$ Quyền chọn có payoff $f_u$.
- Giảm xuống mức: $S_d = S_0 \times d$ ($d < 1$ là hệ số giảm giá) $\implies$ Quyền chọn có payoff $f_d$.
- Lãi suất phi rủi ro gộp cho kỳ đó là $r = 1 + r_f$. Để không có chênh lệch giá, bắt buộc: $d < r < u$.

### Phương pháp 1: Danh mục Sao chép (Replicating Portfolio - Delta Hedging)
Lập một danh mục gồm $\Delta$ cổ phiếu và $B$ tiền gửi/vay phi rủi ro:
$$\begin{cases} \text{Kịch bản Up:} & \Delta S_0 u + B r = f_u \\ \text{Kịch bản Down:} & \Delta S_0 d + B r = f_d \end{cases}$$
Trừ hai phương trình cho nhau, ta tìm được tỷ lệ phòng hộ Delta:
$$\mathbf{\Delta = \frac{f_u - f_d}{S_0(u - d)} = \frac{\text{Biến động giá quyền chọn}}{\text{Biến động giá cổ phiếu}}}$$
Khoản tiền gửi / vay:
$$\mathbf{B = \frac{u f_d - d f_u}{r(u - d)}}$$
Giá trị của quyền chọn hôm nay bằng đúng chi phí lập danh mục sao chép:
$$\mathbf{f_0 = \Delta S_0 + B}$$

---

## 4.2. Định giá Trung lập Rủi ro (Risk-Neutral Valuation)
### Khái niệm Đột phá:
Trong thế giới trung lập rủi ro, nhà đầu tư không đòi hỏi phần bù rủi ro, do đó tỷ suất sinh lời kỳ vọng của cổ phiếu phải đúng bằng lãi suất phi rủi ro $r$:
$$p \cdot (S_0 u) + (1 - p) \cdot (S_0 d) = S_0 r$$
Chia hai vế cho $S_0$:
$$p u + (1 - p) d = r \implies p(u - d) = r - d$$
$$\mathbf{p = \frac{r - d}{u - d}} \quad \text{và} \quad \mathbf{1 - p = \frac{u - r}{u - d}}$$
Trong đó $p$ được gọi là **Xác suất Trung lập Rủi ro (Risk-Neutral Probability)**.

### Định giá Quyền chọn:
Giá trị quyền chọn hôm nay chỉ đơn giản bằng **Kỳ vọng dòng tiền tương lai theo xác suất trung lập rủi ro, chiết khấu về hiện tại theo lãi suất phi rủi ro**:
$$\mathbf{f_0 = \frac{1}{r} \left[ p f_u + (1 - p) f_d \right]}$$

> [!IMPORTANT]
> **Tại sao phương pháp này đúng trong thế giới thực?**  
> Xác suất thực tế ngoài đời ($\pi_{\text{up}}$) của cổ phiếu là bao nhiêu không quan trọng! Dù nhà đầu tư ngoài đời có sợ rủi ro đến đâu, thì giá trị của quyền chọn đã bị "khóa cứng" bởi danh mục sao chép ($\Delta$ cổ phiếu và $B$ trái phiếu). Việc giả định thế giới trung lập rủi ro chỉ là một công cụ toán học thông minh giúp tính ra đúng mức giá phi chênh lệch giá duy nhất!

---

## 4.3. Cây Nhị thức Đa Thời kỳ & Quyền chọn Mỹ (Multi-Period Trees)
Với mô hình 2 thời kỳ ($t = 0 \to 1 \to 2$):
1. **Bước 1**: Vẽ cây giá cổ phiếu từ gốc đến các nút lá tại $T=2$:
   $$S_{uu} = S_0 u^2, \quad S_{ud} = S_0 u d, \quad S_{dd} = S_0 d^2$$
2. **Bước 2**: Tính payoff tại thời điểm đáo hạn $T=2$ cho từng nút lá:
   $$f_{uu} = \max(S_{uu} - K, 0), \quad f_{ud} = \max(S_{ud} - K, 0), \quad f_{dd} = \max(S_{dd} - K, 0)$$
3. **Bước 3: Quy nạp ngược (Backward Induction)**:
   - Tại $t=1$, tính giá trị tiếp tục (Continuation value $H_1$):
     $$H_1^u = \frac{p f_{uu} + (1-p) f_{ud}}{r}, \quad H_1^d = \frac{p f_{ud} + (1-p) f_{dd}}{r}$$
   - **Đối với Quyền chọn Mỹ (American Option)**: Tại mỗi nút $t=1$, so sánh giá trị tiếp tục $H$ với giá trị thực thi ngay (Immediate Exercise Value):
     $$f_1 = \max(\text{Exercise Value}, \text{Continuation Value}) = \max(\text{Intrinsic Value}, H_1)$$
4. **Bước 4**: Lùi về gốc $t=0$ để tìm giá trị hôm nay:
   $$f_0 = \frac{p f_1^u + (1-p) f_1^d}{r}$$

---

## 4.4. Mô hình Black-Scholes-Merton (BSOPM)
Khi chia thời gian thành vô số khoảng cực nhỏ ($N \to \infty$), phân phối nhị thức hội tụ về phân phối chuẩn Log (Lognormal Distribution), sinh ra công thức Black-Scholes:

### Công thức Định giá Quyền chọn Mua (Call):
$$\mathbf{C_0 = S_0 \cdot N(d_1) - K e^{-r T} \cdot N(d_2)}$$

### Công thức Định giá Quyền chọn Bán (Put):
$$\mathbf{P_0 = K e^{-r T} \cdot [1 - N(d_2)] - S_0 \cdot [1 - N(d_1)]}$$

Trong đó:
$$\mathbf{d_1 = \frac{\ln(S_0 / K) + (r + \frac{\sigma^2}{2}) T}{\sigma \sqrt{T}}}$$
$$\mathbf{d_2 = d_1 - \sigma \sqrt{T}}$$
- $S_0$: Giá cổ phiếu hiện tại
- $K$: Giá thực hiện
- $r$: Lãi suất phi rủi ro ghép liên tục hàng năm
- $\sigma$: Độ biến động hàng năm của tỷ suất sinh lời cổ phiếu
- $T$: Thời gian còn lại đến khi đáo hạn (tính bằng năm)
- $N(x)$: Hàm phân phối tích lũy chuẩn tắc (Standard Normal CDF)

### Ý nghĩa Kinh tế của Các Đại lượng trong Công thức:
- **$N(d_1) = \Delta_C$**: Tỷ lệ phòng hộ Delta của quyền chọn mua. Cho biết độ nhạy của giá quyền chọn theo giá cổ phiếu. Trong danh mục sao chép, bạn cần mua đúng $N(d_1)$ cổ phiếu.
- **$N(d_2) = \mathbb{Q}(S_T > K)$**: **Xác suất quyền chọn kết thúc ở trạng thái In-the-Money** (được thực thi) trong thế giới trung lập rủi ro!
- **$K e^{-r T} N(d_2)$**: Giá trị hiện tại của số tiền mặt kỳ vọng mà bạn sẽ phải trả ra khi thực thi mua cổ phiếu.
- Bản chất của Call:
  $$C_0 = \underbrace{S_0 \cdot N(d_1)}_{\text{Giá trị cổ phiếu nắm giữ}} - \underbrace{PV(K) \cdot N(d_2)}_{\text{Khoản vay tiền mặt nợ ngân hàng}}$$

---

## 4.5. Độ nhạy (Greeks), Đòn bẩy ($\Omega$) & Rủi ro Hệ thống ($\beta$)
- **Delta ($\Delta = \frac{\partial V}{\partial S}$)**:
  - Call Delta: $0 < \Delta_C = N(d_1) < 1$.
  - Put Delta: $-1 < \Delta_P = N(d_1) - 1 < 0$.
- **Hệ số Đòn bẩy Quyền chọn (Leverage / Elasticity - $\Omega$)**:
  $$\Omega = \frac{\% \Delta V}{\% \Delta S} = \frac{S \cdot \Delta}{V}$$
  Vì Call Option có giá $V < S$ và $\Delta > 0$, nên $\Omega$ thường rất lớn (từ 5 đến 20 lần)!
- **Hệ số Rủi ro Hệ thống Beta của Quyền chọn**:
  Danh mục sao chép gồm cổ phiếu và tiền vay phi rủi ro ($\beta_{\text{cash}} = 0$):
  $$\mathbf{\beta_{\text{Option}} = \Omega \cdot \beta_{\text{Stock}} = \left(\frac{S \cdot \Delta}{V}\right) \beta_{\text{Stock}}}$$
  - Call Option có $\Delta > 0 \implies \beta_{\text{Call}} > \beta_{\text{Stock}}$ (Rủi ro hệ thống của Call cao hơn nhiều so với cổ phiếu cơ sở!).
  - Put Option có $\Delta < 0 \implies \beta_{\text{Put}} < 0$ (Put có Beta âm, đóng vai trò bảo hiểm rủi ro danh mục).

---

## 4.6. Biến động Ngụ ý (Implied Volatility) & Chỉ số VIX
- Trong công thức Black-Scholes, các biến $S_0, K, r, T$ đều quan sát được trực tiếp trên thị trường, duy chỉ có **$\sigma$ (độ biến động tương lai)** là biến ẩn.
- **Biến động Ngụ ý (Implied Volatility - IV)**: Khi đưa giá thị trường thực tế của quyền chọn vào phương trình Black-Scholes và giải ngược ra $\sigma$, giá trị tìm được gọi là Implied Volatility. Nó phản ánh sự đồng thuận của thị trường về mức độ biến động trong tương lai của cổ phiếu.
- **Chỉ số VIX (CBOE Volatility Index)**: Tính toán từ Implied Volatility của rổ quyền chọn chỉ số S&P 500 kỳ hạn 30 ngày. VIX được mệnh danh là **"Thước đo sự Sợ hãi của Phố Wall" (Fear Gauge)**. Khi thị trường hoảng loạn lao dốc, nhu cầu mua bảo hiểm (Put) tăng vọt làm VIX tăng phi mã.

---

# 5. LECTURE 11: GIẢI CHI TIẾT TẤT CẢ BÀI TẬP MINH HỌA
*(WORKED EXAMPLES AND IN-CLASS PROBLEMS)*

---

### Bài toán 1: Định giá Quyền chọn Mua 1 Thời kỳ (Cell 9)
**Thông số**: $S_0 = \$60$, $K = \$66$, $T = 1$ năm, $r_{\text{EAR}} = 4\%$ ($r = 1.04$). Giá cổ phiếu có thể tăng lên $S_u = \$78$ hoặc giảm xuống $S_d = \$48$.

**Lời giải chi tiết**:
1. Hệ số biến động:
   $$u = \frac{78}{60} = 1.30, \quad d = \frac{48}{60} = 0.80$$
2. Payoff tại đáo hạn:
   $$C_u = \max(78 - 66, 0) = \$12, \quad C_d = \max(48 - 66, 0) = \$0$$
3. **Cách 1: Danh mục Sao chép (Replicating Portfolio)**:
   - Tỷ lệ phòng hộ Delta:
     $$\Delta = \frac{C_u - C_d}{S_u - S_d} = \frac{12 - 0}{78 - 48} = \frac{12}{30} = \mathbf{0.40 \text{ cổ phiếu}}$$
   - Khoản tiền vay $B$:
     $$\Delta S_d + B \cdot r = C_d \implies 0.40(48) + 1.04 B = 0 \implies B = \frac{-19.20}{1.04} \approx -\$18.4615$$
   - Giá trị Call hôm nay:
     $$C_0 = \Delta S_0 + B = 0.40(60) - 18.4615 = 24.00 - 18.4615 = \mathbf{\$5.5385 \approx \$5.54}$$
4. **Cách 2: Định giá Trung lập Rủi ro (Risk-Neutral)**:
   - Xác suất $p$:
     $$p = \frac{r - d}{u - d} = \frac{1.04 - 0.80}{1.30 - 0.80} = \frac{0.24}{0.50} = \mathbf{0.48}, \quad 1 - p = 0.52$$
   - Giá Call:
     $$C_0 = \frac{1}{1.04} [0.48 \times 12 + 0.52 \times 0] = \frac{5.76}{1.04} = \mathbf{\$5.5385 \approx \$5.54}$$

---

### Bài toán 2: Định giá Quyền chọn Bán 1 Thời kỳ (Cell 11 & 14)
**Ví dụ A (Cell 11)**: $S_0 = \$50, u = 1.20 (S_u = 60), d = 0.80 (S_d = 40), K = \$52, r = 1.05$.
- Payoff: $P_u = \max(52 - 60, 0) = 0$, $P_d = \max(52 - 40, 0) = 12$.
- $\Delta = \frac{0 - 12}{60 - 40} = -0.60$.
- $B = \frac{0 - (-0.60 \times 60)}{1.05} = \frac{36}{1.05} \approx 34.2857$.
- Giá Put: $P_0 = -0.60(50) + 34.2857 = -30 + 34.2857 = \mathbf{\$4.2857 \approx \$4.29}$.
- Xác suất rủi ro trung lập: $p = \frac{1.05 - 0.80}{1.20 - 0.80} = \frac{0.25}{0.40} = 0.625$.
  $$P_0 = \frac{0.625(0) + 0.375(12)}{1.05} = \frac{4.50}{1.05} = \mathbf{\$4.29}$$.

**Ví dụ B (Cell 14)**: $S_0 = \$80, u = 1.15 (S_u = 92), d = 0.90 (S_d = 72), K = \$78, r = 1.03$.
- Payoff: $P_u = \max(78 - 92, 0) = 0$, $P_d = \max(78 - 72, 0) = 6$.
- $\Delta = \frac{0 - 6}{92 - 72} = -0.30$.
- $p = \frac{1.03 - 0.90}{1.15 - 0.90} = \frac{0.13}{0.25} = 0.52, 1-p = 0.48$.
- Giá Put: $P_0 = \frac{0.52(0) + 0.48(6)}{1.03} = \frac{2.88}{1.03} = \mathbf{\$2.7961 \approx \$2.80}$.

---

### Bài toán 3: Cổ phiếu Gamma - 4 Câu hỏi Phân tích Toàn diện (Cell 16 & 17)
**Đề bài**: Cổ phiếu Gamma đang giao dịch ở giá $\$50$. Trong 1 năm tới, giá cổ phiếu sẽ hoặc tăng 40% ($u = 1.40$) hoặc giảm 40% ($d = 0.60$). Lãi suất phi rủi ro là 8% (EAR $\implies r = 1.08$).
- (a) Giá của quyền chọn bán kiểu Âu ATM 1 năm ($K=\$50$)?
- (b) Giá của quyền chọn mua kiểu Âu ATM 1 năm ($K=\$50$)?
- (c) Giá của quyền chọn bán kiểu Âu ITM sâu 1 năm với giá thực hiện $K=\$70$?
- (d) Nếu các quyền chọn bán ở câu (a) và (c) là quyền chọn Mỹ (American Puts), giá trị của chúng sẽ là bao nhiêu?

**Lời giải chi tiết từng bước**:
1. **Tìm xác suất trung lập rủi ro**:
   - $u = 1.40 \implies S_u = 50 \times 1.40 = \$70$
   - $d = 0.60 \implies S_d = 50 \times 0.60 = \$30$
   - $r = 1.08$
   $$p = \frac{r - d}{u - d} = \frac{1.08 - 0.60}{1.40 - 0.60} = \frac{0.48}{0.80} = \mathbf{0.60}, \quad 1 - p = \mathbf{0.40}$$

2. **Câu (a): European Put ATM ($K=50$)**:
   - Payoff:
     $$P_u = \max(50 - 70, 0) = 0$$
     $$P_d = \max(50 - 30, 0) = 20$$
   - Giá Put Âu:
     $$P_0 = \frac{p P_u + (1-p) P_d}{r} = \frac{0.60(0) + 0.40(20)}{1.08} = \frac{8.00}{1.08} = \mathbf{\$7.4074 \approx \$7.41}$$

3. **Câu (b): European Call ATM ($K=50$)**:
   - Payoff:
     $$C_u = \max(70 - 50, 0) = 20$$
     $$C_d = \max(30 - 50, 0) = 0$$
   - Giá Call Âu:
     $$C_0 = \frac{0.60(20) + 0.40(0)}{1.08} = \frac{12.00}{1.08} = \mathbf{\$11.1111 \approx \$11.11}$$
   - *Kiểm tra lại bằng Put-Call Parity*:
     $$C_0 - P_0 = 11.1111 - 7.4074 = 3.7037$$
     $$S_0 - \frac{K}{r} = 50 - \frac{50}{1.08} = 50 - 46.2963 = 3.7037 \implies \text{Chính xác 100%!}$$

4. **Câu (c): European Put Deep ITM ($K=70$)**:
   - Payoff:
     $$P_u = \max(70 - 70, 0) = 0$$
     $$P_d = \max(70 - 30, 0) = 40$$
   - Giá Put Âu:
     $$P_0 = \frac{0.60(0) + 0.40(40)}{1.08} = \frac{16.00}{1.08} = \mathbf{\$14.8148 \approx \$14.81}$$

5. **Câu (d): Định giá American Puts & Quyết định Thực thi Sớm**:
   - Với quyền chọn Mỹ, nhà đầu tư có quyền thực thi ngay lập tức tại $t=0$:
     $$\text{American Option Value} = \max(\text{Intrinsic Value tại } t=0, \text{Continuation Value } P_0)$$
   - **Đối với Put ATM ($K=50$)**:
     - Giá trị nội tại hôm nay: $\max(50 - S_0, 0) = \max(50 - 50, 0) = \$0$.
     - Giá trị tiếp tục giữ: $\$7.41$.
     - $\implies P_{\text{American}} = \max(0, 7.41) = \mathbf{\$7.41}$ (Tiếp tục giữ, không thực thi sớm).
   - **Đối với Put ITM sâu ($K=70$)**:
     - Giá trị nội tại hôm nay: $\max(70 - S_0, 0) = \max(70 - 50, 0) = \mathbf{\$20.00}$.
     - Giá trị tiếp tục giữ đến đáo hạn: $\$14.81$.
     - So sánh: Giá trị thực thi ngay ($20) cao hơn hẳn giá trị tiếp tục nắm giữ ($14.81)!
     - $\implies P_{\text{American}} = \max(20.00, 14.81) = \mathbf{\$20.00}$!
     - **Quyết định**: **THỰC THI NGAY LẬP TỨC HÔM NAY (EXERCISE NOW)!**

---

### Bài toán 4: Cây Nhị thức 2 Thời kỳ - Quyền chọn Mua (Cell 19)
**Thông số**: $S_0 = \$64, u = 1.25, d = 0.75, K = \$68$. Thời gian 6 tháng gồm 2 kỳ 3 tháng. Lãi suất danh nghĩa $8\%$/năm ghép lãi theo quý $\implies$ Lãi suất kỳ 3 tháng là $r = 1 + \frac{8\%}{4} = 1.02$.

**Lời giải**:
1. Cây giá cổ phiếu:
   - $t=0: S_0 = 64$
   - $t=1: S_u = 64 \times 1.25 = 80; \quad S_d = 64 \times 0.75 = 48$
   - $t=2: S_{uu} = 80 \times 1.25 = 100; \quad S_{ud} = 80 \times 0.75 = 60; \quad S_{dd} = 48 \times 0.75 = 36$
2. Payoff tại $t=2$ ($K=68$):
   - $C_{uu} = \max(100 - 68, 0) = 32$
   - $C_{ud} = \max(60 - 68, 0) = 0$
   - $C_{dd} = \max(36 - 68, 0) = 0$
3. Xác suất trung lập rủi ro:
   $$p = \frac{r - d}{u - d} = \frac{1.02 - 0.75}{1.25 - 0.75} = \frac{0.27}{0.50} = \mathbf{0.54}, \quad 1 - p = 0.46$$
4. Quy nạp ngược về $t=1$:
   - $C_u = \frac{p C_{uu} + (1-p) C_{ud}}{r} = \frac{0.54(32) + 0.46(0)}{1.02} = \frac{17.28}{1.02} \approx 16.9412$
   - $C_d = \frac{0.54(0) + 0.46(0)}{1.02} = 0$
5. Quy nạp ngược về $t=0$:
   $$C_0 = \frac{p C_u + (1-p) C_d}{r} = \frac{0.54(16.9412) + 0.46(0)}{1.02} = \frac{(0.54)^2 \times 32}{(1.02)^2} = \mathbf{\$8.9689 \approx \$8.97}$$

---

### Bài toán 5: Cây Nhị thức 2 Thời kỳ - Bước nhảy Cộng tiền Delta Corp (Cell 21 & 22)
**Thông số**: Cổ phiếu Delta Corp $S_0 = \$10$. Mỗi năm tăng $\$3$ hoặc giảm $\$2$. Lãi suất năm $r = 1.04$. $K = \$12$.

**Cây giá cổ phiếu**:
- $t=0: S_0 = 10$
- $t=1: S_u = 13, \quad S_d = 8$
- $t=2: S_{uu} = 16, \quad S_{ud} = S_{du} = 11, \quad S_{dd} = 6$

**Định giá Call 2 năm ($K=12$)**:
- Payoffs tại $t=2$: $C_{uu} = 4, C_{ud} = 0, C_{dd} = 0$.
- Tại nút $u$ ($S_u=13$):
  - $u_u = 16/13 \approx 1.2308, \quad d_u = 11/13 \approx 0.8462$
  - $p_u = \frac{1.04 - 11/13}{16/13 - 11/13} = \frac{1.04 - 0.84615}{0.38462} = \mathbf{0.504}$
  - $C_u = \frac{0.504(4) + 0.496(0)}{1.04} \approx \mathbf{1.9385}$
- Tại nút $d$ ($S_d=8$): Cả hai nhánh đều ra 0 $\implies C_d = 0$.
- Tại nút gốc $t=0$ ($S_0=10$):
  - $u_0 = 1.30, d_0 = 0.80 \implies p_0 = \frac{1.04 - 0.80}{1.30 - 0.80} = \mathbf{0.48}$
  - $C_0 = \frac{0.48(1.9385) + 0.52(0)}{1.04} \approx \mathbf{\$0.89}$

**Định giá Put 2 năm ($K=12$)**:
- Payoffs tại $t=2$: $P_{uu} = 0, P_{ud} = 12 - 11 = 1, P_{dd} = 12 - 6 = 6$.
- Tại nút $u$: $P_u = \frac{0.504(0) + 0.496(1)}{1.04} \approx \mathbf{0.4769}$
- Tại nút $d$ ($S_d=8$):
  - $u_d = 11/8 = 1.375, \quad d_d = 6/8 = 0.75$
  - $p_d = \frac{1.04 - 0.75}{1.375 - 0.75} = \frac{0.29}{0.625} = \mathbf{0.464}, \quad 1 - p_d = 0.536$
  - $P_d = \frac{0.464(1) + 0.536(6)}{1.04} = \frac{3.68}{1.04} \approx \mathbf{3.5385}$
- Tại nút gốc $t=0$:
  $$P_0 = \frac{0.48(0.4769) + 0.52(3.5385)}{1.04} = \frac{0.2289 + 1.8400}{1.04} \approx \mathbf{\$1.9893 \approx \$1.99}$$

---

### Bài toán 6: Cây 2 Thời kỳ So sánh American Put vs European Put (Cell 24 & 25)
**Thông số**: $S_0 = \$80, u = 1.25, d = 0.75, K = \$84, r = 1.05$.
- Cây giá cổ phiếu: $S_0 = 80 \to S_u = 100 (S_{uu}=125, S_{ud}=75); S_d = 60 (S_{du}=75, S_{dd}=45)$.
- Payoff tại $t=2$: $P_{uu} = 0, P_{ud} = 84 - 75 = 9, P_{dd} = 84 - 45 = 39$.
- $p = \frac{1.05 - 0.75}{1.25 - 0.75} = \mathbf{0.60}, 1 - p = 0.40$.

**1. Định giá European Put (Cell 24)**:
- $P_1^u = \frac{0.60(0) + 0.40(9)}{1.05} \approx 3.4286$
- $P_1^d = \frac{0.60(9) + 0.40(39)}{1.05} = \frac{5.4 + 15.6}{1.05} = \mathbf{20.00}$
- $P_0^{\text{Euro}} = \frac{0.60(3.4286) + 0.40(20.00)}{1.05} = \frac{2.0571 + 8.00}{1.05} = \mathbf{\$9.5782 \approx \$9.58}$

**2. Định giá American Put với Kiểm tra Thực thi Sớm (Cell 25)**:
- Tại nút $u$ ($S_1 = 100$):
  - Giá trị thực thi ngay: $\max(84 - 100, 0) = 0$.
  - Giá trị tiếp tục giữ: $3.4286$.
  - $\implies P_1^u = \max(0, 3.4286) = \mathbf{3.4286}$ (Tiếp tục giữ).
- **Tại nút $d$ ($S_1 = 60$) - ĐIỂM BẢN LỀ**:
  - Giá trị thực thi ngay: $\max(84 - 60, 0) = \mathbf{24.00}$!
  - Giá trị tiếp tục giữ: $20.00$.
  - Vì $24.00 > 20.00$, người nắm giữ American Put **SẼ THỰC THI SỚM NGAY TẠI NĂM 1**!
  - $\implies P_1^d = \max(24.00, 20.00) = \mathbf{24.00}$!
- Lùi về nút gốc $t=0$:
  - Giá trị tiếp tục: $H_0 = \frac{0.60(3.4286) + 0.40(24.00)}{1.05} = \frac{2.0571 + 9.60}{1.05} = \mathbf{11.1020}$
  - Giá trị thực thi tại gốc: $\max(84 - 80, 0) = 4.00$.
  - $\implies P_0^{\text{American}} = \max(4.00, 11.1020) = \mathbf{\$11.10}$!
- **Phần bù thực thi sớm (Early Exercise Premium)**:
  $$\text{Premium} = P_0^{\text{American}} - P_0^{\text{Euro}} = 11.10 - 9.58 = \mathbf{\$1.52}$$

---

### Bài toán 7: Định giá Black-Scholes - Cổ phiếu Lambda (Cell 39 & 40)
**Thông số**: $S_0 = \$90, K = \$90$ (ATM), $T = 0.5$ năm, $\sigma = 0.30$, $r = 6\%$/năm (ghép liên tục).
1. **Tính $d_1$ và $d_2$**:
   $$\ln(S_0 / K) = \ln(90/90) = \ln(1) = 0$$
   $$\sigma \sqrt{T} = 0.30 \times \sqrt{0.5} \approx 0.30 \times 0.707107 \approx 0.212132$$
   $$d_1 = \frac{0 + (0.06 + 0.5 \times 0.30^2) \times 0.5}{0.212132} = \frac{(0.06 + 0.045) \times 0.5}{0.212132} = \frac{0.0525}{0.212132} \approx \mathbf{0.247487 \approx 0.2475}$$
   $$d_2 = d_1 - \sigma \sqrt{T} = 0.247487 - 0.212132 \approx \mathbf{0.035355 \approx 0.0354}$$
2. **Tra bảng phân phối chuẩn $N(d)$**:
   - $N(d_1) = N(0.2475) \approx \mathbf{0.597734}$
   - $N(d_2) = N(0.0354) \approx \mathbf{0.514102}$
3. **Tính giá trị Call**:
   $$PV(K) = 90 e^{-0.06 \times 0.5} = 90 e^{-0.03} \approx 90 \times 0.970446 = \$87.3401$$
   $$C_0 = 90 \times 0.597734 - 87.3401 \times 0.514102 = 53.7961 - 44.9017 = \mathbf{\$8.8944 \approx \$8.89}$$
4. **Xây dựng danh mục sao chép (Cell 40)**:
   - Mua $\Delta = N(d_1) \approx 0.597734$ cổ phiếu Lambda. Số tiền mua $= 90 \times 0.597734 = \mathbf{\$53.80}$.
   - Vay nợ ngân hàng khoản tiền $PV(K) N(d_2) = \mathbf{\$44.90}$.
   - Chi phí ròng bỏ ra hôm nay: $53.80 - 44.90 = \mathbf{\$8.89}$.

---

### Bài toán 8: Định giá Black-Scholes - Cổ phiếu Sigma / Theta (Cell 42)
**Thông số**: $S_0 = \$120, K = \$125, T = 9/12 = 0.75$ năm, $\sigma = 0.28, r = 4\%$/năm (ghép liên tục).
1. **Tính $d_1, d_2$**:
   $$\ln(120/125) = -0.040822$$
   $$\sigma \sqrt{T} = 0.28 \times \sqrt{0.75} \approx 0.28 \times 0.866025 \approx 0.242487$$
   $$\left(r + \frac{\sigma^2}{2}\right) T = (0.04 + 0.5 \times 0.28^2) \times 0.75 = (0.04 + 0.0392) \times 0.75 = 0.0792 \times 0.75 = 0.059400$$
   $$d_1 = \frac{-0.040822 + 0.059400}{0.242487} = \frac{0.018578}{0.242487} \approx \mathbf{0.076614 \approx 0.0766}$$
   $$d_2 = 0.076614 - 0.242487 \approx \mathbf{-0.165873 \approx -0.1659}$$
2. **Tra bảng xác suất chuẩn**:
   - $N(d_1) = N(0.0766) \approx \mathbf{0.530535}$
   - $N(d_2) = N(-0.1659) \approx \mathbf{0.434129}$
3. **Tính giá Call**:
   $$PV(K) = 125 e^{-0.04 \times 0.75} = 125 e^{-0.03} \approx 125 \times 0.970446 = \$121.3057$$
   $$C_0 = 120(0.530535) - 121.3057(0.434129) = 63.6642 - 52.6623 = \mathbf{\$11.0019 \approx \$11.00}$$
4. **Tính giá Put qua Put-Call Parity**:
   $$P_0 = C_0 - S_0 + PV(K) = 11.0019 - 120.00 + 121.3057 = \mathbf{\$12.3076 \approx \$12.31}$$

---

# 6. BÍ KÍP BẤM MÁY & 10 BẪY THI SỐNG CÒN
*(SPEED-RUN EXAM PLAYBOOK & FATAL PITFALLS)*

> [!WARNING]
> ### 10 Bẫy thi Kinh điển Cần Khắc Cốt Ghi Tâm:
> 1. **Bẫy EAR vs. Ghép liên tục (Compounding Frequency)**: Nếu đề bài cho lãi suất hiệu dụng năm (EAR), bắt buộc chia cho $(1+r_f)^T$. Nếu đề bài nói "continuously compounded", bắt buộc nhân với $e^{-rT}$. Dùng lẫn lộn là sai toàn bộ bài tập Parity!
> 2. **Bẫy Đơn vị Thời gian $T$**: $T$ luôn tính theo đơn vị NĂM. 4 tháng $\implies T = 4/12 = 1/3$; 9 tháng $\implies T = 9/12 = 0.75$.
> 3. **Bẫy Dấu của Put Delta**: Delta của Call là số dương ($0 < \Delta_C < 1$). Delta của Put **BẮT BUỘC LÀ SỐ ÂM** ($-1 < \Delta_P < 0$). Khi viết tỷ lệ danh mục sao chép của Put, $\Delta$ luôn âm (nghĩa là bán khống cổ phiếu).
> 4. **Bẫy Payoff vs. Profit**: Payoff không bao gồm chi phí mua quyền chọn ban đầu! Khi đề bài hỏi "Payoff", công thức chỉ là $\max(S_T - K, 0)$. Khi hỏi "Profit", mới lấy Payoff trừ đi phí $C_0$.
> 5. **Bẫy Thực thi sớm American Call**: Với cổ phiếu KHÔNG CỔ TỨC, không bao giờ được thực thi Call sớm. Giá trị American Call luôn bằng đúng European Call: $C_A = C_E$.
> 6. **Bẫy Thực thi sớm American Put**: American Put ITM sâu RẤT NÊN THỰC THI SỚM! Giá trị của American Put luôn lớn hơn hoặc bằng European Put: $P_A \ge P_E$.
> 7. **Bẫy Cổ tức trong Parity**: Khi có cổ tức $D$, vế cổ phiếu bị trừ đi $PV(D)$: $C - P = S_0 - PV(D) - PV(K)$.
> 8. **Bẫy Chiết khấu trong Cây Nhị thức**: Ở mỗi bước quy nạp ngược, đừng bao giờ quên chia cho $r$! Rất nhiều sinh viên tính $p f_u + (1-p) f_d$ rồi quên chia cho $(1 + r_{\text{period}})$.
> 9. **Bẫy Merton Model**: Vốn chủ sở hữu $E$ là Call option với strike bằng **Mệnh giá Nợ (Face Value of Debt)**, KHÔNG PHẢI thị giá nợ!
> 10. **Bẫy Quy tắc Nhân căn thời gian của Volatility**: $\sigma_{\text{annual}} = \sigma_{\text{daily}} \sqrt{250} = \sigma_{\text{weekly}} \sqrt{52} = \sigma_{\text{monthly}} \sqrt{12}$. Độ lệch chuẩn tăng theo căn bậc hai của thời gian, chứ không tăng tuyến tính!
