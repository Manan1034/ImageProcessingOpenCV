#Shi Tomasi corner detector

import numpy as np
import cv2

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\pic1.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original',img)

corner=cv2.goodFeaturesToTrack(gray,25,0.01,10)       #1st arg is image,2nd arg is max no of corners
                                                      #(if there are more corners in image,then strongest corners will be returned.)
                                                      #3rd arg is quality level i.e. minimum quality value of the corner.
                                                      #4th arg is min distance i.e. min euclidian distance between corners.
#This function does not return integer value.We have to convert these corners value to integer values

corner=np.int0(corner)                 #int0 is the alias for int64

for i in corner:
    x,y=i.ravel()                              #ravel() unbinds the value
    cv2.circle(img,(x,y),3,[255,0,0],-1)

cv2.imshow('Final image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
