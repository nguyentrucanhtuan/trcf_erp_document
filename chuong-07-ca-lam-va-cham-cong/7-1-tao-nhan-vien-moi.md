---
title: "7.1 Tạo nhân viên mới"
description: "Khai hồ sơ nhân viên, gắn tài khoản đăng nhập và mã máy chấm công."
---

Thứ tự làm: **nhân viên → ca làm việc → đăng ký & duyệt ca → chấm công →
công việc**. Bỏ qua bước duyệt ca thì bước sinh việc và phân tích trễ/sớm không
chạy được.

*Quản lý nhân sự → Nhân viên → **Thêm nhân viên***

![Thêm nhân viên](/images/07-nhan-vien-them.png)

Form chia ba nhóm trên cùng một màn.

## Làm từng bước

**Hồ sơ cá nhân** — Họ và tên, Email, Số điện thoại, CMND/CCCD, Địa chỉ.

**Công việc**

| Trường | Điền gì |
|---|---|
| **Chức vụ** | Chọn từ danh sách. |
| **Phòng ban** | Bắt buộc. Khai trước ở *Quản lý nhân sự → Phòng ban*. |
| **Tài khoản đăng nhập** | Gắn hồ sơ này với một tài khoản của hệ thống. |

**Lương & Chấm công**

| Trường | Điền gì |
|---|---|
| **Thông tin ngân hàng** | Số tài khoản, ngân hàng, chi nhánh. |
| **Lương tháng**, **Lương giờ** | Lương giờ dùng để tính tiền công theo bảng chấm công. |
| **ID Chấm công (ZKTeco)** | Mã nhân viên **trên máy chấm công**. |

Bấm **Lưu nhân viên**.

## Hai điểm quyết định về sau

⚠️ **Ô "Tài khoản đăng nhập" quyết định nhân viên có mở ca được hay không.**
Chưa gắn tài khoản thì người đó đăng nhập vào sẽ **không mở được ca** và nhận
thông báo "chưa gắn hồ sơ nhân viên". Đây là hệ quả của nguyên tắc *ai bán thì
người đó mở ca của mình* (xem [mục 5.1](/chuong-05-ban-hang-tai-quay/5-1-mo-phien-va-ban-hang)).

⚠️ **Ô "ID chấm công" phải khớp mã trên máy.** Sai hoặc bỏ trống thì khi đồng bộ,
lượt quẹt thẻ của người đó không ghép được vào ai — hệ thống liệt kê những mã
chưa gán để bạn bổ sung.

## Lưu ý về lương

⚠️ **Lương, CCCD và số tài khoản chỉ hiện với người có quyền sửa nhân viên.**
Người chỉ có quyền xem (VD thu ngân xem bảng công) sẽ **không thấy** các cột
lương. Đây là chặn có chủ đích — đừng cấp quyền sửa nhân viên chỉ để ai đó xem
được tên.

💡 Nhân viên nghỉ việc thì **xoá được** — hệ thống dọn các bản ghi vận hành
(chấm công, đăng ký ca, phân công việc) nhưng **giữ nguyên** chứng từ tiền (đơn
hàng, phiếu mua, sổ quỹ, ca bán hàng), chỉ bỏ liên kết tên. Lịch sử tiền không
bao giờ mất.
