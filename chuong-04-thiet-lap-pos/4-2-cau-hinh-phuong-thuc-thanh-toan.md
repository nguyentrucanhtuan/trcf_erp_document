---
title: "4.2 Cấu hình phương thức thanh toán"
description: "Khai tiền mặt, chuyển khoản, ví điện tử và chọn phương thức tiền mặt cho sổ quỹ."
---

*Thiết lập cửa hàng → Phương thức thanh toán*

![Thêm phương thức thanh toán](/images/04-pttt-them.png)

## Làm từng bước

1. Bấm **Thêm phương thức**.
2. Nhóm **Thông tin chung**:

   | Trường | Điền gì |
   |---|---|
   | **Tên phương thức** | Chữ thu ngân nhìn thấy. VD "Tiền mặt", "Chuyển khoản VCB". |
   | **Mã phương thức** | Viết hoa, không trùng. VD `CASH`, `BANK`, `MOMO`. |
   | **Loại thanh toán** | *Thông thường* / *MoMo* / *VietQR*. |
   | **Hiện tại POS** | Bật thì thu ngân chọn được khi thanh toán. |

3. Nếu chọn **MoMo** hoặc **VietQR**, form hiện thêm nhóm khai báo kết nối
   (Partner Code, Access Key, Secret Key với MoMo; mã ngân hàng, số tài khoản,
   tên chủ tài khoản với VietQR).
4. Bấm **Lưu**.

## Lưu ý nghiệp vụ

⚠️ **Khoá bí mật (Secret Key, Access Key) không bao giờ hiện lại sau khi lưu.**
Mở lại form Sửa, các ô đó trống và ghi "Để trống nếu không đổi". Để trống là
**giữ nguyên khoá cũ**; chỉ điền khi thật sự muốn thay khoá mới. Đây là cách bảo
vệ khoá ký giao dịch — người xem được màn cấu hình không đọc trộm được khoá.

⚠️ **Phương thức đã dùng trong sổ quỹ, phiếu chi, đơn mua, đơn bán hoặc đối soát
ca thì không xoá được.** Muốn ngừng dùng thì tắt *Hiện tại POS*.

⚠️ Nhớ quay lại *Cấu hình hệ thống* chọn phương thức nào là **tiền mặt**
(mục 1.1). Không có bước này thì két không được ghi sổ.

💡 Mã phương thức không phân biệt hoa thường — đã có `CASH` thì không tạo `cash`.
