import cv2

cap=cv2.VideoCapture(0)                 #Video capture class for capturing the frames and 0 defines the primary camera
fourcc=cv2.VideoWriter_fourcc(*'XVID')      #attribute is the four digit video code available at https://www.fourcc.org/codecs.php
out=cv2.VideoWriter('Result.avi',fourcc,20.0,(640,480))   #used to write video from captures(First is file name,second is video code
                                                            #third is no. of frames per second and fourth is the size for storing
while(True):
    ret,frame=cap.read()                        #ret returns true or false depending upon whether data is stored in frame or not
    #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    #return screen width
    #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   #return screen height
    out.write(frame)                            #writes the frames in a video form i.e. stores the video
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #converts frame from colorful to grayscale
    print(frame)
    cv2.imshow('ima',frame)      #shows the frames collected on screen
    if(cv2.waitKey(5)==ord('q')):        #will kill the program only when q is pressed
        break
cap.release()           #releasing the object
out.release()
cv2.destroyAllWindows()
