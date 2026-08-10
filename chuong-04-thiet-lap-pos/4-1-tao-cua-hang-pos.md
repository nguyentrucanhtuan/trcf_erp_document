---
title: "4.1 Tạo cửa hàng POS"
description: "Tạo quầy bán hàng và gắn phương thức thanh toán cho quầy."
---

Chương này dựng chỗ đứng bán hàng. Làm xong bốn mục dưới đây là quán bán được.

*Thiết lập cửa hàng → POS*

Một **quầy POS** là một điểm bán: một máy tính/máy tính bảng có người đứng thu
tiền. Quán một quầy thì khai một; có quầy trong nhà và quầy mang đi thì khai hai.

![Danh sách quầy bán hàng](/images/04-pos-danh-sach.png)

## Làm từng bước

1. Bấm **Thêm quầy**.
2. Điền **Tên quầy bán hàng** (VD "Quầy chính", "Quầy sân vườn").
3. Chọn **Phương thức thanh toán** áp dụng cho quầy này — chọn nhiều được.
4. Bấm **Lưu**.

![Thêm quầy bán hàng](/images/04-pos-them.png)

## Ba nút trên mỗi dòng quầy

| Nút | Mở ra gì |
|---|---|
| **Mở ca** | Vào màn bán hàng của quầy đó. Xem [mục 5.1](/chuong-05-ban-hang-tai-quay/5-1-mo-phien-va-ban-hang). |
| **Màn khách** | Màn hình hướng về phía khách, hiện giỏ hàng và mã QR thanh toán. |
| **Shop Online** | Đường dẫn đặt hàng online của quán. |

## Lưu ý nghiệp vụ

⚠️ **Danh sách phương thức thanh toán chọn ở đây quyết định thu ngân thấy gì khi
thanh toán.** Quên gắn "Chuyển khoản" thì thu ngân không chọn được, dù phương
thức đó vẫn tồn tại trong hệ thống.

⚠️ Quầy đã phát sinh đơn hàng, phiếu chi, ca bán hoặc bút toán quỹ thì **không
xoá được**. Lý do: mọi bút toán trong sổ quỹ đều gắn với quầy; xoá quầy sẽ làm
việc đối chiếu ca cũ mất căn cứ. Ngừng dùng thì **lưu trữ**.

💡 Sửa danh sách phương thức thanh toán là **thay thế**, không phải cộng thêm:
danh sách sau khi lưu đúng bằng những gì đang tick.
