from filters import *

try:
    imgPath = input('Enter a path image: ')
except FileNotFoundError:
    print("No such file or directory.")

    GreyImage(imgPath)
    BlurImage(imgPath,20)
    DilateImage(imgPath)
    RotateImage(imgPath, 20)
