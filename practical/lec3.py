import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r"C:\Users\User\Desktop\44.JPG",0)
#image = image[500:1000, 500:1000]
cv2.imshow("img", image)
# plt.hist(image.ravel(),256,[0,256])
# plt.show()
cv2.waitKey(0)
#
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv2.calcHist([image],[i],None,[256],[0,256])
#     plt.plot(histr,color=col)
#     plt.xlim([0,256])
# plt.show()

# eq = cv2.equalizeHist(image)
# cv2.imshow("eq",eq)
# cv2.waitKey(0)
# plt.hist(eq.ravel(),256,[0,256])
# plt.show()
# cv2.waitKey(0)

# blur = cv2.blur(image,(10,10))
# cv2.imshow("blur",blur)
# cv2.waitKey(0)

# gausian = cv2.GaussianBlur(image, (7, 7), 2)
# cv2.imshow("gau", gausian)
# cv2.waitKey(0)

# med = cv2.medianBlur(image,9)
# cv2.imshow("med", med)
# cv2.waitKey(0)

# sobX = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
# sobY = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
# sobXY = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
# sobXF = cv2.convertScaleAbs(sobX)
# sobYF = cv2.convertScaleAbs(sobY)
# sobXYF = cv2.convertScaleAbs(sobXY)
# cv2.imshow("x",sobXF)
# cv2.waitKey(0)
# cv2.imshow("y",sobYF)
# cv2.waitKey(0)
# cv2.imshow("Xy",sobXYF)
# cv2.waitKey(0)

edge = cv2.Canny(image,threshold1=30,threshold2=130)
cv2.imshow("s",edge)
cv2.waitKey(0)