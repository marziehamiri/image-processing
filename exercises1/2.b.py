
import cv2
import numpy as np
c = [(194,80),(240,154),(179,165),(174,199),(204,238)]
img=cv2.imread('2.jpg',cv2.IMREAD_GRAYSCALE)
m = int(np.mean(img[60:90, 220:250]))
for i in c:
    cv2.circle(img,i,8,(m,0,0),-1)
cv2.imshow('Image processing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()