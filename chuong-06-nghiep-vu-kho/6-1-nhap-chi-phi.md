---
title: "6.1 Nhập chi phí"
description: "Lập phiếu chi cho các khoản chi tiêu của quán."
---

Mọi phiếu trong chương này đều theo **cùng một luật**:

> **Nháp thì chưa đụng gì. Xác nhận rồi thì không sửa được.**
>
> Phiếu mới tạo là *Nháp* — kho và tiền chưa thay đổi, xoá thoải mái. Bấm xác
> nhận là hệ thống ghi vào kho/sổ quỹ **ngay lập tức và không thể quay lui**.
> Sai thì lập phiếu ngược lại chứ không sửa phiếu cũ.

Vào các phiếu này bằng hai đường: từ menu bên trái, hoặc nhanh hơn là nút
**VẬN HÀNH** trên màn bán hàng.

*Chi phí → Chi phí* · hoặc *Vận hành → Chi phí*

Dùng cho mọi khoản chi **không phải mua hàng hoá**: tiền điện, tiền nước, tiền
ship, thuê mặt bằng, mua chổi lau nhà.

![Thêm chi phí](/images/06-chi-phi.png)

## Làm từng bước

1. Bấm **Thêm chi phí**.
2. Nhóm **Nội dung chi**:
   - *Tên chi phí* — mô tả ngắn: "Tiền điện tháng 8".
   - *Danh mục chi phí* — chọn nhóm để báo cáo lãi lỗ gom đúng chỗ.
   - *Số tiền* và *Ngày thanh toán*.
3. Nhóm **Thanh toán & trạng thái**:
   - *Phương thức thanh toán* — tiền mặt hay chuyển khoản.
   - *Quầy phát sinh* — chọn quầy nếu chi từ két của quầy; để *Ngoài ca* nếu chi
     từ tài khoản công ty.
   - *Trạng thái phiếu*: **Nháp** hay **Hoàn tất**.
   - *Trạng thái thanh toán*: **Chưa thanh toán** hay **Đã thanh toán**.
4. Bấm **Thêm chi phí**.

## Khi nào tiền thật sự vào sổ quỹ

Chỉ khi phiếu ở **Hoàn tất** **và** **Đã thanh toán**. Thiếu một trong hai thì
phiếu chỉ là ghi nhớ, chưa động vào quỹ.

## Lưu ý nghiệp vụ

⚠️ **Chi tiền mặt lấy từ két thì bắt buộc chọn đúng quầy.** Không chọn thì khi
đóng ca, số tiền chi đó không được trừ khỏi số dự kiến trong két → cuối ca hiện
thiếu tiền mà không rõ lý do.

⚠️ **Không được gỡ trạng thái "Đã thanh toán" rồi bật lại.** Hệ thống chặn và
báo lỗi, đề nghị lập phiếu chi mới. Lý do: bút toán trong sổ quỹ là bản ghi vĩnh
viễn — gỡ thanh toán sẽ sinh bút toán đảo, và khi bật lại thì tiền **biến mất**
khỏi sổ mà không ai thấy. Trả tiền điện lần nữa thì lập phiếu chi mới cho lần đó.

💡 Khai danh mục chi phí gọn gàng ngay từ đầu (*Chi phí → Danh mục chi phí*) thì
báo cáo lãi lỗ ở chương 8 đọc mới có nghĩa.
