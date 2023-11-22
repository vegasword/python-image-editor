from file import *
from filters import *

try:
   imgPath = input('Enter a path image: ')
except FileNotFoundError:
   print("No such file or directory.")

path = input('Enter a path image: ')
image = OpenImage(path)
image = GreyImage(image)
image = BlurImage(image, 5)
image = DilateImage(image)
image = TextOnImage(image, "FOR GOD SAKE", 12, (40, 40), "green")
image = RotateImage(image, 20)
image = ResizeImage(image, (200, 100))
image = WatercolourImage(image)
SaveImage(image, "result.jpg")
