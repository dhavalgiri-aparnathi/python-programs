from tkinter import *
from tkinter import messagebox

master = Tk()

master.geometry('450x320')
master.resizable(False, False)
master.title('Tkinter Form')

def show_data():
    name = name_textbox.get()
    email = email_textbox.get()
    contact = cnt_textbox.get()
    gender = selected_gender.get()
    country = selected_country.get()

    message = f'''
        Registered Name: {name}\n
        Registered Email: {email}\n
        Registered Contact: {contact}\n
        Registered Gender: {gender}\n
        Registered Country: {country}
    '''
    
    messagebox.showinfo('Success', message)

Label(master,text='Registration Form').place(x=200,y=0)

Label(master,text='Enter Name').place(x=100, y=40)
name_textbox = Entry(master)
name_textbox.place(x=220, y=40)

Label(master,text='Enter Email').place(x=100, y=80)
email_textbox = Entry(master)
email_textbox.place(x=220, y=80)

Label(master,text='Enter Contact No.').place(x=100, y=120)
cnt_textbox = Entry(master)
cnt_textbox.place(x=220, y=120)

Label(master,text='Select Country').place(x=100, y=160)
list_of_countries = ['India','Japan','USA','New Zealand']
selected_country = StringVar()
selected_country.set(list_of_countries[0])
OptionMenu(master, selected_country, *list_of_countries).place(x=220, y=160)

Label(master,text='Select Gender').place(x=100, y=200)
selected_gender = StringVar()
selected_gender.set(None)
Radiobutton(master, text='Male', value='Male', variable=selected_gender).place(x=220, y=200)
Radiobutton(master, text='Female', value='Female', variable=selected_gender).place(x=220, y=220)

Button(master, text='Register Now', width=33, command=show_data).place(x=100, y=260)

master.mainloop()
