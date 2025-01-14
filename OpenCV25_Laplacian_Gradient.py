#Finding laplacian gradient of image


import cv2
import numpy as np
from matplotlib import pyplot as pt


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\sudoku.png',0)          #Reading image in grayscale
lap=cv2.Laplacian(img,cv2.CV_64F)        #used to find laplace gradient
                                         #first arg is image,2nd arg is datatype(We are using 64F where it is 64 bit float)
                                         #This datatype is used to hadle the negative slope
                                         #which is induced due to reading image in grayscale mode


                                         #The laplacian filter detects the edges and color them white.
                                         #The rest of image is turned black.

lap2=cv2.Laplacian(img,cv2.CV_64F,ksize=1)   #The 3rd arg is kernal size.It is optional.The lower the kernal size the better the image
                                             #We have to use alias to specify that it is a kernal size.
sobx=cv2.Sobel(img,cv2.CV_64F,1,0)           #This is the Soble method.In this 1st arg is image,2nd arg is datatype,3rd arg is dx(0 or 1)
                                             #dx=1 means this is sobelx method.4th arg is dy.dx is order of derivative x
                                             #dy is order of derivative y . 5th arg can be ksize dfoe kernal size
soby=cv2.Sobel(img,cv2.CV_64F,0,1)

lap=np.uint8(np.absolute(lap))           #It is to convert the laplace gradient value to absolute value and
                                         #convert it to unsigned int to make it suitable for output as a image
sobx=np.uint8(np.absolute(sobx))
soby=np.uint8(np.absolute(soby))
lap2=np.uint8(np.absolute(lap2))
sobcomb=cv2.bitwise_or(sobx,soby)
titles=['image','Laplacian Gradient','Laplace with kernal','Sobelx','Sobely','Combined sobel image']
images=[img,lap,lap2,sobx,soby,sobcomb]

for i in range(6):
    pt.subplot(3,2,i+1)
    pt.imshow(images[i],'gray')
    pt.title(titles[i])
    pt.xticks([])
    pt.yticks([])


pt.show()



#Image gradient is the directional change in the intensity or the color in an image.
#In sobelx gradient, the change in direction of intensity is in the x direction. We see vertical lines in this gradient
#In sobely gradient, the change in direction of intensity is in the y direction. 1we see horizontal lines in this gradient.
