#!/bin/zsh

cd "$(dirname "$0")"

python3 ttf_to_woff2.py 'Estedad[wght].ttf'

echo ""
echo "Finished. Press any key to close..."
read -n 1 -s