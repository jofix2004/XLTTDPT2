import cv2
import numpy as np

def resize_image(image, value):
    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate the new image dimensions
    new_height = int(height * value)
    new_width = int(width * value)

    # Resize the image
    new_image = cv2.resize(src = image, 
                          dsize=(new_width, new_height), 
                          interpolation=cv2.INTER_CUBIC)

    return new_image
