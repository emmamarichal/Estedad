from fontTools.ttLib import TTFont
from fontTools import subset
import os
import sys

def subset_exclude_and_rename(input_path, exclude_file, new_name, output_path):
    # 1. Load the font
    font = TTFont(input_path)
    is_otf = 'CFF ' in font or 'CFF2' in font
    
    # 2. Load glyph names to exclude from your text file
    with open(exclude_file, "r") as f:
        exclude_names = set(line.strip() for line in f if line.strip())

    # 3. Define glyphs to keep (Everything MINUS the exclude list)
    all_glyphs = font.getGlyphOrder()
    glyphs_to_keep = [name for name in all_glyphs if name not in exclude_names]

    # 4. Configure Subsetter to keep ALL metadata and tables
    # This replicates --name-IDs='*' --layout-features='*' --drop-tables=''
    options = subset.Options()
    options.name_IDs = ['*']           # Keep all name records
    options.name_languages = ['*']     # Keep all languages
    options.drop_tables = []           # Don't drop any tables (keeps all info)
    options.hinting = True             # Keep hinting
    options.notdef_outline = True      # Keep .notdef glyph
    
    # Run subsetting
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(glyphs=glyphs_to_keep)
    subsetter.subset(font)
    
    #Update FullName and internal metadata
    clean_ps_name = new_name.replace(" ", "-")
    # 5. Rename the Font
    # Common nameIDs: 1: Family, 3: Unique ID, 4: Full Name, 6: PostScript Name
    for record in font['name'].names:
        # PostScript Name (ID 6) cannot have spaces
        if record.nameID == 6:
            clean_name = new_name.replace(" ", "-")
            record.string = clean_name.encode(record.getEncoding())
        elif record.nameID == 3:
            clean_name = new_name.replace(" ", "-")
            uniqid = str(record).split(";")[0] + ";" + str(record).split(";")[1] + ";" + clean_name
            record.string = uniqid.encode(record.getEncoding())
        # Family (1), Full Name (4)
        elif record.nameID in [1, 4]:
            record.string = new_name.encode(record.getEncoding())
    
    # Update CFF table for OpenType fonts (.otf)
    if is_otf:
        cff = font['CFF '].cff
        cff.fontNames = [clean_ps_name]
        for top_dict in cff.topDictIndex:
            if hasattr(top_dict, 'FullName'):
                top_dict.FullName = new_name
            if hasattr(top_dict, 'FamilyName'):
                top_dict.FamilyName = new_name

    # 6. Save the final font
    font.save(output_path)

input_path = str(sys.argv[1])
exclude_file = str(sys.argv[2])
new_name = str(sys.argv[3])
output_path = str(sys.argv[4])

subset_exclude_and_rename(input_path=input_path, exclude_file=exclude_file, new_name=new_name, output_path=output_path)