from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Radio buttons in tkinter")
root.iconbitmap('emacs.ico')

# opt = IntVar()
# opt.set(1)

MODES =  [
    ("Onion", "Onion"),
    ("Tomato", "Tomato"),
    ("Spinach", "Spinach"),
    ("Paneer", "Paneer"),
]

Vegetable = StringVar()
Vegetable.set("Onion")

for text, mode in MODES:
    Radiobutton(root, text= text, variable=Vegetable, value=mode).pack()



def clicked(value):
    myLabel = Label(root, text= value)
    myLabel.pack()

# Radiobutton(root, text="Option 1", variable= opt, value=1, command=lambda: clicked(opt.get())).pack()
# Radiobutton(root, text="Option 2", variable= opt, value=2, command=lambda: clicked(opt.get())).pack()
# Radiobutton(root, text="Option 3", variable= opt, value=3, command=lambda: clicked(opt.get())).pack()
# Radiobutton(root, t,ext="Option 4", variable= opt, value=4, command=lambda: clicked(opt.get())).pack()

myLabel = Label(root, text= Vegetable.get())
myLabel.pack()
myButton = Button(root, text="Click Me", command=lambda: clicked(Vegetable.get()))
myButton.pack()
root.mainloop()