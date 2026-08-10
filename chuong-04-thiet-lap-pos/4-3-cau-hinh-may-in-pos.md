---
title: "4.3 Cấu hình máy in POS"
description: "Khai máy in bill và máy in bếp, định tuyến theo danh mục món."
---

*Thiết lập cửa hàng → Máy in*

![Thêm máy in](/images/04-may-in-them.png)

## Làm từng bước

1. Bấm **Thêm máy in**.
2. Nhóm **Thiết bị**:

   | Trường | Điền gì |
   |---|---|
   | **Tên thiết bị** | VD "Máy in bill quầy 1". |
   | **Loại kết nối** | *Mạng LAN* (có IP) hoặc *USB* (cắm trực tiếp). |
   | **Loại máy in** | Hoá đơn / Nhãn dán / Phiếu yêu cầu món (KOT) / Phiếu đóng ca. |
   | **Địa chỉ IP**, **Cổng** | Chỉ hiện khi chọn LAN. Cổng thường là 9100. |
   | **Đang bật** | Tắt = tạm ngừng in ra máy này. |

3. Nhóm **Thiết lập riêng** đổi theo loại máy vừa chọn:

   | Loại máy | Khai thêm |
   |---|---|
   | Hoá đơn | *Chân trang hoá đơn* — câu in ở cuối bill. |
   | Nhãn dán | *Bề rộng / Chiều cao tem* (mm) và *Nguồn in* (loại đơn hàng nào thì in tem). |
   | Phiếu bếp (KOT) | *Danh mục sản phẩm* — máy chỉ in món thuộc danh mục đã chọn. Để trống = in mọi món. |
   | Phiếu đóng ca | Không cần khai thêm. |

4. Bấm **Lưu**.

## Chia máy in theo khu vực làm việc

Cách bố trí phổ biến:

- **Máy in bill** ở quầy thu ngân — loại *Hoá đơn*.
- **Máy in phiếu bếp** ở khu pha chế — loại *KOT*, chọn danh mục Cà phê/Trà.
- **Máy in phiếu bếp thứ hai** ở khu bếp nóng — loại *KOT*, chọn danh mục Đồ ăn.

Nhờ chọn danh mục, mỗi khu chỉ nhận phiếu của phần việc mình làm.

## Lưu ý nghiệp vụ

⚠️ **Chiều cao tem phải đo con tem, không đo cuộn.** Khai sai thì máy nhả giấy
đi tìm khe cắt và ra tem trắng.

⚠️ Máy in nhiệt phổ thông (POS-80) **không có sẵn bảng mã tiếng Việt**, nên hệ
thống in tiếng Việt bằng cách vẽ ảnh. Nếu bill in ra bị mất dấu, kiểm tra lại
loại máy đã khai.

💡 Máy in USB trên máy Linux có thể bị dịch vụ in của hệ điều hành (CUPS) chiếm
mất. Khi máy im lặng dù đã khai đúng, kiểm tra điều này trước.
