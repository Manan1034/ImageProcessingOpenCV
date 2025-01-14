#shows all the mouse events and print pixel coordiantes for left click and color triplet on right click.

import cv2
import numpy as np

for i in dir(cv2):                      #These will tell about all the mouse events in library cv2
    if("EVENT" in i):
        print(i)
def click_event(event,x,y,flags,param):     #These arguments will remain the same always
    if(event==cv2.EVENT_LBUTTONDOWN):       #check for the mouse left button click
        print(x,' ',y)
        font=cv2.FONT_HERSHEY_SIMPLEX       #font style
        strx=str(x)+' '+str(y)
        cv2.putText(img,strx,(x,y),font,1,(255,0,255),1)    #using putText method
        cv2.imshow('image',img)      #naming the window as image
    if(event==cv2.EVENT_RBUTTONDOWN):     #check for the  mouse right button click
        blue=img[y,x,0]                #y and x are coordinates and 0 is subscript for blue
        green=img[y,x,1]               # 1 is subscript for green
        red=img[y,x,2]                 # 2 is subscript for red
        font=cv2.FONT_HERSHEY_SIMPLEX
        strB=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strB,(x,y),font,0.5,[255,255,255],1)
        cv2.imshow('image',img)
img=np.zeros((512,512,3),np.uint8)     #creating the black screen using numpy
cv2.imshow('image',img)                #the name of the window should be same everywhere throughout the program

cv2.setMouseCallback('image',click_event)  #mouseCallback event checks for any event of mouse

cv2.waitKey(0)
cv2.destroyAllWindows()
