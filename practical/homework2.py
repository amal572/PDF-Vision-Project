import cv2
import numpy as np
#
image = cv2.imread(r"C:\Users\User\Desktop\adobe.png")
cv2.imshow("img", image)
cv2.waitKey(0)


rows, cols, depth = image.shape


M = np.float32([[1,0,100],[0,1,40]])
img_translated = cv2.warpAffine(image,M,(cols+100,rows+50))
cv2.imshow("translated", img_translated)
cv2.waitKey(0)

rows,cols,depth = img_translated.shape

M_rot = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
img_rot = cv2.warpAffine(img_translated,M_rot,(cols+50,rows+50))
cv2.imshow("rotate",img_rot)
cv2.waitKey(0)

M_rot2 = cv2.getRotationMatrix2D((cols/2,rows/2),-45,0.8)
img_rot2 = cv2.warpAffine(img_translated,M_rot2,(cols+50,rows+50))
cv2.imshow("rotate1",img_rot2)
cv2.waitKey(0)

inPos = np.float32([[50, 50], [200, 50], [50, 200]])
outPos = np.float32([[50, 50], [300, 50], [10, 150]])
M_prespective = cv2.getAffineTransform(inPos, outPos)
img_affine = cv2.warpAffine(img_translated, M_prespective, (cols + 100, rows + 50))
cv2.imshow("affine",img_affine)
cv2.waitKey(0)


inPos = np.float32([[0, 0], [0, cols], [rows, 0], [rows, cols]])
outPos = np.float32([[0, 30], [0, cols-30], [rows, 0], [rows, cols]])
M_prespective = cv2.getPerspectiveTransform(inPos, outPos)
img_affine = cv2.warpPerspective(img_translated, M_prespective, (cols + 100, rows + 50))
cv2.imshow("prespective",img_affine)
cv2.waitKey(0)

positions = []


def print_coord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'{x, y}\r')
        positions.append((x, y))


img = cv2.imread(r"C:\Users\User\Desktop\22.JPG")
img = cv2.resize(img, (500,500))
cv2.namedWindow('Get Coordinates')
cv2.setMouseCallback('Get Coordinates', print_coord)
cv2.imshow('Get Coordinates', img)
cv2.waitKey(0)

print(positions[0][0])
print(positions[0][1])

inPos = np.float32([[positions[0][0],positions[0][1]], [positions[1][0],positions[1][1]], [positions[2][0],positions[2][1]], [positions[3][0],positions[3][1]]])
outPos = np.float32([[0,0], [300, 0], [300,300], [0,300]])
M_prespective = cv2.getPerspectiveTransform(inPos, outPos)
img_prespective = cv2.warpPerspective(img, M_prespective, (500,500))

positions = []
cv2.namedWindow("prespective1")
cv2.setMouseCallback("prespective1",print_coord)
cv2.imshow("prespective1",img_prespective)
cv2.waitKey(0)

img_prespective = img_prespective[positions[0][0]:positions[1][0],positions[0][1]:positions[3][1] ]
cv2.imshow("cut2",img_prespective)
cv2.waitKey(0)