#For single click, there will be a click
#For more than 2 points, the points will be connected with a line.

import cv2
import numpy as np

def chech_event(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img,(x,y),3,(0,0,255),-1)   #if these is only 1 left click,it will be a point
        point.append((x,y))
        if(len(point)>=2):
            cv2.line(img,point[-1],point[-2],(255,0,0),5)   #it will connect two points
        cv2.imshow('image',img)
img=np.zeros((512,512,3),np.uint8)
point=[]
cv2.imshow('image',img)

cv2.setMouseCallback('image',chech_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
