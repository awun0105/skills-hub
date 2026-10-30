# Các thao tác tạo ý tưởng

Chọn thao tác dựa vào điều còn thiếu, không thực hiện hết như danh sách bắt buộc. Khung này tổng hợp các cách làm có thể thực hành; không hứa tạo đột phá hoặc một lời giải tối ưu.

## Làm rõ khái niệm bằng cách đo

Viết điều người dùng thực sự muốn, quan sát dùng để đánh giá và một trường hợp mà chỉ số có thể đánh lừa. Ví dụ, ảnh tổng hợp trông giống ảnh chụp chưa đủ để kết luận kích thước hay hình học va chạm đã đúng.

Nếu đại lượng chưa đo trực tiếp được, chỉ ra đại lượng thay thế và giới hạn của nó. Không loại bỏ một mục tiêu có ý nghĩa chỉ vì khó đo; có thể cần nhiều phép đánh giá hoặc phản hồi định tính.

**Sản phẩm:** định nghĩa đủ rõ để người khác biết cần quan sát gì, cùng phạm vi mà phép đo hỗ trợ.

## Giữ chức năng cốt lõi, thay cơ chế thực hiện

Nêu tác dụng cần đạt trước khi tối ưu một bộ phận cụ thể. Hỏi bộ phận đó đang làm những việc gì, vì sao nó tồn tại và yêu cầu nào sẽ mất nếu bỏ nó. Tìm cách thực hiện khác khi chức năng vẫn cần; không đồng nhất “bỏ thành phần” với “bỏ chức năng”. Kiểm tra cả chức năng phụ như đồng bộ, xử lý lỗi, độ bền hoặc giao tiếp với phần còn lại nếu chúng liên quan.

Ví dụ giả định, một bước tính toán đắt có thể được cải thiện bằng cách chạy nhanh hơn, chỉ chạy khi đầu vào thay đổi hoặc dùng kết quả đã tính. Hai cách sau chỉ hợp lệ khi nhận biết được điều kiện thay đổi và vẫn đáp ứng yêu cầu về tính đúng, độ mới và nguồn lực. Đừng chọn cơ chế thay thế chỉ vì nó ít thành phần hơn.

**Sản phẩm:** chức năng cần giữ, cơ chế thay thế, điều kiện áp dụng và phép kiểm tra xem yêu cầu có còn được đáp ứng không. Đi vào chi tiết đến mức đủ phân biệt phương án, không đợi một thiết kế hoàn hảo trong đầu.

## Dựng thế giới nhỏ và thí nghiệm tưởng tượng

Chọn một hiện tượng, liệt kê thành phần và quy tắc tương tác. Bỏ yếu tố gây nhiễu để tách cơ chế, nhưng giữ yếu tố làm hiện tượng có thể xuất hiện. Dự đoán trước khi xem kết quả.

Thử những câu hỏi phù hợp:

- Nếu đầu vào hoàn hảo, sai số nào vẫn tồn tại?
- Nếu có vô hạn thời gian tính toán, dữ liệu có phân biệt được các đáp án không?
- Hai thế giới khác nhau có thể cho cùng quan sát nhưng đòi hỏi đáp án khác nhau không?
- Trường hợp nhỏ nhất làm lời khẳng định thất bại là gì?
- Nếu thay một điều kiện, bước suy luận nào không còn hợp lệ?

“Vô hạn thời gian” là công cụ phân tích thông tin, không phải giả định triển khai khả thi. Thí nghiệm tưởng tượng đưa ra hệ quả trong mô hình đã nêu; khi cần hiểu thực tế, kiểm tra lại quy tắc và các yếu tố đã bỏ qua.

**Sản phẩm:** kết luận có điều kiện, phản ví dụ hoặc một câu hỏi thực nghiệm cụ thể. Không kết luận nguyên nhân duy nhất chỉ vì đã dựng được một cơ chế gây lỗi.

## Mô phỏng cơ chế theo từng quan hệ

Theo dõi dữ liệu, vật chất, tín hiệu hoặc quyết định qua các thành phần. Với mỗi bước, hỏi đầu vào nào được nhận, phép biến đổi nào xảy ra, thông tin nào mất đi và hệ quả nào chuyển sang bước tiếp.

Với `mental simulation (mô phỏng trong tư duy)`, ghi trạng thái ban đầu, sự kiện làm thay đổi trạng thái và quy tắc chuyển đổi. Chọn những tình huống liên quan: khởi động, hoạt động ổn định, đổi đầu vào, dừng, khôi phục hoặc lỗi. Hỏi trạng thái nào còn được giữ, thay đổi nào lan sang bộ phận khác và thuộc tính nào phải tiếp tục đúng. Không biến mọi bài toán nhỏ thành một cuộc đánh giá toàn bộ hệ thống.

