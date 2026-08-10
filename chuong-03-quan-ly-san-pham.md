---
title: "Chương 3 — Quản lý sản phẩm"
description: "Danh mục, sản phẩm, phân loại nguyên liệu/bán thành phẩm/thành phẩm, thuộc tính size và công thức pha chế."
---

# Chương 3 — Quản lý sản phẩm

[← Chương 2](/chuong-02-kho-va-don-vi-tinh) · [Về mục lục](/) · [Chương 4 →](/chuong-04-thiet-lap-pos)

Đây là chương dài nhất và cũng là chương quyết định chất lượng số liệu về sau.
Khai sản phẩm sai thì tồn kho sai, giá vốn sai, báo cáo lãi lỗ sai theo.

Thứ tự làm: **danh mục → sản phẩm → thuộc tính → biến thể → công thức**.

---

## 3.1 Tạo danh mục sản phẩm POS

*Quản lý sản phẩm → Danh mục*

Danh mục là **các nút nhóm món trên màn bán hàng**: Cà phê, Trà, Bánh, Đồ ăn
vặt. Thu ngân bấm nhóm rồi mới chọn món.

### Làm từng bước

1. Bấm **Thêm danh mục**.
2. Điền:

   | Trường | Điền gì |
   |---|---|
   | **Tên danh mục** | VD "Cà phê", "Trà trái cây". |
   | **Màu sắc đại diện** | Màu nút trên màn bán hàng, giúp thu ngân nhận diện nhanh. |
   | **Mô tả** | Không bắt buộc. |
   | **Hiển thị ngoài POS** | Bật = hiện trên màn bán hàng. Tắt = chỉ dùng nội bộ (VD nhóm "Nguyên liệu"). |

3. Bấm **Lưu**.

![Thêm danh mục sản phẩm](/images/03-danh-muc-them.png)

### Sắp xếp thứ tự hiển thị

Danh sách danh mục **kéo thả được**. Nhóm nào bán chạy thì kéo lên đầu để thu
ngân bấm ít hơn. Thứ tự này chính là thứ tự hiện trên màn bán hàng.

### Lưu ý nghiệp vụ

⚠️ Danh mục đang gắn sản phẩm thì **không xoá được** — hệ thống báo và liệt kê.
Muốn ẩn khỏi màn bán hàng thì tắt *Hiển thị ngoài POS*, đừng xoá.

💡 Nguyên liệu (cà phê hạt, sữa, đường) nên gom vào một danh mục riêng và **tắt**
*Hiển thị ngoài POS*. Như vậy quản lý vẫn lọc được, còn thu ngân không thấy rác
trên màn bán hàng.

---

## 3.2 Thêm sản phẩm mới

*Quản lý sản phẩm → Sản phẩm → **Thêm sản phẩm***

Form sản phẩm chia hai cột trên cùng một màn — không còn tab, không phải bấm qua
lại. Cột trái là thứ nhập nhiều, cột phải là thứ liếc mắt kiểm tra.

![Form thêm sản phẩm](/images/03-san-pham-them.png)

### Làm từng bước

**Cột trái — Thông tin chính**

