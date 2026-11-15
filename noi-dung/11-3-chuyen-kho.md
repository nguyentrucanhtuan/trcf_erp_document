---
crumb: Bước 11 · Quy trình vận hành kho
---

# 11.3 Chuyển kho

## 1. Đường dẫn vào chức năng

Menu trái: ==Vận hành → Chuyển kho== (địa chỉ `/stock-transfers`, tiêu đề trang **Phiếu chuyển kho**).

hoặc ô **Chuyển kho** ở khối *Tính năng cho bạn* trên Trang chủ.

- Dùng khi: lấy hàng từ kho tổng ra kho quầy, hoặc điều hàng giữa hai chi nhánh.
- Cần có trước: hai kho khác nhau (khai ở **Quản lý kho → Kho hàng**).

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** chuyển 2 kg **Cà phê hạt Robusta** từ **Kho tổng** ra **Kho quầy**.
>
> - Kho xuất đi: **Kho tổng**. Kho nhập đến: **Kho quầy**.
> - Dòng hàng: **Cà phê hạt Robusta**, SL **2**, đơn vị **Kilogam**.

### Bước 1: Mở trang Phiếu chuyển kho

- Ở menu trái, nhóm **Vận hành**, bấm **Chuyển kho**.

![Bước 1: Mở trang Phiếu chuyển kho](images/06-chuyen-kho-buoc-1-danh-sach.png)

### Bước 2: Khai phiếu và dòng hàng

- Bấm nút tròn **+** ở góc dưới bên phải.
- Chọn hai kho, thêm sản phẩm ở ô **Thêm sản phẩm**, điền như ảnh.
- Bấm **Lưu phiếu (Nháp)**.

![Bước 2: Khai phiếu và dòng hàng](images/06-chuyen-kho-buoc-2-form.png)

### Bước 3: Kiểm tra rồi xác nhận chuyển

- Mở tab **Nháp**, bấm vào phiếu vừa lưu.
- Chọn **Xác nhận chuyển**, rồi xác nhận lần nữa ở hộp thoại hỏi lại.
- Phiếu chuyển sang tab **Đã chuyển**.

![Bước 3: Kiểm tra rồi xác nhận chuyển](images/06-chuyen-kho-buoc-3-nhap-menu.png)

## 3. Giải thích các trường

| Trường | Điền gì | Bắt buộc |
| --- | --- | --- |
| Mã phiếu chuyển | Tự sinh, chỉ đọc | — |
| Kho xuất đi | Kho lấy hàng ra | ✅ |
| Kho nhập đến | Kho nhận hàng. **Phải khác kho xuất** | ✅ |
| Sản phẩm / SL / ĐVT | Từng dòng hàng chuyển. Chọn đơn vị lớn được (hệ thống tự quy đổi). Bấm thùng rác để bỏ dòng | ✅ |
| Ghi chú | Ghi thêm (không bắt buộc) | — |

### Xác nhận làm gì

- Ghi **hai bút toán kho cùng lúc**: trừ kho nguồn + cộng kho đích.
- Không có chuyện hàng biến mất giữa đường.

## 4. Lưu ý quan trọng

> - Đã xác nhận thì không sửa, không xoá: chuyển nhầm thì lập phiếu ngược lại.
> - Bê hàng đi mà không lập phiếu thì tồn kho trên hệ thống sai.
