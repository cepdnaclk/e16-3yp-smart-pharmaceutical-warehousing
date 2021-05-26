#import all the modules
from tkinter import *
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox

def connect1():
    global conn1,cursor1,id
    conn1 = mysql.connector.connect(host='localhost',
                                        database='inventory_system',
                                        user='root',
                                        password='Shamra123')
    cursor1 = conn1.cursor()
    cursor1.execute("SELECT Max(id) from inventory")
    result = cursor1.fetchall()
    for r in result:
        id = r[0]

def ShowAddNew(ex):
    addnewform = ex
    AddNewForm(addnewform)

def AddNewForm(ex1):
    global name_e, stock_e,rackNo_e,sectionNo_e
    addnewform=ex1
    heading = Label(addnewform, text="Add New Product", font=('arial 25 bold'), fg='black')
    heading.place(x=110,y=0)

    # lables  for the window
    name_l = Label(addnewform, text="Enter Product Name", font=('arial 18 bold'))
    name_l.place(x=20, y=70)

    stock_l = Label(addnewform, text="Enter Quantity", font=('arial 18 bold'))
    stock_l.place(x=20, y=120)

    rackNo_l = Label(addnewform, text="Enter RackNo", font=('arial 18 bold'))
    rackNo_l.place(x=20, y=170)

    sectionNo_l = Label(addnewform, text="Enter SectionNo", font=('arial 18 bold'))
    sectionNo_l.place(x=20, y=220)

    name_e = Entry(addnewform, width=25, font=('arial 18 bold'))
    name_e.place(x=280, y=70)

    stock_e = Entry(addnewform, width=25, font=('arial 18 bold'))
    stock_e.place(x=280, y=120)

    rackNo_e = Entry(addnewform, width=25, font=('arial 18 bold'))
    rackNo_e.place(x=280, y=170)

    sectionNo_e = Entry(addnewform, width=25, font=('arial 18 bold'))
    sectionNo_e.place(x=280, y=220)

    # button to add to the database
    btn_add = Button(addnewform, text='Add to Database', width=25, height=2, bg="#00022e", fg='white', command=get_items)
    btn_add.place(x=420, y=270)

    btn_clear = Button(addnewform, text="Clear All Fields", width=18, height=2, bg='red', fg='white',command=clear_all)
    btn_clear.place(x=250, y=270)

    addnewform.bind('<Return>', get_items)
    addnewform.bind('<Up>', clear_all)

def get_items():

    # get from entries
    connect1()
    name = name_e.get()
    stock = stock_e.get()
    rackNo = rackNo_e.get()
    sectionNo = sectionNo_e.get()

    # dynamic entries
    if name == '' or stock == '' or rackNo == '' or sectionNo == '' :
        tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
    else:
        cursor1.execute("INSERT INTO inventory (name, stock, rackNo, sectionNo) VALUES(%s,%s,%s,%s)",[name,stock,rackNo,sectionNo])
        conn1.commit()
        tkinter.messagebox.showinfo("Success", "Successfully added to the database")

def clear_all():
    connect1()
    num = id + 1
    name_e.delete(0, END)
    stock_e.delete(0, END)
    rackNo_e.delete(0, END)
    sectionNo_e.delete(0, END)


