---
title: "5.3 Tổng quan quy trình quản lý kho"
description: "Bức tranh tổng thể sáu nghiệp vụ kho và khi nào dùng cái nào."
---

Trong ca, ngoài bán hàng còn phát sinh việc đụng tới kho. Tất cả gom vào một chỗ:
bấm **VẬN HÀNH** trên màn bán hàng.

![Màn vận hành](/images/05-van-hanh-hub.png)

| Ô | Khi nào dùng | Kho bị ảnh hưởng ra sao |
|---|---|---|
| **Nhập hàng** | Nhà cung cấp giao hàng tới quán. | Cộng vào kho |
| **Chuyển kho** | Lấy hàng từ kho tổng ra quầy. | Trừ kho nguồn, cộng kho đích |
| **Chế biến** | Ủ cà phê cốt, nấu syrup. | Trừ nguyên liệu, cộng bán thành phẩm |
| **Huỷ** | Hàng hỏng, hết hạn, làm rơi. | Trừ kho |
| **Kiểm tồn** | Đếm thực tế, chỉnh cho khớp. | Điều chỉnh về đúng số đếm |
| **Chi phí** | Trả tiền điện, tiền ship, mua đồ lặt vặt. | Không đụng kho, ghi sổ quỹ |
| **Cần nhập hàng** | Xem nhanh hàng nào sắp hết. | Chỉ xem |

**Nguyên tắc chung, đúng cho mọi phiếu kho:**

1. Phiếu mới tạo ở trạng thái **Nháp** — **chưa đụng gì tới kho**. Tạo nhầm thì
   xoá thoải mái.
2. Kho chỉ thay đổi khi bấm **Xác nhận** (hoặc *Nhận hàng*, *Hoàn thành* tuỳ
   loại phiếu).
3. Phiếu đã xác nhận **không sửa, không xoá được**. Sai thì lập phiếu ngược lại
   (nhập nhầm → lập phiếu trả hàng; xuất nhầm → lập phiếu nhập bù).

Chi tiết từng loại phiếu ở [chương 6](/chuong-06-nghiep-vu-kho/6-1-nhap-chi-phi).
