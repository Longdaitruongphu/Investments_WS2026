# MASTER LECTURE GUIDE & IN-CLASS QUESTIONS (LECTURES 01 - 07)
## HƯỚNG DẪN BÀI GIẢNG & GIẢI CHI TIẾT CÂU HỎI TRÊN LỚP (SONG NGỮ ANH - VIỆT)
**Course: BFIN Investments (WS2026)**  
*Comprehensive In-Class Questions, Answers, Deep Mathematical Derivations, Economic Intuitions, and Exam Pitfalls*  
*(Tổng hợp câu hỏi trên lớp, lời giải chi tiết, khảo sát toán học, bản chất kinh tế và bẫy thi)*

---

# LECTURE 01: Investment Environment and Instruments
*(Môi trường Đầu tư và Các Công cụ Tài chính)*

## 1. Core Concepts & Theoretical Framework (Khung Lý thuyết Cốt lõi)
- **Real Assets vs. Financial Assets (Tài sản thực vs. Tài sản tài chính)**:
  - *Real Assets (Tài sản thực)*: Physical productive assets (land, buildings, equipment, patents, human capital) used to produce goods and services. They generate net income to the economy. *(Đất đai, nhà xưởng, máy móc, bằng sáng chế, nguồn nhân lực; trực tiếp tạo ra của cải và giá trị gia tăng ròng cho xã hội).*
  - *Financial Assets (Tài sản tài chính)*: Contractual claims on real assets or the cash flows they generate (stocks, bonds, options, bank deposits). They allocate wealth, income, and risk among economic agents. In aggregate, they net out to zero (every financial asset is an asset to one party and a liability to another). *(Các chứng từ xác lập quyền đòi đối với tài sản thực hoặc dòng tiền từ tài sản thực; phân bổ thu nhập và phân tán rủi ro; tổng giá trị tài sản tài chính trong toàn nền kinh tế triệt tiêu bằng 0).*
- **Primary vs. Secondary Markets (Thị trường Sơ cấp vs. Thị trường Thứ cấp)**:
  - *Primary Market (Sơ cấp)*: New issuance of securities (IPO, SEO, corporate bond issuance). **The issuer receives new financing/capital**. *(Doanh nghiệp phát hành nhận được tiền vốn mới phục vụ đầu tư kinh doanh).*
  - *Secondary Market (Thứ cấp)*: Trading of existing securities between investors (NYSE, Nasdaq). **The issuer receives zero new financing**. Secondary markets provide liquidity and price discovery. *(Giao dịch mua đi bán lại giữa các nhà đầu tư; doanh nghiệp phát hành không nhận thêm vốn; vai trò chính là tạo thanh khoản và định giá thị trường).*
- **Investment Process (Quy trình Đầu tư)**:
  - *Top-Down (Từ trên xuống)*: Asset Allocation first (phân bổ vốn vào các nhóm tài sản lớn: Cổ phiếu, Trái phiếu, Tiền mặt) $\rightarrow$ Security Selection second (chọn mã cụ thể).
  - *Bottom-Up (Từ dưới lên)*: Security Selection directly based on individual fundamental valuation, largely ignoring broader macroeconomic asset-class weights.
- **Financial Instruments Summary (Tóm tắt Công cụ Tài chính)**:
  - *Money Market*: Debt instruments with maturity $\le 1$ year (T-bills, Commercial Paper, Repos, CDs, Fed Funds). High liquidity, negligible default risk.
  - *Capital Market*: Long-term debt (Treasury notes/bonds, corporate bonds) and equity (common stock, preferred stock).
  - *Derivatives*: Call options (right to buy at $X$), Put options (right to sell at $X$), Futures/Forwards (mutual obligation to buy/sell at agreed delivery price $F$).
  - *Stock Indexes*: Price-weighted (DJIA, weight $\propto$ share price, sensitive to splits), Market-value-weighted (S&P 500, weight $\propto P \times Q$), Equal-weighted.

---

# LECTURE 02: Bond Prices, Yields, and the Term Structure
*(Định giá Trái phiếu, Lợi suất và Cấu trúc Kỳ hạn Lãi suất)*

### Question 2.1
**Original Question:**  
Kappa observes a 1-year zero-coupon yield of 4% and a 2-year zero-coupon yield of 5%, both with annual compounding.
- What is the implied 1-year forward rate for year 2?
- Under the Expectations Hypothesis, what does it imply about the expected short rate?
- Under Liquidity Preference Theory, could the expected short rate instead remain at 4%? Explain.

**Tóm tắt đề bài (Vietnamese Summary):**  
Lãi suất zero-coupon 1 năm là $s_1 = 4\%$, 2 năm là $s_2 = 5\%$ (ghép lãi hàng năm).
- Tính lãi suất kỳ hạn 1 năm cho năm thứ 2 ($f_{1,2}$)?
- Theo Giả thuyết Kỳ vọng (PEH), lãi suất ngắn hạn kỳ vọng trong năm 2 là bao nhiêu?
- Theo Lý thuyết Ưu tiên Thanh khoản (LPT), lãi suất ngắn hạn kỳ vọng có thể giữ nguyên ở mức 4% không? Giải thích.

**Detailed Bilingual Solution & Explanation (Giải chi tiết & Bản chất):**
1. **Implied 1-Year Forward Rate ($f_{1,2}$)**:
   - Theo nguyên lý phi kinh doanh chênh lệch giá (No-Arbitrage Condition):
     $$(1 + s_2)^2 = (1 + s_1)^1 \times (1 + f_{1,2})$$
   - Thay số:
     $$(1.05)^2 = (1.04) \times (1 + f_{1,2}) \implies 1.1025 = 1.04 \times (1 + f_{1,2})$$
     $$f_{1,2} = \frac{1.1025}{1.04} - 1 = \frac{1.05^2}{1.04} - 1 \approx 0.060096 \approx 6.01\%$$
2. **Under the Pure Expectations Hypothesis (PEH)**:
   - Giả thuyết Kỳ vọng thuần túy giả định phần bù rủi ro kỳ hạn bằng 0 (Zero Liquidity Premium: $LP_2 = 0$).
   - Do đó, lãi suất kỳ hạn chính là kỳ vọng không chệch của lãi suất ngắn hạn trong tương lai:
     $$E(r_2) = f_{1,2} \approx 6.01\%$$
   - Thị trường đang kỳ vọng lãi suất ngắn hạn 1 năm sẽ tăng từ 4% lên 6.01%.
3. **Under Liquidity Preference Theory (LPT)**:
   - LPT cho rằng nhà đầu tư đòi hỏi một khoản phần bù thanh khoản dương ($LP_2 > 0$) để bù đắp rủi ro lãi suất khi cam kết vốn kỳ hạn dài:
     $$f_{1,2} = E(r_2) + LP_2$$
   - Nếu lãi suất ngắn hạn kỳ vọng thực chất không tăng mà giữ nguyên ở mức $E(r_2) = 4\%$, thì:
     $$6.01\% = 4.00\% + LP_2 \implies LP_2 = 2.01\%$$
   - **Kết luận kinh tế**: Điều này hoàn toàn có thể xảy ra! Một đường cong lợi suất dốc lên ($s_1 < s_2$) tự nó **không nhất thiết** chứng minh rằng thị trường kỳ vọng lãi suất sẽ tăng; nó có thể chỉ phản ánh một khoản phần bù thanh khoản dương ($LP > 0$).

---

### Question 2.2
**Original Question:**  
Beta considers two 10-year bonds: Bond A is an option-free straight bond with an 8% coupon; Bond B is identical but callable at par after 5 years.
- Which bond will trade at a higher price, and which has a higher yield to maturity?
- How does the presence of the call option affect the bond's convexity at low market interest rates?

**Tóm tắt đề bài:**  
So sánh trái phiếu 10 năm không kèm quyền chọn A (straight bond, coupon 8%) và trái phiếu B y hệt nhưng tổ chức phát hành có quyền mua lại (callable bond) tại mệnh giá sau 5 năm.
- Trái phiếu nào có giá cao hơn, trái phiếu nào có YTM cao hơn?
- Quyền mua lại ảnh hưởng thế nào đến độ lồi (convexity) của trái phiếu ở mức lãi suất thị trường thấp?

**Detailed Bilingual Solution & Explanation:**
1. **Price & Yield Comparison (So sánh Giá và Lợi suất)**:
   - Cấu trúc tài chính: $\text{Callable Bond} = \text{Straight Bond} - \text{Call Option on Bond}$.
   - Quyền mua lại thuộc về **tổ chức phát hành (issuer)**, gây bất lợi cho nhà đầu tư (trái chủ bị thu hồi trái phiếu khi lãi suất giảm để phát hành lại với lãi suất rẻ hơn).
   - Do nhà đầu tư phải chịu thiệt hại tiềm tàng này, họ chỉ đồng ý mua trái phiếu B ở **mức giá thấp hơn** ($P_B < P_A$).
   - Vì giá thấp hơn đối với cùng một dòng coupon cam kết, **Lợi suất đến ngày đáo hạn (YTM) của Bond B phải cao hơn Bond A** ($YTM_B > YTM_A$) để bù đắp rủi ro bị thu hồi (call risk).
