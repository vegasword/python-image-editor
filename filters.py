import os
import cv2 
import numpy as np 
from PIL import Image

cv2.setLogLevel(0)

def ConvertToGrey(imgPath):
    imgName = os.path.basename(imgPath)

    image = Image.open(imgPath)
    image = image.convert('L')

    image.save(f'img/grey-{imgName}')
    return image

def DilateImage(imgPath):
    img = cv2.imread(imgPath) 
    imgName = os.path.basename(imgPath)
    
    kernel = np.ones((5, 5), np.uint8)
    
    imgDilation = cv2.dilate(img, kernel, iterations=1)
    
    outputPath = "img/dilate-" + imgName
    cv2.imwrite(outputPath, imgDilation)