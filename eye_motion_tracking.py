import requests
from PIL import ImageGrab
import cv2
import winsound
from datetime import datetime
import numpy as np
import imutils

# Initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Variable store execution state
url = "http://192.168.1.2:8080/shot.jpg"
def take_screenshot():
    first_read = True
    blink_counter = 0
    winname = "blinking"
    cv2.namedWindow(winname)
    cv2.moveWindow(winname, 40, 30)
    # Starting the video capture
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, img = cap.read()
    while (True):
        ret, img = cap.read()
        ############################ start of mobile
        # img_resp = requests.get(url)
        # img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        # img = cv2.imdecode(img_arr, -1)
        # img = imutils.resize(img, width=1500, height=2700)
        # img1=img
        ########################### end of mobile
        # Converting the recorded image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        alpha = 1.1  # Contrast control (1.0-3.0)
        beta = 10  # Brightness control (0-100)
        gray = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
        # Applying filter to remove impurities
        gray = cv2.bilateralFilter(gray, 5, 1, 1)

        # Detecting the face for region of image to be fed to eye classifier
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(180, 180))
        if (len(faces) > 0):
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # img = cv2.resize(img,(200,200))
                # roi_face is face which is input to eye classifier
                roi_face = gray[y:y + h, x:x + w]
                roi_face_clr = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 5, minSize=(50, 50))
                # Examining the length of eyes object for eyes
                if len(eyes) >0:
                    for (x, y, w, h) in eyes:
                        # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        # img = cv2.resize(img,(200,200))
                        # roi_face is face which is input to eye classifier
                        roi_face = gray[y:y + h, x:x + w]
                        img1=roi_face
                        roi_face_clr = img[y:y + h, x:x + w]
                        # eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 5, minSize=(50, 50))
                        # Examining the length of eyes object for eyes

                    # Check if program is running for detection
                    blink_counter = 0
                    cv2.putText(img,
                                "Eyes open!", (70, 70),
                                cv2.FONT_HERSHEY_PLAIN, 2,
                                (255, 255, 255), 2)


                else:
                    blink_counter += 1
                    print(f"blink{blink_counter}")
                    if blink_counter > 10:
                        frequency = 2500  # Set Frequency To 2500 Hertz
                        duration = 500  # Set Duration To 1000 ms == 1 second
                        winsound.Beep(frequency, duration)
                        im = ImageGrab.grab()
                        date = datetime.now()
                        im.save(f"IMAGES/Screenshots/{date.time().microsecond}.png")
                        blink_counter = 0

        img = cv2.resize(img, (400, 300))
        cv2.imshow(winname, img)
        a = cv2.waitKey(1)
        if (a == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

# take_screenshot()