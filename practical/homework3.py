import cv2
import numpy as np

image = cv2.imread(r"C:\Users\User\Desktop\44.jpg",0)
lap = cv2.Laplacian(image,cv2.CV_64F,ksize=3)
#lap = cv2.convertScaleAbs(lap)
cv2.imshow("lap",lap)
cv2.waitKey(0)

gaus = cv2.GaussianBlur(image,(13,13),0)
lap2 = cv2.Laplacian(gaus,cv2.CV_64F,ksize=1)
cv2.imshow("lap2",lap2)
cv2.waitKey(0)

lap3 = cv2.Laplacian(image,cv2.CV_64F,ksize=3)
lap3 = np.uint8(np.absolute(lap3))
cv2.imshow("lap3",lap3)
cv2.waitKey(0)
