import os
import cv2 
import numpy as np 
from PIL import ImageDraw, ImageFilter, ImageFont

from utils import *

cv2.setLogLevel(0)

def GreyImage(image):
    return image.convert('L')
  
def BlurImage(image, bluringLvl):
    return image.filter(ImageFilter.GaussianBlur(bluringLvl))

def DilateImage(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2ToPillow(cv2.dilate(image, kernel, iterations=1))
    
def RotateImage(image, angle):
    return image.rotate(angle)
  
def ResizeImage(image, dimension):
    return image.resize(dimension)

def TextOnImage(image, text, size, position):
    copiedImage = image.copy()
    draw = ImageDraw.Draw(copiedImage)
    font = ImageFont.load_default(size)
    draw.text(position, text, font=font, fill=255)
    return copiedImage
