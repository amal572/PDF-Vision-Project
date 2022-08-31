import cv2 as cv
import numpy as np
import pdf2image
import os
from pdf2image import convert_from_path
from pathlib import Path
from PIL import Image
from numba import jit, uint8


@jit(nopython=True, cache=True, fastmath={'fast'})
def speed(a):
    grey = np.full((3), fill_value=70, dtype=np.uint8)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if np.sum(a[i, j]) == 0:
                a[i, j] = grey
    return a


def conver_pdf_to_image(pdfPath):
    filename = os.path.basename(pdfPath)
    if os.path.isdir(f"IMAGES//{filename}"):
        print("exist")
    else:
        Path(f"IMAGES//{filename}").mkdir(parents=True, exist_ok=True)
        pages = convert_from_path(pdf_path=pdfPath, poppler_path=r"D:\\programmes for windows\\poppler\\bin")

        index = 0
        for page in pages:
            page.save(f'IMAGES\\{filename}\\{index}.png', 'PNG')
            index += 1


def conver_one_image(pdfpath, index):
    filename = os.path.basename(pdfpath)
    pages = convert_from_path(pdf_path=pdfpath, poppler_path=r"D:\\programmes for windows\\poppler\\bin",
                              first_page=index, last_page=index)
    print(pages)
    for page in pages:
        print("yes")
        page.save(f'IMAGES\\{filename}\\{index - 1}.png', 'PNG')




kelvin_table = {
    1000: (255, 56, 0),
    1500: (255, 109, 0),
    2000: (255, 137, 18),
    2500: (255, 161, 72),
    3000: (255, 180, 107),
    3500: (255, 196, 137),
    4000: (255, 209, 163),
    4500: (255, 219, 186),
    5000: (255, 228, 206),
    5500: (255, 236, 224),
    6000: (255, 243, 239),
    6500: (255, 249, 253),
    7000: (245, 243, 255),
    7500: (235, 238, 255),
    8000: (227, 233, 255),
    8500: (220, 229, 255),
    9000: (214, 225, 255),
    9500: (208, 222, 255),
    10000: (204, 219, 255)}


def convert_temp(folderpath, temp):
    photolist = []
    filename = os.path.basename(folderpath)
    if os.path.isdir(f"IMAGES//{filename}//night2"):
        print("exist")
    else:
        Path(f"IMAGES//{filename}//night2").mkdir(parents=True, exist_ok=True)
        r, g, b = kelvin_table[temp]
        matrix = (r / 255.0, 0.0, 0.0, 0.0,
                  0.0, g / 255.0, 0.0, 0.0,
                  0.0, 0.0, b / 255.0, 0.0)
        for name in os.listdir(folderpath):
            if name.lower().endswith(".jpg") or name.lower().endswith(".png"):
                photolist.append(name)
        for name in photolist:
            print(name)
            image = cv.imread(f"IMAGES/{filename}/{name}")
            image = Image.fromarray(image)
            image = image.convert('RGB', matrix)
            image.save(f"IMAGES/{filename}/night2/{name}")


def sepia_one_image(filename, index):
    image = cv.imread(f"{filename}\\{index}")
    # print(f"{filename}\\{index}")
    # cv.imshow(" " , image)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    normalized_gray = np.array(gray, np.float32) / 255
    # solid color
    sepia = np.ones(image.shape)
    sepia[:, :, 0] *= 255  # B
    sepia[:, :, 1] *= 230  # G
    sepia[:, :, 2] *= 180  # R
    # hadamard
    sepia[:, :, 0] *= normalized_gray  # B
    sepia[:, :, 1] *= normalized_gray  # G
    sepia[:, :, 2] *= normalized_gray  # R
    img = Image.fromarray(np.array(sepia, np.uint8), 'RGB')
    img.save(f"{filename}/night/{index}")


def sepia(folderpath,new):
    # print("yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees")
    photolist = []
    filename = os.path.basename(folderpath)
    if os.path.isdir(f"IMAGES//{filename}//night") & (not new):
        print("exist")
    else:
        Path(f"IMAGES//{filename}//night").mkdir(parents=True, exist_ok=True)
        for name in os.listdir(folderpath):
            if name.lower().endswith(".jpg") or name.lower().endswith(".png"):
                photolist.append(name)
        for name in photolist:
            sepia_one_image("IMAGES/" + filename, name)


