---
title: "5.4 Kiểm kê doanh thu và đóng phiên"
description: "Đối soát tiền mặt cuối ca và đóng phiên."
---

Cuối ca, vào *Báo cáo → Báo cáo ca*, bấm **Đóng ca** ở dòng ca đang mở.

![Danh sách ca bán hàng](/images/05-ca-ban-hang-danh-sach.png)

Màn này cũng là nơi quản lý xem lại lịch sử ca: bốn ô trên cùng là tổng doanh thu
ca, số ca, số ca đang mở và **tổng chênh lệch tiền mặt** — con số cuối cùng là
thứ nên liếc mỗi tuần.

![Đối soát khi đóng ca](/images/05-dong-ca-doi-soat.png)

## Làm từng bước

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

## Chênh lệch thì làm gì

Chênh lệch **không chặn** việc đóng ca — vẫn đóng được, và con số chênh được ghi
lại vào báo cáo ca để quản lý xem sau. Nhưng trước khi đóng, nên kiểm nhanh:

- Có đơn nào thu tiền mặt mà bấm nhầm sang chuyển khoản không?
- Có khoản chi nào lấy từ két mà quên lập phiếu chi không? (Lập ở
  *Vận hành → Chi phí*.)
- Có ai lấy tiền lẻ đổi mà chưa bỏ lại không?

## Lưu ý nghiệp vụ

⚠️ **Đóng ca là ghi toàn bộ tiền đếm được vào sổ quỹ.** Nghĩa là sau khi đóng ca,
số dư tiền mặt trên sổ về đúng bằng số của ca đang mở kế tiếp — tiền không bị
cộng dồn ảo qua từng ngày. Nếu bạn để lại tiền lẻ trong két cho ca sau, hãy nhập
đúng số tiền đó làm *Tiền mặt đầu ca* của ca mới.

⚠️ **Ca đã đóng không mở lại được**, và không có nút xoá ca. Ca là chứng từ đối
soát. Đóng nhầm thì mở ca mới.

💡 Xem lại ca cũ bất kỳ lúc nào bằng nút **Chi tiết** ở màn Báo cáo ca.
