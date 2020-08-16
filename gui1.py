from tkinter import *
import os

main = Tk()
main.geometry('{}x{}'.format(550, 550))
main.wm_title("Welcome to Face Recognition Based Attendence System ")

svalue3= StringVar() # defines the widget state as string
svalue2 = StringVar()

comments = """ Developed and Design by Aseem Kanungo"""




widgets = Label(main, 
           justify=CENTER,
           padx = 10, 
           text=comments).pack(side="bottom")


w = Entry(main,textvariable=svalue3) # adds a textarea widget
w.pack()
w.place(x=200,y=75)

def fisher_dataset_button_fn():

     scholarid= svalue3.get()
     os.system('python3 01_face_dataset.py {0}'.format(scholarid))
def camera(*args):
  camerano= svalue2.get()
  os.system('python3 01_face_dataset.py {0}'.format(camerano))

train_database_button = Button(main,text="Scholar ID", command=fisher_dataset_button_fn, justify=CENTER, padx = 10)
train_database_button.pack()
train_database_button.place(x=200, y=110)
a=[0,1]
popupMenu = OptionMenu(main, svalue2, *a)
Label(main, text="Choose a Camera").place(x=250, y=150)
popupMenu.place(x=250,y=160)



main.mainloop()
