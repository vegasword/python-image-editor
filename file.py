import os
import cv2 
from PIL import Image

def OpenImage(path):
    """
    Create a pillow and cv2 image instance
    :param path: Path of the image
    """
    supportedExtensions = [".jpg", ".jpeg", ".png", ".webp", ".tga", ".bmp", ".gif"]

    path = path
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
    """
    Save the current image state using pillow
    :param outPath: Export path
    """
    try:
        return image.save(outPath)
    except ValueError:
        print("The output file extension is not supported.")
    except OSError:
        print("Something went wrong during the exportation.")
