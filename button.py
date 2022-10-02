from tkinter import *
# this is just for learning the gui
root = Tk()
def myClick():
    myLabel = Label(root, text="See I clicked the button")
    myLabel.pack()
myButton= Button(root, text="Click Me !", command=myClick,bg='yellow')
myButton.pack()
root.mainloop()
