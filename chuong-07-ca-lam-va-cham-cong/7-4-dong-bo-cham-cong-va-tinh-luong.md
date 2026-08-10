---
title: "7.4 Cấu hình, đồng bộ chấm công và tính lương"
description: "Kết nối máy chấm công, kéo dữ liệu và đọc bảng công tính lương."
---

## Bước A — Khai máy chấm công

*Quản lý nhân sự → Máy chấm công → **Thêm thiết bị***

| Trường | Điền gì |
|---|---|
| **Tên thiết bị** | VD "Máy chấm công cửa trước". |
| **Địa chỉ IP** | IP của máy trong mạng nội bộ quán. |
| **Cổng (Port)** | Mặc định 4370, nhưng **nhiều máy đặt khác**. Xem trên máy: *Menu → Comm/Kết nối → Ethernet*. |
| **Mật khẩu kết nối** | Thường để trống. |
| **Thời gian chờ** | Số giây chờ máy trả lời. |
| **Ngưỡng lọc trùng** | Hai lần quẹt cách nhau dưới ngưỡng này coi là một. |

Sau khi lưu, dùng menu ở dòng thiết bị:

- **Kiểm tra kết nối** — thử nói chuyện với máy, báo về model, firmware, số nhân
  viên, số lượt chấm.
- **Đồng bộ giờ máy** — đẩy giờ của máy chủ lên máy chấm công.

## Bước B — Kéo dữ liệu về

*Quản lý nhân sự → Chấm công → **Đồng bộ từ máy chấm công***

![Đồng bộ chấm công](/images/07-dong-bo-cham-cong.png)

1. Chọn *Máy chấm công*, *Từ ngày*, *Đến ngày*.
2. Bấm **Kiểm tra kết nối** trước cho chắc.
3. Bấm **Đồng bộ**.

Hệ thống đọc lượt quẹt, gom theo từng người từng ngày, **ghép cặp vào–ra**, rồi
ghi vào bảng công. Lượt lẻ cuối ngày (quẹt vào mà chưa quẹt ra) để trống giờ ra.

⚠️ **Đồng bộ là ghi đè.** Hộp thoại cảnh báo rõ bằng chữ đỏ: dữ liệu chấm công
trong khoảng ngày đó của những người có lượt trên máy sẽ được **ghi lại từ đầu**
— mọi chỉnh sửa tay của quản lý trong khoảng đó **sẽ mất**. Chọn khoảng ngày hẹp,
đừng kéo cả tháng nếu chỉ cần bù một ngày.

## Bước C — Cảnh báo lệch giờ máy

Mỗi lần kiểm tra kết nối hoặc đồng bộ, hệ thống **đối chiếu đồng hồ máy chấm công
với đồng hồ máy chủ**. Lệch từ **1 phút** trở lên sẽ hiện cảnh báo màu vàng kèm
nút **Chỉnh giờ ngay**.

⚠️ **Chỉnh giờ chỉ cứu được các lượt chấm SAU đó.** Lượt đã ghi bằng đồng hồ lệch
không sửa ngược được. Giá trị của cảnh báo là phát hiện sớm — thấy cảnh báo thì
chỉnh ngay, đừng để qua tuần.

⚠️ Hệ thống **cố ý không tự chỉnh giờ** khi đồng bộ. Đẩy giờ lên máy là thao tác
ghi đè; chỉnh sai hoặc chỉnh giữa ca sẽ làm nửa ngày lệch nửa ngày đúng, khó gỡ
hơn cả lệch đều.

## Bước D — Đọc bảng công và tính lương

*Quản lý nhân sự → Chấm công*

![Bảng chấm công](/images/07-cham-cong.png)

Lọc theo nhân viên và khoảng ngày ở hàng trên. Nút **Thêm chấm công** dùng để bù
tay cho trường hợp máy chấm công hỏng hoặc nhân viên quên quẹt.

Bảng công có các cột: nhân viên, ngày, **ca**, **giờ vào**, **giờ ra**, thời gian
làm, **lương/giờ**, **thành tiền**.

Ba tình huống nhìn ra ngay bằng cách bày cột:

| Dấu hiệu | Nghĩa |
|---|---|
| Dấu **—** màu hổ phách ở cột Đi hoặc Về | Quên chấm. Dòng nhân viên hiện thêm nhãn "N ngày thiếu giờ". |
| Badge tím **"2 ca"** | Ngày đó người này có hai lượt ca. |
| Badge đỏ ở cột Đi | Đi trễ. Badge hổ phách = đến sớm. |
| Badge xanh ở cột Về | Về muộn (làm thêm). Badge đỏ = về sớm. |

Dung sai mặc định ±10 phút — trong khoảng đó tính là **Đúng giờ**.

💡 Đo trên dữ liệu thật của một quán: khoảng **10% số ngày công chỉ có một lượt
chấm** (quên chấm vào hoặc quên chấm ra). Đây là chuyện thường xuyên, nên quản lý
cần rà cột "thiếu giờ" hằng tuần thay vì đợi cuối tháng.

💡 Nâng *Ngưỡng lọc trùng* **không** giải quyết được chuyện quên chấm — đã đo,
nâng từ 15 lên 120 phút vẫn không đổi tỷ lệ lượt lẻ, còn ngưỡng cao lại nuốt mất
lượt thật.
