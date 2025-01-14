import cv2
import datetime           #to import date and time

cap=cv2.VideoCapture(0)
ret=True
cap.set(3,1280)
cap.set(4,720)
while(ret):
    ret,frame=cap.read()
    font=cv2.FONT_HERSHEY_SIMPLEX     # for font type
    text="Widht: "+str(cap.get(3))+" Height: "+str(cap.get(4))
    datet=str(datetime.datetime.now())     #stores current date and time using datetime.now() method
    frame=cv2.putText(frame,text,(10,50),font,1,[0,120,0],1,cv2.LINE_AA)
    frame=cv2.putText(frame,datet,(800,700),font,1,[0,120,0],1,cv2.LINE_AA)
    cv2.imshow('dekho',frame)
    if(cv2.waitKey(1)==ord('c')):
        break
cap.release()
cv2.destroyAllWindows()
