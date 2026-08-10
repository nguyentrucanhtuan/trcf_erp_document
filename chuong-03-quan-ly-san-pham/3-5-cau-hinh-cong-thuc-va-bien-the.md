---
title: "3.5 Cấu hình công thức pha chế và biến thể"
---

- **Đường dẫn:** *Quản lý sản phẩm → Biến thể* và *→ Công thức*.
- **Cần có trước:** sản phẩm bật *Sản xuất* (3.2), thuộc tính bật *Tạo biến thể* (3.4)
- **Thứ tự:** sinh biến thể → tạo công thức → tính giá vốn.

## Bước A — Sinh biến thể

![Sinh biến thể](/images/03-sinh-bien-the.png)

1. Vào *Biến thể* → bấm **Sinh biến thể**.
2. Chọn **Sản phẩm** gốc (VD Trà đào).
3. Chọn các **giá trị thuộc tính** (VD Size: VỪA, LỚN).
4. Điền **Phụ thu** nếu có.
5. Bấm sinh.

| Trường | Điền gì |
|---|---|
| Sản phẩm | Món gốc cần tách size |
| Giá trị thuộc tính | Chọn nhiều — hệ thống sinh **mỗi tổ hợp một biến thể** |
| Phụ thu | Giá biến thể = giá sản phẩm gốc **+ phụ thu** |

💡 Chọn 2 thuộc tính (Size 3 giá trị × Đế 2 loại) sẽ sinh **6 biến thể**. Bấm sinh lại lần nữa **không tạo trùng** — hệ thống bỏ qua tổ hợp đã có.

![Danh sách biến thể](/images/03-bien-the-danh-sach.png)

⚠️ Danh sách biến thể hiện **giá đã cộng phụ thu** — đây là giá thu ngân thấy trên POS, không phải giá gốc.

## Bước B — Tạo công thức (BOM)

![Tạo công thức](/images/03-cong-thuc-them.png)

1. Vào *Công thức* → bấm **Thêm công thức**.
2. Điền các trường theo bảng dưới.
3. Bấm **Thêm nguyên liệu**, chọn hàng + định lượng + đơn vị.
4. Bấm **Lưu**.

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Sản phẩm (thành phẩm) | Món cần công thức. Danh sách **chỉ hiện sản phẩm đã bật *Sản xuất*** | ✅ |
| Biến thể | Bỏ trống = công thức chung mọi size · Chọn size = công thức riêng size đó | — |
| Loại công thức | *Cần sản xuất* hoặc *Kit* — xem bảng dưới | ✅ |
| Sản lượng (yield) | Công thức làm ra bao nhiêu thành phẩm. Ủ một mẻ được 20 ly → điền 20 | ✅ |
| Hoạt động | Tắt = công thức tạm ngừng dùng | — |
| Nguyên liệu | Hàng + định lượng + đơn vị | ✅ |

**Hai loại công thức:**

| Loại | Trừ kho khi nào | Dùng cho |
|---|---|---|
| Cần sản xuất | Khi lập **phiếu chế biến** ([6.4](/chuong-06-nghiep-vu-kho/6-4-che-bien-ban-thanh-pham)) | Bán thành phẩm ủ trước: cà phê cốt, trà ủ, syrup |
| Kit | Ngay **lúc bán**, tự trừ thành phần | Combo, món ráp tại chỗ không qua chế biến |

## Bước C — Tính giá vốn

1. Ở dòng công thức bấm **Tính giá vốn** (hoặc **Tính lại giá vốn** đầu trang để tính cả loạt).
2. Đọc cảnh báo nếu có nguyên liệu chưa có giá.

Công thức tính: `giá vốn = tổng (giá vốn nguyên liệu × định lượng đã quy đổi) ÷ sản lượng`

Sản phẩm có nhiều công thức đang hoạt động → lấy **công thức rẻ nhất**.

## Kiểm tra đã đúng

- [ ] Biến thể hiện đúng số tổ hợp mong đợi, giá đã cộng phụ thu
- [ ] Công thức có đủ nguyên liệu, sản lượng khớp thực tế một mẻ
- [ ] Bấm *Tính giá vốn* → giá vốn sản phẩm **khác 0** và không có cảnh báo

## Lưu ý

⚠️ **Nguyên liệu giá vốn = 0 làm giá vốn món sai.** Sau khi bấm tính, hệ thống cảnh báo tên nguyên liệu chưa có giá. Giá vốn nguyên liệu tự cập nhật mỗi lần nhập hàng — nguyên liệu chưa nhập lần nào thì vẫn là 0.

⚠️ **Công thức nhiều tầng phải bấm tính hai lần.** Trà đào dùng "trà ủ", mà "trà ủ" lại có công thức riêng: lần đầu tính giá "trà ủ", lần hai mới đưa giá đó vào trà đào.

💡 **Sửa / tắt / xoá công thức thì giá vốn tự tính lại ngay** — không phải nhớ bấm nút. Xoá hết công thức đang hoạt động thì giá vốn giữ giá cuối cùng, không tụt về 0.

💡 Đơn vị trong công thức được phép khác đơn vị tồn kho — khai 18 *gram* trong khi kho quản lý theo *kg* là hợp lệ, hệ thống tự quy đổi.
