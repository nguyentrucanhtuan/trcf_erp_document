---
crumb: Bước 3 · Nhập công thức
---

# 3.1 Công thức bán thành phẩm

## 1. Đường dẫn vào chức năng

Menu trái: ==Quản lý sản phẩm → Công thức== (địa chỉ `/boms`).

- Cần có trước: bán thành phẩm bật **Sản xuất** ([bài 2.3](2-3-ban-thanh-pham.md)).
- Cần có trước: nguyên liệu ([bài 2.4](2-4-nguyen-lieu.md)), nên đã nhập hàng để có giá vốn.

### Hai loại công thức

| Loại         | Trừ kho khi nào                                       | Dùng cho                                                               |
| ------------ | ----------------------------------------------------- | ---------------------------------------------------------------------- |
| CẦN SẢN XUẤT | Khi lập **phiếu chế biến** ([11.4](11-4-che-bien.md)) | Bán thành phẩm ủ trước: TRÀ LÀI Ủ SẴN, MILKFOAM, TRÂN CHÂU NẤU SẴN     |
| KIT          | Ngay **lúc bán**, tự trừ thành phần                   | COMBO, MÓN RÁP TẠI CHỖ: CÀ PHÊ ĐEN, CÀ PHÊ SỮA, BẠC XỈU, TRÀ SỮA OLONG |

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** công thức cho "Cà phê cốt ủ", ủ một mẻ được 1000 g.
>
> - Nguyên liệu: "Cà phê hạt" 200 g + "Đường cát" 50 g.
> - Sản lượng 1000 g

### Bước 1: Tạo công thức

- Vào **Quản lý sản phẩm → Công thức**.
- Bấm **Thêm công thức**.
- **Sản phẩm (bán thành phẩm)**: chọn "Cà phê cốt ủ".
- **Loại công thức**: giữ "Cần sản xuất".
- **Sản lượng**: nhập "1000", đơn vị "Gram".
- Bấm **Thêm nguyên liệu** hai lần.
- Dòng 1: chọn "Cà phê hạt", Số lượng "200", Đơn vị tính "Gram (G)".
- Dòng 2: chọn "Đường cát", Số lượng "50", Đơn vị tính "Gram (G)".
- Bấm nút **Tạo công thức**.

![Bước 1: Tạo công thức](images/03-cong-thuc-btp-buoc-1-tao.png)

### Bước 2: Tính giá vốn

- Công thức mới có **Giá vốn** "Chưa tính".
- Bấm nút **…** ở cuối dòng.
- Chọn **Tính giá vốn**.
- Thấy thông báo *“Đã tính giá vốn công thức”*.
- Cột **Giá vốn** hiện "61₫".
- Tính cả loạt: bấm **Tính lại giá vốn** ở đầu trang.

![Bước 2: Mở menu dòng công thức](images/03-cong-thuc-btp-buoc-2-menu.png)

## 3. Giải thích các trường

### Khai công thức

| Trường                    | Điền gì                                                                | Bắt buộc |
| ------------------------- | ---------------------------------------------------------------------- | -------- |
| Sản phẩm (bán thành phẩm) | Món cần công thức. Danh sách **chỉ hiện sản phẩm đã bật *Sản xuất***   | ✅        |
| Biến thể                  | Bỏ trống: công thức chung mọi size. Chọn size: công thức riêng size đó | —        |
| Loại công thức            | Bán thành phẩm thì chọn *Cần sản xuất*                                 | ✅        |
| Sản lượng (yield)         | Công thức làm ra bao nhiêu thành phẩm. Ủ một mẻ được 20 ly: điền 20    | ✅        |
| Hoạt động                 | Tắt: công thức tạm ngừng dùng                                          | —        |
| Nguyên liệu               | Hàng + số lượng (SL) + đơn vị tính (ĐVT)                               | ✅        |

### Cách tính giá vốn

`giá vốn = tổng giá vốn nguyên liệu`

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
> - Ví dụ "Trà đào" dùng "cà phê cốt ủ", "cà phê cốt ủ" có công thức riêng.
> - Lần 1: tính giá bán thành phẩm.
> - Lần 2: đưa giá đó vào thành phẩm.

> [!TIP]
> Sửa, tắt hoặc xoá công thức thì giá vốn tự tính lại ngay. Xoá hết công thức đang hoạt động thì giá vốn giữ giá cuối cùng, không tụt về 0.

> [!TIP]
> Đơn vị trong công thức được phép khác đơn vị tồn kho. Khai 18 gram trong khi kho quản lý theo kg vẫn đúng, hệ thống tự quy đổi.

## Kiểm tra đã đúng

- [ ] Công thức có đủ nguyên liệu, đúng định lượng và đơn vị
- [ ] Cột **Giá vốn** của công thức không còn "Chưa tính"
- [ ] Không có cảnh báo nguyên liệu thiếu giá vốn
