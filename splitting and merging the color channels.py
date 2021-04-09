import cv2
import matplotlib.pyplot as plt

path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.1.03.tiff"

img= cv2.imread(path1,1)

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

r,g,v = cv2.split(img1)

titles = ["original","red","green","blue"]
images = [cv2.merge((r,g,v)),r,g,v]

plt.subplot(2,2,1)
plt.imshow(images[0])
plt.title(titles[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(images[1],cmap="Reds")
plt.title(titles[1])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(images[2],cmap="Greens")
plt.title(titles[2])
plt.xticks([])
plt.yticks([])


plt.subplot(2,2,4)
plt.imshow(images[3],cmap="Blues")
plt.title(titles[3])
plt.xticks([])
plt.yticks([])
   






















