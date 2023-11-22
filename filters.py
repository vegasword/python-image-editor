import os
import cv2 
import numpy as np 
from PIL import Image, ImageFilter, ImageFont

cv2.setLogLevel(0)

def GreyImage(image):
    return image.convert('L')
  
def BlurImage(image, bluringLvl):
    return image.filter(ImageFilter.GaussianBlur(bluringLvl))

def DilateImage(imgPath):
    img = cv2.imread(imgPath) 
    imgName = os.path.basename(imgPath)
    kernel = np.ones((5, 5), np.uint8)
    imgDilation = cv2.dilate(img, kernel, iterations=1)
    outputPath = "img/dilate-" + imgName
    cv2.imwrite(outputPath, imgDilation)
    
def RotateImage(image, angle):
    return image.rotate(angle)
  
def ResizeImage(image, dimension):
    return image.resize(dimension)

def TextOnImage(image, text, size, position, color):
    copiedImage = image.copy()
    draw = ImageDraw.Draw(copiedImage)
    font = ImageFont.load_default(size)
    draw.text(position, text, font=font, fill=color)
    return copiedImage
