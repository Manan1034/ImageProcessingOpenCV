#Pyramid Representation is a type of multiscale signal representation in which a signal or an image is subject to repeated smoothing
#and subsampling
#There are two types of pyramids in open cv-Gaussian pyramid and laplacian pyramid
#Gaussian Pyramid- Repeat filtering and sub-sampling the image.There are two fucntions for this-pyrup and pyrdown
#Laplacian Pyramids- These are formed from gaussian pyramids.Laplacian Pyramid is formed by the difference between that level in
#Gaussian pyramid and expanded version of its upper level in Gaussian pyramid




import cv2

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg')


pyrdown=cv2.pyrDown(img)      #This is pyrDown method.This reduces resolution to 1/4th of the original size. Image quality remains same.
pyrup=cv2.pyrUp(img)          #This is pyrUp method.This increases the resolution to 4 times the original size. THe result is blurred
                              #as we do not have the sufficient information for each pixel.


cv2.imshow('Original Image',img)
cv2.imshow('Gaussian Pyrdown',pyrdown)
cv2.imshow('Gaussian Pyrup',pyrup)

cv2.waitKey(0)
cv2.destroyAllWindows()
