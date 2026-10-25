#!/usr/bin/env bash
# sync-hub.sh — gom skill lạc về hub, cập nhật repos.lock, commit và push.
# Chạy tự động bởi systemd timer skills-hub-sync (xem README); chạy tay cũng được.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
exec 9>"$ROOT/.git/sync-hub.lock"
flock -n 9 || { echo "Đang có một lần sync khác chạy, bỏ qua."; exit 0; }

echo "== $(date '+%F %T') sync-hub"
out="$(bin/consolidate-skills.sh --apply)"
echo "$out" | grep -E ' (new|dup|CONFLICT|hub-back) |^Tổng|^Bản gốc|^Có CONFLICT' || true
bin/repos-lock.sh save

# Skill mới cài qua `npx skills` -> thêm vào khối skill-lock của .gitignore (cài lại từ nguồn).
python3 -I - <<'PY'
import json, re
names = sorted(json.load(open(".skill-lock.json"))["skills"])
gi = open(".gitignore").read()
block = "# BEGIN skill-lock\n" + "".join(f"/skills/{n}/\n" for n in names) + "# END skill-lock"
open(".gitignore", "w").write(re.sub(r"# BEGIN skill-lock\n.*?# END skill-lock", block, gi, flags=re.S))
PY

git add -A
# Repo public: không tự phát hành thư mục skill thật MỚI (có thể là của bên thứ ba).
# Skill của bạn thì agent tự commit theo hướng dẫn, hoặc bạn `git add` tay.
for name in $(git diff --cached --name-only --diff-filter=A -- skills | awk -F/ 'NF>2{print $2}' | sort -u); do
  if [[ -d "skills/$name" && ! -L "skills/$name" ]] && ! git cat-file -e "HEAD:skills/$name" 2>/dev/null; then
    git reset -q -- "skills/$name"
    echo "CHƯA PHÁT HÀNH: skills/$name là skill thật mới — tự 'git add' nếu được phép public, hoặc thêm vào .gitignore."
  fi
done
if git diff --cached --quiet; then
  echo "Không có thay đổi."
else
  added="$(git diff --cached --name-only --diff-filter=A | awk -F/ '$1=="skills"{print $2}' | sort -u | paste -sd, -)"
  git commit -q -m "Auto-sync skills${added:+: $added}"
  echo "Đã commit: $(git log -1 --format='%h %s')"
fi

if [[ -n "$(git log '@{u}..' --oneline 2>/dev/null)" ]]; then
  git push -q && echo "Đã push."
fi

if echo "$out" | grep -q ' CONFLICT '; then
  echo "CẢNH BÁO: có CONFLICT cần xử lý tay." >&2
  exit 2
fi