2. **Effect on Convexity at Low Interest Rates (Độ lồi ở mức lãi suất thấp)**:
   - Đối với Straight Bond: Đường cong Giá - Lợi suất luôn lồi về gốc tọa độ (**Positive Convexity**).
   - Đối với Callable Bond: Khi lãi suất thị trường giảm sâu, giá trái phiếu không thể tăng vượt quá giá thu hồi (Call Price), vì khả năng nhà phát hành gọi lại trái phiếu tiến tới 100%. Đường cong giá bị chặn trên và uốn cong sang phải, tạo ra hiện tượng **Độ lồi âm (Negative Convexity)**.
   - **Hậu quả**: Khi lãi suất giảm mạnh, giá trái phiếu callable tăng rất ít; nhưng khi lãi suất tăng, giá vẫn giảm mạnh như bình thường!

---

### Question 2.3
**Original Question:**  
An investor expects interest rates to fall across all maturities. Between a 10-year 2% coupon bond and a 10-year 8% coupon bond (both yielding 6% initially), which bond offers greater percentage capital appreciation?

**Tóm tắt đề bài:**  
Nhà đầu tư kỳ vọng lãi suất sẽ giảm. Giữa trái phiếu 10 năm coupon 2% và trái phiếu 10 năm coupon 8% (cùng có YTM ban đầu là 6%), trái phiếu nào sẽ có mức tăng giá phần trăm lớn hơn?

**Detailed Bilingual Solution & Explanation:**
- **Key Principle (Định lý Malkiel số 4)**: Ceteris paribus (các yếu tố khác không đổi), trái phiếu có **lãi suất coupon càng thấp** thì có **Duration càng dài**, do đó **độ nhạy cảm về giá với lãi suất càng cao**.
- Trái phiếu coupon 2% dồn phần lớn giá trị hiện tại dòng tiền vào mệnh giá nhận ở năm thứ 10, trong khi trái phiếu coupon 8% trả nhiều dòng tiền sớm ở các năm đầu.
- Do đó: $D^*_{\text{Coupon 2\%}} > D^*_{\text{Coupon 8\%}}$.
- Khi lãi suất giảm ($\Delta y < 0$), mức thay đổi giá phần trăm:
  $$\frac{\Delta P}{P} \approx -D^* \Delta y > 0$$
- Trái phiếu coupon 2% có Duration lớn hơn nên sẽ **tăng giá phần trăm mạnh hơn nhiều** so với trái phiếu coupon 8%.

---

### Question 2.4
**Original Question:**  
Explain the structure of an inverse floater. If the coupon formula is $c = 12\% - 1.5 \times r_{\text{ref}}$, why does an inverse floater have exceptionally high interest rate risk (duration)?

**Tóm tắt đề bài:**  
Giải thích cấu trúc trái phiếu lãi suất thả dụng nghịch đảo (inverse floater). Nếu coupon là $c = 12\% - 1.5 \times r_{\text{ref}}$, tại sao nó lại chịu rủi ro lãi suất (duration) cực kỳ cao?

**Detailed Bilingual Solution & Explanation:**
- **Structure (Cấu trúc)**: Trái phiếu thả nổi nghịch đảo có lãi suất coupon tỷ lệ nghịch với lãi suất thị trường tham chiếu $r_{\text{ref}}$ (ví dụ SOFR hoặc LIBOR).
- **Cơ chế đòn bẩy kép (Dual / Compounded Interest Rate Risk)**:
  Khi lãi suất thị trường $r$ tăng:
  1. *Hiệu ứng chiết khấu (Discount Effect)*: Mọi dòng tiền tương lai bị chiết khấu ở lãi suất cao hơn, làm giảm giá trị hiện tại (giống trái phiếu thường).
  2. *Hiệu ứng cắt giảm dòng tiền (Cash Flow Reduction Effect)*: Bản thân dòng tiền coupon $c = 12\% - 1.5 r_{\text{ref}}$ bị co cụm giảm trực tiếp!
- Hai hiệu ứng này cộng hưởng cùng một chiều khiến giá của inverse floater lao dốc cực mạnh khi lãi suất tăng.
- **Hệ số Duration**: Duration của inverse floater thường gấp nhiều lần thời gian đáo hạn thực tế của nó (siêu nhạy cảm với lãi suất).

---

### Question 2.5
**Original Question:**  
What economic conditions are typically associated with an inverted yield curve ($s_1 > s_5$), and why is it considered a leading indicator of recessions?

**Tóm tắt đề bài:**  
Đường cong lợi suất đảo ngược ($s_1 > s_5$) thường gắn liền với bối cảnh kinh tế nào và tại sao nó là chỉ báo sớm của suy thoái kinh tế?

**Detailed Bilingual Solution & Explanation:**
- **Economic Mechanism (Cơ chế kinh tế)**:
  1. Khi lạm phát quá nóng, Ngân hàng Trung ương (như Fed) thắt chặt tiền tệ quyết liệt, đẩy lãi suất ngắn hạn ($s_1$) lên rất cao.
  2. Thị trường tài chính kỳ vọng rằng chính sách thắt chặt mạnh tay này sẽ làm đình trệ nền kinh tế, dẫn tới suy thoái.
  3. Để đối phó với suy thoái trong tương lai, Ngân hàng Trung ương sẽ buộc phải cắt giảm lãi suất mạnh mẽ trong các năm tới.
  4. Theo Giả thuyết Kỳ vọng (PEH), lãi suất dài hạn ($s_5$) là mức bình quân của các mức lãi suất ngắn hạn kỳ vọng trong 5 năm tới. Kỳ vọng lãi suất tương lai sụt giảm sâu sẽ kéo $s_5$ xuống thấp hơn $s_1$, tạo ra đường cong đảo ngược ($s_1 > s_5$).
- **Vai trò chỉ báo suy thoái**: Trong lịch sử hơn 60 năm qua, hầu như mọi cuộc suy thoái kinh tế lớn tại Mỹ đều xuất hiện sau khi đường cong lợi suất (chênh lệch 10Y - 2Y hoặc 10Y - 3M) bị đảo ngược từ 6 đến 18 tháng.

---

# LECTURE 03: Duration, Convexity, and Immunization
*(Thời lượng, Độ lồi và Chiến lược Miễn nhiễm Rủi ro)*

### Question 3.1
**Original Question:**  
Bond Alpha is a 3-year zero-coupon bond. Bond Beta is a 3-year 6% coupon bond. Both currently yield 6% (annual compounding).
- What is the Macaulay duration of Bond Alpha?
- Explain why the Macaulay duration of Bond Beta must be strictly less than 3 years without performing full arithmetic.

**Tóm tắt đề bài:**  
Trái phiếu Alpha là zero-coupon 3 năm. Trái phiếu Beta trả coupon 6% hàng năm, đáo hạn 3 năm. Cả 2 có YTM = 6%.
- Macaulay duration của Alpha là bao nhiêu?
- Giải thích tại sao Macaulay duration của Beta chắc chắn nhỏ hơn 3 năm mà không cần bấm máy tính?

**Detailed Bilingual Solution & Explanation:**
1. **Bond Alpha (Zero-Coupon Bond)**:
   - Dòng tiền duy nhất phát sinh tại thời điểm đáo hạn $t = 3$.
   - Trọng số $w_3 = 1.0$.
   - Macaulay duration: $D = 3.0$ năm.
2. **Bond Beta (Coupon Bond)**:
   - Macaulay duration là bình quân gia quyền của thời gian nhận dòng tiền:
     $$D = \sum_{t=1}^3 t \times w_t = 1 \times w_1 + 2 \times w_2 + 3 \times w_3$$
     với $\sum w_t = 1$ và $w_1, w_2, w_3 > 0$.
   - Do có các dòng coupon nhận được ở năm 1 ($w_1 > 0$) và năm 2 ($w_2 > 0$), trọng số thời gian được kéo về sớm hơn năm 3.
   - Vì $w_3 < 1$, giá trị bình quân gia quyền chắc chắn phải thỏa mãn:
     $$D < 3.0 \text{ năm}$$
   *(Tính toán chính xác: $D \approx 2.83$ năm).*

---

### Question 3.2
**Original Question:**  
A bond has a Macaulay duration of 5.4 years and trades at a YTM of 8% with semiannual compounding.
- Calculate its Modified Duration ($D^*$).
- If its yield increases by 25 basis points, estimate the percentage change in the bond's price using duration alone.

**Tóm tắt đề bài:**  
Trái phiếu có Macaulay duration 5.4 năm, YTM = 8% (ghép lãi nửa năm).
- Tính Modified duration ($D^*$)?
- Nếu lợi suất tăng 25 điểm cơ bản, dùng Duration ước tính phần trăm thay đổi giá trái phiếu?

