"""
Noise is unwanted signal
analog / digital

lens = scratch(both)
capture - film / circutary
transmission -- reception
storage (rarely it happens)

salt and pepper noise

SNR ---> signal to noise ratio
SNR = signal power / noise power
"""

import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.07.tiff"

img= cv2.imread(path1,1)

img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows,columns,channels = img.shape
p =0.1
output = np.zeros(img.shape,np.uint8)

for i in range (rows):
    for j in range (columns):
        r = random.random()
        if r<p/2:
            ### pepper noise
            output[i][j]=[0,0,0]
        elif r<p:
            ### salt noise
            output[i][j]=[255,255,255]
        else:
            output[i][j]=img[i][j]
            

plt.imshow(output)
plt.title("image with salt and pepper ")
# plt.title(" original image")
plt.show()
