#!/usr/bin/env bash
# install.sh — cài skills-hub lên một máy (máy mới, hoặc máy của người khác).
#
#   git clone https://github.com/awun0105/skills-hub.git ~/.agents
#   ~/.agents/bin/install.sh            # cài skill + link cho các agent
#   ~/.agents/bin/install.sh --sync     # thêm timer tự gom/commit/push mỗi ngày (chỉ khi bạn có quyền push)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd -P)"
cd "$ROOT"

if [[ "$ROOT" != "$(readlink -f "$HOME/.agents")" ]]; then
  echo "Cảnh báo: hub đang ở $ROOT, không phải ~/.agents." >&2
  echo "Codex, Cursor, Gemini, Antigravity, OpenCode… chỉ tự đọc ~/.agents/skills." >&2
fi

echo "== 1. Clone các repo gốc (repos.lock)"
bin/repos-lock.sh restore

echo "== 2. Cài lại skill từ .skill-lock.json (npx skills)"
if command -v npx >/dev/null; then
  python3 -I - "$ROOT/.skill-lock.json" <<'PY' | while read -r name source; do
import json, sys
for name, s in json.load(open(sys.argv[1]))["skills"].items():
    print(name, s["source"])
PY
    if [[ -d "skills/$name" ]]; then echo "có sẵn: $name"; continue; fi
    npx -y skills add "$source" --skill "$name" -g -y </dev/null >/dev/null 2>&1 \
      && echo "đã cài: $name" || echo "LỖI khi cài $name từ $source" >&2
  done
else
  echo "Không có npx (Node.js) — bỏ qua bước này." >&2
fi

echo "== 3. Link skill cho các agent không tự đọc ~/.agents/skills"
# Codex, Cursor, Gemini CLI, Antigravity, OpenCode… đọc thẳng ~/.agents/skills nên không cần link.
TARGETS=()
[[ -d "$HOME/.claude" ]] && TARGETS+=("$HOME/.claude/skills")
[[ -d "$HOME/.codeium/windsurf" ]] && TARGETS+=("$HOME/.codeium/windsurf/skills")
for t in "${TARGETS[@]}"; do
  mkdir -p "$t"
  n=0
  for s in "$ROOT"/skills/*; do
    [[ -f "$s/SKILL.md" ]] || continue
    name="$(basename "$s")"
    [[ -e "$t/$name" || -L "$t/$name" ]] && continue
    ln -s "$s" "$t/$name"; n=$((n+1))
  done
  echo "$t: thêm $n link"
done
[[ ${#TARGETS[@]} -eq 0 ]] && echo "Không thấy ~/.claude hay Windsurf — bỏ qua."

if [[ "${1:-}" == "--sync" ]]; then
  echo "== 4. Bật timer tự đồng bộ"
  mkdir -p "$HOME/.config/systemd/user"
  cp systemd/skills-hub-sync.service systemd/skills-hub-sync.timer "$HOME/.config/systemd/user/"
  systemctl --user daemon-reload
  systemctl --user enable --now skills-hub-sync.timer
fi

cat <<'EOF'

Xong. Khởi động lại các agent để chúng nhận skill mới.

Các skill sau KHÔNG nằm trong repo vì do app/tool tự cài. Cài app tương ứng nếu bạn cần:
  orca-cli, orca-linear, orca-per-workspace-env   ← app Orca
  hf-cli                                          ← Hugging Face CLI
  colab-operator                                  ← Colab MCP
  use-railway                                     ← Railway CLI
  computer-use, orchestration, reverse-engineer-anything
  _gstack-command và skill gstack cho Claude      ← chạy ./setup trong repos/gstack
  chrome-devtools*, graphify (Gemini)             ← extension của Gemini CLI
EOF
