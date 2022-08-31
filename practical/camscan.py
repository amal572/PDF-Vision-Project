import cv2
import numpy as np

positions = []


def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # return the ordered coordinates
    return rect


def four_point_transform(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    cv2.imshow(warped)
    cv2.waitKey(0)
    # return the warped image
    return warped


def print_coord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'{x, y}\r')
        positions.append(x)
        positions.append(y)

img = cv2.imread(r"C:\Users\User\Desktop\22.JPG")
img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
cv2.namedWindow('Get Coordinates')
cv2.setMouseCallback('Get Coordinates', print_coord)
cv2.imshow('Get Coordinates', img)
cv2.waitKey(0)

# print(positions[0][0])
# print(positions[0][1])
positions =np.array(positions)

pts = order_points(positions)
# inPos = np.float32(
#     [[positions[0][0], positions[0][1]], [positions[1][0], positions[1][1]], [positions[2][0], positions[2][1]],
#      [positions[3][0], positions[3][1]]])
# outPos = np.float32([[0, 0], [0, 500], [500, 500], [0, 500]])
# M_prespective = cv2.getPerspectiveTransform(inPos, outPos)
# img_affine = cv2.warpPerspective(img, M_prespective, (500, 500))
# cv2.imshow("prespective1", img_affine)
# cv2.waitKey(0)
