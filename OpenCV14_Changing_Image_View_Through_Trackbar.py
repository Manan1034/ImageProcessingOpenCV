#Image conversion to gray with switch

import cv2

def nothing(x):
    print(x)

cv2.namedWindow('image')

cv2.createTrackbar('POS','image',10,400,nothing)

switch='color/gray'
cv2.createTrackbar('switch','image',0,1,nothing)

while(1):
    img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg')
    pos=cv2.getTrackbarPos('POS','image')
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(10,150),font,2,(0,0,255))

    s=cv2.getTrackbarPos('switch','image')
    if(s==0):
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

    k=cv2.waitKey(1)
    if(k==27):
        break
    cv2.imshow('image',img)
cv2.destroyAllWindows()
