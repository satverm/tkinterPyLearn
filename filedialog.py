from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# todo: how to have only one image even after the open file is used more than one times
root = Tk()
root.title('Opening a file using a dialog box')
root.iconbitmap("emacs.ico")
my_image_label = Label(root,text=" ").pack()
def open_file():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="images/", title= "Select a file", filetypes=(("jpg files","*.jpg"),("all files", "*.*")))
    my_label = Label(root, text= root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    global my_image_label
    my_image_label= Label(root, text="")
    
    my_image_label = Label(root, image=my_image).pack()

my_button= Button(root, text="Open file", command=open_file).pack()


root.mainloop()