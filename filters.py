import cv2 
import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from logger import *


cv2.setLogLevel(0)
Image.MAX_IMAGE_PIXELS = None

def GreyImage(image):
    """
    Applies a grey filter
    :param image: Inputted pillow image
    :return: New pillow image
    """
    logger.out("Applying grey filter")
    return image.convert('L')
  
def BlurImage(image, bluringRadius):
    """
    Applies a Gaussian blur filter
    :param image: Inputted pillow image
    :param bluringRadius: Radius of the blur filter
    :return: New pillow image
    """
    try:
        logger.out(f"Applying blur filter with a radius of {bluringRadius}")
        return image.filter(ImageFilter.GaussianBlur(bluringRadius))
    except TypeError :
        print("The type of bluringLvl must be a number.")

def DilateImage(image):
    """
    Applies a dilatation filter
    :param image: Inputted cv2 image
    :return: New pillow image
    """
    logger.out("Applying dilatation filter")
    kernel = np.ones((5, 5), np.uint8)
    return Image.fromarray(cv2.dilate(np.array(image), kernel, iterations=1))
    
def RotateImage(image, angle):
    """
    Rotate the image
    :param angle: Angle (in degree counter clockwise)
    :return: New pillow image
    """
    try :
        logger.out(f"Rotating the image by {angle} degrees counter clockwise")
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
        logger.out(f"Resizing the image to {dimension} degrees counter clockwise")
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
        logger.out(f"Applying a {size} pixels sized text ('{text}') onto the image at {position} with the color {color}")
        return copiedImage
    except AttributeError :
        print("Failed to draw on the image.")

def WatercolourImage(image):
    """
    Apply a watercolor effect to the input image.
    :param image: Pillow image or NumPy array representing the image
    :returns: Watercolorized image as a Pillow image
    """
    return Image.fromarray(cv2.stylization(np.array(image), sigma_s=100, sigma_r=0.4))