**Detailed Bilingual Solution & Explanation:**
1. **Modified Duration ($D^*$)**:
   - Đối với trái phiếu ghép lãi bán niên ($m = 2$), lợi suất mỗi kỳ là $y/2 = 8\%/2 = 4\% = 0.04$:
     $$D^* = \frac{D}{1 + y/2} = \frac{5.4}{1 + 0.04} = \frac{5.4}{1.04} \approx 5.1923 \text{ năm}$$
   - *Bẫy đề thi*: Nếu chia cho $1 + 0.08$ là SAI vì trái phiếu ghép lãi nửa năm!
2. **Percentage Price Change Estimation (Ước tính thay đổi giá)**:
   - Thay đổi lợi suất: $\Delta y = +25 \text{ bps} = +0.0025$.
   - Công thức xấp xỉ Duration:
     $$\frac{\Delta P}{P} \approx -D^* \times \Delta y = -5.1923 \times (+0.0025) \approx -0.012981 = -1.298\%$$
   - **Kết luận**: Giá trái phiếu ước tính giảm khoảng 1.30%.

---

### Question 3.3
**Original Question:**  
Explain Dollar Duration ($D_{\$}$) and DV01. A portfolio has a market value of $50,000,000 and a Modified Duration of 6.2 years. Calculate its DV01.

**Tóm tắt đề bài:**  
Giải thích Dollar Duration và DV01. Danh mục có giá trị thị trường 50 triệu USD, Modified Duration 6.2 năm. Tính DV01 của danh mục.

**Detailed Bilingual Solution & Explanation:**
- **Definitions (Định nghĩa)**:
  - *Dollar Duration ($D_{\$})$*: Số tiền tuyệt đối mà giá trị danh mục thay đổi khi lãi suất thay đổi 1 đơn vị (100% hay 1.0):
    $$D_{\$} = D^* \times P = -\frac{dP}{dy}$$
  - *DV01 (Dollar Value of an 01 / PV01)*: Số tiền danh mục thay đổi khi lãi suất thay đổi đúng **1 điểm cơ bản (1 bp = 0.0001)**:
    $$DV01 = D^* \times P \times 0.0001 = D_{\$} \times 0.0001$$
- **Calculation (Tính toán)**:
  $$DV01 = 6.2 \times 50,000,000 \times 0.0001 = 310,000,000 \times 0.0001 = 31,000 \text{ USD}$$
- **Ý nghĩa kinh tế**: Cứ mỗi khi lãi suất thị trường tăng thêm 1 điểm cơ bản (0.01%), danh mục sẽ mất đi khoảng **31,000 USD** giá trị thị trường.

---

### Question 3.4
**Original Question:**  
A bond priced at 1,000 has Modified Duration $D^* = 8.0$ years and Convexity $C = 90.0$.
- Estimate the percentage price change using both duration and convexity for $\Delta y = +200$ bps and $\Delta y = -200$ bps.
- Compare these estimates with the duration-only approximation and explain the direction of error.

**Tóm tắt đề bài:**  
Trái phiếu giá 1,000 có $D^* = 8.0$ năm và $C = 90.0$.
- Ước tính phần trăm thay đổi giá kết hợp Duration và Convexity khi $\Delta y = +200$ bps và $\Delta y = -200$ bps.
- So sánh với ước tính chỉ dùng Duration và nhận xét chiều của sai số.

**Detailed Bilingual Solution & Explanation:**
- **Formula (Công thức xấp xỉ bậc 2)**:
  $$\frac{\Delta P}{P} \approx -D^* \Delta y + \frac{1}{2} C (\Delta y)^2$$
1. **Case 1: Lãi suất tăng 200 bps ($\Delta y = +0.02$)**:
   - Thành phần Duration: $-8.0 \times (+0.02) = -0.16 = -16.00\%$.
   - Thành phần Convexity: $\frac{1}{2} \times 90.0 \times (0.02)^2 = 45 \times 0.0004 = +0.018 = +1.80\%$.
   - Tổng xấp xỉ kết hợp:
     $$\frac{\Delta P}{P} \approx -16.00\% + 1.80\% = -14.20\%$$
   - *So sánh*: Nếu chỉ dùng Duration, dự báo là giảm $-16.00\%$. Thực tế nhờ có độ lồi ($+1.80\%$), giá chỉ giảm $-14.20\%$. Duration đã thổi phồng mức sụt giảm giá (đánh giá thấp giá trái phiếu).
2. **Case 2: Lãi suất giảm 200 bps ($\Delta y = -0.02$)**:
   - Thành phần Duration: $-8.0 \times (-0.02) = +0.16 = +16.00\%$.
   - Thành phần Convexity: $\frac{1}{2} \times 90.0 \times (-0.02)^2 = +1.80\%$.
   - Tổng xấp xỉ kết hợp:
     $$\frac{\Delta P}{P} \approx +16.00\% + 1.80\% = +17.80\%$$
   - *So sánh*: Nếu chỉ dùng Duration, dự báo giá tăng $+16.00\%$. Thực tế giá tăng tới $+17.80\%$. Duration đã ước tính thiếu mức tăng giá.
- **KẾT LUẬN QUAN TRỌNG NHẤT CỦA ĐỘ LỒI**: Do $\frac{1}{2} C (\Delta y)^2$ luôn dương, **xấp xỉ Duration luôn luôn đánh giá thấp (UNDERESTIMATES) giá trị thực tế của trái phiếu ở cả hai chiều biến động của lãi suất**!

---

### Question 3.5
**Original Question:**  
An institution holds two bonds: $30M market value of Bond 1 ($D^* = 3.0$ yrs) and $70M market value of Bond 2 ($D^* = 8.0$ yrs).
- Calculate the portfolio modified duration.
- If rates rise by 50 bps, estimate the dollar change in total portfolio value.

**Tóm tắt đề bài:**  
Danh mục gồm 30 triệu USD Bond 1 ($D^* = 3.0$ năm) và 70 triệu USD Bond 2 ($D^* = 8.0$ năm).
- Tính Modified Duration của danh mục?
- Nếu lãi suất tăng 50 bps, ước tính mức thay đổi bằng USD của toàn danh mục?

**Detailed Bilingual Solution & Explanation:**
1. **Portfolio Modified Duration ($D^*_P$)**:
   - Tổng giá trị thị trường: $V_P = 30 + 70 = 100 \text{ triệu USD}$.
   - Tỷ trọng: $w_1 = 30/100 = 0.30$, $w_2 = 70/100 = 0.70$.
   - Duration của danh mục là bình quân gia quyền theo giá trị thị trường:
     $$D^*_P = w_1 D^*_1 + w_2 D^*_2 = 0.30 \times 3.0 + 0.70 \times 8.0 = 0.90 + 5.60 = 6.50 \text{ năm}$$
2. **Dollar Change in Value (Thay đổi bằng tiền USD)**:
   - $\Delta y = +50 \text{ bps} = +0.0050$.
   - $\Delta V_P \approx -D^*_P \times V_P \times \Delta y = -6.50 \times 100,000,000 \times 0.0050 = -3,250,000 \text{ USD}$.
   - Danh mục giảm giá trị **3,250,000 USD** (tương đương giảm 3.25%).

---

### Question 3.6
**Original Question:**  
An insurance company must pay a guaranteed obligation of $10,000,000 in exactly 5 years. Market interest rate is 6% per annum.
- What is the present value and duration of this liability?
- How can the company immunize this obligation using a 3-year coupon bond ($D_1 = 2.7$ yrs) and an 8-year coupon bond ($D_2 = 6.2$ yrs)?

**Tóm tắt đề bài:**  
Công ty bảo hiểm có nghĩa vụ nợ 10 triệu USD trả sau đúng 5 năm. Lãi suất thị trường 6%/năm.
- Tính giá trị hiện tại (PV) và duration của khoản nợ?
- Làm thế nào để miễn nhiễm nghĩa vụ này bằng 2 trái phiếu: Trái phiếu 1 ($D_1 = 2.7$ năm) và Trái phiếu 2 ($D_2 = 6.2$ năm)?

**Detailed Bilingual Solution & Explanation:**
1. **Liability PV and Duration**:
   - Khoản nợ là một dòng tiền đơn phát sinh tại $t = 5$, do đó:
     $$V_L = \frac{10,000,000}{(1.06)^5} = \frac{10,000,000}{1.338226} \approx 7,472,582 \text{ USD}$$
     $$D_L = 5.0 \text{ năm}$$
2. **Immunization Portfolio Construction (Thiết lập Danh mục Miễn nhiễm)**:
   - Để miễn nhiễm hoàn toàn, danh mục tài sản $A$ cần thỏa mãn:
     1. Khớp giá trị hiện tại: $V_A = V_L = 7,472,582 \text{ USD}$.
     2. Khớp thời lượng: $D_A = D_L = 5.0 \text{ năm}$.
   - Đặt $w_1$ là tỷ trọng đầu tư vào Trái phiếu 1, $w_2 = 1 - w_1$ là tỷ trọng vào Trái phiếu 2:
     $$w_1 D_1 + (1 - w_1) D_2 = D_L$$
     $$w_1 (2.7) + (1 - w_1) (6.2) = 5.0$$
     $$2.7 w_1 + 6.2 - 6.2 w_1 = 5.0 \implies -3.5 w_1 = -1.2 \implies w_1 = \frac{1.2}{3.5} = \frac{12}{35} \approx 34.29\%$$
     $$w_2 = 1 - 0.3429 = 65.71\%$$
   - Số tiền đầu tư:
     - Vào Trái phiếu 1: $7,472,582 \times 34.29\% \approx 2,562,028 \text{ USD}$.
     - Vào Trái phiếu 2: $7,472,582 \times 65.71\% \approx 4,910,554 \text{ USD}$.

