---
title: "6.2 Nhập hàng từ nhà cung cấp"
description: "Lập đơn mua, xác nhận và nhận hàng vào kho."
---

*Vận hành → Mua hàng* · hoặc *Vận hành → Nhập hàng* trên màn bán hàng

![Tạo đơn mua hàng](/images/06-nhap-hang.png)

## Làm từng bước

1. Bấm **Tạo đơn mua hàng**.
2. Chọn *Nhà cung cấp*, *Kho nhập hàng*, *Ngày đặt hàng*, *Phương thức thanh
   toán*.
3. Bấm **Thêm dòng** cho từng mặt hàng: chọn sản phẩm, số lượng, đơn vị, đơn giá,
   VAT. Tổng tiền tự tính ở dưới.
4. Bấm **Lưu đơn nháp**.
5. Kiểm tra lại rồi bấm **Xác nhận**.
6. Khi hàng về tới quán, bấm **Nhận hàng** → hệ thống **cộng hàng vào kho** và
   ghi tiền vào sổ quỹ nếu đơn đã đánh dấu thanh toán.

Ba trạng thái: **Nháp → Đã xác nhận → Đã nhập kho**.

## Giá vốn tự cập nhật

Mỗi lần nhận hàng, hệ thống lấy đơn giá trên phiếu để cập nhật **giá vốn** của
sản phẩm. Đây là nguồn giá vốn cho công thức và cho báo cáo lãi lỗ.

Sản phẩm có bật *Sản xuất* thì **bỏ qua** — giá vốn của nó do công thức tính
(xem [mục 3.5](/chuong-03-quan-ly-san-pham/3-5-cau-hinh-cong-thuc-va-bien-the)).

## Lưu ý nghiệp vụ

⚠️ **Nhận hàng chỉ bấm được một lần.** Bấm hai lần thì lần sau bị chặn — nếu
không, kho sẽ cộng gấp đôi.

⚠️ **Đơn đã nhập kho thì không sửa dòng hàng, không xoá.** Nhập nhầm số lượng
thì lập **phiếu trả hàng NCC** (*Vận hành → Trả hàng NCC*) cho phần dư.

⚠️ Đơn đã thanh toán rồi gỡ thanh toán rồi bật lại cũng bị chặn — cùng lý do với
phiếu chi ở mục 6.1.

💡 Nhập theo đơn vị lớn được: mua 5 *Kg* cà phê trong khi kho quản lý theo
*Gram*, hệ thống tự quy ra 5000 g.
