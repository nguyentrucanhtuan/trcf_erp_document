---
title: "5.3 Tổng quan quy trình quản lý kho"
description: "Bảng tra nhanh: việc nào dùng phiếu nào, kho bị ảnh hưởng ra sao."
---

**Đường dẫn:** Bấm **VẬN HÀNH** trên màn bán hàng
**Dùng để:** Tra nhanh xem tình huống đang gặp thì lập phiếu gì

![Màn vận hành](/images/05-van-hanh-hub.png)

## Bảng tra nhanh

| Ô | Dùng khi | Kho bị ảnh hưởng |
|---|---|---|
| **Nhập hàng** | Nhà cung cấp giao hàng tới quán | Cộng vào kho |
| **Chuyển kho** | Lấy hàng từ kho tổng ra quầy | Trừ kho nguồn, cộng kho đích |
| **Chế biến** | Ủ cà phê cốt, nấu syrup | Trừ nguyên liệu, cộng bán thành phẩm |
| **Huỷ** | Hàng hỏng, hết hạn, làm rơi | Trừ kho |
| **Kiểm tồn** | Đếm thực tế, chỉnh cho khớp | Điều chỉnh về đúng số đếm |
| **Chi phí** | Trả tiền điện, tiền ship, mua đồ lặt vặt | Không đụng kho — ghi sổ quỹ |
| **Cần nhập hàng** | Xem nhanh hàng nào sắp hết | Chỉ xem |

## Ba quy tắc đúng cho mọi phiếu kho

1. Phiếu mới tạo ở trạng thái **Nháp** — **chưa đụng gì tới kho**. Tạo nhầm thì xoá thoải mái.
2. Kho chỉ thay đổi khi bấm **Xác nhận** (hoặc *Nhận hàng* / *Hoàn thành* tuỳ loại phiếu).
3. Phiếu đã xác nhận **không sửa, không xoá được**. Sai thì lập phiếu ngược lại.

**Lập phiếu ngược lại nghĩa là:**

| Sai gì | Sửa bằng |
|---|---|
| Nhập nhầm | Phiếu trả hàng nhà cung cấp |
| Xuất nhầm | Phiếu nhập bù |
| Số lệch không rõ nguyên nhân | Phiếu kiểm kho |

Chi tiết từng loại phiếu ở [chương 6](/chuong-06-nghiep-vu-kho/6-1-nhap-chi-phi).
