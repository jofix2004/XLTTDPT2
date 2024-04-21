import cv2
import numpy as np

def zoom_image(image, scale):
    # Get the image size
    image_size = (image.shape[1], image.shape[0])

    # The following operations are done to get the region of interest of the image
    center = (image_size[0] / 2, image_size[1] / 2)
    width = image_size[0] / scale
    height = image_size[1] / scale
    x1 = center[0] - width / 2
    x2 = center[0] + width / 2
    y1 = center[1] - height / 2
    y2 = center[1] + height / 2

    # Get the region of interest of the image to perform zooming
    image = image[int(y1):int(y2), int(x1):int(x2)]

    # Resize the cropped image to the original image size (to simulate the effect of zooming)
    image = cv2.resize(image, image_size, interpolation = cv2.INTER_LINEAR)

    return image
