A collection of python scripts useful for manga making. `process.py` assumes you have Krita installed.

Scripts:
* alphize.py - adds transparency to images. Useful for screentones and coloring analog drawings
* process.py - converts krita documents to png images, then thresholds, crops, and optionally resizes the image. Parameters are set to match the given templates
* rename.py - some digital scanners name images with a date/timestamp/sequence, so this script renames them to pg1.png, pg2.png, ...

Usage examples:
```bash
./alphize.py examples/alphize/
./process.py examples/process/ 455 645
./rename.py examples/rename/
```

Resource attribution:
* [source of manuscript used in the templates](http://www.flyingchipmunkcomicspress.com/Comic_Art_Boards.html)
* [screentones in examples/alphize/](https://www.deviantart.com/snarkdoodle/art/Krita-dot-screentones-for-brush-pattern-585678496)