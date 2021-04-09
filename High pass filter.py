
"""
Created on Fri Aug 28 17:29:44 2020

@author: jadin

High pass filters are very good at detecting edges of an image
Low pass filters are very good at detecting and removing noise of an image

"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.2.07.tiff"
img= cv2.imread(path1,1)
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

edgeslap = cv2.Laplacian(img,-1,ksize=17,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
sobel = cv2.Sobel(img,-1,dx=1,dy=0,ksize=17,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
output = [img,edgeslap,sobel]
titles = ["original", "Edges","sobel"]

for i in range(len(output)):
    plt.subplot(2,2,i+1)
    plt.imshow(output[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()







