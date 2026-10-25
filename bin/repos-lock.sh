#!/usr/bin/env bash
# repos-lock.sh — ghi lại / khôi phục các git clone không commit vào hub.
#
#   repos-lock.sh save      # ghi repos.lock (đường dẫn, URL, commit)
#   repos-lock.sh restore   # clone những repo còn thiếu, checkout đúng commit, áp overlays/
#
# overlays/<đường dẫn repo>/... chứa file bạn thêm vào repo của người khác (không push được);
# restore chép chúng đè vào repo sau khi clone.
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
        # File chưa commit chỉ đi theo sang máy khác nếu có bản giống hệt trong overlays/.
        git -C "$d" status --porcelain --untracked-files=all | while read -r _ f; do
          cmp -s "$d/$f" "$ROOT/overlays/${d#$ROOT/}/$f" \
            || echo "Cảnh báo: ${d#$ROOT/}/$f chưa commit và không có trong overlays/ — máy khác sẽ thiếu." >&2
        done
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
    # Chép đè file bổ sung (plugin.json, skill thêm…) vào các repo không push được.
    if [[ -d "$ROOT/overlays" ]]; then
      cp -r "$ROOT/overlays/." "$ROOT/"
      echo "đã áp overlays/: $(find "$ROOT/overlays" -type f | wc -l) file"
    fi
    ;;
  *)
    sed -n '2,5p' "$0"; exit 1 ;;
esac
