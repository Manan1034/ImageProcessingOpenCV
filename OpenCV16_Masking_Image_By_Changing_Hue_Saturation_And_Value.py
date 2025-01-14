#controlling hue, saturation and value in real time video and masking the output

import cv2
import numpy as np

def nothing(x):
    pass
cap=cv2.VideoCapture(0)         #applying filter to a window
cv2.namedWindow('Track')
cv2.createTrackbar('LH','Track',0,255,nothing)       #creating trackbars for hue,saturation and value
cv2.createTrackbar('LS','Track',0,255,nothing)
cv2.createTrackbar('LV','Track',0,255,nothing)
cv2.createTrackbar('UH','Track',255,255,nothing)
cv2.createTrackbar('US','Track',255,255,nothing)
cv2.createTrackbar('UV','Track',255,255,nothing)

while(True):
    _,img=cap.read()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lh=cv2.getTrackbarPos('LH','Track')
    ls=cv2.getTrackbarPos('LS','Track')
    lv=cv2.getTrackbarPos('LV','Track')
    uh=cv2.getTrackbarPos('UH','Track')
    us=cv2.getTrackbarPos('US','Track')
    uv=cv2.getTrackbarPos('UV','Track')

    l_b=np.array([lh,ls,lv])       #it sets the lower value for hue,saturation and value
    u_b=np.array([uh,us,uv])       #it sets the upper value for hue, saturation and value

    mask=cv2.inRange(hsv,l_b,u_b)     #this creates a mask for setting the lower bound values and upper bound values in hsv image

    res=cv2.bitwise_and(img,img,mask=mask)      #it performs bitwise and which results in objects in range to be visible with three arguments
                                                #first and second are image itself and third is the mask which sets the range
    cv2.imshow('image',img)
    #cv2.imshow('image1',hsv)
    cv2.imshow('image2',mask)
    cv2.imshow('image3',res)
    if(cv2.waitKey(1)==27):
        break
cap.release()
cv2.destroyAllWindows()
