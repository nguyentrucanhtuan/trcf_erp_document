---
title: "2.2 Thiết lập đơn vị tính (UOM)"
description: "Khai đơn vị tính gốc và đơn vị quy đổi để tồn kho không sai lệch."
---

*Quản lý sản phẩm → Đơn vị tính*

Đơn vị tính trả lời câu hỏi: **hàng này đếm bằng gì**. Ly, kg, gram, chai, thùng.

![Danh sách đơn vị tính](/images/02-uom-danh-sach.png)

## Khái niệm cần nắm trước khi điền

Hệ thống dùng mô hình **đơn vị gốc + đơn vị quy đổi**:

- **Đơn vị gốc** là đơn vị nhỏ nhất bạn muốn lưu tồn kho. Ví dụ với sữa: chọn
  **ml** làm gốc.
- **Đơn vị quy đổi** là đơn vị to hơn, khai kèm **hệ số** so với gốc. Ví dụ:
  *Lít* = 1000 ml → hệ số 1000, đơn vị quy đổi là *ml*.

Nhờ vậy nhân viên nhập hàng theo *thùng*, pha chế trừ theo *ml*, mà tồn kho vẫn
là một con số thống nhất.

## Làm từng bước

1. Bấm **Thêm đơn vị**.
2. Điền:

   | Trường | Điền gì |
   |---|---|
   | **Mã đơn vị** | Ngắn, viết hoa. VD `LY`, `KG`, `G`, `ML`. |
   | **Tên đơn vị** | VD "Ly", "Kilogam", "Gram". |
   | **Hệ số quy đổi** | Bằng bao nhiêu đơn vị quy đổi bên cạnh. Đơn vị gốc để **1**. |
   | **Đơn vị quy đổi** | Để trống nếu đây là đơn vị gốc. Chọn đơn vị gốc nếu đây là đơn vị lớn hơn. |

3. Bấm **Lưu**.

![Thêm đơn vị đo lường](/images/02-uom-them-moi.png)

## Ví dụ khai một bộ đơn vị cho quán

| Mã | Tên | Hệ số | Quy đổi về | Ý nghĩa |
|---|---|---|---|---|
| `LY` | Ly | 1 | *(gốc)* | Đơn vị bán đồ uống |
| `G` | Gram | 1 | *(gốc)* | Đơn vị gốc cho nguyên liệu khô |
| `KG` | Kilogam | 1000 | Gram | 1 kg = 1000 g |
| `ML` | Mililít | 1 | *(gốc)* | Đơn vị gốc cho nguyên liệu lỏng |
| `L` | Lít | 1000 | Mililít | 1 lít = 1000 ml |

Sau đó khi nhập 5 kg cà phê, hệ thống ghi tồn **5000 g**; công thức trừ 18 g mỗi
ly vẫn tính đúng.

## Lưu ý nghiệp vụ

⚠️ **Hệ số quy đổi bị khoá sau khi đơn vị đã được dùng.** Khi đã có sản phẩm hoặc
công thức gắn vào đơn vị đó, hệ thống chặn sửa hệ số và báo lỗi. Lý do: sửa hệ số
sẽ làm **toàn bộ tồn kho và giá vốn trong quá khứ diễn giải sai** — 5000 g đã nhập
bỗng thành 5 kg hay 5.000.000 g tuỳ hướng sửa. Cần đơn vị khác thì tạo đơn vị mới
và lưu trữ đơn vị cũ.

⚠️ **Hệ số phải lớn hơn 0.** Hệ thống chặn ở cả giao diện lẫn cơ sở dữ liệu —
hệ số 0 sẽ làm phép quy đổi mất sạch số lượng.

💡 Mã đơn vị **không phân biệt hoa thường**: đã có `KG` thì không tạo thêm `kg`
được.

💡 Chỉ khai đơn vị quán thật sự dùng. Danh sách dài quá làm nhân viên chọn nhầm.
