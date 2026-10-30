---
name: creative-problem-solving
description: Tạo và phát triển hướng giải khi bài toán bế tắc, cách hiện tại chưa đáp ứng mục tiêu hoặc người dùng muốn một cách tiếp cận mới. Dùng thí nghiệm tưởng tượng, mô hình cơ chế, đổi biểu diễn, tương tự cấu trúc và giả thuyết cạnh tranh để tạo phương án có dự đoán và cách kiểm chứng. Phù hợp với nghiên cứu, thuật toán, thiết kế hệ thống, học tập và vấn đề thực tế; không cần cho thao tác thường lệ đã có cách làm rõ ràng.
metadata:
  version: "0.2.0"
---

# Creative Problem Solving (giải quyết vấn đề sáng tạo)

Giúp người dùng tiến từ “cần một ý tưởng mới” đến một hướng giải có cơ chế, dự đoán và cách đánh giá. Tính sáng tạo có thể nằm ở cách đặt câu hỏi, biểu diễn, cơ chế, phép quan sát hoặc cách kết hợp các thành phần; không đồng nghĩa thêm độ phức tạp.

## Cách diễn đạt và phạm vi

- Viết bằng văn xuôi tiếng Việt, nối kết các ý. Giữ thuật ngữ tiếng Anh cần độ chính xác và giải nghĩa tiếng Việt ngay bên cạnh trong ngoặc tròn ở lần xuất hiện đầu tiên, ví dụ `thought experiment (thí nghiệm tưởng tượng)`. Không cần lặp phần giải nghĩa trong cùng ngữ cảnh. Giữ nguyên tên riêng, định danh, đường dẫn và câu lệnh; đặt lời giải thích bên ngoài chuỗi cần sao chép. Theo ngôn ngữ khác nếu người dùng yêu cầu.
- Điều chỉnh độ sâu theo bài toán. Việc nhỏ có thể chỉ cần một hướng thử và cách đánh giá; bài toán khó cần phân biệt giả định, phương án và bằng chứng. Không bắt buộc đủ số bước, số ý tưởng, bảng hay ví dụ cho mọi yêu cầu.
- Phối hợp với `first-principles` khi cần làm rõ nền tảng và ràng buộc; skill này vẫn dùng được độc lập. Không mặc định tư duy từ nguyên lý gốc chỉ tìm lời giải rẻ nhất hoặc đơn giản nhất.
- Nếu người dùng mới có một chủ đề hoặc hiện tượng và cần tìm câu hỏi đáng theo đuổi, có thể dùng `inquiry-and-problem-framing` nếu có sẵn. Khi đã có bài toán đủ rõ, tập trung phát triển hướng giải; không bắt buộc đi qua cả hai skill.
- Giữ mục tiêu, đầu vào được phép dùng, ngân sách và phạm vi hành động của người dùng. Nếu đề xuất thay đổi điều kiện bài toán, ghi rõ phần đã thay đổi và chỉ xem đó là một phương án mở rộng. Thực hiện kiểm tra trong phạm vi đã được cho phép; yêu cầu phân tích không tự cho phép thay đổi hệ thống đang vận hành hoặc thử nghiệm ngoài phạm vi đó.

## Tổ chức một vòng tìm hướng giải

Các bước dưới đây hướng dẫn công việc, không phải biểu mẫu câu trả lời. Có thể quay lại bước trước khi phát hiện thông tin mới.

### Làm câu hỏi đủ chính xác

Xác định điều cần tạo hoặc cải thiện, dữ liệu được tiếp cận, yêu cầu giữ cố định và tiêu chí thành công. Với các từ như “tốt”, “đúng”, “hiểu”, “nhanh”, chuyển thành điều có thể quan sát, tính toán hoặc đối chiếu với tiêu chí người dùng. Hỏi xem chỉ số có thể tốt lên trong khi mục tiêu vẫn chưa đạt hay không.

Phân biệt dữ kiện có nguồn hoặc quan sát, giả định, điều cố ý bỏ qua và điều chưa biết. Chỉ hỏi thêm khi thông tin thiếu có thể làm đổi hướng giải và không thể suy ra hợp lý; nếu vẫn tiến hành được, nêu giả định tạm thời.

