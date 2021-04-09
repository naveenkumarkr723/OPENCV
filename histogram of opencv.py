
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.2.07.tiff"

img= cv2.imread(path1,1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

R,G,B =cv2.split(img)


plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title("original image")
plt.xticks([])
plt.xticks([])



plt.subplot(2,2,2)
plt.hist(R.ravel(),256,[0,255])
plt.title("RED-Histogram")
plt.xlim(xmin=0,xmax=256)


plt.subplot(2,2,3)
plt.hist(G.ravel(),256,[0,255])
plt.title("GREEN-Histogram")
plt.xlim(xmin=0,xmax=256)


plt.subplot(2,2,4)
plt.hist(B.ravel(),256,[0,255])
plt.title("BLUE-Histogram")
plt.xlim(xmin=0,xmax=256)
plt.show()
