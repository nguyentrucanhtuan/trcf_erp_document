---
title: "8.3 Báo cáo tồn kho và đề xuất nhập hàng"
description: "Theo dõi tồn kho, định mức và đề xuất nhập hàng."
---

## A — Tồn kho hiện tại

*Quản lý kho → Tồn kho*

![Quản lý tồn kho](/images/08-ton-kho.png)

Bảng liệt kê từng mặt hàng theo từng kho, kèm **định mức tối thiểu** và **định
mức tối đa**.

**Khai định mức trước khi trông chờ vào báo cáo này.** Bấm vào dòng để sửa:

- **Định mức tối thiểu** — xuống dưới mức này là phải đặt hàng.
- **Định mức tối đa** — mức đầy kho, dùng để hệ thống gợi ý đặt bao nhiêu.

Mặt hàng dưới định mức được đánh dấu **"Dưới định mức"**, và cũng đếm vào ô
*Sản phẩm dưới định mức* ở màn Tổng quan.

💡 Cách đặt định mức tối thiểu đơn giản: *lượng dùng trung bình mỗi ngày × số
ngày nhà cung cấp giao hàng × 1,5*. Hàng giao trong 2 ngày, mỗi ngày dùng 1 kg →
tối thiểu 3 kg.

## B — Kiểm soát vận hành

*Báo cáo → Kiểm soát vận hành*

![Kiểm soát vận hành](/images/08-kiem-soat-van-hanh.png)

Đây là màn **nhắc việc** — hệ thống tự tìm ra những chỗ đang lệch:

| Ô | Nghĩa |
|---|---|
| **Việc cần xử lý** | Tổng các mục cần chú ý. |
| **Cần rà soát dữ liệu** | Lỗi khai báo sản phẩm: thiếu công thức, sai vai trò, chưa có giá vốn. |
| **Tồn âm cần bù** | Có kho đang âm — cần nhập hoặc chuyển kho gấp. |
| **Cần chế biến / đặt** | Hàng hết hoặc dưới định mức, cần sản xuất hoặc đặt thêm. |

Bên dưới là các danh sách chi tiết, trong đó có **đề xuất nhập hàng**: mặt hàng
nào dưới định mức và nên nhập bao nhiêu để về mức tối đa.

## Tồn âm nghĩa là gì

Tồn kho âm là dấu hiệu **thiếu phiếu ở khâu trước**, không phải lỗi hệ thống. Hệ
thống cố ý cho phép bán khi tồn đã về 0 (để không chặn thu ngân giữa giờ cao
điểm), nên tồn âm xuất hiện khi:

- Đã bán nhưng **quên lập phiếu nhập** cho lô hàng vừa về.
- Đã bê hàng ra quầy nhưng **quên phiếu chuyển kho**.
- Công thức khai sai định mức nên trừ nhiều hơn thực tế.

Cách xử lý: tìm phiếu còn thiếu và lập bù, hoặc chỉnh lại bằng **kiểm kê**
([mục 6.6](/chuong-06-nghiep-vu-kho/6-6-kiem-ke-ton-kho)).

## C — Cây sản phẩm và rà soát

Cũng trong màn Kiểm soát vận hành, phần **Rà soát** vẽ cây quan hệ
*Thành phẩm → Bán thành phẩm → Nguyên liệu* và chỉ ra:

- Món **bán mà không có công thức** → báo cáo lãi lỗ không tính được giá vốn.
- Nguyên liệu **chưa có giá vốn** → giá vốn món tính ra bị thiếu.
- Nguyên liệu **mồ côi** → khai vào hệ thống nhưng không món nào dùng tới.

💡 Rà màn này **một lần mỗi tháng** là đủ. Nó không phải báo cáo để xem hằng
ngày, mà là bộ lọc bắt lỗi khai báo tích tụ dần.

---

## Lịch xem báo cáo gợi ý

| Tần suất | Xem gì | Tìm điều gì |
|---|---|---|
| **Cuối mỗi ca** | Báo cáo ca | Chênh lệch tiền mặt |
| **Hằng ngày** | Tổng quan | Doanh thu, số đơn, sản phẩm dưới định mức |
| **Hằng tuần** | Báo cáo bán hàng, Tồn kho | Giá trị TB/đơn, hàng cần đặt |
| **Hằng tháng** | P&L, Kiểm soát vận hành | Tỷ lệ chi phí, lỗi khai báo |
