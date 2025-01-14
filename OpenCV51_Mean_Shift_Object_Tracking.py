#Mean shift object tracking

#Step 1-Pass the location of target object and histogram back projected image to mean shift function.
#Step 2-As object moves, the histogram back projected image also changes.
#Step 3-Mean shift function moves the window to new location with maximum probability density.
import cv2
import numpy as np

cap=cv2.VideoCapture('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\hellp1.avi')


#How to implement
#Take first frame of the video
ret,frame=cap.read()
#Setup initial location of window
x,y,h,w=600,200,200,100
track_window=(x,y,w,h)
#Setup the ROI for tracking
roi=frame[y:y+h,x:x+w]

cv2.imshow('ROI',roi)
hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
cv2.imshow('Hsv',hsv_roi)
mask=cv2.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255.)))        #inRange function has 3 arguments.1st is image
                                                                               #2nd is lower limit and 3rd is upper limit
#To neglect the false value due to low light, inRange function is used.
hist=cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])         #In hsv, the first value is of hue.
                                                            #so the 2nd argument is 0 for accessing the 1st value.
print(hist)

cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX)          #1st arg is source,2nd arg is destination,3rd arg is alpha and 4th arg is beeta
                                                        #5th arg is norm type
print(hist)
#The above steps from roi will give us the histogram back projected image

#Setup the termination criteria, either 10 iterations or move by exactly one point
term_crit=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10,1)      #10 is for no. of iterations and 1 is for one point shift
while(cap.isOpened()):
    ret,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dst=cv2.calcBackProject([hsv],[0],hist,[0,180],1)      #1st arg is the image,2nd arg is for hue thats why its 0
                                                         #3rd arg is for histogram,4th arg is the range,5th arg is scale
    #Apply mean shift to get new locations
    ret,track_window=cv2.meanShift(dst,track_window,term_crit)
                                   #1st arg is back projected image, 2nd arg is trackwindow and 3rd arg is criteria
    #Drawing rectangle on track window
    x,y,w,h=track_window
    final_img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0))

    cv2.imshow('Destination',dst)
    cv2.imshow('Frame',frame)
    cv2.imshow('Final_img',final_img)

    if(cv2.waitKey(100)==ord(" ")):
        break


cv2.destroyAllWindows()
cap.release()



#Limitations for Mean shift algirithm
#The size of moving window does not change
#We have to give initial position of roi

