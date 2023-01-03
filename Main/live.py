import numpy as np
import cv2


class Face0:
    def openCamera(self):
        classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalcatface_extended.xml')
        cap = cv2.VideoCapture(0)  # 0 means we are selecting default video source

        while cap.isOpened():
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert all the frames to gray scale
            detect = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)  # 1.Source of the image, 2.
            for (x, y, w, h) in detect:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 1, 1), 3)
            cv2.imshow('farme', frame)
            if cv2.waitKey(10)  == ord('x'):
                break
        cap.release()

face = Face0()
face.openCamera()
