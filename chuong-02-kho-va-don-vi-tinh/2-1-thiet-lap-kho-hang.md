---
title: "2.1 Thiết lập kho hàng"
description: "Tạo kho tổng và kho quầy — 3 trường, làm trước khi tạo sản phẩm."
---

**Đường dẫn:** *Quản lý kho → Kho hàng*
**Khi nào:** Một lần khi cài đặt, **trước** khi tạo sản phẩm
**Vì sao:** Chưa có kho thì không nhập được hàng, không bán được

![Danh sách kho](/images/02-kho-danh-sach.png)

## Các bước

1. Bấm **Thêm kho**.
2. Điền 3 trường theo bảng dưới.
3. Bấm **Lưu**.
4. Lặp lại cho kho thứ hai (nếu tách kho tổng / kho quầy).

![Thêm kho mới](/images/02-kho-them-moi.png)

## Giải thích các trường

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Mã kho | Chuỗi ngắn không dấu, viết hoa. VD `KHO-TONG`, `KHO-QUAY` | ✅ |
| Tên kho | Tên người đọc hiểu. VD "Kho tổng", "Kho quầy pha chế" | ✅ |
| Địa chỉ | Địa chỉ thực tế | — |

## Nên chia mấy kho

| Cách chia | Khi nào dùng |
|---|---|
| **2 kho**: Kho tổng + Kho quầy | Có chỗ chứa riêng. Biết được "còn bao nhiêu trong kho tổng để tiếp cho quầy". |
| **1 kho** | Quán nhỏ, một chỗ chứa duy nhất. Ở *Cấu hình hệ thống* chọn cùng kho đó cho tất cả các ô. |

## Kiểm tra đã đúng

- [ ] Kho hiện trong danh sách, trạng thái **Hoạt động**
- [ ] Đã quay lại *Cấu hình hệ thống* chọn kho cho 6 ô kho mặc định

## Lưu ý

⚠️ **Kho đã phát sinh giao dịch thì không xoá được.** Bấm xoá sẽ nhận thông báo liệt kê chỗ đang dùng (tồn kho, phiếu nhập, phiếu chuyển, phiếu kiểm). Kho không dùng nữa thì **lưu trữ**, đừng xoá.

⚠️ Kho đang là kho mặc định trong *Cấu hình hệ thống* cũng không xoá được — phải đổi cấu hình sang kho khác trước.

💡 Kho vừa tạo chưa nhập gì thì xoá bình thường. Hệ thống phân biệt được "kho trống mới tạo" và "kho đã có lịch sử".
