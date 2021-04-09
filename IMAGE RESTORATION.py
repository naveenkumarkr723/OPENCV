# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:58:07 2020

@author: jadin

Inpainting --> technique for restoration of images
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.1.03.tiff"
mask_path = path+"mask.tiff"
img= cv2.imread(path1,0)
img_mask= cv2.imread(mask_path,0)
# img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_mask =cv2.cvtColor(img_mask, cv2.COLOR_BGR2RGB)

output1 = cv2.inpaint(img, img_mask, 5, cv2.IMPAINT_TELEA)
output2 = cv2.inpaint(img, img_mask, 5, cv2.IMPAINT_NS)


output = [img,output2,output1,output2]
titles = ["original", "output2","output1","output2"]

for i in range(len(output)):
    plt.subplot(2,2,i+1)
    plt.imshow(output[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()



























