
"""
Created on Tue Aug 11 13:20:31 2020

@author: jadin
"""

import cv2
import numpy as np

img1=np.zeros((512,512,3),np.uint8)

cv2.line(img1,(0,99),(99,0),(255,0,0),5)

cv2.circle(img1, (60,60), 20, (0,0,255),-1)

cv2.rectangle(img1, (66,126), (100,50), (0,255,0),6)

points=np.array([[20,40],[10,30],[88,99],[77,33],[100,200],[300,400]])
points=points.reshape((-1,1,2))
cv2.polylines(img1, [points], True, (100,250,175),3)



cv2.imshow("structures",img1)
k=cv2.waitKey(0)

outpath=r'C:\Users\jadin\Downloads\misc.jpg'
if k == 27:                             # wait for ESC key to exit
    cv2.destroyAllWindows()
    
    
elif k == ord('s'):                     # wait for 's' key to save and exit
    cv2.imwrite(outpath,img1)
    cv2.destroyAllWindows()
