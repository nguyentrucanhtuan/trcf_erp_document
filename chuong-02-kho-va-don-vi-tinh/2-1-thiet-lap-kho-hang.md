---
title: "2.1 Thiết lập kho hàng"
description: "Tạo kho tổng và kho quầy, hiểu vì sao phải tách kho."
---

Hai màn trong chương này là **nền móng**: chưa có kho và đơn vị tính thì không
tạo được sản phẩm, không nhập được hàng, không bán được. Làm đúng thứ tự: kho
trước, đơn vị tính sau, rồi mới sang chương 3.

*Quản lý kho → Kho hàng*

Kho là nơi hệ thống ghi nhận hàng đang nằm ở đâu. Mỗi lần nhập, bán, chuyển,
huỷ, chế biến — hệ thống đều cộng/trừ vào một kho cụ thể.

![Danh sách kho](/images/02-kho-danh-sach.png)

## Làm từng bước

1. Bấm **Thêm kho**.
2. Điền ba trường:

   | Trường | Điền gì |
   |---|---|
   | **Mã kho** | Chuỗi ngắn không dấu, viết hoa. VD `KHO-TONG`, `KHO-QUAY`. |
   | **Tên kho** | Tên người đọc hiểu. VD "Kho tổng", "Kho quầy pha chế". |
   | **Địa chỉ** | Không bắt buộc. |

3. Bấm **Lưu**.

![Thêm kho mới](/images/02-kho-them-moi.png)

## Nên chia bao nhiêu kho

Cách chia phổ biến cho một quán:

- **Kho tổng** — nơi nhận hàng từ nhà cung cấp, chứa nguyên liệu chưa dùng tới.
- **Kho quầy** — nguyên liệu đã đưa ra quầy, là kho bị trừ khi bán hàng.

Chia như vậy để biết được "còn bao nhiêu trong kho tổng để tiếp cho quầy". Quán
nhỏ, một chỗ chứa duy nhất thì để **một kho** cũng hoàn toàn hợp lệ — khi đó ở
Cấu hình hệ thống chọn cùng kho đó cho tất cả các ô.

## Lưu ý nghiệp vụ

⚠️ **Kho đã phát sinh giao dịch thì không xoá được.** Bấm xoá sẽ nhận thông báo
liệt kê rõ những chỗ đang dùng kho đó (tồn kho, phiếu nhập, phiếu chuyển, phiếu
kiểm...). Đây là cố ý: xoá kho đi thì các phiếu cũ mất chỗ tham chiếu, sổ sách
lịch sử sẽ sai. Kho không dùng nữa thì **lưu trữ**, đừng xoá.

⚠️ Kho đang được đặt làm kho mặc định trong *Cấu hình hệ thống* cũng không xoá
được. Muốn xoá, phải đổi cấu hình sang kho khác trước.

💡 Kho vừa tạo mà chưa nhập gì thì xoá được bình thường — hệ thống phân biệt được
"kho trống mới tạo" và "kho đã có lịch sử".