---

### Question 3.7
**Original Question:**  
Why does an immunized portfolio require ongoing rebalancing, and under what yield curve movements can an immunized position still fail?

**Tóm tắt đề bài:**  
Tại sao danh mục miễn nhiễm bắt buộc phải tái cân bằng liên tục, và dạng dịch chuyển nào của đường cong lợi suất vẫn có thể khiến chiến lược miễn nhiễm thất bại?

**Detailed Bilingual Solution & Explanation:**
- **Rebalancing Requirements (Tại sao phải tái cân bằng)**:
  1. *Sự trôi qua của thời gian (Aging effect)*: Khi thời gian trôi qua, Duration của tài sản (gồm các trái phiếu có dòng coupon) và Duration của nghĩa vụ nợ (khoản thanh toán đơn) suy giảm với tốc độ không đều nhau ($dD_A/dt \ne dD_L/dt$).
  2. *Biến động của lãi suất (Yield shock effect)*: Bản thân Duration phụ thuộc vào lãi suất $y$. Khi $y$ biến động, $D_A$ và $D_L$ lập tức bị lệch nhau.
- **Failures under Non-Parallel Shifts (Thất bại trước dịch chuyển không song song)**:
  - Lý thuyết miễn nhiễm cổ điển dựa trên giả định rằng **toàn bộ đường cong lợi suất dịch chuyển song song (parallel shift)** một lượng $\Delta y$ như nhau tại mọi kỳ hạn.
  - Trong thực tế, đường cong thường xuyên bị **xoắn (twists), đổi độ dốc (steepening / flattening), hoặc đổi độ cong (butterfly shifts)**.
  - Nếu lãi suất ngắn hạn tăng mạnh nhưng lãi suất dài hạn giảm (hoặc ngược lại), điều kiện khớp Duration bị phá vỡ hoàn toàn và danh mục miễn nhiễm có thể chịu thua lỗ nặng!

---

# LECTURE 04: Returns, Risk, and Portfolio Choice
*(Lợi suất, Rủi ro và Lựa chọn Danh mục Đầu tư)*

### Question 4.1 (L04 In-Class Q1)
**Original Question:**  
An investor buys a stock at $P_0 = 50$, receives a dividend of $D_1 = 2$ at year-end, and sells at $P_1 = 53$. Calculate the dividend yield, capital gain yield, and total holding period return (HPR).

**Tóm tắt đề bài:**  
Mua cổ phiếu giá $P_0 = 50$, nhận cổ tức $D_1 = 2$, bán giá $P_1 = 53$ sau 1 năm. Tính tỷ suất cổ tức, tỷ suất lãi vốn và tổng lợi suất kỳ nắm giữ HPR.

**Detailed Bilingual Solution & Explanation:**
- Tỷ suất cổ tức (Dividend Yield): $\frac{D_1}{P_0} = \frac{2}{50} = 4.00\%$.
- Tỷ suất lãi vốn (Capital Gain Yield): $\frac{P_1 - P_0}{P_0} = \frac{53 - 50}{50} = \frac{3}{50} = 6.00\%$.
- Tổng tỷ suất sinh lợi kỳ nắm giữ (Total HPR):
  $$HPR = \frac{P_1 - P_0 + D_1}{P_0} = 6.00\% + 4.00\% = 10.00\%$$

---

### Question 4.2 (L04 In-Class Q2)
**Original Question:**  
An investment experiences returns of $+40\%$ in year 1 and $-30\%$ in year 2.
- Calculate the arithmetic average return and the geometric average return.
- Which average correctly determines the ending wealth of an initial $100 investment?
- Explain the volatility drag formula $r_g \approx \bar{r} - \frac{1}{2}\sigma^2$.

**Tóm tắt đề bài:**  
Đầu tư năm 1 lãi $+40\%$, năm 2 lỗ $-30\%$.
- Tính bình quân số học và bình quân hình học?
- Thước đo nào xác định chính xác của cải cuối cùng từ 100 USD ban đầu?
- Giải thích hiện tượng kéo tụt biến động (volatility drag).

**Detailed Bilingual Solution & Explanation:**
1. **Averages**:
   - Arithmetic Mean (Bình quân số học):
     $$\bar{r} = \frac{+40\% + (-30\%)}{2} = \frac{+10\%}{2} = +5.00\%$$
   - Geometric Mean (Bình quân hình học / CAGR):
     $$r_g = \sqrt{(1 + 0.40)(1 - 0.30)} - 1 = \sqrt{1.40 \times 0.70} - 1 = \sqrt{0.98} - 1 \approx 0.989949 - 1 = -1.005\%$$
2. **Ending Wealth Comparison**:
   - Giá trị thực tế sau 2 năm:
     $$W_2 = 100 \times 1.40 \times 0.70 = 98 \text{ USD} \quad (\text{Lỗ 2 USD})$$
   - Dùng Geometric Mean: $100 \times (1 - 0.01005)^2 = 100 \times 0.98 = 98 \text{ USD}$ $\implies$ **Chính xác tuyệt đối**!
   - Nếu dùng Arithmetic Mean: $100 \times (1 + 0.05)^2 = 110.25 \text{ USD}$ $\implies$ **Sai lệch nghiêm trọng (ảo tưởng lãi 10.25 USD)**!
3. **Volatility Drag (Kéo tụt biến động)**:
   - Phương sai mẫu: độ biến động càng lớn (ở đây $\sigma$ rất lớn), khoảng cách $\frac{1}{2}\sigma^2$ càng kéo tụt tỷ suất sinh lợi thực tế xuống dưới trung bình số học. Muốn tăng trưởng của cải thực tế, phải kiểm soát phương sai!

---

### Question 4.3 (L04 In-Class Q3)
**Original Question:**  
Nominal interest rate is 7.1%, and inflation is 3.0%. Calculate the exact real interest rate and the approximation. Under what conditions is the approximation poor?

**Tóm tắt đề bài:**  
Lãi suất danh nghĩa 7.1%, lạm phát 3.0%. Tính lãi suất thực chính xác và gần đúng. Khi nào xấp xỉ bị sai lệch nhiều?

**Detailed Bilingual Solution & Explanation:**
- Exact Fisher Formula (Chính xác):
  $$1 + r_{\text{real}} = \frac{1 + R_{\text{nom}}}{1 + i} = \frac{1.071}{1.030} \approx 1.039806 \implies r_{\text{real}} = 3.98\%$$
- Approximation (Gần đúng):
  $$r_{\text{real}} \approx R_{\text{nom}} - i = 7.1\% - 3.0\% = 4.10\%$$
- Sai số là $4.10\% - 3.98\% = 0.12\%$.
- **Điều kiện xấp xỉ kém**: Khi lạm phát hoặc lãi suất danh nghĩa rất cao (kinh tế siêu lạm phát), số hạng tích chéo $r_{\text{real}} \times i$ trở nên rất lớn, công thức trừ đơn giản sẽ thổi phồng lãi suất thực một cách sai lệch nghiêm trọng.

---

### Question 4.4 (L04 In-Class Q4)
**Original Question:**  
An investor has utility function $U = E(r) - \frac{1}{2} A \sigma^2$ with $A = 4$.
Evaluate two investment portfolios:
- Portfolio 1: $E(r_1) = 11\%$, $\sigma_1 = 15\%$.
- Portfolio 2: $E(r_2) = 14\%$, $\sigma_2 = 22\%$.
Which portfolio will this investor prefer? What is the certainty equivalent rate of each?

**Tóm tắt đề bài:**  
Hàm thỏa dụng $U = E(r) - \frac{1}{2} A \sigma^2$ với $A = 4$.
So sánh Portfolio 1 ($E(r)=11\%, \sigma=15\%$) và Portfolio 2 ($E(r)=14\%, \sigma=22\%$). Nhà đầu tư chọn danh mục nào? Tính tỷ suất sinh lợi chắc chắn tương đương ($r_{ce}$)?

**Detailed Bilingual Solution & Explanation:**
- *Lưu ý sống còn về đơn vị*: Nhập số dạng thập phân ($11\% = 0.11$, $15\% = 0.15$).
- **Portfolio 1**:
  $$U_1 = 0.11 - \frac{1}{2} (4) (0.15)^2 = 0.11 - 2 \times 0.0225 = 0.11 - 0.045 = 0.065 \text{ (hay 6.50\%)}$$
  $$r_{ce, 1} = 6.50\%$$
- **Portfolio 2**:
  $$U_2 = 0.14 - \frac{1}{2} (4) (0.22)^2 = 0.14 - 2 \times 0.0484 = 0.14 - 0.0968 = 0.0432 \text{ (hay 4.32\%)}$$
  $$r_{ce, 2} = 4.32\%$$
