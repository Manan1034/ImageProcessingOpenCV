#Laplacian Pyramid

import cv2


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg')
frame=img.copy()
gp=[frame]
for i in range(5):
    frame=cv2.pyrDown(frame)
    gp.append(frame)
    cv2.imshow(str(i+1),frame)

layer=gp[5]
cv2.imshow('Upper level Gaussian Pyramid',layer)
for i in range(5,0,-1):
    g_e=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],g_e)
    cv2.imshow(str(i),laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()




#Laplacian pyramid works similar to edge detection algorithms
#Role of these pyramids is to blend the images and reconstruction of images 
