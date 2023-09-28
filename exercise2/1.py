import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('1.jpg') # reading image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to gray
plt.hist(gray.ravel(), bins=256) #showing histogram of original image
plt.show()
w , h = gray.shape
n = w * h #n is the number of pixels
My_dict = dict()
for i in range (0,256): #create a dictionary to keep every pixel intensity as a key
    My_dict[i] = 0 

for item in gray.ravel(): #keep the number of each pixel intensity as dictionary values
    My_dict[item]+=1
                               
for i in My_dict: #calculate cumulative normalized histogram
    if i > 0:
        My_dict[i] += My_dict[i-1]

for i in My_dict: #calculate cumulative normalized histogram and transformed intensity
        My_dict[i] = round(( My_dict[i] / n ) * 255) 

equalized=gray.copy()
for i in range(w): #apply the equalization to original image
    for j in range(h):
        k=equalized[i,j]
        equalized[i,j]=My_dict[k]

plt.hist(equalized.ravel(), bins=256) #showing equalized histogram
plt.show()

cv2.imshow('original',gray) #showing main image
cv2.imshow('equalized',equalized) #showing equalized image
cv2.waitKey(0)
cv2.destroyAllWindows()
