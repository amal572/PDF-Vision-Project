import cv2
import requests
import numpy as np
import imutils

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# To capture video from webcam.
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
url = "http://192.168.1.4:8080/shot.jpg"
img_resp = requests.get(url)
img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
img = cv2.imdecode(img_arr, -1)
img = imutils.resize(img, width=1500, height=2700)
eye =img
while True:
    # Read the frame
    # _, img = cap.read()
    # eye = img
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1500, height=2700)
    img = img.astype(np.uint8)
    img = cv2.resize(img,(600,400))
    # Convert to grayscale
    alpha = 3  # Contrast control (1.0-3.0)
    beta = 10  # Brightness control (0-100)
    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 20)
    # Draw the rectangle around each face

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y + 10), (x + w, y + h), (255, 0, 0), 2)
        eye = gray[y + 5:y + h, x:x + w]
        eye = cv2.resize(eye, (600, 600))

    ret, thresh1 = cv2.threshold(eye, 30, 255, cv2.THRESH_BINARY)
    thresh1 = cv2.erode(thresh1, (15, 15), iterations=4)
    thresh1 = cv2.line(thresh1, (0, 250), (600, 250), (0, 0, 0), 2)
    thresh1 = cv2.line(thresh1, (0, 350), (600, 350), (0, 0, 0), 2)

    thresh1 = cv2.line(thresh1, (300, 0), (300, 600), (0, 0, 0), 2)  # middle line
    thresh1 = cv2.line(thresh1, (350, 0), (350, 600), (0, 0, 0), 2)  # to middle
    thresh1 = cv2.line(thresh1, (250, 0), (250, 600), (0, 0, 0), 2)  # left
    thresh1 = cv2.line(thresh1, (400, 0), (400, 600), (0, 0, 0), 2)  # right

    middle = thresh1[300:350, 250:350]
    left = thresh1[250:300, 250:350]
    right = thresh1[350:400, 250:350]
    try:
        m = cv2.countNonZero(middle)
        l = cv2.countNonZero(left)
        r = cv2.countNonZero(right)
        print(f"m = {m}  , l = {l}  , r = {r}")
        values = [m, l, r]
        minimum = values.index(min(values))
        # print(minimum)
        if minimum == 0:
            print("middle")
        elif minimum == 1:
            print("left")
        elif minimum == 2:
            print("right")
    except:
        print("err")

    cv2.imshow('img', img)
    cv2.imshow("eye", thresh1)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release the VideoCapture object
cap.release()
