import cv2
windowName = "preview"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret ,frame = cap.read()
else:
    ret = False
    
while ret:
    ret ,frame = cap.read()
    thresh = 127
    maxval = 255
    ret , o1 = cv2.threshold(frame, thresh, maxval, cv2.THRESH_BINARY)
    ret , o2 = cv2.threshold(frame, thresh, maxval, cv2.THRESH_BINARY_INV)
    ret , o3 = cv2.threshold(frame, thresh, maxval, cv2.THRESH_TOZERO)
    ret , o4 = cv2.threshold(frame, thresh, maxval, cv2.THRESH_TOZERO_INV)
    ret , o5 = cv2.threshold(frame, thresh, maxval, cv2.THRESH_TRUNC)

    cv2.imshow(windowName,o1)
    cv2.imshow("windowName2",o2)
    cv2.imshow("windowName3",o3)
    cv2.imshow("windowName4",o4)
    cv2.imshow("windowName5",o5)
    
    if cv2.waitKey(1)==27:
        break



cv2.destroyAllWindows()
cap.release()

























