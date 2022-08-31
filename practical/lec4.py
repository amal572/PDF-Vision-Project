import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r"C:\Users\User\Desktop\3.JPG", 0)
#
# ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#
# ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
#
# ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
#
# ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
#
# ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
#
# titles = ['original','binary','binary_inv','trunic','tozero','tozro_inv']
# images = [image,thresh1,thresh2,thresh3,thresh4,thresh5]
#
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
# cv2.imshow("s",thresh4)
# cv2.waitKey(0)

# image2 = cv2.imread(r"C:\Users\User\Desktop\44.jpg",0)
# image2 = cv2.medianBlur(image2,5)
#
# ret,th1 = cv2.threshold(image2,127,255,cv2.THRESH_BINARY)
# ret,th2 = cv2.adaptiveThreshold(image2,127,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# ret,th3 = cv2.adaptiveThreshold(image2,127,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#
#
# titles = ['original','glob thre v =127','adap mean thre','adap gau']
# images = [image,th1,th2,th3]
#
# for i in range(4):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

# image_gaus = cv2.imread(r"C:\Users\User\Desktop\coins.jpg",0)
# image_gaus = cv2.GaussianBlur(image_gaus,(13,13 ),8)
# ret1,th1 = cv2.threshold(image_gaus,127,255,cv2.THRESH_BINARY)
# ret2,th2 = cv2.threshold(image_gaus,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# print(ret2)
# cv2.imshow("1",th1)
# cv2.waitKey(0)
# cv2.imshow("2",th2)
# cv2.waitKey(0)

image3 = cv2.imread(r"C:\Users\User\Desktop\4.JPG", 0)
kernal = np.ones((3, 3), np.uint8)

# eros = cv2.erode(image_gaus,kernal,iterations=1)
# cv2.imshow("1",eros)
# cv2.waitKey(0)
# eros = cv2.erode(image_gaus,kernal,iterations=2)
# cv2.imshow("2",eros)
# cv2.waitKey(0)

# di = cv2.dilate(image_gaus,kernal,iterations=1)
# cv2.imshow("1",di)
# cv2.waitKey(0)
#
di = cv2.dilate(image3, kernal, iterations=2)
cv2.imshow("2", di)
cv2.waitKey(0)

# op = cv2.morphologyEx(image_gaus,cv2.MORPH_OPEN,kernal,iterations=3)
# cv2.imshow("2",op)
# cv2.waitKey(0)

op = cv2.morphologyEx(image_gaus, cv2.MORPH_, kernal, iterations=4)
cv2.imshow("2", op)
cv2.waitKey(0)

# im = di - image_gaus
# cv2.imshow("2",im)
# cv2.waitKey(0)

# op = cv2.morphologyEx(image_gaus,cv2.MORPH_CLOSE,kernal,iterations=4)
# cv2.imshow("2",op)
# cv2.waitKey(0)
