import cv2
import numpy as np



windowName="drawing"
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName) 

def draw_cc(event , x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 20, (250,0,0),-1)
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 20, (0,250,0),-1)
    if event==cv2.EVENT_MOUSEHWHEEL:
        cv2.circle(img, (x,y), 20, (0,0,250),-1)
                            
cv2.setMouseCallback(windowName, draw_cc)

def main():
    while(True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(25)==27:
            break
        
    cv2.destroyAllWindows()
    

if __name__=="__main__":
    main()




