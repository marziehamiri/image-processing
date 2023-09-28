import cv2
import numpy as np
import matplotlib.pyplot as plt

c = [(200,200),(264,400),(200,400),(248,300),(200,300),(232,200),(200,200)]
img = np.ones(shape=[512,512,3], dtype=np.uint8)
cv2.putText(img,"Marzieh Amiri",(130,100),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,200),2)
cv2.putText(img,"Image Processing",(100,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
for item in c:
    cv2.circle(img,item,16,[255,0,200],-1)
    
cv2.imshow("Image Processing",img)   
k = cv2.waitKey(0)
if k == 27:
        cv2.destroyAllWindows()




gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret,thresh = cv2.threshold(gray,70,255,0)


cv2.imshow("Binary Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows() 


lst = []
for i in range(thresh.shape[0]):
    for j in range(thresh.shape[1]):
         lst.append(np.binary_repr(thresh[i][j] ,width=8)) 
one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(thresh.shape[0],thresh.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(thresh.shape[0],thresh.shape[1])
final = cv2.hconcat([one_bit_img,five_bit_img])
cv2.imshow('final',final)
cv2.waitKey(0) 
   