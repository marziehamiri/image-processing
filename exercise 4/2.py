import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('2.png',0)
imgcopy = cv2.imread('2.png',0)
h , w = img.shape
imgcolored = np.zeros((h,w,3),np.uint8)
#divide the image intensities into 8 values
for i in range(h):
    for j in range(w):
        if  img[i][j] < 32:
            imgcolored[i][j] = [255,0,0]
        elif 32 < img[i][j] < 64 :
            imgcolored[i][j] = [0,255,0]
        elif 64 < img[i][j] < 96:
            imgcolored[i][j] = [0,0,255]
        elif 96 < img[i][j] < 128:
            imgcolored[i][j] = [255,255,0]
        elif 128 < img[i][j] < 160:
            imgcolored[i][j] = [0,255,255]
        elif 160 < img[i][j] < 192:
            imgcolored[i][j] = [255,0,255]
        elif 192 < img[i][j] < 224:
            imgcolored[i][j] = [0,0,0]
        else:
            imgcolored[i][j] = [255,255,255]
        
             

#Show images
f, subplt1 = plt.subplots(1,2,figsize=(10,10))
subplt1[0].imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
subplt1[0].set_title("Original Image")
subplt1[1].imshow(cv2.cvtColor(imgcolored, cv2.COLOR_BGR2RGB))
subplt1[1].set_title("Colored Image")
plt.show()
