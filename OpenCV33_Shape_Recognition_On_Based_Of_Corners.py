import cv2


img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\shapes1.png')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(imgGray,240,255,cv2.THRESH_BINARY)

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)   #This function approximates polygonal curve with specific precision
                                            #1st arg is contour or shape,2nd is epsilon-perimeter specifying the approximation accuracy
                                            #3rd arg for approxPolyDp is whether shape is closed or open.True for closed.
                                            #arcLength() calculates the contour perimeter or curve length.It has 2 arguments
                                            #1st arg is contour and 2nd arg is whether the contour is closed or open.True for closed

    cv2.drawContours(img,[approx],0,[0,255,0],5)
    #Finding x and y coordinates for writing names
    x=approx.ravel()[0]       #ravel()[0] stores the x coordinate
    y=approx.ravel()[1]

    #Deciding shape for polygons
    if(len(approx)==3):                            #approx stores the no. of edges
        cv2.putText(img,'Triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    elif(len(approx)==4):

        #Deciding for square and rectangle
        x1,y1,w,h=cv2.boundingRect(approx)
        asra=float(w/h)
        if(0.95<=asra<=1.05):
            cv2.putText(img,'Square',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else:
            cv2.putText(img,'Rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        print(asra)
    elif(len(approx)==5):
        cv2.putText(img,'Pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    elif(len(approx)==10):
        cv2.putText(img,'Star',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    else:
        cv2.putText(img,'Circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))


cv2.imshow('Image',img)
cv2.imshow('Gray Image',imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()
