# CLAUDE.md — Cẩm nang hướng dẫn TRCF ERP

Quy tắc viết bài hướng dẫn trong thư mục này. Bài mẫu chuẩn: [1.1](1-1-cau-hinh-ban-dau.html) và [2.1](2-1-thiet-lap-kho-hang.html). Làm bài mới thì mở bài mẫu ra làm khuôn.

## Định dạng và vị trí

- Viết bài bằng **HTML** để dễ nhìn. Mọi bài HTML đặt **thẳng ở thư mục gốc**, không chia thư mục con theo chương. Tên file dạng số-chương-tên-bài (VD `2-1-thiet-lap-kho-hang.html`).
- **Mục lục `index.html`**: liệt kê các chương và tiêu đề bài. Bài nào chưa viết hiện mờ kèm nhãn "Chưa viết". **Viết xong bài nào thì sửa dòng bài đó trong `index.html`** thành liên kết bấm được (đổi `<li class="todo">…</li>` theo mẫu `<li><a href="<tên-file>.html">…</a></li>`).
- Link giữa các bài chỉ ghi tên file (VD `href="1-1-cau-hinh-ban-dau.html"`).
- Lấy phần `<head>` + CSS của bài 1.1 làm khuôn (có chế độ sáng/tối, đọc được trên điện thoại).
- Ảnh đặt trong `images/`, gọi bằng đường dẫn `images/...`.
- Viết **tiếng Việt**. Giữ tiếng Anh cho tên kỹ thuật (mã, endpoint, tên trường trên giao diện).

## Cấu trúc bài (4 phần, theo README)

1. **Đường dẫn vào chức năng** — menu trên màn hình web, kèm địa chỉ trang.
2. **Ví dụ nền + các bước** — nêu 1 ví dụ làm nền, rồi Bước 1, Bước 2, Bước 3… **Mỗi bước đều có ảnh.**
3. **Giải thích chi tiết các trường** — dạng bảng.
4. **Lưu ý quan trọng** — dạng khung cảnh báo, kèm mục "Kiểm tra đã đúng" (checkbox).

## Cách viết

- **Câu ngắn, dạng chỉ dẫn hành động, dạng danh sách gạch đầu dòng.** Mỗi gạch đầu dòng một thao tác. Không viết đoạn văn dài.
- Giá trị cần nhập hoặc chọn đặt trong dấu ngoặc kép. Ví dụ: Địa chỉ: nhập "Kho tại quầy — trừ hàng khi bán."
  - Câu dài: dấu chấm nằm **trong** ngoặc.
  - Giá trị ngắn (mã, tên, lựa chọn): dấu chấm nằm **ngoài** ngoặc, tránh người đọc gõ nhầm dấu chấm. Ví dụ: Mã kho: nhập "KHO-QUAY".
- Tên nút và tên trường in đậm. Lưu ý quan trọng dùng khung đỏ (nghiêm trọng), vàng (cảnh báo), xanh (mẹo).
- Lưu ý cũng viết ngắn: một ý chính, kèm 1–2 gạch con.

## Ảnh minh hoạ

- **Chụp thật** từ app đang chạy ở `http://localhost:3000` (đăng nhập `admin@trcf.vn`; mật khẩu seed nằm trong `.env` của backend).
- Mỗi bước một ảnh, đặt tên `NN-<chủ-đề>-buoc-<n>-<mô-tả>.png` (VD `02-kho-buoc-2-form.png`).
- Khung hình 1440×900. Chụp đúng phần màn hình của bước đó.
- **Không làm đổi dữ liệu thật** khi chụp: mở form rồi đóng, không bấm lưu. Nếu buộc phải lưu để chụp thông báo, trả lại giá trị cũ ngay và báo cho người dùng.
- Số liệu và nhãn trong bài phải khớp giao diện hiện tại, đối chiếu với trang thật chứ không chép từ bài cũ.
