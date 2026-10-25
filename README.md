# skills-hub

Nơi chứa **tất cả skill** của mọi coding agent trên máy: Claude Code, Codex, Antigravity, Gemini CLI, Cursor, OpenCode, Copilot, Windsurf…

Mỗi skill chỉ có **một bản duy nhất** nằm ở đây. Agent nào cũng dùng chung bản đó, nên sửa một chỗ là mọi agent đều thấy.

## Cài đặt (máy mới, hoặc bạn muốn dùng bộ skill này)

Cần có `git`, `python3`, và Node.js (cho `npx`).

```bash
git clone https://github.com/awun0105/skills-hub.git ~/.agents
~/.agents/bin/install.sh
```

Script sẽ làm 3 việc:
1. Clone các repo skill gốc (superpowers, gstack, ECC…) vào `~/.agents/repos/`, đúng commit đã ghi trong `repos.lock`.
2. Cài lại các skill trong `.skill-lock.json` bằng `npx skills`, lấy thẳng từ nguồn.
3. Tạo symlink cho những agent không tự đọc `~/.agents/skills`, cụ thể là Claude Code và Windsurf. Các agent còn lại (Codex, Cursor, Gemini CLI, Antigravity, OpenCode…) đọc thẳng thư mục này nên không cần link.

Cuối cùng script in ra danh sách skill **không có trong repo** vì do app tự cài (xem [bên dưới](#những-gì-không-có-trong-repo)).

> **Nhất định phải clone vào `~/.agents`.** Đó là thư mục mà `npx skills` và nhiều agent tự tìm đến. Nếu bạn đã có sẵn `~/.agents`, hãy đổi tên nó trước (`mv ~/.agents ~/.agents.old`), clone xong thì copy những gì cần giữ sang.

Repo này dùng **đường dẫn tương đối** (`skills/x -> ../repos/...`) và `$HOME`, nên chạy được với mọi tên user.

---

## Cấu trúc

```
~/.agents/
├── skills/        ← HUB: mọi skill (thư mục thật, hoặc symlink vào repos/)
├── repos/         ← các git clone gốc — không commit, ghi trong repos.lock
├── rules/         ← rule dùng chung
├── workflows/     ← workflow / slash command dùng chung
├── bin/
│   ├── install.sh              ← cài lên máy mới
│   ├── consolidate-skills.sh   ← tìm và gom skill nằm rời rạc về hub
│   ├── repos-lock.sh           ← ghi / khôi phục danh sách git clone
│   └── sync-hub.sh             ← gom + commit + push (timer gọi mỗi ngày)
├── systemd/       ← timer cho sync-hub.sh
├── repos.lock     ← danh sách repo: đường dẫn, URL, commit
└── .skill-lock.json  ← file của `npx skills`, đừng sửa tay

~/.claude/skills/<tên>  ──►  ~/.agents/skills/<tên>  ──►  ~/.agents/repos/.../<tên>
```

---

## Việc hằng ngày

### Cài skill mới

```bash
npx skills add <chủ>/<repo> --list                     # xem repo có những skill nào
npx skills add <chủ>/<repo> --skill <tên> -g -y         # cài cho mọi agent trên máy
```

`-g` nghĩa là cài toàn cục, vào `~/.agents/skills`. `-y` nghĩa là tự chọn mọi agent tìm thấy, không hỏi lại. Skill cài theo cách này **không được commit**: chỉ tên và nguồn được ghi vào `.skill-lock.json`, và máy khác sẽ tự cài lại từ nguồn.

### Tự viết skill

Tạo ở `~/.agents/skills/<tên>/SKILL.md`, rồi link sang Claude Code:

```bash
ln -s ~/.agents/skills/<tên> ~/.claude/skills/<tên>
cd ~/.agents && git add skills/<tên> && git commit -m "Add skill <tên>" && git push
```

Nếu bạn nhờ agent tạo skill thì không cần làm tay. File cấu hình chung của từng agent (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`) đã có hướng dẫn để agent tự làm đúng các bước trên.

### Sửa một skill

Sửa thẳng trong `~/.agents/skills/<tên>/`. Mọi agent dùng bản đã sửa ngay.

> ⚠️ Nếu `skills/<tên>` là **symlink vào `repos/`**, tức là skill của người khác, thì phần bạn sửa nằm trong repo gốc, **không** vào git của hub, và có thể bị ghi đè khi repo gốc cập nhật. Muốn giữ bản sửa riêng thì copy ra thành thư mục thật. Lưu ý chỉ public bản sửa nếu license của skill gốc cho phép.
> ```bash
> cd ~/.agents/skills && cp -rL <tên> <tên>.tmp && rm <tên> && mv <tên>.tmp <tên>
> ```

### Kiểm tra có skill nào bị "lạc" không

Đôi khi một công cụ tự cài skill thẳng vào `~/.claude/skills` thay vì vào hub. Để kiểm tra:

```bash
~/.agents/bin/consolidate-skills.sh            # chỉ xem, KHÔNG thay đổi gì
~/.agents/bin/consolidate-skills.sh --apply    # gom về hub
```

| STATUS | Nghĩa | Script làm gì khi `--apply` |
|---|---|---|
| `new` | Skill thật, hub chưa có | Copy vào hub, thay bản gốc bằng symlink |
| `dup` | Giống hệt bản trong hub | Thay bằng symlink |
| `CONFLICT` | Cùng tên nhưng nội dung khác | **Không đụng vào.** Copy sang thư mục backup để bạn tự chọn bản giữ lại |
| `per-host` | Skill cố ý khác nhau theo agent | Bỏ qua |
| `ext-link` | Symlink trỏ ra ngoài hub | Bỏ qua |

Bản gốc **không bao giờ bị xoá**, mà được chuyển vào `~/skills-backup-<ngày-giờ>/`.

### Tự đồng bộ mỗi ngày (chỉ dành cho chủ repo)

```bash
~/.agents/bin/install.sh --sync
```

Lệnh này bật một systemd timer chạy lúc 21:00 và 15 phút sau khi mở máy. Mỗi lần chạy, timer gom skill lạc về hub, cập nhật `repos.lock`, rồi commit và push. Để giữ an toàn cho repo public, timer **không tự phát hành skill thật mới**, vì đó có thể là skill của bên thứ ba. Gặp trường hợp này, nó chỉ ghi `CHƯA PHÁT HÀNH: ...` vào log để bạn tự quyết.

Xem log: `journalctl --user -u skills-hub-sync -n 30`

Đồng bộ tay: `~/.agents/bin/sync-hub.sh`

---

## Những gì không có trong repo

| Loại | Ví dụ | Cách có lại |
|---|---|---|
| Repo skill gốc | superpowers, gstack, ECC, OpenSpec… | `repos.lock`, `install.sh` tự clone |
| Cài qua `npx skills` | archify, architecture-diagram, svg-diagram, supabase | `.skill-lock.json`, `install.sh` tự cài |
| Do app/tool tự cài, không rõ license | orca-*, hf-cli, colab-operator, use-railway, computer-use… | Cài app tương ứng |
| Sinh ra theo máy | `_gstack-command`, các link vào extension của Gemini | Chạy `./setup` của gstack, cài extension |

Những skill này **vẫn có trên máy chủ repo**, chỉ không được phát hành lại. Lý do là repo public sẽ phân phối bản sao nội dung của người khác, và việc đó cần license cho phép.

---

## Những điều cần nhớ

1. **Đừng gộp skill `per-host`.** Hiện có `gstack`, `graphify` và `connect-chrome`. Mỗi agent có một bản riêng là có chủ đích, ví dụ bản Codex gọi `spawn_agent` còn bản Claude gọi Agent tool. Muốn thêm tên vào danh sách này thì đặt biến `PER_HOST`.
2. **Thay đổi chưa commit trong `repos/` không đi theo sang máy khác.** `repos.lock` chỉ ghi commit. Muốn giữ bản sửa thì fork repo đó.
3. **Không commit bí mật.** `.gitignore` đã chặn `.env`, nhưng trước khi push bạn vẫn nên liếc qua `git status`.
4. **Skill chạy với toàn quyền của agent.** Trước khi cài skill lạ, xem điểm đánh giá bảo mật trên `skills.sh/<chủ>/<repo>`.
5. **Skill cấp project** (`.claude/skills/` bên trong một repo dự án) để nguyên ở đó, không gom về hub.

---

## Khi có sự cố

| Triệu chứng | Cách xử lý |
|---|---|
| Agent không thấy skill vừa cài | Khởi động lại agent. Kiểm tra `ls -la ~/.claude/skills/<tên>` có trỏ đúng không |
| Symlink trong `skills/` bị hỏng | Chạy `bin/repos-lock.sh restore` (thiếu repo gốc) hoặc `bin/install.sh` |
| `Too many levels of symbolic links` | Có vòng lặp symlink. Chạy `readlink` trên từng mắt xích, rồi thay một đầu bằng thư mục thật (lấy từ `~/skills-backup-*`) |
| Lỡ `--apply` sai | Bản gốc nằm trong `~/skills-backup-<ngày-giờ>/<agent>/<tên>`. Xoá symlink rồi `mv` bản gốc về |

Tìm symlink hỏng:

```bash
find ~/.agents/skills ~/.claude/skills -maxdepth 1 -xtype l
```

---

## Ghi công

- `skills/first-principles-skill`: từ [awesome-skills/first-principles-skill](https://github.com/awesome-skills/first-principles-skill), license MIT (xem `LICENSE` trong thư mục). Bản ở đây đã được sửa (v0.2.1): thêm từ khoá và quy tắc diễn đạt tiếng Việt.
- Các skill trong `repos/` thuộc về tác giả của từng repo, theo license của repo đó.
