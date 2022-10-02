from tkinter import *
# this is just for learning the gui
root = Tk()
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Hey my name is Satya")
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

root.mainloop()
