from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Check Boxes")
root.iconbitmap("my_icon.ico")
root.geometry("700x500")

def show():
    my_label = Label(root, text= var.get()).pack()

# var = IntVar()  # depends on whar you use 1/0 or On/Off

var = StringVar()

c_btn = Checkbutton(root,text="Click to Select", variable=var, onvalue="Selected", offvalue="Not Selected") # we can use any string for onvalue and offvalue
c_btn.deselect()

c_btn.pack()

myButton = Button(root, text= "Show Selection", command=show).pack()

root.mainloop()