import os
from PIL import Image

supportedExtensions = [".jpg", ".jpeg", ".png", ".webp", ".tga", ".bmp", ".gif"]

def OpenImage(path):
    fileName = os.path.basename(path)
    fileRoot, fileExtension = os.path.splitext(path)

    validExtension = False
    for extension in supportedExtensions:
        if fileExtension == extension :
            validExtension = True
    if not validExtension:
        print(f"Error: {fileName} is not supported.")
        exit()

    try:
        return Image.open(path)
    except FileNotFoundError:
        print(f"Error: {fileName}{fileExtension} not found.")
        exit()

def SaveImage(image, outPath):
    try:
        image.save(outPath)
    except ValueError:
        print("The output file extension is not supported.")
    except OSError:
        print("Something went wrong during the exportation.")
