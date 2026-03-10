#!/bin/zsh

cd "$(dirname "$0")"

python3 subset.py 'Estedad[wght].ttf' exclude_list.txt "Estedad Lite" 'Estedad[wght]-Lite.ttf'

echo ""
echo "Finished. Press any key to close..."
read -n 1 -s