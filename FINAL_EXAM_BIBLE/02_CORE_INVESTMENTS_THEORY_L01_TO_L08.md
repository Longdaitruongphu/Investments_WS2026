# VOLUME 02: BÁCH KHOA TOÀN THƯ LÝ THUYẾT & PHƯƠNG PHÁP GIẢI NHANH — CORE INVESTMENTS (LECTURES 01 – 08)

**Môn học:** BFIN — Investments (Fall / WS 2026) — Giảng viên: Dr. Omer Cayirli  
**Giáo trình nền tảng:** Bodie, Kane & Marcus (*Investments*, 12th International Student Edition — BKM) & Toàn bộ Slide/Practice Notebooks WS2026  
**Phạm vi tài liệu:** Hệ thống hóa **100% kiến thức lý thuyết, trực giác kinh tế, công thức chuẩn, quy trình bấm máy giải nhanh và bẫy MCQ/tự luận** xuyên suốt **Lectures 01 – 08** (Môi trường đầu tư, Định giá trái phiếu & Cấu trúc kỳ hạn, Duration/Convexity/Immunization, Lợi suất/Rủi ro/Hữu dụng/CAL, Đa dạng hóa Markowitz, SIM & CAPM, Đa nhân tố/APT/Fama-French/ESG, Hiệu quả thị trường EMH & Tài chính hành vi).

> [!IMPORTANT]
> ** TỶ TRỌNG ĐIỂM SỐ TRONG ĐỀ THI CUỐI KỲ (FINAL EXAM — 75 PHÚT, NGÀY 12/11/2026):**
> - **Phần 1 — 10 Câu Trắc nghiệm (MCQs):** Trải rộng toàn bộ các khái niệm, mệnh đề đúng/sai và bài toán 1 bước từ L01 đến L11, Extra Session và 2 bộ Practice. Khoảng **6–7/10 câu MCQ** nằm trực tiếp trong phạm vi L01–L08.
> - **Phần 2 — 5 Bài Tập Tự Luận Tính Toán (Mỗi bài gồm 3 ý nhỏ a, b, c):** Chiếm tỷ trọng điểm lớn nhất. Khoảng **60% khối lượng tự luận (3/5 bài toán lớn = 9 ý nhỏ)** rơi vào khối kiến thức L01–L08 theo 3 trụ cột kinh điển:
>   1. **Trụ cột Fixed Income (L02–L03):** Định giá trái phiếu / Spot-Forward Bootstrapping / Duration – Convexity xấp xỉ bậc 2 / Redington Immunization & Rebalancing.
>   2. **Trụ cột Portfolio Theory (L04–L05):** Phân phối kịch bản / GMVP / Tangency Portfolio $P^*$ (kèm kiểm tra biên cấm bán khống hoặc trần tỷ trọng) / CAL, Kinked CAL & Phân bổ vốn tối ưu $y^*$ theo hàm hữu dụng $U = E(r) - \frac{1}{2}A\sigma^2$ / Ngưỡng đa dạng hóa $S_Y > \rho_{XY}S_X$.
>   3. **Trụ cột Asset Pricing & Market Efficiency (L06–L08):** Single-Index Model ($R^2$, phân rã phương sai, kết hợp cổ phiếu $\alpha \ne 0$ với Market) / CAPM (CML vs. SML, định giá cổ phiếu) / APT Pure Arbitrage 3 bước, Factor-Mimicking & Debt-Financed Hedging / Đánh giá quỹ Fama-French (Gross vs. Net Alpha, phí hòa vốn) / Limits to Arbitrage (No-Arbitrage Band có phí mượn cổ phiếu).
> - **Quy tắc làm tròn chuẩn của đề thi:** Giữ nguyên giá trị chưa làm tròn (*unrounded intermediate values*) trong toàn bộ các bước tính trung gian; chỉ làm tròn kết quả cuối cùng về **2 chữ số thập phân** đối với số tiền (USD/EUR) và tỷ lệ phần trăm (`%`), **4 chữ số thập phân** đối với Duration/Convexity/Sharpe Ratio/Beta, và **ít nhất 6 chữ số thập phân** đối với Variance/Covariance dạng số thập phân.

---

## MỤC LỤC ĐỊNH HƯỚNG NHANH

