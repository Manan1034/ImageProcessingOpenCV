#Morphology 

import cv2
from matplotlib import pyplot as pt
import numpy as np

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\smarties.png',cv2.IMREAD_GRAYSCALE)

_,mask=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)

kernal=np.ones((2,2),np.uint8)

erosion =cv2.erode(mask,kernal,iterations=1)    #Erosion clears the boundaries of objects using kernal
                                                #1st arg is source, 2nd arg is kernal or image which will perform the erosion
                                                #3rd arg is no. of iterations,i.e. no. of times we will perform the operation
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)    #opening is another morphological operation. In this,fisrt erosion is performed
                                                        #followed by dilation
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)   #In closing,first dilation is performed followed by erosion
                                                        #Closing is just opposite to opening
morgrad=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)  #This is the difference between dilation and erosion
tophat=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)     #This is the difference between image and opening of image
                                                          #These two are like the set differences.

image=[img,mask,erosion,opening,closing,morgrad,tophat]       
title=['Original','Mask','Eroded','Opening','Closing','MorGrad','TopHat']

for i in range(7):
    pt.subplot(3,3,i+1)
    pt.imshow(image[i],'gray')
    pt.xticks([])
    pt.yticks([])
    pt.title(title[i])

pt.show()
