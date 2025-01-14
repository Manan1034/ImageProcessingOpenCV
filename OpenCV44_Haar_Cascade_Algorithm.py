#Detecting face from a image

import cv2

face_cascade=cv2.CascadeClassifier('F:\Python\OpenCV\haarcascade_frontalface_default.xml')


img2=cv2.imread('F:\Docs\Manan docs\DSC_8860.jpg')
#cv2.imshow('Original',img2)
img=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(img,1.1,4)
             #1st arg is image,2nd arg is image scale i.e. how much is the image reduced at each scale
             #3rd arg is minNeighbours i.e. the minimum no. of neighbours each rectangle will retain.
             #This face variable will return the vector of rectangles on each face.

for (x,y,w,h) in face:
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
