import cv2

cap=cv2.VideoCapture("F:\Python\OpenCV\opencv-master\opencv-master\samples\data\hellp1.avi")


fgbg=cv2.createBackgroundSubtractorKNN(detectShadows=False)

while(cap.isOpened()):
    _,frame=cap.read()

    fg=fgbg.apply(frame)

    cv2.imshow('Original',frame)
    cv2.imshow('Filtered',fg)

    if(cv2.waitKey(30)==ord(" ")):
        break


cv2.destroyAllWindows()
cap.release()