| Trường | Điền gì |
|---|---|
| **Tên sản phẩm** | Tên hiện trên bill và màn bếp. |
| **Mã SP (SKU)** | Mã ngắn để tra cứu, VD `CFSD01`. |
| **Đơn vị tính chính** | Đơn vị dùng để tính tồn. Đồ uống → *Ly*; nguyên liệu → *Gram* hoặc *ml*. |
| **Loại sản phẩm** | Thành phẩm / Bán thành phẩm / Nguyên liệu — xem [mục 3.3](#33-phân-biệt-nguyên-liệu--bán-thành-phẩm--thành-phẩm). |
| **Đơn vị tính phụ** | Các đơn vị khác cũng dùng cho hàng này (VD nhập theo *Kg*, trừ theo *Gram*). |
| **Danh mục** | Chọn một hoặc nhiều nhóm ở mục 3.1. |
| **Nhóm Addon** | Nhóm topping/mức đường sẽ hỏi khi bán món này. |

**Cột trái — Ghi chú pha chế**

- Các ô chọn ở đây (VD *ĐÁ*: ít đá / nhiều đá) là **ghi chú cho pha chế**. Thu
  ngân bấm khi bán, chữ được ghép vào tên món trên bill và màn bếp.
- **Ghi chú công thức ⚡** — văn bản tự do hiện trên màn bếp khi làm món.

**Cột phải**

| Nhóm | Nội dung |
|---|---|
| **Ảnh sản phẩm** | Ảnh JPEG/PNG/WebP tối đa 10MB, hệ thống tự nén. |
| **Giá & thuế** | *Giá bán* (giá trên POS), *Giá vốn*, *VAT bán ra*, *VAT mua vào*. |
| **Thiết lập** | 4 công tắc: Theo dõi tồn kho · Có thể bán · Có thể mua · Sản xuất. |

Bấm **Lưu sản phẩm**. Nút Lưu luôn nằm ở đáy khung, không cần cuộn xuống tìm.

### Bốn công tắc "Thiết lập" nghĩa là gì

| Công tắc | Bật khi nào | Hệ quả |
|---|---|---|
| **Theo dõi tồn kho** | Hàng cần đếm tồn: nguyên liệu, bánh đóng gói. | Xuất hiện trong màn Tồn kho, bị cộng/trừ khi nhập–bán–huỷ. |
| **Có thể bán** | Món bán cho khách. | Hiện trên màn bán hàng. |
| **Có thể mua** | Hàng mua từ nhà cung cấp. | Chọn được trong phiếu nhập hàng. |
| **Sản xuất (có công thức)** | Món pha chế từ nguyên liệu. | Mở đường dùng công thức; **giá vốn bị khoá** và do công thức tính. |

Ví dụ thường gặp:

- **Cà phê sữa** (món bán): Có thể bán ✅, Sản xuất ✅, Theo dõi tồn kho ❌
  (không đếm tồn "ly cà phê", chỉ đếm nguyên liệu).
- **Cà phê hạt** (nguyên liệu): Có thể mua ✅, Theo dõi tồn kho ✅, Có thể bán ❌.
- **Bánh mua sẵn về bán lại**: Có thể bán ✅, Có thể mua ✅, Theo dõi tồn kho ✅,
  Sản xuất ❌.

### Lưu ý nghiệp vụ

⚠️ **Bật *Sản xuất* thì ô Giá vốn chuyển sang màu xám và không nhập được.** Đây
không phải lỗi: giá vốn của món pha chế được tính từ công thức (mục 3.5) chứ
không gõ tay. Nhập tay thì mỗi lần giá nguyên liệu đổi lại phải sửa từng món.

⚠️ **Tên sản phẩm và SKU không được trùng**, kể cả khác hoa thường và kể cả với
sản phẩm đã lưu trữ. Đây là chặn có chủ đích để tránh hai dòng "Cà phê sữa" song
song làm loạn báo cáo.

⚠️ Sản phẩm đã phát sinh giao dịch (đã bán, đã nhập, có tồn khác 0, đang là
nguyên liệu trong công thức, đang là topping) thì **không xoá được**. Hệ thống
liệt kê rõ nơi đang dùng. Ngừng bán thì dùng **Lưu trữ**.

💡 Sản phẩm mới tạo, chưa bán chưa nhập, thì xoá thoải mái.

---

## 3.3 Phân biệt Nguyên liệu – Bán thành phẩm – Thành phẩm

Trường *Loại sản phẩm* có ba lựa chọn. Nó **không** tự thay đổi hành vi hệ thống —
hành vi do bốn công tắc ở mục 3.2 quyết định — nhưng nó là cách quán tự phân
loại, và là căn cứ cho màn **Rà soát vận hành** ở chương 8.

| Loại | Là gì | Ví dụ | Thường bật công tắc |
|---|---|---|---|
| **Nguyên liệu** | Mua về, không bán trực tiếp, dùng để làm ra thứ khác. | Cà phê hạt, sữa đặc, đường, ly nhựa. | Có thể mua, Theo dõi tồn kho |
| **Bán thành phẩm** | Quán tự làm ra, nhưng chưa bán cho khách; là đầu vào của món khác. | Cà phê cốt ủ sẵn, trà ủ, syrup tự nấu. | Sản xuất, Theo dõi tồn kho |
| **Thành phẩm** | Món bán cho khách. | Cà phê sữa đá, trà đào. | Có thể bán, Sản xuất |

### Vì sao cần bán thành phẩm

Quán ủ sẵn một bình cà phê cốt buổi sáng, cả ngày múc ra pha. Nếu không có bán
thành phẩm, mỗi ly bán ra sẽ phải trừ trực tiếp cà phê hạt + nước — trong khi
thực tế việc ủ đã xảy ra từ sáng.

Có bán thành phẩm thì tách được hai bước:

1. **Sáng**: lập phiếu chế biến — trừ cà phê hạt, cộng "cà phê cốt" vào kho.
   (Xem [mục 6.4](/chuong-06-nghiep-vu-kho#64-chế-biến-bán-thành-phẩm))
2. **Cả ngày**: mỗi ly bán ra trừ "cà phê cốt" theo công thức.

Nhờ vậy cuối ngày biết được bình cốt còn bao nhiêu, và hao hụt nằm ở khâu ủ hay
khâu bán.

### Lưu ý nghiệp vụ

💡 Quán nhỏ chưa cần chi tiết tới mức đó thì bỏ qua bán thành phẩm: cho món bán
trừ thẳng nguyên liệu. Có thể bổ sung sau mà không phải làm lại dữ liệu cũ.

---

## 3.4 Tạo thuộc tính sản phẩm (Size S/M/L)

*Quản lý sản phẩm → Thuộc tính*

![Danh sách thuộc tính](/images/03-thuoc-tinh-danh-sach.png)

### Hai loại thuộc tính — phân biệt trước khi tạo

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

### Làm từng bước

1. Bấm **Thêm thuộc tính**.
2. Điền *Tên thuộc tính* (VD "Size").
3. **Bật hoặc tắt *Tạo biến thể*** theo bảng trên.
4. Nhập các *Giá trị thuộc tính*, mỗi giá trị một dòng (VD NHỎ, VỪA, LỚN).
   Kéo biểu tượng ⠿ để đổi thứ tự — thứ tự này là thứ tự hiện trên POS.
5. Bấm **Lưu**.

![Thêm thuộc tính](/images/03-thuoc-tinh-them.png)

### Lưu ý nghiệp vụ

⚠️ **Không tắt được *Tạo biến thể*** khi thuộc tính đó đã sinh ra biến thể đang
bán. Hệ thống chặn và báo rõ. Tắt được thì mọi biến thể sẽ mất giá riêng và
công thức riêng mà không ai hay.

⚠️ **Đổi tên giá trị thì an toàn** (VD "VỪA" → "SIZE M"): biến thể giữ nguyên,
chỉ đổi chữ hiển thị. Nhưng **xoá bớt giá trị** đang có biến thể thì bị chặn —
xoá được thì biến thể tương ứng thành mồ côi.

💡 Muốn "ít đá" trừ ít đá thật trong kho thì phải làm bằng **biến thể có công
thức riêng**, không phải bằng ghi chú pha chế. Ghi chú pha chế chỉ là chữ.

---

## 3.5 Cấu hình công thức pha chế và biến thể

### Bước A — Sinh biến thể

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

### Bước B — Tạo công thức (BOM)

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

### Bước C — Tính giá vốn

Sau khi lưu công thức, ở dòng công thức bấm **Tính giá vốn** (hoặc nút **Tính
lại giá vốn** ở đầu trang để tính cả loạt).

Hệ thống tính: `giá vốn = tổng (giá vốn nguyên liệu × định lượng đã quy đổi) ÷ sản lượng`,
rồi ghi ngược vào *Giá vốn* của sản phẩm.

Sản phẩm có nhiều công thức đang hoạt động thì lấy **công thức rẻ nhất**.

### Lưu ý nghiệp vụ

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

---

[← Chương 2](/chuong-02-kho-va-don-vi-tinh) · [Về mục lục](/) · [Chương 4 — Thiết lập POS →](/chuong-04-thiet-lap-pos)
