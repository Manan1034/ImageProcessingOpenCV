#Lane Detection in video


import cv2
import numpy as np
import matplotlib.pyplot as pt

def region_of_interest(img2,vertices):                    # to extract the region of interest
    mask=np.zeros_like(img2)                              #Used to create a black image of the size of image
    
    #We do not need color channels as our image is grayscale image
    match_mask_color=255
    cv2.fillPoly(mask,vertices,match_mask_color)

    masked_image=cv2.bitwise_and(img2,mask)
    return masked_image

#Now drawing lines
def draw_the_lines(img,lines):
    cimg=np.copy(img)
    lineimg=np.zeros((img.shape[0],img.shape[1],3),np.uint8)      #This is the blank image for printing lines
                                                                  #We will later merge it with original image
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(lineimg,(x1,y1),(x2,y2),(0,255,0),2)

    img=cv2.addWeighted(img,0.8,lineimg,1,0.0)         #1st arg is 1st image,2nd arg is alpha or its weight
                                                       #3rd arg is 2nd image,4th arg is beta and 5th arg is gamma
    return img
    
def process(img2):
    print(img2.shape)         #it shows height at 0th pos, width at 1st pos and no. of channels at 3rd
    h=img2.shape[0]
    w=img2.shape[1]
    
    roi=[(0,h),(w/2,h/2),(w,h)]
    
    gray_img=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
    cimg=cv2.Canny(gray_img,150,200)
    
    cropp_image=region_of_interest(cimg,np.array([roi],np.int32))
    
    lines=cv2.HoughLinesP(cropp_image,rho=2 ,theta=np.pi/60,threshold=50,lines=np.array([]),minLineLength=40,maxLineGap=100)
    
    finalimg=draw_the_lines(img2,lines)
    return finalimg

cap=cv2.VideoCapture()
while(cap.isOpened()):
    _,frame=cap.read()
    frame=process(frame)
    cv2.imshow('Output',frame)
    if(cv2.waitKey(1)==ord('q')):
       break

cv2.destroyAllWindows()
cap.release() 
