import cv2
import numpy as np
import time

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.1.03.tiff"
path2 = path+"4.1.02.tiff"

windowName = "transition_image"
cv2.namedWindow(windowName)

img1= cv2.imread(path1)
img2= cv2.imread(path2)

def empty_func():
    pass

output = cv2.addWeighted(img1,0.5, img2, 0.5, 0)

cv2.createTrackbar("Alpha", windowName, 0, 100, empty_func)  

while (True):
    
    cv2.imshow(windowName, output)
    
    
    if cv2.waitKey(1)==27:
        break
    
    alpha = cv2.getTrackbarPos("Alpha", windowName)/100.0
    beta =1-alpha
    
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
    print(alpha,beta)
    
cv2.destroyAllWindows()




"""

blending effect(addWeighted)
formula for addWeighted
img1*alpha+img2*beta+gamma


for i in np.linspace(0,1,50):
    alpha = i
    beta = 1-i
    gamma = 0.0
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    cv2.imshow("transition",output)
    time.sleep(0.1)
    if cv2.waitKey(1)==27:
        break
"""











