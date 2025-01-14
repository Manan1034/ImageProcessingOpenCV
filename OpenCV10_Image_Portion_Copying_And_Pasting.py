#Copying the entities of image and pasting it at any location

import cv2

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\messi5.jpg')

print(img.shape)      #tells about the size of image(len,width,no. of color pixels)
print(img.size)       #tells the total number of pixels in the image
print(img.dtype)      #tells about the data type used

b,g,r=cv2.split(img)  #stores the color triplets of bgr for each section of image
print(b,g,r)
color=cv2.merge([b,g,r])#merges the brg of every pixel in the image i order to get the image back

ball=color[280:340 , 330:390]    #stored the coordinates of ball in the variable ball using mouse click event
                                 #This is also known as the region of Interest
color[273:333 , 100:160]=ball    #stored the value of ball to the new place where we want to copy the object

cv2.imshow('color',color)
cv2.waitKey(0)
cv2.destroyAllWindows()
