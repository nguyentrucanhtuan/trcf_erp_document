---
title: "7.4 Cấu hình, đồng bộ chấm công và tính lương"
---

- **Đường dẫn:** Khai máy ở *Quản lý nhân sự → Máy chấm công* · Đồng bộ và xem ở *→ Chấm công*.
- **Cần có trước:** Nhân viên có **ID Chấm công** ([7.1](/chuong-07-ca-lam-va-cham-cong/7-1-tao-nhan-vien-moi)) và ca **đã duyệt** ([7.3](/chuong-07-ca-lam-va-cham-cong/7-3-dang-ky-va-duyet-ca))

## Bước A — Khai máy chấm công

1. Vào *Máy chấm công* → bấm **Thêm thiết bị**.
2. Điền 6 trường theo bảng dưới → Lưu.
3. Ở dòng thiết bị, bấm **Kiểm tra kết nối** để xác nhận nói chuyện được với máy.

| Trường | Điền gì | Bắt buộc |
|---|---|---|
| Tên thiết bị | VD "Máy chấm công cửa trước" | ✅ |
| Địa chỉ IP | IP của máy trong mạng nội bộ quán | ✅ |
| Cổng (Port) | Mặc định 4370, nhưng **nhiều máy đặt khác**. Xem trên máy: *Menu → Comm/Kết nối → Ethernet* | ✅ |
| Mật khẩu kết nối | Thường để trống | — |
| Thời gian chờ | Số giây chờ máy trả lời | — |
| Ngưỡng lọc trùng | Hai lần quẹt cách nhau dưới ngưỡng này coi là một | — |

**Hai nút trong menu thiết bị:**

| Nút | Làm gì |
|---|---|
| Kiểm tra kết nối | Thử nói chuyện với máy → báo model, firmware, số nhân viên, số lượt chấm |
| Đồng bộ giờ máy | Đẩy giờ máy chủ lên máy chấm công |

## Bước B — Kéo dữ liệu về

![Đồng bộ chấm công](/images/07-dong-bo-cham-cong.png)

1. Vào *Chấm công* → bấm **Đồng bộ từ máy chấm công**.
2. Chọn *Máy chấm công*, *Từ ngày*, *Đến ngày* — **chọn khoảng hẹp**.
3. Bấm **Kiểm tra kết nối** trước cho chắc.
4. Đọc cảnh báo đỏ → bấm **Đồng bộ**.

Hệ thống đọc lượt quẹt → gom theo từng người từng ngày → **ghép cặp vào–ra** → ghi vào bảng công. Lượt lẻ cuối ngày (quẹt vào chưa quẹt ra) để trống giờ ra.

⚠️ **Đồng bộ là GHI ĐÈ.** Dữ liệu chấm công trong khoảng ngày đó của những người có lượt trên máy sẽ được ghi lại từ đầu — **mọi chỉnh sửa tay của quản lý trong khoảng đó sẽ mất**. Đừng kéo cả tháng nếu chỉ cần bù một ngày.

## Bước C — Cảnh báo lệch giờ máy

Mỗi lần kiểm tra kết nối hoặc đồng bộ, hệ thống đối chiếu đồng hồ máy chấm công với đồng hồ máy chủ. Lệch từ **1 phút** trở lên → cảnh báo màu vàng kèm nút **Chỉnh giờ ngay**.

- [ ] Thấy cảnh báo → bấm **Chỉnh giờ ngay** luôn, đừng để qua tuần

⚠️ **Chỉnh giờ chỉ cứu được lượt chấm SAU đó.** Lượt đã ghi bằng đồng hồ lệch không sửa ngược được. Giá trị của cảnh báo là **phát hiện sớm**.

⚠️ Hệ thống **cố ý không tự chỉnh giờ** khi đồng bộ. Đẩy giờ lên máy là thao tác ghi đè; chỉnh sai hoặc chỉnh giữa ca làm nửa ngày lệch nửa ngày đúng, khó gỡ hơn cả lệch đều.

## Bước D — Đọc bảng công

![Bảng chấm công](/images/07-cham-cong.png)

1. Lọc theo nhân viên và khoảng ngày ở hàng trên.
2. Máy hỏng hoặc nhân viên quên quẹt → bấm **Thêm chấm công** để bù tay.

**Các cột:** nhân viên · ngày · ca · giờ vào · giờ ra · thời gian làm · lương/giờ · thành tiền.

**Ba dấu hiệu nhìn ra ngay:**

| Dấu hiệu | Nghĩa |
|---|---|
| Dấu **—** màu hổ phách ở cột Đi hoặc Về | Quên chấm. Dòng nhân viên hiện nhãn "N ngày thiếu giờ" |
| Badge tím **"2 ca"** | Ngày đó người này có hai lượt ca |
| Badge đỏ ở cột Đi | Đi trễ (hổ phách = đến sớm) |
| Badge xanh ở cột Về | Về muộn = làm thêm (đỏ = về sớm) |

Dung sai mặc định **±10 phút** — trong khoảng đó tính là *Đúng giờ*.

## Kiểm tra đã đúng

- [ ] Không còn mã nhân viên nào "chưa gán" sau khi đồng bộ
- [ ] Đã rà cột **thiếu giờ** và bù tay những ngày quên chấm
- [ ] Cột thành tiền có số (nếu đã khai Lương giờ)

## Lưu ý

💡 Đo trên dữ liệu thật của một quán: khoảng **10% số ngày công chỉ có một lượt chấm** (quên chấm vào hoặc ra). Đây là chuyện thường xuyên — rà cột "thiếu giờ" **hằng tuần** thay vì đợi cuối tháng.

💡 Nâng *Ngưỡng lọc trùng* **không** giải quyết được chuyện quên chấm — đã đo, nâng từ 15 lên 120 phút vẫn không đổi tỷ lệ lượt lẻ, còn ngưỡng cao lại nuốt mất lượt thật.
