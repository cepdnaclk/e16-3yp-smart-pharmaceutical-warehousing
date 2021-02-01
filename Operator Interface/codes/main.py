from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox



root = Tk()
root.title("Operator Interface")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="grey")

# ========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()


def connect():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                        database='inventory_system',
                                        user='root',
                                        password='Shamra123')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()


def Exit():
    result = tkMessageBox.askquestion('Operator Interface', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('Operator Interface', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Operator Interface/Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()


def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Operator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)


def Login(event=None):
    global admin_id
    connect()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = %s AND `password` = %s", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = %s AND `password` = %s", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()

def Logout():
    result = tkMessageBox.askquestion('Operator Interface', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()

def Home():
    global Home
    Home = Tk()
    Home.title("Operator Interface/Home")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Warehouse Management", font=('arial', 38))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu5 = Menu(menubar, tearoff=0)
    filemenu6 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add")#, command=ShowAddNew)
    filemenu2.add_command(label="Update")  # , command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowOrder)
    filemenu3.add_command(label="View", command=ShowAGV)
    filemenu4.add_command(label="View")
    filemenu5.add_command(label="View Floor Map")
    filemenu6.add_command(label="View")
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    menubar.add_cascade(label="Order List", menu=filemenu6)
    menubar.add_cascade(label="AGV", menu=filemenu3)
    menubar.add_cascade(label="RobotArm", menu=filemenu4)
    menubar.add_cascade(label="Location",menu=filemenu5)
    Home.config(menu=menubar)
    Home.config(bg="grey")


def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()

#-------------------AGV
def ViewAGV():
    connect()
    cursor.execute("SELECT * FROM robotAGV")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    cursor.close()
    conn.close()

def ajaxAGV():
    global get_battery, get_status, get_order
    connect()
    get_robotId = enteride.get()
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM robotAGV WHERE robotId= %s", [get_robotId])
    pc = mycursor.fetchall()
    if pc:
        for r in pc:
            get_robotId = r[0]
            get_status = r[1]
            get_battery = r[2]
            get_order = r[3]
        battery.configure(text="Battery: " + str(get_battery)+"%", fg='black')
        status.configure(text="Status: " + str(get_status), fg='black')
        order.configure(text="Order Being Proceeded (OrderID): " +str(get_order), fg='black')

def ViewFormAGV():
    global tree,enterId,battery,status,order,enteride
    tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="AGV ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="STATUS")
    tree.pack()
    button1 = tk.Button(text="Display data", command=ViewAGV)
    button1.pack(pady=10)
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

def ShowAGV():
    global viewform
    viewform = Toplevel()
    viewform.title("Operator Interface/AGV")
    viewform.geometry("1000x600+0+0")
    ViewFormAGV()

#-----------------------Order
def ViewOrder():
    connect()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    cursor.close()

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

def ShowOrder():
    global viewform
    viewform = Toplevel()
    viewform.title("Operator Interface/Order List")
    viewform.geometry("1000x600+0+0")
    ViewFormOrder()
    ViewOrder()


# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Warehouse Management", font=('arial', 45))
lbl_display.pack()

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()