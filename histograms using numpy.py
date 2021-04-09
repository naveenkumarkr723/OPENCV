import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.2.07.tiff"

img= cv2.imread(path1,1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


R,G,B =cv2.split(img)

#plt.subplot(1,2,1)
#plt.imshow(img,cmap='gray')
#plt.title("original image")
#plt.xticks([])
#plt.xticks([])

plt.subplot(3,1,1)
hist,bins = np.histogram(R.ravel(),255,[0,256])
plt.xlim([0,256])

plt.plot(hist,color='r')
plt.title("RED--Histogram image")

plt.subplot(3,1,2)
hist,bins = np.histogram(G.ravel(),255,[0,256])
plt.xlim([0,256])

plt.plot(hist,color='g')
plt.title("GREEN--Histogram image")

plt.subplot(3,1,3)
hist,bins = np.histogram(B.ravel(),255,[0,256])
plt.xlim([0,256])

plt.plot(hist,color='b')
plt.title("BLUE--Histogram image")



plt.show()









