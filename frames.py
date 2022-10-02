from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("frames in tkinter")
root.iconbitmap('emacs.ico')

frame = LabelFrame(root,text="The first frame",padx=100, pady=80)
frame.pack(padx=10, pady=50)

button1 = Button(frame, text="This button is inside the frame")
button1.grid(row=0, column=0)
button2 = Button(frame,text="This is button 2")
button2.grid(row=2, column=0)

exit_button = Button(root,text= "Click to exit", command= root.quit)
exit_button.pack(padx= 10, pady=10)



root.mainloop()