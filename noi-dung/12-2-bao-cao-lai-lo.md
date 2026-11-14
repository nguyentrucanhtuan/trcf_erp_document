---
crumb: Bước 12 · Đọc hiểu file P&L và báo cáo
---

# 12.2 Báo cáo lãi lỗ (P&L)

## 1. Đường dẫn vào chức năng

Menu trái: ==Báo cáo → Lãi lỗ== (địa chỉ `/pnl-report`, tiêu đề trang **Báo cáo P&L (Lãi lỗ)**).

- Hoặc trên Trang chủ: thẻ **HÔM NAY**, bấm **Xem lãi lỗ**.
- Trên điện thoại: thanh dưới cùng, bấm **Báo cáo** → **Lãi lỗ**.
- Dành cho: quản lý và chủ quán.

## 2. Ví dụ nền và các bước thực hiện

> **Ví dụ:** chủ quán xem kết quả kinh doanh 6 tháng gần nhất (**Tháng 6/2026** – **Tháng 11/2026**).
>
> - Đây là kỳ mặc định khi mở trang.
> - Trên máy này: **Doanh thu bán** **141.000₫**. Chưa có đơn mua hàng và phiếu chi nào, nên **Lãi gộp** và **Lợi nhuận trước thuế** cũng là **141.000₫** (100.0%).

### Bước 1: Chọn kỳ, đọc 4 ô tổng và bảng Kết quả kinh doanh

- Ở menu trái, nhóm **Báo cáo**, bấm **Lãi lỗ**.
- Bấm ô **Từ tháng**, chọn tháng trong danh sách (VD **Tháng 6/2026**). Làm tương tự với **Đến tháng**.
- Đọc 4 ô: **Doanh thu bán**, **Lãi gộp**, **Chi phí vận hành**, **Lợi nhuận trước thuế**.
- Ô **Lợi nhuận trước thuế** ghi *Kinh doanh có lãi* hoặc *Kinh doanh lỗ*, kèm biên lợi nhuận (%).
- Đọc bảng **Kết quả kinh doanh**: cột **Giá trị** và **% Doanh thu** của từng khoản mục.
- Nhóm dưới đường kẻ (**Đơn chưa thanh toán**, **VAT đầu ra**, **VAT đầu vào**, **Giá trị tồn kho**, **COGS nguyên liệu (tham khảo)**) là chỉ số tham khảo, không tính vào lãi lỗ.

![Bước 1: Chọn kỳ, đọc 4 ô tổng và bảng Kết quả kinh doanh](images/08-pnl-buoc-1-tong-quan.png)

### Bước 2: Đọc biểu đồ

- Cuộn xuống: **Cơ cấu chi phí vận hành** theo từng nhóm chi phí, xem khoản nào ăn nhiều nhất.
- Kỳ chưa có phiếu chi: thẻ báo *Chưa có chi phí vận hành trong kỳ đã chọn.*
- **Xu hướng theo tháng**: cột **Doanh thu**, **Chi phí**, **Lợi nhuận** từng tháng.
- Dưới biểu đồ có số cụ thể từng tháng (VD **Tháng 11/2026**: doanh thu **141.000₫**).

![Bước 2: Đọc biểu đồ](images/08-pnl-buoc-2-bieu-do.png)

## 3. Giải thích các trường

### Bốn ô tổng nối với nhau

```
Doanh thu bán                 (đơn đã thanh toán − hàng hoàn)
  −  Chi phí nhập hàng (ròng) (đơn mua − tiền trả lại NCC)
  =  Lãi gộp
  −  Chi phí vận hành         (tổng phiếu chi theo nhóm)
  =  Lợi nhuận trước thuế
```

> **Ví dụ minh hoạ** (số giả định, không phải số trên ảnh):
>
> - Doanh thu bán 100 triệu − chi phí nhập hàng 40 triệu = lãi gộp 60 triệu (60%).
> - Lãi gộp 60 triệu − chi phí vận hành 35 triệu = lợi nhuận trước thuế 25 triệu (25%).

