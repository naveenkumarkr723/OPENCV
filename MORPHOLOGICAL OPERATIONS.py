
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"5.1.12.tiff"

img= cv2.imread(path1,0)
#img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
thresh = 0
maxval = 255


ret , BINARY_INV = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# k = np.ones((5,5),dtype=np.uint8)

# k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
k = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))


print(k)

erosion  = cv2.erode(BINARY_INV, k, iterations = 2)

dilation = cv2.dilate(BINARY_INV, k, iterations = 2)

gradient = cv2.morphologyEx(BINARY_INV, cv2.MORPH_GRADIENT, k)

image = [img,BINARY_INV,erosion,dilation,gradient]
titles = ["original","THRESH_BINARY_INV","erosion","dilation","gradient"]


for i in range(len(image)):
    plt.subplot(3,2,i+1)
    plt.imshow(image[i],cmap = 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()
