from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
root.iconbitmap("emacs.ico")
root.geometry("500x400")

def slide():
    my_label_h = Label(root, text=horizontal.get()).pack(anchor=E)
    my_label_v = Label(root, text=vertical.get()).pack(anchor=E)
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
    

vertical = Scale(root,from_=100,to=700)
vertical.pack(anchor=E)

horizontal = Scale(root, from_=300, to=900, orient= HORIZONTAL)
horizontal.pack(anchor=S)

my_label_h = Label(root, text=horizontal.get()).pack(anchor=N)
my_label_v = Label(root, text=vertical.get()).pack(anchor=N)
my_button = Button(root, text="Click to update", command=slide).pack(anchor=S)





root.mainloop()