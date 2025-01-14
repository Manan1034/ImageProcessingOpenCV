import cv2
import numpy as np
from matplotlib import pyplot as pt


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg')


b,g,r=cv2.split(img)

cv2.imshow('Image',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)


pt.hist(b.ravel(),256,[0,256])
pt.hist(g.ravel(),256,[0,256])
pt.hist(r.ravel(),256,[0,256])


pt.show()                #This overlaps all the histograms and show it in one frame

cv2.waitKey(0)
cv2.destroyAllWindows()
