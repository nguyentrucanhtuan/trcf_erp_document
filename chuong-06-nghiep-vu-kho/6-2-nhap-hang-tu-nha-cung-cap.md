---
title: "6.2 Nhập hàng từ nhà cung cấp"
description: "Lập đơn mua → xác nhận → nhận hàng. Nhận hàng mới cộng kho và cập nhật giá vốn."
---

**Đường dẫn:** *Vận hành → Mua hàng* hoặc *Vận hành → Nhập hàng* trên màn bán hàng
**Ba trạng thái:** Nháp → Đã xác nhận → Đã nhập kho

![Tạo đơn mua hàng](/images/06-nhap-hang.png)

## Các bước

1. Bấm **Tạo đơn mua hàng**.
2. Điền phần đầu phiếu (bảng dưới).
3. Bấm **Thêm dòng** cho từng mặt hàng. Tổng tiền tự tính.
4. Bấm **Lưu đơn nháp**.
5. Kiểm tra lại → bấm **Xác nhận**.
6. Khi hàng về tới quán → bấm **Nhận hàng**.

## Giải thích các trường

**Đầu phiếu**

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Nhà cung cấp | Bên giao hàng | ✅ |
| Kho nhập hàng | Kho nhận hàng về | ✅ |
| Ngày đặt hàng | Ngày đặt | ✅ |
| Phương thức thanh toán | Tiền mặt / chuyển khoản | ✅ |

**Từng dòng hàng**

| Trường | Điền gì |
|---|---|
| Sản phẩm | Hàng mua (chỉ hiện hàng đã bật *Có thể mua*) |
| Số lượng, Đơn vị | Nhập theo đơn vị lớn được — mua 5 *Kg*, hệ thống quy ra 5000 g |
| Đơn giá, VAT | Giá và thuế suất trên hoá đơn NCC |

## Nhận hàng làm gì

Bấm **Nhận hàng** → hệ thống đồng thời:

1. **Cộng hàng vào kho**
2. **Ghi tiền vào sổ quỹ** (nếu đơn đã đánh dấu thanh toán)
3. **Cập nhật giá vốn** sản phẩm theo đơn giá trên phiếu

💡 Sản phẩm bật *Sản xuất* thì **bỏ qua bước cập nhật giá vốn** — giá vốn của nó do công thức tính ([mục 3.5](/chuong-03-quan-ly-san-pham/3-5-cau-hinh-cong-thuc-va-bien-the)).

## Kiểm tra đã đúng

- [ ] Đơn ở trạng thái **Đã nhập kho**
- [ ] Tồn kho đã tăng đúng số lượng
- [ ] Giá vốn nguyên liệu đã cập nhật (nếu là hàng thường)

## Lưu ý

⚠️ **Nhận hàng chỉ bấm được một lần.** Bấm lần hai bị chặn — nếu không, kho sẽ cộng gấp đôi.

⚠️ **Đơn đã nhập kho thì không sửa dòng hàng, không xoá.** Nhập nhầm số lượng → lập **phiếu trả hàng NCC** (*Vận hành → Trả hàng NCC*) cho phần dư.

⚠️ Đơn đã thanh toán rồi gỡ rồi bật lại cũng bị chặn — cùng lý do với phiếu chi ([mục 6.1](/chuong-06-nghiep-vu-kho/6-1-nhap-chi-phi)).
