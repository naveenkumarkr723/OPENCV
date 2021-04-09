
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.2.07.tiff"

img= cv2.imread(path1,1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


R_hist =cv2.calcHist([img], [0], None, [256], [0,255])
G_hist =cv2.calcHist([img], [1], None, [256], [0,255])
B_hist =cv2.calcHist([img], [2], None, [256], [0,255])
#plt.subplot(1,2,1)
#plt.imshow(img,cmap='gray')
#plt.title("original image")
#plt.xticks([])
#plt.xticks([])

plt.subplot(3,1,1)
plt.xlim([0,256])
plt.plot(R_hist,color='r')
plt.title("RED--Histogram image")

plt.subplot(3,1,2)
plt.xlim([0,256])
plt.plot(G_hist,color='g')
plt.title("GREEN--Histogram image")

plt.subplot(3,1,3)
plt.xlim([0,256])
plt.plot(B_hist,color='b')
plt.title("BLUE--Histogram image")



plt.show()









