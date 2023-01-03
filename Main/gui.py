# from live import Face0
# from imgface import Face1
# from videoface import Face2
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfilename
import numpy as np
import cv2 
import os 
import matplotlib.pyplot as plt
# ----------------------------------------Open Image ------------------------------------
def browsefunc1():
      filename = askopenfilename(filetypes=(("jpg file", "*.jpg"), ("png file ",'*.png'), ("All files", "*.*"),))
      path = str(filename)
      return path

    
# ----------------------------------------Open Video-------------------------------------
def browsefunc2():
      filename1 = askopenfilename(filetypes=(("mp4 file", "*.mp4"), ("All files", "*.*"),))
      path1 = str(filename1)
      return path1
      
      
#-----------------------------------------Browse Button --------------------------------
def browse():
    win = Tk()
    label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
    label.pack(pady=10)
    # Create a Button
    ttk.Button(win, text="Browse", command=browsefunc1).pack(pady=20)
    win.mainloop()


# ----------------------------------------Image Face detection --------------------------
def opencam2():
        classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
        i1 = browsefunc1()
        img = cv2.imread(i1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = classifier.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in face:
                cv2.rectangle(img, (x, y), (x + w, y + h), (225, 1, 1), 3)
        cv2.imshow('Image', img)
        cv2.waitKey()


# ----------------------------------------Live Face detection --------------------------
def openCamera():
        classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
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


# ----------------------------------------Video Face Detection -------------------------
def openCam3():
        classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
        l2 = browsefunc2()
        cap = cv2.VideoCapture(l2)  # 0 means we are selecting default video source

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


# ----------------------------------------UI SETUP ------------------------------------
window = Tk()
window.title('Face Detection')
window.config(padx=100, pady=100, bg= '#6fefdb')

title_label = Label(text='FACE DETECTION', fg='black', bg='#6fefdb', font=("Open Sans", 50, 'bold'))
title_label.grid(column=1, row=0)

canvas = Canvas(width=730, height=600, bg='#6fefdb', highlightthickness=0)
img = PhotoImage(file='imgmodule1.png')
canvas.create_image(372, 170, image=img)
canvas.grid(column=1, row=1)

lvb = PhotoImage(file='live.png')
live_button = Button(window, image=lvb, border=0, bg='#6fefdb',highlightthickness=0,command=openCamera)
live_button.grid(column=0, row=2)

vdb = PhotoImage(file='video.png')
vid_button = Button(window, image=vdb, border=0, bg='#6fefdb',highlightthickness=0, command=openCam3)
vid_button.grid(column=1, row=2)

imb = PhotoImage(file='imgbutton.png')
img_button = Button(window, image=imb, border=0, bg='#6fefdb',highlightthickness=0, command=opencam2)
img_button.grid(column=2, row=2)

# br_button = Button(text="Select", highlightthickness=0, command=browse)
# br_button.grid(column=2, row=3)

window.mainloop()



