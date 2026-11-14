---
crumb: Bước 10 · Chi phí
---

# 10.2 Tạo chi phí

## 1. Đường dẫn vào chức năng

Menu trái: ==Chi phí → Thu chi== (địa chỉ `/expenses`, tiêu đề trang **Chi phí**).

hoặc ở màn ==Bán hàng → VẬN HÀNH → Chi phí==.

- Dùng cho mọi khoản chi **không phải mua hàng hoá**: tiền điện, nước, ship, thuê mặt bằng, mua chổi lau nhà.
- Cần có trước: danh mục chi phí ([bài 10.1 Danh mục chi phí](10-1-danh-muc-chi-phi.md)).

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** trả tiền điện tháng 10 bằng tiền mặt lấy từ két **Quầy chính**.
>
> - Tên chi phí: **Tiền điện tháng 10**. Danh mục: **Tiền điện**.
> - Số tiền: **1200000**. Phương thức: **Tiền mặt**. Quầy phát sinh: **Quầy chính**.
> - Trạng thái phiếu: **Hoàn tất**. Trạng thái thanh toán: **Đã thanh toán**.

### Bước 1: Mở trang Chi phí

- Ở menu trái, nhóm **Chi phí**, bấm **Thu chi**.
- Quán chưa có phiếu chi nào thì trang báo *Chưa có chi phí nào*.
- Góc trên phải: biểu tượng hình khối mở nhanh **Danh mục chi phí**, biểu tượng tải xuống để **Xuất Excel**.
- Biểu tượng ba gạch cạnh ô tìm kiếm mở **Bộ lọc**: ngày lập, loại chi phí, thanh toán, lưu trữ.

![Bước 1: Mở trang Chi phí](images/06-chi-phi-buoc-1-danh-sach.png)

### Bước 2: Khai nội dung chi

- Bấm nút tròn **+** ở góc dưới bên phải. Hộp thoại **Thêm chi phí** mở ra.
- **Số tiền (₫)** (ô số lớn trên cùng): nhập **1200000**.
- **Tên chi phí**: nhập **Tiền điện tháng 10**.
- **Danh mục chi phí**: bấm vào ô, chọn **Tiền điện**.
- **Ngày thanh toán**: giữ ngày hôm nay (hoặc chọn ngày trả thật).

![Bước 2: Khai nội dung chi](images/06-chi-phi-buoc-2-form.png)

### Bước 3: Khai thanh toán và trạng thái

- Kéo xuống phần **Thanh toán & trạng thái**.
- **Phương thức thanh toán**: bấm vào ô, chọn **CASH · Tiền mặt**.
- **Quầy phát sinh**: bấm vào ô, chọn **Quầy chính** (chi từ két quầy).
- **Trạng thái phiếu**: chọn **Hoàn tất**.
- **Trạng thái thanh toán**: chọn **Đã thanh toán**.
- Bấm **Thêm chi phí**.
- Phiếu hiện trong danh sách: tên, trạng thái phiếu, danh mục, số tiền, thanh toán, quầy, ngày thanh toán.
- Thao tác sau này: bấm vào phiếu. Tuỳ trạng thái sẽ có **Hoàn tất**, **Sửa**, **Lưu trữ**, **Huỷ phiếu**.

![Bước 3: Khai thanh toán và trạng thái](images/06-chi-phi-buoc-3-thanh-toan.png)

## 3. Giải thích các trường

### Nội dung chi

| Trường | Điền gì | Bắt buộc |
| --- | --- | --- |
| Số tiền (₫) | Số tiền chi, nhập ở ô số lớn đầu hộp thoại | ✅ |
| Tên chi phí | Mô tả ngắn: **Tiền điện tháng 10** | ✅ |
| Danh mục chi phí | Nhóm để báo cáo lãi lỗ gom đúng chỗ | ✅ |
| Ngày thanh toán | Ngày trả tiền thật | ✅ |

### Thanh toán & trạng thái

| Trường | Điền gì |
| --- | --- |
| Phương thức thanh toán | Tiền mặt hay chuyển khoản (bắt buộc) |
| Quầy phát sinh | Chọn quầy nếu chi **từ két của quầy**. Để *— Ngoài ca —* nếu chi từ tài khoản công ty |
| Trạng thái phiếu | **Nháp** hay **Hoàn tất** (mặc định Hoàn tất) |
| Trạng thái thanh toán | **Chưa thanh toán** hay **Đã thanh toán** (mặc định Chưa thanh toán) |
| Ghi chú | Ghi thêm (không bắt buộc) |

### Khi nào tiền thật sự vào sổ quỹ

- Chỉ khi phiếu ở **Hoàn tất** **VÀ** **Đã thanh toán**.
- Thiếu một trong hai: phiếu chỉ là ghi nhớ, chưa động vào quỹ.

## 4. Lưu ý quan trọng

> [!CAUTION]
> **Chi tiền mặt lấy từ két thì bắt buộc chọn đúng quầy.**
>
> - Không chọn thì lúc đóng ca, khoản chi không được trừ khỏi số dự kiến trong két.
> - Cuối ca hiện thiếu tiền mà không rõ lý do.

> [!CAUTION]
> **Không được gỡ *Đã thanh toán* rồi bật lại.**
>
> - Hệ thống chặn và đề nghị lập phiếu mới.
> - Bút toán sổ quỹ là bản ghi vĩnh viễn.
> - Gỡ thanh toán sinh bút toán đảo, bật lại thì tiền biến mất khỏi sổ mà không ai thấy.

> [!WARNING]
> **Phiếu chi không xoá được, chỉ *Huỷ phiếu*.**
>
> - Phiếu đã huỷ không sửa lại được.
> - Sai thì tạo phiếu mới.

> [!TIP]
> Khai danh mục chi phí gọn gàng từ đầu thì báo cáo lãi lỗ ([mục 12.2](12-2-bao-cao-lai-lo.md)) mới đọc có nghĩa.

## Kiểm tra đã đúng

- [ ] Chi từ két quầy: đã chọn đúng **Quầy phát sinh**
- [ ] Phiếu ở *Hoàn tất* + *Đã thanh toán* nếu tiền đã trả
- [ ] Số dư sổ quỹ đã giảm đúng số tiền
