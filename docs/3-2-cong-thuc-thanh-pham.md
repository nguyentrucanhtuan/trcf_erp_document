---
crumb: Bước 3 · Nhập công thức
---

# 3.2 Công thức thành phẩm

## 1. Đường dẫn vào chức năng

Menu trái: ==Quản lý sản phẩm → Công thức== (địa chỉ `/boms`).

- Cần có trước: thành phẩm bật **Sản xuất** ([bài 2.2](2-2-thanh-pham.md)).
- Cần có trước: nguyên liệu, bán thành phẩm đã có giá vốn ([bài 2.4](2-4-nguyen-lieu.md), [bài 3.1](3-1-cong-thuc-ban-thanh-pham.md)).

### Hai loại công thức

| Loại         | Trừ kho khi nào                                       | Dùng cho                                                               |
| ------------ | ----------------------------------------------------- | ---------------------------------------------------------------------- |
| CẦN SẢN XUẤT | Khi lập **phiếu chế biến** ([11.4](11-4-che-bien.md)) | Bán thành phẩm ủ trước: TRÀ LÀI Ủ SẴN, MILKFOAM, TRÂN CHÂU NẤU SẴN     |
| KIT          | Ngay **lúc bán**, tự trừ thành phần                   | COMBO, MÓN RÁP TẠI CHỖ: CÀ PHÊ ĐEN, CÀ PHÊ SỮA, BẠC XỈU, TRÀ SỮA OLONG |

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** món "Trà đào" giá 40.000.
>
> - Công thức: "Trà đen" 15 g + "Đường cát" 10 g.
> - Sản lượng 1 LY.

### Bước 1: Tạo công thức

- Vào **Quản lý sản phẩm → Công thức**.
- Bấm **Thêm công thức**.
- **Sản phẩm (thành phẩm)**: chọn "Trà đào".
- **Loại công thức**: giữ "KIT (Trừ thành phần khi bán)".
- **Sản lượng**: giữ "1", đơn vị "LY".
- Bấm **Thêm nguyên liệu** hai lần.
- Dòng 1: chọn "Trà đen", SL "15", ĐVT "Gram (G)".
- Dòng 2: chọn "Đường cát", SL "10", ĐVT "Gram (G)".
- Bấm nút **Tạo công thức**.

![Bước 1: Tạo công thức](images/03-cong-thuc-buoc-1-tao.png)

### Bước 2: Mở menu dòng công thức

- Công thức mới có **Giá vốn** "Chưa tính".
- Bấm nút **…** ở cuối dòng.
- Menu có: **Tính giá vốn**, **Sửa**, **Xoá**.

![Bước 2: Mở menu dòng công thức](images/03-cong-thuc-buoc-2-danh-sach.png)

### Bước 3: Tính giá vốn

- Chọn **Tính giá vốn**.
- Thấy thông báo *“Đã tính giá vốn công thức”*.
- Cột **Giá vốn** hiện "4.700₫".
- Tính cả loạt: bấm **Tính lại giá vốn** ở đầu trang.

![Bước 3: Tính giá vốn](images/03-cong-thuc-buoc-3-gia-von.png)

## 3. Giải thích các trường

### Khai công thức

| Trường                | Điền gì                                                                | Bắt buộc |
| --------------------- | ---------------------------------------------------------------------- | -------- |
| Sản phẩm (thành phẩm) | Món cần công thức. Danh sách **chỉ hiện sản phẩm đã bật *Sản xuất***   | ✅        |
| Biến thể              | Bỏ trống: công thức chung mọi size. Chọn size: công thức riêng size đó | —        |
| Loại công thức        | *Cần sản xuất* hoặc *Kit* (xem bảng dưới)                              | ✅        |
| Sản lượng             | Công thức làm ra bao nhiêu thành phẩm. Tạo ra được 1 ly: điền 1        | ✅        |
| Hoạt động             | Tắt: công thức tạm ngừng dùng                                          | —        |
| Nguyên liệu           | Hàng + số lượng (SL) + đơn vị tính (ĐVT)                               | ✅        |

### Hai loại công thức

| Loại         | Trừ kho khi nào                                       | Dùng cho                                                           |
| ------------ | ----------------------------------------------------- | ------------------------------------------------------------------ |
| Cần sản xuất | Khi lập **phiếu chế biến** ([11.4](11-4-che-bien.md)) | Bán thành phẩm ủ trước: cà phê cốt, trà ủ, milkfoam, trân châu nấu |
| Kit          | Ngay **lúc bán**, tự trừ thành phần                   | Combo, món ráp tại chỗ không qua chế biến                          |

### Cách tính giá vốn

`giá vốn sản phẩm = tổng giá vốn nguyên liệu cộng lại`

- Sản phẩm có nhiều công thức đang hoạt động: lấy **công thức rẻ nhất**.

## 4. Lưu ý quan trọng

> [!CAUTION]
> **Nguyên liệu có giá vốn = 0 làm giá vốn món sai.**
>
> - Sau khi tính, hệ thống cảnh báo tên nguyên liệu chưa có giá.
> - Giá vốn nguyên liệu tự cập nhật mỗi lần nhập hàng.
> - Nguyên liệu chưa nhập lần nào thì vẫn là 0.

> [!WARNING]
> **Công thức nhiều tầng phải bấm tính hai lần.**
>
> - Ví dụ "Trà đào" dùng "trà ủ", "trà ủ" có công thức riêng.
> - Lần 1: tính giá "trà ủ".
> - Lần 2: đưa giá đó vào "Trà đào".

> [!TIP]
> Sửa, tắt hoặc xoá công thức thì giá vốn tự tính lại ngay. Xoá hết công thức đang hoạt động thì giá vốn giữ giá cuối cùng, không tụt về 0.

> [!TIP]
> Đơn vị trong công thức được phép khác đơn vị tồn kho. Khai 18 gram trong khi kho quản lý theo kg vẫn đúng, hệ thống tự quy đổi.

## Kiểm tra đã đúng

- [ ] Công thức có đủ nguyên liệu, đúng định lượng và đơn vị
- [ ] Cột **Giá vốn** của công thức không còn "Chưa tính"
- [ ] Không có cảnh báo nguyên liệu thiếu giá vốn
