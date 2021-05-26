from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox

def connect():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                        database='inventory_system',
                                        user='root',
                                        password='Shamra123')
    cursor = conn.cursor()
def ViewStock():
    connect()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    cursor.close()
def ajaxStock():
    connect()
    get_id=enteride.get()
    cursor.execute("SELECT * FROM inventory WHERE id= %s",[get_id])
    pc = cursor.fetchall()
    if pc:
        for r in pc:
            get_id=r[0]
            get_name=r[1]
            get_stock=r[2]
            get_rack = r[3]
            get_section = r[4]
        productname.configure(text=" Product Name           :   " +str(get_name),fg='black')
        pprice.configure(text=" Quantity Available   :   "+str(get_stock),fg='black')
        location.configure(text=" Location                  :   RackNo: " + str(get_rack)+ "\n\n                            :   SectionNo: "+ str(get_section), fg='black')
    #else:
      #  lbl_result = Label(text="Invalid username or password", font=('arial', 18),fg="red")
def ViewFormStock(ex1):
    global productname,pprice,enteride,tree,location
    viewform = ex1
    tree = ttk.Treeview(viewform, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="PRODUCT_ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="PRODUCT_NAME")

    tree.pack()
    ViewStock()

    # enter stuff
    enterid = Label(viewform,text="Enter Product's ID", font=('arial 15 bold'), fg='black')
    enterid.place(x=20, y=300)
    enteride = Entry(viewform,width=5, font=('arial 15 bold'), bg='white')
    enteride.place(x=220, y=300)
    enteride.focus()
    # button
    #search_btn1 = Button(viewform, text="Refresh", command=ajaxStock)
    #search_btn1.place(x=150, y=200)

    search_btn = Button(viewform,text="Search", bg="#00022e", fg='white', command=ajaxStock)
    search_btn.place(x=300, y=300)

    productname = Label(viewform,text="", font=('arial 15 bold'), fg='steelblue')
    productname.place(x=20, y=400)

    pprice = Label(viewform,text="", font=('arial 15 bold'), fg='steelblue')
    pprice.place(x=20, y=440)

    location = Label(viewform,text="", font=('arial 15 bold'), fg='steelblue')
    location.place(x=20, y=480)

def ShowStock(ex):
    viewform = ex
    ViewFormStock(viewform)
