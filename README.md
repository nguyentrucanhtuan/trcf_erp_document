# Cẩm nang sử dụng TNTDRINK ERP

Tài liệu hướng dẫn vận hành hệ thống quản trị quán cà phê TNTDRINK ERP, viết cho cả
nhân viên đứng quầy (làm từng bước) lẫn quản lý (lưu ý nghiệp vụ).

Mỗi mục là một bài riêng; mỗi chương là một thư mục. Mục lục đầy đủ ở
[`index.md`](index.md); ảnh minh hoạ nằm trong [`images/`](images/).

> **Lưu ý khi đọc trên GitHub:** đường dẫn trong tài liệu viết theo chuẩn
> Mintlify (dạng `/chuong-02-kho-va-don-vi-tinh/2-1-thiet-lap-kho-hang`), nên
> bấm liên kết ở đây sẽ không sang trang được — mở thẳng tệp trong thư mục, hoặc
> đọc bản đã dựng trên Mintlify.

## Các chương

| Chương | Nội dung | Số bài |
|---|---|---|
| [1](chuong-01-cau-hinh-he-thong/) | Cấu hình hệ thống | 1 |
| [2](chuong-02-kho-va-don-vi-tinh/) | Thiết lập kho hàng, sản phẩm | 2 |
| [3](chuong-03-quan-ly-san-pham/) | Quản lý sản phẩm | 5 |
| [4](chuong-04-thiet-lap-pos/) | Thiết lập POS | 4 |
| [5](chuong-05-ban-hang-tai-quay/) | Quy trình bán hàng tại quầy | 6 |
| [6](chuong-06-nghiep-vu-kho/) | Chi tiết các nghiệp vụ kho | 6 |
| [7](chuong-07-ca-lam-va-cham-cong/) | Quản lý ca làm và chấm công | 5 |
| [8](chuong-08-bao-cao-kinh-doanh/) | Báo cáo kinh doanh | 3 |

## Xuất bản

Cấu hình Mintlify nằm ở [`docs.json`](docs.json) ngay thư mục gốc — mỗi chương là
một nhóm trong `navigation`, mỗi bài là một trang. Trong phần Git settings của
Mintlify: chọn repo này, nhánh `main`, **tắt** công tắc "docs.json is in a
subdirectory".

Thêm một bài mới thì phải khai đường dẫn của nó vào `docs.json`; Mintlify không
tự dò thư mục nên bài không khai sẽ không lên site.
