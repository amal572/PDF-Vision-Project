import cv2 as cv
import numpy as np


image = cv.imread(r"c://Users//User//Desktop//vision files//h.jpg")
open = cv.imread(r"c://Users//User//Desktop//vision files//8.jpg")
cv.imshow("org",image)
cv.waitKey(0)
#
# gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv.cornerHarris(gray,2,5,0.02)
# dst = cv.dilate(dst,None)
#
# cv.imshow("harris",dst)
# cv.waitKey(0)
#
# image[dst>0.01*dst.max()] = [0,0,255]
# cv.imshow("dst",image)
# cv.waitKey(0)

# orb = cv.ORB_create()
# kp = orb.detect(image,None)


# img= cv.resize(image,(128,128))
# wins =(img.shape[1],img.shape[0])
# blokSize= (1,1)
# blokstride  = (8, 8)
# cells = (4,4)
# nbin = 9
# hog = cv.HOGDescriptor(wins, blokstride, blokSize, cells, nbin)
#
# location = []
# hist = hog.compute(img,None,None,location)
# print(hist)
# print(len(hist ))

# img1 = cv.resize(image,(200,200))
# img2 = cv.resize(open,(200,200))

# dst = cv.addWeighted(img1,0.7,img2,0.2,0)
# cv.imshow("dst",dst)
# cv.waitKey(0)

rows,cols,cha = open.shape
roi = image[0:rows,0:cols]

img2gray = cv.cvtColor(open,cv.COLOR_BGR2GRAY)
ret,mask=cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
img1_bg = cv.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv.bitwise_and(open,open,mask=mask)
dst = cv.add(img1_bg,img2_fg)
image[0:rows,0:cols]=dst
cv.imshow("res",image)
cv.waitKey(0)