import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret ,frame = cap.read()    
else:
    ret = False

while ret:
    ret ,frame = cap.read()
    B,G,R = cv2.split(frame)
    M = np.maximum(np.maximum(G,R),B)
    R[R<M] = 0
    G[G<M] = 0
    B[B<M] = 0

    output = cv2.merge((B,G,R))
    
    cv2.imshow("original", output)
    
    if cv2.waitKey(1)==27:
        break
    
   
    



    
cv2.destroyAllWindows()
cap.release()






























