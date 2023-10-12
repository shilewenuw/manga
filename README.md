# Automated manga making workflow (Krita)
Automate parts of your manga making workflow

Krita manga templates are provided in krita_manga

Usage:
1. Draw pages, labeled pg1.kra, pg2.kra, etc. and put in PROJECT/ (or make your own folder in the repo - just make sure you copy the Makefile)
2. `cd PROJECT && make`
3. Rerun above command if changes to pages are made 
4. Upload resulting pngs located in PROJECT/out/

Features:
1. Filters out guidelines and pencils
2. Crops images to trim lines
3. Pads page numbers to 3 digits to maintain lexical ordering when uploading images to sites like Imgur

Notes:
* as of now, tested on Ubuntu Linux
* you should have Krita installed

misc_scripts/:
* alphize.py - adds transparency to images. Useful for screentones and coloring analog drawings
* rename.py - some digital scanners name images with a date/timestamp/sequence, so this script renames them to pg1.png, pg2.png, ...
* krita_shortcuts.sh - a script to set my Krita shortcuts (Ubuntu + Huion Kamvas 20)

Usage examples:
```bash
./misc_scripts/alphize.py examples/alphize/
./misc_scripts/rename.py examples/rename/
```

Resource attribution:
* [source of manuscript used in the templates](http://www.flyingchipmunkcomicspress.com/Comic_Art_Boards.html)
* [screentones in examples/alphize/](https://www.deviantart.com/snarkdoodle/art/Krita-dot-screentones-for-brush-pattern-585678496)
