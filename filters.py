from PIL import Image, ImageDraw, ImageFont

def ResizeImage(image, dimension):
    return image.resize(dimension)

def TextOnImage(image, text, size, position, color):
    copiedImage = image.copy()
    draw = ImageDraw.Draw(copiedImage)
    font = ImageFont.load_default(size)
    draw.text(position, text, font=font, fill=color)
    return copiedImage
