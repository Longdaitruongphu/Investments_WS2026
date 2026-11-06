# 📘 BFIN INVESTMENTS (WS2026) — FINAL EXAM STUDY BIBLE
## VOLUME 04: BỘ LỜI GIẢI CHI TIẾT 40 CÂU HỎI ÔN TẬP LECTURES 08–11 (Q01 – Q40)

> [!IMPORTANT]
> **CHỈ DẪN CHIẾN LƯỢC PHÒNG THI (EXAM-WEIGHTED NAVIGATION):**
> - Tài liệu này giải chi tiết **100% trọn vẹn 40/40 câu hỏi gốc** từ `BFIN-WS2026-Practice_L08-L11_questions.ipynb` của GS. Bora Cayirli, giữ nguyên số liệu không làm tròn ở bước trung gian (*unrounded intermediate values*) và làm tròn 2 chữ số thập phân ở kết quả cuối cùng theo đúng quy chuẩn chấm thi.
> - **Phân loại trọng tâm sát cấu trúc đề thi Final Exam:**
>   1. 🎯 **Q01 – Q05 (Lecture 08)**: *Market Efficiency, Fama-French 3-Factor Alpha, Behavioural Biases & Limits to Arbitrage* — Xuất hiện cả trong **MCQ** và câu hỏi phân tích **Tự luận**.
>   2. 🔥 **26 Câu Cốt Tử Tự Luận Tính Toán Derivatives (40% Điểm Đề Thi) + MCQ**: **Q06–Q21, Q24, Q26–Q28, Q30–Q33, Q39, Q40** (*Forwards, Futures MTM Margin, Swaps, CIP, Put-Call Parity, Option Spreads/Butterflies/Collars, Binomial Trees 1-step & 2-step, Dynamic Delta Hedging, Option Leverage & Beta*). **BẮT BUỘC LÀM THÀNH THỤC 100%!**
>   3. 📌 **9 Câu Nắm Bản Chất Ăn Trọn Điểm MCQ (Không Thi Tính Toán Tự Luận)**: **Q22, Q23, Q25, Q29, Q34, Q35, Q36, Q37, Q38** (*BSM Formula Calculations, Merton Structural Model & Early Exercise / American Options*). Đề thi tự luận không bắt bấm công thức BSM hay cây American Option, nhưng **bản chất kinh tế** của 9 câu này (Time value, Convexity/Gamma, Implied vs Realized Vol, Risk-Neutral vs Physical Prob, European vs American Put Lower Bound, Dividend Early Exercise) là mỏ vàng ra đề cho **10 câu MCQ**! Tài liệu vẫn trình bày đủ lời giải số học chuẩn 100% kèm hộp đúc kết bản chất MCQ.

### Bảng Tra Cứu Nhanh 40 Câu Hỏi (Quick Index)

| Nhóm Bài Học | Câu Hỏi | Chủ Đề Trọng Tâm | Nhãn Chiến Lược |
|---|---|---|---|
| **Lecture 08** | Q01 – Q05 | EMH Forms, Behavioural Biases, FF3 Alpha & Fees, Prospect Theory/Mental Accounting, Short-Borrow Limits to Arbitrage | 🎯 MCQ & Tự luận |
| **Lecture 09** | Q06 – Q15 | Forward Valuation, Futures Margin Ledger, IRS & Currency Swaps, Index/Commodity Forwards, Hedging Liquidity Trap, CIP & Synthetic Forward Arbitrage | 🔥 Tự luận Cốt tử (40%) + MCQ |
| **Lecture 10** | Q16 – Q21, Q24 | Covered Call, Bear Put Spread, Parity Discount Factor, Straddle vs Strangle, Call Lower Bound Arbitrage, Butterfly, Binomial Collar | 🔥 Tự luận Cốt tử (40%) + MCQ |
| **Lecture 10** | Q22, Q23, Q25 | Ex-Dividend American Call, Maturity/Rate Effects on Puts & Calls, Merton Structural Credit Spread & MM | 📌 Bản chất MCQ (Đủ giải chi tiết) |
| **Lecture 11** | Q26–Q28, Q30–Q33, Q39–Q40 | Replicating Portfolio, Arrow-Debreu State Prices, No-Arbitrage Bounds, Log-Return Vol Scaling, Missing Strike, 2-Step Multiplicative & Additive Trees, Dynamic Delta Hedging, Option Beta/CAPM | 🔥 Tự luận Cốt tử (40%) + MCQ |
| **Lecture 11** | Q29, Q34–Q38 | BSM Call/Put, European vs American Lower Bound, BSM Delta/Gamma Repricing, Implied Vol Interpolation, $Q$ vs $P$ Probability, Suboptimal vs Optimal American Put | 📌 Bản chất MCQ (Đủ giải chi tiết) |

---

# PHẦN I — LECTURE 08: MARKET EFFICIENCY AND BEHAVIOURAL FINANCE (Q01 – Q05)

*Quy ước chung từ đề gốc: Với các phép tính số học, bỏ qua thuế và các chi phí ngoài những chi phí được nêu rõ trong đề.*

---
## Question 1 (Easy) — Kiểm Định Các Dạng Hiệu Quả Thị Trường (EMH Forms)
🎯 **[LECTURE 08: EMH, FF3 ALPHA & TÀI CHÍNH HÀNH VI — ÔN CẢ MCQ & TỰ LUẬN]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Two investors make the following claims.
>
> | Investor | Observation and claim |
> |---|---|
> | Alpha | A strategy using only past share prices returned 14% last year, while the market returned 10%. Alpha concludes that weak-form efficiency has been disproved. |
> | Beta | Across many announcements, a strategy using confidential earnings information before publication consistently earns positive risk-adjusted returns after all costs. Beta concludes that semi-strong-form efficiency has been disproved. |
>
> a. Assess Alpha's conclusion. What further evidence would be needed?
>
> b. Taking Beta's reported abnormal performance as established, assess the conclusion about the form of efficiency.

**Tóm tắt dữ kiện:**
- **Alpha**: Dùng dữ liệu giá quá khứ (*past share prices*), đạt tỷ suất sinh lời thô $14\%$ trong **1 năm** so với thị trường $10\%$ $\rightarrow$ Kết luận bác bỏ **Weak-form EMH**.
- **Beta**: Dùng thông tin lợi nhuận **mật / nội gián trước khi công bố** (*confidential earnings information before publication*) qua nhiều kỳ công bố, tạo $\alpha > 0$ đã điều chỉnh rủi ro và trừ mọi chi phí $\rightarrow$ Kết luận bác bỏ **Semi-strong-form EMH**.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Đánh giá kết luận của Alpha & Bằng chứng cần bổ sung**
- **Đánh giá:** Kết luận của Alpha là **không hợp lệ / quá vội vàng (invalid / premature)**. Việc một chiến lược phân tích kỹ thuật dựa trên giá quá khứ có tỷ suất sinh lời thô $14\%$ vượt thị trường ($10\%$) trong **một năm đơn lẻ** hoàn toàn **KHÔNG đủ để bác bỏ hiệu quả dạng yếu (weak-form efficiency)** vì 4 lý do cốt lõi:
  1. **Chưa điều chỉnh rủi ro (Lack of risk adjustment & Joint Hypothesis Problem):** Tỷ suất sinh lời $14\%$ cao hơn $10\%$ có thể chỉ là phần bù hợp lý cho mức rủi ro hệ thống cao hơn (ví dụ hệ số $\beta_M > 1$, phơi nhiễm nhân tố quy mô SMB, giá trị HML, hoặc rủi ro đuôi) chứ không phải lợi nhuận bất thường ($\alpha > 0$).
  2. **Chưa trừ chi phí giao dịch thực tế (Transaction & implementation costs):** Các chiến lược giao dịch dựa trên giá quá khứ thường quay vòng danh mục nhiều, chịu phí hoa hồng, chênh lệch giá mua-bán (*bid-ask spread*) và tác động giá (*market impact*). Lợi nhuận ròng sau chi phí có thể thấp hơn mức chuẩn.
  3. **Cỡ mẫu quá nhỏ / Yếu tố may mắn ngẫu nhiên (Statistical significance / Luck):** Quan sát chỉ trong **1 năm** ($T = 1$) hoàn toàn có thể xảy ra do biến động ngẫu nhiên (*random noise*), không có ý nghĩa thống kê.
  4. **Thiên lệch khai phá dữ liệu & sống sót (Data snooping / Look-ahead / Survivorship bias):** Nếu chiến lược được chọn lọc hậu nghiệm từ hàng trăm quy tắc quá khứ thì hiệu quả trong mẫu không chứng minh được khả năng dự báo ngoài mẫu.
- **Bằng chứng cần bổ sung (Further evidence needed):**
  - Chiến lược chỉ dùng dữ liệu giao dịch quá khứ phải tạo ra **lợi nhuận bất thường dương sau khi đã điều chỉnh rủi ro hợp lý** (*positive risk-adjusted abnormal returns*, $\alpha > 0$ so với mô hình định giá tài sản chuẩn),
  - **Ròng sau tất cả chi phí giao dịch và thực thi** (*net of all transaction, spread, and shorting/implementation costs*),
  - Có **ý nghĩa thống kê** (*statistically significant*) và **bền vững ngoài mẫu** (*persistent out-of-sample*) qua nhiều giai đoạn thị trường khác nhau.

#### **b. Đánh giá kết luận của Beta về cấp độ hiệu quả thị trường**
- **Đánh giá:** Ngay cả khi chấp nhận lợi nhuận bất thường của Beta là có thật, **kết luận của Beta về cấp độ hiệu quả bị bác bỏ là SAI (misidentifies the form of efficiency)**!
- **Giải thích bản chất:**
  - Tập thông tin được phân chia thành 3 tầng lồng nhau:
    - **Weak-form EMH**: Giá phản ánh mọi thông tin lịch sử giao dịch (giá, khối lượng quá khứ).
    - **Semi-strong-form EMH**: Giá phản ánh mọi **thông tin công khai** (*all publicly available information*).
    - **Strong-form EMH**: Giá phản ánh **tất cả mọi thông tin, bao gồm cả công khai lẫn thông tin nội bộ/riêng tư** (*both public and confidential/private information*).
  - Chiến lược của Beta khai thác **thông tin lợi nhuận mật trước khi được công bố ra công chúng** (*non-public / private / inside information*). Đây KHÔNG phải là thông tin công khai.
  - Do đó, kết quả của Beta **bác bỏ hiệu quả dạng mạnh (disproves STRONG-FORM efficiency)**, chứ **KHÔNG bác bỏ hiệu quả dạng bán mạnh (does NOT disprove semi-strong-form efficiency)**! Một thị trường hoàn toàn có thể đạt hiệu quả bán mạnh (giá phản ánh tức thì ngay khi tin tức được công bố) trong khi người nắm tin mật trước giờ công bố vẫn kiếm lời bất thường.

> [!TIP]
> **English Exam-Ready Phrasing:**
> - *Part a:* "Alpha's conclusion is unwarranted. One year of higher raw return (14% vs 10%) does not disprove weak-form efficiency because returns are neither risk-adjusted nor net of transaction costs, and a single-year outcome may simply reflect random luck or data snooping. Disproving weak-form efficiency requires statistically significant, out-of-sample positive risk-adjusted abnormal returns net of all trading costs."
> - *Part b:* "Beta misidentifies the efficiency form. Confidential pre-publication earnings data is private (non-public) information. Consistently profiting from private information after risk adjustment and costs disproves **strong-form** efficiency, not **semi-strong-form** efficiency (which applies only to publicly available information)."

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Quy tắc 3 bước kiểm tra mọi tuyên bố "bác bỏ EMH":**
  1. **Xác định đúng Tập thông tin (*Information Set*)**: Giá/khối lượng quá khứ $\rightarrow$ *Weak*; Báo cáo/tin tức công khai $\rightarrow$ *Semi-strong*; Tin mật/nội gián chưa công bố $\rightarrow$ *Strong*.
  2. **Kiểm tra 3 bộ lọc lợi nhuận (*3 Hurdles*)**: Đã **điều chỉnh rủi ro** chưa? Đã **trừ mọi chi phí giao dịch** chưa? Có **ý nghĩa thống kê dài hạn ngoài mẫu** không?
  3. Thiếu bất kỳ mắt xích nào ở Bước 2 $\rightarrow$ Bác bỏ kết luận của nhà đầu tư; Sai tập thông tin ở Bước 1 $\rightarrow$ Sửa lại đúng cấp độ EMH!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Nhầm thời điểm công bố ở câu b):** Thấy chữ *"earnings announcements"* liền phản xạ chọn *semi-strong-form* mà bỏ sót cụm từ quyết định **"confidential ... before publication"**! Giao dịch *sau* khi công bố mới kiểm định semi-strong; giao dịch *trước* khi công bố bằng tin mật là kiểm định **strong-form**.
- **Bẫy 2 (Bỏ sót Joint Hypothesis ở câu a):** Chỉ nói "1 năm là quá ngắn" mà quên nhắc tới **rủi ro (risk adjustment)** và **chi phí giao dịch (transaction costs)** sẽ mất ít nhất một nửa số điểm câu a.

---
## Question 2 (Average) — Nhận Diện & Phân Biệt Thiên Kiến Hành Vi (Behavioural Biases)
🎯 **[LECTURE 08: EMH, FF3 ALPHA & TÀI CHÍNH HÀNH VI — ÔN CẢ MCQ & TỰ LUẬN]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Consider the following decisions.
>
> | Investor | Decision |
> |---|---|
> | Gamma | Estimates a share's value at USD 82 using cash-flow forecasts and a discount rate. After a colleague mentions that the share once traded at USD 120, Gamma raises the estimate to USD 105 without changing either input, explaining that it should return closer to its old price. |
> | Delta | Expects a firm's sales to recover. Delta retains favourable sales updates in the investment review but excludes equally reliable, relevant evidence of falling orders because it conflicts with that expectation. |
>
> For each investor, identify the bias best supported by the case. Explain the decisive detail and distinguish your answer from one other plausible bias.

**Tóm tắt dữ kiện:**
- **Gamma**: Định giá DCF = USD 82; nghe đồng nghiệp nhắc giá lịch sử từng đạt USD 120 liền nâng định giá lên USD 105 **mà không hề thay đổi dự phóng dòng tiền hay lãi suất chiết khấu**.
- **Delta**: Kỳ vọng doanh thu phục hồi; giữ lại tin tốt phù hợp kỳ vọng nhưng **loại bỏ bằng chứng tin cậy tương đương về đơn hàng sụt giảm** chỉ vì nó mâu thuẫn với kỳ vọng ban đầu.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **Trường hợp 1: Nhà đầu tư Gamma**
1. **Thiên kiến phù hợp nhất (Best-supported bias):** **Anchoring (and insufficient adjustment) — Thiên kiến Neo định (Mỏ neo tâm lý)**.
2. **Chi tiết quyết định (Decisive detail):** Gamma bị "neo" vào một con số tham chiếu trong quá khứ không còn liên quan đến giá trị nội tại hiện tại (**mức giá cũ USD 120**) và kéo ước tính giá trị từ USD 82 lên USD 105 về phía con số neo đó **mà không hề điều chỉnh bất kỳ đầu vào cơ bản nào** (*without changing either cash-flow forecasts or the discount rate*).
3. **Phân biệt với thiên kiến dễ nhầm lẫn khác (Distinction from another plausible bias):**
   - *Phân biệt với **Conservatism bias (Thiên kiến bảo thủ)**:* Conservatism là việc nhà đầu tư cập nhật niềm tin quá chậm trước **thông tin cơ bản mới** (*new fundamental evidence*), bám chặt vào mô hình/niềm tin cơ bản ban đầu của mình. Ngược lại, ở đây **không hề có thông tin cơ bản mới nào**, và Gamma lại từ bỏ chính kết quả định giá cơ bản USD 82 của mình để chạy theo một con số giá quá khứ tùy tiện (USD 120).
   - *(Hoặc phân biệt với **Representativeness / Extrapolation**: Representativeness đánh giá xác suất dựa trên sự tương đồng với khuôn mẫu điển hình hoặc ngoại suy chuỗi xu hướng tăng trưởng gần đây thành quy luật dài hạn, trong khi hành vi của Gamma xoay quanh việc bám vào một mức giá số học cụ thể USD 120 làm điểm neo).*

#### **Trường hợp 2: Nhà đầu tư Delta**
1. **Thiên kiến phù hợp nhất (Best-supported bias):** **Confirmation bias — Thiên kiến Xác nhận**.
2. **Chi tiết quyết định (Decisive detail):** Việc lọc thông tin **bất đối xứng theo chiều hướng niềm tin có sẵn** (*selective filtering based on agreement with prior belief*): Delta giữ lại các cập nhật tích cực ủng hộ kỳ vọng doanh số phục hồi, nhưng **chủ động loại bỏ bằng chứng có độ tin cậy và mức độ liên quan ngang bằng** (đơn đặt hàng giảm) **chỉ vì nó trái ngược với kỳ vọng ban đầu**.
3. **Phân biệt với thiên kiến dễ nhầm lẫn khác (Distinction from another plausible bias):**
   - *Phân biệt với **Conservatism bias (Thiên kiến bảo thủ)**:* Một người mắc thiên kiến bảo thủ sẽ đánh giá thấp/phản ứng chậm với **mọi thông tin mới nói chung** (bất kể tin tốt hay tin xấu) để giữ nguyên tiên nghiệm ban đầu. Ngược lại, Delta **sẵn sàng tiếp nhận ngay thông tin mới nếu nó thuận chiều** kỳ vọng (tin doanh số tích cực) và **chỉ gạt bỏ thông tin mới khi nó ngược chiều** (đơn hàng giảm)!
   - *(Hoặc phân biệt với **Overconfidence (Quá tự tin)**: Overconfidence là đánh giá quá cao độ chính xác của thông tin/kỹ năng phân tích cá nhân — thu hẹp khoảng tin cậy dự báo — chứ không nhất thiết là hành vi chọn lọc giữ tin thuận, xóa bỏ dữ liệu thực tế ngược chiều trong báo cáo rà soát).*

> [!TIP]
> **English Exam-Ready Phrasing:**
> - *Gamma:* "**Anchoring bias**. The decisive detail is that Gamma revises the valuation from USD 82 toward a salient historical price of USD 120 (to USD 105) without altering cash-flow forecasts or the discount rate. Unlike **conservatism** (under-reacting to new fundamental information by clinging to one's prior valuation), Gamma abandons the fundamental valuation in response to an irrelevant numerical reference point."
> - *Delta:* "**Confirmation bias**. The decisive detail is asymmetric, selective treatment of equally reliable new evidence—retaining supportive sales data while excluding contradictory order declines solely because they conflict with Delta's prior belief. Unlike **conservatism** (which underweights new evidence uniformly regardless of direction), Delta readily incorporates confirming new data and rejects only disconfirming data."

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Từ khóa nhận diện 3 giây trong đề thi của GS. Cayirli:**
  - Có con số quá khứ/tùy tiện kéo lệch ước tính dù **inputs không đổi** $\rightarrow$ **Anchoring**.
  - Nhận tin thuận, **gạt bỏ tin ngược dù độ tin cậy ngang nhau** $\rightarrow$ **Confirmation bias**.
  - Phản ứng chậm với tin tức cơ bản mới (ví dụ *post-earnings announcement drift*) $\rightarrow$ **Conservatism**.
  - Ngoại suy vài năm tăng trưởng tốt thành "công ty tốt = cổ phiếu tốt" bỏ qua quy luật hồi quy trung bình (*base rate neglect*) $\rightarrow$ **Representativeness**.
  - Khoảng tin cậy quá hẹp / giao dịch quá mức (*excessive trading*) làm giảm lợi nhuận ròng $\rightarrow$ **Overconfidence**.

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Đọc thiếu yêu cầu kép của đề:** Đề yêu cầu rõ **3 phần** cho mỗi nhà đầu tư: (1) Gọi tên thiên kiến, (2) Chỉ ra chi tiết quyết định trong đề (*decisive detail*), và (3) **Phân biệt với một thiên kiến hợp lý khác** (*distinguish from one other plausible bias*). Sinh viên chỉ nêu tên thiên kiến mà không đối chiếu phân biệt sẽ mất tới 40–50% điểm câu này!

---
## Question 3 (Average) — Đánh Giá Hiệu Quả Quỹ Với Fama-French 3 Nhân Tố & Phí Quản Lý
🎯 **[LECTURE 08: EMH, FF3 ALPHA & TÀI CHÍNH HÀNH VI — ÔN CẢ MCQ & TỰ LUẬN]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Kappa and Lambda report the following results for the same year. Use the three-factor benchmark with these annual inputs:
>
> | Input | Value |
> |---|---:|
> | Risk-free return | 2.00% |
> | Market excess return | 6.00% |
> | SMB return | 2.00% |
> | HML return | 3.00% |
>
> | Fund | Gross return | Market loading | SMB loading | HML loading | Management fee | Trading costs |
> |---|---:|---:|---:|---:|---:|---:|
> | Kappa | 12.80% | 1.40 | 0.50 | -0.20 | 1.10% | 0.70% |
> | Lambda | 11.60% | 0.90 | -0.30 | 0.40 | 1.20% | 0.40% |
>
> Factor loadings remain constant over the year. Gross returns are measured before either listed cost. Each cost is charged as the stated percentage of beginning-of-year fund value and deducted once at year-end. The benchmark has no additional implementation costs in this comparison.
>
> a. Calculate each fund's benchmark return, gross abnormal return, net return and net abnormal return. Compare the rankings by gross return and net abnormal return.
>
> b. Holding gross returns and trading costs fixed, find the management fee at which each fund's net abnormal return becomes zero.
>
> c. Theta says, "Kappa's higher gross return establishes superior skill, and positive net abnormal returns prove that markets are inefficient." Assess both claims.

**Tóm tắt thông số:**
- $r_f = 2.00\%$; $R_M - r_f = 6.00\%$ (lưu ý đề đã cho sẵn **Market excess return**, KHÔNG trừ $r_f$ lần nữa!); $SMB = 2.00\%$; $HML = 3.00\%$.
- **Kappa**: $R_{\text{gross}} = 12.80\%$, $(\beta_M, \beta_{SMB}, \beta_{HML}) = (1.40, 0.50, -0.20)$, $f_{\text{mgmt}} = 1.10\%$, $c_{\text{trade}} = 0.70\%$.
- **Lambda**: $R_{\text{gross}} = 11.60\%$, $(\beta_M, \beta_{SMB}, \beta_{HML}) = (0.90, -0.30, 0.40)$, $f_{\text{mgmt}} = 1.20\%$, $c_{\text{trade}} = 0.40\%$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Tính toán các chỉ tiêu & So sánh thứ hạng**
Công thức tỷ suất sinh lời chuẩn 3 nhân tố Fama-French (*FF3 Benchmark Return*):
$$R_B = r_f + \beta_M (R_M - r_f) + \beta_{SMB} \cdot SMB + \beta_{HML} \cdot HML$$

1. **Quỹ Kappa:**
   - **Benchmark return ($R_{B,K}$):**
     $$R_{B,K} = 2.00\% + 1.40(6.00\%) + 0.50(2.00\%) + (-0.20)(3.00\%) = 2.00\% + 8.40\% + 1.00\% - 0.60\% = \mathbf{10.80\%}$$
   - **Gross abnormal return ($\alpha_{\text{gross},K}$):**
     $$\alpha_{\text{gross},K} = R_{\text{gross},K} - R_{B,K} = 12.80\% - 10.80\% = \mathbf{2.00\%}$$
   - **Net return ($R_{\text{net},K}$):**
     $$R_{\text{net},K} = R_{\text{gross},K} - f_{\text{mgmt},K} - c_{\text{trade},K} = 12.80\% - 1.10\% - 0.70\% = \mathbf{11.00\%}$$
   - **Net abnormal return ($\alpha_{\text{net},K}$):**
     $$\alpha_{\text{net},K} = R_{\text{net},K} - R_{B,K} = 11.00\% - 10.80\% = \mathbf{0.20\%} \quad (\text{hoặc } 2.00\% - 1.80\% = 0.20\%)$$

2. **Quỹ Lambda:**
   - **Benchmark return ($R_{B,L}$):**
     $$R_{B,L} = 2.00\% + 0.90(6.00\%) + (-0.30)(2.00\%) + 0.40(3.00\%) = 2.00\% + 5.40\% - 0.60\% + 1.20\% = \mathbf{8.00\%}$$
   - **Gross abnormal return ($\alpha_{\text{gross},L}$):**
     $$\alpha_{\text{gross},L} = R_{\text{gross},L} - R_{B,L} = 11.60\% - 8.00\% = \mathbf{3.60\%}$$
   - **Net return ($R_{\text{net},L}$):**
     $$R_{\text{net},L} = R_{\text{gross},L} - f_{\text{mgmt},L} - c_{\text{trade},L} = 11.60\% - 1.20\% - 0.40\% = \mathbf{10.00\%}$$
   - **Net abnormal return ($\alpha_{\text{net},L}$):**
     $$\alpha_{\text{net},L} = R_{\text{net},L} - R_{B,L} = 10.00\% - 8.00\% = \mathbf{2.00\%} \quad (\text{hoặc } 3.60\% - 1.60\% = 2.00\%)$$

| Chỉ tiêu | Quỹ Kappa | Quỹ Lambda | Xếp hạng cao hơn |
|---|---:|---:|---|
| Gross return ($R_{\text{gross}}$) | **12.80%** | 11.60% | **Kappa** (+1.20%) |
| FF3 Benchmark return ($R_B$) | 10.80% | 8.00% | Kappa chịu rủi ro cao hơn (+2.80%) |
| Gross abnormal return ($\alpha_{\text{gross}}$) | 2.00% | **3.60%** | **Lambda** (+1.60%) |
| Net return ($R_{\text{net}}$) | 11.00% | 10.00% | Kappa (+1.00%) |
| **Net abnormal return ($\alpha_{\text{net}}$)** | 0.20% | **2.00%** | **Lambda** (+1.80%, gấp 10 lần!) |

- **So sánh thứ hạng:** Xếp theo tỷ suất sinh lời gộp (*gross return*), **Kappa đứng nhất** ($12.80\% > 11.60\%$). Tuy nhiên, sau khi điều chỉnh rủi ro nhân tố và trừ chi phí, xếp theo lợi nhuận bất thường ròng (*net abnormal return*), **thứ hạng đảo ngược hoàn toàn: Lambda vượt trội áp đảo** ($2.00\% > 0.20\%$). Lợi nhuận thô của Kappa cao hơn chỉ vì gánh rủi ro thị trường và quy mô lớn hơn nhiều ($R_{B,K} = 10.80\%$ so với $8.00\%$) và còn bị bào mòn mạnh bởi chi phí giao dịch ($0.70\%$).

#### **b. Mức phí quản lý hòa vốn làm $\alpha_{\text{net}} = 0$**
Giữ nguyên $R_{\text{gross}}$, $R_B$ và $c_{\text{trade}}$, ta đặt $\alpha_{\text{net}} = \alpha_{\text{gross}} - c_{\text{trade}} - f_{\text{mgmt}}^* = 0 \implies f_{\text{mgmt}}^* = \alpha_{\text{gross}} - c_{\text{trade}}$:
- **Kappa:** $f_{\text{mgmt},K}^* = 2.00\% - 0.70\% = \mathbf{1.30\%}$ (kiểm lại: $12.80\% - 0.70\% - 1.30\% = 10.80\% = R_{B,K}$).
- **Lambda:** $f_{\text{mgmt},L}^* = 3.60\% - 0.40\% = \mathbf{3.20\%}$ (kiểm lại: $11.60\% - 0.40\% - 3.20\% = 8.00\% = R_{B,L}$).
*(Ý nghĩa Berk-Green: Đây là mức phí quản lý tối đa nhà quản lý quỹ có thể thu để thu hút toàn bộ thặng dư kỹ năng trước khi nhà đầu tư nhận $\alpha_{\text{net}} = 0$).*

#### **c. Đánh giá hai nhận định của Theta**
1. **Nhận định 1 — *"Kappa's higher gross return establishes superior skill"* (SAI):**
   - Tỷ suất sinh lời gộp (*gross raw return*) trộn lẫn **phần bù rủi ro nhân tố thụ động** ($R_B$) với **kỹ năng chọn lọc chủ động** ($\alpha$). Kappa đạt $12.80\%$ chủ yếu nhờ đòn bẩy rủi ro thị trường cao ($\beta_M = 1.40 \implies R_{B,K} = 10.80\%$). Khi tách bỏ phần bù rủi ro nhân tố, kỹ năng tạo alpha gộp của Lambda cao hơn hẳn ($3.60\%$ so với $2.00\%$) và chi phí giao dịch cũng thấp hơn ($0.40\%$ so với $0.70\%$), mang lại giá trị ròng vượt trội cho nhà đầu tư ($2.00\%$ so với $0.20\%$).
2. **Nhận định 2 — *"Positive net abnormal returns prove that markets are inefficient"* (SAI):**
   - **Thứ nhất (Sampling variation / Luck):** Kết quả chỉ quan sát trong **1 năm duy nhất** ở 2 quỹ; alpha dương trong 1 năm hoàn toàn có thể đến từ may mắn ngẫu nhiên (*random realization / survivorship bias*), không chứng minh được khả năng tạo alpha kỳ vọng bền vững có ý nghĩa thống kê.
   - **Thứ hai (Joint Hypothesis Problem — Vấn đề Giả thuyết Kép):** Mọi phép đo lợi nhuận bất thường đều phụ thuộc đồng thời vào giả định mô hình chuẩn FF3 là mô hình định giá đúng hoàn toàn. Alpha dương so với FF3 có thể phản ánh phần bù của **các nhân tố rủi ro bị bỏ sót** (*omitted risk factors* như quán tính giá *momentum*, khả năng sinh lời, thanh khoản) chứ không phải sự phi hiệu quả của thị trường!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Công thức chuỗi 1 dòng không bao giờ nhầm:**
  $$\alpha_{\text{gross}} = R_{\text{gross}} - R_B \quad \longrightarrow \quad \alpha_{\text{net}} = \alpha_{\text{gross}} - (f_{\text{mgmt}} + c_{\text{trade}}) \quad \longrightarrow \quad f_{\text{mgmt}}^* = \alpha_{\text{gross}} - c_{\text{trade}}$$
- Lưu ý nhanh câu b: Chỉ cần lấy **Net abnormal return hiện tại cộng thêm Management fee hiện tại**:
  - Kappa: $0.20\% + 1.10\% = 1.30\%$!
  - Lambda: $2.00\% + 1.20\% = 3.20\%$! (Tính nhẩm trong 2 giây, không thể sai!).

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Trừ $r_f$ hai lần):** Đề cho *"Market excess return = 6.00%"* (tức là $R_M - r_f = 6.00\%$). Nếu sinh viên lấy $6.00\% - 2.00\% = 4.00\%$ rồi mới nhân $\beta_M$ là sai toàn bộ câu a và câu b!
- **Bẫy 2 (Quên trừ Trading costs ở câu b):** Câu b hỏi mức phí quản lý để $\alpha_{\text{net}} = 0$ khi giữ nguyên chi phí giao dịch. Nếu gán nhầm $f_{\text{mgmt}}^* = \alpha_{\text{gross}}$ ($2.00\%$ và $3.60\%$) mà quên trừ $c_{\text{trade}}$ ($0.70\%$ và $0.40\%$) sẽ mất trọn điểm câu b!

---
## Question 4 (Average) — Lý Thuyết Triển Vọng, Hiệu Ứng Vị Thế & Kế Toán Tâm Lý
🎯 **[LECTURE 08: EMH, FF3 ALPHA & TÀI CHÍNH HÀNH VI — ÔN CẢ MCQ & TỰ LUẬN]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Each comparison below presents two versions of the same decision. Within a comparison, current total wealth, probabilities, investment opportunities and all other circumstances are identical. Only the stated purchase price or source label changes. There are no taxes or transaction costs, and cash earns no interest over the month.
>
> | Investor | Alternatives | Choices in the two versions |
> |---|---|---|
> | Epsilon | Sell a shareholding now for USD 10,000 and keep the cash, or hold it for one month. Its value will then be USD 8,000 or USD 12,000, each with probability 0.50. | If the original purchase cost was USD 6,000, Epsilon sells. If it was USD 14,000, Epsilon holds. |
> | Zeta | Keep USD 10,000 in cash, or invest it for one month and receive USD 8,000 or USD 12,000, each with probability 0.50. | Zeta keeps cash when it is described as accumulated salary savings, but invests when the same amount is described as a bonus. |
>
> a. An observer says Epsilon's choices prove loss aversion. Assess the claim and identify what the comparison does support.
>
> b. The observer explains Zeta's choices as ordinary risk aversion. Is that explanation sufficient? Identify the feature that matters.

**Tóm tắt thông số:**
- Tổng tài sản hiện tại (*current total wealth*), xác suất ($0.50 / 0.50$ cho USD 8,000 hoặc USD 12,000, kỳ vọng = USD 10,000) và mọi hoàn cảnh khác **giống hệt nhau** trong từng cặp so sánh; $r = 0$, không thuế/chi phí.
- **Epsilon**: Giá hiện tại USD 10,000. Nếu giá mua gốc là USD 6,000 $\rightarrow$ **Bán** (chốt chắc USD 10,000). Nếu giá mua gốc là USD 14,000 $\rightarrow$ **Giữ** (chấp nhận trò chơi rủi ro 50/50 giữa USD 8,000 và USD 12,000).
- **Zeta**: Đang cầm USD 10,000 tiền mặt. Nếu gắn nhãn "tiết kiệm lương tích lũy" $\rightarrow$ **Giữ tiền mặt**. Nếu gắn nhãn "tiền thưởng (*bonus*)" $\rightarrow$ **Đầu tư mạo hiểm** (50/50 giữa USD 8,000 và USD 12,000).

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Đánh giá tuyên bố về Epsilon ("chứng minh Loss Aversion") & Xác định bản chất thực sự**
1. **Đánh giá tuyên bố của người quan sát:** Tuyên bố rằng lựa chọn của Epsilon tự nó **chứng minh chứng ghét lỗ (*loss aversion*) là SAI / KHÔNG ĐỦ CƠ SỞ (incorrect / not established by this comparison alone)**!
   - **Giải thích chặt chẽ:** *Loss aversion* (hệ số độ dốc vùng lỗ lớn hơn vùng lãi tại điểm tham chiếu, $|v(-x)| > v(+x)$) giải thích việc nhà đầu tư từ chối các trò chơi **pha trộn cả lãi lẫn lỗ quanh điểm tham chiếu** (*mixed gambles straddling the reference point*, ví dụ $50\%$ thắng $+2,000$ và $50\%$ thua $-2,000$).
   - Ngược lại, trong cả hai phiên bản của Epsilon (lấy giá mua gốc làm điểm tham chiếu):
     - **Khi giá mua gốc = USD 6,000:** Mọi kết cục đều nằm **hoàn toàn trong miền LÃI (pure gain domain)**: bán ngay lãi chắc chắn $+\text{USD } 4,000$; giữ lại nhận $50\%$ lãi $+\text{USD } 2,000$ hoặc $50\%$ lãi $+\text{USD } 6,000$. Không hề có kết cục lỗ nào!
     - **Khi giá mua gốc = USD 14,000:** Mọi kết cục đều nằm **hoàn toàn trong miền LỖ (pure loss domain)**: bán ngay lỗ chắc chắn $-\text{USD } 4,000$; giữ lại nhận $50\%$ lỗ $-\text{USD } 6,000$ hoặc $50\%$ lỗ $-\text{USD } 2,000$. Không hề đi qua điểm tham chiếu!
     - Vì không phương án nào cắt qua điểm tham chiếu giữa miền lãi và miền lỗ, độ gãy khúc (*kink*) của *loss aversion* tại điểm $0$ không phải là yếu tố tạo ra sự đảo chiều này!
2. **Những gì phép so sánh của Epsilon THỰC SỰ chứng minh (What the comparison DOES support):**
   - **Thứ nhất — Phụ thuộc điểm tham chiếu (*Reference-point dependence / Framing around historical purchase cost*):** Vì tổng tài sản hiện tại và phân phối tài sản cuối kỳ (chắc chắn USD 10,000 so với trò chơi 50/50 USD 8,000 / USD 12,000) là **đồng nhất 100%** ở cả hai phiên bản, một nhà đầu tư tối đa hóa hữu dụng kỳ vọng cổ điển (*standard expected-utility investor* đánh giá trên tổng tài sản cuối kỳ $W_T$) **bắt buộc phải đưa ra cùng một lựa chọn** bất kể giá mua quá khứ (*sunk cost*). Việc thay đổi hành vi chứng minh Epsilon đánh giá kết cục theo lãi/lỗ tương đối so với **điểm tham chiếu là giá mua ban đầu**.
   - **Thứ hai — Độ nhạy giảm dần & Thái độ rủi ro đối lập giữa miền lãi và miền lỗ (*Diminishing sensitivity / Reflection effect $\rightarrow$ Disposition Effect*):**
     - Hàm giá trị trong Prospect Theory **lõm (*concave*) trên miền lãi** $\rightarrow$ **Ngại rủi ro trong miền lãi (*risk-averse in gains*)**: tại giá vốn USD 6,000, Epsilon thích khoản lãi chắc chắn $+4,000$ hơn trò chơi kỳ vọng $+4,000$ ($+2,000 / +6,000$) nên **bán sớm cổ phiếu đang lời**.
     - Hàm giá trị **lồi (*convex*) trên miền lỗ** $\rightarrow$ **Ưa rủi ro trong miền lỗ (*risk-seeking in losses*)**: tại giá vốn USD 14,000, Epsilon chấp nhận đánh cược ($-6,000 / -2,000$) để tránh hiện thực hóa khoản lỗ chắc chắn $-4,000$ nên **ôm chặt cổ phiếu đang lỗ**.
     - Hành vi bán cổ phiếu thắng quá sớm và giữ cổ phiếu thua quá lâu này chính là **Hiệu ứng Vị thế (Disposition Effect)**!

#### **b. Đánh giá cách giải thích về Zeta ("Ordinary risk aversion") & Xác định đặc tính cốt lõi**
1. **Cách giải thích bằng "ngại rủi ro thông thường" có đủ không?** **KHÔNG ĐỦ (và thực chất bị mâu thuẫn trực tiếp)!**
   - Theo lý thuyết hữu dụng kỳ vọng chuẩn với tính ngại rủi ro thông thường (*ordinary risk aversion*, $U''(W) < 0$):
     - **Tiền có tính thay thế hoàn toàn (*fungibility of money*)**: chỉ có **tổng tài sản $W$** và phân phối xác suất của tài sản cuối kỳ mới quyết định lựa chọn, chứ tên gọi nguồn gốc khoản tiền hoàn toàn vô nghĩa.
     - Hơn nữa, một nhà đầu tư ngại rủi ro chuẩn mực đứng trước một trò chơi công bằng có lợi nhuận kỳ vọng bằng 0 ($\pm \text{USD } 2,000$ với xác suất $0.50 / 0.50$, không có phần bù rủi ro) sẽ **luôn từ chối đầu tư ở CẢ HAI phiên bản** (hoặc ít nhất phải chọn giống hệt nhau ở cả hai phiên bản vì tổng tài sản hiện tại như nhau)! Việc Zeta chấp nhận trò chơi rủi ro không có phần bù khi tiền mang nhãn *bonus* bác bỏ lời giải thích bằng *ordinary risk aversion*.
2. **Đặc tính quyết định cần chỉ ra (The decisive feature):**
   - **Kế toán tâm lý (*Mental Accounting*) vi phạm nguyên lý tính thay thế của tiền (*violation of fungibility of money*)**: Zeta chia tách cùng một lượng tài sản vào các "ngăn tài khoản tâm lý" riêng biệt ("tiền tiết kiệm lương vất vả" so với "tiền thưởng bất ngờ") với mức độ chấp nhận rủi ro hoàn toàn khác nhau.
   - Kết hợp với **Hiệu ứng Tiền chùa / Tiền nhà cái (*House Money Effect*)**: khi khoản tiền được đóng khung là khoản thu nhập bất ngờ / lợi nhuận vừa kiếm được (*windfall / bonus*), nhà đầu tư sẵn sàng mạo hiểm cao hơn hẳn so với vốn gốc tích lũy từ lương.

> [!TIP]
> **English Exam-Ready Phrasing:**
> - *Part a:* "The claim is incorrect: Epsilon's choices do not isolate **loss aversion** (steeper slope for losses than gains at the reference point), because neither version involves a mixed gamble across the reference point—at a USD 6,000 cost all outcomes are gains (+2k, +4k, +6k), and at a USD 14,000 cost all outcomes are losses (-6k, -4k, -2k). Instead, since terminal wealth distributions are identical, changing choices proves **reference-point dependence** (framing around sunk purchase price) combined with **diminishing sensitivity / the reflection effect**—**risk aversion in the gain domain** and **risk-seeking in the loss domain**—which generates the **disposition effect**."
> - *Part b:* "No, ordinary risk aversion is insufficient. Under standard expected utility, money is **fungible** and an ordinarily risk-averse investor with identical total wealth would make the exact same choice in both versions (strictly rejecting a zero-mean fair gamble). Zeta's reversal demonstrates **mental accounting** (violating fungibility by segregating wealth by source label) and the **house money effect** (higher risk tolerance with windfall bonus money)."

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Mẹo phân biệt 3 khái niệm Prospect Theory cực hay bị hỏi xoáy:**
  1. **Loss aversion (Ghét lỗ — Kink tại 0):** Từ chối trò chơi 50/50 giữa $+\text{USD } 2,000$ và $-\text{USD } 1,800$ (kết cục vắt ngang qua mốc 0).
  2. **Reflection / Diminishing sensitivity + Disposition effect:** Bán khi đang lời (ngại rủi ro vùng dương), gồng khi đang lỗ (ưa rủi ro vùng âm) dù tổng tài sản hiện tại như nhau.
  3. **Mental accounting + House money effect:** Cùng 1 số tiền, cùng tổng tài sản nhưng đổi "nhãn nguồn tiền" (*salary* vs *bonus/dividend*) thì đổi quyết định rủi ro!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy chết người số 1 của GS. Cayirli ở câu 4a:** 90% sinh viên đọc không kỹ thấy "sợ chốt lỗ ở giá vốn 14,000" liền gật đầu đồng ý *"Yes, Epsilon proves loss aversion"*! Đó chính xác là cái bẫy đề bài giăng ra (*"An observer says Epsilon's choices prove loss aversion. Assess the claim..."*). Phải khẳng định rõ: **Không chứng minh loss aversion đơn thuần**, mà chứng minh **reference dependence + risk aversion in gains & risk-seeking in losses (diminishing sensitivity / disposition effect)**!

---
## Question 5 (Hard) — Giới Hạn Kinh Doanh Chênh Lệch Giá & Phí Vay Cổ Phiếu (Limits to Arbitrage)
🎯 **[LECTURE 08: EMH, FF3 ALPHA & TÀI CHÍNH HÀNH VI — ÔN CẢ MCQ & TỰ LUẬN]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Mu observes the following executable terms for Nu shares.
>
> | Item | Terms |
> |---|---|
> | Current share price | USD 100.00 |
> | One-year forward delivery price | USD 100.50 per share; zero initial value and cash settlement at maturity |
> | Dividend | USD 2.00 per share in six months; no other dividend before maturity |
> | Risk-free borrowing and lending | 4.00% annual effective; a dollar invested for $t$ years grows to $(1.04)^t$ |
> | Stock borrowing | Available for the full year at a fixed charge of USD 1.80 per share, paid at year-end |
>
> The dividend is certain. A short seller must compensate the share lender for the dividend when it is paid. Short-sale proceeds are fully available for investment, there are no margin requirements or other costs, and all parties perform as agreed.
>
> Mu says, "The forward differs from the textbook price, so there must be a guaranteed profit."
>
> a. Calculate the forward benchmark ignoring the stock-borrow charge, and compare it with the quotation.
>
> b. For 1,000 shares, construct the trade suggested by that comparison. Show its cash flows today, in six months and at year-end, including the stock-borrow charge. Calculate its terminal net profit or loss.
>
> c. Find the stock-borrow charge per share at which the trade breaks even.
>
> d. Assess Mu's claim. What does this example establish about market efficiency?

**Tóm tắt thông số:**
- $S_0 = \text{USD } 100.00$; kỳ hạn $T = 1$ năm; $F_{\text{quoted}} = \text{USD } 100.50$/cổ phiếu (tất toán tiền mặt lúc đáo hạn).
- Cổ tức chắc chắn $D = \text{USD } 2.00$/cổ phiếu tại $t = 0.5$ năm (người bán khống phải bồi hoàn cổ tức này cho bên cho vay cổ phiếu tại $t = 0.5$).
- Lãi suất phi rủi ro hiệu dụng năm (*annual effective*): $r = 4.00\%$ $\rightarrow$ hệ số tích lũy sau $t$ năm là $(1.04)^t$.
- Phí vay cổ phiếu (*stock-borrow charge*): $b = \text{USD } 1.80$/cổ phiếu, trả tại cuối năm ($t = 1$). Quy mô giao dịch câu b: $N = 1,000$ cổ phiếu.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Giá kỳ hạn chuẩn không ma sát (Textbook Forward Benchmark) & So sánh**
- Giá trị hiện tại của cổ tức USD 2.00 trả sau 6 tháng ($t = 0.5$):
  $$PV(D) = \frac{2.00}{(1.04)^{0.5}} = \frac{2.00}{1.01980390} = \text{USD } 1.961161 \quad (\approx \text{USD } 1.96)$$
- Giá kỳ hạn lý thuyết bỏ qua phí vay cổ phiếu:
  $$F_{\text{benchmark}} = \left[S_0 - PV(D)\right](1.04)^1 = 100.00(1.04) - 2.00(1.04)^{0.5} = 104.00 - 2.039608 = \mathbf{\text{USD } 101.960392 \approx \text{USD } 101.96\text{ per share}}$$
- **So sánh:** Giá kỳ hạn niêm yết trên thị trường ($\text{USD } 100.50$) **thấp hơn** mức giá chuẩn sách giáo khoa ($\text{USD } 101.96$) một khoảng $\text{USD } 1.460392 \approx \mathbf{\text{USD } 1.46}$ mỗi cổ phiếu (hợp đồng kỳ hạn có vẻ đang bị định giá thấp tương đối so với cổ phiếu giao ngay).

#### **b. Thiết lập giao dịch Reverse Cash-and-Carry cho 1,000 cổ phiếu & Bảng dòng tiền**
- Vì $F_{\text{quoted}} (100.50) < F_{\text{benchmark}} (101.96)$, nguyên tắc kinh doanh chênh lệch giá cổ điển gợi ý chiến lược **Reverse Cash-and-Carry**: **Mua kỳ hạn (Long forward)** 1,000 cổ phiếu giá rẻ USD 100.50, đồng thời **Vay và Bán khống (Borrow & Short sell)** 1,000 cổ phiếu giao ngay ở giá đắt USD 100.00, rồi đem tiền bán khống gửi lãi suất phi rủi ro $4\%$.
- Để tự tài trợ hoàn toàn nghĩa vụ trả cổ tức $\text{USD } 2,000.00$ tại $t = 0.5$ mà dòng tiền ròng tại $t = 0$ và $t = 0.5$ đều bằng $0$, ta tách khoản tiền thu từ bán khống $\text{USD } 100,000.00$ thành 2 sổ tiền gửi phi rủi ro *(Lưu ý: nếu gửi cả USD 100,000 kỳ hạn 1 năm nhận USD 104,000 rồi vay USD 2,000 tại $t = 0.5$ trong 6 tháng trả $2,000(1.04)^{0.5} = \text{USD } 2,039.61$ tại $t = 1$ thì kết quả cuối kỳ giống hệt 100% đến từng chữ số thập phân!)*:
  - Khoản gửi 6 tháng vừa đủ trả cổ tức: $\frac{2,000}{(1.04)^{0.5}} = \text{USD } 1,961.1614$ ($\approx \text{USD } 1,961.16$).
  - Khoản gửi 1 năm còn lại: $100,000 - 1,961.1614 = \text{USD } 98,038.8386$ ($\approx \text{USD } 98,038.84$).

| Hạng mục giao dịch (1,000 cổ phiếu) | Hôm nay ($t = 0$) | Sau 6 tháng ($t = 0.5$) | Cuối năm ($t = 1.0$, giá giao ngay $S_1$) |
|---|---:|---:|---:|
| 1. Vay & Bán khống 1,000 cổ phiếu Nu (trả cổ tức tại $t=0.5$, mua lại trả kho tại $t=1$) | $+100,000.00$ | $-2,000.00$ | $-1,000 S_1$ |
| 2. Gửi tiết kiệm 6 tháng ở $4\%$ EAR để tài trợ cổ tức | $-1,961.16$ | $+2,000.00$ | $0.00$ |
| 3. Gửi tiết kiệm 1 năm phần tiền còn lại ở $4\%$ EAR ($98,038.8386 \times 1.04$) | $-98,038.84$ | $0.00$ | $+101,960.39$ |
| 4. Long Forward 1,000 cổ phiếu tại $K = 100.50$ (tất toán tiền mặt) | $0.00$ | $0.00$ | $+1,000(S_1 - 100.50) = 1,000 S_1 - 100,500.00$ |
| *Tổng phụ trước phí vay cổ phiếu (Textbook arbitrage profit)* | *$0.00$* | *$0.00$* | *$+1,460.39$* |
| 5. Trả phí vay cổ phiếu (*Stock-borrow charge*: $1,000 \times 1.80$) | $0.00$ | $0.00$ | $-1,800.00$ |
| **Dòng tiền ròng (Net Cash Flow)** | **USD 0.00** | **USD 0.00** | **-USD 339.61** (*Chính xác: $-339.6078$*) |

- **Kết quả cuối kỳ:** Thay vì thu lãi, thương vụ tạo ra một **khoản LỖ RÒNG chắc chắn là $-\text{USD } 339.61$** ($\text{loss of USD } 339.61$, tức $-\text{USD } 0.3396$/cổ phiếu)!

#### **c. Mức phí vay cổ phiếu hòa vốn (Break-even Stock-Borrow Charge)**
- Trên mỗi cổ phiếu, chênh lệch trước phí vay cổ phiếu tại thời điểm đáo hạn là:
  $$F_{\text{benchmark}} - F_{\text{quoted}} = 101.960392 - 100.50 = \text{USD } 1.460392$$
- Để lợi nhuận ròng cuối kỳ bằng $0$:
  $$b^* = 101.960392 - 100.50 = \mathbf{\text{USD } 1.460392 \approx \text{USD } 1.46\text{ per share}}$$
  *(Kiểm chứng cho 1,000 cổ phiếu: $+1,460.3922 - 1,000(1.460392) = \text{USD } 0.00$).*

#### **d. Đánh giá tuyên bố của Mu & Ý nghĩa đối với Hiệu quả Thị trường (Market Efficiency)**
- **Đánh giá tuyên bố của Mu:** Tuyên bố của Mu là **SAI (False)**. Việc giá thị trường lệch khỏi công thức lý thuyết không ma sát (*frictionless textbook price*) **KHÔNG đảm bảo tồn tại lợi nhuận kinh doanh chênh lệch giá** khi chi phí thực thi thực tế — cụ thể ở đây là **chi phí vay cổ phiếu để bán khống (USD 1.80/cp)** — lớn hơn độ lệch định giá trước phí (USD 1.46/cp).
- **Bài học cốt lõi về Hiệu quả Thị trường (Limits to Arbitrage & No-Arbitrage Band):**
  1. **Vùng không kinh doanh chênh lệch giá (*No-Arbitrage Band*):** Chi phí bán khống và ma sát giao dịch tạo ra một dải biên độ quanh giá lý thuyết. Với phí vay cổ phiếu USD 1.80 trả cuối năm, cận dưới không-arbitrage thực tế của giá kỳ hạn chỉ là $101.96 - 1.80 = \text{USD } 100.16$. Vì giá kỳ hạn niêm yết $\text{USD } 100.50 \ge \text{USD } 100.16$, **không hề có cơ hội "bữa trưa miễn phí" (*no free lunch*) nào bị bỏ ngỏ**!
  2. **Hai mặt của hiệu quả thị trường ("No Free Lunch" vs "Price Equals Frictionless Value"):**
     - Một mặt, sự chênh lệch giữa USD 100.50 và USD 101.96 **không chứng minh thị trường phi hiệu quả** theo nghĩa tồn tại cơ hội kiếm lời phi rủi ro chưa được khai thác.
     - Mặt khác, do **Giới hạn Kinh doanh Chênh lệch giá (*Limits to Arbitrage*)**, lực lượng arbitrage không thể can thiệp để ép giá quay về đúng mốc không ma sát USD 101.96 chừng nào độ lệch còn nằm trong dải chi phí thực thi ($\le \text{USD } 1.80$). Do đó, không có arbitrage khả thi không đồng nghĩa giá tài sản luôn trùng khít công thức sách giáo khoa không ma sát!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Công thức Giá trị Tương lai Trực tiếp (khỏi cần tính qua PV rồi nhân ngược lại):**
  $$F_{\text{benchmark}} = S_0(1+r)^T - D(1+r)^{T - t_D} = 100(1.04) - 2(1.04)^{0.5} = 104 - 2.039608 = 101.960392$$
  - Chỉ mất 1 phép bấm máy duy nhất!
  - Sau đó lấy ngay:
    - $\text{Break-even borrow fee (paid at } T\text{)} = F_{\text{benchmark}} - F_{\text{quoted}} = 101.960392 - 100.50 = \text{USD } 1.46$.
    - $\text{Net P/L per share} = 1.460392 - 1.80 = -\text{USD } 0.339608 \implies 1,000\text{ shares} = -\text{USD } 339.61$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Chiết khấu nhầm thời điểm trả phí vay cổ phiếu):** Đề ghi rõ *"fixed charge of USD 1.80 per share, **paid at year-end**"*. Vì phí trả tại $t = 1$ (cùng thời điểm đáo hạn kỳ hạn), ta trừ trực tiếp USD 1.80 tại $t = 1$, **KHÔNG nhân thêm $(1.04)$**! (Ngược lại, nếu một đề khác cho phí vay trả đầu năm $t = 0$, khi quy về $t = 1$ mới nhân $1.04$).
- **Bẫy 2 (Đảo ngược chiều giao dịch):** Thấy $F_{\text{quoted}} = 100.50 > S_0 = 100.00$ liền tưởng kỳ hạn đắt nên đi *Cash-and-Carry* (mua cổ phiếu, bán kỳ hạn)! Phải so $F_{\text{quoted}}$ với **$F_{\text{benchmark}} = 101.96$**, KHÔNG bao giờ được so $F_{\text{quoted}}$ trực tiếp với $S_0$! Vì $100.50 < 101.96$, kỳ hạn đang **rẻ** so với chuẩn không ma sát $\rightarrow$ chiều gợi ý phải là **Long Forward + Short Stock** (*Reverse Cash-and-Carry*).

---

# PHẦN II — LECTURE 09: FORWARDS, FUTURES AND SWAPS (Q06 – Q15)

*Quy ước chung từ đề gốc: Bỏ qua thuế và chi phí ngoài những khoản được nêu rõ. Sử dụng đúng quy ước lãi suất (effective annual vs continuous vs quarterly) và quy ước thanh toán của từng câu. Giả định các đối tác thực hiện đúng nghĩa vụ hợp đồng.*

---
## Question 6 (Easy) — Định Giá Lại Hợp Đồng Kỳ Hạn Đang Lưu Hành & Đánh Giá Đề Nghị Tất Toán
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Alpha enters a nine-month long forward on 150 non-dividend-paying shares. The current share price is USD 68, and the risk-free rate is 4% effective annually. The contract has zero value at inception.
>
> Three months later, the share price is USD 72. The risk-free rate for the remaining term is now 5% effective annually. The counterparty offers to pay Alpha USD 500 to terminate the entire contract.
>
> a. Determine the original delivery price per share.
>
> b. Calculate the current value of Alpha's contract and assess the termination offer.

**Tóm tắt thông số:**
- Lúc khởi tạo ($t = 0$): Vị thế **Long forward** trên $N = 150$ cổ phiếu không trả cổ tức; kỳ hạn ban đầu $T = 9/12 = 0.75$ năm; $S_0 = \text{USD } 68$; $r_0 = 4\%$ EAR; giá trị hợp đồng ban đầu $V_0 = 0$.
- Sau 3 tháng ($t = 0.25$, kỳ hạn còn lại $\tau = 6/12 = 0.50$ năm): $S_t = \text{USD } 72$; lãi suất mới cho kỳ hạn còn lại $r_t = 5\%$ EAR.
- Đối tác đề nghị trả cho Alpha **USD 500** để hủy (tất toán sớm) toàn bộ hợp đồng 150 cổ phiếu.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Giá giao nhận kỳ hạn ban đầu trên mỗi cổ phiếu ($K$)**
Vì hợp đồng có giá trị bằng $0$ lúc khởi tạo và cổ phiếu không trả cổ tức trong 9 tháng ($T = 0.75$ năm), giá giao nhận ban đầu bằng giá kỳ hạn hợp lý tại $t = 0$:
$$K = F_0 = S_0 (1 + r_0)^{0.75} = 68 \times (1.04)^{0.75} = 68 \times 1.02985245 = \mathbf{\text{USD } 70.029966 \approx \text{USD } 70.03\text{ per share}}$$

#### **b. Giá trị hiện tại của hợp đồng sau 3 tháng & Đánh giá lời đề nghị USD 500**
- Tại thời điểm 3 tháng sau, thời gian còn lại đến khi đáo hạn là **6 tháng** ($\tau = 6/12 = 0.50$ năm) và lãi suất phi rủi ro mới là **$5\%$ EAR**.
- Giữ nguyên giá trị chưa làm tròn $K = 70.029966$, giá trị hiện tại của giá thanh toán $K$ chiết khấu theo lãi suất mới $5\%$ trong $0.50$ năm là:
  $$PV_t(K) = \frac{K}{(1 + r_t)^{0.50}} = \frac{70.029966}{(1.05)^{0.50}} = \frac{70.029966}{1.02469508} = \text{USD } 68.342249\text{ per share}$$
- Giá trị hiện tại trên **1 cổ phiếu** của vị thế Long Forward:
  $$v_t = S_t - PV_t(K) = 72.00 - 68.342249 = \text{USD } 3.657751 \quad (\approx \text{USD } 3.66\text{ per share})$$
- **Tổng giá trị hiện tại của toàn bộ hợp đồng (150 cổ phiếu):**
  $$V_t = 150 \times 3.657751 = \mathbf{\text{USD } 548.662621 \approx \text{USD } 548.66}$$
- **Đánh giá đề nghị tất toán (Assessment):**
  - Hợp đồng Long Forward đang là tài sản có giá trị thực tế **USD 548.66** thuộc về Alpha.
  - Đề nghị thanh toán **USD 500.00** của đối tác **thấp hơn giá trị hợp lý USD 48.66** ($548.66 - 500.00 = \text{USD } 48.66$).
  - Với giả định không có rủi ro vỡ nợ đối tác (*counterparty performs as agreed*), **Alpha nên TỪ CHỐI (Reject) lời đề nghị USD 500** (hoặc yêu cầu mức thanh toán tối thiểu USD 548.66 để tất toán).

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Công thức gộp 1 dòng tránh sai số làm tròn trung gian:**
  $$V_t = N \left[ S_t - \frac{S_0(1 + r_0)^{T}}{(1 + r_t)^{T - t}} \right] = 150 \left[ 72 - \frac{68(1.04)^{0.75}}{(1.05)^{0.50}} \right] = \text{USD } 548.66$$
- **Kiểm tra trực giác chiều biến động:** Giá cổ phiếu tăng ($68 \to 72$) **làm tăng** giá trị Long Forward; đồng thời lãi suất tăng ($4\% \to 5\%$) làm giảm $PV(K)$ nên **càng làm tăng thêm** giá trị Long Forward!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Dùng nhầm kỳ hạn còn lại hoặc lãi suất cũ ở câu b):** Sau 3 tháng của hợp đồng 9 tháng thì kỳ hạn còn lại là **6 tháng ($0.50$ năm)** chứ không phải $0.75$ hay $0.25$ năm; và phải chiết khấu bằng **lãi suất thị trường mới $5\%$**, KHÔNG dùng lại lãi suất lịch sử $4\%$!
- **Bẫy 2 (Quên nhân quy mô hợp đồng 150 cổ phiếu hoặc làm tròn sớm $K = 70.03$):** Dù $150 \times (72 - 70.03 / 1.05^{0.5}) = 548.66$ tình cờ cho cùng số làm tròn 2 chữ số ở bài này, đề thi quy định nghiêm ngặt *"Retain unrounded values during calculations"*. Luôn lưu biến `Ans` trên máy tính!

---

## Question 7 (Easy) — Sổ Cái Ký Quỹ Hợp Đồng Tương Lai Vị Thế Bán & Bẫy "Strictly Below"
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Beta shorts four futures contracts at USD 45.50 per unit. Each contract covers 250 units. Total initial margin is USD 8,000 and total maintenance margin is USD 6,000.
>
> A balance strictly below maintenance requires an immediate deposit restoring it to initial margin. There are no withdrawals, interest or fees. Beta closes the position at the day-4 settlement price.
>
> | Day | Settlement price per unit | Daily profit or loss | Balance before deposit | Additional deposit | Closing balance |
> |---|---:|---:|---:|---:|---:|
> | 1 | 46.30 | ? | ? | ? | ? |
> | 2 | ? | ? | 6,000 | ? | ? |
> | 3 | 48.20 | ? | ? | ? | ? |
> | 4 | 44.30 | ? | ? | ? | ? |
>
> a. Recover the missing price and complete the ledger. Account amounts are in USD.
>
> b. Calculate total external cash contributed, cash released on closing and total trading profit. Reconcile the three amounts.

**Tóm tắt thông số:**
- Vị thế: **SHORT (Bán)** $4 \text{ hợp đồng} \times 250 \text{ đơn vị} = \mathbf{1,000\text{ đơn vị}}$ tại giá mở vị thế $F_0 = \text{USD } 45.50$.
- Tổng ký quỹ ban đầu (*Initial Margin*): $\text{IM} = \text{USD } 8,000$ (đã nộp lúc mở vị thế tại Ngày 0).
- Tổng ký quỹ duy trì (*Maintenance Margin*): $\text{MM} = \text{USD } 6,000$.
- **Quy tắc gọi ký quỹ cực kỳ quan trọng:** Chỉ khi số dư **thấp hơn nghiêm ngặt (*strictly below*, tức $< \text{USD } 6,000$)** mới phải nộp tiền bổ sung (*Variation Margin*) để đưa số dư **quay về mức Initial Margin (USD 8,000)**!

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Khôi phục giá thanh toán Ngày 2 & Hoàn thiện Sổ cái Ký quỹ (Margin Ledger)**
Với vị thế **SHORT** tổng quy mô $Q = 1,000$ đơn vị, lãi/lỗ hàng ngày (*Daily P/L*) ở Ngày $t$ là:
$$\text{Daily P/L}_t = 1,000 \times (P_{t-1} - P_t) \quad (\text{giá TĂNG thì Short LỖ, giá GIẢM thì Short LÃI!})$$

- **Ngày 1 ($P_1 = 46.30$):**
  - $\text{Daily P/L}_1 = 1,000 \times (45.50 - 46.30) = \mathbf{-800}$ (lỗ USD 800).
  - $\text{Balance before deposit}_1 = 8,000 + (-800) = \mathbf{7,200}$.
  - Vì $7,200 \ge 6,000$, không bị margin call $\implies \text{Additional deposit}_1 = \mathbf{0}$; $\text{Closing balance}_1 = \mathbf{7,200}$.
- **Ngày 2 (Biết $\text{Balance before deposit}_2 = 6,000$):**
  - Ta có: $\text{Closing balance}_1 + \text{Daily P/L}_2 = \text{Balance before deposit}_2 \implies 7,200 + \text{Daily P/L}_2 = 6,000 \implies \text{Daily P/L}_2 = \mathbf{-1,200}$.
  - Khôi phục giá $P_2$:
    $$1,000 \times (46.30 - P_2) = -1,200 \implies 46.30 - P_2 = -1.20 \implies P_2 = 46.30 + 1.20 = \mathbf{\text{USD } 47.50}$$
  - **Điểm quyết định:** Số dư trước nộp thêm là $\text{USD } 6,000$, **bằng đúng** mức duy trì ($6,000$), tức **KHÔNG thấp hơn nghiêm ngặt (*NOT strictly below $6,000$*)**! Do đó:
    - $\text{Additional deposit}_2 = \mathbf{0}$.
    - $\text{Closing balance}_2 = \mathbf{6,000}$.
- **Ngày 3 ($P_3 = 48.20$):**
  - $\text{Daily P/L}_3 = 1,000 \times (47.50 - 48.20) = \mathbf{-700}$.
  - $\text{Balance before deposit}_3 = 6,000 + (-700) = \mathbf{5,300}$.
  - Vì $5,300 < 6,000$ (*strictly below maintenance!*), **Margin call kích hoạt**, yêu cầu nộp bù về mức **Initial Margin ($\text{USD } 8,000$)**:
    - $\text{Additional deposit}_3 = 8,000 - 5,300 = \mathbf{2,700}$.
    - $\text{Closing balance}_3 = \mathbf{8,000}$.
- **Ngày 4 ($P_4 = 44.30$, đóng vị thế):**
  - $\text{Daily P/L}_4 = 1,000 \times (48.20 - 44.30) = \mathbf{+3,900}$.
  - $\text{Balance before deposit}_4 = 8,000 + 3,900 = \mathbf{11,900}$.
  - $\text{Additional deposit}_4 = \mathbf{0}$; $\text{Closing balance}_4 = \mathbf{11,900}$.

**Bảng Sổ Cái Ký Quỹ Hoàn Chỉnh (Đơn vị: USD):**

| Day | Settlement price per unit | Daily profit or loss | Balance before deposit | Additional deposit | Closing balance |
|---|---:|---:|---:|---:|---:|
| *(Inception)* | *45.50* | *—* | *—* | *8,000 (Initial)* | *8,000* |
| **1** | **46.30** | **-800.00** | **7,200.00** | **0.00** | **7,200.00** |
| **2** | **47.50** | **-1,200.00** | **6,000.00** | **0.00** | **6,000.00** |
| **3** | **48.20** | **-700.00** | **5,300.00** | **2,700.00** | **8,000.00** |
| **4** | **44.30** | **+3,900.00** | **11,900.00** | **0.00** | **11,900.00** |

#### **b. Tổng tiền mặt nộp vào, Tiền giải phóng khi đóng vị thế, Lãi giao dịch & Đối chiếu**
1. **Tổng tiền mặt bên ngoài đã đóng góp (*Total external cash contributed*):**
   $$\text{Cash Contributed} = \text{Initial Margin} + \sum \text{Additional Deposits} = 8,000 + 2,700 = \mathbf{\text{USD } 10,700.00}$$
2. **Tiền mặt được giải phóng khi đóng vị thế cuối Ngày 4 (*Cash released on closing*):**
   $$\text{Cash Released} = \text{Closing Balance}_{\text{Day 4}} = \mathbf{\text{USD } 11,900.00}$$
3. **Tổng lợi nhuận giao dịch (*Total trading profit*):**
   - Tính từ tổng lãi/lỗ hàng ngày: $-800 - 1,200 - 700 + 3,900 = \mathbf{+\text{USD } 1,200.00}$.
   - Tính trực tiếp từ chênh lệch giá mở và giá đóng của vị thế Short: $1,000 \times (45.50 - 44.30) = 1,000 \times (+1.20) = \mathbf{+\text{USD } 1,200.00}$.
4. **Đối chiếu 3 đại lượng (*Reconciliation*):**
   $$\text{Cash Released} - \text{Total External Cash Contributed} = 11,900.00 - 10,700.00 = \mathbf{+\text{USD } 1,200.00} = \text{Total Trading Profit!}$$
   *(Vì không có rút tiền giữa kỳ, lãi tiền gửi hay phí giao dịch, số dư cuối kỳ đúng bằng tổng tiền mặt nhà đầu tư bỏ vào cộng với tổng lãi giao dịch ròng).*

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Mẹo kiểm tra chéo chống sai 100% ở cuối bài Futures Margin:**
  - Luôn tính độc lập $\text{Total Profit} = Q_{\text{signed}} \times (P_{\text{close}} - F_0)$ (với Short: $Q_{\text{signed}} = -1,000$).
  - Sau đó kiểm tra đẳng thức bất biến: $\text{Closing Balance Cuối Cùng} \equiv \text{Initial Margin} + \sum \text{Variation Margins} + \text{Total Profit}$. Nếu lệch dù chỉ 1 USD nghĩa là có dòng cộng trừ sai trên bảng!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy tử thần số 1 ("Strictly below maintenance" ở Ngày 2):** GS. Cayirli cố tình thiết kế số dư Ngày 2 chạm đúng **USD 6,000**! Ai đọc ẩu tưởng chạm $6,000$ là bị margin call nộp $2,000$ ở Ngày 2 sẽ làm sai dây chuyền sang toàn bộ Ngày 2, Ngày 3, tổng tiền nộp vào và số dư Ngày 4! Hãy gạch chân chữ **"strictly below"** ($< 6,000$ mới nộp!).
- **Bẫy tử thần số 2 (Nộp bù về Maintenance thay vì Initial Margin):** Khi Ngày 3 tụt xuống $5,300 < 6,000$, phải nộp bù lên **Initial Margin USD 8,000** (tức nộp **USD 2,700**), tuyệt đối KHÔNG phải nộp bù lên $6,000$ (USD 700)!
- **Bẫy tử thần số 3 (Ngược dấu Short vs Long):** Beta **shorts** hợp đồng $\rightarrow$ Giá tăng từ $45.50 \to 46.30 \to 47.50 \to 48.20$ là **LỖ**, giá giảm về $44.30$ là **LÃI**!

---

## Question 8 (Easy) — Thanh Toán Định Kỳ Hợp Đồng Hoán Đổi Lãi Suất (Plain-Vanilla Interest-Rate Swap)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Gamma pays 3.80% fixed and receives floating from Delta on a USD 18 million interest-rate swap. Payments are quarterly, with a year fraction of 0.25 for each period.
>
> The floating rates are annualized compounded rates measured over each quarter and known at its end. The first quarter's rate is 3.20%. At the second settlement, Gamma receives USD 18,000 net from Delta.
>
> a. Calculate the fixed leg, floating leg and net settlement for the first quarter. Identify the payer.
>
> b. Recover the second quarter's annualized floating rate.

**Tóm tắt thông số:**
- Vốn danh nghĩa (*Notional*): $N = \text{USD } 18,000,000$; kỳ thanh toán hàng quý $\Delta t = 0.25$.
- Vị thế của **Gamma**: Trả cố định $K = 3.80\%$/năm, nhận thả nổi $L_t$ từ Delta.
- Quý 1: $L_1 = 3.20\%$. Quý 2: Gamma **nhận ròng USD 18,000** từ Delta.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Thanh toán Quý 1 (Chân cố định, Chân thả nổi, Thanh toán ròng & Bên trả tiền)**
- **Chân cố định (*Fixed leg*) mỗi quý:**
  $$\text{Fixed Payment} = N \times K \times \Delta t = 18,000,000 \times 0.0380 \times 0.25 = \mathbf{\text{USD } 171,000.00}$$
- **Chân thả nổi (*Floating leg*) Quý 1 ($L_1 = 3.20\%$):**
  $$\text{Floating Payment}_{Q1} = N \times L_1 \times \Delta t = 18,000,000 \times 0.0320 \times 0.25 = \mathbf{\text{USD } 144,000.00}$$
- **Thanh toán ròng (*Net settlement*) Quý 1 & Xác định bên chi trả:**
  - Từ góc nhìn của Gamma: $\text{Net CF}_{\text{Gamma}, Q1} = 144,000 - 171,000 = -\text{USD } 27,000.00$.
  - Vậy khoản thanh toán ròng là **USD 27,000.00**, do **Gamma trả cho Delta** (*Gamma is the net payer; Delta receives USD 27,000*).

#### **b. Khôi phục lãi suất thả nổi thường niên hóa của Quý 2 ($L_2$)**
- Ở kỳ thanh toán thứ hai, Gamma **nhận ròng USD 18,000** từ Delta, nghĩa là chân thả nổi vượt chân cố định đúng USD 18,000:
  $$\text{Floating Payment}_{Q2} - 171,000 = +18,000 \implies \text{Floating Payment}_{Q2} = \text{USD } 189,000.00$$
- Chia cho cơ sở tính lãi quý ($N \times \Delta t = 18,000,000 \times 0.25 = \text{USD } 4,500,000$):
  $$L_2 = \frac{189,000}{18,000,000 \times 0.25} = \frac{189,000}{4,500,000} = 0.0420 = \mathbf{4.20\%}$$

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Công thức chênh lệch lãi suất trực tiếp (1 dòng 5 giây):**
  - Với người trả cố định - nhận thả nổi: $\text{Net CF} = (L_t - K) \times (N \Delta t)$, trong đó $N \Delta t = 18\text{m} \times 0.25 = \text{USD } 4.5\text{m}$ (tức mỗi $1\%$ chênh lệch lãi suất năm tương ứng USD 45,000/quý, hay $10\text{ bps} = \text{USD } 4,500$/quý!).
  - Quý 1: $(3.20\% - 3.80\%) \times 4.5\text{m} = -0.60\% \times 4.5\text{m} = -\text{USD } 27,000$ (Gamma trả).
  - Quý 2: $L_2 - 3.80\% = \frac{+18,000}{4,500,000} = +0.40\% \implies L_2 = 3.80\% + 0.40\% = \mathbf{4.20\%}$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy quên nhân $\Delta t = 0.25$:** Lãi suất swap luôn yết theo **năm (*annualized*)**, nhưng dòng tiền thanh toán theo **quý (*quarterly*)**. Quên nhân $0.25$ ở câu a sẽ phóng đại dòng tiền gấp 4 lần; quên chia $0.25$ ở câu b sẽ ra $L_2 = 1.05\%$ (lãi suất quý chưa thường niên hóa) thay vì đáp án đúng **$4.20\%$**!

---

## Question 9 (Average) — Hợp Đồng Kỳ Hạn Chỉ Số Cổ Phiếu Với Tỷ Suất Cổ Tức Từng Khúc
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> The Epsilon index stands at 3,200. A nine-month forward is quoted at 3,248.36 index points. The risk-free rate is 4.80% per year, continuously compounded.
>
> The continuous dividend yield is 1.20% per year for the first three months and an unknown constant rate for the remaining six months. Treat the quoted forward as consistent with these known dividend yields.
>
> a. Recover the dividend yield for the final six months.
>
> b. Immediately after a long forward is entered at the quoted price, new information raises only the final six months' dividend yield by one percentage point. No time passes, and spot and interest rates remain unchanged. Calculate the new forward quotation. Does the change benefit the holder of the existing long contract?

**Tóm tắt thông số:**
- Chỉ số giao ngay $S_0 = 3,200$; kỳ hạn $T = 9/12 = 0.75$ năm; giá kỳ hạn niêm yết $F_0 = 3,248.36$.
- Lãi suất phi rủi ro ghép lãi liên tục: $r = 4.80\%$/năm.
- Tỷ suất cổ tức liên tục (*continuous dividend yield*): $q_1 = 1.20\%$/năm trong 3 tháng đầu ($t_1 = 0.25$ năm); $q_2$ chưa biết trong 6 tháng cuối ($t_2 = 0.50$ năm).

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Khôi phục tỷ suất cổ tức liên tục trong 6 tháng cuối ($q_2$)**
Với lãi suất và tỷ suất cổ tức ghép lãi liên tục thay đổi từng khúc thời gian, công thức định giá kỳ hạn chỉ số là:
$$F_0 = S_0 \exp\left(r T - q_1 t_1 - q_2 t_2\right)$$
Thay các thông số vào phương trình:
$$3,248.36 = 3,200 \exp\left(0.048 \times 0.75 - 0.012 \times 0.25 - q_2 \times 0.50\right)$$
Lấy logarit tự nhiên hai vế:
$$\ln\left(\frac{3,248.36}{3,200}\right) = 0.0360 - 0.0030 - 0.50 q_2 = 0.0330 - 0.50 q_2$$
Tính chính xác:
$$\ln(1.0151125) = 0.0149994446 \implies 0.50 q_2 = 0.0330 - 0.0149994446 = 0.0180005554$$
$$\implies q_2 = \frac{0.0180005554}{0.50} = 0.03600111 = \mathbf{3.60\%\text{ per year}}$$

#### **b. Giá kỳ hạn mới khi $q_2$ tăng thêm 1 điểm phần trăm & Tác động lên người giữ Long Forward cũ**
- Khi $q_2$ tăng thêm $1\%$ (tức $\Delta q_2 = +0.01$, lên $q_2^{\text{new}} = 4.600111\% \approx 4.60\%$) trong khi $S_0 = 3,200$, $r = 4.80\%$, $q_1 = 1.20\%$ và thời gian còn lại $T = 0.75$ không đổi:
  $$F_{\text{new}} = 3,200 \exp\left(0.0330 - 0.50 \times 0.04600111\right) = F_0 \cdot e^{-\Delta q_2 \cdot t_2} = 3,248.36 \times e^{-0.01 \times 0.50}$$
  $$F_{\text{new}} = 3,248.36 \times e^{-0.005} = 3,248.36 \times 0.99501248 = \mathbf{3,232.158737 \approx 3,232.16\text{ index points}}$$
- **Sự thay đổi này có lợi cho người đang nắm hợp đồng Long Forward cũ không? KHÔNG — nó GÂY THIỆT HẠI (does NOT benefit; it hurts the existing long holder)!**
  - **Chứng minh bằng định giá:** Hợp đồng Long Forward cũ đã khóa cứng giá mua tại $K = 3,248.36$, trong khi giá kỳ hạn thị trường mới rơi xuống $F_{\text{new}} = 3,232.16$. Giá trị tức thời của hợp đồng Long cũ trở thành âm:
    $$V_{\text{long}} = (F_{\text{new}} - K) e^{-r T} = (3,232.158737 - 3,248.36) e^{-0.048 \times 0.75} = \mathbf{-15.6284 \approx -15.63\text{ index points}} < 0$$
  - **Giải thích kinh tế trực giác:** Người giữ vị thế Long Forward **không được nhận cổ tức** trả trong kỳ trước đáo hạn. Khi mức giá giao ngay hiện tại $S_0 = 3,200$ đứng yên mà cổ tức tương lai tăng lên, một phần lớn hơn của giá trị hiện tại $3,200$ sẽ rơi rụng ra ngoài qua các đợt chia cổ tức trước đáo hạn (làm mức chỉ số kỳ vọng lúc đáo hạn thấp hơn), trong khi người giữ Long Forward cũ vẫn phải mua chỉ số ở mức giá cam kết cao cũ là $3,248.36$!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Tuyệt chiêu Tỷ số Hàm Mũ cho câu b (không cần đụng lại $S_0$, $r$, $q_1$ và miễn nhiễm 100% sai số làm tròn!):**
  $$F_{\text{new}} = F_{\text{old}} \cdot e^{-\Delta q_2 \cdot t_2} = 3,248.36 \times e^{-0.01 \times 0.50} = 3,232.1587 \approx 3,232.16$$
  Chỉ đúng 1 phép nhân, ra kết quả chính xác tuyệt đối tới chữ số thập phân thứ 6!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Lấy trung bình cộng giản đơn tỷ suất cổ tức mà sai trọng số thời gian):** Tổng cổ tức tích lũy trong mũ là $\int_0^T q(t)dt = q_1(0.25) + q_2(0.50)$. Nếu nhân nhầm $q_2$ với $0.75$ thay vì $0.50$ ở câu b ($e^{-0.01 \times 0.75}$) sẽ ra sai kết quả!
- **Bẫy 2 (Tưởng cổ tức tăng là tin tốt cho Long Forward):** Cổ tức tăng là dòng tiền về túi **cổ đông nắm giữ cổ phiếu giao ngay**, còn đối với **Long Forward** (chưa sở hữu cổ phiếu trước ngày đáo hạn) khi $S_0$ giữ nguyên thì cổ tức tăng luôn làm **giảm** giá kỳ hạn và làm **lỗ** vị thế Long Forward hiện hữu!

---

## Question 10 (Average) — Lợi Tức Tiện Ích Hàng Hóa & Bẫy Arbitrage Một Chiều (Convenience Yield)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Zeta observes a commodity spot price of USD 96 per unit and a six-month forward price of USD 94.20. The continuously compounded risk-free rate is 4% per year.
>
> Use net convenience yield, meaning the inventory benefit less storage costs. There is no cash income. Storage costs are nonnegative. The commodity cannot be borrowed or sold short, and existing owners must retain their inventory for production.
>
> a. Calculate the implied annual net convenience yield.
>
> b. In an alternative scenario, the net convenience yield falls by two percentage points while spot, the interest rate and maturity remain unchanged. Calculate the new forward price.
>
> c. Eta proposes borrowing cash, buying and storing one unit, and selling it forward at the original USD 94.20 quotation. Eta calls the trade an arbitrage because the forward is below the financing-only benchmark. Assess the proposal and whether reversing the trade resolves the problem.

**Tóm tắt thông số:**
- Hàng hóa có $S_0 = \text{USD } 96$/đơn vị; kỳ hạn $T = 0.50$ năm; giá kỳ hạn $F_0 = \text{USD } 94.20$ (*backwardation*!).
- Lãi suất phi rủi ro liên tục: $r = 4\%$/năm.
- Lợi tức tiện ích ròng (*net convenience yield* $y = \text{inventory benefit} - \text{storage cost rate}$); chi phí lưu kho không âm.
- Ràng buộc vật chất: **Không thể vay hay bán khống hàng hóa**, và những người đang nắm giữ tồn kho **bắt buộc phải giữ hàng phục vụ sản xuất**.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Lợi tức tiện ích ròng hàm ý hàng năm ($y$)**
Công thức giá kỳ hạn hàng hóa theo lợi tức tiện ích ròng liên tục $y$:
$$F_0 = S_0 e^{(r - y)T} \implies 94.20 = 96 e^{(0.04 - y)(0.50)}$$
Giải tìm $y$:
$$0.04 - y = \frac{1}{0.50} \ln\left(\frac{94.20}{96}\right) = 2 \times (-0.018928011) = -0.037856022$$
$$\implies y = 0.04 + 0.037856022 = 0.07785602 = \mathbf{7.79\%\text{ per year}}$$

#### **b. Giá kỳ hạn mới khi lợi tức tiện ích ròng giảm 2 điểm phần trăm**
Khi $y$ giảm $2\%$ ($\Delta y = -0.02$, xuống $y_{\text{new}} = 5.785602\% \approx 5.79\%$) với $S_0 = 96$, $r = 4\%$, $T = 0.50$ giữ nguyên:
$$F_{\text{new}} = 96 e^{(0.04 - 0.05785602)(0.50)} = F_0 \cdot e^{-(-0.02)(0.50)} = 94.20 \times e^{+0.01} = \mathbf{\text{USD } 95.146726 \approx \text{USD } 95.15\text{ per unit}}$$

#### **c. Đánh giá đề xuất Cash-and-Carry của Eta & Liệu đảo chiều giao dịch có giải quyết được không?**
1. **Đánh giá đề xuất của Eta (Cash-and-Carry: Vay tiền mua hàng lưu kho + Bán kỳ hạn tại USD 94.20):**
   - Đề xuất của Eta **SAI HOÀN TOÀN CHIỀU KINH DOANH CHÊNH LỆCH GIÁ** và chắc chắn tạo ra **THUA LỖ (guaranteed loss)**!
   - Cụ thể: Vay USD 96 ở lãi suất $4\%$ liên tục trong 6 tháng buộc Eta phải hoàn trả gốc + lãi là:
     $$96 e^{0.04 \times 0.50} = 96 e^{0.02} = \text{USD } 97.939329 \approx \mathbf{\text{USD } 97.94}$$
     chưa kể phải gánh thêm **chi phí lưu kho không âm** (*nonnegative storage costs*) — trong khi nhà kinh doanh tài chính mua hàng cất kho không hề thu được dòng tiền mặt nào từ lợi ích vận hành dây chuyền sản xuất!
   - Đến hạn 6 tháng, hợp đồng bán kỳ hạn chỉ mang về cho Eta **USD 94.20**, dẫn đến khoản **lỗ chắc chắn tối thiểu $97.94 - 94.20 = \text{USD } 3.74$/đơn vị** (cộng thêm toàn bộ chi phí lưu kho). *Cash-and-carry* chỉ sinh lời khi giá kỳ hạn **cao hơn** mức chuẩn tài trợ + lưu kho, chứ không phải khi thấp hơn!
2. **Đảo chiều giao dịch (Reverse Cash-and-Carry) có giải quyết được vấn đề không? KHÔNG!**
   - Giao dịch đảo chiều đòi hỏi phải **mua kỳ hạn giá rẻ USD 94.20** đồng thời **bán khống hàng hóa giao ngay ở USD 96** (hoặc rút hàng tồn kho đem bán lấy USD 96 gửi tiết kiệm thu USD 97.94).
   - Tuy nhiên, chiến lược này **bất khả thi (blocked / infeasible)** do hai rào cản thực tế của hàng hóa tiêu dùng/sản xuất:
     - Nhà đầu tư bên ngoài **không thể vay hay bán khống hàng hóa vật chất** (*cannot be borrowed or sold short*).
     - Các doanh nghiệp đang sở hữu hàng tồn kho **phải giữ hàng để duy trì sản xuất** (*must retain their inventory for production*); nếu đem bán tồn kho hiện tại và chờ nhận hàng sau 6 tháng qua hợp đồng kỳ hạn, họ sẽ đánh mất chính **lợi ích tiện ích sản xuất (*convenience yield*)** (nguy cơ đứt gãy dây chuyền sản xuất), vốn có giá trị kinh tế bù đắp cho mức chênh lệch giá!
   - Đây chính là lý do đối với hàng hóa có hạn chế bán khống, bất đẳng thức không-arbitrage chỉ chặn trên: $F_0 \le S_0 e^{(r + u)T}$, còn $F_0$ hoàn toàn có thể nằm thấp hơn $S_0 e^{rT}$ mà không tạo ra cơ hội arbitrage nào!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Nhớ đối xứng hoàn hảo: **Net convenience yield $y$ đóng vai trò toán học y hệt tỷ suất cổ tức liên tục $q$**:
  $$F_0 = S_0 e^{(r - y)T} \iff y = r - \frac{1}{T}\ln\left(\frac{F_0}{S_0}\right)$$
- Khi $\Delta y = -2\%$, giá kỳ hạn nhân ngay hệ số $e^{-\Delta y \cdot T} = e^{+0.02 \times 0.5} = e^{0.01}$: $94.20 \times e^{0.01} = \text{USD } 95.15$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Nhầm dấu của $y$ trong công thức mũ):** Lợi tức tiện ích là lợi ích thuộc về người giữ hàng vật chất (giống cổ tức), nên mang dấu **TRỪ** trong $(r - y)T$ (còn chi phí lưu kho thuần $u$ mới mang dấu cộng $(r + u)T$). Kiểm tra nhanh: vì $F_0 = 94.20 < S_0 = 96$ dù $r = 4\% > 0$, bắt buộc $y$ phải dương và lớn hơn $4\%$ ($7.79\% > 4\%$).
- **Bẫy 2 (Trả lời thiếu vế 2 của câu c):** Câu c hỏi rõ *"and whether reversing the trade resolves the problem"*. Bắt buộc phải giải thích cả hai chiều: chiều của Eta thì lỗ chắc chắn ($94.20 < 97.94$), còn chiều ngược lại thì bị khóa bởi cấm bán khống và nhu cầu giữ tồn kho sản xuất!

---

## Question 11 (Average) — Phòng Hộ Cho Nhà Sản Xuất & Bẫy Thanh Khoản Ký Quỹ (Tailing / Liquidity Risk)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Omicron will sell a fixed quantity of its output in four months. Its sales revenue arrives only on delivery. A futures contract exactly matches the quantity, product and delivery date. A bank also offers a forward at the same initial delivery price, with no interim collateral or settlement payments.
>
> Omicron can post the futures initial margin but cannot finance any additional margin calls. Assume deterministic interest rates and no counterparty default.
>
> Omicron proposes a long futures position and argues, "The hedge removes the price risk, so the eventual sales proceeds will cover any margin calls."
>
> a. Assess the hedge direction and the funding argument. Explain what happens if the product price rises before delivery.
>
> b. Which contract better fits Omicron's constraint, and in which direction should it trade?

**Tóm tắt thông số:**
- Omicron là **nhà sản xuất sẽ BÁN** một lượng sản phẩm cố định sau 4 tháng; tiền bán hàng **chỉ thu về lúc giao hàng ở tháng thứ 4**.
- Lựa chọn công cụ: (1) Hợp đồng **Futures** khớp hoàn hảo sản phẩm, khối lượng, ngày giao hàng; hoặc (2) Hợp đồng **Forward** với ngân hàng ở cùng mức giá kỳ hạn ban đầu, **không yêu cầu tài sản thế chấp hay thanh toán giữa kỳ**, không rủi ro vỡ nợ, lãi suất tất định.
- Ràng buộc thanh khoản: Đủ tiền nộp *Initial Margin* của Futures nhưng **KHÔNG THỂ tài trợ bất kỳ khoản gọi ký quỹ bổ sung (*additional margin calls*) nào**.
- Đề xuất sai của Omicron: Mở vị thế **LONG futures** và lập luận rằng tiền bán hàng cuối kỳ sẽ bù đắp mọi margin calls.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Đánh giá chiều phòng hộ, lập luận nguồn tiền & Kịch bản khi giá tăng trước ngày giao hàng**
1. **Đánh giá chiều phòng hộ (Hedge direction is WRONG):**
   - Vì Omicron sản xuất và sẽ **bán** hàng hóa sau 4 tháng, vị thế kinh doanh tự nhiên của Omicron là **thuận chiều giá lên (*naturally LONG the commodity*)**: Omicron bị thiệt hại khi giá hàng hóa **giảm** và hưởng lợi khi giá tăng.
   - Đề xuất vào vị thế **Long futures** là **NGƯỢC CHIỀU PHÒNG HỘ**: thay vì triệt tiêu rủi ro giá, Long futures **nhân đôi mức độ phơi nhiễm rủi ro (*doubles price exposure*)** (nếu giá giảm, Omicron vừa thất thu doanh số bán hàng vật chất vừa lỗ nặng trên hợp đồng futures!). Để khóa giá bán đầu ra, chiều phòng hộ đúng bắt buộc phải là **SHORT (bán)**.
2. **Đánh giá lập luận tài trợ ký quỹ (Funding argument is FLAWED — Cash-flow timing mismatch):**
   - Hợp đồng tương lai (*futures*) thực hiện **hạch toán theo thị trường và thanh toán tiền mặt hàng ngày (*daily mark-to-market settlement*)**, trong khi doanh thu bán hàng vật chất của Omicron **chỉ về tài khoản sau 4 tháng khi giao hàng**.
   - Do sự **lệch pha thời điểm dòng tiền (*cash-flow timing mismatch*)**, doanh thu tương lai ở tháng thứ 4 **không thể dùng để nộp các lệnh gọi ký quỹ tiền mặt tức thời (*immediate cash variation margin calls*)** phát sinh ở tháng 1, 2 hoặc 3! Vì Omicron không có khả năng huy động vốn nộp thêm ký quỹ, ngay khi bị gọi ký quỹ, sàn giao dịch sẽ **thanh lý cưỡng bức (*force-liquidate*)** vị thế futures trước hạn, phá vỡ hoàn toàn chiến lược phòng hộ (đúng kiểu thảm họa Metallgesellschaft!).
3. **Chuyện gì xảy ra nếu giá sản phẩm TĂNG trước ngày giao hàng?**
   - **Nếu thực hiện đúng chiều phòng hộ là SHORT futures:** Khi giá sản phẩm **tăng mạnh** trước ngày giao hàng, giá trị lô hàng vật chất của Omicron tăng lên trên sổ sách nhưng **chưa tạo ra đồng tiền mặt nào cho đến tháng thứ 4**; trái lại, vị thế **Short futures lập tức chịu lỗ tiền mặt hàng ngày**. Khi khoản lỗ lũy kế đẩy số dư ký quỹ xuống dưới mức duy trì, Omicron bị **gọi ký quỹ bổ sung (*margin call*) ngay lập tức** nhưng không có tiền nộp $\rightarrow$ vị thế phòng hộ bị đóng cưỡng bức giữa chừng, đẩy Omicron trở lại tình trạng phơi nhiễm rủi ro nếu sau đó giá quay đầu sụt giảm!
   - *(Lưu ý bổ sung: Còn dưới đề xuất sai lầm **Long futures** của Omicron, nếu giá tăng thì vị thế Long futures có lãi hàng ngày nhưng đó là đầu cơ kép chứ không phải phòng hộ; ngược lại chỉ cần giá giảm trước khi giao hàng, Omicron lập tức vỡ trận vì vừa dính margin call không thể trả vừa mất giá bán hàng cuối kỳ!).*

#### **b. Hợp đồng phù hợp nhất & Chiều giao dịch chuẩn**
- **Công cụ tối ưu:** Hợp đồng **Kỳ hạn với ngân hàng (Forward contract)**.
- **Chiều giao dịch:** Vị thế **BÁN KỲ HẠN (SHORT forward)**.
- **Lý do kinh tế chặt chẽ:**
  1. Vị thế **Short** khóa cố định mức giá bán đầu ra sau 4 tháng, triệt tiêu hoàn toàn rủi ro giá giảm đối với lô hàng sẽ xuất bán.
  2. Hợp đồng **Forward** chỉ thanh toán **một lần duy nhất tại ngày đáo hạn (tháng thứ 4)** và không có yêu cầu ký quỹ biến đổi hàng ngày (*no interim collateral or MTM settlements*), khớp hoàn hảo với thời điểm Omicron thu tiền bán hàng vật chất nên loại bỏ 100% rủi ro đứt gãy thanh khoản giữa kỳ (đồng thời đề cho lãi suất tất định, cùng giá giao nhận ban đầu và không có rủi ro vỡ nợ đối tác nên Forward không hề chịu bất lợi nào so với Futures).

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Quy tắc Bàn Tay Phải cho Hedging:**
  - **Sẽ BÁN hàng trong tương lai** (*Producer / Inventory holder*) $=$ Đang **Long tự nhiên** $\implies$ Phải **SHORT** phái sinh $\implies$ Sợ giá tăng giữa kỳ gây **Margin Call** trên Futures!
  - **Sẽ MUA nguyên liệu trong tương lai** (*End-user / Airline buying jet fuel*) $=$ Đang **Short tự nhiên** $\implies$ Phải **LONG** phái sinh $\implies$ Sợ giá giảm giữa kỳ gây **Margin Call** trên Futures!
  - Thiếu hạn mức tín dụng/tiền mặt chịu Margin Call hàng ngày $\implies$ Chọn **Forward** thay vì **Futures**!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy bỏ sót một trong hai lỗi của Omicron ở câu a:** Omicron mắc **HAI lỗi độc lập** cùng lúc: (1) Sai chiều phòng hộ (*Long* thay vì *Short*), và (2) Sai cơ chế dòng tiền (*tưởng doanh thu tháng 4 trả được daily margin call tháng 1–3*). Đặc biệt khi phân tích câu *"Explain what happens if the product price rises before delivery"*, nhất định phải chỉ rõ: với vị thế phòng hộ đúng (**Short futures**), chính kịch bản **giá tăng** (vốn là tin tốt cho hàng vật chất!) lại là kịch bản gây **thua lỗ tiền mặt tức thời và kích hoạt margin call làm gãy vị thế phòng hộ**!

---

## Question 12 (Average) — Hoán Đổi Tiền Tệ Cố Định - Cố Định & Rủi Ro Tỷ Giá Dư Thừa (Currency Swap)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Pi needs EUR funding for three years. It borrows USD 9.6 million at 4.50% annual interest, paid at each year-end, with principal repaid at the end of year 3, and enters a fixed-for-fixed currency swap with Rho.
>
> - At inception, Pi exchanges the USD 9.6 million for EUR at 1.20 USD per EUR.
> - Under the swap, Pi receives USD 432,000 and pays EUR 280,000 at each year-end.
> - The original principals are exchanged back at the end of year 3, in addition to that year's interest. No upfront fee applies.
>
> a. Recover the EUR notional and each swap leg's annual fixed rate.
>
> b. Show Pi's swap cash flows and the combined loan-plus-swap cash flows in each currency at inception, in years 1-2 and in year 3. Determine the resulting annual EUR borrowing cost.
>
> c. If the USD loan instead charges 5.25%, with all swap terms unchanged, quantify the remaining annual obligation. Is the overall funding still entirely fixed in EUR?

**Tóm tắt thông số:**
- Khoản vay gốc của Pi: Vay $\text{USD } 9,600,000$ trong 3 năm, lãi suất cố định $4.50\%$/năm trả cuối mỗi năm ($\text{USD } 432,000$/năm), trả gốc cuối năm 3.
- Hoán đổi tiền tệ cố định-cố định (*Fixed-for-fixed currency swap*) với Rho:
  - Lúc khởi tạo ($t = 0$): Đổi USD 9.6 triệu lấy EUR theo tỷ giá $1.20\text{ USD/EUR}$.
  - Cuối mỗi năm 1, 2, 3: Pi **nhận USD 432,000** và **trả EUR 280,000**.
  - Cuối năm 3: Hoán đổi trả lại vốn gốc ban đầu của hai đồng tiền.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Vốn danh nghĩa EUR (EUR Notional) & Lãi suất cố định hàng năm của mỗi chân Swap**
1. **EUR Notional:**
   $$N_{\text{EUR}} = \frac{\text{USD } 9,600,000}{1.20\text{ USD/EUR}} = \mathbf{\text{EUR } 8,000,000} \quad (\text{EUR } 8.00\text{ million})$$
2. **Lãi suất cố định năm của chân USD (*USD swap fixed rate*):**
   $$r_{\text{swap, USD}} = \frac{\text{USD } 432,000}{\text{USD } 9,600,000} = 0.0450 = \mathbf{4.50\%\text{ per year}}$$
3. **Lãi suất cố định năm của chân EUR (*EUR swap fixed rate*):**
   $$r_{\text{swap, EUR}} = \frac{\text{EUR } 280,000}{\text{EUR } 8,000,000} = 0.0350 = \mathbf{3.50\%\text{ per year}}$$

#### **b. Bảng dòng tiền Swap, Dòng tiền Kết hợp (Loan + Swap) & Chi phí vay EUR hiệu dụng**

| Thời điểm | Hạng mục | Dòng tiền USD | Dòng tiền EUR |
|---|---|---:|---:|
| **Khởi tạo ($t = 0$)** | Khoản vay USD (*USD Loan*) | $+9,600,000$ | $0$ |
| | Hợp đồng Swap (*Currency Swap*) | $-9,600,000$ | $+8,000,000$ |
| | **Kết hợp (Loan + Swap tại $t = 0$)** | **USD 0** | **+EUR 8,000,000** |
| **Cuối Năm 1 & Năm 2** *(mỗi năm)* | Khoản vay USD (trả lãi $4.50\%$) | $-432,000$ | $0$ |
| | Hợp đồng Swap (nhận lãi USD, trả lãi EUR) | $+432,000$ | $-280,000$ |
| | **Kết hợp (mỗi năm ở Năm 1 & Năm 2)** | **USD 0** | **-EUR 280,000** |
| **Cuối Năm 3** *(lãi + gốc)* | Khoản vay USD (trả lãi $432\text{k}$ + gốc $9.6\text{m}$) | $-10,032,000$ | $0$ |
| | Hợp đồng Swap (nhận USD $10,032\text{k}$, trả EUR $8,280\text{k}$) | $+10,032,000$ | $-8,280,000$ |
| | **Kết hợp (Cuối Năm 3)** | **USD 0** | **-EUR 8,280,000** |

- **Chi phí vay EUR hàng năm sau kết hợp:** Mọi dòng tiền bằng USD triệt tiêu về **USD 0** ở tất cả các thời điểm! Cấu trúc tổng hợp biến thành một khoản vay EUR thuần túy: nhận ròng $+\text{EUR } 8,000,000$ tại $t = 0$, trả lãi $\text{EUR } 280,000$ cuối mỗi năm trong 3 năm, và hoàn trả gốc $\text{EUR } 8,000,000$ cuối năm 3. Do đó chi phí đi vay EUR cố định hàng năm là:
  $$\text{Effective Annual EUR Borrowing Cost} = \frac{280,000}{8,000,000} = \mathbf{3.50\%\text{ per year}}$$

#### **c. Khi khoản vay USD chịu lãi suất 5.25%/năm (các điều khoản Swap giữ nguyên)**
- Tiền lãi vay USD phải trả cuối mỗi năm tăng lên:
  $$9,600,000 \times 5.25\% = \text{USD } 504,000\text{/năm}$$
- Hợp đồng Swap vẫn chỉ trả cho Pi $+\text{USD } 432,000$/năm, để lại phần chênh lệch thiếu hụt bằng USD mỗi năm là:
  $$504,000 - 432,000 = 9,600,000 \times (5.25\% - 4.50\%) = \mathbf{\text{USD } 72,000\text{/năm}}$$
- **Nghĩa vụ thanh toán hàng năm còn lại của Pi:**
  - Cuối mỗi năm 1, 2, 3 (phần chi phí lãi): Pi phải trả **EUR 280,000 CỘNG VỚI USD 72,000** mỗi năm *(và vào cuối năm 3 trả thêm vốn gốc EUR 8,000,000; vốn gốc USD 9,600,000 vẫn được Swap đối ứng triệt tiêu hết)*.
- **Tổng chi phí huy động vốn có còn cố định hoàn toàn bằng EUR không? KHÔNG (No)!**
  - Vì Pi vẫn phải chi trả một khoản cố định bằng ngoại tệ là **USD 72,000 vào cuối mỗi năm**, số tiền EUR thực tế cần bỏ ra để mua USD 72,000 đó sẽ biến thiên theo tỷ giá giao ngay tương lai tại cuối năm 1, năm 2 và năm 3 (**vẫn còn rủi ro tỷ giá hối đoái dư thừa — residual FX risk**)!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Kiểm tra hướng trao đổi vốn gốc trong Currency Swap (rất nhiều người nhầm dấu $t=0$ và $t=T$!):**
  - Lúc đầu kỳ ($t = 0$): Vừa đi vay được USD trên thị trường ($+\text{USD}$), cần dùng EUR nên đem **nộp USD cho Swap** ($-\text{USD}$) để **nhận EUR về** ($+\text{EUR}$).
  - Trong kỳ & cuối kỳ ($t = 1..T$): Cần USD để trả nợ ngân hàng nên **Swap trả USD cho mình** ($+\text{USD}$), còn mình **trả lãi + gốc EUR cho Swap** ($-\text{EUR}$)!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Nhân thay vì chia tỷ giá khi đổi sang EUR):** Tỷ giá yết là $1.20\text{ USD per EUR}$ ($1\text{ EUR} = 1.20\text{ USD}$). Đổi USD 9.6 triệu sang EUR phải **CHIA** cho $1.20$ ra **EUR 8.0 triệu** (nếu nhân $9.6 \times 1.20 = 11.52$ triệu là sai ngay từ dòng đầu tiên!).
- **Bẫy 2 (Quên cộng vốn gốc trao đổi lại ở Năm 3):** Khác với Interest-Rate Swap (không trao đổi vốn gốc vì cùng 1 đồng tiền), **Currency Swap BẮT BUỘC trao đổi lại vốn gốc ở ngày đáo hạn** ($-\text{EUR } 8,000,000$ và $+\text{USD } 9,600,000$ cộng thêm tiền lãi năm 3)!

---

## Question 13 (Average) — Hoán Đổi Lãi Suất Khóa Lãi Vay & Rủi Ro Cơ Sở (Basis Risk)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Sigma has a USD 32 million floating-rate loan charging $L+0.85\%$. A dealer quotes a zero-upfront swap exchanging $L$ for a fixed annual rate $K$. Sigma states that the appropriate side of this swap would make its combined annual borrowing cost 4.50%.
>
> Loan and swap payments are quarterly with a year fraction of 0.25. Notionals, maturities and payment dates match. The floating rates are annualized three-month rates set at the start of each quarter and paid at its end.
>
> a. Determine Sigma's required swap direction and recover $K$.
>
> b. Consider an otherwise identical loan linked to $M+0.85\%$, while the swap still references $L$ and retains the same $K$. Calculate Sigma's combined annual payment rate and dollar payment for each quarter below. Is the borrowing cost still fixed?
>
> | Quarter | $M$ | $L$ |
> |---|---:|---:|
> | 1 | 3.40% | 3.10% |
> | 2 | 2.70% | 3.00% |

**Tóm tắt thông số:**
- Vốn vay & Notional Swap: $N = \text{USD } 32,000,000$; thanh toán hàng quý $\Delta t = 0.25$.
- Khoản vay gốc: trả thả nổi $L + 0.85\%$. Muốn khóa tổng chi phí đi vay cố định ở $4.50\%$/năm qua Swap trao đổi $L$ lấy $K$.
- Câu b: Khoản vay đổi sang tham chiếu chỉ số thả nổi $M + 0.85\%$, trong khi Swap vẫn tham chiếu $L$ và giữ nguyên $K$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Chiều giao dịch Swap cần thiết của Sigma & Lãi suất cố định $K$**
- **Chiều Swap:** Vì Sigma đang có nghĩa vụ trả lãi thả nổi $L + 0.85\%$ trên khoản vay, để triệt tiêu biến số $L$, Sigma phải tham gia Swap ở vị thế **Trả cố định $K$ và Nhận thả nổi $L$ (Pay fixed $K$, receive floating $L$)**.
- **Khôi phục $K$:** Tổng lãi suất chi trả ròng hàng năm của Sigma là:
  $$\text{Combined Rate} = \underbrace{(L + 0.85\%)}_{\text{Trả ngân hàng}} + \underbrace{K}_{\text{Trả cố định Swap}} - \underbrace{L}_{\text{Nhận thả nổi Swap}} = K + 0.85\%$$
  Đặt bằng mức mục tiêu $4.50\%$:
  $$K + 0.85\% = 4.50\% \implies K = 4.50\% - 0.85\% = \mathbf{3.65\%}$$

#### **b. Khi khoản vay neo theo $M + 0.85\%$ còn Swap vẫn neo theo $L$ (với $K = 3.65\%$)**
Tổng lãi suất thanh toán thường niên hóa kết hợp của Sigma trong mỗi quý là:
$$r_{\text{combined}} = (M + 0.85\%) + 3.65\% - L = \mathbf{4.50\% + (M - L)}$$
Số tiền USD thực trả mỗi quý với $N \Delta t = 32,000,000 \times 0.25 = \text{USD } 8,000,000$:
- **Quý 1 ($M_1 = 3.40\%, L_1 = 3.10\% \implies M_1 - L_1 = +0.30\%$):**
  - Lãi suất thanh toán kết hợp năm: $r_{\text{combined}, Q1} = 4.50\% + (3.40\% - 3.10\%) = \mathbf{4.80\%}$ *(kiểm lại: $3.40\% + 0.85\% + 3.65\% - 3.10\% = 4.80\%$)*.
  - Số tiền thanh toán Quý 1: $\text{Payment}_{Q1} = 32,000,000 \times 0.0480 \times 0.25 = \mathbf{\text{USD } 384,000.00}$.
- **Quý 2 ($M_2 = 2.70\%, L_2 = 3.00\% \implies M_2 - L_2 = -0.30\%$):**
  - Lãi suất thanh toán kết hợp năm: $r_{\text{combined}, Q2} = 4.50\% + (2.70\% - 3.00\%) = \mathbf{4.20\%}$ *(kiểm lại: $2.70\% + 0.85\% + 3.65\% - 3.00\% = 4.20\%$)*.
  - Số tiền thanh toán Quý 2: $\text{Payment}_{Q2} = 32,000,000 \times 0.0420 \times 0.25 = \mathbf{\text{USD } 336,000.00}$.
- **Chi phí vay có còn cố định không? KHÔNG (No)!**
  - Do lãi suất thả nổi trên khoản vay ($M$) và lãi suất thả nổi tham chiếu trên hợp đồng Swap ($L$) không trùng nhau, chúng không triệt tiêu hoàn toàn mà để lại **Rủi ro cơ sở (*Basis Risk*)** bằng đúng chênh lệch $(M - L)$ biến động qua từng quý!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Viết thẳng công thức thu gọn **1 dòng** cho mọi bài *Imperfect Swap Hedge / Basis Risk*:
  $$r_{\text{net}} = (K + \text{Loan Spread}) + (\text{Loan Index} - \text{Swap Index}) = 4.50\% + (M - L)$$
  Nhìn bảng đọc kết quả trong 3 giây: $Q1: 4.50\% + 0.30\% = 4.80\%$; $Q2: 4.50\% - 0.30\% = 4.20\%$; nhân với $32\text{m} / 4 = \text{USD } 8\text{m}$ ra ngay USD 384,000 và USD 336,000!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Cộng thay vì trừ biên độ tín dụng $0.85\%$):** Nhiều bạn lấy nhầm $K = 4.50\% + 0.85\% = 5.35\%$! Nhớ rằng Swap tiêu chuẩn trao đổi $L$ lấy $K$ (không bao gồm phần *credit spread* $0.85\%$ của riêng doanh nghiệp trả cho ngân hàng), nên $K$ phải **nhỏ hơn** tổng chi phí đi vay: $K = 4.50\% - 0.85\% = 3.65\%$.
- **Bẫy 2 (Ngược dấu $M - L$):** Sigma **trả $M$** trên khoản vay và **nhận $L$** từ Swap $\implies$ Khi $M > L$ (Quý 1), chi phí ròng **tăng lên** ($4.80\%$); khi $M < L$ (Quý 2), chi phí ròng **giảm xuống** ($4.20\%$).

---

## Question 14 (Hard) — Ngang Giá Lãi Suất Có Phòng Hộ (CIP) & Bẫy Gấp Đôi Rủi Ro Tỷ Giá Của Tau
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Tau observes these executable nine-month terms:
>
> | Item | Quote |
> |---|---:|
> | Spot exchange rate | 1.0800 USD per EUR |
> | Forward exchange rate | 1.1200 USD per EUR |
> | USD borrowing and lending rate | 5.00% effective annually |
> | EUR borrowing and lending rate | 2.00% effective annually |
>
> Tau proposes the following transactions today:
>
> 1. Borrow EUR 200,000 for nine months.
> 2. Convert it to USD and invest all the proceeds for nine months.
> 3. Sell EUR 200,000 forward for delivery in nine months.
>
> Tau claims a guaranteed USD 8,000 profit because $(1.1200-1.0800)(200,000)=8,000$. The forward requires no upfront payment; EUR is delivered against USD at maturity. There are no transaction costs or margin requirements.
>
> a. Calculate the forward rate consistent with covered interest parity.
>
> b. Express the proposed trade's terminal net USD cash flow in terms of $S_T$, the maturity spot rate in USD per EUR. Assess Tau's profit claim.
>
> c. Construct a self-financing arbitrage using initial borrowing with a spot value of USD 216,000. Show dated cash flows in both currencies and calculate the terminal USD profit.

**Tóm tắt thông số:**
- Tỷ giá yết theo **USD trên 1 EUR** (*USD per EUR*, tức USD là đồng định giá / nội tệ, EUR là đồng cơ sở / hàng hóa): $S_0 = 1.0800\text{ USD/EUR}$; $F_{\text{quoted}} = 1.1200\text{ USD/EUR}$.
- Kỳ hạn $T = 9/12 = 0.75$ năm. Lãi suất hiệu dụng năm: $r_{\text{USD}} = 5.00\%$ EAR; $r_{\text{EUR}} = 2.00\%$ EAR.
- Quy mô giao dịch: $\text{EUR } 200,000 \iff 200,000 \times 1.0800 = \text{USD } 216,000$ theo tỷ giá giao ngay.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Tỷ giá kỳ hạn theo Ngang giá Lãi suất Có Phòng hộ (Covered Interest Parity — CIP)**
Với tỷ giá yết dạng $\text{USD per EUR}$ và lãi suất hiệu dụng năm trong $T = 0.75$ năm:
$$F_{\text{CIP}} = S_0 \left(\frac{1 + r_{\text{USD}}}{1 + r_{\text{EUR}}}\right)^{0.75} = 1.0800 \times \left(\frac{1.05}{1.02}\right)^{0.75} = 1.0800 \times 1.02197848 = \mathbf{1.103737 \approx 1.1037\text{ USD per EUR}}$$
*(Nhận xét ngay: $F_{\text{quoted}} = 1.1200 > F_{\text{CIP}} = 1.1037 \implies$ Đồng EUR đang được **định giá quá cao trên thị trường kỳ hạn**!)*

#### **b. Biểu thức dòng tiền ròng cuối kỳ bằng USD theo $S_T$ của giao dịch Tau đề xuất & Đánh giá**
Hãy lần theo chính xác từng chân giao dịch của Tau tại ngày đáo hạn $T = 0.75$ năm:
1. **Khoản vay EUR 200,000 (9 tháng tại $2.00\%$ EAR):** Tại $T = 0.75$, Tau **nợ phải trả bằng EUR** cả gốc lẫn lãi là:
   $$\text{EUR Loan Due} = 200,000 \times (1.02)^{0.75} = \mathbf{\text{EUR } 202,992.5618} \quad (\approx \text{EUR } 202,992.56)$$
2. **Đổi sang USD ($200,000 \times 1.0800 = \text{USD } 216,000$) và gửi tiết kiệm 9 tháng tại $5.00\%$ EAR:** Tại $T = 0.75$, Tau **thu về bằng USD**:
   $$\text{USD Deposit Proceeds} = 216,000 \times (1.05)^{0.75} = \mathbf{\text{USD } 224,050.4010} \quad (\approx \text{USD } 224,050.40)$$
3. **BÁN kỳ hạn EUR 200,000 (*Sell EUR 200,000 forward*) tại $1.1200\text{ USD/EUR}$:**
   - **CỰC KỲ CHÚ Ý:** Tau đã vay EUR (đang âm EUR), lẽ ra muốn phòng hộ khoản vay thì phải *mua* EUR kỳ hạn, nhưng Tau lại đi **BÁN EUR kỳ hạn**!
   - Do đó tại $T = 0.75$, hợp đồng bán kỳ hạn bắt buộc Tau phải **giao thêm EUR 200,000 nữa** và đổi lại **nhận về bằng USD**:
     $$\text{USD Forward Inflow} = 200,000 \times 1.1200 = \mathbf{\text{USD } 224,000.00}$$
- **Tổng hợp dòng tiền tại ngày đáo hạn ($T = 0.75$) khi quy toàn bộ nghĩa vụ EUR sang USD theo tỷ giá giao ngay lúc đáo hạn $S_T$:**
  - Tổng USD thu vào $= 224,050.4010 + 224,000.00 = \mathbf{\text{USD } 448,050.4010}$ ($\approx \text{USD } 448,050.40$).
  - Tổng EUR phải mua trên thị trường giao ngay giá $S_T$ để trả nợ vay VÀ giao cho hợp đồng kỳ hạn $= 202,992.5618 + 200,000.00 = \mathbf{\text{EUR } 402,992.5618}$ ($\approx \text{EUR } 402,992.56$).
  - **Biểu thức dòng tiền USD ròng cuối kỳ:**
    $$\mathbf{\text{Net Terminal USD Cash Flow} = 448,050.4010 - 402,992.5618\, S_T \approx 448,050.40 - 402,992.56\, S_T}$$
- **Đánh giá tuyên bố lãi chắc chắn USD 8,000 của Tau:** Tuyên bố của Tau **SAI TRẦM TRỌNG trên cả 3 phương diện**:
  1. **Không hề phi rủi ro (Tự nhân đôi rủi ro tỷ giá!):** Vì vừa vay EUR vừa bán EUR kỳ hạn, Tau bị phơi nhiễm vị thế **bán khống ròng tới EUR 402,992.56**! Giao dịch này thực chất là một canh bạc đầu cơ tỷ giá trần trụi và sẽ **THUA LỖ ròng bất cứ khi nào $S_T > \frac{448,050.4010}{402,992.5618} = 1.111808 \approx 1.1118\text{ USD/EUR}$**!
  2. **Sai cả chiều kinh doanh chênh lệch giá gốc:** Kể cả nếu ở bước 3 Tau sửa lại thành *mua* EUR 202,992.56 kỳ hạn ở giá $1.1200$ để khóa khoản vay EUR, Tau vẫn sẽ **lỗ chắc chắn $-\text{USD } 3,301.27$** ($224,050.40 - 202,992.5618 \times 1.1200$), bởi vì EUR kỳ hạn đang quá đắt ($1.1200 > 1.1037$) nên đi vay EUR là đi ngược chiều arbitrage!
  3. Tau hoàn toàn bỏ quên tiền lãi phát sinh trên cả hai đồng tiền và kích cỡ nghĩa vụ lãi vay EUR tăng thêm.

#### **c. Thiết lập Arbitrage Tự Tài Trợ Chuẩn (Self-Financing Arbitrage) với quy mô vay ban đầu USD 216,000**
- Vì $F_{\text{quoted}} (1.1200) > F_{\text{CIP}} (1.1037)$, đồng EUR kỳ hạn đang **đắt hơn** mức cân bằng $\implies$ Quy tắc vàng: **Vay USD $\rightarrow$ Mua giao ngay & Gửi tiết kiệm EUR $\rightarrow$ Bán kỳ hạn TOÀN BỘ cả gốc lẫn lãi EUR sẽ thu về tại $T = 0.75$!**
- Kiểm tra quy mô: Vay $\text{USD } 216,000.00$, đổi ở $S_0 = 1.0800\text{ USD/EUR}$ được đúng $\frac{216,000}{1.0800} = \text{EUR } 200,000.00$. Sau 9 tháng gửi ở $2.00\%$ EAR, số tiền EUR tích lũy thành $\text{EUR } 200,000 \times (1.02)^{0.75} = \text{EUR } 202,992.5618$. Do đó hôm nay ta ký hợp đồng **bán kỳ hạn đúng EUR 202,992.5618** tại tỷ giá $1.1200\text{ USD/EUR}$!

| Hành động giao dịch | Hôm nay ($t = 0$) — USD | Hôm nay ($t = 0$) — EUR | Đáo hạn ($T = 0.75$) — USD | Đáo hạn ($T = 0.75$) — EUR |
|---|---:|---:|---:|---:|
| 1. Vay USD 216,000 trong 9 tháng tại $5.00\%$ EAR | $+216,000.00$ | $0.00$ | $-224,050.40$ | $0.00$ |
| 2. Đổi giao ngay USD 216,000 sang EUR tại $1.0800$ | $-216,000.00$ | $+200,000.00$ | $0.00$ | $0.00$ |
| 3. Gửi tiết kiệm EUR 200,000 trong 9 tháng tại $2.00\%$ EAR | $0.00$ | $-200,000.00$ | $0.00$ | $+202,992.56$ |
| 4. Bán kỳ hạn $\text{EUR } 202,992.5618$ tại $F = 1.1200\text{ USD/EUR}$ | $0.00$ | $0.00$ | $+227,351.67$ | $-202,992.56$ |
| **Dòng tiền ròng (Net Cash Flow)** | **USD 0.00** | **EUR 0.00** | **+USD 3,301.27** | **EUR 0.00** |

- **Kiểm tra số học chính xác không làm tròn:**
  - Thu USD từ hợp đồng bán kỳ hạn: $202,992.5618 \times 1.1200 = \text{USD } 227,351.6692$.
  - Trả nợ gốc + lãi vay USD: $216,000 \times (1.05)^{0.75} = \text{USD } 224,050.4010$.
  - **Lợi nhuận Arbitrage phi rủi ro chắc chắn tại đáo hạn:**
    $$\Pi_T = 227,351.6692 - 224,050.4010 = \mathbf{+\text{USD } 3,301.2683 \approx \text{USD } 3,301.27}$$

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Công thức 1 dòng tính thẳng Lợi nhuận CIP Arbitrage ở câu c (để kiểm tra đáp số trong 5 giây!):**
  $$\Pi_T = N_{\text{EUR},0} (1 + r_{\text{EUR}})^T \times \left(F_{\text{quoted}} - F_{\text{CIP}}\right) = 200,000(1.02)^{0.75} \times (1.1200 - 1.103736998) = 202,992.5618 \times 0.016263002 = \mathbf{\text{USD } 3,301.27!}$$
- **Mẹo nhớ tử số / mẫu số CIP không bao giờ lộn:** Tỷ giá yết $\frac{\text{USD}}{\text{EUR}}$ thì USD nằm trên tử, EUR nằm dưới mẫu $\implies F = S_0 \left(\frac{1 + r_{\text{USD}}}{1 + r_{\text{EUR}}}\right)^T$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy siêu kinh điển của GS. Cayirli ở câu 14b:** Sinh viên đọc lướt câu 14b hay mặc định tưởng Tau đã khóa tỷ giá xong xuôi rồi kết luận "Tau lỗ USD 3,301"! **SAI!** Đọc kỹ từng chữ bước 1 và bước 3 của Tau: *1. Borrow EUR 200,000* và *3. Sell EUR 200,000 forward*! Cả hai bước đều tạo nghĩa vụ **phải trả EUR** lúc đáo hạn (tổng cộng **EUR 402,992.56**)! Chính vì thế đề mới yêu cầu viết dòng tiền theo **$S_T$**: $\mathbf{448,050.40 - 402,992.56 S_T}$!
- **Bẫy 2 ở câu 14c (Chỉ bán kỳ hạn 200,000 EUR gốc mà quên bán phần lãi EUR):** Nếu chỉ bán kỳ hạn EUR 200,000 thì phần lãi $\text{EUR } 2,992.56$ sẽ trôi nổi theo tỷ giá $S_T$, không còn là arbitrage phi rủi ro hoàn hảo! Phải bán kỳ hạn trọn vẹn **EUR 202,992.56** ($= 200,000 \times 1.02^{0.75}$).

---

## Question 15 (Hard) — Kỳ Hạn Tổng Hợp Từ Quyền Chọn & Kinh Doanh Chênh Lệch Giá (Synthetic Forward)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Upsilon observes the following executable prices on Phi shares. The stock pays no dividends over the next six months.
>
> | Instrument | Terms | Current quote |
> |---|---|---:|
> | European call | Six months to expiration; strike USD 70 | USD 6.20 per share |
> | European put | Six months to expiration; strike USD 70 | USD 3.80 per share |
> | Forward | Six months to maturity; covers 1,000 shares | Delivery price USD 73.20 per share; no upfront payment |
>
> Each option contract covers 100 shares. Options and the forward settle in cash using the same terminal share price. Borrowing and lending are available at 4% effective annually. Both long and short positions are permitted, with no fees, margin requirements or trading restrictions.
>
> a. Use the options and borrowing or lending to construct a zero-initial-cost position with the payoff of a long forward. Determine its implied delivery price per share.
>
> b. Construct an arbitrage against the quoted forward for 1,000 shares. State contract quantities and show initial and terminal cash flows for share prices below and above USD 70.
>
> c. If only the call premium changes while the other quotes remain fixed, what call price would remove this discrepancy?

**Tóm tắt thông số:**
- Kỳ hạn chung: $T = 6/12 = 0.50$ năm; cổ phiếu Phi không trả cổ tức. Lãi suất vay & cho vay: $r = 4\%$ EAR.
- Call châu Âu ($K = 70$): $C = \text{USD } 6.20$/cp. Put châu Âu ($K = 70$): $P = \text{USD } 3.80$/cp. (Mỗi hợp đồng quyền chọn = **100 cổ phiếu**).
- Hợp đồng Forward (quy mô **1,000 cổ phiếu**): giá giao nhận $F_{\text{quoted}} = \text{USD } 73.20$/cp, chi phí ban đầu bằng 0.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Thiết lập vị thế Long Forward tổng hợp chi phí ban đầu bằng 0 & Giá giao nhận hàm ý**
- Trên **1 cổ phiếu**, mua 1 Call($K=70$) và bán (viết) 1 Put($K=70$) tạo ra payoff lúc đáo hạn là:
  $$\max(S_T - 70, 0) - \max(70 - S_T, 0) = S_T - 70$$
- Tổ hợp quyền chọn này đòi hỏi chi phí ròng hôm nay là $C - P = 6.20 - 3.80 = \text{USD } 2.40$/cổ phiếu.
- Để biến vị thế thành **chi phí ban đầu bằng 0 (*zero-initial-cost position*)**, ta **VAY USD 2.40** hôm nay ở lãi suất $4\%$ EAR trong 6 tháng ($T = 0.50$):
  - Dòng tiền ròng tại $t = 0$: $-6.20 + 3.80 + 2.40 = \text{USD } 0.00$.
  - Tại $T = 0.50$, khoản vay phải trả gốc + lãi là: $2.40 \times (1.04)^{0.50} = 2.40 \times 1.01980390 = \text{USD } 2.447529$.
- Tổng payoff ròng tại ngày đáo hạn $T = 0.50$ của danh mục tự tài trợ này là:
  $$(S_T - 70) - 2.447529 = S_T - 72.447529$$
  Đây chính xác là payoff $S_T - K_{\text{imp}}$ của một vị thế Long Forward có **giá giao nhận hàm ý (*implied delivery price*)**:
  $$K_{\text{implied}} = 70 + 2.40(1.04)^{0.50} = \mathbf{\text{USD } 72.447529 \approx \text{USD } 72.45\text{ per share}}$$

#### **b. Chiến lược Arbitrage cho 1,000 cổ phiếu & Bảng dòng tiền theo miền giá $S_T$**
- **Xác định chiều giao dịch:** Kỳ hạn tổng hợp từ quyền chọn cho phép mua tương lai ở giá **USD 72.45/cp**, rẻ hơn hợp đồng Forward niêm yết (**USD 73.20/cp**). Do đó ta **Mua thấp (Long Synthetic Forward) — Bán cao (Short Quoted Forward)**!
- **Số lượng hợp đồng chính xác (cho 1,000 cổ phiếu, lưu ý 1 hợp đồng quyền chọn = 100 cổ phiếu!):**
  - **Short (Bán) 1 hợp đồng Forward** (quy mô 1,000 cổ phiếu) tại giá giao nhận USD 73.20/cp.
  - **Buy (Mua) 10 hợp đồng Call** ($10 \times 100 = 1,000$ cổ phiếu) strike USD 70 $\rightarrow$ trả $1,000 \times 6.20 = -\text{USD } 6,200.00$.
  - **Write / Short (Bán) 10 hợp đồng Put** ($10 \times 100 = 1,000$ cổ phiếu) strike USD 70 $\rightarrow$ thu $1,000 \times 3.80 = +\text{USD } 3,800.00$.
  - **Borrow (Vay) USD 2,400.00** trong 6 tháng tại lãi suất $4\%$ EAR $\rightarrow$ nhận $+\text{USD } 2,400.00$ hôm nay, trả $-2,400(1.04)^{0.50} = -\text{USD } 2,447.5294$ ($\approx -\text{USD } 2,447.53$) lúc đáo hạn.

| Thành phần danh mục (1,000 cổ phiếu) | Hôm nay ($t = 0$) | Đáo hạn nếu $S_T < 70$ *(hoặc $S_T \le 70$)* | Đáo hạn nếu $S_T > 70$ *(hoặc $S_T \ge 70$)* |
|---|---:|---:|---:|
| 1. Short 1 Forward ($K_F = 73.20$, 1,000 cp) | $0.00$ | $+1,000(73.20 - S_T) = 73,200 - 1,000 S_T$ | $+1,000(73.20 - S_T) = 73,200 - 1,000 S_T$ |
| 2. Long 10 Call contracts ($K = 70$, 1,000 cp) | $-6,200.00$ | $0.00$ | $+1,000(S_T - 70) = 1,000 S_T - 70,000$ |
| 3. Short 10 Put contracts ($K = 70$, 1,000 cp) | $+3,800.00$ | $-1,000(70 - S_T) = -70,000 + 1,000 S_T$ | $0.00$ |
| 4. Vay USD 2,400.00 tại $4\%$ EAR trong 6 tháng | $+2,400.00$ | $-2,447.53$ | $-2,447.53$ |
| **Tổng dòng tiền ròng (Net Cash Flow)** | **USD 0.00** | **$73,200 - 70,000 - 2,447.53 =$ +USD 752.47** | **$73,200 - 70,000 - 2,447.53 =$ +USD 752.47** |

- **Kết luận câu b:** Không cần bỏ vốn ban đầu ($\text{USD } 0.00$), danh mục thu về **lợi nhuận chắc chắn đúng bằng USD 752.47** (*chính xác: $\text{USD } 752.4706$*) trong mọi kịch bản của $S_T$!

#### **c. Mức phí quyền chọn mua ($C^*$) loại bỏ hoàn toàn chênh lệch giá**
Áp dụng hệ thức Ngang giá Quyền chọn Mua - Bán theo Giá Kỳ hạn (*Forward Put-Call Parity*):
$$C^* - P = \frac{F_{\text{quoted}} - K}{(1 + r)^{0.50}} \implies C^* = 3.80 + \frac{73.20 - 70.00}{(1.04)^{0.50}} = 3.80 + \frac{3.20}{1.01980390} = 3.80 + 3.137858 = \mathbf{\text{USD } 6.937858 \approx \text{USD } 6.94\text{ per share}}$$
*(Kiểm chứng: Với $C^* = 6.937858$, chi phí $C^* - P = 3.137858$, nhân $(1.04)^{0.5}$ ra $3.20 \implies K_{\text{implied}} = 70 + 3.20 = \text{USD } 73.20 = F_{\text{quoted}}$!).*

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Hệ thức Vàng kết nối trực tiếp Quyền chọn & Kỳ hạn (không cần biết giá giao ngay $S_0$!):**
  $$C - P = PV(F - K) \iff F_{\text{implied}} = K + FV(C - P)$$
  - Lãi arbitrage cuối kỳ trên 1,000 cổ phiếu: $1,000 \times (F_{\text{quoted}} - F_{\text{implied}}) = 1,000 \times (73.20 - 72.447529) = \mathbf{\text{USD } 752.47}$!
  - Độ tăng giá Call cần thiết để triệt tiêu arbitrage: $\Delta C = PV(\text{Profit per share}) = \frac{0.7524706}{(1.04)^{0.5}} = 0.737858 \implies C^* = 6.20 + 0.737858 = \mathbf{\text{USD } 6.94}$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy quy mô hợp đồng khác nhau (1,000 vs 100):** Đề gài rất khéo: 1 hợp đồng Forward bao gồm **1,000 cổ phiếu**, còn 1 hợp đồng Option chỉ bao gồm **100 cổ phiếu**! Nếu viết "Buy 1 call, write 1 put, short 1 forward" là lệch quy mô gấp 10 lần và vỡ tan danh mục! Phải ghi rõ: **10 call contracts, 10 put contracts, và 1 forward contract**!

---

# PHẦN III — LECTURE 10: OPTION STRATEGIES, PRICING RELATIONSHIPS AND EXERCISE (Q16 – Q25)

*Quy ước chung từ đề gốc: Phí quyền chọn được yết trên mỗi cổ phiếu (per share). Trừ khi có ghi chú khác, quyền chọn là kiểu châu Âu (European) và tài sản cơ sở không trả cổ tức. Khi tính lợi nhuận chiến lược (strategy profit), lấy payoff đáo hạn trừ chi phí ròng ban đầu (bỏ qua lãi vay tài trợ phí). Sử dụng đúng mức lãi suất nêu trong đề cho bài toán định giá / parity.*

---
## Question 16 (Easy) — Chiến Lược Quyền Chọn Mua Được Bảo Đảm (Covered Call)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Alpha buys 100 shares at USD 48 each and writes one call contract covering those shares, with a strike of USD 52. At expiration, the share price is USD 55. Alpha reports a total profit of USD 650 from the combined position.
>
> a. Recover the call premium per share and the initial net cost of the position.
>
> b. Determine the maximum terminal value of the combined position, its maximum profit and its break-even share price.

**Tóm tắt thông số:**
- Vị thế **Covered Call** (100 cổ phiếu): Mua 100 cổ phiếu tại $S_0 = \text{USD } 48$ + Bán (viết) 1 hợp đồng Call (100 cổ phiếu) tại strike $K = \text{USD } 52$.
- Tại đáo hạn: $S_T = \text{USD } 55$ ($> 52$); tổng lợi nhuận báo cáo $\Pi = \text{USD } 650$ (tức $\text{USD } 6.50$/cổ phiếu).

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Khôi phục phí quyền chọn mua mỗi cổ phiếu ($c$) & Chi phí ròng ban đầu**
- Tại $S_T = 55 \ge K = 52$, quyền chọn mua bị thực hiện, nên giá trị đáo hạn trên mỗi cổ phiếu của vị thế Covered Call bị chặn trần đúng bằng $K$:
  $$V_T = 100 \times \left[S_T - \max(S_T - 52, 0)\right] = 100 \times \left[55 - (55 - 52)\right] = 100 \times 52 = \text{USD } 5,200.00$$
- Theo định nghĩa lợi nhuận chiến lược ($\text{Profit} = V_T - \text{Initial Net Cost}$):
  $$5,200 - \text{Initial Net Cost} = 650 \implies \text{Initial Net Cost} = 5,200 - 650 = \mathbf{\text{USD } 4,550.00} \quad (\text{USD } 45.50\text{/cp})$$
- Vì chi phí mua 100 cổ phiếu ban đầu là $100 \times 48 = \text{USD } 4,800.00$, tổng phí quyền chọn mua thu về là $4,800 - 4,550 = \text{USD } 250.00$, suy ra **phí quyền chọn mua trên mỗi cổ phiếu**:
  $$c = \frac{250.00}{100} = 48.00 - 45.50 = \mathbf{\text{USD } 2.50\text{ per share}}$$

#### **b. Giá trị đáo hạn tối đa, Lợi nhuận tối đa & Giá cổ phiếu hòa vốn**
1. **Giá trị đáo hạn tối đa (*Maximum terminal value*):** Đạt được với mọi $S_T \ge 52$ khi cổ phiếu bị mua đi ở giá thực hiện USD 52:
   $$V_{T,\max} = 100 \times 52 = \mathbf{\text{USD } 5,200.00}$$
2. **Lợi nhuận tối đa (*Maximum profit*):** Đạt được với mọi $S_T \ge 52$ (chính là mức lợi nhuận tại $S_T = 55$!):
   $$\Pi_{\max} = 5,200.00 - 4,550.00 = 100 \times \left[(52 - 48) + 2.50\right] = \mathbf{\text{USD } 650.00}$$
3. **Giá cổ phiếu hòa vốn (*Break-even share price*, $S_{BE}$):** Xảy ra trong vùng $S_T \le 52$ (quyền chọn mua không thực hiện, giá trị danh mục là $100 S_T$):
   $$100 S_{BE} - 4,550 = 0 \implies S_{BE} = S_0 - c = 48.00 - 2.50 = \mathbf{\text{USD } 45.50\text{ per share}}$$

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Công thức siêu tốc cho **Covered Call** (tính trên 1 cổ phiếu rồi nhân 100):
  - $\text{Net Initial Cost/sh} = S_0 - c$
  - $\text{Max Value/sh} = K \quad (\text{với } S_T \ge K)$
  - $\text{Max Profit/sh} = (K - S_0) + c$
  - $\text{Break-even } S_{BE} = S_0 - c$ (bằng đúng *Initial Net Cost per share*!).
  - Ở bài này vì $S_T = 55 > K = 52$, lợi nhuận $6.50$/cp chính là Max Profit $\implies (52 - 48) + c = 6.50 \implies c = 2.50$ trong 2 giây!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Cộng thay vì trừ phí Call vào giá vốn):** Alpha **writes (bán)** Call nên **nhận tiền phí $c$ về**, làm **giảm** chi phí ròng ban đầu xuống $48 - 2.50 = 45.50$/cp (nếu cộng thành $50.50$ là biến thành mua quyền chọn!).
- **Bẫy 2 (Tưởng tại $S_T = 55$ cổ phiếu lãi $55 - 48 = 7$/cp mà quên trừ phần lỗ quyền chọn $55 - 52 = 3$/cp):** Mọi phần tăng giá trên USD 52 đều thuộc về người mua Call!

---

## Question 17 (Easy) — Chiến Lược Chênh Lệch Giá Xuống Bằng Put (Bear Put Spread)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Beta buys one put contract with strike USD 64 for USD 7.10 per share and writes one put contract with strike USD 56. Both contracts cover 100 shares of the same stock and have the same expiration.
>
> The combined position's maximum loss is USD 280.
>
> a. Recover the premium received per share for the written put.
>
> b. Determine the break-even share price and maximum total profit.

**Tóm tắt thông số:**
- **Bear Put Spread** (100 cổ phiếu): Mua 1 Put strike cao $K_2 = \text{USD } 64$ giá $p_{64} = \text{USD } 7.10$/cp + Bán (viết) 1 Put strike thấp $K_1 = \text{USD } 56$ giá $p_{56}$ chưa biết.
- Mức lỗ tối đa của vị thế kết hợp: $\text{Max Loss} = \text{USD } 280$ (tức $\text{USD } 2.80$/cổ phiếu).

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Khôi phục phí quyền chọn bán nhận được trên mỗi cổ phiếu ($p_{56}$)**
- Xét payoff đáo hạn trên 1 cổ phiếu của danh mục $\text{Long Put}(64) + \text{Short Put}(56)$:
  - Nếu $S_T \ge 64$: cả hai quyền chọn đều hết hạn vô giá trị $\implies \text{Payoff} = 0$.
  - Nếu $56 < S_T < 64$: $\text{Payoff} = 64 - S_T > 0$.
  - Nếu $S_T \le 56$: $\text{Payoff} = (64 - S_T) - (56 - S_T) = 8.00$.
- Vì payoff đáo hạn không bao giờ âm ($\ge 0$), **mức lỗ tối đa xảy ra khi $S_T \ge 64$ (payoff $= 0$) và đúng bằng chi phí ròng bỏ ra ban đầu (*initial net debit*)**:
  $$\text{Net Initial Cost per share} = \frac{280}{100} = \text{USD } 2.80 = p_{64} - p_{56} = 7.10 - p_{56}$$
  $$\implies p_{56} = 7.10 - 2.80 = \mathbf{\text{USD } 4.30\text{ per share}}$$

#### **b. Giá cổ phiếu hòa vốn & Tổng lợi nhuận tối đa**
1. **Giá cổ phiếu hòa vốn (*Break-even share price*, $S_{BE}$):** Nằm trong khoảng giữa hai giá thực hiện ($56 \le S_{BE} \le 64$), nơi payoff $(64 - S_{BE})$ bù đắp vừa đủ chi phí ròng USD 2.80/cp:
   $$(64 - S_{BE}) - 2.80 = 0 \implies S_{BE} = 64.00 - 2.80 = \mathbf{\text{USD } 61.20\text{ per share}}$$
2. **Tổng lợi nhuận tối đa (*Maximum total profit*):** Đạt được với mọi $S_T \le 56$, nơi chênh lệch payoff đạt mức tối đa $K_2 - K_1 = 64 - 56 = \text{USD } 8.00$/cp:
   $$\Pi_{\max} = 100 \times \left[(64 - 56) - 2.80\right] = 100 \times 5.20 = \mathbf{\text{USD } 520.00}$$

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Hằng đẳng thức bất biến cho **MỌI Vertical Spread ( cả Bull Call Spread lẫn Bear Put Spread)**:
  $$\text{Max Profit per share} + \text{Max Loss per share} \equiv \text{Strike Width } (K_{\text{high}} - K_{\text{low}})$$
  Áp dụng ngay trong 2 giây: Độ rộng strike $= 64 - 56 = 8.00$/cp (USD 800 cho 100 cp). Đề đã cho $\text{Max Loss} = \text{USD } 280 \implies \text{Max Profit} = 800 - 280 = \mathbf{\text{USD } 520}$! Và với Bear Put Spread, hòa vốn luôn tính từ **strike cao trừ chi phí ròng**: $64 - 2.80 = \mathbf{61.20}$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Cộng nhầm điểm hòa vốn từ strike thấp $56 + 2.80 = 58.80$):** Công thức $K_{\text{low}} + \text{Net Debit}$ là của **Bull Call Spread**! Còn **Bear Put Spread** kiếm lời khi giá giảm xuống dưới $K_{\text{high}}$, nên điểm hòa vốn bắt buộc phải là $K_{\text{high}} - \text{Net Debit} = 64 - 2.80 = 61.20$ (kiểm lại tại $S_T = 61.20$: Put 64 trả $2.80$, Put 56 trả $0$, trừ chi phí $2.80$ ra đúng bằng $0$!).
- **Bẫy 2 (Báo cáo Max Profit trên 1 cổ phiếu USD 5.20 thay vì tổng vị thế USD 520):** Đề hỏi *"maximum **total** profit"* cho vị thế 100 cổ phiếu $\rightarrow$ Phải nhân 100 ra **USD 520.00**!

---

## Question 18 (Easy) — Hệ Số Chiết Khấu & Lãi Suất Hàm Ý Từ Ngang Giá Quyền Chọn (Put-Call Parity)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Gamma observes a share price of USD 84. Matching nine-month European options with strike USD 80 cost USD 9.60 for the call and USD 4.10 for the put.
>
> Assume these quotes satisfy put-call parity and the risk-free rate is nonnegative.
>
> a. Recover the nine-month discount factor.
>
> b. Calculate the implied continuously compounded annual risk-free rate and check whether it is consistent with the stated assumption.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 84$; kỳ hạn $T = 9/12 = 0.75$ năm; cùng strike $K = \text{USD } 80$.
- Call châu Âu $C = \text{USD } 9.60$; Put châu Âu $P = \text{USD } 4.10$. Giả định thỏa mãn Put-Call Parity và $r \ge 0$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Khôi phục hệ số chiết khấu kỳ hạn 9 tháng ($DF_{0, 0.75}$)**
Theo phương trình Ngang giá Quyền chọn Mua - Bán đối với cổ phiếu không trả cổ tức:
$$C + K \cdot DF_{0, 0.75} = S_0 + P \implies K \cdot DF_{0, 0.75} = S_0 + P - C$$
Thay số:
$$80 \cdot DF_{0, 0.75} = 84.00 + 4.10 - 9.60 = \text{USD } 78.50$$
$$\implies DF_{0, 0.75} = \frac{78.50}{80.00} = \mathbf{0.98125} \quad (\approx 0.98\text{ nếu làm tròn 2 chữ số; giữ } 0.98125\text{ chính xác!})$$

#### **b. Lãi suất phi rủi ro ghép lãi liên tục hàng năm hàm ý ($r$) & Kiểm tra tính nhất quán**
Liên hệ giữa hệ số chiết khấu và lãi suất ghép lãi liên tục hàng năm $r$ cho $T = 0.75$ năm:
$$DF_{0, 0.75} = e^{-r T} = 0.98125 \implies r = -\frac{\ln(0.98125)}{0.75} = \frac{0.018928011}{0.75} = 0.02523735 = \mathbf{2.52\%\text{ per year}}$$
- **Kiểm tra tính nhất quán (*Consistency check*):** Vì $r = 2.52\% \ge 0$ (tương đương $0 < DF_{0, 0.75} = 0.98125 \le 1$), mức lãi suất hàm ý **hoàn toàn nhất quán (consistent)** với giả định lãi suất phi rủi ro không âm đã nêu trong đề!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Mẹo không bao giờ nhớ nhầm dấu của Put-Call Parity: Nhớ hai danh mục **Fiduciary Call** ($C + PV(K)$) và **Protective Put** ($P + S_0$) đều cho payoff $\max(S_T, K)$ lúc đáo hạn:
  $$PV(K) = S_0 + P - C = 84 + 4.10 - 9.60 = 78.50 \implies DF = \frac{78.50}{80} = 0.98125$$

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Quên chia cho $T = 0.75$ ở câu b):** Tính $-\ln(0.98125) = 1.89\%$ là lãi suất của **9 tháng**, phải chia cho $0.75$ mới ra lãi suất thường niên hóa **$2.52\%$**!
- **Bẫy 2 (Bỏ sót vế kiểm tra nhất quán ở câu b):** Đề ghi rõ *"and check whether it is consistent with the stated assumption"* — nhớ viết rõ câu kết luận *"Since $2.52\% \ge 0$ (i.e., $DF \le 1$), the implied rate is consistent with the nonnegative interest-rate assumption"* để lấy trọn 100% điểm!

---

## Question 19 (Average) — Đối Đầu Biến Động: Long Straddle vs. Long Strangle
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Delta shares trade at USD 100. The following European options expire in three months. The risk-free rate is zero.
>
> | Option | Strike | Premium per share |
> |---|---:|---:|
> | Put | USD 90 | USD 2 |
> | Put | USD 100 | USD 6 |
> | Call | USD 100 | USD 6 |
> | Call | USD 110 | USD 3 |
>
> Epsilon considers either buying the USD 100 put and call, or buying the USD 90 put and USD 110 call. Each option contract covers 100 shares.
>
> a. Calculate each strategy's initial cost and total net profit at terminal share prices of USD 86, USD 100 and USD 114.
>
> b. Find each strategy's break-even prices and maximum loss.
>
> c. Epsilon will accept a maximum possible loss of USD 600. Which strategy meets that limit, and what does the comparison in part a reveal about the trade-off?

**Tóm tắt thông số:**
- $S_0 = \text{USD } 100$, $T = 3$ tháng, $r = 0$, quy mô **100 cổ phiếu/hợp đồng**.
- **Chiến lược 1 (Long Straddle tại $K = 100$):** Mua 1 Put(100) giá USD 6 + Mua 1 Call(100) giá USD 6.
- **Chiến lược 2 (Long Strangle tại $K_P = 90, K_C = 110$):** Mua 1 Put(90) giá USD 2 + Mua 1 Call(110) giá USD 3.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Chi phí ban đầu & Tổng lợi nhuận ròng tại $S_T \in \{86, 100, 114\}$**
1. **Chiến lược 1 — Long Straddle (Put 100 + Call 100):**
   - **Chi phí ban đầu (*Initial cost*):** $100 \times (6 + 6) = \mathbf{\text{USD } 1,200.00}$ ($\text{USD } 12.00$/cổ phiếu).
   - Công thức lợi nhuận ròng: $\Pi_{\text{Straddle}}(S_T) = 100 \times \left[\max(100 - S_T, 0) + \max(S_T - 100, 0) - 12\right] = 100 \times (|S_T - 100| - 12)$:
     - Tại $S_T = 86$: $100 \times (14 - 12) = \mathbf{+\text{USD } 200.00}$.
     - Tại $S_T = 100$: $100 \times (0 - 12) = \mathbf{-\text{USD } 1,200.00}$.
     - Tại $S_T = 114$: $100 \times (14 - 12) = \mathbf{+\text{USD } 200.00}$.
2. **Chiến lược 2 — Long Strangle (Put 90 + Call 110):**
   - **Chi phí ban đầu (*Initial cost*):** $100 \times (2 + 3) = \mathbf{\text{USD } 500.00}$ ($\text{USD } 5.00$/cổ phiếu).
   - Công thức lợi nhuận ròng: $\Pi_{\text{Strangle}}(S_T) = 100 \times \left[\max(90 - S_T, 0) + \max(S_T - 110, 0) - 5\right]$:
     - Tại $S_T = 86$: $100 \times \left[(90 - 86) + 0 - 5\right] = 100 \times (4 - 5) = \mathbf{-\text{USD } 100.00}$.
     - Tại $S_T = 100$: $100 \times \left[0 + 0 - 5\right] = \mathbf{-\text{USD } 500.00}$.
     - Tại $S_T = 114$: $100 \times \left[0 + (114 - 110) - 5\right] = 100 \times (4 - 5) = \mathbf{-\text{USD } 100.00}$.

| Chiến lược | Chi phí ban đầu | Lãi/lỗ tại $S_T = 86$ | Lãi/lỗ tại $S_T = 100$ | Lãi/lỗ tại $S_T = 114$ |
|---|---:|---:|---:|---:|
| **Straddle (P100 + C100)** | **USD 1,200.00** | **+USD 200.00** | **-USD 1,200.00** | **+USD 200.00** |
| **Strangle (P90 + C110)** | **USD 500.00** | **-USD 100.00** | **-USD 500.00** | **-USD 100.00** |

#### **b. Các mức giá hòa vốn (Break-even prices) & Mức lỗ tối đa (Maximum loss)**
1. **Long Straddle (P100 + C100):**
   - **Hai điểm hòa vốn:** $S_{BE,\text{low}} = 100 - 12 = \mathbf{\text{USD } 88.00}$ và $S_{BE,\text{high}} = 100 + 12 = \mathbf{\text{USD } 112.00}$.
   - **Mức lỗ tối đa:** **USD 1,200.00** (xảy ra khi $S_T = \text{USD } 100$).
2. **Long Strangle (P90 + C110):**
   - **Hai điểm hòa vốn:** $S_{BE,\text{low}} = 90 - 5 = \mathbf{\text{USD } 85.00}$ và $S_{BE,\text{high}} = 110 + 5 = \mathbf{\text{USD } 115.00}$.
   - **Mức lỗ tối đa:** **USD 500.00** (xảy ra với mọi $90 \le S_T \le 110$).

#### **c. Lựa chọn theo hạn mức lỗ USD 600 & Bản chất sự đánh đổi (Economic Trade-off)**
- **Chiến lược đáp ứng hạn mức:** Với giới hạn lỗ tối đa chấp nhận được là USD 600, **chỉ có chiến lược Strangle (mua Put 90 và Call 110)** đạt yêu cầu (vì lỗ tối đa chỉ là $\text{USD } 500 \le \text{USD } 600$, trong khi Straddle có thể lỗ tới $\text{USD } 1,200 > \text{USD } 600$).
- **Sự đánh đổi thể hiện qua câu a:**
  - Chọn **Strangle** dùng các quyền chọn OTM giúp **giảm mạnh chi phí đầu tư ban đầu và giới hạn mức lỗ xấu nhất xuống thấp hơn nhiều** (tiết kiệm được USD 700, chỉ lỗ USD 500 thay vì USD 1,200 nếu giá đứng yên tại USD 100).
  - **Cái giá phải trả:** Strangle tạo ra một "vùng chết" rộng từ USD 90 đến USD 110 và **đòi hỏi giá cổ phiếu phải biến động biên độ lớn hơn hẳn mới bắt đầu có lãi** (cần vượt ngoài hành lang $[\text{USD } 85, \text{USD } 115]$ thay vì $[\text{USD } 88, \text{USD } 112]$). Cụ thể trong câu a, với mức biến động vừa phải $\pm \text{USD } 14$ (về USD 86 hoặc lên USD 114), **Straddle đã có lãi $+\text{USD } 200$ trong khi Strangle vẫn bị lỗ $-\text{USD } 100$**!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Công thức Hòa Vốn Tổng Quát cho cả Straddle (trường hợp riêng $K_P = K_C = K$) lẫn Strangle ($K_P < K_C$):**
  - Gọi $D = p + c$ là tổng phí quyền chọn trên 1 cổ phiếu:
  - $\text{Max Loss} = 100 \times D$
  - $\text{Break-evens} = \left(K_P - D,\; K_C + D\right)$
  - Straddle: $(100 - 12, 100 + 12) = (88, 112)$; Strangle: $(90 - 5, 110 + 5) = (85, 115)$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy cộng trừ phí của từng chân riêng lẻ khi tính Break-even của Strangle:** Tuyệt đối KHÔNG lấy $90 - 2 = 88$ và $110 + 3 = 113$! Khi một đầu ITM tại đáo hạn, nhà đầu tư vẫn phải bù đắp **tổng chi phí của CẢ HAI quyền chọn ($2 + 3 = 5$)**, nên điểm hòa vốn bắt buộc là $90 - 5 = 85$ và $110 + 5 = 115$!

---

## Question 20 (Average) — Vi Phạm Cận Dưới Quyền Chọn Mua & Arbitrage Khai Thác
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Zeta shares trade at USD 100. All options below are European, expire in one year and are quoted per share. The risk-free borrowing and lending rate is 10% effective annually.
>
> | Option | Strike | Premium |
> |---|---:|---:|
> | Call | USD 90 | USD 17 |
> | Call | USD 110 | USD 9 |
> | Put | USD 110 | USD 9 |
>
> Shares and options may be bought or sold short. Short-sale proceeds are fully available for investment, and there are no margin requirements.
>
> a. Identify any pricing inconsistency. Explain which quoted prices satisfy the relevant individual bounds and check parity for the matching pair.
>
> b. Construct a self-financing trade exploiting the inconsistency. Show initial and terminal cash flows and determine the minimum terminal profit per share.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 100$, kỳ hạn $T = 1$ năm, lãi suất vay & cho vay $r = 10\%$ EAR.
- Giá niêm yết trên 1 cổ phiếu: $C(90) = \text{USD } 17$; $C(110) = \text{USD } 9$; $P(110) = \text{USD } 9$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Kiểm tra các cận riêng lẻ (Individual Bounds), Kiểm tra Parity & Chỉ ra điểm vô lý**
1. **Kiểm tra cận của từng quyền chọn châu Âu (trên cổ phiếu không cổ tức):**
   - Với Call châu Âu: $\max\left(0,\; S_0 - \frac{K}{1+r}\right) \le C(K) \le S_0$.
   - Với Put châu Âu: $\max\left(0,\; \frac{K}{1+r} - S_0\right) \le P(K) \le \frac{K}{1+r}$.
   - **Xét Call strike USD 90 ($C_{90} = 17$):**
     - Cận trên: $S_0 = \text{USD } 100$ (thỏa mãn).
     - Cận dưới không-arbitrage:
       $$C_{90} \ge \max\left(0,\; 100 - \frac{90}{1.10}\right) = 100 - 81.818182 = \mathbf{\text{USD } 18.181818 \approx \text{USD } 18.18}$$
     - **PHÁT HIỆN SAI LỆCH ĐỊNH GIÁ (Pricing Inconsistency):** Giá niêm yết $C(90) = \text{USD } 17.00 < \text{USD } 18.18$ **VI PHẠM CẬN DƯỚI CỦA QUYỀN CHỌN MUA CHÂU ÂU** (bị định giá quá thấp một khoảng $\text{USD } 1.1818$/cp)!
   - **Xét Call strike USD 110 ($C_{110} = 9$):**
     - Cận dưới $= \max(0,\; 100 - 110/1.10) = \max(0,\; 0) = \text{USD } 0$; cận trên $= \text{USD } 100$. Vì $0 \le 9 \le 100$, **$C(110) = 9$ thỏa mãn hoàn toàn các cận riêng lẻ**.
   - **Xét Put strike USD 110 ($P_{110} = 9$):**
     - Cận dưới $= \max(0,\; 110/1.10 - 100) = \max(0,\; 0) = \text{USD } 0$; cận trên $= 110/1.10 = \text{USD } 100$. Vì $0 \le 9 \le 100$, **$P(110) = 9$ thỏa mãn hoàn toàn các cận riêng lẻ**.
2. **Kiểm tra Put-Call Parity cho cặp cùng strike $K = 110$:**
   - Vế trái: $C(110) - P(110) = 9.00 - 9.00 = \text{USD } 0.00$.
   - Vế phải: $S_0 - \frac{110}{1.10} = 100.00 - 100.00 = \text{USD } 0.00$.
   - **Kết luận:** Cặp quyền chọn tại $K = 110$ **thỏa mãn chính xác tuyệt đối Put-Call Parity**! *(Lưu ý thêm: chênh lệch giá giữa hai Call $C(90) - C(110) = 8$ cũng thỏa mãn $0 \le 8 \le (110-90)/1.10 = 18.18$; như vậy mâu thuẫn định giá nằm trọn ở việc $C(90) = 17$ thấp hơn cận dưới $S_0 - PV(90) = 18.18$!)*

#### **b. Thiết lập Giao dịch Tự Tài Trợ (Self-Financing Arbitrage) Khai Thác $C(90)$ Rẻ**
Vì $C(90) < S_0 - PV(90) \iff C(90) + PV(90) < S_0$, ta **Mua vế rẻ (Long Call 90 + Cho vay tiền) và Bán vế đắt (Short 1 cổ phiếu Zeta)** sao cho dòng tiền ban đầu bằng $0$:
- **Hôm nay ($t = 0$, tính trên 1 cổ phiếu):**
  1. **Mua 1 quyền chọn mua Call($K=90$):** $-\text{USD } 17.00$.
  2. **Bán khống 1 cổ phiếu Zeta:** $+\text{USD } 100.00$.
  3. **Cho vay / Gửi tiết kiệm toàn bộ số tiền ròng thu được USD 83.00** kỳ hạn 1 năm tại lãi suất $10\%$ EAR: $-\text{USD } 83.00$.
  - **Tổng dòng tiền ròng ban đầu ($t = 0$):** $-17.00 + 100.00 - 83.00 = \mathbf{\text{USD } 0.00}$ (*tự tài trợ hoàn hảo!*).
- **Tại ngày đáo hạn ($T = 1$):** Khoản tiền gửi USD 83.00 sinh lời thành $83.00 \times 1.10 = \mathbf{+\text{USD } 91.30}$.

| Hạng mục danh mục (trên 1 cổ phiếu) | Hôm nay ($t = 0$) | Đáo hạn nếu $S_T \le 90$ | Đáo hạn nếu $S_T > 90$ |
|---|---:|---:|---:|
| 1. Long 1 Call ($K = 90$) | $-17.00$ | $0.00$ *(bỏ quyền chọn)* | Thực hiện quyền mua 1 cp với giá $-90.00$ *(hoặc nhận $+S_T - 90$)* |
| 2. Short 1 cổ phiếu Zeta (mua trả kho tại $T$) | $+100.00$ | Mua trên sàn giá $-S_T$ | Lấy cổ phiếu vừa thực hiện Call trả kho *(hoặc $-S_T$)* |
| 3. Thu hồi gốc + lãi gửi tiết kiệm ($83 \times 1.10$) | $-83.00$ | $+91.30$ | $+91.30$ |
| **Tổng dòng tiền ròng cuối kỳ** | **USD 0.00** | **$91.30 - S_T = 1.30 + (90 - S_T) \ge +\text{USD } 1.30$** | **$91.30 - 90.00 =$ +USD 1.30** |

- **Lợi nhuận cuối kỳ tối thiểu trên mỗi cổ phiếu (*Minimum terminal profit per share*):**
  - Khi $S_T \ge 90$: Lợi nhuận chắc chắn bằng **USD 1.30/cổ phiếu**.
  - Khi $S_T < 90$: Lợi nhuận còn cao hơn nữa ($1.30 + (90 - S_T) > 1.30$, lên tới tối đa USD 91.30 nếu $S_T = 0$)!
  - Vậy lợi nhuận đáo hạn tối thiểu được bảo đảm là **USD 1.30 per share**!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Kiểm tra chéo đáp số Minimum Profit trong 3 giây:**
  - Mức vi phạm cận dưới tại $t = 0$ là: $(100 - 90/1.10) - 17 = \frac{13}{11} = \text{USD } 1.181818$.
  - Khi thiết lập giao dịch tự tài trợ ($CF_0 = 0$), giá trị tương lai của phần chênh lệch đó tại $T = 1$ chính là lợi nhuận tối thiểu: $\frac{13}{11} \times 1.10 = 1.30 = \mathbf{\text{USD } 1.30}$! (Và phần trội thêm $\max(90 - S_T, 0)$ chính là một quyền chọn bán Put(90) được tặng miễn phí nhờ tính đối ngẫu Put-Call Parity!).

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Nhầm cận dưới Call châu Âu là $S_0 - K = 100 - 90 = 10$):** Nếu tính $100 - 90 = 10$ rồi thấy $17 > 10$ sẽ phán bừa "không có vi phạm nào"! Nhớ khắc cốt ghi tâm: Cận dưới của Call châu Âu trên cổ phiếu không trả cổ tức là **$S_0 - PV(K) = 100 - 90/1.10 = 18.18 > S_0 - K$**!
- **Bẫy 2 (Không đảm bảo Self-Financing tại $t = 0$):** Đề yêu cầu *"Construct a **self-financing** trade"* (dòng tiền ròng tại $t=0$ phải bằng $0$). Vì vậy không được gửi tiết kiệm chỉ $PV(90) = 81.82$ để bỏ túi USD 1.18 hôm nay, mà phải đem gửi toàn bộ **USD 83.00** để thu toàn bộ lãi tại thời điểm cuối kỳ (**tối thiểu USD 1.30**)!

---

## Question 21 (Average) — Thiết Kế Payoff Hình Nón Bằng Quyền Chọn Mua (Long Call Butterfly Spread)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Eta shares trade at USD 90. Three calls have the same expiration and the following premiums. The risk-free rate is zero.
>
> | Strike | Premium per share |
> |---|---:|
> | USD 80 | USD 13 |
> | USD 90 | USD 7 |
> | USD 100 | USD 3 |
>
> Theta wants the following terminal payoff, measured in USD. It is linear between the listed stock prices and zero for all $S_T\leq80$ and $S_T\geq100$.
>
> | Terminal share price | USD 80 | USD 90 | USD 100 |
> |---|---:|---:|---:|
> | Target payoff | 0 | 10 | 0 |
>
> a. Construct this payoff using only the three calls. State the signed number of options on one share at each strike.
>
> b. Calculate the initial cost, maximum profit, maximum loss and break-even share prices.

**Tóm tắt thông số:**
- Giá cổ phiếu hiện tại $S_0 = \text{USD } 90$; $r = 0$. Ba quyền chọn Call cùng đáo hạn: $C(80) = 13$, $C(90) = 7$, $C(100) = 3$.
- Hàm payoff mục tiêu (tuyến tính từng khúc): bằng $0$ với $S_T \le 80$; tăng bậc nhất lên $10$ tại $S_T = 90$; giảm bậc nhất về $0$ tại $S_T = 100$; và giữ nguyên bằng $0$ với mọi $S_T \ge 100$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Thiết lập Payoff chỉ từ 3 quyền chọn Call (Phương pháp Bước nhảy Độ dốc — Slope Change Rule)**
- Ta tính độ dốc (đạo hàm theo $S_T$) của hàm payoff mục tiêu trên từng khoảng giá:
  1. Khoảng $S_T < 80$: $\text{Payoff} = 0 \implies \text{Độ dốc } s_0 = 0$.
  2. Khoảng $80 < S_T < 90$: Tăng từ $0$ lên $10$ qua khoảng rộng $10 \implies \text{Độ dốc } s_1 = \frac{10 - 0}{90 - 80} = +1$.
  3. Khoảng $90 < S_T < 100$: Giảm từ $10$ về $0$ qua khoảng rộng $10 \implies \text{Độ dốc } s_2 = \frac{0 - 10}{100 - 90} = -1$.
  4. Khoảng $S_T > 100$: $\text{Payoff} = 0 \implies \text{Độ dốc } s_3 = 0$.
- Vì mỗi đơn vị $\text{Call}(K)$ có độ dốc $0$ bên trái $K$ và $+1$ bên phải $K$, số lượng có dấu quyền chọn Call tại mỗi strike bằng đúng **mức thay đổi độ dốc $\Delta s$ tại điểm gãy đó**:
  - **Tại Strike USD 80:** $n_{80} = s_1 - s_0 = (+1) - 0 = \mathbf{+1}$ (Mua 1 Call strike USD 80).
  - **Tại Strike USD 90:** $n_{90} = s_2 - s_1 = (-1) - (+1) = \mathbf{-2}$ (Viết/Bán 2 Call strike USD 90).
  - **Tại Strike USD 100:** $n_{100} = s_3 - s_2 = 0 - (-1) = \mathbf{+1}$ (Mua 1 Call strike USD 100).
- **Kiểm chứng đại số trên cả 4 miền:**
  - $S_T \le 80$: $0 - 0 + 0 = 0$.
  - $80 < S_T \le 90$: $(S_T - 80) - 0 + 0 = S_T - 80$ (tại $S_T = 90$ bằng $10$).
  - $90 < S_T \le 100$: $(S_T - 80) - 2(S_T - 90) + 0 = 100 - S_T$ (tại $S_T = 100$ bằng $0$).
  - $S_T > 100$: $(S_T - 80) - 2(S_T - 90) + (S_T - 100) = (1 - 2 + 1)S_T + (-80 + 180 - 100) = 0$. *(Khớp 100%!)*

#### **b. Chi phí ban đầu, Lợi nhuận tối đa, Mức lỗ tối đa & Các mức giá hòa vốn**
1. **Chi phí ròng ban đầu (*Initial cost*):**
   $$\text{Initial Cost} = (+1)(13) + (-2)(7) + (+1)(3) = 13 - 14 + 3 = \mathbf{\text{USD } 2.00\text{ per share}}$$
   *(Phản ánh tính lồi của giá Call theo strike: $C(90) = 7 < \frac{13 + 3}{2} = 8$ nên Butterfly luôn có chi phí dương!).*
2. **Lợi nhuận tối đa (*Maximum profit*):** Đạt đỉnh tại $S_T = \text{USD } 90$:
   $$\Pi_{\max} = \text{Max Payoff} - \text{Initial Cost} = 10.00 - 2.00 = \mathbf{\text{USD } 8.00\text{ per share}}$$
3. **Mức lỗ tối đa (*Maximum loss*):** Xảy ra với mọi $S_T \le 80$ hoặc $S_T \ge 100$ (khi payoff $= 0$):
   $$\text{Max Loss} = \text{Initial Cost} = \mathbf{\text{USD } 2.00\text{ per share}}$$
4. **Hai mức giá cổ phiếu hòa vốn (*Break-even share prices*):**
   - Nhánh trái ($80 \le S_T \le 90$): $(S_T - 80) - 2.00 = 0 \implies S_{BE,1} = \mathbf{\text{USD } 82.00}$.
   - Nhánh phải ($90 \le S_T \le 100$): $(100 - S_T) - 2.00 = 0 \implies S_{BE,2} = \mathbf{\text{USD } 98.00}$.

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Thuật toán "Đạo hàm Cấp 2 Rời rạc" giải mọi bài Thiết kế Payoff Quyền chọn trong 10 giây:**
  - Nếu đề cho đỉnh ở $K_2$ cao $H$ và hai chân $K_1, K_3$ đối xứng cách đều khoảng $W = K_2 - K_1 = K_3 - K_2$:
  - Tỷ lệ quyền chọn luôn là $\frac{H}{W} \times (+1,\; -2,\; +1)$! Ở đây $H = 10, W = 10 \implies \frac{10}{10}(+1, -2, +1) = (+1, -2, +1)$! (Nếu đề đổi đỉnh thành USD 25 trên khoảng rộng 10 thì nhân $2.5$ ra $+2.5, -5, +2.5$ ngay lập tức!).
  - Hai điểm hòa vốn luôn nằm cách hai mép ngoài một đoạn đúng bằng $\text{Cost} / \text{Slope} = 2 / 1 = 2$: $80 + 2 = 82$ và $100 - 2 = 98$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy bán 1 Call(90) thay vì bán 2 Call(90):** Nếu chỉ bán 1 Call(90), độ dốc sau mốc 90 chỉ giảm từ $+1$ về $0$ (đi ngang như Bull Spread) chứ không thể gập xuống $-1$ để quay về $0$ tại mốc 100! Phải bán **$-2$** Call ở strike giữa!

---

## Question 22 (Average) — Thực Hiện Sớm Quyền Chọn Mua Kiểu Mỹ Trước Ngày Giao Dịch Không Hưởng Quyền
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Iota holds an American call immediately before the stock goes ex-dividend.
>
> | Item | Value |
> |---|---:|
> | Share price before the dividend | USD 92.60 |
> | Cash dividend paid immediately | USD 1.60 |
> | Call strike | USD 80 |
> | Time remaining after the dividend | Six months |
> | Risk-free rate | 4% effective annually |
> | Matching European put value immediately after the dividend | USD 0.25 |
>
> Assume the ex-dividend share price falls by exactly the cash dividend, with no other simultaneous change. No further dividends are due. The put has the same strike and expiration as the call.
>
> Kappa advises immediate exercise because the dividend exceeds the interest forgone by paying the strike now.
>
> a. Assess Kappa's advice by comparing exercise and continuation values.
>
> b. For an otherwise identical case with the same post-dividend share price and put value, find the dividend that makes the holder indifferent. The pre-dividend share price adjusts to equal the post-dividend price plus that dividend.

**Tóm tắt thông số:**
- Giá cổ phiếu ngay trước chia cổ tức (*cum-dividend*): $S_{\text{cum}} = \text{USD } 92.60$; cổ tức tiền mặt trả ngay $D = \text{USD } 1.60 \implies$ Giá ngay sau chia cổ tức (*ex-dividend*): $S_{\text{ex}} = 92.60 - 1.60 = \text{USD } 91.00$.
- Strike $K = \text{USD } 80$; thời gian còn lại $\tau = 6/12 = 0.50$ năm; $r = 4\%$ EAR; không còn đợt chia cổ tức nào khác.
- Giá Put châu Âu tương ứng ngay sau khi chia cổ tức: $P_{\text{ex}} = \text{USD } 0.25$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. So sánh Giá trị Thực hiện Ngay (Exercise Value) và Giá trị Tiếp tục Nắm giữ (Continuation Value) & Đánh giá lời khuyên của Kappa**
1. **Giá trị thực hiện ngay lập tức trước thời điểm không hưởng quyền (*Immediate exercise value*):**
   $$V_{\text{exercise}} = S_{\text{cum}} - K = 92.60 - 80.00 = \mathbf{\text{USD } 12.60}$$
2. **Giá trị tiếp tục nắm giữ qua thời điểm chia cổ tức (*Continuation value*):**
   - Ngay sau khi cổ phiếu giao dịch không hưởng quyền tại $S_{\text{ex}} = \text{USD } 91.00$, cổ phiếu **không còn đợt chia cổ tức nào nữa** cho đến lúc đáo hạn 6 tháng sau. Vì quyền chọn mua kiểu Mỹ trên cổ phiếu không trả cổ tức không bao giờ tối ưu khi thực hiện sớm (khi $r > 0$), giá trị quyền chọn mua kiểu Mỹ ngay sau chia cổ tức **bằng đúng giá trị quyền chọn mua kiểu châu Âu tương ứng** ($C_{\text{Amer, ex}} = C_{\text{Eur, ex}}$).
   - Áp dụng Put-Call Parity tại thời điểm ngay sau chia cổ tức:
     $$V_{\text{continuation}} = C_{\text{Eur, ex}} = S_{\text{ex}} + P_{\text{ex}} - \frac{K}{(1 + r)^{0.50}} = 91.00 + 0.25 - \frac{80.00}{(1.04)^{0.50}}$$
   - Tính chính xác: $\frac{80.00}{(1.04)^{0.50}} = \frac{80.00}{1.01980390} = \text{USD } 78.446454$.
     $$V_{\text{continuation}} = 91.25 - 78.446454 = \mathbf{\text{USD } 12.803546 \approx \text{USD } 12.80}$$
3. **Đánh giá lời khuyên của Kappa:**
   - Vì $V_{\text{continuation}} (\text{USD } 12.80) > V_{\text{exercise}} (\text{USD } 12.60)$, **lời khuyên thực hiện sớm của Kappa là SAI — Iota KHÔNG nên thực hiện sớm (nên tiếp tục giữ quyền chọn)**! Thực hiện ngay sẽ làm mất đi $12.803546 - 12.60 = \text{USD } 0.203546 \approx \text{USD } 0.20$/cổ phiếu!
   - **Tại sao lập luận của Kappa bị thiếu sót?** Đúng là cổ tức ($D = \text{USD } 1.60$) lớn hơn phần tiền lãi mất đi do phải trả strike sớm ($K - PV(K) = 80 - 78.446454 = \text{USD } 1.553546 \approx \text{USD } 1.55$). Tuy nhiên, Kappa **bỏ quên giá trị bảo hiểm rủi ro giảm giá (*downside protection / put option value*) $P_{\text{ex}} = \text{USD } 0.25$** bị mất trắng khi biến quyền chọn thành cổ phiếu! Thực hiện sớm chỉ tối ưu khi cổ tức vượt qua **tổng** của lãi tiền mặt bị mất **CỘNG VỚI** giá trị quyền chọn bán bảo hiểm còn lại!

#### **b. Mức cổ tức bàng quan ($D^*$) khi giữ nguyên $S_{\text{ex}} = 91.00$ và $P_{\text{ex}} = 0.25$**
Với $S_{\text{cum}} = S_{\text{ex}} + D^*$, người nắm giữ bàng quan giữa thực hiện ngay và giữ tiếp khi:
$$V_{\text{exercise}} = V_{\text{continuation}} \iff (S_{\text{ex}} + D^*) - K = S_{\text{ex}} + P_{\text{ex}} - \frac{K}{(1.04)^{0.50}}$$
Giản ước $S_{\text{ex}}$ ở hai vế:
$$D^* = \underbrace{\left[K - \frac{K}{(1.04)^{0.50}}\right]}_{\text{Tiền lãi mất đi } = 1.553546} + \underbrace{P_{\text{ex}}}_{\text{Giá trị bảo hiểm mất đi } = 0.25} = 1.553546 + 0.25 = \mathbf{\text{USD } 1.803546 \approx \text{USD } 1.80}$$

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ (CORE CONCEPTUAL TAKEAWAY):**
> 1. **Không có cổ tức ($D = 0, r \ge 0$):** KHÔNG BAO GIỜ thực hiện sớm American Call $\implies C_{\text{Amer}} = C_{\text{Eur}}$.
> 2. **Có cổ tức rời rạc:** Chỉ có thể tối ưu thực hiện sớm **ngay sát trước thời điểm không hưởng quyền (*immediately before an ex-dividend instant*)**, và điều kiện CẦN VÀ ĐỦ ở kỳ cổ tức cuối cùng là:
>    $$D > \left[K - PV(K)\right] + P_{\text{ex}}$$
>    Trong đó $D > K - PV(K)$ chỉ mới là điều kiện **cần** (nếu $D \le K - PV(K)$ thì chắc chắn KHÔNG thực hiện sớm ngay cả khi $P_{\text{ex}} \approx 0$), còn muốn đủ phải thắng cả $P_{\text{ex}}$!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Công thức siêu gọn tính thẳng **Lợi ích Ròng của Tiếp tục Nắm giữ so với Thực hiện Sớm** mà không cần cộng trừ qua $S_{\text{ex}}$:
  $$V_{\text{cont}} - V_{\text{ex}} = \left[K - PV(K)\right] + P_{\text{ex}} - D = 1.553546 + 0.25 - 1.60 = +\text{USD } 0.203546 > 0 \implies \text{HOLD!}$$
  Và đặt biểu thức này bằng $0$ rút ra ngay lập tức $D^* = 1.553546 + 0.25 = \mathbf{\text{USD } 1.80}$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Tin vào quy tắc ngón tay cái nửa vời $D > K - PV(K)$):** Rất nhiều sinh viên chỉ tính $80 - 80/1.04^{0.5} = 1.55 < 1.60$ rồi gật đầu đồng ý với Kappa! Đó là bẫy kinh điển: $K - PV(K)$ chỉ mới tính chi phí tài chính của tiền mặt, bỏ sót chi phí mất quyền bảo hiểm $P_{\text{ex}} = 0.25$!
- **Bẫy 2 (Lấy $S_{\text{cum}} = 92.60$ thay vào Put-Call Parity thay vì $S_{\text{ex}} = 91.00$):** $P_{\text{ex}} = 0.25$ được đo **ngay sau** chia cổ tức, nên trong Parity bắt buộc phải ghép với $S_{\text{ex}} = 91.00$!

---

## Question 23 (Average) — Ảnh Hưởng Của Kỳ Hạn & Lãi Suất Lên Quyền Chọn Châu Âu vs. Mỹ
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Lambda compares options on the same non-dividend-paying stock. Use the lecture's standard pricing assumptions and nonnegative interest rates.
>
> Assess each statement and give the economic reasoning.
>
> a. "A twelve-month American put cannot cost less than a six-month American put with the same strike. Therefore, the same maturity ordering must hold for European puts."
>
> b. "If the risk-free rate rises while the other pricing inputs remain unchanged, both European calls and European puts become more valuable because money grows faster."

**Tóm tắt thông số:**
- Cổ phiếu cơ sở **không trả cổ tức**, giả định định giá tiêu chuẩn, lãi suất phi rủi ro $r \ge 0$.
- Đánh giá tính Đúng/Sai và giải thích bản chất kinh tế của hai phát biểu về **Maturity (Theta)** và **Interest Rate (Rho)**.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Đánh giá phát biểu về thứ tự giá theo kỳ hạn của American Put vs. European Put**
- **Vế đầu (*"A 12-month American put cannot cost less than a 6-month American put with the same strike"*) là ĐÚNG (TRUE):**
  - Quyền chọn kiểu Mỹ cho phép thực hiện tại **bất kỳ thời điểm nào** cho tới ngày đáo hạn. Một American Put 12 tháng bao hàm **toàn bộ tập hợp quyền thực hiện** của American Put 6 tháng (người giữ hợp đồng 12 tháng hoàn toàn có thể bắt chước mọi chiến lược thực hiện trong 6 tháng đầu) **cộng thêm** quyền được tiếp tục chờ và thực hiện trong khoảng từ tháng 6 đến tháng 12. Vì quyền lựa chọn tăng thêm mà không kèm nghĩa vụ không bao giờ có giá trị âm, luôn có $P_{\text{Amer}}(12\text{m}) \ge P_{\text{Amer}}(6\text{m})$.
- **Vế suy luận thứ hai (*"Therefore, the same maturity ordering must hold for European puts"*) là SAI (FALSE):**
  - Quyền chọn châu Âu **chỉ được phép thực hiện đúng vào ngày đáo hạn cuối cùng** (tập cơ hội thực hiện ở tháng 12 KHÔNG chứa thời điểm tháng 6!).
  - Khi kéo dài kỳ hạn của European Put từ 6 tháng lên 12 tháng (với $r > 0$), có **hai lực tác động ngược chiều nhau**:
    1. *Hiệu ứng biến động dương (Volatility / Time-dispersion effect $> 0$):* Thêm thời gian giúp biên độ dao động giá cổ phiếu rộng hơn.
    2. *Hiệu ứng chiết khấu giá thực hiện âm (Time-value-of-money / Discounting drag $< 0$):* Người mua Put khi thực hiện sẽ **nhận về số tiền cố định $K$** (bị chặn trần tối đa là $K$). Việc bị buộc phải chờ thêm 6 tháng nữa mới được nhận tiền mặt $K$ làm giảm giá trị hiện tại $PV(K) = K e^{-rT}$ (mất tiền lãi trên khoản tiền $K$).
  - Khi quyền chọn bán đang **ở trạng thái lãi sâu (*deep in-the-money*, $S_0 \ll K$)** và lãi suất $r > 0$, khả năng cổ phiếu bật tăng vượt lên trên $K$ là rất nhỏ (lợi ích biến động thêm gần bằng 0), trong khi thiệt hại do bị hoãn nhận tiền mặt $K$ thêm 6 tháng rất lớn $\implies$ **Một European Put 12 tháng hoàn toàn CÓ THỂ RẺ HƠN một European Put 6 tháng cùng strike!** (Theta của European Put deep-ITM mang dấu dương, nghĩa là càng xa đáo hạn càng rẻ!).

#### **b. Đánh giá phát biểu về tác động của việc tăng lãi suất phi rủi ro ($r \uparrow$) lên European Call và European Put**
- **Phát biểu là SAI (FALSE): Đúng với European Call, nhưng NGƯỢC HOÀN TOÀN đối với European Put!**
- **Giải thích kinh tế (giữ nguyên giá cổ phiếu hiện tại $S_0$ và các đầu vào khác):**
  - Khi lãi suất phi rủi ro $r$ tăng, giá trị hiện tại của khoản thanh toán giá thực hiện tại đáo hạn $PV(K) = K e^{-rT}$ **giảm xuống** (đồng thời dưới xác suất trung hòa rủi ro, tốc độ tăng trưởng kỳ vọng của cổ phiếu $r$ cao hơn đẩy phân phối $S_T$ dịch lên trên):
  1. **Đối với European Call ($\rho_C = \frac{\partial C}{\partial r} > 0$ — ĐẮT LÊN):** Người giữ Call là người sẽ **chi trả tiền mặt $K$** tại ngày đáo hạn để mua cổ phiếu. Lãi suất cao hơn làm giảm giá trị hiện tại của khoản chi $PV(K)$ (lợi ích trì hoãn thanh toán: giữ tiền mặt gửi lấy lãi suất cao hơn trong thời gian chờ đáo hạn có lợi hơn so với mua đứt cổ phiếu ngay hôm nay). Do đó **European Call có giá trị cao hơn**.
  2. **Đối với European Put ($\rho_P = \frac{\partial P}{\partial r} < 0$ — RẺ ĐI):** Người giữ Put là người sẽ **thu về tiền mặt $K$** tại ngày đáo hạn khi bán cổ phiếu. Lãi suất cao hơn làm giảm giá trị hiện tại của khoản tiền $PV(K)$ sẽ nhận trong tương lai (chi phí cơ hội của việc phải chờ đến ngày đáo hạn mới nhận được tiền mặt $K$ để đem đi gửi lãi cao lớn hơn). Do đó **European Put mất giá trị khi lãi suất tăng**!

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ (BẢNG DẤU GREEKS & KỲ HẠN CẦN THUỘC LÒNG):**
> | Biến số tăng ($\uparrow$) | European Call | American Call (không cổ tức) | European Put | American Put |
> |---|---|---|---|---|
> | **Thời gian còn lại $T \uparrow$** | **Tăng ($+$)** *(không giảm)* | **Tăng ($+$)** *(bằng Eur Call)* | **Không xác định ($+/-$)** *(Deep ITM với $r>0$ có thể GIẢM!)* | **Tăng ($+$)** *(không bao giờ giảm!)* |
> | **Lãi suất $r \uparrow$ (Rho)** | **Tăng ($+$)** | **Tăng ($+$)** | **Giảm ($-$)** | **Giảm ($-$)** |
> | **Độ biến động $\sigma \uparrow$ (Vega)** | **Tăng ($+$)** | **Tăng ($+$)** | **Tăng ($+$)** | **Tăng ($+$)** |

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Kiểm chứng câu 23a chỉ bằng 1 trường hợp cực hạn siêu thuyết phục ($S_0 = 0, r > 0$): Nếu công ty đã phá sản giá $S_0 = 0$, American Put trả ngay $K$ cho cả 6m lẫn 12m; còn European Put buộc phải đợi đến đáo hạn nên giá là $K e^{-0.5r}$ (6 tháng) $> K e^{-1.0r}$ (12 tháng)! Chỉ 1 dòng toán học chứng minh ngay $P_{\text{Eur}}(12\text{m}) < P_{\text{Eur}}(6\text{m})$!
- Kiểm chứng câu 23b qua Put-Call Parity: $C - P = S_0 - K e^{-rT}$. Khi $r \uparrow$, vế phải tăng; vì $C$ chỉ nhận payoff dương ở nhánh cao và hưởng lợi từ giảm $PV(K)$ ($C \uparrow$), còn với Put (xét tại $S_0 \to 0$: $P = K e^{-rT}$ giảm rõ rệt khi $r \uparrow$), nên $C$ tăng còn $P$ giảm!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy tư duy thông thường "nhiều thời gian hơn thì quyền chọn luôn đắt hơn":** Quy luật đó **chỉ luôn đúng tuyệt đối cho quyền chọn kiểu Mỹ** (và đúng cho Call châu Âu trên cổ phiếu **không trả cổ tức** với $r \ge 0$). Nó **SAI** với **European Put** (do mất lãi trên $K$) và cũng **SAI** với **European Call trên cổ phiếu CÓ trả cổ tức lớn** (nếu đợt cổ tức khủng rơi vào giữa tháng 6 và tháng 12, Call châu Âu 12m có thể rẻ hơn Call châu Âu 6m!).

---

## Question 24 (Hard) — Định Giá Quyền Chọn Bán Trên Cây Nhị Phân & Thiết Kế Chiến Lược Cổ Áo (Collar)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Mu owns 1,000 Nu shares, currently worth USD 50 each. Over each of the next two three-month periods, the share price rises by 20% or falls by 20%. The risk-free rate is zero.
>
> The following European options expire in six months. Each contract covers 100 shares. Treat the quoted premiums as consistent with the tree.
>
> | Option | Strike | Premium per share |
> |---|---:|---:|
> | Put | USD 46 | USD 3.50 |
> | Put | USD 50 | Unknown |
> | Call | USD 56 | USD 4.00 |
> | Call | USD 64 | USD 2.00 |
>
> Mu wants the combined shares and options to be worth at least USD 50,000 at expiration and can spend at most USD 2,000 in net option premiums. Mu must retain all shares and buy one put per share. Mu may also write one call per share, using a single strike for each leg; mixing strikes or changing the option-to-share ratios is not permitted.
>
> a. Value the USD 50 put using the tree.
>
> b. Identify a permitted strategy meeting the floor and premium budget. State contract quantities, net premium cost, terminal floor and upside cap.
>
> c. Compare the chosen strategy with buying the USD 50 puts alone. Quantify the premium saving and explain what Mu gives up.

**Tóm tắt thông số:**
- Mu đang sở hữu **1,000 cổ phiếu Nu** giá $S_0 = \text{USD } 50$ (giá trị hiện tại USD 50,000).
- Cây nhị phân 2 bước (mỗi bước 3 tháng, tổng 6 tháng): $u = 1.20$, $d = 0.80$, lãi suất $r = 0 \implies R = 1.00$.
- Mỗi hợp đồng quyền chọn = **100 cổ phiếu** $\implies$ Tỷ lệ 1 quyền chọn/cổ phiếu tương ứng **10 hợp đồng** cho mỗi chân!
- Ràng buộc thiết kế:
  1. Giá trị danh mục (cổ phiếu + quyền chọn) lúc đáo hạn $\ge \text{USD } 50,000$ (tức $\ge \text{USD } 50$/cp ở mọi trạng thái).
  2. Chi phí phí quyền chọn ròng ban đầu $\le \text{USD } 2,000$ (tức $\le \text{USD } 2.00$/cp).
  3. Giữ nguyên 1,000 cổ phiếu; bắt buộc mua 1 Put/cp (chọn 1 strike duy nhất: 46 hoặc 50) và có thể bán 1 Call/cp (chọn 1 strike duy nhất: 56 hoặc 64).

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Định giá quyền chọn bán Put strike USD 50 bằng cây nhị phân**
- Xác suất tăng trung hòa rủi ro mỗi bước 3 tháng (với $R = 1.00$):
  $$p = \frac{R - d}{u - d} = \frac{1.00 - 0.80}{1.20 - 0.80} = \frac{0.20}{0.40} = \mathbf{0.50} \quad (1 - p = 0.50)$$
- Cây giá cổ phiếu:
  - $t = 0$: $S_0 = 50$.
  - $t = 3\text{m}$: $S_u = 50(1.20) = 60$; $S_d = 50(0.80) = 40$.
  - $t = 6\text{m}$ (đáo hạn):
    - $S_{uu} = 60(1.20) = \text{USD } 72.00$ (xác suất $p^2 = 0.25$).
    - $S_{ud} = S_{du} = 50(1.20)(0.80) = \text{USD } 48.00$ (tổng xác suất $2p(1-p) = 0.50$).
    - $S_{dd} = 40(0.80) = \text{USD } 32.00$ (xác suất $(1-p)^2 = 0.25$).
- Payoff đáo hạn của $\text{Put}(K = 50)$:
  - $P_{uu} = \max(50 - 72, 0) = \text{USD } 0.00$.
  - $P_{ud} = \max(50 - 48, 0) = \text{USD } 2.00$.
  - $P_{dd} = \max(50 - 32, 0) = \text{USD } 18.00$.
- Chiết khấu ngược về hiện tại (với $R = 1.00$):
  - Tại $t = 3\text{m}$: $P_u = 0.50(0) + 0.50(2.00) = \text{USD } 1.00$; $P_d = 0.50(2.00) + 0.50(18.00) = \text{USD } 10.00$.
  - Tại $t = 0$:
    $$P_0(50) = 0.50(1.00) + 0.50(10.00) = 0.25(0) + 0.50(2.00) + 0.25(18.00) = 1.00 + 4.50 = \mathbf{\text{USD } 5.50\text{ per share}}$$
  *(Kiểm tra chéo các báo giá còn lại trên cây: $P(46) = 0.25(14) = 3.50$; $C(56) = 0.25(16) = 4.00$; $C(64) = 0.25(8) = 2.00$ — khớp hoàn toàn 100%!).*

#### **b. Xác định Chiến lược Hợp lệ Thỏa Mãn Sàn Giá Trị & Ngân Sách Phí (Collar Strategy)**
1. **Lọc điều kiện sàn giá trị đáo hạn $\ge \text{USD } 50,000$ ($\ge \text{USD } 50$/cp):**
   - Nếu chọn mua $\text{Put}(46)$, tại trạng thái giảm sâu $S_{dd} = 32$ (và cả $S_{ud} = 48$), giá trị cổ phiếu cộng Put(46) chỉ đạt USD 46/cp = USD 46,000 (và USD 48,000 tại $ud$, chưa kể nếu viết Call cũng không tăng giá trị ở vùng dưới) $< \text{USD } 50,000$ $\implies$ **Loại Put(46)**!
   - Vậy Mu **bắt buộc phải mua Put strike USD 50** (10 hợp đồng), bảo đảm sàn $\max(S_T, 50) \ge \text{USD } 50$/cp (tổng $\ge \text{USD } 50,000$, miễn là Call bán ra có strike $K_C \ge 50$).
2. **Lọc điều kiện ngân sách phí ròng $\le \text{USD } 2,000$ ($\le \text{USD } 2.00$/cp):**
   - Mua 10 hợp đồng $\text{Put}(50)$ một mình tốn $1,000 \times 5.50 = \text{USD } 5,500 > \text{USD } 2,000$ (vượt ngân sách).
   - Nếu kết hợp viết 10 hợp đồng $\text{Call}(64)$ giá USD 2.00/cp: chi phí ròng $= 5,500 - 2,000 = \text{USD } 3,500 > \text{USD } 2,000$ (vẫn vượt ngân sách $\implies$ loại!).
   - Nếu kết hợp **viết 10 hợp đồng $\text{Call}(56)$ giá USD 4.00/cp**: chi phí ròng $= 5,500 - 4,000 = \mathbf{\text{USD } 1,500.00 \le \text{USD } 2,000}$ (**Thỏa mãn!**).
3. **Tổng kết thông số chiến lược duy nhất hợp lệ (Protective Collar):**
   - **Số lượng hợp đồng:** Giữ **1,000 cổ phiếu Nu**, **Mua 10 hợp đồng Put strike USD 50** (1,000 cp) và **Bán (viết) 10 hợp đồng Call strike USD 56** (1,000 cp).
   - **Chi phí phí quyền chọn ròng (*Net premium cost*):** $1,000 \times (5.50 - 4.00) = \mathbf{\text{USD } 1,500.00}$ ($\text{USD } 1.50$/cổ phiếu).
   - **Sàn giá trị danh mục lúc đáo hạn (*Terminal floor*):** $1,000 \times 50 = \mathbf{\text{USD } 50,000.00}$ (đạt được tại cả $S_{dd} = 32$ lẫn $S_{ud} = 48$).
   - **Trần giá trị danh mục lúc đáo hạn (*Terminal upside cap*):** $1,000 \times 56 = \mathbf{\text{USD } 56,000.00}$ (xảy ra khi $S_T \ge 56$, cụ thể tại $S_{uu} = 72$: $72,000 + 0 - 16,000 = \text{USD } 56,000.00$).

#### **c. So sánh Collar với việc chỉ mua Put USD 50 đơn lẻ (Protective Put Alone)**
- **Số tiền phí tiết kiệm được (*Premium saving*):** Việc bán 10 hợp đồng Call(56) mang về ngay **USD 4,000.00** ($\text{USD } 4.00$/cổ phiếu), kéo chi phí bảo hiểm ban đầu từ USD 5,500.00 xuống còn USD 1,500.00 (**tiết kiệm USD 4,000.00**).
- **Những gì Mu phải đánh đổi / từ bỏ (*What Mu gives up*):**
  - Mu **từ bỏ toàn bộ phần lợi nhuận tăng giá cổ phiếu vượt trên mức trần USD 56.00/cổ phiếu** (tức khóa trần giá trị danh mục tại USD 56,000 thay vì hưởng đà tăng không giới hạn).
  - Cụ thể trên cây nhị phân này, tại nhánh tăng kép $S_{uu} = \text{USD } 72.00$, chiến lược chỉ mua Put(50) cho giá trị cuối kỳ **USD 72,000** (lãi ròng $72,000 - 50,000 - 5,500 = +\text{USD } 16,500$), trong khi chiến lược Collar bị gọi mua mất phần vượt trên 56 nên chỉ còn **USD 56,000** — tức Mu phải hy sinh **USD 16.00/cp = USD 16,000.00 giá trị đáo hạn** (tương đương kém hơn USD 12,000.00 lợi nhuận ròng sau khi tính khoản tiết kiệm phí USD 4,000: lãi $+\text{USD } 4,500$ so với $+\text{USD } 16,500$).

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Với cây nhị phân 2 bước có $p = 0.5, R = 1$: Trọng số 3 nút cuối luôn là **$(1/4,\; 1/2,\; 1/4)$**! Tính giá quyền chọn bất kỳ trong 3 giây: $P(50) = \frac{1}{4}(0) + \frac{1}{2}(2) + \frac{1}{4}(18) = 5.50$!
- Với **Collar** ($\text{Long Stock} + \text{Long Put}(K_P) + \text{Short Call}(K_C)$, $K_P < K_C$):
  - $\text{Floor} = K_P$; $\text{Cap} = K_C$; $\text{Net Premium} = P(K_P) - C(K_C)$.

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Nhầm lẫn "worth at least USD 50,000 at expiration" với lợi nhuận ròng sau phí):** Đề viết cực kỳ chính xác: *"wants the combined shares and options to be **worth at least USD 50,000 at expiration** and can spend at most USD 2,000 in net option premiums"*. Giá trị đáo hạn (*terminal portfolio value*) của Cổ phiếu + Put(50) - Call(56) có sàn đúng bằng **USD 50,000** (còn nếu trừ đi USD 1,500 tiền phí đã chi ở đầu kỳ thì tổng tài sản ròng là USD 48,500 — đừng tự ý nâng strike Put lên 52 không tồn tại trên bảng!).
- **Bẫy 2 (Ghi số hợp đồng là 1,000 thay vì 10):** Mỗi hợp đồng quyền chọn đại diện cho **100 cổ phiếu**, nên để phủ 1,000 cổ phiếu cần **10 hợp đồng Put(50)** và **10 hợp đồng Call(56)**!

---

## Question 25 (Hard) — Mô Hình Cấu Trúc Tín Dụng Merton, Chênh Lệch Tín Dụng & Định Lý Modigliani-Miller
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Xi is initially debt-free. Its operating assets are worth USD 120 million and have annual volatility of 30%. The continuously compounded risk-free rate is 4% per year.
>
> Xi proposes issuing zero-coupon debt promising USD 100 million in two years. All issue proceeds will immediately be paid to the existing shareholders as a special dividend. Operating asset value and volatility remain unchanged. There are no further payouts before maturity, no taxes, no issuance or bankruptcy costs, and shareholders have limited liability. Assume the Black-Scholes framework applies to the operating assets. A calculator or spreadsheet may be used for the standard normal CDF.
>
> a. Determine the market values of equity and debt immediately after the distribution.
>
> b. Calculate the debt's promised effective annual yield and its credit spread over the effective annual risk-free rate.
>
> c. An alternative proposal promises USD 120 million at the same maturity. For this proposal, the model gives an equity value of USD 24.335815 million after the distribution. Calculate the debt proceeds, promised yield and credit spread. Compare the financing raised and borrowing cost with the first proposal.
>
> d. Compare the original shareholders' total current value under the two proposals, including the cash distributed.

**Tóm tắt thông số:**
- Tài sản hoạt động của doanh nghiệp (*operating assets*): $V_0 = \text{USD } 120\text{ million}$ (giữ nguyên sau khi trả hết tiền phát hành nợ làm cổ tức đặc biệt!), độ biến động $\sigma_V = 30\%$/năm.
- Lãi suất phi rủi ro liên tục: $r = 4\%$/năm; kỳ hạn nợ zero-coupon $T = 2$ năm.
- Phương án 1: Mệnh giá nợ hứa trả $F_1 = \text{USD } 100\text{ million}$.
- Phương án 2: Mệnh giá nợ hứa trả $F_2 = \text{USD } 120\text{ million}$, đề cho sẵn $E_{0,\text{alt}} = \text{USD } 24.335815\text{ million}$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Giá trị thị trường của Vốn chủ sở hữu ($E_0$) và Nợ ($D_0$) ngay sau khi chia cổ tức đặc biệt (Phương án $F_1 = 100\text{m}$)**
- Ngay sau khi toàn bộ số tiền thu từ phát hành nợ được chi trả ra ngoài làm cổ tức đặc biệt, tổng tài sản còn lại trong công ty đúng bằng tài sản hoạt động $V_0 = \text{USD } 120\text{ million}$.
- Với trách nhiệm hữu hạn (*limited liability*), tại ngày đáo hạn $T = 2$ năm, cổ đông nhận $\max(V_T - 100, 0)$ $\implies$ **Vốn chủ sở hữu $E_0$ chính là một quyền chọn mua kiểu châu Âu (European Call)** viết trên tài sản công ty $V_0 = 120$ với giá thực hiện $K = F_1 = 100$, kỳ hạn $T = 2$, $\sigma_V = 0.30$, $r = 0.04$:
  - Giá trị hiện tại mệnh giá nợ không rủi ro:
    $$PV(F_1) = 100 e^{-0.04 \times 2} = 100 e^{-0.08} = \text{USD } 92.311635\text{ million}$$
  - Độ lệch chuẩn tích lũy 2 năm: $\sigma_V \sqrt{T} = 0.30 \sqrt{2} = 0.42426407$.
  - Tính $d_1$ và $d_2$:
    $$d_1 = \frac{\ln(120 / 100) + (0.04 + 0.5 \times 0.30^2)(2)}{0.30\sqrt{2}} = \frac{0.18232156 + 0.17000000}{0.42426407} = \mathbf{0.830430}$$
    $$d_2 = d_1 - 0.30\sqrt{2} = 0.830430 - 0.424264 = \mathbf{0.406166}$$
  - Tra hàm phân phối chuẩn tắc: $N(d_1) = N(0.830430) = \mathbf{0.796852}$; $N(d_2) = N(0.406166) = \mathbf{0.657690}$.
  - **Giá trị thị trường của Vốn chủ sở hữu ($E_0$):**
    $$E_0 = V_0 N(d_1) - F_1 e^{-rT} N(d_2) = 120(0.796852) - 92.311635(0.657690) = 95.622219 - 60.712369 = \mathbf{\text{USD } 34.909850\text{ million} \approx \text{USD } 34.91\text{ million}}$$
  - **Giá trị thị trường của Nợ ($D_0$) theo đồng nhất thức bảng cân đối giá trị thị trường ($V_0 = E_0 + D_0$):**
    $$D_0 = V_0 - E_0 = 120.00 - 34.909850 = \mathbf{\text{USD } 85.090150\text{ million} \approx \text{USD } 85.09\text{ million}}$$
    *(Góc nhìn Put-Call Parity của Merton: $D_0 = PV(F_1) - P_{\text{default}} = 92.311635 - 7.221485 = \text{USD } 85.090150\text{ million}$, trong đó quyền chọn bán vỡ nợ trị giá USD 7.22 triệu!).*

#### **b. Lợi suất hứa hẹn hiệu dụng hàng năm của Nợ ($y_D$) & Chênh lệch tín dụng (Credit Spread)**
1. **Lợi suất hứa hẹn hiệu dụng năm (*Promised effective annual yield*):** Nợ zero-coupon thu về hôm nay $D_0 = 85.090150$ và hứa trả $F_1 = 100$ sau 2 năm:
   $$y_D = \left(\frac{100}{85.090150}\right)^{1/2} - 1 = (1.17522416)^{0.5} - 1 = 0.08407756 = \mathbf{8.41\%} \quad (8.4078\%)$$
2. **Lãi suất phi rủi ro hiệu dụng hàng năm (*Effective annual risk-free rate*):**
   $$r_{f,\text{eff}} = e^{0.04} - 1 = 0.04081077 = \mathbf{4.08\%} \quad (4.0811\%)$$
3. **Chênh lệch tín dụng (*Credit spread over effective annual risk-free rate*):**
   $$\text{Credit Spread} = y_D - r_{f,\text{eff}} = 8.407756\% - 4.081077\% = 0.04326679 = \mathbf{4.33\%} \quad (432.67\text{ bps})$$

#### **c. Phương án thay thế ($F_2 = \text{USD } 120\text{ million}$, $E_{0,\text{alt}} = \text{USD } 24.335815\text{ million}$) & So sánh**
1. **Số tiền thu từ phát hành nợ (*Debt proceeds*):**
   $$D_{0,\text{alt}} = V_0 - E_{0,\text{alt}} = 120.00 - 24.335815 = \mathbf{\text{USD } 95.664185\text{ million} \approx \text{USD } 95.66\text{ million}}$$
2. **Lợi suất hứa hẹn hiệu dụng hàng năm ($y_{D,\text{alt}}$):**
   $$y_{D,\text{alt}} = \left(\frac{120}{95.664185}\right)^{1/2} - 1 = (1.25438794)^{0.5} - 1 = 0.11999462 = \mathbf{12.00\%} \quad (11.9995\%)$$
3. **Chênh lệch tín dụng mới (*Credit spread*):**
   $$\text{Credit Spread}_{\text{alt}} = 11.999462\% - 4.081077\% = 0.07918384 = \mathbf{7.92\%} \quad (791.84\text{ bps})$$
4. **So sánh huy động vốn và chi phí vay giữa hai phương án:**
   - Mặc dù công ty nâng mệnh giá nợ cam kết lúc đáo hạn thêm **+USD 20.00 triệu** (từ USD 100m lên USD 120m), số tiền mặt thực tế huy động thêm được ở hiện tại chỉ tăng **+USD 10.57 triệu** ($95.664185 - 85.090150 = \text{USD } 10.574035\text{ million}$)!
   - Đồng thời, lợi suất vay hứa hẹn vọt từ **8.41% lên 12.00%** (chênh lệch tín dụng tăng gần gấp đôi từ **4.33% lên 7.92%**, tức $+3.59$ điểm phần trăm). Nguyên nhân: khi đòn bẩy tài chính tăng cao ($F_2 = V_0 = 120\text{m}$), xác suất và mức độ tổn thất khi vỡ nợ tăng mạnh (giá trị quyền chọn bán vỡ nợ $P_{\text{default}}$ tăng từ USD 7.22m lên $110.77 - 95.66 = \text{USD } 15.11\text{m}$), buộc trái chủ phải chiết khấu sâu giá mua trái phiếu để tự bảo vệ!

#### **d. So sánh Tổng Giá Trị Hiện Tại Của Cổ Đông Hiện Hữu Dưới Hai Phương Án**
Tổng tài sản hiện tại của cổ đông ban đầu bao gồm **giá trị cổ phần giữ lại sau chia cổ tức ($E_0$)** cộng **tiền mặt cổ tức đặc biệt nhận về ($\text{Cash distributed} = D_0$)**:
- **Phương án 1 ($F_1 = 100\text{m}$):** $\text{Total Wealth}_1 = 34.909850 + 85.090150 = \mathbf{\text{USD } 120.00\text{ million}}$.
- **Phương án 2 ($F_2 = 120\text{m}$):** $\text{Total Wealth}_2 = 24.335815 + 95.664185 = \mathbf{\text{USD } 120.00\text{ million}}$.
- **Giải thích kinh tế (Định lý Modigliani-Miller I trong thị trường hoàn hảo):** Trong môi trường không có thuế, không chi phí phát hành hay chi phí khánh kiệt tài chính/phá sản, và hoạt động kinh doanh cơ sở giữ nguyên ($V_0 = \text{USD } 120\text{m}$), việc tái cơ cấu đòn bẩy tài chính không tạo ra cũng không phá hủy giá trị! Trái chủ định giá hợp lý rủi ro vỡ nợ ngay từ đầu nên mọi sự gia tăng giá trị quyền chọn vỡ nợ của cổ đông đều bị trừ thẳng vào số tiền phát hành nợ $D_0$ thu về. Tổng tài sản của cổ đông ban đầu **bất biến ở mức USD 120.00 million** dưới cả hai phương án!

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ (MERTON STRUCTURAL MODEL):**
> - **Cổ phần có đòn bẩy (Levered Equity)** $=$ **Long Call** trên tài sản công ty $V$ với strike $F$: $E_0 = C(V_0, F, T, \sigma_V, r) \implies$ Cổ đông **hưởng lợi khi độ biến động tài sản $\sigma_V$ tăng** (*asset substitution / risk-shifting incentive*)!
> - **Nợ chịu rủi ro vỡ nợ (Risky Debt)** $=$ **Nợ phi rủi ro trừ đi một quyền chọn bán (Risk-free Bond $-$ Short Put on $V$)**: $D_0 = F e^{-rT} - P(V_0, F, T, \sigma_V, r) \implies$ Trái chủ **bị thiệt hại khi $\sigma_V$ tăng** (credit spread mở rộng khi $\sigma_V \uparrow$ hoặc đòn bẩy $F/V_0 \uparrow$)!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Lưu ý ở câu c GS. Cayirli đã cho sẵn $E_{0,\text{alt}} = 24.335815$ nên **tuyệt đối không tốn giờ bấm lại Black-Scholes lần 2**! Chỉ cần dùng định luật bảo toàn giá trị $D_0 = V_0 - E_0 = 120 - 24.335815 = 95.664185$, bấm căn bậc hai $(120 / 95.664185)^{0.5} - 1 = 12.00\%$ là xong trọn câu c trong 15 giây!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Lệch quy ước ghép lãi khi tính Credit Spread ở câu b & c):** Đề yêu cầu *"promised **effective annual** yield and its credit spread over the **effective annual** risk-free rate"*, trong khi đầu bài cho $r = 4\%$ **continuously compounded**! Phải đổi $r_{f,\text{eff}} = e^{0.04} - 1 = 4.0811\%$ rồi mới trừ ($8.4078\% - 4.0811\% = 4.33\%$); nếu trừ thẳng $4.00\%$ ra $4.41\%$ là mắc bẫy quy ước lãi suất!
- **Bẫy 2 (Cộng tiền phát hành nợ $D_0$ vào $V_0 = 120\text{m}$):** Tiền phát hành nợ đã được **chia cổ tức đặc biệt trả ra ngoài ngay lập tức**, nên tài sản còn lại trong công ty để đảm bảo cho nợ vẫn chỉ là **USD 120 triệu**, KHÔNG phải $120 + D_0$!

---

# PHẦN IV — LECTURE 11: BINOMIAL AND BLACK-SCHOLES VALUATION (Q26 – Q40)

*Quy ước chung từ đề gốc: Trừ khi có ghi chú khác, quyền chọn là kiểu châu Âu, quy mô 1 cổ phiếu và tài sản cơ sở không trả cổ tức. Cho phép vị thế lẻ (fractional positions), bán khống và vay/cho vay phi rủi ro. Ký hiệu $R$ là hệ số sinh lời gộp phi rủi ro qua 1 bước cây nhị phân (*gross risk-free return over one step*). Với Black-Scholes, lãi suất ghép lãi liên tục và độ biến động thường niên hóa. Giữ nguyên số chưa làm tròn ở bước trung gian.*

---
## Question 26 (Easy) — Danh Mục Mô Phỏng Quyền Chọn Mua Một Bước (Replicating Portfolio)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Omicron shares trade at USD 72. In nine months, a share will be worth either USD 90 or USD 60. A European call expiring then has strike USD 76. The risk-free rate is 8% effective annually.
>
> a. Determine the stock and cash positions that replicate one call. State whether the cash position represents borrowing or lending.
>
> b. Calculate the call's current value and verify the replicating portfolio's payoff in both states.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 72$; kỳ hạn 1 bước $T = 9/12 = 0.75$ năm; $S_u = \text{USD } 90$, $S_d = \text{USD } 60$.
- Call châu Âu strike $K = \text{USD } 76$; lãi suất phi rủi ro $r = 8\%$ EAR $\implies R = (1.08)^{0.75} = 1.05941911$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Vị thế Cổ phiếu ($\Delta$) và Tiền mặt ($B$) mô phỏng 1 quyền chọn mua**
- Payoff của quyền chọn mua tại $T = 0.75$ năm:
  $$C_u = \max(90 - 76, 0) = \text{USD } 14.00, \qquad C_d = \max(60 - 76, 0) = \text{USD } 0.00$$
- Gọi $\Delta$ là số cổ phiếu nắm giữ và $B$ là vị thế tiền mặt hôm nay (sau 9 tháng tích lũy thành $B \cdot R$). Để mô phỏng chính xác payoff ở cả hai trạng thái:
  $$\begin{cases} 90 \Delta + B \cdot R = 14.00 \\ 60 \Delta + B \cdot R = 0.00 \end{cases}$$
- Trừ hai phương trình tìm **tỷ số phòng hộ (*Hedge ratio / Stock position* $\Delta$)**:
  $$\Delta = \frac{C_u - C_d}{S_u - S_d} = \frac{14.00 - 0.00}{90 - 60} = \frac{14}{30} = \frac{7}{15} = \mathbf{0.466667 \approx 0.47\text{ shares}} \quad (\text{mua } 7/15\text{ cổ phiếu})$$
- Thay $\Delta = 7/15$ vào phương trình trạng thái xuống để tìm **vị thế tiền mặt hôm nay ($B$)**:
  $$B \cdot R = 0 - \frac{7}{15}(60) = -\text{USD } 28.00 \implies B = \frac{-28.00}{(1.08)^{0.75}} = \frac{-28.00}{1.05941911} = \mathbf{-\text{USD } 26.429577 \approx -\text{USD } 26.43}$$
- **Bản chất vị thế tiền mặt:** Vì $B < 0$, vị thế tiền mặt đại diện cho việc **ĐI VAY (Borrowing) USD 26.43** tại lãi suất phi rủi ro (sẽ phải trả gốc + lãi đúng bằng USD 28.00 sau 9 tháng).

#### **b. Giá trị hiện tại của Call ($C_0$) & Kiểm chứng Payoff ở cả hai trạng thái**
- Theo Luật Một Giá (*Law of One Price*), giá trị hiện tại của quyền chọn mua bằng chi phí thiết lập danh mục mô phỏng:
  $$C_0 = \Delta S_0 + B = \frac{7}{15}(72.00) - 26.429577 = 33.60 - 26.429577 = \mathbf{\text{USD } 7.170423 \approx \text{USD } 7.17}$$
- **Kiểm chứng Payoff danh mục mô phỏng tại $T = 0.75$** (khi khoản nợ gốc USD 26.429577 tích lũy thành $26.429577 \times (1.08)^{0.75} = \text{USD } 28.00$):
  - **Trạng thái Tăng ($S_u = 90$):** $\frac{7}{15}(90) - 28.00 = 42.00 - 28.00 = \mathbf{\text{USD } 14.00} = C_u$ *(Khớp chính xác!)*.
  - **Trạng thái Giảm ($S_d = 60$):** $\frac{7}{15}(60) - 28.00 = 28.00 - 28.00 = \mathbf{\text{USD } 0.00} = C_d$ *(Khớp chính xác!)*.

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Quy luật dấu bất biến giúp tự kiểm tra lỗi bấm máy trong 1 giây:
  - **Mô phỏng Long Call:** Luôn là **Mua cổ phiếu ($\Delta > 0$) + Đi vay tiền ($B < 0$)** (dùng đòn bẩy!).
  - **Mô phỏng Long Put:** Luôn là **Bán khống cổ phiếu ($\Delta < 0$) + Cho vay tiền ($B > 0$)**!
- Kiểm tra chéo $C_0$ bằng xác suất trung hòa rủi ro: $u = 90/72 = 1.25$, $d = 60/72 = 5/6$, $p = \frac{1.05941911 - 5/6}{1.25 - 5/6} = 0.542606 \implies C_0 = \frac{0.542606 \times 14}{1.05941911} = \mathbf{7.170423}$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy tính sai hệ số tích lũy 9 tháng của lãi suất Effective Annual:** Đề cho $r = 8\%$ **effective annually**, nên qua 9 tháng ($0.75$ năm) phải lấy lũy thừa **$R = (1.08)^{0.75} = 1.059419$**, TUYỆT ĐỐI KHÔNG lấy tuyến tính $1 + 0.08 \times 0.75 = 1.06$!

---

## Question 27 (Easy) — Giá Trạng Thái Arrow-Debreu & Định Giá Quyền Chọn Bán (State Prices)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Pi shares cost USD 42 and will be worth either USD 54 or USD 34 in four months. A risk-free security costs USD 100 today and pays USD 104 at that date. A European put on Pi has strike USD 44 and expires in four months.
>
> a. Find today's prices of a claim paying USD 1 only in the up state and a claim paying USD 1 only in the down state. Check their sum.
>
> b. Use those state prices to value the put.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 42$; sau 4 tháng: $S_u = \text{USD } 54$ hoặc $S_d = \text{USD } 34$.
- Chứng khoán phi rủi ro giá USD 100 hôm nay trả USD 104 sau 4 tháng $\implies R = \frac{104}{100} = \mathbf{1.04}$ (cho đúng bước 4 tháng, không cần mũ hóa!).
- Put châu Âu strike $K = \text{USD } 44$, đáo hạn sau 4 tháng.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Giá hiện tại của hai chứng khoán trạng thái cơ bản ($\psi_u, \psi_d$) & Kiểm tra tổng**
Gọi $\psi_u$ là giá hôm nay của chứng khoán Arrow-Debreu trả USD 1 duy nhất ở trạng thái Tăng, và $\psi_d$ là giá hôm nay của chứng khoán trả USD 1 duy nhất ở trạng thái Giảm. Định giá cổ phiếu và trái phiếu phi rủi ro theo $(\psi_u, \psi_d)$:
$$\begin{cases} 54 \psi_u + 34 \psi_d = 42 \\ 104 \psi_u + 104 \psi_d = 100 \implies \psi_u + \psi_d = \frac{100}{104} = \frac{25}{26} \end{cases}$$
Thế $\psi_d = \frac{25}{26} - \psi_u$ vào phương trình cổ phiếu:
$$54 \psi_u + 34\left(\frac{25}{26} - \psi_u\right) = 42 \implies 20 \psi_u = 42 - \frac{850}{26} = \frac{1,092 - 850}{26} = \frac{242}{26} = \frac{121}{13}$$
$$\implies \psi_u = \frac{121}{260} = \mathbf{\text{USD } 0.465385 \approx \text{USD } 0.47}$$
$$\implies \psi_d = \frac{25}{26} - \frac{121}{260} = \frac{250 - 121}{260} = \frac{129}{260} = \mathbf{\text{USD } 0.496154 \approx \text{USD } 0.50}$$
- **Kiểm tra tổng (*Check their sum*):**
  $$\psi_u + \psi_d = \frac{121}{260} + \frac{129}{260} = \frac{250}{260} = \frac{100}{104} = \frac{1}{1.04} = \mathbf{\text{USD } 0.961538 \approx \text{USD } 0.96}$$
  *Ý nghĩa kinh tế:* Nắm giữ đồng thời 1 chứng khoán trạng thái Tăng và 1 chứng khoán trạng thái Giảm chắc chắn mang lại USD 1.00 trong mọi trạng thái sau 4 tháng, nên tổng giá của chúng bắt buộc bằng **hệ số chiết khấu phi rủi ro 4 tháng** $DF = 1/R = 100/104 = 0.961538$!

#### **b. Định giá quyền chọn bán ($K = 44$) bằng giá trạng thái**
- Payoff của Put sau 4 tháng:
  $$P_u = \max(44 - 54, 0) = \text{USD } 0.00, \qquad P_d = \max(44 - 34, 0) = \text{USD } 10.00$$
- Giá trị hiện tại của Put (dùng giá trị phân số chính xác chưa làm tròn):
  $$P_0 = \psi_u P_u + \psi_d P_d = \frac{121}{260}(0) + \frac{129}{260}(10.00) = \frac{129}{26} = \mathbf{\text{USD } 4.961538 \approx \text{USD } 4.96}$$

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Công thức Đóng Trực Tiếp của State Prices (bấm thẳng không cần giải hệ phương trình):**
  $$\psi_u = \frac{S_0 - S_d / R}{S_u - S_d} = \frac{42 - 34/1.04}{54 - 34} = \frac{121}{260}, \qquad \psi_d = \frac{S_u / R - S_0}{S_u - S_d} = \frac{54/1.04 - 42}{54 - 34} = \frac{129}{260}$$
  *(Liên hệ vàng với xác suất trung hòa rủi ro: $\psi_u = \frac{p}{R}$ và $\psi_d = \frac{1 - p}{R}$!).*

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Tưởng $4\%$ là lãi suất năm rồi lấy $1.04^{4/12}$):** Đọc kỹ đề: *"costs USD 100 today and pays USD 104 **at that date** [in four months]"*! Tức $R = 1.04$ đã là tổng hệ số sinh lời của trọn kỳ 4 tháng!
- **Bẫy 2 (Làm tròn sớm $\psi_d = 0.50$ rồi nhân $10$ ra $5.00$ thay vì $4.96$):** Nếu dùng số đã làm tròn $0.50 \times 10 = \text{USD } 5.00$, bạn sẽ sai lệch hẳn USD 0.04 so với đáp số chuẩn **USD 4.96** ($129/26$)! Luôn giữ phân số $129/260$ trong máy tính!

---

## Question 28 (Easy) — Xác Suất Trung Hòa Rủi Ro & Điều Kiện Không Kinh Doanh Chênh Lệch Giá ($d < R < u$)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Rho shares cost USD 80. Over the next six months, the price either rises by 8% or falls by 6%. The risk-free rate is 10.25% effective annually.
>
> a. Calculate the six-month gross risk-free return and the risk-neutral up probability.
>
> b. A revised worksheet keeps the stock tree unchanged but replaces the annual risk-free rate with 21%. Assess whether this remains an arbitrage-free model. If not, give a zero-cost trade and its six-month cash flows.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 80$; kỳ hạn $T = 6/12 = 0.50$ năm; $u = 1.08$ ($S_u = \text{USD } 86.40$), $d = 0.94$ ($S_d = \text{USD } 75.20$).
- Câu a: $r = 10.25\%$ EAR. Câu b: Đổi thành $r_{\text{rev}} = 21\%$ EAR.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Hệ số sinh lời gộp phi rủi ro 6 tháng ($R$) & Xác suất tăng trung hòa rủi ro ($p$)**
1. **Hệ số sinh lời gộp 6 tháng ($R$):**
   $$R = (1 + r)^{0.50} = (1.1025)^{0.50} = \mathbf{1.05} \quad (\text{tức lãi suất 6 tháng là } 5.00\%)$$
2. **Xác suất tăng trung hòa rủi ro ($p$):** Vì $d = 0.94 < R = 1.05 < u = 1.08$, mô hình không có arbitrage và:
   $$p = \frac{R - d}{u - d} = \frac{1.05 - 0.94}{1.08 - 0.94} = \frac{0.11}{0.14} = \frac{11}{14} = \mathbf{0.785714 \approx 78.57\%}$$

#### **b. Đánh giá bảng tính sửa đổi với lãi suất năm 21% & Thiết lập giao dịch Arbitrage chi phí bằng 0**
- Với $r_{\text{rev}} = 21\%$ EAR, hệ số sinh lời gộp phi rủi ro trong 6 tháng trở thành:
  $$R_{\text{rev}} = (1.21)^{0.50} = \mathbf{1.10} \quad (\text{tức } +10.00\%\text{ trong 6 tháng})$$
- **Đánh giá điều kiện Không-Arbitrage:** Một cây nhị phân chỉ không có arbitrage khi và chỉ khi **$d < R < u$** ($0.94 < R < 1.08$). Ở đây $R_{\text{rev}} = 1.10 > u = 1.08$: tài sản phi rủi ro tăng $10\%$ chắc chắn, **vượt trội nghiêm ngặt (*strictly dominates*)** so với cổ phiếu ngay cả trong kịch bản tốt nhất cổ phiếu chỉ tăng $8\%$ (nếu thay vào công thức sẽ cho "xác suất" vô nghĩa $p = \frac{1.10 - 0.94}{0.14} = \frac{16}{14} > 1$)! Do đó **mô hình KHÔNG CÒN phi kinh doanh chênh lệch giá (NOT arbitrage-free)**!
- **Giao dịch Arbitrage chi phí bằng 0 (*Zero-cost arbitrage trade*, tính trên 1 cổ phiếu):**
  - **Hôm nay ($t = 0$):** **Bán khống 1 cổ phiếu Rho** thu về $+\text{USD } 80.00$, và đem **cho vay / gửi phi rủi ro toàn bộ USD 80.00** trong 6 tháng ($-\text{USD } 80.00$) $\implies$ **Dòng tiền ròng hôm nay = USD 0.00**.
  - **Sau 6 tháng ($T = 0.50$):** Khoản tiền gửi thu về chắc chắn $80.00 \times 1.10 = +\text{USD } 88.00$; dùng tiền này mua lại 1 cổ phiếu trên thị trường trả kho:
    - **Nếu trạng thái Tăng ($S_u = 86.40$):** $+88.00 - 86.40 = \mathbf{+\text{USD } 1.60}$ (lãi ròng dương!).
    - **Nếu trạng thái Giảm ($S_d = 75.20$):** $+88.00 - 75.20 = \mathbf{+\text{USD } 12.80}$ (lãi ròng dương!).
  *(Không bỏ vốn ban đầu, không có khả năng lỗ, và chắc chắn thu lãi dương trong mọi trạng thái!).*

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Hai con số chính phương đẹp kinh điển GS. Cayirli cài sẵn để tính nhẩm không cần máy: $\sqrt{1.1025} = 1.05$ ($105^2 = 11025$) và $\sqrt{1.21} = 1.10$ ($11^2 = 121$)!
- Nhớ nhanh 2 chiều vi phạm $d < R < u$:
  - Nếu **$R \ge u$** (lãi suất quá cao như câu 28b): **Short Stock + Lend Cash**!
  - Nếu **$R \le d$** (lãi suất quá thấp): **Borrow Cash + Buy Stock**!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy chia đôi lãi suất năm ($21\% / 2 = 10.5\%$ thay vì $\sqrt{1.21} - 1 = 10\%$):** Nếu tính nhầm $R = 1.105$, tiền gửi 6 tháng sẽ ra USD 88.40 và làm sai lệch toàn bộ hai con số dòng tiền cuối kỳ (**+USD 1.60** và **+USD 12.80**)!

---

## Question 29 (Easy) — Định Giá Quyền Chọn Mua Black-Scholes & Giá Trị Thời Gian Của Quyền Chọn OTM
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Sigma shares trade at USD 68. A nine-month European call has strike USD 72. Annual volatility is 26%, and the continuously compounded risk-free rate is 4.5% per year.
>
> a. Calculate $PV(K)$, $d_1$ and $d_2$.
>
> b. Calculate the call value using Black-Scholes. Explain why the option can have a positive price despite its current exercise payoff.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 68$; $K = \text{USD } 72$ (quyền chọn đang *out-of-the-money*); $T = 9/12 = 0.75$ năm; $\sigma = 26\%$; $r = 4.5\%$ liên tục.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Tính $PV(K)$, $d_1$ và $d_2$**
1. **Giá trị hiện tại của giá thực hiện ($PV(K)$):**
   $$PV(K) = K e^{-r T} = 72 e^{-0.045 \times 0.75} = 72 e^{-0.03375} = 72 \times 0.96681318 = \mathbf{\text{USD } 69.610549 \approx \text{USD } 69.61}$$
2. **Độ biến động trong kỳ hạn 9 tháng:** $\sigma \sqrt{T} = 0.26 \sqrt{0.75} = 0.22516660$.
3. **Tính $d_1$ và $d_2$:**
   $$d_1 = \frac{\ln\left(S_0 / PV(K)\right)}{\sigma\sqrt{T}} + \frac{1}{2}\sigma\sqrt{T} = \frac{\ln(68 / 72) + (0.045 + 0.5 \times 0.26^2)(0.75)}{0.22516660} = \frac{-0.05715841 + 0.05910000}{0.22516660} = \mathbf{0.008623} \quad (\approx 0.01)$$
   $$d_2 = d_1 - \sigma\sqrt{T} = 0.008623 - 0.225167 = \mathbf{-0.216544} \quad (\approx -0.22)$$

#### **b. Giá trị quyền chọn mua Black-Scholes & Giải thích kinh tế**
- Tra phân phối chuẩn tắc tại các giá trị chưa làm tròn:
  $$N(d_1) = N(0.008623) = \mathbf{0.503440}, \qquad N(d_2) = N(-0.216544) = \mathbf{0.414282}$$
- **Giá trị quyền chọn mua ($C_0$):**
  $$C_0 = S_0 N(d_1) - PV(K) N(d_2) = 68(0.503440) - 69.610549(0.414282) = 34.233925 - 28.838401 = \mathbf{\text{USD } 5.395524 \approx \text{USD } 5.40}$$
- **Tại sao quyền chọn có giá dương (USD 5.40) mặc dù giá trị thực hiện hiện tại bằng 0?**
  - Giá trị nội tại / thực hiện ngay hiện tại là $\max(S_0 - K, 0) = \max(68 - 72, 0) = \text{USD } 0$ (OTM).
  - Tuy nhiên, quyền chọn sở hữu **cấu trúc payoff bất đối xứng (lồi / *asymmetric, convex payoff*)** $\max(S_T - 72, 0)$ kết hợp với **thời gian còn lại dương ($T = 0.75$ năm)** và **độ biến động dương ($\sigma = 26\%$)**.
  - Có một xác suất thực sự dương là giá cổ phiếu tăng vượt USD 72 vào lúc đáo hạn (mang lại khoản lãi dương $S_T - 72 > 0$), trong khi mọi kịch bản giá giảm sâu hay kết thúc dưới USD 72 đều được **chặn sàn ở mức USD 0** (người mua quyền chọn có quyền bỏ không thực hiện chứ không bị lỗ như hợp đồng kỳ hạn!). Một tài sản có xác suất dương nhận dòng tiền dương và không bao giờ phát sinh dòng tiền âm lúc đáo hạn bắt buộc phải có giá trị hiện tại dương (**Time Value = USD 5.40 > 0**), nếu không sẽ xuất hiện cơ hội arbitrage mua miễn phí!

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ:**
> - $\text{Option Value} = \text{Intrinsic Value} + \text{Time Value}$. Đối với quyền chọn OTM, $100\%$ giá quyền chọn chính là **Time Value (Insurance / Optionality Value)** phát sinh từ tính bất đối xứng $\max(\cdot, 0)$ và phân tán giá $\sigma\sqrt{T} > 0$.
> - Chú ý hiện tượng rất hay ở câu a: Mặc dù quyền chọn đang OTM giao ngay ($S_0 = 68 < K = 72$, và cả $S_0 = 68 < PV(K) = 69.61$), nhưng nhờ số hạng $+\frac{1}{2}\sigma^2 T$, **$d_1 = +0.0086 > 0$ nên $\Delta = N(d_1) = 0.5034 > 0.50$**, trong khi xác suất thực hiện quyền chọn trung hòa rủi ro $N(d_2) = 0.4143 < 0.50$!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Viết công thức $d_1$ trực tiếp qua $PV(K)$ đã tính ở bước 1 cực kỳ sạch và ít bấm nhầm ngoặc nhất:
  $$d_1 = \frac{\ln(S_0 / PV(K))}{\sigma\sqrt{T}} + \frac{1}{2}\sigma\sqrt{T}$$

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1:** Quên lấy căn bậc hai thời gian $\sqrt{0.75} = 0.8660$ ở mẫu số mà nhân nhầm $0.26 \times 0.75$!
- **Bẫy 2:** Làm tròn $d_1 = 0.01$ và $d_2 = -0.22$ trước khi tra hàm $N(\cdot)$ sẽ làm giá Call bị lệch vài xu ($5.45$ thay vì **$5.40$**)!

---

## Question 30 (Easy) — Ước Lượng Độ Biến Động Mẫu Từ Lợi Suất Logarit & Quy Tắc Căn Bậc Hai Thời Gian
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Tau records the following weekly log returns, expressed as decimals:
>
> | Week | 1 | 2 | 3 | 4 | 5 | 6 |
> |---|---:|---:|---:|---:|---:|---:|
> | Log return | 0.020 | -0.010 | 0.030 | -0.020 | 0.010 | 0.000 |
>
> a. Estimate the weekly sample standard deviation using divisor $n-1$.
>
> b. Assuming uncorrelated weekly log returns with constant variance, calculate annual volatility using 52 weeks per year and the standard deviation of a thirteen-week log return.

**Tóm tắt thông số:**
- Chuỗi $n = 6$ lợi suất logarit tuần (*weekly log returns*): $r = \{0.020, -0.010, 0.030, -0.020, 0.010, 0.000\}$.
- Quy ước chia cho bậc tự do $n - 1 = 5$; một năm có $52$ tuần.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Độ lệch chuẩn mẫu hàng tuần ($s_w$)**
1. **Trung bình mẫu hàng tuần ($\bar{r}$):**
   $$\bar{r} = \frac{0.020 + (-0.010) + 0.030 + (-0.020) + 0.010 + 0.000}{6} = \frac{0.030}{6} = \mathbf{0.0050} \quad (0.50\%)$$
2. **Tổng bình phương độ lệch so với trung bình ($\sum_{i=1}^6 (r_i - \bar{r})^2$):**
   - Tuần 1: $(0.020 - 0.005)^2 = (+0.015)^2 = 0.000225$
   - Tuần 2: $(-0.010 - 0.005)^2 = (-0.015)^2 = 0.000225$
   - Tuần 3: $(0.030 - 0.005)^2 = (+0.025)^2 = 0.000625$
   - Tuần 4: $(-0.020 - 0.005)^2 = (-0.025)^2 = 0.000625$
   - Tuần 5: $(0.010 - 0.005)^2 = (+0.005)^2 = 0.000025$
   - Tuần 6: $(0.000 - 0.005)^2 = (-0.005)^2 = 0.000025$
   - **Tổng cộng:** $\sum (r_i - \bar{r})^2 = 2(0.000225 + 0.000625 + 0.000025) = \mathbf{0.001750}$.
3. **Phương sai mẫu ($s_w^2$) và Độ lệch chuẩn mẫu tuần ($s_w$):**
   $$s_w^2 = \frac{0.001750}{6 - 1} = \frac{0.001750}{5} = 0.000350$$
   $$s_w = \sqrt{0.000350} = \mathbf{0.01870829 \approx 1.87\%} \quad (0.0187)$$

#### **b. Độ biến động thường niên hóa (52 tuần) & Độ lệch chuẩn lợi suất logarit 13 tuần**
Vì lợi suất logarit nhiều tuần bằng tổng các lợi suất logarit từng tuần ($r_{k\text{-week}} = \sum_{t=1}^k r_t$) và các tuần không tương quan có phương sai hằng số, nên **phương sai nhân tuyến tính với $k$**, còn **độ lệch chuẩn nhân với $\sqrt{k}$ (*square-root-of-time rule*)**:
1. **Độ biến động hàng năm (*Annual volatility*, $k = 52$ tuần):**
   $$\sigma_{\text{annual}} = s_w \sqrt{52} = \sqrt{52 \times 0.000350} = \sqrt{0.018200} = \mathbf{0.13490738 \approx 13.49\%}$$
2. **Độ lệch chuẩn của lợi suất logarit 13 tuần ($k = 13$ tuần = 1 quý):**
   $$\sigma_{13\text{w}} = s_w \sqrt{13} = \sqrt{13 \times 0.000350} = \sqrt{0.004550} = \mathbf{0.06745369 \approx 6.75\%}$$
   *(Kiểm tra đẹp: 13 tuần bằng đúng $1/4$ năm $\implies \sigma_{13\text{w}} = \sigma_{\text{annual}} \sqrt{0.25} = \frac{1}{2} \sigma_{\text{annual}} = \frac{13.490738\%}{2} = 6.745369\% \approx 6.75\%$!).*

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Nhìn 6 số của GS. Cayirli cho cực đẹp khi nhân 1,000 (đổi ra đơn vị phần nghìn): $\{20, -10, 30, -20, 10, 0\}$, trung bình $= 5$, độ lệch $= \{+15, -15, +25, -25, +5, -5\}$! Bình phương nhẩm 3 giây: $2 \times (225 + 625 + 25) = 1,750$; chia $5$ ra $350$! Vậy $s_w = \sqrt{350} \times 10^{-3} = 18.708 \times 10^{-3} = 1.87\%$ — không bao giờ sợ bấm nhầm số 0 sau dấu phẩy!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Nhân thẳng với $52$ thay vì $\sqrt{52}$):** Phương sai mới nhân $52$, còn **độ biến động (*volatility / standard deviation*) bắt buộc nhân $\sqrt{52}$** (và nhân $\sqrt{13}$ cho 13 tuần)!
- **Bẫy 2 (Chia cho $n = 6$ thay vì $n - 1 = 5$):** Trên máy tính cầm tay Casio/TI, nhớ chọn biến **`sx` (sample SD)** chứ KHÔNG chọn `σx` (population SD chia $n$)!

---

## Question 31 (Average) — Khôi Phục Giá Thực Hiện Bị Khuyết & Định Giá Put Trên Cây Nhị Phân
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Upsilon shares trade at USD 64 and will be worth either USD 80 or USD 48 in one year. The risk-free rate is 5% effective annually. A one-year European call has a nonnegative strike that is missing from a worksheet. Its arbitrage-free price is USD 10.
>
> a. Recover the strike and verify the resulting call payoffs.
>
> b. Determine the value of the European put with that strike and expiration.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 64$; sau $T = 1$ năm: $S_u = \text{USD } 80$ ($u = 1.25$) hoặc $S_d = \text{USD } 48$ ($d = 0.75$).
- Lãi suất phi rủi ro $r = 5\%$ EAR $\implies R = 1.05$. Giá Call châu Âu hợp lý $C_0 = \text{USD } 10$, biết $K \ge 0$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Khôi phục giá thực hiện ($K$) & Kiểm chứng Payoff của Call**
- Xác suất tăng trung hòa rủi ro 1 năm:
  $$p = \frac{R - d}{u - d} = \frac{1.05 - 0.75}{1.25 - 0.75} = \frac{0.30}{0.50} = \mathbf{0.60} \quad (1 - p = 0.40)$$
- Xét các miền giá trị có thể của $K \ge 0$:
  1. *Miền chuẩn $48 \le K < 80$* (Call chỉ thực hiện ở trạng thái Tăng: $C_u = 80 - K$, $C_d = 0$):
     $$C_0 = \frac{p(80 - K) + (1 - p)(0)}{1.05} = \frac{0.60(80 - K)}{1.05} = 10.00$$
     $$\implies 80 - K = \frac{10.00 \times 1.05}{0.60} = \frac{10.50}{0.60} = 17.50 \implies K = 80.00 - 17.50 = \mathbf{\text{USD } 62.50}$$
     Kiểm tra điều kiện miền: $48 \le 62.50 < 80$ **thỏa mãn hoàn toàn**!
  2. *(Kiểm tra tính duy nhất trên miền $0 \le K < 48$: nếu $K < 48$ thì Call luôn ITM ở cả hai trạng thái nên $C_0 = S_0 - K/1.05 = 64 - K/1.05 = 10 \implies K = 54 \times 1.05 = 56.70$, mâu thuẫn với giả thiết $K < 48$! Còn nếu $K \ge 80$ thì $C_0 = 0 \neq 10$. Vậy $K = \text{USD } 62.50$ là nghiệm duy nhất!).*
- **Kiểm chứng Payoff của Call với $K = \text{USD } 62.50$:**
  - $C_u = \max(80.00 - 62.50, 0) = \mathbf{\text{USD } 17.50}$; $C_d = \max(48.00 - 62.50, 0) = \mathbf{\text{USD } 0.00}$.
  - Giá trị hiện tại: $C_0 = \frac{0.60(17.50) + 0.40(0)}{1.05} = \frac{10.50}{1.05} = \text{USD } 10.00$ *(Khớp chính xác!)*.

#### **b. Giá trị quyền chọn bán châu Âu tương ứng ($K = \text{USD } 62.50$)**
- **Cách 1 (Định giá trực tiếp trên cây nhị phân):**
  - Payoff của Put: $P_u = \max(62.50 - 80.00, 0) = 0$; $P_d = \max(62.50 - 48.00, 0) = 14.50$.
  - Giá trị hiện tại của Put:
    $$P_0 = \frac{0.60(0) + 0.40(14.50)}{1.05} = \frac{5.80}{1.05} = \frac{116}{21} = \mathbf{\text{USD } 5.523810 \approx \text{USD } 5.52}$$
- **Cách 2 (Đối chiếu bằng Put-Call Parity):**
  $$P_0 = C_0 - S_0 + \frac{K}{1.05} = 10.00 - 64.00 + \frac{62.50}{1.05} = -54.00 + 59.523810 = \mathbf{\text{USD } 5.523810 \approx \text{USD } 5.52}$$

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Mẹo kiểm tra xem $K$ rơi vào miền $< S_d$ hay $[S_d, S_u]$ ngay lập tức mà không cần giải thử 2 trường hợp:
  - Tại ranh giới $K = S_d = 48$, giá Call là $S_0 - 48/1.05 = 64 - 45.71 = \text{USD } 18.29$.
  - Vì đề cho $C_0 = 10 < 18.29$ (và $> 0$), chắc chắn $100\%$ strike $K$ phải nằm trong khoảng $(48, 80)$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy dùng nhầm công thức kỳ hạn $C_0 = S_0 - PV(K)$ để tìm $K$:** Công thức $C_0 = S_0 - K/R$ chỉ đúng khi quyền chọn chắc chắn thực hiện trong MỌI trạng thái ($K \le S_d = 48$). Nếu giải bừa $64 - K/1.05 = 10 \implies K = 56.70$, rồi không thử lại vào $C_d = \max(48 - 56.70, 0) = 0$ sẽ mất sạch toàn bộ điểm bài này! Chính vì thế đề mới dặn *"and verify the resulting call payoffs"*!

---

## Question 32 (Average) — Cây Nhị Phân Hai Bước & Bắt Lỗi Chiết Khấu Kép Trên Bảng Tính
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Phi shares trade at USD 96. Over each of the next two three-month periods, the price rises by 25% or falls by 20%. A six-month European put has strike USD 100. The risk-free rate is 8% nominal annually, compounded quarterly.
>
> a. Determine the terminal stock prices and put payoffs, both three-month put values and the current put value.
>
> b. Zeta discounts by $(1.02)^2$ at each backward step and reports a current put value of USD 11.152863. Assess the worksheet and quantify any pricing error.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 96$; cây 2 bước, mỗi bước 3 tháng (1 quý), tổng $T = 6$ tháng; $u = 1.25$, $d = 0.80$.
- Put châu Âu strike $K = \text{USD } 100$.
- Lãi suất $8\%$ danh nghĩa năm, ghép lãi hàng quý (*nominal annually, compounded quarterly*) $\implies$ Lãi suất mỗi quý 3 tháng là $8\% / 4 = 2\%$, tức **$R = 1.02$ cho mỗi bước**!

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Giá cổ phiếu & Payoff đáo hạn, Giá trị Put ở tháng thứ 3 ($P_u, P_d$) & Giá trị Put hiện tại ($P_0$)**
1. **Xác suất trung hòa rủi ro mỗi bước quý ($R = 1.02$):**
   $$p = \frac{R - d}{u - d} = \frac{1.02 - 0.80}{1.25 - 0.80} = \frac{0.22}{0.45} = \frac{22}{45} \approx \mathbf{0.488889}, \qquad 1 - p = \frac{23}{45} \approx \mathbf{0.511111}$$
2. **Giá cổ phiếu trên cây & Payoff đáo hạn của Put ($K = 100$):**
   - Tháng 3 ($t = 1$): $S_u = 96(1.25) = \text{USD } 120.00$; $S_d = 96(0.80) = \text{USD } 76.80$.
   - Tháng 6 ($t = 2$, đáo hạn):
     - Trạng thái $uu$: $S_{uu} = 120(1.25) = \mathbf{\text{USD } 150.00} \implies P_{uu} = \max(100 - 150, 0) = \mathbf{\text{USD } 0.00}$.
     - Trạng thái $ud / du$: $S_{ud} = 120(0.80) = \mathbf{\text{USD } 96.00} \implies P_{ud} = \max(100 - 96, 0) = \mathbf{\text{USD } 4.00}$.
     - Trạng thái $dd$: $S_{dd} = 76.80(0.80) = \mathbf{\text{USD } 61.44} \implies P_{dd} = \max(100 - 61.44, 0) = \mathbf{\text{USD } 38.56}$.
3. **Hai giá trị Put tại thời điểm 3 tháng ($P_u$ và $P_d$):**
   $$P_u = \frac{\frac{22}{45}(0.00) + \frac{23}{45}(4.00)}{1.02} = \frac{92 / 45}{1.02} = \frac{92}{45.90} = \mathbf{\text{USD } 2.004357 \approx \text{USD } 2.00}$$
   $$P_d = \frac{\frac{22}{45}(4.00) + \frac{23}{45}(38.56)}{1.02} = \frac{88 + 886.88}{45 \times 1.02} = \frac{974.88}{45.90} = \mathbf{\text{USD } 21.239216 \approx \text{USD } 21.24}$$
4. **Giá trị Put hiện tại ($P_0$):**
   $$P_0 = \frac{\frac{22}{45}(2.004357) + \frac{23}{45}(21.239216)}{1.02} = \frac{22(92) + 23(974.88)}{45^2 \times 1.02^2} = \frac{24,446.24}{2,025 \times 1.0404} = \mathbf{\text{USD } 11.603438 \approx \text{USD } 11.60}$$

#### **b. Đánh giá Bảng tính của Zeta (USD 11.152863) & Định lượng sai số định giá**
- **Kiểm tra con số của Zeta:** Lấy giá trị đúng $P_0 = 11.603438$ chia thêm cho $(1.02)^2$:
  $$\frac{11.603438}{(1.02)^2} = \frac{11.603438}{1.0404} = \mathbf{11.152863}!$$
- **Chẩn đoán lỗi sai trên bảng tính của Zeta:**
  - Zeta đã tính đúng xác suất trung hòa rủi ro $p = 22/45$ (dùng đúng $R = 1.02$), **NHƯNG ở mỗi bước lùi 3 tháng lại đem chia cho hệ số chiết khấu của cả 6 tháng là $(1.02)^2$ thay vì hệ số 1 quý là $1.02$**!
  - Qua 2 bước lùi trên cây, Zeta đã vô tình chiết khấu tổng cộng tới **4 quý: $(1.02)^2 \times (1.02)^2 = (1.02)^4$** (tương đương 1 năm thay vì 6 tháng), tức **chiết khấu gấp đôi thời gian (*double-counted the discounting horizon*)**!
- **Định lượng sai số định giá (*Pricing error*):**
  $$\text{Error} = P_{\text{Zeta}} - P_{\text{true}} = 11.152863 - 11.603438 = \mathbf{-\text{USD } 0.450575 \approx -\text{USD } 0.45\text{ per share}}$$
  *(Bảng tính của Zeta đã **định giá thấp** quyền chọn bán mất **USD 0.45/cổ phiếu**, tương đương sai lệch $-3.88\%$). *

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Đối với quyền chọn **châu Âu** trên cây tái hợp (*recombining multiplicative tree*), có thể kiểm tra ngay $P_0$ bằng công thức tổ hợp Nhị thức 1 dòng:
  $$P_0 = \frac{p^2 P_{uu} + 2p(1-p) P_{ud} + (1-p)^2 P_{dd}}{R^2}$$
  Nhưng lưu ý câu a đề yêu cầu rõ *"both three-month put values"* nên bắt buộc phải trình bày cả $P_u = 2.00$ và $P_d = 21.24$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Đọc nhầm "8% nominal annually, compounded quarterly"):** Với lãi suất *nominal APR compounded $m$ times per year*, lãi suất mỗi kỳ chính xác là $r_{\text{nom}} / m = 8\% / 4 = 2\%$ ($R = 1.02$), **KHÔNG lấy $(1.08)^{0.25}$** (đó là khi đề ghi *8% effective annually*!).
- **Bẫy 2 (Chính là lỗi của Zeta!):** Khi đã đứng trên từng bước lùi của cây nhị phân, mỗi bước chỉ lùi **1 kỳ ($\Delta t = 3$ tháng)** nên chỉ chia cho **$R = 1.02$**, tuyệt đối không chia cho tổng hệ số chiết khấu toàn kỳ hạn $R^2$ ở mỗi nút!

---

## Question 33 (Average) — Cây Nhị Phân Cộng Tuyến Tính (Additive Tree) & Xác Suất Thay Đổi Theo Nút
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Chi shares trade at USD 40. In each of the next two years, the price either rises by USD 12 or falls by USD 8. The risk-free rate is 10% effective annually. A European put expires in two years with strike USD 48.
>
> a. Calculate the risk-neutral up probability at the root and at each one-year node, then value the put.
>
> b. Psi uses the root up probability at every node. Calculate the resulting put price and explain any difference from part a.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 40$; cây **CỘNG SỐ ĐÔ LA CỐ ĐỊNH (*Additive dollar moves*)** qua 2 năm (mỗi bước 1 năm): mỗi năm tăng $+\text{USD } 12$ hoặc giảm $-\text{USD } 8$!
- Lãi suất phi rủi ro $r = 10\%$ EAR $\implies R = 1.10$ mỗi năm. Put châu Âu 2 năm có strike $K = \text{USD } 48$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Xác suất trung hòa rủi ro tại Nút gốc và hai Nút Năm 1 & Định giá Put**
- Trên cây nhị phân bất kỳ, tại một nút có giá cổ phiếu hiện hành là $S$ đi tới $S_{\text{up}} = S + 12$ hoặc $S_{\text{down}} = S - 8$, điều kiện trung hòa rủi ro $E^Q[S_{\text{next}} \mid S] = S \cdot R = 1.10 S$ cho công thức tổng quát:
  $$p(S) = \frac{1.10 S - (S - 8)}{(S + 12) - (S - 8)} = \frac{0.10 S + 8}{20}$$
1. **Tại Nút gốc ($t = 0, S_0 = 40 \to 52\text{ hoặc }32$):**
   $$p_0 = \frac{40(1.10) - 32}{52 - 32} = \frac{44 - 32}{20} = \frac{12}{20} = \mathbf{0.60} \quad (60.00\%,\; 1 - p_0 = 0.40)$$
2. **Tại Nút Năm 1 nhánh Tăng ($t = 1, S_u = 52 \to 64\text{ hoặc }44$):**
   $$p_u = \frac{52(1.10) - 44}{64 - 44} = \frac{57.20 - 44}{20} = \frac{13.20}{20} = \mathbf{0.66} \quad (66.00\%,\; 1 - p_u = 0.34)$$
3. **Tại Nút Năm 1 nhánh Giảm ($t = 1, S_d = 32 \to 44\text{ hoặc }24$):**
   $$p_d = \frac{32(1.10) - 24}{44 - 24} = \frac{35.20 - 24}{20} = \frac{11.20}{20} = \mathbf{0.56} \quad (56.00\%,\; 1 - p_d = 0.44)$$
4. **Định giá quyền chọn bán ($K = 48$) bằng quy nạp ngược:**
   - Giá cổ phiếu & Payoff tại $T = 2$:
     - $S_{uu} = 64 \implies P_{uu} = \max(48 - 64, 0) = 0$.
     - $S_{ud} = S_{du} = 44 \implies P_{ud} = P_{du} = \max(48 - 44, 0) = 4.00$.
     - $S_{dd} = 24 \implies P_{dd} = \max(48 - 24, 0) = 24.00$.
   - Giá trị Put tại Năm 1 (dùng đúng $p_u = 0.66$ ở nút trên và $p_d = 0.56$ ở nút dưới!):
     $$P_u = \frac{0.66(0) + 0.34(4.00)}{1.10} = \frac{1.36}{1.10} = \text{USD } 1.236364 \quad (\approx \text{USD } 1.24)$$
     $$P_d = \frac{0.56(4.00) + 0.44(24.00)}{1.10} = \frac{2.24 + 10.56}{1.10} = \frac{12.80}{1.10} = \text{USD } 11.636364 \quad (\approx \text{USD } 11.64)$$
   - **Giá trị Put hiện tại tại $t = 0$ (dùng $p_0 = 0.60$):**
     $$P_0 = \frac{0.60(1.236364) + 0.40(11.636364)}{1.10} = \frac{0.60(1.36) + 0.40(12.80)}{1.10^2} = \frac{0.816 + 5.120}{1.21} = \frac{5.936}{1.21} = \mathbf{\text{USD } 4.905785 \approx \text{USD } 4.91}$$

#### **b. Giá Put sai khi Psi dùng $p_0 = 0.60$ ở mọi nút & Giải thích nguyên nhân sai lệch**
- **Giá Put theo cách tính của Psi ($p = 0.60$ cố định toàn cây):**
  $$P_{0,\Psi} = \frac{0.60^2(0) + 2(0.60)(0.40)(4.00) + 0.40^2(24.00)}{1.10^2} = \frac{1.92 + 3.84}{1.21} = \frac{5.76}{1.21} = \mathbf{\text{USD } 4.760331 \approx \text{USD } 4.76}$$
- **Chênh lệch & Giải thích kinh tế:**
  - Psi đã **định giá thấp quyền chọn bán mất $4.905785 - 4.760331 = \text{USD } 0.145455 \approx \text{USD } 0.15$** ($\text{USD } 4.76$ so với $\text{USD } 4.91$).
  - **Nguyên nhân gốc rễ:** Xác suất trung hòa rủi ro chỉ không đổi giữa các nút trên **cây nhân tỷ lệ phần trăm không đổi (*multiplicative tree*)**. Ở đây biến động giá cổ phiếu là **số tiền tuyệt đối cố định ($+12 / -8$)** nên tỷ suất sinh lời phần trăm ($+12/S$ và $-8/S$) thay đổi theo mức giá $S$, trong khi mức tăng trưởng kỳ vọng trung hòa rủi ro phải luôn đạt $10\% \times S$ (tức tăng USD 4.00 ở $S_0=40$, tăng USD 5.20 ở $S_u=52$, nhưng chỉ tăng USD 3.20 ở $S_d=32$)!
  - Cụ thể: tại nút dưới $S_d = 32$ — nơi quyền chọn bán tập trung phần lớn giá trị (payoff USD 4 và USD 24) — xác suất tăng hợp lý giảm xuống $p_d = 0.56 < 0.60$ (xác suất rơi vào trạng thái giảm sâu $dd$ thực chất là $0.44$ chứ không phải $0.40$). Việc Psi áp cứng $0.60$ tại $S_d = 32$ vi phạm điều kiện không-arbitrage tại nút đó ($0.60 \times 44 + 0.40 \times 24 = 36.00 \neq 32 \times 1.10 = 35.20$) và đánh tụt trọng số của trạng thái ITM sâu $S_{dd} = 24$ (từ $0.40 \times 0.44 = 0.176$ xuống $0.40 \times 0.40 = 0.160$), làm giá Put bị ép thấp giả tạo (hiệu ứng đánh thấp ở nút $d$ lấn át hiệu ứng đánh cao nhẹ ở nút $u$ do tính lồi của payoff quyền chọn bán!).

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Công thức tổng quát không bao giờ sai cho MỌI loại cây nhị phân (cả nhân lẫn cộng, kể cả cây phi đối xứng bất kỳ!):**
  Đừng thuộc lòng máy móc $p = \frac{R - d}{u - d}$ mà hãy nhớ công thức gốc bằng giá đô-la tại từng nút:
  $$p = \frac{S_{\text{node}} \cdot R - S_{\text{down}}}{S_{\text{up}} - S_{\text{down}}}$$
  Công thức này tự động quy về $\frac{R - d}{u - d}$ khi cây nhân, và cho đáp số đúng tuyệt đối $100\%$ khi cây cộng đô-la như Câu 33!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy quán tính lấy $u = 52/40 = 1.30, d = 32/40 = 0.80$ ở gốc rồi dùng lại cho cả năm 2:** Đây chính là lỗi của nhân vật Psi trong đề! Luôn đọc thật kỹ đề ghi **"rises by 20%"** (cây nhân $\rightarrow p$ hằng số) hay **"rises by USD 12"** (cây cộng $\rightarrow$ bắt buộc tính lại $p$ ở từng nút!).

---

## Question 34 (Average) — Quyền Chọn Bán Deep-ITM Black-Scholes & Cận Dưới Châu Âu vs. Mỹ
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Omega shares trade at USD 60. One-year European options have strike USD 75. Annual volatility is 15%, and the continuously compounded risk-free rate is 8% per year.
>
> a. Calculate the European put value using Black-Scholes and verify it using the matching call and put-call parity.
>
> b. An analyst claims that any put price below USD 15 creates an immediate exercise arbitrage. Assess the claim for this put and for an otherwise identical American put.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 60$; kỳ hạn $T = 1$ năm; strike $K = \text{USD } 75$ (Put đang *deep in-the-money*, giá trị nội tại hiện tại $K - S_0 = \text{USD } 15.00$!).
- Độ biến động $\sigma = 15\%$/năm; lãi suất phi rủi ro liên tục $r = 8\%$/năm.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Định giá European Put bằng Black-Scholes & Kiểm chứng qua Call và Put-Call Parity**
1. **Tính $PV(K), d_1, d_2$:**
   $$PV(K) = 75 e^{-0.08 \times 1} = 75 \times 0.92311635 = \text{USD } 69.233726$$
   $$d_1 = \frac{\ln(60 / 75) + (0.08 + 0.5 \times 0.15^2)(1)}{0.15\sqrt{1}} = \frac{-0.22314355 + 0.09125000}{0.15} = \mathbf{-0.879290}$$
   $$d_2 = d_1 - 0.15 = -0.879290 - 0.15 = \mathbf{-1.029290}$$
2. **Giá trị European Put theo công thức Black-Scholes:**
   - Tra phân phối chuẩn tắc: $N(-d_1) = N(0.879290) = \mathbf{0.810378}$; $N(-d_2) = N(1.029290) = \mathbf{0.848328}$.
   $$P_0 = PV(K) N(-d_2) - S_0 N(-d_1) = 69.233726(0.848328) - 60(0.810378) = 58.732944 - 48.622694 = \mathbf{\text{USD } 10.110250 \approx \text{USD } 10.11}$$
3. **Kiểm chứng qua quyền chọn mua tương ứng ($C_0$) và Put-Call Parity:**
   - $N(d_1) = 1 - 0.810378 = 0.189622$; $N(d_2) = 1 - 0.848328 = 0.151672$.
   - Giá Call tương ứng:
     $$C_0 = 60(0.189622) - 69.233726(0.151672) = 11.377306 - 10.500782 = \mathbf{\text{USD } 0.876524 \approx \text{USD } 0.88}$$
   - Kiểm tra Put-Call Parity:
     $$P_0 = C_0 - S_0 + PV(K) = 0.876524 - 60.00 + 69.233726 = \mathbf{\text{USD } 10.110250 \approx \text{USD } 10.11} \quad (\text{Khớp chính xác 100\%!})$$

#### **b. Đánh giá tuyên bố: "Mọi mức giá Put thấp hơn USD 15 đều tạo ra Arbitrage thực hiện ngay"**
1. **Đối với quyền chọn bán kiểu CHÂU ÂU này (European Put): Nhận định của chuyên gia là SAI (FALSE)!**
   - Người nắm giữ European Put **không được phép thực hiện quyền chọn trước ngày đáo hạn**, nên không thể mua cổ phiếu giá USD 60 hôm nay để bán ngay ở giá USD 75 hôm nay!
   - Vì phải chờ 1 năm mới được nhận USD 75 trong môi trường lãi suất $8\%$, giá trị hiện tại của khoản tiền thực hiện chỉ còn $PV(K) = \text{USD } 69.23$. Cận dưới không-arbitrage của European Put là:
     $$P_{\text{Eur}} \ge \max\left(0,\; K e^{-rT} - S_0\right) = 69.233726 - 60.00 = \mathbf{\text{USD } 9.233726 \approx \text{USD } 9.23}$$
   - Minh chứng rõ nhất: Chính mức giá cân bằng không-arbitrage của Black-Scholes vừa tính ở câu a là **USD 10.11** — nhỏ hơn hẳn USD 15.00 (có *negative time value* $= 10.11 - 15.00 = -\text{USD } 4.89$) nhưng lớn hơn cận dưới châu Âu USD 9.23 nên hoàn toàn không có bất kỳ cơ hội arbitrage nào!
2. **Đối với quyền chọn bán kiểu MỸ tương đồng (American Put): Nhận định của chuyên gia là ĐÚNG (TRUE)!**
   - Vì American Put cho phép thực hiện **ngay lập tức tại $t = 0$**, cận dưới không-arbitrage của nó là:
     $$P_{\text{Amer}} \ge \max(0,\; K - S_0) = 75.00 - 60.00 = \mathbf{\text{USD } 15.00}$$
   - Nếu American Put được chào bán ở bất kỳ mức giá $P_{\text{mkt}} < \text{USD } 15.00$, nhà kinh doanh chênh lệch giá chỉ cần **mua 1 cổ phiếu giá USD 60 + mua 1 American Put giá $P_{\text{mkt}}$**, rồi **thực hiện quyền bán cổ phiếu ngay tức khắc thu về USD 75**, bỏ túi khoản lãi tức thời không rủi ro là $\mathbf{15.00 - P_{\text{mkt}} > 0}$!

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ:**
> - **European Put có thể giao dịch THẤP HƠN giá trị nội tại hiện tại ($P_{\text{Eur}} < K - S_0$, tức Time Value ÂM!)** khi quyền chọn đang *deep ITM* và lãi suất $r > 0$ đủ cao, bởi vì cận dưới châu Âu chỉ là $PV(K) - S_0 < K - S_0$.
> - Ngược lại, **American Put KHÔNG BAO GIỜ giao dịch thấp hơn giá trị nội tại ($P_{\text{Amer}} \ge K - S_0$)**, và trong trường hợp $P_{\text{Eur}} < K - S_0$ như bài này ($10.11 < 15.00$), chắc chắn $P_{\text{Amer}} > P_{\text{Eur}}$ và việc thực hiện sớm American Put có giá trị dương!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Nhớ công thức đối xứng xác suất chuẩn tắc: $N(-x) = 1 - N(x)$. Tính $C_0$ trước hay $P_0$ trước đều được, rồi dùng ngay $P_0 - C_0 = PV(K) - S_0 = 69.233726 - 60 = 9.233726$ để kiểm tra chéo 2 kết quả chỉ trong 2 giây ($10.110250 - 0.876524 = 9.233726$ — chuẩn từng chữ số thập phân thứ 6!).

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy quên đổi dấu $-d_1$ và $-d_2$ trong công thức Put Black-Scholes:** Công thức Put là $PV(K) N(\mathbf{-d_2}) - S_0 N(\mathbf{-d_1})$! Vì ở đây $d_1 = -0.879, d_2 = -1.029$ vốn đang âm, khi thêm dấu trừ thành $-d_1 = +0.879$ và $-d_2 = +1.029$ thì $N(-d_1) = 0.810$ và $N(-d_2) = 0.848$ đều $> 0.5$!

---

## Question 35 (Average) — Danh Mục Mô Phỏng Black-Scholes, Bước Nhảy Giá Lớn & Độ Lồi (Gamma)
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Alpha shares trade at USD 84. A six-month European call has strike USD 86. Annual volatility is 25%, and the continuously compounded risk-free rate is 4% per year. One contract covers 100 shares.
>
> a. Value the contract and determine the stock and cash holdings initially required to replicate a long contract.
>
> b. The stock price rises immediately to USD 90, with no elapsed time or change in the other inputs. Compare the unchanged replicating portfolio's value with the repriced call contract. Quantify the difference and explain why it arises.

**Tóm tắt thông số:**
- Ban đầu: $S_0 = \text{USD } 84$; $T = 0.50$ năm; $K = \text{USD } 86$; $\sigma = 25\%$; $r = 4\%$ liên tục; **1 hợp đồng = 100 cổ phiếu**.
- Sau cú sốc tức thời ($\Delta t = 0$): Giá cổ phiếu nhảy vọt lên $S_{\text{new}} = \text{USD } 90$ ($\Delta S = +6$).

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Định giá hợp đồng Call (100 cổ phiếu) & Danh mục Mô phỏng Ban đầu**
1. **Tính các thông số BSM tại $S_0 = \text{USD } 84$:**
   $$PV(K) = 86 e^{-0.04 \times 0.50} = 86 e^{-0.02} = \text{USD } 84.297086$$
   $$\sigma\sqrt{T} = 0.25 \sqrt{0.50} = 0.17677670$$
   $$d_1 = \frac{\ln(84 / 86) + (0.04 + 0.5 \times 0.25^2)(0.50)}{0.17677670} = \frac{-0.02353050 + 0.03562500}{0.17677670} = \mathbf{0.068417}$$
   $$d_2 = d_1 - 0.17677670 = \mathbf{-0.108360}$$
   $$N(d_1) = \mathbf{0.527273}, \qquad N(d_2) = \mathbf{0.456855}$$
2. **Giá trị trên 1 cổ phiếu & Tổng giá trị 1 hợp đồng (100 cổ phiếu):**
   $$c_0 = 84(0.527273) - 84.297086(0.456855) = 44.290940 - 38.511555 = \text{USD } 5.779384\text{/cp}$$
   $$C_{\text{contract}}(84) = 100 \times 5.779384 = \mathbf{\text{USD } 577.9384 \approx \text{USD } 577.94}$$
3. **Danh mục mô phỏng ban đầu cho 1 hợp đồng Long Call (100 cổ phiếu):**
   - Trong cấu trúc $C = 100 S_0 N(d_1) - 100 PV(K) N(d_2)$:
   - **Lượng cổ phiếu nắm giữ (*Stock holding*):**
     $$\text{Shares} = 100 \times N(d_1) = 100 \times 0.52727309 = \mathbf{52.7273 \approx 52.73\text{ shares}} \quad (\text{trị giá USD } 4,429.09)$$
   - **Vị thế tiền mặt (*Cash holding*):**
     $$\text{Cash} = -100 \times PV(K) N(d_2) = -100 \times 38.511555 = \mathbf{-\text{USD } 3,851.1555 \approx -\text{USD } 3,851.16} \quad (\text{Đi vay USD } 3,851.16)$$
   *(Kiểm lại: $4,429.0940 - 3,851.1555 = \text{USD } 577.9384$!).*

#### **b. So sánh Danh mục Mô phỏng Giữ Nguyên với Hợp đồng Call Định Giá Lại tại $S_{\text{new}} = 90$**
1. **Giá trị của danh mục mô phỏng không điều chỉnh tại $S_{\text{new}} = \text{USD } 90$:**
   $$V_{\text{rep}}(90) = 52.727309 \times 90.00 - 3,851.1555 = 4,745.4578 - 3,851.1555 = \mathbf{\text{USD } 894.3023 \approx \text{USD } 894.30}$$
   *(Hoặc tính qua xấp xỉ tuyến tính Delta: $577.9384 + 52.727309 \times (90 - 84) = 577.9384 + 316.3639 = \text{USD } 894.3023$).*
2. **Giá trị hợp đồng Call định giá lại bằng Black-Scholes tại $S_{\text{new}} = \text{USD } 90$:**
   $$d_1^{\text{new}} = \frac{\ln(90 / 86) + 0.03562500}{0.17677670} = \frac{0.04546237 + 0.03562500}{0.17677670} = \mathbf{0.458699} \implies N(d_1^{\text{new}}) = \mathbf{0.676775}$$
   $$d_2^{\text{new}} = 0.458699 - 0.17677670 = \mathbf{0.281923} \implies N(d_2^{\text{new}}) = \mathbf{0.610999}$$
   $$C_{\text{contract}}(90) = 100 \times \left[90(0.676775) - 84.297086(0.610999)\right] = 100 \times (60.909771 - 51.505425) = \mathbf{\text{USD } 940.4346 \approx \text{USD } 940.43}$$
3. **Định lượng chênh lệch & Giải thích nguyên nhân (Convexity / Gamma Effect):**
   - **Độ chênh lệch:** Hợp đồng Call định giá lại **cao hơn** danh mục mô phỏng giữ nguyên một khoảng:
     $$C_{\text{contract}}(90) - V_{\text{rep}}(90) = 940.4346 - 894.3023 = \mathbf{+\text{USD } 46.1323 \approx \text{USD } 46.13} \quad (\text{tức USD } 0.46\text{/cp})$$
   - **Giải thích bản chất kinh tế:**
     - Danh mục mô phỏng Black-Scholes tại $S_0 = 84$ chỉ là **xấp xỉ tiếp tuyến bậc nhất cục bộ (*local first-order tangent approximation*)** đúng cho những dịch chuyển giá vô cùng bé ($dS \to 0$) và đòi hỏi **tái cân bằng liên tục (*continuous rebalancing*)**.
     - Giá quyền chọn mua là một hàm **lồi nghiêm ngặt theo giá cổ phiếu (*strictly convex in $S$*, tức có $\Gamma = \frac{\partial \Delta}{\partial S} > 0$)**: khi giá cổ phiếu nhảy vọt từ USD 84 lên USD 90, hệ số Delta thực của hợp đồng tăng từ $52.73$ cổ phiếu lên $67.68$ cổ phiếu. Vì danh mục tĩnh bị "kẹt" ở độ dốc cũ thấp hơn ($52.73$ cổ phiếu, đường tiếp tuyến thẳng) mà không kịp mua đuổi thêm cổ phiếu trong quá trình giá tăng, đường thẳng tiếp tuyến luôn nằm **thấp hơn đường cong lồi** của giá quyền chọn đối với mọi bước nhảy giá hữu hạn $\Delta S \neq 0$!

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ (DELTA-GAMMA APPROXIMATION):**
> - Với **Long Call hoặc Long Put**, luôn có **Gamma dương ($\Gamma > 0$)** $\implies$ Đường cong giá quyền chọn nằm **TRÊN** đường tiếp tuyến mô phỏng tĩnh ở **CẢ HAI CHIỀU** giá nhảy tăng mạnh lẫn giá sụt giảm mạnh:
>   $$\Delta C_{\text{exact}} \approx \Delta \cdot \Delta S + \frac{1}{2} \Gamma (\Delta S)^2 > \Delta \cdot \Delta S \quad (\forall \Delta S \neq 0)$$
> - Hệ quả sống còn cho người **Bán quyền chọn (Short Option / Negative Gamma)**: Nếu chỉ phòng hộ Delta tĩnh mà gặp cú nhảy giá lớn (*gap/jump*), danh mục phòng hộ sẽ luôn **hụt tiền** so với nghĩa vụ quyền chọn!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Khi đọc công thức Black-Scholes $C = S N(d_1) - PV(K) N(d_2)$, **không cần giải hệ phương trình gì cả** để tìm danh mục mô phỏng! Hằng đẳng thức Euler cho biết luôn:
  - Số cổ phiếu trên 1 quyền chọn $= \mathbf{+N(d_1)}$ (cho Call) hoặc $\mathbf{-N(-d_1)}$ (cho Put).
  - Tiền mặt trên 1 quyền chọn $= \mathbf{-PV(K)N(d_2)}$ (cho Call, đi vay) hoặc $\mathbf{+PV(K)N(-d_2)}$ (cho Put, cho vay).
  - Nhớ nhân **100** khi đề hỏi cho **1 hợp đồng (100 shares)**!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy quên nhân 100 cổ phiếu/hợp đồng:** Đề hỏi *"Value **the contract** and determine the stock and cash holdings initially required to replicate **a long contract**"* $\rightarrow$ Phải báo cáo **USD 577.94**, **52.73 shares**, **-USD 3,851.16** và chênh lệch **USD 46.13** (kèm số trên 1 cổ phiếu trong ngoặc để an toàn tuyệt đối!).

---

## Question 36 (Average) — Nội Suy Độ Biến Động Hàm Ý (Implied Volatility) & Rủi Ro Bán Quyền Chọn
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Beta shares trade at USD 100. A one-year European call with strike USD 100 trades at USD 10.40. The continuously compounded risk-free rate is 3% per year. A worksheet gives these Black-Scholes prices:
>
> | Annual volatility | Call value per share |
> |---|---:|
> | 18% | USD 8.640660 |
> | 20% | USD 9.413403 |
> | 25% | USD 11.348477 |
> | 30% | USD 13.283308 |
>
> a. Identify the interval containing implied volatility and estimate it by linear interpolation between the nearest listed prices.
>
> b. Beta's estimated historical volatility is 18%. Calculate the market-price gap relative to that estimate. Does the gap establish that selling the call guarantees a profit?

**Tóm tắt thông số:**
- $S_0 = 100, K = 100, T = 1, r = 3\%$ cc; giá thị trường của Call: $C_{\text{mkt}} = \text{USD } 10.40$.
- Bảng giá BSM theo $\sigma$; độ biến động lịch sử ước lượng $\sigma_{\text{hist}} = 18\%$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Khoảng chứa Implied Volatility & Ước lượng bằng Nội suy Tuyến tính**
- Giá quyền chọn mua Black-Scholes là một hàm đồng biến nghiêm ngặt theo độ biến động ($\text{Vega} = \frac{\partial C}{\partial \sigma} > 0$).
- Vì $\text{USD } 9.413403 < \text{USD } 10.40 < \text{USD } 11.348477$, độ biến động hàm ý (*implied volatility* $\sigma_{\text{imp}}$) chắc chắn nằm trong khoảng **từ 20% đến 25%** (*interval $[20\%, 25\%]$*).
- Nội suy tuyến tính giữa hai mốc gần nhất $(20\%, 9.413403)$ và $(25\%, 11.348477)$:
  $$\sigma_{\text{imp}} \approx 20\% + \frac{10.40 - 9.413403}{11.348477 - 9.413403} \times (25\% - 20\%)$$
  $$\sigma_{\text{imp}} \approx 20\% + \frac{0.986597}{1.935074} \times 5\% = 20\% + 0.5098498 \times 5\% = 20\% + 2.549249\% = \mathbf{22.55\%} \quad (22.5492\%)$$
  *(Nhận xét hay: Đối với quyền chọn gần ATM, $C(\sigma)$ gần như tuyến tính hoàn hảo theo $\sigma$, nên phép nội suy này chính xác tới tận hàng phần vạn!).*

#### **b. Chênh lệch Giá Thị Trường so với Độ biến động Lịch sử 18% & Đánh giá cơ hội "Lãi chắc chắn"**
1. **Độ chênh lệch giá thị trường (*Market-price gap*):**
   - Tại $\sigma_{\text{hist}} = 18\%$, giá BSM là $\text{USD } 8.640660$.
   - Khoản chênh lệch của giá thị trường so với mức định giá từ biến động lịch sử là:
     $$\text{Price Gap} = C_{\text{mkt}} - C(18\%) = 10.40 - 8.640660 = \mathbf{+\text{USD } 1.759340 \approx +\text{USD } 1.76\text{ per share}}$$
2. **Khoản chênh lệch USD 1.76 này có chứng minh rằng bán Call đảm bảo lãi chắc chắn không? KHÔNG (NO)!**
   - **Thứ nhất — Quá khứ $\neq$ Tương lai (*Backward-looking vs. Forward-looking*):** Độ biến động lịch sử $18\%$ chỉ đo lường dao động trong *quá khứ* (và bản thân nó cũng có sai số ước lượng mẫu), trong khi độ biến động hàm ý $22.55\%$ phản ánh kỳ vọng của thị trường về mức độ biến động *trong 1 năm tới* (chẳng hạn sắp có công bố sản phẩm mới, M&A, rủi ro vĩ mô hoặc thay đổi chế độ biến động). Nếu biến động thực tế năm tới đạt $\ge 22.55\%$, mức giá USD 10.40 hoàn toàn hợp lý!
   - **Thứ hai — Rủi ro mô hình, bước nhảy giá & chi phí phòng hộ (*Not a riskless arbitrage*):** Bán quyền chọn trần (*naked short call*) có rủi ro thua lỗ không giới hạn nếu cổ phiếu tăng vọt. Ngay cả khi thực hiện phòng hộ Delta (*delta-hedging*), trong thực tế không thể tái cân bằng liên tục không ma sát, độ biến động ngẫu nhiên (*stochastic volatility*), bước nhảy giá rời rạc (*jumps / Gamma risk*) và phần bù rủi ro phương sai (*variance risk premium*) khiến người bán vẫn chịu rủi ro thua lỗ thực sự nếu biến động thực hiện (*realized volatility*) bùng nổ vượt $22.55\%$. Do đó đây chỉ là một **vị thế đặt cược vào độ biến động mang tính rủi ro (*risky volatility trade*)**, tuyệt đối không phải kinh doanh chênh lệch giá phi rủi ro!

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ:**
> - **Implied Volatility (IV)** là biến số hướng tới tương lai (*forward-looking, risk-neutral*) được suy ngược từ giá quyền chọn thị trường qua công thức BSM (nhờ tính đơn điệu $\text{Vega} > 0$).
> - Thực nghiệm trên thị trường tài chính: **IV thường cao hơn Historical/Expected Realized Volatility** do nhà đầu tư sẵn sàng trả thêm **Phần bù Rủi ro Biến động / Sụp đổ (*Variance Risk Premium*)** để mua bảo hiểm quyền chọn! Vì thế thấy $\text{IV} > \text{HV}$ là hiện tượng bình thường của phần bù rủi ro, KHÔNG phải arbitrage!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Công thức Nội suy Tuyến tính tổng quát không bao giờ nhầm thứ tự:
  $$\sigma_{\text{imp}} = \sigma_{\text{low}} + \frac{C_{\text{mkt}} - C_{\text{low}}}{C_{\text{high}} - C_{\text{low}}} (\sigma_{\text{high}} - \sigma_{\text{low}})$$
  Kiểm tra mắt ngay: $10.40$ nằm gần chính giữa $9.41$ và $11.35$ (nhỉnh hơn điểm giữa $10.38$ một chút xíu) $\implies$ kết quả phải nhỉnh hơn $22.50\%$ một chút xíu $\rightarrow \mathbf{22.55\%}$!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy nội suy bằng hai đầu mút xa nhất (18% và 30%) thay vì hai mốc lân cận gần nhất (20% và 25%):** Đề ghi rất rõ *"between the **nearest** listed prices"* $\rightarrow$ Phải dùng cặp **20% và 25%**!

---

## Question 37 (Average) — Xác Suất Trung Hòa Rủi Ro ($Q$) vs. Xác Suất Thực Tế ($P$) & Implied vs. Realized Volatility
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Gamma uses a one-year stock tree with current price USD 50, terminal prices USD 65 and USD 40, and a 4% effective annual risk-free rate. The pricing worksheet gives a risk-neutral up probability of 48%. A separate forecasting model assigns a 60% chance to the up state.
>
> Assess the following claims with economic reasoning:
>
> a. "The forecast must be wrong because no-arbitrage fixes the actual chance of an up move at 48%."
>
> b. "A different stock's one-year call has implied volatility of 28%, so its realized volatility over the next year will be 28%."

**Tóm tắt thông số:**
- Cây 1 năm: $S_0 = 50$, $S_u = 65$, $S_d = 40$, $r = 4\%$ EAR ($R = 1.04$).
- Xác suất trung hòa rủi ro $q = \frac{50(1.04) - 40}{65 - 40} = \frac{12}{25} = 48\%$; mô hình dự báo kinh tế lượng cho xác suất thực $p_{\text{phys}} = 60\%$.

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Đánh giá tuyên bố: "Dự báo 60% chắc chắn sai vì không-arbitrage ấn định xác suất tăng thực tế là 48%"**
- **Đánh giá:** Tuyên bố này **SAI HOÀN TOÀN (FALSE)** — nhầm lẫn tai hại giữa **Xác suất trung hòa rủi ro (*Risk-neutral probability*, độ đo $Q$)** và **Xác suất thực tế khách quan (*Actual / Physical probability*, độ đo $P$)**!
- **Lý giải kinh tế sắc bén (kèm dẫn chứng số học từ đề bài):**
  1. Lập luận mô phỏng không-arbitrage (*no-arbitrage replication*) định giá quyền chọn chỉ dựa trên $S_0 = 50, S_u = 65, S_d = 40$ và $R = 1.04$, hoàn toàn **độc lập với xác suất thực tế $p_{\text{phys}}$** (miễn là $0 < p_{\text{phys}} < 1$ để hai trạng thái đều có thể xảy ra). Con số $q = 48\%$ chỉ là trọng số định giá nhân tạo điều chỉnh theo rủi ro dùng để chiết khấu bằng lãi suất phi rủi ro $4\%$.
  2. Tại sao $p_{\text{phys}} = 60\% > q = 48\%$ lại hoàn toàn tự nhiên và hợp lý trong cân bằng thị trường? Với $p_{\text{phys}} = 60\%$, giá kỳ vọng thực tế của cổ phiếu cuối năm là $0.60(65) + 0.40(40) = \text{USD } 55.00$, tương ứng tỷ suất sinh lời kỳ vọng thực tế là:
     $$E^P[R_S] = \frac{55.00}{50.00} - 1 = \mathbf{10.00\%} > r_f = 4.00\%$$
     Chênh lệch $10.00\% - 4.00\% = \mathbf{+6.00\%}$ chính là **Phần bù Rủi ro Cổ phiếu dương (*Positive Equity Risk Premium*)** mà các nhà đầu tư ngại rủi ro đòi hỏi để nắm giữ cổ phiếu! Để quy đổi sang thế giới định giá trung hòa rủi ro (chiết khấu ở $4\%$ thay vì $10\%$), độ đo $Q$ tự động hạ thấp trọng số của trạng thái tốt (giá lên 65) từ $60\%$ xuống $48\%$!

#### **b. Đánh giá tuyên bố: "Implied Volatility bằng 28% nên Realized Volatility trong năm tới sẽ bằng 28%"**
- **Đánh giá:** Tuyên bố này cũng **SAI (FALSE)** vì 3 nguyên nhân kinh tế cốt lõi:
  1. **Kỳ vọng trước (Ex-ante) vs. Kết quả ngẫu nhiên thực hiện sau (Ex-post realization):** Kể cả khi thị trường dự báo không chệch, đường đi thực tế của giá cổ phiếu trong năm tới chịu tác động của các cú sốc thông tin ngẫu nhiên bất ngờ, nên độ biến động thực hiện (*ex-post realized volatility*) gần như chắc chắn sẽ khác con số kỳ vọng ban đầu.
  2. **Phần bù rủi ro biến động (*Variance Risk Premium — $Q$ vs. $P$*):** Implied volatility được trích xuất từ giá quyền chọn thị trường nên phản ánh kỳ vọng dưới **độ đo trung hòa rủi ro ($Q$)** chứ không phải độ đo thực tế ($P$). Vì nhà đầu tư ngại rủi ro sụp đổ/biến động mạnh và chấp nhận trả phí bảo hiểm cao cho quyền chọn, *implied volatility* thường lớn hơn có hệ thống so với kỳ vọng biến động thực tế.
  3. **Sai lệch giả định mô hình Black-Scholes (*Model misspecification*):** Implied volatility chỉ là con số đưa vào công thức BSM (vốn giả định phân phối log-chuẩn, độ biến động hằng số, không có nhảy giá) để khớp giá thị trường; khi thực tế có đuôi dày (*fat tails*), nhảy giá (*jumps*) và độ biến động ngẫu nhiên (*volatility smile/skew*), IV còn gánh thêm phần điều chỉnh cho các đặc tính phân phối đó chứ không đồng nhất với độ lệch chuẩn thực tế!

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ:**
> - Khi cổ phiếu có phần bù rủi ro dương ($E^P[R_S] > r_f$, tức $\beta_S > 0$), luôn có:
>   $$p_{\text{physical}} > q_{\text{risk-neutral}} \quad (\text{ở đây: } 60\% > 48\%!)$$
> - Thay đổi $p_{\text{physical}}$ (trong khi giữ nguyên $S_0, S_u, S_d, r_f$) **KHÔNG làm thay đổi giá quyền chọn**, vì mọi sự thay đổi của $p_{\text{physical}}$ đã được hấp thụ hết vào giá cổ phiếu hiện tại $S_0$! (Nhưng nếu kỳ vọng tăng trưởng thay đổi làm $S_0$ tăng lên thì giá quyền chọn mới đổi qua kênh $S_0$).

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Trong tự luận hoặc MCQ về câu 37a, việc bấm thêm 1 dòng số học minh họa $E^P[R_S] = \frac{0.6(65)+0.4(40)}{50} - 1 = 10\%$ so với $r_f = 4\%$ (ERP $= 6\%$) biến câu trả lời lý thuyết thành điểm 10/10 tuyệt đối thuyết phục giám khảo!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy nói "xác suất thực tế hoàn toàn không liên quan gì đến thị trường tài chính":** Diễn đạt chuẩn xác phải là: xác suất thực tế và mức ngại rủi ro của nhà đầu tư cùng nhau quyết định **giá cổ phiếu giao ngay $S_0$**; một khi $S_0$ đã được quan sát trên thị trường, việc định giá phái sinh theo nguyên lý mô phỏng không cần biết riêng lẻ $p_{\text{phys}}$ nữa!

---

## Question 38 (Hard) — Quyền Chọn Bán Kiểu Mỹ Hai Bước, Chiến Lược Thực Hiện Sai Lầm & Bẫy Parity
📌 **[ĐỀ THI TỰ LUẬN KHÔNG CÓ TÍNH TOÁN BSM & AMERICAN OPTIONS — ĐỌC LỜI GIẢI ĐỂ NẮM BẢN CHẤT ĂN ĐIỂM 10 CÂU MCQ!]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Delta shares trade at USD 60. In each of the next two years, the price rises by 25% or falls by 20%. The risk-free rate is 2% effective annually. An American put has strike USD 76 and expires in two years.
>
> Epsilon proposes: "Do not exercise today. At the end of year one, exercise whenever the put is in the money; otherwise hold it until expiration."
>
> a. Calculate the current value of the cash flows generated by this policy.
>
> b. Determine the optimal exercise decisions at every nonterminal node and the American put value. Calculate the matching European put value and the value lost by following Epsilon's policy.
>
> c. Calculate the matching European call value. Compare it with the call price obtained by inserting the American put value into European put-call parity, and explain the difference.

**Tóm tắt thông số:**
- $S_0 = \text{USD } 60$; 2 bước (mỗi bước 1 năm); $u = 1.25$, $d = 0.80$; $r = 2\%$ EAR $\implies R = 1.02$.
- American Put strike $K = \text{USD } 76$ (lưu ý $K = 76$ rất cao so với $S_0 = 60$!).

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **Bước chuẩn bị: Cây giá cổ phiếu & Xác suất trung hòa rủi ro**
- Xác suất tăng trung hòa rủi ro mỗi năm:
  $$p = \frac{1.02 - 0.80}{1.25 - 0.80} = \frac{0.22}{0.45} = \frac{22}{45} \approx \mathbf{0.488889}, \qquad 1 - p = \frac{23}{45} \approx \mathbf{0.511111}$$
- Cây giá cổ phiếu và giá trị thực hiện nội tại của Put ($K = 76$):
  - $t = 0$: $S_0 = 60.00 \implies I_0 = 76 - 60 = 16.00$.
  - $t = 1$:
    - Nhánh Tăng ($u$): $S_u = 60(1.25) = \mathbf{75.00} \implies I_u = \max(76 - 75, 0) = \mathbf{1.00 > 0\text{ (ĐANG ITM!)}}$.
    - Nhánh Giảm ($d$): $S_d = 60(0.80) = \mathbf{48.00} \implies I_d = \max(76 - 48, 0) = \mathbf{28.00 > 0\text{ (ĐANG ITM!)}}$.
  - $t = 2$ (Đáo hạn):
    - $S_{uu} = 75(1.25) = 93.75 \implies P_{uu} = \max(76 - 93.75, 0) = \mathbf{0.00}$.
    - $S_{ud} = 75(0.80) = 60.00 \implies P_{ud} = \max(76 - 60, 0) = \mathbf{16.00}$.
    - $S_{dd} = 48(0.80) = 38.40 \implies P_{dd} = \max(76 - 38.40, 0) = \mathbf{37.60}$.

#### **a. Giá trị hiện tại của dòng tiền tạo bởi quy tắc của Epsilon**
- Quy tắc của Epsilon: Không thực hiện tại $t = 0$; tại cuối Năm 1 ($t = 1$), **hễ quyền chọn đang in-the-money ($S_1 < 76$) thì thực hiện ngay lập tức**.
- Quan sát then chốt: Tại cuối Năm 1, **CẢ HAI NÚT** $S_u = 75 < 76$ (payoff thực hiện $= \text{USD } 1.00$) **VÀ** $S_d = 48 < 76$ (payoff thực hiện $= \text{USD } 28.00$) đều đang in-the-money! Do đó quy tắc của Epsilon dẫn đến việc thực hiện tất toán quyền chọn ngay tại $t = 1$ ở mọi trạng thái!
- Giá trị hiện tại của dòng tiền theo quy tắc Epsilon:
  $$V_{\text{Epsilon}} = \frac{\frac{22}{45}(1.00) + \frac{23}{45}(28.00)}{1.02} = \frac{(22 + 644) / 45}{1.02} = \frac{666}{45 \times 1.02} = \frac{14.80}{1.02} = \frac{740}{51} = \mathbf{\text{USD } 14.509804 \approx \text{USD } 14.51}$$

#### **b. Quyết định thực hiện tối ưu tại từng nút, Giá American Put, Giá European Put & Giá trị bị mất bởi Epsilon**
1. **Xét các nút Năm 1 ($t = 1$):**
   - **Tại nút $(t = 1, u)$ với $S_u = 75.00$:**
     - Giá trị giữ tiếp (*Continuation value*): $H_u = \frac{\frac{22}{45}(0.00) + \frac{23}{45}(16.00)}{1.02} = \frac{368}{45.90} = \mathbf{\text{USD } 8.017429 \approx \text{USD } 8.02}$.
     - Giá trị thực hiện ngay (*Immediate exercise*): $I_u = 76 - 75 = \text{USD } 1.00$.
     - Vì $H_u (8.02) > I_u (1.00) \implies$ **Quyết định tối ưu tại $(t = 1, u)$: GIỮ TIẾP (HOLD / Do NOT exercise)**! Giá trị nút $P_u^{\text{Amer}} = \mathbf{\text{USD } 8.017429}$. *(Epsilon thực hiện bừa khi quyền chọn mới chớm ITM USD 1.00 đã vứt sọt rác mất USD 7.02 giá trị thời gian/bảo hiểm!).*
   - **Tại nút $(t = 1, d)$ với $S_d = 48.00$:**
     - Giá trị giữ tiếp (*Continuation value*): $H_d = \frac{\frac{22}{45}(16.00) + \frac{23}{45}(37.60)}{1.02} = \frac{352 + 864.80}{45.90} = \frac{1,216.80}{45.90} = \mathbf{\text{USD } 26.509804 \approx \text{USD } 26.51}$.
     - Giá trị thực hiện ngay (*Immediate exercise*): $I_d = 76 - 48 = \text{USD } 28.00$.
     - Vì $I_d (28.00) > H_d (26.51) \implies$ **Quyết định tối ưu tại $(t = 1, d)$: THỰC HIỆN SỚM (EXERCISE EARLY)**! Giá trị nút $P_d^{\text{Amer}} = \mathbf{\text{USD } 28.00}$. *(Bản chất: từ $S_d = 48$, cả hai nhánh con năm 2 là $60$ và $38.40$ đều nằm dưới $76$, nên giữ tiếp không có bất kỳ lợi ích bảo hiểm tăng giá nào mà chỉ mất trắng 1 năm tiền lãi trên USD 76: $76 - 76/1.02 = 1.490196 = 28.00 - 26.509804$!).*
2. **Xét nút gốc ($t = 0, S_0 = 60.00$):**
   - Giá trị giữ tiếp tối ưu:
     $$H_0^{\text{Amer}} = \frac{\frac{22}{45}(8.017429) + \frac{23}{45}(28.00)}{1.02} = \frac{18.230840}{1.02} = \mathbf{\text{USD } 17.873278 \approx \text{USD } 17.87}$$
   - Giá trị thực hiện ngay hôm nay: $I_0 = 76 - 60 = \text{USD } 16.00$.
   - Vì $H_0^{\text{Amer}} (17.87) > I_0 (16.00) \implies$ **Quyết định tối ưu tại $t = 0$: GIỮ TIẾP (HOLD / Do NOT exercise)**!
   - **Giá trị American Put ($P_0^{\text{Amer}}$):** **USD 17.87** (*chính xác: $\text{USD } 17.873278$*).
3. **Giá trị European Put tương ứng ($P_0^{\text{Eur}}$, không được thực hiện sớm ở nút $d$, dùng $H_u$ và $H_d$):**
   $$P_0^{\text{Eur}} = \frac{\frac{22}{45}(8.017429) + \frac{23}{45}(26.509804)}{1.02} = \mathbf{\text{USD } 17.126556 \approx \text{USD } 17.13}$$
   *(Phần bù thực hiện sớm — Early-exercise premium $= 17.873278 - 17.126556 = \text{USD } 0.746722 \approx \text{USD } 0.75$).*
4. **Giá trị bị đánh mất khi làm theo chính sách sai lầm của Epsilon:**
   $$\text{Value Lost} = P_0^{\text{Amer}} - V_{\text{Epsilon}} = 17.873278 - 14.509804 = \mathbf{\text{USD } 3.363474 \approx \text{USD } 3.36}$$
   *(Thậm chí còn thấp hơn cả việc nắm giữ thụ động đến đáo hạn như European Put USD 17.13!).*

#### **c. Giá trị European Call tương ứng & Tại sao thay American Put vào European Put-Call Parity lại sai**
1. **Giá trị European Call đúng ($K = 76$):**
   - Payoff đáo hạn của Call: $C_{uu} = 93.75 - 76 = 17.75$; $C_{ud} = 0$; $C_{dd} = 0$.
   $$C_0^{\text{Eur}} = \frac{\left(\frac{22}{45}\right)^2 \times 17.75}{(1.02)^2} = \frac{0.23901235 \times 17.75}{1.0404} = \mathbf{\text{USD } 4.077729 \approx \text{USD } 4.08}$$
   *(Kiểm lại bằng European Put-Call Parity chuẩn: $P_0^{\text{Eur}} + S_0 - \frac{76}{1.02^2} = 17.126556 + 60 - 73.048827 = \text{USD } 4.077729$ — khớp tuyệt đối!).*
2. **Giá Call thu được nếu lắp nhầm $P_0^{\text{Amer}}$ vào đẳng thức European Put-Call Parity:**
   $$C_{\text{wrong}} = P_0^{\text{Amer}} + S_0 - \frac{76}{(1.02)^2} = 17.873278 + 60.00 - 73.048827 = \mathbf{\text{USD } 4.824450 \approx \text{USD } 4.82}$$
3. **So sánh & Giải thích bản chất sự chênh lệch:**
   - Cách lắp nhầm này **thổi phồng giá European Call thêm đúng $4.824450 - 4.077729 = \text{USD } 0.746722 \approx \text{USD } 0.75$**, bằng **chính xác 100% Phần bù Thực hiện Sớm (*Early-Exercise Premium*, $P_0^{\text{Amer}} - P_0^{\text{Eur}}$)** của American Put!
   - Đẳng thức Put-Call Parity $C_0 + PV(K) = S_0 + P_0$ dựa trên danh mục tĩnh nắm giữ tới cùng một thời điểm đáo hạn cố định $T$ nên **chỉ đúng dưới dạng dấu bằng cho quyền chọn châu Âu**! Đối với quyền chọn kiểu Mỹ không cổ tức, vì $P_{\text{Amer}} > P_{\text{Eur}}$ khi có thực hiện sớm tối ưu, ta chỉ có bất đẳng thức $S_0 - K \le C_{\text{Amer}} - P_{\text{Amer}} \le S_0 - PV(K)$.

> [!NOTE]
> 💡 **BẢN CHẤT CỐT LÕI ĂN ĐIỂM 10 CÂU MCQ:**
> 1. **"Đang In-The-Money" KHÔNG ĐỒNG NGHĨA với "Nên thực hiện sớm American Put"!** Chỉ thực hiện sớm American Put khi quyền chọn ở trạng thái **deep ITM đủ sâu** sao cho lợi ích tiền lãi thu sớm trên $K$ lớn hơn giá trị bảo hiểm biến động còn lại ($I_{\text{node}} > H_{\text{node}}$, như tại $S_d = 48$, trái ngược hoàn toàn với $S_u = 75$ hay $S_0 = 60$!).
> 2. Tuyệt đối **KHÔNG BAO GIỜ thay giá American Put vào đẳng thức European Put-Call Parity** — làm vậy sẽ cộng nhầm *early-exercise premium* của Put sang cho Call!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- Công thức siêu tốc kiểm tra chéo **Value Lost** của Epsilon ở câu b: Epsilon hành xử y hệt chiến lược tối ưu tại $t = 0$ (cùng Hold) và tại nút $d$ (cùng Exercise nhận $28$), chỉ làm sai duy nhất tại nút $u$ (nhận $1.00$ thay vì $H_u = 8.017429$). Vậy phần giá trị mất đi tại $t = 0$ đơn giản là:
  $$\text{Value Lost} = \frac{p}{R}(H_u - 1.00) = \frac{22/45}{1.02}(8.017429 - 1.00) = \mathbf{\text{USD } 3.363474 \approx \text{USD } 3.36}!$$

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Nhìn lướt tưởng $S_u = 75$ là OTM ở câu a):** Vì $S_0 = 60$ tăng $25\%$ lên $S_u = 75$, rất nhiều bạn theo thói quen tưởng nhánh Tăng thì Put phải OTM ($=0$) nên cho Epsilon giữ tiếp ở nút $u$! Nhìn kỹ strike **$K = 76 > 75$**: tại $S_u = 75$, Put vẫn đang **ITM USD 1.00**, nên theo chữ nghĩa đề bài Epsilon thực hiện ngay tại nút $u$!

---

## Question 39 (Hard) — Phòng Hộ Động Tự Tài Trợ Qua Hai Bước Cây Nhị Phân (Dynamic Delta Hedging)
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Zeta writes one European call on one share for its arbitrage-free price. The stock costs USD 80, the strike is USD 82, and expiration is in one year. In each of two six-month periods, the stock rises by 20% or falls by 10%. The risk-free rate is 6% nominal annually, compounded semiannually.
>
> a. Calculate the call price and the stock and cash holdings Zeta needs initially to hedge the short call. The option premium is available to fund the hedge.
>
> b. At each six-month node, calculate the revised stock and cash holdings. Show how the stock trade is financed without adding or withdrawing external cash.
>
> c. Verify that the rebalanced hedge covers the call payoff along every path. Show numerically why leaving the initial stock and cash holdings unchanged would fail.

**Tóm tắt thông số:**
- Zeta **bán (writes) 1 quyền chọn mua châu Âu** trên 1 cổ phiếu: $S_0 = \text{USD } 80$, $K = \text{USD } 82$, kỳ hạn $T = 1$ năm gồm **2 bước 6 tháng**.
- Mỗi bước 6 tháng: $u = 1.20$, $d = 0.90$.
- Lãi suất $6\%$ danh nghĩa năm, ghép lãi bán niên (*compounded semiannually*) $\implies$ Lãi suất mỗi bước 6 tháng là $6\% / 2 = 3\%$, tức **$R = 1.03$**!

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Giá quyền chọn mua ($C_0$) & Danh mục Phòng hộ Ban đầu tại $t = 0$**
1. **Xác suất trung hòa rủi ro mỗi bước 6 tháng:**
   $$p = \frac{1.03 - 0.90}{1.20 - 0.90} = \frac{0.13}{0.30} = \frac{13}{30} \approx \mathbf{0.433333}, \qquad 1 - p = \frac{17}{30} \approx \mathbf{0.566667}$$
2. **Cây giá cổ phiếu & Giá trị Call tại các nút:**
   - $t = 0.5$ (6 tháng): $S_u = 80(1.20) = \text{USD } 96.00$; $S_d = 80(0.90) = \text{USD } 72.00$.
   - $t = 1.0$ (1 năm, đáo hạn):
     - $S_{uu} = 96(1.20) = 115.20 \implies C_{uu} = \max(115.20 - 82, 0) = \mathbf{\text{USD } 33.20}$.
     - $S_{ud} = S_{du} = 96(0.90) = 86.40 \implies C_{ud} = C_{du} = \max(86.40 - 82, 0) = \mathbf{\text{USD } 4.40}$.
     - $S_{dd} = 72(0.90) = 64.80 \implies C_{dd} = \max(64.80 - 82, 0) = \mathbf{\text{USD } 0.00}$.
   - Quy nạp lùi về $t = 0.5$:
     $$C_u = \frac{\frac{13}{30}(33.20) + \frac{17}{30}(4.40)}{1.03} = \frac{431.60 + 74.80}{30.90} = \frac{506.40}{30.90} = \mathbf{\text{USD } 16.388350 \approx \text{USD } 16.39}$$
     $$C_d = \frac{\frac{13}{30}(4.40) + \frac{17}{30}(0.00)}{1.03} = \frac{57.20}{30.90} = \mathbf{\text{USD } 1.851133 \approx \text{USD } 1.85}$$
   - **Giá quyền chọn mua hợp lý tại $t = 0$ ($C_0$):**
     $$C_0 = \frac{\frac{13}{30}(16.388350) + \frac{17}{30}(1.851133)}{1.03} = \frac{13(506.40) + 17(57.20)}{30 \times 30.90 \times 1.03} = \frac{7,555.60}{954.81} = \mathbf{\text{USD } 7.913197 \approx \text{USD } 7.91}$$
3. **Danh mục phòng hộ ban đầu tại $t = 0$ cho vị thế Short Call (dùng phí $C_0$ thu được để tài trợ):**
   - Để trung hòa nghĩa vụ Short Call, Zeta cần nắm một danh mục mô phỏng đúng 1 Long Call:
   - **Lượng cổ phiếu mua ban đầu ($\Delta_0$):**
     $$\Delta_0 = \frac{C_u - C_d}{S_u - S_d} = \frac{16.388350 - 1.851133}{96.00 - 72.00} = \frac{14.537217}{24.00} = \mathbf{0.605717\text{ shares} \approx 0.61\text{ shares}}$$
     Chi phí mua số cổ phiếu này là $0.605717 \times 80.00 = \text{USD } 48.457389 \approx \text{USD } 48.46$.
   - **Vị thế tiền mặt ban đầu ($B_0$):** Lấy phí quyền chọn thu được $\text{USD } 7.913197$ trừ đi tiền mua cổ phiếu:
     $$B_0 = C_0 - \Delta_0 S_0 = 7.913197 - 48.457389 = \mathbf{-\text{USD } 40.544192 \approx -\text{USD } 40.54} \quad (\text{Đi vay USD } 40.54)$$
   *(Kiểm tra dòng tiền ngoài tại $t = 0$: Thu phí $+7.913197$ + Vay $+40.544192$ $-$ Mua cổ phiếu $48.457389 = \mathbf{\text{USD } 0.00}$!).*

#### **b. Tái cân bằng Danh mục tại Mỗi Nút 6 Tháng ($t = 0.5$) & Chứng minh Tự Tài Trợ 100%**
Sau 6 tháng đầu tiên, khoản nợ gốc ban đầu tích lũy gốc + lãi $3\%$ thành:
$$B_0 \times 1.03 = -40.544192 \times 1.03 = \mathbf{-\text{USD } 41.760518} \quad (\approx -\text{USD } 41.76)$$

1. **Tại Nút Tăng 6 tháng ($S_u = \text{USD } 96.00$):**
   - Giá trị danh mục phòng hộ ngay trước khi tái cân bằng:
     $$V_{\text{pre}, u} = \Delta_0(96.00) + B_0(1.03) = 0.605717(96.00) - 41.760518 = 58.148867 - 41.760518 = \mathbf{\text{USD } 16.388350} = C_u!$$
   - **Vị thế cổ phiếu mới ($\Delta_u$):**
     $$\Delta_u = \frac{C_{uu} - C_{ud}}{S_{uu} - S_{ud}} = \frac{33.20 - 4.40}{115.20 - 86.40} = \frac{28.80}{28.80} = \mathbf{1.000000\text{ share}} \quad (\text{nắm trọn 1.00 cổ phiếu!})$$
   - **Vị thế tiền mặt mới ($B_u$):**
     $$B_u = C_u - \Delta_u S_u = 16.388350 - 1.00(96.00) = \mathbf{-\text{USD } 79.611650 \approx -\text{USD } 79.61} \quad (\text{chú ý } 79.611650 = 82 / 1.03!)$$
   - **Cơ chế tài trợ không cần tiền bên ngoài (*Self-financing mechanics*):** Zeta cần **mua thêm $1.000000 - 0.605717 = 0.394283$ cổ phiếu** tại giá USD 96.00, tốn chi phí $0.394283 \times 96.00 = \mathbf{\text{USD } 37.851133}$ ($\approx \text{USD } 37.85$). Khoản mua thêm này được tài trợ $100\%$ bằng cách **vay thêm đúng USD 37.851133**, nâng tổng dư nợ vay từ $\text{USD } 41.760518$ lên $41.760518 + 37.851133 = \mathbf{\text{USD } 79.611650}$ ($\approx \text{USD } 79.61$) $\implies$ **Dòng tiền bên ngoài = USD 0.00!**

2. **Tại Nút Giảm 6 tháng ($S_d = \text{USD } 72.00$):**
   - Giá trị danh mục phòng hộ ngay trước khi tái cân bằng:
     $$V_{\text{pre}, d} = \Delta_0(72.00) + B_0(1.03) = 0.605717(72.00) - 41.760518 = 43.611650 - 41.760518 = \mathbf{\text{USD } 1.851133} = C_d!$$
   - **Vị thế cổ phiếu mới ($\Delta_d$):**
     $$\Delta_d = \frac{C_{ud} - C_{dd}}{S_{ud} - S_{dd}} = \frac{4.40 - 0.00}{86.40 - 64.80} = \frac{4.40}{21.60} = \frac{11}{54} = \mathbf{0.203704\text{ shares} \approx 0.20\text{ shares}}$$
   - **Vị thế tiền mặt mới ($B_d$):**
     $$B_d = C_d - \Delta_d S_d = 1.851133 - \frac{11}{54}(72.00) = 1.851133 - 14.666667 = \mathbf{-\text{USD } 12.815534 \approx -\text{USD } 12.82}$$
   - **Cơ chế tài trợ không cần tiền bên ngoài (*Self-financing mechanics*):** Zeta **bán bớt $0.605717 - 0.203704 = 0.402014$ cổ phiếu** tại giá USD 72.00, thu về $0.402014 \times 72.00 = \mathbf{\text{USD } 28.944984}$ ($\approx \text{USD } 28.94$), và dùng toàn bộ số tiền này **trả bớt nợ vay**, kéo dư nợ từ $\text{USD } 41.760518$ xuống còn $41.760518 - 28.944984 = \mathbf{\text{USD } 12.815534}$ ($\approx \text{USD } 12.82$) $\implies$ **Dòng tiền bên ngoài = USD 0.00!**

#### **c. Kiểm chứng Danh mục Đã Tái Cân Bằng trên Mọi Đường Đi & Chứng minh Danh mục Tĩnh Thất Bại**
1. **Danh mục ĐÃ tái cân bằng tại $T = 1.0$ (khớp hoàn hảo trên cả 4 đường đi!):**
   - **Đường đi $u \to u$ ($S_{uu} = 115.20$):** $\Delta_u(115.20) + B_u(1.03) = 1.00(115.20) - 79.611650(1.03) = 115.20 - 82.00 = \mathbf{\text{USD } 33.20} = C_{uu}$!
   - **Đường đi $u \to d$ ($S_{ud} = 86.40$):** $\Delta_u(86.40) + B_u(1.03) = 1.00(86.40) - 79.611650(1.03) = 86.40 - 82.00 = \mathbf{\text{USD } 4.40} = C_{ud}$!
   - **Đường đi $d \to u$ ($S_{du} = 86.40$):** $\Delta_d(86.40) + B_d(1.03) = \frac{11}{54}(86.40) - 12.815534(1.03) = 17.60 - 13.20 = \mathbf{\text{USD } 4.40} = C_{du}$!
   - **Đường đi $d \to d$ ($S_{dd} = 64.80$):** $\Delta_d(64.80) + B_d(1.03) = \frac{11}{54}(64.80) - 12.815534(1.03) = 13.20 - 13.20 = \mathbf{\text{USD } 0.00} = C_{dd}$!
2. **Nếu giữ nguyên không đổi danh mục ban đầu ($\Delta_0 = 0.605717$ cp và nợ gốc tích lũy sau 2 kỳ thành $B_0 \times 1.03^2 = -40.544192 \times 1.0609 = -\text{USD } 43.013333$):**
   - **Tại $uu$ ($115.20$):** Giá trị danh mục tĩnh $= 0.605717(115.20) - 43.013333 = \mathbf{\text{USD } 26.77}$ ($26.765307$), trong khi nghĩa vụ trả Call là **USD 33.20** $\implies$ **Thất bại nặng: Thiếu hụt $-\text{USD } 6.43$** ($-6.434693$)!
   - **Tại $ud / du$ ($86.40$):** Giá trị danh mục tĩnh $= 0.605717(86.40) - 43.013333 = \mathbf{\text{USD } 9.32}$ ($9.320647$) so với nghĩa vụ **USD 4.40** $\implies$ Lệch dư $+\text{USD } 4.92$!
   - **Tại $dd$ ($64.80$):** Giá trị danh mục tĩnh $= 0.605717(64.80) - 43.013333 = \mathbf{-\text{USD } 3.76}$ ($-3.762848$) so với nghĩa vụ **USD 0.00** $\implies$ **Thất bại: Thâm hụt âm $-\text{USD } 3.76$**!
   - *Nguyên lý:* Một danh mục tĩnh mua và giữ chỉ tạo ra hàm bậc nhất $a S_T + b$, không bao giờ đi qua được 3 điểm payoff gãy khúc phi tuyến $(64.80, 0), (86.40, 4.40), (115.20, 33.20)$! Việc tái cân bằng động (*buy high at $u$, sell low at $d$*) chính là chìa khóa tạo ra độ lồi của payoff quyền chọn!

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Mẹo kiểm tra tự động chống sai 100% ở mọi bài Dynamic Replication (như Q39):**
  Tại mỗi nút trung gian trước khi tái cân bằng, **bắt buộc phải có $\Delta_0 S_u + B_0 R \equiv C_u$ và $\Delta_0 S_d + B_0 R \equiv C_d$ chính xác đến chữ số cuối cùng**! Nếu bấm ra lệch nhau nghĩa là $\Delta_0, B_0$ hoặc $C_u, C_d$ có lỗi tính toán — dừng lại sửa ngay trước khi làm sang câu b, c!
- Và chú ý tại nút $u$ ($S_u = 96$): cả $S_{uu} = 115.20$ lẫn $S_{ud} = 86.40$ đều $> K = 82$, nên chắc chắn $\Delta_u = 1.00$ và $B_u = -K / R = -82 / 1.03 = -79.611650$ ngay lập tức không cần bấm công thức!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Quên nhân lãi $1.03$ cho khoản nợ $B_0$ khi sang tháng thứ 6):** Sau 6 tháng, khoản vay $-40.54$ đã nở thành **$-41.76$**! Nếu lấy $-40.54$ để tính số tiền vay thêm/trả bớt ở câu b sẽ lệch mất USD 1.22 tiền lãi!
- **Bẫy 2 (Đảo ngược hướng phòng hộ của người BÁN Call):** Zeta **writes (bán)** Call nên đang mang nghĩa vụ âm Call ($-C$). Để **phòng hộ (hedge)** nghĩa vụ đó, tài sản phòng hộ Zeta nắm giữ phải mô phỏng **+1 Long Call** (**Mua $\Delta > 0$ cổ phiếu và Đi vay tiền**), KHÔNG phải bán khống cổ phiếu!

---

## Question 40 (Hard) — Đòn Bẩy Quyền Chọn Bán, Hệ Số Beta Danh Mục Có Ràng Buộc & CAPM Tức Thời
🔥 **[TRỌNG TÂM CỐT TỬ TỰ LUẬN TÍNH TOÁN (40% DERIVATIVES) + MCQ — PHẢI LÀM THÀNH THỤC 100%]**

### 1. Đề bài gốc & Tóm tắt thông số (Original Question & Inputs)

> **Original Question:**
> Eta shares trade at USD 100 and have beta 1.25. A European put on one share costs USD 10 and has delta $-0.40$.
>
> Theta has USD 100,000 to allocate among Eta shares, these puts and risk-free cash. Exactly USD 20,000 must remain in cash. All remaining funds must be invested. Short positions and borrowing are prohibited, and the number of puts may not exceed the number of shares held. Fractional shares and options are permitted.
>
> a. Calculate the put's signed leverage and beta.
>
> b. Determine the share and put quantities required for a current portfolio beta of 0.60. Check all constraints.
>
> c. Can Theta achieve a beta of 0.50 under the same requirements? Support the answer numerically.
>
> d. For the portfolio in part b, calculate the instantaneous CAPM expected return. Use an annualized instantaneous risk-free rate of 3% and market expected return of 9%.

**Tóm tắt thông số:**
- Cổ phiếu Eta: $S = \text{USD } 100$, $\beta_S = 1.25$. Quyền chọn bán châu Âu: $P = \text{USD } 10$, $\Delta_P = -0.40$.
- Tổng vốn $W = \text{USD } 100,000$; bắt buộc giữ đúng $\text{Cash} = \text{USD } 20,000$ ($\beta_{\text{cash}} = 0$) $\implies$ Đúng **USD 80,000** phải phân bổ hết vào cổ phiếu ($N_S$ cổ phiếu) và quyền chọn bán ($N_P$ quyền chọn bán):
  $$100 N_S + 10 N_P = 80,000$$
- Các ràng buộc vị thế: Cấm bán khống & cấm vay ($N_S \ge 0,\; N_P \ge 0$); số lượng Put không được vượt quá số lượng cổ phiếu nắm giữ (**$N_P \le N_S$**).

### 2. Hướng dẫn Giải Chi Tiết Từng Bước (Detailed Step-by-Step Solution)

#### **a. Đòn bẩy có dấu (Signed Leverage / Elasticity $\Omega_P$) và Beta của Put ($\beta_P$)**
1. **Đòn bẩy có dấu (độ co giãn giá quyền chọn theo giá cổ phiếu, $\Omega_P$):**
   $$\Omega_P = \Delta_P \cdot \frac{S}{P} = (-0.40) \times \frac{100}{10} = \mathbf{-4.00}$$
   *(Ý nghĩa: Khi cổ phiếu tăng tức thời $+1\%$, giá quyền chọn bán giảm $-4\%$!).*
2. **Hệ số Beta tức thời của quyền chọn bán ($\beta_P$):**
   $$\beta_P = \Omega_P \cdot \beta_S = (-4.00) \times 1.25 = \mathbf{-5.00}$$

#### **b. Số lượng Cổ phiếu ($N_S$) và Put ($N_P$) để đạt $\beta_{\text{port}} = 0.60$ & Kiểm tra mọi ràng buộc**
- Tỷ trọng vốn trong tổng danh mục USD 100,000 là: $w_S = \frac{100 N_S}{100,000}$, $w_P = \frac{10 N_P}{100,000}$, $w_{\text{cash}} = \frac{20,000}{100,000} = 0.20$.
- Phương trình Beta danh mục bằng $0.60$:
  $$\beta_{\text{port}} = w_S \beta_S + w_P \beta_P + w_{\text{cash}}(0) = \frac{100 N_S (1.25) + 10 N_P (-5.00)}{100,000} = 0.60$$
  $$\implies 125 N_S - 50 N_P = 60,000$$
- Kết hợp với phương trình ngân sách $100 N_S + 10 N_P = 80,000 \iff 50 N_P = 400,000 - 500 N_S$:
  $$125 N_S - (400,000 - 500 N_S) = 60,000 \implies 625 N_S = 460,000 \implies N_S = \frac{460,000}{625} = \mathbf{736.00\text{ shares}}$$
  $$10 N_P = 80,000 - 100(736) = 80,000 - 73,600 = 6,400 \implies N_P = \mathbf{640.00\text{ puts}}$$
- **Kiểm tra đầy đủ tất cả các ràng buộc (*Check all constraints*):**
  1. Tiền mặt giữ lại: Đúng **USD 20,000.00** (thỏa mãn).
  2. Toàn bộ vốn còn lại được giải ngân hết, không đi vay: $736(100) + 640(10) = 73,600 + 6,400 = \text{USD } 80,000.00$; cộng tiền mặt $= \text{USD } 100,000.00$ (thỏa mãn).
  3. Không bán khống: $N_S = 736 \ge 0$ và $N_P = 640 \ge 0$ (thỏa mãn).
  4. Trần số lượng Put không vượt số cổ phiếu: $N_P = 640 \le N_S = 736$ (thỏa mãn!).
  5. Kiểm lại Beta: $0.736(1.25) + 0.064(-5.00) + 0.20(0) = 0.920 - 0.320 = \mathbf{0.60}$ (chính xác!).

#### **c. Theta có thể đạt mức $\beta_{\text{port}} = 0.50$ dưới cùng các ràng buộc không?**
- **Trả lời: KHÔNG THỂ (NO)!** Chứng minh số học chặt chẽ bằng cả 2 cách:
  - **Cách 1 (Tìm mức Beta tối thiểu khả thi):** Vì Put mang Beta âm ($-5.00$) và cổ phiếu mang Beta dương ($+1.25$), để kéo Beta danh mục xuống thấp nhất có thể trong giới hạn $100 N_S + 10 N_P = 80,000$ và $N_P \le N_S$, ta phải mua tối đa số lượng Put cho phép, tức đẩy chạm biên **$N_P = N_S$**:
    $$100 N_S + 10 N_S = 80,000 \implies 110 N_S = 80,000 \implies N_S = N_P = \frac{8,000}{11} \approx 727.27\text{ đơn vị}$$
    Khi đó mức Beta danh mục nhỏ nhất có thể đạt được là:
    $$\beta_{\min} = \frac{125(8,000/11) - 50(8,000/11)}{100,000} = \frac{75 \times 8,000}{1,100,000} = \frac{6}{11} = \mathbf{0.545455 \approx 0.55 > 0.50!}$$
    Vì sàn Beta khả thi thấp nhất là **$0.55$** ($6/11$), mục tiêu $\beta_{\text{port}} = 0.50$ là **bất khả thi**!
  - **Cách 2 (Giải trực tiếp hệ phương trình tại $\beta_{\text{port}} = 0.50$ chỉ ra vi phạm):**
    $$125 N_S - 50 N_P = 50,000 \implies 625 N_S = 450,000 \implies N_S = \mathbf{720\text{ shares}}, \quad N_P = \frac{80,000 - 72,000}{10} = \mathbf{800\text{ puts}}$$
    Nghiệm duy nhất này đòi hỏi $N_P = 800 > N_S = 720$, **vi phạm trực tiếp ràng buộc $N_P \le N_S$**!

#### **d. Tỷ suất sinh lời kỳ vọng CAPM tức thời của danh mục ở câu b**
Với $r_f = 3.00\%$, $E[R_M] = 9.00\%$ (phần bù rủi ro thị trường $E[R_M] - r_f = 6.00\%$) và $\beta_{\text{port}} = 0.60$:
$$E[R_{\text{port}}] = r_f + \beta_{\text{port}} \left(E[R_M] - r_f\right) = 3.00\% + 0.60 \times (9.00\% - 3.00\%) = 3.00\% + 3.60\% = \mathbf{6.60\%}$$
*(Kiểm tra chéo thú vị từ tỷ suất sinh lời kỳ vọng tức thời của từng tài sản thành phần:*
- *Cổ phiếu: $\mu_S = 3\% + 1.25(6\%) = 10.50\%$.*
- *Put bảo hiểm: $\mu_P = 3\% + (-5.00)(6\%) = -27.00\%$ — lợi suất kỳ vọng ÂM rất sâu vì Put là tài sản bảo hiểm chống sụp đổ thị trường!*
- *Tiền mặt: $\mu_{\text{cash}} = 3.00\%$.*
- *Tổng hợp danh mục: $0.736(10.50\%) + 0.064(-27.00\%) + 0.200(3.00\%) = 7.728\% - 1.728\% + 0.600\% = \mathbf{6.60\%}$ — khớp tuyệt đối!).*

### 3. ⚡ Phác Đồ Giải Nhanh & Tối Ưu Trong Phòng Thi (Fast Exam Method & Shortcuts)
- **Mẹo "Beta trên mỗi đơn vị vật chất" biến hệ phương trình câu b & c thành phép tính nhẩm 5 giây!**
  - Nhìn vào tử số của $\beta_{\text{port}} = \frac{\sum \text{Dollar}_i \beta_i}{W}$:
  - Mỗi 1 cổ phiếu đóng góp *Dollar-Beta* là $S \cdot \beta_S = 100 \times 1.25 = \mathbf{+125}$.
  - Mỗi 1 quyền chọn dùng đẳng thức siêu thần tốc: **$P \cdot \beta_P = P \cdot (\Delta_P \frac{S}{P}) \beta_S \equiv \Delta_P \cdot (S \beta_S) = -0.40 \times 125 = \mathbf{-50}$**! (Thậm chí chẳng cần qua trung gian $P$ ở bước này — mỗi 1 Put tương đương $-0.40$ cổ phiếu về mặt rủi ro tức thời!).
  - Do đó tổng số cổ phiếu tương đương (*effective delta-adjusted shares*) của danh mục là $N_S - 0.40 N_P$! Khi ghép 1 cổ phiếu + 1 Put ($N_P = N_S$), cặp Protective Put đó tốn USD 110 và mang độ nhạy chỉ còn $1 - 0.40 = 0.60$ cổ phiếu (Dollar-Beta $= 0.60 \times 125 = +75$)!

### 4. ⚠️ Bẫy Sai Lầm Chết Người Cần Tránh (Common Exam Pitfalls)
- **Bẫy 1 (Chia cho USD 80,000 thay vì tổng tài sản USD 100,000 khi tính Beta danh mục):** USD 20,000 tiền mặt ($\beta = 0$) vẫn nằm trong danh mục USD 100,000 của Theta! Nếu chia cho 80,000 thay vì 100,000 sẽ làm sai toàn bộ $N_S, N_P$ ở câu b và câu c!
- **Bẫy 2 (Bỏ quên dấu âm của $\Delta_P = -0.40$ hoặc lấy trị tuyệt đối khi tính $\Omega_P$ và $\beta_P$):** Quyền chọn bán tăng giá khi thị trường sập nên bắt buộc có **đòn bẩy âm ($-4.00$)** và **Beta âm ($-5.00$)**!

---

# 🏆 BẢNG TỔNG KẾT CÔNG THỨC & BẪY CHẾT NGƯỜI TOÀN TẬP (L08 – L11 MASTER CHEAT-SHEET)

| Chuyên Đề | Công Thức Cốt Tử Cần Nhớ Thuộc Lòng | Bẫy Hiểm Của GS. Bora Cayirli Cần Cảnh Giác |
|---|---|---|
| **FF3 & Limits to Arbitrage (L08)** | $R_B = r_f + \beta_M(R_M - r_f) + \beta_S SMB + \beta_H HML$; $\alpha_{\text{net}} = R_{\text{gross}} - R_B - f - c$ | Đề cho sẵn *Market excess return* $\rightarrow$ cấm trừ $r_f$ lần nữa! Độ lệch khỏi giá lý thuyết $<$ phí vay cổ phiếu $\rightarrow$ nằm trong *No-Arbitrage Band* (Q5). |
| **Behavioural Finance (L08)** | *Prospect Theory*: Lõm vùng lãi (ngại rủi ro), Lồi vùng lỗ (ưa rủi ro), Gãy tại $0$ (ghét lỗ) | Bán lời / gồng lỗ ở 2 mức giá vốn chứng minh *Reference Dependence + Diminishing Sensitivity (Disposition Effect)* chứ chưa tự chứng minh *Loss Aversion* (Q4a)! |
| **Forwards & Futures (L09)** | $F_0 = [S_0 - PV(D)](1+r)^T$ hoặc $S_0 e^{(r - q - y)T}$; $V_t^{\text{long}} = S_t - PV_t(K)$ | Trong bảng Margin: **"strictly below maintenance"** nghĩa là chạm đúng Maintenance KHÔNG nộp thêm tiền (Q7)! Nhà sản xuất bán hàng cần **Short Forward** nếu không chịu nổi daily margin call khi giá tăng (Q11)! |
| **Swaps & CIP (L09)** | IRS Net $= N(L - K)\Delta t$; CIP: $F_{\text{USD/EUR}} = S_0 \left(\frac{1+r_{\text{USD}}}{1+r_{\text{EUR}}}\right)^T$ | *Currency Swap* bắt buộc trao đổi vốn gốc ở $t=0$ và $t=T$ (Q12). Trong CIP Arbitrage, phải bán kỳ hạn **cả gốc lẫn lãi ngoại tệ** $N_{\text{EUR}}(1+r_{\text{EUR}})^T$, và kiểm tra kỹ chiều vay vs chiều bán kỳ hạn (Q14)! |
| **Parity & Bounds (L10)** | $C + PV(K) = S_0 + P$; $C - P = PV(F - K)$; $C_{\text{Eur}} \ge \max(0, S_0 - PV(K))$ | European Put deep-ITM có thể $< K - S_0$ (vì cận dưới chỉ là $PV(K) - S_0$, Q34). Cấm lắp $P_{\text{Amer}}$ vào đẳng thức Parity châu Âu (Q38c)! Ex-div American Call cần $D > [K - PV(K)] + P_{\text{ex}}$ (Q22)! |
| **Binomial & Hedging (L11)** | $p = \frac{S \cdot R - S_d}{S_u - S_d}$; $\Delta = \frac{V_u - V_d}{S_u - S_d}$; $B = V_{\text{node}} - \Delta S$ | Cây **cộng đô-la** (*additive tree*, Q33) phải tính lại $p$ ở từng nút! Mỗi bước lùi trên cây chỉ chiết khấu **1 bước $R$** (Q32b)! Tái cân bằng tự tài trợ: nhớ tính lãi trên nợ cũ $B_0 R$ trước khi cộng/trừ tiền mua bán cổ phiếu (Q39)! |
| **Option Beta & CAPM (L11)** | $\Omega = \Delta \frac{S}{V}$; $\beta_{\text{opt}} = \Omega \beta_S$; $E[R_p] = r_f + \beta_p(E[R_M] - r_f)$ | Chia tổng Dollar-Beta cho **toàn bộ danh mục $W$** (kể cả phần Cash giữ lại có $\beta = 0$), và kiểm tra kỹ ràng buộc $N_P \le N_S$ (Q40)! |
