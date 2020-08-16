from tkinter import *
import os
import sqlite3
from sqlite3 import Error

main = Tk()
main.geometry('{}x{}'.format(640, 420))
main.wm_title("Face recognition ")


comments = """Welcome to Face Recognition Based Attendence System 


"""

widgets = Label(main, justify=CENTER, padx=10, text=comments).pack(side="top")

comments1 =  "Developed and Design by Aseem Kanungo"
widgets1 = Label(main, justify=CENTER, padx=10, text=comments1).pack(side="bottom")

Label(main, text='Name',justify=CENTER).place(relx=0.30, y=100)
name = StringVar()
scholarid = StringVar()

w = Entry(main, textvariable=name, justify=LEFT)
w.pack()
w.place(relx=0.4,y=100)
Label(main, text='ScholarID',justify=CENTER).place(relx=0.54,y=100)

q= Entry(main,textvariable=scholarid, justify=LEFT) # adds a textarea widget
q.pack()
q.place(relx=0.64, y=100)


cwd=os.getcwd()
database = r"{0}\attendence.db".format(cwd)
conn = sqlite3.connect(database)



def database_button_fn():
    sql = ''' INSERT INTO record(name,scholarid)
                  VALUES(?,?) '''
    Name=name.get()
    scholarid1= scholarid.get()
    values=(Name,scholarid1)
    cur = conn.cursor()
    try:
        cur.execute(sql, values)
        print(Name, scholarid1, "1 record inserted")
    except Error as e:
        print(e)
        print("scholarid already inserted")
        Label(main, text='scholarid already inserted', justify=CENTER).place(relx=0.30, y=150)
    conn.commit()



def fisher_dataset_button_fn():

    os.system('python3 gui1.py ')



def fisher_atendence_button_fn():
    os.system('python3 03_face_recognition1.py')

def openattendence():

    os.system('start excel "attendence.xlsx"')

train_database_button = Button(main,text="Enter new data ", command=database_button_fn,justify=CENTER)
train_database_button.pack()
train_database_button.place(relx=0.74,y=95)

recog_fisher_button = Button(main, text="Add to dataset ", command=fisher_dataset_button_fn,justify=CENTER)
recog_fisher_button.pack()
recog_fisher_button.place(x=250,y=225)

recog_train_button = Button(main,text="Take Attendance", command=fisher_atendence_button_fn,justify=CENTER)
recog_train_button.pack()
recog_train_button.place(x=250,y=280)


openattendence = Button(main, text="Open Attendance ", command=openattendence, justify=CENTER)
openattendence.pack()
openattendence.place(x=250,y=310)
main.mainloop()

