# import cv2
# import numpy as np
# image = cv2.imread(r"C:\Users\User\Desktop\adobe.png")
# cv2.imshow("img", image)
# cv2.waitKey(0)
#
#  lanc = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_)
# # cv2.imshow("lanc",lanc)
# # cv2.waitKey(0)
# #
# # five500 = cv2.resize(image, (500,500), fx=3, fy=3, interpolation=cv2.INTER_LANCZOS4)
# # cv2.imshow("500*500",five500)
# # cv2.waitKey(0)
# #
# # linear = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)
# # cv2.imshow("linear",linear)
# # cv2.waitKey(0)
# #
# # cube = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
# # cv2.imshow("cube",cube)
# # cv2.waitKey(0)
# #
# # nearest = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_NEAREST)
# # cv2.imshow("nearest",nearest)
# # cv2.waitKey(0)
#
# rows,cols,depth = image.shape
# # M = np.float32([ [1,0,100],[0,1,50]])
# # dst = cv2.warpAffine(image,M,(cols+100,rows+50))
# # cv2.imshow("im",dst)
# # cv2.waitKey(0)
#
# # M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# # dst = cv2.warpAffine(image,M,(cols,rows))
# # cv2.imshow("im",dst)
# # cv2.waitKey(0)
#
# new = cv2.rotate(image,cv2.ROTATE_180)
# cv2.imshow("img",new)
# cv2.waitKey(0)