- **Quyết định**: Do $U_1 (6.50\%) > U_2 (4.32\%)$, nhà đầu tư **chọn Portfolio 1**.
- **Ý nghĩa kinh tế**: Mặc dù Portfolio 2 có lợi suất cao hơn (+3%), nhưng rủi ro của nó tăng quá nhiều (+7%), với một người có độ ngại rủi ro cao ($A=4$), hình phạt rủi ro ($\frac{1}{2} A \sigma^2$) đã triệt tiêu toàn bộ phần bù lợi nhuận!

---

### Question 4.5 (L04 In-Class Q5)
**Original Question:**  
A risky portfolio $P$ has expected return $E(r_P) = 13\%$ and $\sigma_P = 20\%$. Risk-free rate is $r_f = 5\%$.
- Write the equation of the Capital Allocation Line (CAL) and find its Sharpe ratio.
- If an investor has risk aversion $A = 3$, find the optimal weight $y^*$ in portfolio $P$ and describe their complete portfolio.

**Tóm tắt đề bài:**  
Danh mục rủi ro $P$ có $E(r_P) = 13\%$, $\sigma_P = 20\%$. Lãi suất phi rủi ro $r_f = 5\%$.
- Viết phương trình đường CAL và tính Sharpe ratio?
- Nếu nhà đầu tư có $A = 3$, tính tỷ trọng tối ưu $y^*$ vào $P$ và mô tả danh mục hoàn chỉnh?

**Detailed Bilingual Solution & Explanation:**
1. **CAL and Sharpe Ratio**:
   - Sharpe Ratio của $P$:
     $$SR_P = \frac{E(r_P) - r_f}{\sigma_P} = \frac{0.13 - 0.05}{0.20} = \frac{0.08}{0.20} = 0.40$$
   - Phương trình đường CAL:
     $$E(r_C) = r_f + SR_P \times \sigma_C = 0.05 + 0.40 \times \sigma_C$$
2. **Optimal Allocation ($y^*$)**:
   $$y^* = \frac{E(r_P) - r_f}{A \sigma_P^2} = \frac{0.13 - 0.05}{3 \times (0.20)^2} = \frac{0.08}{3 \times 0.04} = \frac{0.08}{0.12} = \frac{2}{3} \approx 66.67\%$$
   - **Mô tả danh mục hoàn chỉnh**:
     - Đầu tư $66.67\%$ tổng tài sản vào danh mục rủi ro $P$.
     - Cho vay $1 - y^* = 33.33\%$ tài sản ở lãi suất phi rủi ro $r_f = 5\%$.
     - Lợi suất kỳ vọng của danh mục hoàn chỉnh: $E(r_C) = 5\% + 0.6667 \times (13\% - 5\%) = 10.33\%$.
     - Độ lệch chuẩn: $\sigma_C = 0.6667 \times 20\% = 13.33\%$.

---

# LECTURE 05: Portfolio Selection and Capital Allocation
*(Lựa chọn Danh mục Đầu tư và Phân bổ Vốn)*

### Question 5.1 (L05 In-Class Q1)
**Original Question:**  
Stocks A and B have expected returns of 10% and 16%, and standard deviations of 15% and 25%, respectively.
Calculate the portfolio expected return and variance for equal weights ($w_A = 0.5, w_B = 0.5$) under three correlation scenarios: $\rho = +1.0$, $\rho = 0.0$, and $\rho = -1.0$.

**Tóm tắt đề bài:**  
Cổ phiếu A ($E(r)=10\%, \sigma=15\%$), B ($E(r)=16\%, \sigma=25\%$). Đầu tư tỷ trọng 50-50 ($w_A=0.5, w_B=0.5$).
Tính $E(r_P)$ và $\sigma_P$ trong 3 kịch bản tương quan: $\rho = +1.0, 0.0, -1.0$.

**Detailed Bilingual Solution & Explanation:**
- Lợi suất kỳ vọng của danh mục trong mọi kịch bản:
  $$E(r_P) = 0.5 (10\%) + 0.5 (16\%) = 13.00\%$$
- Công thức phương sai danh mục:
  $$\sigma_P^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho \sigma_A \sigma_B$$
  $$= (0.5)^2 (0.15)^2 + (0.5)^2 (0.25)^2 + 2 (0.5)(0.5) \rho (0.15)(0.25)$$
  $$= 0.25 (0.0225) + 0.25 (0.0625) + 0.50 \rho (0.0375) = 0.005625 + 0.015625 + 0.01875 \rho = 0.02125 + 0.01875 \rho$$
1. **Scenario 1: $\rho = +1.0$**:
   $$\sigma_P = \sqrt{0.02125 + 0.01875} = \sqrt{0.0400} = 0.20 = 20.00\%$$
   *(Đúng bằng bình quân tuyến tính $0.5 \times 15\% + 0.5 \times 25\% = 20\%$, không có lợi ích đa dạng hóa).*
2. **Scenario 2: $\rho = 0.0$**:
   $$\sigma_P = \sqrt{0.02125} \approx 0.14577 = 14.58\%$$
   *(Độ lệch chuẩn giảm từ 20% xuống 14.58%, thấp hơn cả cổ phiếu ít rủi ro nhất A!).*
3. **Scenario 3: $\rho = -1.0$**:
   $$\sigma_P = \sqrt{0.02125 - 0.01875} = \sqrt{0.0025} = 0.05 = 5.00\%$$
   *(Rủi ro triệt tiêu mạnh mẽ xuống chỉ còn 5%).*

---

### Question 5.2 (L05 In-Class Q2)
**Original Question:**  
Using the data from Question 5.1, find the weights of the Minimum Variance Portfolio (MVP) when $\rho = 0.2$.

**Tóm tắt đề bài:**  
Với dữ liệu câu 5.1 và $\rho = 0.2$, tìm tỷ trọng của Danh mục Phương sai Tối thiểu (MVP).

**Detailed Bilingual Solution & Explanation:**
- $\sigma_A = 0.15 \implies \sigma_A^2 = 0.0225$.
- $\sigma_B = 0.25 \implies \sigma_B^2 = 0.0625$.
- $\text{Cov}(A, B) = \rho \sigma_A \sigma_B = 0.2 \times 0.15 \times 0.25 = 0.0075$.
- Công thức trọng số MVP cho tài sản A:
  $$w_A^{\text{MVP}} = \frac{\sigma_B^2 - \text{Cov}(A, B)}{\sigma_A^2 + \sigma_B^2 - 2\text{Cov}(A, B)} = \frac{0.0625 - 0.0075}{0.0225 + 0.0625 - 2(0.0075)} = \frac{0.0550}{0.0850 - 0.0150} = \frac{0.0550}{0.0700} = \frac{11}{14} \approx 78.57\%$$
  $$w_B^{\text{MVP}} = 1 - 0.7857 = 21.43\%$$
- Do cổ phiếu A có biến động thấp hơn nhiều (15% vs 25%), danh mục phương sai thấp nhất sẽ dồn phần lớn vốn (78.57%) vào cổ phiếu A.

---

### Question 5.3 (L05 In-Class Q3)
**Original Question:**  
Explain the economic meaning of the Markowitz Efficient Frontier. Why does no rational investor hold a portfolio that lies on the bottom half of the minimum-variance frontier?

**Tóm tắt đề bài:**  
Giải thích ý nghĩa kinh tế của Đường biên Hiệu quả Markowitz. Tại sao không nhà đầu tư duy lý nào lại nắm giữ danh mục nằm ở nửa dưới của đường biên phương sai tối thiểu?

**Detailed Bilingual Solution & Explanation:**
- **Đường biên Hiệu quả (Efficient Frontier)**: Là tập hợp các danh mục tài sản rủi ro cung cấp **lợi suất kỳ vọng cao nhất cho mỗi mức độ rủi ro $\sigma$**, hoặc tương đương, **rủi ro thấp nhất cho mỗi mức lợi suất kỳ vọng mục tiêu**.
- **Tại sao loại bỏ nửa dưới (Inefficient / Dominated Part)**:
  - Với bất kỳ danh mục $X$ nào nằm ở nửa dưới của đường biên (phía dưới điểm MVP), luôn luôn tồn tại một danh mục $Y$ nằm ở nửa trên có **cùng mức rủi ro $\sigma_Y = \sigma_X$ nhưng lại có lợi suất kỳ vọng cao hơn vượt trội ($E(r_Y) > E(r_X)$)**.
  - Do nhà đầu tư có tính chất ngại rủi ro và thích lợi nhuận cao hơn (Risk aversion & Greed / Non-satiation), danh mục $Y$ áp đảo hoàn toàn danh mục $X$ (Strictly dominates). Do đó, nửa dưới bị loại bỏ vì không hiệu quả!

---

### Question 5.4 (L05 In-Class Q4)
**Original Question:**  
Define the Tangency Portfolio. Why is the tangency portfolio identical for all mean-variance investors regardless of their personal risk aversion $A$?

**Tóm tắt đề bài:**  
Định nghĩa Danh mục Tiếp điểm (Tangency Portfolio). Tại sao danh mục tiếp điểm lại giống hệt nhau đối với mọi nhà đầu tư dù họ có mức ngại rủi ro $A$ khác nhau?

