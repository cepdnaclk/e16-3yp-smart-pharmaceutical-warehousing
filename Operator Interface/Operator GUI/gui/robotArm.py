from tkinter import ttk
import tkinter as tk

import PIL
import mysql.connector
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk


def connect():
    global conn,cursor
    conn = mysql.connector.connect(host='localhost',
                                        database='inventory_system',
                                        user='root',
                                        password='Shamra123')
    cursor = conn.cursor()
def ViewArm():
    connect()
    cursor.execute("SELECT * FROM robotArm")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.close()
def ajaxArm():
    global get_battery, get_status, get_order
    connect()
    get_robotId = enteride.get()
    cursor.execute("SELECT * FROM robotArm WHERE robotId= %s", [get_robotId])
    pc = cursor.fetchall()
    if pc:
        for r in pc:
            get_robotId = r[0]
            get_status = r[1]
            get_order = r[2]
        status.configure(text="Status: " + str(get_status), fg='black')
        order.configure(text="Currently Processing Order : " +str(get_order), fg='black')
def ViewFormArm():
    global tree,enterId, battery, status, order, enteride
    tree = ttk.Treeview(viewform, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Arm ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="STATUS")
    tree.pack()
    ViewArm()

    # enter stuff
    enterid = Label(viewform,text="Enter ID", font=('arial 15 bold'), fg='black')
    enterid.place(x=620, y=30)
    enteride = Entry(viewform,width=5, font=('arial 15 bold'), bg='white')
    enteride.place(x=620, y=80)
    enteride.focus()
    # button

    search_btn = Button(viewform,text="Search", bg="#00022e", fg='white', command=ajaxArm)
    search_btn.place(x=620, y=120)

    status = Label(viewform,text="", font=('arial 15 bold'), fg='steelblue')
    status.place(x=200, y=250)

    order = Label(viewform,text="", font=('arial 15 bold'), fg='steelblue')
    order.place(x=200, y=290)

    image1 = PIL.Image.open("/home/dell/Desktop/Operator GUI/gui/resources/robot_arm.png")
    test = ImageTk.PhotoImage(image1)

    label1 =Label(viewform,image=test)
    label1.image = test

    # Position image
    label1.place(x=20, y=30)
def ShowArm():
    global viewform
    viewform = Toplevel()
    viewform.title("Operator Interface/AGV")
    viewform.geometry("800x500+0+0")
    viewform.resizable(0, 0)
    ViewFormArm()
