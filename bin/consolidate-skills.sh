#!/usr/bin/env bash
# consolidate-skills.sh — gom skill của mọi coding agent về một hub duy nhất.
#
#   consolidate-skills.sh            # chỉ kiểm kê (dry run)
#   consolidate-skills.sh --apply    # gom về hub + thay bằng symlink
#
# Biến môi trường:
#   SKILLS_HUB    thư mục hub (mặc định ~/.agents/skills — cũng là nơi `npx skills` lưu)
#   MANAGED_ROOT  symlink trỏ vào đây coi như đã gom (mặc định thư mục cha của hub)
#   PER_HOST      skill cố ý khác nhau theo từng agent, không gom (mặc định "gstack graphify connect-chrome")
#   EXTRA_DIRS    thêm thư mục, dạng "tên:đường_dẫn tên2:đường_dẫn2"
#
# STATUS:
#   new       skill thật, hub chưa có     -> copy vào hub, thay bằng symlink
#   dup       giống hệt bản trong hub     -> thay bằng symlink
#   CONFLICT  cùng tên, khác nội dung     -> copy vào backup/conflicts, KHÔNG link, bạn tự chọn
#   linked    đã trỏ vào hub/MANAGED_ROOT -> bỏ qua
#   per-host  nằm trong PER_HOST          -> bỏ qua
#   ext-link  symlink trỏ chỗ khác        -> bỏ qua
set -euo pipefail

HUB="${SKILLS_HUB:-$HOME/.agents/skills}"
HUB="$(readlink -f "$HUB" 2>/dev/null || echo "$HUB")"
MANAGED_ROOT="$(readlink -f "${MANAGED_ROOT:-$(dirname "$HUB")}")"
PER_HOST=" ${PER_HOST:-gstack graphify connect-chrome} "
APPLY=0
[[ "${1:-}" == "--apply" ]] && APPLY=1
BACKUP="$HOME/skills-backup-$(date +%Y%m%d-%H%M%S)"

AGENTS=(
  "agents:$HOME/.agents/skills"
  "claude:$HOME/.claude/skills"
  "codex:$HOME/.codex/skills"
  "cursor:$HOME/.cursor/skills"
  "gemini:$HOME/.gemini/skills"
  "antigravity:$HOME/.gemini/antigravity/skills"
  "opencode:$HOME/.config/opencode/skills"
  "agents-config:$HOME/.config/agents/skills"
  "copilot:$HOME/.copilot/skills"
  "windsurf:$HOME/.codeium/windsurf/skills"
  "kiro:$HOME/.kiro/skills"
  "qwen:$HOME/.qwen/skills"
  "factory:$HOME/.factory/skills"
  "hermes:$HOME/.hermes/skills"
  "pi:$HOME/.pi/agent/skills"
)
for extra in ${EXTRA_DIRS:-}; do AGENTS+=("$extra"); done

FIND_EXCLUDES=( ! -path './.git/*' ! -path '*/node_modules/*' ! -path '*/.venv/*'
                ! -path '*/__pycache__/*' ! -name '.DS_Store' )

# Hash nội dung một skill (chỉ file thật, bỏ qua .git, node_modules, venv, cache).
skill_hash() {
  (cd "$1" && find . -type f "${FIND_EXCLUDES[@]}" -print0 \
    | LC_ALL=C sort -z | xargs -0 -r sha256sum) | sha256sum | cut -c1-16
}

