import sys

out_file = "/media/minh/DISK/Downloads/Investments_WS2026/MASTER_EXAM_PREPARATION_ULTIMATE_GUIDE.md"

header = """# BFIN INVESTMENTS (WS2026) - BÍ KÍP ÔN THI TOÀN DIỆN & GIẢI CHI TIẾT TẤT CẢ DẠNG BÀI
## MASTER EXAM STUDY BIBLE: LECTURES 01 ĐẾN 11 & TOÀN BỘ 140 CÂU THỰC HÀNH + CÂU HỎI TRÊN LỚP
**Giảng viên: Dr. Omer Cayirli | Biên soạn Chuyên sâu Chuẩn bị Thi Cuối kỳ**  
*Phương pháp Sư phạm Trực quan, Dễ hiểu, Bản chất Kinh tế & Khảo sát Toán học Chặt chẽ*  
*Trọng tâm Đặc biệt: $\ge 40\%$ Điểm thi thuộc về Chứng khoán Phái sinh (Derivatives: Lectures 09, 10, 11)*

---

# MỤC LỤC TỔNG QUAN CHIẾN LƯỢC

1. [PHẦN 1: CHIẾN LƯỢC PHÒNG THI & 12 BẪY THI CỐT TỬ (EXAM SPEED-RUN & FATAL PITFALLS)](#phần-1-chiến-lược-phòng-thi--12-bẫy-thi-cốt-tử)
   - 1.1. Ma trận Phân bổ Đề thi & Quy tắc Quản lý Thời gian (Time Management)
   - 1.2. 12 Bẫy thi Kinh điển Sinh viên hay mắc phải & Cách né tránh
   - 1.3. Cẩm nang Bấm máy Siêu tốc (Formula Cheat-Sheet & Calculator Shortcuts)
2. [PHẦN 2: CHỨNG KHOÁN PHÁI SINH CHUYÊN SÂU ($\ge 40\%$ ĐIỂM THI - LECTURES 09, 10, 11)](#phần-2-chứng-khoán-phái-sinh-chuyên-sâu)
   - 2.1. LECTURE 09: Hợp đồng Kỳ hạn (Forwards), Tương lai (Futures) & Hoán đổi (Swaps)
     - Lý thuyết Nền tảng & Cơ chế Định giá Không chênh lệch giá (No-Arbitrage)
     - Giải Chi tiết Toàn bộ Questions 1 – 11 trong Slide Lecture 09
     - Giải Chi tiết Toàn bộ Questions 6 – 15 trong File Bài tập Thực hành (Practice L08–L11)
   - 2.2. LECTURE 10: Thị trường Quyền chọn, Các Chiến lược & Ngang giá Mua – Bán (Put-Call Parity)
     - 4 Vị thế Cơ bản, Đồ thị Payoff/Profit & Điểm Hòa vốn
     - Các Chiến lược Kinh điển: Spreads, Straddles, Strangles, Collars
     - Ngang giá Mua – Bán (Put-Call Parity) & Vị thế Nhân tạo (Synthetic Positions)
     - Thực thi Sớm Quyền chọn Mỹ (American Options) & Chứng minh Định lý Merton
     - Mô hình Cấu trúc Doanh nghiệp của Merton: Vốn chủ sở hữu & Nợ dưới dạng Quyền chọn
     - Giải Chi tiết Toàn bộ Questions 1 – 10 trong Slide Lecture 10
     - Giải Chi tiết Toàn bộ Questions 16 – 25 trong File Bài tập Thực hành (Practice L08–L11)
   - 2.3. LECTURE 11: Định giá Quyền chọn - Mô hình Nhị thức (BOPM) & Black-Scholes-Merton (BSM)
     - Mô hình Cây Nhị thức 1 Thời kỳ: Danh mục Sao chép ($\Delta, B$), Giá Trạng thái ($P_u, P_d$), Xác suất Trung lập Rủi ro ($p$)
     - Mô hình Cây Nhị thức Đa Thời kỳ (Multi-Period Trees) & Thực thi Sớm American Put
     - Mô hình Black-Scholes-Merton (BSM): Công thức, Ý nghĩa $N(d_1), N(d_2)$, The Greeks & Option Beta
     - Biến động Ngụ ý (Implied Volatility) & Chỉ số VIX
     - Giải Chi tiết Toàn bộ Bài tập Lớn trong Slide Lecture 11 (Gamma, Delta, Lambda, Sigma)
     - Giải Chi tiết Toàn bộ Questions 26 – 40 trong File Bài tập Thực hành (Practice L08–L11)
3. [PHẦN 3: ĐẦU TƯ TRÁI PHIẾU & CẤU TRÚC KỲ HẠN LÃI SUẤT (FIXED INCOME - LECTURES 02, 03)](#phần-3-đầu-tư-trái-phiếu--cấu-trúc-kỳ-hạn-lãi-suất)
   - 3.1. LECTURE 02: Định giá Trái phiếu, Lợi suất (YTM) & Cấu trúc Kỳ hạn
     - 5 Định lý Malkiel về Giá Trái phiếu
     - Lãi suất Giao ngay (Spot Rates) vs Lãi suất Kỳ hạn (Forward Rates)
     - 3 Lý thuyết Cấu trúc Kỳ hạn: Pure Expectations, Liquidity Preference, Market Segmentation
     - Callable Bonds & Hiện tượng Độ lồi Âm (Negative Convexity)
     - Giải Chi tiết Toàn bộ Questions 2.1 – 2.5 trong Slide Lecture 02
   - 3.2. LECTURE 03: Duration, Convexity & Miễn dịch Rủi ro Lãi suất (Immunization)
     - Macaulay Duration vs Modified Duration
     - Quy tắc Xấp xỉ Giá Bậc 2 (Duration + Convexity Rule)
     - Miễn dịch Danh mục (Redington Immunization) & Tái cân bằng (Rebalancing)
     - Giải Chi tiết Toàn bộ Questions 3.1 – 3.7 trong Slide Lecture 03
4. [PHẦN 4: LÝ THUYẾT DANH MỤC & ĐỊNH GIÁ TÀI SẢN (PORTFOLIO THEORY & ASSET PRICING - LECTURES 04 – 08)](#phần-4-lý-thuyết-danh-mục--định-giá-tài-sản)
   - 4.1. LECTURE 04: Lợi suất, Rủi ro & Hàm Thỏa dụng (Utility & CAL) - Giải Questions 1 – 5
   - 4.2. LECTURE 05: Mô hình Lựa chọn Danh mục Markowitz & Phân bổ Vốn - Giải Questions 1 – 5
   - 4.3. LECTURE 06: Mô hình Chỉ số Đơn (SIM) & CAPM (SML vs CML, Alpha) - Giải Questions 1 – 5
   - 4.4. LECTURE 07: Mô hình Đa Nhân tố & Lý thuyết Định giá Chênh lệch (APT) - Giải Questions 1 – 6
   - 4.5. LECTURE 08: Hiệu quả Thị trường (EMH) & Tài chính Hành vi - Giải Questions 1 – 5 (Practice L08–L11)
5. [PHẦN 5: MA TRẬN PHÂN LOẠI & BẢN ĐỒ GIẢI NHANH 100 CÂU THỰC HÀNH LECTURES 01 – 07](#phần-5-ma-trận-phân-loại--bản-đồ-giải-nhanh-100-câu-thực-hành)
   - Phân loại 100 Câu hỏi theo Chuyên đề, Công thức Cốt lõi & Mẹo giải siêu tốc

---
"""

with open(out_file, "w", encoding="utf-8") as f:
    f.write(header)

print("Part 1 written successfully.")
