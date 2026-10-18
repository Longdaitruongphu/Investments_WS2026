# BFIN INVESTMENTS (WS2026) - LECTURE 09: CHỨNG KHOÁN PHÁI SINH I
## (DERIVATIVES I: FORWARDS, FUTURES, SWAPS & CDS)
**Phương pháp Sư phạm Feynman: Dễ hiểu như kể chuyện cho một đứa trẻ, Chặt chẽ về Toán học, Song ngữ Anh - Việt (Bilingual)**

---

# PHẦN I: TỔNG HỢP TOÀN BỘ LÝ THUYẾT THEO PHƯƠNG PHÁP FEYNMAN (ELI5)

## 1. Khái niệm Phái sinh (What is a Derivative?)
- **Giải thích cho một đứa trẻ (Explain Like I'm 5)**:  
  Hãy tưởng tượng bạn có một **con khủng long đồ chơi thật** (Tài sản cơ sở - Underlying Asset). Bây giờ, bạn lấy điện thoại chụp một **tấm ảnh** của con khủng long đó (Tài sản phái sinh - Derivative).  
  Tấm ảnh tự nó chỉ là một mảnh giấy vụn hoặc vài pixel trên màn hình, nó không biết gầm rú, không biết cử động. Nhưng giá trị của tấm ảnh lại **phụ thuộc 100% vào con khủng long**: nếu con khủng long đồ chơi bỗng nhiên trở nên cực hiếm và đắt giá, tấm ảnh có chữ ký cũng sẽ có giá cao; nếu con khủng long bị gãy đầu vứt vào sọt rác, tấm ảnh chẳng còn ai thèm mua.
- **Định nghĩa Học thuật (Formal Definition)**:  
  Tài sản phái sinh (Derivative) là một hợp đồng tài chính mà giá trị của nó bắt nguồn (derived from) hoặc liên kết trực tiếp với hiệu suất của một tài sản cơ sở, tỷ suất, chỉ số hoặc sự kiện (underlying asset, interest rate, exchange rate, commodity, credit risk).

### 4 Mục đích Sử dụng Chính (Uses of Derivatives)
1. **Hedging (Phòng hộ rủi ro)**: Giống như việc bạn **mua một chiếc ô trước khi ra khỏi nhà**. Bạn biết trời sắp mưa (giá có thể biến động xấu), nên bạn khóa trước giá để bảo vệ mình.
2. **Speculation (Đầu cơ)**: Bạn không có ô và cũng chẳng cần đi ra ngoài mưa, nhưng bạn **đặt cược xem ngày mai trời mưa hay nắng** để kiếm tiền chênh lệch. Sử dụng đòn bẩy cao để tìm kiếm lợi nhuận.
3. **Arbitrage (Kinh doanh chênh lệch giá)**: Bạn thấy ở cổng trường bán cái kẹo 5 ngàn, trong khi ở cuối sân trường có bạn đang mua lại với giá 7 ngàn. Bạn lập tức mua ở cổng và chạy vào bán lại, **bỏ túi ngay 2 ngàn tiền lời chắc chắn 100% mà không hề chịu rủi ro và không cần bỏ vốn tự có (Free Lunch / Money Machine)**.
4. **Exposure Transformation (Chuyển đổi trạng thái tài sản/nợ)**: Thay đổi rủi ro của một khoản vay hay danh mục đầu tư (ví dụ từ lãi suất thả nổi sang cố định) mà **không cần phải bán tài sản hay tất toán khoản nợ cũ**.

---

## 2. Hợp đồng Kỳ hạn (Forward Contracts) & Cơ chế Định giá Không Chênh lệch Giá
### 2.1. Bản chất Hợp đồng Kỳ hạn
- Là một thỏa thuận tay đôi tư nhân (Over-the-Counter - OTC) giữa 2 bên:  
  - **Long (Bên Mua kỳ hạn)**: Bắt buộc phải **MUA** tài sản tại ngày tương lai $T$ với giá thỏa thuận $F$.  
    $$\text{Payoff tại đáo hạn} = S_T - F$$
  - **Short (Bên Bán kỳ hạn)**: Bắt buộc phải **BÁN** tài sản tại ngày tương lai $T$ với giá thỏa thuận $F$.  
    $$\text{Payoff tại đáo hạn} = F - S_T$$
- **Đặc điểm sống còn**:  
  - Tại ngày ký kết ($t=0$), giá giao hàng $F$ được thiết lập sao cho **giá trị của hợp đồng bằng 0 ($V_0 = 0$)**. Hai bên **không phải trả cho nhau bất kỳ khoản tiền ban đầu nào (Zero initial premium)**!
  - Nhưng sau ngày ký kết ($t > 0$), khi giá thị trường $S_t$ thay đổi, giá trị hợp đồng $V_t$ sẽ biến động (một bên có lãi, một bên bị lỗ).

### 2.2. Tại sao $F = S_0 (1 + r_f)^T$ hay $F = S_0 e^{r T}$? (Nguyên lý Sao chép - Replication)
- Hãy tưởng tượng bạn muốn có 1 quả táo vào ngày này năm sau ($T=1$):
  - **Cách 1 (Mua vật lý)**: Cầm $S_0 = 50$ USD ra chợ mua quả táo cất vào két. Chi phí hôm nay $= S_0 = 50$.
  - **Cách 2 (Mô phỏng tài chính - Synthetic Position)**: Ký hợp đồng Long Forward mua táo vào năm sau với giá $F$ (tốn 0 USD). Đồng thời, mang số tiền đúng bằng $\frac{F}{1+r_f}$ gửi vào ngân hàng.  
    Đến ngày đáo hạn, tiền gửi ngân hàng nở ra đúng bằng $F$. Bạn lấy $F$ này thanh toán cho hợp đồng Forward và nhận quả táo về.
- **Kết luận**: Cả hai cách đều mang lại đúng 1 quả táo tại $T=1$. Vì không có bữa trưa nào miễn phí (Law of One Price), chi phí hôm nay của 2 cách bắt buộc phải bằng nhau:
  $$S_0 = \frac{F}{(1+r_f)^T} \iff F = S_0 (1+r_f)^T$$

### 2.3. Bắt bài Trọng tài Chênh lệch Giá (Arbitrage Mechanism)
- **Kịch bản A: Giá thị trường cao hơn giá lý thuyết ($F_{\text{market}} > F^*$) $\implies$ Hợp đồng kỳ hạn bị ĐẮT (Overvalued)**:
  - **Chiến lược: Cash-and-Carry Arbitrage**
  - Hôm nay ($t=0$): Vay tiền ngân hàng đúng bằng $S_0$ $\rightarrow$ Mua tài sản thật trên thị trường giao ngay $\rightarrow$ Đồng thời ký hợp đồng BÁN kỳ hạn (Short Forward) ở mức giá cao $F_{\text{market}}$. Dòng tiền ròng hôm nay $= 0$.
  - Đáo hạn ($T$): Lấy tài sản giao cho người mua kỳ hạn, thu về $F_{\text{market}}$ $\rightarrow$ Trả nợ ngân hàng cả gốc lẫn lãi $S_0(1+r_f)^T$ $\rightarrow$ Lợi nhuận chắc chắn 100%: $\Pi_T = F_{\text{market}} - S_0(1+r_f)^T > 0$.
- **Kịch bản B: Giá thị trường thấp hơn giá lý thuyết ($F_{\text{market}} < F^*$) $\implies$ Hợp đồng kỳ hạn bị RẺ (Undervalued)**:
  - **Chiến lược: Reverse Cash-and-Carry Arbitrage**
  - Hôm nay ($t=0$): Mượn tài sản đem bán khống (Short Sell) thu về $S_0$ tiền mặt $\rightarrow$ Đem toàn bộ tiền gửi tiết kiệm lãi suất $r_f$ $\rightarrow$ Ký hợp đồng MUA kỳ hạn (Long Forward) ở mức giá hời $F_{\text{market}}$. Dòng tiền ròng hôm nay $= 0$.
  - Đáo hạn ($T$): Thu tiền gửi tiết kiệm $S_0(1+r_f)^T$ $\rightarrow$ Thực hiện hợp đồng Long Forward trả $F_{\text{market}}$ để lấy lại tài sản trả cho người cho mượn $\rightarrow$ Bỏ túi tiền lời ròng: $\Pi_T = S_0(1+r_f)^T - F_{\text{market}} > 0$.

---

## 3. Hợp đồng Tương lai (Futures) & Cơ chế Ký quỹ Hàng ngày (Marking-to-Market)
### 3.1. Điểm khác biệt Cốt lõi giữa Forward và Futures
| Tiêu chí (Criterion) | Hợp đồng Kỳ hạn (Forwards) | Hợp đồng Tương lai (Futures) |
|---|---|---|
| **Nơi giao dịch** | Thị trường phi tập trung (OTC) | Sàn giao dịch tập trung (CME, ICE) |
| **Tính chuẩn hóa** | May đo riêng biệt theo nhu cầu hai bên | Chuẩn hóa 100% (số lượng, ngày đáo hạn, quy cách) |
| **Thanh toán lãi/lỗ** | Một lần duy nhất vào ngày đáo hạn ($T$) | **Định giá lại và thanh toán hàng ngày (Daily Marking to Market)** |
| **Rủi ro đối tác** | Cao (đối tác có thể bùng nợ) | Gần như bằng 0 (Sở thanh toán bù trừ CCP đứng ra bảo lãnh) |
| **Ký quỹ (Margin)** | Thỏa thuận riêng hoặc không yêu cầu | **Bắt buộc nộp Initial Margin & Maintenance Margin** |

### 3.2. Cơ chế Ký quỹ - "Trọng tài Sân chơi"
- **Initial Margin (Ký quỹ ban đầu)**: Số tiền cọc tối thiểu bạn phải nộp vào tài khoản để mở vị thế. *(Lưu ý đề thi: Đây là tài sản thế chấp rủi ro, KHÔNG PHẢI là tiền mua tài sản!)*
- **Maintenance Margin (Ký quỹ duy trì)**: Mức sàn an toàn. Nếu giá biến động ngược chiều làm số dư tài khoản tụt xuống **thấp hơn** Maintenance Margin:
  - Sở giao dịch sẽ phát ra một **Margin Call (Lệnh gọi ký quỹ bổ sung)**.
  - Bạn bắt buộc phải nộp thêm tiền ngay lập tức để đưa số dư **quay trở lại đúng bằng Initial Margin (chứ không phải chỉ vừa chạm Maintenance Margin)!**
- **Công thức Lãi/Lỗ hàng ngày (Daily P&L)** cho $n$ hợp đồng với quy mô $Q$ đơn vị:
  $$\text{Long P\&L} = n \cdot Q \cdot (F_t - F_{t-1})$$
  $$\text{Short P\&L} = n \cdot Q \cdot (F_{t-1} - F_t)$$

---

## 4. Bảng Tổng hợp Công thức Chi phí Cõng vốn (Cost of Carry Model)
- **Quy tắc trực quan (Golden Intuitive Rule)**:
  - Cái gì làm bạn **tốn thêm tiền** khi ôm giữ tài sản thật (Chi phí lãi vay $r$, Chi phí lưu kho bãi $U$ hoặc tỷ lệ $u$) $\implies$ **Làm TĂNG giá kỳ hạn $F$**.
  - Cái gì đem lại **tiền hoặc lợi ích** cho bạn khi cầm tài sản thật (Cổ tức tiền mặt $I$ hoặc tỷ suất cổ tức $q$, Lãi suất ngoại tệ $r_F$, Lợi suất tiện ích Convenience Yield $y$) $\implies$ **Làm GIẢM giá kỳ hạn $F$**.

| Loại tài sản cơ sở | Lãi suất liên tục ($e^{...}$) | Lãi suất rời rạc ($(1+...)$) | Ý nghĩa kinh tế |
|---|---|---|---|
| **Không cổ tức, không chi phí kho** | $F = S_0 e^{rT}$ | $F = S_0(1+r)^T$ | Chỉ có chi phí cơ hội vốn vay |
| **Có thu nhập tiền mặt cố định $I$ (hoặc coupon)** | $F = (S_0 - I)e^{rT}$ với $I = PV(\text{Income})$ | $F = (S_0 - PV(I))(1+r)^T$ | Khấu trừ hiện giá cổ tức/coupon nhận được |
| **Có tỷ suất cổ tức liên tục $q$** | $F = S_0 e^{(r-q)T}$ | $F = S_0 \frac{(1+r)^T}{(1+q)^T}$ | Cổ tức liên tục làm giảm chi phí cõng vốn |
| **Tiền tệ (Currencies - CIP)** | $F_{D/F} = S_{0, D/F} e^{(r_D - r_F)T}$ | $F_{D/F} = S_{0, D/F} \frac{(1+r_D)^T}{(1+r_F)^T}$ | Ngang giá lãi suất có phòng ngừa (Covered Interest Parity) |
| **Chi phí lưu kho tiền mặt $U$** | $F = (S_0 + U)e^{rT}$ | $F = (S_0 + U)(1+r)^T$ | Cộng thêm chi phí bảo quản, kho bãi |
| **Chi phí lưu kho tỷ lệ liên tục $u$** | $F = S_0 e^{(r+u)T}$ | $F = S_0(1+r+u)^T$ | Lưu kho liên tục như một lãi suất âm |
| **Lợi suất tiện ích ròng (Convenience Yield $y$)** | $F = S_0 e^{(r-y)T}$ | $F = S_0 \frac{(1+r)^T}{(1+y)^T}$ | Lợi ích sở hữu vật lý phòng ngừa đứt gãy nguồn cung |

---

## 5. Hợp đồng Hoán đổi (Swaps) & Hoán đổi Rủi ro Tín dụng (CDS)
### 5.1. Interest Rate Swap (IRS - Hoán đổi Lãi suất Cố định - Thả nổi)
- **Bản chất**: Hai bên thỏa thuận đổi dòng tiền thanh toán lãi vay cho nhau định kỳ trên cùng một lượng vốn danh nghĩa $N$ (Notional Principal).
- **Điểm cực kỳ quan trọng**: **Vốn gốc $N$ KHÔNG BAO GIỜ được chuyển giao**! Hai bên chỉ cấn trừ khoản chênh lệch tiền lãi (Net Settlement).
- **Công thức tính kỳ thanh toán**:
  - Bên trả cố định (Fixed Payer) phải trả: $\text{Fixed Payment} = N \cdot K \cdot \Delta$
  - Bên trả thả nổi (Floating Payer) phải trả: $\text{Floating Payment} = N \cdot L_k \cdot \Delta$
  - Khoản thu ròng của bên trả cố định: $\text{Net Receipt} = N \cdot (L_k - K) \cdot \Delta$  
    *(Nếu $L_k > K$: Bên trả cố định nhận tiền từ bên thả nổi; Nếu $L_k < K$: Bên trả cố định phải trả tiền bù cho bên thả nổi).*

### 5.2. Currency Swap (Hoán đổi Tiền tệ)
- Khác với IRS: Được thực hiện bằng **hai đồng tiền khác nhau** (ví dụ USD và EUR).
- **Có trao đổi vốn gốc**:
  - Tại ngày bắt đầu ($t=0$): Đổi vốn gốc cho nhau theo tỷ giá giao ngay (Spot).
  - Hàng năm: Bên nào giữ tiền nào thì trả lãi suất của đồng tiền đó.
  - Tại ngày đáo hạn ($T$): **Đổi ngược lại vốn gốc ban đầu**.

### 5.3. Credit Default Swap (CDS - Hoán đổi Rủi ro Tín dụng)
- Là **hợp đồng bảo hiểm vỡ nợ** đối với một công ty hoặc chính phủ (Reference Entity).
- **Bên mua bảo hiểm (Protection Buyer)**: Trả phí bảo hiểm định kỳ (gọi là CDS Spread, tính bằng điểm cơ bản bps).
- **Bên bán bảo hiểm (Protection Seller)**: Nếu thực thể phá sản hoặc vỡ nợ (Credit Event):
  - **Cash Settlement (Thanh toán bằng tiền mặt)**: Bên bán bồi thường cho bên mua số tiền bằng:
    $$\text{Payout} = N \cdot (1 - \mathcal{R})$$
    *(với $\mathcal{R}$ là Tỷ lệ thu hồi nợ - Recovery Rate, thường xác định qua đấu giá).*
  - **Sovereign CDS**: Chênh lệch CDS trái phiếu chính phủ phản ánh rủi ro tín dụng của quốc gia đó (càng cao chứng tỏ nguy cơ vỡ nợ càng lớn hoặc thanh khoản càng kém).

---

# PHẦN II: LỜI GIẢI CHI TIẾT TỪNG BƯỚC TOÀN BỘ 11 BÀI TẬP LECTURE 09 (BILINGUAL SOLUTIONS)

---

### Question 1 (L09 In-Class Q1)
**Original Question:**  
In a copper market, all producers, including Kappa, and cable manufacturers, including Lambda, hedge their planned sales and purchases for the next six months using exchange-traded futures. Assume exact matches in quantity, timing, and price exposure between the hedges and the physical transactions.  
Discuss:  
1. **Price Discovery**: Who determines spot copper prices once these firms are fully hedged? Must the futures market become the main driver of spot prices?  
2. **The Speculator's Role**: Can speculators still provide economic value? Does the zero-sum nature of futures payoffs rule out a benefit from trading or a risk premium?  
3. **Systemic Risk**: Does full hedging necessarily concentrate commodity-price risk in clearinghouses and increase systemic risk?  

**Tóm tắt đề bài (Vietnamese Summary):**  
Trong thị trường đồng, toàn bộ nhà sản xuất (như Kappa) và nhà máy chế tạo dây cáp (như Lambda) đều phòng hộ 100% lượng mua/bán dự kiến trong 6 tháng tới bằng hợp đồng tương lai trên sàn giao dịch. Khối lượng và kỳ hạn khớp chính xác 100% với giao dịch vật chất.  
Thảo luận 3 vấn đề:  
1. *Phát hiện giá (Price Discovery)*: Khi các doanh nghiệp đã phòng hộ hết, ai là người quyết định giá đồng giao ngay? Thị trường tương lai có phải là động lực chính chi phối giá giao ngay không?  
2. *Vai trò của nhà đầu cơ (Speculators)*: Nhà đầu cơ có còn mang lại giá trị kinh tế không? Bản chất tổng bằng không (Zero-sum game) của phái sinh có triệt tiêu lợi ích giao dịch hay phần bù rủi ro không?  
3. *Rủi ro hệ thống (Systemic Risk)*: Việc phòng hộ toàn diện có làm tập trung rủi ro giá hàng hóa vào sở thanh toán bù trừ (Clearinghouse/CCP) và làm gia tăng rủi ro hệ thống không?  

**Detailed Bilingual Solution & Deep Analysis:**

1. **Price Discovery (Cơ chế Phát hiện Giá)**:
   - **Bản chất kinh tế (Economic Reality)**: Giá đồng giao ngay (Spot Price $S_0$) tại bất kỳ thời điểm nào vẫn **về mặt căn bản được quyết định bởi cung - cầu vật chất tức thời (Immediate physical supply and demand)**. Những yếu tố này bao gồm: mức tồn kho tại các kho hàng địa phương, sự gián đoạn nguồn cung đột xuất (đình công mỏ đồng, bão lũ), và nhu cầu giao nhận hàng vật chất ngay trong ngày của các bên không phòng hộ.
   - **Tác động của Thị trường Tương lai**: Tuy nhiên, do liên kết định giá phi chênh lệch giá ($F = S_0 e^{(r+u-y)T}$) và điều kiện hội tụ tại ngày đáo hạn ($S_T = F_T$), thị trường tương lai có tính thanh khoản cao hơn rất nhiều, chi phí giao dịch thấp hơn và cho phép sử dụng đòn bẩy. Do đó, **các thông tin vĩ mô và kỳ vọng mới luôn phản ánh vào giá tương lai TRƯỚC (Futures leads Spot)**. Thị trường tương lai đóng vai trò là "ngọn hải đăng" dẫn dắt quá trình phát hiện giá, nhưng giá giao ngay vẫn phản ánh thực tế hàng hóa vật chất tại chỗ.

2. **The Speculator's Role (Vai trò của Nhà Đầu cơ)**:
   - **Bản chất trò chơi tổng bằng không (Zero-Sum vs. Welfare Improvement)**: Trong hợp đồng tương lai, mỗi đồng USD tiền lãi của bên Long đúng bằng một đồng USD tiền lỗ của bên Short (Zero-sum in cash flows). Tuy nhiên, **Zero-sum về mặt tài chính KHÔNG CÓ NGHĨA là Zero-sum về mặt phúc lợi kinh tế (Pareto Improvement)**!
   - **Chuyển giao rủi ro & Phần bù rủi ro (Risk Transfer & Risk Premium)**: Các nhà sản xuất và chế tạo là những người sợ rủi ro (Risk-averse hedgers). Họ sẵn sàng trả một khoản phí bảo hiểm (thể hiện qua phần bù rủi ro / hiện tượng Normal Backwardation) để tống khứ rủi ro biến động giá sang cho các nhà đầu cơ.
   - **Cung cấp thanh khoản (Liquidity Provision)**: Trên thực tế, lượng bán phòng hộ của nhà sản xuất hiếm khi khớp hoàn hảo 1:1 với lượng mua phòng hộ của nhà máy chế tạo. Nhà đầu cơ chính là người nhảy vào hấp thụ phần mất cân đối này (Hedging Pressure), thu hẹp biên độ giá mua-bán (Bid-Ask spread) và làm thị trường vận hành trơn tru.

3. **Systemic Risk and Clearinghouses (Rủi ro Hệ thống và Sở Thanh toán Bù trừ)**:
   - **CCP không ôm rủi ro giá hàng hóa**: Sở thanh toán bù trừ trung tâm (Central Counterparty - CCP) luôn duy trì vị thế cân bằng tuyệt đối (Net Flat: là người mua đối với mọi người bán, và là người bán đối với mọi người mua). CCP **không hề chịu rủi ro định hướng giá đồng (Directional commodity price risk)**.
   - **Cơ chế phòng vệ vững chắc**: Rủi ro đối tác được vô hiệu hóa nhờ cơ chế ký quỹ ban đầu (Initial Margin), ký quỹ duy trì (Maintenance Margin), định giá lại hàng ngày (Daily Marking-to-Market), và quỹ phòng ngừa rủi ro vỡ nợ (Default Fund).
   - **Rủi ro Thanh khoản Hệ thống (Liquidity / Systemic Risk Concentration)**: Mặc dù CCP giảm thiểu nguy cơ lây lan vỡ nợ dây chuyền (Counterparty contagion), nó lại **tập trung rủi ro thanh khoản**. Khi giá đồng biến động dữ dội trong phiên, các lệnh gọi ký quỹ khổng lồ (Margin Calls) có thể buộc các thành viên phải thanh lý tài sản khẩn cấp hoặc mất khả năng thanh toán tạm thời (như cuộc khủng hoảng Nickel trên sàn LME tháng 3/2022). Do đó, rủi ro không biến mất hoàn toàn mà chuyển hóa từ rủi ro tín dụng phân tán thành rủi ro thanh khoản tập trung.

---

### Question 2 (L09 In-Class Q2)
**Original Question:**  
A nine-month long forward contract on one non-dividend-paying Theta share is entered into at the fair forward price. The share price is $84 and the continuously compounded risk-free rate is 4% per annum.  
1. What is the initial forward price?  
2. Four months later, the share price is $82 and the risk-free rate is unchanged. What is the value of the existing long forward contract?  

**Tóm tắt đề bài:**  
Hợp đồng Long Forward kỳ hạn 9 tháng trên 1 cổ phiếu Theta (không trả cổ tức). Giá cổ phiếu ban đầu $S_0 = 84$ USD, lãi suất phi rủi ro liên tục $r = 4\%$/năm.  
1. Giá kỳ hạn ban đầu $F_0$ là bao nhiêu?  
2. Bốn tháng sau, giá cổ phiếu là $S_t = 82$ USD, lãi suất không đổi. Giá trị hợp đồng Long Forward hiện tại ($V_t$) là bao nhiêu?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

**1. Initial Forward Price ($F_0$):**
- Kỳ hạn ban đầu: $T = \frac{9}{12} = 0.75$ năm.
- Công thức định giá kỳ hạn không cổ tức với lãi suất ghép liên tục:
  $$F_0 = S_0 \cdot e^{r \cdot T}$$
- Thay số:
  $$F_0 = 84 \cdot e^{0.04 \times 0.75} = 84 \cdot e^{0.03} \approx 84 \times 1.0304545 = \mathbf{86.5582 \text{ USD}} \approx \mathbf{86.56 \text{ USD}}$$

**2. Value of the Long Forward Contract 4 Months Later ($V_t$):**
- Thời gian đã trôi qua: $t = \frac{4}{12}$ năm.
- Thời gian còn lại đến đáo hạn: $T - t = \frac{9 - 4}{12} = \frac{5}{12} \approx 0.4167$ năm.
- Giá cổ phiếu hiện tại: $S_t = 82$ USD.
- Giá trị của một hợp đồng Long Forward tại thời điểm $t$ được tính bằng hiệu số giữa giá giao ngay hiện tại và hiện giá của mức giá giao hàng đã cam kết $F_0$:
  $$V_t = S_t - F_0 \cdot e^{-r(T - t)}$$
- Thay số:
  $$V_t = 82 - 86.5582 \cdot e^{-0.04 \times \frac{5}{12}} = 82 - 86.5582 \cdot e^{-0.016667}$$
  $$V_t = 82 - 86.5582 \times 0.983471 = 82 - 85.1275 = \mathbf{-3.1275 \text{ USD}} \approx \mathbf{-3.13 \text{ USD}}$$
- **Ý nghĩa kinh tế (Intuition)**:  
  Hợp đồng đang mang **giá trị âm** đối với người mua (Long position is underwater with a loss of $3.13). Lý do: Cổ phiếu rớt giá từ 84 xuống 82 USD, trong khi bạn vẫn bị trói buộc vào nghĩa vụ phải mua nó với giá cam kết ban đầu là 86.56 USD!

---

### Question 3 (L09 In-Class Q3)
**Original Question:**  
Kappa enters into a forward contract to buy a four-year, default-free zero-coupon bond that will be issued in three years.  
- Face value: $2,000.  
- Three-year spot rate: 3%; seven-year spot rate: 5%, both compounded annually.  
What is the forward price?  

**Tóm tắt đề bài:**  
Kappa ký hợp đồng kỳ hạn mua một trái phiếu zero-coupon kỳ hạn 4 năm không rủi ro, được phát hành sau 3 năm nữa.  
- Mệnh giá (Face Value) = $2,000 USD.  
- Lãi suất giao ngay 3 năm $s_3 = 3\%$, 7 năm $s_7 = 5\%$ (ghép lãi hàng năm).  
Tính giá kỳ hạn $F$?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

- **Phân tích dòng tiền & mốc thời gian (Timeline Analysis)**:  
  - Hôm nay là $t=0$.  
  - Hợp đồng kỳ hạn đáo hạn tại $t=3$ năm. Tại $t=3$, trái phiếu bắt đầu tồn tại và có kỳ hạn 4 năm.  
  - Do đó, trái phiếu sẽ đáo hạn và thanh toán mệnh giá $2,000$ USD vào thời điểm $t = 3 + 4 = 7$ năm!
- **Phương pháp 1: Hiện giá của Trái phiếu Zero-Coupon (Present Value Approach)**:  
  - Giá của trái phiếu đáo hạn tại năm 7 trên thị trường hôm nay ($t=0$) là:
    $$P(0, 7) = \frac{2,000}{(1 + s_7)^7} = \frac{2,000}{(1.05)^7} = \frac{2,000}{1.407100} \approx 1,421.3628 \text{ USD}$$
  - Giá kỳ hạn giao hàng tại năm $t=3$ phải thỏa mãn quan hệ không chênh lệch giá:
    $$F = P(0, 7) \cdot (1 + s_3)^3 = \frac{2,000 \cdot (1.03)^3}{(1.05)^7}$$
  - Tính toán:
    $$(1.03)^3 = 1.092727$$
    $$F = 1,421.3628 \times 1.092727 = \mathbf{1,553.1614 \text{ USD}} \approx \mathbf{1,553.16 \text{ USD}}$$

- **Phương pháp 2: Sử dụng Lãi suất Kỳ hạn 4 năm ($f_{3,7}$)**:  
  - Lãi suất kỳ hạn 4 năm từ năm thứ 3 đến năm thứ 7 thỏa mãn:
    $$(1 + s_7)^7 = (1 + s_3)^3 \cdot (1 + f_{3,7})^4$$
    $$(1 + f_{3,7})^4 = \frac{(1.05)^7}{(1.03)^3} = \frac{1.407100}{1.092727} \approx 1.287696 \implies f_{3,7} \approx 6.5332\%$$
  - Giá kỳ hạn $F$ chính là mệnh giá chiết khấu về năm thứ 3 theo lãi suất kỳ hạn $f_{3,7}$:
    $$F = \frac{2,000}{(1 + f_{3,7})^4} = \frac{2,000}{1.287696} = \mathbf{1,553.16 \text{ USD}}$$

---

### Question 4 (L09 In-Class Q4)
**Original Question:**  
Consider a six-month forward contract on the Sigma stock index, currently at 2,400.  
- The continuous dividend yield is 1.5% per annum for the first two months and 3% per annum for the remaining four months. These yields are known with certainty.  
- The continuously compounded risk-free rate is 5% per annum throughout.  
What is the forward price?  

**Tóm tắt đề bài:**  
Hợp đồng kỳ hạn 6 tháng trên chỉ số cổ phiếu Sigma, hiện tại $S_0 = 2,400$.  
- Tỷ suất cổ tức liên tục là 1.5%/năm trong 2 tháng đầu và 3%/năm trong 4 tháng sau.  
- Lãi suất phi rủi ro liên tục $r = 5\%$/năm trong suốt 6 tháng.  
Tính giá kỳ hạn $F$?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

- **Chuyển đổi thời gian sang năm (Time in Years)**:  
  - Tổng thời hạn: $T = \frac{6}{12} = 0.5$ năm.  
  - Giai đoạn 1: $\Delta t_1 = \frac{2}{12} = \frac{1}{6}$ năm với $q_1 = 0.015$.  
  - Giai đoạn 2: $\Delta t_2 = \frac{4}{12} = \frac{1}{3}$ năm với $q_2 = 0.030$.  
- **Tích phân tỷ suất cổ tức lũy kế (Cumulative Dividend Yield)**:
  $$\int_0^T q(t) dt = q_1 \cdot \Delta t_1 + q_2 \cdot \Delta t_2 = 0.015 \times \frac{2}{12} + 0.030 \times \frac{4}{12}$$
  $$= 0.0025 + 0.0100 = 0.0125 \text{ (tức } 1.25\%\text{)}$$
- **Chi phí lãi vay lũy kế (Financing Cost)**:
  $$r \cdot T = 0.05 \times 0.5 = 0.0250 \text{ (tức } 2.50\%\text{)}$$
- **Chi phí cõng vốn ròng (Net Cost of Carry)**:
  $$\text{Net Carry} = r \cdot T - \int_0^T q(t) dt = 0.0250 - 0.0125 = +0.0125$$
- **Tính giá kỳ hạn (Forward Price $F$)**:
  $$F = S_0 \cdot \exp\left(r T - \int_0^T q(t) dt\right) = 2,400 \cdot e^{0.0125}$$
  $$F = 2,400 \times 1.0125785 = \mathbf{2,430.1883 \text{ USD}} \approx \mathbf{2,430.19 \text{ USD}}$$

---

### Question 5 (L09 In-Class Q5)
**Original Question:**  
Kappa observes the following exchange rates and interest rate:  
- Spot GBP/USD rate: 1.2500 USD per GBP.  
- One-year forward rate: 1.2300 USD per GBP.  
- One-year USD risk-free rate: 4% per annum, continuously compounded.  
Ignore transaction costs; borrowing and lending rates are equal within each currency.  
Estimate the one-year GBP risk-free rate, expressed with continuous compounding.  

**Tóm tắt đề bài:**  
- Tỷ giá giao ngay $S_0 = 1.2500$ USD/GBP.  
- Tỷ giá kỳ hạn 1 năm $F = 1.2300$ USD/GBP.  
- Lãi suất USD 1 năm $r_{USD} = 4\%$/năm (ghép lãi liên tục).  
Ước lượng lãi suất GBP 1 năm ($r_{GBP}$) theo ghép lãi liên tục?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

- **Định lý Ngang giá Lãi suất có Phòng ngừa (Covered Interest Parity - CIP)**:  
  Quy ước trích dẫn tỷ giá: Đồng yết giá ngoại tệ là GBP ($F$), đồng định giá nội tệ là USD ($D$).  
  $$F = S_0 \cdot e^{(r_{USD} - r_{GBP}) \cdot T}$$
- Với $T = 1$ năm, ta có:
  $$\frac{F}{S_0} = e^{r_{USD} - r_{GBP}}$$
- Lấy logarit tự nhiên ($\ln$) hai vế:
  $$\ln\left(\frac{F}{S_0}\right) = r_{USD} - r_{GBP}$$
  $$r_{GBP} = r_{USD} - \ln\left(\frac{F}{S_0}\right)$$
- Thay số vào:
  $$\frac{F}{S_0} = \frac{1.2300}{1.2500} = 0.9840$$
  $$\ln(0.9840) \approx -0.016129$$
  $$r_{GBP} = 0.04 - (-0.016129) = 0.04 + 0.016129 = \mathbf{0.056129} \implies \mathbf{5.6129\% \text{ per annum}}$$
- **Giải thích trực quan (Intuition)**:  
  Tỷ giá kỳ hạn của GBP bị giảm giá so với giao ngay (1.2500 rớt xuống 1.2300 USD/GBP $\implies$ GBP trades at a forward discount). Để bù đắp cho sự mất giá này của đồng bảng Anh, lãi suất của đồng GBP bắt buộc phải **cao hơn** lãi suất của đồng USD ($5.61\% > 4.00\%$)!

---

### Question 6 (L09 In-Class Q6)
**Original Question:**  
Delta observes a spot exchange rate of 1.1600 USD per EUR. The continuously compounded risk-free rates are 4.5% per annum in USD and 2.5% in EUR.  
- (a) If the six-month forward rate is 1.1900 USD per EUR, what arbitrage strategy is possible?  
- (b) If the six-month forward rate is instead 1.1500 USD per EUR, what arbitrage strategy is possible?  
For each case, show the profit in USD using an initial borrowing with a spot value of USD 400,000. Ignore transaction costs; borrowing and lending rates are equal within each currency.  

**Tóm tắt đề bài:**  
$S_0 = 1.1600$ USD/EUR, $r_{USD} = 4.5\%$, $r_{EUR} = 2.5\%$ (liên tục), kỳ hạn 6 tháng ($T = 0.5$).  
Số tiền vay ban đầu quy đổi theo giá giao ngay là 400,000 USD.  
- (a) Nếu $F = 1.1900$ USD/EUR, chiến lược kinh doanh chênh lệch giá là gì? Tính lợi nhuận USD?  
- (b) Nếu $F = 1.1500$ USD/EUR, chiến lược kinh doanh chênh lệch giá là gì? Tính lợi nhuận USD?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

**Bước 0: Tính Tỷ giá Kỳ hạn Lý thuyết Không Chênh lệch giá ($F^*$)**:
$$F^* = S_0 \cdot e^{(r_{USD} - r_{EUR}) \cdot T} = 1.1600 \cdot e^{(0.045 - 0.025) \times 0.5} = 1.1600 \cdot e^{0.01} \approx 1.171658 \text{ USD/EUR}$$

---

#### Trường hợp (a): Tỷ giá niêm yết $F = 1.1900 > F^* = 1.1717$ (Hợp đồng kỳ hạn bị ĐẮT / Overvalued)
- **Chiến lược (Arbitrage Strategy)**: **Bán cái đắt, Mua cái rẻ (Cash-and-Carry Arbitrage)**.  
  Bán hợp đồng kỳ hạn EUR (Short Forward EUR) và tạo lập vị thế mua EUR tổng hợp (Vay USD mua EUR giao ngay gửi tiết kiệm).

- **Thiết lập các bước giao dịch cụ thể với 400,000 USD**:
  1. **Tại $t=0$**:
     - Vay $400,000$ USD với lãi suất $4.5\%$/năm trong 6 tháng.
     - Đổi ngay sang EUR theo tỷ giá giao ngay $1.1600$:
       $$\text{Số EUR nhận được} = \frac{400,000}{1.1600} = 344,827.5862 \text{ EUR}$$
     - Gửi toàn bộ số EUR này vào ngân hàng châu Âu với lãi suất $2.5\%$/năm trong 6 tháng.
     - Ký hợp đồng Bán kỳ hạn (Short Forward) đồng EUR tại mức tỷ giá $1.1900$ với khối lượng đúng bằng lượng EUR sẽ nhận được sau 6 tháng.
     - **Dòng tiền ròng tại $t=0$**: $+400,000 - 400,000 = \mathbf{0 \text{ USD}}$.
  2. **Tại đáo hạn $T = 0.5$ năm**:
     - Số dư tài khoản tiết kiệm EUR nở ra:
       $$\text{EUR thu về} = 344,827.5862 \cdot e^{0.025 \times 0.5} = 344,827.5862 \cdot e^{0.0125} = 349,165.7354 \text{ EUR}$$
     - Giao số EUR này theo hợp đồng Short Forward tại tỷ giá $1.1900$, thu về USD:
       $$\text{USD thu về} = 349,165.7354 \times 1.1900 = \mathbf{415,507.23 \text{ USD}}$$
     - Trả nợ khoản vay USD ban đầu:
       $$\text{USD trả nợ} = 400,000 \cdot e^{0.045 \times 0.5} = 400,000 \cdot e^{0.0225} = \mathbf{409,102.90 \text{ USD}}$$
     - **Lợi nhuận chênh lệch giá chắc chắn 100% (Arbitrage Profit)**:
       $$\Pi = 415,507.23 - 409,102.90 = \mathbf{+6,404.33 \text{ USD}}$$

---

#### Trường hợp (b): Tỷ giá niêm yết $F = 1.1500 < F^* = 1.1717$ (Hợp đồng kỳ hạn bị RẺ / Undervalued)
- **Chiến lược (Arbitrage Strategy)**: **Mua cái rẻ, Bán cái đắt (Reverse Cash-and-Carry Arbitrage)**.  
  Mua hợp đồng kỳ hạn EUR (Long Forward EUR) và bán khống EUR giao ngay (Vay EUR đổi ra USD gửi tiết kiệm).

- **Thiết lập các bước giao dịch cụ thể**:
  1. **Tại $t=0$**:
     - Vay một lượng EUR có giá trị đúng bằng $400,000$ USD:
       $$\text{Vay EUR} = \frac{400,000}{1.1600} = 344,827.5862 \text{ EUR}$$
     - Đổi ngay sang USD theo tỷ giá giao ngay thu về $400,000$ USD.
     - Đem gửi tiết kiệm USD với lãi suất $4.5\%$/năm trong 6 tháng.
     - Ký hợp đồng Mua kỳ hạn (Long Forward EUR) ở mức giá rẻ $1.1500$ với khối lượng đúng bằng lượng nợ EUR phải trả sau 6 tháng.
     - **Dòng tiền ròng tại $t=0$**: $\mathbf{0 \text{ USD}}$.
  2. **Tại đáo hạn $T = 0.5$ năm**:
     - Khoản tiền gửi tiết kiệm USD nở ra:
       $$\text{USD thu về} = 400,000 \cdot e^{0.045 \times 0.5} = \mathbf{409,102.90 \text{ USD}}$$
     - Khoản nợ EUR phải hoàn trả:
       $$\text{Nợ EUR} = 344,827.5862 \cdot e^{0.025 \times 0.5} = 349,165.7354 \text{ EUR}$$
     - Thực hiện hợp đồng Long Forward, dùng USD để mua $349,165.7354$ EUR với giá $1.1500$:
       $$\text{Chi phí USD mua EUR} = 349,165.7354 \times 1.1500 = \mathbf{401,540.60 \text{ USD}}$$
     - Dùng số EUR mua được để thanh toán dứt điểm khoản nợ EUR.
     - **Lợi nhuận chênh lệch giá chắc chắn 100% (Arbitrage Profit)**:
       $$\Pi = 409,102.90 - 401,540.60 = \mathbf{+7,562.30 \text{ USD}}$$

---

### Question 7 (L09 In-Class Q7)
**Original Question:**  
Assume deterministic interest rates and no transaction costs.  
- (a) **Index futures**: A six-month futures contract on the Sigma index trades at 4,200. The risk-free rate is 3% per annum, continuously compounded, and the continuous dividend yield is 1.2% per annum. What is the no-arbitrage spot index level?  
- (b) **Bond futures**: Calculate the six-month futures price for delivery of a specified bond.  
  - Full (dirty) spot price: USD 98.50 per USD 100 face value.  
  - Risk-free rate: 6% effective annual rate.  
  - The only coupon before delivery is USD 2.50 per USD 100 face value, paid in two months.  
- (c) **Convenience yield**: Oil trades at USD 74.00 per barrel; the six-month futures price is USD 72.80. The continuously compounded risk-free rate is 3.5% per annum. What is the implied net annual convenience yield $y$ (convenience yield less storage costs), expressed with continuous compounding?  

**Tóm tắt đề bài:**  
- (a) Hợp đồng tương lai chỉ số Sigma 6 tháng có giá $F = 4,200$. Lãi suất liên tục $r = 3\%$, tỷ suất cổ tức liên tục $q = 1.2\%$. Tính mức chỉ số giao ngay $S_0$?  
- (b) Giá tương lai trái phiếu 6 tháng. Giá giao ngay toàn phần (dirty price) $S_0 = 98.50$ USD. Lãi suất hiệu dụng năm $r = 6\%$. Coupon duy nhất trước khi giao hàng là 2.50 USD trả sau 2 tháng. Tính giá tương lai $F$?  
- (c) Dầu giao ngay $S_0 = 74.00$ USD/thùng; giá tương lai 6 tháng $F = 72.80$ USD. Lãi suất liên tục $r = 3.5\%$. Tính tỷ suất lợi ích tiện ích ròng hàng năm $y$?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

#### (a) Spot Index Level ($S_0$):
- Công thức: $F = S_0 \cdot e^{(r - q)T} \implies S_0 = F \cdot e^{-(r - q)T}$
- Với $T = 0.5$ năm, $r = 0.03$, $q = 0.012$:
  $$r - q = 0.03 - 0.012 = 0.018 \text{ (1.8\%)}$$
  $$(r - q)T = 0.018 \times 0.5 = 0.009$$
- Thay số:
  $$S_0 = 4,200 \cdot e^{-0.009} = 4,200 \times 0.9910404 = \mathbf{4,162.3696} \approx \mathbf{4,162.37}$$

#### (b) Bond Futures Price ($F$):
- Thời điểm giao hàng: $T = \frac{6}{12} = 0.5$ năm.
- Thời điểm nhận coupon: $t_c = \frac{2}{12} = \frac{1}{6}$ năm; giá trị coupon $C = 2.50$ USD.
- Lãi suất hiệu dụng năm (Effective Annual Rate): $r = 6\% = 0.06$.
- **Hiện giá của Coupon (Present Value of Coupon)**:
  $$PV(C) = \frac{C}{(1 + r)^{t_c}} = \frac{2.50}{(1.06)^{1/6}} = \frac{2.50}{1.009759} \approx 2.4758 \text{ USD}$$
- **Giá tương lai trái phiếu (Bond Futures Price)**:
  $$F = \left[ S_0 - PV(C) \right] \cdot (1 + r)^T = (98.50 - 2.4758) \cdot (1.06)^{0.5}$$
  $$F = 96.0242 \times 1.029563 = \mathbf{98.8629 \text{ USD}} \approx \mathbf{98.86 \text{ USD}}$$

#### (c) Implied Net Convenience Yield ($y$):
- Mô hình cõng vốn có tỷ suất lợi ích tiện ích ròng:
  $$F = S_0 \cdot e^{(r - y)T}$$
- Lấy logarit hai vế:
  $$\ln\left(\frac{F}{S_0}\right) = (r - y) \cdot T \implies r - y = \frac{1}{T} \ln\left(\frac{F}{S_0}\right)$$
  $$y = r - \frac{1}{T} \ln\left(\frac{F}{S_0}\right)$$
- Thay số $S_0 = 74.00$, $F = 72.80$, $T = 0.5$, $r = 0.035$:
  $$\frac{F}{S_0} = \frac{72.80}{74.00} \approx 0.9837838$$
  $$\ln(0.9837838) \approx -0.0163493$$
  $$y = 0.035 - \frac{-0.0163493}{0.5} = 0.035 + 0.0326986 = \mathbf{0.067699} \implies \mathbf{6.77\% \text{ per annum}}$$
- **Ý nghĩa kinh tế**:  
  Do giá tương lai thấp hơn giá giao ngay ($72.80 < 74.00$ USD $\implies$ Thị trường ở trạng thái **Backwardation**), điều này chỉ ra rằng việc cầm giữ thùng dầu vật chất trong tay đem lại một lợi ích phòng hộ khan hiếm rất lớn ($y = 6.77\%$), vượt xa chi phí lãi vay tài trợ ($r = 3.5\%$)!

---

### Question 8 (L09 In-Class Q8)
**Original Question:**  
All interest rates are effective annual rates. Ignore transaction costs other than the stated storage cost.  
1. **Commodity forward**: Kappa observes a spot price of USD 1,250 per unit and a one-year forward price of USD 1,375.  
   - Storage costs 2% of today's spot price, payable at the end of the year. There is no income or convenience yield.  
   - (a) What risk-free rate is implied by these prices?  
   - (b) If the actual risk-free borrowing and lending rate is 5%, what arbitrage strategy is possible, and what is the profit per unit?  
2. **Currency forward**: The spot exchange rate is 0.0550 USD per MXN; the one-year forward rate is 0.0565 USD per MXN. The USD risk-free rate is 5%.  
   - What is the implied MXN risk-free rate?  

**Tóm tắt đề bài:**  
Tất cả lãi suất là lãi suất hiệu dụng năm.  
1. Hàng hóa: $S_0 = 1,250$ USD, $F = 1,375$ USD, kỳ hạn 1 năm. Chi phí lưu kho $= 2\% \times S_0$ trả vào cuối năm.  
   - (a) Lãi suất phi rủi ro hàm ý là bao nhiêu?  
   - (b) Nếu lãi suất thực tế là 5%, chiến lược kinh doanh chênh lệch giá là gì? Lợi nhuận mỗi đơn vị?  
2. Tiền tệ: Tỷ giá giao ngay $0.0550$ USD/MXN, tỷ giá kỳ hạn 1 năm $0.0565$ USD/MXN. Lãi suất USD là 5%.  
   - Lãi suất MXN hàm ý là bao nhiêu?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

#### 1. Commodity Forward:
- Chi phí lưu kho trả tại cuối năm:  
  $$\text{Storage}_T = 2\% \times 1,250 = 25 \text{ USD}$$
- **(a) Implied Risk-Free Rate ($r$)**:  
  Theo nguyên lý cõng vốn rời rạc, tổng chi phí để giữ 1 đơn vị hàng hóa đến cuối năm là chi phí mua hàng cộng lãi vay, cộng thêm chi phí lưu kho cuối năm:
  $$F = S_0 \cdot (1 + r) + \text{Storage}_T$$
  $$1,375 = 1,250 \cdot (1 + r) + 25$$
  $$1,250 \cdot (1 + r) = 1,350 \implies 1 + r = \frac{1,350}{1,250} = 1.08 \implies \mathbf{r = 8.00\%}$$

- **(b) Arbitrage Strategy when Actual $r = 5\%$**:  
  - Giá kỳ hạn hợp lý theo lãi suất thực tế 5%:
    $$F^* = 1,250 \times 1.05 + 25 = 1,312.50 + 25 = 1,337.50 \text{ USD}$$
  - So sánh: $F_{\text{market}} = 1,375 > F^* = 1,337.50 \implies$ **Giá kỳ hạn trên thị trường bị ĐẮT (Overvalued)**.
  - **Chiến lược: Cash-and-Carry Arbitrage (Mua giao ngay, Bán kỳ hạn)**:
    - **Tại $t=0$**: Vay $1,250$ USD với lãi suất $5\%$/năm $\rightarrow$ Mua 1 đơn vị hàng hóa với giá $1,250$ USD $\rightarrow$ Ký hợp đồng Short Forward tại giá $1,375$ USD. Dòng tiền hôm nay $= 0$.
    - **Tại $T=1$**:
      - Giao hàng hóa theo hợp đồng Short Forward, thu về: $+1,375$ USD.
      - Thanh toán tiền lưu kho: $-25$ USD.
      - Trả nợ ngân hàng (cả gốc và lãi): $-1,250 \times 1.05 = -1,312.50$ USD.
      - **Lợi nhuận ròng chắc chắn 100%**:
        $$\Pi = 1,375 - 25 - 1,312.50 = \mathbf{+37.50 \text{ USD per unit}}$$

#### 2. Currency Forward (USD/MXN):
- Theo Ngang giá Lãi suất có Phòng ngừa dạng rời rạc:
  $$F = S_0 \cdot \frac{1 + r_{USD}}{1 + r_{MXN}}$$
- Thay số $S_0 = 0.0550$, $F = 0.0565$, $r_{USD} = 0.05$:
  $$0.0565 = 0.0550 \cdot \frac{1.05}{1 + r_{MXN}}$$
  $$1 + r_{MXN} = \frac{0.0550 \times 1.05}{0.0565} = \frac{0.05775}{0.0565} \approx 1.02212389$$
  $$r_{MXN} = 1.02212389 - 1 \approx \mathbf{0.022212} \implies \mathbf{2.2212\% \text{ per annum}}$$

---

### Question 9 (L09 In-Class Q9)
**Original Question:**  
Lambda pays 4.2% fixed and receives floating from Mu under a one-year swap.  
- Notional: USD 24 million; quarterly payments with $\Delta=0.25$.  
- The annualized compounded floating rates realized over the four quarters are 3.6%, 4.8%, 4.1%, and 5.1%.  
(a) Calculate both legs and the net settlement each quarter. Identify who pays whom.  
(b) What is Lambda's total net receipt over the year, without discounting? What principal payment is due under the swap at maturity?  

**Tóm tắt đề bài:**  
Hợp đồng hoán đổi lãi suất 1 năm giữa Lambda và Mu. Vốn danh nghĩa $N = 24$ triệu USD. Thanh toán hàng quý ($\Delta = 0.25$).  
- Lambda trả lãi cố định $4.2\%$/năm, nhận lãi thả nổi từ Mu.  
- Lãi suất thả nổi thực tế 4 quý lần lượt là: $3.6\%$, $4.8\%$, $4.1\%$, $5.1\%$.  
(a) Tính số tiền mỗi vế và khoản thanh toán bù trừ ròng từng quý. Xác định ai trả tiền cho ai?  
(b) Tổng số tiền ròng Lambda nhận được trong cả năm (không chiết khấu)? Khoản thanh toán vốn gốc nào phải trả khi đáo hạn?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

**Vế cố định (Fixed Leg)** Lambda phải trả mỗi quý là cố định:
$$\text{Fixed Payment} = N \cdot K \cdot \Delta = 24,000,000 \times 0.042 \times 0.25 = \mathbf{252,000 \text{ USD}} \text{ (0.252 triệu USD)}$$

#### (a) Bảng chi tiết dòng tiền từng quý (Cash Flow Breakdown):
| Quý ($k$) | Lãi suất thả nổi ($L_k$) | Vế thả nổi Mu trả ($N \cdot L_k \cdot 0.25$) | Vế cố định Lambda trả ($N \cdot K \cdot 0.25$) | Thu ròng của Lambda ($\text{Floating} - \text{Fixed}$) | Bên thực hiện thanh toán (Settlement) |
|:---:|:---:|:---:|:---:|:---:|:---|
| **Q1** | $3.6\%$ | $24\text{M} \times 0.036 \times 0.25 = \$216,000$ | $\$252,000$ | $-\$36,000$ | **Lambda trả cho Mu $\$36,000$** |
| **Q2** | $4.8\%$ | $24\text{M} \times 0.048 \times 0.25 = \$288,000$ | $\$252,000$ | $+\$36,000$ | **Mu trả cho Lambda $\$36,000$** |
| **Q3** | $4.1\%$ | $24\text{M} \times 0.041 \times 0.25 = \$246,000$ | $\$252,000$ | $-\$6,000$ | **Lambda trả cho Mu $\$6,000$** |
| **Q4** | $5.1\%$ | $24\text{M} \times 0.051 \times 0.25 = \$306,000$ | $\$252,000$ | $+\$54,000$ | **Mu trả cho Lambda $\$54,000$** |

#### (b) Tổng thu ròng và Vốn gốc khi đáo hạn:
- **Tổng số tiền ròng Lambda nhận được trong cả năm (Undiscounted Total)**:
  $$\text{Total Net Receipt} = -36,000 + 36,000 - 6,000 + 54,000 = \mathbf{+48,000 \text{ USD}}$$
- **Thanh toán vốn gốc khi đáo hạn (Principal Payment at Maturity)**:  
  **BẰNG KHÔNG (ZERO / $\$0 USD)**!  
  *Giải thích bản chất*: Trong hợp đồng hoán đổi lãi suất đơn thuần (Plain Vanilla IRS), vốn danh nghĩa (Notional) chỉ là một con số tham chiếu trên giấy tờ để tính toán dòng tiền lãi. Hai bên **hoàn toàn không trao đổi hay hoàn trả vốn gốc** ở bất kỳ thời điểm nào!

---

### Question 10 (L09 In-Class Q10)
**Original Question:**  
Eta and Theta can enter a swap exchanging 4.4% fixed for floating rate $L$.  
- All rates are annual payment rates.  
- Within each case, the loan or investment and swap have matching notionals, maturities, payment dates, accrual periods, and floating-rate conventions. Ignore fees.  
Consider the two cases independently:  
| Case | Eta's existing position | Eta wants | Theta's existing position | Theta wants |
|:---|:---|:---|:---|:---|
| Borrowing | Pays $L+0.7\%$ | Fixed cost | Pays 5.4% | Floating cost |
| Investment | Receives 4.0% | Floating income | Receives $L-0.3\%$ | Fixed income |
(a) For each case, choose each party's swap direction and calculate its net annual borrowing cost or investment income.  
(b) In the investment case, does the swap remove the credit risk of the underlying investments? Explain briefly.  

**Tóm tắt đề bài:**  
Hợp đồng hoán đổi: 4.4% cố định đổi lấy lãi suất thả nổi $L$.  
- Vay nợ: Eta đang trả $L+0.7\%$ (muốn cố định), Theta đang trả $5.4\%$ cố định (muốn thả nổi).  
- Đầu tư: Eta đang nhận $4.0\%$ cố định (muốn thả nổi), Theta đang nhận $L-0.3\%$ thả nổi (muốn cố định).  
(a) Xác định chiều hoán đổi cho mỗi bên và tính chi phí đi vay ròng / thu nhập đầu tư ròng?  
(b) Trong trường hợp đầu tư, hợp đồng hoán đổi có loại bỏ được rủi ro tín dụng của tài sản đầu tư cơ sở không?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

#### (a) Lựa chọn chiều hoán đổi & Dòng tiền ròng:

**1. Trường hợp Vay nợ (Borrowing Case):**
- **Eta**: Đang có nợ thả nổi ($L+0.7\%$), muốn biến thành nợ cố định $\implies$ **Eta tham gia vị thế TRẢ CỐ ĐỊNH (Pays Fixed 4.4%), NHẬN THẢ NỔI (Receives Floating $L$)**.
  $$\text{Chi phí đi vay ròng của Eta} = \underbrace{(L + 0.7\%)}_{\text{Trả nợ hiện tại}} + \underbrace{4.4\%}_{\text{Trả cố định theo swap}} - \underbrace{L}_{\text{Nhận thả nổi theo swap}} = \mathbf{5.1\% \text{ cố định (Fixed)}}$$
- **Theta**: Đang có nợ cố định ($5.4\%$), muốn biến thành nợ thả nổi $\implies$ **Theta tham gia vị thế TRẢ THẢ NỔI (Pays Floating $L$), NHẬN CỐ ĐỊNH (Receives Fixed 4.4%)**.
  $$\text{Chi phí đi vay ròng của Theta} = \underbrace{5.4\%}_{\text{Trả nợ hiện tại}} + \underbrace{L}_{\text{Trả thả nổi theo swap}} - \underbrace{4.4\%}_{\text{Nhận cố định theo swap}} = \mathbf{L + 1.0\% \text{ thả nổi (Floating)}}$$

**2. Trường hợp Đầu tư (Investment Case):**
- **Eta**: Đang nhận lãi cố định ($4.0\%$), muốn chuyển thành thu nhập thả nổi $\implies$ **Eta tham gia vị thế TRẢ CỐ ĐỊNH (Pays Fixed 4.4%), NHẬN THẢ NỔI (Receives Floating $L$)**.
  $$\text{Thu nhập đầu tư ròng của Eta} = \underbrace{4.0\%}_{\text{Thu nhập hiện tại}} - \underbrace{4.4\%}_{\text{Trả cố định theo swap}} + \underbrace{L}_{\text{Nhận thả nổi theo swap}} = \mathbf{L - 0.4\% \text{ thả nổi (Floating)}}$$
- **Theta**: Đang nhận lãi thả nổi ($L - 0.3\%$), muốn chuyển thành thu nhập cố định $\implies$ **Theta tham gia vị thế TRẢ THẢ NỔI (Pays Floating $L$), NHẬN CỐ ĐỊNH (Receives Fixed 4.4%)**.
  $$\text{Thu nhập đầu tư ròng của Theta} = \underbrace{(L - 0.3\%)}_{\text{Thu nhập hiện tại}} - \underbrace{L}_{\text{Trả thả nổi theo swap}} + \underbrace{4.4\%}_{\text{Nhận cố định theo swap}} = \mathbf{4.1\% \text{ cố định (Fixed)}}$$

#### (b) Rủi ro tín dụng của tài sản đầu tư (Credit Risk):
- **Câu trả lời**: **KHÔNG (NO)**. Hợp đồng hoán đổi **HOÀN TOÀN KHÔNG loại bỏ rủi ro tín dụng của các tài sản đầu tư cơ sở**!
- **Giải thích chi tiết (Explanation)**:  
  Hợp đồng hoán đổi lãi suất chỉ là một hợp đồng phái sinh độc lập bên ngoài để biến đổi thuộc tính dòng tiền lãi (từ cố định sang thả nổi và ngược lại). Nếu tổ chức phát hành tài sản đầu tư ban đầu bị phá sản hoặc vỡ nợ (Default), nhà đầu tư (Eta hoặc Theta) **vẫn phải gánh chịu toàn bộ tổn thất mất vốn gốc và lãi của khoản đầu tư đó**. Thậm chí, việc tham gia hợp đồng hoán đổi còn làm phát sinh thêm **rủi ro đối tác mới (Counterparty Risk)**: nguy cơ đối tác hoán đổi không thực hiện nghĩa vụ thanh toán của họ.

---

### Question 11 (L09 In-Class Q11)
**Original Question:**  
Epsilon needs EUR 10 million for three years. It borrows USD 12 million at 5% annual interest, with principal repaid at maturity, and enters a fixed-for-fixed currency swap with Zeta.  
- Spot exchange rate at inception: 1.20 USD per EUR.  
- Swap notionals: USD 12 million and EUR 10 million.  
- Epsilon receives 5% on the USD notional and pays 3.6% on the EUR notional, annually.  
- The principals are exchanged at inception and reversed at maturity. Ignore fees.  
(a) Show Epsilon's swap cash flows in each currency at inception, in years 1-2, and at maturity.  
(b) Combine the swap with the USD loan. What are Epsilon's net cash flows and effective annual EUR borrowing cost?  
(c) If the loan instead charges 5.6%, with all swap terms unchanged, is the funding entirely converted into fixed EUR payments? Quantify any remaining exposure.  

**Tóm tắt đề bài:**  
Epsilon cần 10 triệu EUR trong 3 năm. Công ty đi vay 12 triệu USD với lãi suất $5\%$/năm trả gốc cuối kỳ, đồng thời ký hợp đồng hoán đổi tiền tệ cố định - cố định với Zeta.  
- Tỷ giá giao ngay: $1.20$ USD/EUR ($10\text{M EUR} \times 1.20 = 12\text{M USD}$).  
- Epsilon nhận $5\%$/năm trên vốn 12 triệu USD và trả $3.6\%$/năm trên vốn 10 triệu EUR.  
- Vốn gốc được trao đổi tại thời điểm ban đầu và hoàn trả ngược lại khi đáo hạn.  
(a) Trình bày dòng tiền của swap theo từng đồng tiền tại $t=0$, năm 1-2, và khi đáo hạn năm 3?  
(b) Kết hợp swap với khoản vay USD. Dòng tiền ròng tổng thể và chi phí đi vay EUR hiệu dụng là bao nhiêu?  
(c) Nếu khoản vay USD có lãi suất là $5.6\%$/năm trong khi swap giữ nguyên 5%, khoản tài trợ có được chuyển đổi hoàn toàn sang EUR cố định không? Định lượng rủi ro còn lại?  

**Detailed Bilingual Solution & Step-by-Step Calculation:**

#### (a) Dòng tiền của Swap đối với Epsilon (Swap Cash Flows for Epsilon):
- **Tại thời điểm bắt đầu ($t=0$)**:
  - Epsilon giao vốn gốc USD: **-12.00 triệu USD**
  - Epsilon nhận vốn gốc EUR: **+10.00 triệu EUR**
- **Hàng năm (Năm 1 và Năm 2)**:
  - Nhận lãi USD: $+12\text{M} \times 5\% = \mathbf{+0.60 \text{ triệu USD}}$
  - Trả lãi EUR: $-10\text{M} \times 3.6\% = \mathbf{-0.36 \text{ triệu EUR}}$
- **Tại thời điểm đáo hạn ($t=3$ năm)**:
  - Nhận lãi + hoàn vốn gốc USD: $+0.60\text{M} + 12\text{M} = \mathbf{+12.60 \text{ triệu USD}}$
  - Trả lãi + hoàn vốn gốc EUR: $-0.36\text{M} - 10\text{M} = \mathbf{-10.36 \text{ triệu EUR}}$

| Thời điểm | Dòng tiền USD từ Swap | Dòng tiền EUR từ Swap |
|---|---:|---:|
| **Năm 0 (Khởi tạo)** | $-12.00\text{ triệu USD}$ | $+10.00\text{ triệu EUR}$ |
| **Năm 1** | $+0.60\text{ triệu USD}$ | $-0.36\text{ triệu EUR}$ |
| **Năm 2** | $+0.60\text{ triệu USD}$ | $-0.36\text{ triệu EUR}$ |
| **Năm 3 (Đáo hạn)** | $+12.60\text{ triệu USD}$ | $-10.36\text{ triệu EUR}$ |

---

#### (b) Kết hợp Khoản vay USD và Hợp đồng Hoán đổi (Combined Portfolio):
Hãy lập bảng hợp nhất dòng tiền giữa khoản vay USD và hợp đồng swap:

| Thời điểm | Khoản vay USD (USD Loan) | Hợp đồng Swap (USD Leg) | **Dòng tiền USD Ròng** | Hợp đồng Swap (EUR Leg) | **Dòng tiền Ròng Tổng thể** |
|---|---:|---:|:---:|---:|:---:|
| **Năm 0** | $+12.00\text{M USD}$ (giải ngân) | $-12.00\text{M USD}$ | **0 USD** | $+10.00\text{M EUR}$ | **+10.00 triệu EUR** |
| **Năm 1** | $-0.60\text{M USD}$ (trả lãi) | $+0.60\text{M USD}$ | **0 USD** | $-0.36\text{M EUR}$ | **-0.36 triệu EUR** |
| **Năm 2** | $-0.60\text{M USD}$ (trả lãi) | $+0.60\text{M USD}$ | **0 USD** | $-0.36\text{M EUR}$ | **-0.36 triệu EUR** |
| **Năm 3** | $-12.60\text{M USD}$ (gốc + lãi) | $+12.60\text{M USD}$ | **0 USD** | $-10.36\text{M EUR}$ | **-10.36 triệu EUR** |

- **Kết luận dòng tiền**: Toàn bộ dòng tiền USD đã triệt tiêu hoàn toàn bằng 0! Epsilon nhận được ngay 10 triệu EUR hôm nay, trả lãi 0.36 triệu EUR mỗi năm, và hoàn trả gốc 10 triệu EUR vào năm thứ 3.
- **Chi phí đi vay EUR hiệu dụng (Effective Annual EUR Borrowing Cost)**:
  $$\text{Effective EUR Cost} = \frac{0.36 \text{ triệu EUR}}{10.00 \text{ triệu EUR}} = \mathbf{3.60\% \text{ per annum}}$$
  *(Epsilon đã tổng hợp thành công một khoản vay bằng đồng EUR cố định ở mức lãi suất 3.6%/năm).*

---

#### (c) Trường hợp Lãi suất Vay USD là 5.6%:
- **Đánh giá chuyển đổi**: Khoản tài trợ **KHÔNG ĐƯỢC CHUYỂN ĐỔI HOÀN TOÀN** sang EUR cố định!
- **Định lượng rủi ro còn lại (Quantifying Remaining Exposure)**:
  - Nghĩa vụ trả lãi hàng năm cho khoản vay USD:
    $$\text{Lãi USD phải trả} = 12\text{M} \times 5.6\% = 0.672 \text{ triệu USD}$$
  - Dòng tiền USD nhận về từ hợp đồng Swap chỉ có:
    $$\text{Swap USD nhận về} = 12\text{M} \times 5.0\% = 0.600 \text{ triệu USD}$$
  - **Dòng tiền USD thiếu hụt ròng mỗi năm**:
    $$\Delta \text{USD} = 0.600\text{M} - 0.672\text{M} = \mathbf{-0.072 \text{ triệu USD} = -\$72,000 \text{ USD/năm}}$$
  - **Phân tích rủi ro tỷ giá**:  
    Epsilon vẫn còn một khoản **rủi ro tỷ giá trần trụi (Unhedged Foreign Exchange Exposure)** trị giá đúng **$\$72,000 USD mỗi năm** (tương đương chênh lệch $5.6\% - 5.0\% = 0.6\%$ trên 12 triệu USD) trong suốt 3 năm. Nếu đồng USD tăng giá mạnh so với EUR, Epsilon sẽ phải tốn nhiều EUR hơn để mua 72,000 USD này nhằm trang trải phần lãi vay thiếu hụt!
