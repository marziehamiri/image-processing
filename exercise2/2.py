import cv2
a=50
b=150
alpha=0.1
beta=0.5
gama=0.8
Ya=20
Yb=160

img = cv2.imread('2.jpg')
h,w,z=img.shape
stretched=img.copy()
for i in range(h):
    for j in range(w):
        for c in range(z):
            if stretched[i,j,c]<a:
                stretched[i,j,c]*=alpha
            elif stretched[i,j,c]<b:
                stretched[i,j,c]=beta*(stretched[i,j,c]-a)+Ya
            else:
                stretched[i,j,c]=gama*(stretched[i,j,c]-b)+Yb

cv2.imshow('original', img)
cv2.imshow('stretched', stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()   