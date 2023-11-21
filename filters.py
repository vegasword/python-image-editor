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
        


