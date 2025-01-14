#To blend the images properly, five steps are to be followed
#Load the images
#Find gaussian pyramids for both images upto certain levels
#Find laplacian pyramids
#Join the portions of image in each of the laplacian pyramid levels
#Finally from joint image pyramids,construct the real image




import cv2
import numpy as np


apple=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\Apple.jpg')
orange=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\orange.jpg')


#Creating Gaussian pyramid for apple
apple_c=apple.copy()
gp_apple=[apple_c]

for i in range(6):
    apple_c=cv2.pyrDown(apple_c)
    gp_apple.append(apple_c)


#Creating Gaussian pyramid for orange
orange_c=orange.copy()
gp_orange=[orange_c]

for i in range(6):
    orange_c=cv2.pyrDown(orange_c)
    gp_orange.append(orange_c)

#Creating laplacian pyramid for apple
apple_c=gp_apple[5]
lp_apple=[apple_c]
for i in range(5,0,-1):
    gp_extended=cv2.pyrUp(gp_apple[i])
    laplacian=cv2.subtract(gp_apple[i-1],gp_extended)
    lp_apple.append(laplacian)
    #cv2.imshow(str(i),laplacian)
    

#Creating laplacian pyramid for orange
orange_c=gp_orange[5]
lp_orange=[orange_c]
for i in range(5,0,-1):
    gp_extended=cv2.pyrUp(gp_orange[i])
    laplacian=cv2.subtract(gp_orange[i-1],gp_extended)
    lp_orange.append(laplacian)
    #cv2.imshow(str(i),laplacian)
    



#Merging the two images
apporapyr=[]
n=0

for apple_l,orange_l in zip(lp_apple,lp_orange):
    n+=1
    cols,rows,chl=apple_l.shape
    laplacian=np.hstack((apple_l[:,0:int(cols/2)],orange_l[:, int(cols/2):]))
    apporapyr.append(laplacian)
    i=0
    i=i+1
    cv2.imshow(str(i),laplacian)
print(apporapyr)




#Reconstructing the image
apporarec=apporapyr[0]
cv2.imshow('Zero',apporarec)

for i in range(1,6):
    apporarec=cv2.pyrUp(apporarec)
    apporarec=cv2.add(apporapyr[i],apporarec)
    #cv2.imshow(str(i),apporarec)



cv2.imshow('Apple_Orange_Reconstructed',apporarec)
cv2.waitKey(0)
cv2.destroyAllWindows()
