---
crumb: Bước 3 · Nhập công thức
---

# 3.2 Công thức thành phẩm

## 1. Đường dẫn vào chức năng

Menu trái: ==Quản lý sản phẩm → Công thức== (địa chỉ `/boms`).

- Cần có trước: thành phẩm bật **Sản xuất (có công thức)** ([bài 2.2](2-2-thanh-pham.md)).
- Cần có trước: nguyên liệu, bán thành phẩm đã có giá vốn ([bài 2.4](2-4-nguyen-lieu.md), [bài 3.1](3-1-cong-thuc-ban-thanh-pham.md)).

### Hai loại công thức

| Loại         | Trừ kho khi nào                                       | Dùng cho                                                               |
| ------------ | ----------------------------------------------------- | ---------------------------------------------------------------------- |
| CẦN SẢN XUẤT | Khi lập **phiếu chế biến** ([11.4](11-4-che-bien.md)) | Bán thành phẩm ủ trước: TRÀ LÀI Ủ SẴN, MILKFOAM, TRÂN CHÂU NẤU SẴN     |
| KIT          | Ngay **lúc bán**, tự trừ thành phần                   | COMBO, MÓN RÁP TẠI CHỖ: CÀ PHÊ ĐEN, CÀ PHÊ SỮA, BẠC XỈU, TRÀ SỮA OLONG |

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** công thức Kit cho **THỬ — Cốt trà sữa**, bán theo ly, trừ thành phần ngay lúc bán.
>
> - Công thức: **Sữa tươi Đà Lạt** 0,1 lít + **Đường mía** 0,01 kg.
> - Sản lượng 1 ly.

### Bước 1: Tạo công thức

- Ở menu trái, nhóm **Quản lý sản phẩm**, bấm **Công thức**.
- Bấm nút tròn **+** ở góc dưới bên phải.
- Điền cột trái như ảnh.
- Bấm **Thêm nguyên liệu** hai lần, điền từng dòng như ảnh.
- Bấm **Tạo công thức**.

![Bước 1: Tạo công thức](images/03-cong-thuc-buoc-1-tao.png)

### Bước 2: Tính giá vốn

- Bấm vào dòng công thức (cột **Giá vốn** đang *Chưa tính*), chọn **Tính giá vốn**.
- Thấy thông báo *“Đã tính giá vốn công thức”*, cột **Giá vốn** hiện số tiền.
- Tính cả loạt: bấm biểu tượng **Tính lại giá vốn** ở góc trên bên phải.

![Bước 2: Bấm vào dòng công thức để mở thao tác](images/03-cong-thuc-buoc-2-danh-sach.png)

## 3. Giải thích các trường

### Khai công thức

| Trường                | Điền gì                                                                | Bắt buộc |
| --------------------- | ---------------------------------------------------------------------- | -------- |
| Sản phẩm (thành phẩm) | Món cần công thức. Danh sách **chỉ hiện sản phẩm đã bật *Sản xuất***   | ✅        |
| Biến thể (tuỳ chọn)   | Bỏ trống: công thức chung mọi size. Chọn size: công thức riêng size đó | —        |
| Loại công thức        | *Cần sản xuất* hoặc *Kit (trừ thành phần khi bán)* (xem bảng đầu bài)  | ✅        |
| Sản lượng             | **Số lượng** + **Đơn vị** công thức làm ra. Tạo ra được 1 ly: nhập 1, chọn Ly | ✅        |
| Hoạt động             | Tắt: công thức tạm ngừng dùng                                          | —        |
| Ghi chú               | Ghi chú nội bộ cho công thức                                           | —        |
| Nguyên liệu           | Hàng + số lượng (SL) + đơn vị tính (ĐVT)                               | ✅        |

### Cách tính giá vốn

`giá vốn sản phẩm = tổng giá vốn nguyên liệu cộng lại`

- Sản phẩm có nhiều công thức đang hoạt động: lấy **công thức rẻ nhất**.

## 4. Lưu ý quan trọng

> - Nguyên liệu giá vốn 0 làm giá vốn món sai: nhập hàng một lần để có giá.
> - Món dùng bán thành phẩm: tính giá bán thành phẩm trước ([bài 3.1](3-1-cong-thuc-ban-thanh-pham.md)), rồi mới tính món.
