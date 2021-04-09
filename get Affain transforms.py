import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.06.tiff"

img= cv2.imread(path1,1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rows,columns,channels = img.shape

point1 = np.float32([[100,100],[300,100],[100,300]])
point2 = np.float32([[400,150],[00,150],[100,300]])

r = cv2.getAffineTransform(point1, point2)
print(r)

output = cv2.warpAffine(img, r, (columns,rows))

plt.imshow(output)
plt.title("get warpAffine shifted image")
plt.show()
