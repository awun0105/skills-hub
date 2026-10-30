---
name: first-principles
description: Tư duy từ nguyên lý gốc (first-principles thinking) để làm rõ mục tiêu, kiểm tra giả định, xây dựng và kiểm chứng phương án từ dữ kiện, yêu cầu và ràng buộc. Dùng khi người dùng yêu cầu phân tích từ gốc, challenge assumptions, 第一性原理, hoặc cần đánh giá lại cách giải một vấn đề trong học tập, công việc, đời sống hay kỹ thuật.
metadata:
  version: "0.3.0"
---

# First Principles Thinking (tư duy từ nguyên lý gốc)

Tìm những điều cơ bản có căn cứ, kiểm tra các giả định đi kèm, rồi xây dựng cách giải từ những điều đó. Câu hỏi trung tâm:

> Điều gì thực sự cần đúng để đạt mục tiêu này? Điều gì chỉ là cách làm mình đã quen hoặc nghe người khác nói?

## Cách diễn đạt và độ sâu

- Viết bằng văn xuôi tiếng Việt, rõ ràng và nối kết các ý. Nếu người dùng yêu cầu ngôn ngữ khác, theo yêu cầu đó.
- Giữ nguyên từ ngữ hoặc thuật ngữ tiếng Anh khi cần độ chính xác, kèm phần giải nghĩa tiếng Việt ngay bên cạnh trong ngoặc tròn, chẳng hạn `latency (độ trễ)` hoặc `baseline (mốc đối chiếu ban đầu)`. Khi lặp lại trong cùng ngữ cảnh, không cần lặp phần giải nghĩa. Giải thích từ viết tắt ở lần xuất hiện đầu tiên.
- Giữ nguyên tên riêng, tên sản phẩm, định danh trong mã, đường dẫn và câu lệnh; khi cần giải nghĩa, đặt lời giải thích bên ngoài chuỗi cần sao chép, không sửa chuỗi đó.
- Điều chỉnh độ sâu theo bài toán: câu hỏi đơn giản có thể chỉ cần vài câu; quyết định phức tạp cần trình bày căn cứ, lựa chọn, đánh đổi và cách kiểm chứng. Không ép mọi câu trả lời vào biểu mẫu nhiều mục.
- Dùng ví dụ đời thường khi giúp làm sáng tỏ một ý khó. Không bắt buộc thêm ví dụ nếu bài toán thực tế đã đủ rõ. Chỉ dùng bảng hoặc danh sách khi chúng giúp so sánh hay theo dõi dễ hơn.

## Cách áp dụng

Các câu hỏi dưới đây hướng dẫn suy luận; không bắt buộc trình bày thành năm phần trong câu trả lời.

### 1. Mục tiêu cụ thể là gì?

Xác định người dùng cần làm được việc gì và kết quả nào cho thấy đã đạt mục tiêu. Phân biệt mục tiêu với giải pháp được đề xuất: “xử lý video trong thời gian cho phép” là mục tiêu; “mua GPU (bộ xử lý đồ họa) mới” là một lựa chọn cần đánh giá.

Giữ đúng phạm vi người dùng yêu cầu. Chỉ hỏi thêm nếu thông tin thiếu có thể làm thay đổi đáng kể kết luận và không thể suy ra hợp lý. Nếu vẫn có thể tiến hành, nêu giả định tạm thời và giới hạn của phân tích.

### 2. Mình thực sự biết gì và đang mặc định điều gì?

Phân biệt các loại cơ sở suy luận sau; không cần lập bảng nếu chỉ có ít thông tin:

| Loại | Cách sử dụng |
|---|---|
| Dữ kiện có bằng chứng | Nêu quan sát, phép đo, nguồn hoặc dữ liệu hỗ trợ, cùng phạm vi mà chúng chứng minh được. |
| Yêu cầu và ràng buộc | Nêu điều bắt buộc để đạt mục tiêu và giới hạn thực tế. Phân biệt yêu cầu người dùng xác nhận với mong muốn hoặc giới hạn đang suy đoán. |
| Giả định và suy luận | Ghi rõ điều được tạm coi là đúng hoặc suy ra từ dữ kiện; không trình bày như sự thật đã đo được. |
| Điều chưa biết | Chỉ ra thông tin còn thiếu có thể ảnh hưởng đến lựa chọn, cùng cách tìm hiểu nếu cần. |

Các cơ sở này thường phụ thuộc vào hoàn cảnh và có thể cần cập nhật. Không gọi yêu cầu nghiệp vụ, số liệu mẫu, ước lượng hay kinh nghiệm là “chân lý tuyệt đối”. Gắn nhãn tình huống và số liệu giả định ngay khi giới thiệu; không kể chúng như kết quả điều tra hoặc thử nghiệm đã thực hiện.

Kiểm tra những câu như “phải”, “luôn”, “chỉ có cách” hoặc “ai cũng làm vậy”: điều này có thật sự cần để đạt mục tiêu không, có bằng chứng gì, và nếu thay đổi thì yêu cầu nào không còn được đáp ứng? Phân biệt ràng buộc thực với lựa chọn trước đây và thói quen.

Ưu tiên giả định có khả năng làm đổi quyết định. Dừng phân rã khi đã đủ cơ sở để lựa chọn hoặc thiết kế một phép kiểm tra hữu ích; không cố tìm nền tảng tuyệt đối cho mọi chi tiết.

### 3. Từ đó có thể xây dựng những cách giải nào?

