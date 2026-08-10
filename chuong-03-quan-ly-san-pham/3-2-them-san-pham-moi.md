---
title: "3.2 Thêm sản phẩm mới"
description: "Khai sản phẩm mới với đầy đủ giá, đơn vị, danh mục và cờ vai trò."
---

*Quản lý sản phẩm → Sản phẩm → **Thêm sản phẩm***

Form sản phẩm chia hai cột trên cùng một màn — không còn tab, không phải bấm qua
lại. Cột trái là thứ nhập nhiều, cột phải là thứ liếc mắt kiểm tra.

![Form thêm sản phẩm](/images/03-san-pham-them.png)

## Làm từng bước

**Cột trái — Thông tin chính**

| Trường | Điền gì |
|---|---|
| **Tên sản phẩm** | Tên hiện trên bill và màn bếp. |
| **Mã SP (SKU)** | Mã ngắn để tra cứu, VD `CFSD01`. |
| **Đơn vị tính chính** | Đơn vị dùng để tính tồn. Đồ uống → *Ly*; nguyên liệu → *Gram* hoặc *ml*. |
| **Loại sản phẩm** | Thành phẩm / Bán thành phẩm / Nguyên liệu — xem [mục 3.3](/chuong-03-quan-ly-san-pham/3-3-phan-biet-nguyen-lieu-ban-thanh-pham-thanh-pham). |
| **Đơn vị tính phụ** | Các đơn vị khác cũng dùng cho hàng này (VD nhập theo *Kg*, trừ theo *Gram*). |
| **Danh mục** | Chọn một hoặc nhiều nhóm ở mục 3.1. |
| **Nhóm Addon** | Nhóm topping/mức đường sẽ hỏi khi bán món này. |

**Cột trái — Ghi chú pha chế**

- Các ô chọn ở đây (VD *ĐÁ*: ít đá / nhiều đá) là **ghi chú cho pha chế**. Thu
  ngân bấm khi bán, chữ được ghép vào tên món trên bill và màn bếp.
- **Ghi chú công thức ⚡** — văn bản tự do hiện trên màn bếp khi làm món.

**Cột phải**

| Nhóm | Nội dung |
|---|---|
| **Ảnh sản phẩm** | Ảnh JPEG/PNG/WebP tối đa 10MB, hệ thống tự nén. |
| **Giá & thuế** | *Giá bán* (giá trên POS), *Giá vốn*, *VAT bán ra*, *VAT mua vào*. |
| **Thiết lập** | 4 công tắc: Theo dõi tồn kho · Có thể bán · Có thể mua · Sản xuất. |

Bấm **Lưu sản phẩm**. Nút Lưu luôn nằm ở đáy khung, không cần cuộn xuống tìm.

## Bốn công tắc "Thiết lập" nghĩa là gì

| Công tắc | Bật khi nào | Hệ quả |
|---|---|---|
| **Theo dõi tồn kho** | Hàng cần đếm tồn: nguyên liệu, bánh đóng gói. | Xuất hiện trong màn Tồn kho, bị cộng/trừ khi nhập–bán–huỷ. |
| **Có thể bán** | Món bán cho khách. | Hiện trên màn bán hàng. |
| **Có thể mua** | Hàng mua từ nhà cung cấp. | Chọn được trong phiếu nhập hàng. |
| **Sản xuất (có công thức)** | Món pha chế từ nguyên liệu. | Mở đường dùng công thức; **giá vốn bị khoá** và do công thức tính. |

Ví dụ thường gặp:

- **Cà phê sữa** (món bán): Có thể bán ✅, Sản xuất ✅, Theo dõi tồn kho ❌
  (không đếm tồn "ly cà phê", chỉ đếm nguyên liệu).
- **Cà phê hạt** (nguyên liệu): Có thể mua ✅, Theo dõi tồn kho ✅, Có thể bán ❌.
- **Bánh mua sẵn về bán lại**: Có thể bán ✅, Có thể mua ✅, Theo dõi tồn kho ✅,
  Sản xuất ❌.

## Lưu ý nghiệp vụ

⚠️ **Bật *Sản xuất* thì ô Giá vốn chuyển sang màu xám và không nhập được.** Đây
không phải lỗi: giá vốn của món pha chế được tính từ công thức (mục 3.5) chứ
không gõ tay. Nhập tay thì mỗi lần giá nguyên liệu đổi lại phải sửa từng món.

⚠️ **Tên sản phẩm và SKU không được trùng**, kể cả khác hoa thường và kể cả với
sản phẩm đã lưu trữ. Đây là chặn có chủ đích để tránh hai dòng "Cà phê sữa" song
song làm loạn báo cáo.

⚠️ Sản phẩm đã phát sinh giao dịch (đã bán, đã nhập, có tồn khác 0, đang là
nguyên liệu trong công thức, đang là topping) thì **không xoá được**. Hệ thống
liệt kê rõ nơi đang dùng. Ngừng bán thì dùng **Lưu trữ**.

💡 Sản phẩm mới tạo, chưa bán chưa nhập, thì xoá thoải mái.
