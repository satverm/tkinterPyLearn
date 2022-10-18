from cgi import print_directory
from cgitb import text
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

# function to delte the data from records table
def remove_rec():
    conn = sqlite3.connect('project_file.db')
    cur = conn.cursor()
    # to select oid we will use " + and this way we can refer to intiger as under
    cur.execute("DELETE from project WHERE oid = " + remove_rec_box.get())
    remove_rec_box.delete(0, END)
    conn.commit()
    conn.close()

def append_data():

    conn = sqlite3.connect('project_file.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO project VALUES (:val_1,:val_2,:val_3, :val_4, :val_5)",
            {
                'val_1': project_name.get(),
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

def show_rec():
    conn = sqlite3.connect('project_file.db')
    cur = conn.cursor()
    cur.execute("SELECT *, oid FROM project")
    records= cur.fetchall()
    # print(records) we can change the print_records variable to print records in a specific way
    print_records = ''
    for item in records:
        print_records += str(item[0]) +" "+ str(item[1]) +"\t"+str(item[5]) + "\n"
    # records label contains the string print_records
    records_label = Label(root, text=print_records)
    records_label.grid(row=12, column=0, columnspan=2)
       
    conn.commit()
    conn.close()

# edit_rec to edit the database
def edit_rec():
    edit_win = Tk()
    edit_win.title("Edit a record")
    edit_win.iconbitmap('my_icon.ico')
    edit_win.geometry('500x400')
    
    conn = sqlite3.connect('project_file.db')
    cur = conn.cursor()
    sel_rec_id = remove_rec_box.get()
    cur.execute("SELECT * FROM project WHERE oid = " + sel_rec_id)
    records= cur.fetchall()
    # print(records) we can change the print_records variable to print records in a specific way
    print_records = ''
    for item in records:
        print_records += str(item[0]) +" "+ str(item[1]) +"\t"+str(item[4]) + "\n"
    # records label contains the string print_records
    records_label = Label(root, text=print_records)
    records_label.grid(row=12, column=0, columnspan=2)
       
    conn.commit()
    conn.close()
    # These are entry boxes for user to enter the data
    project_name_edit = Entry(edit_win, width=30)
    project_name_edit.grid(row=0, column=1 , padx=20, pady=(20,0))
    project_type_edit = Entry(edit_win, width=30)
    project_type_edit.grid(row=1, column=1)
    project_cost_edit = Entry(edit_win, width=30)
    project_cost_edit.grid(row=2, column=1)
    project_head_edit = Entry(edit_win, width=30)
    project_head_edit.grid(row=3, column=1 )
    project_duration_months_edit  = Entry(edit_win, width=30)
    project_duration_months_edit.grid(row=4, column=1)

    # Now let's create the labels for these items

    project_name_label = Label(edit_win,text="Project Name", width=30)
    project_name_label.grid(row=0, column=0, pady=(20,0))
    project_type_label = Label(edit_win,text= "Project Type", width=30)
    project_type_label.grid(row=1, column=0)
    project_cost_label = Label(edit_win,text= "Project Cost", width=30)
    project_cost_label.grid(row=2, column=0)
    project_head_label = Label(edit_win, text= "Project Head", width=30)
    project_head_label.grid(row=3, column=0 )
    project_duration_months_label  = Label(edit_win, text= "Project Duration", width=30)
    project_duration_months_label.grid(row=4, column=0)

    for record in records:
        project_name_edit.insert(0, record[0])
        project_type_edit.insert(0, record[1])
        project_cost_edit.insert(0, record[2])
        project_head_edit.insert(0, record[3])
        project_duration_months_edit.insert(0, record[4])
    
    save_btn = Button(edit_win, text='Save record', command= save_rec)
    save_btn.grid(row=5,column=0, columnspan=2, padx=10, pady=10, ipadx=143)

# These are entry boxes for user to enter the data
project_name = Entry(root, width=30)
project_name.grid(row=0, column=1 , padx=20, pady=(20,0))
project_type = Entry(root, width=30)
project_type.grid(row=1, column=1)
project_cost = Entry(root, width=30)
project_cost.grid(row=2, column=1)
project_head = Entry(root, width=30)
project_head.grid(row=3, column=1 )
project_duration_months  = Entry(root, width=30)
project_duration_months.grid(row=4, column=1)
remove_rec_box = Entry(root, width=20)
remove_rec_box.grid(row=9, column=1, padx=5, pady= 5)

# Now let's create the labels for these items

project_name_label = Label(root,text="Project Name", width=30)
project_name_label.grid(row=0, column=0, pady=(20,0))
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
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=98)

# button to test if data has been updated
query_btn = Button(root, text="Show reconds", command=show_rec)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)
remove_rec_box_lbl= Label(root, text= "Select Record ID")
remove_rec_box_lbl.grid(row=9, column=0, padx=5, pady=5)

remove_btn = Button(root, text="Remove record", command=remove_rec)
remove_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=134)

# Now let's edit a record
edit_btn = Button(root, text='Edit record', command= edit_rec)
edit_btn.grid(row=11,column=0, columnspan=2, padx=10, pady=10, ipadx=143)


root.mainloop()