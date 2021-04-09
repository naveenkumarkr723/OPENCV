import cv2
import numpy as np

winname = "object tracking"
cv2.namedWindow(winname)


cap =cv2.VideoCapture(0)

while cap.isOpened:
    ret,frame = cap.read()
    
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    ## FOR BLUE COLOR
    """b_low = np.array([100,50,50])
    b_high = np.array([140,255,255])"""
    
    """g_low = np.array([40,50,50])
    g_high = np.array([80,255,255])"""
    
    r_low = np.array([140,150,0])
    r_high = np.array([80,255,255])
    ## image_mask
    image_mask = cv2.inRange(hsv, r_low, r_high)
    
    ### for tracking real image
    output = cv2.bitwise_and(frame, frame,mask = image_mask)
    
    
    # print(image_mask)
    cv2.imshow("image_mask", image_mask)
    cv2.imshow(winname, frame)
    cv2.imshow("original", output)
    
    k = cv2.waitKey(1)
    if k == 27:
        break
    
    
cv2.destroyAllWindows()   
cap.release()

