from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Database with Tk")
root.iconbitmap("my_icon.ico")
root.geometry("500x500")


# Creating database
conn = sqlite3.connect('project_file.db')
# create a cursor
cur = conn.cursor()
cur.execute('''CREATE TABLE  IF NOT EXISTS project (
    project_name text,
    project_type text,
    project_cost intiger,
    project_head text,
    project_duration_months intiger
    )''')
conn.commit()
conn.close()

def append_data():

    conn = sqlite3.connect('project_file.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO project VALUES (:project_name,:val_2,:val_3, :val_4, :val_5)",
            {
                'project_name': project_name.get(),
                'val_2': project_type.get(),
                'val_3': project_cost.get(),
                'val_4': project_head.get(),
                'val_5': project_duration_months.get()
            })
    conn.commit()
    conn.close()

    project_name.delete(0, END)
    project_type.delete(0, END)
    project_cost.delete(0, END)
    project_head.delete(0, END)
    project_duration_months.delete(0, END)


project_name = Entry(root, width=30)
project_name.grid(row=0, column=1)
project_type = Entry(root, width=30)
project_type.grid(row=1, column=1)
project_cost = Entry(root, width=30)
project_cost.grid(row=2, column=1)
project_head = Entry(root, width=30)
project_head.grid(row=3, column=1 )
project_duration_months  = Entry(root, width=30)
project_duration_months.grid(row=4, column=1)

# Now let's create the labels for these items

project_name_label = Label(root,text="Project Name", width=30)
project_name_label.grid(row=0, column=0)
project_type_label = Label(root,text= "Project Type", width=30)
project_type_label.grid(row=1, column=0)
project_cost_label = Label(root,text= "Project Cost", width=30)
project_cost_label.grid(row=2, column=0)
project_head_label = Label(root, text= "Project Head", width=30)
project_head_label.grid(row=3, column=0 )
project_duration_months_label  = Label(root, text= "Project Duration", width=30)
project_duration_months_label.grid(row=4, column=0)

# submit buttons for updating the database
submit_button = Button(root, text="Add the data in the database",command= append_data)
submit_button.grid(row=6, column=0, columnspan=2, pady=5, padx=5, ipadx=170)





root.mainloop()