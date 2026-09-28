---
title: "2.1 Thiết lập kho hàng"
---

- **Đường dẫn:** *Quản lý kho → Kho hàng*.

![Danh sách kho](/images/02-kho-danh-sach.png)

## Các bước

1. Bấm **Thêm kho**.
2. Điền 3 trường theo bảng dưới.
3. Bấm **Lưu**.
4. Lặp lại cho kho thứ hai (nếu tách kho tổng / kho quầy).

![Thêm kho mới](/images/02-kho-them-moi.png)

## Giải thích các trường

| Trường  | Điền gì                                                   | Bắt buộc |
| ------- | --------------------------------------------------------- | -------- |
| Mã kho  | Chuỗi ngắn không dấu, viết hoa. VD `KHO-TONG`, `KHO-QUAY` | ✅        |
| Tên kho | Tên người đọc hiểu. VD "KHO TỔNG", "KHO QUẦY"             | ✅        |
| Địa chỉ | Địa chỉ thực tế                                           | —        |

## Nên chia mấy kho

| Cách chia                       | Dùng khi               | Được gì                                                      |
| ------------------------------- | ---------------------- | ------------------------------------------------------------ |
| **2 kho** — Kho tổng + Kho quầy | Có chỗ chứa riêng      | Biết còn bao nhiêu trong kho tổng để tiếp cho quầy           |
| **1 kho**                       | Quán nhỏ, một chỗ chứa | Đơn giản. Chọn kho đó cho tất cả các ô ở *Cấu hình hệ thống* |

## Kiểm tra đã đúng

- [ ] Kho hiện trong danh sách, trạng thái **Hoạt động**
- [ ] Đã quay lại *Cấu hình hệ thống* chọn kho cho 6 ô kho mặc định

## Lưu ý

⚠️ **Kho đã phát sinh giao dịch thì không xoá được.**. Kho không dùng nữa thì **lưu trữ**, đừng xoá.

⚠️ Kho đang là kho mặc định trong *Cấu hình hệ thống* cũng không xoá được — phải đổi cấu hình sang kho khác trước.

💡 Kho vừa tạo chưa nhập gì thì xoá bình thường.