#Harris Corner Detection
#Corners are region in image with large variation of intensity in all directions

#Steps for Harris Corner Detector
#1. Determine which windows produce very large variations in intensity when moved in both x and y directions.
#2. With each such window found, a score R is calculated.
#3. After applying a threshold to this score, important corners are selected and marked.

import cv2
import numpy as np

#cv2.namedWindow("Image", cv2.WINDOW_NORMAL)            this fucntion creates an empty named window of full screensize     
#cv2.namedWindow("Final image", cv2.WINDOW_NORMAL)
img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\chessboard.png')

cv2.imshow("Image",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)        #To get better results

#Harris Corner requires image in float32 format hence converting the image to float32 format

gray=np.float32(gray)

dst=cv2.cornerHarris(gray,2,3,0.04)
                     #1st arg is image in float data type, 2nd arg is block size
                     #3rd arg is ksize i.e. the aperture parameter for sobel operation.4th arg is Harrish detector free parameter
#We will dilate the result image for better result

dst=cv2.dilate(dst,None)

#Now we will revert back to original image by using optimal threshold value

img[dst>0.01* dst.max()]=[0,0,255]    #In this we are marking all the corners with red color

cv2.imshow("Final image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
