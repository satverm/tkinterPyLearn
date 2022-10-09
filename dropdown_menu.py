from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Drop down menu")
root.iconbitmap("my_icon.ico")

def show():
    seleced_label = Label(root, text= var_1.get()).pack()
    
var_1 = StringVar()
var_1.set("default_sel")
opt_btn = OptionMenu(root, var_1,"Selection_1","selection_2")
opt_btn.pack()

button_show = Button(root, text= "Show selection", command= show).pack()



root.mainloop()