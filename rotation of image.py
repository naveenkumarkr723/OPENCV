"""
translation --> shifting an image
geometric operation on image

cv2.warpAffine()
cv2.getRotationMatrix2D

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.06.tiff"

img= cv2.imread(path1,1)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

rows,columns,channels = img.shape

# t= np.float32([[1,0,-50],[0,1,-50]])

r = cv2.getRotationMatrix2D((columns/2,rows/2), 45, 1)
print(r)

output = cv2.warpAffine(img, r, (rows,columns))

plt.imshow(output)
plt.title("warpAffine shifted image")
plt.show()



