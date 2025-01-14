import cv2
img=cv2.imread("F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg",-1)

img=cv2.line(img,(0,0),(200,200),(255,255,0),6) #to draw a line
                                                #second arg is starting point
                                                #third arg is last point
                                                #fourth arg is color in BGR form you can see color from rgb color picker from browser
                                                #fifth arg is thickness
img=cv2.arrowedLine(img,(50,100),(50,500),(255,0,255),3)  #this function is to draw the arrowed line
img=cv2.rectangle(img,(200,300),(400,500),(255,255,0),2)   #this function is used to make a rectange second arg is top left corner
                                                            # third arg is bottom right corner
img=cv2.rectangle(img,(100,200),(200,300),(255,155,0),-1)     #the fifth arg if is -1 then the rect will be filled 
img=cv2.circle(img,(255,255),100,(155,200,255),5)  #this is used to make circle,second arg is center and third arg is radius
font=cv2.FONT_HERSHEY_SIMPLEX          #This tell about the font for the text
img=cv2.putText(img,'Loda Lelo',(10,20),font,1,(123,234,124),3,cv2.LINE_AA)    #this is used to put some text in image
                                                                               #second arg is text third arg is starting point
                                                                                #fourth arg is font type, fifth arg is font size
                                                                                #sixth arg is color, seventh arg is thickness
                                                                                #eight arg is typeof line
cv2.imshow('lodalelo',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
