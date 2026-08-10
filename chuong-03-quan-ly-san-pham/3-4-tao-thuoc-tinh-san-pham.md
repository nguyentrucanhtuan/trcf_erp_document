---
title: "3.4 Tạo thuộc tính sản phẩm (Size S/M/L)"
---

- **Đường dẫn:** *Quản lý sản phẩm → Thuộc tính*.
- **Quyết định quan trọng nhất:** bật hay tắt công tắc *Tạo biến thể*.

![Danh sách thuộc tính](/images/03-thuoc-tinh-danh-sach.png)

## Chọn loại thuộc tính trước khi tạo

| | **Tạo biến thể = Có** | **Tạo biến thể = Không** |
|---|---|---|
| Dùng cho | Size, loại đế bánh — thứ **khác giá, khác định lượng** | Mức đá, mức đường — **chỉ là yêu cầu pha chế** |
| Sinh ra | Món riêng, giá riêng, công thức riêng | Không sinh món mới |
| Ảnh hưởng tiền | ✅ mỗi biến thể một giá | ❌ |
| Ảnh hưởng kho | ✅ công thức riêng, trừ nguyên liệu riêng | ❌ |
| Hiện trên POS | *Trà đào (VỪA)*, *Trà đào (LỚN)* | Ghép vào tên: *Trà đào (VỪA + ÍT ĐÁ)* |

## Các bước

1. Bấm **Thêm thuộc tính**.
2. Điền các trường theo bảng dưới.
3. Kéo biểu tượng ⠿ để xếp thứ tự giá trị — đây là thứ tự hiện trên POS.
4. Bấm **Lưu**.

![Thêm thuộc tính](/images/03-thuoc-tinh-them.png)

## Giải thích các trường

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Tên thuộc tính | VD "Size", "ĐÁ", "ĐƯỜNG" | ✅ |
| Tạo biến thể | Bật/tắt theo bảng trên. **Chọn kỹ — khó đổi về sau** | ✅ |
| Giá trị thuộc tính | Mỗi giá trị một dòng. VD NHỎ, VỪA, LỚN | ✅ |

## Kiểm tra đã đúng

- [ ] Thuộc tính khác giá (Size) → *Tạo biến thể* **bật**
- [ ] Thuộc tính chỉ là yêu cầu pha chế (ĐÁ, ĐƯỜNG) → *Tạo biến thể* **tắt**
- [ ] Thứ tự giá trị đúng như muốn hiện trên POS

## Lưu ý

⚠️ **Không tắt được *Tạo biến thể*** khi thuộc tính đã sinh biến thể đang bán. Hệ thống chặn và báo rõ — tắt được thì mọi biến thể mất giá riêng và công thức riêng mà không ai hay.

⚠️ **Đổi tên giá trị an toàn** (VD "VỪA" → "SIZE M"): biến thể giữ nguyên, chỉ đổi chữ. Nhưng **xoá bớt giá trị** đang có biến thể thì bị chặn.

💡 Muốn "ít đá" trừ ít đá thật trong kho thì phải làm bằng **biến thể có công thức riêng**, không phải ghi chú pha chế. Ghi chú pha chế chỉ là chữ.
