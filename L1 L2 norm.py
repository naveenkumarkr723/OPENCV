
"""
Created on Fri Aug 28 19:05:16 2020

@author: jadin

canny edge detection algorithm 

1. gaussian kernel 5x5 is applied to image for filtering out any noise
2. intensity gradient is calculated using L1 or L2 norm
3. Non-maximum suppression is applied to the output of 2 step
4. Using the gradient thresholds the final edge set is calculated
   a) any fixel is less than gradient1 is excluded
   b) any fixel is greater than gradient2 is included
   c) any fixel in between two gradients only the pixels directly 
      connected to pixels in set b are included in the final image set
"""


import cv2
# import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"7.1.02.tiff"
img= cv2.imread(path1,1)
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

L1_norm= cv2.Canny(img, 50,300, L2gradient = False)


L2_norm = cv2.Canny(img, 100,150, L2gradient = True)


output = [img,L1_norm,L2_norm]
titles = ["original", "L1 norm","L2 norm"]

for i in range(len(output)):
    plt.subplot(2,2,i+1)
    plt.imshow(output[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()

























