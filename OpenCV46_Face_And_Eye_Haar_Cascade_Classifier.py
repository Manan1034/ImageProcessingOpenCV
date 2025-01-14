import cv2


face_cascade=cv2.CascadeClassifier('F:\Python\OpenCV\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('F:\Python\OpenCV\opencv-master\opencv-master\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml')


cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.1,4)
    eye=eye_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    for (x,y,w,h) in eye:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow('Video',frame)

    if(cv2.waitKey(1)==ord(' ')):
        break

cv2.destroyAllWindows()
cap.release()



#We can also detect eyes using roi which is the output of face vector as eyes can not be outside the face.
#Then we can code with respect to region of interest
