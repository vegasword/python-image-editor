from filters import *

try:
    imgPath = input('Enter a path image: ')
    ConvertToGrey(imgPath)
except FileNotFoundError:
    print("No such file or directory.")

try:
    imgPath = input('Enter a path image: ')
    DilateImage(imgPath)
except cv2.error:
    print("No such file or directory.")