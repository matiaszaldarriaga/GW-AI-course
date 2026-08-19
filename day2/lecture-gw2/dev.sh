#!/bin/bash
# Launch the Slidev dev server for the Uros Fest deck.
# Activates the `slidev` conda env (where Node lives) and runs `npm run dev`,
# which uses the @slidev/cli already symlinked from the dotPE_waveforms project.
set -euo pipefail
source "$HOME/anaconda3/etc/profile.d/conda.sh"
conda activate slidev
cd "$(dirname "$0")"
exec npm run dev
