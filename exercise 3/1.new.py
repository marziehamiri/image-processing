import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def Ideal_Lowpass_Filter(img,d):
    dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = img.shape
    crow,ccol = rows//2 , cols//2
    # create a mask first, center square is 1, remaining all zeros
    mask = np.zeros((rows,cols,2),np.uint8)
    mask[crow-d:crow+d, ccol-d:ccol+d] = 1
    # apply mask and inverse DFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv.idft(f_ishift)
    img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
    plt.title('apply Ideal Low Pass Filter'), plt.xticks([]), plt.yticks([])
    plt.show()

img = cv.imread('3.jpg', 0)

assert img is not None, "file could not be read, check with os.path.exists()"
d = 40
Ideal_Lowpass_Filter(img,d)

d = 30
Ideal_Lowpass_Filter(img,d)


d = 20
Ideal_Lowpass_Filter(img,d)

d = 10
Ideal_Lowpass_Filter(img,d)