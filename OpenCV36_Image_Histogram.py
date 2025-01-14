#Finding image histogram using cv2



import cv2
from matplotlib import pyplot as pt

img=cv2.imread('F:\Python\OpenCV\opencv-master\opencv-master\samples\data\lena.jpg',0)


hist=cv2.calcHist([img],[0],None,[256],[0,256])

                  #1st arg is source in list form.2nd arg is the index of channels.In 2nd arg, we can pass[0,1,2] for multiple channels
                  #3rd arg is mask.For finding histogram for whole image which is in grayscale mode , just pass None as mask.
                  #4th arg is hist size in square brackets.5th arg is range


pt.plot(hist)        #Passing image to be plotted in matplotlib


pt.show()



#Histogram can define the whole image.Whether lightning conditions were flat or harsh.Whether image is completely exposed or not.
#We can also perform adjustments for better images
#For plotting histogram, we have the plot the hist in matplotlib
