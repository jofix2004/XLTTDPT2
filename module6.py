import cv2
import numpy as np

def space_image(image, choose):
        
        
    if choose == 0:
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY ) 
    elif choose == 1:
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV ) 
    elif choose == 2:
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB ) 
    elif choose == 3:
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB ) 
    elif choose == 4:
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY ) 
    elif choose == 5:
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY ) 



    return new_image
