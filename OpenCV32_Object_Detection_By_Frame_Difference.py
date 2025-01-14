#Object detection by frame difference


import cv2


cap=cv2.VideoCapture('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\hellp1.avi')


ret,frame1=cap.read()            #Generating frame1 for cap
#cv2.imshow('Frame1',frame1)
ret,frame2=cap.read()            #Generating frame2 for cap
#cv2.imshow('Frame2',frame2)

while(cap.isOpened()):
    diff=cv2.absdiff(frame1,frame2)     #absdiff is for absolute difference to check the difference in frame1 and frame2
    #cv2.imshow('Diff',diff)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)    #converting diff to grayscale in order to find contours
    #cv2.imshow('Gray',gray)
    blurr=cv2.GaussianBlur(gray,(5,5),0)        #Applying gaussian blur to grayscale image
    #cv2.imshow('blurr',blurr)
    _,thresh=cv2.threshold(blurr,20,255,cv2.THRESH_BINARY)
    #cv2.imshow('THresh',thresh)
    #Now dilating the image to fill the voids in order to find the better contours

    dilated=cv2.dilate(thresh,None,iterations=3)     #This method is used to dilate the image
                                                     #1st arg is source,2nd arg is kernal size,3rd arg is no. of iterations
                                                     #We can change no. of iterations as per requirements

    
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow('Dilate',dilated)

    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)      #These draw contours that are outlining the edges of moving objects


    #For developing rectangles on moving objects
    for contour in contours:
        x,y,w,h=cv2.boundingRect(contour)         #this method tells about the x coordinate, y coordinate, width and height of rect

        #Finding contour area
        if(cv2.contourArea(contour)<700):        #This method tells about the contour area it is enclosing
            continue                             #This if statement will not print contours having area less than 700
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)     #this will draw a rectangle on contour with area >700

        #Putting text on image
        cv2.putText(frame1,"Status={}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)


        
    cv2.imshow('Frame1',frame1)

    frame1=frame2                           #Here we are copying the values of frame 2 to frame 1 in order to continue moving
    ret,frame2=cap.read()                   #Here we are reading the new frame
    
    if(cv2.waitKey(10)==27):
        break


cv2.destroyAllWindows()
cap.release()
