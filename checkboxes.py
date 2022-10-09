from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Check Boxes")
root.iconbitmap("my_icon.ico")
root.geometry("700x500")

def show():
    my_label = Label(root, text= var.get()).pack()

var = IntVar()
c_btn = Checkbutton(root,text="Click to Select", variable=var)
c_btn.pack()

myButton = Button(root, text= "Show Selection", command=show).pack()

root.mainloop()