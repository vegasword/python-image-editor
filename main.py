from myImage import *
from filters import *

#try:
#   imgPath = input('Enter a path image: ')
#except FileNotFoundError:
#   print("No such file or directory.")

image = MyImage("img/nishikata.jpg")
image.pillowImg = GreyImage(image.pillowImg)
image.pillowImg = BlurImage(image.pillowImg, 20)
image.pillowImg = DilateImage(image.cv2Img)
image.pillowImg = TextOnImage(image.pillowImg, "AAAAA", 256, (256, 256))
image.pillowImg = RotateImage(image.pillowImg, 20)
image.pillowImg = ResizeImage(image.pillowImg, (64, 64))
image.SaveImage("azerty.jpg")
