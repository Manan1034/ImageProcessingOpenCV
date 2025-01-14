#color changing through trackbars

import cv2
import numpy as np

def nothing(x):                #a function which print the value of track bar
    return None                 #here x stores the value of the trackbar

cv2.namedWindow('image')       #naming the output window as image
img=np.zeros((512,512,3),np.uint8)

cv2.createTrackbar('B','image',0,255,nothing)    #trackbar 1 for blue.1st arg is name, 2nd is window for trackbar,
                                                 #3 is min and 4th is max value and fifth is a function which print value of trackbar
cv2.createTrackbar('G','image',0,255,nothing)    #There can be multiple trackbars for every image
cv2.createTrackbar('R','image',0,255,nothing)
switch='0:OFF\n 1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    if(cv2.waitKey(1)==27):      #to change the color,put value 1 in waitKey
        break
    b=cv2.getTrackbarPos('B','image')   #records the position of trackbar for B
    g=cv2.getTrackbarPos('G','image')   #records the position of trackbar for G
    r=cv2.getTrackbarPos('R','image')   #records the position of trackbar for R
    s=cv2.getTrackbarPos(switch,'image')

    if(s==0):
        img[:]=0
    else:
        img[:]=[b,g,r]       #fill the whole image with these colors
cv2.destroyAllWindows()