def gray_and_white(folderpath):
    photolist = []
    filename = os.path.basename(folderpath)
    if os.path.isdir(f"IMAGES//{filename}//night3"):
        print("exist")
    else:
        Path(f"IMAGES//{filename}//night3").mkdir(parents=True, exist_ok=True)
        for name in os.listdir(folderpath):
            if name.lower().endswith(".jpg") or name.lower().endswith(".png"):
                photolist.append(name)
        for name in photolist:
            inverted = np.where(cv.imread(f"IMAGES/{filename}/{name}") <= 140, 255, 0)
            color_array = speed(inverted)
            cv.imwrite(f"IMAGES/{filename}/night3/{name}", color_array)


def invert_black_white(image):
    row, cols, depth = image.shape
    for i in range(row):
        for j in range(cols):
            if (image[i][j][0] <= 70) & (image[i][j][1] <= 70) & (image[i][j][2] <= 70):
                image[i][j][0] = 255
                image[i][j][1] = 255
                image[i][j][2] = 255
            elif (image[i][j][0] >= 190) & (image[i][j][1] >= 190) & (image[i][j][2] >= 190):
                image[i][j][0] = 0
                image[i][j][1] = 0
                image[i][j][2] = 0
    return image


#
# img = cv.imread("IMAGES/0.png")
# img = cv.resize(img,(600,600))
# # cv.imshow("in,",img)
# # cv.waitKey(0)
# inves = invert_black_white(img)
# cv.imshow("in,",inves)
# cv.waitKey(0)
#
# inverted = np.where(cv.imread("IMAGES/0.png") <= 140, 255, 0)
# cv.imwrite("IMAGES\ss1.png", inves)
# # cv.imshow("in,",inverted)
# # cv.waitKey(0)
# color_array = cv.imread("IMAGES\ss1.png")
# color_array = speed(inves)
# cv.imwrite("IMAGES\ss.png", color_array)

# def get_black_text(image):
#     # print(f"{path}//{index}.png")
#     image = cv.imread(image)
#     image = cv.resize(image, (600, 848))
#     # image = original_image.copy()
#     # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     # thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
#
#     # rgb = cv.cvtColor(thresh, cv.COLOR_GRAY2RGB)
#     rgb = image
#     rgb1= np.zeros(rgb)
#     for i in range(848):
#         for j in range(600):
#             if (rgb[i][j][0] <70) & (rgb[i][j][1] <70) & (rgb[i][j][2] <70):
#                 rgb1[i][j][0] = 255
#                 rgb1[i][j][1] = 0
#                 rgb1[i][j][2] = 0
#
#     cv.imshow(" ",rgb1)
#     cv.waitKey(0)
#     gray = cv.cvtColor(rgb1, cv.COLOR_BGR2GRAY)
#     thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
#     rgb = cv.cvtColor(thresh, cv.COLOR_GRAY2RGB)
#     cv.imshow(" ", rgb)
#     cv.waitKey(0)
#
# get_black_text("IMAGES/2.png")

def unique_count_app(image):
    colors, count = np.unique(image.reshape(-1, image.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]


def change_back_color(back_color, txt_color, path, index):
    print(f"{path}//{index}.png")
    original_image = cv.imread(f"{path}\\{index}.png")
    # rows,cols = original_image.shape
    original_image = cv.resize(original_image, (1000, 1414))
    # image = original_image.copy()
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]

    # rgb = cv.cvtColor(thresh, cv.COLOR_GRAY2RGB)
    color = unique_count_app(original_image)
    print(color)
    rgb = original_image
    for i in range(1414):
        for j in range(1000):
            if (rgb[i][j][0] == color[0]) & (rgb[i][j][1] == color[1]) & (rgb[i][j][2] == color[2]):
                rgb[i][j][0] = back_color[0][0]
                rgb[i][j][1] = back_color[0][1]
                rgb[i][j][2] = back_color[0][2]
            # if (rgb[i][j][0] == 255) & (rgb[i][j][1] == 255) & (rgb[i][j][2] == 255):
            #     rgb[i][j][0] = txt_color[0][0]
            #     rgb[i][j][1] = txt_color[0][1]
            #     rgb[i][j][2] = txt_color[0][2]

    cv.imwrite(f"{path}\\{index}.png", rgb)


