import cv2
import numpy as np
import sys
from PIL import Image

img = cv2.imread('1.jpg',cv2.IMREAD_COLOR)
#convert to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
width,height, = gray.shape

list0 = [] #first bit
list1 = [] #second bit
list2 = [] #third bit
list3 = [] #forth bit
list4 = [] #fifth bit
list5 = [] #sisxth bit
list6 = [] #seventh bit
list7 = [] #eighth bit

mylist = []
mylist2 = []
myStr = ""
#convert decimal to binary
'''
def DecimalToBinary(num):
     
    while num >= 1:
        mylist2.append(num % 2)
        num = num // 2
    myStr = "".join(map(str,mylist2))   
    return myStr 
'''

for i in range(0,width) :
    for j in range(0,height): 
        mylist.append( bin(gray[i][j])[2:])

mylist = list(map(lambda x:x.zfill(8),mylist))
mylist = list(map(lambda x:x[::-1],mylist))

for item in mylist:
    list0.append(int(item[0]))
    list1.append(int(item[1])*2**1)
    list2.append(int(item[2])*2**2)
    list3.append(int(item[3])*2**3)
    list4.append(int(item[4])*2**4)
    list5.append(int(item[5])*2**5)
    list6.append(int(item[6])*2**6)
    list7.append(int(item[7])*2**7)
#print(list0)

img_0=np.uint8(np.reshape(list0,(width,height)))
img_1=np.uint8(np.reshape(list1,(width,height)))
img_2=np.uint8(np.reshape(list2,(width,height)))
img_3=np.uint8(np.reshape(list3,(width,height)))
img_4=np.uint8(np.reshape(list4,(width,height)))
img_5=np.uint8(np.reshape(list5,(width,height)))
img_6=np.uint8(np.reshape(list6,(width,height)))
img_7=np.uint8(np.reshape(list7,(width,height)))

cv2.imshow('level0',img_0)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imshow('level1',img_1)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imshow('level2',img_2)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imshow('level3',img_3)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imshow('level4',img_4)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imshow('level5',img_5)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imshow('level6',img_6)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imshow('level7',img_7)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

