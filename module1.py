import cv2
import numpy as np

def rotate_image(image, angle):
    # Get the image size
    # No that's not an error - NumPy stores image matricies backwards
    image_size = (image.shape[1], image.shape[0])

    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((image_size[0] / 2, image_size[1] / 2), angle, 1)

    # Rotate the image
    image = cv2.warpAffine(image, rotation_matrix, image_size)

    return image
