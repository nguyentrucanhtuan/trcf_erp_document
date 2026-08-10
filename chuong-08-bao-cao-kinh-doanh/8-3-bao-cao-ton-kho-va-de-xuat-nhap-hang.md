---
title: "8.3 Báo cáo tồn kho và đề xuất nhập hàng"
---

**Ba màn trong mục này:**

| Màn | Đường dẫn | Dùng để |
|---|---|---|
| Tồn kho hiện tại | *Quản lý kho → Tồn kho* | Khai định mức, xem hàng dưới mức |
| Kiểm soát vận hành | *Báo cáo → Kiểm soát vận hành* | Nhắc việc: tồn âm, cần đặt, cần chế biến |
| Rà soát | Cùng màn trên, phần dưới | Bắt lỗi khai báo sản phẩm |

## A — Tồn kho hiện tại

![Quản lý tồn kho](/images/08-ton-kho.png)

**Các bước khai định mức:**

1. Bấm vào dòng mặt hàng.
2. Điền 2 trường theo bảng dưới.
3. Lưu.

| Trường | Điền gì |
|---|---|
| Định mức tối thiểu | Xuống dưới mức này là phải đặt hàng |
| Định mức tối đa | Mức đầy kho — hệ thống dùng để gợi ý đặt bao nhiêu |

⚠️ **Khai định mức trước** thì báo cáo này mới có tác dụng. Chưa khai thì không có gì để so.

💡 Công thức đặt định mức tối thiểu: `lượng dùng trung bình mỗi ngày × số ngày NCC giao hàng × 1,5`. Hàng giao trong 2 ngày, mỗi ngày dùng 1 kg → tối thiểu **3 kg**.

💡 Mặt hàng dưới định mức được đánh dấu **"Dưới định mức"** và đếm vào ô *Sản phẩm dưới định mức* ở màn Tổng quan.

## B — Kiểm soát vận hành

![Kiểm soát vận hành](/images/08-kiem-soat-van-hanh.png)

Màn **nhắc việc** — hệ thống tự tìm ra những chỗ đang lệch.

| Ô | Nghĩa |
|---|---|
| Việc cần xử lý | Tổng các mục cần chú ý |
| Cần rà soát dữ liệu | Lỗi khai báo sản phẩm: thiếu công thức, sai vai trò, chưa có giá vốn |
| Tồn âm cần bù | Có kho đang âm — cần nhập hoặc chuyển kho gấp |
| Cần chế biến / đặt | Hàng hết hoặc dưới định mức |

Bên dưới là các danh sách chi tiết, trong đó có **đề xuất nhập hàng**: mặt hàng nào dưới định mức và nên nhập bao nhiêu để về mức tối đa.

### Tồn âm nghĩa là gì

Tồn âm là dấu hiệu **thiếu phiếu ở khâu trước**, không phải lỗi hệ thống. Hệ thống cố ý cho phép bán khi tồn về 0 (để không chặn thu ngân giữa giờ cao điểm).

**Ba nguyên nhân thường gặp — kiểm theo thứ tự:**

- [ ] Đã bán nhưng **quên lập phiếu nhập** cho lô hàng vừa về
- [ ] Đã bê hàng ra quầy nhưng **quên phiếu chuyển kho**
- [ ] Công thức khai sai định mức nên trừ nhiều hơn thực tế

**Cách xử lý:** tìm phiếu còn thiếu và lập bù, hoặc chỉnh lại bằng [kiểm kê](/chuong-06-nghiep-vu-kho/6-6-kiem-ke-ton-kho).

## C — Cây sản phẩm và rà soát

Phần **Rà soát** vẽ cây quan hệ *Thành phẩm → Bán thành phẩm → Nguyên liệu* và chỉ ra:

| Lỗi | Hậu quả |
|---|---|
| Món **bán mà không có công thức** | Báo cáo lãi lỗ không tính được giá vốn |
| Nguyên liệu **chưa có giá vốn** | Giá vốn món tính ra bị thiếu |
| Nguyên liệu **mồ côi** | Khai vào hệ thống nhưng không món nào dùng tới |

💡 Rà màn này **một lần mỗi tháng** là đủ. Nó không phải báo cáo xem hằng ngày, mà là bộ lọc bắt lỗi khai báo tích tụ dần.

## Lịch xem báo cáo gợi ý

| Tần suất | Xem gì | Tìm điều gì |
|---|---|---|
| Cuối mỗi ca | Báo cáo ca | Chênh lệch tiền mặt |
| Hằng ngày | Tổng quan | Doanh thu, số đơn, sản phẩm dưới định mức |
| Hằng tuần | Báo cáo bán hàng, Tồn kho | Giá trị TB/đơn, hàng cần đặt |
| Hằng tháng | P&L, Kiểm soát vận hành | Tỷ lệ chi phí, lỗi khai báo |
