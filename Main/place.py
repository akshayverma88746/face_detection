from tkinter import *
from tkinter import  messageBox
import tkinter

top = tkinter.Tk()

def helloCallBack():
   /MessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
B.place(bordermode=OUTSIDE, height=100, width=100)
top.mainloop()