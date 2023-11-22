import os
import cv2 
import numpy as np 
from PIL import ImageDraw, ImageFilter, ImageFont

from utils import *

cv2.setLogLevel(0)

def GreyImage(image):
    return image.convert('L')
  
def BlurImage(image, bluringLvl):
    try:
        return image.filter(ImageFilter.GaussianBlur(bluringLvl))
    except TypeError :
        print("The type of bluringLvl must be a number.")
    

def DilateImage(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2ToPillow(cv2.dilate(image, kernel, iterations=1))
    
def RotateImage(image, angle):
    try :
        return image.rotate(angle)
    except TypeError :
        print("The type of the angle must be a number.")
  
def ResizeImage(image, dimension):
    try :
        return image.resize(dimension)
    except TypeError :
        print("The type of the dimension must be a tuple.")
    except NameError :
        print("The dimension must be a tuple.")

def TextOnImage(image, text, size, position, color):
    try :
        copiedImage = image.copy()
        draw = ImageDraw.Draw(copiedImage)
        font = ImageFont.load_default(size)
        draw.text(position, text, font=font, fill=color)
        return copiedImage
    except TypeError :
        print("hskuhk ")