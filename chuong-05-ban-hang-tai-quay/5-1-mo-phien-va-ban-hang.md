---
title: "5.1 Hướng dẫn mở phiên và bán hàng"
---

- **Đường dẫn:** *Thiết lập cửa hàng → POS → Mở ca* (hoặc *Báo cáo → Báo cáo ca → Mở ca*)
- **Ai làm:** Nhân viên đứng quầy, bằng **tài khoản của chính mình**.

## Bước 1 — Mở ca

![Mở ca bán hàng](/images/05-mo-ca.png)

1. Chọn **Quầy bán hàng**.
2. Kiểm ô **Thu ngân** — đã điền sẵn tên bạn, **không đổi được**.
3. Đếm tiền mặt thật trong két → nhập vào **Tiền mặt đầu ca**.
4. Bấm **BẮT ĐẦU CA**.

| Trường | Điền gì |
|---|---|
| Quầy bán hàng | Quầy bạn đứng |
| Thu ngân | Tự điền theo tài khoản đăng nhập, không sửa |
| Tiền mặt đầu ca | Số tiền **đếm thật** trong két lúc này |

⚠️ **Đếm tiền đầu ca cho đúng.** Đây là mốc để cuối ca tính "đáng lẽ két phải có bao nhiêu". Nhập đại thì cuối ca chênh lệch mà không biết lỗi ở đâu.

⚠️ Một quầy chỉ có **một ca đang mở**. Người thứ hai bấm Mở ca cùng quầy sẽ bị báo lỗi — chặn có chủ đích.

## Bước 2 — Bốn mục trên màn bán hàng

![Màn bán hàng — chọn bàn](/images/05-man-ban-hang.png)

| Mục | Dùng để |
|---|---|
| **BÀN** | Sơ đồ bàn — bấm bàn để gắn đơn vào bàn đó |
| **MENU** | Danh sách món để bấm chọn |
| **ĐƠN HÀNG** | Các đơn đã lưu, đang chờ xử lý |
| **VẬN HÀNH** | Nghiệp vụ kho phát sinh trong ca → [mục 5.3](/chuong-05-ban-hang-tai-quay/5-3-tong-quan-quy-trinh-quan-ly-kho) |

## Bước 3 — Lên đơn

![Màn bán hàng — chọn món](/images/05-man-ban-hang-menu.png)

1. Bấm **MENU** → chọn nhóm món hoặc gõ vào ô **Tìm món**.
2. Bấm món để thêm vào giỏ bên phải.
3. Chọn size / ghi chú nếu có (xem bảng dưới).
4. Yêu cầu riêng của khách → bấm **Ghi chú**.
5. Có mã khuyến mãi → bấm **Mã giảm giá**.
6. Khách quen → gõ số điện thoại vào ô **Tìm khách hàng** để tích điểm.

**Phân biệt hai loại chip:**

| Chip | Là gì | Đổi giá |
|---|---|---|
| 🟩 Xanh | Biến thể (size) | ✅ Có |
| ⬜ Xám | Ghi chú pha chế (ít đá, ít đường) | ❌ Không — chỉ ghép vào tên món trên bill và màn bếp |

💡 Ghi chú pha chế **mặc định không chọn gì**. Bấm lần nữa để bỏ chọn.

## Bước 4 — Thanh toán

| Nút | Kết quả |
|---|---|
| **Lưu đơn** | Giữ đơn lại, chưa thu tiền (khách còn ngồi, gọi thêm sau) |
| **THANH TOÁN** | Chọn phương thức → xác nhận thu tiền |

**Ngay khi thanh toán, hệ thống làm đồng thời 4 việc trong cùng một lần:**

1. Trừ nguyên liệu trong kho theo công thức
2. Ghi tiền vào sổ quỹ theo phương thức đã chọn
3. Cộng điểm cho khách (nếu có gắn khách)
4. Đẩy món sang màn hình bếp

## Kiểm tra đã đúng

- [ ] Ca hiện trạng thái **Đang mở** với đúng tên bạn
- [ ] Món lên đơn hiện ngay trên màn bếp
- [ ] Đơn đã thanh toán hiện đúng phương thức

## Lưu ý

⚠️ **Đơn đã thanh toán không sửa được món, mã giảm giá hay điểm.** Tiền đã ghi vào sổ quỹ mà sổ quỹ không sửa được — thêm một ly sau khi thu tiền sẽ làm số trong sổ khác số thực thu. Khách gọi thêm thì **lên đơn mới**.

⚠️ **Đổi phương thức thanh toán sau khi đã thu tiền cũng bị chặn**, vì đối soát cuối ca dựa vào phương thức đã ghi.

⚠️ Khách trả lại hàng → dùng **Hoàn đơn** (*Vận hành → Hoàn đơn*), đừng sửa đơn cũ. Hoàn đơn trả hàng vào kho, trả tiền trên sổ quỹ, và nếu hoàn hết thì trả lại cả điểm lẫn lượt dùng voucher.
