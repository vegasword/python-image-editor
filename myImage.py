import os
import cv2 
from PIL import Image


class MyImage:

    def __init__(self, path):
        supportedExtensions = [".jpg", ".jpeg", ".png", ".webp", ".tga", ".bmp", ".gif"]

        self.path = path
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
            self.pillowImg = Image.open(path)
            self.cv2Img = cv2.imread(path)
        except FileNotFoundError:
            print(f"Error: {fileName}{fileExtension} not found.")
            exit()

    def SaveImage(self, outPath):
        try:
            self.pillowImg.save(outPath)
        except ValueError:
            print("The output file extension is not supported.")
        except OSError:
            print("Something went wrong during the exportation.")
