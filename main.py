from filters import *

try:
    imgPath = input('Enter a path image: ')
    ConvertToGrey(imgPath)
except FileNotFoundError:
    print("No such file or directory.")

imgPath = input('Enter a path image: ')
DilateImage(imgPath)