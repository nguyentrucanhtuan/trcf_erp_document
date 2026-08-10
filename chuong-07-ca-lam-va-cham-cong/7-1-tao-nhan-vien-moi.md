---
title: "7.1 Tạo nhân viên mới"
description: "Khai hồ sơ, gắn tài khoản đăng nhập và mã máy chấm công — hai ô quyết định về sau."
---

**Đường dẫn:** *Quản lý nhân sự → Nhân viên → Thêm nhân viên*
**Cần có trước:** Phòng ban (*Quản lý nhân sự → Phòng ban*)
**Thứ tự cả chương 7:** nhân viên → ca làm việc → đăng ký & duyệt ca → chấm công → công việc

![Thêm nhân viên](/images/07-nhan-vien-them.png)

## Các bước

1. Bấm **Thêm nhân viên**.
2. Điền 3 nhóm trên cùng một màn (bảng dưới).
3. Bấm **Lưu nhân viên**.

## Giải thích các trường

**Hồ sơ cá nhân**

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Họ và tên | Tên đầy đủ | ✅ |
| Email, Số điện thoại, CMND/CCCD, Địa chỉ | Thông tin liên hệ | — |

**Công việc**

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Chức vụ | Chọn từ danh sách | — |
| Phòng ban | Khai trước ở *Phòng ban* | ✅ |
| **Tài khoản đăng nhập** | Gắn hồ sơ với một tài khoản hệ thống. **Không gắn thì không mở ca được** | ✅ nếu người này đứng quầy |

**Lương & Chấm công**

| Trường | Điền gì |
|---|---|
| Thông tin ngân hàng | Số tài khoản, ngân hàng, chi nhánh |
| Lương tháng | Lương cố định |
| Lương giờ | Dùng để tính tiền công theo bảng chấm công |
| **ID Chấm công (ZKTeco)** | Mã nhân viên **trên máy chấm công**. Phải khớp |

## Kiểm tra đã đúng

- [ ] Người đứng quầy đã gắn **Tài khoản đăng nhập**
- [ ] Người chấm công bằng máy đã có **ID Chấm công** khớp mã trên máy
- [ ] Có **Lương giờ** nếu muốn bảng công tính ra tiền

## Lưu ý

⚠️ **Chưa gắn tài khoản đăng nhập thì người đó không mở được ca**, sẽ nhận thông báo "chưa gắn hồ sơ nhân viên" — hệ quả của nguyên tắc *ai bán thì người đó mở ca của mình* ([mục 5.1](/chuong-05-ban-hang-tai-quay/5-1-mo-phien-va-ban-hang)).

⚠️ **ID chấm công sai hoặc bỏ trống** thì khi đồng bộ, lượt quẹt thẻ của người đó không ghép được vào ai. Hệ thống liệt kê những mã chưa gán để bạn bổ sung.

⚠️ **Lương, CCCD và số tài khoản chỉ hiện với người có quyền sửa nhân viên.** Người chỉ có quyền xem (VD thu ngân xem bảng công) **không thấy** các cột lương. Đừng cấp quyền sửa nhân viên chỉ để ai đó xem được tên.

💡 Nhân viên nghỉ việc thì **xoá được**: hệ thống dọn bản ghi vận hành (chấm công, đăng ký ca, phân công việc) nhưng **giữ nguyên** chứng từ tiền (đơn hàng, phiếu mua, sổ quỹ, ca bán hàng), chỉ bỏ liên kết tên. Lịch sử tiền không bao giờ mất.
