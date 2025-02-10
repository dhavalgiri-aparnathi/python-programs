from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as msc

conn = None
cursor = None

def configure_database():
    try:
        global conn
        global cursor
        conn = msc.connect (
            host='localhost',
            user='root',
            password='',
            database='my_db',
            autocommit=True
        )
        cursor = conn.cursor()
        # mb.showinfo('Success', 'Database configured successfully')
    except:
        mb.showerror('Error', 'Database configuration failed')
        exit()

def insert_data():
    if validate_data() == False:
        return
    global conn
    global cursor
    id = id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    sql = 'INSERT INTO mytable (Id, Name, Email, Phone) VALUES (%s, %s, %s, %s);'
    cursor.execute(sql, (id, name, email, phone))
    mb.showinfo('Success', 'Data inserted successfully')
    clear_entries()

def update_data():
    if validate_data() == False:
        return
    global conn
    global cursor
    id = id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    sql = 'UPDATE mytable SET Name = %s, Email = %s, Phone = %s WHERE Id = %s;'
    cursor.execute(sql, (name, email, phone, id))
    mb.showinfo('Success', 'Data updated successfully')
    clear_entries()

def delete_data():
    if id_entry.get() == '':
        mb.showwarning('Validation Error', 'Please enter the id to delete data')    
        return
    global conn
    global cursor
    id = id_entry.get()
    sql = "DELETE FROM mytable WHERE Id = '"+id+"';"
    cursor.execute(sql)
    mb.showinfo('Success', 'Data deleted successfully')
    clear_entries()

def display_data():
    if id_entry.get() == '':
        mb.showwarning('Validation Error', 'Please enter the id to delete data')    
        return
    global conn
    global cursor
    sql = "SELECT * FROM mytable WHERE id = '"+id_entry.get()+"';"
    cursor.execute(sql)
    data = cursor.fetchall()
    clear_entries()
    for row in data:
        id_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        email_entry.insert(0, row[2])
        phone_entry.insert(0, row[3])

def validate_data():
    id = id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    if name == '' or email == '' or phone == '' or id == '':
        mb.showwarning('Validation Error', 'One or more fields are empty, please enter all details')    
        return False
    else:
        return True

def clear_entries():
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)

configure_database()

root = Tk()
root.geometry('400x400')
root.title('CRUD Operations')
root.resizable(False, False)

Label(root, text='Enter Id').pack()
id_entry = Entry(root)
id_entry.pack(pady=10)

Label(root, text='Enter Name').pack()
name_entry = Entry(root)
name_entry.pack(pady=10)

Label(root, text='Enter Email').pack()
email_entry = Entry(root)
email_entry.pack(pady=10)

Label(root, text='Enter Phone').pack()
phone_entry = Entry(root)
phone_entry.pack(pady=10)

Button(root, text='Insert Data', command=insert_data).pack(pady=5)
Button(root, text='Update Data', command=update_data).pack(pady=5)
Button(root, text='Delete Data', command=delete_data).pack(pady=5)
Button(root, text='Display Data', command=display_data).pack(pady=5)

root.mainloop()