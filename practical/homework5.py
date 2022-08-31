import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread(r"c://Users//User//Desktop//vision files//7.jpg", 0)
image2 = cv.imread(r"c://Users//User//Desktop//vision files//44.jpg")

# cv.imshow("original",image)
# cv.waitKey(0)

# size = np.size(image)
# skel = np.zeros(image.shape, np.uint8)
#
# ret , image = cv.threshold(image,127,255,0)
# # cv.imshow("thresh",image)
# # cv.waitKey(0)
#
# element = cv.getStructuringElement(cv.MORPH_CROSS,(3,3))
# done = False
#
# while( not done):
#     eroded = cv.erode(image,element)
#     # cv.imshow("erode", eroded)
#     # cv.waitKey(0)
#     temp = cv.dilate(eroded,element)
#     # cv.imshow("temp", temp)
#     # cv.waitKey(0)
#     temp = cv.subtract(image,temp)
#     # cv.imshow("temp1", temp)
#     # cv.waitKey(0)
#     skel = cv.bitwise_or(skel,temp)
#     # cv.imshow("skel", skel)
#     # cv.waitKey(0)
#     image = eroded.copy()
#
#     zeros = size - cv.countNonZero(image)
#     if zeros == size :
#         done = True
#
# cv.imshow("skel1", skel)
# cv.waitKey(0)

# first

img = cv.imread('messi5.jpg',0)
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(image, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# #second
# dft = cv.dft(np.float32(image),flags = cv.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)
# magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
# plt.subplot(121),plt.imshow(image, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()


gray = cv.cvtColor(image2,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,40,200)
# cv.imshow('houghlines5.jpg', edges)
# cv.waitKey(0)

lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=180, maxLineGap=70)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(image2, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Show result
img = cv.resize(image2, dsize=(600, 600))
cv.imshow("Result Image", img)
cv.waitKey(0)
