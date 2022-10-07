from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()  # main window to start with
root.title("Learn windows")
root.iconbitmap('emacs.ico')
my_img1 = ImageTk.PhotoImage(Image.open("images/img_1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img_2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img_3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img_4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img_5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/img_6.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4,my_img5, my_img6]

game_win = Toplevel()

# now working a little
# here we are creating two windows and then using the main window to to generate random images in new window

def myClick(): # the function to open new random image based on a dice value
    # my_Label1 = Label(new_win,text="",padx=100,pady=100).pack()
    global game_win  # since it is also used outside this function
    game_win.destroy()  # to destroy any previous window
    game_win= Toplevel()
    dice_value = random.randint(0,5) # to get a random intiger 1-6
    my_img = image_list[dice_value]  # select an image from the list of images
    Label(game_win,text= dice_value, bg='yellow',fg='black',padx=20, pady=15).pack()
    Label(game_win,image=my_img).pack()

myButton= Button(root, text="Click to get random picture !", command=myClick,bg='yellow')
myButton.pack(padx=50,pady=50)

root.mainloop()     