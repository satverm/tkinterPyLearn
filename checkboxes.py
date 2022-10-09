from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Check Boxes")
root.iconbitmap("my_icon.ico")
root.geometry("700x500")

def show():
    my_label = Label(root, text= var_1.get()).pack()
    my_labe2 = Label(root, text= var_2.get()).pack()

# var = IntVar()  # can be used when you use 1/0 

var_1 = StringVar()
c_btn_1 = Checkbutton(root,text="Click to Select", variable=var_1, onvalue="Selected", offvalue="Not Selected") # we can use any string for onvalue and offvalue
c_btn_1.deselect()
c_btn_1.pack()

# check button 2
var_2 = StringVar()
c_btn_2 = Checkbutton(root,text="Click to Select", variable=var_2, onvalue="Selected", offvalue="Not Selected") # we can use any string for onvalue and offvalue
c_btn_2.deselect()
c_btn_2.pack()


myButton = Button(root, text= "Show Selection", command=show).pack()

root.mainloop()