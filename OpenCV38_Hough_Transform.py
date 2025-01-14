#Hough Transform
#It is a popular technique to detect any shape, if it can be represented in a mathematical form.
#It can even detect the detect if its broken or distorted.

#This algo involves
#Edge detection using Canny Edge Detection
#Mapping of edge point to Hough space and storage in acculmulator
#Interpretation of accumulator to yield lines of infinite length.It is done by thresholding and other constraints
#Conversion of infinite lines to finite lines



#In opencv there are two kinds of Jough transform
#Standard Hough transform(using Hough lines method)
#Probabilistic Hough line transform(using Hough LinesP method)

import cv2
import numpy as np


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\sudoku.png')

imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(imggray,50,150,apertureSize=3)
lines=cv2.HoughLines(edges,1,np.pi/180,200)   #This is standard hough transform.1st arg is the source.
                                              #2nd arg is distance resolution of accumulator in pixels.Normally its value is 1
                                              #3rd arg is angle resolution of accumulator in radians.
                                              #4th arg is accumulator threshold parameter.It returns lines having value > threshold

print(lines)

cv2.imshow('Image',img)
cv2.imshow('Grayscale',imggray)
cv2.imshow('Canny',edges)

for line in lines:
    rho,theta=line[0]                                    #Here the functioning is done using polar coordinates
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho

    x1=int(x0+1000*(-b))

    y1=int(y0+1000*(a))

    x2=int(x0-1000*(-b))

    y2=int(y0-1000*a)

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imshow('Image2',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
