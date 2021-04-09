import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.06.tiff"

img= cv2.imread(path1,1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rows,columns,channels = img.shape

point1 = np.float32([[0,0],[400,0],[0,400],[400,400]])
point2 = np.float32([[0,0],[100,0],[0,100],[100,100]])

r = cv2.getPerspectiveTransform(point1, point2)
print(r)

output = cv2.warpPerspective(img, r, (100,100))

plt.imshow(output)
plt.title(" getPerspectiveTransform shifted image")
plt.show()



