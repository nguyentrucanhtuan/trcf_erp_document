---
title: "5.4 Kiểm kê doanh thu và đóng phiên"
---

- **Đường dẫn:** *Báo cáo → Báo cáo ca → Đóng ca* (ở dòng ca đang mở)
- **Khi nào:** Cuối mỗi ca, dành khoảng 15 phút.

![Danh sách ca bán hàng](/images/05-ca-ban-hang-danh-sach.png)

💡 Bốn ô trên màn Báo cáo ca: tổng doanh thu ca, số ca, số ca đang mở, và **tổng chênh lệch tiền mặt** — con số cuối nên liếc mỗi tuần.

## Các bước

![Đối soát khi đóng ca](/images/05-dong-ca-doi-soat.png)

1. Xem **ba ô trên cùng**: số đơn, số sản phẩm, doanh thu của ca.
2. **Đối soát phương thức không tiền mặt**: đối chiếu cột *Hệ thống* với sao kê / máy POS ngân hàng → nhập số thật vào cột *Thực tế*.
3. **Xem số dự kiến trong két** hệ thống tính sẵn.
4. **Đếm tiền thật trong két** → nhập vào. Chênh lệch hiện ngay bằng chữ màu vàng.
5. Bấm **XÁC NHẬN ĐÓNG CA**.

## Giải thích các cột

| Cột | Nghĩa |
|---|---|
| Hệ thống | Số hệ thống ghi nhận cho phương thức đó |
| Thực tế | Số bạn đếm / đối chiếu được |
| Chênh lệch | Tự tính = Thực tế − Hệ thống |

**Số dự kiến trong két** = `tiền đầu ca + doanh thu tiền mặt − chi tiêu tiền mặt − nhập hàng tiền mặt`

## Chênh lệch thì kiểm gì

- [ ] Có đơn nào thu tiền mặt mà bấm nhầm sang chuyển khoản không?
- [ ] Có khoản chi nào lấy từ két mà quên lập phiếu chi không? (*Vận hành → Chi phí*)
- [ ] Có ai lấy tiền lẻ đổi mà chưa bỏ lại không?

💡 Chênh lệch **không chặn** đóng ca — vẫn đóng được, con số chênh được ghi vào báo cáo ca cho quản lý xem sau. Nhưng nên kiểm trước khi đóng.

## Lưu ý

⚠️ **Đóng ca là ghi toàn bộ tiền đếm được vào sổ quỹ.** Sau khi đóng, số dư tiền mặt trên sổ về đúng bằng số của ca kế tiếp — tiền không cộng dồn ảo qua từng ngày. Để lại tiền lẻ cho ca sau thì nhập đúng số đó làm *Tiền mặt đầu ca* của ca mới.

⚠️ **Ca đã đóng không mở lại được**, và không có nút xoá ca. Ca là chứng từ đối soát. Đóng nhầm thì mở ca mới.

💡 Xem lại ca cũ bất kỳ lúc nào bằng nút **Chi tiết** ở màn Báo cáo ca.
