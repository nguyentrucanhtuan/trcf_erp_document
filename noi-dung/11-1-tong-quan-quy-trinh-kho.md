---
crumb: Bước 11 · Quy trình vận hành kho
---

# 11.1 Tổng quan quy trình kho

## 1. Đường dẫn vào chức năng

Trang chủ: khối ==Tính năng cho bạn== (địa chỉ `/`).

hoặc menu trái: nhóm ==Vận hành== (Mua hàng, Chuyển kho, Chế biến, Huỷ hàng, Kiểm kê).

hoặc ở màn ==Bán hàng → Vận hành== (địa chỉ `/pos-operations`).

- Dùng để: tra nhanh xem tình huống đang gặp thì lập phiếu gì.

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** nhà cung cấp vừa giao 5 kg cà phê hạt tới quán.
>
> - Ở Trang chủ, bấm ô **Nhập hàng**.
> - Lập đơn, bấm **Xác nhận** rồi **Nhận hàng**: kho được cộng 5 kg.

### Bước 1: Mở Trang chủ

- Bấm **Trang chủ** ở đầu menu trái.
- Khối **Tính năng cho bạn** có các ô: **Nhập hàng**, **Chuyển kho**, **Chế biến**, **Huỷ hàng**, **Kiểm kê**, **Tồn kho**, **Chi phí**.
- Bấm ô đúng với tình huống (xem bảng tra nhanh bên dưới).

![Bước 1: Mở Trang chủ](images/05-van-hanh-hub.png)

### Bước 2: Hoặc chọn ở menu trái

- Ở menu trái, kéo xuống nhóm **Vận hành**.
- Có đủ các trang: **Mua hàng**, **Chuyển kho**, **Chế biến**, **Huỷ hàng**, **Kiểm kê**.
- Nhóm **Báo cáo** ngay dưới có **Kiểm soát vận hành** ([bài 11.7](11-7-de-xuat-nhap-hang.md)).

![Bước 2: Hoặc chọn ở menu trái](images/05-van-hanh-buoc-2-menu.png)

## 3. Giải thích các trường

### Bảng tra nhanh

| Ô / trang | Dùng khi | Kho bị ảnh hưởng | Chi tiết |
| --- | --- | --- | --- |
| **Nhập hàng** (Mua hàng) | Nhà cung cấp giao hàng tới quán | Cộng vào kho | [11.2](11-2-nhap-hang.md) |
| **Chuyển kho** | Lấy hàng từ kho tổng ra quầy | Trừ kho nguồn, cộng kho đích | [11.3](11-3-chuyen-kho.md) |
| **Chế biến** | Ủ cà phê cốt, nấu syrup | Trừ nguyên liệu, cộng bán thành phẩm | [11.4](11-4-che-bien.md) |
| **Huỷ hàng** | Hàng hỏng, hết hạn, làm rơi | Trừ kho | [11.5](11-5-huy-hang.md) |
| **Kiểm kê** | Đếm thực tế, chỉnh cho khớp | Điều chỉnh về đúng số đếm | [11.6](11-6-kiem-kho.md) |
| **Chi phí** | Trả tiền điện, tiền ship, mua đồ lặt vặt | Không đụng kho, ghi sổ quỹ | [10.2](10-2-tao-chi-phi.md) |
| **Tồn kho** | Xem nhanh hàng nào sắp hết | Chỉ xem | [11.7](11-7-de-xuat-nhap-hang.md) |

### Sai thì sửa bằng phiếu ngược lại

| Sai gì | Sửa bằng |
| --- | --- |
| Nhập nhầm | Phiếu trả hàng nhà cung cấp |
| Xuất nhầm | Phiếu nhập bù |
| Số lệch không rõ nguyên nhân | Phiếu kiểm kho |

## 4. Lưu ý quan trọng

> [!TIP]
> **1. Phiếu mới tạo ở trạng thái Nháp.**
>
> - Chưa đụng gì tới kho.
> - Tạo nhầm thì xoá thoải mái.

> [!WARNING]
> **2. Kho chỉ thay đổi khi bấm Xác nhận.**
>
> - Hoặc *Nhận hàng* / *Hoàn thành* tuỳ loại phiếu.

> [!CAUTION]
> **3. Phiếu đã xác nhận không sửa, không xoá được.**
>
> - Sai thì lập phiếu ngược lại.

## Kiểm tra đã đúng

- [ ] Biết tình huống nào dùng ô nào
- [ ] Phiếu mới tạo vẫn ở trạng thái Nháp cho tới khi bấm Xác nhận
