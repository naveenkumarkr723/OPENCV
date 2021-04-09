
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"5.3.01.tiff"

img= cv2.imread(path1,0)
#img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
thresh = 0
maxval = 255

ret1 , o1 = cv2.threshold(img, thresh, maxval, (cv2.THRESH_BINARY + cv2.THRESH_OTSU))
ret2 , o2 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret3 , o3 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
ret4 , o4 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
ret5 , o5 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TRUNC+cv2.THRESH_OTSU)

image = [img,o1,o2,o3,o4,o5]
titles = ["original","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TOZERO",
          "THRESH_TOZERO_INV","THRESH_TRUNC"]


for i in range(len(image)):
    plt.subplot(3,2,i+1)
    plt.imshow(image[i],cmap = 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()