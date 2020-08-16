import sqlite3
import os
import csv
import pandas as pd
from tkinter import ttk
import tkinter as tk


cwd=os.getcwd()
database = (r"{0}\attendence.db".format(cwd))
conn = sqlite3.connect(database)
#conn.execute("-header -csv attendence.db 'select * from record;'> data.csv")
def export():
    print("Exporting data into CSV............")
    cursor = conn.cursor()
    cursor.execute("select * from record")
    with open("attendence.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=",")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)
    dirpath = os.getcwd() + "attendence.csv"
    print ("Data exported Successfully into {}".format(dirpath))

def csvtoexcel():
    readfile = pd.read_csv(r"{0}/attendence.csv".format(cwd))
    readfile.to_excel("attendence.xlsx")
    print("Excel is expored")
    mark ="Attendance mark successfully "
    popupmsg(mark)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

if __name__ == '__main__':
    export()
    csvtoexcel()
