#Detecting face from a image

import cv2

face_cascade=cv2.CascadeClassifier('F:\Python\OpenCV\haarcascade_frontalface_default.xml')


cap=cv2.VideoCapture(0)
while(True):
    _,frame=cap.read()
    frame2=frame
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(frame,1.1,4)
             #1st arg is image,2nd arg is image scale i.e. how much is the image reduced at each scale
             #3rd arg is minNeighbours i.e. the minimum no. of neighbours each rectangle will retain.
             #This face variable will return the vector of rectangles on each face.

    for (x,y,w,h) in face:
        cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Image",frame2)
    if(cv2.waitKey(1)==ord(" ")):
        break
cv2.destroyAllWindows()
cap.release()
