# Bài luyện theo đầu ra

Dùng khi người dùng muốn luyện kỹ năng, không giao toàn bộ bài luyện cho một yêu cầu giải quyết công việc. Chọn bài gần với vấn đề thực và điều chỉnh độ khó theo kiến thức hiện có. Ví dụ giả định phải được ghi rõ; bài luyện không tự chứng minh hiệu quả của một chương trình mang tên Einstein hay Tesla.

## Làm rõ một khái niệm

Chọn “chính xác”, “đáng tin”, “hiểu” hoặc “thời gian thực”. Viết nghĩa đang dùng, cách quan sát và một tình huống chỉ số tốt nhưng mục tiêu chưa đạt.

**Tiêu chí:** người khác biết cần đánh giá điều gì mà không phải đoán ý. Nếu dùng chỉ số thay thế, nêu giới hạn của nó.

## Tìm hai thế giới không phân biệt được

Chọn đầu vào của một hệ thống. Dựng hai tình huống cho cùng đầu vào nhưng cần hai đầu ra khác nhau. Chỉ ra điều kiện khiến chúng không thể phân biệt và thông tin nào có thể giúp.

**Tiêu chí:** lập luận áp dụng trong mô hình cụ thể. Không suy rộng thành “không thuật toán nào làm được” khi chưa cố định dữ liệu và giả định.

## Thay một điều kiện

Lấy lập luận đã hiểu, đổi một điều kiện như camera chính xác thành có sai số, vật đục thành trong suốt, hoặc quan sát độc lập thành bản sao của nhau. Xác định bước suy luận nào phải sửa và vì sao.

**Tiêu chí:** chỉ ra quan hệ bị thay đổi, không chỉ nói chung rằng kết quả sẽ khác. Sau bước tách riêng một yếu tố, có thể đưa các tương tác quan trọng trở lại.

## Dự đoán trước khi xem

Trước khi chạy mã, xem mô phỏng hoặc đọc kết quả, ghi dự đoán và cơ chế hỗ trợ. Đối chiếu kết quả, phân biệt điều đã dự đoán trước với lời giải thích xuất hiện sau đó.

**Tiêu chí:** dự đoán nói rõ kết quả ở điều kiện hoặc nhóm nào; phần chênh lệch giúp sửa mô hình hoặc chỉ ra phép đo còn thiếu. Không đánh giá chỉ bằng số lần đoán đúng mà bỏ qua độ khó hay mức chắc chắn đã nêu.

## Chuyển cấu trúc giữa hai bài toán

Chọn hai bài toán khác bề ngoài. Ánh xạ đối tượng, quan hệ, ràng buộc và mục tiêu; chỉ ra điểm không tương ứng. Dùng ánh xạ để tạo một cơ chế, rồi suy ra điều gì phải kiểm tra khi chuyển miền.

**Tiêu chí:** sản phẩm là hướng giải có điều kiện và giới hạn, không chỉ là một phép ví von.

## Theo dõi một vòng hoạt động

Chọn một hệ thống nhỏ, ghi trạng thái ban đầu và lần theo một chuỗi sự kiện liên quan đến mục tiêu. Dự đoán thay đổi ở từng bộ phận; thử thêm tình huống đổi đầu vào, dừng hoặc lỗi khi chúng có ý nghĩa. Có thể dùng sơ đồ, phép tính, mã giả hoặc mẫu thử để đối chiếu.

**Tiêu chí:** nêu được quy tắc hỗ trợ dự đoán, phần mô hình còn thiếu và kết quả nào sẽ khiến mình sửa nó. Không đánh giá bằng mức độ hình dung sống động; một lần chạy khớp chưa chứng minh mọi hành vi đều đúng.

## Thay cơ chế, giữ chức năng

Chọn một bộ phận đang gây chi phí hoặc hạn chế. Liệt kê chức năng chính và chức năng phụ liên quan; đề xuất một cách khác thực hiện chúng. Theo dõi tác động sang các phần còn lại và chọn phép kiểm tra yêu cầu cần giữ.

**Tiêu chí:** chỉ ra chức năng được bảo toàn, điều kiện để cách thay thế hợp lệ và đánh đổi mới phát sinh. Nếu phải bỏ một yêu cầu để phương án hoạt động, ghi rõ đó là thay đổi bài toán.

## Tạo phương án từ các chức năng

Chọn một việc cần thực hiện và tách thành các chức năng. Với những chức năng có thể thay đổi, tìm các cách thực hiện khác nhau rồi ghép những cách tương thích. Chọn tổ hợp có lý do gắn với mục tiêu, mô tả tương tác và một phép kiểm tra.

**Tiêu chí:** có thay đổi cơ chế thực, không chỉ đổi công cụ hoặc tên gọi. Giữ nguyên các yêu cầu bắt buộc hoặc ghi rõ phần đề xuất thay đổi.

## Đọc một công trình bằng cách dựng lại bài toán

Khi có nội dung công trình, trả lời những câu hỏi phù hợp trước khi ghi nhớ tên phương pháp:

- Hiện tượng hoặc mục tiêu nào cần giải quyết?
- Cách trước phụ thuộc giả định gì, và tình huống nào làm lộ hạn chế?
- Thành phần mới thay đổi cơ chế hoặc biểu diễn nào?
- Nếu lời giải thích đó đúng, kết quả nào phải xuất hiện? Có cách giải thích thay thế không?
- Đánh giá đã tách được các khả năng đó chưa? Trong điều kiện nào lợi thế có thể mất?

Phân biệt điều tác giả nêu, điều dữ liệu hỗ trợ và suy luận của người đọc. Nếu chỉ có phần tóm tắt, không suy diễn như đã đọc phương pháp và thí nghiệm đầy đủ.

**Tiêu chí:** giải thích được vai trò của thành phần mới, phạm vi bằng chứng và câu hỏi chưa được giải đáp.

## Ghi lại một vòng học

Khi hữu ích, ghi ngắn: mục tiêu, quan sát, giả định, mô hình nhỏ, thay đổi đề xuất, dự đoán, kiểm tra và điều đã cập nhật. Không bắt buộc thành biểu mẫu dài.

Một vòng có ích có thể chỉ loại bỏ một hướng sai hoặc tìm ra phần kiến thức cần bổ sung. Nếu liên tục không tạo được dự đoán hoặc kiểm tra, thu hẹp bài toán và học hay đo phần cơ chế chưa biết. Theo dõi chất lượng các đầu ra này thay vì cảm giác đã suy nghĩ sâu.