Khi gặp điều bất ngờ hoặc một cách làm quen thuộc chưa giải thích được, ghi điều đã kỳ vọng, quan sát thực có và điều kiện liên quan trước khi chọn giải pháp. Chuyển khoảng chưa hiểu thành câu hỏi có thể tìm hiểu; kiểm tra lại phép đo trước khi xem nó là bất thường có thật. Đọc [Tò mò và đánh giá độc lập](references/curiosity-and-independent-judgment.md) khi cần phát triển câu hỏi hoặc đánh giá một lời khẳng định đang chi phối hướng giải.

### Chọn thao tác theo chỗ đang mắc

| Chỗ cần tiến thêm | Thao tác nên thử | Sản phẩm cần có |
|---|---|---|
| Khái niệm hoặc phép đánh giá mơ hồ | Làm rõ quy trình quan sát và đo | Một câu hỏi cùng tiêu chí đánh giá cụ thể |
| Chưa rõ dữ liệu có đủ không | Dựng hai tình huống khác nhau cho cùng quan sát | Giới hạn có điều kiện hoặc thông tin cần bổ sung |
| Không giải thích được hiện tượng | Dựng mô hình cơ chế nhỏ và giả thuyết cạnh tranh | Các cơ chế dẫn đến dự đoán khác nhau |
| Cách biểu diễn đang cản trở | Đổi biến, cấu trúc, mức mô tả hoặc giữ nhiều khả năng | Biểu diễn mới và quan hệ với bài toán gốc |
| Chưa có cơ chế giải phù hợp | Mượn cấu trúc từ bài toán khác, phân rã chức năng rồi kết hợp các cách thực hiện | Phương án khác nhau về cơ chế, có điều kiện áp dụng |
| Phương pháp có vẻ hợp lý nhưng còn nghi ngờ | Xét cực hạn, đối xứng và phản ví dụ nhỏ | Điều kiện thất bại hoặc thuộc tính phải được giữ |

Đọc [Các thao tác tạo ý tưởng](references/techniques.md) khi cần chỉ dẫn để thực hiện một thao tác trong bảng. Chọn phần liên quan, không tải mọi tài liệu cho câu hỏi nhỏ.

Dựng phiên bản đơn giản vẫn giữ được cơ chế cần nghiên cứu. Ví dụ, phân tích che khuất phải giữ che khuất; đánh giá độ bền trước nhiễu phải đưa nhiễu trở lại sau bước lý tưởng hóa. Ghi rõ các thành phần, quan hệ, quy tắc và điều được giữ cố định; dùng sơ đồ, phương trình, mã giả hoặc mô phỏng nhỏ khi chúng làm dự đoán rõ hơn.

Khi cần nhiều hướng, tạo những phương án khác nhau về cơ chế hoặc biểu diễn, thay vì chỉ đổi tên hay chỉnh vài tham số. Không chặn một ý tưởng chỉ vì chưa quen hoặc chưa đủ chi tiết; phát triển nó đến mức có thể đánh giá. Sau đó sàng lọc bằng ràng buộc thực, cơ sở chuyên môn, đánh đổi và khả năng kiểm chứng. Không mặc định giải pháp mới hơn là tốt hơn giải pháp sẵn có.

Đánh giá độc lập bằng cách dựng lại lý do mạnh nhất ủng hộ một lời khẳng định, rồi kiểm tra bằng chứng và điều kiện áp dụng. Danh tiếng không thay thế bằng chứng, nhưng chuyên môn và kết quả đã được kiểm chứng vẫn có giá trị. Dùng cùng tiêu chuẩn cho ý tưởng phổ biến, ý tưởng trái số đông và ý tưởng của chính mình; nêu bằng chứng nào sẽ khiến mình đổi ý. Bất đồng về ý tưởng cần gắn với lập luận, không suy từ tính cách hoặc động cơ của người đưa ra nó.

### Biến ý tưởng thành dự đoán

Với hướng đáng theo, tóm tắt:

- Thay đổi gì và vì sao cơ chế đó có thể giải quyết điểm mắc?
- Nếu cơ chế đúng, kết quả nào khác với cách hiện tại phải xuất hiện, trong điều kiện nào?
- Có lời giải thích thay thế nào cũng dự đoán kết quả đó? Quan sát nào phân biệt được chúng?

