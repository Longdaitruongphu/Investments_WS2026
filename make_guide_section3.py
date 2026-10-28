import sys

out_file = "/media/minh/DISK/Downloads/Investments_WS2026/MASTER_EXAM_PREPARATION_ULTIMATE_GUIDE.md"

sec3 = r"""
---

# PHẦN 3: LECTURE 08: HIỆU QUẢ THỊ TRƯỜNG & TÀI CHÍNH HÀNH VI
## (EFFICIENT MARKET HYPOTHESIS & BEHAVIORAL FINANCE)

---

### 3.1. Khung Lý Thuyết Cốt Lõi: EMH & Tài Chính Hành Vi

#### A. Giả Thuyết Thị Trường Hiệu Quả (EMH - Eugene Fama)
1. **Ba cấp độ hiệu quả thị trường**:
   - **Hiệu quả dạng Yếu (Weak-form)**: Giá phản ánh toàn bộ thông tin giá và khối lượng giao dịch trong quá khứ.
     - *Hệ quả*: Phân tích kỹ thuật (Technical Analysis / Charting) hoàn toàn vô dụng.
   - **Hiệu quả dạng Bán mạnh (Semi-strong-form)**: Giá phản ánh toàn bộ thông tin công khai (Báo cáo tài chính, tin tức kinh tế, thông báo cổ tức, P/E...).
     - *Hệ quả*: Phân tích cơ bản (Fundamental Analysis) không thể tạo ra tỷ suất sinh lời vượt trội (Alpha) có điều chỉnh rủi ro một cách bền vững.
   - **Hiệu quả dạng Mạnh (Strong-form)**: Giá phản ánh toàn bộ thông tin, bao gồm cả thông tin công khai lẫn **thông tin nội bộ (insider / private information)**.
     - *Thực tế*: Thị trường thực tế KHÔNG BAO GIỜ đạt hiệu quả dạng mạnh vì giao dịch nội gián luôn tạo ra siêu lợi nhuận.
2. **Vấn đề Giả thuyết Kép (Joint Hypothesis Problem)**:
   - Mọi kiểm định về thị trường hiệu quả đều phải sử dụng một mô hình định giá tài sản làm chuẩn (ví dụ CAPM, FF3, FF5).
   - Nếu phát hiện $\alpha \ne 0$, ta không thể kết luận chắc chắn thị trường phi hiệu quả hay do **mô hình định giá của ta bị thiếu biến (Misspecified Benchmark)**.

#### B. Các Thiên Kiến Tâm Lý Hành Vi (Behavioral Biases)
1. **Hiệu ứng Khung (Framing)**: Cách trình bày cùng một vấn đề làm thay đổi quyết định của nhà đầu tư.
2. **Neo và Điều chỉnh (Anchoring and Adjustment)**: Gắn chặt vào một con số ban đầu (như giá cũ đỉnh lịch sử, giá mua) và không điều chỉnh đủ linh hoạt khi có dữ liệu mới.
3. **Thiên lệch Khẳng định (Confirmation Bias)**: Chỉ chăm chăm tìm kiếm và lưu giữ các thông tin củng cố quan điểm cá nhân, đồng thời phớt lờ các thông tin đối lập đáng tin cậy.
4. **Kế toán Tinh thần (Mental Accounting - Thaler)**: Phân chia tiền bạc vào các "ngăn tài khoản ảo" riêng biệt (ví dụ coi tiền thưởng là "tiền đánh bạc / house money", còn tiền lương là "tiền sinh mệnh") dù về mặt kinh tế, tiền có tính thay thế hoàn hảo (fungible).
5. **Lý thuyết Triển vọng & Hiệu ứng Xử lý (Prospect Theory & Disposition Effect)**:
   - Hàm giá trị hình chữ S (S-shaped value function): Lồi ở miền lỗ (ngại chốt lỗ, thích liều lĩnh) và lõm ở miền lãi (thích an toàn, chốt lời non).
   - *Disposition Effect*: Xu hướng vội vàng bán cổ phiếu đang có lãi ("chốt lời non") và ôm chặt cổ phiếu đang thua lỗ trong hy vọng hòa vốn.

---

### 3.2. Giải Chi Tiết Toàn Bộ Questions 1 – 5 (Practice L08-L11)

#### Question 1 (Easy): Phân Biệt Các Cấp Độ Hiệu Quả Thị Trường
- **Đề bài**: Hai nhà đầu tư đưa ra kết luận:
  - **Alpha**: Một chiến lược chỉ dùng giá cổ phiếu trong quá khứ đem lại lợi nhuận 14% năm ngoái, trong khi thị trường tăng 10%. Alpha kết luận hiệu quả dạng yếu bị bác bỏ.
  - **Beta**: Qua nhiều đợt công bố, một chiến lược sử dụng thông tin lợi nhuận nội bộ tuyệt mật trước khi phát hành liên tục kiếm được lợi nhuận vượt trội dương sau chi phí. Beta kết luận hiệu quả dạng bán mạnh bị bác bỏ.
  - (a) Đánh giá kết luận của Alpha. Cần thêm bằng chứng gì?
  - (b) Đánh giá kết luận của Beta về cấp độ hiệu quả thị trường.
- **Lời giải chi tiết**:
  - (a) **Đánh giá kết luận của Alpha**:
    - Kết luận của Alpha là **HOÀN TOÀN SAI / KHÔNG ĐỦ CĂN CỨ**.
    - Việc tỷ suất sinh lời thô vượt thị trường trong **duy nhất 1 năm** (14% vs 10%) có thể hoàn toàn do:
      1. Yếu tố may mắn ngẫu nhiên (Luck / Sampling error).
      2. Danh mục của Alpha chịu mức rủi ro hệ thống (Beta) cao hơn thị trường (ví dụ nếu Beta = 1.5 thì khi thị trường tăng 10%, danh mục tăng 14% là hoàn toàn bình thường, không hề có Alpha vượt trội!).
      3. Chưa tính chi phí giao dịch và thuế.
    - *Bằng chứng bổ sung cần thiết*: Cần kiểm định trên chuỗi thời gian dài qua nhiều chu kỳ thị trường, kiểm soát rủi ro bằng mô hình chuẩn (CAPM/FF3 để tính $\alpha$ có điều chỉnh rủi ro), và chứng minh $\alpha$ dương có ý nghĩa thống kê ($t\text{-stat} > 2.0$) sau khi trừ toàn bộ chi phí giao dịch.
  - (b) **Đánh giá kết luận của Beta**:
    - Kết luận của Beta về cấp độ hiệu quả là **SAI VỀ MẶT PHÂN LOẠI**.
    - Thông tin kết quả kinh doanh nội bộ trước khi công bố là **THÔNG TIN NỘI BỘ / TƯ NHÂN (Private / Insider Information)**, không phải thông tin công khai.
    - Hiệu quả dạng bán mạnh (Semi-strong form) chỉ tuyên bố giá phản ánh toàn bộ thông tin **CÔNG KHAI (Public Information)**. Bán mạnh KHÔNG loại trừ việc người có tin nội gián kiếm được lợi nhuận siêu ngạch.
    - Việc kiếm lợi nhuận từ tin nội gián chứng minh rằng thị trường **BÁC BỎ DẠNG MẠNH (Strong-form EMH)**, chứ không hề bác bỏ dạng bán mạnh!

#### Question 2 (Average): Nhận Diện Thiên Lệch Hành Vi
- **Đề bài**:
  - **Gamma**: Định giá cổ phiếu ở mức 82 USD theo mô hình chiết khấu dòng tiền. Sau khi nghe đồng nghiệp nói cổ phiếu từng giao dịch ở 120 USD, Gamma nâng định giá lên 105 USD dù không thay đổi bất kỳ dự báo dòng tiền hay lãi suất nào, giải thích rằng giá sẽ quay lại gần mức cũ.
  - **Delta**: Kỳ vọng doanh số công ty sẽ hồi phục. Delta chỉ đưa vào báo cáo các tin tức doanh số khả quan, nhưng loại bỏ các bằng chứng đáng tin cậy về việc sụt giảm đơn hàng vì nó mâu thuẫn với kỳ vọng ban đầu.
  - Hãy xác định thiên lệch hành vi của từng người, giải thích chi tiết quyết định và phân biệt với 1 thiên lệch dễ nhầm lẫn khác.
- **Lời giải chi tiết**:
  - **Nhà đầu tư Gamma**:
    - **Thiên lệch chính**: **Neo và Điều Chỉnh (Anchoring and Adjustment)**.
    - *Chi tiết quyết định*: Mức giá lịch sử 120 USD đóng vai trò là một "mỏ neo" tâm lý (anchor). Gamma điều chỉnh định giá từ 82 USD vọt lên 105 USD một cách vô căn cứ chỉ để kéo nó gần về mỏ neo 120 USD, dù mô hình kinh tế không có dữ liệu mới.
    - *Phân biệt với Đại diện (Representativeness)*: Representativeness là suy diễn một xu hướng lớn từ một mẫu nhỏ (coi một vài quý tăng trưởng là công ty vĩ đại). Ở đây, Gamma không suy diễn quy luật từ mẫu, mà bị thôi miên bởi một điểm dữ liệu duy nhất trong quá khứ.
  - **Nhà đầu tư Delta**:
    - **Thiên lệch chính**: **Thiên Lệch Khẳng Định (Confirmation Bias)**.
    - *Chi tiết quyết định*: Delta chủ động sàng lọc thông tin có chọn lọc, chỉ tiếp nhận các dữ liệu phù hợp với niềm tin sẵn có và chủ ý loại bỏ các bằng chứng mâu thuẫn đáng tin cậy (đơn hàng giảm).
    - *Phân biệt với Tự tin thái quá (Overconfidence)*: Overconfidence là tin rằng khả năng dự báo của mình chuẩn xác hơn người khác (khoảng tin cậy quá hẹp). Confirmation bias nhấn mạnh vào hành vi **chọn lọc và bóp méo luồng thông tin** tiếp nhận.

#### Question 3 (Average): Đánh Giá Quản Lý Quỹ, Phí Quản Lý & Fama-French 3 Nhân Tố
- **Đề bài**: Benchmark Fama-French 3 nhân tố: $r_f = 2.00\%, R_M = 6.00\%, SMB = 2.00\%, HML = 3.00\%$.
  - Quỹ Kappa: Gross = 12.80%, $\beta_M = 1.40, \beta_{SMB} = 0.50, \beta_{HML} = -0.20$, Phí quản lý = 1.10%, Chi phí giao dịch = 0.70%.
  - Quỹ Lambda: Gross = 11.60%, $\beta_M = 0.90, \beta_{SMB} = -0.30, \beta_{HML} = 0.40$, Phí quản lý = 1.20%, Chi phí giao dịch = 0.40%.
  - (a) Tính tỷ suất sinh lời benchmark, Alpha gộp, Tỷ suất ròng và Alpha ròng của từng quỹ. So sánh thứ hạng theo Lợi nhuận gộp và Alpha ròng.
  - (b) Cố định chi phí giao dịch và lợi nhuận gộp, tìm mức phí quản lý để Alpha ròng của từng quỹ bằng 0.
  - (c) Đánh giá nhận định của Theta: "Lợi nhuận gộp của Kappa cao hơn chứng tỏ kỹ năng vượt trội, và Alpha ròng dương chứng minh thị trường phi hiệu quả."
- **Lời giải chi tiết**:
  - (a) **Tính toán Benchmark & Alpha**:
    - *Benchmark Return ($r_B$)*:
      $$r_{B, \text{Kappa}} = 2.00\% + 1.40(6.00\%) + 0.50(2.00\%) - 0.20(3.00\%) = 2.00\% + 8.40\% + 1.00\% - 0.60\% = \mathbf{10.80\%}$$
      $$r_{B, \text{Lambda}} = 2.00\% + 0.90(6.00\%) - 0.30(2.00\%) + 0.40(3.00\%) = 2.00\% + 5.40\% - 0.60\% + 1.20\% = \mathbf{8.00\%}$$
    - *Alpha Gộp ($\alpha_{\text{gross}} = r_{\text{gross}} - r_B$)*:
      $$\alpha_{\text{gross, Kappa}} = 12.80\% - 10.80\% = \mathbf{+2.00\%}$$
      $$\alpha_{\text{gross, Lambda}} = 11.60\% - 8.00\% = \mathbf{+3.60\%}$$
    - *Tỷ suất Sinh lời Ròng ($r_{\text{net}} = r_{\text{gross}} - \text{Fee} - \text{Trading}$)*:
      $$r_{\text{net, Kappa}} = 12.80\% - 1.10\% - 0.70\% = \mathbf{11.00\%}$$
      $$r_{\text{net, Lambda}} = 11.60\% - 1.20\% - 0.40\% = \mathbf{10.00\%}$$
    - *Alpha Ròng ($\alpha_{\text{net}} = r_{\text{net}} - r_B$)*:
      $$\alpha_{\text{net, Kappa}} = 11.00\% - 10.80\% = \mathbf{+0.20\%}$$
      $$\alpha_{\text{net, Lambda}} = 10.00\% - 8.00\% = \mathbf{+2.00\%}$$
    - **So sánh thứ hạng**:
      - Theo Lợi nhuận gộp: **Kappa (12.80%) > Lambda (11.60%)**.
      - Theo Alpha ròng: **Lambda (+2.00%) > Kappa (+0.20%)**.
      - *Ý nghĩa*: Thứ hạng bị **ĐẢO NGƯỢC HOÀN TOÀN**! Lợi nhuận gộp cao của Kappa chỉ là ảo tưởng do quỹ này gánh rủi ro thị trường quá lớn ($\beta_M = 1.40$) trong năm thị trường tăng trưởng mạnh. Quỹ Lambda mới là quỹ có kỹ năng lựa chọn cổ phiếu thực sự vượt trội.
  - (b) **Mức Phí Quản Lý Hòa Vốn ($\alpha_{\text{net}} = 0$)**:
    $$\alpha_{\text{net}} = \alpha_{\text{gross}} - \text{Fee} - \text{Trading} = 0 \implies \mathbf{\text{Fee}^* = \alpha_{\text{gross}} - \text{Trading}}$$
    - Quỹ Kappa: $\text{Fee}^* = 2.00\% - 0.70\% = \mathbf{1.30\%}$.
    - Quỹ Lambda: $\text{Fee}^* = 3.60\% - 0.40\% = \mathbf{3.20\%}$.
  - (c) **Đánh giá nhận định của Theta**:
    - Nhận định 1 (Kappa giỏi hơn): **SAI**. Như đã chứng minh ở câu a, Lambda có cả Alpha gộp và Alpha ròng vượt trội Kappa.
    - Nhận định 2 (Alpha ròng dương chứng minh thị trường phi hiệu quả): **SAI**. Một kết quả 1 năm duy nhất không thể bác bỏ EMH do: (1) Có thể là may mắn ngẫu nhiên; (2) Giả thuyết kép (Joint Hypothesis Problem) - có thể mô hình FF3 chưa kiểm soát hết các nhân tố rủi ro khác (như Momentum WML hay Profitability RMW).

#### Question 4 (Average): Hiệu Ứng Xử Lý & Kế Toán Tinh Thần
- **Đề bài**:
  - **Epsilon**: Bán cổ phiếu thu 10,000 USD tiền mặt hoặc giữ thêm 1 tháng (giá trị sẽ là 8,000 hoặc 12,000 với xác suất 0.5 mỗi kịch bản). Nếu giá mua là 6,000 USD, Epsilon bán; nếu giá mua là 14,000 USD, Epsilon giữ lại.
  - **Zeta**: Giữ 10,000 USD tiền mặt hoặc đầu tư 1 tháng thu 8,000 hoặc 12,000 (xác suất 0.5). Zeta giữ tiền mặt nếu số tiền đó được gọi là "tiền lương tích lũy", nhưng đem đầu tư nếu được gọi là "tiền thưởng".
  - (a) Đánh giá nhận định rằng Epsilon minh chứng cho sự ngại mất mát (loss aversion). So sánh này thực sự ủng hộ điều gì?
  - (b) Giải thích của người quan sát rằng lựa chọn của Zeta là sự ngại rủi ro thông thường có đủ không?
- **Lời giải chi tiết**:
  - (a) **Trường hợp của Epsilon**:
    - Nhận định của người quan sát là **chưa chuẩn xác và thiếu bản chất**. Ngại mất mát (Loss aversion) chỉ đơn thuần là việc nỗi đau mất 1 đồng lớn hơn niềm vui nhận 1 đồng.
    - Hành vi của Epsilon thực sự minh chứng cho **Hiệu Ứng Xử Lý (Disposition Effect)** bắt nguồn từ **Lý Thuyết Triển Vọng (Prospect Theory - Kahneman & Tversky)**:
      - Khi giá mua là 6,000 USD, vị thế hiện tại đang có lãi (+4,000 USD). Nhà đầu tư ở **miền được (gain domain)** $\implies$ hàm giá trị lõm, thể hiện **ngại rủi ro (risk-averse)**, vội vã bán ngay để khóa chặt khoản lời.
      - Khi giá mua là 14,000 USD, vị thế đang lỗ (-4,000 USD). Nhà đầu tư ở **miền mất (loss domain)** $\implies$ hàm giá trị lồi, thể hiện **thích rủi ro (risk-seeking)**, sẵn sàng đánh cược giữ cổ phiếu với hy vọng hòa vốn. Điểm mốc tham chiếu (reference point) ở đây chính là giá mua ban đầu.
  - (b) **Trường hợp của Zeta**:
    - Lời giải thích bằng sự ngại rủi ro thông thường là **HOÀN TOÀN KHÔNG ĐỦ**.
    - Theo lý thuyết tài chính chuẩn tắc (Expected Utility Theory), 10,000 USD tiền lương hay 10,000 USD tiền thưởng đều là của cải của cá nhân và có tính thay thế hoàn hảo (fungible). Mức độ ngại rủi ro của một người đối với cùng một canh bạc 10,000 USD phải giống nhau.
    - Hiện tượng Zeta quyết định khác nhau xuất phát từ **Kế Toán Tinh Thần (Mental Accounting - Richard Thaler)**:
      - Zeta gán nhãn "tiền lương" vào ngăn tài khoản "chi tiêu thiết yếu/an toàn" nên cực kỳ ngại rủi ro.
      - Zeta gán nhãn "tiền thưởng" vào ngăn tài khoản "tiền từ trên trời rơi xuống / House Money" nên sẵn sàng chấp nhận rủi ro cao.

#### Question 5 (Hard): Giới Hạn Của Arbitrage - Chi Phí Mượn Chứng Khoán & No-Arbitrage Band
- **Đề bài**: Cổ phiếu Nu giá $S_0 = 100.00$ USD. Forward 1 năm có giá giao hàng $F = 100.50$ USD. Cổ tức chắc chắn $D = 2.00$ USD sau 6 tháng. Lãi suất hiệu dụng $r = 4.00\%$/năm ($EAR = 1.04$). Chi phí mượn cổ phiếu để bán khống là 1.80 USD/cổ phiếu trả tại cuối năm ($T=1$).
  - Mu tuyên bố: "Giá kỳ hạn khác giá sách giáo khoa, chắc chắn có cơ hội kiếm lợi nhuận không rủi ro."
  - (a) Tính giá kỳ hạn lý thuyết bỏ qua chi phí mượn cổ phiếu và so sánh với giá niêm yết.
  - (b) Với 1,000 cổ phiếu, thiết lập giao dịch chênh lệch giá, lập bảng dòng tiền tại $t=0$, $t=0.5$ và $t=1$. Tính lợi nhuận ròng cuối cùng.
  - (c) Tìm mức phí mượn cổ phiếu hòa vốn.
  - (d) Đánh giá tuyên bố của Mu và ý nghĩa về tính hiệu quả của thị trường.
- **Lời giải chi tiết**:
  - (a) **Giá Kỳ Hạn Lý Thuyết Sách Giáo Khoa**:
    $$F^* = S_0 (1+r) - D(1+r)^{0.5} = 100(1.04) - 2.00(1.04)^{0.5} = 104.00 - 2.039608 = \mathbf{101.960392\ \text{USD}}$$
    So sánh: Giá niêm yết $F = 100.50 < F^* = 101.96$ USD $\implies$ Hợp đồng kỳ hạn đang giao dịch thấp hơn giá lý thuyết sách giáo khoa 1.46 USD/cổ phiếu.
  - (b) **Chiến Lược Arbitrage Đảo (Reverse Cash-and-Carry)**:
    - Vì $F$ rẻ hơn giá lý thuyết, chiến lược đề xuất là: **Mua Forward (Long Forward) + Bán khống Cổ phiếu (Short Stock) + Gửi tiết kiệm tiền mặt**.
    - **Lập Bảng Dòng Tiền (Quy mô 1,000 cổ phiếu)**:

| Giao dịch | Hôm nay ($t=0$) | Sau 6 tháng ($t=0.5$) | Đáo hạn ($t=1$) |
|---|---:|---:|---:|
| Mượn & Bán khống 1,000 cổ phiếu tại giá 100 | +100,000.00 USD | 0 | Trả 1,000 cổ phiếu |
| Gửi tiết kiệm tiền bán khống tại lãi suất 4% | -100,000.00 USD | 0 | +104,000.00 USD |
| Đền cổ tức cho người cho mượn cổ phiếu | 0 | -2,000.00 USD | 0 |
| Vay bù tiền đền cổ tức từ $t=0.5$ đến $t=1$ | 0 | +2,000.00 USD | $-2,000(1.04)^{0.5} = -2,039.61$ USD |
| Mua 1,000 cổ phiếu theo Long Forward ($K=100.50$) | 0 | 0 | -100,500.00 USD |
| Trả phí mượn cổ phiếu (1.80 USD/cổ phiếu) | 0 | 0 | -1,800.00 USD |
| **DÒNG TIỀN RÒNG TỔNG CỘNG** | **0.00 USD** | **0.00 USD** | **-\$339.61 USD** |

    - *Kết quả*: Sau khi trừ phí mượn chứng khoán, giao dịch **BỊ LỖ RÒNG 339.61 USD**!
  - (c) **Phí Mượn Cổ Phiếu Hòa Vốn**:
    - Lợi nhuận trước phí mượn cổ phiếu cho 1,000 cổ phiếu là:
      $$\Pi_{\text{gross}} = 104,000.00 - 2,039.61 - 100,500.00 = +1,460.39\ \text{USD}$$
    - Mức phí mượn cổ phiếu tối đa để giao dịch hòa vốn:
      $$\mathbf{c^* = \frac{1,460.39}{1,000} \approx \$1.4604/\text{cổ phiếu}}$$
  - (d) **Đánh Giá Tuyên Bố Của Mu & Bản Chất EMH**:
    - Tuyên bố của Mu là **HOÀN TOÀN SAI**. Mu đã ngây thơ áp dụng công thức sách giáo khoa phi ma sát mà quên mất **chi phí vay mượn chứng khoán thực tế (Short-sale borrowing cost)**.
    - *Ý nghĩa về thị trường hiệu quả*: Sự tồn tại của chi phí giao dịch, phí vay mượn và hạn chế bán khống tạo ra một dải biên độ không thể kinh doanh chênh lệch giá gọi là **No-Arbitrage Band**. Trong dải này, giá kỳ hạn có thể dao động tự do mà không nhà kinh doanh chênh lệch giá nào có thể trục lợi. Do đó, hiện tượng này hoàn toàn nhất quán với thị trường hiệu quả trong điều kiện có ma sát thực tế!

"""

with open(out_file, "a", encoding="utf-8") as f:
    f.write(sec3)

print("Appended Section 3 (Lecture 08 & Questions 1-5) successfully!")
