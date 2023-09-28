
import cv2
import numpy as np
c = [(194,80),(240,154),(179,165),(174,199),(204,238)]
img=cv2.imread('2.jpg',cv2.IMREAD_GRAYSCALE)
for item in c:
    cv2.circle(img,item,7,(255,255,255),2)
cv2.imshow('Image Processing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()