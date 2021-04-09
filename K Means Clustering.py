"""
Created on Fri Aug 28 20:23:57 2020

@author: jadin

Image Quantization --> reducing the no of pixels of color channel
K Means Clustering 
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.1.05.tiff"

img= cv2.imread(path1,1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

z= img.reshape((-1,1))
z= np.float32(z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
            10,1.0)

k=2
ret , label1,center1 = cv2.kmeans(z, k, None,criteria, 10, 
                                  cv2.KMEANS_RANDOM_CENTERS)
center1 = np.uint8(center1)
res1 = center1[label1.flatten()]
output1 = res1.reshape((img.shape))


k=4
ret , label1,center1 = cv2.kmeans(z, k, None,criteria, 10, 
                                  cv2.KMEANS_RANDOM_CENTERS)
center1 = np.uint8(center1)
res1 = center1[label1.flatten()]
output2 = res1.reshape((img.shape))

k=4
ret , label1,center1 = cv2.kmeans(z, k, None,criteria, 10, 
                                  cv2.KMEANS_RANDOM_CENTERS)
center1 = np.uint8(center1)
res1 = center1[label1.flatten()]
output3 = res1.reshape((img.shape))


output = [img,output1,output2,output3]
titles = ["original", "output2","output1","output2"]

for i in range(len(output)):
    plt.subplot(2,2,i+1)
    plt.imshow(output[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()