Nếu chưa nêu được hệ quả khác biệt, tiếp tục làm rõ ý tưởng hoặc tìm kiến thức còn thiếu. Không dùng việc đặt tên một kỹ thuật như thay thế cho mô tả cơ chế.

### Kiểm tra và cập nhật

Chọn phép tính, chứng minh, phản ví dụ, quan sát, thử nghiệm hoặc phản hồi người dùng phù hợp với loại bài toán. Khi cần so sánh, xác định mốc đối chiếu, điều kiện, nguồn lực và tiêu chí trước khi thử; nếu ngân sách khác nhau, công bố khác biệt thay vì quy lợi ích hoàn toàn cho cơ chế.

Phân biệt **kết luận có suy ra từ giả định không** với **giả định có mô tả đủ tốt tình huống thực không**. Mô phỏng đúng mô hình chưa chứng minh mô hình đúng ngoài thực tế. Điểm số tăng chưa xác nhận cơ chế; cần xem điều kiện nào có hoặc mất lợi ích và lời giải thích thay thế. Ví dụ số không thay thế chứng minh toán học, còn phản ví dụ hợp lệ chỉ bác bỏ phát biểu nằm trong phạm vi của nó.

Nêu rõ điều đã kiểm chứng, điều mới suy luận và phép thử còn đề xuất. Không bịa dữ liệu, kết quả, nguồn hoặc độ chắc chắn. Khi chưa thể kiểm tra, đưa kết luận có điều kiện và bước tiếp theo khả thi.

Một vòng hữu ích kết thúc bằng hướng giải có thể kiểm tra, một giới hạn, phản ví dụ, phép đo hoặc nhu cầu kiến thức cụ thể. Nếu chỉ diễn đạt lại cùng câu hỏi, chuyển sang thu thập thông tin hoặc học phần còn thiếu trong phạm vi được phép. Dừng hoặc xem xét lại khi hướng bị bác bỏ, không đáp ứng ràng buộc, hay chi phí theo đuổi vượt giá trị mong đợi; không kéo dài việc đặt câu hỏi vô hạn.

## Mang theo giới hạn của kết luận

- “Chưa tìm thấy cách tốt hơn” khác với “đã chứng minh không thể tốt hơn”. Không dùng tưởng tượng để vượt một giới hạn đã chứng minh trong cùng điều kiện.
- Kiểm tra cả `identifiability (khả năng xác định đáp án từ dữ liệu)` và `stability (độ ổn định trước sai số)`: có đáp án duy nhất trong mô hình lý tưởng chưa đủ để ước lượng chính xác khi có nhiễu.
- Phân biệt `invariance (tính bất biến)` với `equivariance (tính biến đổi tương ứng)`: danh tính hoặc quan hệ vật lý có thể giữ nguyên trong khi tọa độ đầu ra phải đổi theo quy tắc.
- Một giai thoại hoặc hình dung sống động không xác nhận cơ chế. “Einstein thinking” và “Tesla thinking” chỉ là cách gọi gợi nhớ, không phải bảo đảm hiệu quả hay quy trình chuẩn được xác nhận.
- Phân biệt ý tưởng mới đối với người dùng với đóng góp mới đối với lĩnh vực. Tra cứu công trình hoặc giải pháp liên quan trước khi khẳng định tính mới; chưa đối chiếu thì nói rõ.

## Trả kết quả và tài liệu bổ trợ

Trình bày hướng giải hoặc phát hiện quan trọng trước, rồi tóm tắt căn cứ, thay đổi đề xuất, dự đoán, cách kiểm tra và giới hạn cần biết. Chỉ trình bày các phần có ích cho quyết định hiện tại; không yêu cầu người dùng thực hiện một nghi thức dài.

- [Ví dụ có lập luận và giới hạn](references/worked-examples.md): chiều sâu chiếc hộp, gán nhãn khi che khuất, đổi biến trong toán và xử lý chậm trễ bàn giao. Đọc khi cần minh họa thao tác trong miền tương ứng.
- [Bài luyện theo đầu ra](references/practice.md): đọc khi người dùng muốn luyện kỹ năng hoặc dựng lại lập luận của một công trình.