**Detailed Bilingual Solution & Explanation:**
- **Định nghĩa**: Danh mục Tiếp điểm ($P^*$) là danh mục tài sản rủi ro nằm tại điểm tiếp xúc giữa đường thẳng xuất phát từ lãi suất phi rủi ro $r_f$ (đường CAL) với Đường biên Hiệu quả Markowitz. Đây là danh mục **tối đa hóa tỷ số Sharpe (độ dốc của CAL)**:
  $$\max_{w} SR_P = \frac{E(r_P) - r_f}{\sigma_P}$$
- **Tính khách quan (Independence from $A$)**:
  - Bài toán tối đa hóa Sharpe ratio $\frac{E(r_P) - r_f}{\sigma_P}$ là một bài toán thuần túy hình học và toán học, chỉ phụ thuộc vào các thông số thị trường: $r_f$, vector lợi suất kỳ vọng $E(r)$, và ma trận hiệp phương sai $\Sigma$.
  - Tham số ngại rủi ro cá nhân $A$ **hoàn toàn không xuất hiện** trong phương trình xác định trọng số $w^*$ của danh mục tiếp điểm!
  - Do đó, mọi nhà đầu tư đều xác định được cùng 1 danh mục rủi ro tiếp điểm tối ưu $P^*$ (Nguyên lý phân tách 2 quỹ).

---

### Question 5.5 (L05 In-Class Q5)
**Original Question:**  
State the Two-Fund Separation Theorem and explain the difference between the Capital Allocation Line (CAL) and the Capital Market Line (CML).

**Tóm tắt đề bài:**  
Phát biểu Định lý Phân tách Hai quỹ của Tobin và phân biệt giữa đường CAL và đường CML.

**Detailed Bilingual Solution & Explanation:**
- **Two-Fund Separation Theorem (Định lý Phân tách Hai Quỹ)**:
  Quy trình ra quyết định đầu tư được phân tách độc lập thành 2 bước:
  1. *Bước 1 (Xác định danh mục rủi ro tối ưu - Khách quan)*: Tìm danh mục tiếp điểm $P$ tối đa hóa Sharpe ratio. Danh mục này giống nhau cho tất cả mọi người.
  2. *Bước 2 (Phân bổ vốn giữa tài sản rủi ro và phi rủi ro - Chủ quan)*: Mỗi cá nhân chọn tỷ lệ $y^*$ rót vào $P$ và $(1-y^*)$ vào $r_f$ dựa trên độ ngại rủi ro riêng $A$.
- **So sánh CAL vs. CML**:
  - *CAL (Capital Allocation Line)*: Là đường phân bổ vốn nối $r_f$ với **bất kỳ** một danh mục rủi ro $P$ cụ thể nào. Mỗi danh mục rủi ro khác nhau sẽ có 1 đường CAL riêng với độ dốc bằng Sharpe ratio của danh mục đó.
  - *CML (Capital Market Line)*: Là trường hợp đặc biệt và tối ưu nhất của CAL trong trạng thái cân bằng thị trường, khi danh mục tiếp điểm $P$ chính là **Danh mục Thị trường gộp ($M$)**. Độ dốc của CML là Sharpe ratio cao nhất có thể đạt được trong toàn nền kinh tế. CML chỉ dùng cho các danh mục hoàn toàn hiệu quả.

---

# LECTURE 06: Single-Index Model and CAPM
*(Mô hình Chỉ số Đơn và Mô hình Định giá Tài sản Vốn)*

### Question 6.1 (L06 In-Class Q1)
**Original Question:**  
Stock Omega has a covariance with the market portfolio of 0.036. Market portfolio variance is 0.0225 ($\sigma_M = 15\%$). Risk-free rate is 4%, and expected market return is 12%.
- Calculate Omega's Beta ($eta_\Omega$).
- What is Omega's expected return required by CAPM?

**Tóm tắt đề bài:**  
Cổ phiếu Omega có hiệp phương sai với thị trường là 0.036. Phương sai thị trường là 0.0225 ($\sigma_M = 15\%$). $r_f = 4\%$, $E(r_M) = 12\%$.
- Tính Beta của Omega?
- Lợi suất kỳ vọng của Omega theo yêu cầu của CAPM là bao nhiêu?

**Detailed Bilingual Solution & Explanation:**
1. **Beta Calculation**:
   $$eta_\Omega = rac{	ext{Cov}(r_\Omega, r_M)}{	ext{Var}(r_M)} = rac{0.036}{0.0225} = 1.60$$
   *(Omega có rủi ro hệ thống cao hơn thị trường 60%).*
2. **CAPM Required Return**:
   $$E(r_\Omega) = r_f + eta_\Omega [E(r_M) - r_f] = 4\% + 1.60 	imes (12\% - 4\%) = 4\% + 1.60 	imes 8\% = 4\% + 12.8\% = 16.80\%$$

---

### Question 6.2 (L06 In-Class Q2)
**Original Question:**  
Stock Lambda has Beta $eta = 1.2$, total standard deviation $\sigma_\Lambda = 25\%$, and market standard deviation is $\sigma_M = 15\%$.
- Decompose Lambda's total variance into systematic variance and firm-specific variance.
- Calculate the $R^2$ of the regression of Lambda on the market index.

**Tóm tắt đề bài:**  
Cổ phiếu Lambda có $eta = 1.2$, $\sigma_\Lambda = 25\%$, $\sigma_M = 15\%$.
- Phân rã tổng phương sai của Lambda thành phương sai hệ thống và phương sai đặc thù?
- Tính hệ số xác định $R^2$ của hồi quy Lambda theo thị trường?

**Detailed Bilingual Solution & Explanation:**
1. **Variance Decomposition**:
   - Tổng phương sai (Total Variance):
     $$\sigma_\Lambda^2 = (0.25)^2 = 0.0625$$
   - Phương sai hệ thống (Systematic Variance):
     $$eta^2 \sigma_M^2 = (1.2)^2 	imes (0.15)^2 = 1.44 	imes 0.0225 = 0.0324$$
   - Phương sai đặc thù / phi hệ thống (Firm-specific Residual Variance):
     $$\sigma^2(e_\Lambda) = \sigma_\Lambda^2 - eta^2 \sigma_M^2 = 0.0625 - 0.0324 = 0.0301$$
2. **Coefficient of Determination ($R^2$)**:
   $$R^2 = rac{	ext{Systematic Variance}}{	ext{Total Variance}} = rac{0.0324}{0.0625} = 0.5184 \quad (51.84\%)$$
   - **Ý nghĩa kinh tế**: $51.84\%$ sự biến động của cổ phiếu Lambda bắt nguồn từ các cú sốc vĩ mô toàn thị trường; $48.16\%$ còn lại là rủi ro đặc thù nội tại của doanh nghiệp có thể đa dạng hóa được.

---

### Question 6.3 (L06 In-Class Q3)
**Original Question:**  
An analyst forecasts that Stock Psi will return 14% over the next year. Psi has a beta of 0.8. The risk-free rate is 5% and the market risk premium is 8%.
- Calculate the CAPM required return for Psi.
- What is Psi's Jensen's Alpha? Is Psi underpriced, overpriced, or fairly priced? What is the investment recommendation?

**Tóm tắt đề bài:**  
Chuyên viên dự báo Psi sẽ đạt lợi suất 14%. Psi có $eta = 0.8$. $r_f = 5\%$, phần bù rủi ro thị trường $E(r_M)-r_f = 8\%$.
- Tính lợi suất yêu cầu theo CAPM?
- Tính Alpha của Jensen? Cổ phiếu bị định giá cao, thấp hay công bằng? Khuyến nghị đầu tư là gì?

**Detailed Bilingual Solution & Explanation:**
1. **CAPM Required Return**:
   $$E(r_{	ext{CAPM}}) = r_f + eta [E(r_M) - r_f] = 5\% + 0.8 	imes 8\% = 5\% + 6.4\% = 11.40\%$$
2. **Jensen's Alpha & Valuation**:
   $$lpha = E(r_{	ext{forecast}}) - E(r_{	ext{CAPM}}) = 14.00\% - 11.40\% = +2.60\%$$
   - **Đánh giá & Khuyến nghị**:
     - Do $lpha = +2.60\% > 0$, cổ phiếu mang lại lợi nhuận kỳ vọng cao hơn mức bù rủi ro cần thiết.
     - Cổ phiếu **bị định giá thấp (Undervalued)** trên thị trường $\implies$ Nằm **phía trên đường SML**.
     - Khuyến nghị: **MUA (BUY)**. Khi thị trường nhận ra và mua vào, giá sẽ tăng lên làm lợi suất tương lai hạ về mức cân bằng 11.40%.

---

### Question 6.4 (L06 In-Class Q4)
**Original Question:**  
Explain why two stocks can have the exact same Beta ($eta = 1.0$) but completely different total standard deviations. How does CAPM view the difference in their total risk?

