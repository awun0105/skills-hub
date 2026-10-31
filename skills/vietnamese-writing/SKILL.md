---
name: vietnamese-writing
description: Viết hoặc biên tập văn bản tiếng Việt rõ ràng, mạch lạc, dễ hiểu, tự nhiên, văn phong đầy đủ và không dùng đại từ nhân xưng (tôi, bạn, chúng ta, mình…). Dùng khi viết hay sửa README, tài liệu, hướng dẫn, mô tả sản phẩm, giao diện, thông báo, commit message hoặc bất kỳ văn bản tiếng Việt nào; khi người dùng yêu cầu tiếng Việt "tự nhiên", "dễ hiểu", "không giống văn dịch", hoặc "không xưng hô".
---

# Viết tiếng Việt rõ ràng, tự nhiên, không xưng hô

Mục tiêu: người đọc hiểu ngay ở lần đọc đầu, câu chữ nghe như người Việt viết chứ không như bản dịch máy, văn phong đầy đủ và lịch sự, không có đại từ nhân xưng.

Áp dụng cho mọi văn bản tiếng Việt: README, tài liệu kỹ thuật, hướng dẫn cài đặt, chuỗi giao diện, thông báo lỗi, mô tả sản phẩm, email, commit message.

## 1. Không dùng đại từ nhân xưng

**Không dùng:** tôi, ta, chúng tôi, chúng ta, chúng mình, mình, bạn, các bạn, cậu, anh, chị, em, quý vị, quý khách, họ, nó, ai đó (khi dùng để xưng hô).

Văn bản hướng dẫn tiếng Việt vẫn rất tự nhiên khi bỏ chủ ngữ, nhờ các cách sau:

| Cách | Trước | Sau |
|---|---|---|
| Câu mệnh lệnh, bỏ chủ ngữ | Bạn chạy lệnh sau để cài đặt. | Chạy lệnh sau để cài đặt. |
| "Cần / nên / có thể" đứng đầu câu | Bạn cần cài Node.js 18. | Cần cài Node.js 18 trở lên. |
| Lấy sự vật làm chủ ngữ | Chúng tôi lưu dữ liệu trong Redis. | Dữ liệu được lưu trong Redis. → Redis lưu toàn bộ dữ liệu phiên. |
| "Để…, …" thay cho "nếu bạn muốn" | Nếu bạn muốn xuất PDF, hãy bấm X. | Để xuất PDF, bấm `X`. |
| "Muốn… thì…" | Nếu bạn muốn đổi màu thì sửa file theme. | Muốn đổi màu thì sửa file theme. |
| "Khi…" | Khi bạn mở trang, hệ thống sẽ tải dữ liệu. | Khi trang mở, dữ liệu được tải về. → Trang tải dữ liệu ngay khi mở. |
| Danh từ chỉ vai trò (dùng có chừng mực) | Họ có thể xem ghi chú. | Người xem có thể đọc ghi chú. |
| "Hãy / vui lòng" (lịch sự, không xưng hô) | Bạn hãy kiểm tra lại đường dẫn. | Hãy kiểm tra lại đường dẫn. |

Lưu ý:
- "Người dùng", "người đọc", "người trình bày", "quản trị viên" là danh từ, được phép dùng, nhưng không lạm dụng: ưu tiên câu mệnh lệnh và lấy sự vật làm chủ ngữ.
- "Được" dùng khi cần, không biến mọi câu thành câu bị động. Câu có chủ ngữ là sự vật cụ thể thường rõ hơn: "Script tạo thư mục `dist/`" tốt hơn "Thư mục `dist/` được tạo bởi script".
- "Mình" trong nghĩa "bản thân" (tự mình, của riêng mình) cũng tránh; viết "tự", "riêng".

## 2. Câu rõ ràng

