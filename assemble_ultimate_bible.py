import sys

guide_path = "MASTER_EXAM_PREPARATION_ULTIMATE_GUIDE.md"
prac_path = "MASTER_PRACTICE_Q01_Q100_SOLUTIONS.md"

with open(guide_path, "r", encoding="utf-8") as f:
    guide = f.read()

with open(prac_path, "r", encoding="utf-8") as f:
    prac = f.read()

# 1. Update Table of Contents
toc_start = guide.find("# MỤC LỤC TỔNG QUAN CHIẾN LƯỢC")
toc_end = guide.find("# PHẦN 1: CHIẾN LƯỢC PHÒNG THI")

new_toc = r"""# MỤC LỤC TỔNG QUAN CHIẾN LƯỢC (STRATEGIC TABLE OF CONTENTS)

1. [PHẦN 1: CHIẾN LƯỢC PHÒNG THI, 12 BẪY TỬ HUYỆT & CẨM NANG BẤM MÁY SIÊU TỐC](#phần-1-chiến-lược-phòng-thi--12-bẫy-thi-cốt-tử)
   - 1.1. Ma trận Phân bổ Đề thi & Quy tắc Quản lý Thời gian (Time Management)
   - 1.2. 12 Bẫy thi Kinh điển Sinh viên hay mắc phải & Cách né tránh
   - 1.3. Cẩm nang Bấm máy Siêu tốc (Formula Cheat-Sheet & Calculator Shortcuts)
2. [PHẦN 2: CHỨNG KHOÁN PHÁI SINH CHUYÊN SÂU ($\ge 40\%$ ĐIỂM THI - LECTURES 09, 10, 11)](#phần-2-chứng-khoán-phái-sinh-chuyên-sâu)
   - 2.1. LECTURE 09: Hợp đồng Kỳ hạn (Forwards), Tương lai (Futures) & Hoán đổi (Swaps)
     - Khung lý thuyết & Bản chất kinh tế
     - Giải chi tiết In-Class Questions 1 – 11 (Song ngữ Anh - Việt)
     - Giải chi tiết Practice Questions 6 – 15 (Song ngữ Anh - Việt)
   - 2.2. LECTURE 10: Thị trường Quyền chọn, Các Chiến lược & Ngang giá Mua – Bán (Put-Call Parity)
     - 4 Vị thế cơ bản, Đồ thị Payoff/Profit, Spreads, Straddles, Collars
     - Ngang giá Mua – Bán (Put-Call Parity) & Vị thế nhân tạo
     - Mô hình Cấu trúc Doanh nghiệp của Merton: Định giá Nợ & Vốn chủ sở hữu
     - Giải chi tiết In-Class Questions 1 – 10 (Song ngữ Anh - Việt)
     - Giải chi tiết Practice Questions 16 – 25 (Song ngữ Anh - Việt)
   - 2.3. LECTURE 11: Định giá Quyền chọn - Mô hình Nhị thức (BOPM) & Black-Scholes-Merton (BSM)
     - Mô hình Cây Nhị thức 1 thời kỳ & đa thời kỳ (Replication, State Prices, Risk-Neutral, American Early Exercise)
     - Mô hình Black-Scholes-Merton: $d_1, d_2, N(d)$, Greeks & Option Beta
     - Giải chi tiết Bài tập lớn In-Class Slide Lecture 11 (Gamma, Delta, Lambda, Theta) (Song ngữ)
     - Giải chi tiết Practice Questions 26 – 40 (Song ngữ Anh - Việt)
3. [PHẦN 3: LECTURE 08: HIỆU QUẢ THỊ TRƯỜNG (EMH) & TÀI CHÍNH HÀNH VI](#phần-3-lecture-08-hiệu-quả-thị-trường--tài-chính-hành-vi)
   - 3.1. Lý thuyết 3 cấp độ EMH, Vấn đề Giả thuyết Kép & 5 Thiên lệch tâm lý
   - 3.2. Giải chi tiết Practice Questions 1 – 5 (Song ngữ Anh - Việt)
4. [PHẦN 4: TOÀN BỘ CÂU HỎI TRÊN LỚP (IN-CLASS PROOFS & CONCEPTUAL) LECTURES 01 ĐẾN 07](#phần-4-toàn-bộ-câu-hỏi-trên-lớp-in-class-questions--proofs-từ-lecture-01-đến-lecture-07)
   - 4.1. LECTURE 01: Môi trường Đầu tư & Công cụ
   - 4.2. LECTURE 02: In-Class Questions 2.1 – 2.5 (Spot, Forward, Accrued Interest, Callable Bond, HPR vs YTM)
   - 4.3. LECTURE 03: In-Class Questions 3.1 – 3.7 (Macaulay vs Modified Duration, Convexity xấp xỉ, Redington Immunization)
   - 4.4. LECTURE 04: In-Class Questions 1 – 5 (Arithmetic vs Geometric Mean, Utility, CAL, Sharpe, y*)
   - 4.5. LECTURE 05: In-Class Questions 1 – 5 (Markowitz MVP, Tangency Portfolio, Two-Fund Separation)
   - 4.6. LECTURE 06: In-Class Questions 1 – 5 (Single-Index Model OLS, CAPM, SML vs CML, Jensen's Alpha, Excel LINEST)
   - 4.7. LECTURE 07: In-Class Questions 1 – 6 (Multifactor Model, APT Pure Arbitrage, Fama-French 3 nhân tố, Disappearing Alpha)
5. [PHẦN 5: TOÀN BỘ 100 CÂU HỎI THỰC HÀNH LECTURES 01 ĐẾN 07 (QUESTIONS 01 – 100) (SONG NGỮ ANH - VIỆT CHI TIẾT 100%)](#phần-5-toàn-bộ-100-câu-hỏi-thực-hành-lectures-01-đến-07-questions-01--100)
   - Ma trận Phân loại & Bản đồ Giải nhanh 30 giây
   - Bài tập Lecture 01 (Questions 01 – 08)
   - Bài tập Lecture 02 (Questions 09 – 24)
   - Bài tập Lecture 03 (Questions 25 – 38)
   - Bài tập Lecture 04 (Questions 39 – 56)
   - Bài tập Lecture 05 (Questions 57 – 71)
   - Bài tập Lecture 06 (Questions 72 – 86)
   - Bài tập Lecture 07 (Questions 87 – 100)
6. [PHẦN 6: DERIVATIVES MASTER CHEAT-SHEET & 10 QUY TẮC BẤT BIẾN KHI THI ($\ge 40\%$ ĐIỂM SỐ)](#phần-6-derivatives-master-cheat-sheet--40-điểm-số-bài-thi)
   - Bảng Tổng hợp Công thức Phái sinh Toàn diện
   - Mười Quy tắc Vàng Khi Làm Bài Thi Phái sinh

---

"""

