#سوالات سری سوم، سوال یک قسمت الف و ب 
import cv2
import numpy as np
from matplotlib import pyplot as plt


def distance_from_center(x, y, w, h):
    center_x = w // 2
    center_y = h // 2
    return ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5

#تابع فیلتر ایده آل پایین گذر

def ideal_lowpass_filter(img,r):
    w,h=img.shape[:2]
    H_lowpass=np.zeros((w,h,2),np.float32)
    for i in range(w):
        for j in range(h):
            dis=distance_from_center(i, j, w, h)
            if dis<=r:
                H_lowpass[i,j]=1
           
    return H_lowpass

#تابع فیلتر باترورث پایین گذر
def butter_worth_filter(img,r,n):
    w,h=img.shape[:2]
    H=np.zeros((w,h,2),np.float32)
    for i in range(w):
        for j in range(h):
            dis=distance_from_center(i, j, w, h)
            H[i,j]=1/(1+(dis/r)**(2*n))
           
    return H
    
img=cv2.imread('1.jpg',0)
w,h=img.shape
r=100
n=1
p=2*w
q=2*h
H=np.zeros((p,q),np.uint8)

for i in range(w):
    for j in range(h):
        H[i,j]=img[i,j]
shifted_img=H.copy()

#فیلتر ایده آل
mask=ideal_lowpass_filter(H,r)


#فیلتر باترورث با مقدار n=1
# mask=butter_worth_filter(H,r,n)

dft = cv2.dft(np.float32(shifted_img),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)

fshift=dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
fshift_mask_mag=20*np.log(cv2.magnitude(fshift[:,:,0],dft_shift[:,:,1]))


img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],dft_shift[:,:,1])[:w,:h]



fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(2,2,1)
ax1.imshow(img,cmap='gray')
ax1.title.set_text('original')
ax2=fig.add_subplot(2,2,2)
ax2.imshow(magnitude_spectrum,cmap='gray')
ax2.title.set_text('FFt of image')
ax3=fig.add_subplot(2,2,3)
ax3.imshow(fshift_mask_mag,cmap='gray')
ax3.title.set_text('FFT+mask')
ax4=fig.add_subplot(2,2,4)
ax4.imshow(img_back,cmap='gray')
ax4.title.set_text('after inverse')
plt.show
