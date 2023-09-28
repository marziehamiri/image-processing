
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Read images
img1 = cv2.imread("4.jpg",0)
img2 = cv2.imread("6.jpg",0)
img3 = cv2.imread("7.png",0)

def median_filter(image, ksize):
    #Create a new image of the same size as the input image
    filtered_img = np.zeros_like(image)
    #Apply Zero Padding
    padded_img = np.pad(image, ksize//2, mode='constant')
    #Loop over the image pixels
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
          #Get the neighboring pixels
            neighbors = padded_img[i:i+ksize, j:j+ksize]
          #Find the median value
            median = np.median(neighbors)
          #Assign the median value to the filtered image
            filtered_img[i,j] = median
    return filtered_img

#Apply median filter to images
median1_3x3 = median_filter(img1, 3)
median1_5x5 = median_filter(img1, 5)
median1_9x9 = median_filter(img1, 9)

median2_3x3 = median_filter(img2, 3)
median2_5x5 = median_filter(img2, 5)
median2_9x9 = median_filter(img2, 9)

median3_3x3 = median_filter(img3, 3)
median3_5x5 = median_filter(img3, 5)
median3_9x9 = median_filter(img3, 9)

#Show images
f, subplt1 = plt.subplots(2,2,figsize=(10, 20))
subplt1[0,0].imshow(img1,cmap='gray')
subplt1[0,0].set_title("Noisy Image")
subplt1[0,1].imshow(median1_3x3,cmap='gray')
subplt1[0,1].set_title("Median Filtered 3x3")
subplt1[1,0].imshow(median1_5x5,cmap='gray')
subplt1[1,0].set_title("Median Filtered 5x5")
subplt1[1,1].imshow(median1_9x9,cmap='gray')
subplt1[1,1].set_title("Median Filtered 9x9")

f, subplt2 = plt.subplots(2,2,figsize=(10, 20))
subplt2[0,0].imshow(img2,cmap='gray')
subplt2[0,0].set_title("Noisy Image")
subplt2[0,1].imshow(median2_3x3,cmap='gray')
subplt2[0,1].set_title("Median Filtered 3x3")
subplt2[1,0].imshow(median2_5x5,cmap='gray')
subplt2[1,0].set_title("Median Filtered 5x5")
subplt2[1,1].imshow(median2_9x9,cmap='gray')
subplt2[1,1].set_title("Median Filtered 9x9")

f, subplt3 = plt.subplots(2,2,figsize=(10, 20))
subplt3[0,0].imshow(img3,cmap='gray')
subplt3[0,0].set_title("Noisy Image")
subplt3[0,1].imshow(median3_3x3,cmap='gray')
subplt3[0,1].set_title("Median Filtered 3x3")
subplt3[1,0].imshow(median3_5x5,cmap='gray')
subplt3[1,0].set_title("Median Filtered 5x5")
subplt3[1,1].imshow(median3_9x9,cmap='gray')
subplt3[1,1].set_title("Median Filtered 9x9")

plt.show()


