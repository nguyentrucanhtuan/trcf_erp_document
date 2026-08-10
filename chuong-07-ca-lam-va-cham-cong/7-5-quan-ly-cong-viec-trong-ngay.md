---
title: "7.5 Quản lý công việc trong ngày"
description: "Tạo mẫu công việc và phân công cho nhân viên theo ca."
---

## Bước A — Khai mẫu việc lặp

*Quản lý nhân sự → Mẫu công việc → **Thêm mẫu công việc***

| Trường | Điền gì |
|---|---|
| **Tên công việc** | VD "Vệ sinh máy pha cà phê". |
| **Kích hoạt** | Tắt = tạm ngừng, không sinh việc nữa. |
| **Mô tả** | Hướng dẫn chi tiết cho người làm. |
| **Chu kỳ** | *Hàng ngày* / *Thứ trong tuần* / *Hàng tháng*. |
| **Thứ** hoặc **Ngày trong tháng** | Chỉ hiện khi chọn chu kỳ tương ứng. |
| **Giờ bắt đầu**, **Giờ kết thúc** | Khung giờ nên làm việc này. |

## Bước B — Sinh việc cho khoảng ngày

*Quản lý nhân sự → Công việc → **Tạo từ mẫu & ca duyệt***

Chọn khoảng ngày rồi bấm sinh. Hệ thống:

1. Duyệt từng ngày trong khoảng.
2. Lấy các mẫu **đang kích hoạt** khớp lịch của ngày đó.
3. Lấy danh sách nhân viên **đã được duyệt ca** ngày đó.
4. **Chia luân phiên** việc cho những người này.
5. **Bỏ qua** việc đã tồn tại — bấm lại không tạo trùng.

⚠️ Ngày nào không có ai được duyệt ca thì hệ thống **báo lỗi** thay vì sinh việc
treo không người làm. Duyệt ca trước (mục 7.3).

## Bước C — Theo dõi

Nhân viên đổi trạng thái việc sang **Hoàn thành**; hệ thống tự ghi thời điểm.
Quản lý lọc theo ngày/nhân viên/trạng thái để xem việc nào còn dở.

💡 Bỏ *Kích hoạt* ở mẫu là cách tạm ngừng một việc mà không mất lịch sử. Xoá mẫu
thì các việc đã sinh vẫn còn.
