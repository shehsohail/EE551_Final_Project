# Final Project EE551_Engineering Programming_Python
# Pencil function

import numpy as np
import matplotlib.image as image
import matplotlib.pyplot as plt
import cv2

# Pencil Image

# Define Parameter
# Blur_Value
# Line_Size
# Def Function
x=0
def pencil_img(blur_value,line_size,image_location):
    pic1=image_location + "Self_Portrait.jpg"
    # Landscape
    pic2=image_location + "Day2_8.jpg"
    # Urban
    pic3=image_location + "Urban_2.jpg"
    # Nature
    pic4=image_location + "Day6_9.jpg"
    L=[pic1,pic2,pic3,pic4]
    
    for x in range(4):
        
        # reading input_images 
        input_img = cv2.imread(L[x])


        # Edges
        gray = cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
        # Blur Value (x)
        gray = cv2.medianBlur(gray, blur_value)
        # line size and Blur Value (x,x)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                             cv2.THRESH_BINARY,line_size, blur_value)

        # Pencil Sketching

        # Invert image
        inverted_image = 255 - gray

        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

        inverted_blurred = 255 - blurred
        pencil_sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

        for i in range(2):
            if (i==0):
                # with WINDOW_AUTOSIZE, window size is set automatically
                cv2.namedWindow("Display_Original", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("Display_Original", 900, 1000)
                cv2.imshow("Display_Original", input_img)

                cv2.waitKey(5000)
            
            else:
            
                cv2.namedWindow("Display_Pencil", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("Display_Pencil", 900, 1000)
                cv2.imshow("Display_Pencil", pencil_sketch)
                cv2.waitKey(5000)

            cv2.destroyAllWindows()

# Image 1 Self Potrait
pencil_img(5,9,"Pencil_Cartoon_Images/")
