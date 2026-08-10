---
title: "3.4 Tạo thuộc tính sản phẩm (Size S/M/L)"
description: "Tạo thuộc tính sinh biến thể (Size) và thuộc tính ghi chú pha chế."
---

*Quản lý sản phẩm → Thuộc tính*

![Danh sách thuộc tính](/images/03-thuoc-tinh-danh-sach.png)

## Hai loại thuộc tính — phân biệt trước khi tạo

Cột **Tạo biến thể** trong ảnh trên là điểm mấu chốt:

| | **Tạo biến thể = Có** | **Tạo biến thể = Không** |
|---|---|---|
| Dùng cho | Size, loại đế bánh — thứ **khác giá, khác định lượng** | Mức đá, mức đường — thứ **chỉ là yêu cầu pha chế** |
| Sinh ra | Món riêng, có giá riêng, có công thức riêng | Không sinh món mới |
| Ảnh hưởng tiền | Có — mỗi biến thể một mức giá | Không |
| Ảnh hưởng kho | Có — công thức riêng, trừ nguyên liệu riêng | Không |
| Hiện ở đâu | Món trên POS tách thành *Trà đào (VỪA)*, *Trà đào (LỚN)* | Ghép vào tên món: *Trà đào (VỪA + ÍT ĐÁ)* |

Trong ảnh: **Size** có tạo biến thể (VỪA, LỚN) — hai size hai giá. **ĐÁ** không
tạo biến thể (ÍT ĐÁ, VỪA) — chỉ là ghi chú cho bạn pha chế.

## Làm từng bước

1. Bấm **Thêm thuộc tính**.
2. Điền *Tên thuộc tính* (VD "Size").
3. **Bật hoặc tắt *Tạo biến thể*** theo bảng trên.
4. Nhập các *Giá trị thuộc tính*, mỗi giá trị một dòng (VD NHỎ, VỪA, LỚN).
   Kéo biểu tượng ⠿ để đổi thứ tự — thứ tự này là thứ tự hiện trên POS.
5. Bấm **Lưu**.

![Thêm thuộc tính](/images/03-thuoc-tinh-them.png)

## Lưu ý nghiệp vụ

⚠️ **Không tắt được *Tạo biến thể*** khi thuộc tính đó đã sinh ra biến thể đang
bán. Hệ thống chặn và báo rõ. Tắt được thì mọi biến thể sẽ mất giá riêng và
công thức riêng mà không ai hay.

⚠️ **Đổi tên giá trị thì an toàn** (VD "VỪA" → "SIZE M"): biến thể giữ nguyên,
chỉ đổi chữ hiển thị. Nhưng **xoá bớt giá trị** đang có biến thể thì bị chặn —
xoá được thì biến thể tương ứng thành mồ côi.

💡 Muốn "ít đá" trừ ít đá thật trong kho thì phải làm bằng **biến thể có công
thức riêng**, không phải bằng ghi chú pha chế. Ghi chú pha chế chỉ là chữ.
