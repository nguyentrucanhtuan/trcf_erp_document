---
title: "1.1 Làm quen giao diện và cấu hình thông tin ban đầu"
---

- **Đường dẫn:** *Thiết lập cửa hàng → Cấu hình hệ thống*.
- **Ai làm:** Chủ quán (chỉ tài khoản chủ quán mở được trang này).
- **Khi nào:** Một lần khi cài đặt, làm trước mọi việc khác.

## Khai cấu hình nền — các bước

![Cấu hình hệ thống](/images/01-cau-hinh-he-thong.png)

1. Vào *Thiết lập cửa hàng → Cấu hình hệ thống*.
2. Khai lần lượt 8 nhóm thẻ theo bảng dưới.
3. Bấm **Lưu cấu hình** ở cuối trang.

## Giải thích các trường

| Nhóm             | Trường                                    | Điền gì                                                                                                               |
| ---------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Cấu hình chung   | Tiền tệ                                   | VND                                                                                                                   |
|                  | Múi giờ                                   | Asia/Ho_Chi_Minh                                                                                                      |
|                  | Domain công khai                          | Để trống nếu chưa dùng cổng thanh toán online                                                                         |
| Nhập hàng        | Kho nhập mặc định                         | Kho tự điền khi tạo đơn mua                                                                                           |
|                  | Cho phép nhân viên chọn kho nhập          | Bật nếu quán nhiều kho và nhân viên được đổi                                                                          |
| Chuyển kho       | Kho nguồn / Kho đích                      | Kho mặc định của phiếu chuyển                                                                                         |
| Chế biến         | Kho trừ nguyên liệu / Kho nhập thành phẩm | Kho lấy nguyên liệu và kho nhận thành phẩm                                                                            |
| Bán hàng         | Kho bán hàng                              | Kho bị trừ khi bán                                                                                                    |
|                  | Loại đơn hàng mặc định                    | Tại chỗ / Mang đi…                                                                                                    |
|                  | **Phương thức tiền mặt**                  | **Bắt buộc.** Xem cảnh báo dưới.                                                                                      |
| Huỷ hàng         | Kho huỷ                                   | Kho ghi nhận hàng hỏng                                                                                                |
| Tài chính / Thuế | Giá bán đã bao gồm VAT                    | Bật nếu giá niêm yết đã gồm thuế                                                                                      |
| Hoá đơn điện tử  | Minvoice                                  | Chỉ điền khi có hợp đồng xuất hoá đơn GTGT → [mục 5.5](/chuong-05-ban-hang-tai-quay/5-5-cau-hinh-va-xuat-hoa-don-vat) |

## Kiểm tra đã đúng

- [ ] Đủ **6 ô kho** đã chọn (nhập, chuyển nguồn, chuyển đích, chế biến ×2, bán, huỷ)
- [ ] Ô **Phương thức tiền mặt** đã chọn
- [ ] Bấm **Lưu cấu hình** và thấy thông báo thành công

## Lưu ý

⚠️ **Ô *Phương thức tiền mặt* là ô quan trọng nhất trang này.** Bỏ trống thì mở ca và đóng ca vẫn chạy bình thường **nhưng không sinh bút toán quỹ nào** — sổ quỹ đứng im mà không báo lỗi, cuối tháng đối chiếu mới phát hiện.

⚠️ Chưa khai ô kho nào thì nhân viên lập phiếu tương ứng sẽ nhận lỗi "chưa cấu hình kho" và **không lập được phiếu**.

💡 Quán chỉ có một kho vẫn khai đủ 6 ô: chọn cùng một kho cho tất cả.