**Tóm tắt đề bài:**  
Tại sao 2 cổ phiếu có thể có cùng Beta $eta = 1.0$ nhưng độ lệch chuẩn tổng thể $\sigma$ lại hoàn toàn khác nhau? CAPM nhìn nhận sự khác biệt này như thế nào?

**Detailed Bilingual Solution & Explanation:**
- **Giải thích qua công thức SIM**:
  $$\sigma_i^2 = eta_i^2 \sigma_M^2 + \sigma^2(e_i)$$
  - Nếu cả hai cổ phiếu đều có $eta = 1.0$, phần rủi ro hệ thống của chúng là giống hệt nhau: $eta^2 \sigma_M^2 = 1.0 	imes \sigma_M^2$.
  - Tuy nhiên, tổng phương sai $\sigma_i^2$ còn phụ thuộc vào **rủi ro đặc thù $\sigma^2(e_i)$**. Cổ phiếu thuộc ngành công nghệ cao, dược phẩm sinh học có thể có $\sigma^2(e)$ cực lớn (thử nghiệm thuốc thành công/thất bại), trong khi cổ phiếu tiêu dùng thiết yếu có $\sigma^2(e)$ rất nhỏ.
- **Quan điểm của CAPM**:
  - CAPM giả định nhà đầu tư duy lý luôn nắm giữ danh mục thị trường đa dạng hóa tối ưu.
  - Trong một danh mục lớn, toàn bộ rủi ro đặc thù $\sigma^2(e_i)$ sẽ triệt tiêu về 0 nhờ Luật số lớn.
  - Do đó, thị trường **hoàn toàn không trả bất kỳ một đồng phần bù rủi ro nào cho rủi ro đặc thù**.
  - Hai cổ phiếu có cùng $eta = 1.0$ sẽ có **lợi suất kỳ vọng theo CAPM giống hệt nhau**, bất kể cổ phiếu nào có tổng độ lệch chuẩn $\sigma$ lớn hơn!

---

### Question 6.5 (L06 In-Class Q5)
**Original Question:**  
Distinguish between the Sharpe ratio, Treynor ratio, and Information ratio. Which metric is most appropriate for evaluating:
a. An investor's entire wealth portfolio?
b. A mutual fund to be added to an already well-diversified portfolio?
c. An active fund manager seeking to generate alpha against a benchmark?

**Tóm tắt đề bài:**  
Phân biệt Sharpe ratio, Treynor ratio và Information ratio. Chỉ số nào thích hợp nhất để đánh giá:
a. Toàn bộ danh mục tài sản của một cá nhân?
b. Một quỹ đầu tư dự kiến bổ sung vào một danh mục đã đa dạng hóa tốt?
c. Một nhà quản lý quỹ chủ động nhằm tạo alpha so với chỉ số tham chiếu?

**Detailed Bilingual Solution & Explanation:**
- **Formulas & Definitions**:
  1. *Sharpe Ratio*: $SR = rac{E(r_P) - r_f}{\sigma_P}$ (Thưởng trên mỗi đơn vị tổng rủi ro $\sigma$).
  2. *Treynor Ratio*: $TR = rac{E(r_P) - r_f}{eta_P}$ (Thưởng trên mỗi đơn vị rủi ro hệ thống $eta$).
  3. *Information Ratio*: $IR = rac{lpha_P}{\sigma(e_P)}$ (Alpha tạo ra trên mỗi đơn vị rủi ro đặc thù chủ động).
- **Matching (Ứng dụng chuẩn)**:
  - **(a) Toàn bộ tài sản**: Dùng **Sharpe Ratio**. Vì nhà đầu tư gánh toàn bộ rủi ro (cả rủi ro phi hệ thống), tổng độ lệch chuẩn $\sigma$ là thước đo rủi ro duy nhất phù hợp.
  - **(b) Bổ sung vào danh mục đã đa dạng hóa**: Dùng **Treynor Ratio**. Vì danh mục hiện tại đã loại bỏ rủi ro đặc thù, tài sản mới chỉ đóng góp thêm rủi ro hệ thống Beta.
  - **(c) Đánh giá nhà quản lý quỹ chủ động**: Dùng **Information Ratio**. Đo lường khả năng tạo ra tỷ suất sinh lợi vượt trội (alpha) một cách bền vững trên mỗi đơn vị rủi ro chủ động mà họ chấp nhận gánh chịu.

---

# LECTURE 07: Multifactor Models and APT
*(Mô hình Đa nhân tố và Lý thuyết Định giá Chênh lệch giá)*

### Question 7.1 (L07 In-Class Q1)
**Original Question:**  
Define pure arbitrage in Arbitrage Pricing Theory (APT). State the four conditions required for an arbitrage opportunity to exist.

**Tóm tắt đề bài:**  
Định nghĩa kinh doanh chênh lệch giá thuần túy trong APT. Nêu 4 điều kiện bắt buộc để một cơ hội arbitrage tồn tại.

**Detailed Bilingual Solution & Explanation:**
- **Định nghĩa**: Pure Arbitrage là việc thu được một khoản lợi nhuận dương chắc chắn mà không phải bỏ ra bất kỳ đồng vốn tự có nào và không phải chịu bất kỳ một loại rủi ro nào.
- **4 Điều kiện Nghiêm ngặt**:
  1. $\sum_{i} w_i = 0$: Không dùng vốn tự có ròng (Zero Net Investment - bán khống tài sản này để tài trợ mua tài sản kia).
  2. $\sum_{i} w_i eta_{i,k} = 0$: Triệt tiêu 100% rủi ro hệ thống đối với mọi nhân tố $k$ (Zero Factor Beta Risk).
  3. $\sigma^2(e_P) = \sum w_i^2 \sigma^2(e_i) pprox 0$: Triệt tiêu rủi ro phi hệ thống (bằng cách đa dạng hóa trên số lượng rất lớn tài sản theo Luật số lớn).
  4. $\sum_{i} w_i E(R_i) > 0$: Lợi nhuận kỳ vọng chắc chắn dương (Guaranteed Positive Profit).

---

### Question 7.2 (L07 In-Class Q2)
**Original Question:**  
Portfolios Alpha and Beta are well-diversified. Both have a single-factor beta $eta = 1.2$. Portfolio Alpha has an expected return of 14%, while Portfolio Beta has an expected return of 11%. Risk-free rate is 4%.
- Does an arbitrage opportunity exist?
- Construct the specific arbitrage portfolio demonstrating zero net investment, zero factor risk, and positive guaranteed profit.

**Tóm tắt đề bài:**  
Hai danh mục đa dạng hóa Alpha và Beta cùng có $eta = 1.2$. $E(r_lpha) = 14\%$, $E(r_eta) = 11\%$, $r_f = 4\%$.
- Có cơ hội arbitrage không?
- Xây dựng danh mục arbitrage cụ thể (chứng minh vốn bằng 0, rủi ro bằng 0, lãi dương chắc chắn)?

**Detailed Bilingual Solution & Explanation:**
1. **Arbitrage Existence**:
   - Hai danh mục đa dạng hóa hoàn hảo (không có rủi ro đặc thù) có cùng mức rủi ro hệ thống $eta = 1.2$ nhưng lại mang lại mức lợi suất kỳ vọng khác nhau ($14\% 
e 11\%$).
   - Điều này vi phạm Quy luật Một giá (Law of One Price) $\implies$ **Tồn tại cơ hội kinh doanh chênh lệch giá thuần túy**!
2. **Arbitrage Strategy Construction**:
   - Mua (Long) 100 USD danh mục Alpha (định giá rẻ, sinh lời cao 14%).
   - Bán khống (Short) 100 USD danh mục Beta (định giá đắt, sinh lời thấp 11%).
   - **Kiểm tra 3 điều kiện**:
     1. Vốn đầu tư ban đầu: $+100 - 100 = 0 	ext{ USD}$ (Zero Investment).
     2. Rủi ro Beta: $w_lpha eta_lpha + w_eta eta_eta = (+1)(1.2) + (-1)(1.2) = 0$ (Zero Systematic Risk).
     3. Rủi ro phi hệ thống: Cả 2 đều là danh mục đa dạng hóa tốt nên $\sigma^2(e_P) pprox 0$ (Zero Residual Risk).
     4. Lợi nhuận chắc chắn:
        $$\Pi = (+1)(14\%) + (-1)(11\%) = +3.00\% = +3.00 	ext{ USD}$$
   - Nhà đầu tư bỏ túi ngay **+3 USD lợi nhuận không rủi ro** mà không cần bỏ ra một đồng vốn nào!

---

### Question 7.3 (L07 In-Class Q3)
**Original Question:**  
Compare CAPM and APT along the following dimensions:
- Role of the market portfolio.
- Applicability to individual stocks versus well-diversified portfolios.
- Vulnerability to Roll's Critique.

**Tóm tắt đề bài:**  
So sánh CAPM và APT theo 3 tiêu chí: Vai trò của danh mục thị trường; Phạm vi áp dụng cho cổ phiếu lẻ vs danh mục đa dạng hóa; Mức độ ảnh hưởng bởi Phê phán của Roll.

