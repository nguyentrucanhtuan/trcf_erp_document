---
title: "5.1 Hướng dẫn mở phiên và bán hàng"
description: "Mở ca với tiền đầu ca và thao tác bán hàng trên màn quầy."
---

Chương này là **việc hằng ngày của nhân viên đứng quầy**. Đọc theo đúng thứ tự
một ca diễn ra.

## Bước 1 — Mở ca

Vào *Thiết lập cửa hàng → POS*, bấm **Mở ca** ở quầy mình đứng. Hoặc vào
*Báo cáo → Báo cáo ca* rồi bấm **Mở ca**.

![Mở ca bán hàng](/images/05-mo-ca.png)

1. Chọn **Quầy bán hàng**.
2. Ô **Thu ngân** đã điền sẵn tên bạn — **không đổi được**, hệ thống lấy theo tài
   khoản đang đăng nhập.
3. Đếm tiền mặt thật trong két và nhập vào **Tiền mặt đầu ca**.
4. Bấm **BẮT ĐẦU CA**.

> **Vì sao không chọn được thu ngân khác:** ca bán hàng là chứng từ đối soát két.
> Người mở ca là người chịu trách nhiệm phần tiền trong ca đó. Nếu ai cũng mở ca
> đứng tên người khác được thì lúc thiếu tiền không truy được về ai. Mỗi người
> một tài khoản, ai bán thì người đó mở ca của mình.

⚠️ **Đếm tiền đầu ca cho đúng.** Con số này là mốc để cuối ca tính ra "đáng lẽ
trong két phải có bao nhiêu". Nhập đại thì cuối ca chênh lệch mà không biết lỗi ở
đâu.

⚠️ Một quầy chỉ có **một ca đang mở** tại một thời điểm. Người thứ hai bấm Mở ca
cùng quầy sẽ bị báo lỗi — đó là chặn có chủ đích, không phải trục trặc.

## Bước 2 — Màn bán hàng

Sau khi mở ca, hệ thống vào màn bán hàng.

![Màn bán hàng — chọn bàn](/images/05-man-ban-hang.png)

Thanh trên cùng có bốn mục:

| Mục | Dùng để |
|---|---|
| **BÀN** | Sơ đồ bàn. Bấm bàn để gắn đơn vào bàn đó. |
| **MENU** | Danh sách món để bấm chọn. |
| **ĐƠN HÀNG** | Các đơn đã lưu, đang chờ xử lý. |
| **VẬN HÀNH** | Các nghiệp vụ kho phát sinh trong ca — xem [mục 5.3](/chuong-05-ban-hang-tai-quay/5-3-tong-quan-quy-trinh-quan-ly-kho). |

## Bước 3 — Lên đơn

![Màn bán hàng — chọn món](/images/05-man-ban-hang-menu.png)

1. Bấm **MENU**, chọn nhóm món ở hàng nút phía trên (Tất cả / Cà phê / …) hoặc gõ
   vào ô **Tìm món**.
2. Bấm vào món để thêm vào giỏ bên phải.
3. Nếu món có size hoặc topping, hệ thống hiện ô chọn:
   - **Chip màu xanh** = biến thể (size) — **có ảnh hưởng giá**.
   - **Chip màu xám** = ghi chú pha chế (ít đá, ít đường) — **không đổi giá**,
     chỉ ghép vào tên món trên bill và màn bếp.
   - Ghi chú pha chế **mặc định không chọn gì**. Bấm lần nữa để bỏ chọn.
4. Muốn ghi thêm yêu cầu riêng của khách thì bấm **Ghi chú**.
5. Có mã khuyến mãi thì bấm **Mã giảm giá**.
6. Khách quen: gõ số điện thoại vào ô **Tìm khách hàng** để tích điểm.

## Bước 4 — Thanh toán

- **Lưu đơn** — giữ đơn lại, chưa thu tiền (khách còn ngồi, gọi thêm sau).
- **THANH TOÁN** — chọn phương thức, xác nhận thu tiền.

Ngay khi đơn được thanh toán, hệ thống đồng thời:

1. Trừ nguyên liệu trong kho theo công thức.
2. Ghi tiền vào sổ quỹ theo phương thức đã chọn.
3. Cộng điểm cho khách (nếu có gắn khách).
4. Đẩy món sang màn hình bếp.

Tất cả xảy ra trong **cùng một lần** — không có chuyện tiền vào mà kho chưa trừ.

## Lưu ý nghiệp vụ

⚠️ **Đơn đã thanh toán thì không sửa được món, mã giảm giá hay điểm.** Hệ thống
chặn và báo lỗi. Lý do: tiền đã ghi vào sổ quỹ, sổ quỹ không sửa được — thêm một
ly sau khi đã thu tiền sẽ làm số trong sổ khác số thực thu. Khách gọi thêm thì
**lên đơn mới**.

⚠️ **Đổi phương thức thanh toán sau khi đã thu tiền cũng bị chặn**, vì đối soát
cuối ca dựa vào phương thức đã ghi.

⚠️ Khách trả lại hàng thì dùng **Hoàn đơn** (*Vận hành → Hoàn đơn*), đừng sửa
đơn cũ. Hoàn đơn trả lại hàng vào kho, trả tiền trên sổ quỹ, và nếu hoàn hết thì
trả lại cả điểm và lượt dùng voucher.
