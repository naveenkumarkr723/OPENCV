import cv2

import matplotlib.pyplot as plt



path = "C:\\Users\\jadin\\Downloads\\misc\\misc\\"

path1 = path+"4.1.03.tiff"
path2 = path+"4.1.02.tiff"

img1= cv2.imread(path1)
img2= cv2.imread(path2)

img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

add_ = img1*10 
sub_  = img1/20
# sub1 = img2 - img1 

titles = ["1st image","2nd image","add_img","sub_img"]
image = [img1,img2,add_,sub_]

for i in range(4):
    plt.subplot(1,4,i+1)
    plt.imshow(image[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])






