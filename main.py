from file import *
from filters import *


# path = input('Enter a path image: ')
# image = OpenImage(path)
# # image = GreyImage(image)
# # image = BlurImage(image, 5)
# # image = DilateImage(image)
# # image = TextOnImage(image, "FOR GOD SAKE", 12, (40, 40), "green")
# # image = RotateImage(image, 20)
# # image = ResizeImage(image, (200, 100))
# image = WatercolourImage(image)
# SaveImage(image, "img/result.jpg")

images_list = ['img/paysage1.jpg','img/paysage2.jpg','img/paysage3.jpg','img/paysage4.jpg','img/paysage5.jpg','img/paysage6.jpg']
create_gif(images_list, 'img/paysage.gif', duration=500, loop=0)