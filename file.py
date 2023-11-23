import os
import cv2 
from PIL import Image

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
    except ValueError:
        print("The output file extension is not supported.")
    except OSError:
        print("Something went wrong during the exportation.")

def CreateGif(image_paths, gif_path, duration=100, loop=0, resize_dimension=(500, 500)):
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
        resized_image = ResizeImage(image_list[i], resize_dimension)
        if resized_image is not None:
            image_list[i] = resized_image
    image_list[0].save(
        gif_path,
        save_all=True,
        append_images=image_list[1:],
        duration=duration,
        loop=loop
    )

