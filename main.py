from file import *
from filters import *

try:
    imgPath = input('Enter a path image: ')
except FileNotFoundError:
    print("No such file or directory.")

    image = OpenImage("img/Nishikata.jpg")
    image = GreyImage(image)
    image = BlurImage(image,20)
    image = DilateImage(image)
    image = RotateImage(image, 20)
    image = TextOnImage(image, "AAAAA", 256, (256, 256), (255, 0, 0))
    image = ResizeImage(image, (64, 64))
    SaveImage(image, "azerty.jpg")
