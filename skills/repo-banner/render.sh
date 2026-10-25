#!/usr/bin/env bash
# Render a banner HTML file to PNG with headless Chrome (no npm packages needed).
#   render.sh banner.html banner.png [width=1600] [height=500] [scale=1.5]
set -euo pipefail
in="${1:?usage: render.sh banner.html banner.png [width] [height] [scale]}"
out="${2:?usage: render.sh banner.html banner.png [width] [height] [scale]}"
w="${3:-1600}"; h="${4:-500}"; scale="${5:-1.5}"

chrome="${CHROME_PATH:-}"
if [ -z "$chrome" ]; then
  for c in google-chrome google-chrome-stable chromium chromium-browser \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
           "/Applications/Chromium.app/Contents/MacOS/Chromium" \
           "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"; do
    if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then chrome="$c"; break; fi
  done
fi
[ -n "$chrome" ] || { echo "Chrome/Chromium not found; set CHROME_PATH" >&2; exit 1; }

abs_in="$(cd "$(dirname "$in")" && pwd)/$(basename "$in")"
abs_out="$(cd "$(dirname "$out")" && pwd)/$(basename "$out")"
# virtual-time-budget lets web fonts and images load before the shot.
"$chrome" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size="$w,$h" --force-device-scale-factor="$scale" \
  --virtual-time-budget=8000 --screenshot="$abs_out" "file://$abs_in" >/dev/null 2>&1
[ -s "$abs_out" ] || { echo "screenshot failed" >&2; exit 1; }
echo "Wrote $out"
