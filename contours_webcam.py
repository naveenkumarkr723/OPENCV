import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print(cap.get(3))
print(cap.get(4))

if cap.isOpened():
    ret ,frame = cap.read()    
else:
    ret = False
    
ret ,frame1 = cap.read()
ret ,frame2 = cap.read()
    
    
while ret:
    
    d = cv2.absdiff(frame1, frame2)
    gray =cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    ret ,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,np.ones((3,3),np.uint8),iterations =15 )
    erosion  = cv2.erode(dilated, np.ones((3,3),np.uint8), iterations = 15)
    contours,hierarchy = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame1, contours, -1,(0,0,255),3)
    
    cv2.imshow("original", frame2)
    
    cv2.imshow("contours_webcam", frame1)
    
    if cv2.waitKey(1)==27:
        break
    
    frame1 = frame2
    ret ,frame2 = cap.read()




    
cv2.destroyAllWindows()
cap.release()






























