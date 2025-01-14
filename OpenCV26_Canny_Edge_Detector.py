#Canny Edge detector is an edge detection operator that uses a multi stage algorithm to detect the wide range of edges in image
#Steps in Canny edge detector
#1. Noise reduction to apply gaussian filter to smooth the image to remove the noise
#2. Gradient calculation
#3. Non maximum suppression to get rid of spurrier response to edge detection
#4. Double threshold to determine potential edges
#5. Edge tracking by Hysteresis

import cv2
import numpy as np
from matplotlib import pyplot as pt


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\messi5.jpg',cv2.IMREAD_GRAYSCALE)

cn=cv2.Canny(img,100,200)          #This is the Canny function
                                   #1st arg is the source,2nd arg is the first threshold, 3rd arg is the second threshold 

image=[img,cn]
title=['Image','Canny Edge Detection']

for i in range(2):
    pt.subplot(2,1,i+1)
    pt.imshow(image[i],'gray')
    pt.title(title[i])
    pt.xticks([])
    pt.yticks([])



pt.show()



#In difference to the laplacian and sobel methods, this algorithm removes all the noise and provide with the true edges
#For grayscale image,you must have source from opencv in grayscale as well as the output for pyplot.imshow must be mentioned as gray.
