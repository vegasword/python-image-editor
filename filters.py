import os
import cv2 
import numpy as np 
from PIL import Image, ImageDraw, ImageFilter, ImageFont

cv2.setLogLevel(0)

def GreyImage(image):
    """
    Applies a grey filter
    :param image: Inputted pillow image
    :return: New pillow image
    """
    return image.convert('L')
  
def BlurImage(image, bluringRadius):
    """
    Applies a Gaussian blur filter
    :param image: Inputted pillow image
    :param bluringRadius: Radius of the blur filter
    :return: New pillow image
    """
    try:
        return image.filter(ImageFilter.GaussianBlur(bluringRadius))
    except TypeError :
        print("The type of bluringLvl must be a number.")

def DilateImage(image):
    """
    Applies a dilatation filter
    :param image: Inputted cv2 image
    :return: New pillow image
    """
    kernel = np.ones((5, 5), np.uint8)
    return Image.fromarray(cv2.dilate(np.array(image), kernel, iterations=1))
    
def RotateImage(image, angle):
    """
    Rotate the image
    :param angle: Angle (in degree counter clockwise)
    :return: New pillow image
    """
    try :
        return image.rotate(angle)
    except TypeError :
        print("The type of the angle must be a number.")
  
def ResizeImage(image, dimension):
    """
    Resize the image
    :param dimension: New image dimension
    :return: New pillow image
    """
    try :
        return image.resize(dimension)
    except TypeError :
        print("The type of the dimension must be a tuple.")
    except NameError :
        print("The dimension must be a tuple.")

def TextOnImage(image, text, size, position, color):
    """
    Draw a text onto an image
    :param image: Inputted pillow image
    :param text: Inputted text
    :param size: The size of the text
    :param position: The position of the text
    :param color: The color of the text (cv2 color representation)
    :return: New pillow image
    """
    try :
        copiedImage = image.copy()
        draw = ImageDraw.Draw(copiedImage)
        font = ImageFont.load_default(size)
        draw.text(position, text, font=font, fill=color)
        return copiedImage
    except AttributeError :
        print("Failed to draw on the image.")
