# BFIN: Investments (WS2026) — Ngân Hàng 45 Câu Hỏi Chứng Minh (Prove/Derive) & Tự Luận Ngắn Lý Thuyết (Conceptual Questions $\le 100$ Words) + Giải Thích Trực Quan "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)

> **Mục đích sử dụng trong phòng thi (Ngày thi 12/11/2026):**
> 1. **Trả lời trực tiếp các ý lý thuyết / chứng minh ngắn (Sub-questions `a` hoặc `c`)** trong 5 bài tự luận (yêu cầu viết ngắn gọn, súc tích **dưới 100 từ** kèm 2–3 dòng biến đổi toán học chuẩn xác).
> 2. **Xử lý tốc độ cao 10 câu MCQs lý thuyết (Conceptual MCQs)** — đặc biệt là các câu hỏi gài bẫy về **giả định mô hình (Model Assumptions)**, **Black-Scholes**, **American Options**, **Merton Firm Valuation**, **CAPM vs. APT**, **EMH**, và **ESG**.
> 3. **Cấu trúc 3 lớp đặc biệt giúp nhớ sâu ngay lập tức (kể cả khi ôn đêm trước ngày thi):**
>    - **`[Exam Model Answer — English ≤ 100 Words]`**: Đoạn văn mẫu tiếng Anh học thuật chuẩn xác, cô đọng đúng trọng tâm chấm điểm của Dr. Omer Cayirli để bạn có thể **viết thẳng vào bài thi**.
>    - **`[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5 — Đúng 100% Bản Chất)]`**: Ví dụ đời thường siêu dễ hiểu (như tờ giấy nợ giữa hai anh em, chiếc ô đi mưa, vé giữ chỗ mua đồ chơi, bập bênh...) giúp bạn hiểu tận gốc *"Tại sao công thức lại như vậy?"* mà không cần học vẹt.
>    - **`[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm (Grading Keywords)]`**: Ghép câu chuyện đời thường sang đúng thuật ngữ chuyên ngành để không sót điểm nào.

---

## MỤC LỤC NHANH (QUICK NAVIGATION)