Dùng giấy, sơ đồ, phương trình hoặc mã giả; không cần có khả năng hình dung sống động. Nếu không biết một bộ phận tuân theo quy tắc nào, học, tính hoặc đo nó thay vì điền một câu chuyện hợp lý vào khoảng trống. Khi có vòng phản hồi hoặc tác vụ đồng thời, giữ chúng trong mô hình nếu chúng quyết định hành vi. Một mẫu thử nhỏ có thể giúp xây dựng hiểu biết, không chỉ dùng để xác nhận thiết kế đã hoàn tất.

**Sản phẩm:** mô hình đủ rõ để dự đoán tác động của một thay đổi và chỉ ra điều có thể làm dự đoán sai. Ghi nhận cảm giác “đã thấy lời giải” như ý tưởng cần diễn đạt và kiểm tra; độ sống động hoặc sự chắc chắn chủ quan không thay thế bằng chứng.

## Đổi biểu diễn

Thử đổi biến, chọn đại lượng tương đối, dùng đồ thị thay danh sách, biểu diễn phân bố hay tập ứng viên thay một đáp án, hoặc tách quá trình thành trạng thái và chuyển trạng thái. Chọn cách đổi dựa trên quan hệ cần thể hiện.

Kiểm tra biểu diễn mới có giữ đủ thông tin và ràng buộc của bài toán gốc không. Nếu chỉ gần đúng hoặc đổi mục tiêu, ghi rõ phần mất đi. Phân biệt đổi mô tả cùng một dữ liệu với thu thêm dữ liệu: đổi tọa độ không tự làm lộ mặt vật thể đang bị che.

**Sản phẩm:** ánh xạ giữa hai biểu diễn và một phép suy luận hoặc tính toán mới được làm thuận tiện hơn.

## Đối xứng, bất biến và phép biến đổi

Chọn một phép biến đổi cụ thể: đổi nhãn, đổi đơn vị, đổi hệ tọa độ hoặc thay thứ tự khi thứ tự không mang ý nghĩa. Xác định điều gì phải giữ nguyên và điều gì phải biến đổi tương ứng. Chỉ kỳ vọng quan hệ đó khi các điều kiện của bài toán cho phép.

Một đáp án đối xứng có thể là phỏng đoán hữu ích; đối xứng tự nó không chứng minh cực trị. Một kết quả thay đổi bất thường dưới phép đổi đơn vị có thể gợi lỗi, nhưng cần kiểm tra lại các đầu vào và tham số có được đổi nhất quán không.

**Sản phẩm:** thuộc tính cần giữ, kiểm tra tính nhất quán hoặc biến mới giúp lập luận tiến lên.

## Mượn cấu trúc và kết hợp cơ chế

Với một bài toán tham khảo, lập ánh xạ đối tượng, quan hệ, ràng buộc và mục tiêu sang bài toán hiện tại. Nêu ít nhất điểm khác biệt có thể làm phép tương tự không còn đúng. Mượn cơ chế, không mượn kết luận thành công.

Nếu chưa có bài toán tham khảo hữu ích, phân rã chức năng cần thực hiện, tìm các cách khác nhau để thực hiện từng chức năng, rồi kết hợp những cách tương thích. Có thể đổi thứ tự xử lý, đưa tính toán sang thời điểm khác hoặc dùng phản hồi để điều chỉnh. Mỗi tổ hợp cần chỉ rõ tương tác giữa các phần, không chỉ là danh sách công nghệ.

Ví dụ, chọn câu hỏi để phân biệt đáp án và chọn góc camera để phân biệt hình dạng có cấu trúc chung. Nhưng di chuyển camera có chi phí, giới hạn vị trí và nhiễu quan sát; các yếu tố này phải tham gia lựa chọn.

**Sản phẩm:** cơ chế mới trong bài toán hiện tại, ánh xạ hỗ trợ nó và điều kiện cần kiểm tra. Chưa đủ căn cứ để tuyên bố đó là thuật toán mới của lĩnh vực.

## Quay lại bài toán sau khi mắc kẹt

Dùng khi đã có chuẩn bị và đang lặp lại cùng một hướng mà chưa tiến thêm. Ghi ngắn mục tiêu, điểm mắc, các cách đã thử và câu hỏi còn mở để có thể quay lại. Trước hết xem phần thiếu là kiến thức, dữ liệu hay một cách biểu diễn khác; không dùng tạm nghỉ thay cho việc tìm thông tin cần thiết.

Với người dùng, `incubation (tạm rời bài toán rồi quay lại)` có thể là một lựa chọn: đổi sang hoạt động nhẹ hoặc đi bộ nếu phù hợp, rồi quay lại với một câu hỏi hay góc nhìn cụ thể. Không ấn định thời lượng như công thức chung, không yêu cầu chờ ý tưởng tự xuất hiện. Tập trung một mình có thể là lựa chọn ở một giai đoạn; vẫn cần đối chiếu nguồn và phản biện khi có ích.

