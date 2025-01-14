#Probabilistic Hough Lines Method


import cv2
import numpy as np


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\sudoku.png')
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(imggray,50,120,apertureSize=3)
print(edges)

cv2.imshow('edges',edges)

lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
#This method directly return the edge coordinates of each line and not the value of rho and theta

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow('Final',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
