from file import *
from filters import *

path = input('Enter a path image: ')
image = OpenImage(path)
image = GreyImage(image)
image = BlurImage(image, 5)
image = DilateImage(image)
image = TextOnImage(image, "FOR GOD SAKE", 12, (40, 40), "green")
image = RotateImage(image, 20)
image = ResizeImage(image, (200, 100))
SaveImage(image, "result.jpg")
