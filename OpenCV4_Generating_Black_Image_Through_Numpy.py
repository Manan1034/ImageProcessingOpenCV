import numpy as np       #numpy library
import cv2

img=np.zeros([512,400,3],np.uint8)     #image formation through zeros
                                        #first arg is a list.In list, 1st no.is height,2nd is width and third is 3
                                        #second arg is datatype
cv2.imshow('land',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
