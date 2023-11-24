import os
import cv2 
from PIL import Image, ImageDraw

from filters import *

def OpenImage(path):
    """
    Create a pillow and cv2 image instance
    :param path: Path of the image
    """
    supportedExtensions = [".jpg", ".jpeg", ".png", ".webp", ".tga", ".bmp", ".gif"]

    fileName = os.path.basename(path)
    fileRoot, fileExtension = os.path.splitext(path)

    validExtension = False
    for extension in supportedExtensions:
        if fileExtension == extension :
            validExtension = True
    if not validExtension:
        print(f"Error: {fileName} is not supported.")
        exit()

    try:
        return Image.open(path)
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        exit()

def SaveImage(image, outPath):
    """
    Save the current image state using pillow
    :param outPath: Export path
    """
    try:
        return image.save(outPath)
    except AttributeError:
        return None
    except ValueError:
        print("The output file extension is not supported.")
    except OSError:
        print("Something went wrong during the exportation.")

def CreateGif(image_paths, gif_path, duration=100, loop=0, width=500, height = 500):
    """
    Create a GIF from a list of image file paths.

    Parameters:
    - image_paths: List of file paths to images.
    - gif_path: Path to save the resulting GIF file.
    - duration: Duration (in milliseconds) to display each frame.
    - loop: Number of loops (0 for infinite loop).
    - resize_dimension: New image dimension as a tuple (width, height) for resizing.

    Returns:
    - None
    """
    image_list = [Image.open(image_path) for image_path in image_paths]
    for i in range(len(image_list)):
        resized_image = ResizeImage(image_list[i], width, height)
        if resized_image is not None:
            image_list[i] = resized_image
    image_list[0].save(
        gif_path,
        save_all=True,
        append_images=image_list[1:],
        duration=duration,
        loop=loop
    )


def DetectFace(image_path):
    """
    Detect faces in an image using Haarcascades classifier.

    Parameters:
    - image_path : Path to the input image.

    Returns:
    - faces (list): List of tuples representing detected faces' coordinates (x, y, w, h).
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return faces

def DrawSquares(image_path):
    """
    Detect and draw squares around faces in an image.

    Parameters:
    - image_path (str): Path to the input image.
    """
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    faces = DetectFace(image_path)
    for (x, y, w, h) in faces:
        draw.rectangle([x, y, x + w, y + h], outline="red", width=3)
    image.save('img/faceResult.jpg')
