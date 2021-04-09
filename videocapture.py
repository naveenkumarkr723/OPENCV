
"""
Created on Tue Aug 11 16:03:39 2020

@author: jadin
"""

#import numpy as np
import cv2


cap = cv2.VideoCapture(0)

print(cap.get(3))
print(cap.get(4))


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    
    # Our operations on the frame come here
    gray1 = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    # Display the resulting frame
    cv2.imshow('frame',gray1)
    cv2.imshow('frame',gray2)
    if cv2.waitKey(25) == 27:
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