- [**PHẦN I: 12 CÂU HỎI VỀ GIẢ ĐỊNH & CẤU TRÚC CỦA CÁC MÔ HÌNH CỐT LÕI (MODEL ASSUMPTIONS & FRAMEWORKS)**](#phần-i-12-câu-hỏi-về-giả-định--cấu-trúc-của-các-mô-hình-cốt-lõi) *(Cực kỳ hay hỏi ở câu ngắn 60–100 từ hoặc MCQ!)*
- [**PHẦN II: 18 CÂU HỎI CHỨNG MINH & BIẾN ĐỔI CÔNG THỨC NGẮN (PROVE / DERIVE / SHOW THAT)**](#phần-ii-18-câu-hỏi-chứng-minh--biến-đổi-công-thức-ngắn-prove--derive--show-that) *(Trọng tâm cho các ý `a, c` trong 5 bài lớn — đặc biệt là 40% Derivatives!)*
- [**PHẦN III: 15 CÂU HỎI PHẢN BIỆN & PHÂN BIỆT KHÁI NIỆM (CONCEPTUAL CRITIQUE & DISTINCTIONS)**](#phần-iii-15-câu-hỏi-phản-biện--phân-biệt-khái-niệm-conceptual-critique--distinctions) *(Dạng bài "Evaluate the analyst's claim / Explain why..." đặc trưng trong Practice L01–L07 & L08–L11)*

---

## PHẦN I: 12 CÂU HỎI VỀ GIẢ ĐỊNH & CẤU TRÚC CỦA CÁC MÔ HÌNH CỐT LÕI

### Câu A1 (Lecture 06): State the key assumptions of the Capital Asset Pricing Model (CAPM) and explain why they imply that the market portfolio is on the efficient frontier.
*(Nêu các giả định chính của mô hình CAPM và giải thích tại sao chúng suy ra danh mục thị trường nằm trên đường biên hiệu quả.)*

- **[Exam Model Answer — English (~85 words)]:**
  CAPM rests on three core assumption blocks:
  1. **Homogeneous expectations & Mean-Variance optimization:** All investors share the same single-period planning horizon and identical probability beliefs regarding expected returns, variances, and covariances, and select mean-variance efficient portfolios.
  2. **Unlimited risk-free borrowing and lending:** Investors can borrow or lend without limit at a common risk-free rate $r_f$.
  3. **Frictionless, competitive markets:** All assets are publicly tradable and infinitely divisible; investors are price-takers with no taxes, transaction costs, or short-sale restrictions.
  *Implication:* By Two-Fund Separation, every investor holds the **same tangency portfolio** of risky assets. Market clearing requires aggregate demand to equal aggregate supply, so this tangency portfolio must be the **value-weighted market portfolio $M$**.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng cả lớp học đi vào một tiệm sinh tố:
  1. **Giả định 1 (Mọi người có cùng bản đồ vị giác):** Tất cả học sinh đều chấm điểm độ ngon ($E(r)$) và độ chua ($\sigma$) của từng loại trái cây **giống hệt nhau**.
  2. **Giả định 2 (Cùng một bình nước lọc $r_f$):** Ai muốn uống nhạt thì pha thêm nước lọc (cho vay ở $r_f$); ai muốn uống cực đậm thì mượn tiền mua gấp đôi cốt trái cây (đi vay ở $r_f$).
  3. **Giả định 3 (Không phí pha chế, mọi trái cây đều cắt nhỏ được):** Không ai bị tính phí hay bị cấm chọn món.
  - **Kết quả kỳ diệu:** Vì ai cũng nhìn bảng điểm trái cây giống hệt nhau, tất cả mọi người sẽ nhờ chủ quán xay **đúng 1 công thức sinh tố hỗn hợp ngon nhất duy nhất** (gọi là *Danh mục tiếp tuyến $T$*). Bạn nhát gan thì pha $90\%$ nước lọc + $10\%$ sinh tố $T$; bạn liều lĩnh thì uống $100\%$ sinh tố $T$.
  - Vì ai trong lớp cũng chỉ mua đúng bình sinh tố $T$ đó, mà tổng số trái cây trong tiệm phải được bán hết sạch (*thị trường cân bằng*), nên công thức của bình sinh tố $T$ bắt buộc phải chứa **tất cả các loại trái cây đang có trên đời theo đúng tỷ lệ số lượng của chúng** — đó chính là **Danh mục Thị trường $M$**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Nhớ đúng **3 cụm giả định trên slide L06 Cell 23**: (1) *Homogeneous expectations & 1-period mean-variance optimizers*; (2) *Borrow/lend unlimitedly at common $r_f$*; (3) *Tradable, divisible assets; frictionless competitive markets*.
  - **Logic chốt điểm:** Cùng đầu vào $\implies$ cùng **Tangency Portfolio $T$** (*Two-Fund Separation*) + Tổng cầu $=$ Tổng cung (*Market Clearing*) $\implies T \equiv \text{Market Portfolio } M$.

---

### Câu A2 (Lecture 05): State the assumptions required for the Two-Fund Separation Property in Markowitz Portfolio Theory, and explain when this property breaks down.
*(Nêu các giả định của Định lý Phân tách Hai Quỹ trong lý thuyết Markowitz và giải thích khi nào định lý này bị phá vỡ.)*

- **[Exam Model Answer — English (~80 words)]:**
  The **Two-Fund Separation Property** states that all mean-variance investors, regardless of risk aversion $A$, hold a combination of just two funds: the risk-free asset ($r_f$) and a single optimal tangency portfolio ($P^*$). Risk aversion $A$ only determines the weight $y^* = \frac{E(r_{P^*}) - r_f}{A\sigma_{P^*}^2}$ allocated to $P^*$.
  This requires: (1) homogeneous input lists ($E(r), \sigma, \text{Cov}$), (2) a single risk-free rate where $r_{\text{borrow}} = r_{\text{lend}} = r_f$, and (3) no portfolio constraints. Separation fails if $r_{\text{borrow}} > r_{\text{lend}}$ (kinked CAL), borrowing is prohibited, or investors face heterogeneous constraints/beliefs.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy nghĩ đến việc **pha cà phê sữa từ "Nước cốt cà phê đặc" ($P^*$) và "Sữa tươi" ($r_f$)**:
  - **Bước 1 (Kỹ thuật pha cốt — Không phụ thuộc vào ai uống):** Đầu bếp giỏi nhất tiệm sẽ chọn tỷ lệ hạt Arabica và Robusta sao cho ra được **1 bình nước cốt cà phê thơm ngon nhất ($P^*$)** (tối đa hóa độ ngon trên mỗi đơn vị đắng — *Sharpe Ratio*).
  - **Bước 2 (Pha theo gu từng người — Phụ thuộc độ sợ đắng $A$):** Một em bé sợ đắng ($A$ cao) hay một người lớn thích cà phê đậm ($A$ thấp) **không cần tự đi rang xay hạt lại từ đầu**! Cả hai đều dùng chung bình nước cốt $P^*$ đó, chỉ khác nhau ở lượng sữa tươi pha vào ($1 - y^*$).
  - **Khi nào định lý này vỡ?** Khi người muốn uống đậm phải đi mua đá/vay tiền với **giá cắt cổ ($r_{\text{borrow}} > r_{\text{lend}}$)**: lúc đó đường thẳng bị gãy khúc, người đi vay phải đổi sang một bình nước cốt khác đặc hơn ($P_B^* \ne P_L^*$), nên không còn dùng chung 1 bình cốt duy nhất nữa!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Quyết định đầu tư tách làm 2 bước độc lập: **Investment decision** (tìm $P^*$ cực đại hóa Sharpe Ratio) và **Financing decision** (chọn $y^*$ theo độ ngại rủi ro $A$).
  - Bị phá vỡ khi: **$r_B > r_L$ (Kinked CAL)**, cấm bán khống, hoặc cấm vay.

---

### Câu A3 (Lecture 06): State the statistical assumptions of the Single-Index Model (SIM) and show how it solves the "Curse of Dimensionality" of the full Markowitz model.
*(Nêu các giả định thống kê của Mô hình Đơn chỉ số SIM và chỉ ra cách mô hình này giải quyết bài toán bùng nổ số lượng tham số của Markowitz.)*

- **[Exam Model Answer — English (~90 words)]:**
  The Single-Index Model decomposes excess returns as $R_{i,t} = \alpha_i + \beta_i R_{M,t} + e_{i,t}$ under three statistical assumptions:
  1. Zero expected residual: $E(e_{i,t}) = 0$.
  2. Macro-residual independence: $\text{Cov}(e_{i,t}, R_{M,t}) = 0$ for all $i$.
  3. Pairwise mutually uncorrelated residuals: $\text{Cov}(e_{i,t}, e_{j,t}) = 0$ for all $i \ne j$.
  Consequently, all co-movement stems solely from the common market factor: $\text{Cov}(R_i, R_j) = \beta_i\beta_j\sigma_M^2$. For $n$ securities, the full Markowitz model requires $\frac{n(n+3)}{2}$ estimates (including $\frac{n(n-1)}{2}$ covariances), whereas SIM requires only **$3n + 2$** estimates ($\alpha_i, \beta_i, \sigma_{e,i}^2$ for each stock, plus $E(R_M), \sigma_M^2$).

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Tưởng tượng trong lớp có $50$ bạn học sinh:
  - **Cách của Markowitz:** Để biết khi nào các bạn cùng vui hay cùng buồn, thầy giáo phải ngồi đo mối quan hệ tay đôi giữa **từng cặp học sinh một** (An với Bình, An với Chi, Bình với Chi...). Với $50$ bạn, có tới $\frac{50 \times 49}{2} = 1,225$ cặp quan hệ! Nếu lớp có $1,000$ bạn thì có gần nửa triệu cặp — đo xong thì hết giờ!
  - **Cách thông minh của Single-Index Model (SIM):** Thầy giáo nhận ra các bạn cùng vui hay cùng buồn chỉ vì **1 lý do chung duy nhất: "Hôm nay trời nắng hay mưa ($R_M$)"** (còn chuyện riêng ở nhà bạn An $e_{\text{An}}$ hoàn toàn không liên quan gì đến chuyện riêng ở nhà bạn Bình $e_{\text{Bình}} \implies \text{Cov}(e_i, e_j) = 0$).
  - Nhờ vậy, thầy không cần đo từng cặp bạn chơi với nhau nữa! Thầy chỉ cần đo xem **mỗi bạn nhạy cảm với thời tiết thế nào ($\beta_i$)**. Nếu An rất thích nắng ($\beta_{\text{An}}$) và Bình cũng thích nắng ($\beta_{\text{Bình}}$), thì độ gắn kết giữa hai bạn đơn giản là $\beta_{\text{An}} \times \beta_{\text{Bình}} \times \text{Độ thất thường của thời tiết } (\sigma_M^2)$!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **3 phương trình giả định bắt buộc phải viết:** $E(e_i)=0$, $\text{Cov}(e_i, R_M)=0$, và **$\text{Cov}(e_i, e_j)=0 \ (\forall i \ne j)$**.
  - **Số lượng tham số ước lượng cho $n$ cổ phiếu:** Markowitz cần $\frac{n(n+3)}{2}$, còn SIM chỉ cần **$3n + 2$** ($\alpha_i, \beta_i, \sigma_{e,i}^2$ cho $n$ mã + $E(R_M), \sigma_M^2$).

---

### Câu A4 (Lecture 07 & Extra Session): State the core assumptions of Ross's Arbitrage Pricing Theory (APT) and explain why APT requires fewer restrictive assumptions than CAPM.
*(Nêu các giả định cốt lõi của Lý thuyết Định giá Kinh doanh Chênh lệch giá APT và giải thích tại sao APT ít giả định khắt khe hơn CAPM.)*

- **[Exam Model Answer — English (~85 words)]:**
  APT relies on three core assumptions:
  1. **Factor return-generating process:** Security returns follow a linear $K$-factor structure: $r_i = E(r_i) + \sum_{k=1}^K \beta_{i,k} F_k + e_i$, where $E(F_k)=E(e_i)=0$, $\text{Cov}(e_i, F_k)=0$, and residuals $e_i$ are sufficiently independent across securities.
  2. **Law of Large Numbers in large capital markets:** Enough securities exist to form **well-diversified portfolios** whose idiosyncratic risk vanishes ($\sigma_{e,P}^2 \to 0$).
  3. **No Arbitrage (Law of One Price):** Zero-investment, zero-risk portfolios must earn zero expected return.
  Unlike CAPM, APT does **not** require quadratic utility, normally distributed returns, single-period mean-variance optimization, or observability of the true aggregate market portfolio.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Tại sao hai túi quà giống nhau phải có giá bằng nhau?
  - **Cách chứng minh của CAPM (Rất khắt khe):** Phải giả sử **tất cả mọi người trong siêu thị đều suy nghĩ giống hệt nhau**, tính toán cùng một kiểu hàm toán học, và bạn phải kiểm kê được **toàn bộ mọi món hàng trên trái đất** (*Market Portfolio*). Chỉ cần vài người tính khác đi là lập luận lung lay.
  - **Cách chứng minh của APT (Đơn giản và thực tế hơn hẳn):** Không cần tất cả mọi người phải thông minh hay giống nhau! Chỉ cần:
    1. Mỗi giỏ quà gồm rất nhiều viên kẹo nhỏ để một vài viên kẹo bị vỡ ngẫu nhiên sẽ tự bù trừ cho nhau (**Well-diversified portfolio** làm $\sigma_e \to 0$).
    2. Trong siêu thị chỉ cần có **một vài thợ săn giá rẻ tinh mắt (Arbitrageurs)**: hễ thấy hai giỏ quà có cùng lượng sô-cô-la và dâu tây (cùng $\beta_1, \beta_2$) mà một giỏ bán rẻ hơn giỏ kia, họ lập tức **mua giỏ rẻ, bán giỏ đắt** với số lượng khổng lồ cho đến khi hai giỏ về đúng một giá (**No-Arbitrage**)!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **3 trụ cột của APT:** Linear factor model + Well-diversified portfolios ($\sigma_{e,P} \to 0$) + No-Arbitrage.
  - **Đánh đổi giữa CAPM và APT:** APT ít giả định hơn, không cần quan sát Market Portfolio, nhưng chỉ đảm bảo đúng tuyệt đối cho **Well-diversified portfolios** (cổ phiếu lẻ có thể lệch nhẹ vì còn $\sigma_{e,i} > 0$).

---

### Câu A5 (Lecture 03): State the key assumptions of Classical (Redington) Duration Immunization and identify its main practical limitation.
*(Nêu các giả định chính của phương pháp Miễn nhiễm Lãi suất Cổ điển và chỉ ra hạn chế thực tế lớn nhất của nó.)*

- **[Exam Model Answer — English (~80 words)]:**
  Classical (Redington) immunization protects a fixed future liability at horizon $H$ against interest-rate changes under two key assumptions:
  1. **Flat (or parallel-shifting) yield curve:** All spot/yield rates across maturities experience the exact same infinitesimal parallel change $\Delta y$.
  2. **No default or embedded options:** Cash flows are fixed and deterministic.
  By matching present values ($PV_A = PV_L$), matching Macaulay/Modified durations ($D_A = D_L = H$), and ensuring asset convexity exceeds liability convexity ($C_A > C_L$), price risk and reinvestment rate risk exactly offset. Its main limitation is vulnerability to **non-parallel yield curve twists/steepening** and the need for continuous rebalancing as time passes.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng bạn cần đúng **$\$1,000$ sau 5 năm nữa** để đóng học phí, và bạn đặt hai quả tạ lên một **chiếc bập bênh (seesaw)** có điểm tựa đặt ở mốc **năm thứ 5 ($H = 5$)**:
  - Một đầu bập bênh ở năm thứ 2 (dòng tiền coupon nhận sớm): nếu lãi suất ngân hàng tăng, tiền nhận ở năm thứ 2 gửi tiết kiệm tiếp sẽ **sinh lãi nhiều hơn** (*Reinvestment gain*).
  - Đầu kia của bập bênh ở năm thứ 8 (trái phiếu dài hạn phải bán ra ở năm thứ 5): nếu lãi suất tăng, giá bán trái phiếu ở năm thứ 5 sẽ **bị sụt giảm** (*Price loss*).
  - **Immunization** chính là việc đặt hai quả tạ sao cho **trọng tâm (Macaulay Duration) nằm đúng ngay điểm tựa năm thứ 5 ($D_A = H$)**! Khi đó, dù lãi suất tăng hay giảm, một đầu lên bao nhiêu thì đầu kia xuống bấy nhiêu — tổng tiền ở năm thứ 5 luôn đứng yên!
  - **Điểm yếu chí mạng:** Chiếc bập bênh này chỉ cân bằng nếu **cả mặt đất nâng lên hoặc hạ xuống đều nhau (Parallel shift — lãi suất ngắn hạn và dài hạn tăng cùng một mức)**. Nếu mặt đất bị nghiêng xoắn (*Non-parallel twist*: lãi suất năm 2 giảm mà lãi suất năm 8 lại tăng!), cả hai đầu cùng tụt xuống và bạn bị hụt tiền!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Cơ chế cân bằng:** *Price Risk* và *Reinvestment Rate Risk* triệt tiêu nhau tại $D_{\text{Mac}} = H$.
  - **Giả định & Hạn chế:** Giả định **Parallel yield curve shift**; thất bại khi đường cong lãi suất bị xoắn (**Non-parallel twist/steepening**) và đòi hỏi phải **tái cân bằng (rebalancing)** liên tục.

---

### Câu A6 (Lecture 08): Define the three forms of the Efficient Market Hypothesis (EMH) and explain Fama's "Joint Hypothesis Problem".
*(Định nghĩa 3 dạng của Giả thuyết Thị trường Hiệu quả EMH và giải thích "Vấn đề Giả thuyết Kép" của Fama.)*

- **[Exam Model Answer — English (~90 words)]:**
  EMH classifies market efficiency by the information set $\Omega_t$ already reflected in prices:
  1. **Weak form:** Prices reflect all historical trading data (past prices, returns, volume), rendering **technical analysis** useless.
  2. **Semi-strong form:** Prices reflect all publicly available information (financial statements, macroeconomic news, past prices), rendering **fundamental analysis** unable to earn consistent abnormal returns.
  3. **Strong form:** Prices reflect all public and **private (insider)** information.
  **Joint Hypothesis Problem:** Measuring "abnormal return" ($\alpha$) requires specifying an equilibrium risk-pricing model (e.g., CAPM or FF3). Thus, any empirical rejection is ambiguous: either the market is inefficient **or** the chosen asset-pricing benchmark is misspecified.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng trò chơi đoán số kẹo trong bình thủy tinh ở sân trường:
  1. **Weak form (Dạng Yếu):** Mọi kết quả đoán của **những ngày hôm trước** đã được ghi lên bảng. Nhìn lại lịch sử đoán cũ (*Technical Analysis* — kẻ biểu đồ nến) không giúp bạn đoán giỏi hơn ai cả.
  2. **Semi-strong form (Dạng Bán mạnh):** Thầy giáo công khai luôn **kích thước bình và kích thước viên kẹo trên loa phát thanh** (*Public info*). Vì ai cũng nghe loa cùng lúc và sửa giá ngay lập tức, việc bạn ngồi đọc lại tờ thông báo công khai đó (*Fundamental Analysis*) cũng không giúp bạn thắng được thị trường.
  3. **Strong form (Dạng Mạnh):** Ngay cả **người trực tiếp bỏ kẹo vào bình trong phòng kín** (*Insider / Private info*) cũng không thể thắng! (Ngoài đời thực, nếu người bỏ kẹo lén đặt cược thì họ vẫn thắng $\implies$ Strong form bị vi phạm, nhưng Semi-strong vẫn đúng!).
  - **Joint Hypothesis Problem (Bài toán Cái Cân hỏng):** Muốn biết một bạn học sinh có "nặng bất thường ($\alpha \ne 0$)" hay không, bạn phải dùng **một cái cân chuẩn (mô hình CAPM/FF3)**. Nếu cân báo bạn ấy thừa $5\text{ kg}$, bạn không bao giờ dám chắc 100% là do **bạn ấy thừa cân thật (thị trường không hiệu quả)** hay do **cái cân bị lệch sẵn (mô hình CAPM bị sai)**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Weak form $\to$ bác bỏ *Technical analysis*; Semi-strong form $\to$ bác bỏ *Fundamental analysis*; Strong form $\to$ bao gồm cả *Private/Insider info*.
  - **Joint Hypothesis Problem:** Kiểm định EMH luôn đi kèm kiểm định **Asset Pricing Model (CAPM/FF3)**.

---

### Câu A7 (Lecture 08): Explain "Limits to Arbitrage" and state the three main frictions that prevent rational arbitrageurs from immediately eliminating mispricing.
*(Giải thích khái niệm "Giới hạn của Kinh doanh Chênh lệch giá" và nêu 3 lực cản chính ngăn cản các nhà kinh doanh chênh lệch giá xóa bỏ ngay lập tức sự định giá sai.)*

- **[Exam Model Answer — English (~85 words)]:**
  In behavioral finance, **Limits to Arbitrage** explain why irrational mispricings caused by behavioral biases can persist even when rational traders recognize them:
  1. **Fundamental Risk:** In the absence of an identical substitute security, hedging market exposure still leaves firm-specific news risk ($e_i \ne 0$).
  2. **Noise Trader Risk (Horizon / Funding Risk):** Irrational sentiment can deepen the mispricing in the short run, triggering margin calls, capital outflows, or forced liquidation before prices converge.
  3. **Implementation Costs:** Short-sale constraints, **stock-borrowing fees**, bid-ask spreads, and illiquidity create a no-arbitrage band within which mispricing cannot be profitably exploited.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Giả sử một món đồ chơi chỉ đáng giá **$\$10$**, nhưng đám đông cuồng nhiệt đang hét giá nó lên tận **$\$20$** (quá đắt!). Tại sao một người thông minh không dám nhảy vào "bán khống" món đồ chơi đó ở giá $\$20$ rồi chờ nó về $\$10$ mua trả lại để ăn chắc $\$10$? Vì **3 nỗi sợ có thật**:
  1. **Fundamental Risk (Không có hàng thay thế giống hệt):** Nhỡ đâu ngày mai hãng phim công bố món đồ chơi đó được lên phim bom tấn thật, giá trị thật của nó vọt lên $\$30$ thì sao? Bạn không có món đồ chơi sinh đôi nào khác để bảo hiểm 100% rủi ro tin tức riêng đó!
  2. **Noise Trader Risk (Đám đông điên loạn lâu hơn túi tiền của bạn):** Đám đông cuồng nhiệt có thể đẩy giá từ $\$20$ lên $\$50$ vào tuần sau trước khi nó kịp sập về $\$10$ vào năm sau. Khi giá lên $\$50$, chủ tiệm cho mượn đồ chơi đòi bạn nộp tiền thế chấp (**Margin Call**); bạn hết tiền mặt nên bị tịch thu sạch trước khi kịp nhìn thấy ngày mình đúng!
  3. **Implementation Costs (Phí thuê đồ chơi quá đắt):** Để mượn món đồ chơi đi bán khống, chủ tiệm đòi **phí thuê (stock-borrowing fee)** tới $\$11$! Lợi nhuận chênh lệch có $\$10$ mà phí thuê mất $\$11$ thì làm là lỗ chắc (`Practice_L08-L11` Q5)!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **3 từ khóa vàng:** (1) *Fundamental risk* (no perfect substitute, $\sigma_e > 0$); (2) *Noise trader / margin call risk* (short-run divergence forces liquidation); (3) *Implementation costs / stock-borrow fees* (creates a no-arbitrage band).

---

### Câu A8 (Lecture 07 — Pástor, Stambaugh & Taylor 2021): Explain why green (high-ESG) stocks have negative CAPM alpha in equilibrium, yet can outperform brown stocks in realized sample returns.
*(Giải thích tại sao cổ phiếu xanh có CAPM alpha cân bằng âm, nhưng vẫn có thể đạt lợi suất thực hiện trong mẫu cao hơn cổ phiếu nâu.)*

- **[Exam Model Answer — English (~85 words)]:**
  In the Pástor, Stambaugh, and Taylor (2021) ESG equilibrium model, green stocks earn a **lower equilibrium expected return** (negative CAPM alpha, $\alpha_{\text{green}} < 0$) for two reasons:
  1. **Investor ESG tastes:** ESG-oriented investors derive non-pecuniary utility from holding green firms and willingly accept lower financial returns.
  2. **Climate-risk hedging:** Green assets outperform when unexpected climate regulations or shocks hit, acting as an insurance hedge.
  However, if investor ESG preferences and customer demand for green products **strengthen unexpectedly** over the sample period, green stock prices are bid up, generating **higher realized returns** despite lower future expected returns.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy so sánh **Ngôi nhà Xanh cạnh công viên mát mẻ (Green stock)** và **Ngôi nhà Nâu cạnh bãi rác ồn ào (Brown stock)** đều cho thuê thu được **$\$10/\text{năm}$**:
  1. **Tại sao lợi suất kỳ vọng tương lai của Nhà Xanh lại THẤP HƠN ($\alpha_{\text{green}} < 0$)?** Vì ai cũng thích sống cạnh công viên sạch đẹp (*ESG taste*) và sợ bão lũ (*Climate hedge*), mọi người sẵn sàng trả **$\$200$** để mua Nhà Xanh (tỷ suất sinh lời $= 10/200 = 5\%/$năm), trong khi Nhà Nâu cạnh bãi rác phải bán rẻ **$\$100$** mới có người chịu mua (tỷ suất sinh lời $= 10/100 = 10\%/$năm). Vậy **trong trạng thái cân bằng, mua tài sản tốt/đắt thì tỷ suất lợi nhuận tương lai phải thấp hơn ($5\% < 10\%$)**!
  2. **Thế tại sao trong 5 năm qua người giữ Nhà Xanh lại LỜI TO HƠN (*Higher realized return*)?** Vì trong 5 năm qua, cả thành phố **đột nhiên phát sốt với lối sống xanh ngoài dự kiến**! Giá Nhà Xanh được đẩy vọt từ $\$200$ lên $\$300$: người mua từ trước kiếm được một cục lãi tăng giá khổng lồ (*realized capital gain*), nhưng người mới nhảy vào mua ở giá $\$300$ hôm nay thì chỉ còn nhận được lợi suất tương lai $10/300 = 3.33\%$ (càng thấp hơn nữa!).

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Ex-ante Equilibrium Expected Return:** Green < Brown ($\alpha_{\text{green}} < 0$) do *Non-pecuniary ESG tastes* + *Climate-risk hedging*.
  - **Ex-post Realized Return:** Green > Brown khi có **Unexpected positive shock to ESG demand/tastes** đẩy giá tài sản xanh tăng lên.

---

### Câu A9 (Lecture 07): Compare the Fama-French 3-Factor (FF3), Carhart 4-Factor, and Fama-French 5-Factor (FF5) models, and explain why HML becomes redundant in FF5.
*(So sánh mô hình FF3, Carhart 4 nhân tố và FF5; giải thích tại sao nhân tố giá trị HML trở nên dư thừa trong FF5.)*

- **[Exam Model Answer — English (~90 words)]:**
  - **FF3 (1993):** Adds Size (**SMB**: Small Minus Big) and Value (**HML**: High Minus Low book-to-market) to the CAPM market factor (**MKT**).
  - **Carhart (1997):** Appends short-term **Momentum (MOM / WML**: past 12-month winners minus losers) to FF3.
  - **FF5 (2015):** Extends FF3 (without Momentum) by adding Profitability (**RMW**: Robust Minus Weak operating profitability) and Investment (**CMA**: Conservative Minus Aggressive asset growth), motivated by the dividend discount valuation identity.
  Empirically, **HML becomes redundant in FF5** because high book-to-market (value) stock returns are fully spanned by their exposures to profitability (RMW) and conservative investment (CMA).

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng việc chấm điểm sức khỏe một cầu thủ bóng đá:
  - **CAPM (1 nhân tố):** Chỉ nhìn vào điểm số chung của cả đội bóng (`MKT`).
  - **FF3 (3 nhân tố):** Thêm 2 đặc điểm: cầu thủ **Nhỏ con nhưng nhanh nhẹn (`SMB` — Small)** và cầu thủ **Lương rẻ so với năng lực (`HML` — Value)**.
  - **Carhart (4 nhân tố):** Thêm đặc điểm **Đang có chuỗi ghi bàn thắng liên tiếp gần đây (`MOM` — Momentum)**.
  - **FF5 (5 nhân tố):** Thay vì nhìn phong độ ngắn hạn, FF5 thêm 2 phẩm chất gốc rễ: **Sức bền thể lực cực khỏe (`RMW` — Profitability)** và **Không tiêu xài hoang phí sức lực (`CMA` — Conservative Investment)**. Khi đã đo trực tiếp được "Thể lực khỏe (`RMW`)" và "Tiết kiệm sức (`CMA`)", người ta phát hiện ra đặc điểm "Lương rẻ (`HML`)" thực chất chỉ là sự pha trộn của hai phẩm chất kia — nên `HML` trở nên **thừa thãi (redundant)**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Nhớ công thức cấu tạo: `FF3 = MKT + SMB + HML`; `Carhart = FF3 + MOM`; `FF5 = FF3 + RMW + CMA` (không có `MOM`, và `HML` trở nên *redundant* vì đã bị *spanned* bởi `RMW` và `CMA`).

---

### Câu A10 (Extra Session Cell 3): State the key assumptions of the Black-Scholes Option Pricing Model and interpret $N(d_1)$ and $N(d_2)$ economically.
*(Nêu các giả định chính của mô hình định giá quyền chọn Black-Scholes và giải thích ý nghĩa kinh tế của $N(d_1)$ và $N(d_2)$.)*

- **[Exam Model Answer — English (~90 words)]:**
  The Black-Scholes model assumes:
  1. **No arbitrage** and frictionless markets (no transaction costs, taxes, or short-sale restrictions; infinitely divisible securities).
  2. **Continuous trading** in the underlying stock, which pays no dividends before maturity.
  3. **Constant volatility $\sigma$** and constant continuously compounded risk-free rate $r_f$, with continuous lognormal stock price paths (no jumps).
  4. **European exercise style** (exercise only at maturity $T$).
  In $C_t = S_t N(d_1) - K e^{-r_f(T-t)} N(d_2)$:
  - **$N(d_1) = \Delta_C \in (0,1)$** is the **option delta** (number of shares held in the continuous replicating portfolio).
  - **$N(d_2)$** is the **risk-neutral probability** that the call finishes in the money ($S_T > K$).

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Công thức Black-Scholes $C_t = S_t N(d_1) - PV(K) N(d_2)$ nhìn phức tạp nhưng thực chất chỉ nói một câu cực kỳ giản dị:
  $$\text{Giá Quyền Chọn Mua} = (\text{Phần bạn nhận về}) - (\text{Phần tiền bạn phải trả})$$
  - Khi thực hiện quyền chọn mua, **thứ bạn nhận về là 1 cổ phiếu ($S_t$)** và **thứ bạn phải móc túi trả là giá mua $K$ (quy về hôm nay là $PV(K)$)**.
  - Nhưng vì chưa chắc đến ngày cuối bạn đã mua (chỉ mua nếu cổ phiếu tăng cao hơn $K$), nên hai vế phải nhân với trọng số xác suất từ $0$ đến $1$:
    - **$N(d_2)$:** Chính là **xác suất (trong thế giới trung hòa rủi ro) mà phiếu mua hàng của bạn trúng thưởng** ($S_T > K$), nên bạn phải trả số tiền kỳ vọng là $PV(K) \times N(d_2)$ (đây cũng chính là số tiền đi vay $B$ trong danh mục mô phỏng!).
    - **$N(d_1)$:** Chính là **số cổ phiếu ($\Delta_C$) bạn cần mua giữ sẵn hôm nay** để tự chế tạo ra chiếc quyền chọn đó! (Vì khi trúng thưởng thì giá cổ phiếu lúc đó đã cao hơn trung bình, nên $N(d_1)$ luôn lớn hơn $N(d_2)$ một chút: $d_1 = d_2 + \sigma\sqrt{T}$).

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - $N(d_1) = \Delta_C$ (*Call Delta / Hedge ratio*); $N(d_2) = \Pr^{\mathbb{Q}}(S_T > K)$ (*Risk-neutral probability of finishing in the money*); $-PV(K)N(d_2) = B$ (*Borrowing in the replicating portfolio*).

---

### Câu A11 (Lecture 09): Compare Forward Contracts and Futures Contracts across institutional features, cash-flow timing, and credit risk.
*(So sánh Hợp đồng Kỳ hạn và Hợp đồng Tương lai về đặc điểm định chế, thời điểm dòng tiền và rủi ro tín dụng.)*

- **[Exam Model Answer — English (~85 words)]:**
  While both lock in a price today for future delivery, they differ in four key dimensions:
  1. **Trading venue & Standardization:** Forwards are customized, bilateral over-the-counter (**OTC**) agreements; futures are standardized contracts traded on organized **exchanges**.
  2. **Settlement timing:** Forwards settle **once at maturity $T$**; futures are **marked to market daily**, realizing gains and losses in cash every day.
  3. **Counterparty credit risk:** Forwards expose both parties to bilateral default risk; futures interpose a **clearinghouse** and require initial/maintenance margins, virtually eliminating default risk.
  4. **Liquidity Risk:** Daily futures settlement creates interim cash-flow/margin-call funding risk even for a hedged position.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng hai bạn cá cược xem cuối năm giá gạo tăng hay giảm:
  - **Forward (Hợp đồng Kỳ hạn):** Hai người tự viết giấy tay với nhau (**OTC**), muốn ghi bao nhiêu kg gạo hay giao ngày nào cũng được (**Customized**). Suốt cả năm không ai đưa tiền cho ai; chờ **đúng ngày cuối năm mới trả một cục tiền lớn**. Rủi ro là gì? Đến cuối năm người thua lỗ to quá **bỏ trốn luôn không trả** (*Counterparty credit risk*)!
  - **Futures (Hợp đồng Tương lai):** Hai người lên **Sàn giao dịch chính thức**, có **Trọng tài (Clearinghouse)** đứng giữa thu tiền cọc (**Margin**) của cả hai. Luật của Trọng tài: **Chốt sổ trả tiền mặt vào lúc 4 giờ chiều MỖI NGÀY (Daily Marking-to-Market)**! Hôm nay gạo tăng $\$1$, người thua bị trừ ngay $\$1$ trong ví cọc chuyển sang ví người thắng; nếu ví cọc vơi dưới mức an toàn (**Maintenance Margin**), sáng mai phải nộp tiền mặt bù về mức ban đầu (**Initial Margin**), nếu không Trọng tài đóng vị thế ngay lập tức! Nhờ vậy không ai quỵt nợ được ai, nhưng người chơi phải luôn có sẵn tiền mặt dự phòng mỗi ngày (*Liquidity risk*).

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **4 trục đối chiếu:** OTC customized vs. Exchange standardized | Single settlement at $T$ vs. Daily marking-to-market | Bilateral default risk vs. Clearinghouse + Margin | No interim cash flow vs. Daily margin-call liquidity risk.

---

### Câu A12 (Lecture 11): State the assumptions of the Binomial Option Pricing Model and explain why the physical (real-world) probability $q$ does not appear in the option pricing formula.
*(Nêu các giả định của Mô hình Định giá Quyền chọn Nhị phân và giải thích tại sao xác suất thực tế $q$ không xuất hiện trong công thức giá quyền chọn.)*

- **[Exam Model Answer — English (~85 words)]:**
  The binomial model assumes that over each discrete step $\Delta t$, the stock price moves to one of two values ($S_u = uS$ or $S_d = dS$), markets are frictionless (no taxes, transaction costs, or short-sale limits), investors can borrow/lend at gross risk-free factor $r$, and **no arbitrage** holds ($0 < d < r < u$).
  The real-world probability $q$ does not appear because the option's payoff is **exact-replicated** in every state by holding $\Delta = \frac{V_u - V_d}{S_u - S_d}$ shares and $B$ in cash. Since current stock price $S_0$ already embeds investors' risk aversion and beliefs $q$, no-arbitrage relative pricing depends only on $S_0, u, d, r$ via $p = \frac{r-d}{u-d}$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Tại sao bạn không cần biết xác suất trời mưa ($q = 90\%$ hay $q = 10\%$) mà vẫn tính được chính xác giá của một "Combo Áo mưa"?
  - Giả sử ngoài chợ đã niêm yết sẵn giá **1 mét vải nhựa = $\$10$** và **1 cuộn chỉ = $\$2$**. Nếu một chiếc Áo mưa được may từ **đúng $0.5$ mét vải nhựa ($\Delta$) và $1$ cuộn chỉ ($B$)**, thì giá chiếc Áo mưa bắt buộc phải bằng $0.5 \times \$10 + \$2 = \$7$!
  - Nếu có người bảo: *"Ngày mai xác suất mưa tới $99\%$ ($q=0.99$), nên chiếc Áo mưa phải bán giá $\$15$!"* $\implies$ Bạn lập tức mua $0.5$ mét vải + $1$ cuộn chỉ tốn có $\$7$ để tự may thành chiếc Áo mưa giống hệt rồi bán lấy $\$15$, ăn lãi không rủi ro $\$8$!
  - Vì mọi nỗi sợ trời mưa ($q$) đã được người dân phản ánh hết vào giá vải nhựa $\$10$ ($S_0$) ngoài chợ rồi, nên khi định giá chiếc Áo mưa theo nguyên liệu ($\Delta S_0 + B$), con số $q$ trở nên hoàn toàn thừa thãi!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Từ khóa vàng:** *Exact state-by-state replication* ($\Delta$ shares + $B$ cash) + *Relative no-arbitrage pricing* ($S_0$ already incorporates physical probability $q$ and risk aversion).

---

## PHẦN II: 18 CÂU HỎI CHỨNG MINH & BIẾN ĐỔI CÔNG THỨC NGẮN (PROVE / DERIVE / SHOW THAT)

### Câu P1 (Lecture 01): Prove that net financial wealth across all economic agents in a closed economy equals zero, and state how real vs. financial assets determine aggregate national wealth.
*(Chứng minh tổng tài sản tài chính ròng của mọi chủ thể trong nền kinh tế đóng bằng 0, và nêu vai trò của tài sản thực so với tài sản tài chính trong tổng của cải quốc gia.)*

- **[Exam Model Answer — English (~75 words)]:**
  Every **financial asset** (such as a bond, loan, or share of stock) is simultaneously a claim held by an investor (an **asset**) and an exact matching obligation owed by the issuer (a **liability**). Summing across all households, firms, and governments in a closed economy:
  $$\sum_{i} \text{Financial Assets}_i - \sum_{i} \text{Financial Liabilities}_i = 0$$
  Because all financial claims cancel out in aggregation, **aggregate national wealth consists solely of Real Assets** (land, buildings, machines, technology, and knowledge) that produce goods and services.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Trong một gia đình có hai anh em, trong nhà có **1 chiếc xe đạp thật (Real Asset)** trị giá $\$100$. Người anh viết một **tờ giấy nhận nợ $\$50$ (Financial Asset)** đưa cho người em:
  - Người em khoe: *"Em giàu thêm $\$50$ vì cầm tờ giấy nợ!"* ($+\$50$ Financial Asset).
  - Nhưng người anh lại đang **nợ $\$50$** ($-\$50$ Financial Liability).
  - Khi bố mẹ cộng tổng tài sản của cả gia đình lại: $+\$50 + (-\$50) = \$0$! Tờ giấy nợ tự triệt tiêu, cả nhà vẫn chỉ có đúng **1 chiếc xe đạp thật trị giá $\$100$**.

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Mỗi *Financial asset* đều có một *Matching financial liability* đối ứng $\implies$ khi tổng hợp (*aggregation*), chúng triệt tiêu nhau bằng $0$, chỉ còn lại **Real assets**.

---

### Câu P2 (Lecture 02): Derive the exact Fisher equation linking nominal interest rates ($R$), real interest rates ($r$), and inflation ($\pi$), and prove why the linear approximation $r \approx R - \pi$ overstates the real rate when inflation is positive.
*(Chứng minh phương trình Fisher chính xác và chứng minh tại sao công thức xấp xỉ tuyến tính $r \approx R - \pi$ luôn phóng đại lãi suất thực khi lạm phát dương.)*

- **[Exam Model Answer — English (~75 words)]:**
  Investing $\$1$ at nominal rate $R$ yields $\$(1+R)$ in nominal dollars after one year. If the price level rises by inflation rate $\pi$, purchasing power grows by the real gross factor $(1+r) = \frac{1+R}{1+\pi}$, which gives:
  $$1 + R = (1 + r)(1 + \pi) = 1 + r + \pi + r\pi \implies R = r + \pi + r\pi$$
  Solving exactly for the real rate gives:
  $$r = \frac{R - \pi}{1 + \pi}$$
  Whenever $\pi > 0$ (and $R > \pi$), dividing by $(1+\pi) > 1$ ensures $r_{\text{exact}} = \frac{R-\pi}{1+\pi} < R - \pi$, so the linear approximation $R - \pi$ **overstates** the true real rate by $r\pi$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hôm nay bạn có $\$100$, giá 1 chiếc bánh kem là $\$1$ $\implies$ bạn mua được **$100$ chiếc bánh**.
  - Bạn gửi ngân hàng lãi suất danh nghĩa $R = 20\% \implies$ cuối năm bạn có **$\$120$ tiền mặt**.
  - Nhưng trong năm đó, lạm phát $\pi = 10\%$ làm giá mỗi chiếc bánh kem tăng từ $\$1$ lên **$\$1.10$**.
  - Nếu bạn nhẩm ngây thơ $r \approx 20\% - 10\% = 10\%$, bạn tưởng mình sẽ mua được $110$ chiếc bánh. Nhưng thực tế cầm $\$120$ đi mua bánh giá $\$1.10$, bạn chỉ mua được $\frac{120}{1.10} = 109.09$ chiếc bánh (tức lãi thực chỉ là **$9.09\%$**, thấp hơn $10\%$)! Tại sao bị hụt mất $0.91\%$? Vì **chính phần tiền lãi $20\%$ bạn kiếm được cũng bị lạm phát $10\%$ ăn bớt giá trị ($r\pi$)**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Công thức: $1+R = (1+r)(1+\pi) \implies r = \frac{R-\pi}{1+\pi} < R - \pi$ khi $\pi > 0$ vì lạm phát làm xói mòn cả sức mua của phần tiền lãi (*inflation erodes the purchasing power of interest earned*, số hạng chéo $r\pi$).

---

### Câu P3 (Lecture 02): Derive the implied forward rate formula between $t_1$ and $t_2$ from spot rates $s_{t_1}, s_{t_2}$ by no-arbitrage, and prove why an upward-sloping yield curve ($s_2 > s_1$) does NOT necessarily imply that the market expects future short rates to rise under Liquidity Preference Theory.
*(Chứng minh công thức lãi suất kỳ hạn ngầm định từ lãi suất giao ngay bằng lập luận không arbitrage, và chứng minh tại sao đường cong lợi suất dốc lên không nhất thiết hàm ý lãi suất ngắn hạn kỳ vọng tăng theo Lý thuyết Ưu tiên Thanh khoản.)*

- **[Exam Model Answer — English (~85 words)]:**
  To prevent arbitrage between (Strategy A) buying a $t_2$-year zero-coupon bond earning $(1+s_{t_2})^{t_2}$ and (Strategy B) buying a $t_1$-year zero-coupon bond and locking in a forward reinvestment rate $f_{t_1,t_2}$ from $t_1$ to $t_2$, terminal payoffs must match:
  $$(1 + s_{t_2})^{t_2} = (1 + s_{t_1})^{t_1}(1 + f_{t_1,t_2})^{t_2 - t_1} \implies 1 + f_{1,2} = \frac{(1 + s_2)^2}{1 + s_1}$$
  Under **Liquidity Preference Theory**, long-term bonds carry a positive liquidity risk premium $LP_2 > 0$, so $f_{1,2} = E(r_2) + LP_2$. Even if expected short rates are constant or slightly falling ($E(r_2) \le s_1$), a sufficiently large $LP_2 > 0$ makes $f_{1,2} > s_1$, producing an upward-sloping yield curve ($s_2 > s_1$).

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Tại sao $(1+s_2)^2 = (1+s_1)(1+f_{1,2})$?** Giống như đi tàu từ Hà Nội vào Đà Nẵng (2 chặng): Giá vé mua thẳng 1 mạch Hà Nội $\to$ Đà Nẵng $(1+s_2)^2$ phải bằng giá vé chặng 1 Hà Nội $\to$ Vinh $(1+s_1)$ nhân với vé đặt trước chặng 2 Vinh $\to$ Đà Nẵng $(1+f_{1,2})$.
  2. **Tại sao $s_2 > s_1$ chưa chắc là lãi suất năm sau sẽ tăng?** Giả sử ai cũng biết chắc chắn lãi suất gửi tiết kiệm 1 năm của năm nay là $4\%$ và năm sau cũng vẫn là $4\%$ ($E(r_2) = 4\%$). Nhưng nếu ngân hàng bảo bạn **khóa chặt tiền trong két sắt 2 năm không được rút**, bạn sẽ đòi thêm **$1\%$ tiền bồi thường vì sự bất tiện và rủi ro khóa vốn dài hạn ($LP_2 = 1\%$)**. Khi đó $f_{1,2} = 4\% + 1\% = 5\%$, làm lãi suất 2 năm $s_2 \approx 4.5\% > 4\%$! Đường cong dốc lên chỉ vì **tiền thưởng khóa vốn ($LP_2$)** chứ lãi suất năm sau chẳng hề tăng!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Viết đúng hệ thức: $f_{1,2} = E(r_2) + LP_2$ (*Forward rate = Expected short rate + Liquidity Premium*). Vì $LP_2 > 0$, $f_{1,2} > s_1$ có thể xảy ra ngay cả khi $E(r_2) \le s_1$.

---

### Câu P4 (Lecture 03): Prove mathematically that the Macaulay Duration of a zero-coupon bond equals its maturity $T$, whereas the Macaulay Duration of any coupon-bearing bond is strictly less than $T$.
*(Chứng minh toán học rằng Macaulay Duration của trái phiếu zero-coupon bằng đúng kỳ hạn $T$, trong khi trái phiếu có trả coupon luôn có $D_{\text{Mac}} < T$.)*

- **[Exam Model Answer — English (~75 words)]:**
  Macaulay Duration is the present-value-weighted average time to receipt of cash flows:
  $$D_{\text{Mac}} = \sum_{t=1}^{T} t \cdot w_t, \qquad \text{where } w_t = \frac{PV(CF_t)}{P_0}, \quad \sum_{t=1}^{T} w_t = 1$$
  - **Zero-coupon bond:** $CF_t = 0$ for all $t < T$ and $CF_T = F > 0$. Thus $w_1 = \dots = w_{T-1} = 0$ and $w_T = \frac{PV(F)}{P_0} = 1$, giving $D_{\text{Mac}} = T \cdot 1 = T$.
  - **Coupon bond ($C > 0$):** Since $w_t > 0$ for earlier dates $t < T$ where $t < T$, the weighted average satisfies:
    $$D_{\text{Mac}} = \sum_{t=1}^{T-1} t w_t + T w_T < \sum_{t=1}^{T-1} T w_t + T w_T = T \sum_{t=1}^{T} w_t = T$$

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng một thanh thước gỗ dài từ vạch **$0$ đến vạch $10$ mét ($T=10$)**:
  - **Zero-coupon bond:** Bạn đặt toàn bộ $100\%$ khối nặng ở đúng đầu mút vạch $10$ mét. Điểm cân bằng trọng tâm của thanh gỗ đương nhiên nằm ngay tại **vạch $10$ mét ($D_{\text{Mac}} = T$)**.
  - **Coupon bond:** Bạn san bớt một vài viên bi sắt đặt rải rác ở các vạch $1, 2, \dots, 9$ mét phía trước. Ngay lập tức, điểm trọng tâm của thanh thước phải **dịch chuyển về phía trước vạch $10$ mét ($D_{\text{Mac}} < T$)**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Macaulay Duration là **trung bình có trọng số của các mốc thời gian nhận tiền** ($w_t > 0, \sum w_t = 1$). Trung bình có trọng số của các số $\le T$ (trong đó có những số $< T$) bắt buộc phải **nhỏ hơn hẳn $T$**.

---

### Câu P5 (Lecture 03): Using the second-order Duration–Convexity Taylor expansion, prove that the first-order duration approximation ALWAYS underestimates the true price of an option-free bond after any nonzero yield change $\Delta y \ne 0$.
*(Dùng khai triển Taylor bậc hai Duration–Convexity, chứng minh quy tắc xấp xỉ bậc nhất chỉ dùng Duration luôn đánh giá thấp giá thực tế của trái phiếu không kèm quyền chọn cho mọi $\Delta y \ne 0$.)*

- **[Exam Model Answer — English (~80 words)]:**
  By a second-order Taylor series expansion of $P(y)$ around $y_0$:
  $$\frac{\Delta P}{P_0} \approx \underbrace{-D_{\text{Mod}} \Delta y}_{\text{Duration approx.}} + \underbrace{\frac{1}{2} \text{Convexity} \cdot (\Delta y)^2}_{\text{Convexity adjustment}}$$
  For any option-free bond with fixed positive cash flows, $P(y)$ is strictly convex ($\frac{d^2 P}{dy^2} > 0 \implies \text{Convexity} > 0$). For any nonzero yield shift ($\Delta y > 0$ or $\Delta y < 0$), the squared term $(\Delta y)^2 > 0$ is strictly positive, so $\frac{1}{2}\text{Convexity}(\Delta y)^2 > 0$.
  Therefore, $P_{\text{true}} \approx P_{\text{Duration}} + \frac{1}{2}P_0 \cdot \text{Convexity}(\Delta y)^2 > P_{\text{Duration}}$: the linear tangent line always lies **below** the convex price-yield curve.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy đặt một **cái bát tô (đường cong giá trái phiếu $P(y)$ uốn cong lên trên như miệng cười $\smile$)** lên mặt bàn phẳng (**đường thẳng tiếp tuyến Duration**):
  - Vì cái bát uốn cong hướng lên trên ($\text{Convexity} > 0$), nên dù bạn bước sang bên trái ($\Delta y < 0$: lãi suất giảm) hay bước sang bên phải ($\Delta y > 0$: lãi suất tăng), **thành bát thật sự luôn nằm CAO HƠN mặt bàn phẳng**!
  - Về mặt toán học, số hạng cộng thêm là $+\frac{1}{2}CX(\Delta y)^2$: vì **bình phương của số âm hay số dương đều là số dương ($(\Delta y)^2 > 0$)**, nên giá thật của trái phiếu luôn bằng $(\text{Giá dự đoán của Duration}) + (\text{Một số dương}) \implies$ chỉ dùng Duration thì luôn đoán **thấp hơn** giá thật!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Nhớ cụm từ: **$\text{Convexity} > 0$ and $(\Delta y)^2 > 0$ for both $\Delta y > 0$ and $\Delta y < 0$** $\implies$ khi $\Delta y < 0$, giá tăng mạnh hơn Duration dự báo; khi $\Delta y > 0$, giá giảm nhẹ hơn Duration dự báo.

---

### Câu P6 (Lecture 03): Prove using the Duration–Convexity expansion why the three Redington Immunization conditions ($PV_A = PV_L$, $D_{\text{Mod},A} = D_{\text{Mod},L}$, $C_A > C_L$) guarantee a positive net surplus after any small parallel yield shift $\Delta y \ne 0$.
*(Chứng minh bằng khai triển Duration–Convexity tại sao 3 điều kiện Miễn nhiễm Redington đảm bảo thặng dư ròng dương sau mọi dịch chuyển lãi suất song song nhỏ $\Delta y \ne 0$.)*

- **[Exam Model Answer — English (~75 words)]:**
  Let net surplus be $S(y) = PV_A(y) - PV_L(y)$, initialized at $S(y_0) = PV_A - PV_L = 0$ (Condition 1). For a small parallel yield change $\Delta y$, the second-order Taylor expansion of the surplus change is:
  $$\Delta S = \Delta PV_A - \Delta PV_L \approx -PV_0 (D_{\text{Mod},A} - D_{\text{Mod},L})\Delta y + \frac{1}{2}PV_0 (C_A - C_L)(\Delta y)^2$$
  Matching modified durations $D_{\text{Mod},A} = D_{\text{Mod},L}$ (Condition 2) eliminates the first-order term:
  $$\Delta S \approx \frac{1}{2}PV_0 (C_A - C_L)(\Delta y)^2 > 0$$
  Whenever asset convexity exceeds liability convexity ($C_A > C_L$, Condition 3), $\Delta S > 0$ for both $+\Delta y$ and $-\Delta y$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Tưởng tượng bạn đặt hai cái bát chồng lên nhau tại cùng một điểm đáy ($PV_A = PV_L$) và có cùng độ nghiêng ở đáy ($D_A = D_L$):
  - Cái bát bên trên là **Tài sản ($A$)** được làm cong vút lên cao hơn ($C_A$ lớn).
  - Cái bát bên dưới là **Khoản nợ phải trả ($L$)** ít cong hơn ($C_L$ nhỏ).
  - Khi lãi suất nhích sang trái hay sang phải ($\Delta y \ne 0$), vì bát Tài sản uốn cong lên nhanh hơn bát Nợ ($C_A > C_L$), nên **bát Tài sản luôn nằm cao hơn bát Nợ ở cả hai phía** — nghĩa là tiền bạn có luôn nhiều hơn tiền bạn phải trả ($\Delta S > 0$)!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Viết phương trình $\Delta S \approx -PV_0(D_{\text{Mod},A} - D_{\text{Mod},L})\Delta y + \frac{1}{2}PV_0(C_A - C_L)(\Delta y)^2$. Hạng tử bậc nhất triệt tiêu do $D_A = D_L$; hạng tử bậc hai dương do $C_A > C_L$ và $(\Delta y)^2 > 0$.

---

### Câu P7 (Lecture 04): Derive the optimal allocation $y^*$ to a risky portfolio $P$ when combined with a risk-free asset $r_f$ for an investor with quadratic utility $U = E(r_C) - \frac{1}{2}A\sigma_C^2$.
*(Chứng minh công thức tỷ trọng phân bổ vốn tối ưu $y^*$ vào danh mục rủi ro $P$ khi kết hợp với tài sản phi rủi ro $r_f$.)*

- **[Exam Model Answer — English (~70 words)]:**
  Investing weight $y$ in risky portfolio $P$ and $(1-y)$ in the risk-free asset yields complete portfolio expected return $E(r_C) = r_f + y[E(r_P) - r_f]$ and variance $\sigma_C^2 = y^2\sigma_P^2$. Substituting into utility $U(y)$:
  $$U(y) = r_f + y[E(r_P) - r_f] - \frac{1}{2}A y^2 \sigma_P^2$$
  Taking the first-order condition with respect to $y$ and setting $\frac{dU}{dy} = 0$:
  $$\frac{dU}{dy} = [E(r_P) - r_f] - A y \sigma_P^2 = 0 \implies y^* = \frac{E(r_P) - r_f}{A \sigma_P^2}$$
  Since $\frac{d^2 U}{dy^2} = -A\sigma_P^2 < 0$ for $A > 0$, $y^*$ is the unique global maximum.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy nghĩ đến việc ăn ớt cay để nhận phần thưởng:
  - Mỗi thìa ớt ($y$) bạn ăn thêm sẽ mang lại cho bạn **phần thưởng không đổi là $[E(r_P) - r_f]$ đồng** (lợi ích tăng bậc nhất theo $y$).
  - Nhưng nỗi đau rát lưỡi (phương sai rủi ro) lại **tăng theo bình phương số thìa ớt ($\frac{1}{2}A\sigma_P^2 \cdot y^2$)**! Ăn thìa đầu tiên chỉ hơi tê, nhưng ăn thêm thìa thứ hai, thứ ba thì độ rát tăng vọt gấp 4, gấp 9 lần!
  - Bạn sẽ dừng ăn ở đúng thìa $y^*$ nơi **Phần thưởng của thìa tiếp theo $=$ Độ đau rát tăng thêm của thìa đó** (đạo hàm bằng $0$): $[E(r_P) - r_f] = A\sigma_P^2 y^* \implies y^* = \frac{E(r_P) - r_f}{A\sigma_P^2}$!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Lưu ý sống còn khi thay số: $\sigma_C = y\sigma_P \implies \sigma_C^2 = y^2\sigma_P^2$, đạo hàm của $\frac{1}{2}y^2$ ra $y$ (mất số $\frac{1}{2}$!). Và nhớ đổi phần trăm ra **số thập phân** trước khi tính!

---

### Câu P8 (Lecture 05): Prove that the variance of an equally weighted portfolio of $N$ risky assets equals $\sigma_p^2 = \frac{1}{N}\bar{\sigma}^2 + \frac{N-1}{N}\overline{\text{Cov}}$, and explain its limit as $N \to \infty$.
*(Chứng minh phương sai của danh mục trọng số đều $N$ tài sản bằng $\sigma_p^2 = \frac{1}{N}\bar{\sigma}^2 + \frac{N-1}{N}\overline{\text{Cov}}$ và giải thích giới hạn khi $N \to \infty$.)*

- **[Exam Model Answer — English (~80 words)]:**
  In an $N\times N$ covariance matrix with equal weights $w_i = \frac{1}{N}$, there are $N$ diagonal variance terms and $N(N-1)$ off-diagonal covariance terms:
  $$\sigma_p^2 = \sum_{i=1}^N \left(\frac{1}{N}\right)^2 \sigma_i^2 + \sum_{i=1}^N \sum_{j \ne i} \left(\frac{1}{N}\right)^2 \text{Cov}(r_i, r_j)$$
  Defining average variance $\bar{\sigma}^2 = \frac{1}{N}\sum_{i=1}^N \sigma_i^2$ and average covariance $\overline{\text{Cov}} = \frac{1}{N(N-1)}\sum_{i\ne j}\text{Cov}(r_i, r_j)$:
  $$\sigma_p^2 = \frac{1}{N}\bar{\sigma}^2 + \frac{N-1}{N}\overline{\text{Cov}}$$
  As $N \to \infty$, $\frac{1}{N}\bar{\sigma}^2 \to 0$ (firm-specific risk is diversified away), while $\frac{N-1}{N}\overline{\text{Cov}} \to \overline{\text{Cov}}$ (irreducible systematic market risk).

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy vẽ một **bàn cờ hình vuông có $N$ hàng và $N$ cột** (tổng cộng có $N^2$ ô vuông nhỏ, mỗi ô có trọng số $\frac{1}{N^2}$):
  - Trên **đường chéo chính** chỉ có đúng **$N$ ô vuông** (đó là phương sai riêng $\sigma_i^2$ của từng công ty). Cộng $N$ ô này lại rồi chia cho $N^2$ thì chỉ còn **$\frac{N}{N^2} = \frac{1}{N}$**! Khi bàn cờ mở rộng ra $N = 1,000$ ô, đường chéo chỉ chiếm $\frac{1}{1,000} \to 0$ (biến mất hoàn toàn!).
  - Ngược lại, **ngoài đường chéo chính** có tới **$N(N-1)$ ô vuông** (đó là sự biến động cùng nhau $\text{Cov}(r_i, r_j)$). Cộng $N(N-1)$ ô này lại rồi chia cho $N^2$ thì chiếm tới **$\frac{N-1}{N} \to 100\%$ diện tích bàn cờ**! Vì vậy, khi mua thật nhiều cổ phiếu, rủi ro riêng tự triệt tiêu về $0$, nhưng rủi ro chung của cả nền kinh tế ($\overline{\text{Cov}}$) chiếm trọn bàn cờ và không bao giờ biến mất!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Nhớ hình ảnh **Bàn cờ $N \times N$**: $N$ ô đường chéo ($\frac{1}{N}\bar{\sigma}^2 \to 0$) + $N(N-1)$ ô ngoài đường chéo ($\frac{N-1}{N}\overline{\text{Cov}} \to \overline{\text{Cov}}$).

---

### Câu P9 (Lecture 05): Prove how to construct a zero-variance portfolio ($\sigma_p = 0$) from two risky assets with $\sigma_1 \ne \sigma_2$ when (a) $\rho_{12} = -1$ and (b) $\rho_{12} = +1$.
*(Chứng minh cách lập danh mục có phương sai bằng 0 từ 2 tài sản rủi ro khi (a) $\rho_{12} = -1$ và (b) $\rho_{12} = +1$.)*

- **[Exam Model Answer — English (~80 words)]:**
  1. **Perfect negative correlation ($\rho_{12} = -1$):**
     $$\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 - 2w_1 w_2\sigma_1\sigma_2 = (w_1\sigma_1 - w_2\sigma_2)^2$$
     Setting $w_1\sigma_1 - (1-w_1)\sigma_2 = 0$ gives **positive weights** (no short selling required):
     $$w_1 = \frac{\sigma_2}{\sigma_1 + \sigma_2} \in (0,1), \qquad w_2 = \frac{\sigma_1}{\sigma_1 + \sigma_2} \in (0,1)$$
  2. **Perfect positive correlation ($\rho_{12} = +1$, with $\sigma_1 \ne \sigma_2$ and short sales permitted):**
     $$\sigma_p^2 = (w_1\sigma_1 + w_2\sigma_2)^2 = 0 \implies w_1\sigma_1 + (1-w_1)\sigma_2 = 0 \implies w_1 = \frac{-\sigma_2}{\sigma_1 - \sigma_2}, \quad w_2 = \frac{\sigma_1}{\sigma_1 - \sigma_2}$$
     One asset must be sold short ($w < 0$) to offset the other's volatility.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Khi $\rho = -1$ (Cửa hàng Áo mưa $\sigma_1 = 20\%$ và Cửa hàng Kem $\sigma_2 = 10\%$):** Hễ trời mưa thì Áo mưa lãi gấp đôi còn Kem lỗ một nửa; trời nắng thì ngược lại. Bạn chỉ cần **mua cả hai cửa hàng** theo tỷ lệ nghịch với độ dao động của chúng ($1/3$ vào Áo mưa và $2/3$ vào Kem): phần lời của bên này luôn bù khít phần lỗ của bên kia ($w_1\sigma_1 - w_2\sigma_2 = 0$), không cần bán khống!
  2. **Khi $\rho = +1$ (Hai chiếc diều cùng bay lên hoặc cùng hạ xuống theo một cơn gió):** Diều 1 bay cao gấp đôi Diều 2 ($\sigma_1 = 20\%, \sigma_2 = 10\%$). Nếu bạn chỉ mua cả hai, chúng sẽ cùng bay lên hoặc cùng rơi xuống. Nhưng nếu bạn được phép **đặt cược ngược (bán khống $-100\%$ Diều 1) và mua $+200\%$ Diều 2**, thì khi gió thổi mạnh, khoản lỗ từ đặt cược ngược Diều 1 ($-1 \times 20\%$) được bù khít bởi khoản lời từ $2$ chiếc Diều 2 ($+2 \times 10\% = +20\%$) $\implies$ độ rung lắc tổng cộng vẫn bằng $0$!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Khai triển hằng đẳng thức: $\rho = -1 \implies \sigma_p = |w_1\sigma_1 - w_2\sigma_2| = 0$ ($w_1, w_2 > 0$); $\rho = +1 \implies \sigma_p = |w_1\sigma_1 + w_2\sigma_2| = 0$ (đòi hỏi một trọng số âm — *short sale*).

---

### Câu P10 (Lecture 05 Cell 43): State and prove the "Diversification Hurdle" condition ($S_Y > \rho_{XY} S_X$) for adding a small positive weight of asset $Y$ to an existing portfolio $X$, and explain why an asset with $S_Y < 0$ can still be added if $\rho_{XY} < 0$.
*(Nêu và chứng minh điều kiện "Ngưỡng Đa dạng hóa" $S_Y > \rho_{XY} S_X$ để thêm tài sản $Y$ vào danh mục $X$, và giải thích tại sao một tài sản có Sharpe ratio âm vẫn có thể làm tăng Sharpe ratio danh mục nếu $\rho_{XY} < 0$.)*

- **[Exam Model Answer — English (~85 words)]:**
  Adding a marginal weight $w_Y > 0$ of asset $Y$ to portfolio $X$ increases the portfolio's Sharpe ratio if and only if $Y$'s excess return exceeds its systematic exposure to $X$:
  $$E(R_Y) > \beta_{Y,X} E(R_X) = \left(\rho_{XY}\frac{\sigma_Y}{\sigma_X}\right) E(R_X)$$
  Dividing both sides by $\sigma_Y > 0$ yields the **Diversification Hurdle**:
  $$\frac{E(R_Y)}{\sigma_Y} > \rho_{XY} \frac{E(R_X)}{\sigma_X} \iff S_Y > \rho_{XY} S_X$$
  If $\rho_{XY} < 0$ and $S_X > 0$, the right-hand threshold $\rho_{XY} S_X$ is **strictly negative**. Thus, a hedging asset with a slightly negative risk premium ($0 > S_Y > \rho_{XY} S_X$) still improves the overall Sharpe ratio by strongly reducing portfolio variance!

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Giả sử đội bóng của bạn ($X$) đang có hiệu suất ghi bàn rất cao ($S_X = 0.80$). Bạn có nên tuyển thêm một hậu vệ ($Y$) chỉ biết ghi bàn ở mức trung bình ($S_Y = 0.30$) hay không?
  - Nhiều người nhìn thoáng qua bảo: *"$0.30 < 0.80$, tuyển vào làm kéo tụt điểm trung bình của đội!"* — **SAI!**
  - Nếu hậu vệ $Y$ có lối chơi **bù đắp hoàn hảo những lúc tiền đạo $X$ bị kèm chặt** (hệ số trùng lặp $\rho_{XY}$ rất thấp, ví dụ $\rho_{XY} = 0.20$), thì "ngưỡng điểm tối thiểu" mà $Y$ cần đạt chỉ là $0.20 \times 0.80 = 0.16$! Vì $S_Y = 0.30 > 0.16$, đưa $Y$ vào sân làm đội bóng vững chắc hơn hẳn và điểm tổng thể tăng vọt!
  - Thậm chí, nếu $Y$ là một "thủ môn chuyên cứu thua" ($\rho_{XY} = -0.50 < 0$), thì ngưỡng điểm yêu cầu là $-0.50 \times 0.80 = -0.40$. Dù thủ môn đó đôi khi phát bóng hỏng làm mất chút điểm ($S_Y = -0.10 < 0$), nhưng vì $-0.10 > -0.40$, có thủ môn đó trên sân vẫn giúp đội bóng chiến thắng!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Công thức vàng L05 Cell 43: **$S_Y > \rho_{XY} S_X \iff E(R_Y) > \beta_{Y,X} E(R_X)$**.

---

### Câu P11 (Lecture 06): Under the Single-Index Model $R_i = \alpha_i + \beta_i R_M + e_i$, prove both (a) $\sigma_i^2 = \beta_i^2\sigma_M^2 + \sigma^2(e_i)$ and (b) $\text{Cov}(R_i, R_j) = \beta_i\beta_j\sigma_M^2$ ($i \ne j$).
*(Dưới mô hình SIM, chứng minh công thức phân rã phương sai $\sigma_i^2 = \beta_i^2\sigma_M^2 + \sigma^2(e_i)$ và công thức hiệp phương sai $\text{Cov}(R_i, R_j) = \beta_i\beta_j\sigma_M^2$.)*

- **[Exam Model Answer — English (~80 words)]:**
  Since $\alpha_i, \alpha_j$ are constants, they do not affect variances or covariances:
  - **(a) Variance Decomposition:**
    $$\sigma_i^2 = \text{Var}(\beta_i R_M + e_i) = \beta_i^2\text{Var}(R_M) + \text{Var}(e_i) + 2\beta_i\text{Cov}(R_M, e_i)$$
    By the SIM assumption $\text{Cov}(R_M, e_i) = 0$, this simplifies to $\sigma_i^2 = \beta_i^2\sigma_M^2 + \sigma^2(e_i)$.
  - **(b) Pairwise Covariance ($i \ne j$):**
    $$\text{Cov}(R_i, R_j) = \text{Cov}(\beta_i R_M + e_i, \beta_j R_M + e_j)$$
    $$= \beta_i\beta_j\text{Var}(R_M) + \beta_i\text{Cov}(R_M, e_j) + \beta_j\text{Cov}(e_i, R_M) + \text{Cov}(e_i, e_j) = \beta_i\beta_j\sigma_M^2$$
    because $\text{Cov}(R_M, e_j) = \text{Cov}(e_i, R_M) = 0$ and $\text{Cov}(e_i, e_j) = 0$ for $i \ne j$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy nghĩ đến hai chiếc thuyền nhỏ ($i$ và $j$) đang nổi trên mặt biển:
  - Độ nhấp nhô của thuyền $i$ gồm 2 phần: **Sóng biển chung của đại dương ($\beta_i R_M$)** + **Người ngồi trên thuyền $i$ tự rung lắc ($e_i$)**.
  - **(a) Tổng độ rung lắc của thuyền $i$ ($\sigma_i^2$):** Vì việc người trên thuyền tự rung ($e_i$) không liên quan gì đến sóng biển đại dương ($\text{Cov}(R_M, e_i)=0$), tổng độ rung bằng đúng $(\text{Độ rung do sóng biển } \beta_i^2\sigma_M^2) + (\text{Độ rung riêng trên thuyền } \sigma_{e,i}^2)$.
  - **(b) Độ nhấp nhô cùng nhịp giữa thuyền $i$ và thuyền $j$ ($\text{Cov}(R_i, R_j)$):** Người trên thuyền $i$ rung không liên quan đến người trên thuyền $j$ rung ($\text{Cov}(e_i, e_j)=0$). Vậy hai chiếc thuyền chỉ nhấp nhô cùng nhịp với nhau **duy nhất vì chúng cùng cưỡi trên một con sóng đại dương**: $\beta_i \times \beta_j \times \sigma_M^2$!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Khai triển $\text{Cov}(\beta_i R_M + e_i, \beta_j R_M + e_j)$ thành 4 số hạng, gạch bỏ 3 số hạng sau bằng $0$ nhờ giả định $\text{Cov}(R_M, e) = 0$ và $\text{Cov}(e_i, e_j) = 0$.

---

### Câu P12 (Lecture 09 — Trọng tâm 40% Derivatives): Prove the no-arbitrage forward price formula $F_{0,T} = [S_0 - PV(D)](1+r)^T$ for a dividend-paying stock by constructing a zero-cost portfolio table.
*(Chứng minh công thức giá kỳ hạn không arbitrage $F_{0,T} = [S_0 - PV(D)](1+r)^T$ cho cổ phiếu trả cổ tức bằng bảng danh mục chi phí bằng 0.)*

- **[Exam Model Answer — English (~85 words)]:**
  Suppose the stock pays a known dividend $D$ at $t_D < T$, with present value $PV(D)$. At $t=0$, construct a **zero-net-cash-flow** portfolio:
  1. **Buy 1 share** at $-S_0$.
  2. **Borrow $PV(D)$** at $+PV(D)$ (repaid exactly by the dividend $D$ received at $t_D$).
  3. **Borrow $S_0 - PV(D)$** until maturity $T$ at $+[S_0 - PV(D)]$.
  4. **Short 1 forward contract** at delivery price $F_{0,T}$ (cost $\$0$).
  At $t=0$, net cash flow is $-S_0 + PV(D) + [S_0 - PV(D)] = 0$. At $t=T$, the share is delivered into the short forward for $+F_{0,T}$, and the loan owed is $-[S_0 - PV(D)](1+r)^T$. Since a riskless, zero-cost trade must yield zero terminal cash flow:
  $$F_{0,T} - [S_0 - PV(D)](1+r)^T = 0 \implies F_{0,T} = [S_0 - PV(D)](1+r)^T$$

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Giả sử một con gà mái đẻ trứng hôm nay có giá **$S_0 = \$100$**. Bạn bè nhờ bạn mua hộ con gà này nhưng hẹn **1 năm sau mới nhận gà và trả tiền ($F_{0,1}$)**. Giữa năm, con gà sẽ đẻ 1 quả trứng vàng bán được tiền mặt quy về hôm nay là **$PV(D) = \$2$**:
  - Vì bạn giữ hộ con gà trong năm nay nên **bạn được hưởng quả trứng $\$2$ đó**, còn người bạn nhận gà vào cuối năm thì mất quả trứng đó.
  - Vậy thực chất hôm nay bạn chỉ phải bỏ ra số vốn gốc ròng cho phần "xác gà" là **$S_0 - PV(D) = \$100 - \$2 = \$98$** (còn $\$2$ kia bạn vay ngắn hạn rồi lấy tiền bán trứng giữa năm trả nợ là huề!).
  - Khoản vốn $\$98$ bỏ ra hôm nay nếu gửi ngân hàng lãi suất $r$ một năm sẽ nở thành **$\$98 \times (1+r)$**. Do đó, giá hẹn giao gà công bằng sau 1 năm bắt buộc phải là $F_{0,T} = [S_0 - PV(D)](1+r)^T$!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Nguyên lý **Cost-of-Carry**: Giá kỳ hạn $=$ (Giá giao ngay $-$ Giá trị hiện tại của lợi ích thu được trong kỳ) $\times$ Hệ số lãi vay tích lũy $(1+r)^T$.

---

### Câu P13 (Lecture 10 — Trọng tâm 40% Derivatives): State and prove European Put-Call Parity $C_0 + PV(K) = P_0 + S_0 - PV(D)$ using a two-state payoff table at expiration $T$.
*(Phát biểu và chứng minh Đẳng thức Quyền chọn Mua – Bán Châu Âu bằng bảng dòng tiền tại đáo hạn $T$.)*

- **[Exam Model Answer — English (~85 words)]:**
  Consider two European options with strike $K$ and maturity $T$ on a stock paying dividends with present value $PV(D)$:
  - **Portfolio A (Fiduciary Call):** Long 1 Call ($C_0$) + Lend cash $PV(K)$ at the risk-free rate.
  - **Portfolio B (Protective Put on ex-dividend stock):** Long 1 Put ($P_0$) + Buy 1 Share ($S_0$) + Borrow $PV(D)$ (repaid using the dividends).

  | Position | Cost at $t=0$ | Payoff at $T$ if $S_T \le K$ | Payoff at $T$ if $S_T > K$ |
  | :--- | :---: | :---: | :---: |
  | **Portfolio A:** Call + $PV(K)$ | $C_0 + PV(K)$ | $0 + K = K$ | $(S_T - K) + K = S_T$ |
  | **Portfolio B:** Put + Share $-$ $PV(D)$ | $P_0 + S_0 - PV(D)$ | $(K - S_T) + S_T = K$ | $0 + S_T = S_T$ |

  Since both portfolios yield $\max(S_T, K)$ in every state at $T$, the Law of One Price requires identical initial costs: $C_0 + PV(K) = P_0 + S_0 - PV(D)$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Làm sao để cuối năm bạn **luôn có trong tay thứ giá trị hơn giữa "1 Chiếc Xe Đạp ($S_T$)" và "$\$100$ Tiền Mặt ($K$)"** (tức là luôn nhận được $\max(S_T, \$100)$)? Có **2 cách mua sắm hôm nay** cho ra kết quả cuối năm giống hệt nhau 100%:
  - **Cách A (Tiền gửi + Phiếu Mua Xe giá $\$100$ — Fiduciary Call):** Hôm nay bạn bỏ ống heo gửi ngân hàng khoản tiền $PV(100)$ để cuối năm chắc chắn nở thành $\$100$, kèm theo **1 Phiếu được quyền mua xe giá $\$100$ (Call)**. Cuối năm: nếu xe rẻ hơn $\$100$, bạn vứt phiếu đi và cầm $\$100$ tiền mặt; nếu xe đắt hơn $\$100$ (ví dụ $\$150$), bạn lấy đúng $\$100$ trong ống heo ra đổi lấy chiếc xe $\$150$!
  - **Cách B (Mua Xe ngay + Phiếu Bảo Hiểm Bán Xe giá $\$100$ — Protective Put):** Hôm nay bạn **mua luôn chiếc xe ($S_0 - PV(D)$)**, kèm theo **1 Phiếu bảo hiểm được quyền bán lại chiếc xe với giá $\$100$ (Put)**. Cuối năm: nếu xe rớt giá xuống dưới $\$100$, bạn dùng phiếu bảo hiểm đổi chiếc xe lấy $\$100$ tiền mặt; nếu xe tăng lên $\$150$, bạn vứt phiếu bảo hiểm đi và giữ chiếc xe $\$150$!
  - Vì cả **Cách A** và **Cách B** đều giúp bạn cầm về đúng $\max(S_T, \$100)$ trong mọi trường hợp, nên **tổng tiền bỏ ra hôm nay của hai cách bắt buộc phải bằng nhau**: $C_0 + PV(K) = P_0 + S_0 - PV(D)$!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Portfolio A** $=$ *Fiduciary Call* ($C_0 + PV(K)$); **Portfolio B** $=$ *Protective Put* ($P_0 + S_0 - PV(D)$). Cả hai đều có payoff tại $T$ là **$\max(S_T, K)$**.

---

### Câu P14 (Lecture 10 — Trọng tâm 40% Derivatives): Prove the European Call Lower Bound $C_0 \ge \max(0, S_0 - PV(D) - PV(K))$ and European Put Lower Bound $P_0 \ge \max(0, PV(K) - S_0 + PV(D))$, and explain why a deep-ITM European Put can have negative time value ($P_0 < K - S_0$).
*(Chứng minh cận dưới không arbitrage của European Call và European Put, đồng thời giải thích tại sao một European Put ở trạng thái lời sâu có thể có giá trị thời gian âm $P_0 < K - S_0$.)*

- **[Exam Model Answer — English (~90 words)]:**
  Because options carry limited liability ($C_0 \ge 0, P_0 \ge 0$), rearranging Put-Call Parity $C_0 - P_0 = S_0 - PV(D) - PV(K)$ gives:
  - **Call Lower Bound:** Since $P_0 \ge 0$, $C_0 = [S_0 - PV(D) - PV(K)] + P_0 \ge S_0 - PV(D) - PV(K)$. Combining with $C_0 \ge 0$ yields $C_0 \ge \max\big(0, S_0 - PV(D) - PV(K)\big)$.
  - **Put Lower Bound:** Since $C_0 \ge 0$, $P_0 = [PV(K) - S_0 + PV(D)] + C_0 \ge PV(K) - S_0 + PV(D) \implies P_0 \ge \max\big(0, PV(K) - S_0 + PV(D)\big)$.
  For a deep-ITM European put ($S_0 \ll K$) with $r > 0$ and no dividends, $C_0 \approx 0$, so $P_0 \approx PV(K) - S_0 < K - S_0$: because the holder must wait until $T$ to receive the capped cash $K$, the lost interest $K - PV(K)$ exceeds the tiny upside insurance value $C_0$, creating **negative time value**.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Cách nhớ cận dưới trong 3 giây:** Từ phương trình $C_0 - P_0 = S_0 - PV(D) - PV(K)$, vì giá quyền chọn không bao giờ âm ($P_0 \ge 0$ và $C_0 \ge 0$), bỏ $P_0$ đi thì $C_0 \ge S_0 - PV(D) - PV(K)$; đảo dấu bỏ $C_0$ đi thì $P_0 \ge PV(K) - S_0 + PV(D)$!
  2. **Tại sao Deep-ITM European Put lại có giá rẻ hơn cả tiền lời thực hiện ngay ($P_0 < K - S_0$ — Negative Time Value)?**
     Giả sử một công ty đã phá sản khiến giá cổ phiếu hôm nay rơi về **$S_0 = \$0$**, và bạn đang cầm 1 quyền chọn bán Châu Âu cho phép bán cổ phiếu đó ở giá **$K = \$100$ nhưng phải đợi đúng 1 năm sau mới được nhận tiền**!
     - Nếu được đổi tiền ngay hôm nay, bạn có ngay $K - S_0 = \$100 - \$0 = \$100$ (*Intrinsic Value*).
     - Nhưng vì luật Châu Âu bắt bạn **phải chờ 1 năm sau mới đưa $\$100$** (và số tiền nhận được cũng không thể nào tăng quá $\$100$ vì giá cổ phiếu không thể âm!), nên tờ phiếu hẹn nhận $\$100$ sau 1 năm đó hôm nay chỉ đáng giá **$PV(100) = \frac{100}{1+r} < \$100$**! Bạn bị mất oan tiền lãi ngân hàng trong 1 năm chờ đợi, nên giá trị thời gian bị **âm**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Deep-ITM European Put bị kẹt chờ nhận số tiền trần $K$ tại $T \implies$ phần lãi suất mất đi $K - PV(K)$ lớn hơn giá trị bảo hiểm $C_0 \approx 0 \implies P_0 < K - S_0$ (*Negative time value*).

---

### Câu P15 (Lecture 10 — Trọng tâm MCQ & Tự luận ngắn): Prove that an American Call on a non-dividend-paying stock is NEVER optimally exercised before maturity when $r > 0$ ($C_A = C_E$), and state the condition for early exercise just before a dividend $D$.
*(Chứng minh quyền chọn Mua kiểu Mỹ trên cổ phiếu không trả cổ tức không bao giờ tối ưu khi thực hiện sớm với $r > 0$, và nêu điều kiện thực hiện sớm ngay trước ngày hưởng cổ tức $D$.)*

- **[Exam Model Answer — English (~90 words)]:**
  For a non-dividend-paying stock ($PV(D)=0$) with $r > 0$, $PV(K) < K$. By the European call lower bound and $C_A \ge C_E$:
  $$C_A \ge C_E = S_t - PV(K) + P_E > S_t - K \qquad (\text{since } K - PV(K) > 0 \text{ and } P_E \ge 0)$$
  Because the market value of the alive call ($C_A$) **strictly exceeds** its immediate exercise value ($S_t - K$) at every date $t < T$, exercising early destroys both: (1) the time value of money saved by deferring payment of $K$ ($K - PV(K)$), and (2) the downside protection ($P_E$). Hence, an investor is always better off **selling** the call than exercising it early, so **$C_A = C_E$**.
  With a discrete dividend $D$, early exercise just before the ex-dividend date is optimal only if $D > [K - PV(K)] + P_{\text{ex}}$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Tưởng tượng bạn có một **Phiếu giữ chỗ mua chiếc iPhone với giá cố định $K = \$1,000$ vào cuối năm**, trong khi chiếc iPhone ngoài tiệm hôm nay đã tăng lên **$S_t = \$1,200$** (và chiếc iPhone để trong tiệm không đẻ thêm phụ kiện hay tiền cổ tức gì cả). Tại sao bạn **KHÔNG BAO GIỜ nên mang $\$1,000$ ra đổi lấy chiếc iPhone ngay hôm nay**?
  1. **Lợi ích 1 (Giữ tiền trong ngân hàng ăn lãi):** Đằng nào cuối năm bạn cũng chắc chắn mua được chiếc iPhone với giá $\$1,000$. Nếu trả $\$1,000$ ngay hôm nay, bạn mất toi tiền lãi ngân hàng $K - PV(K)$ của khoản $\$1,000$ đó từ nay đến cuối năm!
  2. **Lợi ích 2 (Bảo hiểm lỡ iPhone rớt giá — $P_E$):** Nếu bạn đổi lấy chiếc iPhone ngay hôm nay rồi tuần sau hãng giảm giá iPhone xuống còn $\$800$, bạn lỗ nặng $\$200$! Còn nếu bạn cứ cầm tờ phiếu trong tay, lỡ iPhone rớt xuống $\$800$ thì bạn chỉ việc vứt tờ phiếu đi và không mất đồng nào!
  3. **Vậy nếu bạn cần tiền ngay hôm nay thì sao?** Thay vì xé phiếu đổi iPhone (chỉ thu được $1,200 - 1,000 = \$200$), bạn **bán lại tờ phiếu còn sống đó cho người khác** với giá $C_A = \$200 + (\text{Lãi ngân hàng}) + (\text{Bảo hiểm } P_E) > \$200$!
  - **Khi nào mới chịu đổi sớm?** Chỉ khi cửa hàng thông báo: *"Ai cầm iPhone thật vào sáng mai sẽ được tặng ngay một phong bao lì xì tiền mặt $D$ cực lớn!"* — nếu phong bao lì xì $D$ lớn hơn cả tiền lãi ngân hàng cộng tiền bảo hiểm ($D > [K - PV(K)] + P_{\text{ex}}$), bạn mới đổi ngay trước giờ phát lì xì!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Khẩu quyết: **"Worth more alive ($C_A$) than dead ($S_t - K$)"** vì tiết kiệm được **interest on strike $K - PV(K)$** và giữ được **downside put protection $P_E$**.

---

### Câu P16 (Lecture 10 & Extra Session): In Merton's structural model of a levered firm with assets $V_T$ and zero-coupon debt face value $K$ due at $T$, prove how Equity and Risky Debt can be expressed using European Call and Put options on firm assets.
*(Trong mô hình cấu trúc Merton của công ty có nợ zero-coupon mệnh giá $K$, hãy chứng minh cách biểu diễn Vốn chủ sở hữu và Nợ rủi ro thông qua quyền chọn Mua và Bán Châu Âu trên tài sản công ty.)*

- **[Exam Model Answer — English (~85 words)]:**
  At debt maturity $T$, limited liability gives shareholders the residual claim $E_T = \max(V_T - K, 0)$, which is identical to a **European call option on firm assets $V$** with strike $K$:
  $$E_0 = C_0(V_0, K, T, \sigma_V)$$
  Bondholders receive $D_T = \min(V_T, K)$, which can be decomposed in two equivalent ways:
  1. **Covered Call view:** $D_T = V_T - \max(V_T - K, 0) \implies D_0 = V_0 - E_0$ (owning the firm's assets while writing a call at strike $K$ to shareholders).
  2. **Default Put view:** $D_T = K - \max(K - V_T, 0) \implies D_0 = PV(K) - P_0(V_0, K, T, \sigma_V)$ (lending risk-free $PV(K)$ while writing a European put option to shareholders).
  Equating the two gives firm Put-Call Parity: $V_0 = E_0 + PV(K) - P_0$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng các Cổ đông vay của Ngân hàng **$K = \$120\text{ triệu}$** để mua một nhà máy trị giá **$V_0 = \$150\text{ triệu}$**, hẹn 2 năm sau trả nợ, với luật **Trách nhiệm hữu hạn (Limited Liability — nếu nhà máy lỗ thì cổ đông chỉ mất nhà máy chứ không phải bán nhà riêng đi đền)**:
  1. **Góc nhìn của Cổ đông (Equity = Call Option):** Thực chất cổ đông đã tạm giao sổ đỏ nhà máy cho Ngân hàng giữ làm tin, và cầm một **Phiếu được quyền chuộc lại nhà máy với giá $\$120\text{ triệu}$ (Call option)**. Sau 2 năm: nếu nhà máy trị giá $\$200\text{ triệu}$, cổ đông trả $\$120\text{ triệu}$ chuộc nhà máy về và ăn trọn $\$80\text{ triệu}$; nếu nhà máy cháy chỉ còn $\$90\text{ triệu}$, cổ đông bỏ đi tay trắng ($\$0$), để mặc Ngân hàng tự ôm cái nhà máy $\$90\text{ triệu}$!
  2. **Góc nhìn của Ngân hàng cho vay (Risky Debt = Risk-Free Loan $-$ Put Option):** Ngân hàng cứ tưởng mình cho vay an toàn $\$120\text{ triệu}$, nhưng thực chất Ngân hàng đã **tặng không cho cổ đông một Phiếu Bảo Hiểm Vỡ Nợ (Default Put option)**: hễ nhà máy tụt xuống dưới $\$120\text{ triệu}$ (ví dụ còn $\$90\text{ triệu}$), cổ đông được quyền "bán đứt" cái nhà máy $\$90\text{ triệu}$ đó cho Ngân hàng để xóa khoản nợ $\$120\text{ triệu}$ (Ngân hàng chịu khoản lỗ $\max(K - V_T, 0) = \$30\text{ triệu}$)!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - $E_0 = \text{Call}(V_0, K)$ và $D_0 = V_0 - E_0 = PV(K) - \text{Put}(V_0, K)$.

---

### Câu P17 (Lecture 11 — Trọng tâm 40% Derivatives): Derive the 1-period Binomial Replicating Portfolio $(\Delta, B)$ and Risk-Neutral Probability $p = \frac{r-d}{u-d}$, and prove why $0 < d < r < u$ is required for no-arbitrage.
*(Chứng minh công thức danh mục mô phỏng 1 kỳ $(\Delta, B)$, xác suất trung hòa rủi ro $p = \frac{r-d}{u-d}$, và chứng minh tại sao điều kiện không arbitrage đòi hỏi $0 < d < r < u$.)*

- **[Exam Model Answer — English (~90 words)]:**
  To replicate option payoffs $(V_u, V_d)$ at $t=1$ using $\Delta$ shares and risk-free cash $B$ (with gross rate factor $r = 1 + r_f$), we equate terminal values in both states:
  $$\begin{cases} \Delta (uS_0) + rB = V_u \\ \Delta (dS_0) + rB = V_d \end{cases} \implies \Delta = \frac{V_u - V_d}{(u - d)S_0}, \qquad B = \frac{uV_d - dV_u}{r(u - d)}$$
  By no-arbitrage, the option value today equals replication cost $V_0 = \Delta S_0 + B$:
  $$V_0 = \frac{V_u - V_d}{u - d} + \frac{uV_d - dV_u}{r(u - d)} = \frac{1}{r}\left[\left(\frac{r - d}{u - d}\right)V_u + \left(\frac{u - r}{u - d}\right)V_d\right] = \frac{pV_u + (1 - p)V_d}{r}$$
  where $p = \frac{r - d}{u - d}$. **No-arbitrage requires $d < r < u$** ($0 < p < 1$): if $r \le d$, borrowing at $r$ to buy the stock dominates cash in every state; if $r \ge u$, shorting the stock to lend at $r$ dominates in every state.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Tại sao $\Delta = \frac{V_u - V_d}{S_u - S_d}$?** Giả sử cuối năm nếu cổ phiếu lên $\$120$ ($S_u$) hay xuống $\$90$ ($S_d$) — chênh nhau **$\$30$** — thì quyền chọn Mua nhận được $\$20$ ($V_u$) hoặc $\$0$ ($V_d$) — chênh nhau **$\$20$**. Vì tiền mặt gửi ngân hàng ($rB$) không hề thay đổi theo giá cổ phiếu, nên để tạo ra độ chênh $\$20$ của quyền chọn từ độ chênh $\$30$ của cổ phiếu, bạn chỉ cần mua đúng **$\Delta = \frac{20}{30} = \frac{2}{3}$ cổ phiếu**! Phần tiền còn thiếu bao nhiêu thì bù bằng tiền vay ngân hàng $B$.
  2. **Tại sao bắt buộc $d < r < u$?**
     - Nếu ngân hàng trả lãi $r = 5\%$, mà cổ phiếu ngay cả khi **xui xẻo nhất ($d$) vẫn tăng $+10\%$** ($d \ge r$): thế thì ai thèm gửi tiết kiệm nữa? Mọi người sẽ vay sạch tiền ngân hàng lãi $5\%$ để mua cổ phiếu ăn ít nhất $10\%$ (**Máy in tiền không rủi ro!**).
     - Ngược lại, nếu cổ phiếu ngay cả khi **may mắn nhất ($u$) chỉ tăng $+2\%$** mà ngân hàng trả lãi chắc chắn $5\%$ ($r \ge u$): mọi người sẽ bán khống sạch cổ phiếu để gửi ngân hàng! Do đó, lãi suất ngân hàng $r$ bắt buộc phải **nằm kẹp ở giữa mức giảm $d$ và mức tăng $u$ ($d < r < u$)**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Trừ vế theo vế hệ 2 phương trình $\Delta S_u + rB = V_u$ và $\Delta S_d + rB = V_d$ để khử $rB$ tìm $\Delta$ trước, rồi rút $B$ và gom hệ số của $V_u, V_d$ thành $p = \frac{r-d}{u-d}$.

---

### Câu P18 (Lecture 11 & Extra Session — Trọng tâm 40% Derivatives): Prove that dynamic delta-hedging in a multi-period binomial tree is self-financing at intermediate nodes, and derive the Option Beta formula $\beta_{\text{opt}} = \frac{S\Delta}{V}\beta_S$.
*(Chứng minh chiến lược phòng vệ động Delta trên cây nhị phân nhiều kỳ có tính tự tài trợ tại các nút trung gian, và chứng minh công thức Beta quyền chọn $\beta_{\text{opt}} = \frac{S\Delta}{V}\beta_S$.)*

- **[Exam Model Answer — English (~90 words)]:**
  1. **Self-Financing Property:** At $t=0$, the replicating portfolio $(\Delta_0, B_0)$ is chosen specifically so that its value at $t=1$ in node $u$ matches the option's continuation value $V_u$:
     $$W_u^{\text{old}} = \Delta_0 S_u + r B_0 = V_u$$
     At node $u$, the new replicating portfolio $(\Delta_u, B_u)$ required to replicate $(V_{uu}, V_{ud})$ at $t=2$ has cost $W_u^{\text{new}} = \Delta_u S_u + B_u = V_u$. Therefore, net cash injection required at node $u$ is $W_u^{\text{new}} - W_u^{\text{old}} = V_u - V_u = 0$ (any extra shares $\Delta_u - \Delta_0$ are financed entirely by adjusting $B$).
  2. **Option Beta:** Since the option is locally replicated by a portfolio of stock (weight $w_S = \frac{S\Delta}{V}$) and risk-free cash (weight $w_B = \frac{B}{V}$ with $\beta_B = 0$):
     $$\beta_{\text{opt}} = w_S \beta_S + w_B \beta_B = \left(\frac{S\Delta}{V}\right)\beta_S = \Omega \beta_S$$

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Tại sao đổi danh mục ở giữa đường lại không tốn thêm 1 xu tiền túi nào (Self-financing)?**
     Giống như bạn xếp một bộ Lego trị giá $\$20$ tại năm 1 ($V_u = \$20$). Lúc đầu năm 0 bạn đã chuẩn bị sẵn một giỏ gồm $\Delta_0$ mảnh ghép và $B_0$ tiền lẻ sao cho khi bước sang nút $u$, tổng giá trị giỏ đồ cũ của bạn vừa khít bằng **$\$20$** ($\Delta_0 S_u + rB_0 = V_u$). Bây giờ để đi tiếp sang năm 2, bạn cần xếp lại thành một giỏ mới $(\Delta_u, B_u)$ cũng có tổng giá trị đúng bằng **$\$20$** ($\Delta_u S_u + B_u = V_u$). Nếu bạn cần mua thêm vài mảnh ghép ($\Delta_u > \Delta_0$), bạn chỉ việc rút tiền trong ngăn tiền lẻ $B$ ra trả (hoặc vay thêm vào $B$), **tổng giá trị giỏ trước và sau khi đổi đều là $\$20$ nên bạn không phải xin thêm tiền bố mẹ ($\$0$ net cash flow)**!
  2. **Tại sao $\beta_{\text{opt}} = \frac{S\Delta}{V}\beta_S$?**
     Giả sử cổ phiếu có giá $S = \$100$ ($\beta_S = 1$), còn quyền chọn Mua chỉ tốn $V = \$10$ nhưng được cấu tạo từ $\Delta = 0.60$ cổ phiếu (trị giá $S\Delta = \$60$) trừ đi khoản tiền vay $B = -\$50$ ($\beta_B = 0$). Bỏ ra có $\$10$ tiền vốn mà bạn đang cầm tới $\$60$ cổ phiếu $\implies$ **đòn bẩy của bạn gấp $\Omega = \frac{60}{10} = 6$ lần cổ phiếu**, nên độ nhạy cảm với thị trường ($\beta_{\text{opt}}$) cũng phóng đại gấp $6$ lần ($\beta_{\text{opt}} = 6 \times \beta_S$)!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Hai dòng toán học ăn điểm tuyệt đối: (1) $W_u^{\text{old}} = \Delta_0 S_u + rB_0 = V_u = \Delta_u S_u + B_u = W_u^{\text{new}}$; (2) $\beta_{\text{opt}} = \frac{S\Delta}{V}\beta_S + \frac{B}{V}(0) = \Omega\beta_S$.


---

## PHẦN III: 15 CÂU HỎI PHẢN BIỆN & PHÂN BIỆT KHÁI NIỆM (CONCEPTUAL CRITIQUE & DISTINCTIONS)

### Câu C1 (Lecture 06): Compare the Capital Market Line (CML) and the Security Market Line (SML) across axes, risk measures, applicability, and equilibrium pricing implications.
*(So sánh Đường Thị trường Vốn CML và Đường Thị trường Chứng khoán SML về hệ trục, thước đo rủi ro, phạm vi áp dụng và ý nghĩa định giá.)*

- **[Exam Model Answer — English (~85 words)]:**
  | Feature | Capital Market Line (CML) | Security Market Line (SML) |
  | :--- | :--- | :--- |
  | **Equation** | $E(r_P) = r_f + \frac{E(r_M) - r_f}{\sigma_M}\sigma_P$ | $E(r_i) = r_f + \beta_i[E(r_M) - r_f]$ |
  | **Horizontal Axis (Risk)** | **Total standard deviation ($\sigma_P$)** | **Systematic risk ($\beta_i$)** |
  | **Scope of Assets** | **Efficient portfolios ONLY** (combinations of $r_f$ and $M$) | **ALL individual securities and portfolios** |
  | **Off-line Interpretation** | Individual stocks with $\sigma_e > 0$ always lie **below** the CML even when fairly priced. | In equilibrium, all fairly priced assets lie **on** the SML; above SML = underpriced ($\alpha > 0$), below SML = overpriced ($\alpha < 0$). |

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng nhà trường có **2 Bảng Chấm Điểm** khác nhau:
  1. **Bảng CML (Bảng Xếp Hạng Tập Thể Đỉnh Cao — Trục hoành là Tổng Rủi Ro $\sigma$):** Chỉ dành riêng cho các **"Đội tuyển hoàn hảo" (Efficient Portfolios)** không hề lãng phí một giọt mồ hôi thừa nào ($\sigma_e = 0$). Một cá nhân đơn lẻ ($i$) vì luôn có những sai sót vặt vãnh của riêng mình ($\sigma_{e,i} > 0$) nên tổng độ mệt mỏi $\sigma_i$ bị phình to ra $\implies$ cá nhân lẻ **luôn đứng tụt về bên phải/phía dưới bảng CML**, dù bạn ấy chẳng làm gì sai cả!
  2. **Bảng SML (Bảng Tính Lương Công Bằng Cho Mọi Người — Trục hoành là Đóng Góp Chung $\beta$):** Dùng để trả lương cho **tất cả mọi cá nhân lẫn tập thể**. Bảng này chỉ đo phần công sức đóng góp vào việc chung của tập thể ($\beta_i$), không phạt lỗi vặt riêng ($\sigma_{e,i}$). Nếu tất cả được trả lương công bằng, **mọi cá nhân đều phải nằm đúng trên đường thẳng SML**! Ai nằm **trên** SML ($\alpha > 0$) là món hời đang bị trả giá quá rẻ (**Underpriced $\to$ Mua!**).

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **CML:** Trục hoành $\sigma_P$, chỉ dành cho *Efficient portfolios*; cổ phiếu lẻ có $\sigma_e > 0$ luôn nằm dưới CML.
  - **SML:** Trục hoành $\beta_i$, áp dụng cho *All individual assets & portfolios*; dùng để xét *Underpriced ($\alpha > 0$) vs. Overpriced ($\alpha < 0$)*.

---

### Câu C2 (Lecture 06 & Practice L01–L07 Q83–Q85): An analyst finds a single stock with positive CAPM alpha ($\alpha_i > 0$) and claims: "By buying this stock and shorting $\beta_i$ units of the market portfolio, I can lock in a risk-free arbitrage profit." Critique this claim.
*(Một nhà phân tích tìm thấy một cổ phiếu lẻ có $\alpha_i > 0$ và tuyên bố: "Bằng cách mua cổ phiếu này và bán khống $\beta_i$ đơn vị danh mục thị trường, tôi khóa được lợi nhuận arbitrage phi rủi ro." Hãy phản biện tuyên bố này.)*

- **[Exam Model Answer — English (~75 words)]:**
  The analyst's claim is **incorrect**. In the Single-Index Model, the excess return of stock $i$ is $R_i = \alpha_i + \beta_i R_M + e_i$. Buying $1$ unit of stock $i$ and shorting $\beta_i$ units of the market portfolio yields net excess return:
  $$R_{\text{hedged}} = R_i - \beta_i R_M = \alpha_i + e_i$$
  While this market-neutral position eliminates systematic market risk ($\beta_{\text{net}} = 0$) and has positive expected return $\alpha_i > 0$, its variance is **$\text{Var}(R_{\text{hedged}}) = \sigma^2(e_i) > 0$**. Because firm-specific (idiosyncratic) risk $e_i$ remains, it is a risky active bet (Treynor-Black), **not** a risk-free arbitrage.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Tưởng tượng bạn phát hiện một tiệm bánh ngoài phố bán rẻ hơn bình thường **$\alpha_i = +\$2/\text{hộp}$**. Để tránh rủi ro "trời mưa cả thành phố vắng khách ($\beta_i R_M$)", bạn mua một hợp đồng bảo hiểm thời tiết vừa khít để **khử sạch rủi ro thời tiết ($\beta_{\text{net}} = 0$)**:
  - Vậy bạn đã chắc chắn $100\%$ bỏ túi $\$2$ mà **không có bất kỳ rủi ro nào** chưa? **CHƯA HỀ!**
  - Nhỡ đâu ngày mai **đầu bếp của riêng tiệm bánh đó bị ốm hoặc lò nướng của tiệm bị cháy ($e_i = -\$10$)** thì sao?! Bảo hiểm thời tiết chung của thành phố đâu có đền cho việc lò nướng riêng của tiệm đó bị cháy!
  - Vì bạn chỉ mua **1 tiệm bánh đơn lẻ**, bạn vẫn chịu nguyên **rủi ro tai nạn riêng của tiệm đó ($\sigma^2(e_i) > 0$)** — nên đây chỉ là một vụ đặt cược có lợi thế (*active bet*), **không phải** tiền miễn phí chắc chắn $100\%$ (*risk-free arbitrage*)!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Viết phương trình $R_{\text{hedged}} = R_i - \beta_i R_M = \alpha_i + e_i \implies \text{Var}(R_{\text{hedged}}) = \sigma^2(e_i) > 0$ (*Firm-specific / idiosyncratic risk remains*).

---

### Câu C3 (Lecture 06): Explain why an investor holding a single-index market portfolio $M$ evaluates a candidate active stock using its Information Ratio ($\alpha_i / \sigma_{e,i}$) rather than its standalone Sharpe Ratio.
*(Giải thích tại sao nhà đầu tư đang nắm giữ danh mục thị trường $M$ lại đánh giá một cổ phiếu chủ động bằng Information Ratio $\alpha_i / \sigma_{e,i}$ thay vì Sharpe Ratio độc lập của nó.)*

- **[Exam Model Answer — English (~75 words)]:**
  By the **Treynor-Black model**, when an active asset $A$ is combined with the passive market portfolio $M$, the squared Sharpe ratio of the optimal combined portfolio $P$ is:
  $$S_P^2 = S_M^2 + \left(\frac{\alpha_A}{\sigma(e_A)}\right)^2 = S_M^2 + \text{IR}_A^2$$
  Because the investor can freely adjust systematic market exposure $\beta_A$ by trading the market index $M$, the active stock's systematic risk $\beta_A\sigma_M$ does not constrain performance. The marginal contribution to portfolio Sharpe ratio depends solely on abnormal return $\alpha_A$ relative to the non-diversifiable idiosyncratic noise $\sigma(e_A)$ introduced into the portfolio.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Giả sử bạn đã có sẵn một **Nồi canh chuẩn vị ($M$)**. Bây giờ bạn muốn chọn thêm **1 lọ gia vị bí mật ($A$)** để rắc thêm vào nồi canh cho đậm đà hơn:
  - Khi rắc lọ gia vị $A$ vào nồi canh lớn, bạn cần quan tâm điều gì?
  - Phần **muối cơ bản ($\beta_A$)** có trong lọ gia vị không quan trọng, vì nếu hơi mặn bạn chỉ việc bớt muối ở nồi canh chính đi là xong!
  - Thứ duy nhất quyết định lọ gia vị đó có đáng cho vào nồi canh hay không là: **"Hương thơm đặc biệt mà nó mang lại ($\alpha_A$) chia cho lượng sạn cát riêng mà nó làm bẩn nồi canh ($\sigma(e_A)$)"** — tỷ số đó chính là **Information Ratio ($\text{IR}_A = \frac{\alpha_A}{\sigma(e_A)}$)**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Công thức Treynor-Black: $S_P^2 = S_M^2 + \left[\frac{\alpha_A}{\sigma(e_A)}\right]^2 = S_M^2 + \text{IR}_A^2$.

---

### Câu C4 (Lecture 06 & Extra Session Cell 13): Explain how an asset (such as a gold mining stock or a European put option) can have an equilibrium expected return BELOW the risk-free rate ($E(r_i) < r_f$, or even negative) without violating CAPM.
*(Giải thích làm thế nào một tài sản như quyền chọn bán Châu Âu lại có thể có tỷ suất sinh lời kỳ vọng cân bằng THẤP HƠN lãi suất phi rủi ro $r_f$, thậm chí âm, mà vẫn hoàn toàn tuân theo CAPM.)*

- **[Exam Model Answer — English (~75 words)]:**
  Under CAPM, $E(r_i) = r_f + \beta_i[E(r_M) - r_f]$, where $E(r_M) - r_f > 0$. An asset with **negative beta ($\beta_i < 0$)**—such as a European put option on a positive-beta stock, where $\beta_P = \frac{S\Delta_P}{P}\beta_S < 0$ because $\Delta_P < 0$—covaries negatively with the aggregate market.
  Because such an asset pays off handsomely during market crashes (recessions) when marginal utility of wealth is highest, it acts as **portfolio insurance**. Risk-averse investors willingly accept $E(r_i) < r_f$ (an insurance premium cost) for this crash-hedging benefit.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy nghĩ đến **Bảo hiểm cháy nhà (hoặc Quyền chọn Bán — Put option)**:
  - Trung bình mỗi năm, người mua bảo hiểm cháy nhà có "lãi" tiền mặt không? **KHÔNG!** Trung bình bạn đóng $\$100$ tiền phí nhưng chỉ nhận lại kỳ vọng $\$70$ (tức tỷ suất sinh lời kỳ vọng **âm $-30\% < r_f$**)!
  - Tại sao bạn biết lỗ trung bình mà vẫn vui vẻ mua? Vì tờ giấy bảo hiểm trả tiền cho bạn **đúng vào lúc ngôi nhà của bạn bị cháy rụi (thị trường sụp đổ — $\beta < 0$)**, khi mà $\$1$ tiền cứu trợ quý giá gấp chục lần lúc bình thường! Vì nó giúp giảm mạnh rủi ro của cả gia đình, mọi người sẵn sàng chấp nhận lợi suất kỳ vọng thấp hơn lãi ngân hàng $r_f$ (thậm chí âm)!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - $\beta_i < 0 \implies E(r_i) = r_f + \beta_i[E(r_M) - r_f] < r_f$ vì tài sản đóng vai trò **crash insurance / recession hedge**.

---

### Câu C5 (Lecture 07 & Practice L01–L07 Q97): Explain why a long-only "Smart Beta" Value ETF is NOT equivalent to the academic Fama-French HML factor, and why a statistically positive sample alpha may not prove active stock-picking skill.
*(Giải thích tại sao một quỹ ETF Smart Beta Giá trị chỉ mua (long-only) không tương đương với nhân tố HML học thuật của Fama-French, và tại sao hệ số alpha dương trong mẫu chưa chắc chứng minh được kỹ năng chọn cổ phiếu.)*

- **[Exam Model Answer — English (~85 words)]:**
  1. **Long-only ETF vs. Academic HML:** The academic Fama-French **HML** factor is a **zero-investment, market-neutral long–short portfolio** ($\beta_M \approx 0$) that buys high book-to-market stocks and shorts low book-to-market growth stocks. By contrast, a Smart Beta Value ETF is a **long-only fund** with full market exposure ($\beta_M \approx 1$), management fees, and tracking error.
  2. **Sample Alpha vs. True Skill:** Because a Smart Beta ETF follows transparent, mechanical index rules rather than discretionary research, a positive sample $\hat{\alpha}$ under FF3 usually reflects **omitted factor exposures** (e.g., profitability RMW, investment CMA, or momentum MOM) or random sample luck rather than stock-picking skill.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Sự khác biệt giữa "Nước cốt chanh nguyên chất (`HML` học thuật)" và "Nước lọc pha thêm chanh (`Smart Beta ETF`)":**
     - Nhân tố `HML` của Fama-French là **mua cổ phiếu Giá trị đồng thời bán khống cổ phiếu Tăng trưởng** để lọc bỏ hoàn toàn biến động của thị trường chung ($\beta_M \approx 0$ — giống như chắt lấy vị chua nguyên chất!).
     - Còn quỹ `Smart Beta Value ETF` ngoài đời chỉ được phép **mua cổ phiếu chứ không được bán khống (Long-only)**, nên $90\%$ biến động của nó vẫn là trôi nổi theo thị trường chứng khoán chung ($\beta_M \approx 1$), cộng thêm phí quản lý.
  2. **Tại sao máy chấm điểm FF3 báo có điểm thưởng $\hat{\alpha} = +0.20\%$ mà vẫn không phải do người quản lý giỏi?** Vì quỹ ETF chạy tự động bằng máy tính theo công thức công khai! Điểm $\hat{\alpha}$ thừa ra đó chỉ là do máy chấm FF3 **chưa tính đến các phẩm chất khác vô tình có sẵn trong rổ cổ phiếu** (như lợi nhuận tốt `RMW`, đầu tư tiết kiệm `CMA` trong mô hình FF5).

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Academic HML:** Dollar-neutral, market-neutral Long–Short portfolio ($\beta_M \approx 0$).
  - **Smart Beta ETF:** Long-only ($\beta_M \approx 1$), mechanical rule-based; positive $\hat{\alpha}$ reflects **omitted factors (RMW, CMA, MOM)** or sample noise.

---

### Câu C6 (Lecture 08 & Practice L08–L11 Q1, Q3): Explain why (a) a mutual fund earning $14\%$ when the market earned $10\%$ over one year does NOT refute Weak-Form EMH, and (b) a corporate insider profiting from confidential merger news refutes Strong-Form EMH but NOT Semi-Strong-Form EMH.
*(Giải thích tại sao: (a) một quỹ đạt lợi suất $14\%$ khi thị trường đạt $10\%$ trong 1 năm không bác bỏ EMH dạng yếu, và (b) người nội bộ kiếm lời từ tin sáp nhập mật chỉ bác bỏ EMH dạng mạnh chứ không bác bỏ dạng bán mạnh.)*

- **[Exam Model Answer — English (~85 words)]:**
  - **(a) Raw 1-year outperformance vs. Weak-Form EMH:** First, raw returns are **not risk-adjusted**—the fund may simply hold higher systematic risk ($\beta_P > 1$ or small/value tilts). Second, in a volatile market, a single year of outperformance is statistically indistinguishable from **random luck** (sampling variation). Third, Weak-Form EMH specifically tests whether *past price/volume patterns* predict abnormal returns.
  - **(b) Insider profits vs. Semi-Strong/Strong EMH:** Confidential merger negotiations are **private information**. Profiting from non-public information directly violates **Strong-Form EMH** (which encompasses all public and private information) but is completely consistent with **Semi-Strong-Form EMH** (which only requires prices to reflect **publicly available** information).

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  - **Ý (a):** Một bạn khoe: *"Năm nay tớ kiếm được $14\%$ trong khi cả lớp kiếm được $10\%$, chứng tỏ thị trường không hiệu quả!"* $\implies$ Khoan đã! Có 2 lý do khiến lời khoe đó vô giá trị:
    1. **Bạn ấy liều mạng hơn (Chưa điều chỉnh rủi ro $\beta$):** Khi thị trường tăng $10\%$, một người đi vay tiền đánh cược gấp rưỡi ($\beta = 1.5$) đương nhiên phải kiếm được khoảng $14\%$! Đến năm thị trường sập thì bạn ấy cũng lỗ gấp rưỡi!
    2. **Tung đồng xu ăn may 1 lần (Random luck):** Cho 1,000 người tung đồng xu thì kiểu gì sau 1 năm cũng có hàng trăm người thắng chỉ nhờ may mắn ngẫu nhiên!
  - **Ý (b):** Giám đốc biết trước **bí mật trong phòng họp kín** rồi mua cổ phiếu kiếm lời $\implies$ điều này chỉ chứng tỏ **"Bí mật phòng kín chưa nằm trong giá" (bác bỏ Strong-Form EMH)**, chứ không hề phủ nhận việc **"Tin tức đã đăng lên báo đều đã nằm trong giá" (Semi-Strong-Form EMH vẫn đúng nguyên!)**.

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - 3 từ khóa cho (a): **Lack of risk adjustment ($\beta$)**, **1-year random luck / sampling noise**, **not derived from past price data**.
  - 2 từ khóa cho (b): Confidential news is **private information** $\implies$ refutes **Strong-form**, consistent with **Semi-strong-form**.

---

### Câu C7 (Lecture 08 & Practice L08–L11 Q4): Distinguish between "Loss Aversion / Disposition Effect" and "Mental Accounting / House-Money Effect" in behavioral finance, and state how each harms investor wealth.
*(Phân biệt "Ác cảm thua lỗ / Hiệu ứng Bán non lời - Giữ khư khư lỗ" với "Kế toán Tâm lý / Hiệu ứng Tiền chùa" trong tài chính hành vi và nêu tác hại của từng thiên lệch.)*

- **[Exam Model Answer — English (~85 words)]:**
  1. **Prospect Theory Loss Aversion & Disposition Effect:** Under Kahneman and Tversky's Prospect Theory, the value function is concave over gains (risk-averse) and convex/steeper over losses (risk-seeking to avoid realizing a loss). This causes the **Disposition Effect**: investors sell winning stocks too early ("locking in gains") and hold losing stocks too long ("hoping to break even"), which increases capital-gains taxes and underperforms momentum.
  2. **Mental Accounting & House-Money Effect:** Investors segregate wealth into separate mental buckets rather than treating money as **fungible**, taking excessive, uncompensated risks with recent windfall gains ("playing with the house's money") and violating unified portfolio optimization.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Disposition Effect ("Trồng hoa nhưng nhổ bỏ cây hoa tươi để giữ lại cây cỏ dại"):**
     Vì con người **sợ cảm giác phải thừa nhận mình sai (Loss Aversion)** gấp đôi niềm vui khi thắng: hễ cổ phiếu nào vừa tăng lời một chút là vội vàng bán ngay vì sợ nó tụt mất (*"chốt lời cho chắc"*), còn cổ phiếu nào đang lỗ nát bét thì lại ôm khư khư không dám bán (*"chờ bao giờ về bờ mới bán"*). Kết quả: giữ lại toàn cổ phiếu yếu kém trong giỏ và phải đóng thuế sớm cho cổ phiếu lời!
  2. **Mental Accounting & House-Money Effect ("Chia tiền vào các túi quần khác nhau & Tiêu hoang tiền trúng thưởng"):**
     Tờ $\$100$ tiền lương vất vả làm ra và tờ $\$100$ vừa trúng xổ số có giá trị mua sắm **giống hệt nhau (Fungible)**. Nhưng nhiều người lại chia não mình thành 2 ngăn riêng (**Mental Accounting**): ngăn "tiền lương" thì giữ khư khư cực kỳ nhát gan, còn ngăn "tiền vừa lãi/trúng thưởng" thì coi là **"tiền chùa của sòng bạc" (House-Money Effect)** rồi đem ném vào các trò đầu cơ cực kỳ rủi ro!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Disposition Effect:** Concave over gains, convex over losses relative to purchase-price reference point $\implies$ sell winners too soon, hold losers too long.
  - **Mental Accounting / House-Money Effect:** Violates **fungibility of wealth** across mental accounts.

---

### Câu C8 (Lecture 09 & Practice L08–L11 Q10): Explain why the Cost-of-Carry relation for a consumption commodity with convenience yield $y$ can allow backwardation ($F_{0,T} < S_0$), and why "Reverse Cash-and-Carry" arbitrage often fails when $F_{\text{mkt}} < [S_0 + PV(U)](1+r)^T$.
*(Giải thích tại sao mô hình Cost-of-Carry cho hàng hóa tiêu dùng có lợi ích nắm giữ $y$ cho phép trạng thái bù hoãn bán $F_{0,T} < S_0$, và tại sao chiến lược Reverse Cash-and-Carry thường thất bại khi giá kỳ hạn thấp hơn mức lưu kho thuần túy.)*

- **[Exam Model Answer — English (~85 words)]:**
  For a physical consumption commodity (e.g., crude oil, copper, wheat), holding physical inventory provides a **convenience yield ($y$)**—the operational benefit of preventing production shutdowns during supply shortages—which a paper forward contract does not provide. Under continuous compounding (with storage cost $u$):
  $$F_{0,T} = S_0 e^{(r + u - y)T}$$
  When inventory is scarce, the convenience yield exceeds financing plus storage costs ($y > r + u$), driving the market into **backwardation ($F_{0,T} < S_0$)**.
  **Reverse Cash-and-Carry** (short physical spot + long forward) fails to raise $F_{0,T}$ because industrial users refuse to lend or sell out of strategic physical inventories without give-up compensation $y$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng giữa mùa đông bão tuyết, **1 bình củi đốt sưởi ấm ngay tối nay ($S_0$)** có giá **$\$100$**, trong khi **tờ giấy hẹn giao củi vào mùa hè sang năm ($F_{0,T}$)** chỉ có giá **$\$70$ ($F_{0,T} < S_0$ — Backwardation)**:
  - Tại sao tờ giấy hẹn giao củi lại rẻ hơn củi thật tới $\$30$? Vì **cầm tờ giấy hẹn không đốt lên để sưởi ấm tối nay được**! Củi thật nằm trong kho mang lại lợi ích sống còn là giữ cho nhà máy/gia đình không bị đóng băng ngay lập tức — lợi ích đó gọi là **Convenience Yield ($y$)**!
  - Nếu một nhà kinh doanh thấy củi hôm nay đắt ($\$100$) còn củi kỳ hạn rẻ ($\$70$), anh ta có thể "mượn củi thật trong kho của nhà máy đem bán lấy $\$100$" (**Reverse Cash-and-Carry**) được không? **KHÔNG THỂ!** Không một nhà máy nào chịu cho mượn kho củi dự trữ giữa lúc bão tuyết vì thiếu củi là dây chuyền sản xuất sập ngay lập tức!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Công thức: $F_{0,T} = S_0 e^{(r + u - y)T}$. Khi khan hiếm hàng vật chất, $y > r + u \implies F_{0,T} < S_0$ (*Backwardation*). Chiều *Cash-and-Carry* tạo cận trên cứng, nhưng *Reverse Cash-and-Carry* bị chặn bởi không thể bán khống/vay hàng tiêu dùng thiết yếu.

---

### Câu C9 (Lecture 09 — Omicron Q11 & Practice L08–L11 Q13): Explain two practical risks that prevent a derivative hedge from being perfect: (a) Funding Liquidity Risk in daily-settled futures, and (b) Basis Risk in cross-hedging or interest-rate swaps.
*(Giải thích 2 rủi ro thực tế khiến việc phòng vệ bằng phái sinh không hoàn hảo: (a) Rủi ro thanh khoản dòng tiền trong hợp đồng tương lai thanh toán hàng ngày, và (b) Rủi ro cơ sở trong phòng vệ chéo hoặc hoán đổi lãi suất.)*

- **[Exam Model Answer — English (~85 words)]:**
  1. **Funding Liquidity Risk (Cash-Flow Timing Mismatch):** When hedging a long-term illiquid physical commitment with exchange-traded **futures**, the futures position is marked to market **daily**, whereas the underlying asset generates cash only at maturity $T$. If spot/futures prices move against the futures leg interim, massive **variation margin calls** can force premature liquidation of a solvent hedge.
  2. **Basis Risk:** Arises whenever the hedging instrument's underlying index does not perfectly match the hedged exposure (e.g., hedging jet fuel with crude oil futures, or swapping floating debt indexed to Benchmark $M$ using an IRS indexed to Benchmark $L$ where $M_t \ne L_t$), leaving residual rate/price mismatch $L_t - M_t$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Funding Liquidity Risk (Bài toán "Vàng trong két nhưng cháy túi tiền lẻ" — Omicron L09 Q11):**
     Bạn có một vườn sầu riêng chắc chắn 6 tháng nữa thu hoạch bán được tiền tỷ. Để khóa giá bán, bạn lên sàn **Short Futures sầu riêng**. Nhưng tháng sau giá sầu riêng trên thị trường đột nhiên tăng gấp đôi: vườn sầu riêng thật của bạn có giá trị tăng gấp đôi thật đấy, nhưng **sầu riêng vẫn còn xanh trên cây chưa hái bán lấy tiền mặt được**, trong khi sàn Futures đòi bạn **nộp tiền mặt ký quỹ ngay chiều nay (Variation Margin Call)**! Nếu không vay kịp tiền mặt để nộp, sàn sẽ cắt hợp đồng của bạn ngay lập tức!
  2. **Basis Risk (Bài toán "Đau răng nhưng uống thuốc đau bụng" — `Q13` Swap `M vs. L`):**
     Khoản nợ vay ngân hàng của bạn tính lãi theo chỉ số **$M$**, nhưng hợp đồng bảo hiểm Swap bạn mua lại trả tiền theo chỉ số **$L$**. Nếu bình thường $M = L$ thì khử hết rủi ro; nhưng lúc khủng hoảng nếu $M$ vọt lên $8\%$ mà $L$ chỉ lên $6\%$, bạn vẫn bị hở phần chênh lệch $M - L = 2\%$ (**Basis Risk**)!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Funding Liquidity Risk:** *Daily marking-to-market cash outflows vs. illiquid asset payoff at maturity $T$*.
  - **Basis Risk:** *Imperfect correlation / spread fluctuation ($M_t - L_t \ne 0$) between hedged item and hedging instrument*.

---

### Câu C10 (Lecture 09 — Q11c / Practice L08–L11 Q12c): In a fixed-for-fixed currency swap used to hedge a foreign-currency loan, explain when all foreign exchange risk is eliminated and what happens if the swap's foreign fixed rate is smaller than the loan's interest rate.
*(Trong hợp đồng hoán đổi tiền tệ cố định – cố định dùng để phòng vệ khoản vay ngoại tệ, hãy giải thích khi nào toàn bộ rủi ro tỷ giá được triệt tiêu và điều gì xảy ra nếu lãi suất cố định ngoại tệ trên swap nhỏ hơn lãi suất khoản vay.)*

- **[Exam Model Answer — English (~80 words)]:**
  A fixed-for-fixed currency swap exchanges principal at inception (optional) and re-exchanges principals at maturity $T$, while swapping periodic fixed interest payments in two currencies.
  - **Complete FX Hedge:** Foreign exchange risk is $100\%$ eliminated only if both the swap's **foreign notional principal** and **foreign fixed coupon rate** exactly match the foreign loan's principal and interest rate.
  - **Coupon Rate Mismatch:** If the loan charges $4.5\%$ in EUR while the swap pays only $4.0\%$ in EUR on the same EUR notional, the firm faces a **residual unhedged EUR outflow of $0.50\%$ per year**, which remains exposed to spot FX fluctuations.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Công ty Mỹ của bạn đang nợ ngân hàng Châu Âu **$10\text{ triệu EUR}$** với tiền lãi phải trả mỗi năm là **$4.5\%$ ($450,000\text{ EUR/năm}$)**.
  - Để không lo đồng EUR tăng giá, bạn ký hợp đồng **Currency Swap**: mỗi năm đối tác đưa cho bạn EUR để bạn đem trả ngân hàng, đổi lại bạn chỉ việc trả một khoản USD cố định.
  - Nếu đối tác Swap đưa đủ **$4.5\%\text{ EUR/năm}$** và cuối kỳ đưa đủ **$10\text{ triệu EUR}$ tiền gốc** $\implies$ bạn không còn dính dáng một xu nào đến biến động tỷ giá EUR/USD nữa!
  - Nhưng nếu hợp đồng Swap chỉ đưa cho bạn **$4.0\%\text{ EUR/năm}$ ($400,000\text{ EUR}$)** trong khi ngân hàng đòi **$4.5\%$ ($450,000\text{ EUR}$)**, thì mỗi năm bạn vẫn phải **tự móc túi mua thêm $50,000\text{ EUR}$ ngoài chợ ($0.5\%$)** — phần thiếu hụt $0.5\%\text{ EUR}$ này vẫn bị phơi nhiễm với rủi ro tỷ giá!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Khớp cả **Notional principal** lẫn **Coupon rate** $\implies 0$ FX risk. Nếu $r_{\text{loan}}^{\text{FOR}} > r_{\text{swap}}^{\text{FOR}}$, phần chênh lệch $(r_{\text{loan}}^{\text{FOR}} - r_{\text{swap}}^{\text{FOR}})\times \text{Notional}$ là **residual unhedged foreign-currency cash outflow**.

---

### Câu C11 (Lecture 10 & Practice L08–L11 Q19, Q21, Q24): Compare the economic purpose and payoff trade-offs of (a) Straddle vs. Strangle, (b) Bull Call Spread vs. Uncapped Long Call, and (c) Zero-Cost Collar vs. Protective Put.
*(So sánh mục đích kinh tế và sự đánh đổi lợi nhuận của: (a) Straddle vs. Strangle, (b) Bull Call Spread vs. Long Call đơn thuần, và (c) Collar vs. Protective Put.)*

- **[Exam Model Answer — English (~90 words)]:**
  1. **Long Straddle vs. Long Strangle (Volatility bets):** Both buy a Call and a Put at the same maturity to profit from large price moves in either direction. A **Strangle** ($K_P < K_C$, both OTM) costs **less upfront premium** (smaller maximum loss) than an ATM **Straddle** ($K_P = K_C$), but requires a **wider stock move** to reach its breakeven points.
  2. **Bull Call Spread ($+C(K_1) - C(K_2)$):** Selling the higher-strike call $C(K_2)$ lowers initial cost and lowers the breakeven price, in exchange for **capping upside payoff** at $K_2 - K_1$.
  3. **Collar ($+S_0 + P(K_1) - C(K_2)$):** Finances the protective put floor $K_1$ by writing an OTM call at $K_2$, reducing net insurance cost at the expense of capping share appreciation above $K_2$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  1. **Straddle vs. Strangle ("Đặt bẫy bắt thú chạy sang trái hoặc sang phải"):**
     - **Straddle ($K_P = K_C$):** Đặt hai cái bẫy sát ngay vị trí con thú đang đứng $\implies$ con thú chỉ cần nhích nhẹ sang trái hay sang phải là dính bẫy ngay, nhưng **tiền thuê cặp bẫy này rất đắt**.
     - **Strangle ($K_P < S_0 < K_C$):** Đặt hai cái bẫy ở xa hai bên $\implies$ **tiền thuê bẫy rẻ hơn hẳn**, nhưng con thú phải **chạy thật xa** mới chạm tới bẫy để bạn có lời!
  2. **Bull Call Spread & Collar ("Bán bớt phần ngọn cây để lấy tiền mua phần gốc"):**
     - Mua bảo hiểm Put (hoặc mua Call $K_1$) tốn nhiều tiền mặt. Làm sao để giảm tiền mua hôm nay? Bạn hứa với người khác: *"Nếu cổ phiếu tăng vượt quá mức trần $K_2$, tôi nhường toàn bộ phần lãi phía trên $K_2$ cho anh (Short Call $K_2$) để anh trả tiền mặt cho tôi ngay hôm nay!"* $\implies$ Chi phí ban đầu giảm xuống (thậm chí bằng $\$0$ trong Zero-cost Collar), đổi lại lợi nhuận tối đa bị **đóng trần tại $K_2$**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Strangle vs. Straddle:** Lower upfront cost / smaller max loss, but wider breakeven band.
  - **Bull Spread / Collar:** Reduces initial premium and lowers breakeven by **capping upside potential above $K_2$**.

---

### Câu C12 (Lecture 10 & Practice L08–L11 Q23): Explain why increasing time to expiration $T$ ALWAYS increases (or never decreases) the value of an American option, whereas a longer-lived European option can sometimes be worth LESS than a shorter-lived one.
*(Giải thích tại sao việc tăng thời gian đáo hạn $T$ luôn làm tăng (hoặc không bao giờ làm giảm) giá trị quyền chọn Kiểu Mỹ, trong khi quyền chọn Châu Âu kỳ hạn dài hơn đôi khi lại có giá THẤP HƠN quyền chọn kỳ hạn ngắn.)*

- **[Exam Model Answer — English (~80 words)]:**
  - **American Options ($V_A(T_2) \ge V_A(T_1)$ for $T_2 > T_1$):** Because an American option can be exercised at **any date up to maturity**, the holder of the $T_2$-maturity option possesses **every exercise opportunity** available to the $T_1$-maturity holder, plus additional exercise rights between $T_1$ and $T_2$. More rights can never reduce value.
  - **European Options ($V_E(T_2)$ vs. $V_E(T_1)$):** European options can be exercised **only on their single expiration date**. A longer-lived European Call can be worth less if a **large dividend** goes ex-dividend between $T_1$ and $T_2$; a longer-lived deep-ITM European Put can be worth less because receiving the cash strike $K$ is delayed from $T_1$ to $T_2$.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy so sánh hai loại **Vé vào công viên giải trí**:
  1. **American Option = "Thẻ VIP được vào cửa bất kỳ ngày nào từ hôm nay đến hết hạn":**
     Thẻ VIP có hạn dùng **6 tháng ($T_2$)** đương nhiên luôn quý hơn hoặc bằng Thẻ VIP hạn dùng **3 tháng ($T_1$)**, vì mọi ngày mà thẻ 3 tháng đi được thì thẻ 6 tháng đều đi được, lại còn được tặng thêm 3 tháng nữa!
  2. **European Option = "Vé chỉ được vào cửa ĐÚNG 1 NGÀY DUY NHẤT ghi trên vé":**
     - **Vé Call Châu Âu:** Vé vào cửa **ngày 30/6 ($T_1$)** có thể đắt giá hơn hẳn vé vào cửa **ngày 30/9 ($T_2$)** nếu vào ngày 15/7 công viên **tháo dỡ mất trò tàu lượn siêu tốc (trả một khoản cổ tức tiền mặt khổng lồ $D$ làm giá cổ phiếu sụt mạnh)**! Người có vé ngày 30/9 chỉ được vào sau khi tàu lượn đã bị dỡ mất!
     - **Vé Put Châu Âu đang lời đậm (Deep-ITM):** Giống như tờ phiếu trúng thưởng $\$100$, vé hẹn nhận tiền sau 3 tháng ($T_1$) đương nhiên quý hơn vé bắt bạn phải đợi 10 năm sau ($T_2$) mới cho nhận đúng $\$100$ đó!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **American:** Nested exercise sets ($[0, T_1] \subset [0, T_2]$) $\implies V_A(T_2) \ge V_A(T_1)$.
  - **European:** Different single exercise dates ($T_1 \ne T_2$) $\implies$ large interim dividend hurts longer European Call; delayed receipt of $K$ hurts deep-ITM longer European Put.

---

### Câu C13 (Lecture 11 Cells 21–22 & Practice L08–L11 Q33): Explain why the risk-neutral probability $p$ remains constant across nodes in a multiplicative binomial tree ($S_u = uS, S_d = dS$), but changes at every node in an additive dollar-move tree ($S_{\text{up}} = S + \Delta S_u, S_{\text{down}} = S - \Delta S_d$).
*(Giải thích tại sao xác suất trung hòa rủi ro $p$ không đổi tại mọi nút trên cây nhị phân nhân tử, nhưng lại thay đổi tại từng nút trên cây nhị phân cộng tuyến tính theo số tiền.)*

- **[Exam Model Answer — English (~80 words)]:**
  At any node with current stock price $S_{\text{node}}$, the no-arbitrage risk-neutral probability of an up move over one step (with gross risk-free factor $r$) is:
  $$p_{\text{node}} = \frac{r S_{\text{node}} - S_{\text{down}}}{S_{\text{up}} - S_{\text{down}}} = \frac{r - d_{\text{node}}}{u_{\text{node}} - d_{\text{node}}}$$
  - In a **multiplicative tree**, $S_{\text{up}} = u S_{\text{node}}$ and $S_{\text{down}} = d S_{\text{node}}$ with constant proportional factors $u, d$, so $S_{\text{node}}$ cancels out and $p = \frac{r-d}{u-d}$ is identical at every node.
  - In an **additive dollar-move tree** ($+\$A / -\$B$), $S_{\text{up}} - S_{\text{down}} = A + B$ is constant in dollars, while $r S_{\text{node}} - (S_{\text{node}} - B) = (r-1)S_{\text{node}} + B$ grows with $S_{\text{node}}$. Thus $p_{\text{node}}$ increases at higher stock price nodes ($p_u > p_0 > p_d$).

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Trong thế giới trung hòa rủi ro, **số tiền lãi trung bình của 1 cổ phiếu trong mỗi bước phải bằng đúng số tiền lãi gửi ngân hàng $(r - 1) \times S_{\text{node}}$**:
  - **Cây nhân phần trăm (Multiplicative tree):** Khi giá cổ phiếu tăng gấp đôi, cả tiền lãi ngân hàng cần đạt được lẫn bước nhảy của cổ phiếu đều tăng gấp đôi theo tỷ lệ phần trăm $\implies$ xác suất $p$ giữ nguyên không đổi!
  - **Cây cộng số tiền cố định (Additive tree — ví dụ mỗi bước chỉ tăng $+\$12$ hoặc giảm $-\$8$, lãi suất ngân hàng $4\%/$kỳ):**
    - Khi cổ phiếu ở giá thấp ($S_d = \$92$), để kiếm đủ $4\%$ tiền lãi ngân hàng ($0.04 \times \$92 = +\$3.68$), cổ phiếu chỉ cần xác suất tăng vừa phải ($p_d = \frac{3.68 + 8}{12 + 8} = 0.584$).
    - Nhưng khi cổ phiếu đã leo lên giá cao ($S_u = \$112$), $4\%$ tiền lãi ngân hàng lúc này đòi hỏi tới **$\$4.48$ tiền mặt** ($0.04 \times \$112$), trong khi bước nhảy tối đa của cổ phiếu vẫn bị khóa cứng ở $+\$12$ và $-\$8$! Để kéo mức tăng trung bình bằng tiền lên tới $+\$4.48$, **xác suất nhảy lên ở nút trên ($p_u$) bắt buộc phải lớn hơn ở nút dưới ($p_u > p_0 > p_d$)**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Viết công thức $p_{\text{node}} = \frac{r S_{\text{node}} - S_{\text{down}}}{S_{\text{up}} - S_{\text{down}}} = \frac{(r-1)S_{\text{node}} + B}{A + B}$. Khi $r > 1$, $p_{\text{node}}$ là hàm đồng biến theo $S_{\text{node}}$ nên $p_u > p_0 > p_d$.

---

### Câu C14 (Extra Session Cell 11–12 & Practice L08–L11 Q35): Explain why a static delta-replicating portfolio ($V_{\text{rep}}(S) = \Delta_0 S + B_0$) matches the Black-Scholes option value only for infinitesimal stock moves and underperforms the true option value for large moves in either direction.
*(Giải thích tại sao danh mục mô phỏng tĩnh theo Delta chỉ khớp với giá trị quyền chọn cho các biến động giá rất nhỏ và luôn thấp hơn giá trị thực của quyền chọn khi giá cổ phiếu biến động mạnh theo bất kỳ chiều nào.)*

- **[Exam Model Answer — English (~75 words)]:**
  Option delta $\Delta = \frac{\partial V}{\partial S}$ is the **first-order slope (tangent line)** of the option-value curve $V(S)$ at the current stock price $S_0$. Thus, holding a fixed portfolio of $\Delta_0$ shares and $B_0$ cash traces a **straight tangent line** $V_{\text{rep}}(S) = \Delta_0 S + B_0$.
  Because both European calls and puts on non-dividend stocks have **strictly positive convexity (positive Gamma, $\Gamma = \frac{\partial^2 V}{\partial S^2} > 0$)**, the true curved option value $V(S)$ bends **above** its tangent line for any large move $\Delta S \ne 0$. Continuous rebalancing of $\Delta$ as $S$ changes is required to track the curve.

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Câu này có cơ chế **giống hệt câu cái bát tô (Convexity) của Trái phiếu ở Câu P5**, chỉ đổi tên gọi sang quyền chọn:
  - Quyền chọn có một "phép thuật" tuyệt vời: **Khi cổ phiếu tăng giá, độ nhạy $\Delta$ của quyền chọn Mua tự động phình to ra** (giúp bạn thắng ngày càng nhanh hơn); còn **khi cổ phiếu giảm giá, độ nhạy $\Delta$ tự động co nhỏ lại về $0$** (giúp bạn hãm phanh, lỗ ngày càng chậm lại!). Tính chất "thắng thì đạp ga, thua thì tự đạp phanh" đó làm đường giá quyền chọn uốn cong lên trên như cái bát tô (**Positive Gamma / Convexity $> 0$**).
  - Trong khi đó, nếu bạn giữ khư khư một số lượng cổ phiếu cố định $\Delta_0$ không chịu chỉnh lại (**Static Delta portfolio**), tốc độ thắng và tốc độ thua của bạn là một **đường thẳng cứng nhắc (Tangent line)** nằm dưới đáy bát. Vì vậy, hễ giá cổ phiếu chạy ra xa (dù tăng mạnh hay giảm mạnh), **đường cong quyền chọn thật luôn nằm CAO HƠN đường thẳng tĩnh $\Delta_0 S + B_0$**!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - **Static replicating portfolio** $V_{\text{rep}}(S) = \Delta_0 S + B_0$ là **linear tangent line** tại $S_0$.
  - Vì quyền chọn có **Positive convexity / Gamma ($\Gamma = \frac{\partial^2 V}{\partial S^2} > 0$)**, đường cong $V(S)$ luôn nằm phía trên đường tiếp tuyến với mọi $\Delta S \ne 0$.

---

### Câu C15 (Extra Session `Kappa` Cells 19–25 & Practice L08–L11 Q25): Explain the "Asset Substitution / Risk Shifting" conflict between shareholders and bondholders using the Merton model, and state why a negative-NPV project can still increase a levered firm's stock price.
*(Giải thích mâu thuẫn "Thay thế Tài sản / Dịch chuyển Rủi ro" giữa cổ đông và chủ nợ bằng mô hình Merton, và nêu lý do tại sao một dự án có NPV âm vẫn có thể làm tăng giá cổ phiếu của công ty có vay nợ.)*

- **[Exam Model Answer — English (~85 words)]:**
  In Merton's model, total firm value is split between equity and risky debt: $V_0 = E_0 + D_0$, where equity is a **European call option** on firm assets ($E_0 = C(V_0, K, \sigma_V)$) and risky debt is short a default put ($D_0 = PV(K) - P(V_0, K, \sigma_V)$).
  Because a call option has **positive Vega ($\frac{\partial E_0}{\partial \sigma_V} > 0$)** due to limited liability (shareholders capture all upside above $K$ while losses are capped at $\$0$), increasing asset volatility $\sigma_V$ transfers wealth from bondholders to shareholders. If this volatility-driven wealth transfer ($+\Delta E_{\sigma}$) exceeds a small drop in total asset value ($\Delta V_0 < 0$), **stock price $E_0$ rises even though firm value $V_0$ falls**!

- **[Giải Thích Kiểu "Trẻ Em Cũng Hiểu Ngay" (Feynman / ELI5)]:**
  Hãy tưởng tượng công ty đang có tài sản **$V_0 = \$150\text{ triệu}$**, nhưng nợ Ngân hàng tới **$K = \$120\text{ triệu}$**. Bây giờ Giám đốc (đại diện cho Cổ đông) thấy một dự án đánh bạc siêu mạo hiểm: **Làm tổng giá trị nhà máy giảm mất $\$3\text{ triệu}$ xuống còn $\$147\text{ triệu}$ ($\text{NPV} = -\$3\text{m} < 0$), nhưng độ biến động hên xui ($\sigma_V$) tăng vọt từ $25\%$ lên $40\%$** (hoặc thắng cực to $\$300\text{ triệu}$, hoặc sập xuống còn $\$50\text{ triệu}$)!
  - **Tại sao Cổ đông lại vỗ tay tán thành dự án làm giảm giá trị công ty này?**
    Vì luật chơi **"Ngửa thì Cổ đông ăn cả, Sấp thì Chủ nợ chịu trận"**:
    - Nếu canh bạc **thắng to** (nhà máy lên $\$300\text{ triệu}$): Ngân hàng cũng chỉ được nhận đúng $\$120\text{ triệu}$ tiền nợ cố định, toàn bộ phần lời khổng lồ $\$180\text{ triệu}$ chảy hết vào túi Cổ đông!
    - Nếu canh bạc **thua thảm hại** (nhà máy sập xuống $\$50\text{ triệu}$): Cổ đông phủi tay bỏ đi ($E_T = \$0$ nhờ trách nhiệm hữu hạn), còn Ngân hàng phải ôm trọn cục lỗ $\$70\text{ triệu}$!
  - Nói cách khác, việc tăng độ liều lĩnh ($\sigma_V \uparrow$) giống như **Cổ đông móc túi của Chủ nợ $\$9.09\text{ triệu}$ để bỏ vào túi mình**: dù trong quá trình móc túi làm rơi mất $\$3\text{ triệu}$ xuống đất ($\Delta V = -\$3\text{m}$), túi của Cổ đông vẫn dày thêm được $+9.09 - 3.00 = +\$6.09\text{ triệu}$ (giá cổ phiếu tăng!), còn Chủ nợ thì mất trắng $-\$9.09\text{ triệu}$!

- **[Cầu Nối Học Thuật & Từ Khóa Ăn Điểm]:**
  - Phương trình bảo toàn giá trị: $\Delta V_0 = \Delta E_0 + \Delta D_0$.
  - Khi $\sigma_V \uparrow$ và $V_0 \downarrow$ nhẹ: hiệu ứng **Positive Vega của Equity Call ($\frac{\partial E}{\partial \sigma_V} > 0$)** thắng hiệu ứng giảm tài sản ($\Delta E_0 = +\$6.09\text{m} > 0$), chuyển thiệt hại sang chủ nợ ($\Delta D_0 = -\$9.09\text{m} < 0$). Kết luận vàng của Extra Session: **"A higher stock price does not imply value creation for the firm!"**

---

## BẢNG TỔNG KẾT "MẸO VIẾT TỰ LUẬN NGẮN DƯỚI 100 TỪ ĐẠT ĐIỂM TUYỆT ĐỐI"

Khi gặp bất kỳ câu hỏi `Prove / Show / Explain / Critique` nào trong đề thi ngày mai, hãy nhớ lại **câu chuyện đời thường (Feynman/ELI5)** trong đầu trong 3 giây, rồi viết ra giấy theo **Công thức 3 Câu (3-Sentence Rule — khoảng 60 đến 90 từ)**:
1. **Câu 1 — Nêu Định nghĩa / Phương trình Gốc (1 dòng chữ + 1 dòng công thức):** Viết ngay công thức toán học chuẩn của mô hình (ví dụ: $C_0 - P_0 = S_0 - PV(D) - PV(K)$, hoặc $R_i = \alpha_i + \beta_i R_M + e_i$, hoặc $\frac{\Delta P}{P_0} \approx -D_{\text{Mod}}\Delta y + \frac{1}{2}CX(\Delta y)^2$). **Một phương trình đúng thay thế cho 40 từ diễn giải dài dòng!**
2. **Câu 2 — Chỉ ra Cơ chế / Giả định Quyết định (20–30 từ):** Chỉ đích danh giả định hoặc số hạng nào tạo ra kết quả (ví dụ: *"Since $\text{Cov}(e_i, e_j)=0$..."*, hoặc *"Because $(\Delta y)^2 > 0$ and $\text{Convexity} > 0$ for any nonzero shift..."*, hoặc *"Because $P_E \ge 0$ and $K - PV(K) > 0$ when $r > 0$..."*).
3. **Câu 3 — Kết luận Kinh tế Trực tiếp (15–25 từ):** Chốt lại câu trả lời khớp 100% với câu hỏi của đề (*"Therefore, the analyst's claim is false because idiosyncratic risk $\sigma_e > 0$ remains"*, hoặc *"Hence, an American call on a non-dividend stock is never exercised early, so $C_A = C_E$"*).
