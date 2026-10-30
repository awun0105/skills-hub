# Ví dụ có lập luận và giới hạn

Các tình huống dưới đây là minh họa, không phải kết quả thực nghiệm hoặc đóng góp nghiên cứu đã xác nhận. Đọc ví dụ phù hợp với loại bài toán, không dùng tất cả làm khuôn cho mọi câu trả lời.

## Chiều sâu chiếc hộp: thiếu thông tin và độ ổn định

**Mô hình:** hộp chữ nhật có chiều rộng, cao, sâu là \(w,h,d>0\); camera chiếu trực giao nhìn thẳng mặt trước; tỉ lệ ảnh đã biết; chỉ dùng đường bao, bỏ bóng đổ, kết cấu và phản xạ. Dữ liệu cho biết \((w,h)\), không phụ thuộc \(d\).

Hai hộp cùng \(w,h\) nhưng khác \(d\) cho cùng đầu vào. Một quy tắc chỉ nhận đầu vào đó không thể bảo đảm xuất đúng chiều sâu cho cả hai. Đổi thuật toán hoặc tăng thời gian tính toán không khôi phục được sự phân biệt đã vắng mặt trong dữ liệu này.

**Ý tưởng từ cơ chế:** tìm phép quan sát khiến chiều sâu ảnh hưởng đến dữ liệu. Nếu được phép đổi góc nhìn quanh trục thẳng đứng, bề rộng đường bao với góc \(0\leq\theta\leq90^\circ\) là:

\[
W(\theta)=w\cos\theta+d\sin\theta.
\]

Ở \(0^\circ\), chỉ đo được \(w\); ở \(90^\circ\), đo được \(d\). Với \(w\) và góc \(\theta>0\) đã biết:

\[
d=\frac{W-w\cos\theta}{\sin\theta}.
\]

Tuy nhiên, nếu chỉ có sai số đo \(\Delta W\), giữ \(w,\theta\) chính xác, thì \(\Delta d=\Delta W/\sin\theta\). Góc nhỏ khiến sai số bị khuếch đại. Có thể xác định trong mô hình lý tưởng chưa bảo đảm ước lượng ổn định. Khi \(w\), góc hoặc tỉ lệ cũng có sai số, cần phân tích thêm chúng.

**Điều kiện bài toán:** nếu chỉ cho phép ảnh ban đầu, ghi nhận bất định hoặc dùng kiến thức bổ sung có căn cứ, đồng thời nêu phụ thuộc vào giả định. Chụp thêm ảnh là phương án mở rộng đầu vào, không phải lời giải đáp ứng nguyên vẹn điều kiện một ảnh.

**Kiểm tra đề xuất:** dựng hộp có kích thước biết trước, dự đoán bề rộng ở các góc rồi đối chiếu phép tính hoặc hình chiếu. Thêm nhiễu có kiểm soát để kiểm tra độ nhạy. Thử này kiểm tra mô hình chiếc hộp; nó chưa chứng minh một góc bổ sung đủ tái dựng vật thể bất kỳ.

Nếu chọn góc từ tập hình dạng ứng viên, không coi việc phân biệt tốt các ứng viên là bảo đảm đúng: hình dạng thật có thể không nằm trong tập ấy. Cần xem lại tập ứng viên khi dữ liệu mới không được giải thích tốt.

## Gán nhãn điểm 3D: sửa cách dùng bằng chứng

**Thuật toán giả định:** chiếu một điểm 3D lên ảnh; nếu tọa độ ảnh nằm trong `mask (vùng ảnh mang nhãn đối tượng)` A thì gán điểm cho A.

**Thế giới nhỏ:** camera chính xác, vật đục, vùng nhãn phần nhìn thấy chính xác. A ở phía trước; một điểm của B ở phía sau trên cùng tia nhìn với bề mặt A. Hai điểm chiếu vào cùng vị trí ảnh mang nhãn A.

Thuật toán gán nhầm điểm B cho A dù đầu vào lý tưởng. Phản ví dụ bác bỏ quy tắc “nằm trong vùng nhãn A thì thuộc A” cho mô hình này. Nó không chứng minh mọi lỗi của hệ thống thực đều do che khuất.