Với AI agent, đổi biểu diễn, dựng phản ví dụ, đọc một nguồn liên quan hoặc thử cơ chế khác trong phạm vi được phép. Không ngủ chờ, giả nhận có tiềm thức hoặc ngừng việc đã được giao để mô phỏng trải nghiệm của con người. Khi không còn bước hữu ích khả thi, báo rõ điều thiếu và bước tiếp theo cần thiết.

Sau khi quay lại, viết phần ý tưởng mới, cơ chế và dự đoán trước khi thử. Nếu không có thay đổi, chọn một bước thu thập thông tin hoặc thu hẹp bài toán; không kéo dài việc nghỉ và đặt câu hỏi như một nghi thức.

**Căn cứ và giới hạn:** [Oppezzo và Schwartz (2014)](https://www.apa.org/pubs/journals/releases/xlm-a0036577.pdf) nghiên cứu đi bộ trong các nhiệm vụ tạo ý tưởng, phép tương tự và tìm đáp án. Kết quả không hỗ trợ việc suy rộng lợi ích sang mọi loại suy luận hoặc bảo đảm giải bài toán khó. [Baird và cộng sự (2012)](https://journals.sagepub.com/doi/10.1177/0956797612446024) báo cáo lợi ích của một nhiệm vụ ít đòi hỏi chú ý trong khoảng tạm ngưng đối với bài tạo công dụng khác thường đã được tiếp cận trước đó; không chứng minh đơn thuần chờ đợi sẽ tạo lời giải hay xác nhận toàn bộ quy trình này.

**Sản phẩm:** một hướng biểu diễn, giả thuyết hoặc bước kiểm tra tiếp theo, cùng ghi nhận điều đã thay đổi trong cách hiểu. Những lời kể về Tesla là nguồn gợi ý thao tác, không phải bảo đảm mô phỏng trong đầu tương đương thiết bị thật.

## Tạo giả thuyết cạnh tranh và phép thử phân biệt

Đề xuất các cơ chế khác nhau có thể tạo cùng hiện tượng, chỉ khi chúng có căn cứ hoặc đáng kiểm tra. Suy ra kết quả mà chúng dự đoán khác nhau. Đừng tạo đủ số lượng bằng những giả thuyết vô nghĩa.

Chọn quan sát hoặc thử nghiệm có thể làm thay đổi đánh giá giữa các giả thuyết. Giữ các yếu tố liên quan nhất quán hoặc ghi nhận khác biệt; đặt tiêu chí trước khi biết kết quả. Kết quả không khớp có thể do giả thuyết, giả định phụ, phép đo hoặc triển khai; xác định phần bị thử thách thay vì bác bỏ tùy tiện.

Nếu các giả thuyết hiện tại cùng dự đoán một kết quả, phép thử đó chưa phân biệt được chúng. Nếu tất cả đều không giải thích được dữ liệu, mở lại tập giả thuyết. Trong hệ thống xác suất hoặc nhiều nhiễu, một lần quan sát thường chỉ thay đổi mức tin cậy thay vì loại trừ tuyệt đối.

**Sản phẩm:** dự đoán phân biệt, cách kiểm tra và quy tắc cập nhật phù hợp với bằng chứng.

Cách đặt các giả thuyết thay thế và phép thử để loại bớt khả năng có liên hệ với đề xuất [Strong Inference của John R. Platt](https://courses.cs.duke.edu/fall04/cps296.2/science_platt.html). Đây là nguồn tham khảo cho cách tổ chức nghiên cứu, không phải bằng chứng rằng mọi bài toán đều giải được theo một quy trình chung.

## Chuyển từ ý tưởng sang hướng thực hiện

Sàng lọc theo yêu cầu bắt buộc, giới hạn thông tin, tính khả thi, giá trị dự kiến và chi phí tìm hiểu tiếp. Không chỉ chọn ý tưởng dễ đo nhất nếu phép đo không phản ánh mục tiêu. Đối chiếu cách hiện tại hoặc giải pháp có sẵn khi chúng là mốc so sánh phù hợp.

Nếu chưa đủ căn cứ để chọn lời giải, có thể chọn bước thu thập thông tin giúp phân biệt các hướng. Kiểm chứng bằng lập luận đối với khẳng định toán học; dùng thử nghiệm phù hợp đối với hiệu quả thực tế; dùng tiêu chí và phản hồi người dùng đối với lựa chọn phụ thuộc sở thích.

**Sản phẩm:** hướng thử ưu tiên cùng lý do, điều chưa biết và điều kiện để tiếp tục, sửa hoặc dừng hướng đó.
