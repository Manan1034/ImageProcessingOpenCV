#Contours are curves joining all the continuous points along the boundary which are having the same color or intensity
#This is a tool for shape analysis , object detection and object recognition
#We use binary images for finding the contours for better accuracy


#Convert the image in binary image
#Then either apply threshold or Canny Edge detection to find contours



import cv2


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\opencv-logo.png')
img_gs=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)        #Converts the image to grayscale mode



ret,thr=cv2.threshold(img_gs,200,255,0)         #Here 0 in 4th arg depicts Binary threshold

contours,heirarchy=cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
                                               #This is method of finding contours
                                               #contours is the list of all the contours in the image.
                                               #Each contour is a numpy array of (x,y) of boundary points of the object
                                               #heirarchy is optional output vector containing info about image topology
                                               #1st arg is source,2nd arg is contour retrieval mode,
                                               #3rd arg is contour approximation method
print("Number of contours = "+str(len(contours)))
print(contours[0])



#Drawing contours on the image
cv2.drawContours(img,contours,-1,(0,0,0),3)     #This method draws contours on image.
                                                  #1st arg is original image as we want to show on original
                                                  #2nd arg is the contours list.
                                                  #3rd arg is contours indexes.If this arg is -1,then it shows all contours
                                                  #Otherwise it shows just the  mentioned contour index
                                                  #4th arg is color.
                                                  #5th arg is thickness

cv2.imshow('rayscale',img_gs)
cv2.imshow('Threshold',thr)
cv2.imshow('Original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
