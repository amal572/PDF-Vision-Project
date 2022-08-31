import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\User\Desktop\8.jpg")

# size = np.size(image)
# skel = np.zeros(image.shape, np.uint8)
#
# cv.imshow("skel", skel)
# cv.waitKey(0)
#
# ret, image = cv.threshold(image, 127, 255, 0)
cv.imshow("img", image)
cv.waitKey(0)
#
# element = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
# done = False
#
# while(not done):
#     eroded = cv.erode(image,element)
#     cv.imshow("erode", eroded)
#     cv.waitKey(0)
#     temp = cv.dilate(eroded,element)
#     cv.imshow("temp", temp)
#     cv.waitKey(0)
#     temp = cv.subtract(image,temp)
#     cv.imshow("temp1", temp)
#     cv.waitKey(0)
#     skel = cv.bitwise_or(skel,temp)
#     cv.imshow("skel", skel)
#     cv.waitKey(0)
#     image = eroded.copy()
#
#     zeros = size - cv.countNonZero(image)
#     if zeros == size :
#         done = True
#
# cv.imshow("skel1", skel)
# cv.waitKey(0)

# low = cv.pyrDown(image)
# up = cv.pyrUp(image)
# cv.imshow("low",low)
# cv.imshow("up",up)
# cv.waitKey(0)

# mask = cv.imread(r"C:\Users\User\Desktop\6.JPG",0)
# dst = cv.inpaint(image,mask,8,cv.INPAINT_TELEA)
# dst1  = cv.inpaint(image,mask,3,cv.INPAINT_TELEA)
# cv.imshow("mask",mask)
# cv.waitKey(0)
# cv.imshow("dst",dst)
# cv.waitKey(0)
# cv.imshow("dst1",dst1)
# cv.waitKey(0)

# gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# edges = cv.Canny(gray,30,70)
# cv.imshow("dst1",edges)
# cv.waitKey(0)
# lines = cv.HoughLines(edges,1,np.pi/180,190)
#
# for line in lines:
#     rho,theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0+1000*(-b))
#     y1 = int(y0+1000*a)
#     x2 = int(x0-1000*(-b))
#     y2 = int(y0 - 1000 * a)
#
#     cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
#
# cv.imshow("asd",image)
# cv.waitKey(0)

image = cv.medianBlur(image,5)
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

circle = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,20,param1=100,param2=25,minRadius=90,maxRadius=100)
circle = np.uint16(np.around(circle))

for i in circle[0,:]:
    cv.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
    cv.circle(image,(i[0],i[1]),2,(0,0,255),3)


cv.imshow("asd",image)
cv.waitKey(0)
