import cv2
import numpy as np

def blur_image(image, kernel_size):
    # Ensure kernel_size is at least 3 and is odd
    kernel_size = max(3, int(kernel_size))  # Ensure it's at least 3
    kernel_size = kernel_size + (1 - kernel_size % 2)  # Ensure it's odd

    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    return blurred_image
