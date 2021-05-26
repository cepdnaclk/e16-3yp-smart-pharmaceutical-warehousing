from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import *
import json
import math
import os


def orderDetails(a):
    global MiddleViewForm
    MiddleViewForm = a
    global productname,username,address

    lbl_text = Button(MiddleViewForm, bd=2, text="New Order", fg="white", font=('arial 30 '), bg="#00022e", width=12,command=order)
    lbl_text.place(x=50, y=50)

    username = Label(MiddleViewForm, text="", font=('arial 15 bold'), fg='black')
    username.place(x=50, y=200)

    address = Label(MiddleViewForm, text="", font=('arial 15 bold'), fg='black')
    address.place(x=50, y=250)


def order():
    file_path = 'newOrder.json'
    # check if size of file is 0
    if os.path.getsize(file_path) == 0:
        username.config(text="No new order available", fg="red")
    else:
        with open(file_path) as file:
            data = json.load(file)

        l = len(data["AGV"])

        p = data["AGV"][0]["User"]
        username.configure(text=" Client Name  :   " + data["AGV"][0]["User"] )
        address.configure(text=" Address        :   " + data["AGV"][0]["Address1"]+"\n\n         "+data["AGV"][0]["Address2"]+
                               "\n\n      "+data["AGV"][0]["Address3"]+"\n\n       "+data["AGV"][0]["Address4"])


        tree = ttk.Treeview(MiddleViewForm, column=("c1", "c2"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Product Name")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Quantity")
        tree.place(y=450)

        a = 1
        while a < l:
            x = data["AGV"][a]["Name"]
            y = data["AGV"][a]["Quantity"]
            tree.insert("", tk.END, values=[x,y])
            a = a + 1


'''
root = tk.Tk()
root.title("Operator GUI")

width = 400
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="grey")
orderDetails(root)
root.mainloop()
'''