### Từng ô lấy số từ đâu

| Ô | Nguồn |
| --- | --- |
| Doanh thu bán | Tiền món của đơn bán **đã thanh toán**, **trừ** phiếu trả hàng đã xác nhận (==Vận hành → Trả hàng==) |
| Chi phí nhập hàng (ròng) | Đơn mua **Đã xác nhận**, **Đã nhập kho**, **Đã trả hàng** — **kể cả chưa trả tiền NCC** — tính theo ngày đặt hàng, trừ phiếu trả hàng NCC đã xác nhận (==Vận hành → Trả hàng NCC==). Xem [mục 11.2](11-2-nhap-hang.md) |
| Lãi gộp | Doanh thu bán − chi phí nhập hàng |
| Chi phí vận hành | Mọi phiếu chi **chưa huỷ, chưa lưu trữ** — **kể cả Nháp và Chưa thanh toán** — tính theo **Ngày thanh toán**, gom theo danh mục ([mục 10.2](10-2-tao-chi-phi.md)) |
| Lợi nhuận trước thuế | Lãi gộp − chi phí vận hành, **cộng phí ship** khách trả (nếu có). Bảng chưa có dòng phí ship, nên kỳ có ship thì số này lớn hơn phép trừ trên màn |

### Nhóm chỉ số tham khảo (dưới đường kẻ)

| Dòng | Nghĩa |
| --- | --- |
| Đơn chưa thanh toán | Tổng tiền các đơn trong kỳ chưa thu (khách còn nợ) |
| VAT đầu ra / VAT đầu vào | Thuế trên đơn bán / đơn mua |
| Giá trị tồn kho | Tồn hiện tại × giá vốn sản phẩm |
| COGS nguyên liệu (tham khảo) | Nguyên liệu đã dùng làm món (qua công thức) + nguyên liệu huỷ |

## 4. Lưu ý quan trọng

> [!CAUTION]
> **Chi phí nhập hàng là tiền mua hàng trong kỳ, không phải giá vốn của hàng đã bán.**
>
> - Tháng nhập nhiều để trữ: lãi gộp thấp giả tạo.
> - Tháng sau bán hàng tồn đó: lãi gộp cao giả tạo.
> - Muốn đánh giá đúng: **xem theo quý** hoặc đối chiếu thêm **COGS nguyên liệu** và **Giá trị tồn kho**.

> [!CAUTION]
> **Chỉ khoản chi có phiếu mới vào báo cáo.**
>
> - Trả tiền điện bằng tiền túi mà không lập phiếu chi: lợi nhuận trên báo cáo cao hơn thực tế.

> [!WARNING]
> **Phiếu chi Nháp hoặc Chưa thanh toán vẫn bị trừ vào lợi nhuận.**
>
> - Phiếu lập nhầm: bấm **Huỷ phiếu** hoặc **Lưu trữ**, đừng để Nháp.

> [!WARNING]
> **Chưa trừ lương nhân viên** nếu quán không lập phiếu chi cho lương.
>
> - Muốn P&L đủ: tạo danh mục chi phí **Lương**.
> - Lập phiếu chi hằng tháng.

> [!TIP]
> Nhìn **% Doanh thu** ở cột bên phải bảng thay vì con số tuyệt đối.
>
> - Tỷ lệ chi phí nhập hàng trên doanh thu là chỉ số ổn định để so giữa các tháng.
> - Kể cả khi quy mô thay đổi.

> [!TIP]
> Trục số của biểu đồ **Xu hướng theo tháng** ghi theo triệu (**tr**).
>
> - Tháng doanh thu dưới 1 triệu: trục hiện **0tr**. Đọc số cụ thể ở danh sách dưới biểu đồ.

## Kiểm tra đã đúng

- [ ] Đã chọn đúng kỳ
- [ ] Đã hiểu mỗi ô lấy số từ đâu
- [ ] Đã lập đủ phiếu chi (kể cả lương) và dọn phiếu Nháp lập nhầm trước khi tin vào lợi nhuận
