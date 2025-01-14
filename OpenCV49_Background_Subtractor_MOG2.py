import cv2


cap=cv2.VideoCapture('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\hellp1.avi')

#cap.set(cv2.CAP_PROP_FPS, 10)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)       #Is is a gaussian mixtue base bakground and foregroung segmentation algorithm
                                                      #It has optional parameter like history, no. of gaussian mixtures, threshold.
                                                      #These values are set by default.We can provide input if we need to change.  
while(cap.isOpened()):
    ret,frame=cap.read()

    fgmask=fgbg.apply(frame)
    
    cv2.imshow('Frame',frame)
    cv2.imshow('fgFrame',fgmask)

    if(cv2.waitKey(30)==ord(" ")):                #The value of waitKey decides the fps of output video
       break

cv2.destroyAllWindows()
cap.release()
