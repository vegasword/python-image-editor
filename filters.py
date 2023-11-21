from PIL import Image
from PIL import ImageFilter
import os

def blurFilter(imgPath,bluringLvl):
    imgName = os.path.basename(imgPath)
    img = Image.open(imgPath) 
    imgBlured = img.filter(ImageFilter.GaussianBlur(bluringLvl))
    imgBlured.show()
    imgBlured.save(f'img/blured-{imgName}')
    return imgBlured

def rotateImg(imgPath, angle):
    imgName = os.path.basename(imgPath)
    img = Image.open(imgPath) 
    imgRotated = img.rotate(angle)
    imgRotated.show()
    imgRotated.save(f'img/Rotated-{imgName}')
    return imgRotated

