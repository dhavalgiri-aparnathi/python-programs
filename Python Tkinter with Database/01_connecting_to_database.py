import mysql.connector as msc
from tkinter import *
from tkinter import messagebox

conn = None

def connection():
    try:
        global conn
        conn = msc.connect (
            host='localhost',
            user='root',
            password='',
            database='my_db'
        )
        messagebox.showinfo('Success', 'Connected to the database successfully')
    except:
        messagebox.showerror('Failure', 'An error occurred while connecting to the database')

root = Tk()

root.title('Tkinter Database Connectivity')
root.resizable(False, False)
root.geometry('500x200')

Button(root, text='Connect to Database', command=connection).pack()

root.mainloop()