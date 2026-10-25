#!/usr/bin/env bash
# repos-lock.sh — ghi lại / khôi phục các git clone không commit vào hub.
#
#   repos-lock.sh save      # ghi repos.lock (đường dẫn, URL, commit)
#   repos-lock.sh restore   # clone những repo còn thiếu, checkout đúng commit
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOCK="$ROOT/repos.lock"

case "${1:-}" in
  save)
    {
      echo "# path url commit — tạo bởi bin/repos-lock.sh save"
      for g in "$ROOT"/repos/*/.git "$ROOT"/skills/*/.git; do
        [[ -e "$g" ]] || continue
        d="$(dirname "$g")"
        [[ -L "$d" ]] && continue   # symlink tới repo khác, đã ghi ở đó
        printf '%s %s %s\n' "${d#$ROOT/}" \
          "$(git -C "$d" remote get-url origin)" "$(git -C "$d" rev-parse HEAD)"
        [[ -z "$(git -C "$d" status --porcelain)" ]] \
          || echo "Cảnh báo: ${d#$ROOT/} có thay đổi chưa commit, không được lưu." >&2
      done
    } > "$LOCK"
    echo "Đã ghi $LOCK ($(grep -vc '^#' "$LOCK") repo)."
    ;;
  restore)
    grep -v '^#' "$LOCK" | while read -r path url commit; do
      if [[ -d "$ROOT/$path/.git" ]]; then
        echo "có sẵn: $path"; continue
      fi
      if git clone --quiet "$url" "$ROOT/$path" \
         && git -C "$ROOT/$path" checkout --quiet "$commit"; then
        echo "đã clone: $path @ ${commit:0:7}"
      else
        echo "LỖI: không clone được $path từ $url" >&2
      fi
    done
    ;;
  *)
    sed -n '2,5p' "$0"; exit 1 ;;
esac
