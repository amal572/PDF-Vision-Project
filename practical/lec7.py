import cv2 as cv
import numpy as np
import argparse
img = cv.imread(r"c://Users//User//Desktop//vision files//river.jpg")
# z = img.reshape((-1, 3))
#
# z = np.float32(z)
# crit = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# k = 3
#
# ret,label,center =cv.kmeans(z,k,None,crit,10,cv.KMEANS_RANDOM_CENTERS)
#
# center = np.uint8(center)
# res = center[label.flatten()]
# res2=res.reshape(img.shape)
# cv.imshow("img",img)
# cv.imshow("res2",res2)
# cv.waitKey(0)



cap = cv.VideoCapture(0)
if cap.isOpened():
    ret,frame = cap.read()
else:
    ret =False

ret,frame1 = cap.read()
ret,frame2 = cap.read()

while ret:
    ret,frame =cap.read()
    d=cv.absdiff(frame1,frame2)
    grey = cv.cvtColor(d,cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(grey,(15,15),0)
    ret,th = cv.threshold(blur,20,255,cv.THRESH_BINARY)

    dialet = cv.dilate(th,np.ones((3,3),np.uint8()),iterations=4)
    c,h=cv.findContours(dialet,cv.RETR_TREE,cv.CHAIN_APPROX_TC89_KCOS)
    cv.drawContours(frame1,c,-1,(0,255,0),2)
    cv.imshow("inter",frame1)
    if cv.waitKey(40)==27:
        break
    frame1=frame2
    ret,frame2=cap.read()
cv.destroyWindow(0)
cap.release()