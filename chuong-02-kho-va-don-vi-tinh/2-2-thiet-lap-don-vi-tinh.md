---
title: "2.2 Thiết lập đơn vị tính (UOM)"
---

- **Đường dẫn:** *Quản lý sản phẩm → Đơn vị tính*.
- **Khi nào:** Ngay sau khi tạo kho, **trước** khi tạo sản phẩm.
- **Trả lời câu hỏi:** Hàng này đếm bằng gì — ly, kg, gram, chai, thùng.

![Danh sách đơn vị tính](/images/02-uom-danh-sach.png)

## Hiểu trước khi điền

| Khái niệm | Nghĩa | Khai thế nào |
|---|---|---|
| **Đơn vị gốc** | Đơn vị nhỏ nhất dùng lưu tồn. VD sữa lấy *ml* | Hệ số = 1, bỏ trống ô quy đổi |
| **Đơn vị quy đổi** | Đơn vị to hơn. VD *Lít* = 1000 ml | Hệ số = 1000, chọn quy đổi về *ml* |

💡 Nhờ vậy nhân viên nhập theo *thùng*, pha chế trừ theo *ml*, tồn kho vẫn là một con số.

## Các bước

1. Bấm **Thêm đơn vị**.
2. Khai **đơn vị gốc trước** (hệ số 1, không chọn quy đổi).
3. Khai tiếp đơn vị lớn hơn, chọn đơn vị gốc ở ô *Đơn vị quy đổi*.
4. Bấm **Lưu**.

![Thêm đơn vị đo lường](/images/02-uom-them-moi.png)

## Giải thích các trường

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Mã đơn vị | Ngắn, viết hoa. VD `LY`, `KG`, `G`, `ML` | ✅ |
| Tên đơn vị | VD "Ly", "Kilogam", "Gram" | ✅ |
| Hệ số quy đổi | Bằng bao nhiêu đơn vị quy đổi bên cạnh. Đơn vị gốc điền **1** | ✅ |
| Đơn vị quy đổi | Bỏ trống nếu là đơn vị gốc. Chọn đơn vị gốc nếu đây là đơn vị lớn hơn | — |

## Bộ đơn vị mẫu cho quán

| Mã | Tên | Hệ số | Quy đổi về | Dùng cho |
|---|---|---|---|---|
| `LY` | Ly | 1 | *(gốc)* | Đồ uống bán ra |
| `G` | Gram | 1 | *(gốc)* | Nguyên liệu khô |
| `KG` | Kilogam | 1000 | Gram | Nhập hàng khô |
| `ML` | Mililít | 1 | *(gốc)* | Nguyên liệu lỏng |
| `L` | Lít | 1000 | Mililít | Nhập hàng lỏng |

💡 Nhập 5 kg cà phê → hệ thống ghi tồn **5000 g**; công thức trừ 18 g mỗi ly vẫn đúng.

## Kiểm tra đã đúng

- [ ] Mỗi loại nguyên liệu có **một đơn vị gốc** (hệ số 1, không quy đổi)
- [ ] Đơn vị lớn đã trỏ về đúng đơn vị gốc, hệ số đúng

## Lưu ý

⚠️ **Hệ số bị khoá sau khi đơn vị đã được dùng.** Đã có sản phẩm hoặc công thức gắn vào thì hệ thống chặn sửa. Lý do: sửa hệ số làm **toàn bộ tồn kho và giá vốn quá khứ diễn giải sai** — 5000 g đã nhập bỗng thành 5 kg. Cần đơn vị khác thì tạo mới và lưu trữ cái cũ.

⚠️ Hệ số phải **lớn hơn 0**. Hệ số 0 sẽ làm phép quy đổi mất sạch số lượng.

💡 Mã đơn vị không phân biệt hoa thường: đã có `KG` thì không tạo thêm `kg`.

💡 Chỉ khai đơn vị quán thật sự dùng — danh sách dài làm nhân viên chọn nhầm.
