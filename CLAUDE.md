# CLAUDE.md — Cẩm nang hướng dẫn TRCF ERP

Quy tắc viết bài hướng dẫn trong thư mục này. Bài mẫu chuẩn: [1.1](noi-dung/1-1-thiet-lap-don-vi-tinh.md) và [6.1](noi-dung/6-1-tao-mau-kiem-kho.md). Làm bài mới thì mở bài mẫu ra làm khuôn.

## Định dạng và vị trí

- **Viết bài bằng Markdown (`.md`)** — bản gốc để người dùng tự sửa. HTML **không nằm trong repo**: GitHub Actions (`.github/workflows/pages.yml`) chạy `python3 tools/build.py` mỗi lần push lên `main` rồi đăng GitHub Pages. Chạy build ở máy ra `_site/` (git bỏ qua) để xem thử và để soát ⚠ trước khi push — build có ⚠ thì CI dừng, web giữ bản cũ.
- Cú pháp Markdown của cẩm nang (khung bước, khung lưu ý `> [!CAUTION]`/`[!WARNING]`/`[!TIP]`, khung ví dụ `>`, nhãn menu `==…==`, ô tích `- [ ]`): xem bảng trong [README.md](README.md), mục "Cách sửa bài". Giao diện (CSS sáng/tối, mobile) nằm ở `tools/style.css`.
- Mọi bài đặt **trong thư mục `noi-dung/`**, không chia thư mục con. Cẩm nang gồm 12 bước, mỗi bước có các bài con đánh số `N.k` (VD 6.1, 6.2). Tên file dạng `N-k-tên-bài.md` (VD `6-1-tao-mau-kiem-kho.md`). Trang chủ `noi-dung/index.md` là sơ đồ thứ tự 12 bước.
- **Mục lục `index.md`**: mỗi bước có danh sách link tới bài con. Bài chưa viết thì chưa đưa vào. **Thêm bài mới thì thêm dòng `- [N.k Tên bài](<tên-file>.md)` vào đúng bước trong `index.md`**, rồi chạy build.
- Link giữa các bài ghi tên file `.md` (VD `[mục 1.1](1-1-thiet-lap-don-vi-tinh.md)`) — build tự đổi sang `.html`.
- Ảnh đặt trong `noi-dung/images/`, gọi bằng đường dẫn `images/...`.
- Viết **tiếng Việt**. Giữ tiếng Anh cho tên kỹ thuật (mã, endpoint, tên trường trên giao diện).
- Build phải chạy sạch (không dòng ⚠ nào: ảnh thiếu, link hỏng, bài chưa vào mục lục).

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

## Thanh điều hướng bên trái

- Mọi trang (kể cả trang chủ) có thanh mục lục bên trái, liệt kê 12 bước và các bài con, đánh dấu bài đang xem.
- Thanh này `tools/build.py` tự sinh từ `noi-dung/index.md`. Thêm hoặc đổi tên bài: sửa `index.md` rồi chạy build. Không sửa tay từng trang.
