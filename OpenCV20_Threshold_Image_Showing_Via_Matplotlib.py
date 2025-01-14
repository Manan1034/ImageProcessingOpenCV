#Printing threshold images via matplotlib

import cv2
from matplotlib import pyplot as pt

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\gradient.png')
_,th1=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)


titles=['Original','Binary','Binary Inverse','Trunc','ToZero','ToZero Inverse']
images=[img,th1,th2,th3,th4,th5]

for i in range(6):
    pt.subplot(2,3,i+1)          #It plots multiple images in single frame. First arg is no. of rows, second is no. of columns
                                  #third arg is subscript of image
    pt.imshow(images[i],'gray')  #It is showing the image. The second arg in this tell about the mode in which image should be displayed


pt.show()
