---
title: "4.2 Cấu hình phương thức thanh toán"
description: "Khai tiền mặt, chuyển khoản, ví điện tử — và chọn phương thức tiền mặt cho sổ quỹ."
---

**Đường dẫn:** *Thiết lập cửa hàng → Phương thức thanh toán*
**Việc bắt buộc kèm theo:** quay lại *Cấu hình hệ thống* chọn phương thức nào là **tiền mặt** (mục 1.1)

![Thêm phương thức thanh toán](/images/04-pttt-them.png)

## Các bước

1. Bấm **Thêm phương thức**.
2. Điền nhóm **Thông tin chung**.
3. Chọn *Loại thanh toán* là MoMo / VietQR → form hiện thêm nhóm khai kết nối.
4. Bấm **Lưu**.

## Giải thích các trường

**Thông tin chung**

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Tên phương thức | Chữ thu ngân nhìn thấy. VD "Tiền mặt", "Chuyển khoản VCB" | ✅ |
| Mã phương thức | Viết hoa, không trùng. VD `CASH`, `BANK`, `MOMO` | ✅ |
| Loại thanh toán | *Thông thường* / *MoMo* / *VietQR* | ✅ |
| Hiện tại POS | Bật = thu ngân chọn được khi thanh toán | ✅ |

**Khai kết nối (chỉ khi chọn MoMo / VietQR)**

| Loại | Cần khai |
|---|---|
| MoMo | Partner Code, Access Key, Secret Key |
| VietQR | Mã ngân hàng, số tài khoản, tên chủ tài khoản |

## Kiểm tra đã đúng

- [ ] Phương thức hiện trong danh sách, *Hiện tại POS* đang bật
- [ ] Đã gắn phương thức vào quầy POS (mục 4.1)
- [ ] Đã chọn **Phương thức tiền mặt** ở *Cấu hình hệ thống*

## Lưu ý

⚠️ **Khoá bí mật (Secret Key, Access Key) không hiện lại sau khi lưu.** Mở form Sửa thấy ô trống ghi "Để trống nếu không đổi" — để trống là **giữ khoá cũ**, chỉ điền khi thật sự muốn thay. Đây là cách bảo vệ khoá ký giao dịch: người xem được màn cấu hình không đọc trộm được khoá.

⚠️ Phương thức đã dùng trong sổ quỹ, phiếu chi, đơn mua, đơn bán hoặc đối soát ca thì **không xoá được**. Ngừng dùng thì tắt *Hiện tại POS*.

⚠️ **Chưa chọn phương thức tiền mặt ở Cấu hình hệ thống thì két không được ghi sổ** — mở/đóng ca vẫn chạy nhưng sổ quỹ đứng im.

💡 Mã phương thức không phân biệt hoa thường — đã có `CASH` thì không tạo `cash`.