- **Mỗi câu một ý.** Câu dài quá 30 chữ thì tách. Câu nào phải đọc hai lần mới hiểu thì viết lại.
- **Đủ thành phần.** Câu có vị ngữ rõ ràng, không cụt lủn kiểu ghi chú ("Cài xong. Chạy."). Gạch đầu dòng có thể là cụm từ, nhưng cả danh sách phải cùng một kiểu: hoặc toàn cụm từ, hoặc toàn câu hoàn chỉnh.
- **Ý chính đặt trước.** Điều người đọc cần làm hoặc cần biết đứng đầu câu, điều kiện và giải thích đứng sau. Ví dụ: "Bấm `E` để sửa trực tiếp trên slide." thay cho "Trong trường hợp có nhu cầu chỉnh sửa trực tiếp trên slide thì có thể sử dụng phím `E`."
- **Cụ thể thay vì chung chung.** "Xuất PDF mất khoảng 10 giây cho 20 slide" thay cho "Quá trình xuất diễn ra nhanh chóng."
- **Từ nối cho mạch lạc** giữa các câu và đoạn: trước hết, sau đó, tiếp theo, cuối cùng, vì vậy, do đó, ngoài ra, tuy nhiên, ví dụ, nói cách khác. Mỗi đoạn mở bằng câu chủ đề, các câu sau triển khai câu đó.

## 3. Tự nhiên, không giống văn dịch

Văn dịch từng chữ từ tiếng Anh là nguyên nhân lớn nhất khiến tiếng Việt khó đọc. Các mẫu cần tránh:

| Văn dịch | Viết tự nhiên |
|---|---|
| Thực hiện việc cài đặt / tiến hành cài đặt | Cài đặt |
| Được thiết kế để giúp người dùng quản lý… | Giúp quản lý… |
| Cung cấp khả năng xuất file PDF | Xuất được file PDF |
| Mang lại trải nghiệm liền mạch | (nói rõ lợi ích cụ thể, hoặc bỏ) |
| Đóng vai trò như một cầu nối giữa A và B | Nối A với B |
| Sự hỗ trợ của nhiều ngôn ngữ | Hỗ trợ nhiều ngôn ngữ |
| Việc sử dụng cache sẽ giúp cho việc tải trang nhanh hơn | Cache giúp trang tải nhanh hơn |
| Một trong những tính năng quan trọng nhất là… | Tính năng quan trọng nhất là… |
| Nó cho phép bạn… (It allows you to…) | Cho phép… / Có thể… |
| Hãy chắc chắn rằng… (Make sure that…) | Kiểm tra rằng… / Nhớ… |
| Ở trong / ở bên trong thư mục | Trong thư mục |
| Có khả năng / có thể có khả năng | Có thể |
| Tối ưu hóa hiệu suất một cách đáng kể | Chạy nhanh hơn rõ rệt (kèm con số nếu có) |

Quy tắc chung:
- Bớt các hư từ thừa: "việc", "sự", "của", "các", "những", "một cách", "đối với", "trong việc". Đọc lại câu sau khi bỏ chúng; nếu nghĩa không đổi thì bỏ hẳn.
- Bớt động từ rỗng: "thực hiện", "tiến hành", "tiến hành thực hiện", "đưa ra". Dùng thẳng động từ chính.
- Không dùng tính từ quảng cáo rỗng: mạnh mẽ, vượt trội, đột phá, tối ưu, liền mạch, toàn diện, chuyên nghiệp, hiện đại. Thay bằng sự thật cụ thể hoặc bỏ.
- Trật tự từ tiếng Việt: định ngữ đứng sau danh từ ("tệp cấu hình mẫu", không phải "mẫu cấu hình tệp").

## 4. Từ ngữ và thuật ngữ

- **Ưu tiên từ thông dụng, dễ hiểu.** "Tệp" hay "file" đều được, nhưng chọn một và dùng thống nhất trong cả văn bản. Tương tự: "thư mục" / "folder", "kho mã" / "repository".
- **Giữ thuật ngữ kỹ thuật tiếng Anh khi người trong nghề quen dùng** (commit, branch, pull request, deploy, API, framework, cache, build). Không dịch gượng ("kéo yêu cầu" cho pull request). Khi một thuật ngữ có thể lạ với người đọc, giải thích ở lần xuất hiện đầu: "deploy (đưa lên mạng để có link chia sẻ)".
- **Tên riêng, lệnh, đường dẫn, tên biến** giữ nguyên và đặt trong `code`.
- **Không chêm tiếng Anh tùy tiện** khi đã có từ tiếng Việt thông dụng: "tính năng" chứ không "feature", "cài đặt" chứ không "setup" (trừ khi là tên lệnh hay tên mục).
- **Không viết tắt kiểu chat:** k, ko, đc, j, ntn, vs, bt. Viết đầy đủ: không, được, gì, như thế nào, với, bình thường.

