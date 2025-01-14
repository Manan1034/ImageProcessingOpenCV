#Blurring in image

import cv2
import numpy as np
from matplotlib import pyplot as pt



img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\salt_and_pepper.png')

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)       #Mode is changed as matplotlib reads image in RGB format.Opencv reads image in BGR format.

kernel=np.ones((5,5),np.float32)/25           #For homogenous filter,we have to devide the np.ones array by (no.of rows*no.of coulmns)
                                              #In homogenous filter, we use the mean weight kernel for filtering

dst=cv2.filter2D(img,-3,kernel)               #This is a filter.1st arg is source,2nd arg is depth and 3rd arg is kernel

blur=cv2.blur(img,(5,5))                      #This is used to blur the image.1st arg is source and 2nd arg is the kernel size

gblur=cv2.GaussianBlur(img,(5,5),1)           #This is gaussian blur. In this the kernel matrix is not constant valued but variating.
                                              #1st arg is source,2nd arg is kernel and 3rd arg is sigma-x value
                                              #The values increase while moving to center and decrease while moving away from center.
                                              #The edges are not sharp in gaussian blur. It removes high frequency noise from image


median=cv2.medianBlur(img,5)                  #This is median filter.In this the kernal size must be always odd and never equal to 1.
                                              #This assigns values by taking medians of neighbouring pixels.2nd arg is kernel size
                                              #if we provide the kernal size as 1.It will show the original image.
                                              #It removes all the salt and pepper noise i.e. balck and white grainy noise.

image=[img,dst,blur,gblur,median]
titles=['Original','Homogenous Filter','Blurred Image','Gaussian Blur','Median Filter']

for i in range(5):
    pt.subplot(2,3,i+1)
    pt.xticks([])
    pt.yticks([])
    pt.imshow(image[i])
    pt.title(titles[i])


pt.show()
#In 1-D there are two filters-Low pass filters(LPF) and High pass filters(HPF)
#LPF are used to remove noise and blurr the image
#HPF are used to find edges in the image
