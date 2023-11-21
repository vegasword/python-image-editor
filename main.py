from file import *
from filters import *

from PIL import Image, ImageDraw, ImageFont

image = OpenImage("img/Nishikata.jpg")
image = TextOnImage(image, "AAAAA", 256, (256, 256), (255, 0, 0))
image = ResizeImage(image, (64, 64))
image.show()
SaveImage(image, "azerty.jpg")