## 5. Chính tả và trình bày

- **Viết hoa:** chỉ viết hoa chữ cái đầu của tiêu đề và tên riêng: "Hướng dẫn cài đặt", không phải "Hướng Dẫn Cài Đặt".
- **Dấu thanh và i/y:** thống nhất một kiểu trong cả văn bản (ví dụ "hóa, tùy, thủy" hoặc "hoá, tuỳ, thuỷ"). Khi sửa tài liệu có sẵn, theo kiểu tài liệu đang dùng.
- **Dấu câu:** không có khoảng trắng trước dấu chấm, phẩy, hai chấm, chấm hỏi; có một khoảng trắng sau. Dấu ngoặc kép thống nhất một kiểu ("…" hoặc “…”).
- **Số và đơn vị:** dùng chữ số cho số đo và số lượng kỹ thuật ("3 bước", "16 GB", "Node.js 18"); có khoảng trắng giữa số và đơn vị ("25 MB").
- **In đậm** chỉ cho điều thật sự quan trọng hoặc tên mục trong danh sách định nghĩa; không in đậm cả đoạn.
- **Không dùng emoji, icon** trong tài liệu, trừ khi tài liệu gốc đã dùng.
- **Tiêu đề ngắn, nói rõ nội dung:** "Cài đặt", "Xuất file và chia sẻ", "Repository này chứa gì". Tránh tiêu đề mơ hồ ("Có gì trong này", "Thông tin khác") và tiêu đề kiểu dịch ("Cân nhắc bảo mật" → "Bảo mật").

## 6. Văn phong đầy đủ

"Đầy đủ" nghĩa là lịch sự, trọn vẹn, không suồng sã, nhưng cũng không khô cứng như văn bản hành chính.

- Không dùng khẩu ngữ: "xịn", "ngon", "phê", "cực kỳ luôn", "nha", "nhé", "á", "đó".
- Không dùng lối hành chính nặng nề: "căn cứ vào", "nhằm mục đích", "trên cơ sở", "kính đề nghị".
- Câu cảm thán và dấu chấm than: hạn chế, gần như không dùng trong tài liệu.
- Giọng trung tính, khẳng định: "Lệnh này sẽ xóa thư mục `dist/`." thay cho "Lệnh này có lẽ sẽ xóa thư mục `dist/`." Chỉ dùng từ rào đón khi thật sự không chắc.

## 7. Quy trình viết và tự kiểm tra

1. **Xác định người đọc và việc người đọc cần làm** (cài đặt? hiểu kiến trúc? sửa lỗi?). Mỗi đoạn phục vụ việc đó.
2. **Viết nháp** theo các quy tắc trên.
3. **Dò đại từ nhân xưng bằng script:**
   ```bash
   python3 ~/.agents/skills/vietnamese-writing/check_pronouns.py README.md docs/
   ```
   Script in từng dòng có đại từ (bỏ qua khối code và code inline). Xem từng kết quả: một số từ có nghĩa khác (ví dụ "họ tên", "anh hùng" đã được loại trừ, nhưng vẫn có thể còn trường hợp hợp lệ khác) — sửa những chỗ đúng là xưng hô.
4. **Đọc lại toàn bộ như người đọc lần đầu**, hỏi với từng câu:
   - Câu này có hiểu được ngay không?
   - Có thể nói ngắn hơn mà không mất ý không?
   - Có nghe như văn dịch không (xem bảng mục 3)?
   - Thuật ngữ có thống nhất từ đầu đến cuối không?
5. **Kiểm tra trình bày:** tiêu đề viết hoa đúng, dấu câu, thống nhất i/y, khối code và đường dẫn đặt trong `code`.

## Ví dụ hoàn chỉnh

Trước:

> Đây là một công cụ mạnh mẽ được thiết kế để giúp bạn có thể thực hiện việc tạo ra các bài thuyết trình một cách nhanh chóng. Chúng tôi cung cấp khả năng xuất ra file PDF. Nếu bạn muốn cài đặt thì bạn cần phải có Node.js.

Sau:

> Công cụ tạo bài thuyết trình bằng HTML: chọn mẫu, viết nội dung, mở bằng trình duyệt là trình chiếu được. Bài thuyết trình xuất được ra PDF và PowerPoint. Để cài đặt, cần Node.js 18 trở lên.
