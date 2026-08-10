---
title: "6.5 Nhập liệu hỏng huỷ"
description: "Ghi hàng hỏng, hết hạn, rơi vỡ — mỗi phiếu một mặt hàng."
---

**Đường dẫn:** *Vận hành → Huỷ hàng*
**Dùng khi:** Hàng hỏng, hết hạn, rơi vỡ, pha hỏng phải bỏ
**Lưu ý:** Mỗi phiếu **một mặt hàng**. Huỷ ba thứ thì lập ba phiếu.

![Tạo phiếu huỷ hàng](/images/06-huy-hang.png)

## Các bước

1. Bấm **Tạo phiếu huỷ hàng**.
2. Điền 5 trường theo bảng dưới.
3. Bấm **Lưu nháp** → **Xác nhận huỷ**.

## Giải thích các trường

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Kho huỷ hàng | Kho trừ hàng ra | ✅ |
| Sản phẩm huỷ | Mặt hàng bị huỷ | ✅ |
| Số lượng | Số bị huỷ | ✅ |
| Đơn vị tính | Đơn vị của số lượng | ✅ |
| Lý do huỷ | **Càng cụ thể càng tốt**: "hết hạn 09/08", "làm rơi khi bưng" | ✅ |

## Huỷ món pha sẵn

Huỷ món có công thức dạng *Kit* (VD ly trà đã pha hỏng) → hệ thống **trừ nguyên liệu theo công thức**, không trừ "ly trà" — vì trong kho không có mặt hàng "ly trà đã pha".

## Kiểm tra đã đúng

- [ ] Tồn kho giảm đúng số huỷ
- [ ] Lý do ghi đủ rõ để tháng sau đọc vẫn hiểu

## Lưu ý

⚠️ Đã xác nhận thì không sửa, không xoá.

💡 **Ghi lý do tử tế là phần có giá trị nhất của phiếu huỷ.** Cuối tháng nhìn lại sẽ thấy hao hụt nằm ở đâu: hết hạn (mua nhiều quá), rơi vỡ (thao tác), pha hỏng (đào tạo).

💡 Đừng gộp hao hụt vào phiếu kiểm kho. Kiểm kho chỉ nói "thiếu 2 kg"; phiếu huỷ nói "thiếu **vì sao**".
