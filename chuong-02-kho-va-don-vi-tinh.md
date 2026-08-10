---
title: "Chương 2 — Thiết lập kho hàng, sản phẩm"
description: "Khai báo kho và đơn vị tính — hai thứ phải có trước khi tạo bất kỳ sản phẩm nào."
---

# Chương 2 — Thiết lập kho hàng, sản phẩm

[← Chương 1](/chuong-01-cau-hinh-he-thong) · [Về mục lục](/) · [Chương 3 →](/chuong-03-quan-ly-san-pham)

Hai màn trong chương này là **nền móng**: chưa có kho và đơn vị tính thì không
tạo được sản phẩm, không nhập được hàng, không bán được. Làm đúng thứ tự: kho
trước, đơn vị tính sau, rồi mới sang chương 3.

---

## 2.1 Thiết lập kho hàng

*Quản lý kho → Kho hàng*

Kho là nơi hệ thống ghi nhận hàng đang nằm ở đâu. Mỗi lần nhập, bán, chuyển,
huỷ, chế biến — hệ thống đều cộng/trừ vào một kho cụ thể.

![Danh sách kho](/images/02-kho-danh-sach.png)

### Làm từng bước

1. Bấm **Thêm kho**.
2. Điền ba trường:

   | Trường | Điền gì |
   |---|---|
   | **Mã kho** | Chuỗi ngắn không dấu, viết hoa. VD `KHO-TONG`, `KHO-QUAY`. |
   | **Tên kho** | Tên người đọc hiểu. VD "Kho tổng", "Kho quầy pha chế". |
   | **Địa chỉ** | Không bắt buộc. |

3. Bấm **Lưu**.

![Thêm kho mới](/images/02-kho-them-moi.png)

### Nên chia bao nhiêu kho

Cách chia phổ biến cho một quán:

- **Kho tổng** — nơi nhận hàng từ nhà cung cấp, chứa nguyên liệu chưa dùng tới.
- **Kho quầy** — nguyên liệu đã đưa ra quầy, là kho bị trừ khi bán hàng.

Chia như vậy để biết được "còn bao nhiêu trong kho tổng để tiếp cho quầy". Quán
nhỏ, một chỗ chứa duy nhất thì để **một kho** cũng hoàn toàn hợp lệ — khi đó ở
Cấu hình hệ thống chọn cùng kho đó cho tất cả các ô.

### Lưu ý nghiệp vụ

⚠️ **Kho đã phát sinh giao dịch thì không xoá được.** Bấm xoá sẽ nhận thông báo
liệt kê rõ những chỗ đang dùng kho đó (tồn kho, phiếu nhập, phiếu chuyển, phiếu
kiểm...). Đây là cố ý: xoá kho đi thì các phiếu cũ mất chỗ tham chiếu, sổ sách
lịch sử sẽ sai. Kho không dùng nữa thì **lưu trữ**, đừng xoá.

⚠️ Kho đang được đặt làm kho mặc định trong *Cấu hình hệ thống* cũng không xoá
được. Muốn xoá, phải đổi cấu hình sang kho khác trước.

💡 Kho vừa tạo mà chưa nhập gì thì xoá được bình thường — hệ thống phân biệt được
"kho trống mới tạo" và "kho đã có lịch sử".

---

## 2.2 Thiết lập đơn vị tính (UOM)

*Quản lý sản phẩm → Đơn vị tính*

Đơn vị tính trả lời câu hỏi: **hàng này đếm bằng gì**. Ly, kg, gram, chai, thùng.

![Danh sách đơn vị tính](/images/02-uom-danh-sach.png)

### Khái niệm cần nắm trước khi điền

Hệ thống dùng mô hình **đơn vị gốc + đơn vị quy đổi**:

- **Đơn vị gốc** là đơn vị nhỏ nhất bạn muốn lưu tồn kho. Ví dụ với sữa: chọn
  **ml** làm gốc.
- **Đơn vị quy đổi** là đơn vị to hơn, khai kèm **hệ số** so với gốc. Ví dụ:
  *Lít* = 1000 ml → hệ số 1000, đơn vị quy đổi là *ml*.

Nhờ vậy nhân viên nhập hàng theo *thùng*, pha chế trừ theo *ml*, mà tồn kho vẫn
là một con số thống nhất.

### Làm từng bước

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

### Ví dụ khai một bộ đơn vị cho quán

| Mã | Tên | Hệ số | Quy đổi về | Ý nghĩa |
|---|---|---|---|---|
| `LY` | Ly | 1 | *(gốc)* | Đơn vị bán đồ uống |
| `G` | Gram | 1 | *(gốc)* | Đơn vị gốc cho nguyên liệu khô |
| `KG` | Kilogam | 1000 | Gram | 1 kg = 1000 g |
| `ML` | Mililít | 1 | *(gốc)* | Đơn vị gốc cho nguyên liệu lỏng |
| `L` | Lít | 1000 | Mililít | 1 lít = 1000 ml |

Sau đó khi nhập 5 kg cà phê, hệ thống ghi tồn **5000 g**; công thức trừ 18 g mỗi
ly vẫn tính đúng.

### Lưu ý nghiệp vụ

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

---

[← Chương 1](/chuong-01-cau-hinh-he-thong) · [Về mục lục](/) · [Chương 3 — Quản lý sản phẩm →](/chuong-03-quan-ly-san-pham)
