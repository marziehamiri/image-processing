import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('2.png',0)
imgcopy = cv2.imread('2.png',0)

h , w = img.shape
#RED
imgcoloredR = np.zeros((h,w,3),np.uint8)
for i in range(h):
    for j in range(w):
        if  img[i][j] < 32:
                imgcoloredR[i][j] = [0,0,0]
        elif 32 < img[i][j] < 64 :
            imgcoloredR[i][j] = [14,5,61]
        elif 64 < img[i][j] < 80:
            imgcoloredR[i][j] = [35,14,156]
        elif 80 < img[i][j] < 130:
            imgcoloredR[i][j] = [50,19,221]
        elif 130 < img[i][j] < 160:
            imgcoloredR[i][j] = [95,69,239]
        elif 160 < img[i][j] < 192:
            imgcoloredR[i][j] = [134,115,242]
        elif 192 < img[i][j] < 224:
            imgcoloredR[i][j] = [191,181,249]
        else:
            imgcoloredR[i][j] = [243,241,254]

#Show images
f, subplt1 = plt.subplots(1,2,figsize=(10,10))
subplt1[0].imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
subplt1[0].set_title("Original Image")
subplt1[1].imshow(cv2.cvtColor(imgcoloredR, cv2.COLOR_BGR2RGB))
subplt1[1].set_title("Colored Image 'RED'")
plt.show()

#GREEN
imgcoloredG = np.zeros((h,w,3),np.uint8)
for i in range(h):
    for j in range(w):
        if  img[i][j] < 32:
                imgcoloredG[i][j] = [0,0,0]
        elif 32 < img[i][j] < 64 :
            imgcoloredG[i][j] = [15,56,7]
        elif 64 < img[i][j] < 80:
            imgcoloredG[i][j] = [31,119,15]
        elif 80 < img[i][j] < 130:
            imgcoloredG[i][j] = [0,0,0]
        elif 130 < img[i][j] < 160:
            imgcoloredG[i][j] = [78,230,51]
        elif 160 < img[i][j] < 192:
            imgcoloredG[i][j] = [129,237,109]
        elif 192 < img[i][j] < 224:
            imgcoloredG[i][j] = [174,243,163]
        else:
            imgcoloredG[i][j] = [219,250,214]

#Show images
f, subplt1 = plt.subplots(1,2,figsize=(10,10))
subplt1[0].imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
subplt1[0].set_title("Original Image")
subplt1[1].imshow(cv2.cvtColor(imgcoloredG, cv2.COLOR_BGR2RGB))
subplt1[1].set_title("Colored Image 'GREEN'")
plt.show()


#BLUE
imgcoloredB = np.zeros((h,w,3),np.uint8)
for i in range(h):
    for j in range(w):
        if  img[i][j] < 32:
                imgcoloredB[i][j] = [3,1,16]
        elif 32 < img[i][j] < 64 :
            imgcoloredB[i][j] = [72,6,18]
        elif 64 < img[i][j] < 80:
            imgcoloredB[i][j] = [137,12,34]
        elif 80 < img[i][j] < 130:
            imgcoloredG[i][j] = [0,0,0]
        elif 128 < img[i][j] < 160:
            imgcoloredB[i][j] = [238,47,81]
        elif 160 < img[i][j] < 192:
            imgcoloredB[i][j] = [243,114,136]
        elif 192 < img[i][j] < 224:
            imgcoloredB[i][j] = [250,179,191]
        else:
            imgcoloredG[i][j] = [252,220,225]

#Show images
f, subplt1 = plt.subplots(1,2,figsize=(10,10))
subplt1[0].imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
subplt1[0].set_title("Original Image")
subplt1[1].imshow(cv2.cvtColor(imgcoloredB, cv2.COLOR_BGR2RGB))
subplt1[1].set_title("Colored Image 'BLUE'")
plt.show()

#addition 
imagecolored_final = np.zeros((h,w,3),np.uint8)
for i in range(h):
    for j in range(w):
        imagecolored_final[i][j] =(imgcoloredG[i][j]+ imgcoloredB[i][j] + imgcoloredR[i][j])

#Show images
f, subplt1 = plt.subplots(1,2,figsize=(10,10))
subplt1[0].imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
subplt1[0].set_title("Original Image")
subplt1[1].imshow(cv2.cvtColor(imagecolored_final, cv2.COLOR_BGR2RGB))
subplt1[1].set_title("Colored Image 'Final'")
plt.show()
