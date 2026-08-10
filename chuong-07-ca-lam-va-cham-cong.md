---
title: "Chương 7 — Quản lý ca làm và chấm công"
description: "Hồ sơ nhân viên, ca làm việc, đăng ký và duyệt ca, đồng bộ máy chấm công, checklist công việc."
---

# Chương 7 — Quản lý ca làm và chấm công

[← Chương 6](/chuong-06-nghiep-vu-kho) · [Về mục lục](/) · [Chương 8 →](/chuong-08-bao-cao-kinh-doanh)

Thứ tự làm: **nhân viên → ca làm việc → đăng ký & duyệt ca → chấm công →
công việc**. Bỏ qua bước duyệt ca thì bước sinh việc và phân tích trễ/sớm không
chạy được.

---

## 7.1 Tạo nhân viên mới

*Quản lý nhân sự → Nhân viên → **Thêm nhân viên***

![Thêm nhân viên](/images/07-nhan-vien-them.png)

Form chia ba nhóm trên cùng một màn.

### Làm từng bước

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

### Hai điểm quyết định về sau

⚠️ **Ô "Tài khoản đăng nhập" quyết định nhân viên có mở ca được hay không.**
Chưa gắn tài khoản thì người đó đăng nhập vào sẽ **không mở được ca** và nhận
thông báo "chưa gắn hồ sơ nhân viên". Đây là hệ quả của nguyên tắc *ai bán thì
người đó mở ca của mình* (xem [mục 5.1](/chuong-05-ban-hang-tai-quay#51-hướng-dẫn-mở-phiên-và-bán-hàng)).

⚠️ **Ô "ID chấm công" phải khớp mã trên máy.** Sai hoặc bỏ trống thì khi đồng bộ,
lượt quẹt thẻ của người đó không ghép được vào ai — hệ thống liệt kê những mã
chưa gán để bạn bổ sung.

### Lưu ý về lương

⚠️ **Lương, CCCD và số tài khoản chỉ hiện với người có quyền sửa nhân viên.**
Người chỉ có quyền xem (VD thu ngân xem bảng công) sẽ **không thấy** các cột
lương. Đây là chặn có chủ đích — đừng cấp quyền sửa nhân viên chỉ để ai đó xem
được tên.

💡 Nhân viên nghỉ việc thì **xoá được** — hệ thống dọn các bản ghi vận hành
(chấm công, đăng ký ca, phân công việc) nhưng **giữ nguyên** chứng từ tiền (đơn
hàng, phiếu mua, sổ quỹ, ca bán hàng), chỉ bỏ liên kết tên. Lịch sử tiền không
bao giờ mất.

---

## 7.2 Tạo ca làm việc

*Quản lý nhân sự → Ca làm việc → **Thêm ca làm việc***

![Thêm ca làm việc](/images/07-ca-lam-viec.png)

### Làm từng bước

1. Bấm **Thêm ca làm việc**.
2. Điền *Tên ca* (VD "Ca sáng"), *Giờ bắt đầu*, *Giờ kết thúc*, *Màu sắc*,
   *Ghi chú*.
3. Bấm **Lưu**.

### Ca qua đêm

Ca kết thúc **sớm hơn** giờ bắt đầu là hợp lệ: ca 22:00 → 06:00 được chấp nhận,
hệ thống hiểu là ca qua đêm. Phân tích trễ/sớm cũng tính đúng cho trường hợp
này.

💡 Đặt tên ca theo cách nhân viên gọi hằng ngày ("Ca sáng", "Ca chiều", "Ca gãy")
thay vì "Ca 1", "Ca 2" — lịch tuần dễ đọc hơn nhiều.

---

## 7.3 Đăng ký và duyệt ca cho nhân viên

*Quản lý nhân sự → Đăng ký ca*

![Đăng ký ca làm việc](/images/07-dang-ky-ca.png)

Màn này có hai cách xem: **Lịch theo tuần** (nhìn tổng thể ai làm ca nào) và
**Danh sách** (thao tác duyệt nhanh).

### Làm từng bước

1. Bấm **Đăng ký ca**.
2. Chọn *Nhân viên*, *Ca làm việc*, *Ngày*.
3. Lưu — bản ghi ở trạng thái **Chờ duyệt**.
4. Quản lý mở lại, bấm **Duyệt** hoặc **Từ chối**.

Ba trạng thái: **Chờ duyệt → Đã duyệt / Từ chối**.

### Vì sao phải duyệt

Trạng thái *Đã duyệt* là đầu vào của hai việc khác:

- **Sinh checklist công việc** ([mục 7.5](#75-quản-lý-công-việc-trong-ngày)) chỉ
  chia việc cho người đã được duyệt ca hôm đó.
- **Phân tích trễ/sớm** ([mục 7.4](#74-cấu-hình-đồng-bộ-chấm-công-và-tính-lương))
  so giờ quẹt thẻ với giờ của ca **đã duyệt**. Chưa duyệt thì cột trễ/sớm để
  trống.

### Lưu ý nghiệp vụ

⚠️ Bấm duyệt hai lần cho cùng bản ghi sẽ bị chặn — trạng thái chỉ đi một chiều
từ *Chờ duyệt*.

💡 Đăng ký trùng (cùng người, cùng ca, cùng ngày) **được phép** — để nhân viên bị
từ chối rồi đăng ký lại.

---

## 7.4 Cấu hình, đồng bộ chấm công và tính lương

### Bước A — Khai máy chấm công

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

### Bước B — Kéo dữ liệu về

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

### Bước C — Cảnh báo lệch giờ máy

Mỗi lần kiểm tra kết nối hoặc đồng bộ, hệ thống **đối chiếu đồng hồ máy chấm công
với đồng hồ máy chủ**. Lệch từ **1 phút** trở lên sẽ hiện cảnh báo màu vàng kèm
nút **Chỉnh giờ ngay**.

⚠️ **Chỉnh giờ chỉ cứu được các lượt chấm SAU đó.** Lượt đã ghi bằng đồng hồ lệch
không sửa ngược được. Giá trị của cảnh báo là phát hiện sớm — thấy cảnh báo thì
chỉnh ngay, đừng để qua tuần.

⚠️ Hệ thống **cố ý không tự chỉnh giờ** khi đồng bộ. Đẩy giờ lên máy là thao tác
ghi đè; chỉnh sai hoặc chỉnh giữa ca sẽ làm nửa ngày lệch nửa ngày đúng, khó gỡ
hơn cả lệch đều.

### Bước D — Đọc bảng công và tính lương

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

---

## 7.5 Quản lý công việc trong ngày

### Bước A — Khai mẫu việc lặp

*Quản lý nhân sự → Mẫu công việc → **Thêm mẫu công việc***

| Trường | Điền gì |
|---|---|
| **Tên công việc** | VD "Vệ sinh máy pha cà phê". |
| **Kích hoạt** | Tắt = tạm ngừng, không sinh việc nữa. |
| **Mô tả** | Hướng dẫn chi tiết cho người làm. |
| **Chu kỳ** | *Hàng ngày* / *Thứ trong tuần* / *Hàng tháng*. |
| **Thứ** hoặc **Ngày trong tháng** | Chỉ hiện khi chọn chu kỳ tương ứng. |
| **Giờ bắt đầu**, **Giờ kết thúc** | Khung giờ nên làm việc này. |

### Bước B — Sinh việc cho khoảng ngày

*Quản lý nhân sự → Công việc → **Tạo từ mẫu & ca duyệt***

Chọn khoảng ngày rồi bấm sinh. Hệ thống:

1. Duyệt từng ngày trong khoảng.
2. Lấy các mẫu **đang kích hoạt** khớp lịch của ngày đó.
3. Lấy danh sách nhân viên **đã được duyệt ca** ngày đó.
4. **Chia luân phiên** việc cho những người này.
5. **Bỏ qua** việc đã tồn tại — bấm lại không tạo trùng.

⚠️ Ngày nào không có ai được duyệt ca thì hệ thống **báo lỗi** thay vì sinh việc
treo không người làm. Duyệt ca trước (mục 7.3).

### Bước C — Theo dõi

Nhân viên đổi trạng thái việc sang **Hoàn thành**; hệ thống tự ghi thời điểm.
Quản lý lọc theo ngày/nhân viên/trạng thái để xem việc nào còn dở.

💡 Bỏ *Kích hoạt* ở mẫu là cách tạm ngừng một việc mà không mất lịch sử. Xoá mẫu
thì các việc đã sinh vẫn còn.

---

[← Chương 6](/chuong-06-nghiep-vu-kho) · [Về mục lục](/) · [Chương 8 — Báo cáo kinh doanh →](/chuong-08-bao-cao-kinh-doanh)
