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

def ViewOrder():
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.close()

def ViewFormOrder():
    global tree
    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="ORDER_ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="CLIENT")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="STATUS")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Assigned AGV")
    tree.pack()
    ViewOrder()


# connect to the database
connect()
root = tk.Tk()
root.title("Order List ")
ViewFormOrder()
root.mainloop()