---
title: "3.2 Thêm sản phẩm mới"
---

- **Đường dẫn:** *Quản lý sản phẩm → Sản phẩm → Thêm sản phẩm*.
- **Cần có trước:** đơn vị tính (2.2), danh mục (3.1)

![Form thêm sản phẩm](/images/03-san-pham-them.png)

## Các bước

1. Bấm **Thêm sản phẩm**.
2. Cột trái: khai thông tin chính + ghi chú pha chế.
3. Cột phải: khai ảnh, giá, và **4 công tắc**.
4. Bấm **Lưu sản phẩm** (nút luôn ở đáy khung, không cần cuộn).

## Giải thích các trường

**Cột trái — Thông tin chính**

| Trường              | Điền gì                                                                                                                                | Bắt buộc |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Tên sản phẩm        | Tên hiện trên bill và màn bếp                                                                                                          | ✅        |
| Mã SP (SKU)         | Mã ngắn để tra cứu, VD `CFSD01`                                                                                                        | —        |
| Đơn vị tính chính   | Đơn vị tính tồn. Đồ uống → *Ly* · nguyên liệu → *Gram* / *ml*                                                                          | ✅        |
| Loại sản phẩm       | Thành phẩm / Bán thành phẩm / Nguyên liệu → [mục 3.3](/chuong-03-quan-ly-san-pham/3-3-phan-biet-nguyen-lieu-ban-thanh-pham-thanh-pham) | —        |
| Đơn vị tính phụ     | Đơn vị khác cũng dùng cho hàng này (nhập theo *Kg*, trừ theo *Gram*)                                                                   | —        |
| Danh mục            | Một hoặc nhiều nhóm ở mục 3.1                                                                                                          | —        |
| Nhóm Addon          | Nhóm topping / mức đường sẽ hỏi khi bán món này                                                                                        | —        |
| Ghi chú pha chế     | Ô chọn (VD ĐÁ: ít/nhiều) — thu ngân bấm khi bán, chữ ghép vào tên món                                                                  | —        |
| Ghi chú công thức ⚡ | Văn bản tự do hiện trên màn bếp khi làm món                                                                                            | —        |

**Cột phải**

| Trường                   | Điền gì                                           |
| ------------------------ | ------------------------------------------------- |
| Ảnh sản phẩm             | JPEG/PNG/WebP tối đa 10MB, hệ thống tự nén        |
| Giá bán                  | Giá trên POS                                      |
| Giá vốn                  | Giá nhập. **Bị khoá** nếu bật công tắc *Sản xuất* |
| VAT bán ra / VAT mua vào | Thuế suất áp cho món                              |

## Bốn công tắc — quyết định hành vi hệ thống

| Công tắc                | Bật khi                                      | Hệ quả                                                          |
| ----------------------- | -------------------------------------------- | --------------------------------------------------------------- |
| Theo dõi tồn kho        | Hàng cần đếm tồn: nguyên liệu, bánh đóng gói | Hiện ở màn Tồn kho, bị cộng/trừ khi nhập–bán–huỷ                |
| Có thể bán              | Món bán cho khách                            | Hiện trên màn bán hàng                                          |
| Có thể mua              | Hàng mua từ nhà cung cấp                     | Chọn được trong phiếu nhập hàng                                 |
| Sản xuất (có công thức) | Món pha chế từ nguyên liệu                   | Mở đường dùng công thức; **giá vốn bị khoá**, do công thức tính |

**Ba mẫu thường gặp:**

| Loại hàng                | Tồn kho | Bán | Mua | Sản xuất |
| ------------------------ | ------- | --- | --- | -------- |
| Cà phê sữa (món pha chế) | ❌       | ✅   | ❌   | ✅        |
| Cà phê hạt (nguyên liệu) | ✅       | ❌   | ✅   | ❌        |
| Bánh mua sẵn bán lại     | ✅       | ✅   | ✅   | ❌        |

## Lưu ý

⚠️ **Bật *Sản xuất* thì ô Giá vốn xám lại, không nhập được.** Không phải lỗi — giá vốn món pha chế do công thức tính ([mục 3.5](/chuong-03-quan-ly-san-pham/3-5-cau-hinh-cong-thuc-va-bien-the)).

⚠️ **Tên và SKU không được trùng**, kể cả khác hoa thường và kể cả với sản phẩm đã lưu trữ. Chặn để tránh hai dòng "Cà phê sữa" song song làm loạn báo cáo.

⚠️ Sản phẩm đã bán / đã nhập / tồn khác 0 / đang là nguyên liệu trong công thức / đang là topping thì **không xoá được**. Ngừng bán thì dùng **Lưu trữ**.

💡 Sản phẩm mới tạo chưa bán chưa nhập thì xoá thoải mái.
