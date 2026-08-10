---
title: "Chương 5 — Quy trình bán hàng tại quầy"
description: "Một ca làm việc trọn vẹn: mở ca, bán hàng, làm checklist, xử lý kho phát sinh, đối soát và đóng ca."
---

# Chương 5 — Quy trình bán hàng tại quầy

[← Chương 4](/chuong-04-thiet-lap-pos) · [Về mục lục](/) · [Chương 6 →](/chuong-06-nghiep-vu-kho)

Chương này là **việc hằng ngày của nhân viên đứng quầy**. Đọc theo đúng thứ tự
một ca diễn ra.

---

## 5.1 Hướng dẫn mở phiên và bán hàng

### Bước 1 — Mở ca

Vào *Thiết lập cửa hàng → POS*, bấm **Mở ca** ở quầy mình đứng. Hoặc vào
*Báo cáo → Báo cáo ca* rồi bấm **Mở ca**.

![Mở ca bán hàng](/images/05-mo-ca.png)

1. Chọn **Quầy bán hàng**.
2. Ô **Thu ngân** đã điền sẵn tên bạn — **không đổi được**, hệ thống lấy theo tài
   khoản đang đăng nhập.
3. Đếm tiền mặt thật trong két và nhập vào **Tiền mặt đầu ca**.
4. Bấm **BẮT ĐẦU CA**.

> **Vì sao không chọn được thu ngân khác:** ca bán hàng là chứng từ đối soát két.
> Người mở ca là người chịu trách nhiệm phần tiền trong ca đó. Nếu ai cũng mở ca
> đứng tên người khác được thì lúc thiếu tiền không truy được về ai. Mỗi người
> một tài khoản, ai bán thì người đó mở ca của mình.

⚠️ **Đếm tiền đầu ca cho đúng.** Con số này là mốc để cuối ca tính ra "đáng lẽ
trong két phải có bao nhiêu". Nhập đại thì cuối ca chênh lệch mà không biết lỗi ở
đâu.

⚠️ Một quầy chỉ có **một ca đang mở** tại một thời điểm. Người thứ hai bấm Mở ca
cùng quầy sẽ bị báo lỗi — đó là chặn có chủ đích, không phải trục trặc.

### Bước 2 — Màn bán hàng

Sau khi mở ca, hệ thống vào màn bán hàng.

![Màn bán hàng — chọn bàn](/images/05-man-ban-hang.png)

Thanh trên cùng có bốn mục:

