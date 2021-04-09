"""
cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)

INTER POLATION METHODS

INTER_LINEAR
INTER_NEAREST
INTER_AREA--------------- shrinking
INTER_CUBIC--------------------zooming 4x4
INTER_LANCZOS4 --------------8x8

scaling/resizing = shrinking(scaling down)/zooming(scaling up)

"""
import cv2
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.06.tiff"

img= cv2.imread(path1,1)


output = cv2.resize(img,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)

cv2.imshow("inter polation",output)
cv2.waitKey(0)
cv2.destroyAllWindows()



