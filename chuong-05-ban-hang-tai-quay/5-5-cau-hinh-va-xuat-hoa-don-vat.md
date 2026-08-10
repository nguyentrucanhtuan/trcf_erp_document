---
title: "5.5 Cấu hình và xuất hoá đơn VAT"
---

- **Áp dụng cho:** Quán có hợp đồng hoá đơn điện tử với **Minvoice**.
- **Đường dẫn:** Cấu hình ở *Thiết lập cửa hàng → Cấu hình hệ thống* · Xuất hoá đơn ở *Vận hành → Hoá đơn VAT*.

## Bước 1 — Khai cấu hình (làm một lần)

1. Vào *Cấu hình hệ thống* → nhóm **Hoá đơn điện tử (Minvoice)**.
2. Điền 6 trường theo bảng dưới.
3. Bấm **Lưu cấu hình**.

| Trường | Lấy ở đâu |
|---|---|
| Tên đăng nhập, Mật khẩu | Nhà cung cấp hoá đơn điện tử cấp |
| Tên cửa hàng / Công ty | Tên pháp nhân trên giấy phép |
| Mã số thuế doanh nghiệp | MST của quán |
| API Token | Nhà cung cấp cấp |
| Ký hiệu hoá đơn | VD `C25TAA` |

## Bước 2 — Xuất hoá đơn cho đơn hàng

![Tạo hoá đơn GTGT](/images/05-hoa-don-vat.png)

1. Vào *Vận hành → Hoá đơn VAT* → bấm **Tạo hoá đơn**.
2. Chọn **Đơn hàng** cần xuất.
3. Chọn **Loại người mua** và điền thông tin tương ứng (bảng dưới).
4. Bấm **Tạo hoá đơn** → hoá đơn ở trạng thái **Nháp**.
5. **Kiểm tra lại MST và tên công ty**, rồi bấm **Phát hành**.

| Loại người mua | Điền thêm |
|---|---|
| Không lấy hoá đơn | — |
| Cá nhân | Tên, email, địa chỉ |
| Doanh nghiệp | Tên, email, địa chỉ + **Mã số thuế** |

## Kiểm tra đã đúng

- [ ] Hoá đơn chuyển từ **Nháp** sang **Đã phát hành**
- [ ] Có **mã cơ quan thuế** hiện trên dòng hoá đơn

## Lưu ý

⚠️ **Xuất hoá đơn không đụng tới tiền.** Tiền đã ghi vào sổ quỹ từ lúc khách thanh toán. Hoá đơn GTGT chỉ là chứng từ thuế.

⚠️ **Hoá đơn đã phát hành thì không sửa, không xoá, không huỷ được** — nó đã lên cơ quan thuế. Kiểm kỹ MST và tên công ty **trước khi** bấm Phát hành.

⚠️ Chưa khai đủ cấu hình mà bấm Phát hành thì hệ thống báo *"Thiếu cấu hình Minvoice"* và **giữ hoá đơn ở trạng thái Nháp** — không có chuyện phát hành nửa vời.

💡 Mỗi đơn chỉ có **một** hoá đơn. Bấm tạo lần hai cho cùng đơn sẽ mở lại bản nháp đang có, không tạo bản thứ hai.
