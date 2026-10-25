#!/usr/bin/env bash
# Refresh templates/ from the source repo (awun0105/Best-Readme-Template).
#   sync-templates.sh            # needs git and network access
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
git clone -q --depth 1 https://github.com/awun0105/Best-Readme-Template.git "$tmp/src"
rm -rf "$here/templates"
mkdir -p "$here/templates"
cp "$tmp/src/README_TEMPLATE.md" "$tmp/src/README_VN_TEMPLATE.md" "$here/templates/"
cp -r "$tmp/src/docs" "$here/templates/docs"
echo "templates/ updated from awun0105/Best-Readme-Template @ $(git -C "$tmp/src" rev-parse --short HEAD)"
