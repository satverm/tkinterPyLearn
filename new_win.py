from tkinter import *
from PIL import ImageTk,Image
import random
root = Tk()
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

# Tey to make this work using the lambda function to pass values between 
def myClick():
    # my_Label1 = Label(new_win,text="",padx=100,pady=100).pack()
    global game_win

    game_win.destroy()
    game_win= Toplevel()
    my_Label2 = Label(game_win,text= "", bg='yellow',fg='black',padx=20, pady=15).pack()
    #new_win = Toplevel()
    dice_value = random.randint(0,5)
    my_img = image_list[dice_value]
    my_Label1= Label(game_win,text= dice_value, bg='yellow',fg='black',padx=20, pady=15).pack()
    my_Label2= Label(game_win,image=my_img).pack()
    #myLabel = Label(new_win, text="Click to roll the dice")
    #myLabel.pack()
myButton= Button(root, text="Click to get random picture !", command=myClick,bg='yellow')
myButton.pack(padx=20,pady=20)
# label_1 = Label(new_win,text= "Hello world in a new window").pack()

#my_img = image_list[2]
# dice_value = random.randint(0,5)
# my_img = image_list[dice_value]
# my_dice_label = Label(new_win,text= dice_value, bg='yellow',fg='black',padx=20, pady=15).pack()
# my_label = Label(new_win,image=my_img).pack()

root.mainloop()