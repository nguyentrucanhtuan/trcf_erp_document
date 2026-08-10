---
title: "7.5 Quản lý công việc trong ngày"
description: "Khai mẫu việc lặp, sinh việc luân phiên cho nhân viên đã duyệt ca, theo dõi hoàn thành."
---

**Đường dẫn:** Khai mẫu ở *Quản lý nhân sự → Mẫu công việc* · Sinh và theo dõi ở *→ Công việc*
**Cần có trước:** Nhân viên **đã được duyệt ca** ([7.3](/chuong-07-ca-lam-va-cham-cong/7-3-dang-ky-va-duyet-ca))

## Bước A — Khai mẫu việc lặp

1. Vào *Mẫu công việc* → bấm **Thêm mẫu công việc**.
2. Điền các trường theo bảng dưới → Lưu.

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Tên công việc | VD "Vệ sinh máy pha cà phê" | ✅ |
| Kích hoạt | Tắt = tạm ngừng, không sinh việc nữa | ✅ |
| Mô tả | Hướng dẫn chi tiết cho người làm | — |
| Chu kỳ | *Hàng ngày* / *Thứ trong tuần* / *Hàng tháng* | ✅ |
| Thứ **hoặc** Ngày trong tháng | Chỉ hiện khi chọn chu kỳ tương ứng | ✅ theo chu kỳ |
| Giờ bắt đầu, Giờ kết thúc | Khung giờ nên làm việc này | — |

## Bước B — Sinh việc cho khoảng ngày

1. Vào *Công việc* → bấm **Tạo từ mẫu & ca duyệt**.
2. Chọn khoảng ngày → bấm sinh.

**Hệ thống làm 5 việc:**

1. Duyệt từng ngày trong khoảng
2. Lấy các mẫu **đang kích hoạt** khớp lịch của ngày đó
3. Lấy danh sách nhân viên **đã được duyệt ca** ngày đó
4. **Chia luân phiên** việc cho những người này
5. **Bỏ qua** việc đã tồn tại — bấm lại không tạo trùng

⚠️ Ngày nào không có ai được duyệt ca thì hệ thống **báo lỗi** thay vì sinh việc treo không người làm.

## Bước C — Theo dõi

- Nhân viên đổi trạng thái việc sang **Hoàn thành** → hệ thống tự ghi thời điểm.
- Quản lý lọc theo ngày / nhân viên / trạng thái để xem việc nào còn dở.

## Kiểm tra đã đúng

- [ ] Việc đã sinh đủ cho khoảng ngày, mỗi việc có người nhận
- [ ] Cuối ngày không còn việc ở trạng thái chờ

## Lưu ý

💡 Bỏ *Kích hoạt* ở mẫu là cách tạm ngừng một việc mà không mất lịch sử. Xoá mẫu thì các việc đã sinh vẫn còn.
