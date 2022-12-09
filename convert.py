from PIL import Image
import os

folder = "/home/shile/manga/references"

for f in os.listdir(folder):
    if ".webp" not in f:
        continue
    im = Image.open(os.path.join(folder, f)).convert("RGB")
    im.save(os.path.join(folder, f.split(".")[0] + ".jpg"), "jpeg")
