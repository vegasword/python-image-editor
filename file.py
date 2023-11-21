import os
import shutil

supportedExts = [".jpg", ".jpeg", ".png", ".webp", ".tga", ".bmp", ".gif"]

imgPath = input('Enter a path file: ')
imgName = os.path.basename(imgPath)
imgRoot, imgExt = os.path.splitext(imgPath)
imgDest = "img/" + imgName

validExt = False
for ext in supportedExts:
    if imgExt == ext:
        validExt = True
if not validExt:
    print(f"{imgPath} is not supported.")
    exit()

try:
    shutil.copy2(imgPath, imgDest)
except FileNotFoundError:
    print("No such file or directory")
    
