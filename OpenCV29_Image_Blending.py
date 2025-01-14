#Image blending
#For image blending, the size of the images must be same.You can blend as many images as you want.
#The first section defines the rows to be included.The data after comma defines the no. of columns


import cv2
import numpy as np



apple=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\Apple.jpg')
orange=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\orange.jpg')


cv2.imshow('Apple',apple)
cv2.imshow('Orange',orange)


print(apple.shape)
print(orange.shape)    #shape tells about the size of the image.length*breadth*no. of pixels


app_ora=np.hstack((orange[:, :200],apple[:,201:300],orange[:, 300:]))     #Since the size of image is 512*512.256 will show the half image of the whole image
                                                        #The image mentioned first in bracket will be on left
                                                        #The images mentioned later will come on the right
                                                        #The coordinates tells about the portion of image to be included.
                                                        #The size of the images must be same


cv2.imshow('Blended Image',app_ora)        #This blended image can be easily noticed due to a sharp line between the merging
                                           #which can be removed using image pyramids

cv2.waitKey(0)
cv2.destroyAllWindows()
