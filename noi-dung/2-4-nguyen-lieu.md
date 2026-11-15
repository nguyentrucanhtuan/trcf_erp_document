---
crumb: Bước 2 · Nhập sản phẩm
---

# 2.4 Nguyên liệu

## 1. Đường dẫn vào chức năng

Menu trái: ==Quản lý sản phẩm → Sản phẩm== (địa chỉ `/products`), bấm nút tròn **+** để mở form thêm mới (`/products/new`).

- Cần có trước: đơn vị tính ([bài 1.1](1-1-thiet-lap-don-vi-tinh.md)).

### Công tắc theo loại hàng

| Loại hàng                                          | Tồn kho | Có thể bán | Có thể mua | Sản xuất (Có công thức) |
| -------------------------------------------------- | ------- | ---------- | ---------- | ----------------------- |
| MAY ĐEN ĐÁ (THÀNH PHẨM - ĐƯỢC PHA CHẾ)             | ❌       | ✅          | ❌          | ✅                       |
| NL - CÀ PHÊ VIỆT PHA PHIN - 1000 - 30 (NGUYÊN LIỆU) | ✅       | ❌          | ✅          | ❌                       |
| BTP - TRÀ LÀI (BÁN THÀNH PHẨM)                     | ✅       | ❌          | ❌          | ✅                       |
| CROISSANT CLASSIC (THÀNH PHẨM - MUA SẴN BÁN LẠI)   | ✅       | ✅          | ✅          | ❌                       |

## 2. Ví dụ nền và các bước thực hiện

> **Cách đặt tên**: NL - TÊN NGUYÊN LIỆU - KHỐI LƯỢNG BÊN TRONG - KHỐI LƯỢNG VỎ.
> 
> **Ví dụ cách đặt tên:** 
> - NL - CÀ PHÊ VIỆT PHA PHIN - 1000 - 30 (túi cà phê 1000 GRAM, vỏ túi 30 GRAM)
> - NL - SỮA TƯƠI - 950 - 40 (hộp sữa 950 GRAM, vỏ hộp 40 GRAM)
> - NL - SYRUP MAPLE - 1000 - 617 (chai syrup 1000 GRAM, vỏ chai thuỷ tinh 617 GRAM)

> **Ví dụ:** thêm nguyên liệu **NL - CÀ PHÊ VIỆT PHA PHIN - 1000 - 30**: nhà cung cấp giao theo túi 1000 GR, pha chế trừ theo gram.
>
> - Mua về để pha MAY ĐEN ĐÁ, BTP - CÀ PHÊ ĐEN PHA PHIN, không bán trực tiếp.
> - Bật **Theo dõi tồn kho** và **Có thể mua**.

### Bước 1: Mở form và chọn Loại sản phẩm

- Ở menu trái, nhóm **Quản lý sản phẩm**, bấm **Sản phẩm**.
- Bấm nút tròn **+** ở góc dưới bên phải.
- Bấm ô **Loại sản phẩm**, chọn **Nguyên liệu**.

![Bước 1: Mở form và chọn Loại sản phẩm](images/03-san-pham-nguyen-lieu-1.png)

### Bước 2: Khai thông tin chính

- Điền như ảnh. **Đơn vị tính phụ** và **Danh mục**: tích xong bấm **Xong**.
- **Đơn vị tính chính** chọn **GRAM** (đã tạo ở [bài 1.1](1-1-thiet-lap-don-vi-tinh.md)); **TÚI 1000GR** để nhập hàng theo túi.

![Bước 2: Khai thông tin chính "NL - CÀ PHÊ VIỆT PHA PHIN - 1000 - 30"](images/03-san-pham-nguyen-lieu-2.png)

### Bước 3: Gạt các công tắc và lưu

- Cuộn xuống khung **Thiết lập** (cột phải).
- Gạt công tắc như ảnh. **Có thể bán** mặc định bật, phải gạt tắt.
- Bấm **Lưu sản phẩm**.

![Bước 3: Gạt các công tắc và lưu](images/03-nguyen-lieu-buoc-3-cong-tac.png)

## 3. Giải thích các trường

### Khai nguyên liệu

| Trường                | Điền gì                                                                               |
| --------------------- | ------------------------------------------------------------------------------------- |
| Tên sản phẩm          | VD **NL - CÀ PHÊ VIỆT PHA PHIN - 1000 - 30**, **NL - SỮA ĐẶC - 1250**, **NL - ĐƯỜNG CÁT** |
| Mã SP (SKU)           | Mã ngắn để tra cứu, bắt buộc. VD **NL-CAPHEVIETPHAPHIN**                              |
| Đơn vị tính chính     | Đơn vị tính tồn. Nên chọn đơn vị nhỏ nhất dùng trừ kho, VD **GRAM**                   |
| Đơn vị tính phụ       | Đơn vị khác dùng cho hàng này (nhập theo **TÚI 1000GR**, trừ theo **GRAM**)           |
| Loại sản phẩm         | **Nguyên liệu**                                                                       |
| Giá vốn               | Giá nhập. Tự cập nhật mỗi lần nhập hàng ([bài 11.2](11-2-nhap-hang.md))               |
| Theo dõi tồn kho      | **Bật**. Hiện ở màn Tồn kho, bị cộng/trừ khi nhập, chế biến, bán, huỷ                 |
| Có thể mua            | **Bật**. Chọn được trong phiếu nhập hàng                                              |
| Có thể bán / Sản xuất | **Tắt**                                                                               |

### So sánh ba loại hàng

| Loại               | Là gì                                                    | Ví dụ                                 |
| ------------------ | -------------------------------------------------------- | ------------------------------------- |
| **Nguyên liệu**    | Mua để dùng, không bán trực tiếp, dùng làm ra thứ khác   | Cà phê phin, sữa tươi, trà lài khô, ống hút |
| **Bán thành phẩm** | Quán tự làm, chưa bán cho khách, là đầu vào của món khác | BTP - TRÀ LÀI, BTP - MILKFOAM MUỐI, BTP - COLDBREW |
| **Thành phẩm**     | Món bán cho khách                                        | MAY ĐEN ĐÁ, BẠC XỈU MAY, LATTE (ICED) |

Công tắc cần bật cho từng loại: xem bảng **Công tắc theo loại hàng** ở đầu bài.

## 4. Lưu ý quan trọng

> - Chưa nhập hàng lần nào thì giá vốn là 0, giá vốn món sẽ thiếu.
> - Đơn vị trong công thức được khác đơn vị tồn kho, hệ thống tự quy đổi.
