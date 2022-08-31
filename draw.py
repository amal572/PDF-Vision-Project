import collections

import cv2 as cv
import numpy as np
from urllib3.connectionpool import xrange

def unique_count_app(image):
    colors, count = np.unique(image.reshape(-1, image.shape[-1]), axis=0, return_counts=True)
    index =count.argmax()
    # colors =np.delete(colors,index)
    count[index] = 0
    index = count.argmax()
    # colors = np.delete(colors, index)
    # count = np.delete(count,index)
    return (colors[index],count[index])


def change_text_color(path, index, color):
    colors = []
    values = []
    # Load image, grayscale, Gaussian blur, adaptive threshold
    index = "2"
    image = cv.imread(f"IMAGES/page0.jpg")
    cv.imshow("asdas",image)
    cv.waitKey(0)
    # image = cv2.resize(image,(1000,800))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (9, 9), 0)
    thresh = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 30)

    # Dilate to combine adjacent text contours
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))
    dilate = cv.dilate(thresh, kernel, iterations=4)

    # Find contours, highlight text areas, and extract ROIs
    cnts = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    ROI_number = 0
    for c in cnts:
        area = cv.contourArea(c)
        if area > 10000:
            x, y, w, h = cv.boundingRect(c)
            im = image[y:y+h,x:x+w]
            colorandnum = unique_count_app(im)
            col = colorandnum[0]
            value = colorandnum[1]
            i = 0
            added = False

            for item in colors :
                if item.all==col.all:
                    values[i] = values[i] + value
                    added = True
                i+=1
            if not added :
                colors.append(col)
                values.append(value)
    for c in cnts:
            values = np.asarray(values)
            index = values.argmax()
            changecolor = colors[index]
            area = cv.contourArea(c)
            if area > 10000:
                x, y, w, h = cv.boundingRect(c)
            for i in range(w):
                for j in range(h):
                    if (image[j + y][x + i][0] == changecolor[0]) & (image[j + y][x + i][1] == changecolor[1]) & (
                            image[j + y][x + i][2] == changecolor[2]):
                        # print("no")
                        image[j + y][x + i][0] = color[0][2]
                        image[j + y][x + i][1] = color[0][1]
                        image[j + y][x + i][2] = color[0][0]

    cv.imwrite(f"IMAGES/{index}1212.png", image)
    values =np.asarray(values)
    index = values.argmax()
    print(colors[index])


change_text_color("as","2",([[0,255  ,0],1]))
# image = cv.imread("IMAGES/2.png")
# print(unique_count_app(image)[1])
# print(len(unique_count_app(image)[1]))
# colors = [[255, 215, 255], [1, 2, 3]]
# value = [255, 215, 255]
#
# for item in colors :
#     if item == value:
#         print("yes")

# ########################################
# import cv2
#
#
# def calc_fact(rows, y):
#     if y < rows / 20:
#         print(f"ros={rows / 20}")
#         print(f"ros={rows / 2}")
#         return 2
#     elif (rows / 20 < y) & (rows / 10 > y):
#         return 2.8
#     elif (rows / 10 < y) & (rows / 5 > y):
#         print(f"ros={rows / 20}")
#         print(f"ros={rows / 10}")
#         print(f"y={y}")
#         return 3.3
#     else:
#         return 3.3
#
#
# def add_row_mark(b_mark, index, path, x, y):
#     image = cv.imread(f'IMAGES/2.png')
#     book_mark = cv.imread(f'IMAGES/marker1.jpg')
#     rows, cols, channels = book_mark.shape
#     imrows, _, _ = image.shape
#     fact = calc_fact(imrows, y)
#     print(fact)
#     if rows + y * fact > imrows:
#         print("yes")
#         y -= rows
#     image[int(y * fact):int(rows + (y * fact)), 0:cols] = book_mark
#     cv.imwrite(f"IMAGES/223.png", image)
#
#
# positions = []
#
#
# def print_coord(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(f'{x, y}\r')
#         positions.append(x)
#         positions.append(y)
#
#
# img = cv2.imread(r"IMAGES/2.png")
# cols, rows, _ = img.shape
# img = cv2.resize(img, (int(rows / 3.5), int(cols / 3.5)))
# cv2.namedWindow('Get Coordinates')
# cv2.setMouseCallback('Get Coordinates', print_coord)
# cv2.imshow('Get Coordinates', img)
# cv2.waitKey(0)
# add_row_mark("asd", 2, "asd", positions[0], positions[1])
