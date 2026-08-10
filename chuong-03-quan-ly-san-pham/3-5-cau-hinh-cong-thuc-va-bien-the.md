---
title: "3.5 Cấu hình công thức pha chế và biến thể"
description: "Khai công thức pha chế, tính giá vốn và sinh biến thể theo thuộc tính."
---

## Bước A — Sinh biến thể

*Quản lý sản phẩm → Biến thể → **Sinh biến thể***

![Sinh biến thể](/images/03-sinh-bien-the.png)

1. Chọn **Sản phẩm** gốc (VD Trà đào).
2. Chọn các **giá trị thuộc tính tạo biến thể** (VD Size: VỪA, LỚN).
3. Điền **Phụ thu** nếu muốn: giá biến thể = giá sản phẩm gốc + phụ thu.
4. Bấm sinh. Hệ thống tạo một biến thể cho **mỗi tổ hợp**, và **bỏ qua tổ hợp đã
   có** — bấm lại lần nữa không tạo trùng.

Chọn 2 thuộc tính (Size 3 giá trị × Đế 2 loại) sẽ sinh 6 biến thể.

![Danh sách biến thể](/images/03-bien-the-danh-sach.png)

Danh sách biến thể hiện **giá bán đã cộng phụ thu** — đây là giá thu ngân thấy
trên POS, không phải giá gốc của sản phẩm.

## Bước B — Tạo công thức (BOM)

*Quản lý sản phẩm → Công thức → **Thêm công thức***

![Tạo công thức](/images/03-cong-thuc-them.png)

| Trường | Điền gì |
|---|---|
| **Sản phẩm (thành phẩm)** | Món cần công thức. Danh sách chỉ hiện sản phẩm đã bật *Sản xuất*. |
| **Biến thể (tuỳ chọn)** | Để trống = công thức chung cho mọi size. Chọn size = công thức riêng cho size đó. |
| **Loại công thức** | *Cần sản xuất* hoặc *Kit* — xem bảng dưới. |
| **Sản lượng (yield)** | Công thức này làm ra bao nhiêu thành phẩm. Ủ một mẻ được 20 ly thì điền 20. |
| **Hoạt động** | Tắt = công thức tạm ngừng dùng. |
| **Nguyên liệu** | Bấm *Thêm nguyên liệu*, chọn hàng và định lượng kèm đơn vị. |

**Hai loại công thức:**

| Loại | Trừ kho khi nào | Dùng cho |
|---|---|---|
| **Cần sản xuất** | Khi lập **phiếu chế biến** (chương 6.4). | Bán thành phẩm ủ trước: cà phê cốt, trà ủ, syrup. |
| **Kit** | Ngay **lúc bán**, tự trừ thành phần. | Combo, món ráp tại chỗ không qua bước chế biến. |

## Bước C — Tính giá vốn

Sau khi lưu công thức, ở dòng công thức bấm **Tính giá vốn** (hoặc nút **Tính
lại giá vốn** ở đầu trang để tính cả loạt).

Hệ thống tính: `giá vốn = tổng (giá vốn nguyên liệu × định lượng đã quy đổi) ÷ sản lượng`,
rồi ghi ngược vào *Giá vốn* của sản phẩm.

Sản phẩm có nhiều công thức đang hoạt động thì lấy **công thức rẻ nhất**.

## Lưu ý nghiệp vụ

⚠️ **Nguyên liệu có giá vốn bằng 0 sẽ làm giá vốn món sai.** Sau khi bấm tính,
hệ thống cảnh báo tên những nguyên liệu chưa có giá. Giá vốn nguyên liệu được
cập nhật tự động mỗi lần nhập hàng — nên nguyên liệu chưa nhập lần nào thì vẫn
là 0.

⚠️ **Công thức nhiều tầng cần bấm tính hai lần.** Ví dụ trà đào dùng "trà ủ", mà
"trà ủ" lại có công thức riêng: lần bấm đầu tính xong giá "trà ủ", lần bấm thứ
hai mới đưa được giá đó vào trà đào.

💡 **Sửa, tắt hoặc xoá công thức thì giá vốn sản phẩm tự tính lại ngay** — không
phải nhớ bấm nút. Nếu xoá hết công thức đang hoạt động, giá vốn giữ nguyên giá
cuối cùng thay vì tụt về 0.

💡 Đơn vị trong công thức có thể khác đơn vị tồn kho — khai 18 *gram* trong khi
kho quản lý theo *kg* là hợp lệ, hệ thống tự quy đổi.
