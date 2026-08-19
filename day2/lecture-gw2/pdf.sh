#!/bin/bash
# Export the deck to a single self-contained PDF. Shareable, offline.
# Output: slides.pdf  (in this folder)
set -euo pipefail
source "$HOME/anaconda3/etc/profile.d/conda.sh"
conda activate slidev
cd "$(dirname "$0")"

./node_modules/.bin/slidev export slides.md --output slides.pdf --per-slide --wait 800

echo
echo "Wrote: $(pwd)/slides.pdf"
open slides.pdf 2>/dev/null || true
