---
title: "5.5 Cấu hình và xuất hoá đơn VAT"
description: "Khai cấu hình Minvoice và phát hành hoá đơn GTGT cho khách."
---

Áp dụng cho quán có hợp đồng hoá đơn điện tử với **Minvoice**.

## Bước 1 — Khai cấu hình (làm một lần)

Vào *Thiết lập cửa hàng → Cấu hình hệ thống*, nhóm **Hoá đơn điện tử (Minvoice)**:

| Trường | Lấy ở đâu |
|---|---|
| Tên đăng nhập, Mật khẩu | Nhà cung cấp hoá đơn điện tử cấp |
| Tên cửa hàng/Công ty | Tên pháp nhân trên giấy phép |
| Mã số thuế doanh nghiệp | MST của quán |
| API Token | Nhà cung cấp cấp |
| Ký hiệu hoá đơn | VD `C25TAA` |

Bấm **Lưu cấu hình**.

## Bước 2 — Xuất hoá đơn cho đơn hàng

*Vận hành → Hoá đơn VAT → **Tạo hoá đơn***

![Tạo hoá đơn GTGT](/images/05-hoa-don-vat.png)

1. Chọn **Đơn hàng** cần xuất hoá đơn.
2. Chọn **Loại người mua**:
   - *Không lấy hoá đơn* — khách không yêu cầu.
   - *Cá nhân* — điền tên, email, địa chỉ.
   - *Doanh nghiệp* — điền thêm **Mã số thuế**.
3. Bấm **Tạo hoá đơn**. Hoá đơn ở trạng thái **Nháp**.
4. Kiểm tra lại thông tin người mua, rồi bấm **Phát hành** để gửi lên cơ quan
   thuế qua Minvoice.

## Lưu ý nghiệp vụ

⚠️ **Xuất hoá đơn không đụng tới tiền.** Tiền đã được ghi vào sổ quỹ từ lúc khách
thanh toán. Hoá đơn GTGT chỉ là chứng từ thuế.

⚠️ **Hoá đơn đã phát hành thì không sửa, không xoá, không huỷ được** trong hệ
thống — vì nó đã lên cơ quan thuế. Kiểm tra kỹ MST và tên công ty **trước khi**
bấm Phát hành.

⚠️ Chưa khai đủ cấu hình Minvoice mà bấm Phát hành thì hệ thống báo *"Thiếu cấu
hình Minvoice"* và **giữ nguyên hoá đơn ở trạng thái Nháp** — không có chuyện
phát hành nửa vời.

💡 Đơn nào cũng chỉ có **một** hoá đơn. Bấm tạo lần hai cho cùng đơn sẽ mở lại
bản nháp đang có chứ không tạo bản thứ hai.
