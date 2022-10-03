from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.title("Learn Messages")
root.iconbitmap('emacs.ico')

def popup():
    # messagebox.showinfo("This is a message box","Hello World")
    answer= messagebox.askyesno("Select Yes/No","Select Yes or No")
    Label(root, text=answer).pack()
    if answer == 1:
        Label(root, text= "you selected a 'Yes'!").pack()
    else:
        Label(root, text= "You selected a 'NO'!!").pack()

Button(root, text="Popup",command=popup).pack()

root.mainloop()