| Mục | Dùng để |
|---|---|
| **BÀN** | Sơ đồ bàn. Bấm bàn để gắn đơn vào bàn đó. |
| **MENU** | Danh sách món để bấm chọn. |
| **ĐƠN HÀNG** | Các đơn đã lưu, đang chờ xử lý. |
| **VẬN HÀNH** | Các nghiệp vụ kho phát sinh trong ca — xem [mục 5.3](#53-tổng-quan-quy-trình-quản-lý-kho). |

### Bước 3 — Lên đơn

![Màn bán hàng — chọn món](/images/05-man-ban-hang-menu.png)

1. Bấm **MENU**, chọn nhóm món ở hàng nút phía trên (Tất cả / Cà phê / …) hoặc gõ
   vào ô **Tìm món**.
2. Bấm vào món để thêm vào giỏ bên phải.
3. Nếu món có size hoặc topping, hệ thống hiện ô chọn:
   - **Chip màu xanh** = biến thể (size) — **có ảnh hưởng giá**.
   - **Chip màu xám** = ghi chú pha chế (ít đá, ít đường) — **không đổi giá**,
     chỉ ghép vào tên món trên bill và màn bếp.
   - Ghi chú pha chế **mặc định không chọn gì**. Bấm lần nữa để bỏ chọn.
4. Muốn ghi thêm yêu cầu riêng của khách thì bấm **Ghi chú**.
5. Có mã khuyến mãi thì bấm **Mã giảm giá**.
6. Khách quen: gõ số điện thoại vào ô **Tìm khách hàng** để tích điểm.

### Bước 4 — Thanh toán

- **Lưu đơn** — giữ đơn lại, chưa thu tiền (khách còn ngồi, gọi thêm sau).
- **THANH TOÁN** — chọn phương thức, xác nhận thu tiền.

Ngay khi đơn được thanh toán, hệ thống đồng thời:

1. Trừ nguyên liệu trong kho theo công thức.
2. Ghi tiền vào sổ quỹ theo phương thức đã chọn.
3. Cộng điểm cho khách (nếu có gắn khách).
4. Đẩy món sang màn hình bếp.

Tất cả xảy ra trong **cùng một lần** — không có chuyện tiền vào mà kho chưa trừ.

### Lưu ý nghiệp vụ

⚠️ **Đơn đã thanh toán thì không sửa được món, mã giảm giá hay điểm.** Hệ thống
chặn và báo lỗi. Lý do: tiền đã ghi vào sổ quỹ, sổ quỹ không sửa được — thêm một
ly sau khi đã thu tiền sẽ làm số trong sổ khác số thực thu. Khách gọi thêm thì
**lên đơn mới**.

⚠️ **Đổi phương thức thanh toán sau khi đã thu tiền cũng bị chặn**, vì đối soát
cuối ca dựa vào phương thức đã ghi.

⚠️ Khách trả lại hàng thì dùng **Hoàn đơn** (*Vận hành → Hoàn đơn*), đừng sửa
đơn cũ. Hoàn đơn trả lại hàng vào kho, trả tiền trên sổ quỹ, và nếu hoàn hết thì
trả lại cả điểm và lượt dùng voucher.

---

## 5.2 Thực hiện checklist trong ca làm việc

*Quản lý nhân sự → Công việc*

Checklist là danh sách việc lặp lại mỗi ca: vệ sinh máy pha, lau tủ lạnh, kiểm
tra hạn sử dụng, đổ rác.

![Màn công việc](/images/05-checklist-cong-viec.png)

### Làm từng bước (nhân viên)

1. Đầu ca, mở *Quản lý nhân sự → Công việc*, lọc theo tên mình.
2. Làm xong việc nào thì đổi trạng thái việc đó sang **Hoàn thành**. Hệ thống tự
   ghi lại **thời điểm hoàn thành**.

### Làm từng bước (quản lý)

1. Khai mẫu việc lặp ở *Quản lý nhân sự → Mẫu công việc*
   (xem [mục 7.5](/chuong-07-ca-lam-va-cham-cong#75-quản-lý-công-việc-trong-ngày)).
2. Ở màn Công việc, bấm **Tạo từ mẫu & ca duyệt** — hệ thống sinh việc cho từng
   ngày, **chia luân phiên** cho những nhân viên đã được duyệt ca ngày hôm đó.
3. Cuối ngày mở lại màn này để xem việc nào chưa xong và ai chưa làm.

### Lưu ý nghiệp vụ

⚠️ Nút sinh việc hàng loạt **chỉ chia cho nhân viên đã được duyệt ca** ngày đó.
Chưa duyệt ca cho ai thì hệ thống báo lỗi thay vì sinh việc treo không người
làm. Duyệt ca trước — xem [mục 7.3](/chuong-07-ca-lam-va-cham-cong#73-đăng-ký-và-duyệt-ca-cho-nhân-viên).

💡 Bấm sinh lần hai cho cùng khoảng ngày sẽ **bỏ qua việc đã có**, không tạo
trùng. Cứ bấm lại yên tâm.

---

## 5.3 Tổng quan quy trình quản lý kho

Trong ca, ngoài bán hàng còn phát sinh việc đụng tới kho. Tất cả gom vào một chỗ:
bấm **VẬN HÀNH** trên màn bán hàng.

![Màn vận hành](/images/05-van-hanh-hub.png)

| Ô | Khi nào dùng | Kho bị ảnh hưởng ra sao |
|---|---|---|
| **Nhập hàng** | Nhà cung cấp giao hàng tới quán. | Cộng vào kho |
| **Chuyển kho** | Lấy hàng từ kho tổng ra quầy. | Trừ kho nguồn, cộng kho đích |
| **Chế biến** | Ủ cà phê cốt, nấu syrup. | Trừ nguyên liệu, cộng bán thành phẩm |
| **Huỷ** | Hàng hỏng, hết hạn, làm rơi. | Trừ kho |
| **Kiểm tồn** | Đếm thực tế, chỉnh cho khớp. | Điều chỉnh về đúng số đếm |
| **Chi phí** | Trả tiền điện, tiền ship, mua đồ lặt vặt. | Không đụng kho, ghi sổ quỹ |
| **Cần nhập hàng** | Xem nhanh hàng nào sắp hết. | Chỉ xem |

**Nguyên tắc chung, đúng cho mọi phiếu kho:**

1. Phiếu mới tạo ở trạng thái **Nháp** — **chưa đụng gì tới kho**. Tạo nhầm thì
   xoá thoải mái.
2. Kho chỉ thay đổi khi bấm **Xác nhận** (hoặc *Nhận hàng*, *Hoàn thành* tuỳ
   loại phiếu).
3. Phiếu đã xác nhận **không sửa, không xoá được**. Sai thì lập phiếu ngược lại
   (nhập nhầm → lập phiếu trả hàng; xuất nhầm → lập phiếu nhập bù).

Chi tiết từng loại phiếu ở [chương 6](/chuong-06-nghiep-vu-kho).

---

## 5.4 Kiểm kê doanh thu và đóng phiên

Cuối ca, vào *Báo cáo → Báo cáo ca*, bấm **Đóng ca** ở dòng ca đang mở.

![Danh sách ca bán hàng](/images/05-ca-ban-hang-danh-sach.png)

Màn này cũng là nơi quản lý xem lại lịch sử ca: bốn ô trên cùng là tổng doanh thu
ca, số ca, số ca đang mở và **tổng chênh lệch tiền mặt** — con số cuối cùng là
thứ nên liếc mỗi tuần.

![Đối soát khi đóng ca](/images/05-dong-ca-doi-soat.png)

### Làm từng bước

1. **Xem ba ô trên cùng**: số đơn, số sản phẩm, doanh thu của ca.
2. **Đối soát phương thức không tiền mặt**: với mỗi phương thức (chuyển khoản,
   thẻ), cột *Hệ thống* là số hệ thống ghi nhận. Đối chiếu với sao kê/máy POS
   ngân hàng rồi nhập số thực tế vào cột *Thực tế*. Cột *Chênh lệch* tự tính.
3. **Đối soát tiền mặt trong két**: hệ thống hiện phép tính
   `tiền đầu ca + doanh thu tiền mặt − chi tiêu tiền mặt − nhập hàng tiền mặt`
   = số dự kiến phải có trong két.
4. **Đếm tiền thật trong két** và nhập vào. Chênh lệch hiện ngay bằng chữ màu
   vàng.
5. Bấm **XÁC NHẬN ĐÓNG CA**.

### Chênh lệch thì làm gì

Chênh lệch **không chặn** việc đóng ca — vẫn đóng được, và con số chênh được ghi
lại vào báo cáo ca để quản lý xem sau. Nhưng trước khi đóng, nên kiểm nhanh:

- Có đơn nào thu tiền mặt mà bấm nhầm sang chuyển khoản không?
- Có khoản chi nào lấy từ két mà quên lập phiếu chi không? (Lập ở
  *Vận hành → Chi phí*.)
- Có ai lấy tiền lẻ đổi mà chưa bỏ lại không?

### Lưu ý nghiệp vụ

⚠️ **Đóng ca là ghi toàn bộ tiền đếm được vào sổ quỹ.** Nghĩa là sau khi đóng ca,
số dư tiền mặt trên sổ về đúng bằng số của ca đang mở kế tiếp — tiền không bị
cộng dồn ảo qua từng ngày. Nếu bạn để lại tiền lẻ trong két cho ca sau, hãy nhập
đúng số tiền đó làm *Tiền mặt đầu ca* của ca mới.

⚠️ **Ca đã đóng không mở lại được**, và không có nút xoá ca. Ca là chứng từ đối
soát. Đóng nhầm thì mở ca mới.

💡 Xem lại ca cũ bất kỳ lúc nào bằng nút **Chi tiết** ở màn Báo cáo ca.

---

## 5.5 Cấu hình và xuất hoá đơn VAT

Áp dụng cho quán có hợp đồng hoá đơn điện tử với **Minvoice**.

### Bước 1 — Khai cấu hình (làm một lần)

Vào *Thiết lập cửa hàng → Cấu hình hệ thống*, nhóm **Hoá đơn điện tử (Minvoice)**:

| Trường | Lấy ở đâu |
|---|---|
| Tên đăng nhập, Mật khẩu | Nhà cung cấp hoá đơn điện tử cấp |
| Tên cửa hàng/Công ty | Tên pháp nhân trên giấy phép |
| Mã số thuế doanh nghiệp | MST của quán |
| API Token | Nhà cung cấp cấp |
| Ký hiệu hoá đơn | VD `C25TAA` |

Bấm **Lưu cấu hình**.

### Bước 2 — Xuất hoá đơn cho đơn hàng

*Vận hành → Hoá đơn VAT → **Tạo hoá đơn***

![Tạo hoá đơn GTGT](/images/05-hoa-don-vat.png)

1. Chọn **Đơn hàng** cần xuất hoá đơn.
2. Chọn **Loại người mua**:
   - *Không lấy hoá đơn* — khách không yêu cầu.
   - *Cá nhân* — điền tên, email, địa chỉ.
   - *Doanh nghiệp* — điền thêm **Mã số thuế**.
3. Bấm **Tạo hoá đơn**. Hoá đơn ở trạng thái **Nháp**.
4. Kiểm tra lại thông tin người mua, rồi bấm **Phát hành** để gửi lên cơ quan
   thuế qua Minvoice.

### Lưu ý nghiệp vụ

⚠️ **Xuất hoá đơn không đụng tới tiền.** Tiền đã được ghi vào sổ quỹ từ lúc khách
thanh toán. Hoá đơn GTGT chỉ là chứng từ thuế.

⚠️ **Hoá đơn đã phát hành thì không sửa, không xoá, không huỷ được** trong hệ
thống — vì nó đã lên cơ quan thuế. Kiểm tra kỹ MST và tên công ty **trước khi**
bấm Phát hành.

⚠️ Chưa khai đủ cấu hình Minvoice mà bấm Phát hành thì hệ thống báo *"Thiếu cấu
hình Minvoice"* và **giữ nguyên hoá đơn ở trạng thái Nháp** — không có chuyện
phát hành nửa vời.

💡 Đơn nào cũng chỉ có **một** hoá đơn. Bấm tạo lần hai cho cùng đơn sẽ mở lại
bản nháp đang có chứ không tạo bản thứ hai.

---

## 5.6 Vận hành ca hoàn hảo — mô hình 3S

Ba việc **S**ạch – **S**ẵn sàng – **S**ổ khớp, làm đủ thì ca sau không phải dọn
hậu quả của ca trước.

### S1 — Sạch (đầu ca, 10 phút)

- [ ] Mở ca **bằng tài khoản của chính mình**, đếm tiền két và nhập đúng số.
- [ ] Mở màn hình bếp ở khu pha chế, để nguyên cả ca.
- [ ] Xem checklist của mình ở *Quản lý nhân sự → Công việc*.
- [ ] Liếc ô **Sản phẩm dưới định mức** ở Tổng quan — có số thì báo quản lý.

### S2 — Sẵn sàng (trong ca)

- [ ] Bán hàng lên đơn ngay, không ghi giấy rồi nhập gộp cuối ca.
- [ ] Hàng lấy từ kho tổng ra quầy → lập **phiếu chuyển kho**, đừng bê suông.
- [ ] Hàng đổ, hỏng, làm rơi → lập **phiếu huỷ** ngay lúc xảy ra.
- [ ] Chi tiền lấy từ két (ship, mua đá) → lập **phiếu chi** ngay.
- [ ] Làm xong việc trong checklist thì đánh dấu hoàn thành luôn.

### S3 — Sổ khớp (cuối ca, 15 phút)

- [ ] Đếm tiền két, đối soát từng phương thức.
- [ ] Chênh lệch thì tìm nguyên nhân **trước khi** đóng ca (xem mục 5.4).
- [ ] Đóng ca, ghi lại số tiền để lại cho ca sau.
- [ ] Bàn giao miệng cho ca sau: hàng sắp hết, việc còn dở, khách hẹn quay lại.

### Vì sao ghi ngay quan trọng hơn ghi đủ

Ba khoản hay bị bỏ sót nhất — **huỷ hàng, chi tiền lẻ, chuyển kho** — đều là
những việc "để lát ghi". Để lát thì cuối ca không ai nhớ chính xác, và hệ quả
xuất hiện ở chỗ khác:

- Quên phiếu huỷ → tồn kho trên hệ thống cao hơn thực tế → tới lúc kiểm kho thấy
  thiếu mà không biết thiếu từ đâu.
- Quên phiếu chi → két thiếu tiền → chênh lệch cuối ca không giải thích được.
- Quên chuyển kho → kho tổng trên hệ thống vẫn đầy trong khi kệ đã trống.

Ghi ngay tốn 30 giây. Truy ngược một chênh lệch tốn cả buổi.

---

[← Chương 4](/chuong-04-thiet-lap-pos) · [Về mục lục](/) · [Chương 6 — Chi tiết các nghiệp vụ kho →](/chuong-06-nghiep-vu-kho)
