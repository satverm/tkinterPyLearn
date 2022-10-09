from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Drop down menu using list")
root.iconbitmap("my_icon.ico")

def show():
    seleced_label = Label(root, text= var_1.get()).pack()

options_list = [
    "item_1",
    "item_2",
    "item_3",
    "item_4",
    "item_5"
    ]    

var_1 = StringVar()
var_1.set("default_sel")
opt_btn = OptionMenu(root, var_1,*options_list)  # * is used to open the list items as arguments

opt_btn.pack()

button_show = Button(root, text= "Show selection", command= show).pack()



root.mainloop()