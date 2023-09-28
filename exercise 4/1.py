import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('1.png',1)
imgcopy = cv2.imread('1.png',1)

h , w , ch = img.shape
width = 7
width = np.array([width//2,width//2,width//2])
a = [220,50,70]
red = np.array(a)
c = [0,0,0]
con = np.array(c)
for i in range(h):
    for j in range(w):
        con[0] = (np.subtract(red[0],img[i][j][2]))  
        con[1] = (np.subtract(red[1],img[i][j][1])) 
        con[2] = (np.subtract(red[2],img[i][j][0]))
        if ((abs(con)) > width).all() :
            img[i][j] = [128,128,128]
        
#Show images
f, subplt1 = plt.subplots(1,2,figsize=(10,10))
subplt1[0].imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
subplt1[0].set_title("Original image")
subplt1[1].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
subplt1[1].set_title("Cube Mask")
plt.show()
