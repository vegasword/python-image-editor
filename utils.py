from PIL import Image

from myImage import *

def cv2ToPillow(image):
    return Image.fromarray(cv2.cvtColor(image.cv2Img, cv2.COLOR_BGR2RGB))