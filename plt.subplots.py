import cv2

import matplotlib.pyplot as plt



path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.1.01.tiff"
path2 = path+"4.1.02.tiff"

img1= cv2.imread(path1)
img2= cv2.imread(path2)

img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


plt.subplot(1,2,1)
plt.imshow(img1)
plt.title("1st image")
plt.xticks([])
plt.yticks([])


plt.subplot(1,2,2)
plt.imshow(img2)
plt.title("2nd image")
plt.xticks([])
plt.yticks([])
plt.show()




