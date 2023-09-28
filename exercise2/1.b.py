import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img2 = cv2.equalizeHist(gray) #equalizeHist
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) #createCLAHE
img3 = clahe.apply(gray) #createCLAHE


cv2.imshow('original',gray)
cv2.imshow('equalizedHist',img2)
cv2.imshow('createCLAHE',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()