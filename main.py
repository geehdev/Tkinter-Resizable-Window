from os.path import exists
from tkinter import *
from tkinter import messagebox as ms
from tkinter.ttk import Treeview


def insert_data():
    "add data to treeview."
    name = entry_name.get()
    age = entry_age.get()
    telephone = entry_fone.get()

    if bool(name) and bool(age) and bool(telephone):
        tree.insert('', END, values=(name, age, telephone))
        entry_name.delete(0, END)
        entry_age.delete(0, END)
        entry_fone.delete(0, END)
        entry_name.focus()
    else:
        ms.showerror(title="Resizable Window", message="Do not leave the fields empty.")


def delete_data():
    "Remove data from treeview."
    try:
        tuple_items = tree.selection()[0]
        tree.delete(tuple_items)
    except IndexError:
        ms.showinfo(title="Resizable Window", message="Nothing was selected!")


def show_data():
    "show selected data."
    try:
        tuple_items = tree.selection()[0]
        result = tree.item(item=tuple_items, option='values')
        ms.showinfo(title="Your Info", message=f"Name: {result[0]} / Age: {result[1]} / Telephone: {result[2]}")
    except IndexError:
        ms.showinfo(title="Resizable Window", message="Nothing was selected!")

# open(file='data_user.txt', mode='w').close() if exists('data_user.txt') == False else ''

# programa principal
root = Tk()
root.title('Resizable Window')
root.geometry('650x332+350+200')
root.config(bg='#4f0c4b')

lb_frame_registration = LabelFrame(root, text='Your Information', fg='#9a09b0' , bg='#9c8e9b', width=288, height=180, borderwidth=2, font=('Gabriola', 15, 'italic'))
lb_show_data = LabelFrame(root, text='Registered Data', fg='#9a09b0' , bg='#9c8e9b', width=288, height=180, borderwidth=2, font=('Gabriola', 15, 'italic'))

var_name = Label(lb_frame_registration, background='#9c8e9b', text='Name', font=('Times', 10, 'bold',  'italic') )
var_age = Label(lb_frame_registration, background='#9c8e9b', text='Age', font=('Times', 10, 'bold',  'italic') )
var_fone = Label(lb_frame_registration, background='#9c8e9b', text='Telephone', font=('Times', 10, 'bold',  'italic') )

entry_name = Entry(lb_frame_registration)
entry_age = Entry(lb_frame_registration, justify=CENTER)
entry_fone = Entry(lb_frame_registration)

# Treeview
tree = Treeview(lb_show_data, columns=('name_column', 'age_column', 'phone_column'), show='headings')

# configurando as colunas
tree.column('name_column', width=160)
tree.column('age_column', width=40)
tree.column('phone_column', width=100)

#definindo nomes as colunas
tree.heading('name_column', text='Name', anchor=CENTER)
tree.heading('age_column', text='Age', anchor=CENTER)
tree.heading('phone_column', text='Telephone', anchor=CENTER)

# posicionando widgets
lb_frame_registration.place(relx=0.009, rely=0.04, relheight=0.85, relwidth=0.48)
lb_show_data.place(relx=0.489, rely=0.04, relheight=0.85, relwidth=0.5)

var_name.place(relx=0.01, rely=0, relheight=0.19, relwidth=0.2)
var_age.place(relx=0.01, rely=0.21, relheight=0.19, relwidth=0.2)
var_fone.place(relx=0.01, rely=0.42, relheight=0.19, relwidth=0.2)

entry_name.place(relx=0.22, rely=0, relheight=0.12, relwidth=0.77 )
entry_age.place(relx=0.22, rely=0.21, relheight=0.12, relwidth=0.1)
entry_fone.place(relx=0.22, rely=0.42, relheight=0.12, relwidth=0.30)

tree.place(relx=0.02 ,rely=0, relwidth=0.96, relheight=0.98)

# Buttons
Button(lb_frame_registration, text='Insert Data', bg='#255385', relief='raised', border=1, command=insert_data).place(relx=0.02 ,rely=0.7, relwidth=0.96, relheight=0.15)
Button(root, text='Delete Data', bg='#255385', relief='raised', border=1, command=delete_data).place(relx=0.62 ,rely=0.9, relwidth=0.1, relheight=0.1)
Button(root, text='Show Data', bg='#255385', relief='raised', border=1, command=show_data).place(relx=0.8 ,rely=0.9, relwidth=0.1, relheight=0.1)

root.mainloop()