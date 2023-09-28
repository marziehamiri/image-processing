import cv2
import numpy as np
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
        