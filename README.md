A collection of python scripts useful for manga making. `process.py` assumes you have Krita installed.

Scripts:
* alphize.py - adds transparency to images. Useful for screentones and coloring analog drawings
* process.py - converts krita documents to png images, then thresholds, crops, and optionally resizes the image. Parameters are set to match the given templates
* rename.py - some digital scanners name images with a date and timestamp, so this script renames them to pg1.png, pg2.png, ...