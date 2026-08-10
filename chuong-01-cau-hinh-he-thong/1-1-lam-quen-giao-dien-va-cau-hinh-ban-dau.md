---
title: "1.1 Làm quen giao diện và cấu hình thông tin ban đầu"
description: "Đăng nhập, nhận biết ba vùng màn hình và khai 8 nhóm cấu hình nền trước khi bán hàng."
---

**Đường dẫn:** *Thiết lập cửa hàng → Cấu hình hệ thống*
**Ai làm:** Chủ quán (chỉ tài khoản chủ quán mở được trang này)
**Khi nào:** Một lần khi cài đặt, làm trước mọi việc khác

## Đăng nhập

1. Mở trình duyệt vào địa chỉ hệ thống của quán.
2. Nhập email + mật khẩu → bấm **Đăng nhập**.
3. Quên mật khẩu → bấm **Quên mật khẩu?** → mở đường dẫn trong email.

⚠️ Đường dẫn đặt lại mật khẩu chỉ dùng được **một lần**. Bấm lại lần hai báo hết hạn, phải xin gửi lại.

## Ba vùng màn hình

![Giao diện tổng quan](/images/01-giao-dien-tong-quan.png)

| Vùng | Vị trí | Dùng để |
|---|---|---|
| Thanh bên trái | Cạnh trái, nền xám | Đi tới các màn nghiệp vụ. Bấm tên nhóm để mở màn con. |
| Thanh trên | Cạnh trên | Thu gọn thanh bên, chuyển sáng/tối |
| Vùng nội dung | Phần giữa | Nội dung màn đang mở |
| Góc dưới trái | Cạnh trái dưới cùng | Tên tài khoản → bấm để đăng xuất |

💡 Thanh bên chỉ hiện mục bạn được cấp quyền. Hai vai khác nhau thấy số mục khác nhau — bình thường, không phải lỗi.

## Bốn ô trên màn Tổng quan

| Ô | Nghĩa |
|---|---|
| Doanh thu hôm nay | Chỉ tính đơn **đã thanh toán**. Đơn treo chưa tính. |
| Đơn hàng hôm nay | Số đơn đã thanh toán |
| Khách hàng | Tổng khách đang hoạt động (không phải khách hôm nay) |
| Sản phẩm dưới định mức | Số mặt hàng tồn thấp hơn định mức tối thiểu. **Khác 0 = cần đặt hàng.** |

## Khai cấu hình nền — các bước

![Cấu hình hệ thống](/images/01-cau-hinh-he-thong.png)

1. Vào *Thiết lập cửa hàng → Cấu hình hệ thống*.
2. Khai lần lượt 8 nhóm thẻ theo bảng dưới.
3. Bấm **Lưu cấu hình** ở cuối trang.

⚠️ Trang này **không tự lưu**. Rời trang khi chưa bấm Lưu là mất hết.

## Giải thích các trường

| Nhóm | Trường | Điền gì |
|---|---|---|
| Cấu hình chung | Tiền tệ | VND |
| | Múi giờ | Asia/Ho_Chi_Minh |
| | Domain công khai | Để trống nếu chưa dùng cổng thanh toán online |
| Nhập hàng | Kho nhập mặc định | Kho tự điền khi tạo đơn mua |
| | Cho phép nhân viên chọn kho nhập | Bật nếu quán nhiều kho và nhân viên được đổi |
| Chuyển kho | Kho nguồn / Kho đích | Kho mặc định của phiếu chuyển |
| Chế biến | Kho trừ nguyên liệu / Kho nhập thành phẩm | Kho lấy nguyên liệu và kho nhận thành phẩm |
| Bán hàng | Kho bán hàng | Kho bị trừ khi bán |
| | Loại đơn hàng mặc định | Tại chỗ / Mang đi… |
| | **Phương thức tiền mặt** | **Bắt buộc.** Xem cảnh báo dưới. |
| Huỷ hàng | Kho huỷ | Kho ghi nhận hàng hỏng |
| Tài chính / Thuế | Giá bán đã bao gồm VAT | Bật nếu giá niêm yết đã gồm thuế |
| Hoá đơn điện tử | Minvoice | Chỉ điền khi có hợp đồng xuất hoá đơn GTGT → [mục 5.5](/chuong-05-ban-hang-tai-quay/5-5-cau-hinh-va-xuat-hoa-don-vat) |

## Kiểm tra đã đúng

- [ ] Đủ **6 ô kho** đã chọn (nhập, chuyển nguồn, chuyển đích, chế biến ×2, bán, huỷ)
- [ ] Ô **Phương thức tiền mặt** đã chọn
- [ ] Bấm **Lưu cấu hình** và thấy thông báo thành công

## Lưu ý

⚠️ **Ô *Phương thức tiền mặt* là ô quan trọng nhất trang này.** Bỏ trống thì mở ca và đóng ca vẫn chạy bình thường **nhưng không sinh bút toán quỹ nào** — sổ quỹ đứng im mà không báo lỗi, cuối tháng đối chiếu mới phát hiện.

⚠️ Chưa khai ô kho nào thì nhân viên lập phiếu tương ứng sẽ nhận lỗi "chưa cấu hình kho" và **không lập được phiếu**.

💡 Quán chỉ có một kho vẫn khai đủ 6 ô: chọn cùng một kho cho tất cả.

## Quán đã có sẵn gì sau khi cài đặt

| Loại | Có sẵn |
|---|---|
| Kho | Kho tổng (KHO-TONG), Kho quầy (KHO-QUAY) |
| Phương thức thanh toán | Tiền mặt (CASH), Chuyển khoản (BANK), Thẻ (CARD) |
| Quầy POS | Quầy chính, đã gắn 3 phương thức trên |
| Phòng ban | Vận hành |
| Nhân viên | Hồ sơ "Quản lý" gắn tài khoản chủ quán |

💡 Bộ này chỉ nạp khi bảng còn trống. Bạn xoá bớt (VD xoá phương thức Thẻ) thì khởi động lại **không** hồi sinh nó.
