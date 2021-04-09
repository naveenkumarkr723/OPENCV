# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:09:23 2020

@author: jadin

fourcc == four character code

1.wmv2
2.wmv1
3.mjpg
4.divx
5.xvid
6.h264
"""



import cv2

cap = cv2.VideoCapture(0)

filename = 'C:\\Users\\jadin\\Documents\\open_cv.avi'
codec = cv2.VideoWriter_fourcc("X", "V", "I", "D")
framerate  = 30
resolution = (640,480)

videofileoutput = cv2.VideoWriter(filename,codec,framerate,resolution)

    
if cap.isOpened:
    ret,frame = cap.read()
else:
    ret=False
        
while(ret):
    
    ret,frame = cap.read()
    
    videofileoutput.write(frame)
    
    
    cv2.imshow("livevideo_capture", frame)

    if cv2.waitKey(1) == 27 :
        break
    
    
    


cv2.destroyAllWindows()
videofileoutput.release()
cap.release()