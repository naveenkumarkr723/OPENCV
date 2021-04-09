import cv2
import time


path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.2.06.tiff"
img= cv2.imread(path1,1)

rows,columns,channels = img.shape
angle =0

while True:
    if angle == 360:
        angle =0
        
    r = cv2.getRotationMatrix2D((columns/2,rows/2), angle, 0.5)
    print(r)
    
    output = cv2.warpAffine(img, r, (columns,rows))
    
    cv2.imshow("Angle Rotating image",output)
    
    angle = angle + 1
    time.sleep(0.1)
    
    if cv2.waitKey(1)==27:
        break
    
cv2.destroyAllWindows()
    






















