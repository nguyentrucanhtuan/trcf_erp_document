---
crumb: Bước 6 · Kiểm soát tồn kho
---

# 6.2 Định mức tối thiểu - tối đa của sản phẩm

## 1. Đường dẫn vào chức năng

Menu trái: ==Quản lý kho → Tồn kho== (địa chỉ `/stock`).

- Cần có trước: sản phẩm bật **Theo dõi tồn kho** ([bài 2.4](2-4-nguyen-lieu.md)).
- Mỗi sản phẩm theo dõi tồn kho có một dòng ở mỗi kho, tồn ban đầu là 0.

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** khai định mức cho **NL - CÀ PHÊ VIỆT PHA PHIN - 1000 - 30** ở **KHO CHINH**, đơn vị GRAM.
>
> - Tồn tối thiểu: **5.000** GR (5 túi). Tồn tối đa: **20.000** GR (20 túi).
> - Mỗi ngày dùng khoảng 1.700 GR, nhà cung cấp giao sau 2 ngày: 1.700 × 2 × 1,5 ≈ 5.000 GR.

### Bước 1: Mở trang Tồn kho

- Ở menu trái, nhóm **Quản lý kho**, bấm **Tồn kho**.
- Bấm **Sản phẩm**, chọn **NL - CÀ PHÊ VIỆT PHA PHIN - 1000 - 30**. Bấm **Kho**, chọn **KHO CHINH**.
- Mỗi dòng là một sản phẩm ở một kho.

![Bước 1: Mở trang Tồn kho](images/06-dinh-muc-buoc-1-ton-kho.png)

### Bước 2: Khai định mức

- Bấm vào dòng đó.
- Điền như ảnh, bấm **Lưu**.

![Bước 2: Khai định mức](images/06-dinh-muc-buoc-2-form.png)

### Bước 3: Kiểm tra kết quả

- Thấy thông báo *“Đã cập nhật ngưỡng tồn kho”*. Cột **Trạng thái** hiện **Đủ hàng** (đang tồn 14.000 GR).
- Tồn xuống dưới 5.000 GR thì dòng hiện **Dưới định mức** và được đếm vào ô **Dòng dưới định mức**.
- Bấm nút **Dưới định mức** để chỉ xem các dòng cần nhập thêm. Bấm **Xoá bộ lọc** để xem lại tất cả.

![Bước 3: Kiểm tra trạng thái tồn](images/06-dinh-muc-buoc-3-ket-qua.png)

## 3. Giải thích các trường

| Trường | Điền gì |
| --- | --- |
| Tồn tối thiểu | Xuống dưới mức này là phải đặt hàng. Bằng 0: không cảnh báo |
| Tồn tối đa | Mức đầy kho. Hệ thống dùng để gợi ý đặt bao nhiêu. Bằng **0**: không giới hạn |

Công thức đặt tồn tối thiểu: `lượng dùng trung bình mỗi ngày × số ngày nhà cung cấp giao hàng × 1,5`.

## 4. Lưu ý quan trọng

> - Chưa khai định mức thì không có cảnh báo nhập hàng.
> - Định mức khai riêng cho từng kho.
