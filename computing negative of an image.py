import cv2
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.2.06.tiff"

img= cv2.imread(path1,1)

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img3 = abs(255-img1)
img4 = abs(255-img2)


titles = ["original","gray","ori_neg","gray_neg"]
images = [img1,img2,img3,img4]


plt.subplot(2,2,1)
plt.imshow(images[0])
plt.title(titles[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(images[1],cmap="gray")
plt.title(titles[1])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(images[2])
plt.title(titles[2])
plt.xticks([])
plt.yticks([])


plt.subplot(2,2,4)
plt.imshow(images[3],cmap="gray")
plt.title(titles[3])
plt.xticks([])
plt.yticks([])

