#Intensity distribution

import cv2
import numpy as np
from matplotlib import pyplot as pt



img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg',cv2.IMREAD_GRAYSCALE)

##cv2.rectangle(img,(0,100),(200,200),(255),-1,cv2.LINE_AA)


#cv2.rectangle(img,(0,50),(100,100),(127),-1,cv2.LINE_AA)

pt.hist(img.ravel(),256,[0,256])    #This method helps to find histogram of the image
                                    #1st arg is source info using ravel() function.2nd arg is maximum pixel.3rd arg is the range
                                    #Since the image is gryscale image, it is must easier to find histogram of such image
                                    #y axis has no. of pixels and x axis has the pixel value

#Histogram gives the idea about the intensity distribution of an image.It is another way of understanding the image
#We can know about contrast , brightness and intensity distribution with the help of histogram of the image



cv2.imshow('Image',img)
pt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()
