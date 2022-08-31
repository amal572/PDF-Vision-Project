import cv2
import numpy as np
import pyautogui

import gui

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def scroll():
    left = 0
    right = 0
    work = False
    while True:
        _, frame = cap.read()
        # cv2.imshow('Frame', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        alpha = 1.2  # Contrast control (1.0-3.0)
        beta = 0  # Brightness control (0-100)
        gray = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
        # Applying filter to remove impurities
        # gray_roi = cv2.bilateralFilter(gray, 5, 1, 1)
        gray_roi = gray
        # Detecting the face for region of image to be fed to eye classifier
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(170, 170))
        if (len(faces) > 0):
            print("yes")
            for (x, y, w, h) in faces:
                roi_faces = gray[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_faces, 1.3, 5, minSize=(50, 50))
                # Examining the length of eyes object for eyes
                if len(eyes) >= 0.01:
                    for (x, y, w, h) in eyes:
                        roi = roi_faces[y + 10:y + h, x:x + w]
                        roi = cv2.resize(roi, (600, 600))
        else:
            roi = gray_roi[69:395, 137:716]
        rows, col = roi.shape
        # gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        # gray_roi = cv2.GaussianBlur(roi,(7,7), 0) # Removing Noises
        gray_roi = roi
        _, thres = cv2.threshold(gray_roi, 70, 255, cv2.THRESH_BINARY_INV)
        roi = cv2.line(roi, (0, 250), (600, 250), (255, 255, 255), 2)
        roi = cv2.line(roi, (300, 0), (300, 600), (255, 255, 255), 2)
        contours, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Bounday of white sapce
        contours = sorted(contours, key=lambda x: cv2.contourArea(x),
                          reverse=True)  # it will sort the contours of big to small
        # print(contours)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            # cv2.drawContours(roi, cnt, -1,(0,  0, 255), 3) # here we only print the biggest area
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(w / 2)), (col, y + int(w / 2)), (0, 255, 0), 2)
            if work:
                if x + (w / 2) > 320:
                    left += 1
                    right = 0
                    if left == 2:
                        pyautogui.click(1290, 360)
                        left = 0
                        print("left")
                elif x + (w / 2) < 280:
                    left = 0
                    right += 1
                    if right == 2:
                        pyautogui.click(1290, 413)
                        print("right")
                else:
                    left = 0
                    right = 0
                    print("middle")
            break
                # cv2.imshow("Threshold", thres)
                # cv2.imshow("Gray_Frame", gray_roi)
        cv2.imshow("Roi", roi)
        key = cv2.waitKey(30)
        if key == 27:
            break
        if key == 32:
            work = not work
            print("yyyyes")
    cv2.destroyAllWindows()
