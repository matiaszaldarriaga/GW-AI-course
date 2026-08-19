#!/bin/bash
# Build a single, self-contained HTML file: Slidev's full deck with all JS,
# CSS, fonts, and assets (including the gif animation) inlined as data URLs.
# Opens with double-click on any system, no server, no internet.
# Output: slides-share.html
set -euo pipefail
source "$HOME/anaconda3/etc/profile.d/conda.sh"
conda activate slidev
cd "$(dirname "$0")"

# SINGLEFILE=1 enables the vite-plugin-singlefile branch in vite.config.ts.
SINGLEFILE=1 ./node_modules/.bin/slidev build slides.md --base ./ --out dist-share

cp dist-share/index.html slides-share.html
rm -rf dist-share

SIZE_KB=$(( $(wc -c < slides-share.html) / 1024 ))
echo
echo "Wrote: $(pwd)/slides-share.html  (${SIZE_KB} KB, fully self-contained)"
open slides-share.html 2>/dev/null || true
