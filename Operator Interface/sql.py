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
    cur1.execute("SELECT * FROM inventory")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()


def ajax():
    global get_stock, get_name
    conn = mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='Shamra123')
    get_id=enteride.get()
        #get the product info with that id and fill i the labels above
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM inventory WHERE id= %s",[get_id])
    pc = mycursor.fetchall()
    if pc:
        for r in pc:
            get_id=r[0]
            get_name=r[1]
            get_stock=r[2]
        productname.configure(text="Product Name: " +str(get_name),fg='black')
        pprice.configure(text="Quantity Available: "+str(get_stock),fg='black')


# connect to the database
connect()
root = tk.Tk()
root.title("Stock")
root.geometry("1000x600+0+0")

tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="PRODUCT_ID")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="PRODUCT_NAME")

tree.pack()
#View()
button1 = tk.Button(text="Display data", command=View)
button1.pack(pady=10)

# enter stuff
enterid = Label(text="Enter Product's ID", font=('arial 15 bold'), fg='black')
enterid.place(x=20, y=300)
enteride = Entry(width=5, font=('arial 15 bold'), bg='white')
enteride.place(x=220, y=300)
enteride.focus()
# button
search_btn = Button(text="Search",command=ajax)
search_btn.place(x=300, y=300)

productname = Label(text="", font=('arial 15 bold'),  fg='steelblue')
productname.place(x=20, y=400)

pprice = Label(text="", font=('arial 15 bold'),  fg='steelblue')
pprice.place(x=20, y=440)

root.mainloop()