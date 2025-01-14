import cv2

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg',-1) #reads image using imread with image location
                                                                            #1 for colored image,0 for grayscale and -1 for original
cv2.imshow('image', img)  #will show the screen with label image and collect data from img object
k=cv2.waitKey(5000)     #waits for the time in microsecond before killing the program
print(k)
cv2.destroyAllWindows()       #destroy all the windows
cv2.imwrite('lenacopy.png',img)            #will save the image with the name lenacopy.png using imwrite()
