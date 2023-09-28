import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def Butterworth_lowpass_filter(img,d):
    dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = img.shape
    n = 1
    # create a mask 
    mask = np.zeros((rows,cols,2),np.uint8)
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - rows//2) ** 2 + (j - cols//2) ** 2)
            mask[i, j] = 1 / (1 + (distance//d ) ** (2 * 1))
    # apply mask and inverse DFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv.idft(f_ishift)
    img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
    plt.title('apply Butterworth LowPass Filter'), plt.xticks([]), plt.yticks([])
    plt.show()

img = cv.imread('3.jpg', 0)

assert img is not None, "file could not be read, check with os.path.exists()"
d = 40
Butterworth_lowpass_filter(img,d)

d = 30
Butterworth_lowpass_filter(img,d)

d = 20
Butterworth_lowpass_filter(img,d)

d = 10
Butterworth_lowpass_filter(img,d)