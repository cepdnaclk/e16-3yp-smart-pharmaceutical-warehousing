from tkinter import ttk

import tkinter as tk
import mysql.connector


from tkinter import *
from tkinter import messagebox

def connect():
    global conn,cursor
    conn = mysql.connector.connect(host='localhost',
                                        database='inventory_system',
                                        user='root',
                                        password='Shamra123')
    cursor = conn.cursor()

def ViewAGV():
    cursor.execute("SELECT * FROM robotAGV")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.close()


def ajaxAGV():
    global get_battery, get_status, get_order
    connect()
    get_robotId = enteride.get()
    cursor.execute("SELECT * FROM robotAGV WHERE robotId= %s", [get_robotId])
    pc = cursor.fetchall()
    if pc:
        for r in pc:
            get_robotId = r[0]
            get_status = r[1]
            get_battery = r[2]
            get_order = r[3]
        battery.configure(text="Battery: " + str(get_battery)+"%", fg='black')
        status.configure(text="Status: " + str(get_status), fg='black')
        order.configure(text="Currently Processing Order: " +str(get_order), fg='black')

def ViewFormAGV():
    global tree,enterId, battery, status, order, enteride
    tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="AGV ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="STATUS")
    tree.pack()
    ViewAGV()

    # enter stuff
    enterid = Label(text="Enter AGV ID", font=('arial 15 bold'), fg='black')
    enterid.place(x=20, y=300)
    enteride = Entry(width=5, font=('arial 15 bold'), bg='white')
    enteride.place(x=250, y=300)
    enteride.focus()
    # button
    search_btn = Button(text="Go", command=ajaxAGV)
    search_btn.place(x=350, y=300)

    battery = Label(text="", font=('arial 15 bold'), fg='steelblue')
    battery.place(x=20, y=350)

    status = Label(text="", font=('arial 15 bold'), fg='steelblue')
    status.place(x=20, y=390)

    order = Label(text="", font=('arial 15 bold'), fg='steelblue')
    order.place(x=20, y=430)

    #location = Label(text="Location of AGV's", font=('arial 15 bold'), fg='black')
    #location.place(x=20, y=500)

    #search_btn = Button(text="Locate")
    #search_btn.place(x=250, y=500)



# connect to the database
connect()
root = tk.Tk()
root.title("AGV Status ")
root.geometry("450x500+0+0")
ViewFormAGV()
root.mainloop()