**Detailed Bilingual Solution & Explanation:**
| Tiêu chí | CAPM | APT |
|---|---|---|
| **Vai trò của Danh mục Thị trường ($M$)** | Là nhân tố trung tâm bắt buộc; mọi rủi ro đều đo lường qua hiệp phương sai với $M$. | Không đòi hỏi danh mục thị trường $M$; có thể dùng bất kỳ tập hợp nhân tố vĩ mô hoặc nhân tố danh mục nào giải thích được biến động chung. |
| **Phạm vi áp dụng** | Áp dụng trên lý thuyết cho **từng cổ phiếu riêng lẻ** (mọi cổ phiếu đều nằm trên SML). | Chỉ áp dụng hoàn hảo cho các **danh mục đa dạng hóa lớn**; cổ phiếu đơn lẻ vẫn có thể có alpha khác 0 do rủi ro đặc thù chưa triệt tiêu. |
| **Phê phán của Roll (Roll's Critique)** | **Bị ảnh hưởng chí mạng**. Roll chỉ ra rằng danh mục thị trường thực tế bao gồm toàn bộ của cải (cả tài sản phi tài chính, vốn con người) nên không thể quan sát được; việc kiểm định CAPM thực chất chỉ là kiểm định xem chỉ số đại diện (như S&P 500) có hiệu quả hay không. | **Không bị ảnh hưởng**. Không cần giả định hay quan sát danh mục thị trường gộp. |

---

### Question 7.4 (L07 In-Class Q4)
**Original Question:**  
Write the equation of the Fama-French 3-Factor Model. Define the SMB and HML factors and explain how they are constructed.

**Tóm tắt đề bài:**  
Viết phương trình mô hình Fama-French 3 nhân tố. Định nghĩa và giải thích cách xây dựng nhân tố SMB và HML.

**Detailed Bilingual Solution & Explanation:**
- **Regression Equation (Dạng lợi suất vượt trội)**:
  $$R_{i,t} = lpha_i + eta_{i,MKT} R_{MKT,t} + eta_{i,SMB} SMB_t + eta_{i,HML} HML_t + e_{i,t}$$
  với $R_{i,t} = r_{i,t} - r_{f,t}$, $R_{MKT,t} = r_{M,t} - r_{f,t}$.
- **SMB (Small Minus Big - Nhân tố Quy mô)**:
  - Mua (Long) danh mục các cổ phiếu có giá trị vốn hóa thị trường nhỏ; Bán khống (Short) danh mục các cổ phiếu vốn hóa lớn.
  - Phản ánh phần bù rủi ro quy mô: công ty nhỏ đối mặt với rủi ro thanh khoản và rủi ro tài trợ vốn cao hơn trong chu kỳ suy thoái.
- **HML (High Minus Low - Nhân tố Giá trị)**:
  - Mua (Long) danh mục các công ty có tỷ số Book-to-Market cao (Value stocks); Bán khống (Short) danh mục các công ty có Book-to-Market thấp (Growth stocks).
  - Phản ánh phần bù rủi ro giá trị: các công ty có B/M cao thường là doanh nghiệp lâu năm có nguy cơ kiệt quệ tài chính hoặc tài sản hữu hình dễ bị tổn thương khi nền kinh tế suy thoái.

---

### Question 7.5 (L07 In-Class Q5)
**Original Question:**  
Stock Theta has estimated factor loadings: $eta_{MKT} = 1.1$, $eta_{SMB} = -0.5$, $eta_{HML} = +0.4$.
- What do the signs and magnitudes of $eta_{SMB}$ and $eta_{HML}$ reveal about Theta's investment style and firm characteristics?
- If factor risk premiums are $\lambda_{MKT} = 6.0\%$, $\lambda_{SMB} = 2.0\%$, $\lambda_{HML} = 3.5\%$, and $r_f = 4.0\%$, calculate Theta's expected return under the FF3 model.

**Tóm tắt đề bài:**  
Theta có $eta_{MKT} = 1.1$, $eta_{SMB} = -0.5$, $eta_{HML} = +0.4$.
- Dấu và độ lớn của $eta_{SMB}$ và $eta_{HML}$ phản ánh phong cách đầu tư gì của Theta?
- Nếu $\lambda_{MKT} = 6.0\%$, $\lambda_{SMB} = 2.0\%$, $\lambda_{HML} = 3.5\%$, $r_f = 4.0\%$, tính lợi suất kỳ vọng của Theta theo FF3?

**Detailed Bilingual Solution & Explanation:**
1. **Interpretation of Factor Loadings (Diễn giải Phong cách Đầu tư)**:
   - $eta_{SMB} = -0.5 < 0$: Hệ số âm phản ánh rằng Theta mang thiên hướng **cổ phiếu vốn hóa lớn (Large-Cap Tilt)**. Biến động của nó dịch chuyển cùng chiều với nhóm công ty lớn và ngược chiều với nhóm công ty nhỏ.
   - $eta_{HML} = +0.4 > 0$: Hệ số dương phản ánh rằng Theta mang phong cách **cổ phiếu giá trị (Value Tilt)** (tỷ số Book-to-Market cao).
   - **Tổng kết phong cách**: Theta là một **Cổ phiếu Giá trị Vốn hóa Lớn (Large-Cap Value Stock)** (ví dụ điển hình như các ngân hàng lớn hoặc tập đoàn dầu khí lâu đời).
2. **Expected Return Calculation (Tính Lợi suất Kỳ vọng)**:
   - Lợi suất vượt trội kỳ vọng:
     $$E(R_\Theta) = eta_{MKT} \lambda_{MKT} + eta_{SMB} \lambda_{SMB} + eta_{HML} \lambda_{HML}$$
     $$E(R_\Theta) = 1.1 	imes 6.0\% + (-0.5) 	imes 2.0\% + 0.4 	imes 3.5\%$$
     $$= 6.6\% - 1.0\% + 1.4\% = 7.00\%$$
   - Tổng lợi suất kỳ vọng danh nghĩa:
     $$E(r_\Theta) = r_f + E(R_\Theta) = 4.0\% + 7.0\% = 11.00\%$$

---

### Question 7.6 (L07 In-Class Q6)
**Original Question:**  
A hedge fund reports an annualized CAPM alpha of $+3.6\%$ ($p < 0.01$). However, when regressed against the Fama-French 3 factors, the estimated monthly equation is:
$$R_{t} = 0.03\% + 1.05 R_{MKT,t} + 0.72 SMB_t + 0.65 HML_t + e_t$$
with $t(lpha) = 0.28$ ($p = 0.78$).
- Interpret these regression results.
- Does the manager possess genuine stock-picking skill? Explain.

**Tóm tắt đề bài:**  
Một quỹ đầu cơ báo cáo CAPM Alpha năm là $+3.6\%$ ($p < 0.01$). Tuy nhiên, khi chạy hồi quy FF3, kết quả là $lpha = 0.03\%$/tháng với $t = 0.28$ ($p = 0.78$), $eta_{SMB} = 0.72$, $eta_{HML} = 0.65$.
- Diễn giải kết quả hồi quy?
- Người quản lý quỹ có tài năng chọn cổ phiếu thực sự không? Giải thích.

**Detailed Bilingual Solution & Explanation:**
1. **Interpretation of Regression Results (Diễn giải Kết quả Hồi quy)**:
   - Quỹ có hệ số tiếp xúc nhân tố rất cao và dương: $eta_{SMB} = 0.72 > 0$ và $eta_{HML} = 0.65 > 0$. Điều này chứng minh danh mục của quỹ tập trung dày đặc vào các **cổ phiếu vốn hóa nhỏ (Small-cap)** và **cổ phiếu giá trị (Value stocks)**.
   - Sau khi kiểm soát 2 nguồn rủi ro này, Alpha của quỹ sụt giảm từ mức rất cao xuống chỉ còn $0.03\%$/tháng ($0.36\%$/năm).
   - Thống kê $t$ của Alpha là $0.28$ và $p$-value $= 0.78 \gg 0.05$, nghĩa là Alpha này **hoàn toàn không có ý nghĩa thống kê** (không thể bác bỏ giả thuyết $H_0: lpha = 0$).
2. **Manager Skill Assessment (Đánh giá Năng lực Quản lý Quỹ)**:
   - **Kết luận**: Người quản lý quỹ **HOÀN TOÀN KHÔNG CÓ TÀI NĂNG CHỌN CỔ PHIẾU (No True Stock-Picking Skill)**!
   - Khoản "lợi nhuận vượt trội" ban đầu theo CAPM chỉ là một sự ngụy tạo do mô hình CAPM bị thiếu biến (Omitted Variable Bias). Quỹ đơn thuần chỉ đang mua các nhóm tài sản có rủi ro cao (cổ phiếu nhỏ và cổ phiếu giá trị) và thu về phần bù rủi ro thụ động của thị trường.
   - Nhà đầu tư không nên trả mức phí quản lý chủ động đắt đỏ (2% phí quản lý và 20% phí hiệu quả) cho quỹ này, vì họ hoàn toàn có thể tự sao chép tỷ suất sinh lợi này bằng cách mua các chứng chỉ quỹ ETF Small-Cap Value với mức phí cực rẻ (chưa tới 0.1%/năm)!
