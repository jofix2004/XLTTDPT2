import cv2

def flip_image(image, direction):
    # If direction is 0, flip vertically
    if direction == 0:
        image = cv2.flip(image, 0)
    # Otherwise, flip horizontally
    else:
        image = cv2.flip(image, 1)

    return image