Liên kết từng lựa chọn quan trọng với mục tiêu, dữ kiện hoặc ràng buộc hỗ trợ nó. Với quyết định có đánh đổi đáng kể, so sánh các phương án khả thi, gồm cách hiện tại hoặc giải pháp có sẵn khi phù hợp. Với việc đơn giản, không cần tạo thêm phương án chỉ để đủ số lượng.

Ưu tiên cách đủ đáp ứng mục tiêu với chi phí tổng thể hợp lý: công sức ban đầu, độ tin cậy, thời gian, vận hành và bảo trì. Ít thành phần nhất chưa chắc là phương án phù hợp nhất. Không suy từ một số liệu hoặc một đặc điểm như quy mô nhóm sang kết luận chắc chắn về công nghệ.

Kinh nghiệm và suy luận theo tương tự là điểm bắt đầu hữu ích. Kiểm tra xem mục tiêu, điều kiện và ràng buộc của trường hợp tham khảo có phù hợp không. Không mặc định giải pháp phổ biến là sai, cũng không mặc định phải tự xây lại từ đầu.

### 4. Điều gì có thể chứng minh phương án chưa phù hợp?

Suy luận hợp lý cần được đối chiếu với bằng chứng thích hợp. Chọn cách kiểm chứng tương xứng với bài toán và điều chưa chắc chắn:

- Với bài toán tính toán hoặc logic: kiểm tra tiền đề, phép suy ra, đơn vị và trường hợp biên.
- Với giả thuyết về hành vi thực tế: chọn quan sát, phép đo hoặc thử nghiệm có thể phân biệt các nguyên nhân hay phương án.
- Với lựa chọn phụ thuộc sở thích: đối chiếu tiêu chí người dùng, có thể dùng một lần thử nhỏ nếu hữu ích.

Khi cần thử nghiệm, nêu câu hỏi cần kiểm tra, mốc đối chiếu, điều kiện thử và kết quả nào đủ để chấp nhận hoặc đổi hướng. Dùng dữ liệu và kiểm tra sẵn có nếu đã đủ trả lời; không bắt mọi quyết định nhỏ phải có thử nghiệm mới.

Phân biệt rõ **đã kiểm chứng**, **mới suy luận**, và **đề xuất kiểm chứng**. Nếu chưa có quyền, nguồn lực hoặc dữ liệu để kiểm tra, đưa ra kết luận có điều kiện và bước kiểm tra tiếp theo; không bịa kết quả hoặc coi kế hoạch kiểm tra là bằng chứng. Việc phân tích không tự mở rộng phạm vi hành động được người dùng cho phép.

### 5. Kết luận nào được căn cứ hiện tại hỗ trợ?

Nêu phương án và lý do chính, đánh đổi đáng kể, điều còn chưa chắc chắn và khi nào cần xem xét lại. Nếu thiếu bằng chứng quyết định, ưu tiên bước thu thập thông tin có ích thay vì chọn một giải pháp với sự chắc chắn giả tạo.

## Ví dụ ngắn: học AI (trí tuệ nhân tạo) để làm một ứng dụng

Giả sử mục tiêu là xây ứng dụng nhận diện vật thể trong video và biết cách đánh giá nó. Những điều cần đạt gồm đọc được video, nhận kết quả từ mô hình, đánh giá chất lượng và chạy trong giới hạn phần cứng. “Học hết toán trước”, “tự huấn luyện từ đầu” hay “phải có GPU mạnh” đều là giả định cần kiểm tra theo mục tiêu này.

Một phương án ban đầu là dùng mô hình có sẵn trên video mẫu, xem lỗi rồi học kiến thức cần để giải quyết chúng. Để biết phương án có phù hợp không, cần đánh giá trên dữ liệu đại diện cho nhu cầu sử dụng, theo tiêu chí chất lượng và tốc độ đã xác định. Đây là cách thử đề xuất, chưa phải kết quả chứng minh rằng mô hình đáp ứng yêu cầu.

## Những nhầm lẫn cần tránh

- Hỏi “tại sao?” liên tục có thể giúp tìm giả thuyết; câu trả lời vẫn cần căn cứ. Một câu chuyện hợp lý chưa xác nhận được nguyên nhân.
- Tách vấn đề thành nhiều phần chưa đủ: cần dùng những phần có căn cứ để xây dựng và kiểm tra cách giải.
- Thách thức giả định không đồng nghĩa bác bỏ chuyên môn hoặc bỏ qua ràng buộc thực tế.
- Một ví dụ thành công không bảo đảm áp dụng được ở hoàn cảnh khác; một phép thử cục bộ không chứng minh toàn bộ hệ thống đã đạt mục tiêu.

## Tài liệu đọc khi phù hợp

- [Ví dụ kỹ thuật phần mềm](references/software-examples.md): phân tích hiệu năng và quyết định dùng bộ nhớ đệm.
- [Ví dụ đánh giá kiến trúc](examples/architecture-review.md): phân biệt dữ kiện giả định, suy luận và kế hoạch kiểm chứng khi cân nhắc chia hệ thống thành dịch vụ.
- [Phân rã chi phí và giới hạn của ví dụ nổi tiếng](references/elon-musk-examples.md): tránh suy từ giá nguyên liệu sang chi phí sản phẩm hoặc dùng giai thoại như bằng chứng. Giữ tên tệp để các liên kết cũ tiếp tục hoạt động.
