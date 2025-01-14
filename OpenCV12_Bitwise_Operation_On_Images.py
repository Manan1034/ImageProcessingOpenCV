#Performing bitwise operation son images

import cv2
import numpy as np


img1=np.zeros([250,500,3],np.uint8)
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\chessboard.png')
img2=cv2.resize(img2,(500,250))  #resize takes attributes in height ,length

bitAnd=cv2.bitwise_and(img1,img2)   #performs and operation on two images img1 and img2
bitOr=cv2.bitwise_or(img1,img2)     #performs or operation on two images img1 and img2
bitxor=cv2.bitwise_xor(img1,img2)   #performs xor operation on two images
bitnor=cv2.bitwise_not(img1)        #perorms not operation on the image

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
#cv2.imshow('bitand',bitAnd)
#cv2.imshow('birot',bitOr)
cv2.imshow('bitxor',bitxor)
cv2.imshow('bitnot',bitnor)

cv2.waitKey(0)
cv2.destroyAllWindows()
