# Final Project EE551_Engineering Programming_Python
# Cartooning function

import numpy as np
import matplotlib.image as image
import matplotlib.pyplot as plt
import cv2

# Cartoon Version

# Define Parameters
# Blur_Value
# Line_Size

x=0
def cartoon_img(blur_value,line_size,image_location):
    pic1=image_location + "Self_Portrait.jpg"
    # Landscape
    pic2=image_location + "Day2_8.jpg"
    # Urban
    pic3=image_location + "Urban_2.jpg"
    # Nature
    pic4=image_location + "Day6_9.jpg"
    L=[pic1,pic2,pic3,pic4]
    for x in range(4):
        
        # reading original view input_images 
        input_img = cv2.imread(L[x])

        # Cartoonization
        
        # Edges
        gray = cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
        # Blur Value (x)
        gray = cv2.medianBlur(gray, blur_value)
        # line size and Blur Value (x,x)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                             cv2.THRESH_BINARY,line_size, blur_value)
        
        #gray_blur = cv2.medianBlur(gray, blur_value,sigmaColor=200,sigmaSpace=200)
        color = cv2.bilateralFilter(input_img, blur_value, 250, 250)
        cartoon_sketch = cv2.bitwise_and(color, color, mask=edges)
        
        for i in range(2):
            if (i==0):
                # with WINDOW_AUTOSIZE, window size is set automatically
                cv2.namedWindow("Display_Original", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("Display_Original", 900, 1000)
                cv2.imshow("Display_Original", input_img)

                cv2.waitKey(5000)
            
            else:
            
                cv2.namedWindow("Display_Cartoon", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("Display_Cartoon", 900, 1000)
                cv2.imshow("Display_Cartoon", cartoon_sketch)
                cv2.waitKey(5000)

            cv2.destroyAllWindows()

cartoon_img(5,7,"Pencil_Cartoon_Images/")
