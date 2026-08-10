---
title: "6.4 Chế biến bán thành phẩm"
description: "Ủ cà phê cốt, nấu syrup — trừ nguyên liệu, cộng bán thành phẩm."
---

**Đường dẫn:** *Vận hành → Chế biến*
**Dùng khi:** Quán tự làm ra thứ gì đó — ủ cà phê cốt, nấu syrup, làm sốt
**Cần có trước:** Công thức (BOM) của thành phẩm ([mục 3.5](/chuong-03-quan-ly-san-pham/3-5-cau-hinh-cong-thuc-va-bien-the))

![Tạo phiếu chế biến](/images/06-che-bien.png)

## Các bước

1. Bấm **Tạo phiếu chế biến**.
2. Chọn *Sản phẩm thành phẩm* → hệ thống **tự nạp nguyên liệu từ công thức**.
3. Chọn *Kho trừ nguyên liệu* và *Kho nhập thành phẩm*.
4. Nhập *Số lượng thành phẩm* → danh sách nguyên liệu tự nhân lên theo.
5. Chỉnh số lượng nguyên liệu nếu thực tế dùng khác định mức.
6. Bấm **Lưu nháp** → **Xác nhận chế biến**.

## Giải thích các trường

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Sản phẩm thành phẩm | Thứ làm ra. Phải có công thức | ✅ |
| Kho trừ nguyên liệu | Kho lấy nguyên liệu | ✅ |
| Kho nhập thành phẩm | Kho nhận thành phẩm | ✅ |
| Số lượng thành phẩm | Số làm được thật | ✅ |
| Danh sách nguyên liệu | Tự nạp từ công thức, **sửa được** | ✅ |

## Kiểm tra đã đúng

- [ ] Tồn nguyên liệu giảm đúng số đã khai
- [ ] Tồn bán thành phẩm tăng đúng số làm được

## Lưu ý

⚠️ **Số lượng trên phiếu là nguồn sự thật, không phải công thức.** Công thức chỉ điền sẵn cho nhanh. Hôm nay dùng nhiều hơn định mức thì cứ sửa số trên phiếu — hệ thống trừ đúng số bạn khai.

⚠️ **Đã xác nhận thì không xác nhận lại được.** Hệ thống khoá để tránh trừ kho hai lần khi hai người cùng bấm.

💡 Chế biến **không đụng tới tiền** — chỉ chuyển giá trị từ nguyên liệu sang bán thành phẩm. Phiếu nhẹ nhất chương này.

💡 Chưa có công thức thì phiếu không tự nạp nguyên liệu được. Tạo công thức trước.
