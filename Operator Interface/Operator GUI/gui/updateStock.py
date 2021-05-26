# import all the modules
from tkinter import *
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox


def connect1():
    global conn1, cursor1, id
    conn1 = mysql.connector.connect(host='localhost',
                                    database='inventory_system',
                                    user='root',
                                    password='Shamra123')
    cursor1 = conn1.cursor()
    cursor1.execute("SELECT Max(id) from inventory")
    result = cursor1.fetchall()
    for r in result:
        id = r[0]


def ShowUpdate(ex):
    updateform =ex
    UpdateStock(updateform)


def UpdateStock(ex1):
    global id_leb,name_e,stock_e,stockn_e
    updateform = ex1
    heading = Label(updateform, text="Update Stock", font=('arial 25 bold'), fg='black')
    heading.place(x=20, y=0)

    # label and entry for id
    id_le = Label(updateform, text="Enter ID", font=('arial 18 bold'))
    id_le.place(x=20, y=70)

    id_leb = Entry(updateform, font=('arial 18 bold'), width=10)
    id_leb.place(x=280, y=70)

    btn_search = Button(updateform, text="search", bg="#00022e", fg='white', command=search)
    btn_search.place(x=450, y=70)

    # lables  for the window
    name_l = Label(updateform, text="Product Name", font=('arial 18 bold'))
    name_l.place(x=20, y=120)

    stock_l = Label(updateform, text="Available Quantity:", font=('arial 18 bold'))
    stock_l.place(x=20, y=170)

    stockn_l = Label(updateform, text="New Quantity", font=('arial 18 bold'))
    stockn_l.place(x=20, y=220)

    name_e = Entry(updateform, width=25, font=('arial 18 bold'))
    name_e.place(x=280, y=120)

    stock_e = Entry(updateform, width=25, font=('arial 18 bold'))
    stock_e.place(x=280, y=170)

    stockn_e = Entry(updateform, width=25, font=('arial 18 bold'))
    stockn_e.place(x=280, y=220)

    btn_add = Button(updateform, text='Update Stock', width=25, height=2, bg="#00022e", fg='white', command=update)
    btn_add.place(x=380, y=320)


def search():
    connect1()
    cursor1.execute("SELECT * FROM inventory WHERE id=%s", [id_leb.get()])
    result = cursor1.fetchall()
    for r in result:
        n1 = r[1]  # name
        n2 = r[2]  # stock

    conn1.commit()

    # inster into the enteries to update
    name_e.delete(0, END)
    name_e.insert(0, str(n1))

    stock_e.delete(0, END)
    stock_e.insert(0, str(n2))


def update():
    connect1()
    u1 = name_e.get()
    u2 = int(stock_e.get()) + int(stockn_e.get())

    cursor1.execute("UPDATE  inventory SET name=%s,stock=%s WHERE id=%s", [u1, u2, id_leb.get()])
    conn1.commit()
    tkinter.messagebox.showinfo("Success", "Updated stock successfully.")
