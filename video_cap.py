# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:07:23 2020

@author: jadin
"""


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    
    ret,frame = cap.read()
    
    ## color_img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("video_capturing", frame)
    cv2.imshow("gray window", gray_img)
    
    if cv2.waitKey(1) == 27 :
        break

cap.release()
cv2.destroyAllWindows()