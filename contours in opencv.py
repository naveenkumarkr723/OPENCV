import cv2
# import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.07.tiff"

img= cv2.imread(path1,1)

img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret ,thresh = cv2.threshold(gray,127,255,0)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)
print(contours)

cv2.drawContours(img, contours, -1,(0,0,255),3)


original = cv2.imread(path1,1)
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

image = [original,img]
titles = ["original","drawContours"]


for i in range(len(image)):
    plt.subplot(1,2,i+1)
    plt.imshow(image[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()


























