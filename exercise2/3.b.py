from PIL import Image, ImageFilter
import cv2
# Open an image file
with Image.open("3.jpg") as im:
    # Apply unsharp mask filter
    im_sharp = im.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    # Save the filtered image
    im_sharp.save("image_sharpened.jpg", "JPEG")
imgsh = cv2.imread("image_sharpened.jpg")
img = cv2.imread("3.jpg")
cv2.imshow('original',img)
cv2.imshow('image_sharpened',imgsh)
cv2.waitKey(0)
cv2.destroyAllWindows()