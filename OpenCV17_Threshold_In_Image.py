#Applying threshold in image

import cv2

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\gradient.png')
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)    #Storing information for threshold
                                                      #_ before th1 stores the value of res i.e. true or false
                                                      #First arg is image,second is threshold value,third is max value,
                                                      #and last threshold filter
#THRESH_BINARY mode sets only two colors.Pixels lower than threshold becomes 0 and rest convert to max(3rd arg)
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#THRESH_BINARY_INV works opposite to THRESH_BINARY.Values lower than threshold are set to max and rest to zero
_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#THRESH_TRUNC does not change the pixels lower than threshold. For pixels more than threshold, value remains constant as threshold.
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#THRESH_TOZERO changes the values of all pixels lesser than threshold to zero
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#THRESH_TOZERO_INV works opposite to THRESH_TOZERO. and sets the pixel value greater then threshold to zero

cv2.imshow('image',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)
cv2.imshow('th5',th5)


cv2.waitKey(0)
cv2.destroyAllWindows()
