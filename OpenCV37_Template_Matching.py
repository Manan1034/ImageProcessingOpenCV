#Template matching-Checking whether a portion is present in the image or not.


import cv2
import numpy as np


img=cv2.imread("F:\Python\OpenCV\opencv-master\opencv-master\samples\data\messi5.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

temp=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\messiface.jpg',cv2.IMREAD_GRAYSCALE)

#Types of template matching operations are available at https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCORR_NORMED)    #1st arg is source,2nd arg is template,3rd arg is type of matching


print(res)      #The brightest point would be there where the top left corner of the template will match the point in the image

#The would be a value in res where the value of pixel would be maximum.This will be the point
#where the top left corner of template will be in the source image.

#Finding the brightest point
#The brightest point would be having pixel value near to 0.8
threshold=0.99

loc=np.where(res>=threshold)

print(loc)

#Now since we have the brightest point, we will construct a rectangle from brightest point of the size of template in order to match

#Finding width and height of template

w,h=temp.shape[::-1]      #It means we want the value of columns and rows in reverse order.1st result of shape is column and 2nd is row

#We are going to iterate over every point in order to know if there could be other templates

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(255,255,255),3,cv2.LINE_AA)
    
cv2.imshow('Image',img)
cv2.imshow('Template',temp)

cv2.waitKey(0)
cv2.destroyAllWindows()
