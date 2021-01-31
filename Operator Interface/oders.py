from tkinter import ttk

import tkinter as tk
import mysql.connector


from tkinter import *
from tkinter import messagebox
def connect():
    con1 = mysql.connector.connect(host='localhost',
                                        database='inventory_system',
                                        user='root',
                                        password='Shamra123')
    con1.close()

def View():
    con1 = mysql.connector.connect(host='localhost',
                                   database='inventory_system',
                                   user='root',
                                   password='Shamra123')
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM orders")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()


def ajax():
    conn = mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='Shamra123')
    get_orderId = enteride.get()
        # get the product info with that id and fill i the labels above
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM orders WHERE order_Id= %s", [get_orderId])
    pc = mycursor.fetchall()
    if pc:
        for r in pc:
            get_orderId = r[0]
            get_client = r[1]
            get_status = r[2]
        clientname.configure(text="Client Name: " + str(get_client), fg='black')
        status.configure(text="Status: " + str(get_status), fg='black')


# connect to the database
connect()
root = tk.Tk()
root.title("Order Status ")



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
View()
#button1 = tk.Button(text="Display data", command=View)
#button1.pack(pady=10)
'''
# enter stuff
enterid = Label(text="Enter Client OrderID", font=('arial 15 bold'), fg='black')
enterid.place(x=20, y=300)
enteride = Entry(width=5, font=('arial 15 bold'), bg='white')
enteride.place(x=250, y=300)
enteride.focus()
# button
search_btn = Button(text="Search",command=ajax)
search_btn.place(x=250, y=350)

clientname = Label(text="", font=('arial 15 bold'),  fg='steelblue')
clientname.place(x=20, y=400)

status = Label(text="", font=('arial 15 bold'),  fg='steelblue')
status.place(x=20, y=440)
'''
root.mainloop()