**Thay biểu diễn bằng chứng:** phân biệt điểm nhìn thấy, bị che và ngoài ảnh. Với vùng nhãn A chính xác, điểm bề mặt nhìn thấy nằm trong vùng đó là bằng chứng ủng hộ thuộc A; nhìn thấy nhưng ngoài vùng đó là bằng chứng chống lại. Điểm bị che hoặc ngoài ảnh chưa có bằng chứng trực tiếp từ vùng nhãn này. Không biến “chưa biết” thành phiếu đồng ý hoặc phản đối.

**Dự đoán:** cơ chế xử lý độ nhìn thấy sẽ có lợi rõ hơn ở nhóm bị che so với nhóm không bị che khi giữ các yếu tố khác nhất quán. Giả thuyết thay thế là lợi ích đến từ việc giảm tổng số điểm được gán nhãn, không phải xử lý che khuất đúng.

**Phép thử đề xuất:** so sánh trường hợp có và không có che khuất với vùng nhãn chính xác, rồi đưa nhiễu vào có kiểm soát. Đo cả tỉ lệ gán sai và phần điểm được gán; so sánh thêm một cách từ chối gán có mức bao phủ tương đương nếu cần phân biệt giả thuyết thay thế. Ghi nhận phần chưa biết thay vì chỉ báo độ chính xác trên phần nhỏ đã chọn.

**Giới hạn:** cần xác định độ nhìn thấy từ dữ liệu nào và dữ liệu đó có sẵn trong bài toán gốc không. Nếu phải thêm cảm biến, điều kiện đã thay đổi. Điểm lý tưởng và vật đục không đại diện đầy đủ cho Gaussian có kích thước, độ trong suốt và đóng góp từng phần; phải dựng lại mô hình khi chuyển miền.

## Đổi biến để chứng minh cực trị

**Bài toán:** với \(x,y\) là số thực và \(x+y=10\), tìm giá trị lớn nhất của \(xy\).

Đổi chỗ \(x,y\) giữ điều kiện và mục tiêu, gợi phỏng đoán điểm cân bằng \(x=y=5\). Đối xứng chưa phải chứng minh. Biểu diễn độ lệch bằng \(x=5+t\), \(y=5-t\) tự giữ ràng buộc. Khi đó:

\[
xy=(5+t)(5-t)=25-t^2\leq25.
\]

Dấu bằng đạt tại \(t=0\), nên giá trị lớn nhất là 25. Ý tưởng nằm ở việc dùng một biến đo độ lệch; bước chứng minh là bất đẳng thức đúng với mọi \(t\) thực. Thử vài cặp số có thể gợi quy luật, không thay thế được bước này. Nếu miền biến thay đổi, kiểm tra lại tính hợp lệ và điều kiện đạt dấu bằng.

## Bàn giao công việc chậm: tìm cơ chế trước khi thêm nguồn lực

**Tình huống giả định:** một nhóm muốn giảm thời gian từ lúc tài liệu sẵn sàng đến lúc được duyệt, giữ chất lượng và giờ làm trong giới hạn hiện tại. Có đề xuất bổ sung người duyệt.

**Các cơ chế khả dĩ:** thiếu năng lực xử lý, phải chờ một khung giờ cố định, hoặc hồ sơ thiếu thông tin nên bị trả lại. Chưa có dữ liệu để chọn một cơ chế. Cần phân biệt thời gian chờ, thời gian thực sự xử lý và thời gian sửa lại; không mặc định “chậm” nghĩa là người duyệt làm việc chậm.

**Tạo phương án:** nếu chờ lịch là phần lớn, thử cách thông báo và tiếp nhận sớm hơn; nếu sửa lại là phần lớn, thử làm rõ yêu cầu đầu vào và phản hồi sớm; nếu công việc xử lý vượt khả năng hiện có, xem lại phân bổ nguồn lực hoặc phạm vi. Các hướng thay đổi những cơ chế khác nhau. Không tự điều chỉnh thời hạn hoặc tiêu chuẩn chất lượng đã thống nhất.

**Dự đoán phân biệt:** phản hồi sớm sẽ giảm vòng trả lại nếu thiếu thông tin là nguyên nhân đáng kể; tăng số lần tiếp nhận sẽ giảm thời gian chờ nếu lịch là nguyên nhân. Chọn một lần thử trong phạm vi được phép, so với công việc tương tự và theo dõi cả chất lượng lẫn công sức. Đây là kế hoạch kiểm tra, chưa có kết quả.
