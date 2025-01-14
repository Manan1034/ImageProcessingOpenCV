#Lane Detection
#Finding Mask 

import cv2
import numpy as np
import matplotlib.pyplot as pt

def region_of_interest(img2,vertices):                    # to extract the region of interest
    mask=np.zeros_like(img2)                              #Used to create a black image of the size of image
    cv2.imshow('Mask',mask)
    print(mask.shape)

    #Retrieving color channels
    channel_count=img2.shape[2]
    match_mask_color=(255,) * channel_count
    cv2.fillPoly(mask,vertices,match_mask_color)
    cv2.imshow('Mask',mask)
    masked_image=cv2.bitwise_and(img2,mask)
    return masked_image


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\Road.jpg')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


print(img2.shape)         #it shows height at 0th pos, width at 1st pos and no. of channels at 3rd
h=img2.shape[0]
w=img2.shape[1]

roi=[(0,h),(w/2,h/2),(w,h)]


cropp_image=region_of_interest(img2,np.array([roi],np.int32))



pt.imshow(cropp_image)
pt.show()
                 
cv2.waitKey(0)
cv2.destroyAllWindows()
