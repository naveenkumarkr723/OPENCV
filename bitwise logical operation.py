"""
NOT                         (NOT IMG1)
AND                         (IMG1 AND IMG2)
OR                          (IMG1 OR IMG2)
X-OR(exclusive or)          (IMG1 X-OR IMG2)

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.1.03.tiff"
path2 = path+"4.1.02.tiff"


img1= cv2.imread(path1)
img2= cv2.imread(path2)

img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img3 = cv2.bitwise_not(img1)
img4 = cv2.bitwise_not(img2)
img5 = cv2.bitwise_and(img1, img2)
img6 = cv2.bitwise_or(img1, img2)
img7 = cv2.bitwise_xor(img1, img2)


titles = ["img1","img2","not img1","not img2","and","or","x-or"]
images = [img1,img2,img3,img4,img5,img6,img7]


for i in range(8):
    plt.subplot(4,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    
plt.show()

