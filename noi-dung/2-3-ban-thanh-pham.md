---
crumb: Bước 2 · Nhập sản phẩm
---

# 2.3 Bán thành phẩm

## 1. Đường dẫn vào chức năng

Menu trái: ==Quản lý sản phẩm → Sản phẩm== (địa chỉ `/products`), bấm nút tròn **+** để mở form thêm mới (`/products/new`).

- Cần có trước: đơn vị tính ([bài 1.1](1-1-thiet-lap-don-vi-tinh.md)).
- Nên có trước: danh mục ([bài 2.1](2-1-danh-muc-san-pham.md)) và nguyên liệu ([bài 2.4](2-4-nguyen-lieu.md)).

> **Cách đặt tên:** BTP - TÊN BÁN THÀNH PHẨM
> 
> - BTP - TRÀ LÀI
> - BTP - CÀ PHÊ ĐEN PHA PHIN
> - BTP - MILKFOAM MATCHA

### Công tắc theo loại hàng

| Loại hàng                                          | Tồn kho | Có thể bán | Có thể mua | Sản xuất (Có công thức) |
| -------------------------------------------------- | ------- | ---------- | ---------- | ----------------------- |
| MAY ĐEN ĐÁ (THÀNH PHẨM - ĐƯỢC PHA CHẾ)             | ❌       | ✅          | ❌          | ✅                       |
| NL - CÀ PHÊ VIỆT PHA PHIN - 1000 - 30 (NGUYÊN LIỆU) | ✅       | ❌          | ✅          | ❌                       |
| BTP - TRÀ LÀI (BÁN THÀNH PHẨM)                     | ✅       | ❌          | ❌          | ✅                       |
| CROISSANT CLASSIC (THÀNH PHẨM - MUA SẴN BÁN LẠI)   | ✅       | ✅          | ✅          | ❌                       |

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** sáng nào quán cũng ủ sẵn **BTP - TRÀ LÀI**, mỗi mẻ 800 GR, cả ngày rót ra pha. Tồn tính theo **GRAM**.
>
> - Bật **Sản xuất (có công thức)** và **Theo dõi tồn kho**.

### Bước 1: Mở form và chọn Loại sản phẩm

- Ở menu trái, nhóm **Quản lý sản phẩm**, bấm **Sản phẩm**.
- Bấm nút tròn **+** ở góc dưới bên phải.
- Bấm ô **Loại sản phẩm**, chọn **Bán thành phẩm**.

![Bước 1: Mở form và chọn Loại sản phẩm](images/03-loai-buoc-1-chon-loai.png)

### Bước 2: Khai thông tin chính

- Điền như ảnh. **Danh mục**: tích **BÁN THÀNH PHẨM**, bấm **Xong**.

![Bước 2: Khai thông tin chính "BTP - TRÀ LÀI"](images/03-loai-buoc-2-ban-thanh-pham.png)

### Bước 3: Gạt các công tắc và lưu

- Cuộn xuống khung **Thiết lập** (cột phải).
- Gạt tắt mục **Có thể bán**.
- Bật **Sản xuất** thì ô **Giá vốn** bị khoá, giá vốn do công thức tính.
- Bấm **Lưu sản phẩm**.

![Bước 3: Gạt các công tắc và lưu](images/03-loai-buoc-3-cong-tac.png)

## 3. Giải thích các trường

### Khai bán thành phẩm

| Trường                  | Điền gì                                                                     |
| ----------------------- | --------------------------------------------------------------------------- |
| Tên sản phẩm            | Tên hiện trên màn bếp và phiếu chế biến. VD **BTP - TRÀ LÀI**               |
| Mã SP (SKU)             | Mã ngắn để tra cứu, bắt buộc. VD **BTP-TRALAI**                             |
| Đơn vị tính chính       | Đơn vị tính tồn. Chất lỏng, bột: **GRAM**                                   |
| Loại sản phẩm           | **Bán thành phẩm**                                                          |
| Giá vốn                 | **Bị khoá**, do công thức tính ([bài 3.1](3-1-cong-thuc-ban-thanh-pham.md)) |
| Sản xuất (có công thức) | **Bật**. Có công thức tạo ra bán thành phẩm                                 |
| Theo dõi tồn kho        | **Bật**. Biết bình ủ còn bao nhiêu                                          |
| Có thể bán / Có thể mua | **Tắt**. Không bán trực tiếp, không mua từ nhà cung cấp                     |

### So sánh ba loại hàng

| Loại               | Là gì                                                    | Ví dụ                                 |
| ------------------ | -------------------------------------------------------- | ------------------------------------- |
| **Nguyên liệu**    | Mua để dùng, không bán trực tiếp, dùng làm ra thứ khác   | Cà phê phin, sữa tươi, trà lài khô, ống hút |
| **Bán thành phẩm** | Quán tự làm, chưa bán cho khách, là đầu vào của món khác | BTP - TRÀ LÀI, BTP - MILKFOAM MUỐI, BTP - COLDBREW |
| **Thành phẩm**     | Món bán cho khách                                        | MAY ĐEN ĐÁ, BẠC XỈU MAY, LATTE (ICED) |

Công tắc cần bật cho từng loại: xem bảng **Công tắc theo loại hàng** ở đầu bài.

### Khi nào cần bán thành phẩm

Quán ủ sẵn một mẻ trà lài buổi sáng, cả ngày rót ra pha. Tách thành 2 bước:

- **Sáng**: lập phiếu chế biến, trừ **NL - TRÀ LÀI - 500**, nước nóng, đá; cộng 800 GR **BTP - TRÀ LÀI** vào kho ([mục 11.4](11-4-che-bien.md)).
- **Cả ngày**: mỗi ly bán ra trừ **BTP - TRÀ LÀI** theo công thức.

## 4. Lưu ý quan trọng

> - Loại sản phẩm chỉ để phân loại, hành vi do các công tắc quyết định.
> - Quán nhỏ có thể bỏ qua bán thành phẩm, cho món trừ thẳng nguyên liệu.
