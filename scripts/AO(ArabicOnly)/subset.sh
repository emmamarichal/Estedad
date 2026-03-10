#!/bin/zsh

cd "$(dirname "$0")"

python3 subset.py 'Estedad[wght].ttf' exclude_list.txt "Estedad AO" 'Estedad[wght]-AO.ttf'
#python3 subset.py 'Estedad[wght].woff' exclude_list.txt "Estedad AO" 'Estedad[wght]-AO.woff' 
#python3 subset.py 'Estedad[wght].woff2' exclude_list.txt "Estedad AO" 'Estedad[wght]-AO.woff2'

echo ""
echo "Finished. Press any key to close..."
read -n 1 -s