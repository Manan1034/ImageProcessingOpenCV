#masking and dilations using cv2.dilate

import cv2
import numpy as np
from matplotlib import pyplot as pt


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\smarties.png',cv2.IMREAD_GRAYSCALE)
#In second arg, we can also use 0 for grayscale


_,mask=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)


kernal=np.ones((2,2),np.uint8)   #kernal is used to remove the black dots in image.It is a small window of 2*2 pixels.
                                 #np.ones is used to create white image

dilation=cv2.dilate(mask,kernal,iterations=2)   #dilations is used to dilate the image i.e. to remove the small portions of complete image
                 #eg in case there is a shine on a particle in image. When we perform threshold.The shine can change its color depending
                 #on the threshold.Hence by dilation, we make the surface uniform and overlap the shiny surface with kernal

image=[img,mask,dilation]
titles=['Original','Masked','Dilated']

for i in range(3):
    pt.subplot(1,3,i+1)
    pt.imshow(image[i],'gray')  #First arg is the source and 2nd arg is mode in which image is presented
    pt.title(titles[i])         #This command gives titles to images

pt.show()