def change_text_color(path, index, color):
    # Load image, grayscale, Gaussian blur, adaptive threshold
    image = cv.imread(f"{path}\\{index}.png")
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
            for i in range(w):
                for j in range(h):
                    if (image[j + y][x + i][0] <= 220) & (image[j + y][x + i][1] <= 220) & (
                            image[j + y][x + i][2] <= 220):
                        # print("no")
                        image[j + y][x + i][0] = color[0][2]
                        image[j + y][x + i][1] = color[0][1]
                        image[j + y][x + i][2] = color[0][0]

    cv.imwrite(f"{path}\\{index}.png", image)


def add_book_mark(b_mark, index, path):
    image = cv.imread(f'{path}\\{index}.png')
    print(path)
    book_mark = cv.imread(f'IMAGES/mark.jpg')
    # book_mark = cv.resize(book_mark, (200, 300))
    rows, cols, channels = book_mark.shape
    roi = image[0:rows, 0:cols]
    img2gray = cv.cvtColor(book_mark, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img2gray, 0, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)
    image_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
    bmark_fg = cv.bitwise_and(book_mark, book_mark, mask=mask)
    dst = cv.add(image_bg, bmark_fg)
    image[0:rows, 0:cols] = dst
    cv.imwrite(f"{path}\\{index}.png", image)


def calc_fact(rows, y):
    if y < rows / 20:
        print(f"ros={rows / 20}")
        print(f"ros={rows / 2}")
        return 2
    elif (rows / 20 < y) & (rows / 10 > y):
        return 2.8
    elif (rows / 10 < y) & (rows / 5 > y):
        print(f"ros={rows / 20}")
        print(f"ros={rows / 10}")
        print(f"y={y}")
        return 3.3
    else:
        return 3.3


def add_row_mark(b_mark, index, path, x, y):
    image = cv.imread(f'{path}\\{index}.png')
    image2 = cv.imread(f'{path}\\night\\{index}.png')
    book_mark = cv.imread("IMAGES/marker1.jpg")
    # cv.imshow("asd",image)
    # cv.imshow("asda",book_mark_mark)
    # cv.waitKey(0)
    rows, cols, channels = book_mark.shape
    imrows, _, _ = image.shape
    fact = calc_fact(imrows, y)
    print(fact)
    if rows + y * fact > imrows:
        print("yes")
        y -= rows
    image[int(y * fact):int(rows + (y * fact)), 0:cols] = book_mark
    image2[int(y * fact):int(rows + (y * fact)), 0:cols] = book_mark
    cv.imwrite(f"{path}\\{index}.png", image)
    cv.imwrite(f"{path}\\night\\{index}.png", image2)




def print_coord(event, x, y, flags, param):
    global xpos
    global ypos
    if event == cv.EVENT_LBUTTONDOWN:
        print(f'{x, y}\r')
        xpos = x
        ypos = y


def row_mark(b_mark, index, path):
    img = cv.imread(f'{path}\\{index}.png')
    cols, rows, _ = img.shape
    img = cv.resize(img, (int(rows / 3.5), int(cols / 3.5)))
    cv.namedWindow('Get Coordinates')
    cv.setMouseCallback('Get Coordinates', print_coord)
    cv.imshow('Get Coordinates', img)
    cv.waitKey(0)
    add_row_mark(b_mark,index,path, xpos,ypos)



def concat_images():
    images = [Image.open(x) for x in ['IMAGES/0.png', 'IMAGES/2.png', 'IMAGES/3.png']]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(heights)
    max_height = max(widths)

    new_im = Image.new('RGB', (max_height, total_width))

    x_offset = 0
    for im in images:
        new_im.paste(im, (0, x_offset))
        x_offset += im.size[1]

    new_im.save('4.png')
