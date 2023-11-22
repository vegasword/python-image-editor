from file import *
from filters import *

path = input('Enter a path image: ')

try:
    image = OpenImage(path)
    image = GreyImage(image)
    image = BlurImage(image, 20)
    image = DilateImage(image)
    image = TextOnImage(image, "AAAAA", 256, (256, 256), "blue")
    image = RotateImage(image, 20)
    image = ResizeImage(image, (64, 64))
    SaveImage(image, "img/azerty.jpg")
except NameError :
    print("Image not found.")
except AttributeError : 
    print("The attribute given in parameters are wrong.")
except TypeError :
    print("The type given in parameters are wrong.")
