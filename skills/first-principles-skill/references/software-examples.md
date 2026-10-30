# Ví dụ kỹ thuật phần mềm

Đây là các tình huống giả định để minh họa cách suy luận, không phải kết quả đo hay khuyến nghị công nghệ cho một hệ thống đã kiểm tra.

## Ứng dụng xử lý video chậm

Người dùng đề xuất mua GPU (bộ xử lý đồ họa) mới vì ứng dụng chậm. Trước hết cần làm rõ tốc độ yêu cầu, độ chính xác cần giữ và giới hạn chi phí. “GPU hiện tại yếu” là giả thuyết; cần đo thời gian đọc dữ liệu, tiền xử lý, chạy mô hình và xuất kết quả để phân biệt nguyên nhân.

Giả sử một phép đo trong tình huống minh họa cho thấy đọc và giải mã video chiếm phần lớn thời gian. Điều này làm cho việc kiểm tra khâu đọc dữ liệu trở nên đáng ưu tiên; nó chưa chứng minh GPU mới không mang lại lợi ích. Cũng cần xem phép đo có tính đến các tác vụ chạy chồng nhau và thời gian chờ thiết bị hay không.

Một bước thử hợp lý là so sánh cách đọc hiện tại với một cách cải thiện việc đọc trên cùng video và cùng mô hình. Đo thời gian xử lý toàn bộ, kiểm tra kết quả đầu ra, lặp lại đủ để nhận ra biến động. Chấp nhận thay đổi khi đạt tiêu chí tốc độ đã thống nhất mà vẫn giữ chất lượng trong giới hạn cho phép.

Nếu chưa có phép đo thực, kết luận phù hợp là “đo từng khâu trước khi quyết định đầu tư”, kèm cách đo. Không viết “đã xác định lỗi nằm ở khâu dữ liệu”.

## Có cần thêm bộ nhớ đệm dùng chung?

Mục tiêu là giảm thời gian phản hồi mà vẫn đáp ứng yêu cầu về độ mới của dữ liệu. “Cần Redis”, “chỉ có một máy nên dùng bộ nhớ cục bộ là đủ” và “dữ liệu ít thay đổi nên có thể lưu một giờ” đều cần kiểm tra.

Những thông tin có thể làm đổi quyết định gồm truy vấn nào chậm và xuất hiện thường xuyên, số tiến trình phục vụ, yêu cầu đồng bộ giữa các tiến trình, quy tắc cập nhật dữ liệu và giới hạn bộ nhớ. Một máy có thể chạy nhiều tiến trình; mức độ thay đổi thường thấy của dữ liệu không tự xác định được mức dữ liệu cũ mà người dùng chấp nhận.

Tùy căn cứ thu được, có thể so sánh tối ưu truy vấn, lưu tạm trong từng tiến trình hoặc dùng bộ nhớ đệm chung. Mỗi cách cần được đánh giá về tốc độ, tính đúng của dữ liệu, chi phí vận hành và hành vi khi thành phần lưu tạm bị lỗi. Giải pháp sẵn có và cách hiện tại đều có thể là phương án phù hợp.

Phép thử đề xuất là chạy tải đại diện, đo thời gian phản hồi, đồng thời kiểm tra cập nhật dữ liệu có được phản ánh trong khoảng cho phép hay không. Khi chưa có kết quả, chỉ nêu lựa chọn có điều kiện và thông tin cần bổ sung, không ấn định công nghệ hoặc thời hạn lưu từ thói quen.
