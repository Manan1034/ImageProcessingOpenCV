#It shows the color of the point on which a left click is made


import cv2
import numpy as np


def click_event(event,x,y,frame,param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]

        cv2.circle(img,(x,y),3,[255,0,0],-1)
        color=np.zeros([512,512,3],np.uint8)
        color[:]=[blue,green,red]     #it fill the whole color image with the mentioned color

        cv2.imshow('color',color)     #it opens a new window color

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg',-1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
