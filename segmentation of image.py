"""
segmentation --> dividing the image into various regions

gray21.512
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"gray21.512.tiff"

img= cv2.imread(path1,0)
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
thresh = 127
maxval = 255

ret , o1 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY)
ret , o2 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY_INV)
ret , o3 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO)
ret , o4 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO_INV)
ret , o5 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TRUNC)

image = [img,o1,o2,o3,o4,o5]
titles = ["original","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TOZERO",
          "THRESH_TOZERO_INV","THRESH_TRUNC"]


for i in range(len(image)):
    plt.subplot(3,2,i+1)
    plt.imshow(image[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()