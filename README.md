# Cẩm nang sử dụng TNTDRINK ERP

Tài liệu hướng dẫn vận hành hệ thống quản trị quán cà phê TNTDRINK ERP, viết cho cả
nhân viên đứng quầy (làm từng bước) lẫn quản lý (lưu ý nghiệp vụ).

- Đọc online: <https://nguyentrucanhtuan.github.io/trcf_guide_document/>
- Mục lục 12 bước: [`docs/index.md`](docs/index.md)
- Ảnh minh hoạ: [`docs/images/`](docs/images/)

## Sửa bài ở đâu

**Bài viết là các tệp `.md` trong `docs/`.** Tệp `.html` cùng tên là bản **sinh tự động**
để đăng web — đừng sửa tay, lần sinh sau sẽ ghi đè.

1. Mở tệp `.md` trong VS Code (bấm `Cmd+Shift+V` để xem trước), sửa chữ.
2. Chạy: `python3 tools/build.py` — sinh lại toàn bộ `.html` (không cần cài thêm gì).
3. Commit cả `.md` lẫn `.html` rồi push. GitHub Pages đăng thư mục `docs/`.

Lệnh build báo ⚠ nếu có ảnh thiếu, link hỏng, hoặc bài chưa đưa vào mục lục.

**Thêm bài mới:** tạo `docs/N-k-ten-bai.md` (chép một bài có sẵn làm khuôn), thêm một dòng
`- [N.k Tên bài](N-k-ten-bai.md)` vào đúng bước trong `docs/index.md`, rồi chạy build.
Thanh mục lục bên trái mọi trang tự lấy từ `index.md`.

## Cấu trúc nội dung hướng dẫn

1. Đường dẫn vào chức năng (trên màn hình web)
2. Tạo 1 ví dụ để làm nền, sau đó hướng dẫn chi tiết các bước thực hiện kèm hình ảnh từng bước, ví dụ: Bước 1, Bước 2, Bước 3. Mỗi bước đều có hình ảnh.
3. Giải thích chi tiết các trường.
4. Những lưu ý quan trọng khi thực hiện.

Các câu hướng dẫn nên là câu chỉ dẫn hành động ngắn gọn dễ hiểu và dạng list, bảng để dễ nhìn, không quá dài dòng.

## Cách sửa bài — cú pháp Markdown

Markdown thường, thêm vài quy ước để ra đúng khung đẹp trên web:

| Viết trong `.md` | Ra trên web |
| --- | --- |
| `crumb: Bước 1 · Nhập đơn vị tính` (đầu tệp, giữa hai dòng `---`) | Dòng chữ xám nhỏ trên tiêu đề |
| `# 1.1 Tên bài` | Tiêu đề bài |
| `## 1. Đường dẫn vào chức năng` (có số và dấu chấm) | Mở một **khung trắng** mới |
| `## Kiểm tra đã đúng` (không số) | Tiêu đề phụ, vẫn nằm trong khung đang mở |
| `### Bước 1: Mở trang Đơn vị tính` | **Bước có nhãn xanh**; mọi thứ bên dưới (list, ảnh) thuộc bước đó |
| `### Hai loại công thức` (không bắt đầu bằng "Bước N:") | Tiêu đề nhỏ |
| `==Quản lý sản phẩm → Đơn vị tính==` | Nhãn xanh đường dẫn menu |
| `**Lưu**` / `*Đơn vị gốc*` / `` `/uoms` `` | Đậm / nghiêng / mã |
| `![Bước 1: …](images/02-uom-buoc-1-danh-sach.png)` (một dòng riêng) | Ảnh chụp màn hình |
| `[mục 2.2](2-2-thanh-pham.md)` | Link sang bài khác (tự đổi thành `.html`) |
| Bảng `\| Trường \| Điền gì \|` | Bảng |
| `- [ ] Đã có đơn vị gốc` | Ô tích "Kiểm tra đã đúng" |
| Khối ` ``` ` | Khung chữ đều (sơ đồ công thức) |

Khung ví dụ và khung lưu ý viết bằng dấu `>`:

```markdown
> **Ví dụ:** quán nhập cà phê theo kg, pha chế trừ theo gram.
>
> - Nhập 5 kg → hệ thống ghi tồn 5000 g.

> [!CAUTION]
> **Khung đỏ — nghiêm trọng.**
>
> - Một ý con.

> [!WARNING]
> Khung vàng — cảnh báo.

> [!TIP]
> Khung xanh — mẹo.
```

`>` không có `[!...]` là khung **Ví dụ** (nền xanh nhạt). Các khung `[!CAUTION]`,
`[!WARNING]`, `[!TIP]` cũng hiện có màu khi xem trên GitHub.

Mục lục `docs/index.md` dùng thêm: `## Giai đoạn: Tên nhóm` (nhãn xám), `### Bước N — Tên bước`
(ô có số), một dòng mô tả, rồi danh sách link tới các bài con.