guide_updated_toc = guide[:toc_start] + new_toc + guide[toc_end:]

# 2. Extract full 100 practice questions from prac
prac_start_target = "# PRACTICE QUESTIONS: LECTURE 01 (QUESTIONS 1 - 8)"
prac_start = prac.find(prac_start_target)
prac_body = prac[prac_start:]

# 3. Locate insertion point before Part 6 in guide
p6_target = "# PHẦN 6: DERIVATIVES MASTER CHEAT-SHEET"
p6_idx = guide_updated_toc.find(p6_target)

# We want Part 5 heading to be:
part5_header = r"""
---

# PHẦN 5: TOÀN BỘ 100 CÂU HỎI THỰC HÀNH LECTURES 01 ĐẾN 07 (QUESTIONS 01 – 100)
## (BÀI TẬP THỰC HÀNH & LỜI GIẢI CHI TIẾT 100% SONG NGỮ ANH - VIỆT)

"""

# In guide_updated_toc, replace the existing "# PHẦN 5: BẢN ĐỒ CHIẾN THUẬT..." up to p6_target
p5_target = "# PHẦN 5: BẢN ĐỒ CHIẾN THUẬT & TÓM TẮT 100 CÂU THỰC HÀNH LECTURES 01 – 07"
p5_idx = guide_updated_toc.find(p5_target)

# The content between p5_idx and p6_idx is the summary table. We keep the summary table and append the full 100 questions after it!
summary_table_section = guide_updated_toc[p5_idx:p6_idx]

part5_full_section = summary_table_section + "\n---\n\n" + prac_body + "\n\n---\n\n"

final_content = guide_updated_toc[:p5_idx] + part5_full_section + guide_updated_toc[p6_idx:]

with open(guide_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print(f"Successfully assembled {guide_path}!")
print(f"Total characters: {len(final_content):,}")
print(f"Total lines: {final_content.count(chr(10)):,}")
