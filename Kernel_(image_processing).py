
"""
Kernel () -- convolution matrix

see the portal for different actions
https://en.wikipedia.org/wiki/Kernel_(image_processing)

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.07.tiff"

img= cv2.imread(path1,1)

img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

## edge detection
#k = np.array(([1,0,-1],[0,0,0],[-1,0,1]),np.float32)
#k = np.array(([0,1,0],[1,-4,1],[0,1,0]),np.float32) 
k = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),np.float32)

### kjgfjhh
print(k)
print(type(k))



output = cv2.filter2D(img,-1,k)


plt.subplot(1,2,1)
plt.imshow(img)
plt.title(" Original image ")

plt.subplot(1,2,2)
plt.imshow(output)
plt.title(" Filtered image ")

plt.show()