# Thư mục chỉ chứa symlink trỏ vào MANAGED_ROOT (kiểu gstack tạo ra) = đã gom.
is_link_shell() {
  [[ -z "$(cd "$1" && find . -type f "${FIND_EXCLUDES[@]}" -print -quit)" ]] || return 1
  local l
  while IFS= read -r -d '' l; do
    [[ "$(readlink -f "$l")" == "$MANAGED_ROOT"/* ]] || return 1
  done < <(find "$1" -type l -print0)
}

declare -A HUB_HASH
n_new=0 n_dup=0 n_conf=0 n_linked=0 n_ext=0 n_host=0

row() { printf '%-14s %-38s %-10s %s\n' "$@"; }
row AGENT SKILL STATUS NOTE
row ----- ----- ------ ----

for entry in "${AGENTS[@]}"; do
  agent="${entry%%:*}"; dir="${entry#*:}"
  [[ -d "$dir" ]] || continue
  [[ "$(readlink -f "$dir")" == "$HUB" ]] && continue   # chính là hub
  if [[ -L "$dir" ]]; then
    row "$agent" "(cả thư mục)" dir-link "-> $(readlink -f "$dir")"
    continue
  fi
  for path in "$dir"/*; do
    [[ -e "$path" || -L "$path" ]] || continue
    name="$(basename "$path")"

    if [[ -L "$path" ]]; then
      target="$(readlink -f "$path" || true)"
      if [[ -n "$target" && "$target" == "$MANAGED_ROOT"/* ]]; then
        n_linked=$((n_linked+1))
      else
        row "$agent" "$name" ext-link "-> ${target:-<hỏng>}"
        n_ext=$((n_ext+1))
      fi
      continue
    fi

    [[ -d "$path" ]] || continue
    if [[ "$PER_HOST" == *" $name "* ]]; then
      row "$agent" "$name" per-host ""; n_host=$((n_host+1)); continue
    fi
    if is_link_shell "$path"; then
      n_linked=$((n_linked+1)); continue
    fi
    [[ -f "$path/SKILL.md" ]] || continue

    h="$(skill_hash "$path")"
    dest="$HUB/$name"
    # Hub đang là symlink trỏ ngược về chính thư mục này: thay bằng bản thật,
    # nếu không bước symlink bên dưới sẽ tạo vòng lặp.
    if [[ -L "$dest" && "$(readlink -f "$dest")" == "$(readlink -f "$path")" ]]; then
      row "$agent" "$name" hub-back "hub trỏ ngược về đây -> chuyển bản thật vào hub"
      [[ $APPLY -eq 1 ]] && rm "$dest" && cp -a "$path" "$dest"
    fi
    if [[ -z "${HUB_HASH[$name]:-}" && -d "$dest" ]]; then
      HUB_HASH[$name]="$(skill_hash "$dest")"
    fi

    if [[ -z "${HUB_HASH[$name]:-}" ]]; then
      status=new; n_new=$((n_new+1)); HUB_HASH[$name]="$h"
    elif [[ "${HUB_HASH[$name]}" == "$h" ]]; then
      status=dup; n_dup=$((n_dup+1))
    else
      status=CONFLICT; n_conf=$((n_conf+1))
    fi
    row "$agent" "$name" "$status" "$h"

    [[ $APPLY -eq 1 ]] || continue
    case "$status" in
      new)
        mkdir -p "$HUB"
        [[ -e "$dest" ]] || cp -a "$path" "$dest"
        ;&
      dup)
        mkdir -p "$BACKUP/$agent"
        mv "$path" "$BACKUP/$agent/$name"
        ln -s "$dest" "$path"
        ;;
      CONFLICT)
        # Không để bản xung đột trong hub: vài agent đọc thẳng hub và sẽ thấy skill trùng.
        mkdir -p "$BACKUP/conflicts"
        cp -a "$path" "$BACKUP/conflicts/${name}__$agent"
        ;;
    esac
  done
done

echo
echo "Tổng: new=$n_new dup=$n_dup CONFLICT=$n_conf linked=$n_linked per-host=$n_host ext-link=$n_ext"
echo "Hub: $HUB"
if [[ $APPLY -eq 1 ]]; then
  [[ -d "$BACKUP" ]] && echo "Bản gốc đã chuyển vào: $BACKUP"
  [[ $n_conf -gt 0 ]] && echo "Có CONFLICT: xem $BACKUP/conflicts rồi chọn bản giữ lại."
else
  echo "(Dry run — chạy lại với --apply để thực hiện.)"
fi
exit 0
