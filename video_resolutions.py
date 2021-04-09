
import cv2
import numpy as np

cap = cv2.VideoCapture(0)


print(" the width of frame",cap.get(3))
print(" the height of frame",cap.get(4))

cap.set(3,1080)
cap.set(4,720)

print(" the width of frame",cap.get(3))
print(" the height of frame",cap.get(4))

while(True):
    
    ret,frame = cap.read()
    
    ##color_img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    ## gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("video_capturing", frame)
    ##cv2.imshow("gray window", gray_img)
    
    if cv2.waitKey(1) == 27 :
        break

cap.release()
cv2.destroyAllWindows()