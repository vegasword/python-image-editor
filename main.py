from myImage import *
from filters import *

#try:
#   imgPath = input('Enter a path image: ')
#except FileNotFoundError:
#   print("No such file or directory.")
try :
    image = MyImage("img/nishikata.jpg")
    # image.pillowImg = GreyImage(image.pillowImg)
    # image.pillowImg = BlurImage(image.pillowImg, '20')
    # image.pillowImg = DilateImage(image.cv2Img)
    # image.pillowImg = TextOnImage(image.pillowImg, 'AAAAA', 50, (256, 256),'aqua')
    # image.pillowImg = RotateImage(image.pillowImg,20)
    # image.pillowImg = ResizeImage(image.pillowImg, (600, 600))
    image.SaveImage("img/azerty.jpg")
except NameError :
    print("Image not found.")
except AttributeError : 
    print("The Attribute given in parameters are wrong")
except TypeError :
    print("The Type given in parameters are wrong")


