from tkinter import *
# this is just for learning the gui
root = Tk()
e = Entry(root, width =50, bg='yellow', fg='red', borderwidth=5)
e.insert(0, "Ent youer your name: ")
e.pack()


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
myButton= Button(root, text="Enter Your name", command=myClick,bg='yellow')
myButton.pack()
root.mainloop()
