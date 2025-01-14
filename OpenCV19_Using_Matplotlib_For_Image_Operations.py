#using matplotlib to display image

import cv2
from matplotlib import pyplot as pt

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg')
pt.imshow(img)      #Showing image by matplotlib. This loads the image
pt.show()           #this functions shows the image
                    #opencv reads image in BGR format while matplotlib reads in RGB format
                    #The two images are different due to their different formats

#To get the exact result as opencv
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
pt.imshow(img1)
pt.xticks([])       #It removes the scale from x axis
pt.yticks([])       #It removes the scale from y axis
pt.show()           #The save button on putput window saves image in png format 
cv2.waitKey(0)
cv2.destroyAllWindows()
