import cv2
import numpy as np
windowName = "preview"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

if cap.isOpened():
    ret ,frame = cap.read()
else:
    ret = False
    
while ret:
    ret ,frame = cap.read()
    
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    z= img.reshape((-1,1))
    z= np.float32(z)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
                10,1.0)
    
    k=8
    ret , label1,center1 = cv2.kmeans(z, k, None,criteria, 10, 
                                      cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output1 = res1.reshape((img.shape))
 
    cv2.imshow(windowName,frame)
    cv2.imshow("video quintize",output1)
    
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()




























