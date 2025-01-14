#Detecting face from a video

import cv2

body_cascade=cv2.CascadeClassifier('F:\Python\OpenCV\opencv-master\opencv-master\data\haarcascades\haarcascade_fullbody.xml')


cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=body_cascade.detectMultiScale(gray,1.1,3)

    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('Video',frame)
    if(cv2.waitKey(1)==ord(' ')):
        break

cv2.destroyAllWindows()
cap.release()

