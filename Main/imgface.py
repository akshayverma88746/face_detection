import numpy as np
import cv2


class Face1:
    def opencam2(self):
        classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalcatface_extended.xml')
        img = cv2.imread('images.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = classifier.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in face:
                cv2.rectangle(img, (x, y), (x + w, y + h), (225, 1, 1), 3)
        cv2.imshow('Image', img)
        cv2.waitKey()
    
imagedet = Face1()
imagedet.opencam2()
