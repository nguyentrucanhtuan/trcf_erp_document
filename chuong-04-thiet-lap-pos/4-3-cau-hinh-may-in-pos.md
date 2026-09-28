---
title: "4.3 Cấu hình máy in POS"
---

- **Đường dẫn:** *Thiết lập cửa hàng → Máy in*.

![Thêm máy in](/images/04-may-in-them.png)

## Các bước

1. Bấm **Thêm máy in**.
2. Điền nhóm **Thiết bị**.
3. Điền nhóm **Thiết lập riêng** (nội dung đổi theo loại máy vừa chọn).
4. Bấm **Lưu**.

## Giải thích các trường

**Thiết bị**

| Trường           | Điền gì                                                      | Bắt buộc  |
| ---------------- | ------------------------------------------------------------ | --------- |
| Tên thiết bị     | VD "Máy in bill quầy 1"                                      | ✅         |
| Loại kết nối     | *Mạng LAN* (có IP) hoặc *USB* (cắm trực tiếp)                | ✅         |
| Loại máy in      | Hoá đơn / Nhãn dán / Phiếu yêu cầu món (KOT) / Phiếu đóng ca | ✅         |
| Địa chỉ IP, Cổng | Chỉ hiện khi chọn LAN. Cổng thường **9100**                  | ✅ nếu LAN |
| Đang bật         | Tắt = tạm ngừng in ra máy này                                | —         |

**Thiết lập riêng theo loại máy**

| Loại máy        | Khai thêm                                                                              |
| --------------- | -------------------------------------------------------------------------------------- |
| Hoá đơn         | *Chân trang hoá đơn* — câu in ở cuối bill                                              |
| Nhãn dán        | *Bề rộng / Chiều cao tem* (mm) và *Nguồn in* (loại đơn nào thì in tem)                 |
| Phiếu bếp (KOT) | *Danh mục sản phẩm* — máy **chỉ in món thuộc danh mục đã chọn**. Để trống = in mọi món |
| Phiếu đóng ca   | Không cần khai thêm                                                                    |

## Bố trí máy in mẫu

| Vị trí        | Loại máy | Danh mục chọn |
| ------------- | -------- | ------------- |
| Quầy thu ngân | Hoá đơn  | —             |
| Khu pha chế   | KOT      | Cà phê, Trà   |
| Khu bếp nóng  | KOT      | Đồ ăn         |

## Lưu ý

⚠️ **Chiều cao tem phải đo con tem, không đo cuộn.** Khai sai thì máy nhả giấy đi tìm khe cắt và ra tem trắng.

⚠️ Máy in nhiệt phổ thông (POS-80) **không có bảng mã tiếng Việt** — hệ thống in tiếng Việt bằng cách vẽ ảnh. Bill mất dấu thì kiểm tra lại loại máy đã khai.