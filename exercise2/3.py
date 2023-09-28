import cv2
import numpy as np

#laplacian function
def laplacian_addition_function(img):
    h,w=img.shape
    filtered_img=img.copy()

    #applying laplacian filter to original image 
    # -1 -1 -1 
    # -1  9 -1 
    # -1 -1 -1 
    for i in range(1,h-1):
        for j in range(1,w-1):
            filtered_img[i,j]=-img[i-1,j-1]-img[i-1,j]-img[i-1,j+1]-img[i,j-1]-img[i,j+1]-img[i+1,j-1]-img[i+1,j]-img[i+1,j+1]+9*img[i,j]

    return filtered_img

#bluring function
def bluring_function(img):
    h,w=img.shape
    blured_img=img.copy()
    blured_img-=blured_img
    #average filter
    # 1/16 * 1 2 1
    #        2 4 2
    #        1 2 1  
    for i in range(1,h-1):
        for j in range(1,w-1):
            blured_img[i,j]=1/16*(img[i-1,j-1]+2*img[i-1,j]+img[i-1,j+1]+2*img[i,j-1]+2*img[i,j+1]+img[i+1,j-1]+2*img[i+1,j]+img[i+1,j+1]+4*img[i,j])

    return blured_img


def unsharp_masking(img):
    h,w=img.shape
    k=1
    masked_img=img.copy()
    g_mask=img-bluring_function(img)
    masked_img+=(k*g_mask)

    return masked_img         
                
img = cv2.imread('3.jpg', 0)
filtered_img = laplacian_addition_function(img)
unsharpe_masked = unsharp_masking(img)
g_mask=img-bluring_function(img)
blured=bluring_function(img)

cv2.imshow('Original', img)
cv2.imshow('laplacian',filtered_img)
cv2.imshow('unsharpemasking',unsharpe_masked)
cv2.waitKey(0)
cv2.destroyAllWindows()