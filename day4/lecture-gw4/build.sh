#!/bin/bash
# Build the static deck into ./dist/ and serve it on http://localhost:4040/
# (Browsers block ES modules on file:// — a tiny local server is required.)
# Press Ctrl-C to stop.
set -euo pipefail
source "$HOME/anaconda3/etc/profile.d/conda.sh"
conda activate slidev
cd "$(dirname "$0")"

npm run build

PORT=4040
echo
echo "Serving dist/ at http://localhost:${PORT}/"
echo "Press Ctrl-C to stop."
echo

# Start Python's http server in dist/, open browser, wait until interrupted.
cd dist
( sleep 1 && open "http://localhost:${PORT}/" ) &
exec python3 -m http.server "${PORT}" --bind 127.0.0.1
