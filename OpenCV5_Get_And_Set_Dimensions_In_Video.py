import cv2
cap=cv2.VideoCapture(0)
cap.set(3,1000)    #sets width for the captured frame.3 is alias for CAP_PROP_FRAME_WIDTH
cap.set(4,1000)     #sets height for the captured frame.4 is the alias for CAP_PROP_FRAME_HEIGHT
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret==True):
        cv2.imshow('image',frame)
        if(cv2.waitKey(1)==ord('c')):
            break
cv2.destroyAllWindows()
cap.release()
