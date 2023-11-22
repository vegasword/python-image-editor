import cv2
from PIL import Image

from myImage import *

def cv2ToPillow(imageData):
    return Image.fromarray(cv2.cvtColor(imageData, cv2.COLOR_BGR2RGB))
