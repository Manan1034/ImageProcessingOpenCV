#Adaptive Threshold

import cv2

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\sudoku.png',0)   #adaptive threshold only work for greyscale mode

#_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,5) #first arg is source,second is max pixel
                                                                                       #third is adaptive threshold type
                                                                                       #fourth is threshold type
                                                                                       #fifth is block size(always odd)
                                                                                       #sixth is a constant to substract from each pixel
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,5)
cv2.imshow('image',img)
#cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''In adoptive threshold , the threshold value is not global.
It varies from region to region in the image depending on the value of the neughbouring pixels.
In this, we have two types of adoptive thresholding,mean and gaussian.'''

