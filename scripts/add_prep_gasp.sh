#!/bin/zsh

cd "$(dirname "$0")"

ttx -m Estedad-VF.ttf prep-gasp.ttx
python3 rename_remove.py Estedad-VF.ttf prep-gasp.ttf 'Estedad[wght].ttf'

echo ""
echo "Finished. Press any key to close..."
read -n 1 -s