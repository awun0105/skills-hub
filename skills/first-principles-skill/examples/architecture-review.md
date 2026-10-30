# Ví dụ: có nên chia ứng dụng thành nhiều dịch vụ?

Đây là tình huống giả định. Các thông tin bên dưới được đặt ra để minh họa, không phải dữ kiện đã thu thập từ một doanh nghiệp thực. Mẫu này dành cho quyết định phức tạp; câu hỏi nhỏ không cần trình bày dài như vậy.

## Mục tiêu

Giả sử một nhóm muốn rút ngắn thời gian đưa thay đổi đến người dùng mà vẫn giữ độ tin cậy và chi phí vận hành trong giới hạn đã thống nhất. Nhóm đang cân nhắc microservices (kiến trúc gồm các dịch vụ có thể triển khai độc lập), sau khi thấy công ty khác áp dụng thành công.

Trước khi đánh giá giải pháp, cần xác định thời gian phát hành mong muốn, cách đo độ tin cậy và ngân sách vận hành. “Phải chia dịch vụ” là đề xuất, chưa phải yêu cầu bắt buộc.

## Căn cứ và khoảng trống

| Thông tin trong tình huống giả định | Vai trò và giới hạn |
|---|---|
| Nhóm có 12 kỹ sư, thuộc hai đội | Điều kiện tổ chức; không đủ để kết luận một kiến trúc là tối ưu. |
| Nhóm báo cáo rằng chờ kiểm tra trước phát hành đang gây chậm | Quan sát được cung cấp trong tình huống; cần nhật ký và số đo để xác định khâu chờ thực sự. |
| Độ tin cậy hiện có phải được duy trì | Yêu cầu; cần chuyển thành tiêu chí đánh giá cụ thể với người chịu trách nhiệm. |
| Chia dịch vụ sẽ làm phát hành nhanh hơn | Giả thuyết; phụ thuộc mức tách biệt, dữ liệu dùng chung và quy trình triển khai. |
| Các thành phần có cần tăng tài nguyên độc lập không? | Điều chưa biết; cần dữ liệu tải nếu yếu tố này được dùng để biện minh cho việc tách. |

Việc công ty khác thành công cho biết có một cách làm đáng tham khảo. Cần kiểm tra mục tiêu, nguồn lực và các ràng buộc của họ trước khi áp dụng kinh nghiệm đó.

## Phương án và suy luận

Nếu thời gian chờ chủ yếu nằm ở một bộ kiểm tra chậm, tối ưu cách chọn và chạy kiểm tra là phương án trực tiếp cần đánh giá. Tách dịch vụ chưa chắc xử lý được nguyên nhân đó.

Nếu nhiều thay đổi liên tục ảnh hưởng chéo giữa các phần của ứng dụng, modular monolith (ứng dụng triển khai chung nhưng chia mô-đun với ranh giới rõ ràng) có thể giúp quản lý phụ thuộc. Cần kiểm tra xem ranh giới đề xuất có phản ánh dữ liệu và trách nhiệm thực tế không.

Nếu có một phần ít phụ thuộc, cần phát hành hoặc tăng tài nguyên theo nhu cầu riêng, tách phần đó thành dịch vụ có thể đáng thử. Đánh đổi gồm giao tiếp qua mạng, đồng bộ dữ liệu, theo dõi lỗi và công sức vận hành. Không suy ra lợi ích hoặc chi phí bằng một tỷ lệ cố định chỉ từ số kỹ sư.

## Cách kiểm chứng đề xuất

Đầu tiên, đo thời gian từ lúc một thay đổi sẵn sàng đến khi người dùng nhận được, tách các khoảng chờ để xác định khâu gây chậm. So sánh trên các thay đổi đại diện, tránh quy toàn bộ biến động cho kiến trúc.

Tiếp theo, chọn một cải tiến có phạm vi nhỏ dựa trên nguyên nhân quan sát được. Nếu thử tách dịch vụ, chọn phần có ranh giới phù hợp và so sánh thời gian phát hành, lỗi phát sinh, độ trễ và công sức vận hành với cách hiện tại. Định nghĩa tiêu chí chấp nhận theo mục tiêu của nhóm trước khi thử. Việc triển khai thử phụ thuộc phạm vi được người dùng cho phép; ví dụ này chỉ đề xuất cách đánh giá.

## Kết luận có điều kiện

Với thông tin giả định hiện có, bước được hỗ trợ tốt nhất là đo khâu gây chậm phát hành. Chưa đủ căn cứ để kết luận nên tách toàn bộ hệ thống hoặc giữ nguyên kiến trúc lâu dài.

Xem xét lại lựa chọn khi có bằng chứng về nhu cầu triển khai độc lập, khác biệt tải hoặc chi phí phụ thuộc giữa các đội. Không dùng một ngưỡng số kỹ sư hay một số lần xung đột tự đặt làm quy luật chung.
