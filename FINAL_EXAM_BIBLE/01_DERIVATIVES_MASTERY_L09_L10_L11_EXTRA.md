# BFIN INVESTMENTS (WS2026) — FINAL EXAM STUDY BIBLE
## VOLUME 01: DERIVATIVES MASTERY (LECTURES 09, 10, 11 & EXTRA SESSION)

**Giảng viên phụ trách:** Dr. Omer Cayirli (*Finance 2 - BFIN, Fall/WS 2026*)  
**Ngày thi chính thức:** 12/11/2026 (Thời gian làm bài: 75 phút)  
**Phạm vi tài liệu tích hợp:** Toàn bộ Slides Lý thuyết & Bài tập tại lớp (Lectures 09, 10, 11), Buổi phụ đạo chuyên sâu (Extra Session), và Bộ câu hỏi Thực hành chuẩn (Practice Questions L08–L11).

---

## MỤC LỤC ĐỊNH HƯỚNG NHANH

1. [Tổng quan Tư duy Phái sinh & Ma trận Phân loại Trọng tâm Thi](#phần-mở-đầu--tổng-quan-tư-duy-phái-sinh--ma-trận-phân-loại-trọng-tâm-thi)
2. [Chương 1 — Lecture 09: Forwards, Futures, Swaps & CDS (Trọng tâm Tính toán #1)](#chương-1--lecture-09-forwards-futures-swaps--cds-trọng-tâm-tính-toán-1)
3. [Chương 2 — Lecture 10: Thị trường Quyền chọn, Chiến lược, Put-Call Parity, Bounds & Mô hình Merton (Trọng tâm Tính toán #2)](#chương-2--lecture-10-thị-trường-quyền-chọn-chiến-lược-put-call-parity-bounds--mô-hình-merton-trọng-tâm-tính-toán-2)
4. [Chương 3 — Lecture 11 & Extra Session: Cây Nhị thức Châu Âu (Trọng tâm Tính toán #3), Đòn bẩy/Beta Quyền chọn & Lý thuyết BSM/American cho MCQ](#chương-3--lecture-11--extra-session-cây-nhị-thức-châu-âu-trọng-tâm-tính-toán-3-đòn-bẩybeta-quyền-chọn--lý-thuyết-bsmamerican-cho-mcq)
5. [Phần Cuối — Bộ 6 Phác đồ "Nhìn Đề Biết Cách Giải Trong 10 Giây" Cho Bài Tự luận 3 Ý (`a, b, c`)](#phần-cuối--bộ-6-phác-đồ-nhìn-đề-biết-cách-giải-trong-10-giây-cho-bài-tự-luận-derivatives-3-ý-a-b-c)

---

# PHẦN MỞ ĐẦU — TỔNG QUAN TƯ DUY PHÁI SINH & MA TRẬN PHÂN LOẠI TRỌNG TÂM THI

## 1. Giải phẫu Cấu trúc Đề thi Cuối kỳ (Final Exam Blueprint)

Trong 75 phút phòng thi, đề thi BFIN Investments được chia thành hai mặt trận rõ rệt với chiến thuật phân bổ thời gian hoàn toàn khác nhau:

- **Phần I — 10 Câu Trắc nghiệm (10 MCQs):** Kết hợp cả **tính toán nhanh (mini-calculations)** lẫn **lý thuyết khái niệm – bẫy tư duy (conceptual traps)**. Phạm vi quét **100% tài liệu môn học**: toàn bộ slides bài giảng, cả hai bộ Practice Questions, và toàn bộ nội dung buổi **Extra Session**.
- **Phần II — 5 Bài toán Tự luận Tính toán × 3 ý nhỏ (`a, b, c`) = 15 ý nhỏ:**
  - Riêng mảng **Chứng khoán Phái sinh (Derivatives — Lectures 09, 10, 11)** chiếm **tối đa lên tới 40% số lượng bài toán tự luận** (tương đương **~2 bài toán lớn trọn vẹn = 6 trên 15 ý nhỏ** của cả đề thi!).
  - **Giới hạn phạm vi tính toán cực kỳ quan trọng:** Sẽ **KHÔNG CÓ bài toán tự luận tính toán** yêu cầu bấm công thức **Black-Scholes-Merton (BSM)** hay giải cây **Quyền chọn kiểu Mỹ (American Options)**.
  - **Tuy nhiên (cảnh giác tối đa):** Cả mô hình **Black-Scholes** lẫn **American Options** đều hoàn toàn **CÓ THỂ xuất hiện trong 10 câu MCQ** dưới dạng câu hỏi bản chất kinh tế, ý nghĩa tham số ($N(d_1), N(d_2), \Delta, \Omega, \beta_{\text{opt}}$, Implied Volatility, VIX), hoặc điều kiện thực thi sớm (Early Exercise)!

> [!IMPORTANT]
> **Nguyên tắc làm tròn chuẩn của Dr. Omer Cayirli (áp dụng cho mọi bài tự luận):** Luôn **giữ nguyên số lẻ đầy đủ (unrounded values)** trong tất cả các bước tính trung gian (lưu vào biến nhớ máy tính bỏ túi `A, B, C, D, E, F`), và chỉ làm tròn tới **2 chữ số thập phân** đối với số tiền (USD) hoặc phần trăm (%) ở đáp số báo cáo cuối cùng! Làm tròn sớm $p$, $d_1$, hoặc hệ số chiết khấu ở bước giữa có thể gây sai số dây chuyền sang ý `b` và `c`.

---

## 2. Sợi chỉ Đỏ Xuyên suốt Mọi Công thức Phái sinh: Quy luật Một Giá & Sao chép Không Arbitrage

Nếu ở Học thuyết Danh mục & CAPM (Lectures 05–06), giá tài sản được xác lập từ **cân bằng cung – cầu và khẩu vị ngại rủi ro ($A$)** của nhà đầu tư, thì sang thế giới **Phái sinh (Derivatives)**, tư duy định giá xoay trục 180 độ sang **Định giá Tương đối bằng Không Kinh doanh Chênh lệch Giá (No-Arbitrage / Replication Pricing)**:

1. **Bản chất của Công cụ Phái sinh (Contingent Claims):** Giá trị của hợp đồng phái sinh không tự sinh ra mà phụ thuộc hoàn toàn vào giá của một **tài sản cơ sở (Underlying Asset)** như cổ phiếu, chỉ số, trái phiếu, ngoại tệ, hàng hóa hoặc sự kiện tín dụng.
2. **Nguyên lý Sao chép (Replication Principle):** Nếu ta ghép được một **Danh mục Sao chép (Replicating Portfolio)** gồm tài sản cơ sở ($S$) và vay/cho vay phi rủi ro ($B$) sao cho tại ngày đáo hạn $T$, dòng tiền thu về của danh mục này **bằng hệt dòng tiền của công cụ phái sinh trong MỌI kịch bản thị trường có thể xảy ra**, thì theo **Quy luật Một Giá (Law of One Price)**, chi phí thiết lập danh mục sao chép hôm nay bắt buộc phải bằng giá hợp lý của công cụ phái sinh hôm nay!
3. **Hệ quả "Phép màu" Trung lập Rủi ro:** Vì danh mục sao chép đã khử sạch mọi rủi ro biến động giá, giá hợp lý của Forward, Swap hay Option **KHÔNG HỀ PHỤ THUỘC** vào việc nhà đầu tư thích hay ghét rủi ro, cũng **KHÔNG PHỤ THUỘC** vào xác suất tăng giá thực tế ngoài đời của cổ phiếu! Nếu giá thị trường lệch khỏi chi phí sao chép, quy tắc kiếm lời phi rủi ro bất biến luôn là:
   $$\text{Chiến lược Arbitrage} = \textbf{MUA cái RẺ (Underpriced)} + \textbf{BÁN cái ĐẮT (Overpriced)}$$

---

## 3. Bảng Ma trận Phân loại Trọng tâm Thi: Tự luận Tính toán vs. Trắc nghiệm MCQ

| Chuyên đề Kiến thức | Nguồn Bài giảng | Tự luận Tính toán (40% điểm bài toán) | Trắc nghiệm MCQ (10 câu) | Kỹ năng Trọng tâm Cần Đạt Tới Mức Phản Xạ |
| :--- | :---: | :---: | :---: | :--- |
| **Định giá Forward & Futures (6 dạng tài sản cơ sở)** | L09 + Practice | **CÓ (Trọng tâm cao)** | **CÓ** | Thuộc lòng Cost-of-Carry cho cổ phiếu, cổ tức rời rạc $I$, chỉ số $q$ đổi theo kỳ, ngoại tệ CIP, hàng hóa ($U, y$), trái phiếu; suy ngược lãi suất/lợi suất ngụ ý. |
| **Định giá lại Forward đang nắm giữ tại $t$ & Bảng Arbitrage** | L09 + Practice | **CÓ (Trọng tâm cao)** | **CÓ** | Tính $V_t = PV_{t,\text{new}}(F_t - K)$; lập bảng dòng tiền tự tài trợ ($CF_0=0$), đặc biệt tránh bẫy lệch gốc-lãi ngoại tệ (bài Tau). |
| **Cơ chế Ký quỹ Futures (Marking-to-Market Ledger)** | L09 + Practice | **CÓ (Trọng tâm cao)** | **CÓ** | Lập sổ cái P&L hàng ngày, tìm giá ẩn, bắt chuẩn câu chữ `strictly below` vs `at or below`, đối chiếu tổng lợi nhuận và rủi ro thanh khoản (bài Omicron). |
| **Hoán đổi Lãi suất (IRS) & Hoán đổi Tiền tệ (Currency Swap)** | L09 + Practice | **CÓ (Trọng tâm cao)** | **CÓ** | Tính dòng tiền quý ($\Delta=0.25$), ghép khoản vay + swap, định lượng **Basis Risk ($M \ne L$)** và phần lãi ngoại tệ hở tỷ giá khi lãi vay $\ne$ lãi swap. |
| **Credit Default Swaps (CDS & Sovereign CDS)** | L09 | Không (hoặc ý phụ rất ngắn) | **CÓ** | Hiểu Physical vs Cash settlement $N(1-\mathcal{R})$, tính phí định kỳ từ bps, phân biệt CDS spread với xác suất vỡ nợ. |
| **Moneyness, Intrinsic Value, Time Value & 10 Chiến lược Quyền chọn** | L10 + Practice | **CÓ (Trọng tâm cao)** | **CÓ** | Giải thích Time Value âm; tính nhanh Cost, Payoff, Max Profit/Loss, Breakeven; dùng kỹ thuật $\Delta\text{Slope}$ dựng Butterfly/Payoff bất kỳ; Collar theo ngân sách. |
| **Put-Call Parity, Synthetic Forward & Option Price Bounds** | L10 + Practice | **CÓ (Trọng tâm cao)** | **CÓ** | Dựng Synthetic Forward chi phí $0$ tìm $K_{\text{imp}}$; kiểm tra Bounds của Call/Put/Spread/Box/Butterfly; lập bảng Arbitrage theo 2 miền $S_T \le K$ và $S_T > K$. |
| **6 Nhân tố Tác động lên Giá Quyền chọn (Comparative Statics)** | L10 + Practice | Ý giải thích ngắn (`c`) | **CÓ (Rất hay hỏi)** | Nắm chắc bảng dấu ($S_0, K, \sigma, r, D, T$), đặc biệt sự khác biệt của $T$ giữa American và European Put/Call có cổ tức. |
| **Mô hình Cấu trúc Merton (Equity = Call, Risky Debt)** | L10 + Extra | **CÓ (Khi cho sẵn giá Call hoặc dùng cây 2 kỳ)** | **CÓ (Asset Substitution)** | Tính $E_0, D_0 = V_0 - E_0$, Promised Yield $y$, Credit Spread, định lý MM khi trả cổ tức đặc biệt, và hiện tượng **Risk Shifting** (bài Kappa). |
| **Cây Nhị thức Châu Âu 1 Kỳ & 2 Kỳ (European Binomial Trees)** | L11 + Extra | **CÓ (Trọng tâm #1 của L11)** | **CÓ** | Thành thục 3 cách giải 1 kỳ ($\Delta, B$; $p$; state prices $q_u, q_d$); phân biệt **Cây Nhân Tính** ($p$ cố định, gồm cả CRR $u=e^{\sigma\sqrt{\Delta t}}$) vs **Cây Cộng Tính** ($p$ đổi ở từng nút!); phòng hộ động tự tài trợ 2 kỳ. |
| **Đòn bẩy ($\Omega$), Beta Quyền chọn ($\beta_{\text{opt}}$) & Volatility ($\sqrt{T}$, IV)** | L11 + Extra | **CÓ (Khi cho sẵn $V, \Delta$ hoặc bảng giá)** | **CÓ** | Công thức $\Omega = S\Delta/V$, $\beta_{\text{opt}} = \Omega\beta_S$, ghép danh mục đạt $\beta_{\text{target}}$ với ràng buộc $N_P \le N_S$; tính sample $\sigma$ (chia $n-1$), quy tắc $\sqrt{250}, \sqrt{52}, \sqrt{12}$ và nội suy tuyến tính IV. |
| **Công thức Black-Scholes-Merton (BSM)** | L11 + Extra | **KHÔNG THI TÍNH TOÁN** | **CÓ (Trọng tâm MCQ)** | Giả định BSM, ý nghĩa kinh tế của $N(d_1) = \Delta_C$, $N(d_2) = \Pr^{\mathbb{Q}}(S_T > K)$, vay tiền $-PV(K)N(d_2)$, lỗi lồi Gamma khi giá nhảy mạnh, VIX, $p$ vs xác suất dự báo thực tế. |
| **Quyền chọn Kiểu Mỹ (American Options & Early Exercise)** | L10 + L11 + Extra | **KHÔNG THI TÍNH TOÁN** | **CÓ (Trọng tâm MCQ)** | Quy tắc thực thi sớm: Call không cổ tức ($C_A = C_E$), Call sát ngày GDKHQ ($D > [K-PV(K)] + P_{\text{ex}}$), Put không cổ tức (deep-ITM nhưng không phải cứ ITM là thực thi!). |

---

# CHƯƠNG 1 — LECTURE 09: FORWARDS, FUTURES, SWAPS & CDS (TRỌNG TÂM TÍNH TOÁN #1)

## 1.1. Bản chất Kinh tế: Hợp đồng Kỳ hạn (Forwards) vs. Hợp đồng Tương lai (Futures)

Cả **Forward** và **Futures** đều là thỏa thuận ấn định từ hôm nay ($t=0$) mức giá giao hàng $F_0$, số lượng $Q$ và thời điểm giao hàng tương lai $T$, trong đó **cả hai bên đều có nghĩa vụ bắt buộc phải thực hiện (Obligation)**:
- **Bên Mua (Long position):** Cam kết **mua** tài sản cơ sở tại ngày $T$ với giá $F_0 \implies \text{Payoff trên 1 đơn vị} = S_T - F_0$ (có lợi khi giá giao ngay $S_T$ tăng).
- **Bên Bán (Short position):** Cam kết **bán/giao** tài sản cơ sở tại ngày $T$ với giá $F_0 \implies \text{Payoff trên 1 đơn vị} = F_0 - S_T$ (có lợi khi giá giao ngay $S_T$ giảm).

Tuy có cùng hàm payoff lúc đáo hạn (và có **cùng mức giá lý thuyết $F_0$ khi lãi suất là tất định — deterministic interest rates**), cấu trúc thị trường của hai hợp đồng này tạo ra hệ quả quản trị rủi ro rất khác nhau:

| Tiêu chí So sánh | Hợp đồng Kỳ hạn (Forward Contract) | Hợp đồng Tương lai (Futures Contract) |
| :--- | :--- | :--- |
| **Nơi giao dịch** | Thị trường phi tập trung (**OTC** — thỏa thuận song phương trực tiếp với ngân hàng/đối tác). | Giao dịch tập trung trên **Sàn giao dịch (Exchange-traded)**. |
| **Điều khoản hợp đồng** | **Tùy chỉnh linh hoạt (Customized)** chính xác theo khối lượng, chủng loại và ngày cần phòng hộ. | **Chuẩn hóa hoàn toàn (Standardized)** về quy mô hợp đồng ($Q$), chất lượng và ngày đáo hạn. |
| **Cơ chế thanh toán** | Thanh toán **một lần duy nhất tại ngày đáo hạn $T$** (thường không bù trừ tiền mặt hàng ngày). | **Đánh giá lại theo thị trường hàng ngày (Daily Marking-to-Market)**: lãi/lỗ được cộng/trừ vào tài khoản ký quỹ cuối mỗi ngày. |
| **Đối tác & Rủi ro tín dụng** | Chịu **rủi ro vỡ nợ đối tác trực tiếp (Counterparty Credit Risk)** (có thể giảm thiểu bằng tài sản thế chấp collateral). | **Trung tâm Thanh toán Bù trừ (Clearinghouse)** đứng giữa làm đối tác trung tâm cho mọi bên mua và bán $\implies$ gần như triệt tiêu rủi ro vỡ nợ song phương. |
| **Rủi ro thanh khoản trung gian** | **Không có** (nếu không kèm điều khoản ký quỹ biến đổi) — dòng tiền chỉ phát sinh tại ngày $T$. | **Rất đáng kể (Interim Liquidity / Funding Risk)**: thua lỗ tạm thời trên sàn đòi hỏi nộp tiền mặt ngay lập tức (**Margin Call**) trước khi dòng tiền kinh doanh vật chất kịp về! |

### Ba Góc nhìn Kinh tế Sâu sắc cho Câu hỏi Lý thuyết & Thảo luận (Từ L09 Question 1 & Practice Q11)

1. **Khám phá Giá (Price Discovery) khi toàn ngành đã phòng hộ 100%:** Ngay cả khi mọi nhà khai thác đồng và nhà sản xuất dây cáp đã chốt giá bán/mua 6 tháng tới bằng hợp đồng Futures, giá giao ngay (Spot price) **vẫn phản ánh cung, cầu cận biên và thông tin mới** (phòng hộ chỉ khóa giá cho lô hàng đã định, không làm các quyết định sản xuất thêm, tồn kho hay mua thêm trở nên vô cảm với giá). Thị trường Futures thường dẫn dắt khám phá giá nếu phản ánh thông tin nhanh hơn, và nghiệp vụ Arbitrage gắn chặt hai thị trường với nhau.
2. **Vai trò của Nhà đầu cơ (Speculators) & Trò chơi Tổng bằng Không (Zero-Sum Payoffs):** Xét thuần túy tiền mặt giữa bên Long và Short thì Futures có tổng payoff bằng $0$, nhưng xét về **hữu ích kinh tế (Economic Value)** thì đây **KHÔNG phải trò chơi vô ích**: nhà đầu cơ cung cấp thanh khoản, đưa thông tin vào giá, và hấp thụ nhu cầu phòng hộ chênh lệch khi bên bán hàng và bên mua hàng thực tế không khớp nhau. **Phần bù rủi ro (Risk Premium)** có thể tồn tại như khoản đền bù kỳ vọng cho người gánh chịu rủi ro hệ thống, chứ không phải lợi nhuận chắc chắn cho mọi nhà đầu cơ.
3. **Clearinghouse & Rủi ro Hệ thống (Systemic Risk):** Clearinghouse nắm các vị thế Long và Short đối xứng triệt tiêu nhau nên **không tự mình ôm rủi ro biến động giá một chiều** của hàng hóa. Cơ chế ký quỹ và bù trừ ròng (netting) làm giảm rủi ro tín dụng, nhưng việc tập trung thanh toán lại kết nối chặt các thành viên nên một vụ vỡ nợ lớn hoặc làn sóng Margin Call đồng loạt có thể lan truyền căng thẳng thanh khoản.

> [!WARNING]
> **Bẫy Kinh Điển về Phòng hộ Sản lượng & Đứt gãy Thanh khoản (Bài toán Omicron — Practice Question 11):**  
> Giả sử công ty Omicron sẽ **bán một lượng sản phẩm đầu ra cố định sau 4 tháng** (tiền bán hàng chỉ thu về khi giao hàng ở tháng thứ 4) và **không thể vay thêm tiền mặt để đóng Margin Call**:
> - **Lỗi 1 — Ngược chiều phòng hộ:** Muốn bán hàng trong tương lai, nỗi sợ của doanh nghiệp là **giá giảm** $\implies$ bắt buộc phải vào vị thế **SHORT** (bán kỳ hạn/tương lai), tuyệt đối KHÔNG được Long! Nếu vào Long, khi giá sản phẩm sập, doanh nghiệp lỗ kép ở cả hàng thật lẫn hợp đồng phái sinh!
> - **Lỗi 2 — Ngộ nhận "Doanh thu bán hàng cuối kỳ sẽ bù được Margin Call":** Nếu Omicron chọn **Short Futures**, khi giá hàng hóa **tăng mạnh** ở tháng thứ 1 hoặc tháng thứ 2, hàng tồn kho/sản lượng tương lai có giá trị cao hơn trên giấy tờ nhưng **chưa bán nên chưa có 1 xu tiền mặt nào chảy về**, trong khi sàn Futures lập tức trừ tiền ký quỹ mỗi ngày và phát lệnh **Margin Call đòi tiền mặt ngay lập tức**! Vì Omicron không có nguồn tài trợ bổ sung, vị thế Futures sẽ bị thanh lý cưỡng bức (forced liquidation) giữa chừng, làm hỏng hoàn toàn chiến lược phòng hộ.
> - **Giải pháp chuẩn:** Chọn **Short Forward** với ngân hàng (không tất toán hàng ngày, không phát sinh Margin Call giữa kỳ) để khớp hoàn hảo thời điểm dòng tiền tại tháng thứ 4!

---

## 1.2. Mô hình Chi phí Lưu giữ (Cost-of-Carry) & Định giá Không Arbitrage cho ĐỦ 6 TRƯỜNG HỢP

Khi lãi suất là tất định và thị trường không có ma sát, giá kỳ hạn hợp lý $F_0$ được quyết định bởi phương trình cân bằng giữa **Mua đứt tài sản hôm nay và giữ tới $T$** so với **Mua hợp đồng Forward kèm gửi tiền tiết kiệm để trả $F_0$ tại $T$**:
$$\text{Giá Kỳ Hạn } F_0 = \text{Giá Giao Ngay } S_0 + \text{Chi phí Tài trợ vốn & Lưu kho} - \text{Thu nhập / Lợi ích Tiện ích nhận được từ Tài sản}$$

Dưới đây là cẩm nang đầy đủ 6 trường hợp xuất hiện trong đề thi BFIN:

### Trường hợp 1: Cổ phiếu Không trả Cổ tức (Non-Dividend-Paying Stock)
Người giữ Forward không mất cổ tức nào so với người giữ cổ phiếu, mà còn được lợi nhờ hoãn trả tiền mua cổ phiếu tới tận ngày $T$:
- **Ghép lãi rời rạc theo năm (Effective Annual Rate — EAR $r$):**
  $$F_0 = S_0 (1 + r)^T$$
- **Ghép lãi liên tục (Continuously Compounded Rate — $r_c$):**
  $$F_0 = S_0 e^{r_c T}$$
*(Lưu ý đổi thời gian $T$ ra đơn vị **năm**: 3 tháng $\implies T = 3/12 = 0.25$; 9 tháng $\implies T = 9/12 = 0.75$).*

---

### Trường hợp 2: Cổ phiếu hoặc Trái phiếu Trả Dòng tiền Cố định Rời rạc ($I = PV_0(\text{Cash Income})$)
Nếu trong khoảng $(0, T]$ tài sản cơ sở chi trả các khoản cổ tức tiền mặt hoặc trái tức (coupon) đã biết chắc chắn $D_1, D_2, \dots$ tại các mốc $t_1, t_2, \dots \le T$, người nắm giữ Forward **không được nhận** các dòng tiền này. Do đó, ta trừ trước giá trị hiện tại $I$ của toàn bộ thu nhập này ra khỏi giá giao ngay $S_0$ rồi mới tính lãi gộp tới $T$:
- **Với lãi suất hiệu dụng năm (EAR $r$):**
  $$I = \sum_i \frac{D_i}{(1 + r)^{t_i}}, \qquad F_0 = (S_0 - I)(1 + r)^T$$
- **Với lãi suất ghép liên tục ($r_c$):**
  $$I = \sum_i D_i e^{-r_c t_i}, \qquad F_0 = (S_0 - I)e^{r_c T}$$

**Lưu ý thực chiến cho 2 biến thể đặc biệt trong đề thi:**
1. **Hợp đồng Tương lai Trái phiếu (Bond Futures — Lecture 09 Question 7b):** Luôn xuất phát từ **Full (Dirty) Spot Price** ($S_0 = \text{Clean Price} + \text{Accrued Interest}$). Ví dụ: $S_0 = \text{USD }98.50$, $r = 6\%$ EAR, đáo hạn $T = 6/12 = 0.5$ năm, có 1 kỳ coupon $\text{USD }2.50$ trả sau **2 tháng** ($t_1 = 2/12$):
   $$I = \frac{2.50}{(1.06)^{2/12}} \approx \text{USD }2.47584 \implies F_0 = (98.50 - 2.47584)(1.06)^{0.5} \approx \text{USD }98.86$$
   *(Cẩn thận: Chiết khấu coupon dùng mũ $2/12$, còn đẩy lên ngày giao hàng dùng mũ $6/12 = 0.5$!).*
2. **Khi có Phí Vay Cổ phiếu để Bán khống (Stock-Borrowing Charge — Practice Question 5):** Nếu $F_{\text{mkt}} < F_{\text{textbook}} = (S_0 - I)(1+r)^T$, sách giáo khoa khuyên **Reverse Cash-and-Carry** (bán khống cổ phiếu, gửi tiết kiệm, mua lại qua Forward). Tuy nhiên, người bán khống phải (i) đền bù cổ tức $D$ cho chủ cổ phiếu đúng ngày trả cổ tức, và (ii) trả thêm phí mượn cổ phiếu $c_{\text{borrow}}$ (ví dụ $\text{USD }1.80$/cổ phiếu ở cuối năm). Khi đó mức sàn không kinh doanh chênh lệch giá thực tế bị kéo tụt xuống thành:
   $$F_{\text{lower}} = (S_0 - I)(1 + r)^T - c_{\text{borrow}}$$
   Nếu $F_{\text{mkt}}$ nằm giữa $[F_{\text{lower}}, F_{\text{textbook}}]$, **KHÔNG có lợi nhuận Arbitrage ròng** (nếu cố giao dịch sẽ bị lỗ sau phí!). Điều này chứng minh chênh lệch so với giá lý thuyết không ma sát do chi phí giao dịch/phí vay chứng khoán gây ra **không hề bác bỏ Giả thuyết Thị trường Hiệu quả (EMH)**.

---

### Trường hợp 3: Chỉ số Cổ phiếu có Tỷ suất Cổ tức Liên tục ($q$ — Stock Index)
Với danh mục chỉ số gồm hàng trăm mã cổ phiếu trả cổ tức rải đều quanh năm, dòng cổ tức được mô hình hóa bằng tỷ suất cổ tức ghép liên tục $q$/năm (cổ tức được tái đầu tư làm số đơn vị chỉ số tăng theo $e^{qT}$, nên chỉ cần mua $e^{-qT}$ đơn vị hôm nay là cuối kỳ có đúng 1 đơn vị chỉ số):
- **Khi $q$ không đổi suốt kỳ hạn $T$:**
  $$F_0 = S_0 e^{(r - q)T} \quad \Longleftrightarrow \quad S_0 = F_0 e^{-(r - q)T}$$
- **Mở rộng Cực Quan Trọng: Khi $q$ Thay Đổi Theo Từng Giai Đoạn (Piecewise Constant Dividend Yield — L09 Q4 & Practice Q9):**  
  Giả sử kỳ hạn $T = T_1 + T_2$, trong đó giai đoạn đầu độ dài $T_1$ có tỷ suất cổ tức $q_1$ và giai đoạn sau độ dài $T_2$ có tỷ suất cổ tức $q_2$ (với lãi suất liên tục $r$):
  $$F_0 = S_0 \exp\!\Big[(r - q_1)T_1 + (r - q_2)T_2\Big]$$

**Ví dụ mẫu (Practice Question 9 — Epsilon Index):** Chỉ số $S_0 = 3{,}200$, Forward 9 tháng yết giá $F_0 = 3{,}248.36$, $r = 4.80\%$/năm (liên tục). Trong 3 tháng đầu ($T_1 = 0.25$), $q_1 = 1.20\%$. Tìm $q_2$ trong 6 tháng cuối ($T_2 = 0.50$), và đánh giá chuyện gì xảy ra nếu ngay sau khi ký Long Forward, tin mới làm $q_2$ tăng thêm $1\%$ ($+0.01$):
- **Ý a (Khôi phục $q_2$):** Lấy logarit tự nhiên hai vế:
  $$\ln\!\left(\frac{3{,}248.36}{3{,}200}\right) = (0.048 - 0.012)(0.25) + (0.048 - q_2)(0.50)$$
  $$0.0149994 = 0.0090 + 0.50(0.048 - q_2) \implies 0.048 - q_2 \approx 0.0120 \implies q_2 \approx 3.60\%$$
- **Ý b (Tác động khi $q_2$ tăng lên $4.60\%$):** Giá Forward mới trên thị trường giảm xuống còn:
  $$F_{\text{new}} = 3{,}200 e^{(0.048 - 0.012)(0.25) + (0.048 - 0.046)(0.50)} = 3{,}200 e^{0.0100} \approx 3{,}232.16\text{ điểm}$$
  Người đang nắm giữ hợp đồng **Long Forward cũ** (vẫn bị khóa nghĩa vụ mua ở giá cao $K = 3{,}248.36$) **BỊ THIỆT HẠI** vì giá trị hợp đồng lập tức rơi xuống âm: $V_0 = (3{,}232.16 - 3{,}248.36)e^{-0.048(0.75)} \approx -15.63\text{ điểm}$ (cổ tức trả nhiều hơn cho cổ đông hiện hữu làm giá chỉ số kỳ vọng lúc đáo hạn tụt xuống!).

---

### Trường hợp 4: Ngoại tệ — Ngang giá Lãi suất Có Phòng hộ (Covered Interest Parity — CIP)
Một đơn vị ngoại tệ (Foreign / Base currency) hoàn toàn tương đương với một cổ phiếu trả tỷ suất cổ tức bằng chính **lãi suất phi rủi ro của đồng ngoại tệ đó** ($r_{\text{base}}$)!

- **Công thức Ghép lãi Liên tục:**
  $$F_{0,\text{quote/base}} = S_{0,\text{quote/base}} \cdot e^{(r_{\text{quote}} - r_{\text{base}})T}$$
- **Công thức Ghép lãi Rời rạc theo Năm (EAR):**
  $$F_{0,\text{quote/base}} = S_{0,\text{quote/base}} \cdot \frac{(1 + r_{\text{quote}})^T}{(1 + r_{\text{base}})^T}$$

> [!TIP]
> **MẸO BẤT BẠI "TỬ BÁO – MẪU CƠ" (KHÔNG BAO GIỜ NHẦM TỬ SỐ & MẪU SỐ KHI YẾT GIÁ TỶ GIÁ):**  
> Khi đọc câu yết giá trong đề tiếng Anh, hãy viết ngay đơn vị dưới dạng phân số toán học:
> - Đề ghi `1.1600 USD per EUR` $\implies$ Viết phân số đơn vị là $\dfrac{\text{USD}}{\text{EUR}}$:
>   - `USD` nằm ở **Tử số** (đồng tiền báo giá — Quote / Domestic currency) $\implies$ Lãi suất $r_{\text{USD}}$ nằm trên **Tử số** $(1 + r_{\text{USD}})^T$ hoặc mang dấu **DƯƠNG** $+r_{\text{USD}}$ trên số mũ!
>   - `EUR` nằm ở **Mẫu số** (1 đơn vị hàng hóa cơ sở — Base / Foreign currency) $\implies$ Lãi suất $r_{\text{EUR}}$ nằm dưới **Mẫu số** $(1 + r_{\text{EUR}})^T$ hoặc mang dấu **ÂM** $-r_{\text{EUR}}$ trên số mũ!
> - Tương tự: Đề ghi `0.0550 USD per MXN` $\implies \dfrac{\text{USD}}{\text{MXN}} \implies F_0 = S_0 \dfrac{1 + r_{\text{USD}}}{1 + r_{\text{MXN}}}$ (L09 Question 8.2).
> - **Kiểm tra trực giác kinh tế 2 giây:** Đồng tiền nào có **lãi suất cao hơn** thì khi gửi tiết kiệm sẽ sinh lãi nhiều hơn, nên trên thị trường kỳ hạn đồng tiền đó bắt buộc phải **mất giá kỳ hạn (Forward Discount)** để triệt tiêu cơ hội ăn chênh lệch lãi suất! Ví dụ $r_{\text{GBP}} = 5.61\% > r_{\text{USD}} = 4.00\% \implies$ GBP phải rẻ hơn ở kỳ hạn: $F_0 = 1.2300 < S_0 = 1.2500\text{ USD per GBP}$ (L09 Question 5).

---

### Trường hợp 5: Hàng hóa Vật chất — Chi phí Lưu kho ($U, u$) & Lợi suất Tiện ích Ròng (Net Convenience Yield $y$)
Khác với tài sản tài chính, việc nắm giữ hàng hóa vật chất (dầu thô, đồng, ngô, vàng...) phát sinh hai yếu tố đối ngược nhau:

1. **Khi CHỈ có Chi phí Lưu kho (Storage Cost — tương đương "cổ tức âm"):** Người giữ Forward đỡ tốn tiền kho bãi so với người mua hàng thật cất kho, nên chi phí lưu kho làm **TĂNG** giá Forward:
   - Chi phí lưu kho có hiện giá $U_0$ (hoặc trả ngay $U_0$ tại $t=0$, như L09 C13):
     $$F_0 = (S_0 + U_0)(1 + r)^T \quad \text{hoặc} \quad F_0 = (S_0 + U_0)e^{rT}$$
   - Chi phí lưu kho trả cuối kỳ $C_T$ tại ngày đáo hạn $T$ (như L09 Question 8.1: lưu kho bằng $2\% \times S_0$ trả cuối năm):
     $$F_0 = S_0(1 + r)^T + C_T$$
   - Chi phí lưu kho tỷ lệ liên tục $u$/năm:
     $$F_0 = S_0 e^{(r + u)T}$$

2. **Khi có Lợi suất Tiện ích Ròng (Net Convenience Yield $y$ — L09 Question 7c & Practice Question 10):**
   - Các nhà máy lọc dầu, luyện đồng nắm giữ tồn kho vật chất được hưởng một lợi ích phi tiền tệ gọi là **Convenience Yield** (tránh đứt gãy dây chuyền sản xuất khi nguồn cung khan hiếm đột ngột, tận dụng ngay các đợt sốt giá giao ngay — điều mà tờ giấy hợp đồng Forward không thể làm được!).
   - Đặt $y$ là **Net Convenience Yield** (= Lợi ích tồn kho vật chất $-$ Chi phí lưu kho tỷ lệ):
     $$F_0 = S_0 e^{(r - y)T} \quad \Longleftrightarrow \quad y = r - \frac{\ln(F_0 / S_0)}{T}$$
   - **Tại sao giá Futures hàng hóa rất hay thấp hơn giá giao ngay ($F_0 < S_0$ — Backwardation)?** Khi nguồn cung giao ngay căng thẳng, lợi ích nắm giữ hàng thật vượt trội hơn lãi suất vay vốn (**$y > r$**), làm số mũ $(r - y)T < 0 \implies F_0 < S_0$! (Ví dụ L09 Q7c: Dầu $S_0 = 74.00$, $F_{0.5} = 72.80$, $r = 3.5\% \implies y = 0.035 - \frac{\ln(72.80/74.00)}{0.5} \approx 6.77\% > 3.5\%$).

3. **Bất đối xứng Kinh doanh Chênh lệch Giá trên Hàng hóa Tiêu dùng (Asymmetric Arbitrage — Phân tích sâu Practice Question 10):**
   - Giả sử hàng hóa có $S_0 = \text{USD }96$, $r = 4\%$ (liên tục), $T = 0.5$, nhưng giá kỳ hạn chỉ là $F_{\text{mkt}} = \text{USD }94.20$ (thấp hơn mức chuẩn chỉ tính lãi vay $96 e^{0.04(0.5)} = \text{USD }97.94$).
   - **Sai lầm của Eta (đề xuất Cash-and-Carry khi $F_{\text{mkt}}$ thấp):** Vay $\text{USD }96$, mua hàng cất kho và bán Forward giá $\text{USD }94.20$ sẽ **CHẮC CHẮN LỖ NẶNG** vì tiền thu về $\text{USD }94.20$ còn thấp hơn cả nợ gốc lẫn lãi vay $\text{USD }97.94$ cộng chi phí lưu kho! Cash-and-Carry chỉ kiếm lời được khi **$F_{\text{mkt}} > (S_0 + U_0)e^{rT}$**!
   - **Tại sao đảo ngược giao dịch sang Reverse Cash-and-Carry cũng THẤT BẠI?** Muốn ăn chênh lệch khi $F_{\text{mkt}} = 94.20 < 97.94$, nhà giao dịch phải bán khống hàng hóa hôm nay thu $\text{USD }96$ gửi ngân hàng rồi mua lại ở $\text{USD }94.20$. Nhưng:
     1. Người ngoài ngành **không thể mượn hàng hóa vật chất để bán khống**.
     2. Các doanh nghiệp đang có sẵn hàng trong kho cũng **không chịu bán giao ngay để đổi sang Long Forward**, vì nếu bán hết hàng trong kho, nhà máy của họ phải ngừng chạy — họ đánh mất chính phần **lợi ích tiện ích tồn kho $y$** (ở bài Zeta, $y = 0.04 - \frac{\ln(94.20/96)}{0.5} \approx 7.79\%$/năm)! Do đó, $F_0 = 94.20 < S_0$ hoàn toàn tồn tại bền vững mà không hề tạo ra cơ hội Arbitrage!

---

### Trường hợp 6: Hợp đồng Kỳ hạn trên Trái phiếu (Forward Contract on a Zero-Coupon / Coupon Bond)
Khi định giá hợp đồng kỳ hạn ký tại $t=0$, giao nhận tại năm $T_1$, để mua một trái phiếu sẽ đáo hạn tại năm $T_2$ ($T_2 > T_1$), quy trình 2 bước không bao giờ sai là:
1. **Bước 1:** Tìm giá trị hiện tại tại $t=0$ ($PV_0$) của trái phiếu đó bằng lãi suất giao ngay kỳ hạn $T_2$ ($s_{T_2}$).
2. **Bước 2:** Đẩy $PV_0$ lên thời điểm giao hàng $T_1$ bằng lãi suất giao ngay kỳ hạn $T_1$ ($s_{T_1}$) (trừ đi các coupon trả trước $T_1$ nếu là trái phiếu coupon):
   $$PV_0 = \frac{\text{Face Value}}{(1 + s_{T_2})^{T_2}}, \qquad F_{0, T_1} = PV_0 (1 + s_{T_1})^{T_1} = \frac{\text{Face Value} \cdot (1 + s_{T_1})^{T_1}}{(1 + s_{T_2})^{T_2}}$$

> [!CAUTION]
> **Bẫy Đọc Đề Kỳ hạn Trái phiếu (Lecture 09 Question 3):** Đề ghi *"buy a **four-year**, default-free zero-coupon bond that **will be issued in three years**"* với mệnh giá $\text{USD }2{,}000$, $s_3 = 3\%, s_7 = 5\%$. Trái phiếu kỳ hạn 4 năm phát hành vào năm thứ 3 sẽ đáo hạn vào **năm thứ $T_2 = 3 + 4 = 7$** (chứ không phải năm 4)! Do đó:
> $$PV_0 = \frac{2{,}000}{(1.05)^7} \approx \text{USD }1{,}421.36 \implies F_{0,3} = 1{,}421.36 \times (1.03)^3 \approx \text{USD }1{,}553.16$$

---

## 1.3. Định giá lại Hợp đồng Kỳ hạn Đang Nắm Giữ tại Thời điểm Trung gian $t$ ($0 < t < T$)

Đây là dạng bài xuất hiện cực kỳ thường xuyên ở câu tự luận mở màn (như L09 Question 2 và Practice Question 6). Hãy phân biệt thật sắc nét hai đại lượng:
- **$K = F_0$ (Original Delivery Price):** Giá giao hàng đã ghi chết trên hợp đồng từ ngày ký $t=0$ (khi đó giá trị hợp đồng $V_0 = 0$). Giá $K$ này **KHÔNG BAO GIỜ THAY ĐỔI** trong suốt vòng đời hợp đồng cũ.
- **$F_t$ (New Market Forward Price):** Giá giao hàng của các hợp đồng mới ký tại thời điểm $t$ cho thời gian còn lại $\tau = T - t$.
- **$V_t$ (hay $f_t$ — Current Contract Value):** Giá trị thị trường (Mark-to-market value) của hợp đồng cũ đang nắm giữ tại thời điểm $t$.

### Công thức Tổng quát Tương đương Hai Cách Viết (Đều ra Đúng 1 Kết quả)
Đặt thời gian còn lại đến ngày đáo hạn là **$\tau = T - t$**, và lãi suất phi rủi ro áp dụng tại thời điểm $t$ cho kỳ hạn còn lại $\tau$ là **$r_{\text{new}}$**:

$$\boxed{V_t(\text{Long per unit}) = S_t - PV_t(D_{\text{rem}}) - PV_t(K) = PV_t(F_t - K)}$$
$$\boxed{V_t(\text{Short per unit}) = -V_t(\text{Long per unit}) = PV_t(K) + PV_t(D_{\text{rem}}) - S_t = PV_t(K - F_t)}$$

Trong đó:
- Với lãi suất hiệu dụng năm (EAR $r_{\text{new}}$): $PV_t(K) = \dfrac{K}{(1 + r_{\text{new}})^{T - t}}$ và $F_t = \big[S_t - PV_t(D_{\text{rem}})\big](1 + r_{\text{new}})^{T - t}$.
- Với lãi suất ghép liên tục ($r_{\text{new}}$): $PV_t(K) = K e^{-r_{\text{new}}(T - t)}$ và $F_t = \big[S_t - PV_t(D_{\text{rem}})\big]e^{r_{\text{new}}(T - t)}$ (nếu là chỉ số có tỷ suất cổ tức $q$: $V_t(\text{Long}) = S_t e^{-q(T-t)} - K e^{-r_{\text{new}}(T-t)} = (F_t - K)e^{-r_{\text{new}}(T-t)}$).
- Nếu hợp đồng bao gồm $N$ cổ phiếu/đơn vị: **Tổng giá trị hợp đồng $= N \times V_t(\text{per unit})$**.

**Ví dụ Mẫu Có Bẫy Đổi Lãi Suất & Đề Nghị Chấm Dứt Hợp Đồng (Practice Question 6 — Alpha):**
- Ngày $t=0$: Ký Long Forward 9 tháng ($T = 9/12 = 0.75$) cho $N = 150$ cổ phiếu không cổ tức. $S_0 = \text{USD }68$, $r_0 = 4\%$ EAR.
  $$\implies \text{Giá giao hàng gốc: } K = 68 \times (1.04)^{9/12} \approx \text{USD }70.029966 \text{ (báo cáo USD }70.03\text{)}$$
- Sau 3 tháng ($t = 3/12 \implies$ **thời gian còn lại $T - t = 6/12 = 0.5$ năm**): Giá cổ phiếu lên $S_t = \text{USD }72$, lãi suất mới cho kỳ hạn còn lại tăng lên **$r_{\text{new}} = 5\%$ EAR**. Đối tác đề nghị trả Alpha $\text{USD }500$ để thanh lý toàn bộ hợp đồng:
  $$V_t(\text{per share}) = 72 - \frac{70.029966}{(1.05)^{0.5}} = 72 - 68.342249 = \text{USD }3.657751/\text{cổ phiếu}$$
  $$V_t(\text{total}) = 150 \times 3.657751 \approx \textbf{USD 548.66}$$
- **Đánh giá lời đề nghị:** Hợp đồng đang có giá trị kinh tế hợp lý là $\text{USD }548.66 > \text{USD }500$. Do đó Alpha nên **TỪ CHỐI** mức đền bù $\text{USD }500$ (nếu chấp nhận sẽ thiệt mất $\text{USD }48.66$ giá trị hiện tại!).
- **Bẫy chết người cần tránh:** Tuyệt đối không dùng lãi suất cũ $4\%$ để chiết khấu ở bước 2, và không dùng mũ $9/12$ hay $3/12$ (phải dùng thời gian **còn lại** $6/12 = 0.5$)!

---

## 1.4. Kỹ năng Lập Bảng Dòng tiền Arbitrage Tự Tài Trợ (Cash-and-Carry & Reverse Cash-and-Carry)

Trong đề thi tự luận, chỉ viết con số lợi nhuận cuối cùng là **chưa đủ điểm tối đa** — đề luôn yêu cầu *"specify the trades and show the dated cash flows today and at maturity"*. Dưới đây là quy trình cơ học không bao giờ sai cho cả **Cổ phiếu/Hàng hóa** lẫn **Ngoại tệ**:

### A. Hai Chiều Giao dịch Chuẩn trên Cổ phiếu / Hàng hóa (Khi $F^*$ là giá hợp lý)

1. **Khi $F_{\text{mkt}} > F^*$ (Hợp đồng Kỳ hạn bị Định giá ĐẮT — Chiến lược Cash-and-Carry):**
   - **Tư duy:** Bán kỳ hạn giá cao ($F_{\text{mkt}}$), mua tài sản giao ngay ($S_0$) bằng tiền đi vay để có hàng giao lúc đáo hạn!
   - **Nếu có cổ tức tiền mặt $D$ tại $t_1$:** Tách khoản vay hôm nay thành 2 phần: (i) Vay $PV_0(D)$ kỳ hạn $t_1$ (đến ngày $t_1$ lấy đúng tiền cổ tức $D$ nhận được trả dứt điểm khoản vay này!), và (ii) Vay phần còn lại $S_0 - PV_0(D)$ kỳ hạn $T$ (đến ngày $T$ trả $(S_0 - PV_0(D))(1+r)^T = F^*$).
   - **Lợi nhuận chắc chắn tại $T$ trên 1 đơn vị:** $\Pi_T = F_{\text{mkt}} - F^* > 0$ (mọi số hạng $S_T$ triệt tiêu sạch!).

| Giao dịch (Cash-and-Carry cho $N$ cổ phiếu không cổ tức) | Dòng tiền Hôm nay ($t=0$) | Dòng tiền tại Đáo hạn ($t=T$) |
| :--- | ---: | :--- |
| 1. Vay tiền mặt $N \cdot S_0$ ở lãi suất $r$ | $+N \cdot S_0$ | $-N \cdot S_0 (1+r)^T = -N \cdot F^*$ |
| 2. Mua $N$ cổ phiếu trên thị trường giao ngay | $-N \cdot S_0$ | Giá trị $N \cdot S_T$ (dùng để giao hàng bên dưới) |
| 3. Bán (Short) Forward $N$ cổ phiếu ở giá $F_{\text{mkt}}$ | $0$ | Giao $N$ cổ phiếu, nhận $+N \cdot F_{\text{mkt}}$ (tức $+N(F_{\text{mkt}} - S_T)$) |
| **Dòng tiền Ròng (Net Cash Flow)** | **$0$** | **$+N(F_{\text{mkt}} - F^*) > 0$ (Không phụ thuộc $S_T$!)** |

2. **Khi $F_{\text{mkt}} < F^*$ (Hợp đồng Kỳ hạn bị Định giá RẺ — Chiến lược Reverse Cash-and-Carry):**
   - **Tư duy:** Mua kỳ hạn giá rẻ ($F_{\text{mkt}}$), bán khống tài sản giao ngay thu $+S_0$ đem gửi tiết kiệm (nếu có cổ tức $D$ tại $t_1$, trích $PV_0(D)$ gửi kỳ hạn $t_1$ để lấy tiền trả đền bù cổ tức cho chủ cổ phiếu, phần còn lại $S_0 - PV_0(D)$ gửi đến $T$ thu về $F^*$).
   - **Lợi nhuận chắc chắn tại $T$ trên 1 đơn vị:** $\Pi_T = F^* - F_{\text{mkt}} > 0$.

| Giao dịch (Reverse Cash-and-Carry cho $N$ cổ phiếu) | Dòng tiền Hôm nay ($t=0$) | Dòng tiền tại Đáo hạn ($t=T$) |
| :--- | ---: | :--- |
| 1. Bán khống (Short sell) $N$ cổ phiếu | $+N \cdot S_0$ | Phải trả lại $N$ cổ phiếu (giá trị $-N \cdot S_T$) |
| 2. Gửi tiết kiệm toàn bộ $N \cdot S_0$ ở lãi suất $r$ | $-N \cdot S_0$ | Nhận gốc + lãi $+N \cdot S_0(1+r)^T = +N \cdot F^*$ |
| 3. Mua (Long) Forward $N$ cổ phiếu ở giá $F_{\text{mkt}}$ | $0$ | Trả $-N \cdot F_{\text{mkt}}$, nhận $N$ cổ phiếu (trả kho bán khống) |
| **Dòng tiền Ròng (Net Cash Flow)** | **$0$** | **$+N(F^* - F_{\text{mkt}}) > 0$ (Không phụ thuộc $S_T$!)** |

---

### B. Bảng Arbitrage Ngoại tệ & Phẫu thuật "Bẫy Lệch Gốc – Lãi" (Bài toán Tau — Practice Question 14 & L09 Question 6)

Giả sử tỷ giá yết theo `USD per EUR` ($S_0$ USD đổi được 1 EUR), giá kỳ hạn hợp lý là $F^* = S_0 \dfrac{(1 + r_{\text{USD}})^T}{(1 + r_{\text{EUR}})^T}$ (hoặc $S_0 e^{(r_{\text{USD}} - r_{\text{EUR}})T}$). Đề bài cho hạn mức vay ban đầu có giá trị giao ngay tương đương $W_{\text{USD}}$ (ví dụ $\text{USD }216{,}000$ hoặc $\text{USD }400{,}000$).

- **Trường hợp A: $F_{\text{mkt}} > F^*$ (EUR kỳ hạn đang ĐẮT $\implies$ BÁN EUR KỲ HẠN):**
  1. Vay $W_{\text{USD}}$ bằng đồng USD $\implies$ Tại $T$ nợ $W_{\text{USD}}(1 + r_{\text{USD}})^T$ USD.
  2. Đổi toàn bộ sang EUR giao ngay được $E_0 = \dfrac{W_{\text{USD}}}{S_0}$ EUR, đem gửi tiết kiệm EUR ở lãi suất $r_{\text{EUR}}$.
  3. Tại ngày đáo hạn $T$, sổ tiết kiệm EUR nở thành **CẢ GỐC LẪN LÃI**: $E_T = E_0(1 + r_{\text{EUR}})^T$ EUR.
  4. Ngay tại $t=0$, ký hợp đồng **Bán EUR Forward cho TOÀN BỘ số lượng $E_T$** (chứ không phải $E_0$!) tại tỷ giá $F_{\text{mkt}}$ $\implies$ thu về $F_{\text{mkt}} \cdot E_T$ USD tại $T$.
  5. **Lợi nhuận USD tại $T$:**
     $$\Pi_T(\text{USD}) = F_{\text{mkt}} \left[\frac{W_{\text{USD}}}{S_0}(1 + r_{\text{EUR}})^T\right] - W_{\text{USD}}(1 + r_{\text{USD}})^T > 0$$

- **Trường hợp B: $F_{\text{mkt}} < F^*$ (EUR kỳ hạn đang RẺ $\implies$ MUA EUR KỲ HẠN):**
  1. Vay $E_0 = \dfrac{W_{\text{USD}}}{S_0}$ EUR $\implies$ Tại $T$ phải trả cả gốc lẫn lãi là $E_T = E_0(1 + r_{\text{EUR}})^T$ EUR.
  2. Bán $E_0$ EUR lấy $W_{\text{USD}}$ USD trên thị trường giao ngay, đem gửi tiết kiệm USD $\implies$ Tại $T$ thu về $W_{\text{USD}}(1 + r_{\text{USD}})^T$ USD.
  3. Ngay tại $t=0$, ký hợp đồng **Mua EUR Forward cho ĐÚNG số nợ gốc + lãi $E_T$** tại tỷ giá rẻ $F_{\text{mkt}}$ $\implies$ tốn $F_{\text{mkt}} \cdot E_T$ USD tại $T$.
  4. **Lợi nhuận USD tại $T$:**
     $$\Pi_T(\text{USD}) = W_{\text{USD}}(1 + r_{\text{USD}})^T - F_{\text{mkt}} \left[\frac{W_{\text{USD}}}{S_0}(1 + r_{\text{EUR}})^T\right] > 0$$

> [!CAUTION]
> **PHẪU THUẬT BẪY CHÍ MẠNG TRONG BÀI TAU (PRACTICE QUESTION 14):**  
> Cho $S_0 = 1.0800\text{ USD/EUR}$, $F_{\text{mkt}} = 1.1200\text{ USD/EUR}$, $r_{\text{USD}} = 5\%$ EAR, $r_{\text{EUR}} = 2\%$ EAR, kỳ hạn $T = 9/12 = 0.75$ năm.  
> Tau đề xuất: *(1) Vay $\text{EUR }200{,}000$; (2) Đổi sang USD gửi tiết kiệm; (3) Bán $\text{EUR }200{,}000$ kỳ hạn giá $1.1200$* và khoe lãi chắc chắn $(1.12 - 1.08) \times 200{,}000 = \text{USD }8{,}000$!  
> **Tại sao đề xuất của Tau SAI NGHIÊM TRỌNG trên cả 2 tầng bản chất?**
> 1. **Tính chuẩn CIP:** $F^* = 1.0800 \times \dfrac{(1.05)^{0.75}}{(1.02)^{0.75}} \approx \mathbf{1.103737\text{ USD/EUR}} < F_{\text{mkt}} = 1.1200$.
> 2. **Phân tích dòng tiền thực tế của Tau tại $T = 9$ tháng theo tỷ giá giao ngay lúc đáo hạn $S_T$:**
>    - Về USD: Tiền gửi USD $\text{USD }216{,}000 \times (1.05)^{0.75} = +224{,}050.40\text{ USD}$, cộng tiền bán $\text{EUR }200{,}000$ qua Forward $+224{,}000.00\text{ USD} \implies$ Tổng thu USD $= +448{,}050.40\text{ USD}$.
>    - Về EUR: Tau vừa **nợ ngân hàng gốc + lãi vay EUR** là $-200{,}000(1.02)^{0.75} = -202{,}992.56\text{ EUR}$, lại vừa **phải giao thêm $-200{,}000\text{ EUR}$** cho hợp đồng Short Forward (vì Tau đi ngược chiều ở chân vay EUR!) $\implies$ Tổng thiếu hụt EUR phải ra chợ giao ngay mua bù ở giá $S_T$ là **$402{,}992.56\text{ EUR}$**!
>    - **Dòng tiền USD ròng thực tế của Tau:** $\text{CF}_T(\text{USD}) = \mathbf{448{,}050.40 - 402{,}992.56 \, S_T}$. Vị thế này **phụ thuộc nặng nề vào tỷ giá tương lai $S_T$** (chỉ là đầu cơ khổng lồ vào việc EUR sập giá, nếu $S_T = 1.12$ thì Tau lỗ ngay $-3{,}301.27\text{ USD}$!), hoàn toàn KHÔNG PHẢI Arbitrage!
>    *(Ngay cả khi ai đó chọn đúng chiều giao dịch mà chỉ ký Forward cho gốc $200{,}000\text{ EUR}$ thay vì cả gốc lẫn lãi $202{,}992.56\text{ EUR}$, phần lãi $2{,}992.56\text{ EUR}$ vẫn bị hở tỷ giá $S_T$!).*
> 3. **Bảng Arbitrage Tự tài trợ ĐÚNG CHUẨN (với vốn vay ban đầu $\text{USD }216{,}000$):**

| Giao dịch Đúng Chuẩn (Tau Q14c) | Hôm nay: USD | Hôm nay: EUR | Sau 9 tháng: USD | Sau 9 tháng: EUR |
| :--- | ---: | ---: | ---: | ---: |
| 1. Vay USD ở lãi suất 5% EAR | $+216{,}000.00$ | $0$ | $-224{,}050.40$ | $0$ |
| 2. Mua EUR giao ngay tại $1.0800$ | $-216{,}000.00$ | $+200{,}000.00$ | $0$ | $0$ |
| 3. Đầu tư EUR ở lãi suất 2% EAR | $0$ | $-200{,}000.00$ | $0$ | $+202{,}992.56$ |
| 4. Bán Forward **toàn bộ $202{,}992.56$ EUR** tại $1.1200$ | $0$ | $0$ | $+227{,}351.67$ | $-202{,}992.56$ |
| **Dòng tiền Ròng (Net Cash Flow)** | **$0.00$** | **$0.00$** | **$+3{,}301.27$** | **$0.00$** |

---

## 1.5. Cơ chế Ký quỹ Hợp đồng Tương lai (Futures Marking-to-Market Ledger)

### 1. Bộ Quy tắc Vận hành Tài khoản Ký quỹ
Giả sử nhà đầu tư nắm giữ **$n$ hợp đồng**, mỗi hợp đồng có quy mô **$Q$ đơn vị** (tổng quy mô vị thế là $N = n \times Q$ đơn vị):

1. **Tại ngày mở vị thế ($t = 0$, giá $F_0$):** Nộp **Ký quỹ Ban đầu (Initial Margin — $IM$)**. Đây là tiền đặt cọc thế chấp thực hiện nghĩa vụ (collateral), KHÔNG PHẢI tiền mua tài sản.
2. **Cuối mỗi ngày giao dịch $t = 1, 2, \dots$ (giá thanh toán $F_t$):**
   - **Nếu giữ vị thế MUA (Long Futures):** $\text{Daily P\&L}_t = +n Q (F_t - F_{t-1})$ (giá tăng thì cộng tiền, giá giảm thì trừ tiền).
   - **Nếu giữ vị thế BÁN (Short Futures):** $\text{Daily P\&L}_t = +n Q (F_{t-1} - F_t)$ (giá giảm thì cộng tiền, giá tăng thì trừ tiền!).
   - **Số dư trước nộp thêm (Balance before deposit):** $\text{Bal}_{\text{before}, t} = \text{Closing Balance}_{t-1} + \text{Daily P\&L}_t$.
3. **Kiểm tra Ngưỡng Ký quỹ Duy trì (Maintenance Margin — $MM$) & Lệnh Gọi Ký quỹ Bổ sung (Variation Margin Call):**
   - Khi bị kích hoạt Margin Call, số tiền phải nộp thêm (**Variation Margin**) BẮT BUỘC phải khôi phục tài khoản quay về đúng mức **Initial Margin ($IM$)** (chứ KHÔNG phải chỉ nộp bù lên $MM$!):
     $$\text{Additional Deposit}_t = IM - \text{Bal}_{\text{before}, t} \implies \text{Closing Balance}_t = IM$$

> [!IMPORTANT]
> **PHÂN BIỆT SINH TỬ 2 CÁCH VIẾT CÂU CHỮ ĐỀ BÀI KHI SỐ DƯ CHẠM ĐÚNG BẰNG $MM$ ($\text{Bal}_{\text{before}, t} = MM$):**
> - **Chuẩn mặc định trong các bài giảng & Practice của Dr. Cayirli (L09 C10 & Practice Q7):** Đề ghi *"balance **below** maintenance"* hoặc *"balance **strictly below** maintenance"* ($\text{Bal}_{\text{before}, t} < MM$) $\implies$ Khi số dư **bằng đúng $MM$**, **KHÔNG BỊ gọi ký quỹ** ($\text{Deposit} = 0$, giữ nguyên số dư $MM$ sang ngày hôm sau)!
> - **Trường hợp ngoại lệ nếu đề đổi câu chữ:** Nếu đề ghi rõ *"balance **at or below** maintenance"* ($\text{Bal}_{\text{before}, t} \le MM$) $\implies$ Chạm đúng bằng $MM$ **CÓ BỊ gọi ký quỹ** và phải nộp ngay $IM - MM$!  
> $\implies$ **Luôn gạch chân cụm từ `below` / `strictly below` vs. `at or below` ngay khi đọc đề!**

### 2. Công thức Tìm Nhanh Ngưỡng Giá Margin Call & Đẳng thức Kiểm tra Chéo
- **Ngưỡng giá đầu tiên kích hoạt Margin Call** (khi `strictly below` $MM$, chưa từng nộp thêm):
  - Với **Long** ($nQ$ đơn vị mở tại $F_0$): $IM + nQ(P - F_0) < MM \iff P < F_0 - \dfrac{IM - MM}{nQ}$.
  - Với **Short** ($nQ$ đơn vị mở tại $F_0$): $IM + nQ(F_0 - P) < MM \iff P > F_0 + \dfrac{IM - MM}{nQ}$.
- **Đẳng thức Đối chiếu Sổ cái Bất Bại (Account Reconciliation Identity — luôn dùng ở câu `b`):**
  $$\boxed{\text{Total Trading Profit} = \sum_{t} \text{Daily P\&L}_t = \begin{cases} nQ(F_{\text{close}} - F_0) & \text{(Long)} \\ nQ(F_0 - F_{\text{close}}) & \text{(Short)} \end{cases} = \text{Cash Released on Closing} - \text{Total External Cash Contributed}}$$
  Trong đó: $\text{Total External Cash Contributed} = IM + \sum_{t} \text{Additional Deposit}_t$ (nếu không rút tiền thặng dư giữa kỳ).

### 3. Ví dụ Mẫu Khôi phục Giá Ẩn & Đối chiếu Sổ cái (Practice Question 7 — Beta)
Beta **Short** $4$ hợp đồng $\times 250 = 1{,}000$ đơn vị tại $F_0 = \text{USD }45.50$. Tổng $IM = \text{USD }8{,}000$, tổng $MM = \text{USD }6{,}000$ (`strictly below` $MM$ mới gọi ký quỹ). Cho $F_1 = 46.30$, ngày 2 biết $\text{Balance before deposit} = 6{,}000$, $F_3 = 48.20$, $F_4 = 44.30$ (đóng vị thế):
- **Ngày 1 ($F_1 = 46.30$):** Short lỗ khi giá tăng $\implies \text{P\&L}_1 = 1{,}000(45.50 - 46.30) = -800 \implies \text{Bal}_1 = 8{,}000 - 800 = 7{,}200 > 6{,}000$ (không nộp thêm).
- **Ngày 2 (Tìm ngược $F_2$):** Số dư trước nộp là $6{,}000 \implies \text{P\&L}_2 = 6{,}000 - 7{,}200 = -1{,}200 \implies 1{,}000(46.30 - F_2) = -1{,}200 \implies \mathbf{F_2 = \text{USD }47.50}$. Vì $6{,}000$ **không nhỏ hơn ngặt (`strictly below`)** $6{,}000 \implies \mathbf{\text{Deposit}_2 = 0}$, số dư cuối ngày 2 là $6{,}000$!
- **Ngày 3 ($F_3 = 48.20$):** $\text{P\&L}_3 = 1{,}000(47.50 - 48.20) = -700 \implies \text{Bal}_{\text{before},3} = 6{,}000 - 700 = 5{,}300 < 6{,}000 \implies$ **Margin Call!** Nộp bù $\text{Deposit}_3 = 8{,}000 - 5{,}300 = \mathbf{2{,}700} \implies \text{Closing}_3 = 8{,}000$.
- **Ngày 4 ($F_4 = 44.30$):** $\text{P\&L}_4 = 1{,}000(48.20 - 44.30) = +3{,}900 \implies \text{Closing}_4 = 8{,}000 + 3{,}900 = \mathbf{11{,}900}$.

| Ngày | Giá thanh toán ($F_t$) | Lãi/Lỗ trong ngày (Daily P&L) | Số dư trước nộp bù | Tiền nộp thêm (Deposit) | Số dư cuối ngày (Closing) |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 0 | $45.50$ | — | — | $0$ | $8{,}000$ |
| 1 | $46.30$ | $-800$ | $7{,}200$ | $0$ | $7{,}200$ |
| 2 | **$47.50$** | **$-1{,}200$** | $6{,}000$ | **$0$** *(bằng MM, không gọi!)* | **$6{,}000$** |
| 3 | $48.20$ | $-700$ | $5{,}300$ | **$+2{,}700$** | $8{,}000$ |
| 4 | $44.30$ | $+3{,}900$ | $11{,}900$ | $0$ | **$11{,}900$** |

- **Đối chiếu (Reconciliation):**
  - Tổng tiền mặt bên ngoài đã nộp vào: $8{,}000 + 2{,}700 = \text{USD }10{,}700$.
  - Tiền mặt giải phóng khi đóng vị thế: $\text{USD }11{,}900$.
  - Tổng lợi nhuận giao dịch: $11{,}900 - 10{,}700 = \mathbf{+\text{USD }1{,}200} = 1{,}000 \times (45.50 - 44.30) = -800 - 1{,}200 - 700 + 3{,}900$. Khớp tuyệt đối 100%!

---

## 1.6. Hoán đổi Lãi suất (IRS), Hoán đổi Tiền tệ (Currency Swaps) & CDS

### A. Hoán đổi Lãi suất Cố định – Thả nổi (Plain-Vanilla Interest-Rate Swap — IRS)

1. **Cấu trúc Dòng tiền & Thanh toán Bù trừ Ròng (Netting):**
   - Hai bên thỏa thuận trên cùng một đồng tiền và cùng một **Vốn danh nghĩa (Notional Principal $N$)**. **Vốn gốc $N$ KHÔNG BAO GIỜ ĐƯỢC TRAO ĐỔI** (kể cả lúc bắt đầu lẫn lúc đáo hạn; khoản gốc phải trả lúc đáo hạn của IRS bằng **$0$** — L09 Question 9b!).
   - Với phân số năm mỗi kỳ thanh toán là **$\Delta$** (hàng năm $\Delta = 1$; bán niên $\Delta = 0.5$; hàng quý $\Delta = 0.25$), tại kỳ thứ $k$ có lãi suất thả nổi tham chiếu theo năm là $L_k$ (ví dụ SOFR ghép lãi theo năm tính cuối kỳ, hoặc lãi suất 3 tháng chốt đầu kỳ trả cuối kỳ):
     $$\text{Fixed Leg}_k = N \cdot K \cdot \Delta, \qquad \text{Floating Leg}_k = N \cdot L_k \cdot \Delta$$
   - **Dòng tiền ròng đối với Bên Trả Cố định – Nhận Thả nổi (Fixed Payer / Floating Receiver):**
     $$\boxed{\text{Net Receipt}_k(\text{Fixed Payer}) = N (L_k - K) \Delta}$$
     *(Nếu dương $> 0$: đối tác trả tiền cho Fixed Payer; nếu âm $< 0$: Fixed Payer trả tiền chênh lệch cho đối tác).*
   - **Khôi phục lãi suất ẩn $L_k$ (như Practice Q8b):** Nếu Gamma trả cố định $K = 3.80\%$ trên $N = \text{USD }18\text{m}$ theo quý ($\Delta = 0.25$) và kỳ 2 nhận ròng $+\text{USD }18{,}000 \implies 18{,}000{,}000 \times (L_2 - 0.038) \times 0.25 = +18{,}000 \implies L_2 - 0.038 = +0.0040 \implies L_2 = 4.20\%$.

2. **Chuyển đổi Khoản Vay / Khoản Đầu tư & Cảnh báo Rủi ro Tín dụng (L09 Question 10):**
   - **Quy tắc chọn chiều Swap trong 3 giây:** Nhìn vào vị thế gốc đang có, **muốn xóa bỏ chân lãi suất nào thì dùng Swap làm ngược lại chân đó**!
     - Đang **vay thả nổi** (trả $L + s_1$), muốn chuyển thành **chi phí cố định** $\implies$ Vào Swap **Nhận $L$, Trả cố định $K$** $\implies \text{Chi phí vay ròng} = (L + s_1) - L + K = K + s_1$.
     - Đang **vay cố định** (trả $r_0$), muốn chuyển thành **chi phí thả nổi** $\implies$ Vào Swap **Nhận cố định $K$, Trả $L$** $\implies \text{Chi phí vay ròng} = r_0 - K + L = L + (r_0 - K)$.
     - Đang **đầu tư nhận cố định** (thu $r_0$), muốn đổi sang **thu nhập thả nổi** $\implies$ Vào Swap **Trả cố định $K$, Nhận $L$** $\implies \text{Thu nhập ròng} = r_0 - K + L = L + (r_0 - K)$.
   - **Câu hỏi lý thuyết kinh điển:** Swap **KHÔNG HỀ loại bỏ rủi ro tín dụng** của khoản trái phiếu/khoản đầu tư gốc (nhà đầu tư vẫn nắm trái phiếu gốc nên tổ chức phát hành vỡ nợ thì vẫn mất tiền), đồng thời còn tạo thêm **rủi ro tín dụng đối tác của hợp đồng Swap**!

3. **Rủi ro Cơ sở khi Lãi suất Khoản Vay $M$ Khác Lãi suất Tham chiếu Swap $L$ (Basis Risk — Practice Question 13):**
   - Giả sử Sigma có khoản vay $\text{USD }32\text{m}$ trả hàng quý theo lãi suất **$M + 0.85\%$** (ví dụ lãi suất vay ngân hàng thương mại), trong khi hợp đồng Swap trên thị trường lại tham chiếu theo chỉ số **$L$** (ví dụ SOFR) với mức cố định $K = 3.65\%$ (trả $K = 3.65\%$, nhận $L$).
   - Khi ghép Khoản vay + Swap, $M$ và $L$ **KHÔNG triệt tiêu hết cho nhau**:
     $$\text{Combined Annual Borrowing Rate} = (M + 0.85\%) + 3.65\% - L = \mathbf{4.50\% + (M - L)}$$
   - Ví dụ: Quý 1 có $M = 3.40\%, L = 3.10\% \implies M - L = +0.30\% \implies$ Lãi suất gộp $= 4.80\%$ (trả $32\text{m} \times 0.048 \times 0.25 = \text{USD }384{,}000$). Quý 2 có $M = 2.70\%, L = 3.00\% \implies M - L = -0.30\% \implies$ Lãi suất gộp $= 4.20\%$ (trả $\text{USD }336{,}000$).
   - **Kết luận:** Chi phí đi vay **KHÔNG còn cố định tuyệt đối** ở mức $4.50\%$ mà chịu **Rủi ro cơ sở (Basis Risk)** biến động theo chênh lệch $(M - L)$ mỗi quý!

---

### B. Hoán đổi Tiền tệ Cố định – Cố định (Fixed-for-Fixed Currency Swap — L09 Question 11 & Practice Question 12)

Khác hoàn toàn với IRS, một hợp đồng **Currency Swap** trao đổi tiền lãi cố định trên **hai đồng tiền khác nhau** (ví dụ vốn danh nghĩa $N_{\text{USD}}$ và $N_{\text{EUR}}$, thường thiết lập theo tỷ giá giao ngay lúc ký $N_{\text{USD}} = S_0 \cdot N_{\text{EUR}}$) và **CÓ TRAO ĐỔI VỐN GỐC Ở HAI ĐẦU KỲ HẠN**:

1. **Ba Mốc Thời gian Dòng tiền của Swap (Xét doanh nghiệp cần vốn EUR nên đi vay $N_{\text{USD}}$ rồi vào Swap nhận lãi USD, trả lãi EUR):**
   - **Tại ngày khởi tạo ($t = 0$):** Giao vốn gốc USD cho đối tác swap ($-N_{\text{USD}}$) và nhận về vốn gốc EUR ($+N_{\text{EUR}}$). *(Khi cộng gộp với khoản vay ngân hàng $+N_{\text{USD}}$, dòng USD ngày $t=0$ triệt tiêu bằng $0$, doanh nghiệp cầm ròng $+N_{\text{EUR}}$ để kinh doanh!).*
   - **Cuối mỗi năm trung gian ($t = 1, \dots, T-1$):** Swap trả cho doanh nghiệp tiền lãi USD ($+N_{\text{USD}} \cdot r_{\text{swap,USD}}$) và doanh nghiệp trả cho đối tác swap tiền lãi EUR ($-N_{\text{EUR}} \cdot r_{\text{swap,EUR}}$).
   - **Tại ngày đáo hạn ($t = T$):** Trao đổi kỳ lãi cuối cùng **CỘNG VỚI ĐẢO NGƯỢC VỐN GỐC BAN ĐẦU**: doanh nghiệp nhận lại $+N_{\text{USD}}(1 + r_{\text{swap,USD}})$ để trả sạch gốc + lãi vay ngân hàng USD, và chi trả $-N_{\text{EUR}}(1 + r_{\text{swap,EUR}})$ bằng đồng EUR!

2. **Tình huống Nâng cao Ý `c` (Khi Lãi suất Vay Ngân hàng USD Cao hơn Lãi suất USD Nhận từ Swap — L09 Q11c & Practice Q12c):**
   - Giả sử khoản vay gốc là $N_{\text{USD}} = \text{USD }9.6\text{m}$, Swap trả cho công ty $4.50\%$ trên USD ($+\text{USD }432{,}000$/năm) và thu $3.50\%$ trên $\text{EUR }8.0\text{m}$ ($-\text{EUR }280{,}000$/năm), nhưng ngân hàng cho vay USD lại tính lãi **$5.25\%$**/năm ($-\text{USD }504{,}000$/năm).
   - **Chuyện gì xảy ra khi ghép Khoản vay + Swap?**
     - Vốn gốc USD ở $t=0$ và $t=3$ **vẫn triệt tiêu hoàn toàn bằng $0$**.
     - Nghĩa vụ trả bằng EUR vẫn giữ nguyên $-\text{EUR }280{,}000$/năm (và gốc $-\text{EUR }8.0\text{m}$ cuối năm 3).
     - **Tuy nhiên**, mỗi năm công ty còn bị thiếu hụt một khoản tiền lãi USD chưa được phòng hộ (Uncovered annual USD obligation):
       $$\Delta \text{Interest}_{\text{USD}} = 9{,}600{,}000 \times (5.25\% - 4.50\%) = \textbf{USD 72,000/năm}$$
     - Vì chi phí quy đổi khoản $\text{USD }72{,}000$ mỗi năm này sang EUR phụ thuộc vào tỷ giá giao ngay tương lai $S_t$ tại từng năm thanh toán, tổng chi phí tài trợ **KHÔNG CÒN cố định hoàn toàn bằng đồng EUR nữa** (công ty vẫn còn chịu rủi ro tỷ giá phần dư trên dòng tiền lãi thiếu hụt này)!

---

### C. Hợp đồng Hoán đổi Rủi ro Tín dụng (Credit Default Swaps — CDS & Sovereign CDS cho MCQ)

- **Cơ chế bảo hiểm tín dụng:** **Protection Buyer** trả phí định kỳ (CDS spread, tính theo **basis points**: $100\text{ bps} = 1\% = 0.01$; ví dụ $288\text{ bps}$ trên $\text{USD }10\text{m}$ tương ứng phí cả năm $\text{USD }288{,}000$, trả theo quý là $288{,}000 / 4 = \text{USD }72{,}000$/quý nếu chưa xảy ra sự kiện tín dụng). Đổi lại, **Protection Seller** cam kết bồi thường nếu tổ chức tham chiếu (Reference Entity — công ty hoặc chính phủ quốc gia) xảy ra **Sự kiện tín dụng (Credit Event)** như vỡ nợ không thanh toán hoặc tái cơ cấu nợ.
- **Hai phương thức tất toán khi xảy ra Vỡ nợ (với tỷ lệ thu hồi của trái phiếu là $\mathcal{R}$, ví dụ $\mathcal{R} = 40\%$):**
  1. **Tất toán Vật chất (Physical Settlement):** Bên mua bảo hiểm giao trái phiếu đủ điều kiện (đang chỉ đáng giá $\mathcal{R} \cdot N$) cho bên bán bảo hiểm và nhận về đủ **$100\%$ mệnh giá $N$**.
  2. **Tất toán Tiền mặt (Cash Settlement):** Bên mua giữ lại trái phiếu, bên bán chi trả khoản tiền mặt bù đắp tổn thất (thường xác định qua đấu giá):
     $$\text{Cash Settlement Payment} = N (1 - \mathcal{R})$$
     *(Ví dụ $N = \text{USD }10\text{m}$, $\mathcal{R} = 40\% \implies$ Tiền bồi thường $= 10 \times (1 - 0.40) = \text{USD }6\text{m}$).*
- **Bẫy Lý thuyết MCQ Cực Quan Trọng (L09 Cell 20):**
  1. **CDS Spread KHÔNG PHẢI là xác suất vỡ nợ thực tế (NOT a pure default probability)!** CDS spread là **giá của sự bảo hiểm**, nên ngoài xác suất vỡ nợ, nó còn phản ánh: (i) **Tỷ lệ thu hồi kỳ vọng $\mathcal{R}$** (tổn thất khi vỡ nợ $1 - \mathcal{R}$), (ii) **Phần bù rủi ro (Risk premium)** do vỡ nợ thường xảy ra đúng lúc kinh tế suy thoái xấu nhất, và (iii) **Phần bù thanh khoản (Liquidity)**.
  2. CDS chuyển giao rủi ro tín dụng của tổ chức tham chiếu sang bên bán bảo hiểm, nhưng bên mua vẫn chịu **Rủi ro đối tác (Counterparty risk)** nếu chính bên bán CDS mất khả năng thanh toán đúng lúc sự kiện tín dụng nổ ra!

---

# CHƯƠNG 2 — LECTURE 10: THỊ TRƯỜNG QUYỀN CHỌN, CHIẾN LƯỢC, PUT-CALL PARITY, BOUNDS & MÔ HÌNH MERTON (TRỌNG TÂM TÍNH TOÁN #2)

## 2.1. Nền tảng Quyền chọn: Moneyness, Giá trị Nội tại (Intrinsic Value) & Giá trị Thời gian (Time Value)

Khác với Forward/Futures (nơi cả hai bên đều bị trói nghĩa vụ), **Quyền chọn (Option)** tách bạch hoàn toàn **Quyền (Right)** và **Nghĩa vụ (Obligation)**:
- **Người Mua / Nắm giữ (Holder — Long):** Trả một khoản phí ban đầu (**Premium**) để sở hữu **quyền (nhưng không có nghĩa vụ)** mua (**Call**) hoặc bán (**Put**) tài sản cơ sở tại **Giá thực hiện (Strike / Exercise Price $K$)**. Vì có quyền bỏ không thực hiện nếu bất lợi, **Payoff lúc đáo hạn của người Mua không bao giờ âm ($\ge 0$)**.
- **Người Bán / Phát hành (Writer — Short):** Thu phí Premium đầu kỳ và gánh chịu **nghĩa vụ bắt buộc** phải bán (Short Call) hoặc mua (Short Put) tại giá $K$ nếu người mua yêu cầu thực hiện $\implies$ **Payoff lúc đáo hạn luôn $\le 0$**.
- **Kiểu thực hiện:** **Châu Âu (European)** chỉ được thực hiện đúng ngày đáo hạn $T$; **Kiểu Mỹ (American)** được quyền thực hiện tại bất kỳ thời điểm nào từ lúc mua đến hết ngày $T$ ($0 \le t \le T$).

### 1. Phân loại Trạng thái Tiền (Moneyness) & Giá trị Nội tại (Intrinsic Value)
Giả sử giá cổ phiếu hiện tại là $S_t$ và giá thực hiện là $K$:

| Trạng thái (Moneyness) | Quyền chọn Mua (Call Option) | Quyền chọn Bán (Put Option) | Ý nghĩa Trực quan nếu Thực thi Ngay tại $S_t$ |
| :--- | :---: | :---: | :--- |
| **In-the-Money (ITM)** | $S_t > K$ | $S_t < K$ | Thực thi ngay tạo ra dòng tiền dương. |
| **At-the-Money (ATM)** | $S_t = K$ | $S_t = K$ | Giá thị trường bằng đúng giá thực hiện. |
| **Out-of-the-Money (OTM)** | $S_t < K$ | $S_t > K$ | Thực thi ngay sẽ bất lợi $\implies$ không thực thi. |
| **Giá trị Nội tại (Intrinsic Value)** | $\max(S_t - K, \, 0)$ | $\max(K - S_t, \, 0)$ | Luôn $\ge 0$! (Bằng $0$ khi ATM hoặc OTM). |

> [!NOTE]
> **Bẫy khái niệm MCQ:** Trạng thái **In-the-Money (ITM)** chỉ so sánh thuần túy $S_t$ với $K$, **HOÀN TOÀN KHÔNG trừ phí quyền chọn (Premium)**! Một quyền chọn Call có $K = 65$, mua với phí $C = 8$, khi đáo hạn ở $S_T = 70$ vẫn là **In-the-Money** (Payoff $= +5 > 0$, nên bắt buộc phải thực thi để gỡ vốn!), dù tổng lợi nhuận ròng của người mua là âm ($\text{Profit} = 5 - 8 = -3$).

### 2. Giá trị Thời gian (Time Value) & Giải Mã Sâu Sắc Tại Sao Time Value Có Thể ÂM!

Mọi quyền chọn đang giao dịch ở giá thị trường $V_t$ đều được phân rã thành:
$$\text{Option Price } (V_t) = \text{Intrinsic Value} + \text{Time Value} \quad \Longleftrightarrow \quad \text{Time Value} = V_t - \text{Intrinsic Value}$$

Thông thường học viên hay lầm tưởng *"Time Value luôn dương vì còn thời gian là còn cơ hội"*. Điều này **ĐÚNG với mọi Quyền chọn Kiểu Mỹ** ($V_A \ge \text{Intrinsic Value} \implies \text{Time Value}_A \ge 0$), nhưng **SAI đối với Quyền chọn Châu Âu** trong hai trường hợp kinh điển sau (rất hay hỏi ở cả tự luận lẫn MCQ — L10 Question 8, Cell 20 & Extra Session Cell 8):

1. **Trường hợp 1: Quyền chọn Bán Châu Âu Rất Sâu Trong Tiền (Deep-ITM European Put, $S_0 \ll K$, lãi suất $r > 0$):**
   - Xuất phát từ đẳng thức Put-Call Parity trên cổ phiếu không cổ tức: $P_E = C_E + PV(K) - S_0$.
   - Trừ đi giá trị nội tại của Put là $(K - S_0)$, ta được công thức chính xác tuyệt đối của Time Value:
     $$\text{Time Value}(P_E) = P_E - (K - S_0) = \underbrace{C_E}_{\text{Giá trị bảo hiểm hồi phục}} - \underbrace{\big[K - PV(K)\big]}_{\text{Tiền lãi mất đi do bị giam đến ngày } T}$$
   - **Bản chất kinh tế:** Khi cổ phiếu đã sập quá sâu ($S_0$ rất nhỏ so với $K$), xác suất nó tăng ngược vượt qua $K$ gần như bằng $0$ ($C_E \approx 0$), và dư địa giảm giá thêm cũng bị chặn bởi đáy $S \ge 0$. Người cầm **European Put** rất muốn bán cổ phiếu ngay để lấy tiền mặt $K$ đem gửi ngân hàng hưởng lãi $[K - PV(K)]$, nhưng vì luật Châu Âu **cấm thực thi trước ngày $T$**, họ bị thiệt mất khoản lãi này! Khi $C_E < K - PV(K)$, ta có **$\text{Time Value}(P_E) < 0 \iff P_E < K - S_0$**! *(Và không ai ăn được Arbitrage từ việc $P_E < K - S_0$ vì không được phép thực thi sớm — Practice Q34b!).*

2. **Trường hợp 2: Quyền chọn Mua Châu Âu Rất Sâu Trong Tiền trên Cổ phiếu/Chỉ số Trả Cổ tức Lớn (Deep-ITM European Call with High Dividends — L10 Question 8):**
   - Từ Put-Call Parity có cổ tức $D$: $C_E = S_0 - PV(D) - PV(K) + P_E$.
   - Trừ đi giá trị nội tại $(S_0 - K)$:
     $$\text{Time Value}(C_E) = C_E - (S_0 - K) = P_E + \big[K - PV(K)\big] - PV(D)$$
   - Khi cổ tức sắp chia quá lớn làm **$PV(D) > P_E + [K - PV(K)]$**, người giữ European Call bất lực nhìn cổ phiếu bị điều chỉnh giảm giá mạnh sau ngày chia cổ tức mà không được thực thi sớm để nhận cổ tức $\implies$ **$\text{Time Value}(C_E) < 0 \iff C_E < S_0 - K$**!
   - *Minh họa L10 Q8:* Chỉ số Iota $S_0 = 1{,}800$, Call Châu Âu 1 năm $K = 1{,}200$ có Time Value âm ($C < S_0 - K$), $r = 5\%$ EAR, cổ tức $D$ trả cuối năm:
     $$\frac{D}{1.05} > P + 1{,}200 - \frac{1{,}200}{1.05} \implies D > 1.05 P + 0.05(1{,}200) = 1.05 P + 60 \ge 60 \implies \frac{D}{S_0} > \frac{60}{1{,}800} = 3.33\%!$$

---

## 2.2. Bốn Vị thế Quyền chọn Gốc (4 Basic Positions) & Quy ước Hợp đồng

> [!IMPORTANT]
> **Quy ước Chuẩn trong Môn BFIN (Đọc kỹ hướng dẫn đầu Practice L10):**
> 1. **Hệ số nhân hợp đồng (Contract Multiplier):** Mặc định **1 hợp đồng quyền chọn tiêu chuẩn đại diện cho $100$ cổ phiếu** ($1\text{ contract} = 100\text{ shares}$), trong khi phí quyền chọn ($C, P$) luôn được **yết giá trên 1 cổ phiếu (per share)**. Ví dụ $C = \text{USD }6.20$/cổ phiếu $\implies$ Mua 1 hợp đồng tốn $\text{USD }620$; muốn phòng hộ cho $1{,}000$ cổ phiếu cần giao dịch **$10$ hợp đồng**!
> 2. **Quy ước tính Profit chiến lược:** Theo chuẩn bài giảng Lecture 10, $\text{Profit} = \text{Terminal Payoff} - \text{Net Initial Cost}$ (không cộng lãi suất lên phí ban đầu trừ khi đề yêu cầu dựng vị thế tự tài trợ zero-cost có đi vay/cho vay tường minh).

| Vị thế Cơ bản | Payoff tại $T$ (per share) | Lợi nhuận Ròng (Profit per share) | Lãi Tối đa (Max Profit) | Lỗ Tối đa (Max Loss) | Điểm Hòa vốn ($S_T^*$) | Kỳ vọng Thị trường |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Long Call** | $\max(S_T - K, 0)$ | $\max(S_T - K, 0) - C$ | **Vô hạn ($\infty$)** | $C$ (phí đã trả) | $K + C$ | Giá tăng mạnh (Bullish) |
| **2. Short Call** | $-\max(S_T - K, 0)$ | $C - \max(S_T - K, 0)$ | $C$ (phí thu về) | **Vô hạn ($\infty$)** | $K + C$ | Giá đi ngang / giảm |
| **3. Long Put** | $\max(K - S_T, 0)$ | $\max(K - S_T, 0) - P$ | $K - P$ *(tại $S_T=0$)* | $P$ (phí đã trả) | $K - P$ | Giá giảm mạnh (Bearish) |
| **4. Short Put** | $-\max(K - S_T, 0)$ | $P - \max(K - S_T, 0)$ | $P$ (phí thu về) | **$K - P$** *(Payoff lỗ tối đa là $K$ tại $S_T=0$!)* | $K - P$ | Giá đi ngang / tăng |

*(Chú ý câu hỏi kinh điển L10 Q3: So sánh rủi ro tồi tệ nhất giữa Naked Short Call và Naked Short Put cùng strike $K$: **Short Call nguy hiểm hơn nhiều** vì giá cổ phiếu tăng không có trần nên lỗ là **vô hạn**, còn Short Put chỉ lỗ khi giá giảm nhưng giá cổ phiếu không thể âm ($S_T \ge 0$) nên payoff lỗ tối đa bị chặn ở mức $-K$!).*

---

## 2.3. Cẩm nang Toàn diện 10 Chiến lược Quyền chọn Kinh điển (Master Strategy Handbook)

Để giải mọi bài toán chiến lược trong 60 giây, hãy nắm vững cấu trúc lắp ghép và bảng tra cứu toàn năng của đủ 10 chiến lược dưới đây (các quyền chọn trong cùng một chiến lược đều có cùng ngày đáo hạn $T$, với quy ước các mức giá thực hiện $K_L < K_M < K_H$):

### Nhóm A: Kết hợp Cổ phiếu Cơ sở & Quyền chọn (Hedging / Yield Enhancement)

#### 1. Protective Put (Quyền chọn Bán Bảo hộ — Bảo hiểm Danh mục)
- **Cấu trúc:** Mua 1 cổ phiếu ($S_0$) + Mua 1 Put ($K$, phí $P$). Chi phí ròng ban đầu: $S_0 + P$.
- **Payoff (Giá trị danh mục tại $T$):**
  - Nếu $S_T \le K$: $S_T + (K - S_T) = \mathbf{K}$ *(Sàn giá trị bảo hiểm tuyệt đối!)*.
  - Nếu $S_T > K$: $S_T + 0 = \mathbf{S_T}$ *(Giữ trọn 100% tiềm năng tăng giá!)*.
- **Profit:** $\max(S_T, K) - (S_0 + P)$.
  - **Max Loss:** $(S_0 + P) - K = S_0 - K + P$ (xảy ra khi $S_T \le K$). *(Lưu ý L10 C13: Sàn $K$ bảo vệ giá trị cuối kỳ không tụt dưới $K$, chứ không có nghĩa là không thể lỗ so với tổng vốn bỏ ra ban đầu $S_0 + P$!).*
  - **Max Profit:** Vô hạn ($\infty$). **Breakeven:** $S_T^* = S_0 + P$.

#### 2. Covered Call (Bán Quyền chọn Mua Có Bảo chứng — Tăng thu nhập khi thị trường đi ngang)
- **Cấu trúc:** Mua 1 cổ phiếu ($S_0$) + Bán (Write) 1 Call ($K$, thu phí $C$). Chi phí ròng ban đầu: $S_0 - C$.
- **Payoff (Giá trị danh mục tại $T$):**
  - Nếu $S_T \le K$: $S_T - 0 = \mathbf{S_T}$ *(Vẫn gánh chịu thua lỗ nặng nếu cổ phiếu lao dốc về $0$!)*.
  - Nếu $S_T > K$: $S_T - (S_T - K) = \mathbf{K}$ *(Bị khóa trần giá bán tại $K$, hy sinh toàn bộ phần tăng vượt trên $K$)*.
- **Profit:** $\min(S_T, K) - (S_0 - C)$.
  - **Max Terminal Value:** $K$. **Max Profit:** $K - (S_0 - C) = (K - S_0) + C$ (đạt được tại mọi $S_T \ge K$).
  - **Max Loss:** $S_0 - C$ (khi $S_T = 0$). **Breakeven:** $S_T^* = S_0 - C$.
- *Mẹo giải ngược nhanh (Practice Q16):* Alpha mua $100$ cổ phiếu giá $48$, bán 1 hợp đồng Call $K = 52$; tại $S_T = 55 > 52$, tổng lãi là $\text{USD }650$ ($\text{USD }6.50$/cp) $\implies \text{Max Profit/sh} = (52 - 48) + C = 6.50 \implies C = \text{USD }2.50$/cp; chi phí ròng ban đầu $= 48 - 2.50 = \text{USD }45.50$/cp ($\text{USD }4{,}550$), hòa vốn tại $S_T^* = \text{USD }45.50$!

---

### Nhóm B: Chênh lệch Giá Theo Chiều Dọc (Vertical Spreads — Đặt cược Xu hướng với Chi phí & Rủi ro Hữu hạn)

#### 3. Bull Call Spread (Debit) & 4. Bull Put Spread (Credit) — Đặt cược Giá Tăng Vừa phải ($K_L < K_H$)
- **Bull Call Spread (Chiến lược chuẩn trên lớp):** **Mua Call $K_L$ + Bán Call $K_H$**. Vì $C(K_L) > C(K_H)$, bạn trả phí ròng đầu kỳ $d = C(K_L) - C(K_H) > 0$ (*Net Debit*):
  - $S_T \le K_L$: Payoff $= 0 \implies \text{Profit} = -d$ (**Max Loss $= d$**).
  - $K_L < S_T < K_H$: Payoff $= S_T - K_L \implies \text{Profit} = S_T - K_L - d$ (**Breakeven $S_T^* = K_L + d$**).
  - $S_T \ge K_H$: Payoff $= (S_T - K_L) - (S_T - K_H) = K_H - K_L \implies$ **Max Profit $= (K_H - K_L) - d$**.
- **Bull Put Spread (Biến thể bằng Put):** **Mua Put $K_L$ + Bán Put $K_H$**. Vì $P(K_H) > P(K_L)$, bạn **thu tiền ròng ngay từ đầu** $c = P(K_H) - P(K_L) > 0$ (*Net Credit*), nhưng tại đáo hạn sẽ có nghĩa vụ chi trả nếu giá giảm:
  - $S_T \le K_L$: Payoff $= -(K_H - K_L) \implies$ **Max Loss $= (K_H - K_L) - c$**.
  - $K_L < S_T < K_H$: Payoff $= -(K_H - S_T) \implies \text{Profit} = c - (K_H - S_T)$ (**Breakeven $S_T^* = K_H - c$**).
  - $S_T \ge K_H$: Cả hai Put hết hạn vô giá trị, Payoff $= 0 \implies$ **Max Profit $= c$**.

#### 5. Bear Put Spread (Debit) & 6. Bear Call Spread (Credit) — Đặt cược Giá Giảm Vừa phải ($K_L < K_H$)
- **Bear Put Spread (Chiến lược chuẩn trên lớp & Practice Q17):** **Mua Put giá cao $K_H$ + Bán Put giá thấp $K_L$**. Trả phí ròng đầu kỳ $d = P(K_H) - P(K_L) > 0$:
  - $S_T \le K_L$: Payoff $= (K_H - S_T) - (K_L - S_T) = K_H - K_L \implies$ **Max Profit $= (K_H - K_L) - d$**.
  - $K_L < S_T < K_H$: Payoff $= K_H - S_T \implies \text{Profit} = K_H - S_T - d$ (**Breakeven $S_T^* = K_H - d$**).
  - $S_T \ge K_H$: Payoff $= 0 \implies$ **Max Loss $= d$**.
  - *Mẹo giải ngược nhanh (Practice Q17):* Mua 1 Put contract $K_H = 64$ giá $7.10$, bán 1 Put contract $K_L = 56$, biết Max Loss $= \text{USD }280$ ($\text{USD }2.80$/cp) $\implies d = 7.10 - P(56) = 2.80 \implies P(56) = \text{USD }4.30$/cp; Breakeven $= 64 - 2.80 = \text{USD }61.20$; Max Profit $= 100 \times (8 - 2.80) = \text{USD }520$!
- **Bear Call Spread (Biến thể bằng Call):** **Bán Call $K_L$ + Mua Call $K_H$**. Thu tiền ròng đầu kỳ $c = C(K_L) - C(K_H) > 0$:
  - $S_T \le K_L$: Payoff $= 0 \implies$ **Max Profit $= c$**.
  - $S_T \ge K_H$: Payoff $= -(K_H - K_L) \implies$ **Max Loss $= (K_H - K_L) - c$**. **Breakeven:** $S_T^* = K_L + c$.

---

### Nhóm C: Chiến lược Giao dịch Độ biến động (Volatility Strategies — Đặt cược Biến động Lớn hoặc Đứng Yên)

#### 7. Long / Short Straddle (Cùng Strike $K$) & 8. Long / Short Strangle (Khác Strike $K_L < K_H$)
- **Long Straddle:** **Mua 1 Call $(K)$ + Mua 1 Put $(K)$**, tổng phí trả $d_{\text{straddle}} = C(K) + P(K)$.
  - Payoff chữ **V nhọn** tại đỉnh $K$: $|S_T - K|$.
  - **Max Loss:** $d_{\text{straddle}}$ (nếu cổ phiếu đứng im đúng tại $S_T = K$).
  - **Hai điểm hòa vốn:** $S_{T,\text{low}}^* = K - d_{\text{straddle}}$ và $S_{T,\text{high}}^* = K + d_{\text{straddle}}$.
- **Long Strangle:** **Mua 1 Put OTM $(K_L)$ + Mua 1 Call OTM $(K_H)$** với $K_L < K_H$, tổng phí trả $d_{\text{strangle}} = P(K_L) + C(K_H)$.
  - Payoff hình **đáy chậu bằng phẳng**: Bằng $K_L - S_T$ nếu $S_T \le K_L$; bằng **$0$ trên toàn đoạn $[K_L, K_H]$**; bằng $S_T - K_H$ nếu $S_T \ge K_H$.
  - **Max Loss:** $d_{\text{strangle}}$ (xảy ra trên toàn vùng $K_L \le S_T \le K_H$).
  - **Hai điểm hòa vốn:** $S_{T,\text{low}}^* = K_L - d_{\text{strangle}}$ và $S_{T,\text{high}}^* = K_H + d_{\text{strangle}}$.
- *(Ngược lại, **Short Straddle / Short Strangle** là bán cả Call lẫn Put để thu phí đầu kỳ khi tin rằng thị trường lặng sóng, nhưng gánh rủi ro **lỗ vô hạn** nếu giá bứt phá mạnh ở chiều tăng!).*

> [!TIP]
> **ĐÁNH ĐỔI KINH ĐIỂN GIỮA LONG STRADDLE VÀ LONG STRANGLE (Practice Question 19):**  
> Vì mua các quyền chọn OTM ($K_L < S_0 < K_H$), **Long Strangle luôn có chi phí đầu tư ban đầu RẺ HƠN và lỗ tối đa THẤP HƠN Long Straddle** ($d_{\text{strangle}} < d_{\text{straddle}}$).  
> **Cái giá phải trả (Trade-off):** Vì $C(K) - C(K_H) < K - K_H$ (theo giới hạn giá spread!), điểm hòa vốn của Strangle **LUÔN NẰM XA HƠN** Straddle ở cả hai phía! Nghĩa là cổ phiếu phải biến động mạnh hơn nữa thì Strangle mới bắt đầu có lãi, và ở mọi kịch bản biến động cực lớn ($S_T \le K_L$ hoặc $S_T \ge K_H$), lợi nhuận ròng của Strangle luôn kém hơn Straddle!

---

#### 9. Butterfly Spread (Cánh bướm) & KỸ THUẬT "ĐỘ DỐC $\Delta\text{SLOPE}$" THIẾT KẾ MỌI HÀM PAYOFF TRONG 30 GIÂY!
- **Long Symmetric Butterfly chuẩn ($K_L < K_M < K_H$ với $K_M = \frac{K_L + K_H}{2}$, đặt $\Delta K = K_M - K_L = K_H - K_M$):**
  - **Cấu trúc bằng Call:** **Mua 1 Call $(K_L)$ $-$ Bán 2 Call $(K_M)$ $+$ Mua 1 Call $(K_H)$** (hoặc dùng Put với y hệt hệ số $+1 P(K_L) - 2 P(K_M) + 1 P(K_H)$!). Chi phí ròng: $d = C_L - 2C_M + C_H > 0$.
  - **Payoff hình mái lều tam giác:** Bằng $0$ khi $S_T \le K_L$ hoặc $S_T \ge K_H$; tăng tuyến tính $S_T - K_L$ trên $[K_L, K_M]$ đạt đỉnh cao nhất **$\Delta K$** tại $S_T = K_M$; giảm tuyến tính $K_H - S_T$ trên $[K_M, K_H]$.
  - **Max Profit:** $\Delta K - d$ (tại $S_T = K_M$). **Max Loss:** $d$ (khi giá đi quá xa ra ngoài $[K_L, K_H]$). **Hai điểm hòa vốn:** $K_L + d$ và $K_H - d$.

> [!IMPORTANT]
> **VŨ KHÍ TỐI THƯỢNG: KỸ THUẬT "BƯỚC NHẢY ĐỘ DỐC ($\Delta\text{SLOPE}$)" GIẢI MỌI BÀI TỰ LUẬN DỰNG PAYOFF BẰNG CALL (Practice Question 21):**  
> Bất kỳ hàm payoff tuyến tính từng khúc nào bằng $0$ ở bên trái điểm gãy nhỏ nhất ($S_T \le K_1$) đều dựng được **chỉ bằng các quyền chọn Call** theo quy tắc 3 bước siêu tốc:
> 1. Tính **độ dốc (Slope $= \frac{\Delta \text{Payoff}}{\Delta S_T}$)** của hàm mục tiêu trên từng đoạn giá từ trái sang phải.
> 2. Mỗi quyền chọn mua $C(K_i)$ có độ dốc bằng $0$ bên trái $K_i$ và bằng $+1$ bên phải $K_i$ (nó làm tăng độ dốc thêm $+1$ kể từ mốc $K_i$ trở đi!).
> 3. Do đó, số lượng quyền chọn $C(K_i)$ cần mua/bán tại mỗi điểm gãy $K_i$ chính bằng **Độ dốc đoạn ngay SAU $K_i$ trừ đi Độ dốc đoạn ngay TRƯỚC $K_i$**:
>    $$\boxed{n_i = \text{Slope}_{\text{phải } K_i} - \text{Slope}_{\text{trái } K_i}}$$
>
> **Áp dụng ngay vào Practice Question 21 (Theta):** Mục tiêu Payoff bằng $0$ với $S_T \le 80$; tăng tuyến tính lên $10$ tại $S_T = 90$; giảm tuyến tính về $0$ tại $S_T = 100$ và giữ bằng $0$ với $S_T \ge 100$:
> - Đoạn $S_T < 80$: $\text{Slope}_0 = 0$.
> - Đoạn $(80, 90)$: $\text{Slope}_1 = \frac{10 - 0}{90 - 80} = +1 \implies n_{80} = (+1) - 0 = \mathbf{+1\text{ Call }(K=80)}$.
> - Đoạn $(90, 100)$: $\text{Slope}_2 = \frac{0 - 10}{100 - 90} = -1 \implies n_{90} = (-1) - (+1) = \mathbf{-2\text{ Calls }(K=90)}$.
> - Đoạn $S_T > 100$: $\text{Slope}_3 = 0 \implies n_{100} = 0 - (-1) = \mathbf{+1\text{ Call }(K=100)}$.
> - Với giá $C(80)=13, C(90)=7, C(100)=3$: Chi phí ban đầu $d = 13 - 2(7) + 3 = \text{USD }2$; Max Profit $= 10 - 2 = \text{USD }8$; Max Loss $= \text{USD }2$; Hòa vốn tại $80 + 2 = \text{USD }82$ và $100 - 2 = \text{USD }98$!  
> *(Thậm chí nếu đề ra Butterfly bất đối xứng, ví dụ đỉnh $10$ nằm tại $S_T = 85$ giữa $80$ và $100$: $\text{Slope}_1 = \frac{10}{5} = +2$, $\text{Slope}_2 = \frac{-10}{15} = -\frac{2}{3} \implies +2 C(80) - \frac{8}{3} C(85) + \frac{2}{3} C(100)$ — giải xong trong 15 giây!).*

---

#### 10. Collar (Vòng cổ Bảo vệ Danh mục) & Box Spread (Hộp Chênh lệch Lãi suất)

- **Collar ($+S_0 + P(K_L) - C(K_H)$ với $K_L < K_H$ — Minh họa từ Practice Question 24):**
  - **Bản chất:** Nhà đầu tư đang giữ cổ phiếu muốn mua Put $(K_L)$ để khóa **sàn giá trị tối thiểu $K_L$**, nhưng phí Put quá đắt vượt quá ngân sách cho phép $\implies$ **Bán đi 1 Call $(K_H)$** để lấy phí thu được tài trợ một phần (hoặc toàn bộ — **Zero-Cost Collar** khi $P(K_L) = C(K_H)$) cho phí mua Put!
  - **Chi phí ròng cho quyền chọn:** $P(K_L) - C(K_H)$ (tổng vốn cả cổ phiếu là $S_0 + P(K_L) - C(K_H)$).
  - **Giá trị danh mục lúc đáo hạn:** Bị kẹp trong hành lang **$[K_L, \, K_H]$**: bằng **$K_L$** nếu $S_T \le K_L$; bằng **$S_T$** nếu $K_L < S_T < K_H$; và bị chặn trần tại **$K_H$** nếu $S_T \ge K_H$ (đánh đổi phần tăng giá vượt trên $K_H$ để đổi lấy bảo hiểm giá rẻ!).
  - *Minh họa Practice Q24:* Mu giữ $1{,}000$ cổ phiếu giá $50$, muốn tổng giá trị đáo hạn $\ge \text{USD }50{,}000$ ($\implies$ bắt buộc sàn $K_L \ge 50$, nên phải mua $10$ hợp đồng Put $K=50$ giá $\text{USD }5.50$/cp tốn $\text{USD }5{,}500$), nhưng ngân sách phí tối đa chỉ có $\text{USD }2{,}000$ $\implies$ Phải bán kèm $10$ hợp đồng Call $K_H = 56$ giá $\text{USD }4.00$/cp (thu $\text{USD }4{,}000$), chi phí quyền chọn ròng giảm còn $5{,}500 - 4{,}000 = \text{USD }1{,}500 \le \text{USD }2{,}000$! Tiết kiệm $\text{USD }4{,}000$ phí nhưng chấp nhận trần giá trị danh mục tại $\text{USD }56{,}000$.

- **Long Box Spread ($[C(K_L) - C(K_H)] + [P(K_H) - P(K_L)]$ — L10 Cell 53):**
  - **Cấu trúc:** Ghép 1 **Bull Call Spread** $+[C(K_L) - C(K_H)]$ với 1 **Bear Put Spread** $+[P(K_H) - P(K_L)]$ trên quyền chọn Châu Âu.
  - **Payoff kỳ diệu tại $T$:**
    - Nếu $S_T \le K_L$: $0 + (K_H - K_L) = \mathbf{K_H - K_L}$.
    - Nếu $K_L < S_T < K_H$: $(S_T - K_L) + (K_H - S_T) = \mathbf{K_H - K_L}$.
    - Nếu $S_T \ge K_H$: $(K_H - K_L) + 0 = \mathbf{K_H - K_L}$.
  - **Định giá Không Arbitrage:** Vì Box Spread Châu Âu trả chính xác số tiền cố định $\Delta K = K_H - K_L$ trong **MỌI trạng thái tự nhiên**, nó hoàn toàn tương đương một **Trái phiếu Zero-Coupon phi rủi ro mệnh giá $K_H - K_L$**! Do đó giá hợp lý hôm nay bắt buộc phải bằng:
    $$\boxed{V_0(\text{Box}) = \big[C(K_L) - C(K_H)\big] + \big[P(K_H) - P(K_L)\big] = PV(K_H - K_L)}$$
    *(Nếu giá thị trường của Box rẻ hơn $PV(K_H - K_L)$, mua Box và vay $PV(K_H - K_L)$; nếu đắt hơn, bán Box và gửi tiết kiệm $PV(K_H - K_L)$!).*

### Bảng Tóm tắt Siêu Tốc 10 Chiến lược Quyền chọn (Đơn vị: trên 1 cổ phiếu)

| # | Chiến lược | Cấu trúc Vị thế | Chi phí Ròng Đầu kỳ ($d$ / $-c$) | Max Profit | Max Loss | Điểm Hòa vốn ($S_T^*$) |
| :-: | :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | **Protective Put** | $+S_0 + P(K)$ | $S_0 + P$ | $\infty$ | $S_0 - K + P$ | $S_0 + P$ |
| 2 | **Covered Call** | $+S_0 - C(K)$ | $S_0 - C$ | $K - S_0 + C$ | $S_0 - C$ | $S_0 - C$ |
| 3 | **Bull Call Spread** | $+C(K_L) - C(K_H)$ | $d = C_L - C_H > 0$ | $(K_H - K_L) - d$ | $d$ | $K_L + d$ |
| 4 | **Bull Put Spread** | $+P(K_L) - P(K_H)$ | Thu $c = P_H - P_L > 0$ | $c$ | $(K_H - K_L) - c$ | $K_H - c$ |
| 5 | **Bear Put Spread** | $+P(K_H) - P(K_L)$ | $d = P_H - P_L > 0$ | $(K_H - K_L) - d$ | $d$ | $K_H - d$ |
| 6 | **Bear Call Spread** | $-C(K_L) + C(K_H)$ | Thu $c = C_L - C_H > 0$ | $c$ | $(K_H - K_L) - c$ | $K_L + c$ |
| 7 | **Long Straddle** | $+C(K) + P(K)$ | $d = C + P$ | $\infty$ *(tăng)* / $K-d$ *(giảm)* | $d$ | $K - d$ và $K + d$ |
| 8 | **Long Strangle** | $+P(K_L) + C(K_H)$ | $d = P_L + C_H$ | $\infty$ *(tăng)* / $K_L-d$ *(giảm)* | $d$ | $K_L - d$ và $K_H + d$ |
| 9 | **Long Butterfly** | $+C_L - 2C_M + C_H$ | $d = C_L - 2C_M + C_H$ | $(K_M - K_L) - d$ | $d$ | $K_L + d$ và $K_H - d$ |
| 10 | **Collar** | $+S_0 + P(K_L) - C(K_H)$ | $S_0 + P_L - C_H$ | $K_H - (S_0 + P_L - C_H)$ | $(S_0 + P_L - C_H) - K_L$ | $S_0 + P_L - C_H$ |

---

## 2.4. Ngang giá Quyền chọn Mua – Bán (Put-Call Parity) & Hợp đồng Kỳ hạn Tổng hợp (Synthetic Forward)

### 1. Chứng minh Kinh tế & Ba Dạng Phương trình Chuẩn (CHỈ ÁP DỤNG CHO QUYỀN CHỌN CHÂU ÂU CÙNG $K, T$)

Xét hai danh mục bảo hiểm danh mục đầu tư tại $t=0$ và giữ tới ngày đáo hạn $T$ trên cổ phiếu không trả cổ tức:
- **Danh mục A — Protective Put ($S_0 + P$):** Khi $S_T \le K$ trả $S_T + (K - S_T) = K$; khi $S_T > K$ trả $S_T + 0 = S_T$.
- **Danh mục B — Fiduciary Call ($C + PV(K)$):** Trái phiếu phi rủi ro trả $K$ lúc đáo hạn. Khi $S_T \le K$ trả $0 + K = K$; khi $S_T > K$ trả $(S_T - K) + K = S_T$.

Vì cả hai danh mục đều trả chính xác **$\max(S_T, K)$** trong mọi kịch bản của $S_T$, Quy luật Một Giá bắt buộc chi phí của chúng tại $t=0$ phải bằng nhau tuyệt đối:

1. **Cổ phiếu không trả cổ tức:**
   $$\boxed{C + PV(K) = S_0 + P \quad \Longleftrightarrow \quad C - P = S_0 - PV(K)}$$
   *(Với EAR: $PV(K) = \dfrac{K}{(1+r)^T}$; với ghép lãi liên tục: $PV(K) = K e^{-rT}$; nếu đề hỏi **Discount factor $DF$** như Practice Q18 thì $DF = \dfrac{S_0 + P - C}{K}$ rồi kiểm tra $DF \le 1 \iff r \ge 0$!).*

2. **Cổ phiếu trả cổ tức tiền mặt rời rạc trước đáo hạn ($PV(D)$):**
   $$\boxed{C - P = S_0 - PV(D) - PV(K)}$$

3. **Chỉ số cổ phiếu có tỷ suất cổ tức liên tục $q$:**
   $$\boxed{C - P = S_0 e^{-qT} - K e^{-rT}}$$

---

### 2. Dựng Synthetic Long Forward Không Tốn Vốn Ban Đầu & Arbitrage Giữa Option và Forward (Practice Question 15 — Upsilon)

Đây là dạng bài phối hợp cực hay giữa Lecture 09 và Lecture 10! Đề bài **KHÔNG CHO GIÁ CỔ PHIẾU GIAO NGAY $S_0$**, mà chỉ cho giá Call $C(K)$, giá Put $P(K)$ và giá hợp đồng Forward thực tế trên thị trường $F_{\text{mkt}}$:

- **Bước 1 — Ghép Payoff Kỳ hạn bằng Quyền chọn:** Mua 1 Call $(K)$ và Bán 1 Put $(K)$ cùng kỳ hạn tạo ra payoff tại $T$ là:
  $$\max(S_T - K, 0) - \max(K - S_T, 0) = S_T - K$$
  Tuy nhiên, vị thế $+C - P$ này tốn chi phí ròng tại $t=0$ là **$C - P$** (nếu $C > P$; hoặc thu tiền nếu $C < P$), trong khi một hợp đồng Forward thực thụ phải có **chi phí ban đầu bằng $0$**!
- **Bước 2 — Biến thành Vị thế Zero-Initial-Cost bằng Vay/Cho vay:**
  - Tại $t=0$, **Vay đúng số tiền $(C - P)$** ở lãi suất phi rủi ro $r$ (nếu $C < P$ thì đem gửi tiết kiệm $P - C$) $\implies$ Dòng tiền ròng tại $t=0$ bằng **$0$ tuyệt đối**!
  - Tại $t=T$, phải trả gốc và lãi khoản vay là $(C - P)(1 + r)^T$. Tổng dòng tiền cuối kỳ trở thành:
    $$(S_T - K) - (C - P)(1 + r)^T = S_T - \underbrace{\Big[K + (C - P)(1 + r)^T\Big]}_{K_{\text{imp}}}$$
- **Bước 3 — Giá Giao Hàng Kỳ Hạn Ngụ Ý ($K_{\text{imp}}$) & Chiến thuật Arbitrage:**
  $$\boxed{K_{\text{imp}} = K + (C - P)(1 + r)^T \quad \text{(hoặc } K + (C - P)e^{rT} \text{ nếu lãi liên tục)}}$$
  *(Kiểm chứng: Thay $C - P = S_0 - K/(1+r)^T$ vào sẽ thấy $K_{\text{imp}} = K + S_0(1+r)^T - K = S_0(1+r)^T = F^*$!).*
  - Nếu **$K_{\text{imp}} < F_{\text{mkt}}$**: Mua hàng qua Synthetic Forward rẻ hơn ($K_{\text{imp}}$), Bán hàng qua Forward thị trường đắt hơn ($F_{\text{mkt}}$) $\implies$ Lãi chắc chắn tại $T$ là **$F_{\text{mkt}} - K_{\text{imp}}$** trên mỗi cổ phiếu!
  - Nếu **$K_{\text{imp}} > F_{\text{mkt}}$**: Đảo ngược hoàn toàn (Mua Forward thị trường, Bán Call + Mua Put + Gửi tiết kiệm $C - P$).

**Ví dụ Mẫu Trọn Vẹn (Practice Question 15 — Upsilon, cho $1{,}000$ cổ phiếu = $10$ hợp đồng Option):**  
Cho $K = 70, C = 6.20, P = 3.80, T = 0.5\text{ năm}, r = 4\%\text{ EAR}$, Forward 1,000 cổ phiếu yết giá $F_{\text{mkt}} = \text{USD }73.20$/cp:
- Giá kỳ hạn ngụ ý từ quyền chọn: $K_{\text{imp}} = 70 + (6.20 - 3.80)(1.04)^{0.5} = 70 + 2.40(1.019804) = \mathbf{\text{USD }72.447529/\text{cp}} < 73.20$.
- **Thực thi Arbitrage cho $1{,}000$ cổ phiếu:** Mua **10 hợp đồng Call**, Bán **10 hợp đồng Put**, Vay $1{,}000 \times 2.40 = \text{USD }2{,}400$, và Bán (Short) 1 hợp đồng Forward ($1{,}000$ cp tại $73.20$):

| Giao dịch (Cho 1,000 cổ phiếu) | Hôm nay ($t=0$) | Đáo hạn nếu $S_T \le 70$ | Đáo hạn nếu $S_T > 70$ |
| :--- | ---: | :---: | :---: |
| Mua 10 hợp đồng Call ($K=70$) | $-6{,}200.00$ | $0$ | $+1{,}000(S_T - 70)$ |
| Bán 10 hợp đồng Put ($K=70$) | $+3{,}800.00$ | $-1{,}000(70 - S_T)$ | $0$ |
| Vay tiền mặt tại 4% EAR | $+2{,}400.00$ | $-2{,}447.53$ | $-2{,}447.53$ |
| Bán (Short) Forward 1,000 cp tại $73.20$ | $0.00$ | $+1{,}000(73.20 - S_T)$ | $+1{,}000(73.20 - S_T)$ |
| **Dòng tiền Ròng (Net Cash Flow)** | **$0.00$** | **$+\text{USD }752.47$** | **$+\text{USD }752.47$** |

- **Ý c (Giá Call hợp lý để xóa chênh lệch khi giữ nguyên $P = 3.80, F_{\text{mkt}} = 73.20$):**
  $$70 + (C^* - 3.80)(1.04)^{0.5} = 73.20 \implies C^* = 3.80 + \frac{3.20}{(1.04)^{0.5}} \approx \mathbf{\text{USD }6.94/\text{cổ phiếu}}$$

---

### 3. Khuôn Mẫu Lập Bảng Arbitrage Khi Vi phạm Put-Call Parity (Khi Đã Biết $S_0$)

Viết lại phương trình dưới dạng $C - P - S_0 + PV(K) = 0$. Tính giá lý thuyết $C^* = S_0 + P - PV(K)$:

- **TH1: $C_{\text{mkt}} < C^*$ (Call bị RẺ / Put bị ĐẮT — như L10 Question 6):**  
  **Mua Call + Bán danh mục sao chép của Call** (= Bán Put + Bán khống Cổ phiếu + Gửi tiết kiệm $PV(K)$):
  - Hôm nay ($t=0$): $-C_{\text{mkt}} + P + S_0 - PV(K) = +(C^* - C_{\text{mkt}}) > 0$ (thu tiền tươi ngay lập tức!).
  - Tại $T$: Nếu $S_T \le K$: $0 - (K - S_T) - S_T + K = 0$. Nếu $S_T > K$: $(S_T - K) - 0 - S_T + K = 0$.
- **TH2: $C_{\text{mkt}} > C^*$ (tức $P_{\text{mkt}} < P^*$ — Put bị RẺ / Call bị ĐẮT — như L10 Question 10):**  
  **Mua Put + Bán danh mục sao chép của Put** (= Bán Call + Mua Cổ phiếu + Vay $PV(K)$):
  - Hôm nay ($t=0$): $-P_{\text{mkt}} + C - S_0 + PV(K) = +(P^* - P_{\text{mkt}}) > 0$.
  - Tại $T$: Nếu $S_T \le K$: $(K - S_T) + 0 + S_T - K = 0$. Nếu $S_T > K$: $0 - (S_T - K) + S_T - K = 0$.

---

## 2.5. Giới hạn Giá Quyền chọn (Option Price Bounds) & Arbitrage Vi phạm Chặn Dưới

Ngay cả khi chưa biết độ biến động $\sigma$ để định giá chính xác, quy luật Không Arbitrage vẫn đóng khung giá quyền chọn trong những biên giới cứng (với giả định lãi suất $r \ge 0$):

### 1. Bảng Tổng hợp Chặn Dưới & Chặn Trên (Lower & Upper Bounds — L10 Cells 49–53)

| Loại Quyền chọn / Cấu trúc | Chặn Dưới (Lower Bound) | Chặn Trên (Upper Bound) | Giải thích Trực giác Không Arbitrage |
| :--- | :---: | :---: | :--- |
| **European Call ($C_E$, không cổ tức)** | $\max\!\big(0, \, S_0 - PV(K)\big)$ | $S_0$ | Từ $C_E = S_0 - PV(K) + P_E$ và $P_E \ge 0$; quyền mua 1 cp không bao giờ đắt hơn mua thẳng 1 cp ($S_0$). |
| **European Call ($C_E$, có cổ tức $D$)** | $\max\!\big(0, \, S_0 - PV(D) - PV(K)\big)$ | $S_0 - PV(D)$ | Trừ hiện giá cổ tức vì người giữ Call không được nhận cổ tức. |
| **American Call ($C_A$, không cổ tức)** | $\max\!\big(0, \, S_0 - PV(K)\big)$ *(vì $C_A = C_E$)* | $S_0$ | Vì $S_0 - PV(K) \ge S_0 - K$ với $r \ge 0$, chặn dưới Châu Âu đã tự động lớn hơn giá trị thực thi ngay! |
| **American Call ($C_A$, có cổ tức)** | $\max\!\big(0, \, S_0 - K, \, S_0 - PV(D) - PV(K)\big)$ | $S_0$ | Có quyền thực thi ngay lập tức để lấy $S_0 - K$ trước khi chia cổ tức! |
| **European Put ($P_E$, không cổ tức)** | $\max\!\big(0, \, PV(K) - S_0\big)$ | **$PV(K)$** | Payoff tối đa tại $T$ là $K$ (khi $S_T=0$), nên hôm nay không thể đắt hơn trái phiếu trả $K$ tại $T$ ($PV(K)$). |
| **American Put ($P_A$, không cổ tức)** | $\max\!\big(0, \, K - S_0\big)$ | **$K$** | Thực thi ngay nhận được $K - S_0$ (lớn hơn $PV(K) - S_0$); để bảo chứng thực thi bất cứ lúc nào cần giữ tiền mặt $K$! |
| **Bull Call / Bear Put Spread ($K_L < K_H$)** | $0$ *(tức $C_L \ge C_H$ và $P_H \ge P_L$)* | $PV(K_H - K_L)$ | Payoff luôn $\ge 0$ và không bao giờ vượt quá chênh lệch $\Delta K = K_H - K_L$ tại ngày $T$. |
| **Symmetric Butterfly ($K_M = \frac{K_L+K_H}{2}$)** | $0$ *(tính lồi $C_M \le \frac{C_L + C_H}{2}$)* | $PV(K_M - K_L)$ | Payoff nằm trong đoạn $[0, \, K_M - K_L]$ tại đáo hạn. |

---

### 2. Kỹ thuật Bắt Lỗi & Thiết lập Giao dịch Tự tài trợ Khi Vi phạm Chặn Dưới (Practice Question 20 — Zeta)

Giả sử cổ phiếu $S_0 = \text{USD }100$ (không cổ tức), $T = 1\text{ năm}$, $r = 10\%$ EAR. Bảng yết giá cho: $C(90) = 17$, $C(110) = 9$, $P(110) = 9$:
1. **Kiểm tra từng điều kiện (Ý a):**
   - Cặp $K = 110$: Chặn dưới Call $\max(0, 100 - 110/1.10) = 0 \le 9 \le 100$ (thỏa); Chặn dưới Put $\max(0, 100 - 100) = 0 \le 9 \le 100$ (thỏa); Put-Call Parity: $C(110) - P(110) = 9 - 9 = 0 = 100 - 110/1.10$ (**khớp hoàn hảo!**).
   - Giới hạn Spread: $C(90) - C(110) = 17 - 9 = 8 \in [0, \, 20/1.10 = 18.18]$ (nhìn riêng spread cũng chưa lộ lỗi!).
   - **Phát hiện tử huyệt tại Chặn dưới của $C(90)$:**
     $$C(90) \ge \max\!\left(0, \, 100 - \frac{90}{1.10}\right) = 100 - 81.8182 = \mathbf{\text{USD }18.1818}!$$
     Giá thị trường $C(90) = \text{USD }17 < 18.1818$ **VI PHẠM CHẶN DƯỚI KHÔNG ARBITRAGE**!

2. **Thiết lập Giao dịch Tự tài trợ ($CF_0 = 0$) Khai thác $C(K) < S_0 - PV(K)$ (Ý b):**
   - **Hôm nay ($t=0$):** Mua 1 Call giá rẻ ($-\text{USD }17$), Bán khống 1 cổ phiếu ($+\text{USD }100$), và đem **toàn bộ số tiền mặt dư ra $(S_0 - C) = \text{USD }83$** gửi tiết kiệm ở lãi suất $10\%$ ($\implies CF_0 = -17 + 100 - 83 = \mathbf{0}$!).
   - **Tại ngày đáo hạn ($t=1$):** Tiền gửi nở thành $83 \times 1.10 = \mathbf{+\text{USD }91.30}$:

| Giao dịch Tự tài trợ (Per share) | Hôm nay ($t=0$) | Đáo hạn nếu $S_T \le 90$ | Đáo hạn nếu $S_T > 90$ |
| :--- | ---: | :---: | :---: |
| Mua 1 Call ($K=90$) | $-17.00$ | $0$ | $+(S_T - 90)$ *(thực thi lấy cổ phiếu)* |
| Bán khống 1 cổ phiếu | $+100.00$ | $-S_T$ *(mua trên chợ trả kho)* | $-S_T$ *(dùng cổ phiếu từ Call trả kho)* |
| Cho vay (Gửi tiết kiệm) USD 83 tại 10% | $-83.00$ | $+91.30$ | $+91.30$ |
| **Dòng tiền Ròng (Net Cash Flow)** | **$0.00$** | **$91.30 - S_T \ge +1.30$** | **$+\text{USD }1.30$** |

   - **Kết luận sắc bén:** Vì khi $S_T \le 90$ thì $91.30 - S_T \ge 91.30 - 90 = 1.30$ (thậm chí nếu $S_T = 80$ còn lãi tới $\text{USD }11.30$!), **lợi nhuận đáo hạn tối thiểu chắc chắn là $+\text{USD }1.30$/cổ phiếu** (đúng bằng $(18.1818 - 17) \times 1.10 = \text{USD }1.30$)!
   *(Lưu ý: Tương tự, nếu một European Put bị vi phạm chặn dưới $P(K) < PV(K) - S_0$, ta **Mua Put + Mua Cổ phiếu + Vay $(S_0 + P)$**: tại $T$ luôn thu tối thiểu $\max(K, S_T) \ge K > (S_0 + P)(1+r)^T$!).*

---

## 2.6. Sáu Nhân tố Tác động lên Giá Quyền chọn (Comparative Statics — Bảng Dấu Chuẩn cho MCQ)

Xét sự thay đổi khi **tăng một biến đầu vào** và giữ nguyên tất cả 5 biến còn lại (*ceteris paribus*):

| Biến Đầu Vào Tăng ($\uparrow$) | European Call ($C_E$) | European Put ($P_E$) | American Call ($C_A$) | American Put ($P_A$) | Cơ chế Kinh tế Cốt lõi |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Giá cổ phiếu ($S_0 \uparrow$)** | **$+$** *(Tăng)* | **$-$** *(Giảm)* | **$+$** *(Tăng)* | **$-$** *(Giảm)* | Làm tăng payoff của Call $(S_T-K)^+$ và giảm payoff của Put $(K-S_T)^+$. |
| **2. Giá thực hiện ($K \uparrow$)** | **$-$** *(Giảm)* | **$+$** *(Tăng)* | **$-$** *(Giảm)* | **$+$** *(Tăng)* | Phải mua đắt hơn (hại Call), nhưng được bán giá cao hơn (lợi Put). |
| **3. Độ biến động ($\sigma \uparrow$)** | **$+$** *(Tăng)* | **$+$** *(Tăng)* | **$+$** *(Tăng)* | **$+$** *(Tăng)* | Payoff bất đối xứng: đuôi có lợi mở rộng thêm, còn đuôi bất lợi vẫn bị chặn sàn ở $0$! |
| **4. Lãi suất phi rủi ro ($r \uparrow$)** | **$+$** *(Tăng)* | **$-$** *(Giảm)* | **$+$** *(Tăng)* | **$-$** *(Giảm)* | Làm giảm $PV(K)$: người giữ Call được lợi vì hoãn trả $K$, người giữ Put bị thiệt vì nhận $K$ muộn. |
| **5. Cổ tức kỳ vọng ($D, q \uparrow$)** | **$-$** *(Giảm)* | **$+$** *(Tăng)* | **$-$** *(Giảm)* | **$+$** *(Tăng)* | Tiền mặt rút khỏi doanh nghiệp làm giá cổ phiếu ex-dividend tụt xuống. |
| **6. Thời gian tới đáo hạn ($T \uparrow$)** | **$+$** *(không cổ tức)* / **$?$** *(có cổ tức)* | **$?$** *(Tùy thuộc)* | **$+$** *(Không giảm)* | **$+$** *(Không giảm)* | Xem phân tích chuyên sâu ngay bên dưới! |

> [!WARNING]
> **HAI BẪY LÝ THUYẾT MCQ CỰC HAY RA VỀ $T$ VÀ $r$ (Practice Question 23):**
> 1. **Tại sao Quyền chọn Mỹ dài hạn KHÔNG BAO GIỜ rẻ hơn ngắn hạn ($V_A(T_2) \ge V_A(T_1)$ với $T_2 > T_1$), nhưng Quyền chọn Châu Âu thì CÓ THỂ rẻ hơn?**  
>    - Quyền chọn Mỹ kỳ hạn 12 tháng chứa đựng **mọi thời điểm được phép thực thi** của quyền chọn Mỹ 6 tháng (bao gồm cả mốc 6 tháng!), cộng thêm quyền chọn chờ thêm 6 tháng nữa — thêm quyền không bao giờ làm giảm giá trị.  
>    - Ngược lại, hai quyền chọn **Châu Âu** 6 tháng và 12 tháng có **hai ngày thực thi hoàn toàn khác nhau** (quyền chọn 12 tháng không được phép thực thi ở tháng thứ 6!). Với **European Put deep-ITM**, kéo dài từ 6 tháng lên 12 tháng bắt nhà đầu tư phải chờ thêm nửa năm mới nhận được tiền mặt $K$ (mất thêm lãi suất!), nên Put 12 tháng hoàn toàn có thể **RẺ HƠN** Put 6 tháng! Tương tự, **European Call** nếu kéo dài qua một đợt chia cổ tức khủng cũng có thể rẻ hơn Call đáo hạn trước ngày chia cổ tức!
> 2. **Bẫy ngộ nhận "Lãi suất $r$ tăng làm cả Call và Put đều tăng giá":** **SAI!** Khi giữ cố định $S_0$, lãi suất $r$ tăng làm giảm giá trị hiện tại của giá thực hiện $PV(K) = Ke^{-rT}$. Điều này làm **TĂNG giá Call** ($S_0 - PV(K)$ tăng) nhưng làm **GIẢM giá Put** ($PV(K) - S_0$ giảm)!

---

## 2.7. Mô hình Cấu trúc Merton trong Tài chính Doanh nghiệp (Options & Corporate Finance)

Robert Merton (1974) chỉ ra rằng nhờ cơ chế **Trách nhiệm hữu hạn (Limited Liability)** của cổ đông, toàn bộ cấu trúc vốn của một doanh nghiệp có tổng tài sản $V_t$ và một khoản nợ Zero-coupon mệnh giá $F$ (hay $K$) đáo hạn tại ngày $T$ chính là các vị thế quyền chọn trên tài sản công ty:

### 1. Bảng Cân đối Kế toán Dưới Góc Nhìn Quyền chọn (L10 Cell 23)

| Đối tượng Nắm giữ Quyền đòi nợ | Dòng tiền tại $T$ nếu Vỡ nợ ($V_T < F$) | Dòng tiền tại $T$ nếu Đủ trả ($V_T \ge F$) | Công thức Payoff Tổng quát | Định giá Hiện tại ($t=0$) |
| :--- | :---: | :---: | :---: | :--- |
| **Cổ đông (Equity $E$)** | $0$ *(Bỏ đi, không bù lỗ)* | $V_T - F$ | $\max(V_T - F, \, 0)$ | **$E_0 = C_0(V_0, \, K=F, \, T, \, r, \, \sigma_V)$** |
| **Chủ nợ (Risky Debt $D$)** | $V_T$ *(Tịch biên toàn bộ tài sản)* | $F$ | $\min(V_T, \, F)$ | **$D_0 = V_0 - E_0 = PV(F) - P_0(V_0, F, T)$** |
| **Tổng cộng ($E + D$)** | $V_T$ | $V_T$ | **$V_T$** | **$E_0 + D_0 = V_0$** *(Bảo toàn giá trị!)* |

- **Hai cách đọc bản chất Nợ Rủi ro ($D_0$):**
  1. $D_0 = V_0 - E_0$: Chủ nợ như người sở hữu công ty ($V_0$) nhưng đã bán một Quyền chọn Mua ($E_0$) cho cổ đông với giá thực hiện $F$ để cổ đông chuộc lại công ty!
  2. $D_0 = PV(F) - P_0$: Nợ doanh nghiệp có rủi ro chính bằng **Trái phiếu Chính phủ phi rủi ro mệnh giá $F$** trừ đi **Quyền chọn Bán Vỡ nợ (Default Put / Loan Guarantee $P_0$)** mà chủ nợ đã bán cho cổ đông!

### 2. Lợi suất Hứa hẹn (Promised Yield $y$), Chênh lệch Tín dụng (Credit Spread) & Định lý MM

1. **Cách tính Promised Yield $y$ và Credit Spread (L10 Q9, C26 & Practice Q25):**
   - Sau khi tìm được giá trị thị trường của khoản nợ $D_0 = V_0 - E_0$ đối với khoản nợ Zero-coupon hứa trả $F$ sau $T$ năm:
     - **Nếu đề hỏi theo lãi suất hiệu dụng năm (EAR — chuẩn hay gặp nhất):**
       $$D_0 = \frac{F}{(1 + y)^T} \quad \Longrightarrow \quad y = \left(\frac{F}{D_0}\right)^{1/T} - 1$$
       $$\text{Credit Spread} = y - r_{f,\text{eff}}$$
       *(CỰC KỲ LƯU Ý Practice Q25b: Nếu đề cho lãi suất phi rủi ro dạng liên tục $r_c = 4\%$ mà hỏi Credit Spread trên nền **Effective Annual Rate**, bạn PHẢI quy đổi $r_{f,\text{eff}} = e^{0.04} - 1 \approx 4.0811\%$ rồi mới lấy $y - r_{f,\text{eff}}$! Còn nếu tính cả hai trên nền liên tục thì $y_c = \frac{1}{T}\ln(F/D_0)$ và $\text{Spread}_c = y_c - r_c$).*
   - **Phân biệt Promised Yield vs. Expected Return trên Nợ (cho MCQ):** $y$ dùng dòng tiền tối đa ghi trên hợp đồng là $F$. Vì có xác suất vỡ nợ nhận ít hơn $F$ ($V_T < F$), **Tỷ suất sinh lời kỳ vọng thực sự của chủ nợ luôn THẤP HƠN Lợi suất hứa hẹn ($E[r_D] < y$)**!

2. **Định lý Bất biến Modigliani–Miller (MM Invariance) khi Vay Nợ Trả Cổ tức Đặc biệt (L10 Q9 & Practice Q25d):**
   - Giả sử công ty ban đầu không nợ có tài sản $V_0 = \text{USD }120\text{m}$. Công ty phát hành nợ mệnh giá $F$, thu về số tiền $D_0$ và **đem chia ngay lập tức toàn bộ $D_0$ làm cổ tức tiền mặt đặc biệt (Special Dividend)** cho cổ đông hiện hữu (tài sản hoạt động $V_0$ giữ nguyên, không thuế, không chi phí phá sản).
   - Ngay sau khi chia cổ tức: Cổ đông cầm trong túi **tiền mặt $D_0$** cộng với **cổ phiếu còn lại trị giá $E_0 = V_0 - D_0$**.
   - **Tổng giá trị tài sản của cổ đông ban đầu:** $\text{Cash Distributed } (D_0) + \text{Post-Dividend Equity } (E_0) = \mathbf{V_0 = \text{USD }120\text{m}}$ — **GIỮ NGUYÊN KHÔNG ĐỔI** dù công ty vay mệnh giá $F = 100\text{m}$ hay $F = 120\text{m}$! *(Khi tăng mệnh giá nợ hứa hẹn $F_2 > F_1$, chủ nợ mới định giá rủi ro vỡ nợ cao hơn nên đòi lãi suất $y_2 > y_1$, tiền thu về chỉ tăng đúng bằng phần giá trị vốn cổ phần $E_0$ sụt giảm!).*

---

### 3. HIỆN TƯỢNG THAY THẾ TÀI SẢN / CHUYỂN DỊCH RỦI RO (ASSET SUBSTITUTION / RISK SHIFTING — BÀI TOÁN KAPPA EXTRA SESSION!)

Khác hẳn với việc phát hành nợ *mới* (nơi chủ nợ mới tự bảo vệ mình bằng cách ép giá $D_0$ xuống), chuyện gì xảy ra khi **khoản nợ $F$ ĐÃ PHÁT HÀNH XONG và cố định điều khoản**, sau đó ban giám đốc (đại diện cho cổ đông) thay đổi hoạt động kinh doanh sang dự án mạo hiểm hơn?

Hãy xem trọn vẹn con số kinh điển của **Bài toán Kappa (Extra Session Cells 19–25)**:
- **Hiện trạng ban đầu:** Tài sản $V_0 = \text{USD }150\text{m}$, độ biến động tài sản $\sigma_V = 25\%$, có $6$ triệu cổ phiếu và khoản nợ Zero-coupon mệnh giá $F = \text{USD }120\text{m}$ đáo hạn sau $T = 2$ năm, $r_f = 4\%$ (liên tục). Theo BSM:
  $$E_0 = \text{USD }44.1250\text{m } (\text{USD }7.35/\text{cp}), \qquad D_0 = 150 - 44.1250 = \text{USD }105.8750\text{m}$$
- **Đề xuất thay đổi vận hành (Dự án phá hủy giá trị doanh nghiệp, $\text{NPV} = -\text{USD }3\text{m}$!):** Làm giảm tổng tài sản hiện tại xuống $V_0' = \text{USD }147\text{m}$ ($\Delta V = -\text{USD }3\text{m}$), nhưng đẩy độ biến động tài sản vọt lên **$\sigma_V' = 40\%$** (điều khoản nợ giữ nguyên):
  $$E_0' = \text{USD }50.2128\text{m } (\text{USD }8.37/\text{cp}), \qquad D_0' = 147 - 50.2128 = \text{USD }96.7872\text{m}$$

| Chỉ tiêu Giá trị | Vận hành Hiện tại ($V_0=150, \sigma_V=25\%$) | Đề xuất Mới ($V_0'=147, \sigma_V'=40\%$) | Mức Thay Đổi ($\Delta$) | Thái độ của Các Bên |
| :--- | ---: | ---: | ---: | :--- |
| **Tổng Tài sản ($V$)** | $\text{USD }150.0000\text{m}$ | $\text{USD }147.0000\text{m}$ | **$-\text{USD }3.0000\text{m}$** | Giá trị toàn công ty bị hủy hoại! |
| **Vốn cổ phần ($E$)** | $\text{USD }44.1250\text{m}$ | $\text{USD }50.2128\text{m}$ | **$+\text{USD }6.0878\text{m}$** | **Cổ đông ỦNG HỘ NHIỆT LIỆT** (giá cp tăng $7.35 \to 8.37$)! |
| **Nợ vay ($D$)** | $\text{USD }105.8750\text{m}$ | $\text{USD }96.7872\text{m}$ | **$-\text{USD }9.0878\text{m}$** | **Chủ nợ PHẢN ĐỐI KỊCH LIỆT** (gánh trọn thiệt hại)! |

> [!IMPORTANT]
> **BÀI HỌC VÀNG TỪ BÀI KAPPA (CỰC KỲ DỄ RA TRONG MCQ & CÂU GIẢI THÍCH CUỐI BÀI):**
> 1. **Tại sao tổng tài sản giảm $\text{USD }3\text{m}$ mà cổ đông lại giàu thêm $+\text{USD }6.09\text{m}$?** Vì vốn cổ phần là một **Call Option trên tài sản công ty**: khi độ biến động $\sigma_V$ tăng vọt từ $25\%$ lên $40\%$, nếu canh bạc thắng lớn cổ đông ăn trọn phần lãi vượt trên $120\text{m}$, còn nếu thất bại thảm hại cổ đông phủi tay nhờ trách nhiệm hữu hạn ($E_T = 0$), đẩy toàn bộ phần lỗ xuống đầu chủ nợ! Hiệu ứng tăng giá trị quyền chọn do $\sigma_V \uparrow$ đã lấn át hoàn toàn cú giảm $\text{USD }3\text{m}$ của tài sản!
> 2. **Kiểm tra bảo toàn:** $\Delta E + \Delta D = (+6.0878) + (-9.0878) = -3.0000 = \Delta V$. Chủ nợ vừa mất $\text{USD }3\text{m}$ giá trị công ty, vừa bị cổ đông "móc túi" chuyển dịch sang thêm $\text{USD }6.0878\text{m}$!
> 3. **Kết luận định lý:** Khi doanh nghiệp có nợ rủi ro, **giá cổ phiếu tăng lên KHÔNG đồng nghĩa với việc dự án tạo ra giá trị cho toàn doanh nghiệp (higher stock price does NOT imply firm value creation)**! *(Chú ý kỹ thuật thêm: Khi áp dụng mô hình Merton, luôn dùng **Asset Volatility $\sigma_V$**, tuyệt đối không dùng Stock Volatility $\sigma_E$!).*

---

# CHƯƠNG 3 — LECTURE 11 & EXTRA SESSION: CÂY NHỊ THỨC CHÂU ÂU (TRỌNG TÂM TÍNH TOÁN #3), ĐÒN BẨY/BETA QUYỀN CHỌN & LÝ THUYẾT BSM/AMERICAN CHO MCQ

## 3.1. Mô hình Cây Nhị thức 1 Thời kỳ (One-Period Binomial Option Pricing Model)

Xét một bước thời gian độ dài $\Delta t$ (tính bằng năm). Cổ phiếu hiện có giá $S_0$ (không trả cổ tức), cuối kỳ chỉ nhận một trong hai mức giá:
- **Trạng thái Tăng (Up state):** $S_u = S_0 \cdot u \implies$ Payoff của chứng khoán phái sinh là **$V_u$** (ví dụ Call: $\max(S_u - K, 0)$; Put: $\max(K - S_u, 0)$).
- **Trạng thái Giảm (Down state):** $S_d = S_0 \cdot d \implies$ Payoff của chứng khoán phái sinh là **$V_d$**.
- **Hệ số Lãi gộp Phi rủi ro trong 1 bước ($R$):** Một đồng tiền mặt đầu tư phi rủi ro ở đầu bước sẽ nở thành **$R$** đồng ở cuối bước *(trong một số slide bài giảng ký hiệu hệ số gộp này là $r$, ví dụ $r = 1.05$; trong tài liệu Practice chuẩn hóa ký hiệu là **$R$** để không bao giờ nhầm với lãi suất phần trăm $r_f = 5\%$)*.

### 1. Điều kiện Không Arbitrage ($0 < d < R < u$) & Cách Ăn Arbitrage Khi Vi phạm (Practice Question 28)

Để thị trường không tồn tại máy in tiền miễn phí, hệ số sinh lời phi rủi ro $R$ bắt buộc phải nằm **chính giữa** hệ số giảm $d$ và hệ số tăng $u$:
$$\boxed{0 < d < R < u \quad \Longleftrightarrow \quad S_d < R \cdot S_0 < S_u}$$

**Chuyện gì xảy ra nếu bảng tính vi phạm điều kiện này? (Ví dụ Practice Q28b: $S_0 = 80, u = 1.08, d = 0.94$, nhưng $r_f = 21\%$ EAR cho kỳ 6 tháng $\implies R = (1.21)^{0.5} = \mathbf{1.10 > u = 1.08}$!):**
- **Khi $R \ge u$ (Tiền gửi ngân hàng thắng cả kịch bản tốt nhất của cổ phiếu!):**
  - **Hôm nay ($t=0$, chi phí $0$):** **Bán khống 1 cổ phiếu** thu $+\text{USD }80$, đem **cho vay phi rủi ro toàn bộ $\text{USD }80$** ($\implies CF_0 = 0$).
  - **Sau 6 tháng:** Tiền cho vay thu về chắc chắn $80 \times 1.10 = \mathbf{+\text{USD }88.00}$. Mua lại cổ phiếu trả kho tốn $S_u = 86.40$ (lãi ròng **$+\text{USD }1.60$**) hoặc $S_d = 75.20$ (lãi ròng **$+\text{USD }12.80$**)! Không bao giờ lỗ, chắc chắn lãi dương!
- **Khi $R \le d$ (Cổ phiếu dù sập sàn vẫn sinh lời cao hơn lãi đi vay!):**
  - **Hôm nay ($t=0$, chi phí $0$):** **Vay $S_0$** ở lãi suất phi rủi ro, dùng tiền đó **mua ngay 1 cổ phiếu** ($\implies CF_0 = 0$).
  - **Cuối kỳ:** Bán cổ phiếu thu $S_u$ hoặc $S_d$, trả nợ gốc + lãi $R \cdot S_0 \implies$ Lãi ròng $S_u - R S_0 > S_d - R S_0 \ge 0$!

---

### 2. Thành thục CẢ 3 Phương pháp Định giá Tương đương (Đều Cho Ra Đúng 1 Đáp Số!)

Đề thi có thể chỉ định đích danh một trong ba phương pháp ở từng ý `a, b` (như Practice Q26 hỏi Replicating Portfolio, Q27 hỏi State Prices, Q28 hỏi Risk-Neutral Probability), nên bạn bắt buộc phải làm chủ cả 3 góc nhìn:

#### Phương pháp 1: Danh mục Sao chép ($\Delta$ Cổ phiếu + $B$ Tiền mặt — Replicating Portfolio)
Thiết lập danh mục gồm **$\Delta$ cổ phiếu** và **$B$ đô-la tiền mặt** (nếu $B > 0$: cho vay/gửi tiết kiệm; nếu $B < 0$: đi vay) sao cho khớp payoff ở cả 2 trạng thái:
$$\begin{cases} \Delta S_u + R B = V_u \\ \Delta S_d + R B = V_d \end{cases} \quad \Longrightarrow \quad \boxed{\Delta = \frac{V_u - V_d}{S_u - S_d} = \frac{V_u - V_d}{S_0(u - d)}}$$
$$\boxed{B = \frac{V_u - \Delta S_u}{R} = \frac{V_d - \Delta S_d}{R} = \frac{u V_d - d V_u}{R(u - d)}}$$
$$\boxed{V_0 = \Delta S_0 + B}$$

- **Kiểm tra dấu trực giác:**
  - Với **Call Option** ($V_u \ge V_d$): Luôn có **$\Delta \ge 0$** và **$B \le 0$** $\implies$ Sao chép Long Call bằng cách **Mua $\Delta$ cổ phiếu + Đi vay tiền mặt $(-B)$**!
  - Với **Put Option** ($V_u \le V_d$): Luôn có **$\Delta \le 0$** và **$B \ge 0$** $\implies$ Sao chép Long Put bằng cách **Bán khống $(-\Delta)$ cổ phiếu + Cho vay/gửi tiết kiệm $(+B)$**!
- *(Góc nhìn tương đương — Danh mục Phòng hộ Phi rủi ro Riskless Hedge như L11 Cell 4: Giữ $\Delta$ cổ phiếu và Bán 1 quyền chọn, giá trị danh mục tại $T$ luôn bằng hằng số $\Delta S_u - V_u = \Delta S_d - V_d$, chiết khấu hằng số này về hôm nay chia cho $R$ sẽ bằng $\Delta S_0 - V_0$).*

#### Phương pháp 2: Định giá Trung lập Rủi ro (Risk-Neutral Valuation — Nhanh nhất khi giải nhiều bước!)
Thay $\Delta$ và $B$ vào $V_0 = \Delta S_0 + B$ và gom nhóm theo $V_u, V_d$, ta thu được công thức kỳ vọng chiết khấu dưới **Xác suất tăng trung lập rủi ro $p$** (hay $p_u$):
$$\boxed{p = \frac{R - d}{u - d} = \frac{R \cdot S_0 - S_d}{S_u - S_d}}, \qquad 1 - p = \frac{u - R}{u - d} = \frac{S_u - R \cdot S_0}{S_u - S_d}$$
$$\boxed{V_0 = \frac{p V_u + (1 - p) V_d}{R}}$$
*(Ý nghĩa cốt lõi: Dưới xác suất $p$, giá kỳ vọng của chính cổ phiếu là $p S_u + (1-p)S_d = R S_0$, tức mọi tài sản trong thế giới trung lập rủi ro đều có tỷ suất sinh lời kỳ vọng bằng đúng lãi suất phi rủi ro!).*

#### Phương pháp 3: Giá Trạng thái Arrow–Debreu (State Prices $q_u, q_d$ hay $P_u, P_d$ — L11 Cell 5 & Practice Q27)
- **$q_u$ (hay $P_u$):** Giá hôm nay của chứng khoán cơ sở trả đúng **$\text{USD }1$ nếu trạng thái Up xảy ra** và $\text{USD }0$ nếu Down xảy ra.
- **$q_d$ (hay $P_d$):** Giá hôm nay của chứng khoán cơ sở trả đúng **$\text{USD }1$ nếu trạng thái Down xảy ra** và $\text{USD }0$ nếu Up xảy ra.
$$\boxed{q_u = \frac{p}{R} = \frac{R - d}{R(u - d)} = \frac{R S_0 - S_d}{R(S_u - S_d)}, \qquad q_d = \frac{1 - p}{R} = \frac{u - R}{R(u - d)} = \frac{S_u - R S_0}{R(S_u - S_d)}}$$
- **Đẳng thức kiểm tra bắt buộc (luôn hỏi ở câu `a` như Practice Q27a):** Mua 1 chứng khoán Up + 1 chứng khoán Down chắc chắn nhận được $\text{USD }1$ ở cuối kỳ trong mọi trạng thái, nên tổng giá của chúng **BẮT BUỘC bằng giá trị hiện tại của $\text{USD }1$**:
  $$\boxed{q_u + q_d = \frac{1}{R}}$$
- **Định giá mọi phái sinh bất kỳ trong 3 giây:**
  $$\boxed{V_0 = q_u V_u + q_d V_d}$$
  *(Ví dụ Practice Q27: $S_0 = 42 \to S_u = 54, S_d = 34$; trái phiếu giá $100$ trả $104 \implies R = 1.04$. Suy ra $q_u = \frac{1.04(42) - 34}{1.04(20)} = \frac{9.68}{20.80} \approx 0.465385$, $q_d = \frac{54 - 43.68}{20.80} \approx 0.496154$. Kiểm tra $q_u + q_d = 0.961538 = 1/1.04$! Put $K = 44$ có $P_u = 0, P_d = 10 \implies P_0 = 0 + 10 \times 0.496154 \approx \text{USD }4.96$!).*

---

### 3. Kỹ năng Tìm Ngược Giá Thực Hiện $K$ Bị Ẩn Khi Biết Giá Quyền Chọn (Practice Question 31 — Upsilon)

Giả sử $S_0 = 64 \to S_u = 80, S_d = 48$ ($u = 1.25, d = 0.75$), $R = 1.05 \implies p = \frac{1.05 - 0.75}{1.25 - 0.75} = 0.60$. Biết Call Châu Âu có giá $C_0 = \text{USD }10$, tìm strike $K \ge 0$:
- **Bước 1 — Giả sử $K$ nằm giữa hai nhánh ($48 \le K < 80$):** Khi đó $C_u = 80 - K > 0$ và $C_d = 0$:
  $$C_0 = \frac{0.60(80 - K) + 0.40(0)}{1.05} = 10 \implies 0.60(80 - K) = 10.50 \implies 80 - K = 17.50 \implies \mathbf{K = \text{USD }62.50}$$
  Kiểm tra miền: $48 \le 62.50 < 80$ $\implies$ **THỎA MÃN HOÀN HẢO!** ($C_u = 17.50, C_d = 0$).
- **Bước 2 — Kiểm tra loại trừ miền $0 \le K < 48$ (luôn ITM ở cả 2 nhánh):** Nếu $K < 48$ thì $C_0 = S_0 - \frac{K}{R} = 64 - \frac{K}{1.05} = 10 \implies K = 54 \times 1.05 = 56.70 > 48$ (mâu thuẫn với giả thiết $K < 48$!). *(Và hiển nhiên nếu $K \ge 80$ thì $C_0 = 0 \ne 10$).*
- **Ý b (Tính giá Put cùng $K = 62.50$):** Dùng ngay Put-Call Parity: $P_0 = C_0 - S_0 + \frac{K}{R} = 10 - 64 + \frac{62.50}{1.05} \approx \mathbf{\text{USD }5.52}$ (hoặc dùng cây: $P_u = 0, P_d = 62.50 - 48 = 14.50 \implies P_0 = \frac{0.40 \times 14.50}{1.05} = \text{USD }5.5238$).

---

## 3.2. Cây Nhị thức 2 Thời kỳ Châu Âu (Two-Period European Binomial Tree — LUYỆN THÀNH THỤC TUYỆT ĐỐI!)

Đây là **trái tim tính toán của Lecture 11 & Extra Session**! Để không bao giờ mất dù chỉ $0.25$ điểm, hãy tuân thủ tuyệt đối 3 trụ cột dưới đây:

### Trụ cột 1: Quy tắc Vàng Quy đổi Hệ số Lãi gộp Mỗi Bước $R$ (Chặn đứng lỗi chiết khấu Kép!)
Giả sử quyền chọn có tổng thời gian đáo hạn $T$ được chia làm **2 bước đều nhau**, mỗi bước có độ dài **$\Delta t = T / 2$** (năm). Ví dụ quyền chọn 6 tháng chia làm 2 kỳ 3 tháng ($\Delta t = 0.25$ năm), hoặc quyền chọn 1 năm chia làm 2 kỳ 6 tháng ($\Delta t = 0.5$ năm):

| Cách Đề Bài Cho Lãi Suất Năm | Công thức Hệ số Lãi gộp **MỖI BƯỚC** ($R$) | Ví dụ Cụ thể trong Bài giảng & Practice |
| :--- | :---: | :--- |
| **1. Effective Annual Rate (EAR $r_{\text{eff}}$)** | $R = (1 + r_{\text{eff}})^{\Delta t}$ | $\Delta t = 0.5, r_{\text{eff}} = 10.25\% \implies R = (1.1025)^{0.5} = 1.05$ (Q28). |
| **2. Nominal Annual / APR ghép lãi $m$ lần/năm** *(với $\Delta t = 1/m$)* | $R = 1 + \dfrac{r_{\text{nom}}}{m}$ | $8\%$ APR ghép lãi theo quý ($\Delta t = 0.25, m=4$) $\implies R = 1 + \frac{0.08}{4} = \mathbf{1.02}$ (L11 C19 & Q32). $6\%$ APR ghép bán niên $\implies R = 1.03$ (Q39). |
| **3. Continuously Compounded Rate ($r_c$)** | $R = e^{r_c \Delta t}$ | $\Delta t = 1, r_c = 4\% \implies R = e^{0.04} \approx 1.040811$ (Bài Kappa Extra Session). |

> [!CAUTION]
> **LỖI SAI KINH ĐIỂN TRONG PRACTICE QUESTION 32b (BẪY CHIẾT KHẤU $(1.02)^2$ MỖI BƯỚC):**  
> Ở cây 6 tháng gồm 2 bước 3 tháng với $R = 1.02$/quý:
> - Khi quy nạp ngược **từng bước một** ($t=2 \to t=1$ để tìm $V_u, V_d$; rồi $t=1 \to t=0$ để tìm $V_0$), mỗi bước chỉ đi lùi đúng 1 quý nên **CHỈ ĐƯỢC CHIA CHO $R = 1.02$ MỘT LẦN Ở MỖI BƯỚC**! (Tổng cộng qua 2 bước mới thành chia cho $(1.02)^2$).
> - Trong Q32b, nhân vật Zeta chia cho $(1.02)^2$ ở bước $t=2 \to t=1$ rồi lại chia tiếp cho $(1.02)^2$ ở bước $t=1 \to t=0$, tức là chiết khấu tổng cộng cho **$(1.02)^4$ (12 tháng thay vì 6 tháng!)**, làm giá Put bị tính thiếu đi đúng hệ số $1/(1.02)^2$ ($\text{USD }11.15$ thay vì đáp số đúng $\text{USD }11.60$)!

---

### Trụ cột 2: PHÂN BIỆT SINH TỬ "CÂY NHÂN TÍNH" VS. "CÂY CỘNG TÍNH"!

Đọc đề bài cây 2 kỳ, việc ĐẦU TIÊN trong 3 giây đầu là nhìn xem giá cổ phiếu biến động theo **Tỷ lệ phần trăm ($\%$ / hệ số $u, d$)** hay theo **Số tiền đô-la cố định ($\pm\text{USD}$)**:

#### DẠNG A: Cây Nhân Tính Tái Hợp (Multiplicative Recombining Tree — $u, d$ cố định ở mọi bước)
- **Dấu hiệu nhận diện:** *"rises by 25% or falls by 20% each period"* ($u = 1.25, d = 0.80$), HOẶC **Cây Cox–Ross–Rubinstein (CRR)** cho từ độ biến động $\sigma$ (như **Bài Kappa câu `a` trong Extra Session**):
  $$\boxed{u = e^{\sigma \sqrt{\Delta t}}, \qquad d = \frac{1}{u} = e^{-\sigma \sqrt{\Delta t}}}$$
- **Tính chất Vàng:**
  1. Cây tái hợp thành **3 nút cuối kỳ** tại $t = 2$: $S_{uu} = S_0 u^2$, **$S_{ud} = S_{du} = S_0 u d$** *(đặc biệt với cây CRR vì $d = 1/u$ nên $S_{ud} = S_0$!)*, và $S_{dd} = S_0 d^2$.
  2. Vì $u, d$ và $R$ giống hệt nhau ở mọi nút nên **Xác suất trung lập rủi ro $p = \dfrac{R - d}{u - d}$ là HẰNG SỐ DUY NHẤT trên toàn bộ cây**!
- **Quy trình Giải Chuẩn Ăn Trọn Điểm Thành Phần + Công Thức Tắt Kiểm Tra:**
  - **Bước 1 (Payoff tại $t=2$):** Tính $V_{uu}, V_{ud}, V_{dd}$.
  - **Bước 2 (Lùi về $t=1$ — BẮT BUỘC VIẾT RA nếu đề hỏi giá trị kỳ 1):**
    $$V_u = \frac{p V_{uu} + (1 - p) V_{ud}}{R}, \qquad V_d = \frac{p V_{ud} + (1 - p) V_{dd}}{R}$$
  - **Bước 3 (Lùi về $t=0$ & Kiểm tra bằng Công thức Nhị thức 1 Dòng):**
    $$\boxed{V_0 = \frac{p V_u + (1 - p) V_d}{R} = \frac{p^2 V_{uu} + \mathbf{2} p (1 - p) V_{ud} + (1 - p)^2 V_{dd}}{R^2}}$$
    *(Đừng bao giờ quên hệ số **$2$** trước $p(1-p)V_{ud}$ vì có **2 đường đi** `Up-Down` và `Down-Up` cùng dẫn tới nút giữa $S_{ud}$!).*

---

#### DẠNG B: Cây Cộng Tính (Additive / Dollar-Move Tree — Tăng/Giảm số tiền USD cố định mỗi kỳ!)
*(Xuất hiện trực tiếp trong **Lecture 11 Cells 21–22 (Delta Corp)** và **Practice Question 33 (Chi Shares)** — Bẫy giết điểm số 1 nếu học vẹt công thức $p^2$!)*

- **Dấu hiệu nhận diện:** Đề ghi *"In each of the next two years, the price either **rises by USD 12** or **falls by USD 8**"* (cộng/trừ tiền mặt: $+\Delta U$ hoặc $-\Delta D$).
- **Cơ chế biến đổi ngầm cực hiểm:**
  - Cây giá cổ phiếu **vẫn tái hợp** ở nút giữa: $S_{ud} = S_0 + \Delta U - \Delta D = S_{du}$.
  - **NHƯNG tỷ suất sinh lời phần trăm $u, d$ tại mỗi nút bị THAY ĐỔI** vì mẫu số $S_{\text{node}}$ đã thay đổi! Ví dụ $S_0 = 40$ tăng $+12$ là tăng $+30\%$ ($u_0 = 52/40 = 1.30$), nhưng lên đến nút $S_u = 52$ mà tăng tiếp $+12$ lên $64$ thì chỉ còn tăng $+23.08\%$ ($u_u = 64/52 \approx 1.2308$)!
  - Hệ quả tất yếu: **XÁC SUẤT TRUNG LẬP RỦI RO THAY ĐỔI Ở TỪNG NÚT: $p_0 \ne p_u \ne p_d$!**
  - **TUYỆT ĐỐI CẤM** lấy $p_0$ ở gốc áp cho nút $u$ và nút $d$, và **TUYỆT ĐỐI CẤM** dùng công thức tắt $p^2 V_{uu} + 2p(1-p)V_{ud} + (1-p)^2 V_{dd}$!

> [!TIP]
> **CÔNG THỨC SIÊU TỐC TÍNH $p_{\text{node}}$ TRONG 3 GIÂY CHO CÂY CỘNG TÍNH (KHÔNG CẦN TÍNH $u, d$ LẺ!):**  
> Tại bất kỳ nút nào có giá hiện tại là $S_{\text{node}}$, nhảy lên $S_{\text{up}} = S_{\text{node}} + \Delta U$ hoặc nhảy xuống $S_{\text{down}} = S_{\text{node}} - \Delta D$, công thức tổng quát luôn là:
> $$\boxed{p_{\text{node}} = \frac{R \cdot S_{\text{node}} - S_{\text{down}}}{S_{\text{up}} - S_{\text{down}}} = \frac{R \cdot S_{\text{node}} - S_{\text{down}}}{\Delta U + \Delta D}}$$
> *(Nhìn vào mẫu số kìa: chênh lệch $S_{\text{up}} - S_{\text{down}}$ ở MỌI NÚT trên cây cộng tính luôn là hằng số chẵn đẹp $\Delta U + \Delta D$!).*

**Ví dụ Mẫu Toàn Diện (Practice Question 33 — Chi Shares):**  
$S_0 = \text{USD }40$, mỗi năm tăng $+\text{USD }12$ hoặc giảm $-\text{USD }8$ ($\implies S_{\text{up}} - S_{\text{down}} = 12 + 8 = \mathbf{20}$ ở mọi nút!), $R = 1.10$, định giá European Put 2 năm $K = \text{USD }48$:
1. **Dựng cây giá:**
   - Năm 0: $S_0 = 40$.
   - Năm 1: $S_u = 40 + 12 = 52$; $S_d = 40 - 8 = 32$.
   - Năm 2: $S_{uu} = 52 + 12 = 64$; $S_{ud} = S_{du} = 52 - 8 = 32 + 12 = 44$; $S_{dd} = 32 - 8 = 24$.
   - Payoff Put ($K = 48$): $P_{uu} = \max(48 - 64, 0) = 0$; $P_{ud} = P_{du} = \max(48 - 44, 0) = 4$; $P_{dd} = \max(48 - 24, 0) = 24$.
2. **Tính đúng bộ 3 xác suất nút ($p_0, p_u, p_d$) trong 10 giây:**
   $$p_0 = \frac{1.10(40) - 32}{20} = \frac{44 - 32}{20} = \mathbf{0.60}$$
   $$p_u = \frac{1.10(52) - 44}{20} = \frac{57.2 - 44}{20} = \mathbf{0.66}$$
   $$p_d = \frac{1.10(32) - 24}{20} = \frac{35.2 - 24}{20} = \mathbf{0.56}$$
3. **Quy nạp ngược chuẩn xác:**
   $$P_u = \frac{0.66(0) + 0.34(4)}{1.10} = \frac{1.36}{1.10} \approx \text{USD }1.236364, \qquad P_d = \frac{0.56(4) + 0.44(24)}{1.10} = \frac{12.80}{1.10} \approx \text{USD }11.636364$$
   $$P_0 = \frac{0.60(1.236364) + 0.40(11.636364)}{1.10} = \frac{5.396364}{1.10} \approx \mathbf{\text{USD }4.91}$$
   *(Nếu mắc bẫy dùng $p_0 = 0.60$ cho mọi nút như Psi ở câu `b`, bạn sẽ ra $\text{USD }4.76$ — sai lệch vì không phản ánh đúng thực tế là tỷ suất sinh lời phần trăm $(u, d)$ co giãn theo mức giá $S$ khiến điều kiện không arbitrage đòi hỏi $p_u > p_0 > p_d$!).*

---

## 3.3. Phòng Hộ Động Tự Tài Trợ Qua 2 Thời kỳ (Dynamic Delta-Hedging & Self-Financing Rebalancing)

Làm sao một ngân hàng bán (write) quyền chọn Châu Âu 2 kỳ có thể bảo hiểm rủi ro tuyệt đối 100% mà **chỉ dùng đúng số tiền phí quyền chọn thu về lúc đầu, không cần xin thêm một xu vốn nào ở giữa kỳ**? Đây chính là toàn bộ nội dung của **Practice Question 39 (Zeta)** — bài toán đỉnh cao nối liền cây nhị thức với bản chất tái cân bằng liên tục của Black-Scholes!

### Quy trình 4 Bước Giải Trọn Vẹn (Kèm Số Liệu Đầy Đủ của Bài Toán Zeta Q39)
*Đề bài:* Zeta bán 1 European Call ($K = 82$, $T = 1\text{ năm} = 2\text{ kỳ 6 tháng}$). $S_0 = 80$, mỗi 6 tháng tăng $+20\%$ ($u = 1.20$) hoặc giảm $-10\%$ ($d = 0.90$). Lãi suất $6\%$ APR ghép bán niên $\implies R = 1.03$/kỳ.

#### Bước 1: Định giá Cây & Thiết lập Danh mục Phòng hộ Ban đầu tại $t = 0$
- Cây giá: $S_0 = 80 \to (S_u = 96, S_d = 72) \to (S_{uu} = 115.20, S_{ud} = 86.40, S_{dd} = 64.80)$.
- Payoff Call ($K=82$): $C_{uu} = 33.20$, $C_{ud} = 4.40$, $C_{dd} = 0$.
- Xác suất trung lập rủi ro: $p = \frac{1.03 - 0.90}{1.20 - 0.90} = \frac{0.13}{0.30} \approx 0.433333$ ($1 - p = \frac{0.17}{0.30} \approx 0.566667$).
- Giá quyền chọn tại $t=1$ và $t=0$:
  $$C_u = \frac{\frac{13}{30}(33.20) + \frac{17}{30}(4.40)}{1.03} \approx \mathbf{16.388350}, \qquad C_d = \frac{\frac{13}{30}(4.40) + \frac{17}{30}(0)}{1.03} \approx \mathbf{1.851133}$$
  $$C_0 = \frac{\frac{13}{30}(16.388350) + \frac{17}{30}(1.851133)}{1.03} \approx \mathbf{\text{USD }7.913197 \text{ (USD }7.91\text{)}}$$
- **Danh mục phòng hộ tại $t = 0$ ($\Delta_0, B_0$):**
  $$\Delta_0 = \frac{C_u - C_d}{S_u - S_d} = \frac{16.388350 - 1.851133}{96 - 72} \approx \mathbf{0.605717\text{ cổ phiếu}}$$
  $$B_0 = \frac{C_u - \Delta_0 S_u}{R} = C_0 - \Delta_0 S_0 = 7.913197 - 0.605717(80) \approx \mathbf{-\text{USD }40.544192 \text{ (Đi vay USD }40.54\text{)}}$$
  *(Zeta thu phí bán Call $+\text{USD }7.9132$, vay thêm $+\text{USD }40.5442$ để mua đủ $0.605717$ cổ phiếu trị giá $\text{USD }48.4574 \implies$ Tiền mặt tự bỏ ra hôm nay $= \mathbf{0}$!).*

#### Bước 2: Tái cân bằng Tự tài trợ (Self-Financing Rebalancing) tại $t = 1$ (6 tháng)

- **Nếu nhánh UP xảy ra ($S_u = 96$):**
  1. *Giá trị danh mục cũ mang sang trước khi giao dịch:* $\Pi_1^{\text{before}}(u) = 0.605717(96) + 1.03(-40.544192) = 58.148867 - 41.760518 = \mathbf{16.388350 = C_u}$!
  2. *Danh mục mới cần giữ trong kỳ 2:*
     $$\Delta_u = \frac{C_{uu} - C_{ud}}{S_{uu} - S_{ud}} = \frac{33.20 - 4.40}{115.20 - 86.40} = \frac{28.80}{28.80} = \mathbf{1.000000\text{ cổ phiếu}}$$
     $$B_u = \frac{C_{uu} - \Delta_u S_{uu}}{R} = \frac{33.20 - 1(115.20)}{1.03} = \frac{-82}{1.03} \approx \mathbf{-\text{USD }79.611650}$$
  3. *Chứng minh Tự tài trợ:* Zeta cần **mua thêm** $1.000000 - 0.605717 = \mathbf{0.394283\text{ cổ phiếu}}$ tại giá $96$, tốn $0.394283 \times 96 = \text{USD }37.851133$. Zeta **vay thêm đúng $\text{USD }37.851133$**, làm dư nợ tăng từ $-41.760518$ lên $-41.760518 - 37.851133 = \mathbf{-79.611650 = B_u}$! **Dòng tiền bơm/rút bên ngoài bằng $0$ tuyệt đối!**

- **Nếu nhánh DOWN xảy ra ($S_d = 72$):**
  1. *Giá trị danh mục cũ mang sang:* $\Pi_1^{\text{before}}(d) = 0.605717(72) + 1.03(-40.544192) = 43.611650 - 41.760518 = \mathbf{1.851133 = C_d}$!
  2. *Danh mục mới cần giữ trong kỳ 2:*
     $$\Delta_d = \frac{C_{ud} - C_{dd}}{S_{ud} - S_{dd}} = \frac{4.40 - 0}{86.40 - 64.80} = \frac{4.40}{21.60} \approx \mathbf{0.203704\text{ cổ phiếu}}$$
     $$B_d = \frac{0 - 0.203704(64.80)}{1.03} = \frac{-13.20}{1.03} \approx \mathbf{-\text{USD }12.815534}$$
  3. *Chứng minh Tự tài trợ:* Zeta **bán bớt** $0.605717 - 0.203704 = \mathbf{0.402014\text{ cổ phiếu}}$ tại giá $72$, thu về $+\text{USD }28.944984$ đem **trả bớt nợ vay**, làm dư nợ giảm từ $-41.760518$ về $-41.760518 + 28.944984 = \mathbf{-12.815534 = B_d}$! **Không tốn một xu tiền ngoài!**

#### Bước 3 & 4: Kiểm tra Khớp Payoff tại $t = 2$ & Chứng minh Chiến lược Tĩnh (Không Tái cân bằng) Thất Bại!
- **Với Tái cân bằng Động:**
  - Đường `uu`: $1.00(115.20) + 1.03(-79.611650) = 115.20 - 82.00 = \mathbf{33.20 = C_{uu}}$.
  - Đường `ud`: $1.00(86.40) + 1.03(-79.611650) = 86.40 - 82.00 = \mathbf{4.40 = C_{ud}}$.
  - Đường `du`: $0.203704(86.40) + 1.03(-12.815534) = 17.60 - 13.20 = \mathbf{4.40 = C_{du}}$.
  - Đường `dd`: $0.203704(64.80) + 1.03(-12.815534) = 13.20 - 13.20 = \mathbf{0.00 = C_{dd}}$.
- **Nếu BỎ QUA tái cân bằng (giữ lì $\Delta_0 = 0.605717, B_0 = -40.544192$ suốt 2 kỳ, nợ cuối năm thành $1.03^2 B_0 = -43.013333$):**
  - Tại `uu` ($115.20$): Danh mục chỉ có $0.605717(115.20) - 43.0133 = \mathbf{26.77 < 33.20}$ (**thiếu hụt $-\text{USD }6.43$**!).
  - Tại `ud` ($86.40$): Danh mục có $0.605717(86.40) - 43.0133 = \mathbf{9.32 > 4.40}$ (thừa $+\text{USD }4.92$).
  - Tại `dd` ($64.80$): Danh mục âm $\mathbf{-3.76 < 0.00}$ (**lỗ $-\text{USD }3.76$**!).
  $\implies$ Vì $\Delta$ thay đổi theo giá cổ phiếu và thời gian ($\Delta_u = 1 \ne \Delta_0 = 0.61 \ne \Delta_d = 0.20$), danh mục tĩnh một lần chỉ khớp được 2 trạng thái ở kỳ 1 chứ **không thể khớp đồng thời 3 trạng thái phi tuyến** ở kỳ 2!

---

## 3.4. Đòn bẩy Có Dấu ($\Omega$), Beta Quyền chọn ($\beta_{\text{opt}}$) & Thiết kế Danh mục Đạt Mục tiêu Beta

*(Mặc dù công thức này được giới thiệu ngay sau Black-Scholes trong L11 Cell 37 & Extra Session Cell 13, nó chỉ cần đầu vào là giá quyền chọn $V$ và hệ số $\Delta$ đã cho sẵn — hoặc tính từ cây nhị thức! — nên **RẤT DỄ XUẤT HIỆN Ở CẢ TỰ LUẬN (như Practice Q40) LẪN TRẮC NGHIỆM MCQ**!).*

### 1. Công thức Đòn bẩy Có Dấu ($\Omega$) và Beta Quyền chọn ($\beta_{\text{opt}}$)

Vì một quyền chọn trị giá $V$ được sao chép hoàn hảo trong ngắn hạn bởi danh mục $V = \Delta S + B$ (trong đó tỷ trọng đầu tư vào cổ phiếu là $w_S = \frac{S \Delta}{V}$, tỷ trọng tiền mặt phi rủi ro là $w_B = \frac{B}{V} = 1 - w_S$ với $\beta_B = 0$), beta của quyền chọn chính là trung bình trọng số beta của danh mục sao chép:

$$\boxed{\Omega = \frac{S \cdot \Delta}{V} \quad (\text{Signed Leverage Ratio / Option Elasticity})}$$
$$\boxed{\beta_{\text{opt}} = \Omega \cdot \beta_S = \frac{S \cdot \Delta}{V} \beta_S}$$

Và theo CAPM tức thời (Instantaneous CAPM — Extra Session Cell 14 & Practice Q40d), tỷ suất sinh lời kỳ vọng tức thời quy năm của quyền chọn hoặc danh mục là:
$$\boxed{E[r_{\text{opt}}] = r_f + \beta_{\text{opt}}\big(E[r_M] - r_f\big)}$$

**Ba Tính chất Sống Còn Cho MCQ (Giả sử cổ phiếu có $\beta_S > 0$):**
1. **Đối với Call Option ($\Delta_C > 0, B < 0$):** Vì $S\Delta_C = C - B > C \implies$ **$\Omega_C > 1$** (đòn bẩy dương lớn hơn 1; Call càng OTM thì $C$ càng nhỏ nên $\Omega_C$ càng khổng lồ!) $\implies \mathbf{\beta_C > \beta_S > 0}$ và $E[r_C] > E[r_S]$.
2. **Đối với Put Option ($\Delta_P < 0, B > 0$):** Vì $\Delta_P < 0 \implies$ **$\Omega_P < 0$** $\implies \mathbf{\beta_P < 0}$ (Beta mang dấu **ÂM**!) $\implies E[r_P] < r_f$ (thậm chí lợi suất kỳ vọng của Put thường âm vì nó hoạt động như hợp đồng bảo hiểm trả tiền đúng lúc thị trường sụp đổ!).
3. **Tính biến thiên động:** Khi giá cổ phiếu $S$ thay đổi, cả $\Delta$, đòn bẩy $\Omega$ lẫn $\beta_{\text{opt}}$ đều **thay đổi liên tục** (không phải hằng số như beta cổ phiếu thông thường!).

---

### 2. Kỹ thuật "Dollar Beta" Thiết kế Danh mục Cổ phiếu + Put + Tiền mặt Kèm Ràng buộc (Practice Question 40 — Theta)

Khi bài toán yêu cầu phân bổ tổng vốn $W_{\text{total}}$ vào $N_S$ cổ phiếu (giá $S$), $N_P$ quyền chọn Put (giá $P$, delta $\Delta_P < 0$) và giữ lại lượng tiền mặt cố định $\text{Cash}$ để đạt mức **Beta danh mục mục tiêu $\beta_{\text{target}}$**, hãy lập ngay **Hệ 2 Phương trình Tuyến tính 2 Ẩn $(N_S, N_P)$**:

1. **Phương trình Ngân sách (Budget Constraint):**
   $$S \cdot N_S + P \cdot N_P = W_{\text{total}} - \text{Cash}$$
2. **Phương trình Tổng Dollar Beta (Portfolio Beta Constraint):**  
   Vì $\beta_{\text{port}} = \sum w_i \beta_i = \frac{(S N_S)\beta_S + (P N_P)\beta_P + \text{Cash}\cdot 0}{W_{\text{total}}}$, nhân chéo $W_{\text{total}}$ lên (lưu ý mẹo siêu đẹp: $P \cdot \beta_P = P \cdot \frac{S\Delta_P}{P}\beta_S = S\Delta_P\beta_S$!):
   $$(S \cdot \beta_S) N_S + (P \cdot \beta_P) N_P = W_{\text{total}} \cdot \beta_{\text{target}} \quad \Longleftrightarrow \quad S \beta_S \big(N_S + \Delta_P N_P\big) = W_{\text{total}} \cdot \beta_{\text{target}}$$
3. **Kiểm tra Đầy Đủ Các Ràng Buộc (Constraints Check — Đừng bao giờ quên bước này!):**
   - Không bán khống / không đi vay: **$N_S \ge 0, \quad N_P \ge 0$**.
   - Ràng buộc phòng hộ không đầu cơ giá xuống ròng: **Số lượng Put không vượt quá số lượng cổ phiếu nắm giữ ($N_P \le N_S$)**!

**Ví dụ Mẫu Đầy Đủ (Practice Question 40 — Theta):**  
Cho $S = \text{USD }100, \beta_S = 1.25$; Put có $P = \text{USD }10, \Delta_P = -0.40$. Tổng vốn $W = \text{USD }100{,}000$, bắt buộc giữ $\text{Cash} = \text{USD }20{,}000$ ($\implies$ còn $\text{USD }80{,}000$ cho cổ phiếu + Put), cấm bán khống, ràng buộc **$N_P \le N_S$**:
- **Ý a (Đòn bẩy & Beta của Put):**
  $$\Omega_P = \frac{100 \times (-0.40)}{10} = \mathbf{-4.00}, \qquad \beta_P = (-4.00) \times 1.25 = \mathbf{-5.00}$$
- **Ý b (Tìm $N_S, N_P$ để đạt $\beta_{\text{target}} = 0.60$):**
  $$\begin{cases} 100 N_S + 10 N_P = 80{,}000 \\ (100 \times 1.25) N_S + (10 \times [-5.00]) N_P = 100{,}000 \times 0.60 \end{cases} \iff \begin{cases} 10 N_P = 80{,}000 - 100 N_S \\ 125 N_S - 50 N_P = 60{,}000 \end{cases}$$
  Thế $50 N_P = 5(80{,}000 - 100 N_S) = 400{,}000 - 500 N_S$ vào phương trình dưới:
  $$125 N_S - (400{,}000 - 500 N_S) = 60{,}000 \implies 625 N_S = 460{,}000 \implies \mathbf{N_S = 736\text{ cổ phiếu}}, \quad \mathbf{N_P = 640\text{ quyền chọn Put}}$$
  *Kiểm tra ràng buộc:* $N_S = 736 \ge 0$, $N_P = 640 \ge 0$, tổng chi $73{,}600 + 6{,}400 = 80{,}000$, và **$640 \le 736$ ($N_P \le N_S$ THỎA MÃN!)**.
- **Ý c (Có đạt được $\beta_{\text{target}} = 0.50$ không?):**
  - Giải hệ với vế phải $50{,}000$: $625 N_S = 450{,}000 \implies N_S = 720 \implies N_P = \frac{80{,}000 - 72{,}000}{10} = \mathbf{800 > 720}$ (**VI PHẠM ràng buộc $N_P \le N_S$!**).
  - *Chứng minh mức Beta thấp nhất có thể đạt được:* Beta nhỏ nhất xảy ra khi mua tối đa số Put cho phép trên mỗi cổ phiếu, tức chạm biên **$N_P = N_S = N$**:
    $$(100 + 10) N = 80{,}000 \implies N = \frac{80{,}000}{110} \approx 727.2727 \implies \beta_{\min} = \frac{727.2727 \times (125 - 50)}{100{,}000} = \frac{6}{11} \approx \mathbf{0.5455 > 0.50}$$
    Do đó, **KHÔNG THỂ** đạt mức beta $0.50$ dưới các ràng buộc đã cho!
- **Ý d (Tỷ suất sinh lời kỳ vọng CAPM tức thời của danh mục ý b với $r_f = 3\%, E[r_M] = 9\%$):**
  $$E[r_P] = 3\% + 0.60 \times (9\% - 3\%) = \mathbf{6.60\%/\text{năm}}$$

---

## 3.5. Ước lượng Độ biến động Mẫu (Sample Volatility), Quy tắc $\sqrt{T}$ & Nội suy Implied Volatility

### 1. Độ lệch Chuẩn Mẫu từ Dữ liệu Lịch sử & Quy tắc Căn bậc hai Thời gian (Practice Question 30)
Cho $n$ quan sát tỷ suất sinh lời ghép lãi liên tục (log returns) $r_1, r_2, \dots, r_n$:
1. **Trung bình mẫu:** $\bar{r} = \dfrac{1}{n}\sum_{t=1}^n r_t$.
2. **Độ lệch chuẩn mẫu một kỳ (Sample Standard Deviation — LUÔN CHIA CHO $n - 1$, KHÔNG CHIA $n$!):**
   $$\boxed{s_{\text{period}} = \sqrt{\frac{1}{n - 1} \sum_{t=1}^n (r_t - \bar{r})^2}}$$
3. **Quy tắc Căn bậc hai Thời gian (Square-Root-of-Time Rule — L11 Cell 30 & Extra Session Cell 6):**  
   Khi các log return qua các kỳ **không tự tương quan (uncorrelated)** và có **phương sai không đổi (constant variance)**, phương sai cộng tính theo thời gian ($\sigma_{k}^2 = k \sigma_1^2$), nên độ lệch chuẩn nhân với **$\sqrt{k}$**:
   - **Tháng $\to$ Năm:** $\sigma_{\text{annual}} = \sqrt{12} \, \sigma_{\text{monthly}}$.
   - **Tuần $\to$ Năm:** $\sigma_{\text{annual}} = \sqrt{52} \, \sigma_{\text{weekly}}$ *(và kỳ hạn $k$ tuần bất kỳ: $\sigma_{k\text{-week}} = \sqrt{k} \, \sigma_{\text{weekly}}$, ví dụ $13$ tuần $\implies \sqrt{13} \, \sigma_{\text{weekly}}$)*.
   - **Ngày $\to$ Năm (Quy ước chuẩn của môn BFIN):** Dùng **250 ngày giao dịch/năm**:
     $$\boxed{\sigma_{\text{annual}} = \sqrt{250} \, \sigma_{\text{daily}}}$$
   - *Minh họa Practice Q30:* 6 tuần log returns $[0.020, -0.010, 0.030, -0.020, 0.010, 0.000] \implies \bar{r} = 0.0050$; tổng bình phương độ lệch $= 0.001750$; chia cho **$n - 1 = 5$** được phương sai tuần $= 0.000350 \implies s_w = \sqrt{0.000350} \approx \mathbf{1.87\%}$ ($0.018708$). Quy năm: $0.018708 \times \sqrt{52} \approx \mathbf{13.49\%}$; 13 tuần: $0.018708 \times \sqrt{13} \approx \mathbf{6.75\%}$.

---

### 2. Nội suy Tuyến tính Tìm Độ biến động Ngụ ý (Linear Interpolation for Implied Volatility — Practice Question 36)
Trong 5 biến đầu vào của giá quyền chọn $(S_0, K, r, T, \sigma)$, duy nhất **$\sigma$ là biến không quan sát trực tiếp được**. Nếu đề cho bảng giá quyền chọn tính sẵn tại một số mức $\sigma$ và cho giá giao dịch thực tế $C_{\text{mkt}}$, ta kẹp $C_{\text{mkt}}$ giữa hai mức giá gần nhất $C(\sigma_1) < C_{\text{mkt}} < C(\sigma_2)$ rồi dùng **Công thức Nội suy Tuyến tính**:

$$\boxed{\sigma_{\text{imp}} \approx \sigma_1 + \frac{C_{\text{mkt}} - C(\sigma_1)}{C(\sigma_2) - C(\sigma_1)} \times (\sigma_2 - \sigma_1)}$$

- **Ví dụ Practice Q36 (Beta):** $C_{\text{mkt}} = \text{USD }10.40$ nằm giữa $\sigma_1 = 20\%$ ($C_1 = 9.413403$) và $\sigma_2 = 25\%$ ($C_2 = 11.348477$):
  $$\sigma_{\text{imp}} \approx 20\% + \frac{10.40 - 9.413403}{11.348477 - 9.413403} \times (25\% - 20\%) = 20\% + \frac{0.986597}{1.935074} \times 5\% \approx \mathbf{22.55\%}$$
- **Bẫy tư duy câu `b` (Tại sao $\sigma_{\text{imp}} = 22.55\% > \sigma_{\text{hist}} = 18\%$ KHÔNG đảm bảo bán Call chắc chắn có lời?):**
  1. $\sigma_{\text{hist}} = 18\%$ chỉ đo biến động **trong quá khứ**, còn giá trị quyền chọn phụ thuộc vào biến động **sẽ thực sự xảy ra trong tương lai** (thị trường có thể đang định giá đúng một sự kiện lớn sắp tới như công bố lợi nhuận, sáp nhập, chính sách lãi suất).
  2. Ngay cả khi biến động thực tế thấp hơn, việc phòng hộ trong thực tế chịu rủi ro bước nhảy giá, giao dịch rời rạc và chi phí giao dịch, nên chênh lệch giữa Implied Volatility và Historical Volatility là sự khác biệt về kỳ vọng/phần bù rủi ro chứ **KHÔNG PHẢI cơ hội Arbitrage phi rủi ro**!

---

## 3.6. CHUYÊN MỤC ĐẶC BIỆT DÀNH RIÊNG CHO 10 CÂU MCQ: TINH HOA KHÁI NIỆM BLACK-SCHOLES & AMERICAN OPTIONS

> [!IMPORTANT]
> **Nhắc lại Chiến lược Phòng thi:** Bạn **không phải bấm tay công thức BSM hay giải cây American Options trong 5 bài toán tự luận**, nhưng Dr. Cayirli dành rất nhiều tâm huyết giảng giải **trực giác hình học và kinh tế** của hai chủ đề này trong Lecture 10, Lecture 11 và đặc biệt là buổi **Extra Session**. Dưới đây là toàn bộ các mệnh đề cốt lõi có xác suất cao nhất xuất hiện trong **10 câu Trắc nghiệm MCQ**!

### PHẦN A — 6 Tinh hoa Khái niệm của Mô hình Black–Scholes–Merton (BSM)

1. **Năm Giả định Cốt lõi & Hạn chế Thực tế (L11 Cell 27 & Extra Session Cell 3):**
   - Không có cơ hội Arbitrage; Quyền chọn là kiểu **Châu Âu** trên cổ phiếu không trả cổ tức; Lãi suất phi rủi ro liên tục $r_f$ và độ biến động $\sigma$ là **hằng số đã biết**, giá tài sản biến thiên liên tục **không có bước nhảy đột ngột (no jumps)** *(tương ứng với cây nhị thức có $u, d$ cố định qua các bước thời gian bằng nhau khi số bước $n \to \infty$)*; Không thuế/chi phí giao dịch, chứng khoán chia nhỏ tùy ý, bán khống tự do.
   - **Điểm yếu của giả định giao dịch liên tục (Continuous trading):** Khi thị trường mở cửa thì xấp xỉ tốt, nhưng **thị trường có đóng cửa qua đêm / cuối tuần** (giá mở cửa hôm sau có thể nhảy gap), khiến việc tái cân bằng liên tục không thể hoàn hảo 100% ngoài đời thực.

2. **Giải phẫu Ý nghĩa Kinh tế Từng Thành phần trong Công thức BSM (Extra Session Cells 4–6, 11):**
   $$C_t = S_t \underbrace{N(d_1)}_{\Delta_C} - \underbrace{PV(K) N(d_2)}_{\text{Khoản Vay } (-B)}, \qquad P_t = \underbrace{PV(K)[1 - N(d_2)]}_{\text{Khoản Cho vay } (+B)} + \underbrace{[N(d_1) - 1]}_{\Delta_P} S_t$$
   Với $PV(K) = K e^{-r_f(T-t)}$, $d_1 = \dfrac{\ln(S_t / PV(K))}{\sigma\sqrt{T-t}} + \dfrac{\sigma\sqrt{T-t}}{2}$ và $d_2 = d_1 - \sigma\sqrt{T-t}$:
   - **$N(d)$** là hàm phân phối tích lũy chuẩn tắc $\Pr(Z \le d)$, luôn nằm chặt trong khoảng **$(0, 1)$** với mọi $d$ hữu hạn. Vì $\sigma\sqrt{T-t} > 0 \implies$ **luôn luôn có $d_1 > d_2$ và $N(d_1) > N(d_2)$**!
   - **$N(d_1) = \Delta_C = \frac{\partial C}{\partial S} \in (0, 1)$:** Là **Delta của Call** (độ dốc cục bộ của đường giá Call và cũng là số cổ phiếu cần mua để sao chép 1 Call). Delta của Put là **$\Delta_P = N(d_1) - 1 = -N(-d_1) \in (-1, 0)$** *(lưu ý đẳng thức đẹp từ Put-Call Parity: $\Delta_C - \Delta_P = 1$)*.
   - **$N(d_2) = \Pr^{\mathbb{Q}}(S_T > K)$:** Là **xác suất trung lập rủi ro để Call kết thúc ở trạng thái In-the-Money lúc đáo hạn**! *(Cực dễ bẫy MCQ: Hỏi xác suất trung lập rủi ro đáo hạn ITM của Call là $N(d_1)$ hay $N(d_2)$? Đáp án bắt buộc là **$N(d_2)$**, còn của Put là **$1 - N(d_2) = N(-d_2)$**!).*
   - **$-PV(K)N(d_2)$:** Là vị thế tiền mặt đi vay trong danh mục sao chép Call; còn **$+PV(K)[1 - N(d_2)]$** là vị thế cho vay trong danh mục sao chép Put.

3. **Các Giới hạn Biên Suy biến của BSM (Extra Session Cell 8):**
   - Khi tiến sát ngày đáo hạn ($\tau = T - t \to 0$): $C \to \max(S - K, 0)$ và $P \to \max(K - S, 0)$.
   - Khi độ biến động tiến về không ($\sigma \to 0$, tài sản trở thành tất định): $C \to \max(S - PV(K), 0)$ và $P \to \max(PV(K) - S, 0)$.
   - Khi quyền chọn rất sâu trong tiền ($S \to \infty$): $d_1, d_2 \to +\infty \implies N(d_1) \to 1$ (Call biến động 1:1 như cổ phiếu) và $\Delta_P \to 0$. Khi $S \to 0$: $C \to 0, P \to PV(K), \Delta_C \to 0, \Delta_P \to -1$.

4. **Đường Tiếp Tuyến Cục Bộ & Lỗi Lồi Gamma Khi Giá Nhảy Mạnh (Extra Session Cells 11–12 & Practice Q35):**
   - Đường giá trị quyền chọn $V(S)$ là một **đường cong LỒI hướng lên (strictly convex curve, Gamma $= \frac{\partial^2 V}{\partial S^2} > 0$)** nằm phía trên mọi đường tiếp tuyến của nó!
   - Danh mục cổ phiếu + tiền mặt cố định $V_{\text{rep}}(S) = \Delta_0 S + B_0$ chỉ là **đường thẳng tiếp tuyến** chạm vào đường cong $V(S)$ tại mức giá hiện tại $S_0$ (khớp cả giá trị lẫn độ dốc tại $S_0$).
   - **Hệ quả vàng cho MCQ:** Nếu giá cổ phiếu nhảy vọt một bước lớn (dù nhảy **TĂNG** như từ $84 \to 90$ ở Practice Q35b, hay nhảy **GIẢM**!) mà danh mục sao chép **chưa kịp tái cân bằng**, đường cong quyền chọn thực tế luôn uốn cong nằm **CAO HƠN** đường thẳng tiếp tuyến cố định $\implies$ **$V_{\text{repriced}}(S_1) > \Delta_0 S_1 + B_0$**! (Người giữ Long Option lời hơn danh mục tĩnh; người bán Short Option phòng hộ tĩnh sẽ bị **thiếu hụt tiền**!).

5. **Chỉ số VIX (CBOE Volatility Index — Extra Session Cell 10):**
   - VIX đo lường **kỳ vọng độ biến động ngụ ý (implied volatility) trong 30 ngày tới của chỉ số S&P 500** (báo cáo theo tỷ lệ % năm), được trích xuất từ giá thị trường của rổ quyền chọn S&P 500. VIX thường được gọi là "thước đo nỗi sợ" vì vọt tăng mạnh trong các đợt hoảng loạn tài chính.

6. **Không Nhầm Lẫn Giữa Xác suất Trung lập Rủi ro ($p, N(d_2)$) và Xác suất Dự báo Thực tế ($p_{\text{physical}}$) (Practice Question 37):**
   - *"Cây nhị thức tính ra $p = 48\%$, nên mô hình kinh tế lượng dự báo xác suất cổ phiếu tăng $60\%$ chắc chắn bị sai"* $\implies$ **MỆNH ĐỀ SAI HOÀN TOÀN!**
   - $p = 48\%$ **không phải xác suất xảy ra ngoài đời thực**, mà là trọng số điều chỉnh rủi ro (risk-adjusted weight) ép tỷ suất sinh lời kỳ vọng của cổ phiếu bằng $r_f$ để định giá không arbitrage. Ngoài đời thực, nhà đầu tư ngại rủi ro đòi hỏi phần bù rủi ro dương trên cổ phiếu ($\mu > r_f$), nên xác suất tăng giá thực tế $p_{\text{physical}} = 60\% > p = 48\%$ là hoàn toàn hợp lý và nhất quán!
   - Tương tự: Implied volatility $28\%$ là mức độ biến động thị trường đang định giá vào quyền chọn hôm nay (bao gồm cả phần bù rủi ro biến động), **không đảm bảo** biến động thực hiện (realized volatility) năm tới chắc chắn bằng đúng $28\%$!

---

### PHẦN B — Ba Quy Tắc Vàng Về Thực Thi Sớm Quyền Chọn Kiểu Mỹ (American Options Early Exercise Rules)

Nguyên lý gốc tại mọi nút trước đáo hạn: Quyền chọn Mỹ có giá trị bằng $V_A = \max(\text{Intrinsic Value}, \, \text{Continuation Value } H)$, và chỉ thực thi sớm khi **$\text{Intrinsic Value} \ge H$**.

#### Quy tắc 1: American Call trên Cổ phiếu KHÔNG Trả Cổ tức ($r \ge 0$) $\implies$ KHÔNG BAO GIỜ THỰC THI SỚM!
- Từ Put-Call Parity: $C_E = S_0 - PV(K) + P_E = (S_0 - K) + \underbrace{[K - PV(K)]}_{\text{Tiền lãi tiết kiệm } \ge 0} + \underbrace{P_E}_{\text{Bảo hiểm } \ge 0}$.
- Nếu thực thi sớm hôm nay, bạn chỉ nhận được $S_0 - K$: bạn vừa **tự vứt bỏ tiền lãi** $[K - PV(K)]$ từ việc hoãn trả tiền mặt $K$, vừa **tự hủy tấm bảo hiểm giảm giá** $P_E$ (nếu cổ phiếu sau đó sập xuống dưới $K$, cầm cổ phiếu lỗ nặng còn cầm Call chỉ mất tối đa phí)!
- Nếu muốn thoát vị thế lấy tiền mặt hôm nay, **bán lại quyền chọn Call trên thị trường** luôn thu được $C_A = C_E > S_0 - K$ (lợi hơn thực thi sớm!).
- **Hệ quả tất yếu cho MCQ:** Với cổ phiếu không cổ tức và $r \ge 0$, **$C_{\text{American}} = C_{\text{European}}$** và **Early-exercise premium $= 0$**!

#### Quy tắc 2: American Call trên Cổ phiếu CÓ Trả Cổ tức Tiền mặt $D$ (L10 Cells 21–22 & Practice Question 22)
- Nếu có thực thi sớm để giành lấy cổ tức $D$, thời điểm duy nhất hợp lý là **ngay sát trước thời khắc giao dịch không hưởng quyền (immediately before the ex-dividend date)** (thực thi sớm hơn mốc đó chỉ làm mất oan tiền lãi trên $K$ mà không được thêm lợi ích gì!).
- Giả sử ngay trước khi chia cổ tức $D$ (sau đó không còn đợt cổ tức nào nữa), giá cổ phiếu là $S_{\text{cum}}$, sau khi chia cổ tức giá rớt xuống $S_{\text{ex}} = S_{\text{cum}} - D$, và quyền chọn Put Châu Âu tương ứng ngay sau chia cổ tức có giá $P_{\text{ex}}$:
  - Giá trị nếu **Thực thi ngay**: $I_{\text{now}} = S_{\text{cum}} - K$.
  - Giá trị nếu **Giữ tiếp qua ngày chia cổ tức**: $C_{\text{cont}} = C_E(S_{\text{ex}}) = S_{\text{ex}} + P_{\text{ex}} - PV(K) = (S_{\text{cum}} - D) + P_{\text{ex}} - PV(K)$.
  - Lấy hiệu hai vế, ta có **Công thức Vàng Đánh Giá Lợi Ích Thực Thi Sớm**:
    $$\boxed{\text{Exercise Advantage} = I_{\text{now}} - C_{\text{cont}} = D - \big[K - PV(K)\big] - P_{\text{ex}}}$$

> [!WARNING]
> **BẪY MCQ CỰC ĐỘC TỪ PRACTICE QUESTION 22 (IOTA):**  
> Một cố vấn khuyên thực thi sớm ngay vì thấy cổ tức $D = \text{USD }1.60$ lớn hơn tiền lãi mất đi $K - PV(K) = 80 - \frac{80}{(1.04)^{0.5}} = \text{USD }1.5535$.  
> **Đánh giá:** Lời khuyên này **SAI!** Vì điều kiện $D > K - PV(K)$ chỉ là **ĐIỀU KIỆN CẦN chứ CHƯA ĐỦ**! Cố vấn đã bỏ quên giá trị bảo hiểm còn lại $P_{\text{ex}} = \text{USD }0.25$! Thực tế:
> $$I_{\text{now}} - C_{\text{cont}} = 1.60 - 1.5535 - 0.25 = \mathbf{-\text{USD }0.2035 < 0} \quad (12.60 < 12.8035)$$
> Nên **KHÔNG ĐƯỢC thực thi sớm** (phải giữ tiếp!). Mức cổ tức tối thiểu để bàng quan phải bằng tổng cả tiền lãi lẫn giá trị Put: **$D^* = [K - PV(K)] + P_{\text{ex}} = 1.5535 + 0.25 = \text{USD }1.8035$**!

#### Quy tắc 3: American Put trên Cổ phiếu KHÔNG Trả Cổ tức (L10 Cell 20, Extra Session Cell 32 & Practice Question 38)
- **CÓ THỂ tối ưu thực thi sớm** khi quyền chọn ở trạng thái **Rất sâu trong tiền (Deep ITM, $S_t$ rất thấp)** và lãi suất $r > 0$: vì lúc này thực thi ngay giúp cầm tiền mặt $K$ về sớm gửi ngân hàng ăn lãi $rK$, trong khi khả năng cổ phiếu tăng vọt ngược lên trên $K$ quá thấp và cổ phiếu cũng không thể giảm xuống dưới $0$ ($\implies P_{\text{American}} \ge P_{\text{European}}$). *(Nếu cổ phiếu có trả cổ tức $D$, việc thực thi sớm American Put lại **kém hấp dẫn hơn** vì chờ qua ngày chia cổ tức giá cổ phiếu tự tụt xuống có lợi cho Put!).*
- **Hai Bẫy Chết Người Trong MCQ Về American Put (Practice Question 38 — Delta):**
  1. **Bẫy 1 — *"Cứ hễ American Put đang In-the-Money ($S_t < K$) ở kỳ trung gian là nên thực thi sớm"*:** **SAI HOÀN TOÀN!** Ở nút chỉ hơi ITM (ví dụ $S_u = 75 < K = 76 \implies$ thực thi ngay chỉ được $I_u = \text{USD }1.00$, trong khi giữ tiếp chờ năm 2 có giá trị $H_u = \text{USD }8.02$!), thực thi sớm mù quáng sẽ vứt sọt rác $\text{USD }7.02$ giá trị thời gian! Chỉ thực thi khi **$K - S_t \ge H_t$**!
  2. **Bẫy 2 — Thay nhầm $P_{\text{American}}$ vào công thức Put-Call Parity của Châu Âu:** Vì $P_A = P_E + \text{Early-Exercise Premium} > P_E$, nếu ai lấy $S_0 + P_A - PV(K)$ để tính giá Call thì sẽ **ước lượng THỪA (overstate)** giá Call đúng bằng phần Early-Exercise Premium $(P_A - P_E)$! Put-Call Parity dạng dấu bằng chỉ dành riêng cho cặp quyền chọn Châu Âu!

---

# PHẦN CUỐI — BỘ 6 PHÁC ĐỒ "NHÌN ĐỀ BIẾT CÁCH GIẢI TRONG 10 GIÂY" CHO BÀI TỰ LUẬN DERIVATIVES 3 Ý (`a, b, c`)

Trong phòng thi 75 phút, mỗi bài toán tự luận Derivatives luôn được thiết kế theo **cấu trúc leo thang 3 tầng (`a` $\to$ `b` $\to$ `c`)**:
- **Ý `a` (Nền tảng — 30% điểm):** Tính giá lý thuyết không arbitrage / khôi phục tham số ẩn.
- **Ý `b` (Thực thi — 45% điểm):** Lập bảng dòng tiền Arbitrage / Sổ cái Ký quỹ / Tái cân bằng Danh mục / Định giá lại khi thông số thay đổi.
- **Ý `c` (Bản chất & Bẫy thực tế — 25% điểm):** Bắt lỗi lập luận sai của một nhân vật giả định (Tau, Zeta, Eta, Omicron...) hoặc kiểm tra điều kiện ràng buộc / rủi ro còn sót lại.

Ngay khi lật đề, hãy đối chiếu từ khóa với **6 Phác đồ Tác chiến** dưới đây để kích hoạt lời giải trong vòng 10 giây:

---

### PHÁC ĐỒ #1: ĐỊNH GIÁ FORWARD (CIP / CHỈ SỐ / HÀNG HÓA) + ĐỊNH GIÁ LẠI GIỮA KỲ + ARBITRAGE TỰ TÀI TRỢ
- **Dấu hiệu nhận diện trong 3 giây:** Xuất hiện *spot exchange rate (`USD per EUR`), continuous dividend yield theo từng đoạn, commodity convenience yield, hoặc termination offer sau vài tháng*.
- **Lộ trình Giải `a → b → c` Chuẩn Điểm Tối Đa:**
  - **Ý `a` (Tính $F^*$ hoặc tìm ngược lãi suất/dividend yield):**
    - Kiểm tra kỹ kiểu ghép lãi: **EAR** dùng $(1+r)^T$, **Continuous** dùng $e^{rT}$.
    - Ngoại tệ `USD per EUR` ($\text{USD}/\text{EUR}$): Tử `USD`, Mẫu `EUR` $\implies F^* = S_0 \frac{(1+r_{\text{USD}})^T}{(1+r_{\text{EUR}})^T}$ hoặc $S_0 e^{(r_{\text{USD}}-r_{\text{EUR}})T}$.
    - Chỉ số 2 giai đoạn cổ tức: $\ln(F_0/S_0) = (r - q_1)T_1 + (r - q_2)T_2$.
  - **Ý `b` (Định giá lại hợp đồng cũ tại $t$ HOẶC Lập bảng Arbitrage):**
    - *Nếu định giá lại hợp đồng cũ:* Giữ nguyên $K = F_0$ ban đầu, chiết khấu theo **lãi suất mới $r_{\text{new}}$** và **thời gian còn lại $T - t$**: $V_t(\text{Long}) = N \times \big[S_t - PV_t(D_{\text{rem}}) - PV_{t,\text{new}}(K)\big]$. So sánh với tiền đền bù hủy hợp đồng!
    - *Nếu lập bảng Arbitrage ngoại tệ ($CF_0 = 0$ ở cả 2 đồng tiền):* Nếu $F_{\text{mkt}} > F^*$, Vay USD $\to$ Mua EUR spot ($E_0$) $\to$ Gửi EUR nở thành **$E_T = E_0(1+r_{\text{EUR}})^T$** $\to$ Bán Forward **ĐÚNG SỐ $E_T$** (cả gốc lẫn lãi!).
  - **Ý `c` (Phản biện đề xuất sai / Hàng hóa thực tế):**
    - Nếu nhân vật ký Forward bằng gốc $E_0$ thay vì $E_T$ (hoặc đi ngược chiều vay): viết phương trình dòng tiền theo $S_T$ để chứng minh vị thế **còn hở rủi ro tỷ giá $S_T$** (đầu cơ chứ không phải arbitrage!).
    - Nếu hàng hóa có $F_{\text{mkt}} < S_0 e^{rT}$: chỉ ra Reverse Cash-and-Carry thất bại vì không bán khống được hàng vật chất và chủ kho cần giữ hàng cho sản xuất (hưởng convenience yield $y$).

---

### PHÁC ĐỒ #2: SỔ CÁI KÝ QUỸ FUTURES (MARKING-TO-MARKET LEDGER) & BẪY THANH KHOẢN PHÒNG HỘ
- **Dấu hiệu nhận diện trong 3 giây:** Xuất hiện *Initial Margin ($IM$), Maintenance Margin ($MM$), bảng Settlement prices theo ngày (có thể khuyết 1 ô `?`), đóng vị thế ở ngày cuối*.
- **Lộ trình Giải `a → b → c` Chuẩn Điểm Tối Đa:**
  - **Bước chuẩn bị (2 giây):** Tính tổng quy mô $N = n \times Q$. Gạch chân vị thế (**Long** dùng $F_t - F_{t-1}$; **Short** dùng $F_{t-1} - F_t$ — cực dễ nhầm dấu Short!) và điều kiện gọi ký quỹ (**`strictly below` $< MM$** thì chạm đúng $MM$ **KHÔNG nộp thêm**!).
  - **Ý `a` (Hoàn thiện bảng & Khôi phục giá ẩn):**
    - Tại ngày khuyết giá: lấy $\text{P\&L}_t = \text{Bal}_{\text{before},t} - \text{Closing}_{t-1}$, rồi chia cho $\pm nQ$ để suy ra $F_t$.
    - Khi kích hoạt Margin Call: nộp bù về đúng **$IM$** ($\text{Deposit}_t = IM - \text{Bal}_{\text{before},t}$).
  - **Ý `b` (Đối chiếu 3 con số tiền mặt):**
    - $\text{Total External Cash In} = IM + \sum \text{Deposits}$; $\text{Cash Released} = \text{Final Closing Balance}$.
    - Kiểm tra bắt buộc: $\text{Cash Released} - \text{Total External Cash In} = \pm nQ(F_{\text{close}} - F_0) = \sum \text{Daily P\&L}$.
  - **Ý `c` (Tư vấn chọn Forward vs. Futures cho doanh nghiệp sản xuất):**
    - Doanh nghiệp sẽ **bán hàng** trong tương lai $\implies$ phải **Short** (chống giảm giá). Nếu không có hạn mức tiền mặt đóng Margin Call khi giá hàng hóa tăng tạm thời trước ngày giao hàng, bắt buộc chọn **Short Forward** thay vì Short Futures!

---

### PHÁC ĐỒ #3: HOÁN ĐỔI LÃI SUẤT (IRS) & HOÁN ĐỔI TIỀN TỆ (CURRENCY SWAP) + RỦI RO CƠ SỞ / RỦI RO TỶ GIÁ DƯ
- **Dấu hiệu nhận diện trong 3 giây:** Xuất hiện *Fixed-for-floating swap, year fraction $\Delta = 0.25$ hoặc $0.5$, hoặc Fixed-for-fixed currency swap trao đổi gốc hai đầu*.
- **Lộ trình Giải `a → b → c` Chuẩn Điểm Tối Đa:**
  - **Ý `a` (Tính dòng tiền từng chân / Khôi phục lãi suất $K$ hoặc $L_k$):**
    - Với IRS: $\text{Fixed} = N K \Delta$, $\text{Floating}_k = N L_k \Delta$, không trao đổi gốc $N$. Muốn biến khoản vay thả nổi $L + s$ thành cố định $\implies$ vào Swap **Trả cố định $K$, Nhận $L$** (chi phí gộp $= K + s$).
    - Với Currency Swap: Tính vốn gốc $N_{\text{EUR}} = N_{\text{USD}} / S_0$; lãi năm $= \text{Notional} \times r_{\text{swap}}$.
  - **Ý `b` (Ghép Khoản Vay + Swap lập bảng dòng tiền ròng):**
    - Với Currency Swap, nhớ tách 3 dòng rõ ràng: **Inception ($t=0$)** trao đổi gốc, **Years $1 \dots T-1$** trả/nhận lãi, **Maturity ($t=T$)** trả/nhận **CẢ LÃI LẪN ĐẢO NGƯỢC VỐN GỐC**! Khi lãi vay USD khớp đúng lãi USD của Swap, mọi dòng USD bằng $0$, chi phí vay EUR hiệu dụng $= r_{\text{swap,EUR}}$.
  - **Ý `c` (Định lượng Rủi ro Còn Sót Lại khi Không Khớp Hoàn Hảo):**
    - *Với IRS (Basis Risk):* Khoản vay gắn với $M + s$ nhưng Swap nhận $L$ $\implies$ Lãi suất gộp $= (K + s) + (M - L)$ — **không cố định** mà biến động theo $(M - L)$!
    - *Với Currency Swap:* Lãi vay USD cao hơn lãi USD nhận từ Swap ($r_{\text{loan}} > r_{\text{swap,USD}}$) $\implies$ Vốn gốc cuối kỳ vẫn triệt tiêu, nhưng mỗi năm phát sinh khoản thiếu hụt USD cố định $N_{\text{USD}}(r_{\text{loan}} - r_{\text{swap,USD}})$ làm tổng chi phí quy ra EUR phụ thuộc tỷ giá tương lai!

---

### PHÁC ĐỒ #4: CHIẾN LƯỢC QUYỀN CHỌN (SPREAD / STRADDLE-STRANGLE / BUTTERFLY $\Delta\text{SLOPE}$ / COLLAR)
- **Dấu hiệu nhận diện trong 3 giây:** Cho bảng Strike & Premium của các Call/Put cùng đáo hạn, yêu cầu dựng hàm Payoff mục tiêu, tính Breakeven, Max Profit/Loss, hoặc chọn chiến lược thỏa ngân sách phí & sàn bảo vệ.
- **Lộ trình Giải `a → b → c` Chuẩn Điểm Tối Đa:**
  - **Bước chuẩn bị:** Kiểm tra ngay đề hỏi **per share** hay **total position** (nhân $100\text{ cp/contract} \times \text{số hợp đồng}$!).
  - **Ý `a` (Xác lập số lượng quyền chọn & Chi phí ban đầu):**
    - Nếu dựng hàm Payoff tuyến tính từng khúc bằng Call: tính độ dốc từng đoạn rồi áp công thức **$n_i = \text{Slope}_{\text{sau } K_i} - \text{Slope}_{\text{trước } K_i}$**!
    - Nếu tìm chiến lược bảo vệ $N$ cổ phiếu có sàn giá trị tối thiểu và trần ngân sách phí: chọn Put có strike $K_L$ đúng bằng mức sàn/cp, rồi **bán kèm Call $K_H$ (Collar)** sao cho $N(P_L - C_H) \le \text{Ngân sách}$.
  - **Ý `b` (Tính Max Profit, Max Loss, Breakeven $S_T^*$):**
    - Cho $\text{Profit}(S_T) = \text{Payoff}(S_T) - d = 0$ trên từng nhánh dốc khác $0$ để giải ra chính xác mọi điểm hòa vốn $S_T^*$ (Straddle, Strangle, Butterfly đều có **2 điểm hòa vốn**!).
  - **Ý `c` (Phân tích Đánh đổi Kinh tế — Trade-off):**
    - Strangle vs. Straddle: Giảm chi phí ban đầu & lỗ tối đa, đổi lại biên hòa vốn bị đẩy ra xa hơn và lãi thấp hơn khi biến động cực lớn.
    - Collar vs. Protective Put: Tiết kiệm phí mua bảo hiểm nhờ tiền bán Call, đổi lại hy sinh toàn bộ phần lợi nhuận cổ phiếu tăng vượt trên trần $K_H$.

---

### PHÁC ĐỒ #5: PUT-CALL PARITY, SYNTHETIC FORWARD & OPTION BOUNDS + BẢNG ARBITRAGE 2 MIỀN GIÁ
- **Dấu hiệu nhận diện trong 3 giây:** Cho giá Call, Put (và Forward hoặc $S_0$), hỏi *pricing inconsistency / synthetic forward / arbitrage cash-flow table*.
- **Lộ trình Giải `a → b → c` Chuẩn Điểm Tối Đa:**
  - **Ý `a` (Phát hiện điểm lệch giá):**
    - Nếu cho Call, Put cùng $K$ và Forward (không cho $S_0$): Dựng **Zero-cost Synthetic Long Forward** (Mua Call $K$, Bán Put $K$, Vay $C - P$) $\implies$ Giá giao hàng ngụ ý **$K_{\text{imp}} = K + (C - P)(1+r)^T$** (hoặc $e^{rT}$). So sánh $K_{\text{imp}}$ với $F_{\text{mkt}}$!
    - Nếu cho $S_0$ và nhiều quyền chọn: Kiểm tra lần lượt (1) Chặn dưới Call $C \ge \max(0, S_0 - PV(K))$, (2) Chặn dưới Put $P \ge \max(0, PV(K) - S_0)$, (3) Put-Call Parity $C - P = S_0 - PV(D) - PV(K)$, (4) Spread bound $C_L - C_H \le PV(K_H - K_L)$.
  - **Ý `b` (Kẻ Bảng Dòng Tiền Arbitrage Chuẩn 4 Cột):**
    - Bắt buộc kẻ đủ 4 cột: **`Transaction` | `Today (t=0)` | `At T if S_T <= K` | `At T if S_T > K`**.
    - Cộng tổng dòng cuối (`Net Cash Flow`): chứng minh tất cả các chữ $S_T$ triệt tiêu (hoặc với bài vi phạm chặn dưới tự tài trợ $CF_0 = 0$: chứng minh dòng cuối luôn $\ge \text{Min Profit} > 0$ ở cả hai miền!).
  - **Ý `c` (Mức giá cân bằng xóa bỏ Arbitrage / Mô hình Merton nếu ghép tài chính doanh nghiệp):**
    - Nếu là bài Merton: $E_0 = \text{Call}(V_0, F, T)$, $D_0 = V_0 - E_0$, Promised yield $y = (F/D_0)^{1/T} - 1$, Credit spread $= y - r_{f,\text{eff}}$.

---

### PHÁC ĐỒ #6: CÂY NHỊ THỨC CHÂU ÂU 2 KỲ (NHÂN TÍNH VS. CỘNG TÍNH) + PHÒNG HỘ ĐỘNG $(\Delta, B)$ & DANH MỤC BETA ($\Omega$)
- **Dấu hiệu nhận diện trong 3 giây:** Cổ phiếu tăng/giảm qua 2 thời kỳ (theo $\%$ hoặc theo $\text{USD}$), hỏi giá quyền chọn Châu Âu, tái cân bằng tự tài trợ ở kỳ giữa, hoặc ghép cổ phiếu + quyền chọn đạt $\beta_{\text{target}}$.
- **Lộ trình Giải `a → b → c` Chuẩn Điểm Tối Đa:**
  - **Bước Kiểm tra Sống Còn (5 giây đầu tiên):**
    1. Đổi lãi suất năm sang **Hệ số gộp 1 bước $R$** (EAR: $(1+r_{\text{eff}})^{\Delta t}$; APR ghép $m$ lần: $1 + r_{\text{nom}}/m$; Liên tục: $e^{r_c \Delta t}$). Nhớ mỗi bước lùi chỉ chia cho **$R$ một lần**!
    2. Nhìn quy luật nhảy giá: **Tăng/giảm theo $\%$** $\implies$ $p = \frac{R-d}{u-d}$ cố định toàn cây; **Tăng/giảm số tiền USD cố định** $\implies$ Cây Cộng Tính, **BẮT BUỘC tính riêng 3 xác suất** $p_0, p_u, p_d$ bằng công thức $p_{\text{node}} = \dfrac{R \cdot S_{\text{node}} - S_{\text{down}}}{S_{\text{up}} - S_{\text{down}}}$!
  - **Ý `a` (Định giá Cây & Danh mục ban đầu):**
    - Tính $V_{uu}, V_{ud}, V_{dd} \to V_u, V_d \to V_0$. Nếu cần phòng hộ tại $t=0$: $\Delta_0 = \frac{V_u - V_d}{S_u - S_d}$ và $B_0 = V_0 - \Delta_0 S_0$.
  - **Ý `b` (Tái cân bằng Tự tài trợ tại $t=1$ HOẶC Bắt lỗi Bảng tính sai):**
    - Tại mỗi nút $u$ và $d$: Tính $(\Delta_u, B_u)$ và $(\Delta_d, B_d)$. Viết rõ đẳng thức tự tài trợ: giá trị trước tái cân bằng $\Delta_0 S_u + R B_0 = V_u = \Delta_u S_u + B_u$ (mua thêm cổ phiếu $(\Delta_u - \Delta_0)S_u$ được tài trợ 100% bằng vay thêm tiền, dòng tiền ngoài $= 0$!).
    - Nếu là bài Thiết kế Danh mục Beta: Tính $\Omega = \frac{S\Delta}{V}$, $\beta_{\text{opt}} = \Omega \beta_S$, giải hệ 2 phương trình $(S N_S + P N_P = W - \text{Cash})$ và $(S\beta_S N_S + P\beta_{\text{opt}} N_P = W \beta_{\text{target}})$.
  - **Ý `c` (Chứng minh Danh mục Tĩnh Thất Bại / Kiểm tra Ràng buộc $N_P \le N_S$):**
    - Tính $\Delta_0 S_{\text{terminal}} + R^2 B_0$ tại `uu, ud, dd` để chỉ ra số tiền lệch cụ thể so với payoff quyền chọn khi không tái cân bằng.
    - Với bài Beta: Kiểm tra $N_S \ge 0, N_P \ge 0$ và **$N_P \le N_S$**; nếu vi phạm, cho $N_P = N_S = \frac{W - \text{Cash}}{S + P}$ để chứng minh mức $\beta_{\min}$ khả thi!

---

*Chúc bạn bước vào phòng thi ngày 12/11/2026 với tâm thế làm chủ tuyệt đối từng con số, bóc tách mọi cái bẫy ngay từ dòng đầu tiên và giành trọn điểm tối đa ở toàn bộ mặt trận Derivatives!*
