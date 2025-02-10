from tkinter import *
from tkinter import messagebox
import mysql.connector as msc

conn = None
db = None

def connection():
    try:
        global conn
        global db
        conn = msc.connect (
            host='localhost',
            user='root',
            password='',
            database='my_db',
            autocommit=True
        )
        db = conn.cursor()
    except:
        messagebox.showerror('Failure', 'An error occurred while connecting to the database')
        exit()

def insert_data():
    entered_username = username.get()    
    entered_password = password.get()

    global db
    query = 'INSERT INTO MyTable (Username, Password) VALUES (%s, %s);'
    db.execute(query, (entered_username, entered_password))
    messagebox.showinfo('Success', 'Data Inserted Successfully')

root = Tk()

root.title('Tkinter Database Connectivity')
root.resizable(False, False)
root.geometry('500x200')

connection()

Label(root, text='Enter Username').pack()
username = Entry(root)
username.pack()

Label(root, text='Enter Password').pack()
password = Entry(root)
password.pack()

Button(root, text='Insert Data', command=insert_data).pack()

root.mainloop()