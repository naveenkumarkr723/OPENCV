# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 08:27:55 2020

@author: jadin
"""




import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.1.04.tiff"

img= cv2.imread(path1,1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

R,G,B = cv2.split(img)


output1_R = cv2.equalizeHist(R)
output1_G = cv2.equalizeHist(G)
output1_B = cv2.equalizeHist(B)

output1 = cv2.merge((output1_R,output1_G,output1_B))
"""clahe1 = cv2.createCLAHE()
clahe2 = cv2.createCLAHE(clipLimit = 2.0,tileGridSize =(8,8))
output2 = clahe1.apply(img)
output3 = clahe2.apply(img)
"""
clahe1 = cv2.createCLAHE()
output2_R = clahe1.apply(R)
output2_G = clahe1.apply(G)
output2_B = clahe1.apply(B)

output2 = cv2.merge((output2_R,output2_G,output2_B))


clahe2 = cv2.createCLAHE(clipLimit = 2.0,tileGridSize =(8,8))
output3_R = clahe2.apply(R)
output3_G = clahe2.apply(G)
output3_B = clahe2.apply(B)

output3 = cv2.merge((output3_R,output3_G,output3_B))

output = [img,output1,output2,output3]
titles = ["original", "output1","output2","output3"]

for i in range(len(output)):
    plt.subplot(2,2,i+1)
    plt.imshow(output[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()




