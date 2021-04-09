
"""
Created on Fri Aug 28 17:19:20 2020

@author: jadin

salt and pepper noise can be handled by efficiently by median filter 
it is low pass filter
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
            

denoising = cv2.medianBlur(output, 5)


outputs = [img,output,denoising]
titles = ["original", "noisy_salt_pepper","de-noising_salt_pepper"]

for i in range(len(outputs)):
    plt.subplot(1,3,i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])
plt.show()
