import os
import cv2 
import numpy as np 
from PIL import Image, ImageFilter

cv2.setLogLevel(0)

def GreyImage(imgPath):
    imgName = os.path.basename(imgPath)

    image = Image.open(imgPath)
    image = image.convert('L')

    image.save(f'img/grey-{imgName}')
    return image
  
def BlurImage(imgPath,bluringLvl):
    imgName = os.path.basename(imgPath)
    img = Image.open(imgPath) 
    imgBlured = img.filter(ImageFilter.GaussianBlur(bluringLvl))
    imgBlured.show()
    imgBlured.save(f'img/blured-{imgName}')
    return imgBlured

def DilateImage(imgPath):
    img = cv2.imread(imgPath) 
    imgName = os.path.basename(imgPath)
    
    kernel = np.ones((5, 5), np.uint8)
    
    imgDilation = cv2.dilate(img, kernel, iterations=1)
    
    outputPath = "img/dilate-" + imgName
    cv2.imwrite(outputPath, imgDilation)
    
def RotateImage(imgPath, angle):
    imgName = os.path.basename(imgPath)
    img = Image.open(imgPath) 
    imgRotated = img.rotate(angle)
    imgRotated.show()
    imgRotated.save(f'img/Rotated-{imgName}')
    return imgRotated

  