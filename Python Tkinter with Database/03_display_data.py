from tkinter import *
from tkinter import messagebox
import mysql.connector as msc

conn = None
db = None

def connection():
    global conn
    global db
    try:
        conn = msc.connect (
            host='localhost',
            user=username_textbox.get(),
            password=password_textbox.get(),
            database='my_db',
            autocommit=True
        )
        db = conn.cursor()
        messagebox.showinfo('Success', 'Connection to the database success, check the console')
        get_data()
    except:
        messagebox.showerror('Failure', 'Connection to the database failed')

def get_data():
    global db
    db.execute('SELECT * FROM mytable;')
    data = db.fetchall()
    for row in data:
        print(row)

root = Tk()

root.title('Tkinter Database')
root.geometry('500x200')
root.resizable(False, False)

Label(root, text='Enter Server Username').pack()
username_textbox = Entry(root)
username_textbox.pack(pady=10)

Label(root, text='Enter Server Password').pack()
password_textbox = Entry(root)
password_textbox.pack(pady=10)

Button(root, text='Connect', command=connection).pack(pady=10)

root.mainloop()