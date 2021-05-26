from tkinter import ttk

import tkinter as tk

import PIL
import mysql.connector

from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox


def connect():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                   database='inventory_system',
                                   user='root',
                                   password='Shamra123')
    cursor = conn.cursor()
def ViewAGV():
    connect()
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
        battery.configure(text="Battery: " + str(get_battery) + "%", fg='black')
        status.configure(text="Status: " + str(get_status), fg='black')
        order.configure(text="Currently Processing Order: " + str(get_order), fg='black')
def ViewFormAGV():
    global tree, enterId, battery, status, order, enteride
    tree = ttk.Treeview(viewform, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="AGV ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="STATUS")
    tree.pack()
    ViewAGV()

    # enter stuff
    enterid = Label(viewform,text="Enter AGV ID", font=('arial 15 bold'), fg='black')
    enterid.place(x=620, y=30)
    enteride = Entry(viewform,width=5, font=('arial 15 bold'), bg='white')
    enteride.place(x=620, y=80)
    enteride.focus()
    # button
    search_btn = Button(viewform,text="Search", bg="#00022e", fg='white', command=ajaxAGV)
    search_btn.place(x=620, y=120)

    battery = Label(viewform,text="", font=('arial 15 bold'), fg='steelblue')
    battery.place(x=200, y=250)

    status = Label(viewform,text="", font=('arial 15 bold'), fg='steelblue')
    status.place(x=200, y=290)

    order = Label(viewform,text="", font=('arial 15 bold'), fg='steelblue')
    order.place(x=200, y=330)

    # location = Label(text="Location of AGV's", font=('arial 15 bold'), fg='black')
    # location.place(x=20, y=500)

    # search_btn = Button(text="Locate")
    # search_btn.place(x=250, y=500)


    image1 = PIL.Image.open("/home/dell/Desktop/Operator GUI/gui/resources/agv.png")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(viewform, image=test)
    label1.image = test

    # Position image
    label1.place(x=20, y=20)
def ShowAGV():
    global viewform
    viewform = Toplevel()
    viewform.title("Operator Interface/AGV")
    viewform.geometry("800x500+0+0")
    viewform.resizable(0, 0)
    ViewFormAGV()

