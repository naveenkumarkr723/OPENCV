"""
low pass filters do :
    
1.blurring the image
2.denoising the image
3.smoothing the image
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.07.tiff"

img= cv2.imread(path1,1)

img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

box = cv2.boxFilter(img, -1, (53,53))

blur = cv2.blur(img,(13,13)) 
gaussian= cv2.GaussianBlur(img, (37,37), 0)

output = [img,box,blur,gaussian]
titles = ["original", "box_blur","blur","gaussian_blur"]

for i in range(len(output)):
    plt.subplot(2,2,i+1)
    plt.imshow(output[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()

