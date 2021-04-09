import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"5.2.10.tiff"
img= cv2.imread(path1,0)

blockSize =  513
constant = 2 


thr1  = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, blockSize, constant)

thr2  = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                              cv2.THRESH_BINARY, blockSize, constant)

output = [img,thr1,thr2]
titles = ["original", "adaptive_thresh_mean","adaptive_thresh_gaussian"]

for i in range(len(output)):
    plt.subplot(1,3,i+1)
    plt.imshow(output[i],cmap = 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()











