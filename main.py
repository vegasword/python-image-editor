from file import *
from filters import *

#try:
#   imgPath = input('Enter a path image: ')
#except FileNotFoundError:
#   print("No such file or directory.")

image = OpenImage("img/Nishikata.jpg")
# image = GreyImage(image)
# image = BlurImage(image, 20)
# image = DilateImage(image)
# image = TextOnImage(image, "AAAAA", 256, (256, 256), "blue")
# image = RotateImage(image, 20)
# image = ResizeImage(image, (64, 64))
# image = WatercolourImage(image)
SaveImage(image, "img/azerty.jpg")

