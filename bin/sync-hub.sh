#!/usr/bin/env bash
# Consolidate skills and publish only managed metadata and tracked skill changes.
# --dry-run previews consolidation and candidate paths without writing to the hub.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
case "${1:-}" in
  '') DRY_RUN=0 ;;
  --dry-run) DRY_RUN=1 ;;
  *) echo 'Usage: bin/sync-hub.sh [--dry-run]' >&2; exit 2 ;;
esac

# Never include someone else's staged work or publish existing local commits.
if ! git diff --cached --quiet; then
  echo 'STOP: index contains staged changes; commit or unstage them before sync.' >&2
  exit 1
fi
upstream="$(git rev-parse --abbrev-ref '@{u}')"
if [[ "$(git rev-list --count "$upstream..HEAD")" != 0 ]]; then
  echo 'STOP: branch has unpushed commits; review and push them before sync.' >&2
  exit 1
fi

if [[ "$DRY_RUN" == 0 ]]; then
  exec 9>"$ROOT/.git/sync-hub.lock"
  flock -n 9 || { echo 'Another sync is running; skipping.'; exit 0; }
  out="$(bin/consolidate-skills.sh --apply)"
else
  out="$(bin/consolidate-skills.sh)"
fi
printf '%s\n' "$out"

# Build metadata in scratch space, including during preview. Existing clones and
# skill directories are only read; repos-lock writes exclusively to scratch.
scratch="$(mktemp -d)"
trap 'rm -rf -- "$scratch"' EXIT
mkdir -p "$scratch/bin"
cp bin/repos-lock.sh "$scratch/bin/"
ln -s "$ROOT/repos" "$scratch/repos"
ln -s "$ROOT/skills" "$scratch/skills"
ln -s "$ROOT/overlays" "$scratch/overlays"
cp .gitignore "$scratch/.gitignore"
cp .skill-lock.json "$scratch/.skill-lock.json"
GIT_OPTIONAL_LOCKS=0 bash "$scratch/bin/repos-lock.sh" save
python3 -I - "$scratch" <<'PY'
import json, re, sys
from pathlib import Path
root = Path(sys.argv[1])
names = sorted(json.loads((root / '.skill-lock.json').read_text())['skills'])
if any('/' in n or '\n' in n or '\r' in n for n in names):
    raise SystemExit('Invalid skill name in lock file')
p = root / '.gitignore'
block = '# BEGIN skill-lock\n' + ''.join(f'/skills/{n}/\n' for n in names) + '# END skill-lock'
text, count = re.subn(r'# BEGIN skill-lock\n.*?# END skill-lock', lambda _: block, p.read_text(), flags=re.S)
if count != 1:
    raise SystemExit('Expected exactly one skill-lock block in .gitignore')
p.write_text(text)
PY

printf '\nCandidate commit paths (tracked skills and managed metadata only):\n'
git diff --name-only HEAD -- skills/
for path in .gitignore .skill-lock.json repos.lock; do
  if ! git show "HEAD:$path" | cmp -s - "$scratch/$path"; then
    printf '%s\n' "$path"
  fi
done
printf '\nUntracked skill directories are never automatically published.\n'
if [[ "$DRY_RUN" == 1 ]]; then
  echo 'Preview only: no hub files, index, commits, or remotes changed.'
  echo 'Consolidation may affect tracked skills; inspect its proposal above.'
  exit 0
fi

cp "$scratch/.gitignore" .gitignore
cp "$scratch/repos.lock" repos.lock
git add -- .gitignore .skill-lock.json repos.lock
git add -u -- skills/
if git diff --cached --quiet; then
  echo 'No managed changes.'
else
  git diff --cached --check
  git commit -m 'Auto-sync tracked skills and metadata'
  git push
fi
if [[ "$out" == *' CONFLICT '* ]]; then
  echo 'WARNING: skill conflicts require manual resolution.' >&2
  exit 2
fi
