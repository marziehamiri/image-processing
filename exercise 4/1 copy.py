import cv2
import matplotlib.pyplot as plt
import numpy as np

#Red selection function get image name and cutoff as the radius of the sphere
def Red_Selection(img1,cutoff):
    img = cv2.imread(img1,1) #read image
    imgcopy = cv2.imread(img1,1)

    h , w , ch = img.shape #image size
    r = cutoff #radius of the image
    ''' 
    I chose the intensity of a red pixel by paint 
    If the distance of other pixels from the red pixel is
    larger than the radius of the sphere
    make it [220,220,220]
    otherwise
    keep it
    '''
    for i in range(h):
        for j in range(w):
            co = (220 - img[i][j][2]) **2 + (50 - img[i][j][1])**2 + (70 - img[i][j][0])**2
            if ((co) > [r**2,r**2,r**2]).all() :
                img[i][j] = [220,220,220]
        
    #Show images
    f, subplt1 = plt.subplots(1,2,figsize=(10,10))
    subplt1[0].imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
    subplt1[0].set_title("Original image")
    subplt1[1].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    subplt1[1].set_title("Red selection by sphere with the radius of {0}".format(cutoff))
    plt.show()

Red_Selection('1.png',50) #cutoff == 50
Red_Selection('1.png',80) #cutoff == 80
Red_Selection('1.png',100) #cutoff == 100
Red_Selection('1.png',120) #cutoff == 120
