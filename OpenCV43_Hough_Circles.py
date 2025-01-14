#Drawing circles across objects

import cv2
import numpy as np


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\smarties.png')
output=img.copy()

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=cv2.medianBlur(gray,5)        #Hough circle method works better with blurred image
                                   #1st arg is source and 2nd arg is kernal size
circle=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
                                  #1st arg is source,2nd arg is method(only 1 method is used)
                                  #3rd arg is dp(inverse ratio of resolution of accumulator to resolution of image
                                  #4th arg is min dist between centres of detected circles.5th and 6th arg are param1 and param2
                                  #For clarity about param1 and param2 check image HoughCircles Arguments in opencv folder
                                  #7th arg is minimum radius.8th arg is maximum radius

#This HoughCircles method returns vectors.We will convert the value to integers to draw the circles

det_cir=np.uint16(np.around(circle))      #Converting vector to integer values
print(det_cir)

for (x,y,r) in det_cir[0, :]:                          #Unpacking the det_cir array
    cv2.circle(output,(x,y),r,(0,255,0),2)
    cv2.circle(output,(x,y),2,(0,255,255),3)           #This will print the center of circle in the image

    
cv2.imshow('Output',output)

cv2.waitKey(0)
cv2.destroyAllWindows()
