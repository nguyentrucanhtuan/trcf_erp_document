---
crumb: Bước 8 · Cài đặt máy chấm công
---

# 8.2 Cài đặt máy chấm công

## 1. Đường dẫn vào chức năng

Menu trái: ==Quản lý nhân sự → Máy chấm công== (địa chỉ `/attendance-devices`).

- Cần có trước: nhân viên có **ID Chấm công** ([bài 8.1](8-1-tao-nhan-vien.md)).

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** máy ZKTeco ở cửa trước quán.
>
> - Máy: tên **Máy chấm công cửa trước**, IP **192.168.1.201**, cổng **4370**.
> - Nhân viên **Nguyễn Văn An** có ID Chấm công **101**.

### Bước 1: Mở trang Máy chấm công

- Ở menu trái, nhóm **Quản lý nhân sự**, bấm **Máy chấm công**.

![Bước 1: Mở trang Máy chấm công](images/07-cham-cong-buoc-1-may-cham-cong.png)

### Bước 2: Khai kết nối

- Bấm nút tròn **+** ở góc dưới bên phải.
- Xem IP và cổng thật của máy ngay trên máy chấm công: *Menu → Comm/Kết nối → Ethernet*.
- Điền như ảnh, thay IP và cổng bằng số của máy quán. Chưa bấm lưu.

![Bước 2: Khai kết nối](images/07-cham-cong-buoc-2-form-may.png)

### Bước 3: Khai cách đồng bộ

- Kéo xuống phần **Đồng bộ**.
- Giữ như ảnh, bấm **Thêm thiết bị**.

![Bước 3: Khai cách đồng bộ](images/07-cham-cong-buoc-3-dong-bo-may.png)

### Bước 4: Kiểm tra kết nối

- Bấm vào dòng thiết bị trong danh sách.
- Chọn **Kiểm tra kết nối** để xác nhận nói chuyện được với máy.

![Bước 4: Bấm vào thiết bị để mở thao tác](images/07-cham-cong-buoc-4-thao-tac-may.png)

## 3. Giải thích các trường

### Khai máy chấm công

| Trường | Điền gì | Bắt buộc |
| --- | --- | --- |
| Tên thiết bị | VD **Máy chấm công cửa trước** | ✅ |
| Địa chỉ IP | IP của máy trong mạng nội bộ quán | ✅ |
| Cổng (Port) | Mặc định 4370, **nhiều máy đặt khác** | ✅ |
| Mật khẩu kết nối (nếu có) | Thường để trống | — |
| Thời gian chờ (giây) | Số giây chờ máy trả lời | — |
| Ngưỡng lọc trùng (phút) | Hai lần quẹt cách nhau dưới ngưỡng này coi là một | — |
| Kích hoạt | Tắt: hệ thống không kết nối với máy này, cột **Kết nối** hiện **Tắt** | — |

### Hai thao tác riêng của máy chấm công

| Nút | Làm gì |
| --- | --- |
| Kiểm tra kết nối | Thử nói chuyện với máy, báo model, firmware, số nhân viên, số lượt chấm |
| Chỉnh giờ máy | Đẩy giờ máy chủ lên máy chấm công |

### Cảnh báo lệch giờ máy

- Mỗi lần kiểm tra kết nối hoặc đồng bộ, hệ thống đối chiếu đồng hồ máy chấm công với máy chủ.
- Lệch từ **1 phút** trở lên: cảnh báo vàng kèm nút **Chỉnh giờ ngay**.
- Thấy cảnh báo: bấm **Chỉnh giờ ngay** luôn, đừng để qua tuần.

## 4. Lưu ý quan trọng

> - Chỉnh giờ máy chỉ đúng cho lượt chấm **sau** đó, không sửa được lượt cũ.
> - Đừng chỉnh giờ giữa ca.
> - Nâng ngưỡng lọc trùng không chữa được chuyện quên chấm.
