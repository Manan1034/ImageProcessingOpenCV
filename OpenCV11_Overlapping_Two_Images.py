#Overlapping two images depending on their weight

import cv2

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\messi5.jpg')
img2=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\opencv-logo-white.png')

img=cv2.resize(img,(512,512))        #resizing the image
img2=cv2.resize(img2,(512,512))      #resizing the image
#dst=cv2.add(img2,img)                #adding only two images.Images can only be added when the size of both images is the same
dst=cv2.addWeighted(img,0.7,img2,0.3,0)    #in this we can change the percentage of images visible by assigning weights
cv2.imshow('destination',dst)
print(dst.shape)
cv2.waitKey(5000)
cv2.destroyAllWindows()
