import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread(r"C:\Users\User\Desktop\coins.jpg",0)
image1 = cv.imread(r"C:\Users\User\Desktop\7.jpg",0)

image_gaus = cv.GaussianBlur(image, (3,3), 1)


ret, thresh = cv.threshold (image_gaus, 127, 255, cv.THRESH_BINARY)
ret2 , threh2 = cv.threshold (image_gaus, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
erosion = cv.erode(threh2,kernel,iterations = 2)


images = [image,image.ravel(),thresh,image,image.ravel(),threh2,image_gaus,image_gaus.ravel(),erosion]
titles = ["original", "histogram", "global thresh v = 127", "original", "histogram", "OTSU","gaus image","histogram","OTSU erusion"]
length = len(images)
j = 0
for i in range(3):
    plt.subplot(3, 3, j+1), plt.imshow(images[j],"gray")
    plt.title(titles[j])
    plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, j+2), plt.hist(images[j+1], 256, [0, 256])
    plt.xticks([]), plt.yticks([])
    plt.title(titles[j+1])

    plt.subplot(3, 3, j+3), plt.imshow(images[j+2],"gray")
    plt.title(titles[j+2])
    plt.xticks([]), plt.yticks([])

    j = j+3
plt.show()

kernal = np.ones((5, 5), np.uint8)
top=cv.morphologyEx(image1,cv.MORPH_TOPHAT,kernal,iterations=5)
cv.imshow("2",top)
cv.waitKey(0)

kernal = np.ones((5, 5), np.uint8)
top=cv.morphologyEx(image1,cv.MORPH_BLACKHAT,kernal,iterations=5)
cv.imshow("2",top)
cv.waitKey(0)