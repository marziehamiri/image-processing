import cv2
import matplotlib.pyplot as plt
import numpy as np

#red selection function get image name and cutoff as the width of the cube
def Red_Selection(img1,cutoff):
    img = cv2.imread(img1,1) #read image
    imgcopy = cv2.imread(img1,1) 
    h , w , ch = img.shape #image size
    cu = cutoff #width of the cube
    co = np.array([0,0,0])
    ''' 
    I chose the intensity of a red pixel by paint 
    If the subtraction of that red pixel from the other pixels is
    larger than the half of the width of the cube
    make it [220,220,220]
    otherwise
    keep it
       '''
    for i in range(h):
        for j in range(w):
            co[2] = (220 - img[i][j][2]) #red value of pixel 
            co[1] = (50 - img[i][j][1]) #green value of pixel
            co[0] = (70 - img[i][j][0]) #blue value of pixel
            if ((abs(co)) > [cu//2,cu//2,cu//2]).all() :
                img[i][j] = [220,220,220]
        
    #Show images
    f, subplt1 = plt.subplots(1,2,figsize=(10,10))
    subplt1[0].imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
    subplt1[0].set_title("Original image")
    subplt1[1].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    subplt1[1].set_title("Red selection by cube with the width of {0}".format(cutoff))
    plt.show()


#execution
Red_Selection('1.png',4) #cutoff == 4
Red_Selection('1.png',7) #cutoff == 7
Red_Selection('1.png',10) #cutoff == 10
Red_Selection('1.png',20) #cutoff == 20