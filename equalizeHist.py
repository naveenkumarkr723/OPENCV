

import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"
path1 = path+"4.1.04.tiff"

img= cv2.imread(path1,0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


output1 = cv2.equalizeHist(img)


clahe1 = cv2.createCLAHE()
clahe2 = cv2.createCLAHE(clipLimit = 2.0,tileGridSize =(8,8))

output2 = clahe1.apply(img)
output3 = clahe2.apply(img)





output = [img,output1,output2,output3]
titles = ["original", "output1","output2","output3"]

for i in range(len(output)):
    plt.subplot(2,2,i+1)
    plt.imshow(output[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()