1. [LECTURE 01: Môi Trường Đầu Tư & Các Công Cụ Tài Chính (The Investment Environment & Financial Instruments)](#lecture-01)
2. [LECTURE 02: Định Giá Trái Phiếu, Lợi Suất & Cấu Trúc Kỳ Hạn Lãi Suất (Bond Prices, Yields, and Term Structure)](#lecture-02)
3. [LECTURE 03: Duration, Convexity & Quản Trị Danh Mục Trái Phiếu (Duration, Convexity, and Immunization)](#lecture-03)
4. [LECTURE 04: Tỷ Suất Sinh Lời, Rủi Ro & Phân Bổ Vốn (Returns, Risk, and Capital Allocation)](#lecture-04)
5. [LECTURE 05: Đa Dạng Hóa Hiệu Quả Markowitz & Tối Ưu Hóa Danh Mục (Markowitz Portfolio Selection & Diversification)](#lecture-05)
6. [LECTURE 06: Mô Hình Đơn Chỉ Số & Mô Hình Định Giá Tài Sản Vốn (Single-Index Model & CAPM)](#lecture-06)
7. [LECTURE 07: Mô Hình Đa Nhân Tố, APT, Fama-French & Định Giá ESG (Multifactor Models, APT, Fama-French & ESG)](#lecture-07)
8. [LECTURE 08: Giả Thuyết Thị Trường Hiệu Quả & Tài Chính Hành Vi (Market Efficiency & Behavioral Finance)](#lecture-08)
9. [PHỤ LỤC TỔNG HỢP: Ma Trận Đối Chiếu Nhanh Xuyên Chương & Checklist Chống Sai Sót Phòng Thi](#phu-luc-tong-hop)

---

<a id="lecture-01"></a>
# LECTURE 01: MÔI TRƯỜNG ĐẦU TƯ & CÁC CÔNG CỤ TÀI CHÍNH
*(THE INVESTMENT ENVIRONMENT & FINANCIAL INSTRUMENTS)*

---

## 1.1. Trực giác Kinh tế Cốt lõi & Tổng hợp Lý thuyết Toàn diện

### A. Tài sản Thực (Real Assets) vs. Tài sản Tài chính (Financial Assets)
- **Tài sản thực (Real Assets):** Bao gồm đất đai, nhà xưởng, dây chuyền máy móc, thiết bị phòng thí nghiệm, hàng tồn kho, cũng như tài sản vô hình như bằng sáng chế (*patents*), phần mềm, thương hiệu và kiến thức nhân lực (*human knowledge*).
  - *Bản chất kinh tế:* Trực tiếp quyết định **năng lực sản xuất thực (productive capacity)** và tạo ra thu nhập ròng (GDP) cho nền kinh tế.
- **Tài sản tài chính (Financial Assets):** Bao gồm tiền mặt, tiền gửi ngân hàng, trái phiếu, cổ phiếu phổ thông, cổ phiếu ưu đãi, chứng khoán phái sinh.
  - *Bản chất kinh tế:* Không trực tiếp tạo ra hàng hóa/dịch vụ mà là **quyền đòi hỏi pháp lý (claims)** đối với thu nhập hoặc tài sản được tạo ra bởi các tài sản thực. Chúng định nghĩa cách phân chia thu nhập giữa các nhà đầu tư.
- **Đồng nhất thức Của cải Quốc gia (Aggregate Balance Sheet Identity):**
  - Mọi tài sản tài chính của chủ thể này luôn đồng thời là một **nghĩa vụ nợ tài chính (financial liability / obligation)** đối ứng trên bảng cân đối kế toán của chủ thể phát hành.
  - Khi cộng gộp toàn bộ các cá nhân, doanh nghiệp và chính phủ trong nền kinh tế đóng, tất cả các quyền đòi hỏi và nghĩa vụ tài chính tự triệt tiêu hoàn toàn:
    $$\text{Net Financial Wealth} = \sum \text{Financial Assets} - \sum \text{Financial Liabilities} = 0$$
  - Do đó, **tổng của cải ròng của nền kinh tế chỉ bằng tổng giá trị của các Tài sản Thực (Real Assets)**.

#### Vòng đời của Quyền đòi hỏi Tài chính: Tạo lập – Chuyển nhượng – Triệt tiêu (Creation, Transfer, Extinction)
Đây là dạng câu hỏi phân tích giao dịch kinh điển trong cả slide bài giảng (L01 Cell 33) và bộ đề luyện tập (Practice Q1):

| Cơ chế | Định nghĩa & Dấu hiệu nhận biết | Ví dụ chuẩn từ Đề luyện tập (Zeta / Alpha–Beta–Gamma) |
|---|---|---|
| **1. Tạo lập (Creation)** | Một chủ thể phát hành chứng khoán **mới** (trái phiếu mới, cổ phiếu mới) trực tiếp cho nhà đầu tư hoặc đối tác để đổi lấy tiền mặt hoặc tài sản thực. Tổng quy mô quyền đòi hỏi tài chính đang lưu hành tăng lên. | - Zeta phát hành trái phiếu doanh nghiệp 5 năm mệnh giá USD 250,000 thu về USD 250,000 tiền mặt.<br>- Alpha mua dây chuyền sản xuất (real asset) từ Beta và phát hành trái phiếu mới trực tiếp cho Beta để thanh toán.<br>- Eta phát hành 6,000 cổ phiếu phổ thông mới cho Zeta để đổi lấy bằng sáng chế thuốc (*patent* — real asset). |
| **2. Chuyển nhượng (Transfer)** | Quyền sở hữu một tài sản tài chính **đã tồn tại** (bao gồm cả tiền mặt hoặc cổ phiếu/trái phiếu cũ) được chuyển từ người nắm giữ này sang người khác. Tổ chức phát hành gốc **không nhận thêm vốn mới** và nghĩa vụ trả nợ gốc của họ không thay đổi (chỉ đổi chủ nợ/cổ đông). | - Beta bán lại lô trái phiếu Alpha đang nắm giữ cho Gamma lấy tiền mặt trên thị trường thứ cấp (Alpha vẫn nợ gốc + lãi như cũ, chủ nợ đổi từ Beta sang Gamma).<br>- Zeta bán 6,000 cổ phiếu Eta đang nắm giữ cho các nhà đầu tư khác lấy USD 300,000 tiền mặt.<br>- Zeta chi tiền mặt (financial asset được chuyển giao cho nhân viên/nhà cung cấp) để nghiên cứu tạo ra bằng sáng chế mới (real asset được tạo lập). |
| **3. Triệt tiêu / Chấm dứt (Extinction)** | Tổ chức phát hành mua lại, tất toán hoặc hoàn trả mệnh giá chứng khoán nợ/vốn khi đáo hạn hoặc thu hồi trước hạn. Quyền đòi hỏi pháp lý biến mất khỏi hệ thống. | - Zeta dùng USD 250,000 tiền mặt để mua lại/tất toán toàn bộ lô trái phiếu đang lưu hành theo mệnh giá (*redeem all outstanding bonds at face value*). |

---

### B. Bốn Vai trò Kinh tế của Thị trường Tài chính & Vấn đề Đại diện (Agency Problems)
1. **Vai trò Thông tin (The Informational Role of Markets):** Giá cổ phiếu và lợi suất trái phiếu phản ánh "đánh giá tập thể" (*collective assessment*) của hàng triệu nhà đầu tư về hiệu quả hiện tại và triển vọng tương lai của doanh nghiệp. Doanh nghiệp có ý tưởng/triển vọng xuất sắc sẽ có định giá cao, chi phí huy động vốn rẻ hơn $\implies$ thị trường vốn dẫn dòng vốn khan hiếm về nơi sử dụng hiệu quả nhất.
2. **Điều phối Thời điểm Tiêu dùng (Consumption Timing):** Thu nhập lao động thường cao khi còn trẻ và giảm lúc nghỉ hưu. Cá nhân dùng chứng khoán tài chính như kho lưu trữ sức mua (*store of wealth*) để chuyển tiêu dùng từ giai đoạn thặng dư thu nhập sang tương lai (mua chứng khoán khi đi làm, bán dần khi nghỉ hưu).
3. **Phân bổ Rủi ro (Allocation of Risk):** Cùng một dòng tiền rủi ro từ nhà máy thực có thể được tách thành nhiều lớp chứng khoán khác nhau: người ưa mạo hiểm mua cổ phiếu phổ thông (*common stock*), người thận trọng mua trái phiếu ưu tiên có tài sản đảm bảo (*senior secured bonds*). Rủi ro thực của nền kinh tế không tự biến mất, nhưng được phân bổ tới đúng những chủ thể có khả năng và sự sẵn lòng chịu đựng rủi ro đó tốt nhất.
4. **Tách biệt Sở hữu – Điều hành & Quản trị Công ty (Separation of Ownership and Management & Corporate Governance):**
   - Trong tập đoàn hiện đại, cổ đông (*principals / owners*) phân tán nên thuê ban giám đốc chuyên nghiệp (*agents / managers*) điều hành.
   - **Vấn đề đại diện (Agency Problem):** Ban giám đốc có thể theo đuổi lợi ích riêng thay vì tối đa hóa giá trị cổ đông (ví dụ: mở rộng quy mô đế chế vô bổ *empire building*, hưởng thụ đặc quyền xa xỉ, hoặc né tránh các dự án NPV dương có rủi ro cao vì sợ mất ghế).
   - **Các cơ chế giải quyết xung đột đại diện:**
     - Thiết kế gói thù lao gắn chặt với giá cổ phiếu/hiệu quả dài hạn (thưởng cổ phiếu hạn chế, quyền chọn cổ phiếu — dù cần cẩn trọng tránh khuyến khích chấp nhận rủi ro thái quá).
     - Giám sát trực tiếp bởi Hội đồng quản trị (*Board of Directors*), các nhà đầu tư định chế lớn (*large institutional investors*) và giới phân tích chứng khoán (*security analysts*).
     - **Mối đe dọa thâu tóm (Takeover Threat):** Nếu ban giám đốc điều hành yếu kém làm cổ phiếu bị định giá thấp so với tiềm năng thực, các tập đoàn bên ngoài hoặc quỹ *private equity* sẽ thu gom cổ phần để thâu tóm và sa thải ban giám đốc cũ.

---

### C. Quy trình Đầu tư (Investment Process), Chiến lược Quản lý & Cấu trúc Thị trường
1. **Hai quyết định trọng tâm của xây dựng danh mục:**
   - **Phân bổ Tài sản (Asset Allocation):** Quyết định phân chia tổng vốn đầu tư vào các **nhóm tài sản lớn (broad asset classes)** như cổ phiếu, trái phiếu dài hạn, công cụ thị trường tiền tệ, bất động sản, hàng hóa, tài sản quốc tế.
   - **Lựa chọn Chứng khoán (Security Selection):** Quyết định chọn mua các **mã chứng khoán cụ thể** bên trong từng nhóm tài sản dựa trên phân tích chứng khoán (*security analysis* & định giá).
2. **Ba phương pháp tiếp cận xây dựng danh mục:**
   - **Top-Down Approach (Từ trên xuống):** Bắt đầu bằng phân tích kinh tế vĩ mô (tăng trưởng GDP, lạm phát, lãi suất) để quyết định *Asset Allocation* và chọn ngành hấp dẫn trước, sau đó mới đi xuống chọn từng cổ phiếu/trái phiếu cụ thể bên trong nhóm đó.
   - **Bottom-Up Approach (Từ dưới lên):** Bắt đầu trực tiếp từ việc sàng lọc và định giá cơ bản từng doanh nghiệp riêng lẻ (dòng tiền, lợi thế cạnh tranh, giá trị nội tại) để mua các mã đang bị định giá thấp (*undervalued*), **bất chấp triển vọng chung của ngành hay vĩ mô đang ảm đạm** (L01 Cell 27 & Practice Q3). Nhược điểm là danh mục dễ bị tập trung ngoài ý muốn vào một số ngành hoặc khu vực nhất định.
   - **Passive vs. Active Management (Quản lý Thụ động vs. Chủ động):**
     - *Passive Management:* Nắm giữ danh mục đa dạng hóa cao (thường mô phỏng chỉ số thị trường *index replication*), **không cố gắng tìm kiếm chứng khoán định giá sai** và **không cố gắng căn thời điểm thị trường (*no market timing*)**. Dựa trên niềm tin thị trường hiệu quả và tối thiểu hóa chi phí.
     - *Active Management:* Nỗ lực tạo lợi nhuận vượt trội thông qua *Security Selection* (săn tìm $\alpha > 0$) và/hoặc *Market Timing* (tăng/giảm tỷ trọng cổ phiếu trước các đợt sóng vĩ mô).
3. **Thị trường Cạnh tranh & Đánh đổi Rủi ro – Lợi nhuận (Competitive Markets):**
   - Lợi nhuận **kỳ vọng** (*expected return*) cao hơn là phần đền bù cho những rủi ro hệ thống không thể triệt tiêu bằng đa dạng hóa. Rủi ro cao hơn **không bao giờ đảm bảo** lợi nhuận thực hiện (*realized return*) sẽ cao hơn (vì nếu đảm bảo chắc chắn thì nó không còn là rủi ro nữa!).
4. **Thị trường Sơ cấp vs. Thị trường Thứ cấp (Primary vs. Secondary Markets):**
   - **Primary Market:** Nơi chứng khoán mới được phát hành lần đầu (IPO — *Initial Public Offering*, SEO / *Follow-on offerings*, phát hành riêng lẻ *private placements*) có sự hỗ trợ bảo lãnh phát hành của các ngân hàng đầu tư (*underwriters*). Dòng tiền chảy trực tiếp từ nhà đầu tư vào két sắt của tổ chức phát hành.
   - **Secondary Market:** Nơi các nhà đầu tư giao dịch mua bán lại các chứng khoán đã phát hành trước đó (sàn tập trung khớp lệnh *order-driven* như NYSE, hoặc thị trường phi tập trung qua các nhà tạo lập thị trường báo giá *quote-driven OTC dealer markets*). Vai trò sống còn: cung cấp thanh khoản (*liquidity*) và tín hiệu giá thị trường (*price discovery*), từ đó gián tiếp giúp tổ chức phát hành huy động vốn dễ hơn ở các đợt phát hành sơ cấp sau.

---

### D. Hệ thống Phân loại Toàn diện Các Công cụ Tài chính

#### 1. Công cụ Thị trường Tiền tệ (Money Market Instruments)
Đặc trưng chung: Công cụ nợ **ngắn hạn** (kỳ hạn gốc thường $\le 1$ năm), **thanh khoản rất cao**, **rủi ro vỡ nợ và rủi ro biến động giá rất thấp**, thường giao dịch sỉ với mệnh giá lớn.

| Công cụ | Đặc điểm cốt lõi, Tổ chức phát hành & Cơ chế vận hành |
|---|---|
| **Treasury Bills (T-Bills)** | Trái phiếu Kho bạc Mỹ ngắn hạn (kỳ hạn 4, 8, 13, 17, 26, 52 tuần). Là chứng khoán chiết khấu thuần túy (**zero-coupon discount securities**): bán với giá thấp hơn mệnh giá và trả đúng mệnh giá khi đáo hạn. Thanh khoản cao nhất, không có rủi ro vỡ nợ (*default-free*), tiền lãi được miễn thuế tiểu bang và địa phương tại Mỹ. |
| **Certificates of Deposit (CDs)** | Chứng chỉ tiền gửi có kỳ hạn do ngân hàng phát hành (không được rút theo yêu cầu trước hạn mà không chịu phạt). Các **Negotiable CDs** (mệnh giá lớn, thường từ USD 100,000 trở lên) có thể bán chuyển nhượng tự do trên thị trường thứ cấp ngắn hạn; được bảo hiểm FDIC tới ngưỡng quy định. |
| **Commercial Paper (CP)** | Kỳ phiếu thương mại ngắn hạn **không có tài sản đảm bảo (*unsecured promissory notes*)** do các tập đoàn lớn phi tài chính hoặc tài chính có uy tín tín dụng cao trực tiếp phát hành (thay vì vay ngân hàng). Kỳ hạn thường dưới 270 ngày (nhằm được miễn thủ tục đăng ký phát hành công khai với SEC), phổ biến nhất dưới 1–2 tháng. Thường được bảo chứng bởi hạn mức tín dụng dự phòng ngân hàng (*backup line of credit*). |
| **Bankers' Acceptances (BAs)** | Lệnh yêu cầu ngân hàng thanh toán một khoản tiền vào ngày xác định trong tương lai (thường 1–6 tháng); khi ngân hàng đóng dấu **"Accepted"**, ngân hàng chịu trách nhiệm thanh toán cuối cùng cho người cầm giữ. Rất phổ biến trong tài trợ thương mại quốc tế (xuất nhập khẩu) khi độ tín nhiệm của đối tác mua hàng chưa được biết rõ; giao dịch chiết khấu trên thị trường thứ cấp tương tự T-Bills. |
| **Eurodollars** | Các khoản tiền gửi có kỳ hạn định danh bằng **đồng Đô-la Mỹ (USD)** đặt tại các ngân hàng nước ngoài hoặc tại chi nhánh nước ngoài của các ngân hàng Mỹ (nằm ngoài phạm vi quản lý dự trữ bắt buộc và phí bảo hiểm của Fed tại Mỹ). *Lưu ý:* Không nhất thiết phải nằm ở châu Âu! |
| **Repos & Reverse Repos** | Hợp đồng vay ngắn hạn có tài sản thế chấp bằng chứng khoán Chính phủ (thường qua đêm *overnight*; nếu dài hơn từ vài ngày đến trên 30 ngày gọi là *Term Repo*):<br>- **Repo (Repurchase Agreement — Góc nhìn người ĐI VAY TIỀN / Cash Borrower):** Bán chứng khoán Chính phủ cho đối tác hôm nay lấy tiền mặt $P_0$, đồng thời cam kết **mua lại** chính chứng khoán đó vào ngày tương lai với giá thỏa thuận cao hơn $P_T > P_0$. Chênh lệch $P_T - P_0$ chính là tiền lãi vay.<br>- **Reverse Repo (Góc nhìn người CHO VAY TIỀN / Cash Lender):** Có tiền mặt nhàn rỗi, **mua** chứng khoán từ bên đi vay hôm nay tại giá $P_0$ và cam kết **bán lại** cho họ vào ngày hẹn trước tại giá $P_T$. (Cùng một giao dịch: bên thiếu tiền gọi là Repo, bên thừa tiền gọi là Reverse Repo!). |
| **Federal Funds (Fed Funds)** | Các ngân hàng thương mại phải duy trì tiền dự trữ trong tài khoản tại Ngân hàng Dự trữ Liên bang (Fed). Trên thị trường *Fed Funds*, các ngân hàng thừa dự trữ cho các ngân hàng thiếu dự trữ vay **qua đêm không tài sản đảm bảo (*unsecured overnight interbank loans*)** tại mức lãi suất **Federal Funds Rate** (mục tiêu điều hành chính sách tiền tệ trọng tâm của Fed). |
| **LIBOR vs. SOFR** | - **LIBOR (London Interbank Offered Rate):** Lãi suất tham chiếu vay tín chấp liên ngân hàng tại London dựa trên báo giá khảo sát ước tính của các ngân hàng lớn — đã bị khai tử do thanh khoản giao dịch thực mỏng và bê bối thao túng báo giá.<br>- **SOFR (Secured Overnight Financing Rate):** Chuẩn lãi suất tham chiếu mới thay thế USD LIBOR, đo lường chi phí vay tiền mặt **qua đêm CÓ TÀI SẢN ĐẢM BẢO bằng chứng khoán Kho bạc Mỹ** dựa trên dữ liệu giao dịch Repo thực tế khổng lồ hàng ngày (gần như phi rủi ro tín dụng). |

> [!TIP]
> **Diễn biến Chênh lệch Lợi suất Tín dụng (Credit Spread = $y_{\text{CP}} - y_{\text{T-Bill}}$) trong Suy thoái Kinh tế (L01 Cell 30):**  
> Khi nền kinh tế rơi vào suy thoái nghiêm trọng (*severe recession*), khoảng chênh lệch lợi suất giữa Commercial Paper của doanh nghiệp và T-Bills cùng kỳ hạn sẽ **GIÃN RỘNG MẠNH (widens sharply)** bởi tác động kép từ hai phía:
> 1. **Rủi ro vỡ nợ tăng cao (Higher Default Risk):** Dòng tiền và lợi nhuận doanh nghiệp suy giảm làm xác suất mất khả năng thanh toán CP tăng lên $\implies$ nhà đầu tư đòi hỏi phần bù vỡ nợ cao hơn, đẩy lợi suất $y_{\text{CP}}$ tăng lên.
> 2. **Hiện tượng tháo chạy tìm nơi trú ẩn an toàn (Flight to Safety & Liquidity):** Trong khủng hoảng, mức ngại rủi ro tăng vọt khiến dòng vốn ồ ạt rút khỏi tài sản rủi ro tư nhân để đổ dồn vào T-Bills (an toàn tuyệt đối và thanh khoản cao nhất), đẩy giá T-Bills tăng và ép lợi suất $y_{\text{T-Bill}}$ giảm xuống.

---

#### 2. Công cụ Thị trường Vốn (Capital Market Instruments)
1. **Chứng khoán Nợ Dài hạn (Fixed-Income Capital Market):**
   - **Treasury Notes & Treasury Bonds:** Chính phủ Mỹ phát hành, trả lãi coupon cố định mỗi 6 tháng (*semiannual*). **T-Notes** có kỳ hạn từ trên 1 năm đến **10 năm**; **T-Bonds** có kỳ hạn dài từ **10 đến 30 năm**.
   - **TIPS (Treasury Inflation-Protected Securities):** Trái phiếu Kho bạc bảo vệ chống lạm phát (mệnh giá gốc được điều chỉnh theo chỉ số giá tiêu dùng CPI — phân tích chi tiết tại Lecture 02).
   - **Federal Agency Debt:** Phát hành bởi các tổ chức tài trợ thế chấp do Chính phủ bảo trợ (GSEs như Fannie Mae, Freddie Mac) hoặc cơ quan chính phủ (Ginnie Mae) để bơm thanh khoản cho thị trường vay mua nhà; lợi suất chỉ nhỉnh hơn Kho bạc một chút.
   - **International Bonds (Trái phiếu Quốc tế):**
     - **Foreign Bonds:** Phát hành bởi tổ chức vay vốn nước ngoài nhưng chào bán ngay tại một quốc gia khác và **định danh bằng đồng nội tệ của quốc gia nơi chào bán** (Ví dụ: **Yankee bonds** bán tại Mỹ bằng USD bởi tổ chức ngoài Mỹ; **Samurai bonds** bán tại Nhật bằng JPY; **Bulldog bonds** bán tại Anh bằng GBP).
     - **Eurobonds:** Trái phiếu định danh bằng một đồng tiền (thường là đồng tiền của tổ chức phát hành) nhưng được phát hành và chào bán tại các thị trường quốc gia **không sử dụng đồng tiền đó làm nội tệ** (Ví dụ: *Eurodollar bond* định danh bằng USD nhưng phát hành tại London/châu Âu; *Euroyen*, *Eurosterling*).
   - **Municipal Bonds (Munis):** Do chính quyền tiểu bang và địa phương phát hành (*General Obligation bonds* bảo đảm bằng quyền thu thuế vs. *Revenue bonds* bảo đảm bằng doanh thu dự án cụ thể như cầu đường, sân bay, bệnh viện). **Đặc quyền thuế:** Tiền lãi coupon của Munis được **miễn thuế thu nhập liên bang** (và thường miễn cả thuế tiểu bang nếu cư trú tại bang phát hành), nên Munis có lợi suất danh nghĩa thấp hơn trái phiếu doanh nghiệp chịu thuế có cùng rủi ro.
   - **Corporate Bonds:** Do doanh nghiệp tư nhân phát hành: *Secured bonds* (có tài sản thế chấp), *Debentures* (không có tài sản thế chấp), *Subordinated debentures* (thứ cấp — xếp sau các chủ nợ thông thường khác), kèm theo các điều khoản quyền chọn như *Callable*, *Puttable*, *Convertible*.
   - **MBS & ABS (Mortgage-Backed & Asset-Backed Securities):** Chứng khoán hóa (*securitization*) tập hợp các khoản vay thế chấp mua nhà hoặc vay mua ô tô, thẻ tín dụng để chuyển dòng tiền trả góp sang nhà đầu tư trên thị trường vốn.

2. **Chứng khoán Vốn Cổ phần (Equity) & Thứ tự Ưu tiên Thanh toán (Seniority):**
   - **Thứ tự ưu tiên nhận tài sản khi thanh lý/phá sản (Absolute Priority / Seniority Rule):**
     $$\text{Secured Debt} \succ \text{Senior Unsecured Debt / Bondholders} \succ \text{Subordinated Debt} \succ \text{Preferred Stock} \succ \text{Common Stock}$$
   - **Common Stock (Cổ phiếu Phổ thông):**
     - Đại diện quyền sở hữu doanh nghiệp (*ownership*), có **quyền biểu quyết (*voting rights*)** bầu HĐQT và quyết sách lớn.
     - **Residual Claim (Quyền đòi hỏi phần còn lại cuối cùng):** Đứng cuối hàng khi chia lợi nhuận hay thanh lý tài sản (chỉ được nhận phần dôi ra sau khi chủ nợ, thuế, lương và cổ đông ưu đãi đã được thanh toán đủ), nhưng hưởng toàn bộ tiềm năng tăng trưởng không giới hạn (*unlimited upside*) khi công ty thịnh vượng.
     - **Limited Liability (Trách nhiệm hữu hạn):** Nếu công ty phá sản và tài sản không đủ trả nợ, chủ nợ **không được phép truy đòi tài sản cá nhân** của cổ đông. Khoản lỗ tối đa của cổ đông phổ thông khi mua đứt bằng tiền thật là **100% số vốn đầu tư ban đầu** (cổ phiếu về giá 0).
   - **Preferred Stock (Cổ phiếu Ưu đãi — Chứng khoán Lai ghép / Hybrid Security):**
     - *Giống Fixed Income:* Hứa hẹn mức cổ tức cố định (hoặc thả nổi theo tham chiếu), thường không có quyền biểu quyết, được ưu tiên nhận cổ tức và giá trị thanh lý **trước cổ đông phổ thông** (nhưng luôn xếp **sau mọi trái chủ/chủ nợ!**). Đa số có điều khoản tích lũy (*cumulative*): mọi cổ tức ưu đãi bị khất lại các năm trước phải được trả bù đủ trước khi được phép chia 1 đồng cổ tức nào cho cổ phiếu phổ thông.
     - *Giống Equity:* Thường không có ngày đáo hạn cố định (vĩnh cửu, dù hay kèm quyền mua lại *callable*); việc công ty bỏ lỡ/tạm ngừng trả cổ tức ưu đãi **KHÔNG cấu thành sự kiện vỡ nợ (*does NOT trigger bankruptcy*)** như bỏ trả coupon trái phiếu; cổ tức ưu đãi trả ra **không được khấu trừ thuế thu nhập doanh nghiệp** đối với tổ chức phát hành (ngược lại, lãi vay trái phiếu được khấu trừ thuế).
   - **ADRs (American Depository Receipts):** Chứng chỉ do ngân hàng Mỹ phát hành và giao dịch trực tiếp trên sàn Mỹ (bằng USD), đại diện cho quyền sở hữu một số lượng cổ phần nhất định của công ty nước ngoài đang lưu ký tại ngân hàng, giúp công ty ngoại tiếp cận nhà đầu tư Mỹ và đáp ứng quy định đăng ký thuận tiện hơn.

3. **Công cụ Phái sinh Sơ lược (Derivatives — Contingent Claims):**
   - Giá trị bắt nguồn (*derived*) phụ thuộc vào giá của tài sản cơ sở (*underlying asset*: cổ phiếu, trái phiếu, hàng hóa, tỷ giá, lãi suất, chỉ số).
   - **Quyền chọn (Options):** Người mua (*Buyer / Holder / Long*) trả khoản phí **Premium** ngay thời điểm mở vị thế để nhận **QUYỀN, nhưng KHÔNG có nghĩa vụ** (*right, but no obligation*):
     - *Call Option:* Quyền **mua** tài sản cơ sở tại giá thực hiện (*strike/exercise price*) $K$. Chỉ thực hiện tại đáo hạn khi $S_T > K$. Với hai quyền chọn mua cùng kỳ hạn trên cùng cổ phiếu, quyền chọn có **$K$ thấp hơn luôn có giá cao hơn** ($C(K_1) \ge C(K_2)$ khi $K_1 < K_2$) vì cho phép mua cùng tài sản với giá rẻ hơn!
     - *Put Option:* Quyền **bán** tài sản cơ sở tại giá thực hiện $K$. Chỉ thực hiện tại đáo hạn khi $S_T < K$. Quyền chọn bán có **$K$ cao hơn luôn có giá cao hơn** ($P(K_2) \ge P(K_1)$ khi $K_2 > K_1$) vì cho phép bán tài sản với giá cao hơn!
   - **Hợp đồng Kỳ hạn / Tương lai (Forwards / Futures):** Là **NGHĨA VỤ HỢP ĐỒNG BẮT BUỘC (*contractual obligation*)** từ cả hai phía vào ngày đáo hạn tại mức giá kỳ hạn đã chốt $F_0$ (không thu phí quyền chọn trả trước): bên **Long** bắt buộc phải mua và trả $F_0$ ngay cả khi $S_T < F_0$ (chịu lỗ $S_T - F_0 < 0$); bên **Short** bắt buộc phải bán/giao hàng nhận $F_0$ ngay cả khi $S_T > F_0$ (chịu lỗ $F_0 - S_T < 0$).

---

### E. Chỉ số Thị trường Chứng khoán (Stock & Bond Market Indexes)

| Phương pháp Xây dựng Chỉ số | Cơ chế Tính toán & Trọng số | Đặc tính Danh mục Tương ứng & Xử lý Chia tách Cổ phiếu (Stock Splits) |
|---|---|---|
| **1. Gia quyền theo Giá (Price-Weighted Index)**<br>*(VD: Dow Jones Industrial Average — DJIA 30 mã, Nikkei 225)* | $\text{Index}_t = \frac{\sum_{i=1}^n P_{i,t}}{\text{Divisor}}$<br>Mức thay đổi phần trăm chỉ số phụ thuộc vào biến động đô-la của thị giá từng cổ phiếu. | - Tương ứng với chiến lược mua **cùng một số lượng cổ phiếu bằng nhau** (ví dụ 1 cổ phiếu mỗi công ty).<br>- *Thiên lệch:* Công ty có thị giá 1 cổ phiếu cao ($P_i$ lớn) chi phối mạnh chỉ số dù tổng vốn hóa có thể nhỏ hơn công ty khác.<br>- *Khi có Stock Split (chia tách cổ phiếu) hoặc đổi mã thành phần:* Thị giá cổ phiếu bị chia nhỏ làm tử số giảm đột ngột $\implies$ Phải **điều chỉnh giảm ước số `Divisor`** sao cho điểm số Index ngay trước và ngay sau chia tách giữ nguyên không đổi! |
| **2. Gia quyền theo Vốn hóa Thị trường (Market-Value-Weighted Index)**<br>*(VD: S&P 500, Nasdaq Composite, Wilshire 5000; thực tế dùng Free-Float)* | $\text{Index}_t = \text{Index}_0 \times \frac{\sum_{i=1}^n P_{i,t} Q_{i,t}}{\sum_{i=1}^n P_{i,0} Q_{i,0}}$<br>Tỷ suất sinh lời chỉ số là trung bình có trọng số theo vốn hóa đầu kỳ $w_i = \frac{MktCap_i}{\sum MktCap_j}$. | - Phản ánh chính xác chiến lược **Buy-and-Hold** thụ động vĩ mô (tự động điều chỉnh tỷ trọng khi giá cổ phiếu tăng/giảm, không tốn chi phí giao dịch tái cân bằng).<br>- *Stock Splits:* **Tự động miễn nhiễm** (giá giảm một nửa nhưng số cổ phiếu tăng gấp đôi nên $P_i Q_i$ giữ nguyên, không cần chỉnh Divisor vì lý do split!).<br>- *Nhược điểm:* Các siêu tập đoàn vốn hóa khổng lồ chi phối biến động toàn chỉ số. |
| **3. Gia quyền Tỷ trọng Bằng nhau (Equally-Weighted Index)** | Đặt tỷ trọng tiền đầu tư bằng nhau $w_i = \frac{1}{n}$ vào mỗi mã:<br>$r_{\text{EW}} = \frac{1}{n}\sum_{i=1}^n r_i$ | - Đặt trọng số cao hơn nhiều cho các cổ phiếu vốn hóa nhỏ (*small-cap tilt*) so với chỉ số vốn hóa.<br>- **Bắt buộc phải tái cân bằng định kỳ (periodic rebalancing):** Khi một cổ phiếu tăng giá mạnh hơn các mã khác, tỷ trọng của nó vượt quá $1/n$ nên phải bán bớt mã thắng và mua thêm mã thua để khôi phục tỷ trọng $1/n$ (phát sinh chi phí giao dịch và thuế). |

---

### F. Mua Ký quỹ (Buying on Margin) & Bán Khống (Short Selling)
1. **Mua Ký quỹ (Buying on Margin — Đòn bẩy vị thế Mua):**
   - Nhà đầu tư bỏ một phần vốn tự có (**Equity**) và vay phần tiền còn lại (**Margin Loan / Debit Balance**) từ công ty chứng khoán (*broker*) theo lãi suất vay ký quỹ (*call money rate*) để mua cổ phiếu.
   - **Initial Margin ($IM$):** Tỷ lệ vốn tự có tối thiểu bắt buộc lúc mở vị thế (theo Regulation T của Fed tại Mỹ thường là $IM = 50\%$).
   - **Maintenance Margin ($MM$):** Ngưỡng tỷ lệ vốn chủ tối thiểu phải duy trì mọi lúc ($MM < IM$, ví dụ $25\%$ hoặc $30\%$). Nếu giá cổ phiếu sụt giảm làm tỷ lệ ký quỹ rơi xuống **thấp hơn $MM$**, nhà đầu tư bị **Margin Call**: buộc phải nộp thêm tiền mặt hoặc chứng khoán thế chấp (nếu không nộp, broker sẽ bán giải chấp cổ phiếu để thu hồi nợ vay).
2. **Bán Khống (Short Selling — Kiếm lời khi Giá Giảm):**
   - Quy trình: Mượn $N$ cổ phiếu từ broker (lấy từ tài khoản của khách hàng khác) $\to$ Bán ngay ra thị trường thu tiền mặt $N P_0$ (khoản tiền bán khống này bị giữ lại làm tài sản đảm bảo tại broker) $\to$ Đồng thời nhà đầu tư phải nộp thêm khoản ký quỹ ban đầu $N P_0 \cdot IM$ (tiền mặt hoặc T-Bills) $\to$ Đóng vị thế trong tương lai bằng cách mua lại $N$ cổ phiếu ngoài thị trường tại giá $P_1$ để trả cho người cho mượn (*covering the short position*).
   - **Quy tắc Cổ tức khi Bán khống:** Nếu công ty chia cổ tức tiền mặt $D$ mỗi cổ phiếu trong thời gian vị thế bán khống đang mở, người mua mới ngoài thị trường nhận cổ tức từ công ty, còn **người bán khống bắt buộc phải trích tiền túi đền bù đúng khoản cổ tức $N \cdot D$ cho người đã cho mượn cổ phiếu**!
   - **Rủi ro Bán khống:** Lợi nhuận tối đa bị chặn trên (khi $P_1 \to 0$), nhưng **khoản lỗ tiềm tàng là VÔ HẠN (unlimited potential loss)** vì giá cổ phiếu $P_1$ có thể tăng không giới hạn! Khi giá cổ phiếu **tăng** vượt ngưỡng kích hoạt $P^*$, tài khoản bị Margin Call.

---

## 1.2. Hệ thống Công thức Đầy đủ & Quy ước Đơn vị (Lecture 01)

### 1. Lợi suất Tương đương Thuế của Trái phiếu Đô thị (Municipal Bond Tax-Equivalent Yield)
Gọi $r_{\text{muni}}$ là lợi suất miễn thuế của trái phiếu đô thị, $r_{\text{taxable}}$ là lợi suất trước thuế của trái phiếu chịu thuế có cùng mức rủi ro, và $t$ là thuế suất biên (*marginal tax rate*) của nhà đầu tư:
$$\text{After-Tax Yield}_{\text{taxable}} = r_{\text{taxable}}(1 - t)$$
- **Lợi suất chịu thuế tương đương (Tax-Equivalent Yield):**
  $$r_{\text{TEY}} = \frac{r_{\text{muni}}}{1 - t}$$
  *(Chọn mua Muni nếu $r_{\text{muni}} > r_{\text{taxable}}(1 - t)$, hay tương đương $r_{\text{TEY}} > r_{\text{taxable}}$).*
- **Thuế suất Hòa vốn / Bàng quan (Indifference Marginal Tax Rate $t^*$):**
  $$1 - t^* = \frac{r_{\text{muni}}}{r_{\text{taxable}}} \implies t^* = 1 - \frac{r_{\text{muni}}}{r_{\text{taxable}}}$$
  *(Nhà đầu tư có thuế suất cá nhân $t > t^*$ sẽ ưu tiên nắm giữ Municipal Bond).*

### 2. Lãi suất Repo Ngắn hạn (Repo Rate — Quy ước Thị trường Tiền tệ 360 ngày)
Bán chứng khoán hôm nay giá $P_0$ và cam kết mua lại sau $d$ ngày với giá $P_T$:
$$\text{HPR}_{d\text{ days}} = \frac{P_T - P_0}{P_0}, \qquad r_{\text{repo, simple 360}} = \frac{P_T - P_0}{P_0} \times \frac{360}{d}$$

### 3. Công thức Mua Ký quỹ (Buying on Margin — $N$ cổ phiếu mua tại $P_0$)
- Tổng giá trị mua ban đầu: $V_0 = N P_0$. Vốn tự có ban đầu: $E_0 = V_0 \cdot IM$. Khoản nợ vay gốc: $\text{Loan} = V_0(1 - IM)$.
- Tại mức giá thị trường mới $P$ (nếu tính tức thời chưa cộng lãi vay; nếu sau 1 năm có lãi vay $r_L$ thì thay $\text{Loan}$ bằng $\text{Loan}(1+r_L)$):
  $$\text{Percentage Margin} = \frac{\text{Equity}}{\text{Market Value of Stock}} = \frac{N P - \text{Loan}}{N P}$$
- **Giá Kích hoạt Margin Call ($P^*$ khi $\text{Margin} = MM$):**
  $$\mathbf{P^* = \frac{\text{Loan} / N}{1 - MM} = P_0 \frac{1 - IM}{1 - MM}}$$
- **Tỷ suất Sinh lời trên Vốn Tự có sau 1 kỳ (có cổ tức $D_1$ và lãi vay $r_L$):**
  $$\text{HPR}_{\text{margin}} = \frac{N(P_1 - P_0 + D_1) - \text{Loan} \cdot r_L}{E_0}$$

### 4. Công thức Bán Khống (Short Selling — Bán khống $N$ cổ phiếu tại $P_0$)
- Tiền bán khống thu về: $N P_0$. Ký quỹ ban đầu nộp thêm: $N P_0 \cdot IM$.
- Tổng tài sản trên tài khoản ký quỹ: $\text{Total Assets} = N P_0 (1 + IM)$ (nếu trong kỳ phải trích tiền tài khoản đền cổ tức $N D$, tổng tài sản còn $\text{Total Assets} - N D$).
- Nghĩa vụ nợ cổ phiếu theo giá thị trường $P$: $\text{Liability} = N P$. Vốn chủ còn lại: $E = \text{Total Assets} - N P$.
  $$\text{Percentage Margin}_{\text{short}} = \frac{\text{Equity}}{\text{Value of Shares Owed}} = \frac{\text{Total Assets} - N P}{N P}$$
- **Giá Kích hoạt Margin Call khi Bán Khống ($P^*$ khi giá TĂNG chạm ngưỡng $MM$):**
  $$\mathbf{P^* = \frac{\text{Total Assets} / N}{1 + MM} = P_0 \frac{1 + IM}{1 + MM}}$$
- **Tỷ suất Sinh lời Bán khống (nếu không hưởng lãi trên tài khoản ký quỹ và phải đền cổ tức $D_1$):**
  $$\text{HPR}_{\text{short}} = \frac{N(P_0 - P_1 - D_1)}{N P_0 \cdot IM} = \frac{P_0 - P_1 - D_1}{P_0 \cdot IM}$$

### 5. Payoff & Lợi nhuận Ròng Quyền chọn tại Đáo hạn (Mỗi cổ phiếu)
- **Long Call** (mua quyền mua giá thực hiện $K$, phí $C_0$): $\text{Payoff} = \max(S_T - K, 0)$, $\text{Net Profit} = \max(S_T - K, 0) - C_0$, $\text{Breakeven } S_T^* = K + C_0$.
- **Long Put** (mua quyền bán giá thực hiện $K$, phí $P_0$): $\text{Payoff} = \max(K - S_T, 0)$, $\text{Net Profit} = \max(K - S_T, 0) - P_0$, $\text{Breakeven } S_T^* = K - P_0$.

---

## 1.3. Quy trình Giải nhanh Bài tập Tính toán Phòng thi (Lecture 01)

### Dạng 1.1: Giải Nhanh Margin Call & HPR cho Mua Ký Quỹ và Bán Khống
- **Mẹo nhớ không bao giờ nhầm dấu $(1 - MM)$ và $(1 + MM)$:**
  - **Mua ký quỹ (Long on Margin)** sợ giá **GIẢM** ($P^* < P_0$) $\implies$ Tử số là Nợ trên mỗi cổ phiếu $P_0(1-IM)$, mẫu số là $(1 - MM)$: $P^* = \frac{\text{Loan}/N}{1 - MM}$.
  - **Bán khống (Short Sale)** sợ giá **TĂNG** ($P^* > P_0$) $\implies$ Tử số là Tổng tài sản trên mỗi cổ phiếu $P_0(1+IM)$, mẫu số là $(1 + MM)$: $P^* = \frac{\text{Total Assets}/N}{1 + MM}$.
- **Ví dụ kiểm chứng nhanh:**
  - *Long Margin:* Mua 100 cổ phiếu tại `USD 100`, $IM = 50\%$, $MM = 30\%$. Ta có $\text{Loan}/N = 100(1 - 0.50) = 50$. Giá bị Margin Call ngay lập tức là $P^* = \frac{50}{1 - 0.30} = \text{USD } 71.43$.
  - *Short Sale:* Bán khống 100 cổ phiếu tại `USD 100`, $IM = 50\%$, $MM = 30\%$. Tổng tài sản mỗi cổ phiếu là $100(1 + 0.50) = 150$. Giá bị Margin Call là $P^* = \frac{150}{1 + 0.30} = \text{USD } 115.38$.

### Dạng 1.2: Khôi phục Giá Thực hiện $K$ và Phí Quyền chọn $C_0$ từ Bảng Lợi nhuận (Practice Q7)
- **Quy trình 2 giây:**
  1. Nhìn dòng giá cổ phiếu thấp nhất mà lợi nhuận ròng âm không đổi (hoặc thử xem quyền chọn OTM): khi $S_T \le K$, quyền chọn không thực hiện nên $\text{Net Profit} = -C_0 \implies$ suy ra ngay $C_0 = -\text{Profit}_{\text{OTM}}$.
  2. Nhìn dòng có lợi nhuận dương (chắc chắn ITM, $S_T > K$): từ $\text{Profit} = S_T - K - C_0 \implies K = S_T - C_0 - \text{Profit}$. Kiểm tra lại độ dốc 1-đối-1 giữa 2 dòng ITM ($\Delta \text{Profit} = \Delta S_T$)!
  - *Áp dụng Practice Q7:* Tại $S_T = 47$ lãi ròng $-4$; tại $S_T = 59$ lãi $+3$; tại $S_T = 68$ lãi $+12$. Thấy $68 - 59 = 9 = 12 - 3$ (cả 59 và 68 đều ITM!). Nếu $S_T = 47$ là OTM thì $C_0 = 4 \implies K = 59 - 4 - 3 = 52$. Kiểm tra $47 \le 52$ (đúng là OTM!). Vậy $C_0 = \text{USD } 4, K = \text{USD } 52$. Tại $S_T = 54 > 52$: vẫn **PHẢI THỰC HIỆN QUYỀN (Exercise)** vì $\text{Payoff} = 54 - 52 = +2 > 0$, giúp thu hẹp lỗ ròng xuống $2 - 4 = -\text{USD } 2$ (tốt hơn là bỏ quyền để chịu lỗ toàn bộ $-\text{USD } 4$!).

### Dạng 1.3: Điều chỉnh Ước số (Divisor) cho Chỉ số Gia quyền theo Giá khi Chia tách Cổ phiếu
- Giả sử chỉ số gồm 3 cổ phiếu giá `USD 30`, `USD 60`, `USD 90`, $\text{Divisor}_0 = 3 \implies \text{Index}_0 = \frac{30+60+90}{3} = 60$.
- Cổ phiếu giá `USD 90` thực hiện chia tách 3-for-1 (1 cổ phiếu cũ tách thành 3 cổ phiếu mới $\implies$ giá mới giảm còn $90 / 3 = \text{USD } 30$).
- Đặt tổng giá mới chia cho $\text{Divisor}_{\text{new}}$ bằng đúng điểm chỉ số ngay trước khi tách:
  $$\frac{30 + 60 + 30}{\text{Divisor}_{\text{new}}} = 60 \implies \text{Divisor}_{\text{new}} = \frac{120}{60} = 2.0$$

---

## 1.4. Các Bẫy Lý thuyết & Lỗi Sai Chết Người trong MCQ (Lecture 01)

> [!CAUTION]
> **7 BẪY MCQ KINH ĐIỂN CỦA LECTURE 01 PHẢI TRÁNH TUYỆT ĐỐI:**
> 1. **Bẫy "Thực hiện quyền chọn khi đang lỗ ròng" (Practice Q6c & Q7b):** Khi $K < S_T < K + C_0$ (cho Call) hoặc $K - P_0 < S_T < K$ (cho Put), tổng giao dịch tuy vẫn đang **lỗ ròng** ($\text{Net Profit} < 0$), nhưng người nắm giữ **VẪN BẮT BUỘC PHẢI THỰC HIỆN QUYỀN (*must exercise*)**! Vì phí quyền chọn đã trả là chi phí chìm (*sunk cost*); thực hiện quyền thu về $\text{Payoff} > 0$ giúp thu hồi một phần phí, còn bỏ quyền thì thu $0$ và mất trắng 100% phí!
> 2. **Bẫy "Quyền chọn không thực hiện thì không tốn đồng nào" (Practice Q4c):** SAI! Bỏ quyền giúp tránh khoản lỗ tại đáo hạn khi giá đi ngược chiều, nhưng người mua đã mất khoản phí **Premium** trả ngay từ lúc mở hợp đồng.
> 3. **Bẫy Repo vs. Reverse Repo (L01 Cell 29 & Practice Q5a):** Đừng nhầm ai mua/bán hôm nay! Nhớ câu thần chú: **"Repo = Bán hôm nay, Mua lại ngày mai (Đi vay tiền); Reverse Repo = Mua hôm nay, Bán lại ngày mai (Cho vay tiền nhàn rỗi)"**.
> 4. **Bẫy Seniority của Cổ phiếu Ưu đãi & Trách nhiệm Hữu hạn (Practice Q2):** (a) Cổ phiếu ưu đãi đứng trước cổ phiếu thường nhưng **LUÔN ĐỨNG SAU TRÁI CHỦ (Bondholders)**; (b) Không trả cổ tức ưu đãi **không làm công ty phá sản** như vỡ nợ lãi trái phiếu; (c) *Limited liability* chỉ bảo vệ tài sản riêng ngoài công ty, cổ đông hoàn toàn có thể **mất sạch 100% số tiền đã mua cổ phiếu**.
> 5. **Bẫy Giao dịch Thứ cấp là "Huy động vốn vòng mới" (Practice Q1b):** Khi nhà đầu tư này bán lại trái phiếu/cổ phiếu cũ cho nhà đầu tư khác lấy tiền mặt, đó là giao dịch **thị trường thứ cấp** (*transfer of existing financial claim*) — doanh nghiệp phát hành gốc không nhận thêm một đồng vốn mới nào!
> 6. **Bẫy "Giữ nhiều chứng khoán = Chiến lược Thụ động (Passive)" (Practice Q3b):** SAI! Một danh mục giữ hàng trăm mã nhưng liên tục thay đổi tỷ trọng cổ phiếu/trái phiếu theo dự báo lạm phát hoặc sàng lọc tổ chức phát hành có lợi suất hấp dẫn vẫn là **Active Management** (cụ thể là quy trình *Top-down active*).
> 7. **Bẫy Đánh đổi Rủi ro – Lợi nhuận với Quyền chọn Đòn bẩy (Practice Q8d):** Chiến lược mua Call Options + Tiền mặt có thể mang lại **Expected Return cao hơn** mua cổ phiếu cơ sở (do đòn bẩy quyền chọn khuếch đại trạng thái giá tăng), nhưng đồng thời có **Standard Deviation lớn hơn rất nhiều** và xác suất mất sạch phần tiền mua quyền chọn cao hơn $\implies$ chọn chiến lược chỉ nhìn vào Expected Return mà phớt lờ rủi ro biến động và khẩu vị rủi ro cá nhân là sai lầm nghiêm trọng!

---

<a id="lecture-02"></a>
# LECTURE 02: ĐỊNH GIÁ TRÁI PHIẾU, LỢI SUẤT & CẤU TRÚC KỲ HẠN LÃI SUẤT
*(BOND PRICES, YIELDS, AND THE TERM STRUCTURE OF INTEREST RATES)*

---

## 2.1. Trực giác Kinh tế Cốt lõi & Tổng hợp Lý thuyết Toàn diện

### A. Đặc trưng Trái phiếu & Các Biến thể Cấu trúc Dòng tiền
- **Khế ước trái phiếu (Bond Indenture):** Hợp đồng pháp lý giữa tổ chức phát hành (*issuer / borrower*) và trái chủ (*bondholder*), quy định mệnh giá (*par / face value*, chuẩn thường là `USD 1,000`), lãi suất coupon danh nghĩa hàng năm (*annual coupon rate*), kỳ trả lãi, ngày đáo hạn (*maturity*) và các điều khoản bảo vệ/quyền chọn đi kèm.
- **Các loại Trái phiếu Đặc biệt & Đặc tính Rủi ro:**
  1. **Callable Bonds (Trái phiếu có thể mua lại trước hạn):** Trao cho **tổ chức phát hành** quyền mua lại trái phiếu trước ngày đáo hạn tại mức giá mua lại xác định (**Call Price**), thường sau một khoảng thời gian khóa bảo vệ không được mua lại (*call protection period / deferred callable*).
     - *Trực giác kinh tế:* Tổ chức phát hành sẽ thực hiện quyền gọi mua khi **lãi suất thị trường giảm sâu** khiến giá trị trái phiếu thường vượt quá giá gọi mua ($P_{\text{straight}} > P_{\text{call}}$), bởi vì họ có thể thu hồi nợ cũ lãi cao và phát hành nợ mới với lãi suất thấp hơn!
     - Do bất lợi cho người nắm giữ (mất tiềm năng tăng giá và buộc phải tái đầu tư tiền thu hồi ở mức lãi suất thị trường thấp), trái phiếu Callable luôn có **giá thấp hơn** và **lợi suất YTM đòi hỏi cao hơn** trái phiếu không quyền chọn tương đương.
  2. **Puttable Bonds (Trái phiếu có quyền bán lại):** Trao cho **trái chủ** quyền yêu cầu tổ chức phát hành hoàn trả mệnh giá sớm (hoặc gia hạn nếu lãi suất coupon vượt lãi suất thị trường). Có lợi cho nhà đầu tư nên có giá cao hơn và lợi suất đòi hỏi thấp hơn trái phiếu thường.
  3. **Convertible Bonds (Trái phiếu chuyển đổi):** Cho phép trái chủ đổi mỗi trái phiếu lấy một số lượng cổ phiếu phổ thông xác định (**Conversion Ratio** $CR$).
     - *Market Conversion Value* $= P_{\text{stock}} \times CR$.
     - *Conversion Premium* $= P_{\text{convertible bond}} - \text{Market Conversion Value} \ge 0$. Nhờ hưởng lợi thế tăng giá cổ phiếu, trái phiếu chuyển đổi trả lãi suất coupon thấp hơn trái phiếu thường.
  4. **Floating-Rate Bonds (Trái phiếu lãi suất thả nổi):** Lãi suất coupon được đặt lại định kỳ theo một lãi suất tham chiếu thị trường (như SOFR, T-Bill rate) cộng một biên độ cố định (*fixed quoted margin/spread*). **Bẫy lý thuyết cực tinh vi (L02 C4):** Lãi suất coupon chỉ điều chỉnh theo **mặt bằng lãi suất tham chiếu chung**, **KHÔNG điều chỉnh theo sự suy giảm chất lượng tín dụng riêng của tổ chức phát hành**! Do đó nếu tình hình tài chính của công ty xấu đi làm *credit spread* yêu cầu tăng vọt, giá trái phiếu thả nổi vẫn sụt giảm dưới mệnh giá!
  5. **Inverse Floaters (Trái phiếu thả nổi ngược — L02 C7):** Lãi suất coupon biến thiên **ngược chiều** với lãi suất tham chiếu thị trường (ví dụ: $\text{Coupon Rate} = 12\% - 2 \times \text{SOFR}$, chặn dưới tại 0%).
     - *Hiệu ứng khuếch đại kép (Double Whammy):* Khi lãi suất thị trường tăng, nhà đầu tư bị thiệt hại kép: (1) mẫu số chiết khấu tăng làm giảm hiện giá, VÀ (2) tử số tiền coupon nhận được cũng bị cắt giảm! Do đó Inverse Floater có độ nhạy giá với lãi suất (Duration) **cao gấp bội** so với trái phiếu cố định cùng kỳ hạn!
  6. **Catastrophe Bonds (Cat Bonds — L02 C7):** Công cụ chuyển giao rủi ro thảm họa thiên nhiên/đại dịch (như động đất, bão lớn, World Bank pandemic bonds) từ công ty bảo hiểm/chính phủ sang thị trường vốn. Trả lãi suất coupon rất cao trong điều kiện bình thường; nhưng nếu thảm họa vượt ngưỡng kích hoạt xảy ra, trái chủ bị xóa một phần hoặc toàn bộ tiền gốc/lãi để tài trợ khắc phục thảm họa.
  7. **TIPS (Treasury Inflation-Protected Securities — L02 C8 & Practice Q16):**
     - Lãi suất coupon niêm yết trên TIPS là **lãi suất thực cố định ($c_{\text{real}}$)**.
     - Mỗi kỳ, **mệnh giá gốc (Principal/Par)** được điều chỉnh nhân với tỷ lệ lạm phát của kỳ vừa qua trước: $\text{Par}_t = \text{Par}_{t-1}(1 + \pi_t)$; sau đó tiền coupon danh nghĩa của kỳ đó được tính bằng $c_{\text{real}} \times \text{Par}_t$. Vào ngày đáo hạn $T$, nhà đầu tư nhận coupon kỳ cuối cộng với toàn bộ phần mệnh giá gốc đã điều chỉnh lạm phát $\text{Par}_T$. (Trong thực tế TIPS Mỹ có sàn bảo vệ giảm phát *deflation floor* đảm bảo gốc hoàn trả khi đáo hạn không thấp hơn mệnh giá ban đầu `USD 1,000`; trong bài tập lý thuyết nếu đề ghi rõ *"no deflation floor"* như Practice Q16 thì khi $\pi_t < 0$, gốc điều chỉnh giảm bình thường theo công thức!).

---

### B. Giá Sạch (Clean/Flat Price) vs. Lãi Tích Lũy (Accrued Interest) vs. Giá Thanh Toán (Dirty/Invoice Price)
- Khi giao dịch trái phiếu diễn ra vào một ngày nằm giữa hai kỳ trả coupon, người mua sẽ nhận **trọn vẹn 100% tờ séc coupon kế tiếp** từ tổ chức phát hành. Do đó, công bằng kinh tế đòi hỏi người mua phải đền bù ngay lúc thanh toán cho người bán phần lãi coupon tương ứng với số ngày người bán đã nắm giữ trái phiếu kể từ kỳ trả lãi gần nhất — gọi là **Accrued Interest (AI)**.
- **Tại sao báo giá niêm yết trên bảng điện dùng Clean (Flat) Price thay vì Dirty Price?** Nếu niêm yết Dirty Price, ngay cả khi lãi suất thị trường hoàn toàn đứng yên tại mức bằng Coupon Rate, giá trái phiếu vẫn sẽ bò lên mỗi ngày theo hình răng cưa rồi sụt giảm đúng bằng khoản coupon vào ngày trả lãi! Tách riêng Clean Price giúp nhà đầu tư nhìn thấy ngay trái phiếu đang giao dịch ở Premium hay Discount do biến động lãi suất thực sự thay vì nhiễu lịch trả lãi.
- **Đối chiếu với Cổ phiếu (L02 C11):** Cổ phiếu giao dịch **KHÔNG có khoản thanh toán "accrued dividend"** cộng thêm vào giá niêm yết. Ai mua trước ngày giao dịch không hưởng quyền (*ex-dividend date*) và nắm giữ tới ngày đó sẽ nhận toàn bộ cổ tức sắp trả; ai mua từ ngày *ex-dividend* trở đi sẽ không nhận được. Giữ các yếu tố khác không đổi, giá thị trường cổ phiếu tự động điều chỉnh giảm xấp xỉ bằng số tiền cổ tức vào ngày *ex-dividend date*.

---

### C. Yield to Maturity (YTM) vs. Current Yield vs. Holding Period Return vs. Realized Compound Return
1. **Yield to Maturity (YTM):** Lãi suất hoàn vốn nội bộ (IRR) duy nhất làm cho tổng hiện giá của toàn bộ các dòng tiền hứa hẹn trong tương lai bằng đúng giá mua trái phiếu hôm nay (**Dirty Price**, hoặc bằng Clean Price nếu định giá ngay sau ngày trả coupon khi $\text{AI}=0$).
2. **Current Yield:** Chỉ lấy tổng tiền coupon hàng năm chia cho giá trái phiếu ($\frac{\text{Annual Coupon}}{\text{Price}}$). Nó bỏ qua hoàn toàn phần lãi vốn (*capital gain* khi mua chiết khấu $P < \text{Par}$) hoặc lỗ vốn (*capital loss* khi mua phụ trội $P > \text{Par}$) khi trái phiếu kéo dần về mệnh giá lúc đáo hạn (*pull-to-par effect*).
   - **Hệ thức Thứ tự Bất biến (cho trái phiếu thường không quyền chọn):**
     - **Premium Bond ($P > \text{Par}$):** $\text{Coupon Rate} > \text{Current Yield} > \text{YTM}$
     - **Par Bond ($P = \text{Par}$):** $\text{Coupon Rate} = \text{Current Yield} = \text{YTM}$
     - **Discount Bond ($P < \text{Par}$):** $\text{Coupon Rate} < \text{Current Yield} < \text{YTM}$
3. **Realized Compound Return vs. YTM — Giả định Tái đầu tư Sống còn (L02 C19, Q2.2 & Practice Q17):**
   - **Tuyên bố "Mua trái phiếu chính phủ không vỡ nợ tại YTM = 5% và giữ đến đáo hạn sẽ khóa cứng mức sinh lời kép 5%/năm" là ĐÚNG hay SAI?**
     - **SAI đối với mọi trái phiếu có trả coupon!** (Chỉ đúng duy nhất với **Zero-Coupon Bond** vì không có dòng tiền trung gian).
     - YTM chỉ bằng đúng **Realized Compound Annual Return** khi giữ tới đáo hạn **NẾU VÀ CHỈ NẾU toàn bộ các khoản coupon nhận được dọc đường đều có thể tái đầu tư tại mức lãi suất đúng bằng chính YTM ban đầu đó!**
     - **Hai kịch bản lệch pha bắt buộc thuộc lòng:**
       1. Nếu lãi suất tái đầu tư tương lai giảm xuống thấp hơn YTM ban đầu ($r_{\text{reinvest}} < \text{YTM}$): Tổng tài sản tích lũy cuối kỳ $TV_T$ thấp hơn dự kiến $\implies \mathbf{r_{\text{realized}} < \text{YTM}}$ (**Rủi ro tái đầu tư — Reinvestment Rate Risk**).
       2. Nếu ngay sau khi mua, mặt bằng lãi suất thị trường **tăng vọt** (ví dụ từ 5% lên 6%): Giá thị trường tức thời của trái phiếu sụt giảm (nếu bán sớm sẽ lỗ vốn — *Price Risk*), **NHƯNG** nếu nhà đầu tư giữ chặt đến đáo hạn (vẫn nhận đủ mệnh giá gốc) và tái đầu tư toàn bộ các kỳ coupon ở mức lãi suất mới cao hơn 6% $\implies$ **tỷ suất sinh lời kép thực hiện cuối cùng sẽ VƯỢT QUÁ mức 5% YTM ban đầu ($r_{\text{realized}} > \text{YTM}$)!**

---

### D. Cấu trúc Kỳ hạn Lãi suất (The Term Structure of Interest Rates)
1. **Pure Yield Curve vs. On-the-Run Yield Curve (L02 C21):**
   - **Pure Yield Curve (Zero-Coupon / Spot Curve):** Biểu diễn lợi suất đến đáo hạn của các trái phiếu **zero-coupon** (hoặc Treasury STRIPS) không rủi ro vỡ nợ theo kỳ hạn. Đây là chuẩn lý thuyết chính xác nhất để định giá mọi dòng tiền theo thời điểm xuất hiện của nó.
   - **On-the-Run Yield Curve:** Biểu diễn YTM của các trái phiếu coupon Kho bạc vừa mới phát hành gần nhất (*on-the-run*, có thanh khoản cao nhất và thường giao dịch xấp xỉ mệnh giá). Hai đường cong này có thể khác nhau do **hiệu ứng coupon (*coupon effect*)**: hai trái phiếu cùng ngày đáo hạn nhưng khác lãi suất coupon có thể có YTM khác nhau khi đường cong spot không phẳng, bởi YTM chỉ là một mức trung bình phức hợp phi tuyến của các lãi suất spot dọc theo các kỳ trả coupon!
2. **Ba Khái niệm Lãi suất Phải Phân biệt Tuyệt đối (L02 C25):**
   - **Spot Rate ($s_n$ hay $y_n$):** Lãi suất YTM hiệu dụng năm của trái phiếu zero-coupon kỳ hạn $n$ năm giao dịch **ngay hôm nay** (biết chắc chắn tại $t=0$).
   - **Short Rate ($r_n$ hay $r_{n-1,n}$):** Lãi suất ngắn hạn 1 kỳ sẽ thực sự hiện hữu trên thị trường vào thời điểm tương lai từ năm $n-1$ đến năm $n$. Tại thời điểm hôm nay $t=0$ (với $n \ge 2$), $r_n$ là **biến ngẫu nhiên chưa biết trước (*uncertain today*)**!
   - **Implied Forward Rate ($f_n$ hay $f_{n-1,n}$):** Lãi suất kỳ hạn 1 năm cho giai đoạn $[n-1, n]$ **được hàm ý toán học và có thể khóa chặt ngay hôm nay** từ các lãi suất giao ngay $s_{n-1}$ và $s_n$, sao cho việc mua zero-coupon $n$ năm tương đương với việc mua zero-coupon $(n-1)$ năm rồi lăn tiếp 1 năm tại lãi suất $f_n$:
     $$(1 + s_n)^n = (1 + s_{n-1})^{n-1}(1 + f_n)$$
     *(Lưu ý quy ước: $f_1 = s_1$ là lãi suất spot 1 năm hôm nay).*
3. **Các Lý thuyết Giải thích Hình dạng Đường cong Lợi suất (PEH vs. LPT — L02 C25-26, Q2.1, Practice Q20-21):**

| Lý thuyết | Phương trình Liên hệ $f_n$ và $E(r_n)$ | Giải thích Đường cong Spot Dốc Lên ($s_1 < s_2 < s_3$) |
|---|---|---|
| **1. Giả thuyết Kỳ vọng Thuần túy (Pure Expectations Hypothesis — PEH)** | $LP_n = 0 \implies \mathbf{f_n = E(r_n)}$<br>Mọi chiến lược kỳ hạn đều có lợi suất kỳ vọng bằng nhau; nhà đầu tư trung lập với rủi ro kỳ hạn. | Chỉ có **một lời giải thích duy nhất**: Thị trường đang kỳ vọng lãi suất ngắn hạn tương lai $E(r_n)$ sẽ **TĂNG LÊN** vượt mức lãi suất ngắn hạn hiện tại! |
| **2. Lý thuyết Ưa thích Thanh khoản (Liquidity Preference Theory — LPT)** | $\mathbf{f_n = E(r_n) + LP_n}$ với **$LP_n > 0$**<br>Nhà đầu tư chân trời ngắn hạn thống trị thị trường. Giữ trái phiếu dài hạn rồi bán sau 1 năm chịu **rủi ro giá (price risk)** do lãi suất biến động $\implies$ đòi phần bù thanh khoản dương $LP_n > 0$ (thường tăng dần theo kỳ hạn). | Đường cong dốc lên **KHÔNG tự động chứng tỏ lãi suất ngắn hạn được kỳ vọng tăng!** Đường cong dốc lên hoàn toàn nhất quán với việc:<br>- Lãi suất ngắn hạn kỳ vọng tăng, **HOẶC**<br>- Lãi suất ngắn hạn kỳ vọng **đi ngang không đổi** ($E(r_n) = r_1$, toàn bộ độ dốc do $LP_n > 0$ tạo ra — Q2.1 & Practice Q21!), **HOẶC thậm chí**<br>- Lãi suất ngắn hạn kỳ vọng **giảm nhẹ**, nhưng phần bù thanh khoản $LP_n$ đủ lớn để áp đảo mức giảm đó! |
| **3. Nhà đầu tư Dài hạn Thống trị (Preferred Habitat / Long-horizon Dominance)** | Nếu các định chế chân trời dài hạn (quỹ hưu trí, bảo hiểm) thống trị, nắm giữ trái phiếu ngắn hạn lăn vòng lại chịu **rủi ro tái đầu tư (reinvestment risk)**. | Khi đó họ sẵn sàng trả giá cao cho trái phiếu dài hạn để khóa lãi suất $\implies$ phần bù kỳ hạn có thể âm, làm **$f_n < E(r_n)$**! |

---

## 2.2. Hệ thống Công thức Đầy đủ & Quy ước Ghép lãi (Lecture 02)

### 1. Phương trình Fisher Chính xác & Định giá Dòng tiền TIPS
- **Exact Fisher Equation:** Liên hệ lãi suất danh nghĩa $R$, lãi suất thực $r$, và tỷ lệ lạm phát $\pi$:
  $$(1 + R) = (1 + r)(1 + \pi) \iff r = \frac{R - \pi}{1 + \pi}, \qquad \text{Xấp xỉ khi } \pi \text{ nhỏ: } R \approx r + \pi$$
- **Lịch thanh toán TIPS (Lãi suất coupon thực hàng năm $c_{\text{real}}$, gốc ban đầu $\text{Par}_0$):**
  $$\text{Par}_t = \text{Par}_{t-1}(1 + \pi_t) = \text{Par}_0 \prod_{j=1}^t (1 + \pi_j)$$
  $$\text{Coupon}_t = c_{\text{real}} \times \text{Par}_t, \qquad \text{Total Payment}_t = \begin{cases} \text{Coupon}_t & (t < T) \\ \text{Coupon}_T + \text{Par}_T & (t = T) \end{cases}$$

### 2. Định giá Trái phiếu Chuẩn (Annual & Semiannual), YTC & Quy đổi APR – EAR
Với tần suất trả lãi $m$ lần/năm ($m=1$ cho annual, $m=2$ cho semiannual), kỳ hạn còn lại $T$ năm $\implies$ tổng số kỳ trả lãi $N = mT$, tiền coupon mỗi kỳ $C_p = \frac{\text{Coupon Rate} \times \text{Par}}{m}$, lãi suất chiết khấu mỗi kỳ $r_p = \frac{\text{YTM}_{\text{APR}}}{m}$:
$$P_B = \sum_{k=1}^{N} \frac{C_p}{(1 + r_p)^k} + \frac{\text{Par}}{(1 + r_p)^N} = C_p \cdot \frac{1 - (1 + r_p)^{-N}}{r_p} + \frac{\text{Par}}{(1 + r_p)^N}$$
- **Yield to First Call (YTC):** Gọi $T_c$ là số năm tới ngày được phép gọi mua đầu tiên ($N_c = m T_c$) và $P_{\text{call}}$ là giá gọi mua lại:
  $$P_B = C_p \cdot \frac{1 - (1 + r_c)^{-N_c}}{r_c} + \frac{P_{\text{call}}}{(1 + r_c)^{N_c}}, \qquad \text{YTC}_{\text{APR}} = m \cdot r_c$$
- **Giá Trái phiếu Có quyền Mua lại Ngay lập tức (Immediate Call Cap — L02 C18, Q2.3, Practice Q37):**
  $$P_{\text{callable}} = \min\left(P_{\text{straight}}, \, P_{\text{call}}\right)$$
- **Quy đổi Nominal Annual Yield (APR / Bond Equivalent Yield) sang Effective Annual Yield (EAR):**
  $$\text{EAR} = \left(1 + \frac{\text{APR}}{m}\right)^m - 1 = (1 + r_p)^m - 1$$

### 3. Lãi Tích Lũy (Accrued Interest) & Giá Hóa Đơn Thanh Toán (Dirty / Invoice Price)
$$\text{Accrued Interest (AI)} = C_p \times \frac{\text{Days since last coupon payment}}{\text{Total days in coupon period}}$$
$$\text{Dirty (Invoice / Full) Price} = \text{Clean (Flat / Quoted) Price} + \text{AI}$$
*(Nếu đề bài báo giá Clean Quote $q$ trên mỗi 100 mệnh giá và nhà đầu tư mua tổng mệnh giá $F_{\text{total}}$, thì $\text{Clean Value} = F_{\text{total}} \times \frac{q}{100}$ và $\text{Total AI} = F_{\text{total}} \times \frac{c_{\text{annual}}}{m} \times \frac{d_{\text{elapsed}}}{d_{\text{period}}}$).*

### 4. Realized Compound Annual Return ($r_{\text{realized}}$)
Giả sử mua trái phiếu giá $P_0$, giữ đến đáo hạn $T$ năm, nhận mệnh giá $\text{Par}$ cộng với tổng giá trị tương lai tích lũy của toàn bộ các khoản coupon tái đầu tư tới năm $T$ là $\text{FV}_{\text{coupons}, T}$:
$$\text{Terminal Wealth } TV_T = \text{Par} + \text{FV}_{\text{coupons}, T}, \qquad r_{\text{realized}} = \left(\frac{TV_T}{P_0}\right)^{1/T} - 1$$

### 5. Định giá theo Đường cong Spot Rates & Lãi suất Kỳ hạn Hàm ý (Forward Rates)
- **Định giá không chênh lệch giá bằng Spot Rates ($s_1, s_2, \dots, s_T$):**
  $$P_B = \frac{CF_1}{1 + s_1} + \frac{CF_2}{(1 + s_2)^2} + \dots + \frac{CF_T}{(1 + s_T)^T} = \sum_{t=1}^T CF_t \cdot d_t$$
  trong đó $d_t = (1+s_t)^{-t} = \frac{P_{\text{zero}, t}}{\text{Par}_{\text{zero}}}$ là hệ số chiết khấu (giá của USD 1 mệnh giá zero-coupon kỳ hạn $t$).
- **Công thức Tổng quát Forward Rate giữa năm $k$ và năm $n$ ($n > k$):**
  $$(1 + s_n)^n = (1 + s_k)^k (1 + f_{k,n})^{n-k} \implies \mathbf{f_{k,n} = \left[\frac{(1 + s_n)^n}{(1 + s_k)^k}\right]^{\frac{1}{n-k}} - 1}$$
  Với kỳ hạn 1 năm từ $n-1$ đến $n$:
  $$\mathbf{f_{n-1,n} = \frac{(1 + s_n)^n}{(1 + s_{n-1})^{n-1}} - 1}$$

---

## 2.3. Quy trình Giải nhanh Bài tập Tính toán Phòng thi (Lecture 02)

### Dạng 2.1: Bootstrapping Spot Rate Còn Thiếu & Sao Chép Trái Phiếu Coupon Bằng Zero-Coupon Bonds (Practice Q22 & Q23)
- **Bài toán Bootstrapping (Practice Q22):** Cho $s_1 = 3\%, s_2 = 4\%$. Trái phiếu Chi 3 năm trả coupon năm 40, mệnh giá 1,000 có giá chuẩn theo đường cong là 980. Tìm $s_3$ và định giá trái phiếu Psi 3 năm trả coupon 25.
  1. *Bước 1:* Tách riêng các dòng tiền đã biết lãi suất spot ở năm 1 và năm 2 ra khỏi giá trái phiếu Chi:
     $$PV(CF_1 + CF_2) = \frac{40}{1.03} + \frac{40}{(1.04)^2} = 38.834951 + 36.982249 = 75.817200$$
  2. *Bước 2:* Phần giá trị còn lại chính là hiện giá của dòng tiền cuối $CF_3 = 1,040$:
     $$\frac{1,040}{(1 + s_3)^3} = 980 - 75.817200 = 904.182800 \implies (1+s_3)^3 = \frac{1,040}{904.182800} = 1.150210 \implies s_3 = (1.150210)^{1/3} - 1 \approx \mathbf{4.78\%}$$
  3. *Bước 3:* Dùng ngay các hệ số chiết khấu vừa tìm được để định giá Psi ($CF = 25, 25, 1025$):
     $$P_{\text{Psi}} = \frac{25}{1.03} + \frac{25}{1.04^2} + \frac{1,025}{1.150210} = 24.271845 + 23.113905 + 891.141767 = \mathbf{938.53}$$
- **Bài toán Sao chép bằng Danh mục Zero-Coupon (Practice Q23):** Trái phiếu coupon 6% năm trên mệnh giá `10,000` trả `600` năm 1, `600` năm 2, và `10,600` năm 3. Nếu giá các zero-coupon trên mỗi 100 mệnh giá là $96.00, 91.00, 85.50$:
  - Mua đúng mệnh giá zero 1 năm = `600`, zero 2 năm = `600`, zero 3 năm = `10,600`.
  - Tổng chi phí danh mục sao chép $= 600(0.96) + 600(0.91) + 10,600(0.855) = 576 + 546 + 9,063 = \mathbf{10,185.00}$ (tương ứng báo giá hợp lý `101.85` per 100). Nếu thị trường báo giá trái phiếu coupon ở `102.60` (`10,260.00`), trái phiếu coupon đang bị **định giá quá cao (overpriced)** mất `75.00` (`0.75` per 100) $\implies$ bán trái phiếu coupon, mua danh mục zero để hưởng chênh lệch phi rủi ro!

### Dạng 2.2: Tính Siêu Tốc Realized Compound Return với Lãi suất Tái đầu tư Thay đổi theo Từng Năm (Practice Q17)
- **Đề chuẩn Practice Q17:** Mua trái phiếu 3 năm giá $P_0 = 970$, mệnh giá $1,000$, coupon năm $C = 50$. Tiền mặt coupon tích lũy sinh lãi $2\%$ từ năm 1 sang năm 2, và $7\%$ từ năm 2 sang năm 3.
  1. *Coupon năm 1 ($t=1$ nhận 50):* Sinh lãi qua 2 chặng (năm 1$\to$2 tại $2\%$, năm 2$\to$3 tại $7\%$): $\text{FV}_1 = 50 \times (1.02) \times (1.07) = 54.57$.
  2. *Coupon năm 2 ($t=2$ nhận 50):* Sinh lãi qua 1 chặng (năm 2$\to$3 tại $7\%$): $\text{FV}_2 = 50 \times (1.07) = 53.50$.
  3. *Dòng tiền năm 3 ($t=3$):* Nhận trực tiếp coupon $50$ + mệnh giá $1,000 = 1,050.00$.
  4. *Tổng tài sản cuối năm 3:* $TV_3 = 54.57 + 53.50 + 1,050.00 = \mathbf{1,158.07}$.
  5. *Realized Compound Annual Return:* $r_{\text{realized}} = \left(\frac{1,158.07}{970}\right)^{1/3} - 1 = (1.193887)^{1/3} - 1 \approx \mathbf{6.085\% \approx 6.09\%}$ (thấp hơn YTM lúc mua là $6.12\%$ do lãi tái đầu tư năm đầu quá thấp ở mức $2\%$!).

### Dạng 2.3: Khôi phục Lạm phát Ẩn trên TIPS (Practice Q16)
- Gốc đầu kỳ $\text{Par}_0 = 2,000$, lãi suất thực $c_{\text{real}} = 2.5\%$, lạm phát năm 1 là $\pi_1 = 3\%$, biết tiền coupon thực trả ở cuối năm 2 là $\text{Coupon}_2 = 53.56$. Tìm $\pi_2$:
  1. Gốc điều chỉnh cuối năm 1: $\text{Par}_1 = 2,000 \times 1.03 = 2,060.00$ ($\implies \text{Coupon}_1 = 2,060 \times 0.025 = 51.50$).
  2. Từ $\text{Coupon}_2 = c_{\text{real}} \times \text{Par}_2 = 53.56 \implies \text{Par}_2 = \frac{53.56}{0.025} = 2,142.40$.
  3. Lạm phát năm 2: $1 + \pi_2 = \frac{\text{Par}_2}{\text{Par}_1} = \frac{2,142.40}{2,060.00} = 1.04 \implies \mathbf{\pi_2 = 4.00\%}$!
  4. Năm 3 có giảm phát $\pi_3 = -1\%$: $\text{Par}_3 = 2,142.40 \times (1 - 0.01) = 2,120.976 \approx 2,120.98$, $\text{Coupon}_3 = 2,120.976 \times 0.025 = 53.0244 \approx 53.02$, tổng thanh toán năm 3 $= 2,120.976 + 53.0244 = \mathbf{2,174.0004 \approx 2,174.00}$.

---

## 2.4. Các Bẫy Lý thuyết & Lỗi Sai Chết Người trong MCQ (Lecture 02)

> [!WARNING]
> **7 BẪY LÝ THUYẾT & TÍNH TOÁN CHÍ MẠNG CỦA LECTURE 02:**
> 1. **Bẫy "Quên chia đôi hoặc chỉ chia một vế" với Trái phiếu Semiannual (Practice Q10b):** Khi trả lãi bán niên, phải thực hiện **ĐỒNG THỜI 3 phép biến đổi**: chia đôi coupon ($C/2$), chia đôi YTM danh nghĩa ($Y/2$), và nhân đôi số năm ($2T$). Ngoài ra khi giải ngược ra lãi suất bán niên $r_{\text{6m}}$ (ví dụ $3.104\%$), phải nhớ: **Nominal Annual YTM (APR)** $= 2 \times r_{\text{6m}} = 6.21\%$, còn **Effective Annual Yield (EAR)** $= (1 + r_{\text{6m}})^2 - 1 = 6.30\%$!
> 2. **Bẫy "Chiết khấu toàn bộ dòng tiền của trái phiếu coupon bằng Spot Rate kỳ đáo hạn cuối $s_T$" (Practice Q22c):** Sai lầm chết người! Khi đường cong lợi suất không phẳng (ví dụ dốc lên $s_1 < s_2 < s_3$), việc lấy $s_3$ chiết khấu cả coupon năm 1 và năm 2 sẽ áp mức lãi suất quá cao cho các dòng tiền sớm, làm **định giá thấp (understate)** giá trị hợp lý của trái phiếu! Mỗi dòng tiền tại năm $t$ bắt buộc phải được chiết khấu bằng đúng spot rate $s_t$ của năm đó.
> 3. **Bẫy "YTC thấp hơn YTM chứng tỏ tổ chức phát hành chắc chắn sẽ gọi mua lại trái phiếu" (L02 Q2.5 & Practice Q15c):** SAI! Việc $\text{YTC} < \text{YTM}$ hôm nay làm cho YTC trở thành ước tính thận trọng hơn (*yield to worst*), nhưng quyết định có thực sự gọi mua vào ngày call trong tương lai (ví dụ 2 năm hoặc 6 năm tới) phụ thuộc vào **lãi suất tái cấp vốn trên thị trường tại thời điểm tương lai đó** — điều chưa hề chắc chắn ở hiện tại!
> 4. **Bẫy "Đường cong lợi suất dốc lên chứng minh thị trường kỳ vọng lãi suất ngắn hạn tăng" (L02 Q2.1 & Practice Q21):** SAI dưới Liquidity Preference Theory! Đường cong dốc lên vừa không loại trừ PEH, vừa không loại trừ LPT, và cũng không tự thiết lập (chứng minh) bất kỳ giả thuyết nào nếu không biết trước phần bù thanh khoản $LP_t$. Khi $LP_t$ thay đổi (Practice Q20b), **Forward rate $f_t$ vẫn giữ nguyên cố định** vì $f_t$ chỉ phụ thuộc vào đường cong Spot quan sát được; thứ thay đổi chính là suy luận về $E(r_{t-1,t}) = f_t - LP_t$!
> 5. **Bẫy "Lãi vốn trên Zero-Coupon 3 năm bằng 13.6% nghĩa là lợi suất năm là 13.6%" (Practice Q11b):** Mua giá 4,320 so với mệnh giá 5,000 rẻ hơn $13.6\%$ mệnh giá (tương đương tổng HPR 3 năm là $\frac{5,000 - 4,320}{4,320} = 15.74\%$), còn lợi suất ghép lãi hàng năm chỉ là $(5,000/4,320)^{1/3} - 1 = \mathbf{5.00\%}$!
> 6. **Bẫy "Mua trái phiếu YTM 5% rồi bán sau 1 năm thì HPR 1 năm luôn bằng 5%" (Practice Q24d):** Hoàn toàn sai! HPR 1 năm chỉ bằng đúng 5% nếu sau 1 năm YTM của trái phiếu 2 năm còn lại vẫn đứng yên ở 5%. Nếu YTM tại ngày bán vọt lên 8%, giá bán sụt giảm làm HPR 1 năm tụt xuống gần 0% hoặc âm; nếu YTM giảm xuống 3%, giá bán tăng vọt đẩy HPR 1 năm lên gần 9%!
> 7. **Bẫy Trừ nhầm Coupon vào Giá Gọi mua ngày Call (Practice Q15a):** Vào ngày trả coupon năm thứ 2, người nắm giữ nhận đồng thời khoản coupon định kỳ năm 2 **CỘNG VỚI** khoản tiền thanh toán gọi mua lại (*call price / call payment*). Khi giải phương trình $P_0 = \frac{C}{1+y_c} + \frac{C + P_{\text{call}}}{(1+y_c)^2}$, nhớ tách riêng coupon $C$ ra để không báo nhầm tổng $(C + P_{\text{call}})$ thành giá gọi mua $P_{\text{call}}$!


---

<a id="lecture-03"></a>
# LECTURE 03: DURATION, CONVEXITY & QUẢN TRỊ DANH MỤC TRÁI PHIẾU
*(DURATION, CONVEXITY, AND IMMUNIZATION)*

---

## 3.1. Trực giác Kinh tế Cốt lõi & Tổng hợp Lý thuyết Toàn diện

### A. Năm Quy tắc Định giá Trái phiếu của Malkiel (Malkiel's Five Bond-Pricing Relationships)
Mọi thước đo rủi ro lãi suất trong thu nhập cố định đều bắt nguồn từ hình dạng toán học của hàm giá trái phiếu không kèm quyền chọn (*option-free bond*) theo YTM. Burton Malkiel đúc kết **5 định luật nền tảng** (cực hay hỏi trong MCQ):

1. **Quy tắc 1 (Quan hệ nghịch biến):** Giá trái phiếu và lợi suất đáo hạn (YTM) biến động **ngược chiều nhau** ($\frac{\partial P}{\partial y} < 0$). Khi lãi suất tăng, hệ số chiết khấu mẫu số tăng lên làm hiện giá các dòng tiền cố định sụt giảm.
2. **Quy tắc 2 (Tính bất đối xứng có lợi — Nguồn gốc của Positive Convexity):** Với cùng một biên độ biến động lãi suất $|\Delta y|$, mức **giảm giá** khi YTM tăng **nhỏ hơn** mức **tăng giá** khi YTM giảm cùng biên độ đó:
   $$|P(y + \Delta y) - P(y)| < |P(y - \Delta y) - P(y)|$$
   *Trực giác:* Đường cong Giá – Lợi suất uốn cong lồi về phía gốc tọa độ (*convex toward the origin*, $\frac{\partial^2 P}{\partial y^2} > 0$).
3. **Quy tắc 3 (Hiệu ứng kỳ hạn đáo hạn $T$):** Kỳ hạn đáo hạn càng dài, giá trái phiếu càng nhạy cảm với biến động lãi suất (xét trên các trái phiếu ngang giá, phụ trội và zero-coupon thông thường).
   - *Lưu ý ngoại lệ tinh tế cho MCQ nâng cao:* Đối với trái phiếu trả coupon rất thấp đang giao dịch chiết khấu cực sâu (*very deep-discount coupon bonds*) ở kỳ hạn cực dài, Macaulay Duration có thể đạt đỉnh rồi hơi lùi nhẹ về tiệm cận của niên kim vĩnh cửu $D_{\infty} = \frac{1+y}{y}$; nhưng với trái phiếu ngang giá (*par*), phụ trội (*premium*) và *zero-coupon*, độ nhạy giá **luôn tăng đơn điệu** theo kỳ hạn $T$.
4. **Quy tắc 4 (Tốc độ tăng độ nhạy giảm dần theo kỳ hạn):** Độ nhạy giá tăng theo kỳ hạn đáo hạn nhưng **với tốc độ giảm dần** (*sensitivity increases at a decreasing rate as maturity lengthens*). Ví dụ: bước nhảy độ nhạy từ trái phiếu 1 năm lên 5 năm lớn hơn rất nhiều so với bước nhảy từ 25 năm lên 29 năm (do dòng tiền năm thứ 29 đã bị chiết khấu rất nhỏ trong hiện tại).
5. **Quy tắc 5 (Hiệu ứng lãi suất Coupon & Mặt bằng YTM đầu kỳ):**
   - **Lãi suất coupon càng thấp**, độ nhạy cảm giá của trái phiếu càng **lớn** (vì tỷ trọng hiện giá hoàn trả sớm qua các kỳ coupon nhỏ, phần lớn giá trị dồn vào mệnh giá cuối kỳ; đạt cực đại tuyệt đối ở **Zero-Coupon Bond**).
   - **Bổ đề mở rộng (Hiệu ứng mặt bằng YTM ban đầu):** Giữ nguyên coupon và kỳ hạn, khi **YTM ban đầu càng thấp**, cả Macaulay Duration và Modified Duration đều **lớn hơn** (vì ở lãi suất thấp, mệnh giá xa trong tương lai bị chiết khấu ít hơn nên chiếm tỷ trọng hiện giá lớn hơn).

---

### B. Macaulay Duration, Modified Duration, Dollar Duration & DV01
1. **Bản chất Vật lý – Tài chính của Macaulay Duration ($D$):**
   - Thời gian đáo hạn danh nghĩa $T$ chỉ nhìn vào ngày trả khoản tiền **cuối cùng**, bỏ qua toàn bộ lịch trả coupon trung gian.
   - **Macaulay Duration ($D$)** của Frederick Macaulay là **thời gian đáo hạn trung bình gia quyền của toàn bộ các dòng tiền** (*weighted-average time until cash flows are received*), trong đó trọng số $w_k$ của kỳ $k$ chính là **tỷ trọng Giá trị Hiện tại (Present Value share)** của dòng tiền kỳ đó trong tổng giá trái phiếu hôm nay ($w_k = \frac{PV(CF_k)}{P_0}$).
   - Hình ảnh trực giác: Hãy tưởng tượng thanh thước thời gian từ $0$ đến $T$, tại mỗi mốc trả tiền treo một quả cân nặng đúng bằng $PV(CF_k)$. **Macaulay Duration $D$ chính là điểm tựa trọng tâm (fulcrum / center of gravity)** giúp thanh thước cân bằng nằm ngang!
   - **Ba mốc chuẩn thuộc lòng để kiểm tra nhanh kết quả bấm máy:**
     - **Zero-Coupon Bond:** Chỉ có duy nhất 1 quả cân tại $t = T \implies w_T = 1 \implies \mathbf{D = T}$ (luôn bằng đúng số năm đáo hạn, **hoàn toàn độc lập** với mức YTM hay quy ước ghép lãi năm/bán niên!).
     - **Coupon-Bearing Bond ($C > 0$):** Có các quả cân phụ nằm rải từ kỳ $1$ đến $T-1$ kéo trọng tâm về bên trái $\implies$ luôn có **$D < T$**.
     - **Perpetuity / Consol Bond ($T \to \infty$, trả lãi cố định hàng kỳ mãi mãi):** Dù kỳ hạn là vô cực ($T = \infty$), hiện giá các dòng tiền quá xa tiến về 0 nên trọng tâm hữu hạn tại $\mathbf{D = \frac{1 + y}{y}}$ (tính theo kỳ; nếu ghép lãi $f$ lần/năm với lãi suất danh nghĩa năm $Y$ thì $D_{\text{years}} = \frac{1 + Y/f}{Y}$ và $D_M = \frac{1}{Y}$).

2. **Modified Duration ($D_M$) — Thước đo Trực tiếp Độ Co giãn Giá:**
   - Lấy đạo hàm bậc nhất của giá trái phiếu theo lợi suất danh nghĩa năm $Y$ (ghép lãi $f$ lần/năm):
     $$\frac{dP}{dY} = -\frac{1}{1 + Y/f} \sum_{k=1}^{fT} \left(\frac{k}{f}\right) PV(CF_k) = -\left(\frac{D}{1 + Y/f}\right) P_0 = -D_M \cdot P_0$$
   - Suy ra $\frac{dP}{P_0} = -D_M \, dY$: Khi YTM năm thay đổi một lượng nhỏ $\Delta Y$, phần trăm thay đổi giá xấp xỉ bằng **$-D_M \times \Delta Y$**.
   - **So sánh tinh tế giữa Annual ($f=1$) và Semiannual ($f=2$) (Practice Q26):**
     - *Tình huống 1 (Cùng Macaulay Duration $D$ và cùng YTM năm $Y$):* Trái phiếu trả lãi bán niên có mẫu số $1 + Y/2 < 1 + Y \implies D_{M,\text{semi}} = \frac{D}{1 + Y/2} > \frac{D}{1 + Y} = D_{M,\text{annual}}$. Vậy **trái phiếu bán niên nhạy cảm giá hơn**!
     - *Tình huống 2 (Cùng coupon rate danh nghĩa, cùng kỳ hạn $T$ và cùng YTM năm $Y$):* Trái phiếu bán niên trả nửa khoản coupon sớm hơn nửa năm ở mỗi năm, kéo trọng tâm $D$ sang trái đáng kể làm cả $D$ lẫn $D_M$ thường nhỏ hơn trái phiếu trả lãi năm.

3. **Dollar (Money) Duration & Price Value of a Basis Point (DV01 / PVBP):**
   - $D_M$ đo biến động theo **tỷ lệ `%`**, còn quản trị rủi ro bàn giao dịch (*trading desk*) cần biết mình lãi/lỗ bao nhiêu **tiền tuyệt đối (USD/EUR)**.
   - **Money (Dollar) Duration:** $DD = P_0 \times D_M \implies \Delta P \approx -DD \times \Delta Y$.
   - **DV01 (Dollar Value of 01 basis point):** Mức thay đổi giá bằng tiền khi YTM dịch chuyển đúng $1\text{ bp} = 0.01\% = 0.0001$:
     $$\text{DV01} = P_0 \times D_M \times 0.0001 = \frac{DD}{10,000}$$

4. **Duration của Danh mục Trái phiếu (Portfolio Duration):**
   - Duration (Macaulay hoặc Modified, khi dùng cùng chuẩn ghép lãi) của một danh mục là **trung bình gia quyền theo Giá trị Thị trường (Market-Value Weights)** của các trái phiếu thành phần:
     $$D_P = \sum_{i=1}^{m} w_i D_i \quad \text{và} \quad D_{M,P} = \sum_{i=1}^{m} w_i D_{M,i}, \quad \text{với } w_i = \frac{V_i}{\sum_{j=1}^m V_j}$$
   - Tổng Dollar Duration và tổng DV01 của danh mục có **tính cộng tuyến tính trực tiếp**: $\text{DV01}_P = \sum_{i=1}^m \text{DV01}_i$. (Nếu bán khống một trái phiếu để phòng hộ *hedge*, vị thế short mang dấu âm!).

---

### C. Độ lồi (Convexity): Bản chất Hình học, Xấp xỉ Taylor Bậc 2 & Negative Convexity
1. **Tại sao Xấp xỉ Tuyến tính Duration-Only luôn có Sai số Một chiều?**
   - Xấp xỉ bậc nhất $\Delta P \approx -(P_0 D_M)\Delta Y$ chính là **đường thẳng tiếp tuyến (tangent line)** tiếp xúc với đường cong giá thực tại điểm $(Y_0, P_0)$.
   - Đối với mọi trái phiếu không kèm quyền chọn (*option-free bond*), đường cong giá lồi nghiêm ngặt ($C > 0$) nên nằm **hoàn toàn phía trên** đường thẳng tiếp tuyến tại mọi điểm $\Delta Y \ne 0$:
     - **Khi lãi suất TĂNG ($\Delta Y > 0$):** Giá thực giảm chậm dần nhờ độ lồi, còn đường tiếp tuyến lao dốc thẳng tuột $\implies$ Duration-only **phóng đại mức giảm giá (overstates the price decline)** $\implies P_{\text{Duration}} < P_{\text{Actual}}$.
     - **Khi lãi suất GIẢM ($\Delta Y < 0$):** Giá thực tăng vọt nhanh dần nhờ độ lồi, còn đường tiếp tuyến tăng tuyến tính chậm hơn $\implies$ Duration-only **đánh giá thấp mức tăng giá (understates the price increase)** $\implies P_{\text{Duration}} < P_{\text{Actual}}$.
   - **Định lý Vàng cho MCQ (L03 Cell 16 & Practice Q29–Q31):** Đối với trái phiếu có độ lồi dương ($C > 0$), phép xấp xỉ chỉ dùng Duration **LUÔN LUÔN dự báo thấp hơn giá thực tế mới ($P_{\text{Duration}} < P_{\text{Actual}}$) cho CẢ HAI CHIỀU tăng và giảm lãi suất!**

2. **Khai triển Taylor Bậc 2 (Duration + Convexity Approximation):**
   - Bổ sung đạo hàm bậc hai chuẩn hóa $C = \frac{1}{P_0}\frac{d^2 P}{dY^2}$ vào khai triển Taylor quanh $Y_0$:
     $$\frac{\Delta P}{P_0} \approx -D_M (\Delta Y) + \frac{1}{2} C (\Delta Y)^2$$
   - Hãy chú ý dấu của số hạng thứ hai: Vì $(\Delta Y)^2 > 0$ bất kể $\Delta Y$ âm hay dương, nên khi $C > 0$, lượng hiệu chỉnh **$\frac{1}{2}C(\Delta Y)^2$ LUÔN MANG DẤU DƯƠNG ($> 0$)**!
     - Khi $\Delta Y > 0$: Số hạng dương này đỡ bớt đà rơi của $-D_M\Delta Y$.
     - Khi $\Delta Y < 0$: Số hạng dương này cộng thêm vào đà tăng của $-D_M\Delta Y$.
   - Với biến động nhỏ ($\pm 5$ đến $10\text{ bps}$), $(\Delta Y)^2$ cực bé (ví dụ $0.001^2 = 10^{-6}$) nên Duration-only rất sát. Với cú sốc lớn ($\pm 100$ đến $300\text{ bps}$), số hạng Convexity trở nên quyết định.
   - **Giá trị kinh tế của Convexity trên thị trường:** Nếu hai trái phiếu có cùng xếp hạng tín nhiệm và cùng Duration nhưng trái phiếu A có Convexity cao hơn B, nhà đầu tư ưa chuộng A hơn (lãi dày hơn khi lãi suất giảm, lỗ mỏng hơn khi lãi suất tăng) $\implies$ thị trường định giá A cao hơn, tức A giao dịch với **YTM cân bằng thấp hơn** B (*convexity premium*).

3. **Độ lồi Âm (Negative Convexity) của Trái phiếu Có thể Mua lại (Callable Bond) & Effective Duration/Convexity:**
   - Với trái phiếu kèm quyền chọn mua lại (*callable bond*), khi lãi suất thị trường ở mức rất cao (xa phía trên coupon rate), xác suất bị gọi mua rất thấp nên nó cư xử giống trái phiếu thường (vùng **Positive Convexity**).
   - Khi lãi suất giảm xuống sát hoặc thấp hơn coupon rate, tổ chức phát hành có động lực gọi mua lại ở trần giá $P_{\text{call}}$. Đà tăng giá bị "ép trần" (*price compression*), khiến đường cong Giá – Lợi suất uốn cong lõm xuống phía dưới $\implies$ **Độ lồi Âm ($C < 0$, Negative Convexity)**!
   - Hệ quả kép bất lợi cho người nắm giữ Callable Bond ở vùng lãi suất thấp: Khi lãi suất giảm tiếp thì giá hầu như không tăng thêm (bị chặn bởi $P_{\text{call}}$), nhưng nếu lãi suất bật tăng trở lại thì giá rơi tự do như trái phiếu dài hạn! (Để bù đắp, callable bond lúc phát hành phải trả YTM / coupon cao hơn straight bond tương đương).
   - Vì dòng tiền của trái phiếu kèm quyền chọn (Callable, Putable, Mortgage-Backed Securities — MBS có rủi ro trả nợ trước hạn *prepayment risk*) **thay đổi nội sinh khi lãi suất biến động**, ta không thể dùng công thức Macaulay/Analytical cố định dòng tiền mà bắt buộc dùng **Sai phân Hữu hạn (Finite-Difference / Effective Duration & Effective Convexity)** thông qua mô hình định giá lại ở $Y - h$ và $Y + h$.

---

### D. Quản trị Danh mục Trái phiếu Thụ động: Indexing, Cash-Flow Matching & Redington Immunization
Nhà quản lý thụ động coi giá thị trường là hợp lý và tập trung kiểm soát rủi ro hoặc sao chép chuẩn thay vì đầu cơ dự báo lãi suất:

| Chiến lược | Mục tiêu & Cơ chế Vận hành | Ưu điểm, Hạn chế & Yêu cầu Tái cân bằng |
|---|---|---|
| **1. Quỹ Chỉ số Trái phiếu (Bond-Index Funds)** | Sao chép hiệu quả của một chỉ số trái phiếu rộng (Bloomberg US Aggregate, Government/Corporate Index). Do số lượng mã quá lớn (hàng ngàn trái phiếu), giao dịch kém thanh khoản (*thinly traded*) và rổ chỉ số biến động liên tục khi trái phiếu đáo hạn/bị gọi mua/phát hành mới, quỹ áp dụng **Lấy mẫu Phân tầng (Stratified Sampling / Cellular Approach)**: chia vũ trụ trái phiếu thành ma trận các ô (*cells*) theo kỳ hạn, loại tổ chức phát hành, xếp hạng tín nhiệm, mức coupon rồi mua mẫu đại diện khớp đúng tỷ trọng thị trường từng ô. | - Đa dạng hóa rộng, chi phí thấp.<br>- Vẫn có sai số bám sát nhỏ (*tracking error*) và phải điều chỉnh định kỳ khi trái phiếu rơi khỏi khung kỳ hạn của chỉ số (thường $> 1$ năm). |
| **2. Khớp Dòng tiền Tuyệt đối (Cash-Flow Matching / Dedication)** | Mua một danh mục trái phiếu (zero-coupon strips hoặc chuỗi trái phiếu coupon giải ngược từ kỳ xa nhất về gần nhất) sao cho tổng tiền lãi + gốc thu về ở **từng mốc thời gian** khớp chính xác 100% số tiền nghĩa vụ nợ phải chi trả tại đúng mốc thời gian đó. | - **Ưu điểm vô địch:** Triệt tiêu hoàn toàn cả Price Risk lẫn Reinvestment Risk; **KHÔNG cần tái cân bằng (*once-and-for-all*)**; an toàn tuyệt đối ngay cả dưới các cú xoắn đường cong lợi suất không song song (*non-parallel twists*)!<br>- **Hạn chế:** Tốn kém hơn, bị áp đặt quá nhiều ràng buộc chọn mã, đôi khi thị trường không có sẵn trái phiếu đủ kỳ hạn cực dài (30–40 năm) cho quỹ hưu trí. |
| **3. Miễn nhiễm Lãi suất (Redington Immunization — Single Liability)** | Bảo vệ giá trị tài sản ròng cho một nghĩa vụ nợ cố định tại chân trời $H$ bằng cách cho **Price Risk** và **Reinvestment Risk** tự triệt tiêu lẫn nhau thông qua khớp Hiện giá, khớp Duration và giữ Convexity tài sản lớn hơn nợ. | - Linh hoạt hơn Dedication rất nhiều.<br>- **BẮT BUỘC phải tái cân bằng định kỳ (*rebalancing required*)**.<br>- Chỉ miễn nhiễm hoàn hảo trước **dịch chuyển song song (*parallel shifts*)** tức thời nhỏ/vừa; vẫn **dễ tổn thương trước dịch chuyển không song song (*non-parallel shifts / twists*)**! |

#### Giải phẫu Sâu Cơ chế Redington Immunization (Trọng tâm Đề thi Tự luận & MCQ!)
1. **Cơ chế triệt tiêu hai rủi ro ngược chiều tại $H = D_A$:**
   - Giả sử quỹ bảo hiểm phải trả nghĩa vụ đơn lẻ tại năm $H$. Nếu quỹ mua trái phiếu coupon có kỳ hạn $T > H$ nhưng có **Macaulay Duration $D_A = H$**:
     - Nếu lãi suất **tăng** ngay sau khi mua: Giá bán trái phiếu tại năm $H$ **giảm** (thiệt hại Price Risk), nhưng toàn bộ các khoản coupon thu được từ năm $1$ đến $H$ được tái đầu tư ở lãi suất cao hơn nên tổng giá trị tích lũy coupon **tăng** (lợi ích Reinvestment Risk). Tại đúng mốc $H = D_A$, phần lãi tái đầu tư bù đắp vừa khít phần lỗ giá bán!
     - Nếu lãi suất **giảm**: Lãi tái đầu tư coupon giảm, nhưng giá bán trái phiếu tại năm $H$ tăng vọt bù đắp vừa khít!
2. **Ba Điều kiện Toán học của Redington Immunization:**
   - **Điều kiện 1 (Khớp Hiện giá):** $PV_A(Y_0) = PV_L(Y_0)$ (Tài trợ đủ 100% ở mặt bằng lãi suất ban đầu).
   - **Điều kiện 2 (Khớp Độ dốc bậc nhất):** $D_A = D_L$ (tương đương $D_{M,A} = D_{M,L}$ trên đường cong phẳng).
   - **Điều kiện 3 (Bất đẳng thức Độ lồi bậc hai):** $C_A > C_L$ (*Asset Convexity strictly exceeds Liability Convexity* — nghĩa là tài sản phân tán dòng tiền rộng hơn quanh $H$, ví dụ chiến lược **Barbell** kết hợp trái phiếu ngắn hạn $T_1 < H$ và dài hạn $T_2 > H$ để bảo vệ khoản nợ đơn lẻ tại $H$).
   - *Hệ quả kỳ diệu của $C_A > C_L$:* Xét hàm thặng dư ròng $S(Y) = PV_A(Y) - PV_L(Y)$. Tại $Y_0$, ta có $S(Y_0) = 0$, $S'(Y_0) = 0$, và $S''(Y_0) = P_0(C_A - C_L) > 0$. Khai triển Taylor cho thấy $S(Y_0 + \Delta Y) \approx \frac{1}{2}P_0(C_A - C_L)(\Delta Y)^2 > 0$! Nghĩa là dưới dịch chuyển song song về **bất kỳ phía nào** (dù lãi suất tăng hay giảm), giá trị tài sản luôn nằm cao hơn giá trị nghĩa vụ nợ, tạo ra **Thặng dư Miễn nhiễm Dương (Post-Shift Surplus > 0)**!
3. **Hai Lý do Bắt buộc Phải Tái cân bằng (Why Rebalancing is Mandatory — L03 Q4 & Practice Q34):**
   - **Lý do 1 (Time Decay lệch pha ngay cả khi lãi suất đứng yên $\Delta Y = 0$):** Sau 1 năm trôi qua, thời gian còn lại (và Duration) của nghĩa vụ nợ đơn lẻ giảm đúng **1.00 năm**, nhưng Macaulay Duration của danh mục trái phiếu coupon (hoặc tổ hợp zero-coupon nhiều kỳ hạn) nói chung giảm với tốc độ **khác 1.00 năm**! Sự lệch pha này phá vỡ điều kiện $D_A = D_L$ nếu không điều chỉnh lại tỷ trọng $w_i$.
   - **Lý do 2 (Yield Shifts làm biến dạng Duration & Market Weights):** Khi lãi suất thị trường thay đổi, cả Duration từng trái phiếu lẫn tỷ trọng giá trị thị trường $w_i = V_i / V_A$ của chúng đều dịch chuyển bất đối xứng.
4. **Rủi ro Xoắn Đường cong Lợi suất (Non-Parallel Shift Vulnerability — Practice Q35):**
   - Khi đường cong lợi suất dốc lên (*steepening*) hoặc phẳng đi (*flattening*): ví dụ danh mục Barbell giữ Zero-coupon 2 năm và 10 năm để miễn nhiễm khoản nợ 5 năm. Nếu lãi suất 2 năm tăng $+50\text{ bps}$, lãi suất 5 năm đứng yên $0\text{ bps}$ (nên $PV_L$ không đổi!), và lãi suất 10 năm chỉ giảm $-10\text{ bps}$ (hoặc tăng $+60\text{ bps}$), biến động trái chiều tại hai đầu barbell không còn tuân theo một $\Delta Y$ chung duy nhất $\implies$ danh mục hoàn toàn có thể rơi vào **trạng thái thiếu hụt tài sản ($PV_A < PV_L$, Underfunded)**!

---

## 3.2. Hệ thống Công thức Đầy đủ & Quy ước Ghép lãi / Đơn vị

*(Quy ước ký hiệu chuẩn của khóa học: $Y$ là YTM danh nghĩa năm APR, $f$ là số lần trả lãi/ghép lãi mỗi năm [$f=1$ cho annual, $f=2$ cho semiannual], tổng số kỳ $N = fT$, dòng tiền mỗi kỳ $CF_k$ tại $t_k = k/f$ năm)*

1. **Macaulay Duration (đơn vị: Năm — Years):**
   $$D = \sum_{k=1}^{fT} \left(\frac{k}{f}\right) w_k, \qquad \text{với } w_k = \frac{PV(CF_k)}{P_0} = \frac{CF_k / (1 + Y/f)^k}{P_0}, \quad \sum_{k=1}^{fT} w_k = 1$$
   - *Công thức đóng (Closed-form) bấm máy cực nhanh khi $N$ lớn (với $y_p = Y/f$ là YTM mỗi kỳ và $c_p = \text{Coupon Rate}/f$ là lãi suất coupon mỗi kỳ):*
     $$D_{\text{periods}} = \frac{1 + y_p}{y_p} - \frac{(1 + y_p) + N(c_p - y_p)}{c_p\left[(1 + y_p)^N - 1\right] + y_p}, \qquad D_{\text{years}} = \frac{D_{\text{periods}}}{f}$$
   - *Đặc biệt cho Trái phiếu Ngang giá (Par Bond, $c_p = y_p$):* Công thức rút gọn siêu tốc thành:
     $$D_{\text{periods}}^{\text{par}} = \frac{1 + y_p}{y_p}\left[1 - \frac{1}{(1 + y_p)^N}\right]$$

2. **Modified Duration, Money Duration & DV01:**
   $$D_M = \frac{D}{1 + Y/f}, \qquad DD = P_0 \times D_M, \qquad \text{DV01} = P_0 \times D_M \times 0.0001$$

3. **Analytical Annual Convexity (đơn vị: $\text{Năm}^2$ — $\text{Years}^2$):**
   $$C = \frac{1}{P_0 \cdot f^2 \cdot (1 + Y/f)^2} \sum_{k=1}^{fT} k(k + 1) \, PV(CF_k) = \frac{1}{P_0 (1 + Y/f)^2} \sum_{k=1}^{fT} t_k\left(t_k + \frac{1}{f}\right) PV(CF_k)$$
   - *Với Trái phiếu Annual ($f = 1$, kỳ $t = 1, \dots, T$):*
     $$C_{\text{annual}} = \frac{1}{P_0 (1 + Y)^2} \sum_{t=1}^{T} t(t + 1) \frac{CF_t}{(1 + Y)^t}$$
   - *Với Trái phiếu Zero-Coupon kỳ hạn $T$ năm:*
     - Nếu ghép lãi theo năm ($f = 1$, $n = T$): $C_{\text{zero, annual}} = \frac{T(T + 1)}{(1 + Y)^2}$.
     - Nếu ghép lãi bán niên ($f = 2$, $N = 2T$ kỳ 6 tháng): $C_{\text{zero, semi}} = \frac{2T(2T + 1)}{4(1 + Y/2)^2} = \frac{T(T + 0.5)}{(1 + Y/2)^2}$.
   - *Convexity của Danh mục:* $C_P = \sum_{i=1}^m w_i C_i$ (trọng số giá trị thị trường $w_i$).

4. **Finite-Difference (Effective) Modified Duration & Convexity:**
   Định giá lại trái phiếu tại $Y - h$ được $P_-$ và tại $Y + h$ được $P_+$ (lưu ý sống còn: **$h$ luôn là bước nhảy của YTM danh nghĩa năm dạng số thập phân**, ví dụ $h = 10\text{ bps} = 0.0010$ hay $h = 50\text{ bps} = 0.0050$, kể cả khi trái phiếu trả lãi bán niên!):
   $$D_{M,\text{FD}} \approx \frac{P_- - P_+}{2 \cdot P_0 \cdot h}, \qquad C_{\text{FD}} \approx \frac{P_- + P_+ - 2P_0}{P_0 \cdot h^2}$$

5. **Xấp xỉ Biến động Giá theo Duration & Convexity:**
   $$\frac{\Delta P}{P_0} \approx -D_M (\Delta Y) + \frac{1}{2} C (\Delta Y)^2 \implies \hat{P}_{\text{new}} = P_0 \left[1 - D_M(\Delta Y) + \frac{1}{2} C (\Delta Y)^2\right]$$

6. **Công thức Giải Nhanh Tỷ trọng Miễn nhiễm 2 Trái phiếu ($w_1, w_2$):**
   Để miễn nhiễm nghĩa vụ nợ có hiện giá $PV_L$ và Macaulay Duration $D_L$ bằng Trái phiếu 1 ($D_1$) và Trái phiếu 2 ($D_2$, giả sử $D_1 < D_L < D_2$):
   $$\begin{cases} w_1 + w_2 = 1 \\ w_1 D_1 + w_2 D_2 = D_L \end{cases} \implies \mathbf{w_1 = \frac{D_2 - D_L}{D_2 - D_1}}, \qquad \mathbf{w_2 = 1 - w_1 = \frac{D_L - D_1}{D_2 - D_1}}$$
   - Số tiền đầu tư vào từng trái phiếu: $V_1 = w_1 \cdot PV_L$, $V_2 = w_2 \cdot PV_L$.
   - Số lượng trái phiếu cần mua (Units) = $\frac{V_i}{\text{Market Price per Bond } P_i}$ (KHÔNG chia cho mệnh giá trừ khi trái phiếu đang giao dịch ngang giá!).

---

## 3.3. Quy trình Giải nhanh Bài tập Tính toán Phòng thi

### Dạng 3.1: Bảng Tính Nhanh $P_0, D, D_M, C$ & Đánh giá Xấp xỉ Bậc 1 vs. Bậc 2
**Đề bài chuẩn (L03 Cell 16 / Practice Q29):** Trái phiếu 3 năm, mệnh giá EUR 1,000, coupon 6%/năm trả hàng năm ($f=1$), YTM ban đầu $Y_0 = 5\%$. Tính $P_0, D, D_M, C$. Nếu YTM tăng vọt lên $7\%$ ($\Delta Y = +0.02$), so sánh dự báo Duration-only, dự báo Duration+Convexity và giá thực tế mới!
- **Bước 1 — Lập bảng 5 cột siêu tốc:**
  - $t=1$: $CF_1 = 60 \implies PV_1 = \frac{60}{1.05} = 57.142857 \implies t \cdot PV_1 = 57.142857 \implies t(t+1)PV_1 = 2 \times 57.142857 = 114.285714$.
  - $t=2$: $CF_2 = 60 \implies PV_2 = \frac{60}{1.05^2} = 54.421769 \implies t \cdot PV_2 = 108.843537 \implies t(t+1)PV_2 = 6 \times 54.421769 = 326.530612$.
  - $t=3$: $CF_3 = 1,060 \implies PV_3 = \frac{1,060}{1.05^3} = 915.663751 \implies t \cdot PV_3 = 2,746.991254 \implies t(t+1)PV_3 = 12 \times 915.663751 = 10,987.965015$.
- **Bước 2 — Cộng tổng & suy ra 4 chỉ tiêu:**
  - $P_0 = \sum PV_t = \mathbf{\text{EUR } 1,027.228377 \approx 1,027.23}$.
  - $D = \frac{\sum t \cdot PV_t}{P_0} = \frac{2,912.977648}{1,027.228377} = \mathbf{2.8358\text{ năm}}$.
  - $D_M = \frac{2.835764}{1.05} = \mathbf{2.7007}$.
  - $C = \frac{\sum t(t+1)PV_t}{P_0 (1.05)^2} = \frac{11,428.781341}{1,027.228377 \times 1.1025} = \mathbf{10.0915}$.
- **Bước 3 — Xấp xỉ tại $\Delta Y = +0.02$ so với giá thực $P(7\%)$:**
  - *Duration-only:* $\frac{\Delta P}{P_0} \approx -2.700728 \times 0.02 = -5.4015\% \implies \hat{P}_{\text{Dur}} = 1,027.2284 \times (1 - 0.054015) = \mathbf{\text{EUR } 971.74}$.
  - *Duration + Convexity:* $\frac{\Delta P}{P_0} \approx -0.054015 + \frac{1}{2}(10.0915)(0.02)^2 = -0.054015 + 0.002018 = -5.1996\% \implies \hat{P}_{\text{Dur+Conv}} = \mathbf{\text{EUR } 973.82}$.
  - *Giá thực tại $Y = 7\%$:* $P(7\%) = \frac{60}{1.07} + \frac{60}{1.07^2} + \frac{1,060}{1.07^3} = \mathbf{\text{EUR } 973.76}$.
  - *Kiểm chứng trực giác:* $\hat{P}_{\text{Dur}} (971.74) < P_{\text{Actual}} (973.76)$ (Duration-only đánh giá thấp giá mới tới EUR 2.02, trong khi bổ sung Convexity thu hẹp sai số xuống chỉ còn EUR 0.06!).

---

### Dạng 3.2: Effective Duration & Convexity cho Trái phiếu Semiannual (Practice Q32)
**Đề bài chuẩn:** Trái phiếu 4 năm mệnh giá USD 1,000, coupon 6%/năm **trả bán niên ($f=2$)**, YTM danh nghĩa hiện tại $Y_0 = 6\%$ ($P_0 = 1,000$). Dùng bước nhảy sai phân $h = 50\text{ bps} = 0.0050$ trên YTM năm để tính $D_{M,\text{FD}}$ và $C_{\text{FD}}$.
- **Bước 1 — Định giá tại $Y_- = 5.50\%$ ($y_{6m} = 2.75\%$, $N = 8$, $PMT = 30$) và $Y_+ = 6.50\%$ ($y_{6m} = 3.25\%$):**
  - $P_- = 30 \times \frac{1 - 1.0275^{-8}}{0.0275} + \frac{1,000}{1.0275^8} = \mathbf{1,017.7867}$.
  - $P_+ = 30 \times \frac{1 - 1.0325^{-8}}{0.0325} + \frac{1,000}{1.0325^8} = \mathbf{982.5877}$.
- **Bước 2 — Áp công thức sai phân với $h = 0.0050$ (NHỚ: chia cho $h = 0.0050$ của năm, KHÔNG chia cho $0.0025$!):**
  - $D_{M,\text{FD}} = \frac{1,017.7867 - 982.5877}{2 \times 1,000 \times 0.0050} = \frac{35.1990}{10} = \mathbf{3.5199}$.
  - $C_{\text{FD}} = \frac{1,017.7867 + 982.5877 - 2,000}{1,000 \times (0.0050)^2} = \frac{0.3744}{0.025} = \mathbf{14.98}$.

---

### Dạng 3.3: Thiết kế Danh mục Redington Immunization, Thặng dư Song song & Rủi ro Xoắn Đường cong (L03 Q3 & Practice Q35)
**Đề bài chuẩn (L03 Q3):** Công ty bảo hiểm có nghĩa vụ trả EUR 1,000,000 đúng 6 năm nữa ($H = D_L = 6$). Đường cong lợi suất phẳng ở $Y = 5\%$ (ghép lãi năm). Chỉ được đầu tư vào hai trái phiếu Zero-Coupon kỳ hạn 4 năm ($D_1 = 4$) và 10 năm ($D_2 = 10$).
1. **Tìm số tiền đầu tư vào từng trái phiếu hôm nay:**
   - Hiện giá nghĩa vụ nợ: $PV_L = \frac{1,000,000}{1.05^6} = \mathbf{\text{EUR } 746,215.40}$.
   - Tỷ trọng miễn nhiễm: $w_4 = \frac{10 - 6}{10 - 4} = \frac{4}{6} = \mathbf{\frac{2}{3} (66.67\%)}$ và $w_{10} = 1 - \frac{2}{3} = \mathbf{\frac{1}{3} (33.33\%)}$.
   - Số tiền phân bổ: $V_4 = \frac{2}{3} \times 746,215.40 = \mathbf{\text{EUR } 497,476.93}$ (tương ứng mệnh giá đáo hạn năm 4 là $497,476.93 \times 1.05^4 = \text{EUR } 604,687.50$); $V_{10} = \frac{1}{3} \times 746,215.40 = \mathbf{\text{EUR } 248,738.47}$ (tương ứng mệnh giá đáo hạn năm 10 là $248,738.47 \times 1.05^{10} = \text{EUR } 405,168.79$).
2. **Kiểm chứng Thặng dư Dương khi lãi suất nhảy song song lên $6\%$ ngay lập tức:**
   - Hiện giá nghĩa vụ nợ mới: $PV_L(6\%) = \frac{1,000,000}{1.06^6} = \text{EUR } 704,960.54$.
   - Hiện giá tài sản mới: $PV_A(6\%) = \frac{604,687.50}{1.06^4} + \frac{405,168.79}{1.06^{10}} = 478,968.89 + 226,243.43 = \text{EUR } 705,212.32$.
   - **Thặng dư ròng:** $\text{Surplus} = PV_A(6\%) - PV_L(6\%) = \mathbf{+\text{EUR } 251.78 > 0}$!
   - *Giải thích chuẩn điểm tối đa:* Vì Barbell (4y + 10y) có độ lồi $C_A = \frac{2}{3}\frac{4 \times 5}{1.05^2} + \frac{1}{3}\frac{10 \times 11}{1.05^2} = \frac{130/3}{1.1025} = 39.30 > C_L = \frac{6 \times 7}{1.05^2} = 38.10$, đường giá trị tài sản cong lên cao hơn nghĩa vụ nợ ở cả hai phía dịch chuyển song song!
3. **Minh họa Rủi ro Tái cân bằng sau 1 năm (nếu YTM đứng yên ở 5%):**
   - Sau 1 năm ($t=1$), nghĩa vụ nợ còn $D_L' = 5\text{ năm}$, $PV_L' = 746,215.40 \times 1.05 = 783,526.17$.
   - Hai trái phiếu còn kỳ hạn $D_1' = 3\text{ năm}$ và $D_2' = 9\text{ năm}$. Nếu **không** tái cân bằng, hai khoản đầu tư đều tăng đúng $5\%$ nên tỷ trọng vẫn là $2/3$ và $1/3 \implies D_A' = \frac{2}{3}(3) + \frac{1}{3}(9) = 5.00\text{ năm}$ *(Lưu ý cực hay: Riêng với tổ hợp toàn Zero-Coupon dưới đường cong phẳng đứng yên, $D_i$ của mỗi zero-coupon đều giảm đúng 1 năm nên $D_A'$ vẫn khớp 5 năm cho đến khi trái phiếu ngắn đáo hạn tại năm 4! Nhưng nếu dùng **trái phiếu trả coupon**, $D$ của trái phiếu coupon giảm chậm hơn 1 năm nên sau 1 năm lập tức lệch $D_A' \ne 5$ và bắt buộc phải giải lại $w_1' = \frac{D_2' - 5}{D_2' - D_1'}$!)*.

---

## 3.4. Các Bẫy Lý thuyết & Lỗi Sai Chết Người trong MCQ (Lecture 03)

> [!WARNING]
> **7 BẪY LÝ THUYẾT & TÍNH TOÁN CHÍ MẠNG CỦA LECTURE 03:**
> 1. **Bẫy "Dùng Tỷ trọng Mệnh giá (Face-Value Weights) để tính Duration Danh mục" (Practice Q28):** Sai hoàn toàn! Nếu bạn giữ 1 trái phiếu Zero-Coupon 10 năm mệnh giá 1,000 (giá thị trường chỉ ~558) và 1 trái phiếu Coupon 12% mệnh giá 1,000 (giá thị trường ~1,300), tỷ trọng trong Duration danh mục bắt buộc tính theo **Market Value ($V_i / \sum V_j$)**, không bao giờ chia theo mệnh giá!
> 2. **Bẫy Dấu trong Quy tắc Xấp xỉ Duration-Only:** Học sinh hay nhầm rằng "khi lãi suất tăng thì Duration dự báo cao hơn giá thực, khi lãi suất giảm thì dự báo thấp hơn". SAI! Vì đường thẳng tiếp tuyến nằm **dưới** đường cong lồi ở cả hai bên điểm tiếp xúc, Duration-only **LUÔN LUÔN dự báo giá mới THẤP HƠN giá thực tế ($P_{\text{Dur}} < P_{\text{Actual}}$)** cho cả $\Delta Y > 0$ lẫn $\Delta Y < 0$ (với trái phiếu option-free)!
> 3. **Bẫy Quên đổi `%` sang Số thập phân trong Số hạng Convexity $\frac{1}{2}C(\Delta Y)^2$:** Nếu $\Delta Y = 2\%$, phải thay $\Delta Y = 0.02 \implies (\Delta Y)^2 = 0.0004$. Nếu thay nhầm số $2$ rồi chia $100$ một lần sẽ làm số hạng Convexity phóng đại gấp **100 lần**!
> 4. **Bẫy Nhầm $h$ Bán niên khi tính Finite-Difference Convexity $C_{\text{FD}}$ (Practice Q32):** Dù trái phiếu trả lãi bán niên (nên khi bấm giá $P_-$ và $P_+$ bạn phải dùng lãi suất 6 tháng $Y/2 \mp h/2$), mẫu số của công thức $D_{M,\text{FD}} = \frac{P_- - P_+}{2 P_0 h}$ và $C_{\text{FD}} = \frac{P_- + P_+ - 2P_0}{P_0 h^2}$ để ra thước đo chuẩn hóa theo **năm** bắt buộc phải dùng **$h$ của YTM năm** (ví dụ $50\text{ bps} \implies h = 0.0050$, không phải $0.0025$)!
> 5. **Bẫy "Macaulay Duration của Zero-Coupon Bond thay đổi khi YTM tăng hoặc ghép lãi bán niên":** SAI! Zero-coupon chỉ có duy nhất 1 dòng tiền tại $T$ với trọng số $w_T = 100\%$, nên **Macaulay Duration luôn bằng đúng $T$ năm** ở mọi mức lãi suất; chỉ có **Modified Duration** $D_M = \frac{T}{1 + Y/f}$ mới giảm khi $Y$ tăng hoặc tăng nhẹ khi $f$ tăng!
> 6. **Bẫy "Immunization là chiến lược Mua-và-Nắm-giữ Vĩnh viễn (Set-and-Forget)":** SAI! Chỉ có **Cash-Flow Matching (Dedication)** mới không cần tái cân bằng; còn **Redington Immunization** bắt buộc phải tái cân bằng định kỳ khi thời gian trôi đi và khi lãi suất dịch chuyển!
> 7. **Bẫy "Khớp $PV_A = PV_L$ và $D_A = D_L$ đảm bảo không bao giờ lỗ vốn trong mọi kịch bản lãi suất" (Practice Q35):** SAI! Nếu đường cong lợi suất dịch chuyển **không song song (twist / steepening / flattening)** hoặc nếu bạn chọn danh mục tài sản có độ lồi thấp hơn nghĩa vụ nợ ($C_A < C_L$), giá trị tài sản vẫn có thể tụt xuống dưới nghĩa vụ nợ!

---

<a id="lecture-04"></a>
# LECTURE 04: TỶ SUẤT SINH LỜI, RỦI RO & PHÂN BỔ VỐN
*(RETURNS, RISK, AND CAPITAL ALLOCATION)*

---

## 4.1. Trực giác Kinh tế Cốt lõi & Tổng hợp Lý thuyết Toàn diện

### A. Đo lường Lợi suất: HPR, Phân tích Kịch bản vs. Mẫu Lịch sử, Trung bình Cộng vs. Trung bình Nhân
1. **Holding Period Return (HPR) & Tái phân rã Lợi suất:**
   - HPR đo tổng phần trăm tăng trưởng tài sản trên một kỳ nắm giữ bất kỳ bao gồm cả **lãi vốn (Capital Gain/Loss Yield)** và **lợi suất thu nhập tiền mặt (Dividend / Coupon Income Yield)**:
     $$\text{HPR} = \frac{P_1 - P_0 + D_1}{P_0} = \underbrace{\frac{P_1 - P_0}{P_0}}_{\text{Capital Gain Yield}} + \underbrace{\frac{D_1}{P_0}}_{\text{Dividend Yield}}$$
   - **Phần bù rủi ro (Risk Premium)** là chênh lệch kỳ vọng $\mathbf{E(r) - r_f}$, trong khi **Lợi suất vượt trội thực hiện (Excess Return)** là chênh lệch thực tế quan sát được trong một kỳ cụ thể $\mathbf{R_t = r_t - r_{f,t}}$.
   - Vì lãi suất phi rủi ro $r_f$ của kỳ đầu tư đơn lẻ đã được ấn định chắc chắn ngay tại đầu kỳ ($t=0$), nó là một hằng số đối với kết quả tại $t=1$. Do đó, **phương sai và độ lệch chuẩn của Excess Return bằng chính xác phương sai và độ lệch chuẩn của Total Return**:
     $$\operatorname{Var}(r - r_f) = \operatorname{Var}(r) \implies \sigma(R) = \sigma(r)$$

2. **Phân tích Kịch bản (Scenario Analysis) vs. Dữ liệu Chuỗi Thời gian Lịch sử (Historical Sample):**
   - Trong **Scenario Analysis**, nhà phân tích chỉ định trước không gian đầy đủ các trạng thái kinh tế $s = 1, \dots, S$ cùng xác suất quần thể đã biết $p(s)$ ($\sum p(s) = 1$) $\implies$ phương sai tính trực tiếp $\sigma^2 = \sum p(s)[r(s) - E(r)]^2$.
   - Trong **Historical Data** gồm $n$ kỳ quá khứ quan sát được, ta không biết trung bình thực $\mu$ mà phải dùng chính trung bình mẫu $\bar{r} = \frac{1}{n}\sum r_t$ làm tâm quy chiếu. Việc thay $\mu$ bằng $\bar{r}$ làm giảm tổng bình phương độ lệch và tiêu tốn **1 bậc tự do (*degree of freedom*)**, nên để có ước lượng không chệch (*unbiased estimator*) cho phương sai, bắt buộc phải chia cho **$n - 1$** thay vì $n$!

3. **Arithmetic Average ($\bar{r}_A$) vs. Geometric (Time-Weighted) Average ($\bar{r}_G$) — Volatility Drag:**
   - **Geometric Average ($\bar{r}_G$):** Lãi suất kép cố định mỗi kỳ giúp tài sản đầu kỳ $W_0$ tăng trưởng thành đúng tài sản cuối kỳ $TV_n = W_0 \prod_{t=1}^n (1 + r_t) = W_0 (1 + \bar{r}_G)^n$. Nó còn gọi là **Time-Weighted Average Return** vì gán trọng số ngang nhau cho mỗi kỳ thời gian bất kể quy mô vốn quản lý (AUM) phình to hay thu hẹp do khách hàng nạp/rút vốn — đây là thước đo chuẩn mực để **đánh giá thành tích quá khứ của nhà quản lý quỹ**.
   - **Arithmetic Average ($\bar{r}_A$):** Trung bình cộng đơn giản $\frac{1}{n}\sum r_t$. Nếu phân phối lợi suất độc lập và ổn định qua thời gian, **$\bar{r}_A$ là ước lượng không chệch tốt nhất cho lợi suất kỳ vọng của 1 kỳ đơn lẻ tiếp theo ($E(r_{n+1})$)**!
   - **Định luật Bất đẳng thức & Lực cản Biến động (Volatility Drag):**
     - Luôn luôn có **$\bar{r}_G \le \bar{r}_A$**, và dấu bằng `=` chỉ xảy ra khi và chỉ khi lợi suất mọi kỳ hoàn toàn bằng nhau ($\sigma = 0$).
     - Độ lệch chuẩn $\sigma$ càng lớn, khoảng cách kéo tụt lợi suất kép càng sâu theo xấp xỉ bậc hai kinh điển:
       $$\bar{r}_G \approx \bar{r}_A - \frac{1}{2}\sigma^2$$
     - *Trực giác sắc bén:* Một khoản lỗ $-50\%$ đòi hỏi khoản lãi $+100\%$ ở kỳ sau mới chỉ vừa hòa vốn ($\bar{r}_G = 0\%$), dù trung bình cộng của $(-50\%, +100\%)$ lên tới $+25\%$!

---

### B. Phân phối Chuẩn, Độ Lệch (Skewness), Độ Nhọn Đuôi Dày (Kurtosis) & Rủi ro Phía dưới (Tail Risk)
1. **Khi nào khung Mean–Variance ($E(r), \sigma$) là đủ?**
   - Nếu lợi suất danh mục tuân theo **Phân phối Chuẩn (Normal Distribution)**, toàn bộ hình dáng xác suất được xác định trọn vẹn chỉ bởi hai tham số $\mu$ và $\sigma$ ($\text{Skew} = 0$, $\text{Kurtosis} = 3 \iff \text{Excess Kurtosis} = 0$), đồng thời mọi tổ hợp tuyến tính các biến chuẩn cũng có phân phối chuẩn và mọi thước đo rủi ro đuôi đều chỉ là bội số cố định của $\sigma$.
   - Thực tế thị trường tài chính vi phạm giả định chuẩn ở 2 khía cạnh trọng yếu khiến **$\sigma$ một mình có thể đánh lừa nhà đầu tư** (Practice Q52):
     - **Negative Skewness ($\text{Skew} < 0$):** Đuôi trái kéo dài hơn đuôi phải (nhiều tháng tăng nhẹ nhưng thỉnh thoảng sụp đổ thảm khốc). Khi $\text{Skew} < 0$, độ lệch chuẩn $\sigma$ (vốn gộp chung cả độ lệch dương tốt lẫn độ lệch âm xấu) **đánh giá thấp (understates)** nguy cơ thua lỗ nặng! Ngược lại nhà đầu tư ưa thích $\text{Skew} > 0$.
     - **Fat Tails / Leptokurtosis ($\text{Kurtosis} > 3 \iff \text{Excess Kurtosis} > 0$):** Xác suất xảy ra các biến động cực đoan ở cả hai đuôi xa cao hơn hẳn dự báo của hình chuông Gauss. Hai chiến lược có thể có **cùng chính xác $E(r)$ và $\sigma$**, nhưng một chiến lược rải biến động đều quanh $\pm 1\sigma$, còn chiến lược kia tĩnh lặng $98\%$ thời gian rồi nổ tung $-60\%$ trong $2\%$ thời gian!

2. **Bốn Thước đo Rủi ro Bổ trợ Phía dưới & Đuôi Trái (Downside & Tail Risk Measures):**
   - **Value at Risk ($\text{VaR}_\alpha$):** Ngưỡng lợi suất phân vị mức $\alpha$ (ví dụ $\alpha = 5\%$ hoặc $1\%$) ở đuôi trái — tức trong $(1 - \alpha)$ thời gian lợi suất không tệ hơn ngưỡng này, còn trong $\alpha$ kịch bản tồi tệ nhất lợi suất rơi xuống bằng hoặc thấp hơn $\text{VaR}_\alpha$. *(Với phân phối chuẩn: $\text{VaR}_{5\%} = E(r) - 1.6449\sigma$, $\text{VaR}_{1\%} = E(r) - 2.3263\sigma$)*. **Điểm mù chí mạng của VaR:** Không hề cho biết mức lỗ trung bình **bên trong** vùng đuôi vượt quá ngưỡng VaR nặng tới đâu!
   - **Expected Shortfall ($\text{ES}_\alpha$ / Conditional Tail Expectation / CVaR):** Giá trị kỳ vọng của lợi suất (hoặc khoản lỗ) **với điều kiện kịch bản đã rơi vào vùng đuôi $\alpha\%$ xấu nhất**: $\text{ES}_\alpha = E[r \mid r \le \text{VaR}_\alpha]$. **ES thực tế hơn và ưu việt hơn VaR** khi có *fat tails* vì nó đo trực tiếp mức độ tàn phá trung bình khi thảm họa thực sự xảy ra!
   - **Lower Partial Standard Deviation (LPSD) & Sortino Ratio:** Chỉ tính căn bậc hai trung bình bình phương các độ lệch âm rơi xuống dưới lãi suất phi rủi ro $r_f$ ($r_t - r_f < 0$). $\text{Sortino Ratio} = \frac{E(r) - r_f}{\text{LPSD}}$ thay thế Sharpe Ratio khi phân phối bất đối xứng mạnh.

---

### C. Mức ngại Rủi ro (Risk Aversion), Thống trị Mean–Variance & Hàm Hữu dụng Bậc hai
1. **Speculation vs. Gambling & Ba Thái độ Đối với Rủi ro:**
   - **Speculation (Đầu cơ hợp lý):** Chấp nhận rủi ro đầu tư đáng kể vì kỳ vọng nhận được **phần bù rủi ro dương tương xứng ($E(r) - r_f > 0$)**. **Gambling (Đánh bạc):** Chấp nhận rủi ro cho một trò chơi công bằng hoặc bất lợi ($E(r) - r_f \le 0$) chỉ vì sở thích mạo hiểm tự thân.
   - **Hàm Hữu dụng chuẩn của khóa học (BKM Quadratic / Mean-Variance Utility):**
     *(Suy ra từ khai triển Taylor bậc hai của hàm hữu dụng tài sản $u(W)$ quanh kỳ vọng: $E[u(W)] \approx u(\mu_W) + \frac{1}{2}u''(\mu_W)\sigma_W^2$, với hệ số ngại rủi ro tương đối $A = -\frac{W \cdot u''(W)}{u'(W)}$)*:
     $$U = E(r) - \frac{1}{2} A \sigma^2$$

| Nhóm Nhà đầu tư | Giá trị $A$ | Thái độ với Fair Game ($E(r) = r_f, \sigma > 0$) | Hình dáng Đường Bàng quan trên hệ trục $(\sigma, E(r))$ |
|---|---|---|---|
| **Ngại rủi ro (Risk-Averse)** | **$A > 0$** | **Từ chối thẳng thừng** ($U = r_f - \frac{1}{2}A\sigma^2 < r_f$). Đòi hỏi phần bù rủi ro dương để bù đắp phương sai. $A$ càng lớn càng phạt nặng rủi ro! | Dốc lên và cong lồi hướng xuống ($E(r) = U_0 + \frac{1}{2}A\sigma^2$). $A$ càng cao đường càng **dốc đứng**. |
| **Trung lập rủi ro (Risk-Neutral)** | **$A = 0$** | **Bàng quan (Indifferent)** ($U = E(r) = r_f$). Chỉ quan tâm duy nhất tới $E(r)$ cao nhất, bỏ qua hoàn toàn $\sigma$. | Các **đường thẳng nằm ngang** song song trục hoành ($E(r) = U_0$). |
| **Ưa thích rủi ro (Risk-Seeking / Loving)** | **$A < 0$** | **Chấp nhận hào hứng** ($U > r_f$ vì $-\frac{1}{2}A\sigma^2 > 0$). Biến động càng lớn càng làm tăng hữu dụng! | Các **đường cong dốc xuống** khi $\sigma$ tăng. |

2. **Certainty Equivalent Rate ($\text{CEQ}$) & Tiêu chuẩn Thống trị Mean–Variance (Dominance Criterion):**
   - **$\text{CEQ}$** là mức lợi suất phi rủi ro giả định mang lại đúng bằng mức hữu dụng $U$ của danh mục rủi ro $\implies \mathbf{\text{CEQ} = U = E(r) - \frac{1}{2}A\sigma^2}$. Một danh mục rủi ro chỉ hấp dẫn hơn T-bill khi và chỉ khi $\text{CEQ} > r_f$.
   - **Quy tắc Thống trị Mean–Variance:** Tài sản X thống trị Y đối với **mọi** nhà đầu tư ngại rủi ro ($A > 0$) nếu $E(r_X) \ge E(r_Y)$ **VÀ** $\sigma_X \le \sigma_Y$ (có ít nhất 1 dấu bất đẳng thức ngặt) — tức X nằm ở góc phần tư **Tây–Bắc (North-West: trái–trên)** so với Y.
   - *Giới hạn quan trọng:* Nếu X có $E(r_X) > E(r_Y)$ nhưng đồng thời $\sigma_X > \sigma_Y$, **không bên nào thống trị bên nào theo Mean–Variance**! Để chọn giữa X và Y bắt buộc phải biết hệ số $A$: tính ngưỡng hoán đổi $A^* = \frac{2[E(r_X) - E(r_Y)]}{\sigma_X^2 - \sigma_Y^2}$ — nhà đầu tư có $A < A^*$ chọn danh mục mạo hiểm hơn X, người có $A > A^*$ chọn danh mục an toàn hơn Y!

---

### D. Đường Phân bổ Vốn (CAL), Tỷ số Sharpe, Phân bổ Tối ưu $y^*$ & Kinked CAL ($r_B > r_L$)
1. **Capital Allocation Line (CAL) & Sharpe Ratio khi $r_B = r_L = r_f$:**
   - Gọi $y$ là tỷ trọng vốn đầu tư vào danh mục rủi ro $P$ và $(1 - y)$ là tỷ trọng đầu tư vào tài sản phi rủi ro $F$:
     - Nếu $0 < y < 1$: Nhà đầu tư **cho vay (lending)** một phần vốn ở lãi suất $r_f$.
     - Nếu $y = 1$: Đầu tư trọn 100% vốn tự có vào $P$.
     - Nếu $y > 1$: Nhà đầu tư **đi vay đòn bẩy (leveraged / borrowing on margin)** lượng $(y - 1)$ ở lãi suất $r_f$ để mua thêm $P$.
   - Lợi suất kỳ vọng và độ lệch chuẩn của danh mục hoàn chỉnh $C$ (với $y \ge 0$):
     $$E(r_C) = (1 - y)r_f + y E(r_P) = r_f + y\left[E(r_P) - r_f\right], \qquad \sigma_C = y \sigma_P$$
   - Khử tham số $y = \frac{\sigma_C}{\sigma_P}$ ta thu được phương trình đường thẳng CAL đi qua $(0, r_f)$ và $(\sigma_P, E(r_P))$:
     $$E(r_C) = r_f + \underbrace{\left[\frac{E(r_P) - r_f}{\sigma_P}\right]}_{S_P\text{ (Sharpe Ratio)}} \sigma_C$$
   - **Độ dốc của CAL chính là Tỷ số Sharpe ($S_P$ — Reward-to-Volatility Ratio)**: phần bù rủi ro kiếm được trên mỗi 1 đơn vị tổng độ lệch chuẩn. Dọc theo toàn bộ tia thẳng CAL ($y > 0$), mọi danh mục kết hợp $C$ đều có **cùng chính xác Sharpe Ratio bằng $S_P$**!

2. **Tối ưu hóa Tỷ trọng Vốn Rủi ro $y^*$:**
   - Giải bài toán $\max_y U(y) = r_f + y[E(r_P) - r_f] - \frac{1}{2}A y^2 \sigma_P^2$:
     - Đạo hàm bậc nhất theo $y$ bằng 0: $[E(r_P) - r_f] - A y \sigma_P^2 = 0 \implies \mathbf{y^* = \frac{E(r_P) - r_f}{A \sigma_P^2}}$.
     - Đạo hàm bậc hai $-A\sigma_P^2 < 0$ (khi $A > 0$) đảm bảo cực đại toàn cục (điểm tiếp xúc hình học giữa đường bàng quan cao nhất và đường thẳng CAL!).
     - Mức hữu dụng tối đa đạt được tại $y^*$:
       $$U(y^*) = r_f + \frac{\left[E(r_P) - r_f\right]^2}{2 A \sigma_P^2} = r_f + \frac{S_P^2}{2A}$$

3. **Đường CAL Gãy Khúc (Kinked CAL) khi Lãi suất Đi vay Cao hơn Lãi suất Cho vay ($r_B > r_L$):**
   - Trong thực tế, nhà đầu tư cá nhân cho vay (mua T-bill) ở lãi suất $r_L$, nhưng khi đi vay ký quỹ ($y > 1$) phải trả lãi suất vay $r_B > r_L$:
     - **Nhánh Cho vay ($0 \le y \le 1$):** Xuất phát từ $(0, r_L)$ tới $(\sigma_P, E(r_P))$ với độ dốc cao $S_L = \frac{E(r_P) - r_L}{\sigma_P}$.
     - **Nhánh Đi vay ($y > 1$):** Xuất phát từ điểm gãy $(\sigma_P, E(r_P))$ đi lên với độ dốc **thoải hơn** $S_B = \frac{E(r_P) - r_B}{\sigma_P} < S_L$, theo phương trình $E(r_C) = r_B + y[E(r_P) - r_B] = E(r_P) + (y - 1)[E(r_P) - r_B]$.
   - **Thuật toán 3 Miền Giải Tối ưu $y^*$ trên Kinked CAL (Bách phát bách trúng!):**
     Tính hai giá trị nghiệm không ràng buộc $y_L = \frac{E(r_P) - r_L}{A\sigma_P^2}$ và $y_B = \frac{E(r_P) - r_B}{A\sigma_P^2}$ (do $r_B > r_L$ nên luôn có $y_B < y_L$):
     - **Miền 1 — Cho vay ($y_L < 1 \iff A > \frac{E(r_P) - r_L}{\sigma_P^2}$):** Nhà đầu tư rất ngại rủi ro, điểm tiếp xúc nằm trên nhánh trái $\implies \mathbf{y^* = y_L < 1}$ (đầu tư $y^*$ vào $P$, gửi $1 - y^*$ ở lãi suất $r_L$).
     - **Miền 2 — Điểm Gãy / Góc ($y_B \le 1 \le y_L \iff \frac{E(r_P) - r_B}{\sigma_P^2} \le A \le \frac{E(r_P) - r_L}{\sigma_P^2}$):** Cho vay ở $r_L$ thì sinh lời quá thấp ($y_L \ge 1$ muốn vượt quá 100%), nhưng đi vay ở $r_B$ lại quá đắt ($y_B \le 1$ không muốn vay) $\implies$ đường bàng quan tựa vào đúng đỉnh nhọn $(\sigma_P, E(r_P)) \implies \mathbf{y^* = 1.00}$ (đầu tư đúng 100% vào $P$, không vay cũng không cho vay)!
     - **Miền 3 — Đi vay ($y_B > 1 \iff A < \frac{E(r_P) - r_B}{\sigma_P^2}$, khi $E(r_P) > r_B$):** Nhà đầu tư chịu rủi ro cao, điểm tiếp xúc nằm trên nhánh phải $\implies \mathbf{y^* = y_B > 1}$ (vay thêm $(y^* - 1)$ ở lãi suất $r_B$ để đầu tư tổng $y^*$ vào $P$). *Chú ý:* Nếu $r_B \ge E(r_P)$ thì $y_B \le 0 < 1$, nên **không một nhà đầu tư ngại rủi ro ($A > 0$) nào đi vay cả**!

---

## 4.2. Hệ thống Công thức Đầy đủ & Quy ước Đơn vị

1. **Thống kê Kịch bản (Population / Scenario) vs. Dữ liệu Mẫu Lịch sử (Sample):**
   - *Kịch bản:* $E(r) = \sum_{s=1}^S p(s)r(s)$, $\sigma^2 = \sum_{s=1}^S p(s)[r(s) - E(r)]^2$, $\operatorname{Cov}(r_1, r_2) = \sum_{s=1}^S p(s)[r_1(s) - E(r_1)][r_2(s) - E(r_2)]$.
   - *Mẫu lịch sử ($n$ kỳ):* $\bar{r}_A = \frac{1}{n}\sum_{t=1}^n r_t$, $\hat{\sigma}^2 = \frac{1}{n - 1}\sum_{t=1}^n (r_t - \bar{r}_A)^2$, $\widehat{\operatorname{Cov}}(r_1, r_2) = \frac{1}{n - 1}\sum_{t=1}^n (r_{1,t} - \bar{r}_1)(r_{2,t} - \bar{r}_2)$.
   - *Geometric Average & Annualization:*
     $$\bar{r}_G = \left[\prod_{t=1}^n (1 + r_t)\right]^{1/n} - 1 \approx \bar{r}_A - \frac{1}{2}\sigma^2$$
     - Quy ước năm hóa chuẩn từ dữ liệu tháng i.i.d. (L06/Extra Session): $\bar{R}_{\text{annual}} = 12 \times \bar{R}_{\text{monthly}}$, $\sigma_{\text{annual}} = \sqrt{12} \times \sigma_{\text{monthly}}$, $\text{Sharpe}_{\text{annual}} = \sqrt{12} \times \text{Sharpe}_{\text{monthly}}$ (nếu ghép lãi kép thì EAR $= (1 + \bar{r}_m)^{12} - 1$).

2. **Danh mục 2 Tài sản Rủi ro ($w_1 + w_2 = 1$):**
   $$E(r_p) = w_1 E(r_1) + w_2 E(r_2)$$
   $$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \operatorname{Cov}(r_1, r_2) = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$$
   - Biên chặn khi $w_1, w_2 \ge 0$ và $-1 \le \rho_{12} \le +1$:
     $$|w_1 \sigma_1 - w_2 \sigma_2| \le \sigma_p \le w_1 \sigma_1 + w_2 \sigma_2$$

3. **Hàm Hữu dụng, Ngưỡng Bàng quan $A^*$ & Phân bổ Vốn $y^*$ (QUY TẮC SỐ THẬP PHÂN SỐNG CÒN!):**
   - **Bắt buộc chuyển toàn bộ $E(r), r_f, \sigma$ về DẠNG SỐ THẬP PHÂN (`decimals`, ví dụ $12\% \to 0.12$, $\sigma = 20\% \to 0.20 \implies \sigma^2 = 0.04$)** trước khi thay vào công thức!
   $$U = E(r) - \frac{1}{2} A \sigma^2, \qquad \text{CEQ} = U, \qquad A_{\text{indiff}}^* = \frac{2\left[E(r_X) - E(r_Y)\right]}{\sigma_X^2 - \sigma_Y^2}$$
   $$y^* = \frac{E(r_P) - r_f}{A \sigma_P^2}, \qquad E(r_C) = \begin{cases} r_L + y^*[E(r_P) - r_L] & \text{nếu } y^* \le 1 \\ r_B + y^*[E(r_P) - r_B] & \text{nếu } y^* > 1 \end{cases}, \qquad \sigma_C = |y^*|\sigma_P$$

---

## 4.3. Quy trình Giải nhanh Bài tập Tính toán Phòng thi

### Dạng 4.1: Giải Nhanh Kinked CAL 3 Miền ($r_B > r_L$) & Tính $E(r_C), \sigma_C, U^*$
**Đề bài mẫu tích hợp (L04 Slides & Practice Q66–Q67):** Quỹ rủi ro $P$ có $E(r_P) = 15\%$, $\sigma_P = 20\%$ ($\sigma_P^2 = 0.04$). Lãi suất cho vay T-bill $r_L = 5\%$, lãi suất đi vay ký quỹ $r_B = 9\%$. Xác định phân bổ vốn tối ưu $y^*$, $E(r_C)$, $\sigma_C$ và $U^*$ cho 3 nhà đầu tư có: (a) $A = 4$; (b) $A = 2$; (c) $A = 1$.
- **Bước 1 — Tìm dải ngưỡng $A$ tại điểm gãy $y = 1$:**
  - Ngưỡng trên của đi vay: $A_{\text{borrow}} = \frac{E(r_P) - r_B}{\sigma_P^2} = \frac{0.15 - 0.09}{0.04} = \mathbf{1.50}$.
  - Ngưỡng dưới của cho vay: $A_{\text{lend}} = \frac{E(r_P) - r_L}{\sigma_P^2} = \frac{0.15 - 0.05}{0.04} = \mathbf{2.50}$.
  - *Kết luận phân miền tức thì:* $A > 2.50 \implies$ Cho vay; $1.50 \le A \le 2.50 \implies$ Đứng tại điểm gãy $y^* = 1$; $A < 1.50 \implies$ Đi vay!
- **Bước 2 — Bấm nghiệm cho từng nhà đầu tư:**
  - **(a) Với $A = 4 > 2.50$ (Miền Cho vay):** $y^* = y_L = \frac{0.10}{4 \times 0.04} = \mathbf{0.625 (62.50\%)}$ vào $P$ và **37.50%** vào T-bill ($r_L = 5\%$).
    - $E(r_C) = 0.05 + 0.625(0.10) = \mathbf{11.25\%}$; $\sigma_C = 0.625 \times 20\% = \mathbf{12.50\%}$; $U^* = 0.1125 - 0.5(4)(0.125)^2 = \mathbf{0.08125 (8.125\%)}$.
  - **(b) Với $A = 2 \in [1.50, 2.50]$ (Miền Điểm Gãy):** Kiểm tra nhanh $y_L = \frac{0.10}{2 \times 0.04} = 1.25 > 1$ nhưng $y_B = \frac{0.06}{2 \times 0.04} = 0.75 < 1 \implies \mathbf{y^* = 1.00 (100\%)}$ vào $P$!
    - $E(r_C) = \mathbf{15.00\%}$; $\sigma_C = \mathbf{20.00\%}$; $U^* = 0.15 - 0.5(2)(0.04) = \mathbf{0.1100 (11.00\%)}$.
  - **(c) Với $A = 1 < 1.50$ (Miền Đi vay):** $y^* = y_B = \frac{0.15 - 0.09}{1 \times 0.04} = \mathbf{1.50 (150\%)}$ vào $P$ và **vay $-50\%$** ở lãi suất $r_B = 9\%$.
    - $E(r_C) = 0.09 + 1.50(0.15 - 0.09) = \mathbf{18.00\%}$ *(kiểm tra lại: $1.50 \times 15\% - 0.50 \times 9\% = 22.5\% - 4.5\% = 18.00\%$ — khớp tuyệt đối!)*; $\sigma_C = 1.50 \times 20\% = \mathbf{30.00\%}$; $U^* = 0.18 - 0.5(1)(0.30)^2 = \mathbf{0.1350 (13.50\%)}$.

---

### Dạng 4.2: Phân phối Rời rạc — Tính VaR 5% & Expected Shortfall (ES) 5%
**Quy tắc bấm nhanh khi đề cho bảng kịch bản rời rạc:**
1. Sắp xếp các kịch bản theo thứ tự lợi suất **từ thấp nhất (tệ nhất) lên cao nhất**, cộng dồn xác suất tích lũy từ trái sang phải.
2. **$\text{VaR}_{5\%}$:** Là mức lợi suất tại kịch bản đầu tiên làm xác suất tích lũy đạt hoặc vượt qua mốc $0.05$ ($5\%$).
3. **$\text{ES}_{5\%}$:** Lấy kỳ vọng có điều kiện trên đúng $5\%$ khối lượng xác suất đuôi trái:
   - Nếu các kịch bản xấu nhất có tổng xác suất vừa khít $0.05$ (ví dụ Kịch bản Crash $p_1 = 0.02, r_1 = -35\%$ và Kịch bản Severe $p_2 = 0.03, r_2 = -20\%$):
     $$\text{ES}_{5\%} = \frac{0.02(-35\%) + 0.03(-20\%)}{0.05} = \frac{-0.70\% - 0.60\%}{0.05} = \mathbf{-26.00\%}$$
   - Nếu một kịch bản vắt ngang qua mốc $0.05$ (ví dụ $p_1 = 0.03$ tại $-30\%$ và $p_2 = 0.05$ tại $-15\%$): lấy trọn $0.03$ của kịch bản 1 cộng với phần thiếu $(0.05 - 0.03) = 0.02$ của kịch bản 2 rồi chia cho $0.05$: $\text{ES}_{5\%} = \frac{0.03(-30\%) + 0.02(-15\%)}{0.05} = \mathbf{-24.00\%}$.

---

### Dạng 4.3: Ràng buộc Trần Đòn bẩy hoặc Trần Duration lên Phân bổ Tối ưu $y^*$ (Practice Q71)
**Đề bài chuẩn:** Quỹ trái phiếu rủi ro $B$ có $E(r_B) = 7\%$, $\sigma_B = 10\%$, Modified Duration $D_{M,B} = 6.0$. T-bill có $r_f = 3\%$ ($D_{M,f} = 0$). Nhà đầu tư có $A = 3$, nhưng quy chế đầu tư quy định Modified Duration của danh mục hoàn chỉnh **không được vượt quá $4.5$**. Tìm $y^*$ thực tế!
- **Bước 1 — Giải nghiệm tối ưu không ràng buộc:** $y_{\text{unc}}^* = \frac{0.07 - 0.03}{3 \times 0.10^2} = \frac{0.04}{0.03} = \mathbf{1.3333}$.
- **Bước 2 — Chuyển ràng buộc Duration thành trần tỷ trọng $y_{\max}$:**
  $$D_{M,C} = y \cdot D_{M,B} + (1 - y) \cdot 0 = 6.0 y \le 4.5 \implies y \le \frac{4.5}{6.0} = \mathbf{0.75}$$
- **Bước 3 — Vì hàm hữu dụng bậc hai là parabol úp lõm nghiêm ngặt đạt đỉnh tại $1.3333$, trên miền khả thi $y \le 0.75$, điểm tốt nhất chính là sát biên phải:** $\mathbf{y_{\text{constrained}}^* = 0.75 (75\%)}$!

---

## 4.4. Các Bẫy Lý thuyết & Lỗi Sai Chết Người trong MCQ (Lecture 04)

> [!WARNING]
> **7 BẪY LÝ THUYẾT & TÍNH TOÁN CHÍ MẠNG CỦA LECTURE 04:**
> 1. **BẪY SỐ 1 TOÀN KHÓA HỌC — Thay số Phần trăm (`%`) thay vì Số thập phân (`decimal`) vào $U$ và $y^*$:** Công thức $U = E(r) - \frac{1}{2}A\sigma^2$ và $y^* = \frac{E(r_P) - r_f}{A\sigma_P^2}$ của BKM được chuẩn hóa cho **số thập phân**! Nếu $E(r) = 12\%$, $r_f = 4\%$, $\sigma = 20\%$, $A = 2$:
>    - **ĐÚNG (Decimals):** $U = 0.12 - 0.5(2)(0.20)^2 = 0.12 - 0.04 = \mathbf{0.08 (8\%)}$; $y^* = \frac{0.08}{2 \times 0.04} = \mathbf{1.00}$.
>    - **SAI CHẾT NGƯỜI (Percentages):** Nếu gõ $12 - 0.5(2)(20)^2 = -388$ hoặc $y^* = \frac{8}{2 \times 400} = 0.01$, bạn sẽ sai lệch gấp **100 lần**! *(Nếu muốn nhẩm theo điểm phần trăm, công thức đổi đơn vị bắt buộc phải có hệ số $0.01$: $U_{\%} = E(r)_{\%} - 0.005 A \sigma_{\%}^2$ — tốt nhất cứ đổi hết về số thập phân cho an toàn tuyệt đối!)*
> 2. **Bẫy Chia cho $n$ thay vì $n - 1$ khi đề bài nói "Historical Annual Returns over the past 5 years" (Practice Q37):** Hễ dữ liệu là **lợi suất lịch sử quan sát được** (không có cột xác suất $p_s$), phương sai và hiệp phương sai mẫu bắt buộc chia cho **$n - 1$**! Ngược lại, hễ đề bài cho **bảng kịch bản tương lai kèm xác suất (ví dụ 4 trạng thái đồng xác suất 25% mỗi trạng thái)** thì chia đúng theo xác suất (không có $n - 1$).
> 3. **Bẫy Dùng nhầm Geometric Average để dự báo kỳ vọng 1 năm tới (hoặc dùng Arithmetic để tính số tiền tích lũy cuối kỳ):** Nhớ khẩu quyết: **Quá khứ ghép lãi nhiều kỳ $\to$ Geometric ($\bar{r}_G$); Dự báo kỳ vọng 1 kỳ tới $\to$ Arithmetic ($\bar{r}_A$)**!
> 4. **Bẫy Quên kiểm tra Kink ($y^* = 1$) khi $r_B > r_L$:** Tuyệt đối không lấy trung bình của $r_B$ và $r_L$, và không bao giờ báo nghiệm $y_L = 1.25$ (vô lý vì tại $y > 1$ không được hưởng lãi suất $r_L$!) hay $y_B = 0.75$ (vô lý vì tại $y < 1$ không phải chịu lãi vay $r_B$!). Hễ $y_B \le 1 \le y_L$, đáp án chắc chắn là **$y^* = 1.00$**!
> 5. **Bẫy Tính sai $E(r_C)$ ở miền Đi vay ($y > 1$) bằng công thức $r_L + y[E(r_P) - r_B]$:** Nhiều sinh viên giữ nguyên $r_L$ ở số hạng đầu khi $y > 1$ — SAI! Khi đi vay $(y - 1)$ ở lãi suất $r_B$, công thức đúng phải là $E(r_C) = y E(r_P) - (y - 1)r_B = \mathbf{r_B + y[E(r_P) - r_B]}$!
> 6. **Bẫy Nhầm Nhà đầu tư Risk-Neutral ($A=0$) "sợ phương sai cao" hoặc "thích phương sai cao":** Người trung lập rủi ro hoàn toàn **mù với $\sigma$** — nếu danh mục X có $E(r_X) = 10.01\%, \sigma_X = 80\%$ và danh mục Y có $E(r_Y) = 10.00\%, \sigma_Y = 0\%$, người $A = 0$ vẫn chọn X!
> 7. **Bẫy Tưởng Sharpe Ratio không đổi khi đi vay ở $r_B > r_L$:** Khi $r_B = r_L = r_f$, đòn bẩy giữ nguyên Sharpe Ratio. Nhưng khi $r_B > r_L$, việc đi vay ($y > 1$) đẩy bạn sang nhánh CAL thoải hơn, khiến Sharpe Ratio tổng thể của danh mục hoàn chỉnh tính trên $r_L$ ($\frac{E(r_C) - r_L}{\sigma_C}$) **bị sụt giảm nghiêm trọng** so với đứng tại $P$!


---

<a id="lecture-05"></a>
# LECTURE 05: ĐA DẠNG HÓA HIỆU QUẢ MARKOWITZ & TỐI ƯU HÓA DANH MỤC
*(MARKOWITZ PORTFOLIO SELECTION & DIVERSIFICATION)*

---

## 5.1. Trực giác Kinh tế Cốt lõi & Tổng hợp Lý thuyết Toàn diện

### A. Giải phẫu Đa dạng hóa: Rủi ro Đặc thù vs. Rủi ro Hệ thống
1. **Hai Nguồn Rủi ro Cốt lõi trên Thị trường Chứng khoán:**
   - **Rủi ro Đặc thù / Rủi ro Doanh nghiệp (Firm-Specific / Idiosyncratic / Unique / Nonsystematic / Diversifiable Risk):** Bắt nguồn từ các sự kiện vi mô riêng lẻ của từng công ty (thử nghiệm thuốc FDA thất bại, cháy nhà máy, CEO từ chức, kiện tụng bản quyền). Khi ghép nhiều mã vào danh mục, tin xấu bất ngờ của công ty A được bù trừ bởi tin tốt bất ngờ của công ty B $\implies$ **có thể triệt tiêu hoàn toàn thông qua đa dạng hóa**.
   - **Rủi ro Hệ thống / Rủi ro Thị trường (Systematic / Market-Wide / Macroeconomic / Nondiversifiable Risk):** Bắt nguồn từ các cú sốc vĩ mô tác động đồng loạt lên hầu hết các doanh nghiệp (suy thoái GDP, cú sốc lãi suất của ngân hàng trung ương, lạm phát phi mã, khủng hoảng địa chính trị). Vì các cổ phiếu có xu hướng biến động cùng chiều trước cú sốc chung ($\overline{\operatorname{Cov}} > 0$), phần rủi ro này **KHÔNG THỂ xóa bỏ bằng đa dạng hóa**, dù bạn nắm giữ 500 hay 5,000 cổ phiếu!

2. **Định lý Giới hạn Phương sai của Danh mục Chia đều $N$ Tài sản ($w_i = 1/N$):**
   - Trong ma trận hiệp phương sai kích thước $N \times N$, có đúng **$N$ phần tử phương sai** nằm trên đường chéo chính (mỗi phần tử nhân với $1/N^2$) và **$N(N - 1)$ phần tử hiệp phương sai** nằm ngoài đường chéo chính (mỗi phần tử cũng nhân với $1/N^2$). Gọi $\bar{\sigma}^2$ là phương sai trung bình và $\overline{\operatorname{Cov}}$ là hiệp phương sai trung bình giữa các cặp cổ phiếu:
     $$\sigma_p^2 = \frac{1}{N} \bar{\sigma}^2 + \frac{N - 1}{N} \overline{\operatorname{Cov}} = \overline{\operatorname{Cov}} + \frac{\bar{\sigma}^2 - \overline{\operatorname{Cov}}}{N}$$
   - **Hai kịch bản giới hạn khi $N \to \infty$:**
     - *Kịch bản Nguyên lý Bảo hiểm (Uncorrelated risks, $\overline{\operatorname{Cov}} = 0$):* $\lim_{N \to \infty} \sigma_p^2 = \lim_{N \to \infty} \frac{\bar{\sigma}^2}{N} = \mathbf{0}$. Rủi ro biến mất 100%!
     - *Kịch bản Thị trường Vốn Thực tế (Correlated assets, $\overline{\operatorname{Cov}} = \bar{\rho}\bar{\sigma}^2 > 0$):* Khi $N \to \infty$, thành phần đặc thù $\frac{\bar{\sigma}^2 - \overline{\operatorname{Cov}}}{N} \to 0$, nhưng tổng phương sai danh mục hội tụ về **sàn rủi ro hệ thống không thể xuyên thủng**:
       $$\lim_{N \to \infty} \sigma_p^2 = \overline{\operatorname{Cov}} \implies \lim_{N \to \infty} \sigma_p = \sqrt{\overline{\operatorname{Cov}}}$$
   - **Hệ quả vàng:** Khi số lượng tài sản $N$ đã lớn, đóng góp của một chứng khoán vào rủi ro danh mục phụ thuộc gần như hoàn toàn vào **hiệp phương sai của nó với các tài sản khác**, chứ không còn phụ thuộc vào phương sai riêng lẻ của chính nó!

---

### B. Hình học Cơ hội Đầu tư 2 Tài sản theo $\rho_{AB}$ & Global Minimum-Variance Portfolio (GMVP)
Xét hai tài sản rủi ro $A$ và $B$ (giả sử $E(r_A) < E(r_B)$ và $\sigma_A < \sigma_B$) với $w_A + w_B = 1$:

| Giá trị $\rho_{AB}$ | Hình dáng Đường Cơ hội trên mặt phẳng $(\sigma, E(r))$ | Đặc tính Đa dạng hóa & GMVP |
|---|---|---|
| **$\rho_{AB} = +1$** | **Đoạn thẳng nối trực tiếp A và B** ($\sigma_p = w_A\sigma_A + w_B\sigma_B$ khi $w_A, w_B \ge 0$). | **Không có bất kỳ lợi ích giảm rủi ro nào khi chỉ mua long ($w \in [0, 1]$)**: độ lệch chuẩn danh mục chỉ là trung bình gia quyền tuyến tính. *(Nếu cho phép bán khống không giới hạn tài sản rủi ro cao B, có thể đẩy $\sigma_p = 0$ tại $w_A = \frac{\sigma_B}{\sigma_B - \sigma_A} > 1, w_B < 0$)*. |
| **$-1 < \rho_{AB} < +1$** | **Đường cong Hyperbol uốn cong sang BÊN TRÁI** về phía trục tung. $\rho_{AB}$ càng giảm, độ cong sang trái càng sâu. | Có lợi ích đa dạng hóa thực sự ($\sigma_p < w_A\sigma_A + w_B\sigma_B$). Đỉnh nhô xa nhất về bên trái là **GMVP** (có thể có $\sigma_{\text{GMVP}} < \min(\sigma_A, \sigma_B)$ khi $\rho_{AB} < \frac{\sigma_A}{\sigma_B}$!). |
| **$\rho_{AB} = -1$** | **Hai đoạn thẳng gãy góc chạm vào trục tung tại $\sigma_p = 0$!** | **Phòng hộ hoàn hảo (Perfect Hedge):** Không cần bán khống, tổ hợp dương $w_A^{\text{ZV}} = \frac{\sigma_B}{\sigma_A + \sigma_B} > 0$ và $w_B^{\text{ZV}} = \frac{\sigma_A}{\sigma_A + \sigma_B} > 0$ triệt tiêu hoàn toàn rủi ro ($\sigma_p = 0$)! Theo điều kiện không kinh doanh chênh lệch giá (*No-Arbitrage*), lợi suất của danh mục $\sigma_p = 0$ này phải bằng đúng $r_f$. |

- **Tính chất Độc lập Kỳ vọng của GMVP (Bẫy MCQ tinh tế):** Tỷ trọng của **Global Minimum-Variance Portfolio (GMVP)** $w_A^{\text{GMVP}} = \frac{\sigma_B^2 - \operatorname{Cov}(r_A, r_B)}{\sigma_A^2 + \sigma_B^2 - 2\operatorname{Cov}(r_A, r_B)}$ được giải thuần túy từ cực tiểu hóa phương sai $\min \sigma_p^2$, nên nó **hoàn toàn KHÔNG phụ thuộc vào $E(r_A), E(r_B)$ hay $r_f$**!

---

### C. Đường Biên Hiệu quả Markowitz (Efficient Frontier), Danh mục Tiếp điểm ($P^*$) & Ràng buộc Cấm Bán Khống
1. **Minimum-Variance Frontier vs. Efficient Frontier of Risky Assets:**
   - **Minimum-Variance Frontier (Đường biên phương sai tối thiểu):** Tập hợp các danh mục có $\sigma_p$ nhỏ nhất ứng với mỗi mức $E(r_p)$ cho trước trên toàn bộ $N$ tài sản rủi ro (hình đầu đạn *bullet*).
   - **Efficient Frontier (Đường biên hiệu quả):** Chỉ bao gồm **nửa nhánh phía trên tính từ điểm GMVP trở lên**. Mọi danh mục nằm trên nửa nhánh dưới của viên đạn (phía dưới GMVP) đều **bị thống trị nghiêm ngặt (inefficient / dominated)** vì ngay thẳng phía trên nó luôn tồn tại một danh mục trên nhánh trên có **cùng chính xác độ lệch chuẩn $\sigma$ nhưng mang lại $E(r)$ cao hơn hẳn** (Practice Q63)!
   - *Lưu ý quan trọng:* Một cổ phiếu đơn lẻ nằm dưới GMVP là không hiệu quả nếu đứng **một mình**, nhưng nó **KHÔNG hề vô dụng** — nó vẫn thường xuất hiện với tỷ trọng dương bên trong các danh mục trên Efficient Frontier nhờ khả năng giảm phương sai tổng thể khi phối hợp với các cổ phiếu khác!

2. **Tangency Portfolio / Optimal Risky Portfolio ($P^*$) & Kiểm tra Biên Ràng buộc (Practice Q69):**
   - Từ điểm lãi suất phi rủi ro $(0, r_f)$ trên trục tung, xoay tia CAL lên phía Tây–Bắc cho đến khi tiếp xúc với Efficient Frontier tại điểm duy nhất **$P^*$**.
   - $P^*$ là danh mục rủi ro có **Sharpe Ratio lớn nhất có thể đạt được ($S_{P^*} = \max_w \frac{E(r_p) - r_f}{\sigma_p}$)**. Đường CAL đi qua $P^*$ thống trị mọi đường CAL khác!
   - **Quy trình bắt buộc khi đề có Ràng buộc Cấm Bán Khống ($w_i \ge 0$) hoặc Trần Tỷ Trọng ($w_i \le w_{\max}$):**
     1. Bấm công thức nghiệm tiếp điểm không ràng buộc $w_A^*$ (xem Mục 5.2).
     2. Nếu $0 \le w_A^* \le 1$ (và thỏa trần $w_{\max}$): Nhận ngay nghiệm nội điểm này!
     3. Nếu nghiệm tự do rơi ra ngoài biên — ví dụ $w_A^* = -0.18 < 0$ (muốn bán khống A để dồn $118\%$ vào B) trong khi đề bài ghi rõ **"No short sales are allowed ($w_i \ge 0$)"** — thì do hàm mục tiêu đơn đỉnh dọc theo đường cong 2 tài sản, nghiệm tối ưu có ràng buộc nằm ngay tại **điểm biên gần nhất ($w_A = 0, w_B = 1$, tức giữ 100% tài sản B có Sharpe cao hơn)**! Tương tự, nếu trần quy định $w_B \le 0.70$ mà nghiệm tự do đòi $w_B^* = 0.85$, nghiệm tối ưu có ràng buộc chốt ngay tại **$w_B = 0.70, w_A = 0.30$**!

---

### D. Định lý Tách biệt Hai Quỹ (Two-Fund Separation Property) & Khi nào Định lý Bị Phá vỡ!
1. **Nội dung Định lý Separation Property (James Tobin, 1958):**
   Khi mọi nhà đầu tư đối mặt với cùng tập đầu vào $(E(\mathbf{r}), \boldsymbol{\Sigma})$ và có thể đi vay lẫn cho vay không giới hạn ở cùng một lãi suất phi rủi ro $r_f$, quyết định đầu tư tách làm **2 bước hoàn toàn độc lập**:
   - **Bước 1 — Xác định Danh mục Rủi ro Tối ưu $P^*$ (Bài toán thuần túy kỹ thuật):** Giải cực đại hóa Sharpe Ratio để tìm bộ tỷ trọng nội bộ $(w_1^*, w_2^*, \dots, w_N^*)$ bên trong $P^*$. **Kết quả bước 1 hoàn toàn KHÔNG chứa hệ số ngại rủi ro $A$!** Một cụ già hưu trí cực kỳ thận trọng ($A = 8$) và một quỹ đầu cơ trẻ mạo hiểm ($A = 1.2$) đều nắm giữ **chính xác cùng một tỷ lệ cổ phiếu–trái phiếu bên trong rổ rủi ro $P^*$**!
   - **Bước 2 — Phân bổ Vốn Cá nhân $y^*$ (Bài toán sở thích cá nhân):** Khác biệt về $A$ chỉ thể hiện duy nhất ở việc chia tổng vốn giữa T-bill $(1 - y^*)$ và quỹ chung $P^*$ ($y^* = \frac{E(r_{P^*}) - r_f}{A\sigma_{P^*}^2}$).

2. **Ba Trường hợp Thực tế Phá vỡ Tính Tách biệt Hai Quỹ (Practice Q68 — Bẫy tự luận & MCQ kinh điển!):**
   - **Trường hợp 1 — Chênh lệch lãi suất Đi vay và Cho vay ($r_B > r_L$):** Đường CAL từ $(0, r_L)$ tiếp xúc với Efficient Frontier tại $P_L^*$, còn đường CAL từ $(0, r_B)$ tiếp xúc tại một danh mục mạo hiểm hơn $P_B^*$ nằm phía trên bên phải $P_L^*$:
     - Nhóm khách hàng thận trọng (cho vay) nắm giữ T-bill + $P_L^*$.
     - Nhóm khách hàng mạo hiểm cao (đi vay ở $r_B$) nắm giữ khoản vay + $P_B^*$.
     - Nhóm khách hàng trung gian không vay cũng không cho vay mà **nắm giữ trực tiếp các danh mục rủi ro khác nhau dọc theo cung cong Efficient Frontier nối từ $P_L^*$ đến $P_B^*$** tùy theo hệ số $A$ của họ!
   - **Trường hợp 2 — Cấm Đi vay Đòn bẩy ($y \le 1$, Borrowing Prohibition):** Những người muốn $y^* \le 1$ vẫn giữ T-bill + $P^*$. Nhưng những nhà đầu tư ít ngại rủi ro (có $y_{\text{unc}}^* > 1$) không được phép kéo dài tia CAL qua phải $P^*$, nên để tăng lợi suất kỳ vọng họ buộc phải dịch chuyển danh mục rủi ro của mình **trượt lên phía trên bên phải dọc theo đường cong Efficient Frontier** (tăng tỷ trọng tài sản rủi ro cao, giảm tài sản an toàn bên trong rổ rủi ro $\implies$ phá vỡ rổ chung $P^*$!).
   - **Trường hợp 3 — Kỳ vọng không đồng nhất (*Heterogeneous Expectations*) hoặc Ràng buộc Pháp lý/Thuế suất Riêng biệt:** Mỗi người nhìn thấy một đường biên hiệu quả khác nhau nên chọn $P^*$ khác nhau.

---

### E. Quy tắc Ngưỡng Đa dạng hóa Khi Thêm Tài sản Mới: $S_Y > \rho_{XY} S_X$
*(Trọng tâm L05 Cell 43, L05 Q5 & L04 Q1 — Chìa khóa giải mã mọi câu hỏi "Có nên thêm tài sản Y vào danh mục X không?")*

1. **Thiết lập Bài toán & Chứng minh Ngắn gọn:**
   - Giả sử danh mục rủi ro hiện hữu của bạn là $X$ (có $S_X = \frac{E(r_X) - r_f}{\sigma_X} > 0$). Bạn cân nhắc trích một tỷ trọng dương nhỏ $w_Y > 0$ mua thêm tài sản mới $Y$ (ghép với $(1 - w_Y)$ của $X$).
   - Dựa vào tử số công thức tiếp điểm (hoặc đạo hàm $\left.\frac{d S_p}{d w_Y}\right|_{w_Y = 0} > 0$):
     $$[E(r_Y) - r_f]\sigma_X^2 - [E(r_X) - r_f]\rho_{XY}\sigma_X\sigma_Y > 0$$
     Chia cả hai vế cho đại lượng dương $\sigma_X^2 \sigma_Y > 0$, ta thu được **Bất đẳng thức Ngưỡng Đa dạng hóa Vàng**:
     $$\underbrace{\frac{E(r_Y) - r_f}{\sigma_Y}}_{S_Y} > \rho_{XY} \underbrace{\frac{E(r_X) - r_f}{\sigma_X}}_{S_X} \iff \mathbf{S_Y > \rho_{XY} S_X}$$

2. **Ý nghĩa Kinh tế Sâu sắc qua 4 Trường hợp Hệ số Tương quan $\rho_{XY}$:**
   - **Nếu $\rho_{XY} = +1$:** Điều kiện đòi hỏi $S_Y > S_X$. Vì không có bất kỳ hiệu ứng khử rủi ro nào, $Y$ bắt buộc phải tự mình có Sharpe Ratio cao hơn $X$ mới xứng đáng được mua.
   - **Nếu $0 < \rho_{XY} < 1$:** Ngưỡng hạ xuống chỉ còn $\rho_{XY}S_X < S_X$! **Một tài sản có Sharpe Ratio THẤP HƠN danh mục hiện tại ($S_Y < S_X$) vẫn nâng cao Sharpe Ratio của tổng danh mục** miễn là $S_Y > \rho_{XY}S_X$!
   - **Nếu $\rho_{XY} = 0$:** Ngưỡng bằng **0** ($S_Y > 0 \iff E(r_Y) > r_f$). Mọi tài sản độc lập có phần bù rủi ro dương (dù nhỏ tới $0.01\%$) đều chắc chắn cải thiện Sharpe Ratio khi thêm vào với tỷ trọng nhỏ phù hợp!
   - **Nếu $\rho_{XY} < 0$ (Tài sản Phòng hộ / Bảo hiểm):** Vế phải $\rho_{XY}S_X$ **NHỎ HƠN 0 (ÂM)**! Điều này chứng minh một chân lý cực kỳ phản trực giác: **Nhà đầu tư tối ưu vẫn MUA LONG ($w_Y^* > 0$) một tài sản có phần bù rủi ro ÂM ($E(r_Y) < r_f \iff S_Y < 0$)** nếu độ tương quan âm của nó đủ mạnh sao cho $S_Y > \rho_{XY}S_X$! *(Và nếu được phép bán khống không giới hạn: khi $S_Y < \rho_{XY}S_X$, bạn sẽ **BÁN KHỐNG $Y$ ($w_Y^* < 0$)** để nâng cao Sharpe Ratio; chỉ duy nhất khi $S_Y = \rho_{XY}S_X$ thì $Y$ mới có tỷ trọng tối ưu bằng $0$!)*

---

## 5.2. Hệ thống Công thức Đầy đủ & Quy ước Đơn vị

1. **Danh mục $N$ Tài sản Tổng quát & Danh mục Chia đều:**
   $$E(r_p) = \sum_{i=1}^N w_i E(r_i), \qquad \sigma_p^2 = \sum_{i=1}^N w_i^2 \sigma_i^2 + \sum_{i=1}^N \sum_{j \ne i} w_i w_j \operatorname{Cov}(r_i, r_j)$$
   - *Chia đều $w_i = 1/N$:* $\sigma_p^2 = \frac{1}{N}\bar{\sigma}^2 + \frac{N - 1}{N}\overline{\operatorname{Cov}}$. Để đạt mục tiêu $\sigma_p \le \sigma_{\text{target}}$ (khi $\sigma_{\text{target}}^2 > \overline{\operatorname{Cov}}$), giải bất phương trình tìm số cổ phiếu tối thiểu (Practice Q53):
     $$N \ge \frac{\bar{\sigma}^2 - \overline{\operatorname{Cov}}}{\sigma_{\text{target}}^2 - \overline{\operatorname{Cov}}} \quad \text{(làm tròn LÊN số nguyên gần nhất } \lceil N \rceil \text{!)}$$

2. **Global Minimum-Variance Portfolio (GMVP) cho 2 Tài sản $A$ và $B$:**
   $$w_A^{\text{GMVP}} = \frac{\sigma_B^2 - \operatorname{Cov}(r_A, r_B)}{\sigma_A^2 + \sigma_B^2 - 2\operatorname{Cov}(r_A, r_B)} = \frac{\sigma_B^2 - \rho_{AB}\sigma_A\sigma_B}{\sigma_A^2 + \sigma_B^2 - 2\rho_{AB}\sigma_A\sigma_B}, \qquad w_B^{\text{GMVP}} = 1 - w_A^{\text{GMVP}}$$
   - *Trường hợp đặc biệt $\rho_{AB} = -1$ (Zero-Variance Portfolio):* $w_A^{\text{ZV}} = \frac{\sigma_B}{\sigma_A + \sigma_B}$, $w_B^{\text{ZV}} = \frac{\sigma_A}{\sigma_A + \sigma_B}$, $\sigma_{\text{ZV}} = 0$.

3. **Tangency Portfolio / Optimal Risky Portfolio ($P^*$) cho 2 Tài sản Rủi ro $A$ và $B$:**
   Đặt phần bù rủi ro $m_A = E(r_A) - r_f$, $m_B = E(r_B) - r_f$ và hiệp phương sai $c_{AB} = \operatorname{Cov}(r_A, r_B) = \rho_{AB}\sigma_A\sigma_B$:
   $$w_A^* = \frac{m_A \sigma_B^2 - m_B c_{AB}}{m_A \sigma_B^2 + m_B \sigma_A^2 - (m_A + m_B)c_{AB}}, \qquad w_B^* = 1 - w_A^*$$
   *(Mẹo bấm máy không bao giờ nhầm mẫu số: Tính tử số của A là $N_A = m_A\sigma_B^2 - m_B c_{AB}$, tính tử số đối xứng của B là $N_B = m_B\sigma_A^2 - m_A c_{AB}$, khi đó mẫu số chung chính là **$N_A + N_B$** $\implies w_A^* = \frac{N_A}{N_A + N_B}$ và $w_B^* = \frac{N_B}{N_A + N_B}$! Cực nhanh, tự động kiểm tra tổng bằng 1 và nhìn dấu của $N_A, N_B$ biết ngay có bán khống hay không!)*

4. **Quy trình Khép kín 3 Bước Markowitz + CAL Toàn diện:**
   - **Bước 1:** Tính $w_A^*, w_B^*$ của $P^*$ (kiểm tra ràng buộc cấm bán khống nếu có) $\implies$ suy ra $E(r_{P^*})$ và $\sigma_{P^*}^2$.
   - **Bước 2:** Tính tỷ trọng phân bổ vào rổ rủi ro $y^* = \frac{E(r_{P^*}) - r_f}{A \sigma_{P^*}^2}$ (kiểm tra Kinked CAL nếu $r_B > r_L$).
   - **Bước 3:** Tỷ trọng cuối cùng trong **Danh mục Hoàn chỉnh (Complete Portfolio)** gồm 3 thành phần:
     $$w_{\text{T-bill}}^{\text{complete}} = 1 - y^*, \qquad w_A^{\text{complete}} = y^* \cdot w_A^*, \qquad w_B^{\text{complete}} = y^* \cdot w_B^*$$

---

## 5.3. Quy trình Giải nhanh Bài tập Tính toán Phòng thi

### Dạng 5.1: Giải Siêu Tốc Toàn Trình GMVP, Tangency $P^*$ (Mẹo $N_A, N_B$) & Complete Portfolio
**Đề bài chuẩn (Tích hợp L05 Slides & Practice Q64–Q65):** Quỹ Cổ phiếu $E$ có $E(r_E) = 13\%$, $\sigma_E = 20\%$ ($\sigma_E^2 = 0.04$); Quỹ Trái phiếu $D$ có $E(r_D) = 8\%$, $\sigma_D = 12\%$ ($\sigma_D^2 = 0.0144$); hệ số tương quan $\rho_{ED} = 0.30$; T-bill $r_f = 5\%$. Nhà đầu tư có $A = 4$.
1. **Tính hiệp phương sai:** $c_{ED} = 0.30 \times 0.20 \times 0.12 = \mathbf{0.0072}$ *(lưu ý bạn có thể tính toàn bộ tỷ trọng GMVP và $P^*$ theo đơn vị $(\%)^2$: $\sigma_E^2 = 400, \sigma_D^2 = 144, c_{ED} = 72, m_E = 8, m_D = 3$ vì tỷ lệ tự triệt tiêu bậc đơn vị — bấm máy nhẩm cực kỳ sạch sẽ! Đổi về decimal khi sang bước $y^*$!)*.
2. **Tìm GMVP:**
   $$w_E^{\text{GMVP}} = \frac{144 - 72}{400 + 144 - 2(72)} = \frac{72}{400} = \mathbf{0.1800 (18.00\%)}, \qquad w_D^{\text{GMVP}} = \mathbf{0.8200 (82.00\%)}$$
   - $E(r_{\text{GMVP}}) = 0.18(13\%) + 0.82(8\%) = \mathbf{8.90\%}$.
   - $\sigma_{\text{GMVP}} = \sqrt{0.18^2(400) + 0.82^2(144) + 2(0.18)(0.82)(72)} = \sqrt{12.96 + 96.8256 + 21.2544} = \sqrt{131.04} = \mathbf{11.45\%}$ *(thấp hơn cả trái phiếu $12\%$!)*.
3. **Tìm Danh mục Tiếp điểm $P^*$ bằng mẹo $N_E, N_D$:**
   - $m_E = 13 - 5 = 8$; $m_D = 8 - 5 = 3$.
   - $N_E = m_E \sigma_D^2 - m_D c_{ED} = 8(144) - 3(72) = 1,152 - 216 = \mathbf{936}$.
   - $N_D = m_D \sigma_E^2 - m_E c_{ED} = 3(400) - 8(72) = 1,200 - 576 = \mathbf{624}$.
   - $N_E + N_D = 936 + 624 = 1,560 \implies w_E^* = \frac{936}{1,560} = \mathbf{0.6000 (60.00\%)}, \quad w_D^* = \frac{624}{1,560} = \mathbf{0.4000 (40.00\%)}$!
   - $E(r_{P^*}) = 0.60(13\%) + 0.40(8\%) = \mathbf{11.00\%}$.
   - $\sigma_{P^*}^2 = 0.60^2(400) + 0.40^2(144) + 2(0.60)(0.40)(72) = 144 + 23.04 + 34.56 = \mathbf{201.60 (\%)^2 = 0.020160}$ $\implies \sigma_{P^*} = \mathbf{14.20\%}$.
   - Sharpe Ratio cực đại: $S_{P^*} = \frac{11.00 - 5.00}{14.1986} = \mathbf{0.4226}$ *(vượt trội cả $S_E = 0.4000$ lẫn $S_D = 0.2500$!)*.
4. **Phân bổ Danh mục Hoàn chỉnh cho $A = 4$ (đổi sang decimal: $\sigma_{P^*}^2 = 0.020160$):**
   - $y^* = \frac{0.11 - 0.05}{4 \times 0.020160} = \frac{0.06}{0.08064} = \mathbf{0.7440 (74.40\%)}$.
   - Tỷ trọng 3 tài sản cuối cùng: **T-bill $= 25.60\%$**, **Cổ phiếu $E = 0.7440 \times 60\% = 44.64\%$**, **Trái phiếu $D = 0.7440 \times 40\% = 29.76\%$**.

---

### Dạng 5.2: Kiểm định Nhanh Ngưỡng Đa dạng hóa $S_Y > \rho_{XY}S_X$ (L05 Q5 & Practice Q70)
**Đề bài chuẩn:** Bạn đang giữ danh mục $X$ có $E(r_X) = 13\%$, $\sigma_X = 20\%$, $r_f = 5\%$ ($\implies S_X = \frac{8\%}{20\%} = \mathbf{0.40}$). Phân tích xem có nên thêm vị thế mua dương ($w_Y > 0$) vào hai tài sản ứng viên sau không (giả sử chỉ mua long):
- **Ứng viên 1 (Quỹ Vàng phòng hộ $G$):** $E(r_G) = 4\%$ (thấp hơn cả T-bill $5\%$!), $\sigma_G = 15\%$, tương quan với $X$ là $\rho_{XG} = -0.30$.
  - Tính $S_G = \frac{4\% - 5\%}{15\%} = \mathbf{-0.0667}$.
  - Tính ngưỡng yêu cầu: $\rho_{XG} S_X = (-0.30)(0.40) = \mathbf{-0.1200}$.
  - So sánh: Vì **$-0.0667 > -0.1200$ ($S_G > \rho_{XG}S_X$)** $\implies$ **CÓ MUA!** Dù Vàng có lợi suất kỳ vọng thấp hơn T-bill (Sharpe âm), sức mạnh phòng hộ ngược chiều ($\rho = -0.30$) giúp giảm phương sai danh mục mạnh hơn phần hy sinh lợi suất, đẩy Sharpe Ratio tổng thể vượt lên trên $0.40$!
- **Ứng viên 2 (Cổ phiếu ngành hẹp $Z$):** $E(r_Z) = 9.5\%$, $\sigma_Z = 15\%$ ($\implies S_Z = \mathbf{+0.30} > 0$), nhưng tương quan rất chặt với $X$ là $\rho_{XZ} = 0.85$.
  - Tính ngưỡng yêu cầu: $\rho_{XZ} S_X = 0.85 \times 0.40 = \mathbf{0.3400}$.
  - So sánh: Vì **$0.3000 < 0.3400$ ($S_Z < \rho_{XZ}S_X$)** $\implies$ **KHÔNG MUA LONG!** (Nếu bị cấm bán khống thì $w_Z^* = 0$; nếu được phép bán khống tự do thì thậm chí nên **short $Z$** để tài trợ mua thêm $X$!).

---

## 5.4. Các Bẫy Lý thuyết & Lỗi Sai Chết Người trong MCQ (Lecture 05)

> [!WARNING]
> **6 BẪY LÝ THUYẾT & TÍNH TOÁN CHÍ MẠNG CỦA LECTURE 05:**
> 1. **Bẫy "Tài sản có Sharpe Ratio thấp hơn danh mục hiện tại thì không nên đưa vào danh mục":** SAI CHẾT NGƯỜI! Tiêu chuẩn đúng là **$S_Y > \rho_{XY}S_X$**, không phải $S_Y > S_X$. Chỉ cần tương quan đủ thấp (hoặc âm), tài sản có Sharpe thấp hơn — thậm chí Sharpe âm — vẫn làm tăng độ dốc đường CAL!
> 2. **Bẫy Quên Kiểm tra Ràng buộc Cấm Bán khống ($w_i \ge 0$) trong Công thức Tangency (Practice Q69):** Khi hai tài sản có tương quan rất cao (ví dụ $\rho = 0.85$) mà một bên có Sharpe vượt trội bên kia, công thức $N_A / (N_A + N_B)$ sẽ tự động cho ra một trọng số **âm** (bán khống tài sản kém để đòn bẩy tài sản tốt). Nếu đề có dòng chữ *"short selling is prohibited / long-only constraint"*, bạn **BẮT BUỘC** phải gạt nghiệm âm đó đi và kết luận $w = 0\%$ và $100\%$!
> 3. **Bẫy Làm tròn Xuống khi Tìm Số lượng Cổ phiếu Tối thiểu $N$ để Đa dạng hóa (Practice Q53):** Nếu giải phương trình $\sigma_p^2 \le \sigma_{\text{target}}^2$ ra $N \ge 23.14$ cổ phiếu, đáp án bắt buộc phải làm tròn **LÊN** thành **$N = 24$ cổ phiếu** (vì ở $N = 23$, độ lệch chuẩn vẫn còn vượt quá ngưỡng trần cho phép!).
> 4. **Bẫy Tưởng Tỷ trọng GMVP Thay đổi khi $r_f$ hoặc $E(r_i)$ Thay đổi:** GMVP chỉ phụ thuộc duy nhất vào ma trận phương sai – hiệp phương sai $(\sigma_A, \sigma_B, \rho_{AB})$. Khi ngân hàng trung ương tăng $r_f$, **điểm tiếp điểm $P^*$ dịch chuyển lên trên dọc theo Efficient Frontier**, nhưng **điểm mũi GMVP đứng yên tuyệt đối**!
> 5. **Bẫy Nhầm Tỷ trọng trong Rổ Rủi ro ($w_A^*$) với Tỷ trọng trong Danh mục Hoàn chỉnh ($y^* \cdot w_A^*$):** Đọc thật kỹ câu hỏi cuối cùng của đề tự luận: *"What are the weights of Stock A and Bond B in the optimal risky portfolio?"* ($w_A^*, w_B^*$ cộng lại bằng $100\%$) hay *"What are the proportions invested in T-bills, Stock A, and Bond B in the investor's complete portfolio?"* ($1 - y^*, y^* w_A^*, y^* w_B^*$)!
> 6. **Bẫy Tưởng Separation Property Luôn Đúng Ngay Cả Khi Bị Cấm Đi Vay ($y \le 1$) (Practice Q68):** Khi cấm đi vay ký quỹ, hai nhà đầu tư rất mạo hiểm có $A_1 = 0.8$ và $A_2 = 1.2$ (cả hai đều muốn vượt quá $P^*$) sẽ chọn **hai danh mục rủi ro khác hẳn nhau nằm trên cung cong Efficient Frontier phía phải $P^*$** $\implies$ tính tách biệt hai quỹ bị phá vỡ đối với nhóm nhà đầu tư bị chạm trần vay!

---

<a id="lecture-06"></a>
# LECTURE 06: MÔ HÌNH ĐƠN CHỈ SỐ & MÔ HÌNH ĐỊNH GIÁ TÀI SẢN VỐN
*(SINGLE-INDEX MODEL & CAPITAL ASSET PRICING MODEL — CAPM)*

---

## 6.1. Trực giác Kinh tế Cốt lõi & Tổng hợp Lý thuyết Toàn diện

### A. Mô hình Đơn Chỉ số (Single-Index Model — SIM): Phá giải "Lời nguyền Số chiều" của Markowitz
1. **Bài toán Nút thắt Đầu vào của Markowitz Đầy đủ:**
   - Để chạy tối ưu hóa Markowitz cho $n$ cổ phiếu, bộ phận phân tích phải ước lượng $n$ lợi suất kỳ vọng, $n$ phương sai và $\frac{n(n-1)}{2}$ hiệp phương sai $\implies$ tổng cộng **$\frac{n(n+3)}{2}$ ước lượng**.
   - Với $n = 50 \implies \mathbf{1,325}$ tham số; với $n = 1,000 \implies \mathbf{501,500}$ tham số! Hậu quả kép: (i) Các nhà phân tích chuyên ngành riêng lẻ không có cơ chế chuẩn để ước lượng hiệp phương sai chéo giữa cổ phiếu ngành ngân hàng và ngành bán dẫn; (ii) Ma trận hiệp phương sai ước lượng rời rạc chứa đầy sai số mẫu, thậm chí có thể **vi phạm tính xác định dương (inconsistent / non-positive-definite)** tạo ra các danh mục "phi rủi ro ảo" vô nghĩa.

2. **Cấu trúc Đại số & Giả định Trực giao của Single-Index Model (William Sharpe, 1963):**
   - SIM giả định mọi mối tương quan cùng chiều giữa các cổ phiếu đều xuất phát từ phản ứng của chúng đối với **1 nhân tố vĩ mô chung duy nhất**, được đại diện bằng lợi suất vượt trội của chỉ số thị trường rộng $R_M = r_M - r_f$.
   - Phương trình hồi quy **Security Characteristic Line (SCL)** viết trên **Excess Returns** ($R_i = r_i - r_f$):
     $$R_i = \alpha_i + \beta_i R_M + e_i$$
   - **Ba giả định thống kê cốt lõi:**
     1. Kỳ vọng phần dư bằng 0: $E(e_i) = 0 \implies E(R_i) = \alpha_i + \beta_i E(R_M)$.
     2. Phần dư độc lập với thị trường: $\operatorname{Cov}(e_i, R_M) = 0$.
     3. **Phần dư giữa hai công ty bất kỳ không tương quan nhau:** $\operatorname{Cov}(e_i, e_j) = 0 \quad (\forall i \ne j)$.
   - **Sự cắt giảm tham số ngoạn mục:** Chỉ cần $n$ hệ số $\alpha_i$, $n$ hệ số $\beta_i$, $n$ phương sai đặc thù $\sigma_{e,i}^2$, cộng thêm 2 ước lượng vĩ mô $(E(R_M), \sigma_M^2)$ = tổng cộng chỉ **$3n + 2$ ước lượng**! (Với $n = 50 \implies \mathbf{152}$ thay vì $1,325$; với $n = 1,000 \implies \mathbf{3,002}$ thay vì $501,500$!). Nó còn cho phép phân công lao động chuyên môn hóa hoàn hảo giữa đội kinh tế vĩ mô (dự báo $E(R_M), \sigma_M^2$) và đội phân tích từng doanh nghiệp (ước lượng $\alpha_i, \beta_i, \sigma_{e,i}^2$).
   - **Đánh đổi của SIM (Cost of Simplification):** Vì giả định $\operatorname{Cov}(e_i, e_j) = 0$, SIM bỏ qua các cú sốc chung cấp độ ngành hoặc chuỗi cung ứng ngoài thị trường chung (ví dụ cú sốc giá nhiên liệu máy bay tác động riêng lên toàn ngành hàng không). Nếu thực tế $\operatorname{Cov}(e_i, e_j) = \rho_e \sigma_{e,i}\sigma_{e,j} > 0$ (Practice Q86d), việc áp dụng công thức SIM ngây thơ sẽ **đánh giá thấp (understate)** hiệp phương sai và tổng rủi ro của danh mục tập trung vào cùng một ngành!

3. **Phân rã Rủi ro, Giải mã $R^2$ & Đa dạng hóa dưới SIM:**
   - **Tổng phương sai = Phương sai hệ thống + Phương sai đặc thù:** $\sigma_i^2 = \beta_i^2 \sigma_M^2 + \sigma_{e,i}^2$.
   - **Hệ số xác định $R^2$:** Tỷ phần của tổng phương sai được giải thích bởi biến động thị trường:
     $$R_i^2 = \frac{\beta_i^2 \sigma_M^2}{\sigma_i^2} = 1 - \frac{\sigma_{e,i}^2}{\sigma_i^2} = \rho_{i,M}^2$$
   - **Hiệp phương sai chéo chỉ đi qua kênh Beta:** $\operatorname{Cov}(R_i, R_j) = \operatorname{Cov}(\beta_i R_M + e_i, \beta_j R_M + e_j) = \mathbf{\beta_i \beta_j \sigma_M^2}$.
     - *Hệ quả cực hay (Practice Q78b):* Nếu rủi ro đặc thù $\sigma_{e,i}^2$ của công ty $i$ tăng gấp đôi (do kiện tụng nội bộ) trong khi $\beta_i, \beta_j, \sigma_M^2$ không đổi, thì **$\operatorname{Cov}(R_i, R_j)$ hoàn toàn KHÔNG ĐỔI**, nhưng tổng độ lệch chuẩn $\sigma_i$ tăng lên làm mẫu số của $\rho_{ij} = \frac{\operatorname{Cov}(R_i, R_j)}{\sigma_i \sigma_j}$ lớn hơn $\implies$ **hệ số tương quan $|\rho_{ij}|$ GIẢM XUỐNG**!
   - **Danh mục dưới SIM:** Với tỷ trọng $w_i$, ta có $\alpha_P = \sum w_i \alpha_i$, $\beta_P = \sum w_i \beta_i$, và phương sai đặc thù của danh mục là $\sigma^2(e_P) = \sum_{i=1}^n w_i^2 \sigma^2(e_i)$. Nếu chia đều $w_i = 1/n$, $\sigma^2(e_P) = \frac{1}{n}\bar{\sigma}_e^2 \to 0$ khi $n \to \infty$ $\implies$ danh mục đa dạng hóa tốt có $R_P^2 \to 1$ và $\sigma_P \to |\beta_P|\sigma_M$!

---

### B. Tối ưu hóa Chủ động Treynor–Black: Kết hợp Cổ phiếu Mispriced ($\alpha_A \ne 0$) với Danh mục Thị trường $M$
*(Trọng tâm L06 Q5 & Practice Q88 — Một trong những dạng bài tự luận sắc sảo nhất của học phần!)*

1. **Bản chất Chiến lược Active + Passive:**
   - Giả sử thị trường nhìn chung hiệu quả nhưng nhờ nghiên cứu sâu, bạn tìm được một cổ phiếu (hoặc danh mục chủ động) $A$ bị định giá sai với $\alpha_A \ne 0$, hệ số $\beta_A$, và phương sai đặc thù $\sigma_{e,A}^2 > 0$.
   - Nếu bạn dồn 100% tiền vào $A$, bạn phải gánh toàn bộ gánh nặng rủi ro đặc thù $\sigma_{e,A}^2$ khổng lồ làm kéo tụt Sharpe Ratio. Nếu bạn chỉ giữ 100% Thị trường $M$ ($\alpha_M = 0, \beta_M = 1, \sigma_{e,M} = 0$), bạn bỏ lỡ món hời $\alpha_A$.
   - **Giải pháp tối ưu (Treynor–Black, 1973):** Kết hợp tỷ trọng $w_A$ vào cổ phiếu chủ động $A$ và $(1 - w_A)$ vào Danh mục Thị trường $M$ để **tối đa hóa Sharpe Ratio tổng thể**!

2. **Trực giác Công thức Tỷ trọng & Định lý Bình phương Tỷ số Thông tin:**
   - Mức đặt cược ban đầu tỉ lệ thuận với **Alpha trên mỗi đơn vị phương sai đặc thù** ($\alpha_A / \sigma_{e,A}^2$) so với phần thưởng trên phương sai của thị trường ($E(R_M) / \sigma_M^2$):
     $$w_0 = \frac{\alpha_A / \sigma_{e,A}^2}{E(R_M) / \sigma_M^2}, \qquad w_A^* = \frac{w_0}{1 + (1 - \beta_A)w_0}, \qquad w_M^* = 1 - w_A^*$$
   - Khi nắm giữ ở đúng tỷ trọng $w_A^*$, bình phương Sharpe Ratio của danh mục tối ưu $P$ tuân theo định lý Pythagoras tài chính tuyệt đẹp:
     $$S_P^2 = S_M^2 + \left(\frac{\alpha_A}{\sigma_{e,A}}\right)^2 \implies S_P = \sqrt{S_M^2 + \text{IR}_A^2} > S_M$$
     trong đó $\text{IR}_A = \frac{\alpha_A}{\sigma_{e,A}}$ được gọi là **Information Ratio (hoặc Appraisal Ratio)**.
   - **Giải thích câu hỏi tư duy ăn điểm tuyệt đối (L06 Q5):**
     - *Hỏi:* Nếu cổ phiếu $A$ có $\beta_A = 1.5 > 1$ và $\alpha_A > 0$, danh mục kết hợp $P$ có $\beta_P > 1$ (rủi ro hệ thống cao hơn thị trường) VÀ còn mang thêm rủi ro đặc thù $\sigma^2(e_P) = (w_A^*)^2 \sigma_{e,A}^2 > 0$ (khiến $P$ kém đa dạng hóa hơn $M$). Tại sao $P$ vẫn có Sharpe Ratio cao hơn $M$?
     - *Đáp:* Trong trạng thái cân bằng CAPM thuần túy ($\alpha = 0$), việc gánh thêm $\sigma_e > 0$ luôn làm giảm Sharpe Ratio xuống dưới $S_M$. Nhưng ở đây cổ phiếu $A$ đang **bị định giá thấp ($\alpha_A > 0$)**, đóng góp thêm lợi suất bất thường dương $w_A^* \alpha_A$ vào tử số mà không đòi hỏi thêm rủi ro thị trường tương ứng. Tại tỷ trọng tối ưu $w_A^*$, lợi ích biên từ $\alpha_A$ vượt trội hoàn toàn chi phí biên của rủi ro đặc thù $\sigma^2(e_P)$, đẩy $S_P = \sqrt{S_M^2 + (\alpha_A/\sigma_{e,A})^2} > S_M$!

---

### C. Mô hình Định giá Tài sản Vốn (CAPM): Giả định, Cân bằng, CML vs. SML & Ứng dụng Định giá
1. **Từ Sáu Giả định Lý tưởng tới Phương trình Cân bằng Thị trường:**
   - **6 Giả định chuẩn của CAPM (Sharpe–Lintner–Mossin):**
     1. Thị trường cạnh tranh hoàn hảo gồm nhiều nhà đầu tư nhỏ là *price-takers*.
     2. Mọi nhà đầu tư cùng hoạch định cho một kỳ nắm giữ đồng nhất (*single-period horizon*).
     3. Vũ trụ đầu tư giới hạn trong các tài sản tài chính giao dịch công khai (không có tài sản phi giao dịch như *human capital*) và nhà đầu tư được vay/cho vay không giới hạn ở cùng lãi suất phi rủi ro $r_f$.
     4. Không có thuế thu nhập và không có chi phí giao dịch hay hạn chế bán khống (*frictionless markets*).
     5. Mọi nhà đầu tư đều là người tối ưu hóa Mean–Variance hợp lý (*rational mean-variance optimizers*).
     6. **Kỳ vọng đồng nhất (*Homogeneous Expectations*):** Mọi người phân tích thông tin công khai giống nhau và đi đến cùng một bộ phân phối xác suất $(E(\mathbf{r}), \boldsymbol{\Sigma})$.
   - **Chuỗi suy luận cân bằng hoàn chỉnh:**
     - Nhờ Giả định (3)–(6) và Định lý Tách biệt Hai Quỹ, **mọi nhà đầu tư đều nắm giữ cùng một danh mục tiếp điểm $P^*$**.
     - Để thị trường thanh toán bù trừ hết cung cầu (*market clearing*), tỷ trọng từng chứng khoán trong $P^*$ bắt buộc phải bằng tỷ trọng tổng giá trị vốn hóa của chứng khoán đó trên toàn thị trường $\implies$ **$P^*$ chính là Danh mục Thị trường $M$ (Market Portfolio)**!
     - Cộng gộp cầu vốn toàn nền kinh tế (tổng vay ròng bằng 0 $\implies \bar{y} = 1$), **Phần bù Rủi ro Thị trường** được ấn định bởi mức ngại rủi ro trung bình gia quyền theo của cải $\bar{A}$ và phương sai thị trường $\sigma_M^2$:
       $$E(R_M) = E(r_M) - r_f = \bar{A} \sigma_M^2$$
     - Với bất kỳ tài sản đơn lẻ $i$ nào, đóng góp rủi ro biên của nó vào phương sai danh mục thị trường $M$ đúng bằng $2\operatorname{Cov}(R_i, R_M)$. Cân bằng cung cầu đòi hỏi tỷ số giữa phần bù rủi ro và hiệp phương sai với thị trường của mọi tài sản phải bằng nhau và bằng tỷ số của chính thị trường:
       $$\frac{E(R_i)}{\operatorname{Cov}(R_i, R_M)} = \frac{E(R_M)}{\sigma_M^2} = \bar{A} \implies \mathbf{E(r_i) = r_f + \beta_i\left[E(r_M) - r_f\right]}, \quad \text{với } \beta_i = \frac{\operatorname{Cov}(R_i, R_M)}{\sigma_M^2}$$

2. **Bảng Đối chiếu Sống còn: Capital Market Line (CML) vs. Security Market Line (SML):**

| Tiêu chí Đối chiếu | Capital Market Line (CML) | Security Market Line (SML) |
|---|---|---|
| **Phương trình toán học** | $E(r_P) = r_f + \left[\frac{E(r_M) - r_f}{\sigma_M}\right] \sigma_P$ | $E(r_i) = r_f + \beta_i \left[E(r_M) - r_f\right]$ |
| **Biến số trên Trục hoành (X-axis)** | **Tổng độ lệch chuẩn $\sigma_P$** (*Total Risk* = Systematic + Idiosyncratic). | **Hệ số Beta $\beta_i$** (*Systematic / Market Risk only*). |
| **Tung độ gốc & Độ dốc (Slope)** | Tung độ gốc $= r_f$; Độ dốc $= \mathbf{S_M = \frac{E(r_M) - r_f}{\sigma_M}}$ (Sharpe Ratio của Thị trường). | Tung độ gốc $= r_f$; Độ dốc $= \mathbf{E(r_M) - r_f}$ (Phần bù rủi ro thị trường — tại $\beta_M = 1$, $E(r) = E(r_M)$). |
| **Phạm vi Tài sản Áp dụng (CỰC QUAN TRỌNG!)** | **CHỈ áp dụng cho các Danh mục Hiệu quả hoàn hảo** (tổ hợp của $r_f$ và $M$, nơi $\sigma_{e,P} = 0$). Mọi cổ phiếu đơn lẻ hoặc danh mục kém đa dạng hóa ($\sigma_e > 0$) đều nằm **PHÍA DƯỚI** đường CML! | **Áp dụng cho TẤT CẢ mọi chứng khoán đơn lẻ VÀ mọi danh mục bất kỳ** (dù hiệu quả hay tập trung 1 mã duy nhất) trong trạng thái cân bằng CAPM! |
| **Ý nghĩa Kinh tế** | Mô tả đánh đổi Lợi suất – Tổng rủi ro tốt nhất cho danh mục hoàn chỉnh của nhà đầu tư. | Định giá mức lợi suất yêu cầu công bằng (*fair required return* / *hurdle rate*) cho từng tài sản hoặc dự án đầu tư vốn (*capital budgeting*). |

3. **Jensen's Alpha, Nhận diện Định giá Sai trên SML & Giá Hợp lý $P_0$:**
   - **Jensen's Alpha:** $\alpha_i = E(r_i)_{\text{analyst}} - \left[r_f + \beta_i\left(E(r_M) - r_f\right)\right]$.
     - Trong cân bằng CAPM, mọi tài sản đều nằm đúng trên SML nên **$\alpha_i = 0$**. (Cũng lưu ý: tổng trung bình gia quyền vốn hóa của mọi $\beta_i$ trên toàn thị trường luôn bằng đúng **$\sum w_{M,i}\beta_i = 1.0$**!).
     - **Nếu $\alpha_i > 0$ (Điểm dự báo vẽ nằm PHÍA TRÊN đường SML):** Lợi suất kỳ vọng cao hơn mức bù đắp rủi ro đòi hỏi $\implies$ giá thị trường hiện tại đang quá rẻ $\implies$ chứng khoán **ĐỊNH GIÁ THẤP (Underpriced / Undervalued)**. Giá hợp lý nội tại hôm nay phải cao hơn giá đang giao dịch:
       $$P_{\text{intrinsic},0} = \frac{E(P_1 + D_1)}{1 + r_{\text{CAPM}}} > P_{\text{market},0} = \frac{E(P_1 + D_1)}{1 + E(r_i)_{\text{analyst}}}$$
     - **Nếu $\alpha_i < 0$ (Điểm dự báo vẽ nằm PHÍA DƯỚI đường SML):** Lợi suất kỳ vọng không đủ bù đắp rủi ro $\implies$ giá thị trường hiện tại đang quá đắt $\implies$ chứng khoán **ĐỊNH GIÁ CAO (Overpriced / Overvalued, $P_{\text{intrinsic},0} < P_{\text{market},0}$)**.

---

### D. Ước lượng Beta Lịch sử (OLS SCL), Sai số Chuẩn $\operatorname{S.E.}(\hat{\beta}_i)$ & Adjusted Beta
1. **Hồi quy Chuỗi thời gian Lịch sử (Historical SCL Regression):**
   - Thu thập $T$ kỳ dữ liệu lịch sử (ví dụ $T = 60$ tháng trong 5 năm gần nhất) của cặp lợi suất vượt trội $(R_{i,t}, R_{M,t})$ và chạy hồi quy OLS: $R_{i,t} = \hat{\alpha}_i + \hat{\beta}_i R_{M,t} + \hat{e}_{i,t}$.
   - Hệ số góc ước lượng: $\hat{\beta}_i = \frac{\widehat{\operatorname{Cov}}(R_i, R_M)}{\hat{\sigma}_M^2}$; Hệ số chặn: $\hat{\alpha}_i = \bar{R}_i - \hat{\beta}_i \bar{R}_M$.
   - Ước lượng không chệch của phương sai phần dư đặc thù: $\hat{\sigma}_{e,i}^2 = \frac{\sum_{t=1}^T \hat{e}_{i,t}^2}{T - 2} = \frac{\text{SSE}}{T - 2}$ *(lưu ý chia cho **$T - 2$** vì mất 2 bậc tự do cho 2 tham số hồi quy $\hat{\alpha}_i$ và $\hat{\beta}_i$!)*.
2. **Độ chính xác của Ước lượng Beta — Sai số chuẩn $\operatorname{S.E.}(\hat{\beta}_i)$ (L06 Cell 29):**
   $$\operatorname{S.E.}(\hat{\beta}_i) = \sqrt{\frac{1 - R^2}{T - 2}} \cdot \frac{\hat{\sigma}_i}{\hat{\sigma}_M} = \frac{\hat{\sigma}_{e,i}}{\hat{\sigma}_M \sqrt{T - 1}}$$
   - **Kiểm định giả thuyết thống kê:** Để kiểm định xem cổ phiếu có rủi ro hệ thống khác thị trường không ($H_0: \beta_i = 1$ thay vì $H_0: \beta_i = 0$ mặc định của phần mềm!), ta tính $t\text{-stat} = \frac{\hat{\beta}_i - 1}{\operatorname{S.E.}(\hat{\beta}_i)}$! Còn để kiểm định kỹ năng tạo Alpha có ý nghĩa thống kê không ($H_0: \alpha_i = 0$), ta tính $t_{\alpha} = \frac{\hat{\alpha}_i}{\operatorname{S.E.}(\hat{\alpha}_i)}$ (đòi hỏi $|t| > 1.96$ ở mức ý nghĩa $5\%$ mẫu lớn).
   - **Ba nhân tố giúp thu hẹp $\operatorname{S.E.}(\hat{\beta}_i)$ (tăng độ chính xác ước lượng Beta):** (i) Phương sai đặc thù $\hat{\sigma}_{e,i}^2$ nhỏ ($R^2$ cao — đó là lý do ước lượng Beta cho **danh mục ngành** chuẩn xác hơn gấp bội so với ước lượng cho 1 cổ phiếu riêng lẻ!); (ii) Số quan sát $T$ lớn hơn (nhưng đánh đổi với rủi ro cấu trúc doanh nghiệp đã thay đổi theo thời gian); (iii) Phương sai biến động của thị trường $\hat{\sigma}_M^2$ trong giai đoạn mẫu lớn hơn.
3. **Adjusted Beta (Hiệu chỉnh hướng về trung bình 1.0):**
   - Thực nghiệm cho thấy các ước lượng $\hat{\beta}$ quá cao ($> 1$) hoặc quá thấp ($< 1$) trong một giai đoạn mẫu đều có xu hướng hội tụ dần về trung bình thị trường $1.0$ trong tương lai (*mean reversion toward 1.0*, vừa do doanh nghiệp trưởng thành đa dạng hóa hoạt động, vừa do lọc nhiễu sai số ước lượng cực đoan). Công thức hiệu chỉnh chuẩn Bloomberg:
     $$\beta_{\text{adj}} = \frac{2}{3}\hat{\beta}_{\text{OLS}} + \frac{1}{3}(1.0)$$

---

## 6.2. Hệ thống Công thức Đầy đủ & Quy ước Đơn vị

1. **Hệ phương trình Single-Index Model (SIM):**
   $$R_i = \alpha_i + \beta_i R_M + e_i \implies E(R_i) = \alpha_i + \beta_i E(R_M)$$
   $$\sigma_i^2 = \beta_i^2 \sigma_M^2 + \sigma_{e,i}^2, \qquad R_i^2 = \frac{\beta_i^2 \sigma_M^2}{\sigma_i^2} = \rho_{i,M}^2 \implies \sigma_i = \frac{|\beta_i|\sigma_M}{\sqrt{R_i^2}}, \quad \rho_{i,M} = \operatorname{sign}(\beta_i)\sqrt{R_i^2}$$
   $$\operatorname{Cov}(R_i, R_j) = \beta_i \beta_j \sigma_M^2 \quad \text{(nếu } \operatorname{Cov}(e_i, e_j) \ne 0 \implies \operatorname{Cov}(R_i, R_j) = \beta_i\beta_j\sigma_M^2 + \rho_e\sigma_{e,i}\sigma_{e,j}\text{)}$$
   $$\text{Số tham số: } \text{SIM} = 3n + 2 \quad \text{vs.} \quad \text{Markowitz} = \frac{n(n + 3)}{2} = 2n + \frac{n(n - 1)}{2}$$

2. **Treynor–Black (Kết hợp 1 Cổ phiếu Chủ động $A$ với Danh mục Thị trường $M$):**
   $$w_0 = \frac{\alpha_A / \sigma_{e,A}^2}{E(R_M) / \sigma_M^2}, \qquad w_A^* = \frac{w_0}{1 + (1 - \beta_A)w_0}, \qquad w_M^* = 1 - w_A^*$$
   $$\alpha_P = w_A^* \alpha_A, \quad \beta_P = w_A^* \beta_A + (1 - w_A^*), \quad E(R_P) = \alpha_P + \beta_P E(R_M), \quad \sigma_P^2 = \beta_P^2 \sigma_M^2 + (w_A^*)^2 \sigma_{e,A}^2$$
   $$S_P = \sqrt{S_M^2 + \left(\frac{\alpha_A}{\sigma_{e,A}}\right)^2}$$

3. **Hệ phương trình CAPM & Định giá Cổ phiếu:**
   $$E(R_M) = \bar{A}\sigma_M^2, \qquad E(r_i) = r_f + \beta_i\left[E(r_M) - r_f\right], \qquad \beta_i = \frac{\operatorname{Cov}(r_i, r_M)}{\sigma_M^2} = \rho_{i,M}\frac{\sigma_i}{\sigma_M}$$
   $$\alpha_i = E(r_i)_{\text{forecast}} - \left[r_f + \beta_i\left(E(r_M) - r_f\right)\right], \qquad P_0^{\text{fair}} = \frac{E(P_1 + D_1)}{1 + r_f + \beta_i[E(r_M) - r_f]}$$

---

## 6.3. Quy trình Giải nhanh Bài tập Tính toán Phòng thi

### Dạng 6.1: Khôi phục Đầy đủ Tham số từ $(\beta_i, R^2, \sigma_M)$ & Tính Danh mục SIM
**Đề bài chuẩn (Tích hợp L06 Q1 & Practice Q78):** Thị trường có $E(R_M) = 8\%$, $\sigma_M = 20\%$ ($\sigma_M^2 = 0.04$). Cổ phiếu X có $\alpha_X = 1.5\%$, $\beta_X = 1.2$, $R_X^2 = 0.36$. Cổ phiếu Y có $\alpha_Y = -0.5\%$, $\beta_Y = -0.5$, $R_Y^2 = 0.25$.
1. **Khôi phục $\sigma_i$, $\sigma_{e,i}$ và $\rho_{i,M}$ trong 15 giây:**
   - Cổ phiếu X: $\rho_{X,M} = +\sqrt{0.36} = \mathbf{+0.60}$ (vì $\beta_X > 0$). Tổng độ lệch chuẩn $\sigma_X = \frac{|1.2| \times 20\%}{0.60} = \mathbf{40.00\%}$ ($\sigma_X^2 = 0.16$). Phương sai hệ thống $= 1.2^2(0.04) = 0.0576$; Phương sai đặc thù $\sigma_{e,X}^2 = 0.16 - 0.0576 = \mathbf{0.1024}$ ($\sigma_{e,X} = \mathbf{32.00\%}$).
   - Cổ phiếu Y: $\rho_{Y,M} = -\sqrt{0.25} = \mathbf{-0.50}$ *(chú ý dấu âm vì $\beta_Y = -0.5 < 0$!)*. Tổng độ lệch chuẩn $\sigma_Y = \frac{|-0.5| \times 20\%}{0.50} = \mathbf{20.00\%}$ ($\sigma_Y^2 = 0.04$). Phương sai hệ thống $= (-0.5)^2(0.04) = 0.01$; Phương sai đặc thù $\sigma_{e,Y}^2 = 0.04 - 0.01 = \mathbf{0.03}$ ($\sigma_{e,Y} = \mathbf{17.32\%}$).
2. **Hiệp phương sai & Tương quan giữa X và Y dưới SIM:**
   - $\operatorname{Cov}(R_X, R_Y) = \beta_X \beta_Y \sigma_M^2 = (1.2)(-0.5)(0.04) = \mathbf{-0.0240}$.
   - $\rho_{XY} = \frac{-0.0240}{0.40 \times 0.20} = \mathbf{-0.30}$ *(kiểm tra nhanh bằng công thức tích: $\rho_{X,M} \times \rho_{Y,M} = (+0.60)(-0.50) = -0.30$ — khớp tức thì!)*.
3. **Danh mục chia đều 50% X + 50% Y:**
   - $\alpha_P = 0.5(1.5\%) + 0.5(-0.5\%) = \mathbf{+0.50\%}$; $\beta_P = 0.5(1.2) + 0.5(-0.5) = \mathbf{0.35}$.
   - $E(R_P) = 0.50\% + 0.35(8\%) = \mathbf{3.30\%}$.
   - $\sigma_P^2 = \beta_P^2 \sigma_M^2 + w_X^2 \sigma_{e,X}^2 + w_Y^2 \sigma_{e,Y}^2 = (0.35)^2(0.04) + (0.25)(0.1024) + (0.25)(0.03) = 0.0049 + 0.0256 + 0.0075 = \mathbf{0.0380} \implies \sigma_P = \mathbf{19.49\%}$.

---

### Dạng 6.2: Bài toán Kinh điển Treynor–Black — Cổ phiếu Kappa + Thị trường (L06 Q5)
**Đề bài chuẩn từ Slide L06 Q5:** Danh mục Thị trường $M$ có $E(R_M) = 8\%$, $\sigma_M = 20\%$ ($\implies S_M = \frac{8}{20} = \mathbf{0.4000}$). Cổ phiếu Kappa bị định giá thấp với $\alpha_K = +2\%$, $\beta_K = 1.5$, và độ lệch chuẩn đặc thù $\sigma_{e,K} = 15\%$ ($\sigma_{e,K}^2 = 0.0225$). Tìm tỷ trọng tối ưu kết hợp Kappa và $M$, tính $\beta_P$ và Sharpe Ratio mới $S_P$!
- **Bước 1 — Tính vị thế khởi tạo $w_0$:**
  $$w_0 = \frac{\alpha_K / \sigma_{e,K}^2}{E(R_M) / \sigma_M^2} = \frac{0.02 / 0.0225}{0.08 / 0.0400} = \frac{0.888889}{2.0000} = \mathbf{\frac{4}{9} \approx 0.4444}$$
- **Bước 2 — Hiệu chỉnh Beta tìm $w_K^*$ và $w_M^*$:**
  $$w_K^* = \frac{4/9}{1 + (1 - 1.5)(4/9)} = \frac{4/9}{1 - 2/9} = \frac{4/9}{7/9} = \mathbf{\frac{4}{7} \approx 57.14\%}, \qquad w_M^* = 1 - \frac{4}{7} = \mathbf{\frac{3}{7} \approx 42.86\%}$$
- **Bước 3 — Tính $\beta_P$, $E(R_P)$, $\sigma_P$ và kiểm chứng Định lý $S_P^2 = S_M^2 + \text{IR}_K^2$:**
  - $\beta_P = \frac{4}{7}(1.5) + \frac{3}{7}(1.0) = \frac{6 + 3}{7} = \mathbf{\frac{9}{7} \approx 1.2857}$.
  - $E(R_P) = \frac{4}{7}(2\%) + \frac{9}{7}(8\%) = \frac{8\% + 72\%}{7} = \mathbf{\frac{80}{7}\% \approx 11.4286\%}$.
  - $\sigma_P^2 = \left(\frac{9}{7}\right)^2 (0.04) + \left(\frac{4}{7}\right)^2 (0.0225) = \frac{3.24 + 0.36}{49} = \frac{3.60}{49} = \mathbf{0.073469} \implies \sigma_P = \frac{\sqrt{3.60}}{7} = \mathbf{27.1052\%}$.
  - $S_P = \frac{11.42857\%}{27.1052\%} = \mathbf{0.4216 > S_M (0.4000)}$!
  - *Kiểm tra chéo siêu tốc 3 giây:* $\sqrt{S_M^2 + (\alpha_K / \sigma_{e,K})^2} = \sqrt{0.40^2 + (2 / 15)^2} = \sqrt{0.16 + 0.017778} = \sqrt{0.177778} = \mathbf{0.4216}$ — khớp tới chữ số thập phân thứ 6!

---

### Dạng 6.3: Tìm Giá Hợp lý $P_0$ & Kết luận Mua/Bán theo CAPM (Practice Q83)
**Đề bài chuẩn:** $r_f = 4\%$, $E(r_M) = 10\%$ (chú ý đề ghi **expected market return $= 10\%$**, nên Market Risk Premium $= 10\% - 4\% = \mathbf{6\%}$, KHÔNG phải $10\%$!). Cổ phiếu Omega có $\beta = 1.25$, dự kiến năm sau trả cổ tức $D_1 = \text{USD } 2.20$ và có giá kỳ vọng cuối năm $E(P_1) = \text{USD } 55.00$. Hiện tại Omega đang giao dịch ở giá thị trường $P_{\text{mkt}} = \text{USD } 50.00$.
1. **Lợi suất yêu cầu theo SML (CAPM hurdle rate):** $r_{\text{CAPM}} = 4\% + 1.25(10\% - 4\%) = \mathbf{11.50\%}$.
2. **Lợi suất kỳ vọng dự báo tại giá thị trường 50:** $E(r)_{\text{forecast}} = \frac{55.00 - 50.00 + 2.20}{50.00} = \frac{7.20}{50.00} = \mathbf{14.40\%}$.
3. **Jensen's Alpha & Giá nội tại hợp lý:**
   - $\alpha = 14.40\% - 11.50\% = \mathbf{+2.90\% > 0}$ (nằm **TRÊN** SML).
   - $P_0^{\text{fair}} = \frac{55.00 + 2.20}{1.1150} = \frac{57.20}{1.1150} = \mathbf{\text{USD } 51.30 > \text{USD } 50.00}$.
   - **Kết luận chuẩn:** Cổ phiếu đang bị **Định giá thấp (Underpriced)** khoảng USD 1.30/cổ phiếu $\implies$ khuyến nghị **Mua / Tăng tỷ trọng**.

---

## 6.4. Các Bẫy Lý thuyết & Lỗi Sai Chết Người trong MCQ (Lecture 06)

> [!WARNING]
> **7 BẪY LÝ THUYẾT & TÍNH TOÁN CHÍ MẠNG CỦA LECTURE 06:**
> 1. **Bẫy Kinh Điển Nhất Mọi Đề Thi CAPM — Nhầm $E(r_M)$ với Market Risk Premium $[E(r_M) - r_f]$:** Đọc từng chữ trong đề!
>    - Nếu đề viết *"The expected return on the market portfolio is 11%"* và $r_f = 3\%$: phải tự trừ $11\% - 3\% = \mathbf{8\%}$ trước khi nhân với $\beta$!
>    - Nếu đề viết *"The market risk premium is 8%"* (hoặc *"expected excess market return $E(R_M) = 8\%$"*): con số $8\%$ **đã trừ $r_f$ rồi**, nhân thẳng $\beta \times 8\%$, TUYỆT ĐỐI KHÔNG trừ $r_f$ thêm lần thứ hai!
> 2. **Bẫy Ngược Chiều "Nằm Trên SML là Overpriced, Nằm Dưới SML là Underpriced":** Đây là lỗi sai do nhầm đồ thị Giá với đồ thị Lợi suất! Trục tung của SML là **Expected Return $E(r)$** (tỉ lệ nghịch với giá mua $P_0$). Điểm nằm **TRÊN** SML có lợi suất quá cao $\implies$ giá đang quá rẻ (**Underpriced**); điểm nằm **DƯỚI** SML có lợi suất quá thấp $\implies$ giá đang quá đắt (**Overpriced**)!
> 3. **Bẫy Quên Bình phương Trọng số $w_i^2$ trong Phương sai Đặc thù của Danh mục $\sigma^2(e_P) = \sum w_i^2 \sigma^2(e_i)$:** Với Beta và Alpha ta lấy $\sum w_i \beta_i$, nhưng với phương sai phần dư độc lập bắt buộc phải lấy **$\sum w_i^2 \sigma_{e,i}^2$** (không phải $\sum w_i \sigma_{e,i}^2$)!
> 4. **Bẫy Mất Dấu Âm của $\rho_{i,M}$ khi Khai căn $R^2$:** Khi đề cho $\beta_i = -0.8$ và $R^2 = 0.64$, đừng bấm máy $\sqrt{0.64} = +0.80$! Vì $\beta_i = \rho_{i,M}\frac{\sigma_i}{\sigma_M}$ mà $\sigma_i, \sigma_M > 0$, nên $\rho_{i,M}$ **luôn luôn mang cùng dấu với $\beta_i$** ($\implies \rho_{i,M} = -0.80$)!
> 5. **Bẫy Tưởng Cổ phiếu Đơn lẻ có $\alpha = 0$ Nằm Trên cả SML lẫn CML:** Cổ phiếu đơn lẻ có $\sigma_{e,i} > 0$ trong cân bằng CAPM nằm **chính xác trên đường SML**, nhưng vì tổng rủi ro $\sigma_i > |\beta_i|\sigma_M$, nó có Sharpe Ratio thấp hơn $S_M$ nên luôn nằm **PHÍA DƯỚI đường CML**!
> 6. **Bẫy Tưởng $\sigma_M$ Tăng Gấp Đôi thì Phần bù Rủi ro Thị trường $E(R_M) = \bar{A}\sigma_M^2$ Chỉ Tăng Gấp Đôi (Practice Q82):** Vì $\sigma_M$ mang số mũ **bậc hai ($\sigma_M^2$)**, nếu độ lệch chuẩn thị trường tăng gấp $2$ lần (và $\bar{A}$ không đổi) thì $E(R_M)$ tăng gấp **$2^2 = 4$ lần**!
> 7. **Bẫy Gọi việc Mua 1 Cổ phiếu Lẻ có $\alpha_i > 0$ và Bán khống Thị trường là "Pure Risk-Free Arbitrage" (Practice Q83c):** Dù $\beta$ ròng có thể được khử về $0$, cổ phiếu đơn lẻ vẫn mang rủi ro đặc thù $\sigma_{e,i} > 0$ (công ty có thể gặp tai nạn riêng làm giá sập bất chấp thị trường). Đó chỉ là vị thế đầu cơ có lợi thế thống kê (*positive-alpha active bet*), **KHÔNG PHẢI** kinh doanh chênh lệch giá phi rủi ro (*pure arbitrage*)!


---

<a id="lecture-07"></a>
# LECTURE 07: MÔ HÌNH ĐA NHÂN TỐ, APT, FAMA-FRENCH & ĐỊNH GIÁ TÀI SẢN ESG
*(MULTIFACTOR MODELS, ARBITRAGE PRICING THEORY, FAMA-FRENCH & ESG ASSET PRICING)*

---

## 7.1. Trực giác Kinh tế Cốt lõi & Tổng hợp Lý thuyết Toàn diện

### A. Giới hạn Lý thuyết của CAPM & Động lực Mở rộng sang Đa Nhân tố
CAPM giả định mọi nhà đầu tư chỉ quan tâm tới biến động của cải 1 kỳ và mọi tài sản đều giao dịch không ma sát. Khi nới lỏng các giả định lý tưởng này, cân bằng thị trường tự nhiên xuất hiện thêm các nguồn rủi ro hệ thống được định giá ngoài $\beta_M$:

1. **Vốn Nhân lực Phi Giao dịch (Nontradable Human Capital):**
   - Tài sản lớn nhất của phần lớn cá nhân là giá trị hiện tại của thu nhập lao động tương lai (*human wealth*), vốn không thể bán đứt hay đa dạng hóa tự do trên sàn.
   - Người lao động sẽ né tránh các cổ phiếu có tương quan dương mạnh với rủi ro mất việc/giảm lương của mình và sẵn sàng trả giá cao hơn (chấp nhận lợi suất kỳ vọng thấp hơn) cho những tài sản giúp **phòng hộ rủi ro thu nhập lao động** $\implies$ danh mục thị trường chứng khoán $M$ không còn là danh mục hiệu quả duy nhất cho mọi người!
2. **ICAPM Đa kỳ của Robert Merton (1973 — Intertemporal CAPM):**
   - Nhà đầu tư hoạch định dài hạn không chỉ lo của cải cuối năm nay giảm, mà còn lo **tập cơ hội đầu tư tương lai xấu đi** (ví dụ lãi suất thực sụt giảm làm thu nhập tái đầu tư về già teo tóp, hoặc lạm phát năng lượng tăng vọt làm giảm sức mua).
   - Bất kỳ tài sản nào hoạt động tốt đúng vào lúc điều kiện kinh tế vĩ mô / cơ hội đầu tư tương lai mem theo hướng bất lợi sẽ đóng vai trò **danh mục phòng hộ liên thời gian (*hedging portfolio*)**, được săn đón nhiều hơn và mang phần bù rủi ro cân bằng riêng biệt $\lambda_k$.
3. **Rủi ro Thanh khoản Hệ thống (Liquidity Risk — Pástor & Stambaugh, 2003):**
   - Ngoài phần bù cho mức chi phí giao dịch trung bình (*illiquidity level*), nhà đầu tư đặc biệt sợ những cổ phiếu có **Liquidity Beta cao** — tức những mã đột ngột bốc hơi thanh khoản và sụt giá sâu đúng vào những tháng khủng hoảng khi thanh khoản toàn thị trường cạn kiệt.
4. **Nguyên lý Phân định Sống còn cho MCQ (L07 Cell 3 & Practice Q90b):**
   - Việc thêm một biến ngành hoặc biến vĩ mô vào hồi quy lợi suất làm **tăng $R^2$ (mô tả thêm sự biến động cùng chiều / co-movement)** **KHÔNG tự động chứng minh** biến đó mang phần bù rủi ro cân bằng $\lambda_k \ne 0$ và **KHÔNG tự động bác bỏ CAPM**!
   - Nếu biến động thêm của ngành đó có thể được đa dạng hóa hết trên phạm vi toàn nền kinh tế (hoặc nhà đầu tư biên không đòi bảo hiểm trước biến động đó), thì dù $\beta_{i,\text{sector}} \ne 0$ giúp tăng $R^2$, phần bù cân bằng của nó vẫn bằng **$\lambda_{\text{sector}} = 0$**!

---

### B. Phương trình Tạo sinh Lợi suất Đa nhân tố: Phân biệt Tuyệt đối $\lambda_k$ vs. $F_k$!
*(Trọng tâm L07 Q4 — Tuyệt đối không được nhầm lẫn giữa Kỳ vọng đầu kỳ và Cú sốc thực hiện cuối kỳ!)*

1. **Phương trình Lợi suất Thực hiện (Realized Return via Factor Surprises):**
   $$r_i = E(r_i) + \sum_{k=1}^K \beta_{i,k} F_k + e_i$$
   - Trong đó **$F_k = \text{Actual}_k - \text{Expected}_k$** là **Cú sốc / Phần bất ngờ của nhân tố vĩ mô $k$ (*Factor Surprise / Macroeconomic Innovation*)**, luôn có kỳ vọng đầu kỳ bằng không ($E(F_k) = 0$), và $e_i$ là cú sốc đặc thù doanh nghiệp ($E(e_i) = 0$, không tương quan với các $F_k$ và không tương quan giữa các công ty).
2. **Phương trình Lợi suất Kỳ vọng Cân bằng (Expected Return via Factor Risk Premia):**
   $$E(r_i) = r_f + \sum_{k=1}^K \beta_{i,k} \lambda_k$$
   - Trong đó **$\lambda_k = E(r_{P,k}) - r_f$** là **Phần bù Rủi ro Nhân tố $k$ (*Factor Risk Premium*)** — phần thưởng kỳ vọng hàng năm để nắm giữ 1 đơn vị độ nhạy $\beta_k = 1$ của nhân tố đó.
3. **Sự Tương phản Sắc bén giữa $\lambda_k$ và $F_k$ (Ví dụ Lạm phát L07 Q4):**
   - **$\lambda_k$ hoàn toàn có thể mang dấu ÂM!** Giả sử tài sản có $\beta_{\text{Inf}} > 0$ tăng giá khi lạm phát vọt tăng (giúp bảo vệ sức mua cho nhà đầu tư). Vì đặc tính bảo hiểm quý giá này, nhà đầu tư sẵn sàng chấp nhận $\lambda_{\text{Inf}} = -1.0\% < 0$, làm **hạ thấp lợi suất kỳ vọng đầu năm $E(r_i)$** của cổ phiếu có $\beta_{\text{Inf}} = +1.5$ đi một lượng $1.5 \times (-1.0\%) = -1.50\%$.
   - Ngược lại, nếu đầu năm thị trường dự báo lạm phát là $2.5\%$ nhưng cuối năm lạm phát thực tế vọt lên $4.5\%$, thì cú sốc bất ngờ là **$F_{\text{Inf}} = 4.5\% - 2.5\% = +2.0\% > 0$**. Chính cổ phiếu có $\beta_{\text{Inf}} = +1.5$ đó lại được cộng thêm **$+1.5 \times (+2.0\%) = +3.00\%$** vào lợi suất thực hiện $r_i$ trong năm đó!
   - *Bài học xương máu:* Nếu đầu năm dự báo GDP tăng $3\%$ và cuối năm GDP thực tế tăng $2\%$, thì **$F_{\text{GDP}} = 2\% - 3\% = -1\%$** (tin xấu làm giảm giá cổ phiếu có $\beta_{\text{GDP}} > 0$, chứ đừng thấy chữ "GDP tăng dương $2\%$" mà thay $+2\%$ vào $F_{\text{GDP}}$!).

---

### C. Lý thuyết Định giá Kinh doanh Chênh lệch (Arbitrage Pricing Theory — APT, Stephen Ross 1976)
1. **Ba Giả định Tối giản & Sức mạnh của Luật Số Lớn:**
   - APT chỉ cần 3 trụ cột nhẹ nhàng hơn CAPM rất nhiều: (i) Lợi suất được sinh ra bởi mô hình nhân tố tuyến tính; (ii) Có đủ nhiều chứng khoán để lập các **danh mục đa dạng hóa tốt (*well-diversified portfolios*)** làm phương sai đặc thù biến mất ($\sigma_{e,P}^2 = \sum w_i^2 \sigma_{e,i}^2 \to 0$); (iii) Thị trường không tồn tại cơ hội **kinh doanh chênh lệch giá phi rủi ro (*No-Arbitrage*)**.
   - Với một danh mục đa dạng hóa tốt $P$ ($\sigma_{e,P} \approx 0$), lợi suất của nó hoàn toàn tất định theo các nhân tố chung: $r_P = E(r_P) + \sum_{k=1}^K \beta_{P,k} F_k$. Nếu hai danh mục đa dạng hóa tốt có cùng bộ hệ số nhạy $(\beta_1, \dots, \beta_K)$ mà lại có lợi suất kỳ vọng khác nhau, nhà đầu tư chỉ cần **mua danh mục có $E(r)$ cao và bán khống danh mục có $E(r)$ thấp** với cùng số tiền để thu khoản lãi chắc chắn 100% mà không tốn 1 đồng vốn và không chịu bất kỳ rủi ro nào! Để loại bỏ máy in tiền vô hạn đó, $E(r_P)$ bắt buộc phải là hàm tuyến tính chính xác của các $\beta_{P,k}$:
     $$E(r_P) = r_f + \beta_{P,1}\lambda_1 + \beta_{P,2}\lambda_2 + \dots + \beta_{P,K}\lambda_K$$

2. **Ba Điều kiện Nghiêm ngặt của Danh mục Pure Arbitrage & Giới hạn với Cổ phiếu Đơn lẻ:**
   - Một chiến lược chỉ được gọi là **Pure (Risk-Free) Arbitrage** khi thỏa mãn đồng thời cả 3 phương trình:
     1. **Đầu tư ròng bằng 0 (Zero Net Investment):** $\sum_i w_i = 0$ (tự tài trợ 100%).
     2. **Rủi ro bằng 0 tuyệt đối (Zero Systematic AND Zero Idiosyncratic Risk):** $\beta_{\text{arb},k} = \sum_i w_i \beta_{i,k} = 0$ với **mọi** nhân tố $k = 1, \dots, K$, **ĐỒNG THỜI** các thành phần phải là các **danh mục đa dạng hóa tốt** để $e_{\text{arb}} \approx 0$!
     3. **Lợi nhuận chắc chắn dương (Strictly Positive Sure Return):** $\sum_i w_i E(r_i) > 0$.
   - **Tại sao 1 Cổ phiếu Đơn lẻ bị định giá sai KHÔNG tạo ra Pure Arbitrage? (L07 Q1b):** Nếu bạn mua USD 1,000,000 một cổ phiếu đơn lẻ $X$ có $\alpha_X = +2\%$ và bán khống danh mục chỉ số + T-bill để đưa $\beta_k = 0$, vị thế của bạn vẫn phơi nhiễm trọn vẹn trước cú sốc đặc thù $e_X$ ($\sigma_{e,X} > 0$) của công ty $X$! Nếu CEO của $X$ bị bắt vào ngày mai, bạn lỗ nặng $\implies$ đây là giao dịch cải thiện Sharpe Ratio (*statistical / risky arbitrage*), **KHÔNG PHẢI** pure risk-free arbitrage!

3. **Bảng Đối chiếu Kinh điển CAPM vs. APT:**

| Tiêu chí Đối chiếu | CAPM (Sharpe–Lintner–Mossin) | APT (Stephen Ross) |
|---|---|---|
| **Cơ chế dẫn xuất cân bằng** | Tối ưu hóa hữu dụng Mean–Variance của toàn bộ cá nhân + Thanh toán bù trừ thị trường (*Market Clearing*). Một lượng lớn nhà đầu tư mua bán nhẹ từng mã để khôi phục cân bằng. | Điều kiện **Không kinh doanh chênh lệch giá (*No-Arbitrage*)** + Luật Số Lớn. Chỉ cần **một vài nhà đầu tư lớn** đánh cược quy mô khổng lồ vào cơ hội arbitrage là đủ ép giá về cân bằng! |
| **Vai trò của Danh mục Thị trường $M$** | **Tối quan trọng** (cần quan sát được Market Portfolio thực sự chứa mọi tài sản rủi ro — *Roll's Critique* chỉ ra điều này bất khả thi trên thực tế!). | **KHÔNG CẦN** xác định hay quan sát danh mục thị trường $M$! |
| **Phạm vi định giá chính xác** | Áp dụng chính xác cho **TẤT CẢ mọi cổ phiếu đơn lẻ** lẫn mọi danh mục. | Áp dụng chính xác tuyệt đối cho **mọi danh mục đa dạng hóa tốt**; một số ít cổ phiếu đơn lẻ có thể lệch nhẹ mà chưa vi phạm No-Arbitrage. |
| **Xác định tên các Nhân tố** | Lý thuyết chỉ định rõ duy nhất 1 nhân tố là **Market Excess Return ($R_M$)**. | Đa nhân tố linh hoạt, nhưng **lý thuyết APT tự thân không cho biết trước các nhân tố đó cụ thể là biến vĩ mô nào** (phải tìm bằng thực nghiệm). |

---

### D. Factor-Mimicking Portfolios & Phòng hộ Nhân tố Tài trợ Bằng Nợ Vay (Debt-Financed Factor Hedging)
1. **Xây dựng Danh mục Thuần Nhân tố (Pure Factor / Factor-Mimicking Portfolio — L07 Cell 38 & Practice Q99):**
   - Trong một nền kinh tế 2 nhân tố (ví dụ GDP và Lãi suất), để lập **Danh mục Thuần Nhân tố 1** (có $\beta_{P,1} = 1$, $\beta_{P,2} = 0$, và tổng tỷ trọng $\sum w_i = 1$) từ 3 tài sản đa dạng hóa (hoặc 2 danh mục rủi ro + T-bill có $\beta_{f,1} = \beta_{f,2} = 0$), bạn chỉ cần giải hệ 3 phương trình tuyến tính:
     $$\begin{cases} w_A + w_B + w_f = 1 \\ w_A \beta_{A,1} + w_B \beta_{B,1} = 1 \\ w_A \beta_{A,2} + w_B \beta_{B,2} = 0 \end{cases}$$
   - Sau khi tìm được $(w_A, w_B, w_f)$, phần bù rủi ro nhân tố 1 suy ra ngay lập tức: **$\lambda_1 = E(r_P) - r_f = w_A[E(r_A) - r_f] + w_B[E(r_B) - r_f]$**!
   - *(Lưu ý từ Practice Q99: Nếu $A$ và $B$ chỉ là **2 cổ phiếu đơn lẻ** có $\sigma_{e,A}, \sigma_{e,B} > 0$, tổ hợp giải ra có đúng $\beta_{P,1} = 1, \beta_{P,2} = 0$ nhưng phương sai phần dư $\sigma_{e,P}^2 = w_A^2\sigma_{e,A}^2 + w_B^2\sigma_{e,B}^2 > 0$ chưa bằng 0, nên gọi chính xác là **Noisy Factor-Tracking Portfolio** thay vì Pure Mimicking Portfolio không nhiễu!)*

2. **Phòng hộ Nhân tố bằng Nợ Vay tính trên Vốn Chủ Sở Hữu Ròng (Debt-Financed Factor Hedging on Net Equity — Bài toán Đỉnh Cao L07 Q6!):**
   - Hãy phân biệt thật tỉnh táo hai cách phòng hộ:
     - *Cách 1 (Tái phân bổ nội bộ không vay nợ):* Bán bớt một phần danh mục gốc để mua danh mục phòng hộ.
     - *Cách 2 (Giữ nguyên 100% vị thế gốc và đi vay nợ ở $r_f$ để mua chồng thêm danh mục phòng hộ — L07 Q6):* Giả sử bạn giữ nguyên **EUR 100** vốn chủ ở danh mục Iota ($\beta_{I,M} = 1.1, \beta_{I,IR} = -0.6$) và đi vay thêm **EUR $100x$** ở lãi suất phi rủi ro ($\beta_{\text{loan}} = 0$) để mua **EUR $100x$** danh mục Kappa ($\beta_{K,M} = 0.2, \beta_{K,IR} = +0.2$).
   - Tính trên nền **Vốn Chủ Ròng (Net Equity = EUR 100)**, bộ tỷ trọng là $(w_I = 1, w_K = +x, w_{\text{loan}} = -x)$ (tổng bằng $1 + x - x = 1$).
   - Để khử sạch độ nhạy lãi suất về 0: $1(-0.6) + x(+0.2) = 0 \implies \mathbf{x = 3.0}$ (vay thêm **EUR 300** để mua **EUR 300** Kappa!).
   - Khi đó, độ nhạy với Thị trường tính trên EUR 100 vốn chủ ròng **KHÔNG nằm giữa 1.1 và 0.2**, mà bị đòn bẩy cộng dồn lên thành:
     $$\beta_{\text{net},M} = 1.0(1.1) + 3.0(0.2) - 3.0(0) = \mathbf{1.70}!$$

---

### E. Hệ Sinh Thái Fama–French (FF3, Carhart 4, FF5), Smart Beta & Định giá Tài sản Cân bằng ESG
1. **Tổng hợp Cấu trúc Nhân tố Fama–French & Carhart:**
   - **Fama–French 3-Factor (1993):** $E(r_i) - r_f = \beta_{i,M}\lambda_M + \beta_{i,SMB}\lambda_{SMB} + \beta_{i,HML}\lambda_{HML}$.
     - Cách tính chuẩn từ lưới phân loại $2 \times 3$ (2 nhóm Size `S, B` $\times$ 3 nhóm Book-to-Market `L, N, H` — Practice Q94):
       $$\text{SMB} = \frac{SL + SN + SH}{3} - \frac{BL + BN + BH}{3}, \qquad \text{HML} = \frac{SH + BH}{2} - \frac{SL + BL}{2}$$
     - Giải thích kinh tế cho SMB & HML: **Quan điểm rủi ro hợp lý** coi công ty nhỏ và công ty `B/M` cao là nhóm dễ tổn thương trước **rủi ro kiệt quệ tài chính chu kỳ (*distress risk*)**; **Quan điểm hành vi** cho rằng nhà đầu tư ngoại suy quá đà đẩy giá cổ phiếu tăng trưởng hào nhoáng (*glamour/low B/M*) lên quá đắt và dìm giá cổ phiếu giá trị (*value/high B/M*) xuống quá rẻ.
   - **Carhart 4-Factor (1997):** Thêm nhân tố quán tính giá **`MOM` / `WML` (Winners Minus Losers)** dựa trên thành tích 2–12 tháng trước.
   - **Fama–French 5-Factor (2015):** Mở rộng FF3 bằng việc thêm **`RMW` (Robust Minus Weak operating profitability)** và **`CMA` (Conservative Minus Aggressive asset growth/investment)**. **CỰC KỲ LƯU Ý CHO MCQ:** Mô hình FF5 **KHÔNG bao gồm Momentum (`MOM`)**, và trong dữ liệu thực nghiệm Mỹ của FF (2015), sự xuất hiện của `RMW` và `CMA` làm cho nhân tố **`HML` trở nên dư thừa (*redundant*)**!
   - **Smart Beta vs. Academic Factors & "Disappearing Alpha" (L07 Q2 & Practice Q97, Q100):**
     - Các nhân tố học thuật (`SMB, HML, RMW...`) là danh mục **Long–Short tự tài trợ (zero-cost)**; còn các sản phẩm **Smart Beta ETF** ngoài đời thực là danh mục **chỉ mua (long-only)** nghiêng tỷ trọng (*tilted*) theo quy tắc minh bạch sang Value/Quality/Low-Vol để thu hoạch phần bù nhân tố với phí rẻ hơn quỹ chủ động.
     - Một quỹ chủ động khoe có **CAPM Alpha $= +3.5\%$** nhưng khi đưa vào hồi quy **FF3/Carhart** lại có hệ số chặn $\alpha_{\text{FF3}} \approx 0\%$ thực chất **không hề có kỹ năng chọn cổ phiếu vượt trội**, mà chỉ đang thu hoạch thụ động phần bù rủi ro của cổ phiếu nhỏ và cổ phiếu giá trị (*style tilt*)!

2. **Định giá Tài sản Cân bằng ESG (Pástor, Stambaugh & Taylor, 2021 — Trọng tâm L07 Cell 37!):**
   - Mô hình định giá cân bằng khi nhà đầu tư vừa quan tâm lợi suất tài chính vừa có **sở thích phi tiền tệ đối với tính bền vững ESG (*ESG Taste*)**:
     $$E[R_i] = \beta_{i,M}\lambda_M - \beta_{i,\text{ESG}}\lambda_{\text{Taste}} \qquad (\lambda_{\text{Taste}} > 0)$$
     trong đó cổ phiếu Xanh (*Green*) có $\beta_{i,\text{ESG}} > 0$ và cổ phiếu Nâu (*Brown*) có $\beta_{i,\text{ESG}} < 0$.
   - **Giải mã Nghịch lý Hai Chiều của Cổ phiếu Xanh (Thuộc lòng từng chữ cho bài thi!):**
     1. **Lợi suất Kỳ vọng Cân bằng Dài hạn (Ex-Ante Equilibrium Expected Return): CỔ PHIẾU XANH CÓ $E[R]$ THẤP HƠN CỔ PHIẾU NÂU!**
        - *Tại sao?* Thứ nhất (**Taste Channel**): Nhà đầu tư nhận được lợi ích phi tài chính khi nắm giữ doanh nghiệp sạch, nên họ sẵn sàng trả giá mua hôm nay $P_0$ cao hơn $\implies$ kéo lợi suất tài chính kỳ vọng tương lai thấp xuống (giúp doanh nghiệp xanh hưởng **chi phí vốn thấp hơn** để đầu tư chuyển đổi xanh!). Thứ hai (**Climate-Risk Hedging Channel**): Cổ phiếu xanh là tấm khiên bảo hiểm tăng giá nếu rủi ro khí hậu hoặc thuế carbon bất ngờ bùng phát, nên mang phần bù bảo hiểm âm!
     2. **Lợi suất Thực hiện Ngắn hạn Khi Cầu ESG Tăng Đột biến (Ex-Post Realized Return under Unexpected Demand Shift): CỔ PHIẾU XANH LẠI THẮNG LỚN ($r_{\text{Green}} > r_{\text{Brown}}$)!**
        - *Tại sao?* Khi mối lo ngại khí hậu và dòng tiền đổ vào các quỹ ESG tăng mạnh **ngoài dự kiến** ($F_{\text{ESG}} > 0$), áp lực cầu mới đẩy giá $P_1$ của cổ phiếu xanh tăng vọt lên mặt bằng định giá cao mới, tạo ra lãi vốn thực hiện khổng lồ trong giai đoạn chuyển dịch! Việc ngoại suy lãi vốn quá khứ này thành "cổ phiếu xanh luôn có lợi suất kỳ vọng cao hơn trong tương lai" là một sai lầm kinh tế học nghiêm trọng!

---

## 7.2. Hệ thống Công thức Đầy đủ & Quy ước Đơn vị

1. **Multifactor Pricing & Realized Surprise Equation:**
   $$E(r_i) = r_f + \sum_{k=1}^K \beta_{i,k} \lambda_k, \qquad r_i = E(r_i) + \sum_{k=1}^K \beta_{i,k}(\text{Actual}_k - \text{Expected}_k) + e_i$$
   $$\sigma_i^2 = \sum_{k=1}^K \beta_{i,k}^2 \sigma_{F_k}^2 + \sigma_{e,i}^2 \quad \text{(khi các nhân tố } F_k \text{ trực giao đôi một: } \operatorname{Cov}(F_k, F_j) = 0\text{)}$$

2. **Hệ Phương trình 3 Bước Thiết lập Danh mục Pure Arbitrage APT:**
   - **Bước 1 (Khôi phục $\lambda_k$ chuẩn):** Từ $r_f$ và $K$ danh mục đa dạng hóa chuẩn đang ở cân bằng, giải hệ $E(r_P) - r_f = \sum_{k=1}^K \beta_{P,k}\lambda_k$ tìm $(\lambda_1, \dots, \lambda_K)$.
   - **Bước 2 (Phát hiện định giá sai $\alpha_Q$):** Với danh mục mục tiêu $Q$, tính lợi suất hợp lý theo APT: $E(r_Q)_{\text{APT}} = r_f + \sum_{k=1}^K \beta_{Q,k}\lambda_k$. So với lợi suất dự báo thực tế $E(r_Q)_{\text{actual}}$:
     - Nếu $E(r_Q)_{\text{actual}} > E(r_Q)_{\text{APT}} \implies \alpha_Q > 0$ ($Q$ bị **Underpriced** $\to$ **MUA $Q$**).
     - Nếu $E(r_Q)_{\text{actual}} < E(r_Q)_{\text{APT}} \implies \alpha_Q < 0$ ($Q$ bị **Overpriced** $\to$ **BÁN KHỐNG $Q$**).
   - **Bước 3 (Ghép Danh mục Phản chiếu *Benchmark Replicating Portfolio* $R$ có cùng chính xác $\boldsymbol{\beta}$ với $Q$):**
     Tìm tỷ trọng $(w_1, \dots, w_K, w_f)$ trên các danh mục chuẩn + T-bill sao cho $\sum w = 1$ và $\beta_{R,k} = \beta_{Q,k} \, (\forall k)$. Khi đó vị thế **Mua USD $V$ danh mục rẻ + Bán khống USD $V$ danh mục đắt** có:
     $$\text{Vốn ròng} = 0, \qquad \boldsymbol{\beta}_{\text{arb}} = \boldsymbol{\beta}_Q - \boldsymbol{\beta}_R = \mathbf{0}, \qquad \text{Lãi chắc chắn} = V \times |\alpha_Q| > 0!$$

---

## 7.3. Quy trình Giải nhanh Bài tập Tính toán Phòng thi

### Dạng 7.1: Thực chiến 3 Bước Lập Danh mục Pure Arbitrage Đa Nhân tố (L07 Q3 & Practice Q98)
**Đề bài chuẩn (Practice Q98 — APT 2 nhân tố):** Cho $r_f = 4\%$, phần bù rủi ro cân bằng của 2 nhân tố vĩ mô là $\lambda_1 = 5\%$ và $\lambda_2 = 3\%$. Giả sử đã có hai danh mục chuẩn thuần nhân tố đa dạng hóa tốt: Danh mục $P_1$ ($\beta_{11} = 1, \beta_{12} = 0, E(r_1) = 9\%$) và Danh mục $P_2$ ($\beta_{21} = 0, \beta_{22} = 1, E(r_2) = 7\%$). Bạn phát hiện một danh mục đa dạng hóa tốt $Q$ có $\beta_{Q,1} = 1.2$, $\beta_{Q,2} = 0.5$ đang có lợi suất kỳ vọng trên thị trường là **$E(r_Q)_{\text{mkt}} = 13.0\%$**. Hãy kiểm tra cơ hội arbitrage và nêu rõ giao dịch cụ thể cho quy mô USD 1,000,000!
- **Bước 1 — Tính lợi suất cân bằng APT của $Q$:**
  $$E(r_Q)_{\text{APT}} = 4\% + 1.2(5\%) + 0.5(3\%) = 4\% + 6\% + 1.5\% = \mathbf{11.50\%}$$
- **Bước 2 — Tính Alpha & Xác định chiều Mua/Bán:**
  $$\alpha_Q = 13.00\% - 11.50\% = \mathbf{+1.50\% > 0} \implies Q \text{ đang bị Underpriced } \implies \mathbf{\text{MUA LONG } Q!}$$
- **Bước 3 — Lập Danh mục Nhân bản $R$ có cùng $(\beta_1 = 1.2, \beta_2 = 0.5)$ từ $(P_1, P_2, r_f)$:**
  - Đặt $w_{P_1} = 1.2$ (để khớp $\beta_1 = 1.2$), $w_{P_2} = 0.5$ (để khớp $\beta_2 = 0.5$), và phần còn lại vào T-bill để tổng tỷ trọng bằng $1$: $w_f = 1 - 1.2 - 0.5 = \mathbf{-0.70}$!
  - Kiểm tra lợi suất của $R$: $E(r_R) = 1.2(9\%) + 0.5(7\%) - 0.7(4\%) = 10.8\% + 3.5\% - 2.8\% = \mathbf{11.50\%}$ (khớp tuyệt đối!).
- **Bước 4 — Chốt Lệnh Giao dịch Zero-Investment Pure Arbitrage (Quy mô USD 1,000,000):**
  - **Mua (Long)** USD 1,000,000 danh mục $Q$.
  - **Bán khống (Short)** danh mục $R$, tức là: **Short USD 1,200,000 danh mục $P_1$**, **Short USD 500,000 danh mục $P_2$**, và **Cho vay (Lend / Buy T-bills) USD 700,000** ở lãi suất $4\%$!
  - *Kiểm tra 3 tiêu chuẩn vàng:*
    1. Tiền ròng đầu kỳ: $+1.0\text{M} - 1.2\text{M} - 0.5\text{M} + 0.7\text{M} = \mathbf{\text{USD } 0}$!
    2. Độ nhạy nhân tố ròng: $\beta_1 = 1.2 - 1.2 = \mathbf{0}$; $\beta_2 = 0.5 - 0.5 = \mathbf{0}$; rủi ro đặc thù $\approx \mathbf{0}$!
    3. Lợi nhuận chắc chắn phi rủi ro cuối năm: $1,000,000 \times (13.00\% - 11.50\%) = \mathbf{+\text{USD } 15,000}$!

---

### Dạng 7.2: Bài toán Surprise Đa Nhân tố Có Dấu Ngược Chiều (L07 Q4)
**Đề bài chuẩn:** Lợi suất cổ phiếu Omega phụ thuộc vào 2 nhân tố: Tăng trưởng Công nghiệp ($IP$) và Lạm phát ($INF$) với $\beta_{IP} = 1.2$, $\beta_{INF} = +0.8$. Đầu năm: $r_f = 3\%$, phần bù rủi ro cân bằng $\lambda_{IP} = +5\%$, $\lambda_{INF} = -1.5\%$ (phần bù bảo hiểm lạm phát âm); thị trường dự báo đầu năm $E(IP) = 4.0\%$ và $E(INF) = 2.5\%$. Cuối năm thực tế ghi nhận: $IP_{\text{actual}} = 3.0\%$, $INF_{\text{actual}} = 4.5\%$, và công ty Omega trúng thầu hợp đồng riêng giúp tạo ra cú sốc đặc thù $e_{\Omega} = +1.4\%$. Tính lợi suất kỳ vọng đầu năm $E(r_{\Omega})$ và lợi suất thực hiện cuối năm $r_{\Omega}$!
1. **Lợi suất kỳ vọng đầu năm (dùng $\lambda_k$):**
   $$E(r_{\Omega}) = 3\% + 1.2(+5\%) + 0.8(-1.5\%) = 3\% + 6.0\% - 1.2\% = \mathbf{7.80\%}$$
2. **Các cú sốc vĩ mô bất ngờ (Actual $-$ Forecast):**
   - $F_{IP} = 3.0\% - 4.0\% = \mathbf{-1.0\%}$ (tăng trưởng thấp hơn kỳ vọng!).
   - $F_{INF} = 4.5\% - 2.5\% = \mathbf{+2.0\%}$ (lạm phát cao hơn kỳ vọng!).
3. **Lợi suất thực hiện cuối năm (dùng $F_k$ và $e_{\Omega}$):**
   $$r_{\Omega} = 7.80\% + 1.2(-1.0\%) + 0.8(+2.0\%) + 1.4\% = 7.80\% - 1.20\% + 1.60\% + 1.40\% = \mathbf{9.60\%}$$

---

## 7.4. Các Bẫy Lý thuyết & Lỗi Sai Chết Người trong MCQ (Lecture 07)

> [!WARNING]
> **6 BẪY LÝ THUYẾT & TÍNH TOÁN CHÍ MẠNG CỦA LECTURE 07:**
> 1. **Bẫy Thay Giá trị Vĩ mô Thực tế (`Actual`) thay vì Cú sốc (`Actual - Expected`) vào Phương trình Đa nhân tố:** Nếu GDP thực tế tăng $+3\%$ trong khi thị trường đầu năm đã kỳ vọng GDP tăng $+4\%$, thì tin tức mới là **tin xấu ($F_{\text{GDP}} = -1\%$)**, làm cổ phiếu chu kỳ giảm điểm so với kỳ vọng chứ không phải tăng!
> 2. **Bẫy Đảo Ngược Định lý ESG (L07 Cell 37):** Học sinh rất hay chọn nhầm mệnh đề *"Green stocks have higher expected returns in equilibrium because investors prefer them"*. **SAI NGƯỢC 180 ĐỘ!** Chính vì nhà đầu tư ưa chuộng cổ phiếu Xanh và ghét cổ phiếu Nâu, giá hiện tại của cổ phiếu Xanh bị đẩy lên cao hơn $\implies$ **cổ phiếu Xanh có lợi suất kỳ vọng cân bằng THẤP HƠN ($E[R_{\text{Green}}] < E[R_{\text{Brown}}]$)**! Cổ phiếu Xanh chỉ thắng về lợi suất **thực hiện (*realized return*)** khi sở thích ESG tăng mạnh **bất ngờ** ngoài dự đoán!
> 3. **Bẫy Tưởng Fama–French 5-Factor Bao gồm Momentum:** Mô hình 5 nhân tố của Fama–French (2015) gồm `MKT, SMB, HML, RMW, CMA` — **TUYỆT ĐỐI KHÔNG CÓ `MOM` (Momentum)**! Mô hình có Momentum là **Carhart 4-Factor** (`MKT, SMB, HML, MOM`).
> 4. **Bẫy Lẫn lộn Smart Beta ETF với Academic Factor Portfolio (Practice Q97):** Nhân tố học thuật `HML` hay `SMB` là danh mục **zero-cost long-short** (mua một vế, bán khống một vế, $\beta_M \approx 0$); còn quỹ **Smart Beta ETF** ngoài thị trường là quỹ **long-only** nắm giữ cổ phiếu thực nên vẫn chịu rủi ro thị trường chung ($\beta_M \approx 1$) rất lớn!
> 5. **Bẫy Tính Beta Vốn Chủ Ròng bằng Trung bình Tỷ trọng 50/50 khi Đi Vay Nợ Phòng hộ (L07 Q6):** Khi bạn giữ nguyên EUR 100 tài sản gốc và vay thêm EUR 300 mua tài sản phòng hộ, tổng vị thế rủi ro gấp 4 lần vốn chủ ròng ($w_1 = +1, w_2 = +3, w_{\text{loan}} = -3$) $\implies \beta_{\text{net},M} = 1\beta_{1,M} + 3\beta_{2,M}$, không bao giờ chia cho $1 + 3 = 4$ (chia cho 4 là tính trên *Gross Assets* EUR 400, không phải trên *Net Equity* EUR 100)!
> 6. **Bẫy Tưởng APT Đòi hỏi Mọi Cổ phiếu Đơn lẻ Đều Phải Nằm Chính xác Trên Mặt phẳng Định giá:** Khác CAPM, lý thuyết No-Arbitrage thuần túy của APT chỉ đóng đinh chính xác đối với các **Well-Diversified Portfolios**; một vài cổ phiếu lẻ có thể bị lệch giá nhẹ mà chưa đủ tạo ra cơ hội arbitrage phi rủi ro hoàn toàn do vướng $\sigma_{e,i} > 0$.

---

<a id="lecture-08"></a>
# LECTURE 08: GIẢ THUYẾT THỊ TRƯỜNG HIỆU QUẢ & TÀI CHÍNH HÀNH VI
*(MARKET EFFICIENCY & BEHAVIORAL FINANCE)*

---

## 8.1. Trực giác Kinh tế Cốt lõi & Tổng hợp Lý thuyết Toàn diện

### A. Bước Đi Ngẫu Nhiên (Random Walk) & Ba Dạng Thị trường Hiệu quả (EMH — Eugene Fama)
1. **Tại sao Cạnh tranh Thông tin Tạo ra Bước Đi Ngẫu Nhiên của Giá Cổ phiếu?**
   - Một thị trường vốn được gọi là **hiệu quả về mặt thông tin (*informationally efficient*)** nếu giá chứng khoán hiện tại phản ánh nhanh chóng, đầy đủ và không thiên lệch toàn bộ các thông tin hiện có.
   - **Mối liên hệ nhân quả với Random Walk (Maurice Kendall / Eugene Fama):** Giả sử một mô hình định lượng dự báo chắc chắn cổ phiếu X đang giá USD 50 sẽ tăng lên USD 58 vào thứ Sáu tới. Các nhà đầu tư săn tìm lợi nhuận sẽ lập tức đặt lệnh mua ồ ạt **ngay sáng thứ Hai hôm nay**, đẩy giá nhảy vọt lên sát USD 58 (chiết khấu nhẹ rủi ro và lãi suất vài ngày) ngay tức khắc!
   - Hệ quả tất yếu: Một khi giá hôm nay đã hấp thụ hết mọi điều có thể dự đoán, giá ngày mai chỉ dịch chuyển khi có **Thông tin Mới (News)**. Vì bản chất của "tin mới" là bất ngờ không thể biết trước (xác suất tin tốt / tin xấu là ngẫu nhiên quanh kỳ vọng), nên **biến động giá chứng khoán cũng phải không thể dự báo trước — tức tuân theo Bước đi Ngẫu nhiên có Xu hướng Trôi Dương (*Random Walk with Positive Drift* bằng mức lợi suất cân bằng đền bù rủi ro $E(r) > 0$)**!

2. **Ba Cấp độ Hiệu quả Thị trường (Nested Information Sets: $\Omega_{\text{Weak}} \subset \Omega_{\text{Semi-Strong}} \subset \Omega_{\text{Strong}}$):**

| Cấp độ EMH | Tập Thông tin Đã Phản ánh vào Giá | Chiến lược Nào Mất Tác dụng Tạo Alpha? | Bằng chứng Thực nghiệm Nào Bác bỏ Trực tiếp? |
|---|---|---|---|
| **1. Dạng Yếu (Weak-Form EMH)** | Toàn bộ **dữ liệu giao dịch thị trường trong quá khứ**: chuỗi lịch sử giá, lợi suất quá khứ, khối lượng giao dịch (*trading volume*), số dư bán khống (*short interest*). | **Phân tích Kỹ thuật (*Technical Analysis* / vẽ biểu đồ nến, ngưỡng kháng cự – hỗ trợ, đường MA)**. *(Phân tích cơ bản và tin nội gián vẫn có thể sinh lời nếu thị trường chỉ mới đạt dạng Yếu!)* | Một quy tắc giao dịch thuần túy dựa trên giá/khối lượng quá khứ kiếm được **Alpha dương có ý nghĩa thống kê trên mẫu dài hạn SAU KHI đã điều chỉnh rủi ro ($\beta$/nhân tố) và trừ sạch chi phí giao dịch**! |
| **2. Dạng Bán Mạnh (Semi-Strong-Form EMH)** | Toàn bộ dữ liệu thị trường quá khứ **CỘNG VỚI mọi thông tin công khai (*publicly available information*)**: BCTC, thông báo chia tách/cổ tức/M&A, bằng sáng chế công bố, dữ liệu vĩ mô, chất lượng quản trị. | **Cả Phân tích Kỹ thuật LẪN Phân tích Cơ bản (*Fundamental Analysis*)** dựa trên nguồn tin công khai. | Hiện tượng **trôi dạt giá kéo dài sau thông báo công khai** (như **PEAD** — giá tiếp tục tăng nhiều tuần sau ngày công bố BCTC vượt kỳ vọng thay vì nhảy 1 bước duy nhất!). |
| **3. Dạng Mạnh (Strong-Form EMH)** | Toàn bộ thông tin công khai **CỘNG VỚI mọi thông tin nội bộ mật chưa công bố (*private / corporate insider information*)**. | **Mọi chiến lược, kể cả Giao dịch Nội gián (*Insider Trading*)**! | Lãnh đạo/người nội bộ giao dịch dựa trên tin mật trước giờ công bố kiếm được lợi nhuận bất thường vượt trội (thực tế Strong-form bị bác bỏ rõ rệt, và luật chứng khoán cấm giao dịch nội gián!). |

- **Quy tắc Suy luận Lồng nhau cho Câu hỏi Trắc nghiệm Lý luận (Practice L08 Q1):**
  - $\text{Strong} \implies \text{Semi-Strong} \implies \text{Weak}$.
  - Nếu một giám đốc mua cổ phiếu bằng **tin sáp nhập mật trước khi công bố** và lãi đậm lúc tin ra, còn ngay sau giây phút công bố giá phản ánh trọn vẹn và ngừng trôi $\implies$ bằng chứng này **BÁC BỎ Strong-Form**, nhưng **HOÀN TOÀN NHẤT QUÁN (KHÔNG BÁC BỎ) Semi-Strong-Form và Weak-Form**!
  - Ngược lại, nếu một quy tắc kỹ thuật thực sự đánh bại thị trường sau điều chỉnh rủi ro & chi phí (bác bỏ Weak-Form), thì **cả Semi-Strong lẫn Strong-Form cũng tự động bị bác bỏ theo**!

---

### B. Vấn đề Giả thuyết Kép (Joint Hypothesis Problem), Dị thường & Hiệu quả Quỹ Tương hỗ
1. **Joint Hypothesis Problem (Định lý Bất khả phân tách của Fama):**
   - Để kết luận một chiến lược tạo ra "lợi suất bất thường $\alpha \ne 0$", nhà nghiên cứu bắt buộc phải trừ đi mức "lợi suất bình thường hợp lý tương ứng với rủi ro" được tính từ một **Mô hình Định giá Tài sản cụ thể** (như CAPM hoặc Fama–French).
   - Do đó, mọi kiểm định EMH luôn là **kiểm định đồng thời (joint test) của HAI giả thuyết**: **(H1) Thị trường hiệu quả về thông tin** VÀ **(H2) Mô hình định giá rủi ro được chọn là hoàn toàn đúng**!
   - Nếu kiểm định bị bác bỏ ($\hat{\alpha} \ne 0$), không bao giờ kết luận tuyệt đối được rằng thị trường phi lý trí, bởi rất có thể thị trường hoàn toàn hiệu quả nhưng mô hình CAPM đã bỏ sót nhân tố rủi ro thực sự!

2. **Các Dị thường Thị trường Nổi bật (Empirical Anomalies) & Tranh luận Giải thích:**
   - **Sự kiện Ngắn hạn — Post-Earnings-Announcement Drift (PEAD):** Sau ngày doanh nghiệp công bố lợi nhuận gây bất ngờ dương (*positive earnings surprise*), giá nhảy lên một phần ngay ngày công bố nhưng vẫn **tiếp tục bò lên dần suốt 60–90 ngày tiếp theo** (do nhà đầu tư bảo thủ cập nhật thông tin quá chậm!).
   - **Chuỗi Thời gian — Momentum Ngắn–Trung hạn (3–12 tháng) vs. Đảo chiều Dài hạn (Long-Term Reversal 3–5 năm — DeBondt & Thaler):** Nhóm cổ phiếu thắng lớn 6–12 tháng qua tiếp tục thắng trong vài tháng tới (*momentum*), nhưng xét trên chân trời 3–5 năm thì nhóm cổ phiếu từng bị vùi dập thê thảm nhất (*extreme past losers*) lại bật tăng vượt trội nhóm từng tăng nóng nhất (*extreme past winners*) — gợi ý hiện tượng phản ứng thái quá dài hạn (*overreaction & correction*).
   - **Lát cắt Ngang — Size, Value (`B/M`), Neglected-Firm & Liquidity Effects.**

3. **Nghịch lý Grossman–Stiglitz & Đánh giá Quỹ Chủ động: Gross Alpha vs. Net Alpha (Practice L08 Q3):**
   - **Nghịch lý Grossman–Stiglitz (1980):** Nếu giá thị trường lúc nào cũng phản ánh miễn phí 100% mọi thông tin ẩn, chẳng nhà phân tích nào chịu bỏ tiền lương và mua dữ liệu để nghiên cứu cổ phiếu nữa — mà khi không ai nghiên cứu thì giá lại mù thông tin! Vì vậy, trạng thái cân bằng thực tế phải là **"Gần như hiệu quả" (*sensibly efficient*)**: các quỹ chuyên nghiệp giỏi nhất kiếm được **Gross Alpha dương trước phí ($\alpha_{\text{gross}} > 0$)** vừa đủ bù đắp chi phí nghiên cứu và chi phí giao dịch, nhưng do cạnh tranh vốn (Berk & Green, 2004) và mức thu phí quản lý, **Net Alpha để lại cho nhà đầu tư cá nhân trung bình bằng 0 hoặc âm nhẹ ($\alpha_{\text{net}} \le 0$)**!
   - **Công thức Phân rã Alpha & Mức Phí Quản lý Hòa vốn (Break-Even Management Fee — Practice L08 Q3):**
     $$\alpha_{\text{gross}} = r_{\text{gross}} - \left[r_f + \beta_M R_M + \beta_{SMB}\text{SMB} + \beta_{HML}\text{HML}\right]$$
     $$\alpha_{\text{net}} = \alpha_{\text{gross}} - \text{Trading Costs} - \text{Management Fee}$$
     $$\implies \mathbf{\text{Break-Even Management Fee} = \alpha_{\text{gross}} - \text{Trading Costs}} \quad (\text{để } \alpha_{\text{net}} = 0!)$$

---

### C. Tài chính Hành vi (Behavioral Finance): Giới hạn Arbitrage & Hệ thống Các Thiên kiến Tâm lý
Để một sai lệch định giá tồn tại bền vững trên thị trường, Tài chính hành vi chỉ ra cần **hai điều kiện song hành**: nhà đầu tư cá nhân mắc các thiên kiến có hệ thống (*irrationality is systematic, not random canceling noise*) **VÀ** các nhà kinh doanh chênh lệch giá hợp lý bị trói tay bởi **Giới hạn Arbitrage (*Limits to Arbitrage*)**.

#### 1. Ba Trụ cột Giới hạn Kinh doanh Chênh lệch Giá (Limits to Arbitrage)
- **Rủi ro Cơ bản (Fundamental Risk):** Khi bán khống một cổ phiếu công nghệ đang bong bóng, không có tài sản thay thế hoàn hảo 100% để phòng hộ rủi ro riêng của công ty đó; nếu công ty bất ngờ phát minh ra sản phẩm đột phá thật, quỹ short có thể cháy tài khoản.
- **Rủi ro Nhà giao dịch Nhiễu / Rủi ro Chân trời Vốn (Noise Trader Risk / Horizon Risk):** Đám đông quá khích có thể đẩy cổ phiếu định giá cao **càng tăng điên cuồng hơn nữa trong ngắn hạn**, làm quỹ arbitrage bị lỗ tạm thời trên sổ sách (*mark-to-market losses*), dẫn tới bị gọi ký quỹ (*margin calls*) hoặc nhà đầu tư rút vốn buộc phải thanh lý vị thế ở đúng đỉnh lỗ trước khi giá kịp quay đầu về giá trị nội tại!
- **Chi phí Thực thi, Rào cản Bán khống & Dải Không Kinh doanh Chênh lệch Giá (Implementation Costs, Short-Sale Constraints & No-Arbitrage Band — Trọng tâm Tính toán Practice L08 Q5!):**
  - Để khai thác tài sản bị định giá quá đắt (hoặc chiến lược **Reverse Cash-and-Carry**: Bán khống cổ phiếu cơ sở giá $S_0$ + Cho vay tiền + Mua hợp đồng kỳ hạn giá $F_{\text{quoted}}$ khi thấy $F_{\text{quoted}}$ rẻ hơn giá kỳ hạn lý thuyết $F^*$), quỹ bắt buộc phải đi mượn cổ phiếu và chịu **phí mượn cổ phiếu (*stock-borrowing fee*)**, rủi ro bị đòi lại cổ phiếu bất thình lình (*recall risk*) và phí giao dịch. (Ví dụ lịch sử kinh điển: vụ tách cổ phần **3Com / Palm** và cặp cổ phiếu song sinh **Royal Dutch / Shell**!).
  - **Định lý Dải Không Kinh doanh Chênh lệch (No-Arbitrage Band):**
    - Giá kỳ hạn lý thuyết không ma sát (với cổ tức trả cuối kỳ $D_1$): $F^* = S_0(1 + r_f) - D_1$.
    - Nếu việc bán khống 1 cổ phiếu tốn chi phí mượn cổ phiếu quy về cuối kỳ là $c_{\text{borrow}}$ (USD/cổ phiếu), thì lợi nhuận ròng cuối kỳ trên mỗi cổ phiếu của chiến lược Reverse Cash-and-Carry là:
      $$\Pi_{\text{reverse}} = \left[S_0(1 + r_f) - D_1\right] - F_{\text{quoted}} - c_{\text{borrow}} = (F^* - F_{\text{quoted}}) - c_{\text{borrow}}$$
    - Chiến lược **CHỈ có lãi** nếu $F_{\text{quoted}} < F^* - c_{\text{borrow}}$! Ngược lại, nếu $F^* - c_{\text{borrow}} \le F_{\text{quoted}} \le F^* + k_{\text{long}}$, chênh lệch giá trên bảng điện hoàn toàn bị nuốt chửng bởi ma sát giao dịch $\implies$ **KHÔNG tồn tại lợi nhuận arbitrage thực tế** và cũng **KHÔNG vi phạm tính hiệu quả thị trường sau chi phí**!

#### 2. Bảng Phân biệt Chuẩn Xác Các Thiên kiến Tâm lý (Nhận diện Tình huống Thực tế 100% Chính xác — Practice L08 Q2 & Q4!)

| Tên Thiên kiến (Bias) | Nhóm Bản chất | Dấu hiệu Nhận diện Điển hình trong Đề bài Tình huống & Hệ quả Thị trường |
|---|---|---|
| **Overconfidence** *(Quá tự tin)* | Xử lý thông tin | Quá tin vào kỹ năng chọn mã và khoảng dự báo hẹp của bản thân $\implies$ **giao dịch mua bán liên tục (*excessive trading*)**, danh mục kém đa dạng hóa, lợi suất ròng thua kém nhóm ít giao dịch. |
| **Confirmation Bias** *(Thiên kiến xác nhận — Q2b)* | Xử lý thông tin | Đã kết luận trước về một cổ phiếu, sau đó **chỉ chọn lọc đọc các bài phân tích/tin tức củng cố niềm tin sẵn có** và bỏ ngoài tai/hạ thấp các cảnh báo rủi ro hoặc báo cáo kiểm toán xấu! |
| **Anchoring & Adjustment** *(Neo tâm lý — Q2a)* | Xử lý thông tin | Neo chặt định giá vào một con số lịch sử tùy ý (như **đỉnh giá 52 tuần EUR 120** hay giá mua ban đầu) và chỉ chịu hạ mục tiêu giá rất ít dù lợi nhuận cơ bản của công ty đã suy giảm vĩnh viễn! |
| **Representativeness** *(Thiên kiến đại diện)* | Xử lý thông tin | Bỏ qua cỡ mẫu nhỏ và quy luật hồi quy về trung bình: thấy doanh nghiệp tăng trưởng tốt 2–3 năm đã ngoại suy thành siêu cổ phiếu tăng trưởng mãi mãi $\implies$ đẩy giá quá đà (*overreaction*) dẫn tới **Long-Term Reversal**. |
| **Conservatism** *(Bảo thủ)* | Xử lý thông tin | Cập nhật niềm tin **quá chậm chạp** khi có tin tức cơ bản mới thực sự thay đổi cuộc chơi $\implies$ phản ứng thiếu hụt lúc đầu (*underreaction*), tạo ra **PEAD** và **Momentum**. |
| **Prospect Theory & Loss Aversion** *(Lý thuyết triển vọng)* | Sở thích hành vi | Đánh giá hữu dụng theo **Lãi/Lỗ so với Điểm tham chiếu (*Reference Point*)** thay vì tổng của cải cuối kỳ: **ngại rủi ro ở miền lãi** (hàm lõm), **ưa thích rủi ro ở miền lỗ** (hàm lồi — đánh cược để gỡ hòa), và nỗi đau thua lỗ nặng gấp $\sim 2.25$ lần niềm vui lãi tương đương. |
| **Disposition Effect** *(Hiệu ứng vị thế — Q4a)* | Sở thích hành vi | Hệ quả trực tiếp của điểm tham chiếu + độ cong chữ S: **vội vã bán chốt lời cổ phiếu đang xanh quá sớm (*sell winners too soon*), nhưng cố chấp ôm chặt cổ phiếu đang đỏ quá lâu (*hold losers too long*)** chỉ vì giá mua lịch sử khác nhau dù triển vọng tương lai hai mã y hệt nhau! |
| **Mental Accounting & House-Money Effect** *(Kế toán tâm lý — Q4b)* | Sở thích hành vi | **Vi phạm tính thay thế của đồng tiền (*violates fungibility of money*)**: chia tài sản thành các "hũ tinh thần" riêng biệt — tiền tiết kiệm lương thì gửi trái phiếu siêu an toàn, còn **tiền thưởng Tết hoặc tiền lãi mới thắng chứng khoán (*house money*)** thì đem tất tay vào cổ phiếu đầu cơ rủi ro cực cao thay vì tối ưu hóa một danh mục chung! |
| **Framing & Regret Avoidance** *(Khung trình bày & Né tránh hối tiếc)* | Sở thích hành vi | Thay đổi quyết định rủi ro chỉ vì cách dùng từ ("tỷ lệ sống sót" vs. "tỷ lệ thất bại"); chuộng cổ phiếu *blue-chip* nổi tiếng hoặc bầy đàn (*herding*) để giảm cảm giác tự trách mình nếu thua lỗ. |

---

## 8.2. Hệ thống Công thức Đầy đủ & Quy ước Đơn vị

1. **Đánh giá Quỹ theo Mô hình Đa nhân tố (FF3 / Carhart Benchmark):**
   $$E(r_{\text{bench}}) = r_f + \beta_M(r_M - r_f) + \beta_{SMB}\text{SMB} + \beta_{HML}\text{HML} \ (+ \beta_{MOM}\text{MOM})$$
   $$\alpha_{\text{gross}} = r_{\text{fund, gross}} - E(r_{\text{bench}}), \qquad \alpha_{\text{net}} = \alpha_{\text{gross}} - c_{\text{trading}} - f_{\text{mgmt}}, \qquad f_{\text{mgmt}}^{\text{break-even}} = \alpha_{\text{gross}} - c_{\text{trading}}$$

2. **Định giá Kỳ hạn Cổ phiếu Có Cổ tức & Lợi nhuận Arbitrage Có Phí Mượn Cổ phiếu:**
   - Giá kỳ hạn lý thuyết không ma sát (kỳ hạn 1 năm, lãi suất $r_f$, cổ tức tiền mặt dự kiến trả cuối năm $D_1$ — hoặc hiện giá cổ tức $PV(D)$ nhân $(1+r_f)$):
     $$F^* = S_0(1 + r_f) - D_1 = \left[S_0 - PV(D_1)\right](1 + r_f)$$
   - **Khi $F_{\text{quoted}} < F^*$ (Kiểm tra chiến lược Reverse Cash-and-Carry: Short 1 cổ phiếu tại $S_0$, gửi tiền lãi $r_f$, trả cổ tức thay $D_1$ cuối năm, Long 1 hợp đồng kỳ hạn mua lại cổ phiếu giá $F_{\text{quoted}}$, chịu phí mượn cổ phiếu quy về cuối năm $c_{\text{borrow}}$):**
     - *Lưu ý về thời điểm thu phí mượn cổ phiếu:* Nếu phí mượn $b_0$ thu ngay **đầu kỳ ($t=0$)** thì giá trị cuối kỳ của phí là $c_{\text{borrow}} = b_0(1 + r_f)$; nếu đề cho thẳng phí mượn thanh toán vào **cuối kỳ thanh toán ($t=1$)** là $c_1$ (như Practice L08 Q5) thì dùng trực tiếp $c_{\text{borrow}} = c_1$!
     $$\text{Net Arbitrage Profit per Share at } T = (F^* - F_{\text{quoted}}) - c_{\text{borrow}}$$
     $$\text{Break-Even Stock-Borrowing Fee at } T = F^* - F_{\text{quoted}}$$

---

## 8.3. Quy trình Giải nhanh Bài tập Tính toán Phòng thi

### Dạng 8.1: Đảo Ngược Thứ hạng Quỹ Tương hỗ dưới Chuẩn Fama–French 3 Nhân tố & Phí Hòa vốn (Practice L08 Q3)
**Đề bài chuẩn từ Bộ đề Luyện tập L08 Q3:** Trong năm qua: $r_f = 3.0\%$, $R_M = r_M - r_f = 7.0\%$, $\text{SMB} = 2.5\%$, $\text{HML} = 4.0\%$. Xét hai quỹ chủ động:
- **Quỹ Kappa:** Lợi suất gộp trước phí $r_{\text{gross},K} = 15.6\%$; hệ số nhạy $(\beta_M = 1.20, \beta_{SMB} = 0.80, \beta_{HML} = 0.60)$; chi phí giao dịch $0.70\%$; phí quản lý $1.10\%$.
- **Quỹ Lambda:** Lợi suất gộp trước phí $r_{\text{gross},L} = 12.9\%$ (thấp hơn Kappa tới $2.7\%$!); hệ số nhạy $(\beta_M = 0.85, \beta_{SMB} = -0.20, \beta_{HML} = 0.10)$; chi phí giao dịch $0.35\%$; phí quản lý $0.95\%$.
1. **Tính Benchmark Return yêu cầu theo FF3:**
   - $\text{Bench}_K = 3.0\% + 1.20(7.0\%) + 0.80(2.5\%) + 0.60(4.0\%) = 3.0\% + 8.4\% + 2.0\% + 2.4\% = \mathbf{15.80\%}$.
   - $\text{Bench}_L = 3.0\% + 0.85(7.0\%) + (-0.20)(2.5\%) + 0.10(4.0\%) = 3.0\% + 5.95\% - 0.50\% + 0.40\% = \mathbf{8.85\%}$.
2. **Tính Gross Alpha & Net Alpha cho nhà đầu tư:**
   - **Kappa:** $\alpha_{\text{gross},K} = 15.60\% - 15.80\% = \mathbf{-0.20\%}$ (chưa trừ phí đã thua chuẩn rủi ro!); $\alpha_{\text{net},K} = -0.20\% - 0.70\% - 1.10\% = \mathbf{-2.00\%}$!
   - **Lambda:** $\alpha_{\text{gross},L} = 12.90\% - 8.85\% = \mathbf{+4.05\%}$ (kỹ năng chọn cổ phiếu cực xuất sắc!); $\alpha_{\text{net},L} = +4.05\% - 0.35\% - 0.95\% = \mathbf{+2.75\%}$!
   - *Nhận xét ăn điểm:* Nhìn lợi suất thô thì tưởng Kappa giỏi hơn ($15.6\% > 12.9\%$), nhưng thực chất Kappa chỉ ôm cổ phiếu rủi ro cao, nhỏ và giá trị rồi làm lỗ giá trị khách hàng ($-2.00\%$); còn Lambda giữ rủi ro thấp mà tạo ra $+2.75\%$ Net Alpha ròng!
3. **Mức phí quản lý tối đa mà Quỹ Lambda có thể thu để khách hàng vẫn không bị âm Net Alpha ($\alpha_{\text{net},L} \ge 0$):**
   $$f_{\text{mgmt},L}^{\max} = \alpha_{\text{gross},L} - \text{Trading Cost}_L = 4.05\% - 0.35\% = \mathbf{3.70\%/\text{năm}}$$

---

### Dạng 8.2: Thực chiến Limits to Arbitrage — Phí Mượn Cổ phiếu & No-Arbitrage Band (Practice L08 Q5)
**Đề bài chuẩn từ Bộ đề Luyện tập L08 Q5 (Cổ phiếu Nu):** Cổ phiếu Nu đang giao dịch ở giá giao ngay $S_0 = \text{USD } 100.00$. Dự kiến trả cổ tức chắc chắn $D_{0.5} = \text{USD } 2.00$ sau đúng 6 tháng nữa ($t = 0.5$). Lãi suất phi rủi ro ghép lãi năm (EAR) là $r_f = 4.00\%$. Hợp đồng kỳ hạn 1 năm (*1-year forward*) trên cổ phiếu Nu đang được báo giá ở mức **$F_{\text{quoted}} = \text{USD } 100.50$**. Tuy nhiên, việc mượn cổ phiếu Nu để bán khống chịu **phí mượn cổ phiếu USD $1.80$/cổ phiếu thanh toán vào cuối năm ($t = 1$)**. Xét quy mô 1,000 cổ phiếu!
1. **Bước 1 — Tính giá kỳ hạn lý thuyết không ma sát $F^*$ tại $t = 1$:**
   - Cổ tức USD $2.00$ nhận ở $t = 0.5$ được tái đầu tư thêm nửa năm đến $t = 1$ với hệ số $(1.04)^{0.5}$: $FV_1(\text{Div}) = 2.00 \times (1.04)^{0.5} = \text{USD } 2.039608$.
   - Giá kỳ hạn lý thuyết:
     $$F^* = 100.00(1.04) - 2.00(1.04)^{0.5} = 104.00 - 2.039608 = \mathbf{\text{USD } 101.9604}$$
2. **Bước 2 — Kiểm tra chiến lược Reverse Cash-and-Carry (vì $F_{\text{quoted}} = 100.50 < F^* = 101.9604$, hợp đồng kỳ hạn trông "rẻ" hơn cơ sở USD $1.4604$):**
   - Nếu không có phí mượn cổ phiếu: Short 1,000 cổ phiếu thu USD 100,000 gửi ở $4\%$, trả thay cổ tức giữa năm, Long kỳ hạn mua lại ở $100.50$ sẽ lãi $1,000 \times (101.9604 - 100.50) = +\text{USD } 1,460.39$.
   - **Tính cả phí mượn cổ phiếu USD $1.80$/cổ phiếu cuối năm:**
     $$\text{Net Payoff (1,000 shares)} = 1,000 \times \left(101.960392 - 100.50 - 1.80\right) = 1,000 \times (-0.339608) = \mathbf{-\text{USD } 339.61 \text{ (THUA LỖ CHẮC CHẮN!)}}$$
3. **Bước 3 — Tìm mức phí mượn cổ phiếu hòa vốn (Break-even stock-borrowing fee) & Kết luận EMH:**
   - Phí mượn cổ phiếu hòa vốn tại $t=1$: $c_{\text{borrow}}^* = F^* - F_{\text{quoted}} = 101.9604 - 100.50 = \mathbf{\text{USD } 1.4604 \approx \text{USD } 1.46/\text{cổ phiếu}}$.
   - *Kết luận chuẩn điểm tối đa:* Chênh lệch USD $1.46$ giữa giá kỳ hạn thực tế và công thức sách giáo khoa nằm hoàn toàn bên trong rào cản chi phí bán khống USD $1.80$ (*inside the no-arbitrage band $[100.16, \, 101.96]$*). Do đó **không tồn tại cơ hội arbitrage có lãi thực tế**, và sự lệch giá này phản ánh **Limits to Arbitrage (chi phí thực thi bán khống)** chứ không hề đồng nghĩa với "tiền miễn phí chưa ai nhặt"!

---

## 8.4. Các Bẫy Lý thuyết & Lỗi Sai Chết Người trong MCQ (Lecture 08)

> [!WARNING]
> **6 BẪY LÝ THUYẾT & TÍNH TOÁN CHÍ MẠNG CỦA LECTURE 08:**
> 1. **Bẫy Nhầm "Lợi nhuận Nội gián Bác bỏ Semi-Strong EMH" (Practice L08 Q1b):** Hãy đọc xem thông tin được giao dịch là **công khai** hay **mật chưa công bố**! Nếu lãnh đạo mua trước giờ ra tin mật rồi chốt lời lúc tin công bố (và ngay sau lúc công bố giá nhảy tức thời không trôi tiếp), đó là bằng chứng bác bỏ **Strong-Form**, tuyệt đối **KHÔNG bác bỏ Semi-Strong-Form**!
> 2. **Bẫy Đồng nhất "Random Walk" với "Kỳ vọng Giá Cổ phiếu Ngày Mai Bằng Giá Hôm Nay ($E(\Delta P) = 0$)":** SAI! Cổ phiếu rủi ro phải mang lại lợi suất kỳ vọng dương $E(r) = r_f + \text{Risk Premium} > 0$, nên giá kỳ vọng có **xu hướng trôi lên dương (*positive drift*)**. Random walk nghĩa là **phần chênh lệch xung quanh xu hướng trôi dương đó** là không thể dự đoán được từ dữ liệu quá khứ!
> 3. **Bẫy Nhầm Confirmation Bias với Overconfidence hoặc Anchoring (Practice L08 Q2):**
>    - Bám vào con số giá đỉnh cũ EUR 120 không chịu hạ $\to$ **Anchoring**.
>    - Chỉ tìm đọc tin tốt ủng hộ quyết định đã mua và phớt lờ báo cáo phân tích cảnh báo nợ xấu $\to$ **Confirmation Bias**.
>    - Bán vội cổ phiếu đang lời nhưng gồng lì cổ phiếu đang lỗ vì căn cứ vào giá mua gốc $\to$ **Disposition Effect** (từ **Prospect Theory**).
>    - Đem tiền thưởng đi đánh bạc cổ phiếu nóng trong khi tiền lương gửi tiết kiệm $\to$ **Mental Accounting / House-Money Effect** (vi phạm *fungibility*).
> 4. **Bẫy Trả lời Thiếu Ý trong Câu hỏi "Loss Aversion Có Đủ Giải thích Việc Bán Lời – Ôm Lỗ Không?" (Practice L08 Q4a):** Riêng khái niệm *Loss Aversion* (mất 1 đồng đau hơn được 1 đồng) giải thích tại sao người ta sợ tham gia các canh bạc 50/50 quanh điểm 0, nhưng để giải thích trọn vẹn việc **bán ngay ở vùng đang lời (+USD 4,000) trong khi ôm giữ ở vùng đang lỗ (-USD 4,000)** bắt buộc phải nêu đủ: **Phụ thuộc điểm tham chiếu (*Reference-Point Dependence* tại giá mua) + Độ cong hàm giá trị chữ S (*Risk-averse / lõm trong miền lãi và Risk-seeking / lồi trong miền lỗ*) tạo thành Disposition Effect**!
> 5. **Bẫy Quên Trừ Cả Hai Khoản Phí (`Trading Costs` VÀ `Management Fee`) khi Tính Net Investor Alpha (Practice L08 Q3):** Chi phí giao dịch nội bộ ăn trực tiếp vào tài sản danh mục và phí quản lý trừ tiếp vào NAV của nhà đầu tư, nên phải trừ **cả hai** khỏi $\alpha_{\text{gross}}$!
> 6. **Bẫy Kết luận "Hễ Giá Thực tế Khác Công thức Lý thuyết Không Ma sát là Có Arbitrage Lãi Chắc chắn" (Practice L08 Q5):** Luôn phải kiểm tra phí mượn cổ phiếu (*stock-borrowing fee*), *bid-ask spread*, và rủi ro *noise trader* trước khi kết luận có khai thác được hay không!

---

<a id="phu-luc-tong-hop"></a>
# PHỤ LỤC TỔNG HỢP: MA TRẬN ĐỐI CHIẾU NHANH XUYÊN CHƯƠNG & CHECKLIST PHÒNG THI
*(MASTER CROSS-LECTURE REFERENCE MATRIX & 60-SECOND EXAM VERIFICATION CHECKLIST)*

---

## P.1. Ma Trận Phân Biệt 12 Cặp Khái Niệm "Sinh Tử" Xuyên Suốt Lectures 01 – 08

| STT | Cặp Khái Niệm Dễ Nhầm | Chốt Phân Biệt Nhanh Trong 10 Giây Cho MCQ & Tự Luận |
|---|---|---|
| **1** | **Repo** vs. **Reverse Repo** *(L01)* | Nhìn từ góc độ **Dealer**: **Repo** = Dealer *bán* T-bill hôm nay + cam kết *mua lại* ngày mai (**Dealer đi vay tiền**); **Reverse Repo** = Dealer *mua* T-bill hôm nay + cam kết *bán lại* ngày mai (**Dealer cho vay tiền**). |
| **2** | **Clean (Flat) Price** vs. **Dirty (Invoice) Price** *(L02)* | Bảng điện niêm yết **Clean Price** (để không bị sụt giả tạo ngày trả coupon); số tiền thực thanh toán chuyển khoản khi mua là **Dirty Price = Clean Price + Accrued Interest** ($\text{AI} = \text{Coupon}_{\text{kỳ}} \times \frac{\text{Days elapsed}}{\text{Days in period}}$). |
| **3** | **YTM** vs. **Realized Compound Return** *(L02)* | Hai con số **CHỈ bằng nhau** nếu nắm giữ tới đáo hạn VÀ mọi khoản coupon giữa kỳ đều được tái đầu tư ở lãi suất bằng đúng YTM ban đầu ($r_{\text{reinvest}} = \text{YTM}$). Nếu $r_{\text{reinvest}} < \text{YTM} \implies \text{Realized Return} < \text{YTM}$! |
| **4** | **Pure Expectations (PEH)** vs. **Liquidity Preference (LPT)** *(L02)* | PEH: $f_n = E(r_n)$ (LP $= 0$); LPT: $f_n = E(r_n) + LP_n$ ($LP_n > 0$). Dưới LPT, đường cong lợi suất dốc lên **KHÔNG chứng minh** lãi suất ngắn hạn được kỳ vọng tăng (kỳ vọng đi ngang hoặc giảm nhẹ cộng với $LP > 0$ đủ lớn vẫn tạo đường cong dốc lên!). |
| **5** | **Cash-Flow Matching** vs. **Redington Immunization** *(L03)* | **Cash-Flow Matching**: khớp dòng tiền từng kỳ, **không cần tái cân bằng**, miễn nhiễm cả xoắn đường cong. **Immunization**: khớp $PV_A = PV_L$, $D_A = D_L$, $C_A > C_L$, **bắt buộc tái cân bằng** định kỳ và vẫn chịu rủi ro khi đường cong dịch chuyển **không song song**! |
| **6** | **Arithmetic Mean ($\bar{r}_A$)** vs. **Geometric Mean ($\bar{r}_G$)** *(L04)* | **$\bar{r}_G$** đo tốc độ tăng trưởng kép thực tế của của cải quá khứ; **$\bar{r}_A$** là dự báo không chệch tốt nhất cho kỳ vọng 1 kỳ đơn lẻ tiếp theo. Luôn có $\bar{r}_G \approx \bar{r}_A - \frac{1}{2}\sigma^2 \le \bar{r}_A$. |
| **7** | **Value at Risk (VaR)** vs. **Expected Shortfall (ES / CVaR)** *(L04)* | $\text{VaR}_{5\%}$ chỉ là vạch ngưỡng bắt đầu của $5\%$ xấu nhất (**mù đuôi** bên dưới ngưỡng); $\text{ES}_{5\%} = E[r \mid r \le \text{VaR}_{5\%}]$ đo mức lỗ trung bình bên trong đuôi $5\%$ xấu nhất (**nhạy cảm với fat tails**). |
| **8** | **GMVP** vs. **Tangency Portfolio ($P^*$)** *(L05)* | **GMVP** chỉ phụ thuộc phương sai & hiệp phương sai (độc lập với $E(r)$ và $r_f$). **$P^*$** cực đại hóa Sharpe Ratio (độc lập với $A$ nhờ Separation Property, nhưng phải kiểm tra biên cấm bán khống $w \in [0,1]$!). Ngưỡng thêm tài sản mới: **$S_Y > \rho_{XY}S_X$**. |
| **9** | **Capital Market Line (CML)** vs. **Security Market Line (SML)** *(L06)* | **CML** vẽ theo **Tổng rủi ro $\sigma_P$**, độ dốc $S_M$, **chỉ đúng cho danh mục hiệu quả hoàn hảo**. **SML** vẽ theo **Rủi ro hệ thống $\beta_i$**, độ dốc $E(R_M)$, **đúng cho mọi tài sản lẻ và mọi danh mục** trong cân bằng CAPM. Nằm **TRÊN** SML ($\alpha > 0$) là **Underpriced**! |
| **10** | **Factor Risk Premium ($\lambda_k$)** vs. **Factor Surprise ($F_k$)** *(L07)* | **$\lambda_k$** quyết định lợi suất kỳ vọng đầu kỳ $E(r_i) = r_f + \sum \beta_{ik}\lambda_k$ (có thể âm nếu là nhân tố bảo hiểm); **$F_k = \text{Actual}_k - \text{Expected}_k$** quyết định chênh lệch thực hiện $r_i - E(r_i)$ trong kỳ! |
| **11** | **ESG Equilibrium $E[R]$** vs. **ESG Realized Demand Shock** *(L07)* | Trong cân bằng dài hạn, cổ phiếu Xanh có **$E[R]$ THẤP HƠN** cổ phiếu Nâu ($\beta_{\text{ESG}} > 0$ trừ bớt $-\beta_{\text{ESG}}\lambda_{\text{Taste}}$ do sở thích xanh & phòng hộ khí hậu). Cổ phiếu Xanh chỉ có **lợi suất thực hiện cao hơn** khi cầu ESG tăng đột biến bất ngờ! |
| **12** | **Semi-Strong EMH** vs. **Strong-Form EMH** *(L08)* | Tin nội gián mật kiếm lời trước giờ công bố rồi giá nhảy ngay khi công bố: **bác bỏ Strong-Form**, nhưng **KHÔNG bác bỏ Semi-Strong-Form**! Giá tiếp tục trôi nhiều tuần *sau* ngày công bố BCTC (PEAD): **bác bỏ trực tiếp Semi-Strong-Form**! |

---

## P.2. Checklist Rà Soát 60 Giây Sinh Tử Trước Khi Nộp Bài Tự Luận (75 Phút)

1. **Kiểm tra Đơn vị Thập phân (`Decimals`) trong L04–L05:** Đã đổi $E(r), r_f, \sigma$ sang số thập phân (`0.12`, `0.20` $\implies \sigma^2 = 0.04$) khi bấm $U = E(r) - \frac{1}{2}A\sigma^2$ và $y^* = \frac{E(r_P) - r_f}{A\sigma_P^2}$ chưa? Trong $\frac{1}{2}C(\Delta Y)^2$ của L03, đã thay $\Delta Y = 0.02$ (bình phương $= 0.0004$) chưa?
2. **Kiểm tra Quy ước Ghép lãi Bán niên (`Semiannual`, $f=2$) trong L02–L03:** Đã chia đôi coupon ($C/2$), chia đôi YTM ($Y/2$), nhân đôi số kỳ ($2T$), chia Macaulay Duration kỳ cho $2$ để ra năm, chia cho $(1 + Y/2)$ để ra $D_M$, nhưng vẫn giữ nguyên $h$ theo **năm** ở mẫu số Finite-Difference Convexity $C_{\text{FD}}$ chưa?
3. **Kiểm tra Câu chữ CAPM trong L06–L07:** Đề cho *"Expected return on the market $E(r_M) = 11\%$"* (phải trừ $r_f$!) hay *"Market risk premium $E(R_M) = 8\%$"* (KHÔNG trừ $r_f$ nữa!)?
4. **Kiểm tra Biên Ràng buộc trong L04–L05:** Nếu $r_B > r_L$, đã kiểm tra vùng điểm gãy $y^* = 1.00$ chưa? Nếu đề cấm bán khống (*no short sales*), cả $w_A^*$ và $w_B^*$ có nằm trong $[0, 1]$ không?
5. **Kiểm tra Chia cho $n - 1$ vs. Xác suất Kịch bản:** Dữ liệu chuỗi lịch sử (*historical sample*) đã chia phương sai/hiệp phương sai cho **$n - 1$** chưa? Dữ liệu kịch bản tương lai có xác suất $p(s)$ đã tính trực tiếp theo $\sum p(s)$ chưa?
6. **Kiểm tra Làm tròn Chuẩn:** Giữ toàn bộ chữ số thập phân ở các bước trung gian trên máy tính cầm tay; chỉ làm tròn ở đáp số đóng khung cuối cùng (`2` chữ số thập phân cho tiền & `%`, `4` chữ số thập phân cho Duration / Convexity / Sharpe / Beta, `6` chữ số thập phân cho Variance / Covariance dạng decimal).
