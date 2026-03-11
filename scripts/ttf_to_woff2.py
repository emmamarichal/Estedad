import sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.woff2 import main as woff2_main
import os

input_path = sys.argv[1]

base, _ = os.path.splitext(input_path)
output_path = base + ".woff2"

font = TTFont(input_path)
font.flavor = "woff2"
font.save(output_path)